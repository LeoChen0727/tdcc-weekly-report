from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


MODEL_ID = "tdcc_short_term_continuation_d5_d10"
RESEARCH_ID = "tdcc_short_term_continuation_d5_d10_exact_edge_replay"
ARTIFACT_VERSION = "tdcc_short_term_continuation_d5_d10_research_v1"
RULE_A = "phase_overheated_bb_normal_2w20_50_tdcc1w"
RULE_B = "phase_overheated_kd_bull_not_hot_1w10_30_2w20_50"
RULE_C = "all_thresholds_overheated_1w10_30_macd_hist_pos"
RULE_IDS = (RULE_A, RULE_B, RULE_C)
SCENARIOS = (("fixed_d5_close", 5), ("fixed_d10_close", 10))
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

INDEPENDENT_SELECTOR_CONTRACT = {
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
        INDEPENDENT_SELECTOR_CONTRACT,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
).hexdigest()

EVENT_REQUIRED_COLUMNS = {
    "research_id",
    "artifact_version",
    "model_id",
    "signal_event_key",
    "scenario_event_key",
    "signal_date",
    "stock_id",
    "market_regime",
    "source_signal_id",
    "source_signal_row_sha256",
    "source_tdcc_dataset_id",
    "source_tdcc_dataset_hash",
    "source_tdcc_manifest_sha256",
    "source_signal_snapshot_sha256",
    "source_price_sha256",
    "selector_contract_sha256",
    "matched_rule_ids",
    "matched_rule_count",
    "rule_a_matched",
    "rule_b_matched",
    "rule_c_matched",
    "rule_membership_overlap",
    "bb_width_percentile_120d",
    "k_value",
    "d_value",
    "macd_hist",
    "scenario_id",
    "horizon_trading_days_after_signal",
    "entry_rule_id",
    "entry_date",
    "entry_price",
    "exit_rule_id",
    "exit_date",
    "exit_price",
    "stop_rule_id",
    "return_valid",
    "invalid_reason",
    "realized_return_pct",
    "return_outcome",
    "mfe_pct_advisory",
    "mae_pct_advisory",
    "intraday_metrics_formal_use",
    "same_stock_overlap_candidate",
    "anomaly_candidate",
    "anomaly_disposition",
    "primary_metric_included",
    "unresolved_candidate_retained_in_primary",
    "pit_exact_replay",
    "pit_replay_status",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
    "promotion_blocked",
    "promotion_block_reason",
}

SUMMARY_REQUIRED_COLUMNS = {
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
    "pit_replay_status",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
    "promotion_blocked",
    "promotion_block_reason",
}

ANOMALY_REQUIRED_COLUMNS = {
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
}

FALSE_ONLY_EVENT_FIELDS = {
    "intraday_metrics_formal_use",
    "pit_exact_replay",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
}
FALSE_ONLY_SUMMARY_FIELDS = {
    "sensitivity_is_corrected_primary",
    "formal_operation_contract_defined",
    "formal_use",
    "approved_for_daily",
    "production_selector_change",
    "promotion_eligible",
}


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
    raise RuntimeError(f"invalid boolean value: {value!r}")


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
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def canonical_row_sha256(row: pd.Series) -> str:
    return canonical_json_sha256(
        {str(column): text_value(row.get(column, "")) for column in sorted(row.index)}
    )


def display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def require_columns(frame: pd.DataFrame, required: set[str], label: str) -> None:
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"{label} missing required columns: {missing}")


def read_csv(path: Path, label: str) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"{label} is missing or empty: {path.as_posix()}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def false_only(frame: pd.DataFrame, fields: set[str], label: str) -> None:
    for field in fields:
        if set(frame[field].map(text_value)) != {"False"}:
            raise RuntimeError(f"{label}.{field} must remain false")


def key_set_sha256(frame: pd.DataFrame, columns: list[str]) -> str:
    keys = sorted(
        tuple(text_value(row.get(column, "")) for column in columns)
        for _, row in frame.iterrows()
    )
    return canonical_json_sha256(keys)


def _resolve_history_snapshot_path(
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
    if (
        resolved.parent != approved_root
        or resolved.name != f"tdcc_holder_ratio_{snapshot_date}.csv"
    ):
        raise RuntimeError(
            "canonical TDCC history snapshot path identity mismatch: "
            f"date={snapshot_date} path={path_text!r}"
        )
    if not resolved.is_file() or resolved.stat().st_size <= 0:
        raise RuntimeError(
            f"canonical TDCC history snapshot is missing or empty: {resolved.as_posix()}"
        )
    return resolved


def _verify_history_snapshot(
    item: dict[str, Any],
    *,
    snapshot_date: str,
    repo_root: Path,
) -> tuple[dict[str, Any], set[str]]:
    source_path = _resolve_history_snapshot_path(
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
    frame = read_csv(source_path, f"canonical TDCC history snapshot {snapshot_date}")
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


def load_source_manifest(path: Path, *, repo_root: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read canonical TDCC manifest: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError("canonical TDCC manifest must be an object")
    if value.get("status") != "pass" or value.get("schema_version") != TDCC_MANIFEST_SCHEMA:
        raise RuntimeError("canonical TDCC manifest must be a passing tdcc_dataset_manifest_v1")
    if text_value(value.get("hash_mode")) != TDCC_HASH_MODE:
        raise RuntimeError("canonical TDCC manifest hash_mode is invalid")
    if text_value(value.get("canonical_source_root")).replace("\\", "/") != (
        TDCC_HISTORY_RELATIVE_ROOT.as_posix()
    ):
        raise RuntimeError("canonical TDCC manifest source root is not approved")
    signal_date = normalize_date(value.get("signal_date"))
    dataset_id = text_value(value.get("dataset_id"))
    dataset_hash = text_value(value.get("dataset_hash")).lower()
    history_dates = [normalize_date(item) for item in value.get("history_dates", [])]
    required_dates = [normalize_date(item) for item in value.get("required_dates", [])]
    if len(signal_date) != 8:
        raise RuntimeError("canonical TDCC manifest identity is invalid")
    if not history_dates or history_dates != sorted(set(history_dates)) or history_dates[-1] != signal_date:
        raise RuntimeError("canonical TDCC manifest history_dates are invalid")
    if (
        not required_dates
        or required_dates != sorted(set(required_dates))
        or len(required_dates) > len(history_dates)
        or history_dates[-len(required_dates) :] != required_dates
        or required_dates[-1] != signal_date
    ):
        raise RuntimeError("canonical TDCC manifest required_dates are invalid")
    history_snapshots = value.get("history_snapshots", [])
    if not isinstance(history_snapshots, list) or int(value.get("history_snapshot_count", -1)) != len(history_snapshots):
        raise RuntimeError("canonical TDCC manifest history snapshot count is invalid")
    observed_dates = [
        normalize_date(item.get("date")) for item in history_snapshots if isinstance(item, dict)
    ]
    if observed_dates != history_dates or len(observed_dates) != len(history_snapshots):
        raise RuntimeError("canonical TDCC manifest history snapshots do not match history_dates")
    verified_results = [
        _verify_history_snapshot(
            item,
            snapshot_date=history_dates[index],
            repo_root=Path(repo_root),
        )
        for index, item in enumerate(history_snapshots)
        if isinstance(item, dict)
    ]
    if len(verified_results) != len(history_snapshots):
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


def load_source_snapshot(path: Path, manifest: dict[str, Any]) -> pd.DataFrame:
    frame = read_csv(path, "canonical TDCC signal snapshot")
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
        raise RuntimeError("canonical TDCC signal snapshot contains empty identity")
    if frame["signal_id"].eq("").any() or frame["signal_id"].duplicated().any():
        raise RuntimeError("canonical TDCC signal snapshot signal ids are invalid")
    if frame[["signal_date", "code"]].duplicated().any():
        raise RuntimeError("canonical TDCC signal snapshot has duplicate signal_date + code")
    if set(frame["source_tdcc_dataset_id"].map(text_value)) != {text_value(manifest["dataset_id"])}:
        raise RuntimeError("signal snapshot dataset id does not match canonical manifest")
    outside = set(frame["signal_date"]) - set(manifest["history_dates"])
    if outside:
        raise RuntimeError(f"signal snapshot dates are outside canonical history: {sorted(outside)[:10]}")
    return frame.sort_values(["signal_date", "code", "signal_id"]).reset_index(drop=True)


def load_price(path: Path, stock_id: str) -> pd.DataFrame:
    frame = read_csv(path, f"price history for {stock_id}")
    require_columns(frame, {"date", "open", "high", "low", "close"}, f"price history for {stock_id}")
    frame = frame.copy()
    frame["date"] = frame["date"].map(normalize_date)
    if frame["date"].eq("").any() or frame["date"].duplicated().any():
        raise RuntimeError(f"price history identity is invalid for {stock_id}")
    for column in ("open", "high", "low", "close"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
        if (frame[column].notna() & frame[column].le(0)).any():
            raise RuntimeError(f"price history contains non-positive {column} for {stock_id}")
    frame = frame.sort_values("date").reset_index(drop=True)
    close = frame["close"]
    ema12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
    ema26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
    dif = ema12 - ema26
    dea = dif.ewm(span=9, adjust=False, min_periods=9).mean()
    frame["macd_hist"] = dif - dea
    low9 = frame["low"].rolling(9, min_periods=9).min()
    high9 = frame["high"].rolling(9, min_periods=9).max()
    rsv = ((close - low9) / (high9 - low9) * 100).replace([np.inf, -np.inf], np.nan)
    frame["k_value"] = rsv.ewm(alpha=1 / 3, adjust=False, min_periods=1).mean()
    frame["d_value"] = frame["k_value"].ewm(alpha=1 / 3, adjust=False, min_periods=1).mean()
    ma20 = close.rolling(20, min_periods=20).mean()
    std20 = close.rolling(20, min_periods=20).std()
    width = ((ma20 + 2 * std20) - (ma20 - 2 * std20)) / ma20 * 100
    frame["bb_width_percentile_120d"] = width.rolling(120, min_periods=20).apply(
        lambda values: (values <= values[-1]).mean() * 100
        if not np.isnan(values[-1])
        else np.nan,
        raw=True,
    )
    return frame


def in_range(value: Any, lower: float, upper: float) -> bool:
    parsed = number(value)
    return finite(parsed) and lower <= parsed <= upper


def preliminary(row: pd.Series) -> tuple[bool, bool, bool]:
    phase = text_value(row.get("tdcc_price_phase"))
    return (
        phase == "overheated_after_tdcc"
        and in_range(row.get("price_ret_2w"), 20, 50)
        and number(row.get("tdcc_consecutive_up_weeks")) == 1,
        phase == "overheated_after_tdcc"
        and in_range(row.get("price_ret_1w"), 10, 30)
        and in_range(row.get("price_ret_2w"), 20, 50),
        bool_value(row.get("is_all_thresholds"))
        and text_value(row.get("overheat_bucket")) == "overheated"
        and in_range(row.get("price_ret_1w"), 10, 30),
    )


def independent_rule_membership(
    row: pd.Series,
    bb_pct: float,
    k_value: float,
    d_value: float,
    macd_hist: float,
) -> tuple[str, ...]:
    pre_a, pre_b, pre_c = preliminary(row)
    matched: list[str] = []
    if pre_a and finite(bb_pct) and 0 <= bb_pct <= 80:
        matched.append(RULE_A)
    if pre_b and finite(k_value) and finite(d_value) and k_value > d_value and k_value < 90:
        matched.append(RULE_B)
    if pre_c and finite(macd_hist) and macd_hist > 0:
        matched.append(RULE_C)
    return tuple(matched)


def path_metrics(price: pd.DataFrame, signal_index: int, horizon: int, entry: float) -> tuple[float, float]:
    exit_index = signal_index + horizon
    if not finite(entry) or signal_index + 1 >= len(price) or exit_index >= len(price):
        return math.nan, math.nan
    window = price.iloc[signal_index + 1 : exit_index + 1]
    highs = pd.to_numeric(window["high"], errors="coerce").dropna()
    lows = pd.to_numeric(window["low"], errors="coerce").dropna()
    mfe = (highs.max() / entry - 1) * 100 if not highs.empty else math.nan
    mae = (lows.min() / entry - 1) * 100 if not lows.empty else math.nan
    return float(mfe), float(mae)


def recompute_expected_events(
    snapshot: pd.DataFrame,
    manifest: dict[str, Any],
    *,
    snapshot_path: Path,
    manifest_path: Path,
    price_dir: Path,
    repo_root: Path,
) -> tuple[pd.DataFrame, list[dict[str, str]]]:
    rows: list[dict[str, Any]] = []
    cache: dict[str, tuple[pd.DataFrame, Path, str]] = {}
    price_records: dict[str, dict[str, str]] = {}
    snapshot_sha = normalized_text_sha256(snapshot_path)
    manifest_sha = normalized_text_sha256(manifest_path)
    for _, source_row in snapshot.iterrows():
        pre_a, pre_b, pre_c = preliminary(source_row)
        if not (pre_a or pre_b or pre_c):
            continue
        stock_id = normalize_stock_id(source_row.get("code"))
        if stock_id not in cache:
            price_path = price_dir / f"{stock_id}.csv"
            price = load_price(price_path, stock_id)
            cache[stock_id] = (price, price_path, normalized_text_sha256(price_path))
        price, price_path, price_sha = cache[stock_id]
        price_records[stock_id] = {
            "stock_id": stock_id,
            "path": display_path(price_path, repo_root),
            "sha256": price_sha,
            "high_water_date": text_value(price["date"].max()),
        }
        signal_date = normalize_date(source_row.get("signal_date"))
        indexes = price.index[price["date"].eq(signal_date)].tolist()
        if len(indexes) != 1:
            raise RuntimeError(f"prequalified signal date price match failed: {signal_date}:{stock_id}")
        signal_index = int(indexes[0])
        signal_price = price.iloc[signal_index]
        bb_pct = number(signal_price.get("bb_width_percentile_120d"))
        k_value = number(signal_price.get("k_value"))
        d_value = number(signal_price.get("d_value"))
        macd_hist = number(signal_price.get("macd_hist"))
        if (pre_a and not finite(bb_pct)) or (pre_b and not (finite(k_value) and finite(d_value))) or (pre_c and not finite(macd_hist)):
            raise RuntimeError(f"prequalified technical input is missing: {signal_date}:{stock_id}")
        matched = independent_rule_membership(source_row, bb_pct, k_value, d_value, macd_hist)
        if not matched:
            continue
        signal_key = f"{signal_date}:{stock_id}"
        for scenario_id, horizon in SCENARIOS:
            entry_index = signal_index + 1
            exit_index = signal_index + horizon
            reasons: list[str] = []
            entry_date = ""
            entry = math.nan
            exit_date = ""
            exit_price = math.nan
            if entry_index >= len(price):
                reasons.append("right_censored_entry")
            else:
                entry_date = text_value(price.iloc[entry_index].get("date"))
                entry = number(price.iloc[entry_index].get("open"))
                if not finite(entry):
                    reasons.append("missing_entry_open")
            if exit_index >= len(price):
                reasons.append("right_censored_exit")
            else:
                exit_date = text_value(price.iloc[exit_index].get("date"))
                exit_price = number(price.iloc[exit_index].get("close"))
                if not finite(exit_price):
                    reasons.append("missing_exit_close")
            valid = not reasons
            realized = (exit_price / entry - 1) * 100 if valid else math.nan
            outcome = (
                "win" if valid and realized > 0 else
                "loss" if valid and realized < 0 else
                "neutral" if valid else
                "pending_or_invalid"
            )
            mfe, mae = path_metrics(price, signal_index, horizon, entry)
            anomaly = bool(valid and abs(realized) >= ANOMALY_TRIGGER_THRESHOLD_PCT)
            scenario_key = f"{signal_key}:{scenario_id}"
            rows.append(
                {
                    "signal_event_key": signal_key,
                    "scenario_event_key": scenario_key,
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "market_regime": text_value(source_row.get("market_regime")) or "unknown",
                    "source_signal_id": text_value(source_row.get("signal_id")),
                    "source_signal_row_sha256": canonical_row_sha256(source_row),
                    "source_tdcc_dataset_id": text_value(manifest.get("dataset_id")),
                    "source_tdcc_dataset_hash": text_value(manifest.get("dataset_hash")),
                    "source_tdcc_manifest_sha256": manifest_sha,
                    "source_signal_snapshot_sha256": snapshot_sha,
                    "source_price_sha256": price_sha,
                    "selector_contract_sha256": SELECTOR_CONTRACT_SHA256,
                    "matched_rule_ids": "|".join(matched),
                    "matched_rule_count": len(matched),
                    "rule_a_matched": RULE_A in matched,
                    "rule_b_matched": RULE_B in matched,
                    "rule_c_matched": RULE_C in matched,
                    "rule_membership_overlap": len(matched) > 1,
                    "bb_width_percentile_120d": bb_pct,
                    "k_value": k_value,
                    "d_value": d_value,
                    "macd_hist": macd_hist,
                    "scenario_id": scenario_id,
                    "horizon_trading_days_after_signal": horizon,
                    "entry_date": entry_date,
                    "entry_price": entry,
                    "exit_date": exit_date,
                    "exit_price": exit_price,
                    "return_valid": valid,
                    "invalid_reason": "|".join(reasons),
                    "realized_return_pct": realized,
                    "return_outcome": outcome,
                    "mfe_pct_advisory": mfe,
                    "mae_pct_advisory": mae,
                    "anomaly_candidate": anomaly,
                    "anomaly_disposition": "unresolved_anomaly_candidate" if anomaly else "not_applicable",
                    "primary_metric_included": valid,
                    "unresolved_candidate_retained_in_primary": anomaly,
                    "same_stock_overlap_candidate": False,
                    "_interval_start": signal_index + 1,
                    "_interval_end": signal_index + horizon,
                }
            )
    expected = pd.DataFrame(rows)
    if expected.empty:
        return expected, sorted(price_records.values(), key=lambda item: item["stock_id"])
    for (_, _), indexes in expected.groupby(["scenario_id", "stock_id"], sort=False).groups.items():
        index_list = list(indexes)
        for left_position, left_index in enumerate(index_list):
            for right_index in index_list[left_position + 1 :]:
                left = expected.loc[left_index]
                right = expected.loc[right_index]
                if max(int(left["_interval_start"]), int(right["_interval_start"])) <= min(
                    int(left["_interval_end"]), int(right["_interval_end"])
                ):
                    expected.loc[[left_index, right_index], "same_stock_overlap_candidate"] = True
    expected = expected.drop(columns=["_interval_start", "_interval_end"])
    return expected, sorted(price_records.values(), key=lambda item: item["stock_id"])


def numeric_matches(actual: Any, expected: Any, tolerance: float = 1e-8) -> bool:
    actual_number = number(actual)
    expected_number = number(expected)
    if math.isnan(actual_number) and math.isnan(expected_number):
        return True
    if math.isnan(actual_number) or math.isnan(expected_number):
        return False
    return math.isclose(actual_number, expected_number, rel_tol=tolerance, abs_tol=tolerance)


def validate_events(actual: pd.DataFrame, expected: pd.DataFrame) -> None:
    require_columns(actual, EVENT_REQUIRED_COLUMNS, "events artifact")
    if actual["scenario_event_key"].duplicated().any():
        raise RuntimeError("events artifact scenario_event_key must be unique")
    if set(actual["research_id"].map(text_value)) != {RESEARCH_ID}:
        raise RuntimeError("events artifact research_id mismatch")
    if set(actual["artifact_version"].map(text_value)) != {ARTIFACT_VERSION}:
        raise RuntimeError("events artifact artifact_version mismatch")
    if set(actual["model_id"].map(text_value)) != {MODEL_ID}:
        raise RuntimeError("events artifact model_id mismatch")
    false_only(actual, FALSE_ONLY_EVENT_FIELDS, "events")
    if set(actual["promotion_blocked"].map(text_value)) != {"True"}:
        raise RuntimeError("events promotion_blocked must be true")
    if set(actual["promotion_block_reason"].map(text_value)) != {PROMOTION_BLOCK_REASON}:
        raise RuntimeError("events promotion_block_reason mismatch")
    expected_keys = set(expected.get("scenario_event_key", pd.Series(dtype=str)).map(text_value))
    actual_keys = set(actual["scenario_event_key"].map(text_value))
    if actual_keys != expected_keys:
        missing = sorted(expected_keys - actual_keys)[:10]
        extra = sorted(actual_keys - expected_keys)[:10]
        raise RuntimeError(f"events key set mismatch missing={missing} extra={extra}")
    if len(actual) != len(expected):
        raise RuntimeError("events row count differs from independent replay")
    scenario_counts = actual.groupby("signal_event_key")["scenario_id"].agg(
        lambda series: set(series.map(text_value))
    )
    required_scenarios = {item[0] for item in SCENARIOS}
    if any(value != required_scenarios for value in scenario_counts):
        raise RuntimeError("each union event must have exactly separate D+5 and D+10 scenario rows")

    actual_by_key = actual.set_index("scenario_event_key", drop=False)
    text_fields = [
        "signal_event_key",
        "signal_date",
        "stock_id",
        "market_regime",
        "source_signal_id",
        "source_signal_row_sha256",
        "source_tdcc_dataset_id",
        "source_tdcc_dataset_hash",
        "source_tdcc_manifest_sha256",
        "source_signal_snapshot_sha256",
        "source_price_sha256",
        "selector_contract_sha256",
        "matched_rule_ids",
        "scenario_id",
        "entry_date",
        "exit_date",
        "invalid_reason",
        "return_outcome",
        "anomaly_disposition",
    ]
    numeric_fields = [
        "matched_rule_count",
        "bb_width_percentile_120d",
        "k_value",
        "d_value",
        "macd_hist",
        "horizon_trading_days_after_signal",
        "entry_price",
        "exit_price",
        "realized_return_pct",
        "mfe_pct_advisory",
        "mae_pct_advisory",
    ]
    boolean_fields = [
        "rule_a_matched",
        "rule_b_matched",
        "rule_c_matched",
        "rule_membership_overlap",
        "return_valid",
        "same_stock_overlap_candidate",
        "anomaly_candidate",
        "primary_metric_included",
        "unresolved_candidate_retained_in_primary",
    ]
    for _, expected_row in expected.iterrows():
        key = text_value(expected_row["scenario_event_key"])
        actual_row = actual_by_key.loc[key]
        for field in text_fields:
            if text_value(actual_row.get(field)) != text_value(expected_row.get(field)):
                raise RuntimeError(f"events {field} mismatch for {key}")
        for field in numeric_fields:
            if not numeric_matches(actual_row.get(field), expected_row.get(field)):
                raise RuntimeError(f"events {field} mismatch for {key}")
        for field in boolean_fields:
            if bool_value(actual_row.get(field)) != bool_value(expected_row.get(field)):
                raise RuntimeError(f"events {field} mismatch for {key}")
        horizon = int(number(actual_row["horizon_trading_days_after_signal"]))
        if text_value(actual_row["entry_rule_id"]) != ENTRY_RULE_ID:
            raise RuntimeError(f"events entry rule is not next-open for {key}")
        if text_value(actual_row["exit_rule_id"]) != f"signal_dplus_{horizon}_close":
            raise RuntimeError(f"events fixed close exit mismatch for {key}")
        if text_value(actual_row["stop_rule_id"]) != STOP_RULE_ID:
            raise RuntimeError(f"events stop rule mismatch for {key}")
        if text_value(actual_row["pit_replay_status"]) != PIT_STATUS:
            raise RuntimeError(f"events PIT blocker status mismatch for {key}")
        if bool_value(actual_row["anomaly_candidate"]):
            if not text_value(actual_row.get("anomaly_candidate_ids")):
                raise RuntimeError(f"events anomaly id missing for {key}")
            if not bool_value(actual_row["primary_metric_included"]):
                raise RuntimeError(f"unresolved anomaly was removed from primary metrics for {key}")


def load_published_rows(path: Path | None) -> tuple[pd.DataFrame, str, str, int]:
    columns = [
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
        return pd.DataFrame(columns=columns), "not_available", "", 0
    source = read_csv(path, "published snapshot supplement")
    require_columns(
        source,
        {
            "snapshot_report_date",
            "stock_id",
            "model_id",
            "trade_eligible",
            "forward_window_status",
            "return_d5_close_pct",
            "return_d10_close_pct",
        },
        "published snapshot supplement",
    )
    target = source[source["model_id"].map(text_value).eq(MODEL_ID)].copy()
    if target.empty:
        return pd.DataFrame(columns=columns), "present_no_target_rows", normalized_text_sha256(path), 0
    if target["trade_eligible"].map(bool_value).any():
        raise RuntimeError("published supplement target rows must remain trade_eligible=False")
    target["snapshot_report_date"] = target["snapshot_report_date"].map(normalize_date)
    target["stock_id"] = target["stock_id"].map(normalize_stock_id)
    if target[["snapshot_report_date", "stock_id"]].duplicated().any():
        raise RuntimeError("published supplement target identity is duplicated")
    rows: list[dict[str, Any]] = []
    for _, row in target.iterrows():
        report_date = normalize_date(row.get("snapshot_report_date"))
        stock_id = normalize_stock_id(row.get("stock_id"))
        for scenario_id, horizon in SCENARIOS:
            realized = number(row.get(f"return_d{horizon}_close_pct"))
            # Independently respect horizon-specific maturity: partial rows may have D+5 only.
            valid = finite(realized)
            outcome = (
                "win" if valid and realized > 0 else
                "loss" if valid and realized < 0 else
                "neutral" if valid else
                "pending_or_invalid"
            )
            signal_key = f"published:{report_date}:{stock_id}"
            rows.append(
                {
                    "scenario_id": scenario_id,
                    "horizon_trading_days_after_signal": horizon,
                    "signal_event_key": signal_key,
                    "scenario_event_key": f"{signal_key}:{scenario_id}",
                    "signal_date": report_date,
                    "stock_id": stock_id,
                    "realized_return_pct": realized,
                    "return_valid": valid,
                    "return_outcome": outcome,
                    "invalid_reason": "" if valid else "published_horizon_not_mature",
                    "high_return_hit": bool(valid and realized >= HIGH_RETURN_THRESHOLD_PCT),
                    "anomaly_candidate": bool(
                        valid and abs(realized) >= ANOMALY_TRIGGER_THRESHOLD_PCT
                    ),
                    "same_stock_overlap_candidate": False,
                }
            )
    return (
        pd.DataFrame(rows, columns=columns),
        "present_supplementary_unverified_selector_population",
        normalized_text_sha256(path),
        len(target),
    )


def metric_expectations(part: pd.DataFrame, *, primary: bool) -> dict[str, Any]:
    valid_mask = part.get("return_valid", pd.Series(False, index=part.index)).map(bool_value)
    all_returns = pd.to_numeric(
        part.get("realized_return_pct", pd.Series(dtype=float)), errors="coerce"
    )
    valid = all_returns[valid_mask].dropna()
    outcomes = part.loc[valid.index, "return_outcome"].map(text_value) if not valid.empty else pd.Series(dtype=str)
    anomaly_count = int(
        part.get("anomaly_candidate", pd.Series(False, index=part.index)).map(bool_value).sum()
    )
    anomaly_mask = part.get(
        "anomaly_candidate", pd.Series(False, index=part.index)
    ).map(bool_value)
    sensitivity = all_returns[valid_mask & ~anomaly_mask].dropna()
    invalid_reasons = part.get("invalid_reason", pd.Series("", index=part.index)).map(text_value)
    right_censored_count = int((~valid_mask & invalid_reasons.str.contains("right_censored")).sum())
    overlap_count = int(
        part.get("same_stock_overlap_candidate", pd.Series(False, index=part.index))
        .map(bool_value)
        .sum()
    )
    valid_count = len(valid)
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
    high_return_count = int((valid >= HIGH_RETURN_THRESHOLD_PCT).sum())
    return {
        "signal_event_count": len(part),
        "valid_return_count": valid_count,
        "pending_or_invalid_count": len(part) - valid_count,
        "right_censored_count": right_censored_count,
        "non_right_censored_invalid_count": len(part) - valid_count - right_censored_count,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": win_count / valid_count * 100 if valid_count else math.nan,
        "neutral_rate_pct": neutral_count / valid_count * 100 if valid_count else math.nan,
        "loss_rate_pct": loss_count / valid_count * 100 if valid_count else math.nan,
        "average_return_pct": float(valid.mean()) if valid_count else math.nan,
        "median_return_pct": float(valid.median()) if valid_count else math.nan,
        "minimum_return_pct": float(valid.min()) if valid_count else math.nan,
        "maximum_return_pct": float(valid.max()) if valid_count else math.nan,
        "high_return_hit_count": high_return_count,
        "high_return_hit_rate_pct": high_return_count / valid_count * 100 if valid_count else math.nan,
        "anomaly_candidate_count": anomaly_count,
        "unresolved_anomaly_candidate_count": anomaly_count,
        "same_stock_overlap_candidate_count": overlap_count,
        "primary_metric_retains_unresolved_candidates": bool(primary and anomaly_count > 0),
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
    }


def chronological_thirds(events: pd.DataFrame) -> dict[str, str]:
    dates = sorted(set(events.get("signal_date", pd.Series(dtype=str)).map(text_value)))
    if not dates:
        return {}
    names = ("early", "middle", "recent")
    return {
        date: names[min(2, int(index * 3 / len(dates)))]
        for index, date in enumerate(dates)
    }


def expected_summary_groups(
    events: pd.DataFrame,
    published: pd.DataFrame,
    published_status: str,
) -> dict[tuple[str, str, str], dict[str, Any]]:
    groups: dict[tuple[str, str, str], dict[str, Any]] = {}
    thirds = chronological_thirds(events)
    regimes = sorted(set(events.get("market_regime", pd.Series(dtype=str)).map(text_value))) or ["unknown"]

    def register(
        part: pd.DataFrame,
        scenario_id: str,
        horizon: int,
        kind: str,
        value: str,
        overlap_policy: str,
        evidence_role: str,
        source_status: str,
    ) -> None:
        record = metric_expectations(part, primary=evidence_role == "primary_exact_union_replay")
        record.update(
            {
                "horizon_trading_days_after_signal": horizon,
                "group_overlap_policy": overlap_policy,
                "evidence_role": evidence_role,
                "source_status": source_status,
                "entry_rule_id": ENTRY_RULE_ID,
                "exit_rule_id": f"signal_dplus_{horizon}_close",
                "stop_rule_id": STOP_RULE_ID,
            }
        )
        groups[(scenario_id, kind, value)] = record

    for scenario_id, horizon in SCENARIOS:
        scenario = events[events.get("scenario_id", pd.Series(dtype=str)).eq(scenario_id)].copy()
        source_status = "canonical_sources_replayed_with_PIT_blocker"
        register(
            scenario,
            scenario_id,
            horizon,
            "overall_union",
            "all",
            "deduplicated_signal_date_stock_union",
            "primary_exact_union_replay",
            source_status,
        )
        for rule_id in RULE_IDS:
            part = scenario[
                scenario.get("matched_rule_ids", pd.Series(dtype=str))
                .map(text_value)
                .map(lambda value: rule_id in value.split("|") if value else False)
            ]
            register(
                part,
                scenario_id,
                horizon,
                "rule_membership_overlap_labeled",
                rule_id,
                "memberships_overlap_do_not_sum_as_union",
                "primary_exact_union_replay",
                source_status,
            )
        for third in ("early", "middle", "recent"):
            part = scenario[
                scenario.get("signal_date", pd.Series(dtype=str)).map(thirds).eq(third)
            ]
            register(
                part,
                scenario_id,
                horizon,
                "chronological_third",
                third,
                "mutually_exclusive_by_signal_date",
                "primary_exact_union_replay",
                source_status,
            )
        for regime in regimes:
            part = scenario[
                scenario.get("market_regime", pd.Series(dtype=str)).map(text_value).eq(regime)
            ]
            register(
                part,
                scenario_id,
                horizon,
                "market_regime",
                regime,
                "mutually_exclusive_source_label",
                "primary_exact_union_replay",
                source_status,
            )
        published_part = published[
            published.get("scenario_id", pd.Series(dtype=str)).eq(scenario_id)
        ]
        register(
            published_part,
            scenario_id,
            horizon,
            "published_snapshot_supplementary",
            "all_target_published_rows",
            "daily_published_rows_not_selector_union_events",
            "supplementary_published_snapshot",
            published_status,
        )
    return groups


def validate_summary(
    summary: pd.DataFrame,
    events: pd.DataFrame,
    published: pd.DataFrame,
    published_status: str,
) -> None:
    require_columns(summary, SUMMARY_REQUIRED_COLUMNS, "summary artifact")
    if summary[["scenario_id", "group_kind", "group_value"]].duplicated().any():
        raise RuntimeError("summary group keys must be unique")
    if set(summary["research_id"].map(text_value)) != {RESEARCH_ID}:
        raise RuntimeError("summary research_id mismatch")
    if set(summary["artifact_version"].map(text_value)) != {ARTIFACT_VERSION}:
        raise RuntimeError("summary artifact_version mismatch")
    if set(summary["model_id"].map(text_value)) != {MODEL_ID}:
        raise RuntimeError("summary model_id mismatch")
    false_only(summary, FALSE_ONLY_SUMMARY_FIELDS, "summary")
    if set(summary["promotion_blocked"].map(text_value)) != {"True"}:
        raise RuntimeError("summary promotion_blocked must be true")
    if set(summary["pit_replay_status"].map(text_value)) != {PIT_STATUS}:
        raise RuntimeError("summary PIT status mismatch")
    if set(summary["promotion_block_reason"].map(text_value)) != {PROMOTION_BLOCK_REASON}:
        raise RuntimeError("summary promotion_block_reason mismatch")
    expected = expected_summary_groups(events, published, published_status)
    actual_keys = set(
        zip(
            summary["scenario_id"].map(text_value),
            summary["group_kind"].map(text_value),
            summary["group_value"].map(text_value),
        )
    )
    if actual_keys != set(expected):
        raise RuntimeError("summary group set differs from independent aggregation")
    indexed = summary.set_index(["scenario_id", "group_kind", "group_value"], drop=False)
    numeric_fields = [
        "horizon_trading_days_after_signal",
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
        "high_return_hit_count",
        "high_return_hit_rate_pct",
        "anomaly_candidate_count",
        "unresolved_anomaly_candidate_count",
        "same_stock_overlap_candidate_count",
        "candidate_exclusion_sensitivity_valid_return_count",
        "candidate_exclusion_sensitivity_excluded_candidate_count",
        "candidate_exclusion_sensitivity_win_rate_pct",
        "candidate_exclusion_sensitivity_average_return_pct",
        "candidate_exclusion_sensitivity_median_return_pct",
    ]
    text_fields = [
        "group_overlap_policy",
        "evidence_role",
        "source_status",
        "entry_rule_id",
        "exit_rule_id",
        "stop_rule_id",
    ]
    for key, expected_row in expected.items():
        actual_row = indexed.loc[key]
        for field in numeric_fields:
            if not numeric_matches(actual_row.get(field), expected_row.get(field)):
                raise RuntimeError(f"summary {field} mismatch for {key}")
        for field in text_fields:
            if text_value(actual_row.get(field)) != text_value(expected_row.get(field)):
                raise RuntimeError(f"summary {field} mismatch for {key}")
        if bool_value(actual_row["primary_metric_retains_unresolved_candidates"]) != bool(
            expected_row["primary_metric_retains_unresolved_candidates"]
        ):
            raise RuntimeError(f"summary anomaly retention mismatch for {key}")
        if bool_value(actual_row["sensitivity_is_corrected_primary"]):
            raise RuntimeError(f"summary sensitivity cannot replace corrected primary for {key}")


def validate_anomaly(
    anomaly: pd.DataFrame,
    events: pd.DataFrame,
    published: pd.DataFrame,
) -> None:
    require_columns(anomaly, ANOMALY_REQUIRED_COLUMNS, "anomaly artifact")
    if anomaly["anomaly_candidate_id"].duplicated().any():
        raise RuntimeError("anomaly candidate ids must be unique")
    expected: dict[str, dict[str, Any]] = {}
    primary = events[events.get("anomaly_candidate", pd.Series(dtype=str)).map(bool_value)]
    for _, row in primary.iterrows():
        candidate_id = text_value(row.get("anomaly_candidate_ids"))
        expected[candidate_id] = {
            "evidence_role": "primary_exact_union_replay",
            "metric_scope": "primary_metrics_retained",
            "scenario_event_key": text_value(row.get("scenario_event_key")),
            "realized_return_pct": number(row.get("realized_return_pct")),
            "retained_in_primary_metrics": True,
            "supplementary_metric_included": False,
        }
    supplementary = published[
        published.get("anomaly_candidate", pd.Series(dtype=str)).map(bool_value)
    ]
    for _, row in supplementary.iterrows():
        scenario_key = text_value(row.get("scenario_event_key"))
        candidate_id = f"{scenario_key}:{ANOMALY_TRIGGER_ID}"
        expected[candidate_id] = {
            "evidence_role": "supplementary_published_snapshot",
            "metric_scope": "supplementary_metrics_only",
            "scenario_event_key": scenario_key,
            "realized_return_pct": number(row.get("realized_return_pct")),
            "retained_in_primary_metrics": False,
            "supplementary_metric_included": True,
        }
    if set(anomaly["anomaly_candidate_id"].map(text_value)) != set(expected):
        raise RuntimeError("anomaly candidate set differs from independent numerical triggers")
    if anomaly.empty:
        return
    if set(anomaly["research_id"].map(text_value)) != {RESEARCH_ID}:
        raise RuntimeError("anomaly research_id mismatch")
    if set(anomaly["artifact_version"].map(text_value)) != {ARTIFACT_VERSION}:
        raise RuntimeError("anomaly artifact_version mismatch")
    if set(anomaly["model_id"].map(text_value)) != {MODEL_ID}:
        raise RuntimeError("anomaly model_id mismatch")
    indexed = anomaly.set_index("anomaly_candidate_id", drop=False)
    for candidate_id, expected_row in expected.items():
        row = indexed.loc[candidate_id]
        for field in ("evidence_role", "metric_scope", "scenario_event_key"):
            if text_value(row.get(field)) != text_value(expected_row[field]):
                raise RuntimeError(f"anomaly {field} mismatch for {candidate_id}")
        if not numeric_matches(row.get("realized_return_pct"), expected_row["realized_return_pct"]):
            raise RuntimeError(f"anomaly return mismatch for {candidate_id}")
        if not numeric_matches(
            row.get("trigger_observed_abs_return_pct"),
            abs(float(expected_row["realized_return_pct"])),
        ):
            raise RuntimeError(f"anomaly trigger magnitude mismatch for {candidate_id}")
        if text_value(row.get("trigger_id")) != ANOMALY_TRIGGER_ID:
            raise RuntimeError(f"anomaly trigger id mismatch for {candidate_id}")
        if not numeric_matches(row.get("trigger_threshold_pct"), ANOMALY_TRIGGER_THRESHOLD_PCT):
            raise RuntimeError(f"anomaly threshold mismatch for {candidate_id}")
        for false_field in (
            "trigger_is_classification",
            "all_required_checks_complete",
            "excluded_from_primary_metrics",
            "formal_use",
        ):
            if bool_value(row.get(false_field)):
                raise RuntimeError(f"anomaly {false_field} must be false for {candidate_id}")
        if not bool_value(row.get("promotion_blocked")):
            raise RuntimeError(f"anomaly promotion must remain blocked for {candidate_id}")
        if text_value(row.get("final_disposition")) != "unresolved_anomaly_candidate":
            raise RuntimeError(f"anomaly final disposition must remain unresolved for {candidate_id}")
        if bool_value(row.get("retained_in_primary_metrics")) != bool(
            expected_row["retained_in_primary_metrics"]
        ):
            raise RuntimeError(f"anomaly primary retention mismatch for {candidate_id}")
        if bool_value(row.get("supplementary_metric_included")) != bool(
            expected_row["supplementary_metric_included"]
        ):
            raise RuntimeError(f"anomaly supplementary retention mismatch for {candidate_id}")
        for pending_field in (
            "identity_and_non_overlap_check_status",
            "formal_entry_exit_stop_replay_check_status",
            "pit_dates_and_trading_calendar_check_status",
            "raw_source_lineage_and_immutable_hash_check_status",
            "units_formula_and_adjustment_basis_check_status",
            "authoritative_corporate_action_history_check_status",
            "independent_source_corroboration_check_status",
            "reproducible_evidence_reference_check_status",
        ):
            if not text_value(row.get(pending_field)):
                raise RuntimeError(f"anomaly root-check status missing: {pending_field} {candidate_id}")


MANIFEST_REQUIRED_COLUMNS = {
    "schema_version",
    "research_id",
    "artifact_version",
    "model_id",
    "producer_path",
    "validator_path",
    "selector_contract_sha256",
    "selector_rule_ids",
    "selector_union_policy",
    "source_tdcc_dataset_id",
    "source_tdcc_dataset_hash",
    "source_tdcc_manifest_sha256",
    "source_signal_snapshot_sha256",
    "source_signal_snapshot_row_count",
    "evaluated_price_file_count",
    "evaluated_price_bundle_sha256",
    "source_price_high_water_date",
    "published_snapshot_sha256",
    "published_snapshot_status",
    "published_snapshot_role",
    "published_snapshot_target_row_count",
    "events_artifact_sha256",
    "events_row_count",
    "events_key_set_sha256",
    "summary_artifact_sha256",
    "summary_row_count",
    "summary_key_set_sha256",
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
}


def validate_manifest(
    manifest_frame: pd.DataFrame,
    *,
    events: pd.DataFrame,
    summary: pd.DataFrame,
    anomaly: pd.DataFrame,
    events_path: Path,
    summary_path: Path,
    anomaly_path: Path,
    snapshot_path: Path,
    snapshot_rows: int,
    tdcc_manifest_path: Path,
    tdcc_manifest: dict[str, Any],
    evaluated_prices: list[dict[str, str]],
    published_sha256: str,
    published_status: str,
    published_target_count: int,
) -> None:
    require_columns(manifest_frame, MANIFEST_REQUIRED_COLUMNS, "research manifest artifact")
    if len(manifest_frame) != 1:
        raise RuntimeError("research manifest artifact must contain exactly one row")
    row = manifest_frame.iloc[0]
    expected_text = {
        "schema_version": "tdcc_short_term_continuation_research_manifest_v1",
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "model_id": MODEL_ID,
        "producer_path": "scripts/build_tdcc_short_term_continuation_d5_d10_research.py",
        "validator_path": "scripts/validate_tdcc_short_term_continuation_d5_d10_research.py",
        "selector_contract_sha256": SELECTOR_CONTRACT_SHA256,
        "selector_rule_ids": "|".join(RULE_IDS),
        "selector_union_policy": "A_or_B_or_C_deduplicated_by_signal_date_stock",
        "source_tdcc_dataset_id": text_value(tdcc_manifest.get("dataset_id")),
        "source_tdcc_dataset_hash": text_value(tdcc_manifest.get("dataset_hash")),
        "source_tdcc_manifest_sha256": normalized_text_sha256(tdcc_manifest_path),
        "source_signal_snapshot_sha256": normalized_text_sha256(snapshot_path),
        "published_snapshot_sha256": published_sha256,
        "published_snapshot_status": published_status,
        "published_snapshot_role": PUBLISHED_ROLE,
        "events_artifact_sha256": normalized_text_sha256(events_path),
        "events_key_set_sha256": key_set_sha256(events, ["scenario_event_key"]),
        "summary_artifact_sha256": normalized_text_sha256(summary_path),
        "summary_key_set_sha256": key_set_sha256(
            summary, ["scenario_id", "group_kind", "group_value"]
        ),
        "anomaly_artifact_sha256": normalized_text_sha256(anomaly_path),
        "anomaly_key_set_sha256": key_set_sha256(anomaly, ["anomaly_candidate_id"]),
        "entry_rule_id": ENTRY_RULE_ID,
        "exit_rule_ids": "signal_dplus_5_close|signal_dplus_10_close",
        "stop_rule_id": STOP_RULE_ID,
        "pit_replay_status": PIT_STATUS,
        "pit_replay_blocker": PIT_BLOCKER,
        "promotion_block_reason": PROMOTION_BLOCK_REASON,
    }
    for field, expected in expected_text.items():
        if text_value(row.get(field)) != expected:
            raise RuntimeError(f"research manifest {field} mismatch")
    price_bundle = [
        {"stock_id": item["stock_id"], "path": item["path"], "sha256": item["sha256"]}
        for item in sorted(evaluated_prices, key=lambda value: value["stock_id"])
    ]
    expected_counts = {
        "source_signal_snapshot_row_count": snapshot_rows,
        "evaluated_price_file_count": len(evaluated_prices),
        "published_snapshot_target_row_count": published_target_count,
        "events_row_count": len(events),
        "summary_row_count": len(summary),
        "anomaly_row_count": len(anomaly),
        "union_signal_event_count": events["signal_event_key"].nunique() if not events.empty else 0,
        "scenario_event_count": len(events),
        "rule_membership_overlap_event_count": (
            events.loc[events["rule_membership_overlap"].map(bool_value), "signal_event_key"].nunique()
            if not events.empty else 0
        ),
        "same_stock_overlap_candidate_count": (
            int(events["same_stock_overlap_candidate"].map(bool_value).sum()) if not events.empty else 0
        ),
        "valid_d5_count": int(
            (events["scenario_id"].eq("fixed_d5_close") & events["return_valid"].map(bool_value)).sum()
        ) if not events.empty else 0,
        "valid_d10_count": int(
            (events["scenario_id"].eq("fixed_d10_close") & events["return_valid"].map(bool_value)).sum()
        ) if not events.empty else 0,
        "unresolved_anomaly_candidate_count": len(anomaly),
    }
    for field, expected in expected_counts.items():
        if int(number(row.get(field))) != int(expected):
            raise RuntimeError(f"research manifest {field} mismatch")
    if text_value(row.get("evaluated_price_bundle_sha256")) != canonical_json_sha256(price_bundle):
        raise RuntimeError("research manifest evaluated price bundle hash mismatch")
    expected_high_water = max(
        [text_value(item.get("high_water_date")) for item in evaluated_prices] or [""]
    )
    if text_value(row.get("source_price_high_water_date")) != expected_high_water:
        raise RuntimeError("research manifest price high-water date mismatch")
    if not text_value(row.get("operation_replay_semantics")):
        raise RuntimeError("research manifest operation replay semantics are missing")
    if text_value(row.get("intraday_metric_role")) != "MFE_MAE_advisory_only_never_realized_return":
        raise RuntimeError("research manifest intraday metric boundary mismatch")
    if text_value(row.get("unresolved_candidates_primary_policy")) != (
        "retain_unresolved_candidates_in_primary_metrics; exclusion_is_sensitivity_only"
    ):
        raise RuntimeError("research manifest unresolved-candidate retention policy mismatch")
    for field in (
        "formal_operation_contract_defined",
        "formal_use",
        "approved_for_daily",
        "production_selector_change",
        "promotion_eligible",
    ):
        if text_value(row.get(field)) != "False":
            raise RuntimeError(f"research manifest {field} must remain false")
    if text_value(row.get("promotion_blocked")) != "True":
        raise RuntimeError("research manifest promotion_blocked must remain true")


def validate_artifacts(
    *,
    events_path: Path,
    summary_path: Path,
    manifest_path: Path,
    anomaly_path: Path,
    snapshot_path: Path,
    tdcc_manifest_path: Path,
    price_dir: Path,
    published_path: Path | None,
    repo_root: Path,
) -> list[str]:
    try:
        events = read_csv(events_path, "events artifact")
        summary = read_csv(summary_path, "summary artifact")
        research_manifest = read_csv(manifest_path, "research manifest artifact")
        anomaly = read_csv(anomaly_path, "anomaly artifact")
        source_manifest = load_source_manifest(tdcc_manifest_path, repo_root=repo_root)
        snapshot = load_source_snapshot(snapshot_path, source_manifest)
        expected_events, evaluated_prices = recompute_expected_events(
            snapshot,
            source_manifest,
            snapshot_path=snapshot_path,
            manifest_path=tdcc_manifest_path,
            price_dir=price_dir,
            repo_root=repo_root,
        )
        validate_events(events, expected_events)
        published, published_status, published_sha256, published_target_count = load_published_rows(
            published_path
        )
        validate_summary(summary, events, published, published_status)
        validate_anomaly(anomaly, events, published)
        validate_manifest(
            research_manifest,
            events=events,
            summary=summary,
            anomaly=anomaly,
            events_path=events_path,
            summary_path=summary_path,
            anomaly_path=anomaly_path,
            snapshot_path=snapshot_path,
            snapshot_rows=len(snapshot),
            tdcc_manifest_path=tdcc_manifest_path,
            tdcc_manifest=source_manifest,
            evaluated_prices=evaluated_prices,
            published_sha256=published_sha256,
            published_status=published_status,
            published_target_count=published_target_count,
        )
    except Exception as exc:
        return [str(exc)]
    return []


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = repo_root / "output/latest/research_backtest"
    stem = "tdcc_short_term_continuation_d5_d10_research"
    parser = argparse.ArgumentParser(
        description=(
            "Independently recompute and validate TDCC short-term exact-edge research artifacts."
        )
    )
    parser.add_argument("--events", type=Path, default=output_dir / f"{stem}_events_latest.csv")
    parser.add_argument("--summary", type=Path, default=output_dir / f"{stem}_summary_latest.csv")
    parser.add_argument("--manifest", type=Path, default=output_dir / f"{stem}_manifest_latest.csv")
    parser.add_argument(
        "--anomaly-candidates",
        type=Path,
        default=output_dir / f"{stem}_anomaly_candidates_latest.csv",
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
        "--price-dir", type=Path, default=repo_root / "data/stock_price_history"
    )
    parser.add_argument(
        "--published-snapshot",
        type=Path,
        default=repo_root / "output/history/research/daily_published_snapshot_ranking_events.csv",
    )
    parser.add_argument("--no-published-supplement", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    errors = validate_artifacts(
        events_path=args.events,
        summary_path=args.summary,
        manifest_path=args.manifest,
        anomaly_path=args.anomaly_candidates,
        snapshot_path=args.signal_snapshot,
        tdcc_manifest_path=args.tdcc_manifest,
        price_dir=args.price_dir,
        published_path=None if args.no_published_supplement else args.published_snapshot,
        repo_root=repo_root,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: TDCC short-term D+5/D+10 research artifacts independently recomputed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
