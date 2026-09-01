from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

try:
    from model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
        validate_changed_paths,
    )
except ModuleNotFoundError:  # pragma: no cover - package import used by focused tests
    from scripts.model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
        validate_changed_paths,
    )


MODEL_ID = "tdcc_short_term_continuation_d5_d10"
RESEARCH_ID = "tdcc_short_term_continuation_d5_d10_exact_edge_replay"
ARTIFACT_VERSION = "tdcc_short_term_continuation_d5_d10_research_v1"
PRODUCER = "scripts/build_tdcc_short_term_continuation_d5_d10_research.py"
VALIDATOR = "scripts/validate_tdcc_short_term_continuation_d5_d10_research.py"

RULE_A = "phase_overheated_bb_normal_2w20_50_tdcc1w"
RULE_B = "phase_overheated_kd_bull_not_hot_1w10_30_2w20_50"
RULE_C = "all_thresholds_overheated_1w10_30_macd_hist_pos"
RULE_IDS = (RULE_A, RULE_B, RULE_C)

SCENARIOS = (
    ("fixed_d5_close", 5),
    ("fixed_d10_close", 10),
)
ENTRY_RULE_ID = "signal_close_confirmed_next_trading_day_open"
STOP_RULE_ID = "none_fixed_horizon_research"
PIT_STATUS = "blocked_no_event_time_immutable_signal_packet"
PIT_BLOCKER = (
    "historical rows come from a rebuilt canonical signal snapshot bound to one current TDCC "
    "dataset id; no immutable event-time specialty packet and manifest proves that each "
    "historical interpreted row existed unchanged on its signal date"
)
PROMOTION_BLOCK_REASON = (
    "PIT_event_time_lineage_missing|formal_operation_contract_undefined|"
    "unresolved_anomaly_candidates_block_when_present"
)
TDCC_MANIFEST_SCHEMA = "tdcc_dataset_manifest_v1"
TDCC_HASH_MODE = "utf8_text_lf_normalized_sha256"
TDCC_HISTORY_RELATIVE_ROOT = Path("output/history/tdcc")
TDCC_HISTORY_REQUIRED_COLUMNS = {
    "date",
    "code",
    "over_400_pct",
    "over_600_pct",
    "over_800_pct",
    "over_1000_pct",
}
PUBLISHED_ROLE = "supplementary_only_not_selector_or_primary"
ANOMALY_TRIGGER_ID = "abs_realized_return_ge_20pct_investigation_trigger_v1"
ANOMALY_TRIGGER_THRESHOLD_PCT = 20.0
HIGH_RETURN_THRESHOLD_PCT = 10.0

FROZEN_SELECTOR_CONTRACT = {
    "model_id": MODEL_ID,
    "union_key": ["signal_date", "stock_id"],
    "union_policy": "A_or_B_or_C_deduplicated_before_scenario_expansion",
    "rules": {
        RULE_A: (
            "tdcc_price_phase=overheated_after_tdcc; "
            "0<=bb_width_percentile_120d<=80; 20<=price_ret_2w<=50; "
            "tdcc_consecutive_up_weeks=1"
        ),
        RULE_B: (
            "tdcc_price_phase=overheated_after_tdcc; k_value>d_value; k_value<90; "
            "10<=price_ret_1w<=30; 20<=price_ret_2w<=50"
        ),
        RULE_C: (
            "is_all_thresholds=True; overheat_bucket=overheated; "
            "10<=price_ret_1w<=30; macd_hist>0"
        ),
    },
}
SELECTOR_CONTRACT_SHA256 = hashlib.sha256(
    json.dumps(
        FROZEN_SELECTOR_CONTRACT,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
).hexdigest()

EVENT_COLUMNS = [
    "research_id",
    "artifact_version",
    "model_id",
    "signal_event_key",
    "scenario_event_key",
    "signal_date",
    "stock_id",
    "stock_name",
    "market_regime",
    "benchmark_index",
    "source_signal_id",
    "source_signal_row_sha256",
    "source_tdcc_dataset_id",
    "source_tdcc_dataset_hash",
    "source_tdcc_manifest_path",
    "source_tdcc_manifest_sha256",
    "source_signal_snapshot_path",
    "source_signal_snapshot_sha256",
    "source_price_path",
    "source_price_sha256",
    "source_price_high_water_date",
    "selector_contract_sha256",
    "matched_rule_ids",
    "matched_rule_count",
    "rule_a_matched",
    "rule_b_matched",
    "rule_c_matched",
    "rule_membership_overlap",
    "tdcc_price_phase",
    "overheat_bucket",
    "is_all_thresholds",
    "tdcc_consecutive_up_weeks",
    "price_ret_1w_pct",
    "price_ret_2w_pct",
    "bb_width_percentile_120d",
    "k_value",
    "d_value",
    "macd_hist",
    "signal_close_price",
    "scenario_id",
    "horizon_trading_days_after_signal",
    "entry_rule_id",
    "entry_date",
    "entry_price",
    "exit_rule_id",
    "exit_date",
    "exit_price",
    "stop_rule_id",
    "return_formula",
    "return_valid",
    "invalid_reason",
    "realized_return_pct",
    "return_outcome",
    "high_return_hit",
    "loss_flag",
    "mfe_pct_advisory",
    "mae_pct_advisory",
    "intraday_metrics_role",
    "intraday_metrics_formal_use",
    "same_stock_overlap_candidate",
    "same_stock_overlap_policy",
    "anomaly_candidate",
    "anomaly_candidate_ids",
    "anomaly_disposition",
    "primary_metric_included",
    "unresolved_candidate_retained_in_primary",
    "price_adjustment_basis_status",
    "pit_exact_replay",
    "pit_replay_status",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
    "promotion_blocked",
    "promotion_block_reason",
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "model_id",
    "scenario_id",
    "horizon_trading_days_after_signal",
    "group_kind",
    "group_value",
    "group_overlap_policy",
    "evidence_role",
    "source_status",
    "signal_event_count",
    "valid_return_count",
    "pending_or_invalid_count",
    "right_censored_count",
    "non_right_censored_invalid_count",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "average_return_pct",
    "median_return_pct",
    "minimum_return_pct",
    "maximum_return_pct",
    "high_return_threshold_pct",
    "high_return_hit_count",
    "high_return_hit_rate_pct",
    "anomaly_candidate_count",
    "unresolved_anomaly_candidate_count",
    "same_stock_overlap_candidate_count",
    "primary_metric_retains_unresolved_candidates",
    "candidate_exclusion_sensitivity_valid_return_count",
    "candidate_exclusion_sensitivity_excluded_candidate_count",
    "candidate_exclusion_sensitivity_win_rate_pct",
    "candidate_exclusion_sensitivity_average_return_pct",
    "candidate_exclusion_sensitivity_median_return_pct",
    "sensitivity_is_corrected_primary",
    "sample_status",
    "entry_rule_id",
    "exit_rule_id",
    "stop_rule_id",
    "pit_replay_status",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
    "promotion_blocked",
    "promotion_block_reason",
]

ANOMALY_COLUMNS = [
    "research_id",
    "artifact_version",
    "model_id",
    "anomaly_candidate_id",
    "evidence_role",
    "metric_scope",
    "scenario_id",
    "signal_event_key",
    "scenario_event_key",
    "signal_date",
    "stock_id",
    "realized_return_pct",
    "trigger_id",
    "trigger_observed_abs_return_pct",
    "trigger_threshold_pct",
    "trigger_is_classification",
    "identity_and_non_overlap_check_status",
    "formal_entry_exit_stop_replay_check_status",
    "pit_dates_and_trading_calendar_check_status",
    "raw_source_lineage_and_immutable_hash_check_status",
    "units_formula_and_adjustment_basis_check_status",
    "authoritative_corporate_action_history_check_status",
    "independent_source_corroboration_check_status",
    "reproducible_evidence_reference_check_status",
    "all_required_checks_complete",
    "final_disposition",
    "retained_in_primary_metrics",
    "excluded_from_primary_metrics",
    "supplementary_metric_included",
    "formal_use",
    "promotion_blocked",
    "investigation_note",
]

MANIFEST_COLUMNS = [
    "schema_version",
    "research_id",
    "artifact_version",
    "model_id",
    "producer_path",
    "validator_path",
    "generated_at",
    "selector_contract_sha256",
    "selector_rule_ids",
    "selector_union_policy",
    "source_tdcc_dataset_id",
    "source_tdcc_dataset_hash",
    "source_tdcc_manifest_path",
    "source_tdcc_manifest_sha256",
    "source_signal_snapshot_path",
    "source_signal_snapshot_sha256",
    "source_signal_snapshot_row_count",
    "source_price_root",
    "evaluated_price_file_count",
    "evaluated_price_bundle_sha256",
    "source_price_high_water_date",
    "published_snapshot_path",
    "published_snapshot_sha256",
    "published_snapshot_status",
    "published_snapshot_role",
    "published_snapshot_target_row_count",
    "events_artifact_path",
    "events_artifact_sha256",
    "events_row_count",
    "events_key_set_sha256",
    "summary_artifact_path",
    "summary_artifact_sha256",
    "summary_row_count",
    "summary_key_set_sha256",
    "anomaly_artifact_path",
    "anomaly_artifact_sha256",
    "anomaly_row_count",
    "anomaly_key_set_sha256",
    "union_signal_event_count",
    "scenario_event_count",
    "rule_membership_overlap_event_count",
    "same_stock_overlap_candidate_count",
    "valid_d5_count",
    "valid_d10_count",
    "unresolved_anomaly_candidate_count",
    "entry_rule_id",
    "exit_rule_ids",
    "stop_rule_id",
    "operation_replay_semantics",
    "intraday_metric_role",
    "unresolved_candidates_primary_policy",
    "pit_replay_status",
    "pit_replay_blocker",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
    "promotion_blocked",
    "promotion_block_reason",
]


@dataclass(frozen=True)
class OutputPaths:
    events: Path
    summary: Path
    manifest: Path
    anomaly: Path


def output_paths(output_dir: Path) -> OutputPaths:
    stem = "tdcc_short_term_continuation_d5_d10_research"
    return OutputPaths(
        events=output_dir / f"{stem}_events_latest.csv",
        summary=output_dir / f"{stem}_summary_latest.csv",
        manifest=output_dir / f"{stem}_manifest_latest.csv",
        anomaly=output_dir / f"{stem}_anomaly_candidates_latest.csv",
    )


def normalize_date(value: Any) -> str:
    digits = "".join(character for character in str(value or "") if character.isdigit())
    return digits[:8] if len(digits) >= 8 else ""


def normalize_stock_id(value: Any) -> str:
    text = str(value or "").strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def text_value(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return str(value).strip()


def bool_value(value: Any) -> bool:
    text = text_value(value).lower()
    if text in {"true", "1", "yes"}:
        return True
    if text in {"false", "0", "no", ""}:
        return False
    raise RuntimeError(f"invalid boolean value in canonical signal snapshot: {value!r}")


def number(value: Any) -> float:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return float(parsed) if pd.notna(parsed) else math.nan


def finite(value: Any) -> bool:
    parsed = number(value)
    return not math.isnan(parsed) and math.isfinite(parsed)


def normalized_text_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def canonical_json_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def canonical_row_sha256(row: pd.Series) -> str:
    return canonical_json_sha256(
        {str(column): text_value(row.get(column, "")) for column in sorted(row.index)}
    )


def require_columns(frame: pd.DataFrame, required: set[str], label: str) -> None:
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"{label} missing required columns: {missing}")


def read_csv_str(path: Path, label: str) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"{label} is missing or empty: {path.as_posix()}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    except Exception as exc:
        raise RuntimeError(f"cannot read {label} {path.as_posix()}: {exc}") from exc


def _resolve_tdcc_history_snapshot_path(
    path_text: str,
    *,
    snapshot_date: str,
    repo_root: Path,
) -> Path:
    normalized = path_text.replace("\\", "/")
    relative = Path(normalized)
    if (
        not normalized
        or relative.is_absolute()
        or any(part in {"", ".", ".."} for part in relative.parts)
    ):
        raise RuntimeError(
            f"canonical TDCC history snapshot path is not repository-relative: {path_text!r}"
        )
    approved_root = (repo_root / TDCC_HISTORY_RELATIVE_ROOT).resolve()
    resolved = (repo_root / relative).resolve()
    try:
        resolved.relative_to(approved_root)
    except ValueError as exc:
        raise RuntimeError(
            "canonical TDCC history snapshot path escapes the approved root: "
            f"{path_text!r}"
        ) from exc
    expected_name = f"tdcc_holder_ratio_{snapshot_date}.csv"
    if resolved.parent != approved_root or resolved.name != expected_name:
        raise RuntimeError(
            "canonical TDCC history snapshot path identity mismatch: "
            f"date={snapshot_date} path={path_text!r}"
        )
    if not resolved.is_file() or resolved.stat().st_size <= 0:
        raise RuntimeError(
            f"canonical TDCC history snapshot is missing or empty: {resolved.as_posix()}"
        )
    return resolved


def _verify_tdcc_history_snapshot(
    item: dict[str, Any],
    *,
    snapshot_date: str,
    repo_root: Path,
) -> tuple[dict[str, Any], set[str]]:
    source_path = _resolve_tdcc_history_snapshot_path(
        text_value(item.get("path")),
        snapshot_date=snapshot_date,
        repo_root=repo_root,
    )
    expected_sha256 = text_value(item.get("sha256")).lower()
    if len(expected_sha256) != 64 or any(
        character not in "0123456789abcdef" for character in expected_sha256
    ):
        raise RuntimeError(
            f"canonical TDCC history snapshot sha256 is invalid: date={snapshot_date}"
        )
    actual_sha256 = normalized_text_sha256(source_path)
    if actual_sha256 != expected_sha256:
        raise RuntimeError(
            "canonical TDCC history snapshot hash mismatch: "
            f"date={snapshot_date} expected={expected_sha256} actual={actual_sha256}"
        )
    frame = read_csv_str(source_path, f"canonical TDCC history snapshot {snapshot_date}")
    require_columns(
        frame,
        TDCC_HISTORY_REQUIRED_COLUMNS,
        f"canonical TDCC history snapshot {snapshot_date}",
    )
    dates = frame["date"].map(normalize_date)
    codes = frame["code"].map(normalize_stock_id)
    if frame.empty or set(dates) != {snapshot_date}:
        raise RuntimeError(
            f"canonical TDCC history snapshot date identity mismatch: {snapshot_date}"
        )
    if codes.eq("").any() or codes.duplicated().any():
        raise RuntimeError(
            f"canonical TDCC history snapshot stock identity is empty or duplicated: {snapshot_date}"
        )
    try:
        expected_row_count = int(item.get("row_count", -1))
        expected_stock_count = int(item.get("stock_count", -1))
    except (TypeError, ValueError) as exc:
        raise RuntimeError(
            f"canonical TDCC history snapshot counts are invalid: {snapshot_date}"
        ) from exc
    if len(frame) != expected_row_count:
        raise RuntimeError(
            "canonical TDCC history snapshot row_count mismatch: "
            f"date={snapshot_date} expected={expected_row_count} actual={len(frame)}"
        )
    if codes.nunique() != expected_stock_count:
        raise RuntimeError(
            "canonical TDCC history snapshot stock_count mismatch: "
            f"date={snapshot_date} expected={expected_stock_count} actual={codes.nunique()}"
        )
    return (
        {
            "date": snapshot_date,
            "row_count": expected_row_count,
            "stock_count": expected_stock_count,
            "sha256": actual_sha256,
        },
        set(codes),
    )


def load_tdcc_manifest(path: Path, *, repo_root: Path) -> dict[str, Any]:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"canonical TDCC manifest is missing or empty: {path.as_posix()}")
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read canonical TDCC manifest {path.as_posix()}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError("canonical TDCC manifest must be a JSON object")
    if value.get("status") != "pass" or value.get("schema_version") != TDCC_MANIFEST_SCHEMA:
        raise RuntimeError("canonical TDCC manifest is not a passing tdcc_dataset_manifest_v1")
    if text_value(value.get("hash_mode")) != TDCC_HASH_MODE:
        raise RuntimeError("canonical TDCC manifest hash_mode is invalid")
    if text_value(value.get("canonical_source_root")).replace("\\", "/") != (
        TDCC_HISTORY_RELATIVE_ROOT.as_posix()
    ):
        raise RuntimeError("canonical TDCC manifest source root is not approved")
    signal_date = normalize_date(value.get("signal_date", ""))
    dataset_id = text_value(value.get("dataset_id", ""))
    dataset_hash = text_value(value.get("dataset_hash", "")).lower()
    history_dates = [normalize_date(item) for item in value.get("history_dates", [])]
    required_dates = [normalize_date(item) for item in value.get("required_dates", [])]
    if len(signal_date) != 8:
        raise RuntimeError("canonical TDCC manifest identity is invalid")
    if not history_dates or history_dates != sorted(set(history_dates)) or signal_date != history_dates[-1]:
        raise RuntimeError("canonical TDCC manifest history_dates are invalid")
    if (
        not required_dates
        or required_dates != sorted(set(required_dates))
        or len(required_dates) > len(history_dates)
        or history_dates[-len(required_dates) :] != required_dates
        or signal_date != required_dates[-1]
    ):
        raise RuntimeError("canonical TDCC manifest required_dates are invalid")
    snapshots = value.get("history_snapshots", [])
    if not isinstance(snapshots, list) or int(value.get("history_snapshot_count", -1)) != len(snapshots):
        raise RuntimeError("canonical TDCC manifest history snapshot count is invalid")
    observed_snapshot_dates = [
        normalize_date(item.get("date", "")) for item in snapshots if isinstance(item, dict)
    ]
    if observed_snapshot_dates != history_dates or len(observed_snapshot_dates) != len(snapshots):
        raise RuntimeError("canonical TDCC manifest history snapshots do not match history_dates")
    verified_results = [
        _verify_tdcc_history_snapshot(
            item,
            snapshot_date=history_dates[index],
            repo_root=Path(repo_root),
        )
        for index, item in enumerate(snapshots)
        if isinstance(item, dict)
    ]
    if len(verified_results) != len(snapshots):
        raise RuntimeError("canonical TDCC manifest history snapshots must contain objects")
    verified_snapshots = [identity for identity, _ in verified_results]
    snapshot_codes = {
        history_dates[index]: codes for index, (_, codes) in enumerate(verified_results)
    }
    try:
        current_stock_count = int(value.get("current_stock_count", -1))
    except (TypeError, ValueError) as exc:
        raise RuntimeError("canonical TDCC manifest current_stock_count is invalid") from exc
    if current_stock_count <= 0 or current_stock_count != int(
        verified_snapshots[-1]["stock_count"]
    ):
        raise RuntimeError(
            "canonical TDCC manifest current_stock_count does not match final history snapshot"
        )
    official_date_source = text_value(value.get("official_date_source"))
    if not official_date_source:
        raise RuntimeError("canonical TDCC manifest official_date_source is empty")
    accepted_raw = value.get("accepted_history_exceptions", [])
    if not isinstance(accepted_raw, list):
        raise RuntimeError("canonical TDCC manifest accepted_history_exceptions must be a list")
    accepted: list[dict[str, str]] = []
    required_date_set = set(required_dates)
    for item in accepted_raw:
        if not isinstance(item, dict):
            raise RuntimeError("canonical TDCC accepted history exception must be an object")
        exception_date = normalize_date(item.get("date"))
        stock_id = normalize_stock_id(item.get("stock_id"))
        if exception_date not in required_date_set or not stock_id:
            raise RuntimeError("canonical TDCC accepted history exception identity is invalid")
        accepted.append({"date": exception_date, "stock_id": stock_id})
    if accepted != sorted(accepted, key=lambda item: (item["date"], item["stock_id"])) or len(
        {(item["date"], item["stock_id"]) for item in accepted}
    ) != len(accepted):
        raise RuntimeError("canonical TDCC accepted history exceptions are not ordered unique")
    current_codes = snapshot_codes[signal_date]
    observed_missing_pairs = {
        (required_date, stock_id)
        for required_date in required_dates
        for stock_id in current_codes - snapshot_codes[required_date]
    }
    accepted_pairs = {(item["date"], item["stock_id"]) for item in accepted}
    if accepted_pairs != observed_missing_pairs:
        raise RuntimeError(
            "canonical TDCC accepted history exceptions do not match verified required snapshots"
        )
    identity_payload = {
        "schema_version": TDCC_MANIFEST_SCHEMA,
        "signal_date": signal_date,
        "official_date_source": official_date_source,
        "required_dates": required_dates,
        "history_dates": history_dates,
        "current_stock_count": current_stock_count,
        "history_snapshots": verified_snapshots,
        "accepted_history_exceptions": accepted,
    }
    expected_dataset_hash = canonical_json_sha256(identity_payload)
    expected_dataset_id = f"tdcc-{signal_date}-{expected_dataset_hash[:16]}"
    if dataset_hash != expected_dataset_hash:
        raise RuntimeError("canonical TDCC manifest dataset_hash does not match verified history")
    if dataset_id != expected_dataset_id:
        raise RuntimeError("canonical TDCC manifest dataset_id does not bind verified history")
    value["signal_date"] = signal_date
    value["required_dates"] = required_dates
    value["history_dates"] = history_dates
    value["dataset_hash"] = expected_dataset_hash
    value["dataset_id"] = expected_dataset_id
    return value


def load_signal_snapshot(path: Path, manifest: dict[str, Any]) -> pd.DataFrame:
    frame = read_csv_str(path, "canonical TDCC signal snapshot")
    required = {
        "signal_id",
        "signal_date",
        "code",
        "name",
        "tdcc_price_phase",
        "overheat_bucket",
        "is_all_thresholds",
        "tdcc_consecutive_up_weeks",
        "price_ret_1w",
        "price_ret_2w",
        "market_regime",
        "benchmark_index",
        "source_tdcc_dataset_id",
    }
    require_columns(frame, required, "canonical TDCC signal snapshot")
    frame = frame.copy()
    frame["signal_date"] = frame["signal_date"].map(normalize_date)
    frame["code"] = frame["code"].map(normalize_stock_id)
    if frame.empty or frame["signal_date"].eq("").any() or frame["code"].eq("").any():
        raise RuntimeError("canonical TDCC signal snapshot contains empty identity fields")
    if frame["signal_id"].eq("").any() or frame["signal_id"].duplicated().any():
        raise RuntimeError("canonical TDCC signal snapshot signal_id must be non-empty and unique")
    if frame[["signal_date", "code"]].duplicated().any():
        raise RuntimeError("canonical TDCC signal snapshot must be unique by signal_date + code")
    history_dates = set(manifest["history_dates"])
    outside = sorted(set(frame["signal_date"]) - history_dates)
    if outside:
        raise RuntimeError(f"canonical TDCC signal snapshot dates are outside manifest history: {outside[:10]}")
    dataset_ids = set(frame["source_tdcc_dataset_id"].map(text_value))
    if dataset_ids != {text_value(manifest["dataset_id"])}:
        raise RuntimeError("canonical TDCC signal snapshot source_tdcc_dataset_id does not match manifest")
    return frame.sort_values(["signal_date", "code", "signal_id"]).reset_index(drop=True)


def load_price_frame(path: Path, stock_id: str) -> pd.DataFrame:
    frame = read_csv_str(path, f"price history for {stock_id}")
    require_columns(frame, {"date", "open", "high", "low", "close"}, f"price history for {stock_id}")
    frame = frame.copy()
    frame["date"] = frame["date"].map(normalize_date)
    if frame["date"].eq("").any() or frame["date"].duplicated().any():
        raise RuntimeError(f"price history for {stock_id} contains empty or duplicate dates")
    for column in ["open", "high", "low", "close"]:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
        non_positive = frame[column].notna() & frame[column].le(0)
        if non_positive.any():
            raise RuntimeError(f"price history for {stock_id} contains non-positive {column}")
    frame = frame.sort_values("date").reset_index(drop=True)
    close = frame["close"]
    high = frame["high"]
    low = frame["low"]
    ema12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
    ema26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
    dif = ema12 - ema26
    dea = dif.ewm(span=9, adjust=False, min_periods=9).mean()
    frame["macd_hist"] = dif - dea
    low9 = low.rolling(9, min_periods=9).min()
    high9 = high.rolling(9, min_periods=9).max()
    rsv9 = ((close - low9) / (high9 - low9) * 100).replace([np.inf, -np.inf], np.nan)
    frame["k_value"] = rsv9.ewm(alpha=1 / 3, adjust=False, min_periods=1).mean()
    frame["d_value"] = frame["k_value"].ewm(alpha=1 / 3, adjust=False, min_periods=1).mean()
    ma20 = close.rolling(20, min_periods=20).mean()
    std20 = close.rolling(20, min_periods=20).std()
    bb_width = ((ma20 + 2 * std20) - (ma20 - 2 * std20)) / ma20 * 100
    frame["bb_width_percentile_120d"] = bb_width.rolling(120, min_periods=20).apply(
        lambda values: (values <= values[-1]).mean() * 100
        if not np.isnan(values[-1])
        else np.nan,
        raw=True,
    )
    return frame


def display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def in_range(value: Any, lower: float, upper: float) -> bool:
    parsed = number(value)
    return finite(parsed) and lower <= parsed <= upper


def preliminary_rule_requirements(row: pd.Series) -> tuple[bool, bool, bool]:
    phase = text_value(row.get("tdcc_price_phase"))
    pre_a = (
        phase == "overheated_after_tdcc"
        and in_range(row.get("price_ret_2w"), 20, 50)
        and number(row.get("tdcc_consecutive_up_weeks")) == 1
    )
    pre_b = (
        phase == "overheated_after_tdcc"
        and in_range(row.get("price_ret_1w"), 10, 30)
        and in_range(row.get("price_ret_2w"), 20, 50)
    )
    pre_c = (
        bool_value(row.get("is_all_thresholds"))
        and text_value(row.get("overheat_bucket")) == "overheated"
        and in_range(row.get("price_ret_1w"), 10, 30)
    )
    return pre_a, pre_b, pre_c


def matched_rule_ids(
    row: pd.Series,
    *,
    bb_width_percentile_120d: float,
    k_value: float,
    d_value: float,
    macd_hist: float,
) -> tuple[str, ...]:
    pre_a, pre_b, pre_c = preliminary_rule_requirements(row)
    matches: list[str] = []
    if pre_a and finite(bb_width_percentile_120d) and 0 <= bb_width_percentile_120d <= 80:
        matches.append(RULE_A)
    if pre_b and finite(k_value) and finite(d_value) and k_value > d_value and k_value < 90:
        matches.append(RULE_B)
    if pre_c and finite(macd_hist) and macd_hist > 0:
        matches.append(RULE_C)
    return tuple(matches)


def _advisory_path_metrics(
    price: pd.DataFrame,
    *,
    signal_index: int,
    horizon: int,
    entry_price: float,
) -> tuple[float, float]:
    if not finite(entry_price):
        return math.nan, math.nan
    end_index = signal_index + horizon
    if signal_index + 1 >= len(price) or end_index >= len(price):
        return math.nan, math.nan
    window = price.iloc[signal_index + 1 : end_index + 1]
    highs = pd.to_numeric(window["high"], errors="coerce").dropna()
    lows = pd.to_numeric(window["low"], errors="coerce").dropna()
    mfe = ((highs.max() / entry_price) - 1) * 100 if not highs.empty else math.nan
    mae = ((lows.min() / entry_price) - 1) * 100 if not lows.empty else math.nan
    return float(mfe), float(mae)


def build_events(
    snapshot: pd.DataFrame,
    manifest: dict[str, Any],
    *,
    price_loader: Callable[[str], tuple[pd.DataFrame, Path, str]],
    source_signal_snapshot_path: str,
    source_signal_snapshot_sha256: str,
    source_tdcc_manifest_path: str,
    source_tdcc_manifest_sha256: str,
) -> tuple[pd.DataFrame, list[dict[str, str]]]:
    event_rows: list[dict[str, Any]] = []
    price_cache: dict[str, tuple[pd.DataFrame, Path, str]] = {}
    evaluated_prices: dict[str, dict[str, str]] = {}

    for _, source_row in snapshot.iterrows():
        pre_a, pre_b, pre_c = preliminary_rule_requirements(source_row)
        if not (pre_a or pre_b or pre_c):
            continue
        stock_id = normalize_stock_id(source_row.get("code"))
        if stock_id not in price_cache:
            price_cache[stock_id] = price_loader(stock_id)
        price, price_path, price_sha256 = price_cache[stock_id]
        evaluated_prices[stock_id] = {
            "stock_id": stock_id,
            "path": price_path.as_posix(),
            "sha256": price_sha256,
            "high_water_date": text_value(price["date"].max()) if not price.empty else "",
        }
        signal_date = normalize_date(source_row.get("signal_date"))
        signal_matches = price.index[price["date"].eq(signal_date)].tolist()
        if len(signal_matches) != 1:
            raise RuntimeError(
                f"prequalified signal date must occur exactly once in price history: {signal_date}:{stock_id}"
            )
        signal_index = int(signal_matches[0])
        price_row = price.iloc[signal_index]
        bb_pct = number(price_row.get("bb_width_percentile_120d"))
        k_value = number(price_row.get("k_value"))
        d_value = number(price_row.get("d_value"))
        macd_hist = number(price_row.get("macd_hist"))
        missing_technical: list[str] = []
        if pre_a and not finite(bb_pct):
            missing_technical.append("bb_width_percentile_120d")
        if pre_b and (not finite(k_value) or not finite(d_value)):
            missing_technical.append("k_value_or_d_value")
        if pre_c and not finite(macd_hist):
            missing_technical.append("macd_hist")
        if missing_technical:
            raise RuntimeError(
                "prequalified selector inputs are unavailable for "
                f"{signal_date}:{stock_id}: {sorted(set(missing_technical))}"
            )
        matches = matched_rule_ids(
            source_row,
            bb_width_percentile_120d=bb_pct,
            k_value=k_value,
            d_value=d_value,
            macd_hist=macd_hist,
        )
        if not matches:
            continue

        signal_event_key = f"{signal_date}:{stock_id}"
        signal_close = number(price_row.get("close"))
        source_row_sha256 = canonical_row_sha256(source_row)
        price_high_water = text_value(price["date"].max())
        for scenario_id, horizon in SCENARIOS:
            scenario_event_key = f"{signal_event_key}:{scenario_id}"
            entry_index = signal_index + 1
            exit_index = signal_index + horizon
            invalid_reasons: list[str] = []
            entry_date = ""
            entry_price = math.nan
            exit_date = ""
            exit_price = math.nan
            if entry_index >= len(price):
                invalid_reasons.append("right_censored_entry")
            else:
                entry_date = text_value(price.iloc[entry_index].get("date"))
                entry_price = number(price.iloc[entry_index].get("open"))
                if not finite(entry_price):
                    invalid_reasons.append("missing_entry_open")
            if exit_index >= len(price):
                invalid_reasons.append("right_censored_exit")
            else:
                exit_date = text_value(price.iloc[exit_index].get("date"))
                exit_price = number(price.iloc[exit_index].get("close"))
                if not finite(exit_price):
                    invalid_reasons.append("missing_exit_close")
            return_valid = not invalid_reasons
            realized_return = (
                ((exit_price / entry_price) - 1) * 100 if return_valid else math.nan
            )
            if return_valid and realized_return > 0:
                outcome = "win"
            elif return_valid and realized_return < 0:
                outcome = "loss"
            elif return_valid:
                outcome = "neutral"
            else:
                outcome = "pending_or_invalid"
            mfe, mae = _advisory_path_metrics(
                price,
                signal_index=signal_index,
                horizon=horizon,
                entry_price=entry_price,
            )
            anomaly_candidate = bool(
                return_valid and abs(realized_return) >= ANOMALY_TRIGGER_THRESHOLD_PCT
            )
            anomaly_id = (
                f"{scenario_event_key}:{ANOMALY_TRIGGER_ID}" if anomaly_candidate else ""
            )
            event_rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    "model_id": MODEL_ID,
                    "signal_event_key": signal_event_key,
                    "scenario_event_key": scenario_event_key,
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "stock_name": text_value(source_row.get("name")),
                    "market_regime": text_value(source_row.get("market_regime")) or "unknown",
                    "benchmark_index": text_value(source_row.get("benchmark_index")),
                    "source_signal_id": text_value(source_row.get("signal_id")),
                    "source_signal_row_sha256": source_row_sha256,
                    "source_tdcc_dataset_id": text_value(manifest.get("dataset_id")),
                    "source_tdcc_dataset_hash": text_value(manifest.get("dataset_hash")),
                    "source_tdcc_manifest_path": source_tdcc_manifest_path,
                    "source_tdcc_manifest_sha256": source_tdcc_manifest_sha256,
                    "source_signal_snapshot_path": source_signal_snapshot_path,
                    "source_signal_snapshot_sha256": source_signal_snapshot_sha256,
                    "source_price_path": price_path.as_posix(),
                    "source_price_sha256": price_sha256,
                    "source_price_high_water_date": price_high_water,
                    "selector_contract_sha256": SELECTOR_CONTRACT_SHA256,
                    "matched_rule_ids": "|".join(matches),
                    "matched_rule_count": len(matches),
                    "rule_a_matched": RULE_A in matches,
                    "rule_b_matched": RULE_B in matches,
                    "rule_c_matched": RULE_C in matches,
                    "rule_membership_overlap": len(matches) > 1,
                    "tdcc_price_phase": text_value(source_row.get("tdcc_price_phase")),
                    "overheat_bucket": text_value(source_row.get("overheat_bucket")),
                    "is_all_thresholds": bool_value(source_row.get("is_all_thresholds")),
                    "tdcc_consecutive_up_weeks": number(source_row.get("tdcc_consecutive_up_weeks")),
                    "price_ret_1w_pct": number(source_row.get("price_ret_1w")),
                    "price_ret_2w_pct": number(source_row.get("price_ret_2w")),
                    "bb_width_percentile_120d": bb_pct,
                    "k_value": k_value,
                    "d_value": d_value,
                    "macd_hist": macd_hist,
                    "signal_close_price": signal_close,
                    "scenario_id": scenario_id,
                    "horizon_trading_days_after_signal": horizon,
                    "entry_rule_id": ENTRY_RULE_ID,
                    "entry_date": entry_date,
                    "entry_price": entry_price,
                    "exit_rule_id": f"signal_dplus_{horizon}_close",
                    "exit_date": exit_date,
                    "exit_price": exit_price,
                    "stop_rule_id": STOP_RULE_ID,
                    "return_formula": "(signal_DplusN_close/next_trading_day_open-1)*100",
                    "return_valid": return_valid,
                    "invalid_reason": "|".join(invalid_reasons),
                    "realized_return_pct": realized_return,
                    "return_outcome": outcome,
                    "high_return_hit": bool(return_valid and realized_return >= HIGH_RETURN_THRESHOLD_PCT),
                    "loss_flag": bool(return_valid and realized_return < 0),
                    "mfe_pct_advisory": mfe,
                    "mae_pct_advisory": mae,
                    "intraday_metrics_role": "advisory_path_diagnostic_only",
                    "intraday_metrics_formal_use": False,
                    "same_stock_overlap_candidate": False,
                    "same_stock_overlap_policy": "flag_only_no_exclusion_no_formal_policy",
                    "anomaly_candidate": anomaly_candidate,
                    "anomaly_candidate_ids": anomaly_id,
                    "anomaly_disposition": (
                        "unresolved_anomaly_candidate" if anomaly_candidate else "not_applicable"
                    ),
                    "primary_metric_included": return_valid,
                    "unresolved_candidate_retained_in_primary": anomaly_candidate,
                    "price_adjustment_basis_status": "not_formally_verified",
                    "pit_exact_replay": False,
                    "pit_replay_status": PIT_STATUS,
                    "formal_operation_contract_defined": False,
                    "formal_use": False,
                    "approved_for_daily": False,
                    "production_selector_change": False,
                    "promotion_eligible": False,
                    "promotion_blocked": True,
                    "promotion_block_reason": PROMOTION_BLOCK_REASON,
                    "_signal_index": signal_index,
                    "_expected_interval_start": signal_index + 1,
                    "_expected_interval_end": signal_index + horizon,
                }
            )

    work = pd.DataFrame(event_rows)
    if work.empty:
        return pd.DataFrame(columns=EVENT_COLUMNS), list(evaluated_prices.values())
    for (_, _), index_values in work.groupby(["scenario_id", "stock_id"], sort=False).groups.items():
        indexes = list(index_values)
        for left_position, left_index in enumerate(indexes):
            left = work.loc[left_index]
            for right_index in indexes[left_position + 1 :]:
                right = work.loc[right_index]
                intervals_overlap = max(
                    int(left["_expected_interval_start"]), int(right["_expected_interval_start"])
                ) <= min(int(left["_expected_interval_end"]), int(right["_expected_interval_end"]))
                if intervals_overlap:
                    work.loc[[left_index, right_index], "same_stock_overlap_candidate"] = True
    work = work.drop(
        columns=["_signal_index", "_expected_interval_start", "_expected_interval_end"]
    )
    work = work[EVENT_COLUMNS].sort_values(
        ["signal_date", "stock_id", "horizon_trading_days_after_signal"]
    ).reset_index(drop=True)
    if work["scenario_event_key"].duplicated().any():
        raise RuntimeError("union replay emitted duplicate scenario_event_key rows")
    return work, sorted(evaluated_prices.values(), key=lambda item: item["stock_id"])


def load_published_supplement(
    path: Path | None,
) -> tuple[pd.DataFrame, str, str, int]:
    internal_columns = [
        "scenario_id",
        "horizon_trading_days_after_signal",
        "signal_event_key",
        "scenario_event_key",
        "signal_date",
        "stock_id",
        "realized_return_pct",
        "return_valid",
        "return_outcome",
        "invalid_reason",
        "high_return_hit",
        "anomaly_candidate",
        "same_stock_overlap_candidate",
    ]
    if path is None or not path.exists():
        return pd.DataFrame(columns=internal_columns), "not_available", "", 0
    source = read_csv_str(path, "published ranking snapshot supplement")
    required = {
        "snapshot_report_date",
        "stock_id",
        "model_id",
        "trade_eligible",
        "forward_window_status",
        "return_d5_close_pct",
        "return_d10_close_pct",
    }
    require_columns(source, required, "published ranking snapshot supplement")
    target = source[source["model_id"].map(text_value).eq(MODEL_ID)].copy()
    if target.empty:
        return pd.DataFrame(columns=internal_columns), "present_no_target_rows", normalized_text_sha256(path), 0
    if target["trade_eligible"].map(bool_value).any():
        raise RuntimeError("published ranking supplement target rows must remain trade_eligible=False")
    target["snapshot_report_date"] = target["snapshot_report_date"].map(normalize_date)
    target["stock_id"] = target["stock_id"].map(normalize_stock_id)
    if target["snapshot_report_date"].eq("").any() or target["stock_id"].eq("").any():
        raise RuntimeError("published ranking supplement contains empty target-row identity")
    if target[["snapshot_report_date", "stock_id"]].duplicated().any():
        raise RuntimeError("published ranking supplement target rows must be unique by report date + stock")
    rows: list[dict[str, Any]] = []
    for _, row in target.iterrows():
        signal_date = normalize_date(row.get("snapshot_report_date"))
        stock_id = normalize_stock_id(row.get("stock_id"))
        for scenario_id, horizon in SCENARIOS:
            realized_return = number(row.get(f"return_d{horizon}_close_pct"))
            # The shared status can be partial when D+5 is mature but D+10 is not.
            # Each supplementary horizon is therefore mature only from its own return field.
            return_valid = finite(realized_return)
            if return_valid and realized_return > 0:
                outcome = "win"
            elif return_valid and realized_return < 0:
                outcome = "loss"
            elif return_valid:
                outcome = "neutral"
            else:
                outcome = "pending_or_invalid"
            signal_event_key = f"published:{signal_date}:{stock_id}"
            rows.append(
                {
                    "scenario_id": scenario_id,
                    "horizon_trading_days_after_signal": horizon,
                    "signal_event_key": signal_event_key,
                    "scenario_event_key": f"{signal_event_key}:{scenario_id}",
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "realized_return_pct": realized_return,
                    "return_valid": return_valid,
                    "return_outcome": outcome,
                    "invalid_reason": "" if return_valid else "published_horizon_not_mature",
                    "high_return_hit": bool(
                        return_valid and realized_return >= HIGH_RETURN_THRESHOLD_PCT
                    ),
                    "anomaly_candidate": bool(
                        return_valid and abs(realized_return) >= ANOMALY_TRIGGER_THRESHOLD_PCT
                    ),
                    "same_stock_overlap_candidate": False,
                }
            )
    return (
        pd.DataFrame(rows, columns=internal_columns),
        "present_supplementary_unverified_selector_population",
        normalized_text_sha256(path),
        len(target),
    )


def _metric_row(
    part: pd.DataFrame,
    *,
    scenario_id: str,
    horizon: int,
    group_kind: str,
    group_value: str,
    group_overlap_policy: str,
    evidence_role: str,
    source_status: str,
) -> dict[str, Any]:
    valid_mask = part.get("return_valid", pd.Series(False, index=part.index)).map(bool_value)
    all_returns = pd.to_numeric(
        part.get("realized_return_pct", pd.Series(dtype=float)), errors="coerce"
    )
    valid = all_returns[valid_mask].dropna()
    outcomes = part.loc[valid.index, "return_outcome"].map(text_value) if not valid.empty else pd.Series(dtype=str)
    anomaly_mask = part.get("anomaly_candidate", pd.Series(False, index=part.index)).map(bool_value)
    sensitivity = all_returns[valid_mask & ~anomaly_mask].dropna()
    invalid_reasons = part.get("invalid_reason", pd.Series("", index=part.index)).map(text_value)
    right_censored_count = int((~valid_mask & invalid_reasons.str.contains("right_censored")).sum())
    non_right_censored_invalid_count = int((~valid_mask).sum()) - right_censored_count
    overlap_mask = part.get(
        "same_stock_overlap_candidate", pd.Series(False, index=part.index)
    ).map(bool_value)
    valid_count = int(len(valid))
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
    high_return_count = int((valid >= HIGH_RETURN_THRESHOLD_PCT).sum())
    anomaly_count = int(anomaly_mask.sum())
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "model_id": MODEL_ID,
        "scenario_id": scenario_id,
        "horizon_trading_days_after_signal": horizon,
        "group_kind": group_kind,
        "group_value": group_value,
        "group_overlap_policy": group_overlap_policy,
        "evidence_role": evidence_role,
        "source_status": source_status,
        "signal_event_count": int(len(part)),
        "valid_return_count": valid_count,
        "pending_or_invalid_count": int(len(part) - valid_count),
        "right_censored_count": right_censored_count,
        "non_right_censored_invalid_count": non_right_censored_invalid_count,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": (win_count / valid_count * 100) if valid_count else math.nan,
        "neutral_rate_pct": (neutral_count / valid_count * 100) if valid_count else math.nan,
        "loss_rate_pct": (loss_count / valid_count * 100) if valid_count else math.nan,
        "average_return_pct": float(valid.mean()) if valid_count else math.nan,
        "median_return_pct": float(valid.median()) if valid_count else math.nan,
        "minimum_return_pct": float(valid.min()) if valid_count else math.nan,
        "maximum_return_pct": float(valid.max()) if valid_count else math.nan,
        "high_return_threshold_pct": HIGH_RETURN_THRESHOLD_PCT,
        "high_return_hit_count": high_return_count,
        "high_return_hit_rate_pct": (
            high_return_count / valid_count * 100 if valid_count else math.nan
        ),
        "anomaly_candidate_count": anomaly_count,
        "unresolved_anomaly_candidate_count": anomaly_count,
        "same_stock_overlap_candidate_count": int(overlap_mask.sum()),
        "primary_metric_retains_unresolved_candidates": bool(
            evidence_role == "primary_exact_union_replay" and anomaly_count > 0
        ),
        "candidate_exclusion_sensitivity_valid_return_count": len(sensitivity),
        "candidate_exclusion_sensitivity_excluded_candidate_count": int(
            (valid_mask & anomaly_mask).sum()
        ),
        "candidate_exclusion_sensitivity_win_rate_pct": (
            float((sensitivity > 0).mean() * 100) if len(sensitivity) else math.nan
        ),
        "candidate_exclusion_sensitivity_average_return_pct": (
            float(sensitivity.mean()) if len(sensitivity) else math.nan
        ),
        "candidate_exclusion_sensitivity_median_return_pct": (
            float(sensitivity.median()) if len(sensitivity) else math.nan
        ),
        "sensitivity_is_corrected_primary": False,
        "sample_status": "descriptive_only" if valid_count else "no_mature_returns",
        "entry_rule_id": ENTRY_RULE_ID,
        "exit_rule_id": f"signal_dplus_{horizon}_close",
        "stop_rule_id": STOP_RULE_ID,
        "pit_replay_status": PIT_STATUS,
        "formal_operation_contract_defined": False,
        "formal_use": False,
        "approved_for_daily": False,
        "production_selector_change": False,
        "promotion_eligible": False,
        "promotion_blocked": True,
        "promotion_block_reason": PROMOTION_BLOCK_REASON,
    }


def _chronological_thirds(events: pd.DataFrame) -> dict[str, str]:
    dates = sorted(set(events.get("signal_date", pd.Series(dtype=str)).map(text_value)))
    if not dates:
        return {}
    names = ("early", "middle", "recent")
    return {
        date: names[min(2, int(position * 3 / len(dates)))]
        for position, date in enumerate(dates)
    }


def build_summary(
    events: pd.DataFrame,
    published: pd.DataFrame,
    *,
    published_status: str,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    date_thirds = _chronological_thirds(events)
    regimes = sorted(set(events.get("market_regime", pd.Series(dtype=str)).map(text_value))) or ["unknown"]
    for scenario_id, horizon in SCENARIOS:
        scenario = events[events.get("scenario_id", pd.Series(dtype=str)).eq(scenario_id)].copy()
        rows.append(
            _metric_row(
                scenario,
                scenario_id=scenario_id,
                horizon=horizon,
                group_kind="overall_union",
                group_value="all",
                group_overlap_policy="deduplicated_signal_date_stock_union",
                evidence_role="primary_exact_union_replay",
                source_status="canonical_sources_replayed_with_PIT_blocker",
            )
        )
        for rule_id in RULE_IDS:
            membership = scenario[
                scenario.get("matched_rule_ids", pd.Series(dtype=str))
                .map(text_value)
                .map(lambda value: rule_id in value.split("|") if value else False)
            ]
            rows.append(
                _metric_row(
                    membership,
                    scenario_id=scenario_id,
                    horizon=horizon,
                    group_kind="rule_membership_overlap_labeled",
                    group_value=rule_id,
                    group_overlap_policy="memberships_overlap_do_not_sum_as_union",
                    evidence_role="primary_exact_union_replay",
                    source_status="canonical_sources_replayed_with_PIT_blocker",
                )
            )
        for third in ("early", "middle", "recent"):
            third_part = scenario[
                scenario.get("signal_date", pd.Series(dtype=str)).map(date_thirds).eq(third)
            ]
            rows.append(
                _metric_row(
                    third_part,
                    scenario_id=scenario_id,
                    horizon=horizon,
                    group_kind="chronological_third",
                    group_value=third,
                    group_overlap_policy="mutually_exclusive_by_signal_date",
                    evidence_role="primary_exact_union_replay",
                    source_status="canonical_sources_replayed_with_PIT_blocker",
                )
            )
        for regime in regimes:
            regime_part = scenario[
                scenario.get("market_regime", pd.Series(dtype=str)).map(text_value).eq(regime)
            ]
            rows.append(
                _metric_row(
                    regime_part,
                    scenario_id=scenario_id,
                    horizon=horizon,
                    group_kind="market_regime",
                    group_value=regime,
                    group_overlap_policy="mutually_exclusive_source_label",
                    evidence_role="primary_exact_union_replay",
                    source_status="canonical_sources_replayed_with_PIT_blocker",
                )
            )
        published_part = published[
            published.get("scenario_id", pd.Series(dtype=str)).eq(scenario_id)
        ].copy()
        rows.append(
            _metric_row(
                published_part,
                scenario_id=scenario_id,
                horizon=horizon,
                group_kind="published_snapshot_supplementary",
                group_value="all_target_published_rows",
                group_overlap_policy="daily_published_rows_not_selector_union_events",
                evidence_role="supplementary_published_snapshot",
                source_status=published_status,
            )
        )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS).sort_values(
        ["scenario_id", "group_kind", "group_value"]
    ).reset_index(drop=True)


def _anomaly_row(
    row: pd.Series,
    *,
    evidence_role: str,
    metric_scope: str,
) -> dict[str, Any]:
    scenario_event_key = text_value(row.get("scenario_event_key"))
    candidate_id = text_value(row.get("anomaly_candidate_ids")) or (
        f"{scenario_event_key}:{ANOMALY_TRIGGER_ID}"
    )
    retained_in_primary = evidence_role == "primary_exact_union_replay"
    overlap = bool_value(row.get("same_stock_overlap_candidate", False))
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "model_id": MODEL_ID,
        "anomaly_candidate_id": candidate_id,
        "evidence_role": evidence_role,
        "metric_scope": metric_scope,
        "scenario_id": text_value(row.get("scenario_id")),
        "signal_event_key": text_value(row.get("signal_event_key")),
        "scenario_event_key": scenario_event_key,
        "signal_date": normalize_date(row.get("signal_date")),
        "stock_id": normalize_stock_id(row.get("stock_id")),
        "realized_return_pct": number(row.get("realized_return_pct")),
        "trigger_id": ANOMALY_TRIGGER_ID,
        "trigger_observed_abs_return_pct": abs(number(row.get("realized_return_pct"))),
        "trigger_threshold_pct": ANOMALY_TRIGGER_THRESHOLD_PCT,
        "trigger_is_classification": False,
        "identity_and_non_overlap_check_status": (
            "pending_formal_non_overlap_policy_overlap_flagged"
            if overlap
            else "identity_verified_formal_non_overlap_policy_undefined"
        ),
        "formal_entry_exit_stop_replay_check_status": (
            "research_fixed_horizon_replay_verified_formal_contract_absent"
        ),
        "pit_dates_and_trading_calendar_check_status": "pending_event_time_immutable_packet",
        "raw_source_lineage_and_immutable_hash_check_status": (
            "current_artifact_hashes_recorded_event_time_lineage_missing"
        ),
        "units_formula_and_adjustment_basis_check_status": "pending_adjustment_basis_audit",
        "authoritative_corporate_action_history_check_status": "not_investigated",
        "independent_source_corroboration_check_status": "not_investigated",
        "reproducible_evidence_reference_check_status": "artifact_hashes_recorded_case_packet_incomplete",
        "all_required_checks_complete": False,
        "final_disposition": "unresolved_anomaly_candidate",
        "retained_in_primary_metrics": retained_in_primary,
        "excluded_from_primary_metrics": False,
        "supplementary_metric_included": not retained_in_primary,
        "formal_use": False,
        "promotion_blocked": True,
        "investigation_note": (
            "numerical magnitude is an investigation trigger only; no data-error, "
            "non-comparable, or verified-real-extreme classification has been made"
        ),
    }


def build_anomaly_candidates(events: pd.DataFrame, published: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if not events.empty:
        primary = events[events["anomaly_candidate"].map(bool_value)]
        rows.extend(
            _anomaly_row(
                row,
                evidence_role="primary_exact_union_replay",
                metric_scope="primary_metrics_retained",
            )
            for _, row in primary.iterrows()
        )
    if not published.empty:
        supplementary = published[published["anomaly_candidate"].map(bool_value)]
        rows.extend(
            _anomaly_row(
                row,
                evidence_role="supplementary_published_snapshot",
                metric_scope="supplementary_metrics_only",
            )
            for _, row in supplementary.iterrows()
        )
    result = pd.DataFrame(rows, columns=ANOMALY_COLUMNS)
    if result.empty:
        return result
    if result["anomaly_candidate_id"].duplicated().any():
        raise RuntimeError("anomaly candidate ids must be unique")
    return result.sort_values(
        ["evidence_role", "signal_date", "stock_id", "scenario_id"]
    ).reset_index(drop=True)


def write_csv_frame(frame: pd.DataFrame, path: Path, columns: list[str]) -> None:
    if list(frame.columns) != columns:
        raise RuntimeError(f"artifact schema mismatch before write: {path.as_posix()}")
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding="utf-8", lineterminator="\n", na_rep="")


def key_set_sha256(frame: pd.DataFrame, key_columns: list[str]) -> str:
    require_columns(frame, set(key_columns), "artifact key set")
    keys = sorted(
        tuple(text_value(row.get(column, "")) for column in key_columns)
        for _, row in frame.iterrows()
    )
    return canonical_json_sha256(keys)


def build_manifest_frame(
    *,
    events: pd.DataFrame,
    summary: pd.DataFrame,
    anomaly: pd.DataFrame,
    outputs: OutputPaths,
    repo_root: Path,
    snapshot_path: Path,
    snapshot_sha256: str,
    snapshot_row_count: int,
    tdcc_manifest_path: Path,
    tdcc_manifest_sha256: str,
    tdcc_manifest: dict[str, Any],
    price_dir: Path,
    evaluated_prices: list[dict[str, str]],
    published_path: Path | None,
    published_sha256: str,
    published_status: str,
    published_target_row_count: int,
) -> pd.DataFrame:
    price_bundle = [
        {
            "stock_id": item["stock_id"],
            "path": item["path"],
            "sha256": item["sha256"],
        }
        for item in sorted(evaluated_prices, key=lambda value: value["stock_id"])
    ]
    price_high_water = max(
        [text_value(item.get("high_water_date")) for item in evaluated_prices] or [""]
    )
    overlap_signal_count = (
        events.loc[events["rule_membership_overlap"].map(bool_value), "signal_event_key"].nunique()
        if not events.empty
        else 0
    )
    valid_d5 = (
        events[
            events["scenario_id"].eq("fixed_d5_close")
            & events["return_valid"].map(bool_value)
        ].shape[0]
        if not events.empty
        else 0
    )
    valid_d10 = (
        events[
            events["scenario_id"].eq("fixed_d10_close")
            & events["return_valid"].map(bool_value)
        ].shape[0]
        if not events.empty
        else 0
    )
    row = {
        "schema_version": "tdcc_short_term_continuation_research_manifest_v1",
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "model_id": MODEL_ID,
        "producer_path": PRODUCER,
        "validator_path": VALIDATOR,
        "generated_at": datetime.now(ZoneInfo("Asia/Taipei")).strftime(
            "%Y-%m-%d %H:%M:%S Asia/Taipei"
        ),
        "selector_contract_sha256": SELECTOR_CONTRACT_SHA256,
        "selector_rule_ids": "|".join(RULE_IDS),
        "selector_union_policy": "A_or_B_or_C_deduplicated_by_signal_date_stock",
        "source_tdcc_dataset_id": text_value(tdcc_manifest.get("dataset_id")),
        "source_tdcc_dataset_hash": text_value(tdcc_manifest.get("dataset_hash")),
        "source_tdcc_manifest_path": display_path(tdcc_manifest_path, repo_root),
        "source_tdcc_manifest_sha256": tdcc_manifest_sha256,
        "source_signal_snapshot_path": display_path(snapshot_path, repo_root),
        "source_signal_snapshot_sha256": snapshot_sha256,
        "source_signal_snapshot_row_count": snapshot_row_count,
        "source_price_root": display_path(price_dir, repo_root),
        "evaluated_price_file_count": len(evaluated_prices),
        "evaluated_price_bundle_sha256": canonical_json_sha256(price_bundle),
        "source_price_high_water_date": price_high_water,
        "published_snapshot_path": (
            display_path(published_path, repo_root) if published_path is not None else ""
        ),
        "published_snapshot_sha256": published_sha256,
        "published_snapshot_status": published_status,
        "published_snapshot_role": PUBLISHED_ROLE,
        "published_snapshot_target_row_count": published_target_row_count,
        "events_artifact_path": display_path(outputs.events, repo_root),
        "events_artifact_sha256": normalized_text_sha256(outputs.events),
        "events_row_count": len(events),
        "events_key_set_sha256": key_set_sha256(events, ["scenario_event_key"]),
        "summary_artifact_path": display_path(outputs.summary, repo_root),
        "summary_artifact_sha256": normalized_text_sha256(outputs.summary),
        "summary_row_count": len(summary),
        "summary_key_set_sha256": key_set_sha256(
            summary, ["scenario_id", "group_kind", "group_value"]
        ),
        "anomaly_artifact_path": display_path(outputs.anomaly, repo_root),
        "anomaly_artifact_sha256": normalized_text_sha256(outputs.anomaly),
        "anomaly_row_count": len(anomaly),
        "anomaly_key_set_sha256": key_set_sha256(anomaly, ["anomaly_candidate_id"]),
        "union_signal_event_count": events["signal_event_key"].nunique() if not events.empty else 0,
        "scenario_event_count": len(events),
        "rule_membership_overlap_event_count": overlap_signal_count,
        "same_stock_overlap_candidate_count": (
            int(events["same_stock_overlap_candidate"].map(bool_value).sum())
            if not events.empty
            else 0
        ),
        "valid_d5_count": valid_d5,
        "valid_d10_count": valid_d10,
        "unresolved_anomaly_candidate_count": len(anomaly),
        "entry_rule_id": ENTRY_RULE_ID,
        "exit_rule_ids": "signal_dplus_5_close|signal_dplus_10_close",
        "stop_rule_id": STOP_RULE_ID,
        "operation_replay_semantics": (
            "signal close confirms membership; enter next trading day open; exit at signal D+5 "
            "or D+10 close; no stop; no intraday price is a realized operation price"
        ),
        "intraday_metric_role": "MFE_MAE_advisory_only_never_realized_return",
        "unresolved_candidates_primary_policy": (
            "retain_unresolved_candidates_in_primary_metrics; exclusion_is_sensitivity_only"
        ),
        "pit_replay_status": PIT_STATUS,
        "pit_replay_blocker": PIT_BLOCKER,
        "formal_operation_contract_defined": False,
        "formal_use": False,
        "approved_for_daily": False,
        "production_selector_change": False,
        "promotion_eligible": False,
        "promotion_blocked": True,
        "promotion_block_reason": PROMOTION_BLOCK_REASON,
    }
    return pd.DataFrame([row], columns=MANIFEST_COLUMNS)


def produce_artifacts(
    *,
    snapshot_path: Path,
    tdcc_manifest_path: Path,
    price_dir: Path,
    published_path: Path | None,
    output_dir: Path,
    repo_root: Path,
) -> OutputPaths:
    tdcc_manifest = load_tdcc_manifest(tdcc_manifest_path, repo_root=repo_root)
    snapshot = load_signal_snapshot(snapshot_path, tdcc_manifest)
    snapshot_sha256 = normalized_text_sha256(snapshot_path)
    tdcc_manifest_sha256 = normalized_text_sha256(tdcc_manifest_path)

    def price_loader(stock_id: str) -> tuple[pd.DataFrame, Path, str]:
        source_path = price_dir / f"{stock_id}.csv"
        if not source_path.exists():
            raise RuntimeError(f"required price history is missing: {source_path.as_posix()}")
        frame = load_price_frame(source_path, stock_id)
        recorded_path = Path(display_path(source_path, repo_root))
        return frame, recorded_path, normalized_text_sha256(source_path)

    events, evaluated_prices = build_events(
        snapshot,
        tdcc_manifest,
        price_loader=price_loader,
        source_signal_snapshot_path=display_path(snapshot_path, repo_root),
        source_signal_snapshot_sha256=snapshot_sha256,
        source_tdcc_manifest_path=display_path(tdcc_manifest_path, repo_root),
        source_tdcc_manifest_sha256=tdcc_manifest_sha256,
    )
    published, published_status, published_sha256, published_target_count = (
        load_published_supplement(published_path)
    )
    summary = build_summary(events, published, published_status=published_status)
    anomaly = build_anomaly_candidates(events, published)
    outputs = output_paths(output_dir)
    write_csv_frame(events, outputs.events, EVENT_COLUMNS)
    write_csv_frame(summary, outputs.summary, SUMMARY_COLUMNS)
    write_csv_frame(anomaly, outputs.anomaly, ANOMALY_COLUMNS)
    manifest = build_manifest_frame(
        events=events,
        summary=summary,
        anomaly=anomaly,
        outputs=outputs,
        repo_root=repo_root,
        snapshot_path=snapshot_path,
        snapshot_sha256=snapshot_sha256,
        snapshot_row_count=len(snapshot),
        tdcc_manifest_path=tdcc_manifest_path,
        tdcc_manifest_sha256=tdcc_manifest_sha256,
        tdcc_manifest=tdcc_manifest,
        price_dir=price_dir,
        evaluated_prices=evaluated_prices,
        published_path=published_path,
        published_sha256=published_sha256,
        published_status=published_status,
        published_target_row_count=published_target_count,
    )
    write_csv_frame(manifest, outputs.manifest, MANIFEST_COLUMNS)
    return outputs


def preflight_output_ownership(
    output_dir: Path,
    *,
    repo_root: Path,
    registry_path: Path | None = None,
) -> OutputPaths:
    outputs = output_paths(Path(output_dir))
    relative_paths: list[str] = []
    resolved_root = Path(repo_root).resolve()
    for path in (outputs.events, outputs.summary, outputs.manifest, outputs.anomaly):
        resolved = path.resolve()
        try:
            relative_paths.append(resolved.relative_to(resolved_root).as_posix())
        except ValueError as exc:
            raise RuntimeError(
                f"model-owned research output must remain under repository root: {resolved.as_posix()}"
            ) from exc
    rules = (
        load_ownership_rules(Path(registry_path))
        if registry_path is not None
        else load_ownership_rules()
    )
    errors = validate_changed_paths(MODEL_ID, PRODUCER, relative_paths, rules)
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise RuntimeError(f"model-owned artifact ownership preflight failed:\n{details}")
    return outputs


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description=(
            "Build model-owned TDCC short-term exact-edge research artifacts. "
            "All outputs remain formal_use=False."
        )
    )
    parser.add_argument(
        "--signal-snapshot",
        type=Path,
        default=repo_root / "output/history/tdcc_signals/tdcc_signal_snapshot.csv",
    )
    parser.add_argument(
        "--tdcc-manifest",
        type=Path,
        default=repo_root / "output/latest/tdcc_dataset_manifest_latest.json",
    )
    parser.add_argument(
        "--price-dir",
        type=Path,
        default=repo_root / "data/stock_price_history",
    )
    parser.add_argument(
        "--published-snapshot",
        type=Path,
        default=repo_root / "output/history/research/daily_published_snapshot_ranking_events.csv",
    )
    parser.add_argument(
        "--no-published-supplement",
        action="store_true",
        help="Do not read the optional published-ranking supplementary source.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repo_root / "output/latest/research_backtest",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    published_path = None if args.no_published_supplement else args.published_snapshot
    expected_outputs = preflight_output_ownership(
        args.output_dir,
        repo_root=repo_root,
    )
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        outputs = produce_artifacts(
            snapshot_path=args.signal_snapshot,
            tdcc_manifest_path=args.tdcc_manifest,
            price_dir=args.price_dir,
            published_path=published_path,
            output_dir=args.output_dir,
            repo_root=repo_root,
        )
    if outputs != expected_outputs:  # pragma: no cover - defensive invariant
        raise RuntimeError("produced artifact paths differ from ownership preflight")
    print(f"Saved: {outputs.events}")
    print(f"Saved: {outputs.summary}")
    print(f"Saved: {outputs.manifest}")
    print(f"Saved: {outputs.anomaly}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
