"""Frozen revenue v3 observations; only share-unit outcome reconciliation."""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
from decimal import Decimal
import fnmatch
import hashlib
import io
import json
from pathlib import Path
import re

import pandas as pd

from model_research_artifact_guard import (
    _dirty_snapshot, changed_during_run, load_ownership_rules,
    load_protected_sentinels, validate_changed_paths,
)
from revenue_unreacted_range_projection_source_io import read_git_payloads, _git

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
OWNER_ID = "revenue_unreacted_range_outcome_unit_reconciliation"
PRODUCER = "scripts/build_revenue_unreacted_range_outcome_unit_reconciliation.py"
VALIDATOR = "scripts/validate_revenue_unreacted_range_outcome_unit_reconciliation.py"
VERSION = "outcome_unit_reconciliation_v1_20260923"
EVIDENCE_COMMIT = "001b82f856c4ca1a863d64998890fb1fdfba8030"
PRICE_COMMIT = "231d2e279a99a89f1888ece0361ea64d45f69ecd"
CUTOFF = "20260713"
CONFIG = "config/revenue_unreacted_range_outcome_unit_actions_v1.json"
PRICE_RESOLUTION = "config/revenue_unreacted_range_price_comparability_resolution.csv"
OLD_PREFIX = "output/research/revenue_unreacted_range/revenue_unreacted_range_source_snapshot_projection_v3_20260923_"
OLD_PATHS = tuple(OLD_PREFIX + name + suffix for name, suffix in (
    ("manifest", ".csv"), ("detail", ".csv"), ("price_diff", ".csv"),
    ("episode_diff", ".csv"), ("comparison", ".csv"), ("report", ".md"),
))
PREFIX = "output/research/revenue_unreacted_range/revenue_unreacted_range_outcome_unit_reconciliation_v1_20260923_"
OUTPUTS = {name: PREFIX + name + suffix for name, suffix in (
    ("manifest", ".json"), ("detail", ".csv"), ("actions", ".csv"),
    ("comparison", ".csv"), ("changes", ".csv"), ("report", ".md"),
)}
FLAGS = {"research_only": "true", "formal_model_use_allowed": "false",
         "promotion_evidence_allowed": "false", "pdf_consumption_allowed": "false",
         "production_change": "false"}
ADDED_COLUMNS = (
    "unit_d20_date", "unit_raw_d0_close", "unit_raw_d20_close", "unit_existing_action_ids",
    "unit_added_action_ids", "unit_added_share_factor", "unit_reconciled_d20_return_pct",
    "unit_delta_percentage_points", "unit_reconciliation_status", "unit_anomaly_disposition",
)


def sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def transport(payload: bytes) -> bytes:
    return payload.removeprefix(b"\xef\xbb\xbf").replace(b"\r\n", b"\n")


def csv_frame(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False, low_memory=False)


def csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def number(value: float) -> str:
    return format(float(value), ".10f")


def validate_actions(config: dict, root: Path) -> list[dict]:
    if config.get("model_id") != MODEL_ID or config.get("version") != VERSION:
        raise RuntimeError("action model/version mismatch")
    events = config.get("events", [])
    if not events:
        raise RuntimeError("no verified share-unit actions")
    expected_event = ("4763_20250630_par_value_change_1_to_10", "4763", "20250630", "10")
    if len(events) != 1 or tuple(str(events[0].get(key, "")) for key in
                               ("event_id", "stock_id", "effective_date", "new_shares_per_old_share")) != expected_event:
        raise RuntimeError("unapproved share-unit event or ratio")
    keys = set()
    for event in events:
        key = (event["stock_id"], event["effective_date"])
        if key in keys or event["event_id"] in keys:
            raise RuntimeError("duplicate share-unit action")
        keys.update((key, event["event_id"]))
        ratio = Decimal(str(event["new_shares_per_old_share"]))
        if not ratio.is_finite() or ratio <= 0 or not re.fullmatch(r"\d{8}", event["effective_date"]):
            raise RuntimeError("invalid share-unit ratio/date")
        if event["effective_date"] > CUTOFF or event.get("verification_status") != "official_share_unit_event_verified":
            raise RuntimeError("unverified or post-cutoff action")
        if event.get("cash_component_status") != "not_modelled_not_total_return":
            raise RuntimeError("cash-flow scope mismatch")
        if not event.get("documents"):
            raise RuntimeError("official receipt missing")
        for document_id in event["documents"]:
            doc = config["documents"][document_id]
            raw = base64.b64decode(doc["payload_base64"], validate=True)
            if sha(raw) != doc["sha256"] or len(raw) != doc["bytes"]:
                raise RuntimeError("official receipt SHA mismatch")
            if doc.get("first_publication_verified") is not False or doc.get("original_revision_chain_verified") is not False:
                raise RuntimeError("unsupported official receipt PIT claim")
            text = raw.decode("utf-8")
            tokens = doc.get("required_tokens", [])
            if len(tokens) < 3 or not all(token and token in text for token in tokens):
                raise RuntimeError("official receipt assertion mismatch")
        if {config["documents"][key]["sha256"] for key in event["documents"]} != {
            "95fedb4a005b238a3c7959ce34bc16fce375c4c82bcb23334697efbf36ff06e9",
            "33116fef9d83a263a03908697c399d1edcc9b1cb030efb7a09e647180c2d96f9",
        }:
            raise RuntimeError("unapproved official receipt identity")
    return sorted(events, key=lambda item: (item["stock_id"], item["effective_date"], item["event_id"]))


def prepare_prices(payload: bytes, stock: str, resolutions: pd.DataFrame) -> pd.DataFrame:
    frame = csv_frame(payload)
    if not {"date", "close"}.issubset(frame):
        raise RuntimeError("price schema missing")
    if not frame.date.str.fullmatch(r"\d{8}").all() or frame.date.duplicated().any():
        raise RuntimeError("invalid/duplicate price dates")
    frame = frame.loc[frame.date.le(CUTOFF)].sort_values("date", kind="mergesort").copy()
    frame["raw_close"] = pd.to_numeric(frame.close, errors="coerce")
    frame = frame.dropna(subset=["raw_close"]).reset_index(drop=True)
    if (frame.raw_close <= 0).any():
        raise RuntimeError("nonpositive price")
    frame["analysis_close"] = frame.raw_close
    for event in resolutions.loc[resolutions.stock_id.eq(stock)].to_dict("records"):
        if event["root_cause_status"] != "verified_non_comparable_raw_price_scale" or event["resume_date"] > CUTOFF:
            continue
        ratio = float(event["exchange_ratio"])
        if not 0 < ratio < float("inf"):
            raise RuntimeError("invalid existing resolution ratio")
        frame.loc[frame.date.lt(event["resume_date"]), "analysis_close"] /= ratio
    return frame


def reconcile(detail: pd.DataFrame, prices: dict[str, pd.DataFrame], resolutions: pd.DataFrame, events: list[dict]) -> pd.DataFrame:
    if detail.episode_key.duplicated().any() or set(ADDED_COLUMNS) & set(detail.columns):
        raise RuntimeError("episode identity/schema drift")
    added = []
    for row in detail.to_dict("records"):
        record = dict.fromkeys(ADDED_COLUMNS, "")
        record.update(unit_reconciliation_status="no_mature_d20_observation",
                      unit_anomaly_disposition="unresolved_anomaly_candidate" if any(
                          str(row[key]).lower() == "true" for key in (
                              "qualifying_source_revenue_anomaly_candidate_flag", "unresolved_price_path_candidate_flag")) else "not_assessed_not_a_clearance")
        if not row["first_breakout_d20_return_pct"]:
            added.append(record)
            continue
        stock, date = row["stock_id"], row["first_breakout_date"]
        frame = prices[stock]
        indices = frame.index[frame.date.eq(date)].tolist()
        if len(indices) != 1 or indices[0] + 20 >= len(frame):
            raise RuntimeError("frozen D20 sequence is missing")
        start, end = frame.iloc[indices[0]], frame.iloc[indices[0] + 20]
        old = float(row["first_breakout_d20_return_pct"])
        replayed = (float(end.analysis_close) / float(start.analysis_close) - 1) * 100
        if abs(old - replayed) > 0.000051:
            raise RuntimeError(f"frozen original outcome mismatch: {row['episode_key']}")
        existing = resolutions.loc[resolutions.stock_id.eq(stock) & resolutions.resume_date.gt(date)
                                   & resolutions.resume_date.le(end.date)
                                   & resolutions.root_cause_status.eq("verified_non_comparable_raw_price_scale")]
        factor, applied = 1.0, []
        for event in events:
            if event["stock_id"] != stock or not date < event["effective_date"] <= end.date:
                continue
            if not existing.loc[existing.resume_date.eq(event["effective_date"])].empty:
                raise RuntimeError("new action overlaps an already normalized resolution")
            factor *= float(event["new_shares_per_old_share"])
            applied.append(event["event_id"])
        # Preserve original precision for unchanged rows; do not inject rounding-only differences.
        value = (float(end.analysis_close) * factor / float(start.analysis_close) - 1) * 100 if applied else old
        record.update(unit_d20_date=end.date, unit_raw_d0_close=str(start.close), unit_raw_d20_close=str(end.close),
                      unit_existing_action_ids="|".join(existing.resolution_id), unit_added_action_ids="|".join(applied),
                      unit_added_share_factor=number(factor), unit_reconciled_d20_return_pct=number(value),
                      unit_delta_percentage_points=number(value - old),
                      unit_reconciliation_status="share_unit_only_reconciled" if applied else "unchanged_frozen_observation")
        added.append(record)
    result = pd.concat([detail.reset_index(drop=True), pd.DataFrame(added, columns=ADDED_COLUMNS)], axis=1)
    if not result.loc[:, detail.columns].equals(detail.reset_index(drop=True)):
        raise RuntimeError("frozen source columns changed")
    return result


def comparison(detail: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for variant, group in detail.groupby("condition_variant_id", sort=True):
        candidates = group.qualifying_source_revenue_anomaly_candidate_flag.str.lower().eq("true") | group.unresolved_price_path_candidate_flag.str.lower().eq("true")
        for basis, selected in (("primary_all_rows", group), ("candidate_exclusion_sensitivity_only", group.loc[~candidates])):
            for version, column in (("frozen_v3", "first_breakout_d20_return_pct"), (VERSION, "unit_reconciled_d20_return_pct")):
                values = pd.to_numeric(selected[column], errors="coerce").dropna()
                row = dict(condition_variant_id=variant, metric_basis=basis, outcome_version=version,
                           episode_count=str(len(selected)), stock_count=str(selected.stock_id.nunique()),
                           observed_d20_count=str(len(values)), unresolved_candidate_count=str(int(candidates.loc[selected.index].sum())))
                for key, value in (("positive_rate_pct", (values > 0).mean() * 100), ("neutral_rate_pct", (values == 0).mean() * 100),
                                   ("loss_rate_pct", (values < 0).mean() * 100), ("high_return_ge20_rate_pct", (values >= 20).mean() * 100),
                                   ("mean_pct", values.mean()), ("median_pct", values.median()), ("min_pct", values.min()), ("max_pct", values.max())):
                    row[key] = number(value) if len(values) else ""
                row.update(metric_interpretation="frozen_breakout_close_D20_share_unit_observation_not_total_return_or_formal_win_rate", **FLAGS)
                rows.append(row)
    return pd.DataFrame(rows)


def load_inputs(root: Path) -> tuple[dict, dict, pd.DataFrame, dict[str, pd.DataFrame], pd.DataFrame, list[dict]]:
    frozen = read_git_payloads(root, EVIDENCE_COMMIT, OLD_PATHS)
    if set(frozen) != set(OLD_PATHS):
        raise RuntimeError("six frozen v3 artifacts required")
    detail = csv_frame(frozen[OLD_PREFIX + "detail.csv"])
    if len(detail) != 20430 or sha(frozen[OLD_PREFIX + "detail.csv"]) != "fad447e45ba84f9767cd3a317a3ce0ea9e930f434370788e407294ef57792972":
        raise RuntimeError("frozen v3 detail identity mismatch")
    config = json.loads((root / CONFIG).read_text(encoding="utf-8-sig"))
    events = validate_actions(config, root)
    stocks = sorted(set(detail.loc[detail.first_breakout_d20_return_pct.ne(""), "stock_id"]))
    paths = (PRICE_RESOLUTION, *(f"data/stock_price_history/{stock}.csv" for stock in stocks))
    # Keep each Windows process command below the CreateProcess argument limit.
    raw = {}
    for offset in range(0, len(paths), 128):
        raw.update(read_git_payloads(root, PRICE_COMMIT, paths[offset:offset + 128]))
    if set(raw) != set(paths):
        raise RuntimeError("fixed price blobs missing")
    resolutions = csv_frame(raw[PRICE_RESOLUTION])
    frames = {stock: prepare_prices(raw[f"data/stock_price_history/{stock}.csv"], stock, resolutions) for stock in stocks}
    lineage = {"evidence_commit": EVIDENCE_COMMIT, "price_commit": PRICE_COMMIT,
               "source_artifact_sha256": {path: sha(value) for path, value in sorted(frozen.items())},
               "raw_source_sha256": {path: sha(value) for path, value in sorted(raw.items())},
               "config_canonical_sha256": sha(canonical_json(config))}
    return lineage, config, detail, frames, resolutions, events


def build(root: Path = ROOT) -> dict[str, bytes]:
    lineage, _, frozen, prices, resolutions, events = load_inputs(root)
    detail = reconcile(frozen, prices, resolutions, events)
    metrics = comparison(detail)
    changes = detail.loc[detail.unit_added_action_ids.ne(""), ["episode_key", "condition_variant_id", "stock_id", "first_breakout_date", "first_breakout_d20_return_pct", *ADDED_COLUMNS]]
    actions = pd.DataFrame([{**event, "documents": "|".join(event["documents"])} for event in events])
    report = ("# 營收爆發但股價尚未反應：凍結事件公司行動單位校準\n\n"
              f"保留全部 {len(detail)} 筆 v3 事件與所有舊欄位、突破日期、D20 個股有效 close 序列。新單位校準影響 {len(changes)} 個情境事件，不等於獨立交易數。\n\n"
              "只校準已確認換股的固定 D20 價格觀察；不重算條件、特徵、launch、啟動率或買賣日期。舊 launch labels 不得解讀為單位校準後的新啟動結果。\n\n"
              "這不是完整總報酬、正式操作損益、首次發布 PIT 或 promotion 證據；股利、其他公司行動完整覆蓋、交易日曆完整性與可成交性仍未證實。\n\n"
              "原有未解異常旗標與 primary 全列保留，candidate_exclusion_sensitivity_only 僅為敏感度，不能叫修正績效。未標記不代表已查明無異常。\n\n"
              "只使用月營收既有事件，不納入 EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報。正式模型、adapter、readiness、六份 PDF、Apps Script 及舊證據均未改動。\n")
    payloads = {OUTPUTS["detail"]: csv_bytes(detail), OUTPUTS["actions"]: csv_bytes(actions),
                OUTPUTS["comparison"]: csv_bytes(metrics), OUTPUTS["changes"]: csv_bytes(changes), OUTPUTS["report"]: report.encode("utf-8")}
    manifest = dict(version=VERSION, model_id=MODEL_ID, owner_id=OWNER_ID, cutoff=CUTOFF,
                    source_row_count=len(frozen), changed_row_count=len(changes), **lineage,
                    code_canonical_sha256={path: sha(transport((root / path).read_bytes())) for path in (PRODUCER, VALIDATOR)},
                    output_sha256={path: sha(value) for path, value in payloads.items()},
                    launch_labels_recomputed=False, cash_flow_total_return_complete=False,
                    first_publication_PIT_proven=False, **FLAGS)
    payloads[OUTPUTS["manifest"]] = canonical_json(manifest) + b"\n"
    return payloads


def protected_snapshot(root: Path) -> dict:
    sentinels = load_protected_sentinels(root / "config/model_research_protected_sentinels.csv")
    patterns = [row.artifact_glob for row in sentinels]
    patterns.extend(OLD_PATHS)
    matches = lambda path: any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    maps = []
    for args in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        mapping = {}
        for entry in _git(root, *args).decode().split("\0"):
            if entry:
                meta, path = entry.split("\t", 1)
                if matches(path):
                    mapping[path] = meta
        maps.append(mapping)
    paths = set(maps[0]) | set(maps[1])
    for pattern in patterns:
        paths.update(path.relative_to(root).as_posix() for path in root.glob(pattern) if path.is_file())
    for sentinel in sentinels:
        if sentinel.required and not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in paths):
            raise RuntimeError("missing protected sentinel: " + sentinel.sentinel_id)
    return {"tree": maps[0], "index": maps[1], "physical": {p: sha((root / p).read_bytes()) for p in paths if (root / p).is_file()}}


@contextmanager
def model_owned_artifact_guard(root: Path):
    errors = validate_changed_paths(OWNER_ID, PRODUCER, list(OUTPUTS.values()), load_ownership_rules(root / "config/model_research_artifact_ownership.csv"))
    if errors:
        raise RuntimeError("unregistered outcome-unit output: " + "; ".join(errors))
    before, protected = _dirty_snapshot(root), protected_snapshot(root)
    try:
        yield
    finally:
        if set(changed_during_run(root, before)) - set(OUTPUTS.values()) or protected_snapshot(root) != protected:
            raise RuntimeError("outcome-unit producer changed protected/out-of-scope files")


def write_outputs(root: Path, payloads: dict[str, bytes]) -> None:
    if set(payloads) != set(OUTPUTS.values()):
        raise RuntimeError("exactly six outcome-unit outputs required")
    for relative, payload in payloads.items():
        target = root / relative
        if target.exists() and transport(target.read_bytes()) != payload:
            raise RuntimeError("immutable outcome-unit output already differs: " + relative)
    for relative, payload in payloads.items():
        target = root / relative
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as handle:
                handle.write(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()
    with model_owned_artifact_guard(args.repo_root):
        write_outputs(args.repo_root, build(args.repo_root))
    print("營收研究單位校準新版本已產生；舊證據及正式模型維持不變。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
