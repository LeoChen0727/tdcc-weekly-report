from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_deep_low_base_matrix_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_deep_low_base_matrix_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_deep_low_base_matrix_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_deep_low_base_matrix.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_deep_low_base_matrix_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_deep_low_base_matrix"
ARTIFACT_VERSION = "volume_range_breakout_v2_deep_low_base_matrix_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_raw_market_rerun"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

RETURN_KEY = "return_pct"

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "matrix_family",
    "condition_set_id",
    "condition_set_label",
    "population_basis",
    "requires_60d_high_breakout",
    "requires_next_day_continuation",
    "deep_low_window_days",
    "deep_low_threshold_pct",
    "range_window_days",
    "range_width_threshold_pct",
    "extra_gate",
    "baseline_sample_size",
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
    "sample_status",
    "win_rate_delta_pct",
    "loss_rate_delta_pct",
    "avg_return_delta_pct",
    "median_return_delta_pct",
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
    "advisory_status",
    "model_id",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "return_pct",
    "return_outcome",
    "exit_reason",
    "holding_days",
    "mfe_pct",
    "mae_pct",
    "signal_close",
    "previous_60d_high",
    "previous_60d_low",
    "previous_120d_high",
    "previous_120d_low",
    "previous_240d_high",
    "previous_240d_low",
    "off_60d_low_pct",
    "off_120d_low_pct",
    "off_240d_low_pct",
    "range_width_60_pct",
    "range_width_120_pct",
    "range_width_240_pct",
    "position_in_120d_range_pct",
    "position_in_240d_range_pct",
    "deep_low_120_le20",
    "deep_low_120_le30",
    "deep_low_120_le40",
    "deep_low_240_le20",
    "deep_low_240_le30",
    "deep_low_240_le40",
    "range60_le25",
    "range60_le35",
    "range120_le25",
    "range120_le35",
    "range120_le45",
    "source_high_breakout_60d_met",
    "source_next_day_continuation_confirmed",
    "classification_id",
    "attack_method",
    "price_position_type",
    "consolidation_type",
    "risk_type",
    "limit_up_like",
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
class ConditionSet:
    matrix_family: str
    condition_set_id: str
    condition_set_label: str
    deep_low_window_days: str = ""
    deep_low_threshold_pct: str = ""
    range_window_days: str = ""
    range_width_threshold_pct: str = ""
    extra_gate: str = ""
    note: str = ""


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
    if text.endswith(".0") and text.replace(".", "", 1).isdigit():
        return text[:-2]
    return text


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


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


def false_text() -> str:
    return "False"


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


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


def source_artifact_version(df: pd.DataFrame) -> str:
    versions = sorted(set(df.get("artifact_version", pd.Series(dtype=str)).astype(str)))
    if len(versions) != 1:
        raise SystemExit(f"ERROR: source detail must have exactly one artifact_version; got {versions[:5]}")
    return versions[0]


def load_source_detail() -> tuple[pd.DataFrame, str]:
    detail = read_csv(SOURCE_DETAIL_CSV)
    if detail.empty:
        raise SystemExit("ERROR: source raw-market detail is empty")
    if set(detail.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: source detail must be volume_range_breakout_v2_raw_market_rerun")
    approved = set(detail.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower())
    if not approved <= {"false", "0", ""}:
        raise SystemExit("ERROR: source detail must remain approved_for_daily=False")
    if detail["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: source_event_key must be unique in source detail")
    return detail, source_artifact_version(detail)


def load_price_cache(stock_ids: pd.Series) -> dict[str, pd.DataFrame]:
    cache: dict[str, pd.DataFrame] = {}
    for stock_id in sorted(set(stock_ids.astype(str))):
        path = PRICE_DIR / f"{stock_id}.csv"
        if not path.exists():
            cache[stock_id] = pd.DataFrame()
            continue
        price = pd.read_csv(path, dtype=str, keep_default_na=False)
        if price.empty or "date" not in price.columns:
            cache[stock_id] = pd.DataFrame()
            continue
        price = price.copy()
        price["date"] = price["date"].map(normalize_date)
        price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
        for col in ["open", "high", "low", "close", "volume"]:
            price[col] = pd.to_numeric(price.get(col, ""), errors="coerce")
        high = price["high"]
        low = price["low"]
        close = price["close"]
        for window in [60, 120, 240]:
            price[f"previous_{window}d_high_calc"] = high.shift(1).rolling(window, min_periods=window).max()
            price[f"previous_{window}d_low_calc"] = low.shift(1).rolling(window, min_periods=window).min()
            price[f"range_width_{window}_pct_calc"] = (
                (price[f"previous_{window}d_high_calc"] - price[f"previous_{window}d_low_calc"])
                / price[f"previous_{window}d_low_calc"].replace(0, pd.NA)
                * 100.0
            )
            price[f"off_{window}d_low_pct_calc"] = (
                close / price[f"previous_{window}d_low_calc"].replace(0, pd.NA) - 1.0
            ) * 100.0
            price[f"position_in_{window}d_range_pct_calc"] = (
                (close - price[f"previous_{window}d_low_calc"])
                / (price[f"previous_{window}d_high_calc"] - price[f"previous_{window}d_low_calc"]).replace(0, pd.NA)
                * 100.0
            )
        cache[stock_id] = price
    return cache


def add_deep_low_features(source: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    source = source.copy()
    source["stock_id"] = source["stock_id"].map(safe_str)
    source["signal_date"] = source["signal_date"].map(normalize_date)
    cache = load_price_cache(source["stock_id"])
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        out = row.to_dict()
        stock_id = safe_str(row.get("stock_id"))
        signal_date = normalize_date(row.get("signal_date"))
        price = cache.get(stock_id, pd.DataFrame())
        matched = pd.DataFrame()
        if not price.empty:
            matched = price[price["date"].astype(str).eq(signal_date)]
        if not matched.empty:
            price_row = matched.iloc[0]
            out["signal_close"] = pct_round(price_row.get("close"))
            for window in [60, 120, 240]:
                out[f"previous_{window}d_high"] = pct_round(price_row.get(f"previous_{window}d_high_calc"))
                out[f"previous_{window}d_low"] = pct_round(price_row.get(f"previous_{window}d_low_calc"))
                out[f"off_{window}d_low_pct"] = pct_round(price_row.get(f"off_{window}d_low_pct_calc"))
                out[f"range_width_{window}_pct"] = pct_round(price_row.get(f"range_width_{window}_pct_calc"))
                out[f"position_in_{window}d_range_pct"] = pct_round(price_row.get(f"position_in_{window}d_range_pct_calc"))
        else:
            out["signal_close"] = ""
            for window in [60, 120, 240]:
                out[f"previous_{window}d_high"] = ""
                out[f"previous_{window}d_low"] = ""
                out[f"off_{window}d_low_pct"] = ""
                out[f"range_width_{window}_pct"] = ""
                out[f"position_in_{window}d_range_pct"] = ""
        rows.append(out)

    detail = pd.DataFrame(rows)
    for col in [
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "signal_close",
        "off_60d_low_pct",
        "off_120d_low_pct",
        "off_240d_low_pct",
        "range_width_60_pct",
        "range_width_120_pct",
        "range_width_240_pct",
        "position_in_120d_range_pct",
        "position_in_240d_range_pct",
    ]:
        detail[col] = pd.to_numeric(detail.get(col, ""), errors="coerce")

    detail["return_outcome"] = "neutral"
    detail.loc[detail["return_pct"].gt(0), "return_outcome"] = "win"
    detail.loc[detail["return_pct"].lt(0), "return_outcome"] = "loss"
    for window in [120, 240]:
        for threshold in [20, 30, 40]:
            detail[f"deep_low_{window}_le{threshold}"] = detail[f"off_{window}d_low_pct"].le(threshold).fillna(False).map(bool_text)
    for threshold in [25, 35]:
        detail[f"range60_le{threshold}"] = detail["range_width_60_pct"].le(threshold).fillna(False).map(bool_text)
    for threshold in [25, 35, 45]:
        detail[f"range120_le{threshold}"] = detail["range_width_120_pct"].le(threshold).fillna(False).map(bool_text)
    detail["source_high_breakout_60d_met"] = detail.get("high_breakout_60d_met", "").astype(str)
    detail["source_next_day_continuation_confirmed"] = detail.get("next_day_continuation_confirmed", "").astype(str)
    detail["research_id"] = RESEARCH_ID
    detail["artifact_version"] = ARTIFACT_VERSION
    detail["source_research_id"] = SOURCE_RESEARCH_ID
    detail["source_artifact_version"] = source_version
    detail["advisory_status"] = ADVISORY_STATUS
    detail["model_id"] = MODEL_ID
    detail["approved_for_daily"] = false_text()
    detail["production_readiness"] = PRODUCTION_READINESS
    detail["generated_at"] = generated_at
    return detail


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


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    if sample_size >= 50:
        return "thin_sample"
    if sample_size >= 20:
        return "very_thin_sample"
    return "insufficient_sample"


def condition_sets() -> list[ConditionSet]:
    rows: list[ConditionSet] = [
        ConditionSet(
            matrix_family="baseline",
            condition_set_id="baseline_prev60_high_next_day_continuation",
            condition_set_label="current v2 raw-market population",
            note="baseline still requires 60d high breakout and next-day continuation",
        )
    ]
    for condition_set_id, label, extra_gate in [
        ("coverage_off120_available", "events with 120d low/range coverage", "off120_available"),
        ("coverage_off240_available", "events with 240d low/range coverage", "off240_available"),
        ("coverage_range120_available", "events with 120d range coverage", "range120_available"),
    ]:
        rows.append(
            ConditionSet(
                matrix_family="coverage_diagnostic",
                condition_set_id=condition_set_id,
                condition_set_label=label,
                extra_gate=extra_gate,
                note="data coverage diagnostic only; missing lookback windows are not treated as failed trades",
            )
        )
    for low_window in [120, 240]:
        for low_threshold in [20, 30, 40]:
            rows.append(
                ConditionSet(
                    matrix_family="deep_low_only",
                    condition_set_id=f"off{low_window}_le{low_threshold}",
                    condition_set_label=f"off {low_window}d low <= {low_threshold}%",
                    deep_low_window_days=str(low_window),
                    deep_low_threshold_pct=str(low_threshold),
                    note="deep low proxy under the current v2 60d-high + continuation population",
                )
            )
            for range_window, widths in [(60, [25, 35]), (120, [25, 35, 45])]:
                for width in widths:
                    rows.append(
                        ConditionSet(
                            matrix_family="deep_low_and_range",
                            condition_set_id=f"off{low_window}_le{low_threshold}_range{range_window}_le{width}",
                            condition_set_label=f"off {low_window}d low <= {low_threshold}% and {range_window}d range <= {width}%",
                            deep_low_window_days=str(low_window),
                            deep_low_threshold_pct=str(low_threshold),
                            range_window_days=str(range_window),
                            range_width_threshold_pct=str(width),
                            note="tests very-low-base plus consolidation width; research-only, not a production gate",
                        )
                    )
    for range_window, widths in [(60, [25, 35]), (120, [25, 35, 45])]:
        for width in widths:
            rows.append(
                ConditionSet(
                    matrix_family="range_only",
                    condition_set_id=f"range{range_window}_le{width}",
                    condition_set_label=f"{range_window}d range <= {width}%",
                    range_window_days=str(range_window),
                    range_width_threshold_pct=str(width),
                    note="range-width proxy alone; does not prove low base",
                )
            )
    return rows


def condition_mask(detail: pd.DataFrame, condition: ConditionSet) -> pd.Series:
    mask = pd.Series(True, index=detail.index)
    if condition.condition_set_id == "baseline_prev60_high_next_day_continuation":
        return mask
    if condition.extra_gate == "off120_available":
        return detail["off_120d_low_pct"].notna()
    if condition.extra_gate == "off240_available":
        return detail["off_240d_low_pct"].notna()
    if condition.extra_gate == "range120_available":
        return detail["range_width_120_pct"].notna()
    if condition.deep_low_window_days and condition.deep_low_threshold_pct:
        flag = f"deep_low_{condition.deep_low_window_days}_le{condition.deep_low_threshold_pct}"
        mask &= detail[flag].astype(str).eq("True")
    if condition.range_window_days and condition.range_width_threshold_pct:
        flag = f"range{condition.range_window_days}_le{condition.range_width_threshold_pct}"
        mask &= detail[flag].astype(str).eq("True")
    return mask.fillna(False)


def decision_hint(row: dict[str, Any], baseline: dict[str, Any], condition: ConditionSet) -> str:
    if condition.matrix_family == "baseline":
        return "baseline_reference"
    if condition.matrix_family == "coverage_diagnostic":
        return "data_coverage_diagnostic_not_condition"
    sample_size = int(row.get("sample_size") or 0)
    if sample_size < 20:
        return "insufficient_sample_do_not_use"
    if sample_size < 50:
        return "very_thin_sample_review_only"
    avg = float(row.get("avg_return_pct") or 0.0)
    median = float(row.get("median_return_pct") or 0.0)
    win_rate = float(row.get("win_rate_pct") or 0.0)
    loss_rate = float(row.get("loss_rate_pct") or 0.0)
    base_avg = float(baseline.get("avg_return_pct") or 0.0)
    base_median = float(baseline.get("median_return_pct") or 0.0)
    base_win = float(baseline.get("win_rate_pct") or 0.0)
    base_loss = float(baseline.get("loss_rate_pct") or 0.0)
    if avg >= base_avg + 1.0 and median >= base_median and win_rate >= base_win and loss_rate <= base_loss:
        return "possible_deep_low_gate_or_score_candidate_research_only"
    if avg <= base_avg - 1.0 and median <= base_median and win_rate <= base_win and loss_rate >= base_loss:
        return "weaker_than_current_v2_do_not_promote_as_gate"
    return "mixed_or_thin_result_research_only"


def row_for_condition(
    detail: pd.DataFrame,
    condition: ConditionSet,
    generated_at: str,
    source_version: str,
    baseline_metrics: dict[str, Any],
) -> dict[str, Any]:
    mask = condition_mask(detail, condition)
    part = detail[mask]
    metrics = return_metrics(part)
    baseline_size = len(detail)
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "matrix_family": condition.matrix_family,
        "condition_set_id": condition.condition_set_id,
        "condition_set_label": condition.condition_set_label,
        "population_basis": "current_v2_raw_market_events_requires_prev60_high_breakout_and_next_day_continuation",
        "requires_60d_high_breakout": "True",
        "requires_next_day_continuation": "True",
        "deep_low_window_days": condition.deep_low_window_days,
        "deep_low_threshold_pct": condition.deep_low_threshold_pct,
        "range_window_days": condition.range_window_days,
        "range_width_threshold_pct": condition.range_width_threshold_pct,
        "extra_gate": condition.extra_gate,
        "baseline_sample_size": baseline_size,
        "coverage_pct": pct_round(int(metrics["sample_size"]) / baseline_size * 100.0 if baseline_size else math.nan, 2),
        "note": condition.note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics)
    row["sample_status"] = sample_status(int(row["sample_size"]))
    row["win_rate_delta_pct"] = pct_round(float(row["win_rate_pct"] or 0.0) - float(baseline_metrics["win_rate_pct"] or 0.0), 2)
    row["loss_rate_delta_pct"] = pct_round(float(row["loss_rate_pct"] or 0.0) - float(baseline_metrics["loss_rate_pct"] or 0.0), 2)
    row["avg_return_delta_pct"] = pct_round(float(row["avg_return_pct"] or 0.0) - float(baseline_metrics["avg_return_pct"] or 0.0))
    row["median_return_delta_pct"] = pct_round(float(row["median_return_pct"] or 0.0) - float(baseline_metrics["median_return_pct"] or 0.0))
    row["decision_hint"] = decision_hint(row, baseline_metrics, condition)
    row["value_a"] = f"source_rows={baseline_size}"
    row["value_b"] = "current_v2_population=True"
    row["value_c"] = "deep_low_not_yet_raw_rerun_without_60d_high_gate"
    return row


def build_summary(detail: pd.DataFrame, generated_at: str, source_version: str) -> pd.DataFrame:
    baseline_metrics = return_metrics(detail)
    rows = [row_for_condition(detail, condition, generated_at, source_version, baseline_metrics) for condition in condition_sets()]
    return pd.DataFrame(rows)


def write_markdown(summary: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 30) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
        return lines

    rows = summary.copy()
    rows["_sample"] = pd.to_numeric(rows["sample_size"], errors="coerce")
    rows["_avg"] = pd.to_numeric(rows["avg_return_pct"], errors="coerce")
    deep = rows[rows["matrix_family"].isin(["deep_low_only", "deep_low_and_range"])].copy()
    enough = deep[pd.to_numeric(deep["sample_size"], errors="coerce").ge(20)]
    lines = [
        "# volume_range_breakout v2 deep low-base matrix",
        "",
        "Research-only artifact. This does not change production model conditions, ranking, scoring, registry, or PDF behavior.",
        "",
        "Population basis: current v2 raw-market events, which still require previous-60-day high breakout and next-day continuation.",
        "Purpose: test the user's stricter low-base meaning using 120/240-day distance from low and 60/120-day range width.",
        "",
        "Coverage diagnostic rows are included because 120/240-day lookback windows may be unavailable for some source events.",
        "",
        "Important boundary: if deep-low samples are too thin or weak inside this population, that does not disprove a future low-base model without the current 60d-high continuation gate.",
        "",
        "## Baseline And Deep-Low Rows",
        "",
    ]
    lines += md_table(
        rows.sort_values(["matrix_family", "_sample"], ascending=[True, False]),
        [
            "condition_set_id",
            "sample_size",
            "win_rate_pct",
            "loss_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "sample_status",
            "decision_hint",
        ],
    )
    lines += [
        "",
        "## Deep-Low Rows With At Least 20 Samples",
        "",
    ]
    lines += md_table(
        enough.sort_values(["_avg", "_sample"], ascending=[False, False]),
        [
            "condition_set_id",
            "sample_size",
            "coverage_pct",
            "win_rate_pct",
            "loss_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "decision_hint",
        ],
    )
    lines += [
        "",
        "## Promotion Boundary",
        "",
        "These rows are diagnostic and research-only. A production low-base breakout model still requires a separate raw producer/backtest that can remove or replace the current 60d-high continuation gate.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    source, source_version = load_source_detail()
    detail = add_deep_low_features(source, source_version, generated_at)
    summary = build_summary(detail, generated_at, source_version)
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in research artifact: {forbidden}")
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
