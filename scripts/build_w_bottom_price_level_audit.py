from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
SOURCE_TAXONOMY_CSV = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_price_level_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_price_level_audit_detail.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_price_level_audit"
SOURCE_RESEARCH_ID = "w_bottom_path_quality_filter_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_price_level_audit_20260625"

LOOKBACK_DAYS_REQUESTED = 252
MIN_PRICE_HISTORY_DAYS = 180
OBSERVATION_TO_VOLUME = "observation_to_volume_confirmation"
WV_CATEGORY = "wv_multiple_turn_risk"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

DETAIL_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "transition_status",
    "slope_curvature_category",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "effective_mainstream_label",
    "has_hot_theme",
    "structural_theme_bucket",
    "primary_theme",
    "taxonomy_source",
    "taxonomy_confidence",
    "lookback_days_requested",
    "min_price_history_days",
    "lookback_observed_days",
    "lookback_start_date",
    "lookback_end_date",
    "signal_close",
    "lookback_low_price",
    "lookback_high_price",
    "lookback_close_median",
    "lookback_close_mean",
    "price_position_252_pct",
    "below_252_median",
    "below_252_mean",
    "source_long_position_gate_passed",
    "price_level_bucket",
    "price_level_reason",
    "price_level_available",
    "core_mainstream_exclude_wv_review_candidate",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "summary_scope",
    "summary_description",
    "price_level_bucket",
    "sample_size",
    "price_level_available_count",
    "below_252_median_count",
    "below_252_mean_count",
    "source_long_position_gate_pass_count",
    "volume_confirmation_count",
    "volume_confirmation_rate_pct",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "tdcc_any_age7_count",
    "smooth_count",
    "sharp_v_count",
    "wv_multiple_turn_count",
    "slope_break_count",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


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


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        number = float(text)
    except ValueError:
        return math.nan
    return number if not math.isnan(number) else math.nan


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def bool_text(value: Any) -> str:
    return "true" if bool_value(value) or value is True else "false"


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: Any) -> str:
    digits = "".join(ch for ch in safe_str(value) if ch.isdigit())
    return digits[:8]


def pct_round(value: float, digits: int = 4) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, digits)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def load_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in price.columns:
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    for column in ["open", "high", "low", "close", "volume"]:
        if column in price.columns:
            price[column] = pd.to_numeric(price[column], errors="coerce")
    return price[price["date"].ne("")].sort_values("date").reset_index(drop=True)


def read_taxonomy() -> pd.DataFrame:
    taxonomy = read_csv(SOURCE_TAXONOMY_CSV)
    if "stock_id" not in taxonomy.columns:
        raise SystemExit(f"ERROR: taxonomy missing stock_id column: {SOURCE_TAXONOMY_CSV}")
    taxonomy = taxonomy.copy()
    taxonomy["stock_id"] = taxonomy["stock_id"].map(normalize_code)
    wanted = [
        "stock_id",
        "effective_mainstream_label",
        "has_hot_theme",
        "structural_theme_bucket",
        "primary_theme",
        "taxonomy_source",
        "confidence",
    ]
    for column in wanted:
        if column not in taxonomy.columns:
            taxonomy[column] = ""
    taxonomy = taxonomy[wanted].drop_duplicates("stock_id", keep="first")
    taxonomy = taxonomy.rename(columns={"confidence": "taxonomy_confidence"})
    return taxonomy


def price_level_bucket(position_pct: float, available: bool) -> tuple[str, str]:
    if not available or math.isnan(position_pct):
        return "price_history_insufficient", "missing_or_insufficient_price_history"
    if position_pct <= 25:
        return "bottom_quartile_level", "signal_close_in_bottom_25pct_of_lookback_range"
    if position_pct <= 40:
        return "low_level", "signal_close_in_25_to_40pct_of_lookback_range"
    if position_pct <= 60:
        return "mid_level", "signal_close_in_40_to_60pct_of_lookback_range"
    return "high_level", "signal_close_above_60pct_of_lookback_range"


def price_level_for(stock_id: str, signal_date: str) -> dict[str, Any]:
    price = load_price(stock_id)
    if price.empty:
        return unavailable_price_level("missing_price_history")
    signal_date = normalize_date(signal_date)
    matches = price.index[price["date"].eq(signal_date)]
    if len(matches) == 0:
        return unavailable_price_level("signal_date_missing_in_price_history")
    signal_idx = int(matches[0])
    start_idx = max(0, signal_idx - LOOKBACK_DAYS_REQUESTED + 1)
    lookback = price.iloc[start_idx : signal_idx + 1].copy()
    observed_days = int(len(lookback))
    valid = lookback.dropna(subset=["close", "high", "low"])
    signal_close = safe_float(price.iloc[signal_idx].get("close"))
    if observed_days < MIN_PRICE_HISTORY_DAYS or len(valid) < MIN_PRICE_HISTORY_DAYS or math.isnan(signal_close):
        result = unavailable_price_level("insufficient_price_history")
        result.update(
            {
                "lookback_observed_days": observed_days,
                "lookback_start_date": safe_str(lookback.iloc[0].get("date")) if observed_days else "",
                "lookback_end_date": safe_str(lookback.iloc[-1].get("date")) if observed_days else "",
                "signal_close": pct_round(signal_close),
            }
        )
        return result

    low_price = float(valid["low"].min())
    high_price = float(valid["high"].max())
    median_close = float(valid["close"].median())
    mean_close = float(valid["close"].mean())
    if high_price <= low_price:
        position_pct = math.nan
    else:
        position_pct = (signal_close - low_price) / (high_price - low_price) * 100.0
        position_pct = max(0.0, min(100.0, position_pct))
    available = not math.isnan(position_pct)
    bucket, reason = price_level_bucket(position_pct, available)
    below_median = signal_close <= median_close
    below_mean = signal_close <= mean_close
    return {
        "lookback_observed_days": observed_days,
        "lookback_start_date": safe_str(lookback.iloc[0].get("date")),
        "lookback_end_date": safe_str(lookback.iloc[-1].get("date")),
        "signal_close": pct_round(signal_close),
        "lookback_low_price": pct_round(low_price),
        "lookback_high_price": pct_round(high_price),
        "lookback_close_median": pct_round(median_close),
        "lookback_close_mean": pct_round(mean_close),
        "price_position_252_pct": pct_round(position_pct),
        "below_252_median": bool_text(below_median),
        "below_252_mean": bool_text(below_mean),
        "source_long_position_gate_passed": bool_text(below_median and observed_days >= MIN_PRICE_HISTORY_DAYS),
        "price_level_bucket": bucket,
        "price_level_reason": reason,
        "price_level_available": bool_text(available),
    }


def unavailable_price_level(reason: str) -> dict[str, Any]:
    return {
        "lookback_observed_days": 0,
        "lookback_start_date": "",
        "lookback_end_date": "",
        "signal_close": "",
        "lookback_low_price": "",
        "lookback_high_price": "",
        "lookback_close_median": "",
        "lookback_close_mean": "",
        "price_position_252_pct": "",
        "below_252_median": "false",
        "below_252_mean": "false",
        "source_long_position_gate_passed": "false",
        "price_level_bucket": "price_history_insufficient",
        "price_level_reason": reason,
        "price_level_available": "false",
    }


def read_source_detail() -> pd.DataFrame:
    detail = read_csv(SOURCE_DETAIL_CSV)
    required = {
        "stock_id",
        "stock_name",
        "signal_date",
        "transition_status",
        "slope_curvature_category",
        "a_mature",
        "a_return_pct",
        "c_mature",
        "c_return_pct",
        "tdcc_any_age7",
        "tdcc_any_age14",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: path quality detail missing columns: {missing}")
    detail = detail.copy()
    detail["stock_id"] = detail["stock_id"].map(normalize_code)
    detail["signal_date"] = detail["signal_date"].map(normalize_date)
    taxonomy = read_taxonomy()
    detail = detail.merge(taxonomy, on="stock_id", how="left")
    for column in [
        "effective_mainstream_label",
        "has_hot_theme",
        "structural_theme_bucket",
        "primary_theme",
        "taxonomy_source",
        "taxonomy_confidence",
    ]:
        if column not in detail.columns:
            detail[column] = ""
    return detail


def build_detail(generated_at: str) -> pd.DataFrame:
    source = read_source_detail()
    rows: list[dict[str, Any]] = []
    for _, source_row in source.iterrows():
        stock_id = normalize_code(source_row.get("stock_id"))
        signal_date = normalize_date(source_row.get("signal_date"))
        level = price_level_for(stock_id, signal_date)
        is_core_exclude_wv = (
            safe_str(source_row.get("transition_status")) == OBSERVATION_TO_VOLUME
            and safe_str(source_row.get("slope_curvature_category")) != WV_CATEGORY
            and safe_str(source_row.get("effective_mainstream_label")) == "core_mainstream"
        )
        row = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "stock_id": stock_id,
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": signal_date,
            "transition_status": safe_str(source_row.get("transition_status")),
            "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
            "a_mature": bool_text(source_row.get("a_mature")),
            "a_return_pct": safe_str(source_row.get("a_return_pct")),
            "c_mature": bool_text(source_row.get("c_mature")),
            "c_return_pct": safe_str(source_row.get("c_return_pct")),
            "tdcc_any_age7": bool_text(source_row.get("tdcc_any_age7")),
            "tdcc_any_age14": bool_text(source_row.get("tdcc_any_age14")),
            "effective_mainstream_label": safe_str(source_row.get("effective_mainstream_label")),
            "has_hot_theme": safe_str(source_row.get("has_hot_theme")).lower(),
            "structural_theme_bucket": safe_str(source_row.get("structural_theme_bucket")),
            "primary_theme": safe_str(source_row.get("primary_theme")),
            "taxonomy_source": safe_str(source_row.get("taxonomy_source")),
            "taxonomy_confidence": safe_str(source_row.get("taxonomy_confidence")),
            "lookback_days_requested": LOOKBACK_DAYS_REQUESTED,
            "min_price_history_days": MIN_PRICE_HISTORY_DAYS,
            "core_mainstream_exclude_wv_review_candidate": bool_text(is_core_exclude_wv),
            "manual_review_status": "pending_research_review",
            "approved_for_daily": "false",
            "production_readiness": "not_production_ready_research_only",
            "generated_at": generated_at,
        }
        row.update(level)
        rows.append(row)
    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in price level detail: {forbidden}")
    return detail[DETAIL_COLUMNS]


def metric_number(value: float) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.4f}"


def metrics_for(sample: pd.DataFrame, scope: str, description: str, bucket: str, generated_at: str) -> dict[str, Any]:
    mature = sample[sample["a_mature"].astype(str).str.lower().eq("true")].copy()
    returns = pd.to_numeric(mature["a_return_pct"], errors="coerce").dropna()
    positions = pd.to_numeric(sample["price_position_252_pct"], errors="coerce").dropna()
    sample_size = int(len(sample))
    volume_count = int(sample["transition_status"].astype(str).eq(OBSERVATION_TO_VOLUME).sum()) if sample_size else 0
    categories = sample["slope_curvature_category"].value_counts().to_dict() if sample_size else {}
    row = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "summary_scope": scope,
        "summary_description": description,
        "price_level_bucket": bucket,
        "sample_size": sample_size,
        "price_level_available_count": int(sample["price_level_available"].astype(str).str.lower().eq("true").sum()) if sample_size else 0,
        "below_252_median_count": int(sample["below_252_median"].astype(str).str.lower().eq("true").sum()) if sample_size else 0,
        "below_252_mean_count": int(sample["below_252_mean"].astype(str).str.lower().eq("true").sum()) if sample_size else 0,
        "source_long_position_gate_pass_count": int(sample["source_long_position_gate_passed"].astype(str).str.lower().eq("true").sum()) if sample_size else 0,
        "volume_confirmation_count": volume_count,
        "volume_confirmation_rate_pct": metric_number(volume_count / sample_size * 100.0 if sample_size else math.nan),
        "mature_sample_size": int(len(returns)),
        "win_count": int(returns.gt(0).sum()),
        "win_rate_pct": metric_number(returns.gt(0).mean() * 100.0 if len(returns) else math.nan),
        "avg_a_return_pct": metric_number(float(returns.mean()) if len(returns) else math.nan),
        "median_a_return_pct": metric_number(float(returns.median()) if len(returns) else math.nan),
        "avg_price_position_252_pct": metric_number(float(positions.mean()) if len(positions) else math.nan),
        "median_price_position_252_pct": metric_number(float(positions.median()) if len(positions) else math.nan),
        "tdcc_any_age7_count": int(sample["tdcc_any_age7"].astype(str).str.lower().eq("true").sum()) if sample_size else 0,
        "smooth_count": int(categories.get("smooth_rounded_w_like", 0)),
        "sharp_v_count": int(categories.get("sharp_v_bottom_risk", 0)),
        "wv_multiple_turn_count": int(categories.get("wv_multiple_turn_risk", 0)),
        "slope_break_count": int(categories.get("slope_break_discontinuous", 0)),
        "approved_for_daily": "false",
        "production_readiness": "not_production_ready_research_only",
        "generated_at": generated_at,
    }
    return row


def scope_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (
            "all_w_bottom_candidates",
            "All 470 W-bottom right-side candidates from the path-quality audit.",
            lambda df: pd.Series(True, index=df.index),
        ),
        (
            "observation_to_volume_confirmation",
            "Candidates that started as right-side observation and later confirmed by neckline volume breakout.",
            lambda df: df["transition_status"].eq(OBSERVATION_TO_VOLUME),
        ),
        (
            "observation_volume_exclude_wv",
            "Observation-to-volume-confirmation candidates excluding WV/WVV multiple-turn paths.",
            lambda df: df["transition_status"].eq(OBSERVATION_TO_VOLUME) & ~df["slope_curvature_category"].eq(WV_CATEGORY),
        ),
        (
            "core_mainstream_observation_volume_exclude_wv",
            "Core-mainstream observation-to-volume-confirmation candidates excluding WV/WVV multiple-turn paths.",
            lambda df: df["core_mainstream_exclude_wv_review_candidate"].astype(str).str.lower().eq("true"),
        ),
    ]


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    bucket_order = ["all", "bottom_quartile_level", "low_level", "mid_level", "high_level", "price_history_insufficient"]
    for scope, description, predicate in scope_specs():
        scope_sample = detail[predicate(detail)].copy()
        rows.append(metrics_for(scope_sample, scope, description, "all", generated_at))
        for bucket in bucket_order[1:]:
            sample = scope_sample[scope_sample["price_level_bucket"].eq(bucket)].copy()
            if sample.empty:
                continue
            rows.append(metrics_for(sample, scope, description, bucket, generated_at))
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in price level summary: {forbidden}")
    return summary[SUMMARY_COLUMNS]


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 60) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    bucket_counts = (
        detail.groupby("price_level_bucket", dropna=False)
        .size()
        .reset_index(name="candidate_count")
        .sort_values("price_level_bucket")
    )
    selected_summary = summary[
        summary["summary_scope"].isin(
            [
                "all_w_bottom_candidates",
                "observation_to_volume_confirmation",
                "core_mainstream_observation_volume_exclude_wv",
            ]
        )
        & summary["price_level_bucket"].ne("price_history_insufficient")
    ].copy()
    sample_detail = detail[
        detail["core_mainstream_exclude_wv_review_candidate"].astype(str).str.lower().eq("true")
    ][
        [
            "stock_id",
            "stock_name",
            "signal_date",
            "price_level_bucket",
            "price_position_252_pct",
            "below_252_median",
            "below_252_mean",
            "a_mature",
            "a_return_pct",
            "slope_curvature_category",
        ]
    ]
    lines = [
        "# W-Bottom Price Level Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- detail_rows: `{len(detail)}`",
        f"- lookback_days_requested: `{LOOKBACK_DAYS_REQUESTED}`",
        f"- min_price_history_days: `{MIN_PRICE_HISTORY_DAYS}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: the existing W-bottom source already applies a coarse long-position gate of signal close <= 252-day median close; this audit makes that gate visible and adds low/high-range position buckets.",
        "",
        "## Price Level Buckets",
        "",
        "| bucket | definition |",
        "| --- | --- |",
        "| bottom_quartile_level | signal close is in the bottom 0-25% of the lookback low/high range |",
        "| low_level | signal close is in the 25-40% range |",
        "| mid_level | signal close is in the 40-60% range |",
        "| high_level | signal close is above 60% of the lookback range |",
        "",
        "## Bucket Counts",
        "",
        *markdown_table(bucket_counts, ["price_level_bucket", "candidate_count"], limit=20),
        "",
        "## Summary",
        "",
        *markdown_table(
            selected_summary,
            [
                "summary_scope",
                "price_level_bucket",
                "sample_size",
                "mature_sample_size",
                "win_rate_pct",
                "avg_a_return_pct",
                "median_a_return_pct",
                "volume_confirmation_rate_pct",
                "avg_price_position_252_pct",
                "below_252_median_count",
            ],
            limit=80,
        ),
        "",
        "## Core-Mainstream Exclude-WV Detail",
        "",
        *markdown_table(sample_detail, list(sample_detail.columns), limit=30),
        "",
        "## Reading Notes",
        "",
        "- If low-level buckets outperform mid/high buckets consistently, price level can become a candidate research filter.",
        "- If the current 252-day median gate already removes every high-level case, the next discussion should focus on whether bottom-quartile or low-level should be required for W-bottom observation.",
        "- This is research-only evidence. Any formal W-bottom production change still needs a separate promotion/model-change PR.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(detail, summary, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {HISTORY_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {HISTORY_SUMMARY_CSV} rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
