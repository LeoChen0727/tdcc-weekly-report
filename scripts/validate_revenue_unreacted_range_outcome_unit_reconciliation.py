"""Independent frozen-event revenue share-unit outcome validator."""
from __future__ import annotations

import argparse
import base64
from decimal import Decimal
import hashlib
from io import BytesIO
import json
import math
from pathlib import Path
import statistics

import pandas as pd

from revenue_unreacted_range_projection_source_io import read_git_payloads

ROOT = Path(__file__).resolve().parents[1]
VERSION = "outcome_unit_reconciliation_v1_20260923"
EVIDENCE_COMMIT = "001b82f856c4ca1a863d64998890fb1fdfba8030"
PRICE_COMMIT = "231d2e279a99a89f1888ece0361ea64d45f69ecd"
CONFIG = "config/revenue_unreacted_range_outcome_unit_actions_v1.json"
RESOLUTION = "config/revenue_unreacted_range_price_comparability_resolution.csv"
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
CODE = ("scripts/build_revenue_unreacted_range_outcome_unit_reconciliation.py",
        "scripts/validate_revenue_unreacted_range_outcome_unit_reconciliation.py")
ADDED_COLUMNS = (
    "unit_d20_date", "unit_raw_d0_close", "unit_raw_d20_close", "unit_existing_action_ids",
    "unit_added_action_ids", "unit_added_share_factor", "unit_reconciled_d20_return_pct",
    "unit_delta_percentage_points", "unit_reconciliation_status", "unit_anomaly_disposition",
)
FLAGS = {"research_only": "true", "formal_model_use_allowed": "false", "promotion_evidence_allowed": "false",
         "pdf_consumption_allowed": "false", "production_change": "false"}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def normalize(raw: bytes) -> bytes:
    return raw.removeprefix(b"\xef\xbb\xbf").replace(b"\r\n", b"\n")


def csv(raw: bytes) -> pd.DataFrame:
    return pd.read_csv(BytesIO(raw), dtype=str, keep_default_na=False, low_memory=False)


def canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def check_config(config: dict) -> None:
    if config.get("model_id") != "revenue_unreacted_range" or config.get("version") != VERSION:
        raise ValueError("action contract identity mismatch")
    events = config.get("events", [])
    if len(events) != 1:
        raise ValueError("exact single action required")
    event = events[0]
    for key, expected in {"event_id": "4763_20250630_par_value_change_1_to_10", "stock_id": "4763",
                          "effective_date": "20250630", "new_shares_per_old_share": "10",
                          "verification_status": "official_share_unit_event_verified",
                          "cash_component_status": "not_modelled_not_total_return"}.items():
        if event.get(key) != expected:
            raise ValueError("unapproved action value: " + key)
    observed = set()
    for key in event["documents"]:
        document = config["documents"][key]
        raw = base64.b64decode(document["payload_base64"], validate=True)
        if len(raw) != document["bytes"] or sha(raw) != document["sha256"]:
            raise ValueError("official evidence bytes differ")
        if document["first_publication_verified"] is not False or document["original_revision_chain_verified"] is not False:
            raise ValueError("unsupported first-publication/revision claim")
        tokens = document["required_tokens"]
        if len(tokens) < 3 or not all(token and token in raw.decode("utf-8") for token in tokens):
            raise ValueError("official document content assertions differ")
        observed.add(sha(raw))
    if observed != {"95fedb4a005b238a3c7959ce34bc16fce375c4c82bcb23334697efbf36ff06e9",
                    "33116fef9d83a263a03908697c399d1edcc9b1cb030efb7a09e647180c2d96f9"}:
        raise ValueError("wrong official documents")


def verify_detail(frozen: pd.DataFrame, actual: pd.DataFrame, raw_prices: dict[str, bytes], resolutions: pd.DataFrame, events: list[dict]) -> None:
    if list(actual.columns) != [*frozen.columns, *ADDED_COLUMNS] or len(actual) != len(frozen):
        raise ValueError("detail schema/row count mismatch")
    if frozen.episode_key.duplicated().any() or not actual.loc[:, frozen.columns].equals(frozen):
        raise ValueError("frozen event identity/columns changed")
    price_lookup = {}
    for stock, raw in raw_prices.items():
        frame = csv(raw)
        if frame.date.duplicated().any() or not frame.date.str.fullmatch(r"\d{8}").all():
            raise ValueError("duplicate/invalid raw dates")
        values = []
        for row in frame.sort_values("date").to_dict("records"):
            if row["date"] > "20260713":
                continue
            try:
                close = Decimal(row["close"])
            except Exception:
                continue
            if not close.is_finite():
                continue
            if close <= 0:
                raise ValueError("nonpositive close")
            values.append((row["date"], row["close"], close))
        price_lookup[stock] = (values, {value[0]: index for index, value in enumerate(values)})
    for original, row in zip(frozen.to_dict("records"), actual.to_dict("records")):
        flagged = any(original[key].lower() == "true" for key in (
            "qualifying_source_revenue_anomaly_candidate_flag", "unresolved_price_path_candidate_flag"))
        status = "unresolved_anomaly_candidate" if flagged else "not_assessed_not_a_clearance"
        if row["unit_anomaly_disposition"] != status:
            raise ValueError("anomaly disposition changed")
        if not original["first_breakout_d20_return_pct"]:
            if row["unit_reconciliation_status"] != "no_mature_d20_observation" or any(row[key] for key in ADDED_COLUMNS[:-2]):
                raise ValueError("invented immature outcome")
            continue
        stock, start_date = original["stock_id"], original["first_breakout_date"]
        values, date_indices = price_lookup[stock]
        index = date_indices[start_date]
        start, end = values[index], values[index + 20]
        old_factor = Decimal(1)
        old_ids = []
        for resolution in resolutions.to_dict("records"):
            if resolution["stock_id"] == stock and resolution["root_cause_status"] == "verified_non_comparable_raw_price_scale" and start_date < resolution["resume_date"] <= end[0]:
                ratio = Decimal(resolution["exchange_ratio"])
                if not ratio.is_finite() or ratio <= 0:
                    raise ValueError("invalid legacy action")
                old_factor *= ratio
                old_ids.append(resolution["resolution_id"])
        replay = (end[2] * old_factor / start[2] - 1) * 100
        original_return = Decimal(original["first_breakout_d20_return_pct"])
        if abs(replay - original_return) > Decimal("0.000051"):
            raise ValueError("old outcome does not match raw/legacy action replay")
        factor, ids = Decimal(1), []
        for event in events:
            if event["stock_id"] == stock and start_date < event["effective_date"] <= end[0]:
                if any(res["stock_id"] == stock and res["resume_date"] == event["effective_date"] and res["root_cause_status"] == "verified_non_comparable_raw_price_scale" for res in resolutions.to_dict("records")):
                    raise ValueError("double adjustment forbidden")
                factor *= Decimal(event["new_shares_per_old_share"])
                ids.append(event["event_id"])
        value = (end[2] * old_factor * factor / start[2] - 1) * 100 if ids else original_return
        expected_text = {"unit_d20_date": end[0], "unit_raw_d0_close": start[1], "unit_raw_d20_close": end[1],
                         "unit_existing_action_ids": "|".join(old_ids), "unit_added_action_ids": "|".join(ids),
                         "unit_reconciliation_status": "share_unit_only_reconciled" if ids else "unchanged_frozen_observation"}
        for key, expected in expected_text.items():
            if row[key] != expected:
                raise ValueError("outcome lineage mismatch: " + key)
        for key, expected in (("unit_added_share_factor", factor), ("unit_reconciled_d20_return_pct", value),
                              ("unit_delta_percentage_points", value - original_return)):
            if abs(Decimal(row[key]) - expected) > Decimal("0.00000001"):
                raise ValueError("independent outcome mismatch: " + key)


def verify_comparison(detail: pd.DataFrame, actual: pd.DataFrame) -> None:
    expected = []
    for variant in sorted(detail.condition_variant_id.unique()):
        population = [row for row in detail.to_dict("records") if row["condition_variant_id"] == variant]
        flagged = lambda row: any(row[key].lower() == "true" for key in ("qualifying_source_revenue_anomaly_candidate_flag", "unresolved_price_path_candidate_flag"))
        for basis in ("primary_all_rows", "candidate_exclusion_sensitivity_only"):
            selected = population if basis == "primary_all_rows" else [row for row in population if not flagged(row)]
            for version, column in (("frozen_v3", "first_breakout_d20_return_pct"), (VERSION, "unit_reconciled_d20_return_pct")):
                values = [float(row[column]) for row in selected if row[column]]
                count = len(values)
                row = {"condition_variant_id": variant, "metric_basis": basis, "outcome_version": version,
                       "episode_count": str(len(selected)), "stock_count": str(len({r["stock_id"] for r in selected})),
                       "observed_d20_count": str(count), "unresolved_candidate_count": str(sum(flagged(r) for r in selected)),
                       "metric_interpretation": "frozen_breakout_close_D20_share_unit_observation_not_total_return_or_formal_win_rate", **FLAGS}
                numeric = {"positive_rate_pct": sum(v > 0 for v in values) / count * 100,
                           "neutral_rate_pct": sum(v == 0 for v in values) / count * 100,
                           "loss_rate_pct": sum(v < 0 for v in values) / count * 100,
                           "high_return_ge20_rate_pct": sum(v >= 20 for v in values) / count * 100,
                           "mean_pct": statistics.mean(values), "median_pct": statistics.median(values),
                           "min_pct": min(values), "max_pct": max(values)} if count else {key: "" for key in (
                               "positive_rate_pct", "neutral_rate_pct", "loss_rate_pct", "high_return_ge20_rate_pct", "mean_pct", "median_pct", "min_pct", "max_pct")}
                expected.append((row, numeric))
    if len(actual) != len(expected):
        raise ValueError("comparison population count mismatch")
    for observed, (text, numbers) in zip(actual.to_dict("records"), expected):
        if set(observed) != set(text) | set(numbers):
            raise ValueError("comparison schema mismatch")
        for key, value in text.items():
            if observed[key] != value:
                raise ValueError("comparison count/boundary mismatch: " + key)
        for key, value in numbers.items():
            if value == "":
                if observed[key] != "":
                    raise ValueError("empty comparison metric invented")
            else:
                number = float(observed[key])
                if not math.isfinite(number) or abs(number - value) > 1e-8:
                    raise ValueError("comparison metric mismatch: " + key)


def verify_report(raw: bytes, row_count: int, changed_count: int) -> None:
    expected = ("# 營收爆發但股價尚未反應：凍結事件公司行動單位校準\n\n"
                f"保留全部 {row_count} 筆 v3 事件與所有舊欄位、突破日期、D20 個股有效 close 序列。新單位校準影響 {changed_count} 個情境事件，不等於獨立交易數。\n\n"
                "只校準已確認換股的固定 D20 價格觀察；不重算條件、特徵、launch、啟動率或買賣日期。舊 launch labels 不得解讀為單位校準後的新啟動結果。\n\n"
                "這不是完整總報酬、正式操作損益、首次發布 PIT 或 promotion 證據；股利、其他公司行動完整覆蓋、交易日曆完整性與可成交性仍未證實。\n\n"
                "原有未解異常旗標與 primary 全列保留，candidate_exclusion_sensitivity_only 僅為敏感度，不能叫修正績效。未標記不代表已查明無異常。\n\n"
                "只使用月營收既有事件，不納入 EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報。正式模型、adapter、readiness、六份 PDF、Apps Script 及舊證據均未改動。\n")
    if normalize(raw) != expected.encode("utf-8"):
        raise ValueError("report exact research-only contract mismatch")


def validate(root: Path = ROOT) -> dict:
    payloads = {key: normalize((root / path).read_bytes()) for key, path in OUTPUTS.items()}
    manifest = json.loads(payloads["manifest"])
    expected_identity = {"version": VERSION, "model_id": "revenue_unreacted_range", "owner_id": "revenue_unreacted_range_outcome_unit_reconciliation",
                         "evidence_commit": EVIDENCE_COMMIT, "price_commit": PRICE_COMMIT, "cutoff": "20260713",
                         "source_row_count": 20430, "launch_labels_recomputed": False, "cash_flow_total_return_complete": False,
                         "first_publication_PIT_proven": False, **FLAGS}
    for key, value in expected_identity.items():
        if manifest.get(key) != value:
            raise ValueError("manifest identity/boundary mismatch: " + key)
    hashes = {OUTPUTS[key]: sha(value) for key, value in payloads.items() if key != "manifest"}
    if manifest.get("output_sha256") != hashes:
        raise ValueError("artifact SHA mismatch")
    if manifest.get("code_canonical_sha256") != {path: sha(normalize((root / path).read_bytes())) for path in CODE}:
        raise ValueError("code canonical binding mismatch")
    frozen = read_git_payloads(root, EVIDENCE_COMMIT, OLD_PATHS)
    if set(frozen) != set(OLD_PATHS) or manifest["source_artifact_sha256"] != {p: sha(v) for p, v in frozen.items()}:
        raise ValueError("fixed v3 source binding mismatch")
    old = csv(frozen[OLD_PREFIX + "detail.csv"])
    if len(old) != 20430 or sha(frozen[OLD_PREFIX + "detail.csv"]) != "fad447e45ba84f9767cd3a317a3ce0ea9e930f434370788e407294ef57792972":
        raise ValueError("wrong frozen v3 detail")
    config = json.loads((root / CONFIG).read_text(encoding="utf-8-sig"))
    check_config(config)
    if manifest["config_canonical_sha256"] != sha(canonical(config)):
        raise ValueError("config canonical SHA mismatch")
    stocks = sorted(set(old.loc[old.first_breakout_d20_return_pct.ne(""), "stock_id"]))
    paths = (RESOLUTION, *(f"data/stock_price_history/{stock}.csv" for stock in stocks))
    raw = {}
    for offset in range(0, len(paths), 96):
        raw.update(read_git_payloads(root, PRICE_COMMIT, paths[offset:offset + 96]))
    if set(raw) != set(paths) or manifest["raw_source_sha256"] != {p: sha(v) for p, v in raw.items()}:
        raise ValueError("raw price binding mismatch")
    detail = csv(payloads["detail"])
    verify_detail(old, detail, {stock: raw[f"data/stock_price_history/{stock}.csv"] for stock in stocks}, csv(raw[RESOLUTION]), config["events"])
    verify_comparison(detail, csv(payloads["comparison"]))
    changes = detail.loc[detail.unit_added_action_ids.ne(""), ["episode_key", "condition_variant_id", "stock_id", "first_breakout_date", "first_breakout_d20_return_pct", *ADDED_COLUMNS]].reset_index(drop=True)
    if not changes.equals(csv(payloads["changes"])) or manifest["changed_row_count"] != len(changes):
        raise ValueError("changed events missing/modified")
    actions = csv(payloads["actions"])
    expected_actions = pd.DataFrame([{**event, "documents": "|".join(event["documents"])} for event in config["events"]]).astype(str)
    if not actions.equals(expected_actions):
        raise ValueError("action evidence ledger differs")
    verify_report(payloads["report"], len(detail), len(changes))
    return {"rows": len(detail), "changed_rows": len(changes), "formal_use": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()
    print("營收研究獨立單位校準驗證通過：" + json.dumps(validate(args.repo_root), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
