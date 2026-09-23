"""Independent, read-only validation of the versioned revenue v3 candidate."""
from __future__ import annotations

import argparse
from collections.abc import Mapping
from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
from io import BytesIO
import json
from pathlib import Path

import pandas as pd

from revenue_unreacted_range_projection_source_io import (
    MONTHLY_RESOLUTION_REL, PRICE_PREFIX, PRICE_RESOLUTION_REL, REVENUE_REL,
    V2_SOURCE_COMMIT, V3_SOURCE_COMMIT, _git, load_source_payloads, read_git_payloads,
)
import validate_revenue_unreacted_range_source_snapshot_projection as replay

ROOT = Path(__file__).resolve().parents[1]
VERSION = "source_snapshot_projection_v3_20260923"
CUTOFF = "20260713"
PREFIX = "output/research/revenue_unreacted_range/revenue_unreacted_range_source_snapshot_projection_v3_20260923_"
OUTPUTS = {
    name: PREFIX + name + suffix for name, suffix in (
        ("manifest", ".csv"), ("detail", ".csv"), ("price_diff", ".csv"),
        ("episode_diff", ".csv"), ("comparison", ".csv"), ("report", ".md"),
    )
}
V2_MANIFEST = "output/history/research/revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv"
V2_DETAIL = "output/history/research/revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv"
FLAGS = {
    "research_only": "true", "formal_model_use_allowed": "false",
    "promotion_evidence_allowed": "false", "pdf_consumption_allowed": "false",
    "production_change": "false",
}
PRICE_DIFF_COLUMNS = (
    "stock_id", "old_row_count", "new_row_count", "old_semantic_sha256", "new_semantic_sha256",
    "added_date_count", "removed_date_count", "shared_changed_date_count",
    "shared_raw_ohlcv_changed_date_count", "shared_volume_ratio_changed_date_count",
    "first_added_date", "last_added_date", "change_class",
)
EPISODE_DIFF_COLUMNS = (
    "episode_key", "condition_variant_id", "stock_id", "change_class", "changed_columns",
    "old_row_sha256", "new_row_sha256",
)


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _csv(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(BytesIO(payload), dtype=str, keep_default_na=False, low_memory=False)


def _strings(frame: pd.DataFrame) -> pd.DataFrame:
    return _csv(frame.to_csv(index=False, lineterminator="\n").encode("utf-8"))


def _table_errors(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> list[str]:
    expected = _strings(expected)
    if list(actual.columns) != list(expected.columns):
        return [f"{label} schema drift"]
    if len(actual) != len(expected):
        return [f"{label} row count mismatch: {len(actual)}/{len(expected)}"]
    if not actual.reset_index(drop=True).equals(expected.reset_index(drop=True)):
        different = actual.reset_index(drop=True).ne(expected.reset_index(drop=True))
        row, column = next((i, column) for i in range(len(actual)) for column in actual if different.at[i, column])
        return [f"{label} independently recomputed value mismatch: row={row} column={column}"]
    return []


def _same_price(left: str, right: str) -> bool:
    if left == right:
        return True
    try:
        return Decimal(left) == Decimal(right)
    except InvalidOperation:
        return False


def _expected_price_diff(old: dict[str, pd.DataFrame], new: dict[str, pd.DataFrame]) -> pd.DataFrame:
    output = []
    for stock in sorted(set(old) | set(new)):
        blank = pd.DataFrame(columns=list(replay.PRICE_INPUT_COLUMNS))
        before, after = old.get(stock, blank), new.get(stock, blank)
        left = before.set_index("date").to_dict("index")
        right = after.set_index("date").to_dict("index")
        added, removed = sorted(set(right) - set(left)), sorted(set(left) - set(right))
        raw_changes, ratio_changes, all_changes = set(), set(), set()
        textual_change = False
        for date in set(left) & set(right):
            for column in replay.PRICE_INPUT_COLUMNS[1:]:
                a, b = str(left[date][column]), str(right[date][column])
                textual_change |= a != b
                if not _same_price(a, b):
                    all_changes.add(date)
                    (ratio_changes if column == "volume_ratio" else raw_changes).add(date)
        classes = []
        if added:
            classes.append("historical_rows_added")
        if removed:
            classes.append("historical_rows_removed")
        if raw_changes:
            classes.append("shared_raw_ohlcv_changed_requires_review")
        if ratio_changes:
            classes.append("shared_volume_ratio_changed")
        if textual_change and not (all_changes or added or removed):
            classes.append("numeric_format_only")
        output.append((
            stock, len(before), len(after),
            replay._canonical_frame_sha256(before, columns=list(replay.PRICE_INPUT_COLUMNS)),
            replay._canonical_frame_sha256(after, columns=list(replay.PRICE_INPUT_COLUMNS)),
            len(added), len(removed), len(all_changes), len(raw_changes), len(ratio_changes),
            added[0] if added else "", added[-1] if added else "", "|".join(classes) or "unchanged",
        ))
    return pd.DataFrame(output, columns=PRICE_DIFF_COLUMNS)


def _expected_episode_diff(old: pd.DataFrame, new: pd.DataFrame) -> pd.DataFrame:
    if list(old.columns) != list(new.columns):
        raise RuntimeError("v2/v3 episode schema drift")
    if old.episode_key.duplicated().any() or new.episode_key.duplicated().any():
        raise RuntimeError("v2/v3 episode keys are duplicated")
    columns = [column for column in old if column not in {"generated_at", "monthly_revenue_history_blob_sha256"}]
    indexed = [frame.set_index("episode_key", drop=False).to_dict("index") for frame in (old, new)]
    rows = []
    def digest(row):
        if row is None:
            return ""
        return _sha(json.dumps([columns, [str(row[column]) for column in columns]], ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    for key in sorted(set(indexed[0]) | set(indexed[1])):
        left, right = indexed[0].get(key), indexed[1].get(key)
        changed = [column for column in columns if left is not None and right is not None and str(left[column]) != str(right[column])]
        if left is not None and right is not None and not changed:
            continue
        row = right if right is not None else left
        kind = "added_episode" if left is None else "removed_episode" if right is None else "changed_episode"
        rows.append((key, row["condition_variant_id"], row["stock_id"], kind, "|".join(changed), digest(left), digest(right)))
    return pd.DataFrame(rows, columns=EPISODE_DIFF_COLUMNS)


def _expected_comparison(old: pd.DataFrame, new: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for version, frame in (("v2", old), ("v3_candidate", new)):
        for variant in sorted(frame.condition_variant_id.unique()):
            part = frame.loc[frame.condition_variant_id.eq(variant)]
            flagged = part.qualifying_source_revenue_anomaly_candidate_flag.str.lower().eq("true") | part.unresolved_price_path_candidate_flag.str.lower().eq("true")
            for basis in ("primary_all_rows", "candidate_exclusion_sensitivity_only"):
                selected = part if basis == "primary_all_rows" else part.loc[~flagged]
                counts = selected.episode_status.value_counts()
                launch = int(counts.get("launch_within_active_horizon", 0))
                no_launch = int(counts.get("no_launch_within_active_horizon", 0))
                values = pd.to_numeric(selected.first_breakout_d20_return_pct, errors="coerce").dropna()
                row = {
                    "source_version": version, "condition_variant_id": variant, "metric_basis": basis,
                    "episode_count": len(selected), "stock_count": selected.stock_id.nunique(),
                    "launch_count": launch, "no_launch_count": no_launch,
                    "right_censored_count": int(counts.get("right_censored_before_active_horizon", 0)),
                    "retrospective_launch_rate_pct": round(100 * launch / (launch + no_launch), 4) if launch + no_launch else "",
                    "unresolved_candidate_count": int(flagged.reindex(selected.index).sum()),
                    "observed_d20_count": len(values),
                }
                metrics = {
                    "positive_rate_pct": (values > 0).mean() * 100,
                    "neutral_rate_pct": (values == 0).mean() * 100,
                    "loss_rate_pct": (values < 0).mean() * 100,
                    "high_return_ge20_rate_pct": (values >= 20).mean() * 100,
                    "mean_pct": values.mean(), "median_pct": values.median(),
                    "min_pct": values.min(), "max_pct": values.max(),
                }
                row.update({"first_breakout_d20_" + name: round(float(value), 4) if len(values) else "" for name, value in metrics.items()})
                row.update(metric_interpretation="retrospective_close_observation_not_formal_operation_win_rate", **FLAGS)
                rows.append(row)
    return pd.DataFrame(rows)


def _source_evidence(root: Path):
    old_sources = load_source_payloads(root, V2_SOURCE_COMMIT)
    new_sources = load_source_payloads(root, V3_SOURCE_COMMIT)
    frozen = read_git_payloads(root, V2_SOURCE_COMMIT, (V2_MANIFEST, V2_DETAIL))
    old_manifest, old_detail = _csv(frozen[V2_MANIFEST]), _csv(frozen[V2_DETAIL])
    binding_errors = replay.validate_projection_binding_frames(old_manifest, old_detail)
    if binding_errors:
        raise RuntimeError("frozen v2 binding: " + "; ".join(binding_errors))
    captured = old_manifest.iloc[0]
    cutoff_frames = []
    prices = []
    for label, sources in (("v2", old_sources), ("v3", new_sources)):
        monthly_registry = _csv(sources[MONTHLY_RESOLUTION_REL])
        cutoff = replay._resolve_monthly(_csv(sources[REVENUE_REL]), monthly_registry, CUTOFF)
        if replay._canonical_monthly_table_sha256(cutoff) != str(captured.cutoff_revenue_subset_semantic_sha256):
            raise RuntimeError(f"{label} cutoff monthly semantics changed")
        paths = replay._price_paths_by_stock(Path(PRICE_PREFIX), source_payloads=sources)
        stock_ids = replay._cutoff_price_input_stock_ids(cutoff, Path(PRICE_PREFIX), source_payloads=sources)
        prices.append({stock: replay._price_file(paths[stock], stock, CUTOFF, source_payloads=sources) for stock in stock_ids})
        cutoff_frames.append(cutoff)
    for path in (MONTHLY_RESOLUTION_REL, PRICE_RESOLUTION_REL):
        if old_sources[path] != new_sources[path]:
            raise RuntimeError(f"v2/v3 resolution bytes differ: {path}")
    old_lineage = replay._price_input_lineage(cutoff_frames[0], Path(PRICE_PREFIX), CUTOFF, source_payloads=old_sources)
    for suffix, key in (("stock_count", "stock_count"), ("row_count", "row_count"), ("file_semantic_sha256s", "file_semantic_sha256s"), ("semantic_sha256", "semantic_sha256")):
        if str(captured["cutoff_price_input_" + suffix]) != str(old_lineage[key]):
            raise RuntimeError(f"frozen v2 price descriptor mismatch: {suffix}")
    monthly_ids, monthly_sha = replay._applied_monthly_lineage(
        cutoff_frames[0], _csv(old_sources[MONTHLY_RESOLUTION_REL])
    )
    price_ids, price_sha = replay._applied_price_lineage(
        sorted(prices[0]), _csv(old_sources[PRICE_RESOLUTION_REL]), CUTOFF
    )
    for name, ids, digest in (("monthly", monthly_ids, monthly_sha), ("price", price_ids, price_sha)):
        expected = {"count": str(len(ids)), "ids": "|".join(ids) or "none", "semantic_sha256": digest}
        for suffix, value in expected.items():
            if str(captured[f"applied_{name}_resolution_{suffix}"]) != value:
                raise RuntimeError(f"frozen v2 {name} resolution lineage mismatch: {suffix}")
    new_replay = replay._rebuild_cutoff_source_detail(
        cutoff_frames[1], price_dir=Path(PRICE_PREFIX), price_registry=_csv(new_sources[PRICE_RESOLUTION_REL]),
        monthly_blob_sha=_sha(new_sources[REVENUE_REL]),
        cutoff_monthly_sha=replay._canonical_monthly_table_sha256(cutoff_frames[1]),
        monthly_registry_sha=replay._monthly_registry_sha256(_csv(new_sources[MONTHLY_RESOLUTION_REL])),
        source_payloads=new_sources,
    )
    fields = {
        "model_id": "revenue_unreacted_range", "artifact_version": VERSION, "cutoff_date": CUTOFF,
        "v2_source_commit": V2_SOURCE_COMMIT, "v3_source_commit": V3_SOURCE_COMMIT,
        "v2_manifest_bytes_sha256": _sha(frozen[V2_MANIFEST]), "v2_detail_bytes_sha256": _sha(frozen[V2_DETAIL]),
        "cutoff_monthly_semantic_sha256": str(captured.cutoff_revenue_subset_semantic_sha256),
        "old_price_stock_count": len(prices[0]), "new_price_stock_count": len(prices[1]),
        "old_price_row_count": sum(len(frame) for frame in prices[0].values()),
        "new_price_row_count": sum(len(frame) for frame in prices[1].values()),
        "old_episode_count": len(old_detail), "new_episode_count": len(new_replay),
        "historical_availability_status": "current_version_replay_not_first_publication_PIT",
        "candidate_status": "not_adopted_pending_review", **FLAGS,
    }
    for label, commit, sources in (("v2", V2_SOURCE_COMMIT, old_sources), ("v3", V3_SOURCE_COMMIT, new_sources)):
        fields[label + "_price_tree_oid"] = _git(root, "rev-parse", f"{commit}:{PRICE_PREFIX.rstrip('/')}").decode("ascii").strip()
        for source_name, path in (("monthly_revenue", REVENUE_REL), ("monthly_resolution", MONTHLY_RESOLUTION_REL), ("price_resolution", PRICE_RESOLUTION_REL)):
            fields[label + "_" + source_name + "_bytes_sha256"] = _sha(sources[path])
    return fields, old_detail, new_replay, prices[0], prices[1]


def _report_errors(payload: bytes, prices: pd.DataFrame, episodes: pd.DataFrame, comparison: pd.DataFrame) -> list[str]:
    text = payload.decode("utf-8-sig")
    required = (
        "# 營收爆發但股價尚未反應模型：行情版本差異稽核",
        f"舊 v2 綁定 `{V2_SOURCE_COMMIT}`；新 v3 候選綁定 `{V3_SOURCE_COMMIT}`。",
        "兩版均以 2026/07/13 為觀察截止日，模型條件、事件組裝及計算規則不變。舊 v2 全部保留，v3 不取代 canonical latest。",
        "補入歷史日期不代表證明當時已可取得這個資料版本；本次是固定資料版本的研究重播，不是首次發布版本的嚴格 PIT 證據。",
        f"行情有差異 {int(prices.change_class.ne('unchanged').sum())} 檔；新增歷史列 {int(prices.added_date_count.sum())}；移除 {int(prices.removed_date_count.sum())}。",
        f"共同日期 raw OHLCV 變動 {int(prices.shared_raw_ohlcv_changed_date_count.sum())} 列；volume_ratio 變動 {int(prices.shared_volume_ratio_changed_date_count.sum())} 列。",
        f"事件差異 {len(episodes)} 筆：{json.dumps(episodes.change_class.value_counts().to_dict(), ensure_ascii=False)}。",
        "上述是版本差異分類，不是已查明資料錯誤或公司行動原因的判定。",
        "D20 是既有研究的突破收盤後固定期間觀察，不是正式買賣策略的實現報酬或正式勝率。",
        "數值異常候選保留於 primary；另列的 candidate_exclusion_sensitivity_only 不得稱為修正績效。最小／最大值、虧損及高報酬比例均見 comparison.csv，不能僅憑數值大小判定資料錯誤。",
        "本次不選出較佳條件、不調參、不升級模型；新資料版本是否採用仍待另行決定與必要的底層來源查核。",
        "僅月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報均不在範圍。",
        "正式 adapter、readiness、評分、排序、六份 PDF 與 Apps Script 未改動。",
    )
    errors = [f"report required evidence or boundary missing: {line[:50]}" for line in required if line not in text.splitlines()]
    table_rows = []
    for row in comparison.loc[comparison.metric_basis.eq("primary_all_rows")].itertuples(index=False):
        table_rows.append(f"| {row.source_version} | {row.condition_variant_id} | {row.episode_count} | {row.retrospective_launch_rate_pct} | {row.observed_d20_count} | {row.first_breakout_d20_mean_pct} | {row.first_breakout_d20_median_pct} | {row.unresolved_candidate_count} |")
    observed_rows = [line for line in text.splitlines() if line.startswith("| v2 |") or line.startswith("| v3_candidate |")]
    if observed_rows != table_rows:
        errors.append("report primary metric table mismatch")
    expected_nonempty = [
        *required[:8], "## 同條件主要統計",
        "| 版本 | 條件 | 事件數 | 可分類啟動率 % | D20 觀察數 | D20 均值 % | D20 中位 % | 未解候選數 |",
        "|---|---|---:|---:|---:|---:|---:|---:|", *table_rows, *required[8:],
    ]
    if [line for line in text.splitlines() if line] != expected_nonempty:
        errors.append("report contains unverified wording or evidence layout drift")
    return errors


def validate(repository_root: Path = ROOT, *, artifacts: Mapping[str, bytes] | None = None) -> list[str]:
    try:
        if artifacts is None:
            artifacts = {}
            for relative in OUTPUTS.values():
                path = Path(repository_root) / relative
                if path.is_symlink() or not path.is_file():
                    raise RuntimeError(f"v3 research artifact is missing or unsafe: {relative}")
                artifacts[relative] = path.read_bytes()
        if set(artifacts) != set(OUTPUTS.values()):
            return ["v3 requires exactly six declared artifacts"]
        # Artifact hashes bind the producer's UTF-8/LF serialization. Windows
        # checkout may add CRLF or a transport BOM without changing CSV values.
        # Git source blobs above remain byte-exact and are never normalized.
        artifacts = {
            relative: payload.decode("utf-8-sig").replace("\r\n", "\n").encode("utf-8")
            for relative, payload in artifacts.items()
        }
        manifest = _csv(artifacts[OUTPUTS["manifest"]])
        if len(manifest) != 1:
            return ["v3 manifest must contain exactly one row"]
        row = manifest.iloc[0]
        errors = []
        for name, relative in OUTPUTS.items():
            if name != "manifest" and row.get(name + "_bytes_sha256") != _sha(artifacts[relative]):
                errors.append(f"v3 {name} artifact bytes SHA-256 mismatch")
        if errors:
            return errors
        if not str(row.get("generated_at", "")).strip():
            return ["v3 manifest generated_at is missing"]
        datetime.fromisoformat(str(row["generated_at"]))
        fields, old_detail, rebuilt, old_prices, new_prices = _source_evidence(Path(repository_root))
        columns = set(fields) | {"generated_at"} | {name + "_bytes_sha256" for name in OUTPUTS if name != "manifest"}
        if set(manifest.columns) != columns:
            errors.append("v3 manifest schema drift")
        for name, expected in fields.items():
            if row.get(name) != str(expected):
                errors.append(f"v3 manifest source contract mismatch: {name}")
        detail = _csv(artifacts[OUTPUTS["detail"]])
        errors.extend(replay._replay_detail_errors(detail, rebuilt))
        if errors:
            return errors
        prices = _expected_price_diff(old_prices, new_prices)
        episodes = _expected_episode_diff(old_detail, detail)
        comparison = _expected_comparison(old_detail, detail)
        for name, expected in (("price_diff", prices), ("episode_diff", episodes), ("comparison", comparison)):
            errors.extend(_table_errors(_csv(artifacts[OUTPUTS[name]]), expected, name))
        errors.extend(_report_errors(artifacts[OUTPUTS["report"]], prices, episodes, comparison))
        return errors
    except (OSError, RuntimeError, ValueError, KeyError, TypeError, IndexError, UnicodeDecodeError) as exc:
        return [f"v3 independent validation failed: {exc}"]


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    errors = validate()
    if errors:
        for error in errors:
            print("ERROR: " + error)
        return 1
    print("revenue projection v3 independent validation passed; candidate_status=not_adopted_pending_review; formal_model_use_allowed=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
