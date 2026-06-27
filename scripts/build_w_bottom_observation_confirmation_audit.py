from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_DEFINITION_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_definition_audit_latest.csv"
SOURCE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"

LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_observation_confirmation_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_observation_confirmation_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_observation_confirmation_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_observation_confirmation_audit"
SOURCE_RESEARCH_ID = "w_bottom_candidate_quality_audit"
SOURCE_DEFINITION_RESEARCH_ID = "w_bottom_candidate_definition_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_observation_confirmation_split_20260625"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

INITIAL_STAGES = {
    "right_side_observation_zone",
    "right_side_extended_rebound",
    "near_neckline_at_signal",
    "already_above_neckline_at_signal",
    "right_side_rebound_too_early",
    "right_side_unclassified",
}

CONFIRMATION_STAGES = {
    "volume_confirmed_neckline_breakout",
    "price_confirmed_without_volume",
    "right_low_support_failed",
    "late_confirmation_not_w",
    "no_confirmation_within_symmetry",
    "future_window_incomplete",
    "invalid_or_missing_confirmation_path",
}

TRANSITION_STATUSES = {
    "observation_to_volume_confirmation",
    "observation_to_price_only_confirmation",
    "observation_support_failed",
    "observation_late_confirmation_not_w",
    "observation_no_confirmation",
    "observation_future_window_incomplete",
    "near_neckline_or_above_volume_confirmation",
    "not_observation_near_neckline_or_above",
    "not_primary_observation_extended_rebound",
    "not_primary_observation_too_early",
    "not_primary_observation_unclassified",
}

OUTPUT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "source_definition_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "stock_id",
    "stock_name",
    "signal_date",
    "initial_stage",
    "confirmation_stage",
    "transition_status",
    "surface_recommendation",
    "observation_stage_eligible",
    "confirmation_stage_eligible",
    "price_confirmation_only",
    "in_manual_review_packet",
    "primary_review_flag",
    "sym1_5_quality_bucket",
    "definition_status",
    "definition_issue_reasons",
    "slope_curvature_category",
    "signal_close",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "neckline_price",
    "right_low_value",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "first_rebound_days",
    "right_rebound_days_at_signal",
    "second_arc_volume_ratio",
    "sym1_5_w_shape_completed",
    "sym1_5_completion_date",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_breakout_date",
    "sym1_5_right_low_broken",
    "sym1_5_late_neckline_completion_not_w",
    "sym1_5_late_volume_breakout_not_w",
    "event_breakout_date",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "chart_path",
    "manual_review_status",
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


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def classify_initial_stage(row: pd.Series) -> str:
    distance = safe_float(row.get("signal_distance_to_neckline_pct"))
    rebound = safe_float(row.get("signal_rebound_from_right_low_pct"))
    if bool_value(row.get("signal_above_neckline")):
        return "already_above_neckline_at_signal"
    if bool_value(row.get("signal_near_neckline_zone")):
        return "near_neckline_at_signal"
    if math.isnan(rebound) or math.isnan(distance):
        return "right_side_unclassified"
    if rebound < 3.0:
        return "right_side_rebound_too_early"
    if rebound > 15.0:
        return "right_side_extended_rebound"
    return "right_side_observation_zone"


def classify_confirmation_stage(row: pd.Series) -> str:
    bucket = safe_str(row.get("sym1_5_quality_bucket"))
    if bool_value(row.get("sym1_5_neckline_volume_breakout")):
        return "volume_confirmed_neckline_breakout"
    if bool_value(row.get("sym1_5_w_shape_completed")):
        return "price_confirmed_without_volume"
    if bool_value(row.get("sym1_5_right_low_broken")):
        return "right_low_support_failed"
    if bool_value(row.get("sym1_5_late_neckline_completion_not_w")) or bool_value(row.get("sym1_5_late_volume_breakout_not_w")):
        return "late_confirmation_not_w"
    if bucket == "future_window_incomplete":
        return "future_window_incomplete"
    if bucket in {"price_history_missing", "price_date_missing", "invalid_price_inputs"}:
        return "invalid_or_missing_confirmation_path"
    return "no_confirmation_within_symmetry"


def transition_status(initial_stage: str, confirmation_stage: str) -> str:
    is_observation = initial_stage == "right_side_observation_zone"
    near_or_above = initial_stage in {"near_neckline_at_signal", "already_above_neckline_at_signal"}
    if is_observation and confirmation_stage == "volume_confirmed_neckline_breakout":
        return "observation_to_volume_confirmation"
    if is_observation and confirmation_stage == "price_confirmed_without_volume":
        return "observation_to_price_only_confirmation"
    if is_observation and confirmation_stage == "right_low_support_failed":
        return "observation_support_failed"
    if is_observation and confirmation_stage == "late_confirmation_not_w":
        return "observation_late_confirmation_not_w"
    if is_observation and confirmation_stage == "future_window_incomplete":
        return "observation_future_window_incomplete"
    if is_observation:
        return "observation_no_confirmation"
    if near_or_above and confirmation_stage == "volume_confirmed_neckline_breakout":
        return "near_neckline_or_above_volume_confirmation"
    if near_or_above:
        return "not_observation_near_neckline_or_above"
    if initial_stage == "right_side_extended_rebound":
        return "not_primary_observation_extended_rebound"
    if initial_stage == "right_side_rebound_too_early":
        return "not_primary_observation_too_early"
    return "not_primary_observation_unclassified"


def recommendation_for(transition: str, confirmation_stage: str) -> str:
    if transition in {"observation_to_volume_confirmation", "near_neckline_or_above_volume_confirmation"}:
        return "confirmation_model_research_candidate"
    if transition == "observation_to_price_only_confirmation":
        return "confirmation_requires_volume_or_followup_review"
    if transition in {"observation_no_confirmation", "observation_future_window_incomplete"}:
        return "observation_model_watch_only_research"
    if confirmation_stage == "right_low_support_failed":
        return "drop_or_support_failure_review"
    if confirmation_stage == "late_confirmation_not_w":
        return "drop_or_late_confirmation_review"
    if transition == "not_observation_near_neckline_or_above":
        return "exclude_from_observation_route_near_neckline"
    return "manual_review_before_any_promotion"


def load_sources() -> pd.DataFrame:
    quality = read_csv(SOURCE_QUALITY_CSV)
    required = {
        "stock_id",
        "stock_name",
        "signal_date",
        "sample_mode",
        "signal_distance_to_neckline_pct",
        "signal_rebound_from_right_low_pct",
        "signal_near_neckline_zone",
        "signal_above_neckline",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_right_low_broken",
        "sym1_5_late_neckline_completion_not_w",
        "sym1_5_late_volume_breakout_not_w",
        "sym1_5_quality_bucket",
        "primary_review_flag",
    }
    missing = sorted(required - set(quality.columns))
    if missing:
        raise SystemExit(f"ERROR: quality audit missing columns: {missing}")

    quality = quality.copy()
    quality["stock_id"] = quality["stock_id"].map(normalize_code)
    quality["signal_date"] = quality["signal_date"].map(normalize_date)

    if SOURCE_DEFINITION_CSV.exists():
        definition = read_csv(SOURCE_DEFINITION_CSV)
        definition = definition.copy()
        definition["stock_id"] = definition["stock_id"].map(normalize_code)
        definition["signal_date"] = definition["signal_date"].map(normalize_date)
        definition_cols = [
            "stock_id",
            "signal_date",
            "definition_status",
            "definition_issue_reasons",
            "slope_curvature_category",
            "chart_path",
        ]
        quality = quality.merge(definition[definition_cols], on=["stock_id", "signal_date"], how="left")

    if SOURCE_EVENTS_CSV.exists():
        events = read_csv(SOURCE_EVENTS_CSV)
        events = events.copy()
        events["stock_id"] = events["stock_id"].map(normalize_code)
        events["signal_date"] = events["signal_date"].map(normalize_date)
        events = events[
            events["symmetry_ratio"].astype(str).eq("1.5")
            & events["dedup_20d_eligible"].map(bool_value)
        ].copy()
        event_cols = [
            "stock_id",
            "signal_date",
            "breakout_date",
            "a_mature",
            "a_return_pct",
            "c_mature",
            "c_return_pct",
            "tdcc_any_age7",
            "tdcc_any_age14",
        ]
        events = events[event_cols].rename(columns={"breakout_date": "event_breakout_date"})
        quality = quality.merge(events, on=["stock_id", "signal_date"], how="left")

    for column in [
        "definition_status",
        "definition_issue_reasons",
        "slope_curvature_category",
        "chart_path",
        "event_breakout_date",
        "a_mature",
        "a_return_pct",
        "c_mature",
        "c_return_pct",
        "tdcc_any_age7",
        "tdcc_any_age14",
    ]:
        if column not in quality.columns:
            quality[column] = ""
        quality[column] = quality[column].fillna("")
    return quality


def build_audit(generated_at: str) -> pd.DataFrame:
    source = load_sources()
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        initial = classify_initial_stage(row)
        confirmation = classify_confirmation_stage(row)
        transition = transition_status(initial, confirmation)
        observation_eligible = initial == "right_side_observation_zone"
        confirmation_eligible = confirmation == "volume_confirmed_neckline_breakout"
        price_only = confirmation == "price_confirmed_without_volume"
        in_review_packet = bool(safe_str(row.get("definition_status")))
        output = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "source_definition_research_id": SOURCE_DEFINITION_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "sample_mode": safe_str(row.get("sample_mode")),
            "stock_id": normalize_code(row.get("stock_id")),
            "stock_name": safe_str(row.get("stock_name")),
            "signal_date": normalize_date(row.get("signal_date")),
            "initial_stage": initial,
            "confirmation_stage": confirmation,
            "transition_status": transition,
            "surface_recommendation": recommendation_for(transition, confirmation),
            "observation_stage_eligible": bool_text(observation_eligible),
            "confirmation_stage_eligible": bool_text(confirmation_eligible),
            "price_confirmation_only": bool_text(price_only),
            "in_manual_review_packet": bool_text(in_review_packet),
            "primary_review_flag": safe_str(row.get("primary_review_flag")),
            "sym1_5_quality_bucket": safe_str(row.get("sym1_5_quality_bucket")),
            "definition_status": safe_str(row.get("definition_status")),
            "definition_issue_reasons": safe_str(row.get("definition_issue_reasons")),
            "slope_curvature_category": safe_str(row.get("slope_curvature_category")),
            "signal_close": safe_str(row.get("signal_close")),
            "left_peak_date": normalize_date(row.get("left_peak_date")),
            "left_low_date": normalize_date(row.get("left_low_date")),
            "neckline_date": normalize_date(row.get("neckline_date")),
            "right_low_date": normalize_date(row.get("right_low_date")),
            "neckline_price": safe_str(row.get("neckline_price")),
            "right_low_value": safe_str(row.get("right_low_value")),
            "signal_distance_to_neckline_pct": safe_str(row.get("signal_distance_to_neckline_pct")),
            "signal_rebound_from_right_low_pct": safe_str(row.get("signal_rebound_from_right_low_pct")),
            "first_rebound_days": safe_str(row.get("first_rebound_days")),
            "right_rebound_days_at_signal": safe_str(row.get("right_rebound_days_at_signal")),
            "second_arc_volume_ratio": safe_str(row.get("second_arc_volume_ratio")),
            "sym1_5_w_shape_completed": bool_text(bool_value(row.get("sym1_5_w_shape_completed"))),
            "sym1_5_completion_date": normalize_date(row.get("sym1_5_completion_date")),
            "sym1_5_neckline_volume_breakout": bool_text(bool_value(row.get("sym1_5_neckline_volume_breakout"))),
            "sym1_5_breakout_date": normalize_date(row.get("sym1_5_breakout_date")),
            "sym1_5_right_low_broken": bool_text(bool_value(row.get("sym1_5_right_low_broken"))),
            "sym1_5_late_neckline_completion_not_w": bool_text(bool_value(row.get("sym1_5_late_neckline_completion_not_w"))),
            "sym1_5_late_volume_breakout_not_w": bool_text(bool_value(row.get("sym1_5_late_volume_breakout_not_w"))),
            "event_breakout_date": normalize_date(row.get("event_breakout_date")),
            "a_mature": bool_text(bool_value(row.get("a_mature"))),
            "a_return_pct": safe_str(row.get("a_return_pct")),
            "c_mature": bool_text(bool_value(row.get("c_mature"))),
            "c_return_pct": safe_str(row.get("c_return_pct")),
            "tdcc_any_age7": bool_text(bool_value(row.get("tdcc_any_age7"))),
            "tdcc_any_age14": bool_text(bool_value(row.get("tdcc_any_age14"))),
            "chart_path": safe_str(row.get("chart_path")),
            "manual_review_status": "pending_user_shape_review" if in_review_packet else "not_in_chart_review_packet",
            "approved_for_daily": "false",
            "production_readiness": "not_production_ready_research_only",
            "generated_at": generated_at,
        }
        rows.append(output)

    audit = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in audit.columns:
            audit[column] = ""
    invalid_initial = sorted(set(audit["initial_stage"]) - INITIAL_STAGES)
    invalid_confirmation = sorted(set(audit["confirmation_stage"]) - CONFIRMATION_STAGES)
    invalid_transition = sorted(set(audit["transition_status"]) - TRANSITION_STATUSES)
    if invalid_initial:
        raise SystemExit(f"ERROR: invalid initial stages: {invalid_initial}")
    if invalid_confirmation:
        raise SystemExit(f"ERROR: invalid confirmation stages: {invalid_confirmation}")
    if invalid_transition:
        raise SystemExit(f"ERROR: invalid transition statuses: {invalid_transition}")
    forbidden = sorted(set(audit.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in observation/confirmation audit: {forbidden}")
    return audit[OUTPUT_COLUMNS]


def markdown_table(data: pd.DataFrame | list[dict[str, Any]], columns: list[str], limit: int = 40) -> list[str]:
    df = data if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    if df.empty:
        return ["_No rows._"]
    rows = df.head(limit).to_dict("records")
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def count_table(df: pd.DataFrame, column: str) -> pd.DataFrame:
    counter = Counter(df[column].astype(str))
    return pd.DataFrame([{"bucket": key, "count": count} for key, count in counter.most_common()])


def rate(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return ""
    return f"{numerator / denominator * 100.0:.2f}%"


def performance_by(df: pd.DataFrame, group_column: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for group_value, group in df.groupby(group_column, dropna=False):
        mature = group["a_mature"].map(bool_value)
        returns = pd.to_numeric(group["a_return_pct"], errors="coerce")
        mature_returns = returns[mature]
        wins = int((mature_returns > 0).sum())
        mature_count = int(mature.sum())
        rows.append(
            {
                group_column: group_value,
                "sample_size": len(group),
                "mature_sample_size": mature_count,
                "win_rate": rate(wins, mature_count),
                "avg_a_return_pct": "" if mature_returns.empty else f"{float(mature_returns.mean()):.4f}",
                "tdcc_any_age7_count": int(group["tdcc_any_age7"].map(bool_value).sum()),
            }
        )
    return pd.DataFrame(rows).sort_values(["sample_size", group_column], ascending=[False, True])


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    total = len(audit)
    review = audit[audit["in_manual_review_packet"].map(bool_value)].copy()
    observation_count = int(audit["observation_stage_eligible"].map(bool_value).sum())
    confirmation_count = int(audit["confirmation_stage_eligible"].map(bool_value).sum())
    price_only_count = int(audit["price_confirmation_only"].map(bool_value).sum())
    cross = (
        audit.groupby(["initial_stage", "confirmation_stage"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["initial_stage", "confirmation_stage"])
    )
    lines: list[str] = [
        "# W-Bottom Observation vs Confirmation Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- rows: `{total}` dedup candidates",
        f"- manual_review_packet_rows: `{len(review)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: observation-stage candidates and neckline-confirmation candidates are intentionally evaluated as separate research surfaces.",
        "",
        "## Headline Counts",
        "",
        "| metric | count | rate |",
        "| --- | ---: | ---: |",
        f"| observation-stage eligible | {observation_count} | {rate(observation_count, total)} |",
        f"| volume-confirmed neckline breakout | {confirmation_count} | {rate(confirmation_count, total)} |",
        f"| price-confirmed without volume | {price_only_count} | {rate(price_only_count, total)} |",
        f"| in manual chart review packet | {len(review)} | {rate(len(review), total)} |",
        "",
        "## Initial Stage Counts",
        "",
        *markdown_table(count_table(audit, "initial_stage"), ["bucket", "count"], limit=20),
        "",
        "## Confirmation Stage Counts",
        "",
        *markdown_table(count_table(audit, "confirmation_stage"), ["bucket", "count"], limit=20),
        "",
        "## Transition Status Counts",
        "",
        *markdown_table(count_table(audit, "transition_status"), ["bucket", "count"], limit=30),
        "",
        "## Initial Stage X Confirmation Stage",
        "",
        *markdown_table(cross, ["initial_stage", "confirmation_stage", "count"], limit=80),
        "",
        "## A-Path Performance By Transition Status",
        "",
        *markdown_table(
            performance_by(audit, "transition_status"),
            ["transition_status", "sample_size", "mature_sample_size", "win_rate", "avg_a_return_pct", "tdcc_any_age7_count"],
            limit=40,
        ),
        "",
        "## Manual Review Packet Cross-Check",
        "",
        *markdown_table(count_table(review, "transition_status"), ["bucket", "count"], limit=30),
        "",
        "## Review Sample",
        "",
        *markdown_table(
            audit[
                [
                    "stock_id",
                    "signal_date",
                    "initial_stage",
                    "confirmation_stage",
                    "transition_status",
                    "primary_review_flag",
                    "definition_status",
                    "slope_curvature_category",
                    "a_return_pct",
                ]
            ],
            [
                "stock_id",
                "signal_date",
                "initial_stage",
                "confirmation_stage",
                "transition_status",
                "primary_review_flag",
                "definition_status",
                "slope_curvature_category",
                "a_return_pct",
            ],
            limit=40,
        ),
    ]
    LATEST_AUDIT_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    audit = build_audit(generated_at)
    if audit.empty:
        raise SystemExit("ERROR: W-bottom observation/confirmation audit produced no rows")
    write_csv(audit, LATEST_AUDIT_CSV)
    write_csv(audit, HISTORY_AUDIT_CSV)
    write_markdown(audit, generated_at)
    print(f"Saved: {LATEST_AUDIT_CSV} rows={len(audit)}")
    print(f"Saved: {LATEST_AUDIT_MD}")
    print(f"Saved: {HISTORY_AUDIT_CSV} rows={len(audit)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
