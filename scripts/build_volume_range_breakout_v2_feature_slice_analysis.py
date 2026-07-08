from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RAW_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_detail_latest.csv"
SEMANTIC_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_feature_slice_analysis_latest.csv"
LATEST_SUMMARY_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_feature_slice_analysis_latest.md"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_feature_slice_analysis_detail_latest.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_feature_slice_analysis.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_feature_slice_analysis_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_feature_slice_analysis"
ARTIFACT_VERSION = "volume_range_breakout_v2_feature_slice_analysis_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_raw_market_rerun"
SEMANTIC_SOURCE_RESEARCH_ID = "volume_range_breakout_v2_semantic_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

RETURN_KEY = "return_pct"
HIGH_RETURN_Q = 0.80
LOW_RETURN_Q = 0.20

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "semantic_source_research_id",
    "semantic_source_artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "slice_family",
    "slice_id",
    "slice_label",
    "basis",
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
    "min_return_pct",
    "max_return_pct",
    "trim_sample_size",
    "trim_avg_return_pct",
    "trim_median_return_pct",
    "top20_count",
    "bottom20_count",
    "top20_share_pct",
    "bottom20_share_pct",
    "top_minus_bottom_share_pct",
    "overall_share_pct",
    "high_return_share_pct",
    "low_return_share_pct",
    "high_minus_low_share_pct",
    "numeric_overall_median",
    "numeric_top20_median",
    "numeric_bottom20_median",
    "numeric_top_minus_bottom_median",
    "sample_status",
    "decision_hint",
    "value_a",
    "value_b",
    "value_c",
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
    "semantic_source_research_id",
    "semantic_source_artifact_version",
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
    "top20_return_flag",
    "bottom20_return_flag",
    "entry_price",
    "exit_price",
    "exit_reason",
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
    "off_60d_low_bucket",
    "range_width_60_bucket",
    "range_width_20_bucket",
    "volume_ratio_bucket",
    "signal_return_bucket",
    "low_base_loose_flag",
    "low_base_strict_flag",
    "consolidated_any_flag",
    "locked_limit_up_flag",
    "overheat_flag",
    "anomaly_flag",
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
class SliceSpec:
    slice_family: str
    slice_id: str
    slice_label: str
    basis: str
    note: str


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


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


def false_text() -> str:
    return "False"


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


def num_text(value: float | int | str, digits: int = 4) -> str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return safe_str(value)
    if math.isnan(number) or math.isinf(number):
        return ""
    return f"{number:.{digits}f}"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


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


def merge_sources() -> tuple[pd.DataFrame, str, str]:
    raw = read_csv(RAW_DETAIL_CSV)
    semantic = read_csv(SEMANTIC_DETAIL_CSV)
    if raw.empty:
        raise SystemExit("ERROR: raw rerun detail is empty")
    if semantic.empty:
        raise SystemExit("ERROR: semantic audit detail is empty")
    if set(raw.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: raw detail must come from volume_range_breakout_v2_raw_market_rerun")
    if set(semantic.get("research_id", pd.Series(dtype=str)).astype(str)) != {SEMANTIC_SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: semantic detail must come from volume_range_breakout_v2_semantic_audit")
    require_research_only(raw, "raw detail")
    require_research_only(semantic, "semantic detail")
    if raw["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: raw detail source_event_key must be unique")
    if semantic["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: semantic detail source_event_key must be unique")

    raw_version = source_artifact_version(raw, "raw detail")
    semantic_version = source_artifact_version(semantic, "semantic detail")
    semantic_columns = [
        "source_event_key",
        "previous_40d_high",
        "previous_60d_low",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "low_position_60_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "breakout_over_prev40_pct",
        "breakout_over_prev60_pct",
    ]
    semantic_columns = [col for col in semantic_columns if col in semantic.columns]
    merged = raw.merge(
        semantic[semantic_columns],
        on="source_event_key",
        how="left",
        suffixes=("", "_semantic"),
        validate="one_to_one",
    )
    if len(merged) != len(raw):
        raise SystemExit("ERROR: merged detail row count changed")
    missing_semantic = merged[semantic_columns[1]].astype(str).eq("").sum() if len(semantic_columns) > 1 else 0
    if missing_semantic:
        raise SystemExit(f"ERROR: semantic join missing rows: {missing_semantic}")
    for col in semantic_columns:
        if col == "source_event_key":
            continue
        sem_col = f"{col}_semantic"
        if sem_col in merged.columns:
            base = merged[col].astype(str) if col in merged.columns else pd.Series("", index=merged.index)
            merged[col] = base.where(base.ne(""), merged[sem_col])
            merged = merged.drop(columns=[sem_col])
    return merged, raw_version, semantic_version


def to_numeric_columns(detail: pd.DataFrame) -> pd.DataFrame:
    out = detail.copy()
    for col in [
        "return_pct",
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
        out[col] = pd.to_numeric(out.get(col, ""), errors="coerce")
    return out


def bucket_off_60d_low(value: float) -> str:
    if pd.isna(value):
        return "missing"
    if value <= 35:
        return "off60_le35_low_base"
    if value <= 50:
        return "off60_35_50_low_mid_base"
    if value <= 75:
        return "off60_50_75_extended"
    return "off60_gt75_high_extended"


def bucket_range_60(value: float) -> str:
    if pd.isna(value):
        return "missing"
    if value <= 35:
        return "range60_le35_narrow"
    if value <= 45:
        return "range60_35_45_moderate"
    if value <= 60:
        return "range60_45_60_wide"
    return "range60_gt60_very_wide"


def bucket_range_20(value: float) -> str:
    if pd.isna(value):
        return "missing"
    if value <= 15:
        return "range20_le15_tight"
    if value <= 25:
        return "range20_15_25_moderate"
    return "range20_gt25_wide"


def bucket_volume(value: float) -> str:
    if pd.isna(value):
        return "missing"
    if value < 2:
        return "volume_lt2_weak"
    if value <= 6:
        return "volume_2_to_6_controlled_attack"
    return "volume_gt6_overheat"


def bucket_signal_return(value: float) -> str:
    if pd.isna(value):
        return "missing"
    if value < 3:
        return "signal_return_lt3_modest"
    if value < 7:
        return "signal_return_3_to_7_strong"
    if value < 9.8:
        return "signal_return_7_to_9_8_extended"
    return "signal_return_ge9_8_limit_up_like"


def enrich_detail(detail: pd.DataFrame, raw_version: str, semantic_version: str, generated_at: str) -> pd.DataFrame:
    out = to_numeric_columns(detail)
    returns = out[RETURN_KEY]
    low_cut = float(returns.quantile(LOW_RETURN_Q))
    high_cut = float(returns.quantile(HIGH_RETURN_Q))
    out["return_outcome"] = "neutral"
    out.loc[returns > 0, "return_outcome"] = "win"
    out.loc[returns < 0, "return_outcome"] = "loss"
    out["top20_return_flag"] = returns.ge(high_cut).map(bool_text)
    out["bottom20_return_flag"] = returns.le(low_cut).map(bool_text)
    out["off_60d_low_bucket"] = out["off_60d_low_pct"].map(bucket_off_60d_low)
    out["range_width_60_bucket"] = out["range_width_60_pct"].map(bucket_range_60)
    out["range_width_20_bucket"] = out["range_width_20_pct"].map(bucket_range_20)
    out["volume_ratio_bucket"] = out["volume_ratio"].map(bucket_volume)
    out["signal_return_bucket"] = out["signal_return_1d_pct"].map(bucket_signal_return)
    out["low_base_loose_flag"] = (
        out["off_60d_low_pct"].le(50) & out["range_width_60_pct"].le(45)
    ).fillna(False).map(bool_text)
    out["low_base_strict_flag"] = (
        out["off_60d_low_pct"].le(40) & out["range_width_60_pct"].le(35)
    ).fillna(False).map(bool_text)
    out["consolidated_any_flag"] = out["consolidation_type"].isin(["short_consolidation", "long_consolidation"]).map(bool_text)
    out["locked_limit_up_flag"] = (
        out["limit_up_like"].astype(str).eq("True") | out["attack_method"].astype(str).eq("locked_limit_up")
    ).map(bool_text)
    out["overheat_flag"] = (
        out["risk_type"].isin(["volume_overheat", "high_position_chase"])
        | out["signal_return_1d_pct"].ge(9.8)
        | out["volume_ratio"].gt(6)
    ).fillna(False).map(bool_text)
    out["research_id"] = RESEARCH_ID
    out["artifact_version"] = ARTIFACT_VERSION
    out["source_research_id"] = SOURCE_RESEARCH_ID
    out["source_artifact_version"] = raw_version
    out["semantic_source_research_id"] = SEMANTIC_SOURCE_RESEARCH_ID
    out["semantic_source_artifact_version"] = semantic_version
    out["advisory_status"] = ADVISORY_STATUS
    out["model_id"] = MODEL_ID
    out["approved_for_daily"] = false_text()
    out["production_readiness"] = PRODUCTION_READINESS
    out["generated_at"] = generated_at
    return out


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get(RETURN_KEY, pd.Series(dtype=float)), errors="coerce").dropna()
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
            "min_return_pct": "",
            "max_return_pct": "",
            "trim_sample_size": 0,
            "trim_avg_return_pct": "",
            "trim_median_return_pct": "",
        }
    win_count = int((returns > 0).sum())
    neutral_count = int((returns == 0).sum())
    loss_count = int((returns < 0).sum())
    lower = float(returns.quantile(0.01))
    upper = float(returns.quantile(0.99))
    trim = returns[returns.between(lower, upper)]
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
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
        "trim_sample_size": int(len(trim)),
        "trim_avg_return_pct": pct_round(float(trim.mean())) if len(trim) else "",
        "trim_median_return_pct": pct_round(float(trim.median())) if len(trim) else "",
    }


def base_row(
    row_type: str,
    slice_family: str,
    slice_id: str,
    slice_label: str,
    basis: str,
    generated_at: str,
    raw_version: str,
    semantic_version: str,
    note: str = "",
) -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": raw_version,
        "semantic_source_research_id": SEMANTIC_SOURCE_RESEARCH_ID,
        "semantic_source_artifact_version": semantic_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "slice_family": slice_family,
        "slice_id": slice_id,
        "slice_label": slice_label,
        "basis": basis,
        "note": note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    if sample_size >= 50:
        return "thin_sample"
    return "insufficient_sample"


def performance_decision_hint(row: dict[str, Any], baseline: dict[str, Any], slice_id: str) -> str:
    sample_size = int(row.get("sample_size") or 0)
    if slice_id == "baseline_all_v2_raw_events":
        return "baseline_reference"
    if sample_size < 50:
        return "insufficient_sample_do_not_use_as_gate"
    avg = float(row.get("avg_return_pct") or 0.0)
    median = float(row.get("median_return_pct") or 0.0)
    loss_rate = float(row.get("loss_rate_pct") or 0.0)
    base_avg = float(baseline.get("avg_return_pct") or 0.0)
    base_median = float(baseline.get("median_return_pct") or 0.0)
    base_loss = float(baseline.get("loss_rate_pct") or 0.0)
    if sample_size >= 100 and avg >= base_avg + 1.0 and median >= base_median + 0.5 and loss_rate <= base_loss:
        return "possible_positive_gate_or_score_candidate_research_only"
    if sample_size >= 100 and avg <= base_avg - 1.0 and median <= base_median - 0.5 and loss_rate >= base_loss:
        return "possible_risk_tag_or_deduct_candidate_research_only"
    if sample_size >= 100 and "overheat" in slice_id and avg < base_avg:
        return "possible_overheat_risk_tag_research_only"
    return "mixed_or_weak_difference_research_only"


def add_performance_slice(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    mask: pd.Series,
    spec: SliceSpec,
    generated_at: str,
    raw_version: str,
    semantic_version: str,
    baseline_metrics: dict[str, Any],
) -> None:
    part = detail[mask.fillna(False)]
    row = base_row(
        "performance_slice",
        spec.slice_family,
        spec.slice_id,
        spec.slice_label,
        spec.basis,
        generated_at,
        raw_version,
        semantic_version,
        spec.note,
    )
    row.update(return_metrics(part))
    sample_size = int(row["sample_size"])
    baseline_size = len(detail)
    row["coverage_pct"] = pct_round(sample_size / baseline_size * 100.0 if baseline_size else math.nan, 2)
    top_count = int(part["top20_return_flag"].astype(str).eq("True").sum())
    bottom_count = int(part["bottom20_return_flag"].astype(str).eq("True").sum())
    row["top20_count"] = top_count
    row["bottom20_count"] = bottom_count
    row["top20_share_pct"] = pct_round(top_count / sample_size * 100.0 if sample_size else math.nan, 2)
    row["bottom20_share_pct"] = pct_round(bottom_count / sample_size * 100.0 if sample_size else math.nan, 2)
    row["top_minus_bottom_share_pct"] = pct_round(
        float(row["top20_share_pct"] or 0.0) - float(row["bottom20_share_pct"] or 0.0),
        2,
    )
    row["sample_status"] = sample_status(sample_size)
    row["decision_hint"] = performance_decision_hint(row, baseline_metrics, spec.slice_id)
    rows.append(row)


def performance_slices(detail: pd.DataFrame) -> list[tuple[SliceSpec, pd.Series]]:
    always = pd.Series(True, index=detail.index)
    off = detail["off_60d_low_pct"]
    width60 = detail["range_width_60_pct"]
    width20 = detail["range_width_20_pct"]
    vol = detail["volume_ratio"]
    sig_ret = detail["signal_return_1d_pct"]
    consolidated = detail["consolidated_any_flag"].eq("True")
    locked = detail["locked_limit_up_flag"].eq("True")
    overheat = detail["overheat_flag"].eq("True")
    low_loose = detail["low_base_loose_flag"].eq("True")
    low_strict = detail["low_base_strict_flag"].eq("True")
    return [
        (
            SliceSpec("baseline", "baseline_all_v2_raw_events", "all 60d breakout + next-day continuation events", "all 808 raw-market v2 mature events", "baseline for this research-only feature analysis"),
            always,
        ),
        (
            SliceSpec("low_base_proxy", "off60_le50_range60_le45", "off 60d low <=50% and 60d range <=45%", "low-base proxy", "tests whether the user's low-base intuition improves payoff"),
            low_loose,
        ),
        (
            SliceSpec("low_base_proxy", "off60_le40_range60_le35", "off 60d low <=40% and 60d range <=35%", "strict low-base proxy", "stricter low-base proxy; sample shrink must be reviewed"),
            low_strict,
        ),
        (
            SliceSpec("low_base_proxy", "off60_gt75_or_range60_gt60", "off 60d low >75% or 60d range >60%", "extended/high-base proxy", "diagnoses high-extension or wide-base risk"),
            off.gt(75) | width60.gt(60),
        ),
        (
            SliceSpec("range_width", "range60_le35_narrow", "60d range width <=35%", "narrow 60d consolidation proxy", "tests narrow base independently from off-low position"),
            width60.le(35),
        ),
        (
            SliceSpec("range_width", "range60_gt60_very_wide", "60d range width >60%", "wide 60d base risk proxy", "wide range can mean volatility rather than constructive consolidation"),
            width60.gt(60),
        ),
        (
            SliceSpec("range_width", "range20_le15_tight", "20d range width <=15%", "tight recent consolidation proxy", "tests whether the most recent base is tight"),
            width20.le(15),
        ),
        (
            SliceSpec("range_width", "range20_gt25_wide", "20d range width >25%", "wide recent range risk proxy", "diagnoses loose recent action"),
            width20.gt(25),
        ),
        (
            SliceSpec("consolidation", "consolidated_any", "short or long consolidation label", "existing consolidation_type label", "tests existing consolidation classifier"),
            consolidated,
        ),
        (
            SliceSpec("consolidation", "non_consolidation", "non-consolidation label", "existing consolidation_type label", "diagnoses breakouts without a base"),
            detail["consolidation_type"].eq("non_consolidation"),
        ),
        (
            SliceSpec("limit_up", "locked_limit_up", "locked limit-up like signal", "limit_up_like=True or attack_method=locked_limit_up", "tests lock-limit behavior separately"),
            locked,
        ),
        (
            SliceSpec("limit_up", "not_locked_limit_up", "not locked limit-up like", "not lock-limit", "tests non-lock volume attacks"),
            ~locked,
        ),
        (
            SliceSpec("overheat", "overheat_flag_true", "overheat flag true", "risk_type overheat/chase or volume>6 or signal return>=9.8", "diagnoses overheated breakout risk"),
            overheat,
        ),
        (
            SliceSpec("overheat", "overheat_flag_false", "overheat flag false", "not overheat by provisional proxy", "tests cleaner breakouts without overheat proxy"),
            ~overheat,
        ),
        (
            SliceSpec("overheat", "volume_ratio_2_to_6", "volume ratio 2 to 6", "controlled volume expansion", "tests whether controlled volume is better than weak or excessive volume"),
            vol.between(2, 6, inclusive="both"),
        ),
        (
            SliceSpec("overheat", "volume_ratio_gt6", "volume ratio >6", "excessive volume expansion", "diagnoses volume overheat"),
            vol.gt(6),
        ),
        (
            SliceSpec("overheat", "signal_return_ge9_8", "signal day return >=9.8%", "limit-up like daily return", "diagnoses locked/extended signal day"),
            sig_ret.ge(9.8),
        ),
        (
            SliceSpec("combined", "low_base_loose_and_consolidated", "loose low-base proxy and consolidated", "off60<=50, range60<=45, consolidated", "tests hard-gate style low-base consolidation"),
            low_loose & consolidated,
        ),
        (
            SliceSpec("combined", "low_base_loose_not_overheat", "loose low-base proxy and not overheat", "off60<=50, range60<=45, overheat=False", "tests low-base plus risk cleanup"),
            low_loose & ~overheat,
        ),
        (
            SliceSpec("combined", "low_base_loose_not_locked", "loose low-base proxy and not locked", "off60<=50, range60<=45, locked=False", "tests whether low-base works without lock-limit rows"),
            low_loose & ~locked,
        ),
        (
            SliceSpec("combined", "high_or_wide_overheat", "extended/wide and overheat", "(off60>75 or range60>60) and overheat", "candidate risk-tag cluster"),
            (off.gt(75) | width60.gt(60)) & overheat,
        ),
        (
            SliceSpec("combined", "high_wide_non_consolidation", "extended or wide and non-consolidation", "(off60>75 or range60>60) and non-consolidation", "candidate separate-model or avoid cluster"),
            (off.gt(75) | width60.gt(60)) & detail["consolidation_type"].eq("non_consolidation"),
        ),
    ]


def add_feature_share_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    generated_at: str,
    raw_version: str,
    semantic_version: str,
) -> None:
    top = detail[detail["top20_return_flag"].astype(str).eq("True")]
    bottom = detail[detail["bottom20_return_flag"].astype(str).eq("True")]
    features = [
        "off_60d_low_bucket",
        "range_width_60_bucket",
        "range_width_20_bucket",
        "volume_ratio_bucket",
        "signal_return_bucket",
        "consolidation_type",
        "limit_up_like",
        "locked_limit_up_flag",
        "overheat_flag",
        "attack_method",
        "classification_id",
        "risk_type",
        "candle_quality",
        "price_position_type",
    ]
    baseline_size = len(detail)
    for feature in features:
        values = sorted(set(detail.get(feature, pd.Series(dtype=str)).fillna("").astype(str)))
        for value in values:
            part = detail[detail[feature].fillna("").astype(str).eq(value)]
            if part.empty:
                continue
            overall_share = len(part) / baseline_size * 100.0 if baseline_size else math.nan
            high_share = top[feature].fillna("").astype(str).eq(value).mean() * 100.0 if len(top) else math.nan
            low_share = bottom[feature].fillna("").astype(str).eq(value).mean() * 100.0 if len(bottom) else math.nan
            if max(overall_share, high_share, low_share) < 5.0:
                continue
            row = base_row(
                "high_low_feature_share",
                feature,
                f"{feature}={value or '(blank)'}",
                value or "(blank)",
                "top20 return share vs bottom20 return share",
                generated_at,
                raw_version,
                semantic_version,
                "feature share comparison only; not a standalone gate",
            )
            row.update(return_metrics(part))
            row["coverage_pct"] = pct_round(overall_share, 2)
            row["overall_share_pct"] = pct_round(overall_share, 2)
            row["high_return_share_pct"] = pct_round(high_share, 2)
            row["low_return_share_pct"] = pct_round(low_share, 2)
            row["high_minus_low_share_pct"] = pct_round(high_share - low_share, 2)
            diff = float(row["high_minus_low_share_pct"] or 0.0)
            if diff >= 10:
                row["decision_hint"] = "more_common_in_high_return_research_signal"
            elif diff <= -10:
                row["decision_hint"] = "more_common_in_low_return_risk_signal"
            else:
                row["decision_hint"] = "weak_or_mixed_feature_difference"
            row["value_a"] = f"top20_n={len(top)}"
            row["value_b"] = f"bottom20_n={len(bottom)}"
            rows.append(row)


def add_numeric_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    generated_at: str,
    raw_version: str,
    semantic_version: str,
) -> None:
    top = detail[detail["top20_return_flag"].astype(str).eq("True")]
    bottom = detail[detail["bottom20_return_flag"].astype(str).eq("True")]
    for feature in [
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "breakout_over_prev60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "mfe_pct",
        "mae_pct",
    ]:
        values = pd.to_numeric(detail.get(feature, pd.Series(dtype=float)), errors="coerce").dropna()
        top_values = pd.to_numeric(top.get(feature, pd.Series(dtype=float)), errors="coerce").dropna()
        bottom_values = pd.to_numeric(bottom.get(feature, pd.Series(dtype=float)), errors="coerce").dropna()
        row = base_row(
            "high_low_numeric_median",
            "numeric_feature",
            feature,
            feature,
            "top20 return median vs bottom20 return median",
            generated_at,
            raw_version,
            semantic_version,
            "numeric median comparison only; use with slice rows before changing gates",
        )
        row["sample_size"] = len(values)
        row["coverage_pct"] = pct_round(len(values) / len(detail) * 100.0 if len(detail) else math.nan, 2)
        row["numeric_overall_median"] = pct_round(float(values.median())) if len(values) else ""
        row["numeric_top20_median"] = pct_round(float(top_values.median())) if len(top_values) else ""
        row["numeric_bottom20_median"] = pct_round(float(bottom_values.median())) if len(bottom_values) else ""
        if row["numeric_top20_median"] != "" and row["numeric_bottom20_median"] != "":
            row["numeric_top_minus_bottom_median"] = pct_round(
                float(row["numeric_top20_median"]) - float(row["numeric_bottom20_median"])
            )
        row["value_a"] = f"top20_n={len(top_values)}"
        row["value_b"] = f"bottom20_n={len(bottom_values)}"
        diff = float(row.get("numeric_top_minus_bottom_median") or 0.0)
        if feature in {"range_width_20_pct", "range_width_60_pct", "off_60d_low_pct"} and diff <= -5:
            row["decision_hint"] = "top_return_has_lower_feature_value_research_signal"
        elif feature in {"range_width_20_pct", "range_width_60_pct", "off_60d_low_pct"} and diff >= 5:
            row["decision_hint"] = "top_return_has_higher_feature_value_research_signal"
        else:
            row["decision_hint"] = "numeric_difference_diagnostic_only"
        rows.append(row)


def add_anomaly_rows(
    rows: list[dict[str, Any]],
    detail: pd.DataFrame,
    generated_at: str,
    raw_version: str,
    semantic_version: str,
) -> None:
    returns = pd.to_numeric(detail[RETURN_KEY], errors="coerce").dropna()
    lower = float(returns.quantile(0.01))
    upper = float(returns.quantile(0.99))
    trimmed = detail[pd.to_numeric(detail[RETURN_KEY], errors="coerce").between(lower, upper)]
    row = base_row(
        "anomaly_check",
        "trim_return_tail",
        "trim_1pct_each_tail",
        "trim 1pct each tail",
        "numeric anomaly sensitivity",
        generated_at,
        raw_version,
        semantic_version,
        "extreme rows remain in detail; trimmed row is sensitivity only",
    )
    row.update(return_metrics(trimmed))
    row["value_a"] = f"lower_cutoff={num_text(lower)}"
    row["value_b"] = f"upper_cutoff={num_text(upper)}"
    row["value_c"] = f"removed_rows={len(detail) - len(trimmed)}"
    row["decision_hint"] = "anomaly_sensitivity_research_only"
    rows.append(row)
    for key, part in [
        ("top_10_returns", detail.nlargest(10, RETURN_KEY)),
        ("bottom_10_returns", detail.nsmallest(10, RETURN_KEY)),
    ]:
        item = base_row(
            "anomaly_extreme_list",
            "return_extremes",
            key,
            key,
            "manual anomaly inspection list",
            generated_at,
            raw_version,
            semantic_version,
            "inspect before using averages as promotion evidence",
        )
        item["sample_size"] = len(part)
        item["value_a"] = "|".join(part["source_event_key"].astype(str).head(10))
        item["decision_hint"] = "manual_review_required_before_promotion"
        rows.append(item)


def build_summary(detail: pd.DataFrame, generated_at: str, raw_version: str, semantic_version: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    baseline_metrics = return_metrics(detail)
    for spec, mask in performance_slices(detail):
        add_performance_slice(rows, detail, mask, spec, generated_at, raw_version, semantic_version, baseline_metrics)
    add_feature_share_rows(rows, detail, generated_at, raw_version, semantic_version)
    add_numeric_rows(rows, detail, generated_at, raw_version, semantic_version)
    add_anomaly_rows(rows, detail, generated_at, raw_version, semantic_version)
    return pd.DataFrame(rows)


def write_markdown(summary: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 20) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
        return lines

    perf = summary[summary["row_type"].eq("performance_slice")].copy()
    feature = summary[summary["row_type"].eq("high_low_feature_share")].copy()
    numeric = summary[summary["row_type"].eq("high_low_numeric_median")].copy()
    perf["sample_size_n"] = pd.to_numeric(perf["sample_size"], errors="coerce")
    perf["avg_return_n"] = pd.to_numeric(perf["avg_return_pct"], errors="coerce")
    perf["top_minus_bottom_n"] = pd.to_numeric(perf["top_minus_bottom_share_pct"], errors="coerce")
    feature["diff_n"] = pd.to_numeric(feature["high_minus_low_share_pct"], errors="coerce").abs()

    lines = [
        "# volume_range_breakout v2 feature slice analysis",
        "",
        "Research-only artifact. This does not change production model conditions, ranking, scoring, registry, or PDF behavior.",
        "",
        "Source population: 808 raw-market events for `prev60_high_next_day_continuation` after source sync.",
        "Purpose: compare low-base vs high/extended setups, narrow vs wide consolidation, locked limit-up behavior, overheat proxies, and top/bottom return feature differences before any v2 promotion discussion.",
        "",
        "## Performance Slices",
        "",
    ]
    lines += md_table(
        perf.sort_values(["sample_size_n", "avg_return_n"], ascending=[False, False]),
        [
            "slice_id",
            "sample_size",
            "win_rate_pct",
            "loss_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "top_minus_bottom_share_pct",
            "decision_hint",
        ],
        limit=30,
    )
    lines += [
        "",
        "## Strongest Top/Bottom Return Feature Differences",
        "",
    ]
    lines += md_table(
        feature.sort_values("diff_n", ascending=False),
        [
            "slice_id",
            "sample_size",
            "overall_share_pct",
            "high_return_share_pct",
            "low_return_share_pct",
            "high_minus_low_share_pct",
            "decision_hint",
        ],
        limit=30,
    )
    lines += [
        "",
        "## Numeric Top/Bottom Median Comparison",
        "",
    ]
    lines += md_table(
        numeric,
        [
            "slice_id",
            "sample_size",
            "numeric_overall_median",
            "numeric_top20_median",
            "numeric_bottom20_median",
            "numeric_top_minus_bottom_median",
            "decision_hint",
        ],
        limit=20,
    )
    lines += [
        "",
        "## Promotion Boundary",
        "",
        "These rows are diagnostic and research-only. A hard gate, score, risk tag, or model split still requires a separate promotion review with operation contract and production parity evidence.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail_raw, raw_version, semantic_version = merge_sources()
    detail = enrich_detail(detail_raw, raw_version, semantic_version, generated_at)
    summary = build_summary(detail, generated_at, raw_version, semantic_version)
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in research artifact: {forbidden}")
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_markdown(summary, LATEST_SUMMARY_MD)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
