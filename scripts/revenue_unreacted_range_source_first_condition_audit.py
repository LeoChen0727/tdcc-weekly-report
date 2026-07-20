from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (
    RESOLUTION_CSV as MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    canonical_monthly_revenue_history_table_sha256,
    cross_market_resolution_registry_canonical_sha256,
    load_canonical_monthly_revenue_history,
    load_cross_market_resolutions,
    monthly_revenue_history_blob_sha256,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
ARTIFACT_VERSION = "source_first_condition_v3_20260720"

REVENUE_HISTORY_CSV = ROOT / "data/monthly_revenue_history/monthly_revenue_history.csv"
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
PRICE_RESOLUTION_CSV = ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"

LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"

DISCOVERY_HORIZON_DAYS = 126
OUTCOME_WINDOW_DAYS = 20
FIRST_HIT_DEADLINE_DAYS = 15
PRIMARY_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
BASELINE_VARIANT_ID = "absolute_strong"
INCREMENTAL_VARIANT_ID = "two_month_yoy_ge15_only"
KNOWN_SUCCESS_STOCK_IDS = ("4916", "1303")
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
NO_CROSS_MARKET_RESOLUTION_ID = "none"


@dataclass(frozen=True)
class ConditionSpec:
    condition_order: int
    condition_variant_id: str
    condition_family: str
    condition_rule: str
    decision_status: str


CONDITION_SPECS = (
    ConditionSpec(
        0,
        BASELINE_VARIANT_ID,
        "absolute_strength",
        "latest monthly revenue YoY >= 30% OR cumulative revenue YoY >= 20%",
        "baseline_anchor",
    ),
    ConditionSpec(
        10,
        "absolute_or_latest_yoy_ge15",
        "single_month_moderate_growth_sensitivity",
        "absolute_strong OR latest monthly revenue YoY >= 15%",
        "not_selected_broader_single_month_sensitivity",
    ),
    ConditionSpec(
        20,
        "absolute_or_two_month_yoy_ge10",
        "two_month_threshold_sweep",
        "absolute_strong OR latest revenue YoY >= 10% in two consecutive calendar months",
        "threshold_sweep_not_selected",
    ),
    ConditionSpec(
        30,
        "absolute_or_two_month_yoy_ge12_5",
        "two_month_threshold_sweep",
        "absolute_strong OR latest revenue YoY >= 12.5% in two consecutive calendar months",
        "threshold_sweep_not_selected",
    ),
    ConditionSpec(
        40,
        PRIMARY_VARIANT_ID,
        "two_month_moderate_growth",
        "absolute_strong OR latest revenue YoY >= 15% in two consecutive calendar months",
        "research_candidate_selected_for_forward_confirmation_audit",
    ),
    ConditionSpec(
        50,
        "absolute_or_two_month_yoy_ge17_5",
        "two_month_threshold_sweep",
        "absolute_strong OR latest revenue YoY >= 17.5% in two consecutive calendar months",
        "not_selected_case_boundary_overfit_risk",
    ),
    ConditionSpec(
        60,
        "absolute_or_two_month_yoy_ge18",
        "two_month_threshold_sweep",
        "absolute_strong OR latest revenue YoY >= 18% in two consecutive calendar months",
        "threshold_sweep_not_selected",
    ),
    ConditionSpec(
        70,
        "absolute_or_two_month_yoy_ge20",
        "two_month_threshold_sweep",
        "absolute_strong OR latest revenue YoY >= 20% in two consecutive calendar months",
        "not_selected_omits_known_success_1303",
    ),
    ConditionSpec(
        80,
        "absolute_or_two_month_yoy_ge25",
        "two_month_threshold_sweep",
        "absolute_strong OR latest revenue YoY >= 25% in two consecutive calendar months",
        "not_selected_omits_known_success_1303",
    ),
    ConditionSpec(
        90,
        "absolute_or_two_month_yoy_ge15_cumulative_improving",
        "two_month_combo_sensitivity",
        "absolute_strong OR two-month revenue YoY >= 15% with cumulative YoY improving",
        "not_selected_extra_combo_does_not_improve",
    ),
    ConditionSpec(
        100,
        "absolute_or_turn_positive_accel20",
        "turnaround_sensitivity",
        "absolute_strong OR latest revenue YoY turns positive with >= 20 percentage-point acceleration",
        "not_selected_lower_launch_discrimination",
    ),
    ConditionSpec(
        110,
        "absolute_or_positive_accel20",
        "acceleration_sensitivity",
        "absolute_strong OR positive latest revenue YoY with >= 20 percentage-point acceleration",
        "not_selected_lower_launch_discrimination",
    ),
    ConditionSpec(
        120,
        INCREMENTAL_VARIANT_ID,
        "incremental_path",
        "two consecutive calendar months with latest revenue YoY >= 15%, excluding absolute_strong rows",
        "incremental_path_evidence",
    ),
)

SUMMARY_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
    "condition_order",
    "condition_variant_id",
    "condition_family",
    "condition_rule",
    "source_event_count",
    "source_price_mapped_event_count",
    "source_missing_price_history_event_count",
    "source_left_censored_event_count",
    "source_after_price_history_event_count",
    "source_already_reacted_event_count",
    "source_price_unreacted_event_count",
    "candidate_episode_count",
    "unique_stock_count",
    "launch_count",
    "no_launch_count",
    "right_censored_count",
    "classifiable_episode_count",
    "retrospective_launch_rate_pct",
    "retrospective_launch_rate_wilson_low_pct",
    "retrospective_launch_rate_wilson_high_pct",
    "delta_vs_baseline_launch_rate_pct_points",
    "candidate_exclusion_episode_count",
    "excluding_candidate_launch_count",
    "excluding_candidate_no_launch_count",
    "excluding_candidate_classifiable_count",
    "retrospective_launch_rate_excluding_candidates_pct",
    "delta_vs_baseline_excluding_candidates_pct_points",
    "first_breakout_success_count",
    "first_breakout_failure_count",
    "first_breakout_right_censored_count",
    "first_breakout_classifiable_count",
    "first_breakout_strict_success_rate_pct",
    "known_success_4916_covered",
    "known_success_1303_covered",
    "source_revenue_anomaly_candidate_count",
    "price_path_threshold_candidate_count",
    "unresolved_price_path_candidate_count",
    "same_stock_overlap_pair_count",
    "right_censor_policy",
    "sample_policy",
    "anomaly_policy",
    "retrospective_label_status",
    "financial_statement_scope",
    "decision_status",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
]

DETAIL_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
    "condition_variant_id",
    "episode_key",
    "stock_id",
    "stock_name",
    "episode_number",
    "episode_start_revenue_period",
    "episode_start_source_date",
    "episode_start_cross_market_resolution_id",
    "episode_start_source_row_canonical_sha256",
    "episode_start_canonical_source_table_date",
    "episode_start_trade_date",
    "episode_start_sequence_index",
    "latest_qualifying_revenue_period",
    "latest_qualifying_source_date",
    "latest_qualifying_cross_market_resolution_id",
    "latest_qualifying_source_row_canonical_sha256",
    "latest_qualifying_canonical_source_table_date",
    "latest_qualifying_trade_date",
    "latest_qualifying_sequence_index",
    "qualifying_update_count",
    "qualifying_revenue_periods",
    "qualifying_source_dates",
    "qualifying_cross_market_resolution_ids",
    "qualifying_source_row_canonical_sha256s",
    "qualifying_canonical_source_table_dates",
    "qualifying_trade_dates",
    "qualifying_sequence_indices",
    "episode_end_sequence_index",
    "episode_end_date",
    "episode_status",
    "start_latest_revenue_yoy_pct",
    "start_cumulative_revenue_yoy_pct",
    "start_previous_latest_revenue_yoy_pct",
    "start_latest_yoy_delta_pct_points",
    "start_month_over_month_pct",
    "start_source_revenue_anomaly_candidate_flag",
    "qualifying_source_revenue_anomaly_candidate_flag",
    "source_price_unreacted_flag",
    "source_close",
    "source_return_5d_pct",
    "source_return_20d_pct",
    "source_volume_ratio",
    "source_range_width_23d_pct",
    "first_breakout_date",
    "first_breakout_lag_from_episode_start_days",
    "first_breakout_outcome",
    "first_breakout_d20_return_pct",
    "launch_date",
    "launch_lag_from_episode_start_days",
    "launch_lag_from_latest_source_days",
    "first_hit_20_day_offset",
    "launch_d20_return_pct",
    "launch_post_hit_min_return_pct",
    "price_path_threshold_candidate_flag",
    "price_path_resolution_ids",
    "unresolved_price_path_candidate_flag",
    "same_stock_non_overlap_applied",
    "right_censored_flag",
    "retrospective_label_status",
    "financial_statement_scope",
    "approved_for_daily",
    "production_change",
]


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _normalize_stock_id(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text else ""


def _normalize_date(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace(r"\D", "", regex=True).str[:8]


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _stable(value: object, digits: int = 4) -> float | str:
    number = _number(value)
    return "" if number is None else round(number, digits)


def _cross_market_resolution_id(value: object) -> str:
    text = str(value).strip()
    return text if text else NO_CROSS_MARKET_RESOLUTION_ID


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _wilson(successes: int, total: int) -> tuple[float | str, float | str]:
    if total <= 0:
        return "", ""
    z = 1.959963984540054
    p = successes / total
    denominator = 1.0 + z * z / total
    center = (p + z * z / (2.0 * total)) / denominator
    margin = z * np.sqrt((p * (1.0 - p) + z * z / (4.0 * total)) / total) / denominator
    return round((center - margin) * 100.0, 4), round((center + margin) * 100.0, 4)


def _period_ordinal(series: pd.Series) -> pd.Series:
    text = series.astype(str).str.replace(r"\D", "", regex=True).str[:6]
    year = pd.to_numeric(text.str[:4], errors="coerce")
    month = pd.to_numeric(text.str[4:6], errors="coerce")
    return year * 12 + month


def load_revenue_history(
    path: Path = REVENUE_HISTORY_CSV,
    resolution_path: Path = MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
) -> pd.DataFrame:
    frame = load_canonical_monthly_revenue_history(path, resolution_path)
    required = {
        "stock_id",
        "stock_name",
        "revenue_period",
        "source_table_date",
        "source_row_canonical_sha256",
        "cross_market_resolution_id",
        "canonical_source_table_date",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
        "revenue_numerical_anomaly_flag",
        "research_join_allowed",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"source-first revenue history is missing columns: {missing}")
    frame = frame.copy()
    frame["stock_id"] = frame["stock_id"].map(_normalize_stock_id)
    frame["source_table_date"] = _normalize_date(frame["source_table_date"])
    frame["canonical_source_table_date"] = _normalize_date(
        frame["canonical_source_table_date"]
    )
    frame["source_row_canonical_sha256"] = (
        frame["source_row_canonical_sha256"].astype(str).str.strip().str.lower()
    )
    if not frame["source_row_canonical_sha256"].str.fullmatch(r"[0-9a-f]{64}").all():
        raise RuntimeError("source-first revenue history has invalid canonical row SHA-256")
    frame["cross_market_resolution_id"] = (
        frame["cross_market_resolution_id"].astype(str).str.strip()
    )
    if (
        ~frame["canonical_source_table_date"].str.fullmatch(r"\d{8}")
        | frame["canonical_source_table_date"].ne(frame["source_table_date"])
    ).any():
        raise RuntimeError(
            "source-first revenue history canonical source date does not match the selected source row"
        )
    frame["revenue_period"] = frame["revenue_period"].astype(str).str.replace(r"\D", "", regex=True).str[:6]
    for column in (
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
    ):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.sort_values(
        ["stock_id", "source_table_date", "revenue_period"],
        kind="mergesort",
    )
    if frame.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("source-first revenue history contains unresolved stock-period duplicates")
    grouped = frame.groupby("stock_id", sort=False, dropna=False)
    frame["previous_latest_revenue_yoy_pct"] = grouped["latest_revenue_yoy_pct"].shift(1)
    frame["previous_cumulative_revenue_yoy_pct"] = grouped["cumulative_revenue_yoy_pct"].shift(1)
    frame["previous_revenue_period"] = grouped["revenue_period"].shift(1)
    frame["latest_yoy_delta_pct_points"] = (
        frame["latest_revenue_yoy_pct"] - frame["previous_latest_revenue_yoy_pct"]
    )
    frame["cumulative_yoy_delta_pct_points"] = (
        frame["cumulative_revenue_yoy_pct"] - frame["previous_cumulative_revenue_yoy_pct"]
    )
    frame["consecutive_calendar_month_flag"] = (
        _period_ordinal(frame["revenue_period"])
        - _period_ordinal(frame["previous_revenue_period"])
    ).eq(1)
    frame["absolute_strong_flag"] = (
        frame["latest_revenue_yoy_pct"].ge(30.0)
        | frame["cumulative_revenue_yoy_pct"].ge(20.0)
    )
    frame["research_join_allowed_flag"] = _boolish(frame["research_join_allowed"])
    frame["source_revenue_anomaly_candidate_flag"] = _boolish(
        frame["revenue_numerical_anomaly_flag"]
    )
    return frame.reset_index(drop=True)


def _monthly_revenue_run_lineage(
    revenue: pd.DataFrame,
    *,
    revenue_path: Path,
    resolution_path: Path,
) -> dict[str, str]:
    return {
        "monthly_revenue_history_blob_sha256": monthly_revenue_history_blob_sha256(
            revenue_path
        ),
        "monthly_revenue_canonical_table_sha256": (
            canonical_monthly_revenue_history_table_sha256(revenue)
        ),
        "cross_market_resolution_registry_canonical_sha256": (
            cross_market_resolution_registry_canonical_sha256(
                load_cross_market_resolutions(resolution_path)
            )
        ),
    }


def condition_masks(revenue: pd.DataFrame) -> dict[str, pd.Series]:
    latest = revenue["latest_revenue_yoy_pct"]
    previous = revenue["previous_latest_revenue_yoy_pct"]
    absolute = revenue["absolute_strong_flag"]
    consecutive = revenue["consecutive_calendar_month_flag"]

    def two_month(threshold: float) -> pd.Series:
        return consecutive & latest.ge(threshold) & previous.ge(threshold)

    turn_positive = (
        latest.gt(0.0)
        & previous.le(0.0)
        & revenue["latest_yoy_delta_pct_points"].ge(20.0)
    )
    positive_acceleration = latest.gt(0.0) & revenue["latest_yoy_delta_pct_points"].ge(20.0)
    masks = {
        BASELINE_VARIANT_ID: absolute,
        "absolute_or_latest_yoy_ge15": absolute | latest.ge(15.0),
        "absolute_or_two_month_yoy_ge10": absolute | two_month(10.0),
        "absolute_or_two_month_yoy_ge12_5": absolute | two_month(12.5),
        PRIMARY_VARIANT_ID: absolute | two_month(15.0),
        "absolute_or_two_month_yoy_ge17_5": absolute | two_month(17.5),
        "absolute_or_two_month_yoy_ge18": absolute | two_month(18.0),
        "absolute_or_two_month_yoy_ge20": absolute | two_month(20.0),
        "absolute_or_two_month_yoy_ge25": absolute | two_month(25.0),
        "absolute_or_two_month_yoy_ge15_cumulative_improving": (
            absolute | (two_month(15.0) & revenue["cumulative_yoy_delta_pct_points"].gt(0.0))
        ),
        "absolute_or_turn_positive_accel20": absolute | turn_positive,
        "absolute_or_positive_accel20": absolute | positive_acceleration,
        INCREMENTAL_VARIANT_ID: two_month(15.0) & ~absolute,
    }
    return {key: value.fillna(False) for key, value in masks.items()}


def _load_price_resolutions() -> pd.DataFrame:
    if not PRICE_RESOLUTION_CSV.is_file():
        return pd.DataFrame(columns=["stock_id", "resume_date", "exchange_ratio", "resolution_id"])
    frame = pd.read_csv(PRICE_RESOLUTION_CSV, dtype={"stock_id": str}, keep_default_na=False)
    required = {"stock_id", "resume_date", "exchange_ratio", "resolution_id", "root_cause_status"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"source-first price resolution is missing columns: {missing}")
    frame = frame.loc[
        frame["root_cause_status"].eq("verified_non_comparable_raw_price_scale")
    ].copy()
    frame["stock_id"] = frame["stock_id"].map(_normalize_stock_id)
    frame["resume_date"] = _normalize_date(frame["resume_date"])
    frame["exchange_ratio"] = pd.to_numeric(frame["exchange_ratio"], errors="coerce")
    return frame


def load_stock_price(
    stock_id: str,
    path: Path,
    resolutions: pd.DataFrame,
) -> pd.DataFrame:
    frame = pd.read_csv(path, low_memory=False)
    required = {"date", "open", "high", "low", "close", "volume", "volume_ratio"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"source-first price history is missing columns for {stock_id}: {missing}")
    frame = frame.copy()
    frame["date"] = _normalize_date(frame["date"])
    frame = frame.sort_values("date", kind="mergesort").drop_duplicates("date", keep="last")
    for column in ("open", "high", "low", "close", "volume", "volume_ratio"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna(subset=["close"]).reset_index(drop=True)
    frame["raw_close"] = frame["close"]
    frame["analysis_price_adjustment_factor"] = 1.0
    frame["price_resolution_ids_on_date"] = ""
    stock_resolutions = resolutions.loc[resolutions["stock_id"].eq(stock_id)]
    for event in stock_resolutions.itertuples(index=False):
        ratio = float(event.exchange_ratio)
        frame.loc[frame["date"].lt(str(event.resume_date)), "analysis_price_adjustment_factor"] *= (
            1.0 / ratio
        )
        frame.loc[frame["date"].eq(str(event.resume_date)), "price_resolution_ids_on_date"] = str(
            event.resolution_id
        )
    frame["analysis_close"] = frame["raw_close"] * frame["analysis_price_adjustment_factor"]
    close = frame["analysis_close"]
    frame["analysis_return_1d_pct"] = close.pct_change() * 100.0
    frame["analysis_return_5d_pct"] = close.pct_change(5) * 100.0
    frame["analysis_return_20d_pct"] = close.pct_change(20) * 100.0
    frame["previous_20d_highest_close"] = close.shift(1).rolling(20, min_periods=20).max()
    frame["previous_23d_highest_close"] = close.shift(1).rolling(23, min_periods=20).max()
    frame["previous_23d_lowest_close"] = close.shift(1).rolling(23, min_periods=20).min()
    frame["range_width_23d_pct"] = (
        frame["previous_23d_highest_close"] / frame["previous_23d_lowest_close"] - 1.0
    ) * 100.0
    frame["close_breakout_prev20"] = close.gt(frame["previous_20d_highest_close"])
    frame["range_breakout_prev20_pct"] = (
        close / frame["previous_20d_highest_close"] - 1.0
    ) * 100.0
    frame["close_location_pct"] = np.where(
        frame["high"].gt(frame["low"]),
        (frame["close"] - frame["low"]) / (frame["high"] - frame["low"]) * 100.0,
        100.0,
    )
    frame["locked_limit_up_like"] = (
        frame["analysis_return_1d_pct"].ge(9.0)
        & frame["close"].ge(frame["high"] - 1e-9)
    )
    volume_ma20 = frame["volume"].shift(1).rolling(20, min_periods=20).mean()
    normal_attack = (
        frame["volume_ratio"].ge(2.0)
        & frame["range_breakout_prev20_pct"].ge(2.0)
        & volume_ma20.ge(1_000_000.0)
        & frame["close"].gt(frame["open"])
    )
    frame["active_attack_flag"] = (
        normal_attack
        | frame["locked_limit_up_like"]
        | frame["volume_ratio"].ge(2.5)
        | frame["analysis_return_5d_pct"].ge(8.0)
        | frame["analysis_return_20d_pct"].ge(20.0)
    )
    frame["price_unreacted_flag"] = (
        frame["analysis_close"].ge(frame["previous_23d_lowest_close"] * 0.95)
        & frame["analysis_close"].le(frame["previous_23d_highest_close"] * 1.05)
        & ~frame["active_attack_flag"]
    ).fillna(False)
    frame["raw_price_jump_threshold_candidate_flag"] = (
        frame["raw_close"].pct_change().abs().ge(0.80)
    )
    frame["analysis_price_jump_threshold_candidate_flag"] = (
        frame["analysis_close"].pct_change().abs().ge(0.80)
    )
    return frame.reset_index(drop=True)


def _strict_launch_metrics(price: pd.DataFrame, index: int) -> dict[str, object]:
    if index + OUTCOME_WINDOW_DAYS >= len(price):
        return {
            "mature": False,
            "strict_success": False,
            "first_hit_offset": "",
            "d20_return_pct": "",
            "post_hit_min_return_pct": "",
        }
    base = float(price.at[index, "analysis_close"])
    closes = pd.to_numeric(
        price.loc[index : index + OUTCOME_WINDOW_DAYS, "analysis_close"],
        errors="coerce",
    )
    first_window = closes.iloc[: FIRST_HIT_DEADLINE_DAYS + 1]
    hits = np.flatnonzero(first_window.to_numpy(dtype=float) >= base * 1.20)
    first_hit = int(hits[0]) if len(hits) else None
    post_min = ""
    strict = False
    if first_hit is not None:
        post_min = float(closes.iloc[first_hit:].min() / base - 1.0) * 100.0
        strict = post_min >= 20.0 - 1e-9
    return {
        "mature": True,
        "strict_success": strict,
        "first_hit_offset": first_hit if first_hit is not None else "",
        "d20_return_pct": float(closes.iloc[-1] / base - 1.0) * 100.0,
        "post_hit_min_return_pct": post_min,
    }


def _source_events(
    revenue: pd.DataFrame,
    mask: pd.Series,
    price: pd.DataFrame,
) -> tuple[list[tuple[int, pd.Series]], dict[str, int]]:
    dates = price["date"].to_numpy(dtype=str)
    events: list[tuple[int, pd.Series]] = []
    counts = {
        "mapped": 0,
        "left_censored": 0,
        "after_history": 0,
        "already_reacted": 0,
        "unreacted": 0,
    }
    for index, row in revenue.loc[mask & revenue["research_join_allowed_flag"]].iterrows():
        source_date = str(row["source_table_date"])
        price_index = int(np.searchsorted(dates, source_date, side="left"))
        if source_date < str(dates[0]):
            counts["left_censored"] += 1
            continue
        if price_index >= len(price):
            counts["after_history"] += 1
            continue
        counts["mapped"] += 1
        if bool(price.at[price_index, "price_unreacted_flag"]):
            events.append((price_index, row))
            counts["unreacted"] += 1
        else:
            counts["already_reacted"] += 1
    return (
        sorted(events, key=lambda item: (item[0], str(item[1]["revenue_period"]))),
        counts,
    )


def _episode_rows(
    *,
    generated_at: str,
    stock_id: str,
    stock_name: str,
    variant_id: str,
    events: list[tuple[int, pd.Series]],
    price: pd.DataFrame,
    monthly_revenue_run_lineage: dict[str, str],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    position = 0
    episode_number = 0
    while position < len(events):
        start_index, start_event = events[position]
        latest_index = start_index
        used = [events[position]]
        position += 1
        natural_expiry = latest_index + DISCOVERY_HORIZON_DAYS
        day = start_index
        first_breakout_index: int | None = None
        launch_index: int | None = None

        while day <= min(natural_expiry, len(price) - 1):
            while position < len(events) and events[position][0] <= day:
                latest_index = events[position][0]
                used.append(events[position])
                position += 1
                natural_expiry = latest_index + DISCOVERY_HORIZON_DAYS
            if bool(price.at[day, "close_breakout_prev20"]):
                if first_breakout_index is None:
                    first_breakout_index = day
                metrics = _strict_launch_metrics(price, day)
                if bool(metrics["strict_success"]):
                    launch_index = day
                    break
            day += 1

        if launch_index is not None:
            episode_status = "launch_within_active_horizon"
            episode_end_index = launch_index
        elif natural_expiry < len(price):
            episode_status = "no_launch_within_active_horizon"
            episode_end_index = natural_expiry
        else:
            episode_status = "right_censored_before_active_horizon"
            episode_end_index = len(price) - 1

        first_metrics = (
            _strict_launch_metrics(price, first_breakout_index)
            if first_breakout_index is not None
            else None
        )
        if first_metrics is None:
            first_outcome = "no_breakout_observed"
        elif not bool(first_metrics["mature"]):
            first_outcome = "right_censored_before_d20"
        elif bool(first_metrics["strict_success"]):
            first_outcome = "strict_success"
        else:
            first_outcome = "mature_failure"
        launch_metrics = (
            _strict_launch_metrics(price, launch_index) if launch_index is not None else None
        )

        observation = price.loc[start_index:episode_end_index]
        raw_candidate = bool(observation["raw_price_jump_threshold_candidate_flag"].fillna(False).any())
        adjusted_candidate = bool(
            observation["analysis_price_jump_threshold_candidate_flag"].fillna(False).any()
        )
        resolution_ids = sorted(
            {
                value
                for value in observation["price_resolution_ids_on_date"].astype(str)
                if value
            }
        )
        latest_event = used[-1][1]
        episode_number += 1
        episode_key = (
            f"{variant_id}|{stock_id}|{start_event['source_table_date']}|{episode_number}"
        )
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                **monthly_revenue_run_lineage,
                "condition_variant_id": variant_id,
                "episode_key": episode_key,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "episode_number": episode_number,
                "episode_start_revenue_period": str(start_event["revenue_period"]),
                "episode_start_source_date": str(start_event["source_table_date"]),
                "episode_start_cross_market_resolution_id": (
                    _cross_market_resolution_id(
                        start_event["cross_market_resolution_id"]
                    )
                ),
                "episode_start_source_row_canonical_sha256": str(
                    start_event["source_row_canonical_sha256"]
                ),
                "episode_start_canonical_source_table_date": str(
                    start_event["canonical_source_table_date"]
                ),
                "episode_start_trade_date": str(price.at[start_index, "date"]),
                "episode_start_sequence_index": start_index,
                "latest_qualifying_revenue_period": str(latest_event["revenue_period"]),
                "latest_qualifying_source_date": str(latest_event["source_table_date"]),
                "latest_qualifying_cross_market_resolution_id": (
                    _cross_market_resolution_id(
                        latest_event["cross_market_resolution_id"]
                    )
                ),
                "latest_qualifying_source_row_canonical_sha256": str(
                    latest_event["source_row_canonical_sha256"]
                ),
                "latest_qualifying_canonical_source_table_date": str(
                    latest_event["canonical_source_table_date"]
                ),
                "latest_qualifying_trade_date": str(price.at[latest_index, "date"]),
                "latest_qualifying_sequence_index": latest_index,
                "qualifying_update_count": len(used),
                "qualifying_revenue_periods": "|".join(
                    str(event[1]["revenue_period"]) for event in used
                ),
                "qualifying_source_dates": "|".join(
                    str(event[1]["source_table_date"]) for event in used
                ),
                "qualifying_cross_market_resolution_ids": "|".join(
                    _cross_market_resolution_id(
                        event[1]["cross_market_resolution_id"]
                    )
                    for event in used
                ),
                "qualifying_source_row_canonical_sha256s": "|".join(
                    str(event[1]["source_row_canonical_sha256"])
                    for event in used
                ),
                "qualifying_canonical_source_table_dates": "|".join(
                    str(event[1]["canonical_source_table_date"])
                    for event in used
                ),
                "qualifying_trade_dates": "|".join(
                    str(price.at[event[0], "date"]) for event in used
                ),
                "qualifying_sequence_indices": "|".join(
                    str(event[0]) for event in used
                ),
                "episode_end_sequence_index": episode_end_index,
                "episode_end_date": str(price.at[episode_end_index, "date"]),
                "episode_status": episode_status,
                "start_latest_revenue_yoy_pct": _stable(start_event["latest_revenue_yoy_pct"]),
                "start_cumulative_revenue_yoy_pct": _stable(
                    start_event["cumulative_revenue_yoy_pct"]
                ),
                "start_previous_latest_revenue_yoy_pct": _stable(
                    start_event["previous_latest_revenue_yoy_pct"]
                ),
                "start_latest_yoy_delta_pct_points": _stable(
                    start_event["latest_yoy_delta_pct_points"]
                ),
                "start_month_over_month_pct": _stable(start_event["month_over_month_pct"]),
                "start_source_revenue_anomaly_candidate_flag": bool(
                    start_event["source_revenue_anomaly_candidate_flag"]
                ),
                "qualifying_source_revenue_anomaly_candidate_flag": any(
                    bool(event[1]["source_revenue_anomaly_candidate_flag"])
                    for event in used
                ),
                "source_price_unreacted_flag": True,
                "source_close": _stable(price.at[start_index, "analysis_close"]),
                "source_return_5d_pct": _stable(price.at[start_index, "analysis_return_5d_pct"]),
                "source_return_20d_pct": _stable(
                    price.at[start_index, "analysis_return_20d_pct"]
                ),
                "source_volume_ratio": _stable(price.at[start_index, "volume_ratio"]),
                "source_range_width_23d_pct": _stable(price.at[start_index, "range_width_23d_pct"]),
                "first_breakout_date": (
                    str(price.at[first_breakout_index, "date"])
                    if first_breakout_index is not None
                    else ""
                ),
                "first_breakout_lag_from_episode_start_days": (
                    first_breakout_index - start_index
                    if first_breakout_index is not None
                    else ""
                ),
                "first_breakout_outcome": first_outcome,
                "first_breakout_d20_return_pct": (
                    _stable(first_metrics["d20_return_pct"])
                    if first_metrics is not None
                    else ""
                ),
                "launch_date": (
                    str(price.at[launch_index, "date"])
                    if launch_index is not None
                    else ""
                ),
                "launch_lag_from_episode_start_days": (
                    launch_index - start_index if launch_index is not None else ""
                ),
                "launch_lag_from_latest_source_days": (
                    launch_index - latest_index if launch_index is not None else ""
                ),
                "first_hit_20_day_offset": (
                    launch_metrics["first_hit_offset"] if launch_metrics is not None else ""
                ),
                "launch_d20_return_pct": (
                    _stable(launch_metrics["d20_return_pct"])
                    if launch_metrics is not None
                    else ""
                ),
                "launch_post_hit_min_return_pct": (
                    _stable(launch_metrics["post_hit_min_return_pct"])
                    if launch_metrics is not None
                    else ""
                ),
                "price_path_threshold_candidate_flag": raw_candidate,
                "price_path_resolution_ids": ";".join(resolution_ids),
                "unresolved_price_path_candidate_flag": adjusted_candidate,
                "same_stock_non_overlap_applied": True,
                "right_censored_flag": episode_status.startswith("right_censored"),
                "retrospective_label_status": (
                    "research_only_future_outcome_label_not_tradable_confirmation"
                ),
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "production_change": False,
            }
        )
    return rows


def build_source_first_condition_audit(
    revenue_path: Path = REVENUE_HISTORY_CSV,
    price_dir: Path = PRICE_HISTORY_DIR,
    resolution_path: Path = MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    generated_at = _now_text()
    revenue = load_revenue_history(revenue_path, resolution_path)
    monthly_revenue_run_lineage = _monthly_revenue_run_lineage(
        revenue,
        revenue_path=revenue_path,
        resolution_path=resolution_path,
    )
    masks = condition_masks(revenue)
    resolutions = _load_price_resolutions()
    rows: list[dict[str, object]] = []
    price_paths = sorted(price_dir.glob("*.csv"))
    price_stock_ids = {_normalize_stock_id(path.stem) for path in price_paths}
    source_counts = {
        spec.condition_variant_id: int(
            (
                masks[spec.condition_variant_id]
                & revenue["research_join_allowed_flag"]
            ).sum()
        )
        for spec in CONDITION_SPECS
    }
    source_partitions = {
        spec.condition_variant_id: {
            "missing_price_history": int(
                (
                    masks[spec.condition_variant_id]
                    & revenue["research_join_allowed_flag"]
                    & ~revenue["stock_id"].isin(price_stock_ids)
                ).sum()
            ),
            "mapped": 0,
            "left_censored": 0,
            "after_history": 0,
            "already_reacted": 0,
            "unreacted": 0,
        }
        for spec in CONDITION_SPECS
    }

    for path in price_paths:
        stock_id = _normalize_stock_id(path.stem)
        stock_revenue = revenue.loc[revenue["stock_id"].eq(stock_id)].copy()
        if stock_revenue.empty:
            continue
        price = load_stock_price(stock_id, path, resolutions)
        if price.empty:
            continue
        stock_name = str(stock_revenue["stock_name"].iloc[-1])
        for spec in CONDITION_SPECS:
            local_mask = masks[spec.condition_variant_id].loc[stock_revenue.index]
            events, event_counts = _source_events(stock_revenue, local_mask, price)
            for key, value in event_counts.items():
                source_partitions[spec.condition_variant_id][key] += value
            rows.extend(
                _episode_rows(
                    generated_at=generated_at,
                    stock_id=stock_id,
                    stock_name=stock_name,
                    variant_id=spec.condition_variant_id,
                    events=events,
                    price=price,
                    monthly_revenue_run_lineage=monthly_revenue_run_lineage,
                )
            )

    detail = pd.DataFrame(rows, columns=DETAIL_COLUMNS)
    summary_rows: list[dict[str, object]] = []
    for spec in CONDITION_SPECS:
        part = detail.loc[detail["condition_variant_id"].eq(spec.condition_variant_id)].copy()
        launch = part["episode_status"].eq("launch_within_active_horizon")
        no_launch = part["episode_status"].eq("no_launch_within_active_horizon")
        right_censored = part["episode_status"].eq("right_censored_before_active_horizon")
        classifiable = int(launch.sum() + no_launch.sum())
        launch_count = int(launch.sum())
        low, high = _wilson(launch_count, classifiable)
        first_success = part["first_breakout_outcome"].eq("strict_success")
        first_failure = part["first_breakout_outcome"].eq("mature_failure")
        first_censored = part["first_breakout_outcome"].eq("right_censored_before_d20")
        first_classifiable = int(first_success.sum() + first_failure.sum())
        known = part.loc[
            part["stock_id"].isin(KNOWN_SUCCESS_STOCK_IDS)
            & part["episode_status"].eq("launch_within_active_horizon")
        ]
        exclusion_candidate = (
            _boolish(part["qualifying_source_revenue_anomaly_candidate_flag"])
            | _boolish(part["unresolved_price_path_candidate_flag"])
        )
        clean = part.loc[~exclusion_candidate].copy()
        clean_launch = clean["episode_status"].eq("launch_within_active_horizon")
        clean_no_launch = clean["episode_status"].eq("no_launch_within_active_horizon")
        clean_classifiable = int(clean_launch.sum() + clean_no_launch.sum())
        overlap_pairs = 0
        for _stock_id, stock in part.groupby("stock_id", sort=False):
            ordered = stock.sort_values("episode_start_sequence_index", kind="mergesort")
            starts = pd.to_numeric(ordered["episode_start_sequence_index"], errors="coerce")
            prior_ends = pd.to_numeric(ordered["episode_end_sequence_index"], errors="coerce").shift(1)
            overlap_pairs += int(starts.le(prior_ends).fillna(False).sum())
        summary_rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                **monthly_revenue_run_lineage,
                "condition_order": spec.condition_order,
                "condition_variant_id": spec.condition_variant_id,
                "condition_family": spec.condition_family,
                "condition_rule": spec.condition_rule,
                "source_event_count": source_counts[spec.condition_variant_id],
                "source_price_mapped_event_count": source_partitions[
                    spec.condition_variant_id
                ]["mapped"],
                "source_missing_price_history_event_count": source_partitions[
                    spec.condition_variant_id
                ]["missing_price_history"],
                "source_left_censored_event_count": source_partitions[
                    spec.condition_variant_id
                ]["left_censored"],
                "source_after_price_history_event_count": source_partitions[
                    spec.condition_variant_id
                ]["after_history"],
                "source_already_reacted_event_count": source_partitions[
                    spec.condition_variant_id
                ]["already_reacted"],
                "source_price_unreacted_event_count": source_partitions[
                    spec.condition_variant_id
                ]["unreacted"],
                "candidate_episode_count": len(part),
                "unique_stock_count": part["stock_id"].nunique(),
                "launch_count": launch_count,
                "no_launch_count": int(no_launch.sum()),
                "right_censored_count": int(right_censored.sum()),
                "classifiable_episode_count": classifiable,
                "retrospective_launch_rate_pct": _rate(launch_count, classifiable),
                "retrospective_launch_rate_wilson_low_pct": low,
                "retrospective_launch_rate_wilson_high_pct": high,
                "delta_vs_baseline_launch_rate_pct_points": "",
                "candidate_exclusion_episode_count": int(exclusion_candidate.sum()),
                "excluding_candidate_launch_count": int(clean_launch.sum()),
                "excluding_candidate_no_launch_count": int(clean_no_launch.sum()),
                "excluding_candidate_classifiable_count": clean_classifiable,
                "retrospective_launch_rate_excluding_candidates_pct": _rate(
                    int(clean_launch.sum()), clean_classifiable
                ),
                "delta_vs_baseline_excluding_candidates_pct_points": "",
                "first_breakout_success_count": int(first_success.sum()),
                "first_breakout_failure_count": int(first_failure.sum()),
                "first_breakout_right_censored_count": int(first_censored.sum()),
                "first_breakout_classifiable_count": first_classifiable,
                "first_breakout_strict_success_rate_pct": _rate(
                    int(first_success.sum()), first_classifiable
                ),
                "known_success_4916_covered": known["stock_id"].eq("4916").any(),
                "known_success_1303_covered": known["stock_id"].eq("1303").any(),
                "source_revenue_anomaly_candidate_count": int(
                    _boolish(part["qualifying_source_revenue_anomaly_candidate_flag"]).sum()
                ),
                "price_path_threshold_candidate_count": int(
                    _boolish(part["price_path_threshold_candidate_flag"]).sum()
                ),
                "unresolved_price_path_candidate_count": int(
                    _boolish(part["unresolved_price_path_candidate_flag"]).sum()
                ),
                "same_stock_overlap_pair_count": overlap_pairs,
                "right_censor_policy": (
                    "rows without 126 trading days after the latest qualifying source are right-censored, not failures"
                ),
                "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
                "anomaly_policy": (
                    "threshold candidates retained until bottom-level root-cause verification; verified model-owned price resolutions applied"
                ),
                "retrospective_label_status": (
                    "research_only_eventual_launch_discrimination_not_operation_win_rate"
                ),
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "decision_status": spec.decision_status,
                "approved_for_daily": False,
                "production_change": False,
                "promotion_readiness": (
                    "blocked_pending_forward_first_breakout_confirmation_feature_audit"
                ),
            }
        )
    summary = pd.DataFrame(summary_rows, columns=SUMMARY_COLUMNS)
    baseline_rate = _number(
        summary.loc[
            summary["condition_variant_id"].eq(BASELINE_VARIANT_ID),
            "retrospective_launch_rate_pct",
        ].iloc[0]
    )
    if baseline_rate is not None:
        current = pd.to_numeric(summary["retrospective_launch_rate_pct"], errors="coerce")
        summary["delta_vs_baseline_launch_rate_pct_points"] = (current - baseline_rate).round(4)
    clean_baseline_rate = _number(
        summary.loc[
            summary["condition_variant_id"].eq(BASELINE_VARIANT_ID),
            "retrospective_launch_rate_excluding_candidates_pct",
        ].iloc[0]
    )
    if clean_baseline_rate is not None:
        current_clean = pd.to_numeric(
            summary["retrospective_launch_rate_excluding_candidates_pct"],
            errors="coerce",
        )
        summary["delta_vs_baseline_excluding_candidates_pct_points"] = (
            current_clean - clean_baseline_rate
        ).round(4)
    return summary, detail


def _markdown(summary: pd.DataFrame, detail: pd.DataFrame) -> str:
    selected = summary.loc[summary["condition_variant_id"].eq(PRIMARY_VARIANT_ID)].iloc[0]
    known = detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["stock_id"].isin(KNOWN_SUCCESS_STOCK_IDS)
        & detail["episode_status"].eq("launch_within_active_horizon")
    ].copy()
    summary_columns = [
        "condition_variant_id",
        "source_event_count",
        "source_missing_price_history_event_count",
        "source_left_censored_event_count",
        "source_after_price_history_event_count",
        "source_already_reacted_event_count",
        "source_price_unreacted_event_count",
        "candidate_episode_count",
        "launch_count",
        "no_launch_count",
        "right_censored_count",
        "retrospective_launch_rate_pct",
        "retrospective_launch_rate_excluding_candidates_pct",
        "delta_vs_baseline_launch_rate_pct_points",
        "delta_vs_baseline_excluding_candidates_pct_points",
        "first_breakout_strict_success_rate_pct",
        "known_success_4916_covered",
        "known_success_1303_covered",
        "decision_status",
    ]
    known_columns = [
        "stock_id",
        "episode_start_source_date",
        "latest_qualifying_source_date",
        "first_breakout_date",
        "first_breakout_outcome",
        "launch_date",
        "launch_lag_from_latest_source_days",
        "first_hit_20_day_offset",
        "launch_d20_return_pct",
        "launch_post_hit_min_return_pct",
    ]
    lines = [
        "# 營收尚未反應模型：來源優先條件稽核",
        "",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        "- 狀態：research-only；未修改 production registry、operation adapter、ranking 或 PDF。",
        "- 核心修正：先從 PIT 月營收來源建立候選，不再用已發生的訊號日反推 8～14 日延遲，也不再要求連續三個月同時達到 30%/20%。",
        "- 候選價格語意：來源可得日第一個交易日仍位於前 23 日收盤區間的 95%～105%，且尚未出現既定主攻擊條件。",
        "- 建議 research 候選：最新年增 >=30% 或累計年增 >=20%；或連續兩個曆月的單月年增均 >=15%。",
        "- 15% 是 12.5%～18% 正向區間內的中間整數門檻；未採用樣本內最高的 17.5%，避免貼近南亞 18.05% 的個案邊界調參。",
        "- 已知涵蓋案例：事欣科（4916）與南亞（1303）均落入建議 research 候選並形成嚴格事後成功。",
        "- 限制：兩月 15% 的增量路徑單獨辨識力偏弱，只能用來擴充下一輪確認訊號研究母體，尚不能成為正式 required gate。",
        "- 事後發動標籤：候選有效期內，任一收盤突破前 20 日最高收盤後，15 日內收盤達 +20%，且從首次達標到 D+20 每日收盤均維持 >=+20%。",
        "- 重要限制：retrospective_launch_rate_pct 是最終是否發動的辨識率，不是正式買入勝率；first_breakout_strict_success_rate_pct 才是第一個可觀察突破的前向壓力測試。",
        f"- 建議條件辨識率：{selected['retrospective_launch_rate_pct']}%；第一個突破嚴格成功率：{selected['first_breakout_strict_success_rate_pct']}%。",
        f"- 排除尚未完成底層查核的 anomaly candidates 後，建議條件辨識率為 {selected['retrospective_launch_rate_excluding_candidates_pct']}%。",
        "- 右設限：最新 qualifying source 後不足 126 個交易日者不列失敗。",
        "- 異常規則：高低數字只產生 candidate；未查到底層原因前保留在 primary，不能直接命名或排除為極端值。",
        f"- 財報範圍：`{FINANCIAL_STATEMENT_SCOPE}`。EPS、毛利率、營益率、營業利益、業外與淨利均未納入。",
        "- promotion blocker：必須先解決第一個突破可能失敗的 confirmation 問題，再用 close-confirmed、隔日開盤的 operation basis 重算勝／和／敗與報酬。",
        "",
        "## 條件矩陣",
        "",
        summary[summary_columns].to_markdown(index=False),
        "",
        "## 已知成功案例",
        "",
        known[known_columns].to_markdown(index=False),
        "",
    ]
    return "\n".join(lines)


def write_source_first_condition_audit(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    for path, frame in (
        (LATEST_CSV, summary),
        (DETAIL_CSV, detail),
        (HISTORY_CSV, summary),
        (DOCS_CSV, summary),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")
    markdown = _markdown(summary, detail)
    for path in (LATEST_MD, DOCS_MD):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    built_summary, built_detail = build_source_first_condition_audit()
    write_source_first_condition_audit(built_summary, built_detail)
    print(
        f"wrote {LATEST_CSV.relative_to(ROOT)} rows={len(built_summary)} "
        f"detail_rows={len(built_detail)}"
    )
