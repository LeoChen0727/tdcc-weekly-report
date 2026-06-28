from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_w_bottom_candidate_chart_review_packet import normalize_code, normalize_date, safe_str


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_RULE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_detail_latest.csv"
SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_PRICE_LEVEL_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_replay_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_replay_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_replay_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_replay_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_replay.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_left_anchor_rule_replay"
SOURCE_RESEARCH_ID = "w_bottom_left_anchor_rule_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_left_anchor_rule_replay_20260625"

BASELINE_RULE_ID = "current_detector_left_peak"

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
    "rule_id",
    "rule_window_days",
    "selector_method",
    "source_audit_scope",
    "case_review_tag",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "source_pattern_family",
    "baseline_current_left_peak_date",
    "candidate_left_peak_date",
    "candidate_days_before_left_low",
    "candidate_drop_to_left_low_pct",
    "candidate_left_descent_wrong_direction_rate_pct",
    "candidate_matches_human_left_peak",
    "candidate_selection_status",
    "candidate_selection_reason",
    "outcome_available",
    "sym1_5_quality_bucket",
    "sym1_5_w_shape_completed",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_breakout_date",
    "primary_review_flag",
    "transition_status",
    "slope_curvature_category",
    "price_level_bucket",
    "effective_mainstream_label",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "selected_for_rule_replay",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "rule_id",
    "rule_window_days",
    "selector_method",
    "rule_source_rows",
    "selected_rows",
    "selected_rate_pct",
    "outcome_available_rows",
    "manual_positive_rows",
    "shape_completed_count",
    "shape_completed_rate_pct",
    "volume_breakout_count",
    "volume_breakout_rate_pct",
    "observation_to_volume_confirmation_count",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "tdcc_any_age7_count",
    "baseline_outcome_available_rows",
    "baseline_volume_breakout_rate_pct",
    "baseline_mature_sample_size",
    "baseline_win_rate_pct",
    "baseline_avg_a_return_pct",
    "delta_selected_rows_vs_baseline",
    "delta_volume_breakout_rate_pct",
    "delta_win_rate_pct",
    "delta_avg_a_return_pct",
    "sample_warning",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def pct(value: float) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, 4)


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        number = float(text)
    except ValueError:
        return math.nan
    return number if not math.isnan(number) else math.nan


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    view = df.loc[:, columns].head(limit).copy()
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def normalize_keys(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_code)
    if "signal_date" in df.columns:
        df["signal_date"] = df["signal_date"].map(normalize_date)
    return df


def load_inputs() -> pd.DataFrame:
    rule = normalize_keys(read_csv(SOURCE_RULE_DETAIL_CSV))
    quality = normalize_keys(read_csv(SOURCE_QUALITY_CSV))
    price = normalize_keys(read_csv(SOURCE_PRICE_LEVEL_DETAIL_CSV))

    required_rule = {
        "rule_id",
        "stock_id",
        "signal_date",
        "candidate_selection_status",
        "source_audit_scope",
    }
    required_quality = {
        "stock_id",
        "signal_date",
        "sym1_5_quality_bucket",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_breakout_date",
        "primary_review_flag",
    }
    required_price = {
        "stock_id",
        "signal_date",
        "transition_status",
        "slope_curvature_category",
        "price_level_bucket",
        "effective_mainstream_label",
        "a_mature",
        "a_return_pct",
        "c_mature",
        "c_return_pct",
        "tdcc_any_age7",
    }
    missing_rule = sorted(required_rule - set(rule.columns))
    missing_quality = sorted(required_quality - set(quality.columns))
    missing_price = sorted(required_price - set(price.columns))
    if missing_rule:
        raise SystemExit(f"ERROR: rule detail missing columns: {missing_rule}")
    if missing_quality:
        raise SystemExit(f"ERROR: quality audit missing columns: {missing_quality}")
    if missing_price:
        raise SystemExit(f"ERROR: price-level detail missing columns: {missing_price}")

    quality_cols = [
        "stock_id",
        "signal_date",
        "sym1_5_quality_bucket",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_breakout_date",
        "primary_review_flag",
    ]
    price_cols = [
        "stock_id",
        "signal_date",
        "transition_status",
        "slope_curvature_category",
        "price_level_bucket",
        "effective_mainstream_label",
        "a_mature",
        "a_return_pct",
        "c_mature",
        "c_return_pct",
        "tdcc_any_age7",
    ]
    merged = rule.merge(quality[quality_cols], on=["stock_id", "signal_date"], how="left")
    merged = merged.merge(price[price_cols], on=["stock_id", "signal_date"], how="left", suffixes=("", "_price"))
    return merged


def build_detail(generated_at: str) -> pd.DataFrame:
    source = load_inputs()
    rows: list[dict[str, Any]] = []
    for _, source_row in source.iterrows():
        selected = safe_str(source_row.get("candidate_selection_status")) == "selected"
        outcome_available = safe_str(source_row.get("sym1_5_quality_bucket")) != ""
        row = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "rule_id": safe_str(source_row.get("rule_id")),
            "rule_window_days": safe_str(source_row.get("rule_window_days")),
            "selector_method": safe_str(source_row.get("selector_method")),
            "source_audit_scope": safe_str(source_row.get("source_audit_scope")),
            "case_review_tag": safe_str(source_row.get("case_review_tag")),
            "manual_case_id": safe_str(source_row.get("manual_case_id")),
            "stock_id": normalize_code(source_row.get("stock_id")),
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": normalize_date(source_row.get("signal_date")),
            "source_pattern_family": safe_str(source_row.get("source_pattern_family")),
            "baseline_current_left_peak_date": normalize_date(source_row.get("baseline_current_left_peak_date")),
            "candidate_left_peak_date": normalize_date(source_row.get("candidate_left_peak_date")),
            "candidate_days_before_left_low": safe_str(source_row.get("candidate_days_before_left_low")),
            "candidate_drop_to_left_low_pct": safe_str(source_row.get("candidate_drop_to_left_low_pct")),
            "candidate_left_descent_wrong_direction_rate_pct": safe_str(
                source_row.get("candidate_left_descent_wrong_direction_rate_pct")
            ),
            "candidate_matches_human_left_peak": safe_str(source_row.get("candidate_matches_human_left_peak")),
            "candidate_selection_status": safe_str(source_row.get("candidate_selection_status")),
            "candidate_selection_reason": safe_str(source_row.get("candidate_selection_reason")),
            "outcome_available": bool_text(outcome_available),
            "sym1_5_quality_bucket": safe_str(source_row.get("sym1_5_quality_bucket")),
            "sym1_5_w_shape_completed": safe_str(source_row.get("sym1_5_w_shape_completed")),
            "sym1_5_neckline_volume_breakout": safe_str(source_row.get("sym1_5_neckline_volume_breakout")),
            "sym1_5_breakout_date": normalize_date(source_row.get("sym1_5_breakout_date")),
            "primary_review_flag": safe_str(source_row.get("primary_review_flag")),
            "transition_status": safe_str(source_row.get("transition_status")),
            "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
            "price_level_bucket": safe_str(source_row.get("price_level_bucket")),
            "effective_mainstream_label": safe_str(source_row.get("effective_mainstream_label")),
            "a_mature": safe_str(source_row.get("a_mature")),
            "a_return_pct": safe_str(source_row.get("a_return_pct")),
            "c_mature": safe_str(source_row.get("c_mature")),
            "c_return_pct": safe_str(source_row.get("c_return_pct")),
            "tdcc_any_age7": safe_str(source_row.get("tdcc_any_age7")),
            "selected_for_rule_replay": bool_text(selected),
            "manual_review_status": "pending_research_review",
            "approved_for_daily": "false",
            "production_readiness": "not_production_ready_research_only",
            "generated_at": generated_at,
        }
        rows.append(row)
    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def summarize_selected(rule_frame: pd.DataFrame) -> dict[str, Any]:
    selected = rule_frame[rule_frame["selected_for_rule_replay"].eq("true")].copy()
    outcome = selected[selected["outcome_available"].eq("true")].copy()
    mature = outcome[outcome["a_mature"].map(bool_value)].copy()
    returns = pd.to_numeric(mature["a_return_pct"], errors="coerce").dropna()
    win_count = int((returns > 0).sum()) if not returns.empty else 0
    selected_rows = len(selected)
    outcome_rows = len(outcome)
    shape_count = int(outcome["sym1_5_w_shape_completed"].map(bool_value).sum())
    volume_count = int(outcome["sym1_5_neckline_volume_breakout"].map(bool_value).sum())
    observation_to_volume = int(outcome["transition_status"].eq("observation_to_volume_confirmation").sum())
    mature_count = len(mature)
    return {
        "rule_source_rows": len(rule_frame),
        "selected_rows": selected_rows,
        "selected_rate_pct": pct(selected_rows / len(rule_frame) * 100.0 if len(rule_frame) else math.nan),
        "outcome_available_rows": outcome_rows,
        "manual_positive_rows": int(selected["source_audit_scope"].eq("manual_positive_missed_case").sum()),
        "shape_completed_count": shape_count,
        "shape_completed_rate_pct": pct(shape_count / outcome_rows * 100.0 if outcome_rows else math.nan),
        "volume_breakout_count": volume_count,
        "volume_breakout_rate_pct": pct(volume_count / outcome_rows * 100.0 if outcome_rows else math.nan),
        "observation_to_volume_confirmation_count": observation_to_volume,
        "mature_sample_size": mature_count,
        "win_count": win_count,
        "win_rate_pct": pct(win_count / mature_count * 100.0 if mature_count else math.nan),
        "avg_a_return_pct": pct(float(returns.mean())) if not returns.empty else "",
        "median_a_return_pct": pct(float(returns.median())) if not returns.empty else "",
        "tdcc_any_age7_count": int(outcome["tdcc_any_age7"].map(bool_value).sum()),
    }


def summarize(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    baseline_frame = detail[detail["rule_id"].eq(BASELINE_RULE_ID)].copy()
    baseline = summarize_selected(baseline_frame)
    rows: list[dict[str, Any]] = []
    for rule_id, rule_frame in detail.groupby("rule_id", sort=True):
        stats = summarize_selected(rule_frame)
        rule_meta = rule_frame.iloc[0]
        mature_count = int(stats["mature_sample_size"])
        sample_warning = "sample_size_ok_for_research_review" if mature_count >= 30 else "directional_only_below_promotion_review_size"
        rows.append(
            {
                "model_id": MODEL_ID,
                "confirmation_model_id": CONFIRMATION_MODEL_ID,
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "rule_id": rule_id,
                "rule_window_days": safe_str(rule_meta.get("rule_window_days")),
                "selector_method": safe_str(rule_meta.get("selector_method")),
                **stats,
                "baseline_outcome_available_rows": baseline["outcome_available_rows"],
                "baseline_volume_breakout_rate_pct": baseline["volume_breakout_rate_pct"],
                "baseline_mature_sample_size": baseline["mature_sample_size"],
                "baseline_win_rate_pct": baseline["win_rate_pct"],
                "baseline_avg_a_return_pct": baseline["avg_a_return_pct"],
                "delta_selected_rows_vs_baseline": int(stats["selected_rows"]) - int(baseline["selected_rows"]),
                "delta_volume_breakout_rate_pct": pct(
                    safe_float(stats["volume_breakout_rate_pct"]) - safe_float(baseline["volume_breakout_rate_pct"])
                ),
                "delta_win_rate_pct": pct(safe_float(stats["win_rate_pct"]) - safe_float(baseline["win_rate_pct"])),
                "delta_avg_a_return_pct": pct(safe_float(stats["avg_a_return_pct"]) - safe_float(baseline["avg_a_return_pct"])),
                "sample_warning": sample_warning,
                "production_readiness": "not_production_ready_research_only",
                "generated_at": generated_at,
            }
        )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    key_cases = detail[
        detail["stock_id"].isin(["8069", "6415"])
        & detail["rule_id"].isin(
            [
                BASELINE_RULE_ID,
                "highest_high_90d_before_left_low",
                "nearest_micro_pressure_45d_min15_before_left_low",
                "nearest_micro_pressure_90d_min15_before_left_low",
            ]
        )
    ].copy()
    lines = [
        "# W-Bottom Left-Anchor Rule Replay",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- detail_rows: `{len(detail)}`",
        f"- summary_rows: `{len(summary)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this replay does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: left-anchor rules are replayed as candidate filters/quality segments, not as production logic.",
        "",
        "## Replay Summary",
        "",
        *markdown_table(
            summary,
            [
                "rule_id",
                "selected_rows",
                "outcome_available_rows",
                "volume_breakout_rate_pct",
                "mature_sample_size",
                "win_rate_pct",
                "avg_a_return_pct",
                "delta_volume_breakout_rate_pct",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "sample_warning",
            ],
        ),
        "",
        "## Key Cases",
        "",
        *markdown_table(
            key_cases,
            [
                "stock_id",
                "stock_name",
                "rule_id",
                "source_audit_scope",
                "candidate_left_peak_date",
                "candidate_matches_human_left_peak",
                "outcome_available",
                "selected_for_rule_replay",
                "sym1_5_quality_bucket",
                "a_return_pct",
            ],
            limit=20,
        ),
        "",
        "## Reading Notes",
        "",
        "- This replay does not recompute production candidates. It compares existing W candidate outcomes after applying left-anchor rule selection.",
        "- Manual positive rows such as `8069` can appear in key-case detail but are excluded from outcome metrics when no production-like outcome row exists.",
        "- A better human anchor match is not enough for promotion; the selected subset must also improve confirmation and return metrics with enough mature rows.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: left-anchor replay emitted forbidden production fields: {forbidden}")
    summary = summarize(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(detail, summary, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
