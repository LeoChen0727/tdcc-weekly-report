"""One model, two fixed source versions, six new research-only artifacts."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime
from decimal import Decimal, InvalidOperation
import fnmatch
import hashlib
import io
import json
from pathlib import Path

import pandas as pd

from model_research_artifact_guard import (
    _dirty_snapshot, changed_during_run, load_ownership_rules,
    load_protected_sentinels, validate_changed_paths,
)
from revenue_unreacted_range_projection_source_io import (
    MONTHLY_RESOLUTION_REL, PRICE_PREFIX, PRICE_RESOLUTION_REL, REVENUE_REL,
    V2_SOURCE_COMMIT, V3_SOURCE_COMMIT, _git, load_source_payloads, read_git_payloads,
)
from revenue_unreacted_range_source_first_condition_audit import build_source_first_condition_audit, load_revenue_history
from revenue_unreacted_range_source_snapshot_projection import (
    PRICE_INPUT_COLUMNS, _canonical_frame_sha256,
)

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
OWNER_ID = "revenue_unreacted_range_source_snapshot_projection_v3_candidate"
VERSION = "source_snapshot_projection_v3_20260923"
CUTOFF = "20260713"
PRODUCER = "scripts/build_revenue_unreacted_range_projection_v3.py"
PREFIX = "output/research/revenue_unreacted_range/revenue_unreacted_range_source_snapshot_projection_v3_20260923_"
OUTPUTS = {name: PREFIX + name + suffix for name, suffix in (
    ("manifest", ".csv"), ("detail", ".csv"), ("price_diff", ".csv"),
    ("episode_diff", ".csv"), ("comparison", ".csv"), ("report", ".md"),
)}
V2_PREFIX = "output/history/research/revenue_unreacted_range_source_snapshot_projection_"
V2_MANIFEST = V2_PREFIX + "manifest_v2_20260822.csv"
V2_DETAIL = V2_PREFIX + "detail_v2_20260822.csv"
PRICE_DIFF_COLUMNS = (
    "stock_id", "old_row_count", "new_row_count", "old_semantic_sha256", "new_semantic_sha256",
    "added_date_count", "removed_date_count", "shared_changed_date_count", "shared_raw_ohlcv_changed_date_count",
    "shared_volume_ratio_changed_date_count", "first_added_date", "last_added_date", "change_class",
)
EPISODE_DIFF_COLUMNS = ("episode_key", "condition_variant_id", "stock_id", "change_class", "changed_columns", "old_row_sha256", "new_row_sha256")
IGNORED_DETAIL_COLUMNS = {"generated_at", "monthly_revenue_history_blob_sha256"}
FLAGS = {"research_only": "true", "formal_model_use_allowed": "false", "promotion_evidence_allowed": "false", "pdf_consumption_allowed": "false", "production_change": "false"}


def sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def csv_frame(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False, low_memory=False)


def csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def cutoff_prices(payloads: dict[str, bytes], stocks: set[str]) -> dict[str, pd.DataFrame]:
    frames = {}
    for path in sorted(payloads):
        if not path.startswith(PRICE_PREFIX):
            continue
        stock = Path(path).stem
        if stock not in stocks:
            continue
        frame = csv_frame(payloads[path]).loc[:, list(PRICE_INPUT_COLUMNS)]
        if not frame["date"].str.fullmatch(r"\d{8}").all():
            raise RuntimeError(f"invalid price date: {stock}")
        frame = frame.loc[frame.date.le(CUTOFF)].sort_values("date", kind="mergesort").reset_index(drop=True)
        if frame.date.duplicated().any():
            raise RuntimeError(f"duplicate cutoff stock/date: {stock}")
        frames[stock] = frame
    return frames


def price_diff(old: dict[str, pd.DataFrame], new: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for stock in sorted(old.keys() | new.keys()):
        blank = pd.DataFrame(columns=list(PRICE_INPUT_COLUMNS))
        before, after = old.get(stock, blank), new.get(stock, blank)
        left, right = before.set_index("date"), after.set_index("date")
        added, removed = right.index.difference(left.index), left.index.difference(right.index)
        common = left.index.intersection(right.index)
        changed = left.loc[common].ne(right.loc[common])
        textual_change = changed.any().any()
        for column in changed:
            for date in changed.index[changed[column]]:
                try:
                    if Decimal(str(left.loc[date, column])) == Decimal(str(right.loc[date, column])):
                        changed.loc[date, column] = False
                except InvalidOperation:
                    pass
        raw_count = int(changed.loc[:, ["open", "high", "low", "close", "volume"]].any(axis=1).sum())
        ratio_count = int(changed.volume_ratio.sum())
        classes = []
        if len(added): classes.append("historical_rows_added")
        if len(removed): classes.append("historical_rows_removed")
        if raw_count: classes.append("shared_raw_ohlcv_changed_requires_review")
        if ratio_count: classes.append("shared_volume_ratio_changed")
        if textual_change and not changed.any().any() and not len(added) and not len(removed):
            classes.append("numeric_format_only")
        rows.append(dict(zip(PRICE_DIFF_COLUMNS, (
            stock, len(before), len(after),
            _canonical_frame_sha256(before, columns=PRICE_INPUT_COLUMNS),
            _canonical_frame_sha256(after, columns=PRICE_INPUT_COLUMNS),
            len(added), len(removed), int(changed.any(axis=1).sum()), raw_count, ratio_count,
            min(added, default=""), max(added, default=""), "|".join(classes) or "unchanged",
        ))))
    return pd.DataFrame(rows, columns=PRICE_DIFF_COLUMNS)


def episode_diff(old: pd.DataFrame, new: pd.DataFrame) -> pd.DataFrame:
    if list(old.columns) != list(new.columns) or old.episode_key.duplicated().any() or new.episode_key.duplicated().any():
        raise RuntimeError("projection detail schema or episode identity drift")
    columns = [column for column in old if column not in IGNORED_DETAIL_COLUMNS]
    left = old.set_index("episode_key", drop=False).astype(str)
    right = new.set_index("episode_key", drop=False).astype(str)
    rows = []
    for key in sorted(set(left.index) | set(right.index)):
        before = left.loc[key] if key in left.index else None
        after = right.loc[key] if key in right.index else None
        changed = [column for column in columns if before is not None and after is not None and before[column] != after[column]]
        if before is not None and after is not None and not changed:
            continue
        identity = after if after is not None else before
        digest = lambda row: sha(json.dumps([columns, row[columns].tolist()], ensure_ascii=False, separators=(",", ":")).encode()) if row is not None else ""
        rows.append((key, identity.condition_variant_id, identity.stock_id,
                     "added_episode" if before is None else "removed_episode" if after is None else "changed_episode",
                     "|".join(changed), digest(before), digest(after)))
    return pd.DataFrame(rows, columns=EPISODE_DIFF_COLUMNS)


def comparison(old: pd.DataFrame, new: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for version, frame in (("v2", old), ("v3_candidate", new)):
        for variant, part in frame.groupby("condition_variant_id", sort=True):
            candidates = part.qualifying_source_revenue_anomaly_candidate_flag.astype(str).str.lower().eq("true") | part.unresolved_price_path_candidate_flag.astype(str).str.lower().eq("true")
            for basis, selected in (("primary_all_rows", part), ("candidate_exclusion_sensitivity_only", part.loc[~candidates])):
                statuses = selected.episode_status
                launch = int(statuses.eq("launch_within_active_horizon").sum())
                no_launch = int(statuses.eq("no_launch_within_active_horizon").sum())
                returns = pd.to_numeric(selected.first_breakout_d20_return_pct, errors="coerce").dropna()
                row = dict(source_version=version, condition_variant_id=variant, metric_basis=basis,
                           episode_count=len(selected), stock_count=selected.stock_id.nunique(), launch_count=launch,
                           no_launch_count=no_launch, right_censored_count=int(statuses.eq("right_censored_before_active_horizon").sum()),
                           retrospective_launch_rate_pct=round(100 * launch / (launch + no_launch), 4) if launch + no_launch else "",
                           unresolved_candidate_count=int(candidates.loc[selected.index].sum()), observed_d20_count=len(returns))
                for name, value in (("positive_rate_pct", (returns > 0).mean() * 100), ("neutral_rate_pct", (returns == 0).mean() * 100),
                                    ("loss_rate_pct", (returns < 0).mean() * 100), ("high_return_ge20_rate_pct", (returns >= 20).mean() * 100),
                                    ("mean_pct", returns.mean()), ("median_pct", returns.median()), ("min_pct", returns.min()), ("max_pct", returns.max())):
                    row["first_breakout_d20_" + name] = round(float(value), 4) if len(returns) else ""
                row.update(metric_interpretation="retrospective_close_observation_not_formal_operation_win_rate", **FLAGS)
                rows.append(row)
    return pd.DataFrame(rows)


def report(manifest: dict[str, object], prices: pd.DataFrame, episodes: pd.DataFrame, metrics: pd.DataFrame) -> bytes:
    changed = prices.loc[prices.change_class.ne("unchanged")]
    primary = metrics.loc[metrics.metric_basis.eq("primary_all_rows")]
    lines = ["# 營收爆發但股價尚未反應模型：行情版本差異稽核", "",
             f"舊 v2 綁定 `{V2_SOURCE_COMMIT}`；新 v3 候選綁定 `{V3_SOURCE_COMMIT}`。",
             "兩版均以 2026/07/13 為觀察截止日，模型條件、事件組裝及計算規則不變。舊 v2 全部保留，v3 不取代 canonical latest。",
             "補入歷史日期不代表證明當時已可取得這個資料版本；本次是固定資料版本的研究重播，不是首次發布版本的嚴格 PIT 證據。", "",
             f"行情有差異 {len(changed)} 檔；新增歷史列 {int(prices.added_date_count.sum())}；移除 {int(prices.removed_date_count.sum())}。",
             f"共同日期 raw OHLCV 變動 {int(prices.shared_raw_ohlcv_changed_date_count.sum())} 列；volume_ratio 變動 {int(prices.shared_volume_ratio_changed_date_count.sum())} 列。",
             f"事件差異 {len(episodes)} 筆：{json.dumps(episodes.change_class.value_counts().to_dict(), ensure_ascii=False)}。",
             "上述是版本差異分類，不是已查明資料錯誤或公司行動原因的判定。", "",
             "## 同條件主要統計", "", "| 版本 | 條件 | 事件數 | 可分類啟動率 % | D20 觀察數 | D20 均值 % | D20 中位 % | 未解候選數 |",
             "|---|---|---:|---:|---:|---:|---:|---:|"]
    for row in primary.itertuples(index=False):
        lines.append(f"| {row.source_version} | {row.condition_variant_id} | {row.episode_count} | {row.retrospective_launch_rate_pct} | {row.observed_d20_count} | {row.first_breakout_d20_mean_pct} | {row.first_breakout_d20_median_pct} | {row.unresolved_candidate_count} |")
    lines.extend(["", "D20 是既有研究的突破收盤後固定期間觀察，不是正式買賣策略的實現報酬或正式勝率。",
                  "數值異常候選保留於 primary；另列的 candidate_exclusion_sensitivity_only 不得稱為修正績效。最小／最大值、虧損及高報酬比例均見 comparison.csv，不能僅憑數值大小判定資料錯誤。",
                  "本次不選出較佳條件、不調參、不升級模型；新資料版本是否採用仍待另行決定與必要的底層來源查核。",
                  "僅月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報均不在範圍。",
                  "正式 adapter、readiness、評分、排序、六份 PDF 與 Apps Script 未改動。", ""])
    return "\n".join(lines).encode("utf-8")


def build(repository_root: Path = ROOT) -> dict[str, bytes]:
    old_sources = load_source_payloads(repository_root, V2_SOURCE_COMMIT)
    new_sources = load_source_payloads(repository_root, V3_SOURCE_COMMIT)
    frozen = read_git_payloads(repository_root, V2_SOURCE_COMMIT, (V2_MANIFEST, V2_DETAIL))
    old_manifest, old_detail = csv_frame(frozen[V2_MANIFEST]), csv_frame(frozen[V2_DETAIL])
    print("building v3 candidate with unchanged source-first calculation", flush=True)
    summary, detail = build_source_first_condition_audit(observation_cutoff_date=CUTOFF, source_payloads=new_sources)
    detail = csv_frame(csv_bytes(detail))
    captured = old_manifest.iloc[0]
    if set(summary.monthly_revenue_canonical_table_sha256.astype(str)) != {str(captured.cutoff_revenue_subset_semantic_sha256)}:
        raise RuntimeError("cutoff monthly source changed; price-only comparison cannot proceed")
    for path in (MONTHLY_RESOLUTION_REL, PRICE_RESOLUTION_REL):
        if old_sources[path] != new_sources[path]:
            raise RuntimeError(f"resolution source changed; separate review required: {path}")
    # Include the entire revenue universe, not only stocks that produced an episode.
    cutoff_revenue = load_revenue_history(observation_cutoff_date=CUTOFF, source_payloads=old_sources)
    stocks = set(cutoff_revenue.stock_id.astype(str))
    old_prices, new_prices = cutoff_prices(old_sources, stocks), cutoff_prices(new_sources, stocks)
    descriptors = "|".join(f"{stock}:{len(frame)}:{_canonical_frame_sha256(frame, columns=PRICE_INPUT_COLUMNS)}" for stock, frame in sorted(old_prices.items()))
    if descriptors != str(captured.cutoff_price_input_file_semantic_sha256s):
        raise RuntimeError("selected v2 Git source does not reproduce frozen cutoff price descriptors")
    prices = price_diff(old_prices, new_prices)
    episodes = episode_diff(old_detail, detail)
    metrics = comparison(old_detail, detail)
    payloads = {OUTPUTS["detail"]: csv_bytes(detail), OUTPUTS["price_diff"]: csv_bytes(prices),
                OUTPUTS["episode_diff"]: csv_bytes(episodes), OUTPUTS["comparison"]: csv_bytes(metrics)}
    manifest = dict(generated_at=datetime.now().astimezone().isoformat(), model_id=MODEL_ID,
                    artifact_version=VERSION, cutoff_date=CUTOFF, v2_source_commit=V2_SOURCE_COMMIT,
                    v3_source_commit=V3_SOURCE_COMMIT, v2_manifest_bytes_sha256=sha(frozen[V2_MANIFEST]),
                    v2_detail_bytes_sha256=sha(frozen[V2_DETAIL]),
                    cutoff_monthly_semantic_sha256=str(captured.cutoff_revenue_subset_semantic_sha256),
                    old_price_stock_count=len(old_prices), new_price_stock_count=len(new_prices),
                    old_price_row_count=sum(map(len, old_prices.values())), new_price_row_count=sum(map(len, new_prices.values())),
                    old_episode_count=len(old_detail), new_episode_count=len(detail),
                    historical_availability_status="current_version_replay_not_first_publication_PIT",
                    candidate_status="not_adopted_pending_review", **FLAGS)
    for label, commit in (("v2", V2_SOURCE_COMMIT), ("v3", V3_SOURCE_COMMIT)):
        manifest[label + "_price_tree_oid"] = _git(repository_root, "rev-parse", f"{commit}:{PRICE_PREFIX.rstrip('/')}").decode().strip()
        sources = old_sources if label == "v2" else new_sources
        for source_name, source_path in (("monthly_revenue", REVENUE_REL), ("monthly_resolution", MONTHLY_RESOLUTION_REL), ("price_resolution", PRICE_RESOLUTION_REL)):
            manifest[label + "_" + source_name + "_bytes_sha256"] = sha(sources[source_path])
    payloads[OUTPUTS["report"]] = report(manifest, prices, episodes, metrics)
    for name, path in OUTPUTS.items():
        if name != "manifest": manifest[name + "_bytes_sha256"] = sha(payloads[path])
    payloads[OUTPUTS["manifest"]] = csv_bytes(pd.DataFrame([manifest]))
    return payloads


def protected_snapshot(root: Path) -> dict[str, object]:
    """Keep the existing sentinel contract in sparse worktrees without hydration."""
    sentinels = load_protected_sentinels(root / "config/model_research_protected_sentinels.csv")
    patterns = [row.artifact_glob for row in sentinels]
    matches = lambda path: any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    maps = []
    for args in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        mapping = {}
        for entry in _git(root, *args).decode().split("\0"):
            if entry:
                meta, path = entry.split("\t", 1)
                if matches(path): mapping[path] = meta
        maps.append(mapping)
    paths = set(maps[0]) | set(maps[1])
    for pattern in patterns:
        paths.update(path.relative_to(root).as_posix() for path in root.glob(pattern) if path.is_file())
    physical = {path: sha((root / path).read_bytes()) for path in paths if (root / path).is_file()}
    for sentinel in sentinels:
        if sentinel.required and not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in paths):
            raise RuntimeError(f"missing protected sentinel: {sentinel.sentinel_id}")
    return dict(tree=maps[0], index=maps[1], physical=physical)


@contextmanager
def model_owned_artifact_guard(root: Path):
    rules = load_ownership_rules(root / "config/model_research_artifact_ownership.csv")
    errors = validate_changed_paths(OWNER_ID, PRODUCER, list(OUTPUTS.values()), rules)
    if errors: raise RuntimeError("unregistered v3 output: " + "; ".join(errors))
    protected = protected_snapshot(root)
    before = _dirty_snapshot(root)
    try:
        yield
    finally:
        changed = changed_during_run(root, before)
        if set(changed) - set(OUTPUTS.values()) or protected_snapshot(root) != protected:
            raise RuntimeError("v3 producer changed files outside its six-artifact allowlist")
        print(f"v3 artifact guard passed; changed_paths={len(changed)}; protected_git_paths={len(protected['tree'])}; protected_physical_files={len(protected['physical'])}", flush=True)


def write_outputs(root: Path, payloads: dict[str, bytes]) -> None:
    if set(payloads) != set(OUTPUTS.values()):
        raise RuntimeError("v3 requires exactly six registered outputs")
    for relative, payload in payloads.items():
        path = root / relative
        if path.exists() and path.read_bytes() != payload:
            raise RuntimeError(f"immutable v3 output already exists: {relative}")
    for relative, payload in payloads.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            with path.open("xb") as handle: handle.write(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    with model_owned_artifact_guard(ROOT):
        write_outputs(ROOT, build(ROOT))
    print("v3 candidate produced; canonical v2 and formal surfaces retained")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
