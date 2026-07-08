from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"

SOURCE_OVERLAP_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv"
)
SOURCE_FEATURE_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_feature_slice_analysis_detail_latest.csv"
)
SOURCE_RAW_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_detail_latest.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_feature_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_feature_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_feature_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_split_feature_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_split_feature_audit_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_split_feature_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_split_feature_audit_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_overlap_sensitivity"
FEATURE_SOURCE_RESEARCH_ID = "volume_range_breakout_v2_feature_slice_analysis"
RAW_SOURCE_RESEARCH_ID = "volume_range_breakout_v2_raw_market_rerun"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "feature_source_research_id",
    "feature_source_artifact_version",
    "raw_source_research_id",
    "raw_source_artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "split_group_id",
    "split_group_label",
    "feature_id",
    "feature_label",
    "feature_family",
    "condition_expression",
    "candidate_id",
    "candidate_label",
    "source_total_events",
    "source_non_overlap_events",
    "sample_size",
    "coverage_pct",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "high_return_ge10_count",
    "high_return_ge10_rate_pct",
    "loss_le_minus5_count",
    "loss_le_minus5_rate_pct",
    "success_with_feature_count",
    "failure_with_feature_count",
    "success_share_pct",
    "failure_share_pct",
    "success_minus_failure_share_pct",
    "failure_common_flag",
    "success_median_value",
    "failure_median_value",
    "success_minus_failure_median",
    "baseline_win_rate_pct",
    "baseline_loss_rate_pct",
    "baseline_avg_return_pct",
    "baseline_median_return_pct",
    "uplift_win_rate_pp",
    "uplift_loss_rate_pp",
    "uplift_avg_return_pct",
    "uplift_median_return_pct",
    "sample_status",
    "candidate_status",
    "decision_hint",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "feature_source_research_id",
    "feature_source_artifact_version",
    "raw_source_research_id",
    "raw_source_artifact_version",
    "advisory_status",
    "model_id",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "return_pct",
    "return_outcome",
    "exit_reason",
    "split_group_id",
    "split_group_label",
    "same_stock_non_overlap_included",
    "event_sequence_for_stock",
    "entry_price",
    "exit_price",
    "holding_days",
    "mfe_pct",
    "mae_pct",
    "off_60d_low_pct",
    "position_in_60d_range_pct",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "breakout_over_prev60_pct",
    "volume_ratio",
    "signal_return_1d_pct",
    "classification_id",
    "attack_method",
    "price_position_type",
    "consolidation_type",
    "risk_type",
    "candle_quality",
    "follow_through_type",
    "limit_up_like",
    "low_base_loose_flag",
    "low_base_strict_flag",
    "consolidated_any_flag",
    "locked_limit_up_flag",
    "overheat_flag",
    "anomaly_flag",
    "signal_open",
    "signal_high",
    "signal_low",
    "signal_close",
    "confirmation_close",
    "close_location_pct",
    "signal_body_return_pct",
    "confirm_vs_signal_close_pct",
    "hist_close",
    "hist_ma20",
    "hist_ma60",
    "hist_ma120",
    "hist_ema23",
    "hist_return_5d_pct",
    "hist_return_20d_pct",
    "hist_return_60d_pct",
    "hist_return_120d_pct",
    "hist_volume_ratio20",
    "dist_ma20_pct",
    "dist_ma60_pct",
    "dist_ma120_pct",
    "dist_ema23_pct",
    "dist_high20_pct",
    "dist_high60_pct",
    "dist_high120_pct",
    "dist_low60_pct",
    "dist_low120_pct",
    "close_gt_ma20",
    "close_gt_ma60",
    "close_gt_ma120",
    "ma20_gt_ma60",
    "ma60_gt_ma120",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
}


@dataclass(frozen=True)
class FeatureSpec:
    feature_id: str
    feature_label: str
    feature_family: str
    condition_expression: str
    mask_builder: Callable[[pd.DataFrame], pd.Series]


@dataclass(frozen=True)
class CandidateSpec:
    candidate_id: str
    candidate_label: str
    split_group_id: str
    condition_expression: str
    candidate_status: str
    decision_hint: str
    mask_builder: Callable[[pd.DataFrame], pd.Series]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def false_text() -> str:
    return "False"


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def bool_series(series: pd.Series) -> pd.Series:
    return series.map(boolish).fillna(False)


def bool_text_series(series: pd.Series) -> pd.Series:
    return bool_series(series).map(lambda value: "True" if value else "False")


def pct_round(value: float | int | None, digits: int = 4) -> float | str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    if math.isnan(number) or math.isinf(number):
        return ""
    return round(number, digits)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def source_artifact_version(df: pd.DataFrame, source_name: str) -> str:
    versions = sorted(set(df.get("artifact_version", pd.Series(dtype=str)).astype(str)))
    if len(versions) != 1:
        raise SystemExit(f"ERROR: {source_name} must have exactly one artifact_version; got {versions[:5]}")
    return versions[0]


def require_research_only(df: pd.DataFrame, source_name: str) -> None:
    values = set(df.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower())
    if not values <= {"false", "0", ""}:
        raise SystemExit(f"ERROR: {source_name} must remain approved_for_daily=False")
    readiness = set(df.get("production_readiness", pd.Series(dtype=str)).astype(str))
    if readiness and readiness != {PRODUCTION_READINESS}:
        raise SystemExit(f"ERROR: {source_name} must remain {PRODUCTION_READINESS}; got {readiness}")


def require_source_id(df: pd.DataFrame, expected: str, source_name: str) -> None:
    values = set(df.get("research_id", pd.Series(dtype=str)).astype(str))
    if values != {expected}:
        raise SystemExit(f"ERROR: {source_name} research_id must be {expected}; got {values}")


def numeric(df: pd.DataFrame, col: str) -> pd.Series:
    return pd.to_numeric(df.get(col, pd.Series("", index=df.index)), errors="coerce")


def normalize_date_text(value: Any) -> str:
    text = safe_str(value).replace("-", "").replace("/", "")
    if text.endswith(".0"):
        text = text[:-2]
    return text


def merge_sources() -> tuple[pd.DataFrame, str, str, str, int]:
    overlap = read_csv(SOURCE_OVERLAP_DETAIL_CSV)
    feature = read_csv(SOURCE_FEATURE_DETAIL_CSV)
    raw = read_csv(SOURCE_RAW_DETAIL_CSV)
    if overlap.empty or feature.empty or raw.empty:
        raise SystemExit("ERROR: source artifacts must not be empty")
    require_source_id(overlap, SOURCE_RESEARCH_ID, "overlap detail")
    require_source_id(feature, FEATURE_SOURCE_RESEARCH_ID, "feature detail")
    require_source_id(raw, RAW_SOURCE_RESEARCH_ID, "raw detail")
    require_research_only(overlap, "overlap detail")
    require_research_only(feature, "feature detail")
    require_research_only(raw, "raw detail")
    for name, frame in [("overlap", overlap), ("feature", feature), ("raw", raw)]:
        if frame["source_event_key"].duplicated().any():
            raise SystemExit(f"ERROR: {name} detail source_event_key must be unique")

    overlap_version = source_artifact_version(overlap, "overlap detail")
    feature_version = source_artifact_version(feature, "feature detail")
    raw_version = source_artifact_version(raw, "raw detail")
    source_total_events = len(overlap)

    included = overlap[bool_series(overlap["same_stock_non_overlap_included"])].copy()
    if included.empty:
        raise SystemExit("ERROR: same-stock non-overlap population is empty")

    feature_columns = [
        "source_event_key",
        "entry_price",
        "exit_price",
        "holding_days",
        "mfe_pct",
        "mae_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "breakout_over_prev60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "classification_id",
        "attack_method",
        "price_position_type",
        "candle_quality",
        "follow_through_type",
        "low_base_loose_flag",
        "low_base_strict_flag",
        "consolidated_any_flag",
        "locked_limit_up_flag",
        "overheat_flag",
        "anomaly_flag",
    ]
    feature_columns = [col for col in feature_columns if col in feature.columns]
    raw_columns = [
        "source_event_key",
        "signal_open",
        "signal_high",
        "signal_low",
        "signal_close",
        "confirmation_close",
    ]
    raw_columns = [col for col in raw_columns if col in raw.columns]
    detail = included.merge(feature[feature_columns], on="source_event_key", how="left", validate="one_to_one")
    detail = detail.merge(raw[raw_columns], on="source_event_key", how="left", validate="one_to_one")
    if len(detail) != len(included):
        raise SystemExit("ERROR: merged detail row count changed")
    missing_feature = detail.get("entry_price", pd.Series("", index=detail.index)).astype(str).eq("").sum()
    missing_raw = detail.get("signal_close", pd.Series("", index=detail.index)).astype(str).eq("").sum()
    if missing_feature or missing_raw:
        raise SystemExit(f"ERROR: source joins missing feature={missing_feature}, raw={missing_raw}")
    return detail, overlap_version, feature_version, raw_version, source_total_events


def load_price_row(stock_id: str, signal_date: str) -> dict[str, Any]:
    path = PRICE_HISTORY_DIR / f"{stock_id}.csv"
    if not path.exists():
        return {}
    price = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    if "date" not in price.columns:
        return {}
    price = price.copy()
    price["_date_key"] = price["date"].map(normalize_date_text)
    hit = price[price["_date_key"].eq(normalize_date_text(signal_date))]
    if hit.empty:
        return {}
    row = hit.iloc[-1]
    mapping = {
        "hist_close": "close",
        "hist_ma20": "ma20",
        "hist_ma60": "ma60",
        "hist_ma120": "ma120",
        "hist_ema23": "ema23",
        "hist_return_5d_pct": "return_5d",
        "hist_return_20d_pct": "return_20d",
        "hist_return_60d_pct": "return_60d",
        "hist_return_120d_pct": "return_120d",
        "hist_volume_ratio20": "volume_ratio",
        "dist_ma20_pct": "distance_to_ma20_pct",
        "dist_ma60_pct": "distance_to_ma60_pct",
        "dist_ma120_pct": "distance_to_ma120_pct",
        "dist_ema23_pct": "distance_to_ema23_pct",
        "dist_high20_pct": "distance_to_high_20_pct",
        "dist_high60_pct": "distance_to_high_60_pct",
        "dist_high120_pct": "distance_to_high_120_pct",
        "dist_low60_pct": "distance_to_low_60_pct",
        "dist_low120_pct": "distance_to_low_120_pct",
    }
    return {target: safe_str(row.get(source, "")) for target, source in mapping.items()}


def add_technical_history(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    cache: dict[tuple[str, str], dict[str, Any]] = {}
    for _, row in detail.iterrows():
        key = (safe_str(row.get("stock_id")), safe_str(row.get("signal_date")))
        if key not in cache:
            cache[key] = load_price_row(key[0], key[1])
        rows.append(cache[key])
    tech = pd.DataFrame(rows, index=detail.index)
    out = detail.join(tech)
    for col in [
        "signal_open",
        "signal_high",
        "signal_low",
        "signal_close",
        "confirmation_close",
        "hist_close",
        "hist_ma20",
        "hist_ma60",
        "hist_ma120",
        "hist_ema23",
    ]:
        out[col] = numeric(out, col)
    high_low = out["signal_high"] - out["signal_low"]
    out["close_location_pct"] = ((out["signal_close"] - out["signal_low"]) / high_low * 100.0).where(high_low != 0)
    out["signal_body_return_pct"] = (out["signal_close"] / out["signal_open"] - 1.0) * 100.0
    out["confirm_vs_signal_close_pct"] = (out["confirmation_close"] / out["signal_close"] - 1.0) * 100.0
    out["close_gt_ma20"] = (out["hist_close"] > out["hist_ma20"]).fillna(False).map(lambda value: "True" if value else "False")
    out["close_gt_ma60"] = (out["hist_close"] > out["hist_ma60"]).fillna(False).map(lambda value: "True" if value else "False")
    out["close_gt_ma120"] = (out["hist_close"] > out["hist_ma120"]).fillna(False).map(lambda value: "True" if value else "False")
    out["ma20_gt_ma60"] = (out["hist_ma20"] > out["hist_ma60"]).fillna(False).map(lambda value: "True" if value else "False")
    out["ma60_gt_ma120"] = (out["hist_ma60"] > out["hist_ma120"]).fillna(False).map(lambda value: "True" if value else "False")
    return out


def enrich_detail(detail: pd.DataFrame, versions: tuple[str, str, str], source_total_events: int, generated_at: str) -> pd.DataFrame:
    overlap_version, feature_version, raw_version = versions
    out = detail.copy()
    for col in [
        "return_pct",
        "entry_price",
        "exit_price",
        "holding_days",
        "mfe_pct",
        "mae_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "breakout_over_prev60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
    ]:
        out[col] = numeric(out, col)
    for col in [
        "limit_up_like",
        "low_base_loose_flag",
        "low_base_strict_flag",
        "consolidated_any_flag",
        "locked_limit_up_flag",
        "overheat_flag",
        "anomaly_flag",
        "same_stock_non_overlap_included",
    ]:
        out[col] = bool_text_series(out.get(col, pd.Series(False, index=out.index)))
    out = add_technical_history(out)
    low_base = bool_series(out["low_base_loose_flag"]) & bool_series(out["consolidated_any_flag"])
    out["split_group_id"] = low_base.map(
        lambda value: "low_base_consolidated" if value else "momentum_continuation"
    )
    out["split_group_label"] = out["split_group_id"].map(
        {
            "low_base_consolidated": "low-base and consolidated proxy",
            "momentum_continuation": "non-low-base momentum continuation",
        }
    )
    out["research_id"] = RESEARCH_ID
    out["artifact_version"] = ARTIFACT_VERSION
    out["source_research_id"] = SOURCE_RESEARCH_ID
    out["source_artifact_version"] = overlap_version
    out["feature_source_research_id"] = FEATURE_SOURCE_RESEARCH_ID
    out["feature_source_artifact_version"] = feature_version
    out["raw_source_research_id"] = RAW_SOURCE_RESEARCH_ID
    out["raw_source_artifact_version"] = raw_version
    out["advisory_status"] = ADVISORY_STATUS
    out["model_id"] = MODEL_ID
    out["approved_for_daily"] = false_text()
    out["production_readiness"] = PRODUCTION_READINESS
    out["generated_at"] = generated_at
    out.attrs["source_total_events"] = source_total_events
    return out


def group_masks(detail: pd.DataFrame) -> dict[str, pd.Series]:
    return {
        "baseline_non_overlap": pd.Series(True, index=detail.index),
        "low_base_consolidated": detail["split_group_id"].eq("low_base_consolidated"),
        "momentum_continuation": detail["split_group_id"].eq("momentum_continuation"),
    }


def group_label(group_id: str) -> str:
    return {
        "baseline_non_overlap": "same-stock non-overlap baseline",
        "low_base_consolidated": "low-base and consolidated proxy",
        "momentum_continuation": "non-low-base momentum continuation",
    }.get(group_id, group_id)


def feature_specs() -> list[FeatureSpec]:
    return [
        FeatureSpec("locked_limit_up", "locked or limit-up-like signal", "signal_candle", "locked_limit_up_flag OR limit_up_like", lambda d: bool_series(d["locked_limit_up_flag"]) | bool_series(d["limit_up_like"])),
        FeatureSpec("not_locked_limit_up", "not locked or limit-up-like", "signal_candle", "NOT locked_limit_up", lambda d: ~(bool_series(d["locked_limit_up_flag"]) | bool_series(d["limit_up_like"]))),
        FeatureSpec("non_consolidation", "non-consolidation label", "base_shape", "consolidation_type == non_consolidation", lambda d: d["consolidation_type"].astype(str).eq("non_consolidation")),
        FeatureSpec("long_consolidation", "long consolidation label", "base_shape", "consolidation_type == long_consolidation", lambda d: d["consolidation_type"].astype(str).eq("long_consolidation")),
        FeatureSpec("consolidated_any", "short or long consolidation label", "base_shape", "consolidated_any_flag", lambda d: bool_series(d["consolidated_any_flag"])),
        FeatureSpec("range20_gt25", "20d range width >25%", "base_width", "range_width_20_pct > 25", lambda d: numeric(d, "range_width_20_pct").gt(25)),
        FeatureSpec("range20_le15", "20d range width <=15%", "base_width", "range_width_20_pct <= 15", lambda d: numeric(d, "range_width_20_pct").le(15)),
        FeatureSpec("range60_gt60", "60d range width >60%", "base_width", "range_width_60_pct > 60", lambda d: numeric(d, "range_width_60_pct").gt(60)),
        FeatureSpec("range60_le35", "60d range width <=35%", "base_width", "range_width_60_pct <= 35", lambda d: numeric(d, "range_width_60_pct").le(35)),
        FeatureSpec("off60_le35", "off 60d low <=35%", "price_position", "off_60d_low_pct <= 35", lambda d: numeric(d, "off_60d_low_pct").le(35)),
        FeatureSpec("off60_gt60", "off 60d low >60%", "price_position", "off_60d_low_pct > 60", lambda d: numeric(d, "off_60d_low_pct").gt(60)),
        FeatureSpec("pos60_ge85", "60d range position >=85", "price_position", "position_in_60d_range_pct >= 85", lambda d: numeric(d, "position_in_60d_range_pct").ge(85)),
        FeatureSpec("volume_2_to_6", "volume ratio 2 to 6", "volume", "2 <= volume_ratio <= 6", lambda d: numeric(d, "volume_ratio").between(2, 6, inclusive="both")),
        FeatureSpec("volume_gt6", "volume ratio >6", "volume", "volume_ratio > 6", lambda d: numeric(d, "volume_ratio").gt(6)),
        FeatureSpec("signal_ret_5_to_10", "signal return 5% to 10%", "signal_candle", "5 <= signal_return_1d_pct <= 10", lambda d: numeric(d, "signal_return_1d_pct").between(5, 10, inclusive="both")),
        FeatureSpec("signal_ret_ge9", "signal return >=9%", "signal_candle", "signal_return_1d_pct >= 9", lambda d: numeric(d, "signal_return_1d_pct").ge(9)),
        FeatureSpec("close_loc_ge80", "signal close location >=80%", "signal_candle", "close_location_pct >= 80", lambda d: numeric(d, "close_location_pct").ge(80)),
        FeatureSpec("close_loc_ge95", "signal close location >=95%", "signal_candle", "close_location_pct >= 95", lambda d: numeric(d, "close_location_pct").ge(95)),
        FeatureSpec("confirm_gain_ge3", "confirmation close >= signal close +3%", "confirmation", "confirm_vs_signal_close_pct >= 3", lambda d: numeric(d, "confirm_vs_signal_close_pct").ge(3)),
        FeatureSpec("confirm_gain_ge7", "confirmation close >= signal close +7%", "confirmation", "confirm_vs_signal_close_pct >= 7", lambda d: numeric(d, "confirm_vs_signal_close_pct").ge(7)),
        FeatureSpec("not_overheat", "not overheat proxy", "risk", "NOT overheat_flag", lambda d: ~bool_series(d["overheat_flag"])),
        FeatureSpec("overheat", "overheat proxy", "risk", "overheat_flag", lambda d: bool_series(d["overheat_flag"])),
        FeatureSpec("close_gt_ma20", "signal close > MA20", "technical_ma", "hist_close > hist_ma20", lambda d: bool_series(d["close_gt_ma20"])),
        FeatureSpec("close_gt_ma60", "signal close > MA60", "technical_ma", "hist_close > hist_ma60", lambda d: bool_series(d["close_gt_ma60"])),
        FeatureSpec("close_gt_ma120", "signal close > MA120", "technical_ma", "hist_close > hist_ma120", lambda d: bool_series(d["close_gt_ma120"])),
        FeatureSpec("ma20_gt_ma60", "MA20 > MA60", "technical_ma", "hist_ma20 > hist_ma60", lambda d: bool_series(d["ma20_gt_ma60"])),
        FeatureSpec("ma60_gt_ma120", "MA60 > MA120", "technical_ma", "hist_ma60 > hist_ma120", lambda d: bool_series(d["ma60_gt_ma120"])),
        FeatureSpec("ret20_0_to_25", "20d return 0% to 25%", "technical_return", "0 <= hist_return_20d_pct <= 25", lambda d: numeric(d, "hist_return_20d_pct").between(0, 25, inclusive="both")),
        FeatureSpec("ret20_gt25", "20d return >25%", "technical_return", "hist_return_20d_pct > 25", lambda d: numeric(d, "hist_return_20d_pct").gt(25)),
        FeatureSpec("ret60_gt40", "60d return >40%", "technical_return", "hist_return_60d_pct > 40", lambda d: numeric(d, "hist_return_60d_pct").gt(40)),
        FeatureSpec("dist_ma20_0_to_20", "distance to MA20 0% to 20%", "technical_ma", "0 <= dist_ma20_pct <= 20", lambda d: numeric(d, "dist_ma20_pct").between(0, 20, inclusive="both")),
        FeatureSpec("dist_ma20_gt20", "distance to MA20 >20%", "technical_ma", "dist_ma20_pct > 20", lambda d: numeric(d, "dist_ma20_pct").gt(20)),
        FeatureSpec("dist_ma60_gt30", "distance to MA60 >30%", "technical_ma", "dist_ma60_pct > 30", lambda d: numeric(d, "dist_ma60_pct").gt(30)),
        FeatureSpec("near_20d_high", "close within 1% of previous 20d high", "technical_breakout", "dist_high20_pct >= -1", lambda d: numeric(d, "dist_high20_pct").ge(-1)),
        FeatureSpec("near_60d_high", "close within 1% of previous 60d high", "technical_breakout", "dist_high60_pct >= -1", lambda d: numeric(d, "dist_high60_pct").ge(-1)),
        FeatureSpec("near_120d_high", "close within 1% of previous 120d high", "technical_breakout", "dist_high120_pct >= -1", lambda d: numeric(d, "dist_high120_pct").ge(-1)),
        FeatureSpec("locked_and_wide20", "locked and 20d range >25%", "combined", "locked_limit_up AND range_width_20_pct > 25", lambda d: (bool_series(d["locked_limit_up_flag"]) | bool_series(d["limit_up_like"])) & numeric(d, "range_width_20_pct").gt(25)),
        FeatureSpec("locked_and_non_consolidation", "locked and non-consolidation", "combined", "locked_limit_up AND non_consolidation", lambda d: (bool_series(d["locked_limit_up_flag"]) | bool_series(d["limit_up_like"])) & d["consolidation_type"].astype(str).eq("non_consolidation")),
        FeatureSpec("non_consolidation_and_wide20", "non-consolidation and 20d range >25%", "combined", "non_consolidation AND range_width_20_pct > 25", lambda d: d["consolidation_type"].astype(str).eq("non_consolidation") & numeric(d, "range_width_20_pct").gt(25)),
    ]


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = numeric(part, "return_pct").dropna()
    sample_size = int(len(returns))
    if sample_size == 0:
        return {
            "sample_size": 0,
            "win_count": 0,
            "neutral_count": 0,
            "loss_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "loss_rate_pct": "",
            "avg_return_pct": "",
            "median_return_pct": "",
            "p10_return_pct": "",
            "p90_return_pct": "",
            "high_return_ge10_count": 0,
            "high_return_ge10_rate_pct": "",
            "loss_le_minus5_count": 0,
            "loss_le_minus5_rate_pct": "",
        }
    outcomes = part["return_outcome"].astype(str).str.lower()
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
    high_count = int(returns.ge(10).sum())
    bad_count = int(returns.le(-5).sum())
    return {
        "sample_size": sample_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct_round(win_count / sample_size * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral_count / sample_size * 100.0, 2),
        "loss_rate_pct": pct_round(loss_count / sample_size * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
        "high_return_ge10_count": high_count,
        "high_return_ge10_rate_pct": pct_round(high_count / sample_size * 100.0, 2),
        "loss_le_minus5_count": bad_count,
        "loss_le_minus5_rate_pct": pct_round(bad_count / sample_size * 100.0, 2),
    }


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    if sample_size >= 30:
        return "thin_sample"
    if sample_size > 0:
        return "very_thin_sample"
    return "insufficient_sample"


def base_row(
    row_type: str,
    split_group_id: str,
    detail: pd.DataFrame,
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> dict[str, Any]:
    overlap_version, feature_version, raw_version = versions
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": overlap_version,
        "feature_source_research_id": FEATURE_SOURCE_RESEARCH_ID,
        "feature_source_artifact_version": feature_version,
        "raw_source_research_id": RAW_SOURCE_RESEARCH_ID,
        "raw_source_artifact_version": raw_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "split_group_id": split_group_id,
        "split_group_label": group_label(split_group_id),
        "source_total_events": source_total_events,
        "source_non_overlap_events": len(detail),
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def add_metric_uplift(row: dict[str, Any], baseline: dict[str, Any]) -> None:
    for src, target in [
        ("win_rate_pct", "uplift_win_rate_pp"),
        ("loss_rate_pct", "uplift_loss_rate_pp"),
        ("avg_return_pct", "uplift_avg_return_pct"),
        ("median_return_pct", "uplift_median_return_pct"),
    ]:
        try:
            row[target] = pct_round(float(row.get(src) or 0.0) - float(baseline.get(src) or 0.0), 4)
        except (TypeError, ValueError):
            row[target] = ""
    row["baseline_win_rate_pct"] = baseline.get("win_rate_pct", "")
    row["baseline_loss_rate_pct"] = baseline.get("loss_rate_pct", "")
    row["baseline_avg_return_pct"] = baseline.get("avg_return_pct", "")
    row["baseline_median_return_pct"] = baseline.get("median_return_pct", "")


def feature_row(
    row_type: str,
    group_id: str,
    spec: FeatureSpec,
    sub: pd.DataFrame,
    mask: pd.Series,
    detail: pd.DataFrame,
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
    group_baseline: dict[str, Any],
) -> dict[str, Any]:
    selected = sub[mask.reindex(sub.index).fillna(False)]
    wins = sub[sub["return_outcome"].astype(str).str.lower().eq("win")]
    losses = sub[sub["return_outcome"].astype(str).str.lower().eq("loss")]
    success_with = int(mask.reindex(wins.index).fillna(False).sum()) if len(wins) else 0
    failure_with = int(mask.reindex(losses.index).fillna(False).sum()) if len(losses) else 0
    success_share = success_with / len(wins) * 100.0 if len(wins) else math.nan
    failure_share = failure_with / len(losses) * 100.0 if len(losses) else math.nan
    row = base_row(row_type, group_id, detail, generated_at, versions, source_total_events)
    row.update(return_metrics(selected))
    row["feature_id"] = spec.feature_id
    row["feature_label"] = spec.feature_label
    row["feature_family"] = spec.feature_family
    row["condition_expression"] = spec.condition_expression
    row["coverage_pct"] = pct_round(len(selected) / len(sub) * 100.0 if len(sub) else math.nan, 2)
    row["success_with_feature_count"] = success_with
    row["failure_with_feature_count"] = failure_with
    row["success_share_pct"] = pct_round(success_share, 2)
    row["failure_share_pct"] = pct_round(failure_share, 2)
    row["success_minus_failure_share_pct"] = pct_round(success_share - failure_share, 2)
    row["failure_common_flag"] = "True" if failure_share >= 60.0 else "False"
    row["sample_status"] = sample_status(int(row["sample_size"]))
    add_metric_uplift(row, group_baseline)
    diff = float(row.get("success_minus_failure_share_pct") or 0.0)
    if success_share >= 60.0 and failure_share >= 60.0 and abs(diff) < 10.0:
        row["decision_hint"] = "common_in_success_and_failure_do_not_use_alone"
    elif diff >= 10:
        row["decision_hint"] = "more_common_in_success_research_signal"
    elif diff <= -10:
        row["decision_hint"] = "more_common_in_failure_risk_signal"
    else:
        row["decision_hint"] = "weak_or_mixed_feature_difference"
    row["candidate_status"] = "research_only_diagnostic"
    row["note"] = "feature share always includes failure_share_pct to prevent win-rate-only interpretation"
    return row


def build_group_baselines(
    detail: pd.DataFrame,
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    baselines: dict[str, dict[str, Any]] = {}
    masks = group_masks(detail)
    for group_id, mask in masks.items():
        sub = detail[mask.fillna(False)].copy()
        row = base_row("group_baseline", group_id, detail, generated_at, versions, source_total_events)
        row.update(return_metrics(sub))
        row["coverage_pct"] = pct_round(len(sub) / len(detail) * 100.0 if len(detail) else math.nan, 2)
        row["sample_status"] = sample_status(int(row["sample_size"]))
        row["candidate_status"] = "baseline_reference"
        row["decision_hint"] = "same_stock_non_overlap_reference"
        if group_id == "low_base_consolidated":
            row["note"] = "low-base proxy must be compared against failures before becoming any gate"
        elif group_id == "momentum_continuation":
            row["note"] = "momentum complement of low-base consolidated proxy"
        else:
            row["note"] = "baseline excludes same-stock overlapping active windows"
        baselines[group_id] = row.copy()
        rows.append(row)
    return rows, baselines


def add_feature_comparison_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    baselines: dict[str, dict[str, Any]],
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> None:
    specs = feature_specs()
    masks = group_masks(detail)
    for group_id in ["low_base_consolidated", "momentum_continuation"]:
        sub = detail[masks[group_id]].copy()
        if sub.empty:
            continue
        min_n = max(8, int(len(sub) * 0.05))
        computed = []
        for spec in specs:
            mask = spec.mask_builder(detail).fillna(False)
            selected_count = int(mask.reindex(sub.index).fillna(False).sum())
            if selected_count < min_n:
                continue
            computed.append(
                feature_row(
                    "feature_candidate_pool",
                    group_id,
                    spec,
                    sub,
                    mask,
                    detail,
                    generated_at,
                    versions,
                    source_total_events,
                    baselines[group_id],
                )
            )
        frame = pd.DataFrame(computed)
        if frame.empty:
            continue
        frame["_success_share"] = pd.to_numeric(frame["success_share_pct"], errors="coerce")
        frame["_failure_share"] = pd.to_numeric(frame["failure_share_pct"], errors="coerce")
        frame["_abs_diff"] = pd.to_numeric(frame["success_minus_failure_share_pct"], errors="coerce").abs()
        for _, item in frame.sort_values(["_success_share", "sample_size"], ascending=[False, False]).head(12).iterrows():
            row = item.drop(labels=[c for c in item.index if c.startswith("_")]).to_dict()
            row["row_type"] = "success_common_feature"
            rows.append(row)
        for _, item in frame.sort_values(["_failure_share", "sample_size"], ascending=[False, False]).head(12).iterrows():
            row = item.drop(labels=[c for c in item.index if c.startswith("_")]).to_dict()
            row["row_type"] = "failure_common_feature"
            rows.append(row)
        for _, item in frame.sort_values(["_abs_diff", "sample_size"], ascending=[False, False]).head(16).iterrows():
            row = item.drop(labels=[c for c in item.index if c.startswith("_")]).to_dict()
            row["row_type"] = "discriminative_feature"
            rows.append(row)


def candidate_specs() -> list[CandidateSpec]:
    return [
        CandidateSpec(
            "momentum_volume_control_wide20",
            "momentum + volume ratio 2..6 + 20d wide range",
            "momentum_continuation",
            "momentum_continuation AND 2 <= volume_ratio <= 6 AND range_width_20_pct > 25",
            "research_only_candidate",
            "best_current_direction_but_not_production_gate",
            lambda d: d["split_group_id"].eq("momentum_continuation")
            & numeric(d, "volume_ratio").between(2, 6, inclusive="both")
            & numeric(d, "range_width_20_pct").gt(25),
        ),
        CandidateSpec(
            "momentum_locked_wide_nonconsolidation",
            "momentum + locked + wide 20d + non-consolidation",
            "momentum_continuation",
            "momentum_continuation AND locked_limit_up AND range_width_20_pct > 25 AND non_consolidation",
            "research_only_candidate",
            "possible_momentum_continuation_semantic_not_low_base",
            lambda d: d["split_group_id"].eq("momentum_continuation")
            & (bool_series(d["locked_limit_up_flag"]) | bool_series(d["limit_up_like"]))
            & numeric(d, "range_width_20_pct").gt(25)
            & d["consolidation_type"].astype(str).eq("non_consolidation"),
        ),
        CandidateSpec(
            "momentum_close_loc95_volume2to6",
            "momentum + close at top 95% + volume ratio 2..6",
            "momentum_continuation",
            "momentum_continuation AND close_location_pct >= 95 AND 2 <= volume_ratio <= 6",
            "research_only_candidate",
            "technical_signal_quality_candidate",
            lambda d: d["split_group_id"].eq("momentum_continuation")
            & numeric(d, "close_location_pct").ge(95)
            & numeric(d, "volume_ratio").between(2, 6, inclusive="both"),
        ),
        CandidateSpec(
            "momentum_volume_gt6_overheat",
            "momentum + volume ratio >6",
            "momentum_continuation",
            "momentum_continuation AND volume_ratio > 6",
            "research_only_risk_tag_candidate",
            "overheat_risk_tag_candidate_not_buy_gate",
            lambda d: d["split_group_id"].eq("momentum_continuation") & numeric(d, "volume_ratio").gt(6),
        ),
        CandidateSpec(
            "lowbase_vol2to6_confirm3",
            "low-base + volume ratio 2..6 + confirmation gain >=3%",
            "low_base_consolidated",
            "low_base_consolidated AND 2 <= volume_ratio <= 6 AND confirm_vs_signal_close_pct >= 3",
            "research_only_candidate",
            "low_base_needs_more_evidence_currently_weak",
            lambda d: d["split_group_id"].eq("low_base_consolidated")
            & numeric(d, "volume_ratio").between(2, 6, inclusive="both")
            & numeric(d, "confirm_vs_signal_close_pct").ge(3),
        ),
        CandidateSpec(
            "lowbase_closehigh_confirm3",
            "low-base + close location >=80% + confirmation gain >=3%",
            "low_base_consolidated",
            "low_base_consolidated AND close_location_pct >= 80 AND confirm_vs_signal_close_pct >= 3",
            "rejected_as_hard_gate_candidate",
            "low_base_signal_still_common_in_failures",
            lambda d: d["split_group_id"].eq("low_base_consolidated")
            & numeric(d, "close_location_pct").ge(80)
            & numeric(d, "confirm_vs_signal_close_pct").ge(3),
        ),
        CandidateSpec(
            "lowbase_ma60_gt_ma120",
            "low-base + MA60 > MA120",
            "low_base_consolidated",
            "low_base_consolidated AND MA60 > MA120",
            "research_only_candidate",
            "weak_low_base_quality_filter_needs_followup",
            lambda d: d["split_group_id"].eq("low_base_consolidated") & bool_series(d["ma60_gt_ma120"]),
        ),
        CandidateSpec(
            "lowbase_off60_le35",
            "low-base and off 60d low <=35%",
            "low_base_consolidated",
            "low_base_consolidated AND off_60d_low_pct <= 35",
            "rejected_as_hard_gate_candidate",
            "deeper_low_position_performed_worse_in_current_evidence",
            lambda d: d["split_group_id"].eq("low_base_consolidated") & numeric(d, "off_60d_low_pct").le(35),
        ),
    ]


def add_candidate_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    baselines: dict[str, dict[str, Any]],
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> None:
    for spec in candidate_specs():
        mask = spec.mask_builder(detail).fillna(False)
        part = detail[mask].copy()
        row = base_row("candidate_condition_matrix", spec.split_group_id, detail, generated_at, versions, source_total_events)
        row.update(return_metrics(part))
        row["candidate_id"] = spec.candidate_id
        row["candidate_label"] = spec.candidate_label
        row["feature_id"] = spec.candidate_id
        row["feature_label"] = spec.candidate_label
        row["feature_family"] = "candidate_matrix"
        row["condition_expression"] = spec.condition_expression
        row["coverage_pct"] = pct_round(len(part) / len(detail) * 100.0 if len(detail) else math.nan, 2)
        row["sample_status"] = sample_status(int(row["sample_size"]))
        row["candidate_status"] = spec.candidate_status
        row["decision_hint"] = spec.decision_hint
        row["note"] = "research-only matrix row; not production ranking, scoring, or operation contract"
        add_metric_uplift(row, baselines[spec.split_group_id])
        rows.append(row)


def add_numeric_gap_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    baselines: dict[str, dict[str, Any]],
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> None:
    numeric_features = [
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "breakout_over_prev60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "close_location_pct",
        "signal_body_return_pct",
        "confirm_vs_signal_close_pct",
        "hist_return_5d_pct",
        "hist_return_20d_pct",
        "hist_return_60d_pct",
        "hist_return_120d_pct",
        "hist_volume_ratio20",
        "dist_ma20_pct",
        "dist_ma60_pct",
        "dist_ma120_pct",
        "dist_ema23_pct",
        "dist_high20_pct",
        "dist_high60_pct",
        "dist_high120_pct",
        "dist_low60_pct",
        "dist_low120_pct",
        "mfe_pct",
        "mae_pct",
    ]
    for group_id in ["low_base_consolidated", "momentum_continuation"]:
        sub = detail[detail["split_group_id"].eq(group_id)]
        wins = sub[sub["return_outcome"].astype(str).str.lower().eq("win")]
        losses = sub[sub["return_outcome"].astype(str).str.lower().eq("loss")]
        group_rows = []
        for feature in numeric_features:
            win_values = numeric(wins, feature).dropna()
            loss_values = numeric(losses, feature).dropna()
            if len(win_values) < 10 or len(loss_values) < 10:
                continue
            success_median = float(win_values.median())
            failure_median = float(loss_values.median())
            group_rows.append(
                {
                    "feature": feature,
                    "success_median": success_median,
                    "failure_median": failure_median,
                    "diff": success_median - failure_median,
                    "abs_diff": abs(success_median - failure_median),
                }
            )
        for item in sorted(group_rows, key=lambda x: (x["abs_diff"], x["feature"]), reverse=True)[:12]:
            row = base_row("numeric_success_failure_gap", group_id, detail, generated_at, versions, source_total_events)
            row["feature_id"] = item["feature"]
            row["feature_label"] = item["feature"]
            row["feature_family"] = "numeric_technical_gap" if item["feature"].startswith(("hist_", "dist_")) else "numeric_gap"
            row["condition_expression"] = "win median minus failure median"
            row["sample_size"] = len(sub)
            row["success_median_value"] = pct_round(item["success_median"])
            row["failure_median_value"] = pct_round(item["failure_median"])
            row["success_minus_failure_median"] = pct_round(item["diff"])
            row["sample_status"] = sample_status(len(sub))
            row["candidate_status"] = "research_only_diagnostic"
            row["decision_hint"] = "numeric_success_failure_gap_for_feature_design"
            row["note"] = "numeric gap compares winners and failures under the same non-overlap population"
            add_metric_uplift(row, baselines[group_id])
            rows.append(row)


def add_anomaly_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> None:
    returns = numeric(detail, "return_pct").dropna()
    lower = float(returns.quantile(0.01))
    upper = float(returns.quantile(0.99))
    trimmed = detail[numeric(detail, "return_pct").between(lower, upper)].copy()
    row = base_row("anomaly_check", "baseline_non_overlap", detail, generated_at, versions, source_total_events)
    row.update(return_metrics(trimmed))
    row["feature_id"] = "trim_1pct_each_tail"
    row["feature_label"] = "trim 1pct each return tail"
    row["feature_family"] = "anomaly_check"
    row["condition_expression"] = f"{lower:.4f} <= return_pct <= {upper:.4f}"
    row["coverage_pct"] = pct_round(len(trimmed) / len(detail) * 100.0 if len(detail) else math.nan, 2)
    row["sample_status"] = sample_status(int(row["sample_size"]))
    row["candidate_status"] = "research_only_anomaly_sensitivity"
    row["decision_hint"] = "compare_with_untrimmed_before_discussing_promotion"
    row["note"] = f"trimmed sensitivity only; removed_rows={len(detail) - len(trimmed)}"
    rows.append(row)


def build_summary(
    detail: pd.DataFrame,
    generated_at: str,
    versions: tuple[str, str, str],
    source_total_events: int,
) -> pd.DataFrame:
    rows, baselines = build_group_baselines(detail, generated_at, versions, source_total_events)
    add_feature_comparison_rows(rows, detail, baselines, generated_at, versions, source_total_events)
    add_candidate_rows(rows, detail, baselines, generated_at, versions, source_total_events)
    add_numeric_gap_rows(rows, detail, baselines, generated_at, versions, source_total_events)
    add_anomaly_rows(rows, detail, generated_at, versions, source_total_events)
    return pd.DataFrame(rows)


def md_table(df: pd.DataFrame, cols: list[str], limit: int = 20) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, path: Path) -> None:
    baselines = summary[summary["row_type"].eq("group_baseline")].copy()
    candidates = summary[summary["row_type"].eq("candidate_condition_matrix")].copy()
    success = summary[summary["row_type"].eq("success_common_feature")].copy()
    failure = summary[summary["row_type"].eq("failure_common_feature")].copy()
    diff = summary[summary["row_type"].eq("discriminative_feature")].copy()
    for frame, col in [(success, "success_share_pct"), (failure, "failure_share_pct")]:
        frame["_sort"] = pd.to_numeric(frame[col], errors="coerce")
    diff["_sort"] = pd.to_numeric(diff["success_minus_failure_share_pct"], errors="coerce").abs()
    lines = [
        "# volume_range_breakout v2 split feature audit",
        "",
        "- status: research-only; this does not change production model conditions, ranking, scoring, registry, operation adapter, or PDF behavior.",
        "- source population: same-stock non-overlap rows from `volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv`.",
        "- purpose: split low-base/consolidated rows from momentum-continuation rows, then compare success common features, failure common features, discriminative feature gaps, and candidate condition matrix rows.",
        "- guardrail: success feature rows include `failure_share_pct` so a feature cannot be promoted from win-rate-only evidence.",
        "",
        "## Group Baselines",
        "",
    ]
    lines += md_table(
        baselines,
        [
            "split_group_id",
            "sample_size",
            "win_rate_pct",
            "neutral_rate_pct",
            "loss_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "loss_le_minus5_rate_pct",
        ],
    )
    lines += ["", "## Candidate Condition Matrix", ""]
    lines += md_table(
        candidates,
        [
            "candidate_id",
            "split_group_id",
            "sample_size",
            "win_rate_pct",
            "loss_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "candidate_status",
            "decision_hint",
        ],
        limit=30,
    )
    lines += ["", "## Success Common Features With Failure Check", ""]
    lines += md_table(
        success.sort_values("_sort", ascending=False),
        [
            "split_group_id",
            "feature_id",
            "sample_size",
            "win_rate_pct",
            "loss_rate_pct",
            "success_share_pct",
            "failure_share_pct",
            "failure_common_flag",
            "decision_hint",
        ],
        limit=30,
    )
    lines += ["", "## Failure Common Features", ""]
    lines += md_table(
        failure.sort_values("_sort", ascending=False),
        [
            "split_group_id",
            "feature_id",
            "sample_size",
            "win_rate_pct",
            "loss_rate_pct",
            "success_share_pct",
            "failure_share_pct",
            "decision_hint",
        ],
        limit=30,
    )
    lines += ["", "## Discriminative Feature Gaps", ""]
    lines += md_table(
        diff.sort_values("_sort", ascending=False),
        [
            "split_group_id",
            "feature_id",
            "success_share_pct",
            "failure_share_pct",
            "success_minus_failure_share_pct",
            "decision_hint",
        ],
        limit=30,
    )
    lines += [
        "",
        "## Promotion Boundary",
        "",
        "This artifact is diagnostic. Any hard gate, score, deduct item, risk tag, model split, operation contract, or PDF presentation change still requires a separate promotion review and production PR.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    detail_raw, overlap_version, feature_version, raw_version, source_total_events = merge_sources()
    versions = (overlap_version, feature_version, raw_version)
    detail = enrich_detail(detail_raw, versions, source_total_events, generated_at)
    forbidden = sorted((set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in detail: {forbidden}")
    summary = build_summary(detail, generated_at, versions, source_total_events)
    forbidden_summary = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden_summary:
        raise SystemExit(f"ERROR: forbidden production fields in summary: {forbidden_summary}")
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_markdown(summary, LATEST_MD)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
