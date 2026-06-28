from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

NEAREST_MICRO_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail_latest.csv"
COMBINED_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_detail_latest.csv"
SPLIT_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_detail_latest.csv"
PARAMETER_GRID_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_data_coverage_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_data_coverage_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_data_coverage_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_early_entry_data_coverage_audit"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
TARGET_EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
TARGET_OUTCOME_RULE_ID = "tp10_or_neutral_after_5pct_close_40d"
STRICT_SEGMENT_ID = "smooth_right_rebound_5_20"

OUTPUT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "audit_section",
    "audit_item_id",
    "source_artifact",
    "event_set_id",
    "outcome_rule_id",
    "segment_id",
    "period_id",
    "row_count",
    "stock_count",
    "unique_signal_count",
    "min_date",
    "max_date",
    "month_count",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "mature_signal_month_count",
    "months_with_mature_ge5",
    "months_with_mature_ge10",
    "price_files_with_dates",
    "price_rows",
    "price_global_min_date",
    "price_global_max_date",
    "files_with_180_days",
    "earliest_180th_observed_date",
    "signal_window_status",
    "maturity_status",
    "promotion_readiness",
    "blocker_reason",
    "required_followup_owner",
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
}


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


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def month_id(date_text: str) -> str:
    date_text = normalize_date(date_text)
    return f"{date_text[:4]}-{date_text[4:6]}" if len(date_text) >= 6 else ""


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def base_row(generated_at: str) -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "audit_section": "",
        "audit_item_id": "",
        "source_artifact": "",
        "event_set_id": "",
        "outcome_rule_id": "",
        "segment_id": "",
        "period_id": "",
        "row_count": "",
        "stock_count": "",
        "unique_signal_count": "",
        "min_date": "",
        "max_date": "",
        "month_count": "",
        "sample_size": "",
        "evaluated_sample_size": "",
        "mature_sample_size": "",
        "win_count": "",
        "neutral_count": "",
        "loss_count": "",
        "incomplete_count": "",
        "mature_signal_month_count": "",
        "months_with_mature_ge5": "",
        "months_with_mature_ge10": "",
        "price_files_with_dates": "",
        "price_rows": "",
        "price_global_min_date": "",
        "price_global_max_date": "",
        "files_with_180_days": "",
        "earliest_180th_observed_date": "",
        "signal_window_status": "",
        "maturity_status": "",
        "promotion_readiness": "",
        "blocker_reason": "",
        "required_followup_owner": "",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def date_series(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series(dtype=str)
    dates = df[column].map(normalize_date)
    return dates[dates.str.len().ge(8)]


def unique_signal_count(df: pd.DataFrame, date_column: str) -> int:
    if "stock_id" not in df.columns or date_column not in df.columns:
        return 0
    keys = set()
    for _, row in df.iterrows():
        stock_id = safe_str(row.get("stock_id"))
        date_text = normalize_date(row.get(date_column))
        if stock_id and date_text:
            keys.add((stock_id, date_text))
    return len(keys)


def price_coverage(generated_at: str) -> dict[str, Any]:
    mins: list[str] = []
    maxs: list[str] = []
    observed_180th_dates: list[str] = []
    price_rows = 0
    price_files_with_dates = 0
    for path in sorted(PRICE_DIR.glob("*.csv")):
        try:
            price = pd.read_csv(path, dtype=str, keep_default_na=False, usecols=lambda c: c.lower() in {"date", "日期"})
        except Exception:
            continue
        date_column = "date" if "date" in price.columns else ("日期" if "日期" in price.columns else "")
        if not date_column:
            continue
        dates = price[date_column].map(normalize_date)
        dates = dates[dates.str.len().ge(8)].sort_values().reset_index(drop=True)
        if dates.empty:
            continue
        mins.append(str(dates.iloc[0]))
        maxs.append(str(dates.iloc[-1]))
        price_rows += int(len(dates))
        price_files_with_dates += 1
        if len(dates) >= 180:
            observed_180th_dates.append(str(dates.iloc[179]))

    price_min = min(mins) if mins else ""
    price_max = max(maxs) if maxs else ""
    earliest_180th = min(observed_180th_dates) if observed_180th_dates else ""
    extended_180_gate = bool(earliest_180th and earliest_180th < "20260105")
    row = base_row(generated_at)
    row.update(
        {
            "audit_section": "price_history_coverage",
            "audit_item_id": "stock_price_history_global",
            "source_artifact": str(PRICE_DIR).replace("\\", "/"),
            "row_count": price_rows,
            "stock_count": price_files_with_dates,
            "price_files_with_dates": price_files_with_dates,
            "price_rows": price_rows,
            "price_global_min_date": price_min,
            "price_global_max_date": price_max,
            "min_date": price_min,
            "max_date": price_max,
            "files_with_180_days": len(observed_180th_dates),
            "earliest_180th_observed_date": earliest_180th,
            "signal_window_status": (
                "price_history_backfill_extended_180_day_gate"
                if extended_180_gate
                else "price_history_available_but_w_signals_start_later"
            ),
            "maturity_status": "not_an_outcome_row",
            "promotion_readiness": "research_data_coverage_reference",
            "blocker_reason": (
                "approved_official_price_backfill_extends_180_day_gate_before_20260105"
                if extended_180_gate
                else "price_history_begins_2025_04_for_most_files_so_180_day_gate_limits_early_w_signal_window"
            ),
            "required_followup_owner": "research_backtest_data_governance",
        }
    )
    return row


def source_window_row(
    generated_at: str,
    audit_item_id: str,
    source_artifact: Path,
    df: pd.DataFrame,
    date_column: str,
    event_set_id: str = "",
) -> dict[str, Any]:
    dates = date_series(df, date_column)
    months = {month_id(value) for value in dates if month_id(value)}
    min_date = dates.min() if not dates.empty else ""
    max_date = dates.max() if not dates.empty else ""
    extended_signal_window = bool(min_date and min_date < "20260101")
    row = base_row(generated_at)
    row.update(
        {
            "audit_section": "w_bottom_signal_source_window",
            "audit_item_id": audit_item_id,
            "source_artifact": str(source_artifact).replace("\\", "/"),
            "event_set_id": event_set_id,
            "row_count": int(len(df)),
            "stock_count": int(df["stock_id"].nunique()) if "stock_id" in df.columns else "",
            "unique_signal_count": unique_signal_count(df, date_column),
            "min_date": min_date,
            "max_date": max_date,
            "month_count": len(months),
            "signal_window_status": (
                "extended_signal_window_after_official_price_backfill"
                if extended_signal_window
                else "short_signal_window_current_inputs"
            ),
            "maturity_status": "not_an_outcome_row",
            "promotion_readiness": (
                "research_signal_window_extended_not_production_ready"
                if extended_signal_window
                else "blocked_data_window_too_short"
            ),
            "blocker_reason": (
                "signal_window_extended_after_official_price_backfill_but_research_remains_advisory"
                if extended_signal_window
                else "current_w_bottom_research_outputs_have_signal_dates_only_from_2026_01_to_2026_06"
            ),
            "required_followup_owner": "research_backtest_data_governance",
        }
    )
    return row


def strict_segment_mask(df: pd.DataFrame) -> pd.Series:
    return df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")


def outcome_counts(sample: pd.DataFrame) -> dict[str, int]:
    return {
        "sample_size": int(len(sample)),
        "evaluated_sample_size": int(sample["outcome_result"].isin(["win", "neutral", "loss"]).sum()) if "outcome_result" in sample.columns else 0,
        "mature_sample_size": int(sample["outcome_result"].isin(["win", "loss"]).sum()) if "outcome_result" in sample.columns else 0,
        "win_count": int(sample["outcome_result"].eq("win").sum()) if "outcome_result" in sample.columns else 0,
        "neutral_count": int(sample["outcome_result"].eq("neutral").sum()) if "outcome_result" in sample.columns else 0,
        "loss_count": int(sample["outcome_result"].eq("loss").sum()) if "outcome_result" in sample.columns else 0,
        "incomplete_count": int(sample["outcome_result"].eq("incomplete").sum()) if "outcome_result" in sample.columns else 0,
    }


def maturity_summary_rows(generated_at: str, source: pd.DataFrame) -> list[dict[str, Any]]:
    target = source[
        source["event_set_id"].eq(TARGET_EVENT_SET_ID)
        & source["outcome_rule_id"].eq(TARGET_OUTCOME_RULE_ID)
    ].copy()
    target["period_id"] = target["entry_signal_date"].map(month_id)
    segments = [
        ("all_rows", target),
        (STRICT_SEGMENT_ID, target[strict_segment_mask(target)].copy()),
    ]
    rows: list[dict[str, Any]] = []
    for segment_id, segment in segments:
        month_rows: list[dict[str, Any]] = []
        for period_id, period in sorted(segment.groupby("period_id"), key=lambda item: item[0]):
            counts = outcome_counts(period)
            row = base_row(generated_at)
            row.update(
                {
                    "audit_section": "outcome_month_maturity",
                    "audit_item_id": f"{segment_id}_{period_id}",
                    "source_artifact": str(PARAMETER_GRID_DETAIL_CSV).replace("\\", "/"),
                    "event_set_id": TARGET_EVENT_SET_ID,
                    "outcome_rule_id": TARGET_OUTCOME_RULE_ID,
                    "segment_id": segment_id,
                    "period_id": period_id,
                    "row_count": counts["sample_size"],
                    "min_date": date_series(period, "entry_signal_date").min(),
                    "max_date": date_series(period, "entry_signal_date").max(),
                    **counts,
                    "mature_signal_month_count": 1 if counts["mature_sample_size"] > 0 else 0,
                    "months_with_mature_ge5": 1 if counts["mature_sample_size"] >= 5 else 0,
                    "months_with_mature_ge10": 1 if counts["mature_sample_size"] >= 10 else 0,
                    "signal_window_status": "current_signal_month",
                    "maturity_status": "future_window_incomplete" if counts["evaluated_sample_size"] == 0 else "partially_mature",
                    "promotion_readiness": "blocked_research_stability_sample_too_thin",
                    "blocker_reason": "40_trading_day_outcome_and_mature_sample_thresholds_still_need_stability_review",
                    "required_followup_owner": "research_backtest_data_governance",
                }
            )
            month_rows.append(row)
            rows.append(row)

        counts = outcome_counts(segment)
        mature_month_count = sum(int(row["mature_signal_month_count"]) for row in month_rows)
        months_with_mature_ge5 = sum(int(row["months_with_mature_ge5"]) for row in month_rows)
        months_with_mature_ge10 = sum(int(row["months_with_mature_ge10"]) for row in month_rows)
        dates = date_series(segment, "entry_signal_date")
        summary = base_row(generated_at)
        summary.update(
            {
                "audit_section": "outcome_maturity_summary",
                "audit_item_id": segment_id,
                "source_artifact": str(PARAMETER_GRID_DETAIL_CSV).replace("\\", "/"),
                "event_set_id": TARGET_EVENT_SET_ID,
                "outcome_rule_id": TARGET_OUTCOME_RULE_ID,
                "segment_id": segment_id,
                "row_count": counts["sample_size"],
                "unique_signal_count": unique_signal_count(segment, "entry_signal_date"),
                "min_date": dates.min() if not dates.empty else "",
                "max_date": dates.max() if not dates.empty else "",
                "month_count": len({month_id(value) for value in dates if month_id(value)}),
                **counts,
                "mature_signal_month_count": mature_month_count,
                "months_with_mature_ge5": months_with_mature_ge5,
                "months_with_mature_ge10": months_with_mature_ge10,
                "signal_window_status": "extended_signal_window_after_official_price_backfill",
                "maturity_status": "insufficient_mature_months_for_promotion",
                "promotion_readiness": "blocked_research_stability_sample_too_thin",
                "blocker_reason": "strict_segment_mature_sample_months_remain_too_thin_for_production_promotion",
                "required_followup_owner": "research_backtest_data_governance",
            }
        )
        rows.append(summary)
    return rows


def conclusion_row(generated_at: str, price_row: dict[str, Any], source_rows: list[dict[str, Any]], maturity_rows: list[dict[str, Any]]) -> dict[str, Any]:
    summary = next(row for row in maturity_rows if row["audit_section"] == "outcome_maturity_summary" and row["segment_id"] == STRICT_SEGMENT_ID)
    source_min_dates = [safe_str(row["min_date"]) for row in source_rows if safe_str(row["min_date"])]
    source_max_dates = [safe_str(row["max_date"]) for row in source_rows if safe_str(row["max_date"])]
    input_extended = bool(
        safe_str(price_row["earliest_180th_observed_date"])
        and safe_str(price_row["earliest_180th_observed_date"]) < "20260105"
        and source_min_dates
        and min(source_min_dates) < "20260101"
    )
    row = base_row(generated_at)
    row.update(
        {
            "audit_section": "promotion_readiness_conclusion",
            "audit_item_id": "w_bottom_right_low_early_entry_current_data_window",
            "source_artifact": "research_backtest_w_bottom_latest_outputs",
            "event_set_id": TARGET_EVENT_SET_ID,
            "outcome_rule_id": TARGET_OUTCOME_RULE_ID,
            "segment_id": STRICT_SEGMENT_ID,
            "min_date": min(source_min_dates) if source_min_dates else "",
            "max_date": max(source_max_dates) if source_max_dates else "",
            "month_count": summary["month_count"],
            "sample_size": summary["sample_size"],
            "evaluated_sample_size": summary["evaluated_sample_size"],
            "mature_sample_size": summary["mature_sample_size"],
            "win_count": summary["win_count"],
            "neutral_count": summary["neutral_count"],
            "loss_count": summary["loss_count"],
            "incomplete_count": summary["incomplete_count"],
            "mature_signal_month_count": summary["mature_signal_month_count"],
            "months_with_mature_ge5": summary["months_with_mature_ge5"],
            "months_with_mature_ge10": summary["months_with_mature_ge10"],
            "price_files_with_dates": price_row["price_files_with_dates"],
            "price_rows": price_row["price_rows"],
            "price_global_min_date": price_row["price_global_min_date"],
            "price_global_max_date": price_row["price_global_max_date"],
            "files_with_180_days": price_row["files_with_180_days"],
            "earliest_180th_observed_date": price_row["earliest_180th_observed_date"],
            "signal_window_status": (
                "extended_signal_window_after_official_price_backfill"
                if input_extended
                else "cannot_extend_stability_from_current_w_bottom_outputs"
            ),
            "maturity_status": "insufficient_mature_months_for_promotion",
            "promotion_readiness": (
                "blocked_research_stability_sample_too_thin"
                if input_extended
                else "blocked_data_window_too_short"
            ),
            "blocker_reason": (
                "input_coverage_extended_but_strict_segment_has_only_"
                f"{summary['months_with_mature_ge10']}_months_with_mature_ge10"
                if input_extended
                else "need_longer_historical_price_backfill_or_more_future_mature_months_before_promotion_review"
            ),
            "required_followup_owner": "research_backtest_data_governance",
        }
    )
    return row


def build_markdown(rows: pd.DataFrame) -> str:
    price = rows[rows["audit_section"].eq("price_history_coverage")].iloc[0]
    conclusion = rows[rows["audit_section"].eq("promotion_readiness_conclusion")].iloc[0]
    source = rows[rows["audit_section"].eq("w_bottom_signal_source_window")].copy()
    maturity = rows[rows["audit_section"].eq("outcome_month_maturity") & rows["segment_id"].eq(STRICT_SEGMENT_ID)].copy()

    lines = [
        "# W-Bottom Early-Entry Data Coverage Audit",
        "",
        f"- generated_at: `{conclusion['generated_at']}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- production impact: `none`",
        "- scope: right-low early-entry W-bottom research data coverage only.",
        "- this audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.",
        "- rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "",
        "## Price History Coverage",
        "",
        f"- price history files with dates: `{price['price_files_with_dates']}`",
        f"- price rows: `{price['price_rows']}`",
        f"- global date range: `{price['price_global_min_date']}` to `{price['price_global_max_date']}`",
        f"- files with at least 180 observed trading dates: `{price['files_with_180_days']}`",
        f"- earliest 180th observed date across files: `{price['earliest_180th_observed_date']}`",
        "",
        "## W-Bottom Signal Windows",
        "",
        "| artifact | rows | unique signals | min date | max date | months |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for _, row in source.iterrows():
        lines.append(
            f"| `{row['audit_item_id']}` | {row['row_count']} | {row['unique_signal_count']} | "
            f"{row['min_date']} | {row['max_date']} | {row['month_count']} |"
        )

    lines.extend(
        [
            "",
            f"## `{STRICT_SEGMENT_ID}` Monthly Maturity",
            "",
            "| month | sample | evaluated | mature | win | neutral | loss | incomplete | maturity status |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for _, row in maturity.iterrows():
        lines.append(
            f"| {row['period_id']} | {row['sample_size']} | {row['evaluated_sample_size']} | "
            f"{row['mature_sample_size']} | {row['win_count']} | {row['neutral_count']} | "
            f"{row['loss_count']} | {row['incomplete_count']} | `{row['maturity_status']}` |"
        )

    lines.extend(
        [
            "",
            "## Conclusion",
            "",
            f"- promotion_readiness: `{conclusion['promotion_readiness']}`",
            f"- blocker_reason: `{conclusion['blocker_reason']}`",
            f"- mature signal months for `{STRICT_SEGMENT_ID}`: `{conclusion['mature_signal_month_count']}`",
            f"- months with mature sample >= 5: `{conclusion['months_with_mature_ge5']}`",
            f"- months with mature sample >= 10: `{conclusion['months_with_mature_ge10']}`",
            "- Interpretation: the approved official price backfill extends the W-bottom input and signal window, but the strict smooth/rebound segment remains research-only until stability and mature-sample thresholds are reviewed.",
            "- Required follow-up owner: `research_backtest_data_governance` for continued coverage, stability, and mature-month validation.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    generated_at = now_text()
    for path in [NEAREST_MICRO_DETAIL_CSV, COMBINED_DETAIL_CSV, SPLIT_DETAIL_CSV, PARAMETER_GRID_DETAIL_CSV]:
        if not path.exists():
            raise SystemExit(f"ERROR: missing required input: {path}")

    nearest = read_csv(NEAREST_MICRO_DETAIL_CSV)
    combined = read_csv(COMBINED_DETAIL_CSV)
    split = read_csv(SPLIT_DETAIL_CSV)
    parameter_grid = read_csv(PARAMETER_GRID_DETAIL_CSV)

    for name, df in [("nearest", nearest), ("combined", combined), ("split", split), ("parameter_grid", parameter_grid)]:
        forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
        if forbidden:
            raise SystemExit(f"ERROR: {name} source unexpectedly contains production decision fields: {forbidden}")

    price_row = price_coverage(generated_at)
    source_rows = [
        source_window_row(generated_at, "nearest_micro_detail_signal_window", NEAREST_MICRO_DETAIL_CSV, nearest, "signal_date"),
        source_window_row(
            generated_at,
            "combined_variant_signal_window",
            COMBINED_DETAIL_CSV,
            combined[combined["event_set_id"].eq(TARGET_EVENT_SET_ID)].copy(),
            "signal_date",
            TARGET_EVENT_SET_ID,
        ),
        source_window_row(
            generated_at,
            "split_variant_early_entry_signal_window",
            SPLIT_DETAIL_CSV,
            split[split["event_set_id"].eq(TARGET_EVENT_SET_ID) & split["surface_id"].eq(SURFACE_ID)].copy(),
            "source_signal_date",
            TARGET_EVENT_SET_ID,
        ),
        source_window_row(
            generated_at,
            "parameter_grid_variant_signal_window",
            PARAMETER_GRID_DETAIL_CSV,
            parameter_grid[parameter_grid["event_set_id"].eq(TARGET_EVENT_SET_ID)].copy(),
            "source_signal_date",
            TARGET_EVENT_SET_ID,
        ),
    ]
    maturity_rows = maturity_summary_rows(generated_at, parameter_grid)
    rows = [price_row, *source_rows, *maturity_rows]
    rows.append(conclusion_row(generated_at, price_row, source_rows, maturity_rows))

    output = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in output.columns:
            output[column] = ""
    output = output[OUTPUT_COLUMNS]

    write_csv(output, LATEST_CSV)
    write_csv(output, HISTORY_CSV)
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text(build_markdown(output), encoding="utf-8")
    print(f"Saved: {LATEST_CSV} rows={len(output)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
