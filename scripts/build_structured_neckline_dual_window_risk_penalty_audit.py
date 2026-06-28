from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from build_structured_neckline_dual_window_context_rule_audit import (
    DUAL_WINDOW_RULE_SCOPE_ID as SOURCE_DUAL_WINDOW_RULE_SCOPE_ID,
    LATEST_DETAIL_CSV as SOURCE_DUAL_WINDOW_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_DUAL_WINDOW_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_DUAL_WINDOW_RESEARCH_ID,
)
from build_structured_neckline_retest_entry_exit_grid import metric_text, safe_str


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_dual_window_risk_penalty_audit"
PARAMETER_SET_ID = "structured_neckline_dual_window_risk_penalty_audit_20260629"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
RISK_PENALTY_SCOPE_ID = "dual_window_45_pass_90_bearish_risk_penalty_grid"

SOURCE_RULE_ID = "dual_45_entry_90_risk_warning"

RISK_RULE_IDS = [
    "strict_45_90_non_bearish",
    "broad_45_non_bearish_with_90_warning",
    "confirmed_plus_risk_penalty_le_1",
    "confirmed_plus_risk_penalty_le_2",
    "confirmed_plus_risk_penalty_le_3",
    "confirmed_plus_risk_return90_ge_neg10",
    "confirmed_plus_risk_return90_ge_neg5",
    "confirmed_plus_risk_drawdown90_ge_neg25",
    "confirmed_plus_risk_drawdown90_ge_neg20",
    "confirmed_plus_risk_slope90_ge_neg2",
    "confirmed_plus_risk_slope90_ge_0",
    "confirmed_plus_risk_short_return45_ge_5",
    "confirmed_plus_risk_short_return45_ge_8",
    "confirmed_plus_risk_short_slope45_ge_2",
    "confirmed_plus_risk_short_strength_return45_ge_5_slope45_ge_2",
    "confirmed_plus_risk_mild_damage_return90_ge_neg10_drawdown90_ge_neg25",
    "confirmed_plus_risk_strict_repair_return45_ge_5_slope45_ge_2_return90_ge_neg15",
]

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_risk_penalty_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_risk_penalty_audit_summary_latest.csv"
LATEST_MANUAL_ALIGNMENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_risk_penalty_manual_alignment_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_risk_penalty_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_dual_window_risk_penalty_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_dual_window_risk_penalty_audit_summary.csv"
HISTORY_MANUAL_ALIGNMENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_dual_window_risk_penalty_manual_alignment.csv"

DETAIL_COLUMNS = [
    "research_id",
    "source_dual_window_research_id",
    "source_dual_window_parameter_set_id",
    "source_dual_window_rule_scope_id",
    "source_candidate_rule_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "risk_penalty_scope_id",
    "risk_penalty_rule_id",
    "risk_penalty_candidate_accept",
    "risk_penalty_candidate_status",
    "risk_penalty_points",
    "risk_penalty_flags",
    "source_event_key",
    "event_family_id",
    "source_segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "in_low_position_le60_market_bull",
    "failure_exit_rule_id",
    "entry_price",
    "exit_date",
    "exit_price",
    "holding_days",
    "return_pct",
    "max_close_return_pct",
    "min_close_return_pct",
    "outcome_result",
    "exit_reason",
    "manual_label_scope_id",
    "manual_label_status",
    "manual_label_values",
    "manual_label_rows",
    "manual_label_conflict_for_event",
    "manual_alignment_for_rule",
    "context_45",
    "filter_45",
    "return_45",
    "slope20_45",
    "drawdown_45",
    "context_90",
    "filter_90",
    "return_90",
    "slope20_90",
    "drawdown_90",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "risk_penalty_scope_id",
    "summary_scope_id",
    "analysis_scope_id",
    "risk_penalty_rule_id",
    "risk_penalty_candidate_status",
    "sample_count",
    "unique_events",
    "win_count",
    "neutral_count",
    "loss_count",
    "other_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

MANUAL_ALIGNMENT_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "risk_penalty_scope_id",
    "risk_penalty_rule_id",
    "manual_alignment_scope_id",
    "manual_good_rows",
    "manual_good_accepted_rows",
    "manual_good_rejected_rows",
    "manual_bad_rows",
    "manual_bad_accepted_rows",
    "manual_bad_rejected_rows",
    "manual_conflict_rows",
    "manual_good_false_negative_rate_pct",
    "manual_bad_false_positive_rate_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def pct_text(numerator: int | float, denominator: int | float) -> str:
    if denominator == 0:
        return ""
    return f"{float(numerator) / float(denominator) * 100.0:.4f}"


def to_float(value: object) -> float | None:
    try:
        text = safe_str(value)
        if not text:
            return None
        return float(text)
    except (TypeError, ValueError):
        return None


def ge(value: float | None, threshold: float) -> bool:
    return value is not None and value >= threshold


def lt(value: float | None, threshold: float) -> bool:
    return value is not None and value < threshold


def is_non_bearish(value: object) -> bool:
    return safe_str(value) == "auto_non_bearish"


def is_bearish(value: object) -> bool:
    return safe_str(value) == "auto_bearish"


def risk_penalty_points(row: pd.Series) -> tuple[int, str]:
    flags: list[str] = []
    points = 0

    return_45 = to_float(row.get("return_45"))
    slope_45 = to_float(row.get("slope20_45"))
    return_90 = to_float(row.get("return_90"))
    slope_90 = to_float(row.get("slope20_90"))
    drawdown_90 = to_float(row.get("drawdown_90"))

    if is_bearish(row.get("filter_90")):
        points += 2
        flags.append("long_90_bearish_base_risk")
    if lt(return_90, -10.0):
        points += 1
        flags.append("return90_below_neg10")
    if lt(return_90, -20.0):
        points += 1
        flags.append("return90_below_neg20")
    if lt(drawdown_90, -25.0):
        points += 1
        flags.append("drawdown90_below_neg25")
    if lt(drawdown_90, -35.0):
        points += 1
        flags.append("drawdown90_below_neg35")
    if lt(slope_90, -2.0):
        points += 1
        flags.append("slope90_below_neg2")
    if lt(slope_90, -4.0):
        points += 1
        flags.append("slope90_below_neg4")
    if ge(return_45, 5.0):
        points -= 1
        flags.append("repair_credit_return45_ge_5")
    if ge(slope_45, 2.0):
        points -= 1
        flags.append("repair_credit_slope45_ge_2")
    if ge(return_45, 8.0) and ge(slope_45, 3.0):
        points -= 1
        flags.append("repair_credit_return45_ge_8_slope45_ge_3")

    return max(points, 0), ";".join(flags)


def evaluate_rule(rule_id: str, row: pd.Series, points: int) -> tuple[bool, str]:
    pass_45 = is_non_bearish(row.get("filter_45"))
    pass_90 = is_non_bearish(row.get("filter_90"))
    bearish_90 = is_bearish(row.get("filter_90"))
    return_45 = to_float(row.get("return_45"))
    slope_45 = to_float(row.get("slope20_45"))
    return_90 = to_float(row.get("return_90"))
    slope_90 = to_float(row.get("slope20_90"))
    drawdown_90 = to_float(row.get("drawdown_90"))

    if not pass_45:
        return False, "rejected_45_bearish_or_unknown"
    if pass_90:
        return True, "accepted_clean_45_90_non_bearish"

    if not bearish_90:
        return rule_id == "broad_45_non_bearish_with_90_warning", (
            "accepted_45_non_bearish_90_unknown"
            if rule_id == "broad_45_non_bearish_with_90_warning"
            else "rejected_90_unknown"
        )

    if rule_id == "strict_45_90_non_bearish":
        return False, "rejected_90_bearish_risk"
    if rule_id == "broad_45_non_bearish_with_90_warning":
        return True, "accepted_risk_all_45_non_bearish_90_bearish"
    if rule_id == "confirmed_plus_risk_penalty_le_1":
        return points <= 1, "accepted_risk_penalty_le_1" if points <= 1 else "rejected_risk_penalty_gt_1"
    if rule_id == "confirmed_plus_risk_penalty_le_2":
        return points <= 2, "accepted_risk_penalty_le_2" if points <= 2 else "rejected_risk_penalty_gt_2"
    if rule_id == "confirmed_plus_risk_penalty_le_3":
        return points <= 3, "accepted_risk_penalty_le_3" if points <= 3 else "rejected_risk_penalty_gt_3"
    if rule_id == "confirmed_plus_risk_return90_ge_neg10":
        return ge(return_90, -10.0), "accepted_risk_return90_ge_neg10" if ge(return_90, -10.0) else "rejected_risk_return90_lt_neg10"
    if rule_id == "confirmed_plus_risk_return90_ge_neg5":
        return ge(return_90, -5.0), "accepted_risk_return90_ge_neg5" if ge(return_90, -5.0) else "rejected_risk_return90_lt_neg5"
    if rule_id == "confirmed_plus_risk_drawdown90_ge_neg25":
        return ge(drawdown_90, -25.0), "accepted_risk_drawdown90_ge_neg25" if ge(drawdown_90, -25.0) else "rejected_risk_drawdown90_lt_neg25"
    if rule_id == "confirmed_plus_risk_drawdown90_ge_neg20":
        return ge(drawdown_90, -20.0), "accepted_risk_drawdown90_ge_neg20" if ge(drawdown_90, -20.0) else "rejected_risk_drawdown90_lt_neg20"
    if rule_id == "confirmed_plus_risk_slope90_ge_neg2":
        return ge(slope_90, -2.0), "accepted_risk_slope90_ge_neg2" if ge(slope_90, -2.0) else "rejected_risk_slope90_lt_neg2"
    if rule_id == "confirmed_plus_risk_slope90_ge_0":
        return ge(slope_90, 0.0), "accepted_risk_slope90_ge_0" if ge(slope_90, 0.0) else "rejected_risk_slope90_lt_0"
    if rule_id == "confirmed_plus_risk_short_return45_ge_5":
        return ge(return_45, 5.0), "accepted_risk_return45_ge_5" if ge(return_45, 5.0) else "rejected_risk_return45_lt_5"
    if rule_id == "confirmed_plus_risk_short_return45_ge_8":
        return ge(return_45, 8.0), "accepted_risk_return45_ge_8" if ge(return_45, 8.0) else "rejected_risk_return45_lt_8"
    if rule_id == "confirmed_plus_risk_short_slope45_ge_2":
        return ge(slope_45, 2.0), "accepted_risk_slope45_ge_2" if ge(slope_45, 2.0) else "rejected_risk_slope45_lt_2"
    if rule_id == "confirmed_plus_risk_short_strength_return45_ge_5_slope45_ge_2":
        accepted = ge(return_45, 5.0) and ge(slope_45, 2.0)
        return accepted, "accepted_risk_short_strength" if accepted else "rejected_risk_short_strength_missing"
    if rule_id == "confirmed_plus_risk_mild_damage_return90_ge_neg10_drawdown90_ge_neg25":
        accepted = ge(return_90, -10.0) and ge(drawdown_90, -25.0)
        return accepted, "accepted_risk_mild_long_damage" if accepted else "rejected_risk_long_damage_too_high"
    if rule_id == "confirmed_plus_risk_strict_repair_return45_ge_5_slope45_ge_2_return90_ge_neg15":
        accepted = ge(return_45, 5.0) and ge(slope_45, 2.0) and ge(return_90, -15.0)
        return accepted, "accepted_risk_strict_repair" if accepted else "rejected_risk_strict_repair_missing"

    raise ValueError(f"unknown risk rule: {rule_id}")


def manual_alignment(manual_status: str, accepted: bool) -> str:
    if manual_status == "manual_conflict":
        return "manual_conflict_not_scored"
    if manual_status == "manual_good" and accepted:
        return "manual_good_accepted"
    if manual_status == "manual_good" and not accepted:
        return "manual_good_rejected_false_negative"
    if manual_status == "manual_bad" and accepted:
        return "manual_bad_accepted_false_positive"
    if manual_status == "manual_bad" and not accepted:
        return "manual_bad_rejected"
    return "unlabeled_not_scored"


def source_rows() -> pd.DataFrame:
    source = read_csv(SOURCE_DUAL_WINDOW_DETAIL_CSV)
    source = source.loc[source["candidate_rule_id"].eq(SOURCE_RULE_ID)].copy()
    if source.empty:
        raise ValueError(f"missing source rows for {SOURCE_RULE_ID}")
    if source["source_event_key"].duplicated().any():
        duplicated = source.loc[source["source_event_key"].duplicated(), "source_event_key"].head(5).tolist()
        raise ValueError(f"source rows must be one row per event; duplicated={duplicated}")
    return source


def build_detail() -> pd.DataFrame:
    source = source_rows()
    generated_at = now_text()
    rows: list[dict[str, str]] = []

    for _, base in source.iterrows():
        points, flags = risk_penalty_points(base)
        for rule_id in RISK_RULE_IDS:
            accepted, status = evaluate_rule(rule_id, base, points)
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_dual_window_research_id": SOURCE_DUAL_WINDOW_RESEARCH_ID,
                    "source_dual_window_parameter_set_id": SOURCE_DUAL_WINDOW_PARAMETER_SET_ID,
                    "source_dual_window_rule_scope_id": SOURCE_DUAL_WINDOW_RULE_SCOPE_ID,
                    "source_candidate_rule_id": SOURCE_RULE_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "risk_penalty_scope_id": RISK_PENALTY_SCOPE_ID,
                    "risk_penalty_rule_id": rule_id,
                    "risk_penalty_candidate_accept": "true" if accepted else "false",
                    "risk_penalty_candidate_status": status,
                    "risk_penalty_points": str(points),
                    "risk_penalty_flags": flags,
                    "source_event_key": safe_str(base.get("source_event_key")),
                    "event_family_id": safe_str(base.get("event_family_id")),
                    "source_segment_id": safe_str(base.get("source_segment_id")),
                    "stock_id": safe_str(base.get("stock_id")),
                    "stock_name": safe_str(base.get("stock_name")),
                    "signal_date": safe_str(base.get("signal_date")),
                    "retest_date": safe_str(base.get("retest_date")),
                    "retest_attack_date": safe_str(base.get("retest_attack_date")),
                    "retest_entry_date": safe_str(base.get("retest_entry_date")),
                    "market_regime": safe_str(base.get("market_regime")),
                    "low_position_120_pct": safe_str(base.get("low_position_120_pct")),
                    "base_width_pct": safe_str(base.get("base_width_pct")),
                    "support_touch_count": safe_str(base.get("support_touch_count")),
                    "in_low_position_le60_market_bull": safe_str(base.get("in_low_position_le60_market_bull")),
                    "failure_exit_rule_id": safe_str(base.get("failure_exit_rule_id")),
                    "entry_price": safe_str(base.get("entry_price")),
                    "exit_date": safe_str(base.get("exit_date")),
                    "exit_price": safe_str(base.get("exit_price")),
                    "holding_days": safe_str(base.get("holding_days")),
                    "return_pct": safe_str(base.get("return_pct")),
                    "max_close_return_pct": safe_str(base.get("max_close_return_pct")),
                    "min_close_return_pct": safe_str(base.get("min_close_return_pct")),
                    "outcome_result": safe_str(base.get("outcome_result")),
                    "exit_reason": safe_str(base.get("exit_reason")),
                    "manual_label_scope_id": safe_str(base.get("manual_label_scope_id")),
                    "manual_label_status": safe_str(base.get("manual_label_status")),
                    "manual_label_values": safe_str(base.get("manual_label_values")),
                    "manual_label_rows": safe_str(base.get("manual_label_rows")),
                    "manual_label_conflict_for_event": safe_str(base.get("manual_label_conflict_for_event")),
                    "manual_alignment_for_rule": manual_alignment(safe_str(base.get("manual_label_status")), accepted),
                    "context_45": safe_str(base.get("context_45")),
                    "filter_45": safe_str(base.get("filter_45")),
                    "return_45": safe_str(base.get("return_45")),
                    "slope20_45": safe_str(base.get("slope20_45")),
                    "drawdown_45": safe_str(base.get("drawdown_45")),
                    "context_90": safe_str(base.get("context_90")),
                    "filter_90": safe_str(base.get("filter_90")),
                    "return_90": safe_str(base.get("return_90")),
                    "slope20_90": safe_str(base.get("slope20_90")),
                    "drawdown_90": safe_str(base.get("drawdown_90")),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )
    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def numeric_return(frame: pd.DataFrame) -> pd.Series:
    return pd.to_numeric(frame["return_pct"], errors="coerce")


def summary_row(summary_scope_id: str, analysis_scope_id: str, group: pd.DataFrame) -> dict[str, str]:
    returns = numeric_return(group)
    outcomes = group["outcome_result"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    other = len(group) - win - neutral - loss
    denominator = win + loss
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "risk_penalty_scope_id": RISK_PENALTY_SCOPE_ID,
        "summary_scope_id": summary_scope_id,
        "analysis_scope_id": analysis_scope_id,
        "risk_penalty_rule_id": safe_str(group["risk_penalty_rule_id"].iloc[0]),
        "risk_penalty_candidate_status": safe_str(group["risk_penalty_candidate_status"].iloc[0])
        if summary_scope_id == "accepted_by_candidate_status"
        else "all_accepted",
        "sample_count": str(len(group)),
        "unique_events": str(group["source_event_key"].nunique()),
        "win_count": str(win),
        "neutral_count": str(neutral),
        "loss_count": str(loss),
        "other_count": str(other),
        "pure_win_rate_pct": pct_text(win, denominator),
        "neutral_inclusive_success_rate_pct": pct_text(win + neutral, len(group)),
        "positive_return_rate_pct": pct_text(int((returns > 0).sum()), int(returns.notna().sum())),
        "avg_return_pct": metric_text(float(returns.mean())) if returns.notna().any() else "",
        "median_return_pct": metric_text(float(returns.median())) if returns.notna().any() else "",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": now_text(),
    }


def build_summary(detail: pd.DataFrame) -> pd.DataFrame:
    accepted = detail.loc[detail["risk_penalty_candidate_accept"].eq("true")].copy()
    scopes = [
        ("all_retest_entries", accepted),
        ("low_position_le60_market_bull", accepted.loc[accepted["in_low_position_le60_market_bull"].eq("true")]),
        ("manual_good_non_conflict", accepted.loc[accepted["manual_label_status"].eq("manual_good")]),
        ("manual_bad_non_conflict", accepted.loc[accepted["manual_label_status"].eq("manual_bad")]),
    ]
    rows: list[dict[str, str]] = []
    for analysis_scope_id, scope in scopes:
        if scope.empty:
            continue
        for _, group in scope.groupby("risk_penalty_rule_id", dropna=False):
            rows.append(summary_row("accepted_overall", analysis_scope_id, group))
        for _, group in scope.groupby(["risk_penalty_rule_id", "risk_penalty_candidate_status"], dropna=False):
            rows.append(summary_row("accepted_by_candidate_status", analysis_scope_id, group))
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def build_manual_alignment(detail: pd.DataFrame) -> pd.DataFrame:
    manual = detail.loc[detail["manual_label_status"].isin(["manual_good", "manual_bad", "manual_conflict"])].copy()
    rows: list[dict[str, str]] = []
    for rule_id, group in manual.groupby("risk_penalty_rule_id", dropna=False):
        good = group.loc[group["manual_label_status"].eq("manual_good")]
        bad = group.loc[group["manual_label_status"].eq("manual_bad")]
        conflict = group.loc[group["manual_label_status"].eq("manual_conflict")]
        good_accepted = int(good["risk_penalty_candidate_accept"].eq("true").sum())
        bad_accepted = int(bad["risk_penalty_candidate_accept"].eq("true").sum())
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "risk_penalty_scope_id": RISK_PENALTY_SCOPE_ID,
                "risk_penalty_rule_id": safe_str(rule_id),
                "manual_alignment_scope_id": "manual_non_conflict_and_conflict_totals",
                "manual_good_rows": str(len(good)),
                "manual_good_accepted_rows": str(good_accepted),
                "manual_good_rejected_rows": str(len(good) - good_accepted),
                "manual_bad_rows": str(len(bad)),
                "manual_bad_accepted_rows": str(bad_accepted),
                "manual_bad_rejected_rows": str(len(bad) - bad_accepted),
                "manual_conflict_rows": str(len(conflict)),
                "manual_good_false_negative_rate_pct": pct_text(len(good) - good_accepted, len(good)),
                "manual_bad_false_positive_rate_pct": pct_text(bad_accepted, len(bad)),
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": now_text(),
            }
        )
    return pd.DataFrame(rows, columns=MANUAL_ALIGNMENT_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, manual_alignment_df: pd.DataFrame) -> None:
    lines = [
        "# Structured-Neckline Dual Window Risk Penalty Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- source_rule_id: `{SOURCE_RULE_ID}`",
        f"- risk_penalty_scope_id: `{RISK_PENALTY_SCOPE_ID}`",
        f"- source_events: `{detail['source_event_key'].nunique() if not detail.empty else 0}`",
        f"- detail_rows: `{len(detail)}`",
        "- approved_for_daily: `false`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "",
        "## Low-Position Bull Accepted Overall",
        "",
    ]
    low = summary.loc[
        summary["summary_scope_id"].eq("accepted_overall")
        & summary["analysis_scope_id"].eq("low_position_le60_market_bull")
    ].sort_values("risk_penalty_rule_id")
    for _, row in low.iterrows():
        lines.append(
            "- "
            f"{row['risk_penalty_rule_id']}: sample=`{row['sample_count']}`, "
            f"success=`{row['neutral_inclusive_success_rate_pct']}`, "
            f"pure_win=`{row['pure_win_rate_pct']}`, avg_return_pct=`{row['avg_return_pct']}`, "
            f"median_return_pct=`{row['median_return_pct']}`"
        )

    lines.extend(["", "## Manual Alignment", ""])
    for _, row in manual_alignment_df.sort_values("risk_penalty_rule_id").iterrows():
        lines.append(
            "- "
            f"{row['risk_penalty_rule_id']}: good_rejected=`{row['manual_good_rejected_rows']}/"
            f"{row['manual_good_rows']}`, bad_accepted=`{row['manual_bad_accepted_rows']}/"
            f"{row['manual_bad_rows']}`"
        )

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This is a research-only risk penalty grid for the 45-session pass / 90-session bearish-risk group.",
            "- It is not a production score, rank, filter, or model condition.",
            "- It does not write research variants back to production baseline.",
        ]
    )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    detail = build_detail()
    summary = build_summary(detail)
    manual_alignment_df = build_manual_alignment(detail)
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    detail.to_csv(LATEST_DETAIL_CSV, index=False, encoding="utf-8")
    summary.to_csv(LATEST_SUMMARY_CSV, index=False, encoding="utf-8")
    manual_alignment_df.to_csv(LATEST_MANUAL_ALIGNMENT_CSV, index=False, encoding="utf-8")
    detail.to_csv(HISTORY_DETAIL_CSV, index=False, encoding="utf-8")
    summary.to_csv(HISTORY_SUMMARY_CSV, index=False, encoding="utf-8")
    manual_alignment_df.to_csv(HISTORY_MANUAL_ALIGNMENT_CSV, index=False, encoding="utf-8")
    write_markdown(detail, summary, manual_alignment_df)
    print(
        "structured neckline dual window risk penalty audit built "
        f"detail_rows={len(detail)} summary_rows={len(summary)} manual_alignment_rows={len(manual_alignment_df)}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV}")
    print(f"latest_summary={LATEST_SUMMARY_CSV}")
    print(f"latest_manual_alignment={LATEST_MANUAL_ALIGNMENT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
