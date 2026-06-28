from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from build_structured_neckline_context_window_grid_audit import (
    CONTEXT_WINDOW_GRID_SCOPE_ID as SOURCE_CONTEXT_WINDOW_GRID_SCOPE_ID,
    LATEST_DETAIL_CSV as CONTEXT_WINDOW_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_CONTEXT_WINDOW_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_CONTEXT_WINDOW_RESEARCH_ID,
)
from build_structured_neckline_retest_entry_exit_grid import metric_text, safe_str


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_dual_window_context_rule_audit"
PARAMETER_SET_ID = "structured_neckline_dual_window_context_rule_audit_20260629"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
DUAL_WINDOW_RULE_SCOPE_ID = "dual_window_pre_signal_context_candidate_rules"

WINDOWS = [30, 45, 60, 90]
PRIMARY_WINDOW = "45"
LONG_WINDOW = "90"

RULE_IDS = [
    "single_45_non_bearish",
    "single_90_non_bearish",
    "dual_45_entry_90_risk_warning",
    "dual_45_and_90_non_bearish",
    "dual_45_repaired_90_bearish_watchlist",
    "dual_45_or_90_non_bearish",
]

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_context_rule_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_context_rule_audit_summary_latest.csv"
LATEST_MANUAL_ALIGNMENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_context_rule_manual_alignment_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_context_rule_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_dual_window_context_rule_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_dual_window_context_rule_audit_summary.csv"
HISTORY_MANUAL_ALIGNMENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_dual_window_context_rule_manual_alignment.csv"

DETAIL_COLUMNS = [
    "research_id",
    "source_context_window_research_id",
    "source_context_window_parameter_set_id",
    "source_context_window_grid_scope_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "dual_window_rule_scope_id",
    "candidate_rule_id",
    "candidate_accept",
    "candidate_rule_status",
    "long_window_risk_status",
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
    "context_30",
    "filter_30",
    "return_30",
    "slope20_30",
    "drawdown_30",
    "context_45",
    "filter_45",
    "return_45",
    "slope20_45",
    "drawdown_45",
    "context_60",
    "filter_60",
    "return_60",
    "slope20_60",
    "drawdown_60",
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
    "dual_window_rule_scope_id",
    "summary_scope_id",
    "analysis_scope_id",
    "candidate_rule_id",
    "candidate_rule_status",
    "long_window_risk_status",
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
    "dual_window_rule_scope_id",
    "candidate_rule_id",
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


def is_non_bearish(value: str) -> bool:
    return value == "auto_non_bearish"


def is_bearish(value: str) -> bool:
    return value == "auto_bearish"


def pct_text(numerator: int | float, denominator: int | float) -> str:
    if denominator == 0:
        return ""
    return f"{float(numerator) / float(denominator) * 100.0:.4f}"


def context_by_window(group: pd.DataFrame) -> dict[str, pd.Series]:
    result: dict[str, pd.Series] = {}
    for _, row in group.iterrows():
        result[safe_str(row.get("window_sessions_requested"))] = row
    return result


def long_window_risk_status(filter_90: str) -> str:
    if is_non_bearish(filter_90):
        return "long_90_non_bearish_confirmed"
    if is_bearish(filter_90):
        return "long_90_bearish_risk_warning"
    return "long_90_unknown"


def evaluate_rule(rule_id: str, filter_45: str, filter_90: str) -> tuple[bool, str]:
    pass_45 = is_non_bearish(filter_45)
    pass_90 = is_non_bearish(filter_90)
    bearish_90 = is_bearish(filter_90)

    if rule_id == "single_45_non_bearish":
        return pass_45, "accepted_45_non_bearish" if pass_45 else "rejected_45_bearish_or_unknown"
    if rule_id == "single_90_non_bearish":
        return pass_90, "accepted_90_non_bearish" if pass_90 else "rejected_90_bearish_or_unknown"
    if rule_id == "dual_45_entry_90_risk_warning":
        if pass_45 and pass_90:
            return True, "accepted_45_non_bearish_90_confirmed"
        if pass_45 and bearish_90:
            return True, "accepted_45_non_bearish_90_bearish_risk"
        if pass_45:
            return True, "accepted_45_non_bearish_90_unknown"
        return False, "rejected_45_bearish_or_unknown"
    if rule_id == "dual_45_and_90_non_bearish":
        return pass_45 and pass_90, "accepted_45_and_90_non_bearish" if pass_45 and pass_90 else "rejected_not_both_windows"
    if rule_id == "dual_45_repaired_90_bearish_watchlist":
        accepted = pass_45 and bearish_90
        return accepted, "accepted_45_repaired_90_bearish_watchlist" if accepted else "rejected_not_short_repaired_long_bearish"
    if rule_id == "dual_45_or_90_non_bearish":
        accepted = pass_45 or pass_90
        return accepted, "accepted_45_or_90_non_bearish" if accepted else "rejected_45_and_90_bearish_or_unknown"
    raise ValueError(f"unknown rule_id: {rule_id}")


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


def first_row_for_event(contexts: dict[str, pd.Series]) -> pd.Series:
    if PRIMARY_WINDOW in contexts:
        return contexts[PRIMARY_WINDOW]
    return contexts[sorted(contexts.keys())[0]]


def window_value(contexts: dict[str, pd.Series], window: int, column: str) -> str:
    row = contexts.get(str(window))
    if row is None:
        return ""
    return safe_str(row.get(column))


def build_detail() -> pd.DataFrame:
    source = read_csv(CONTEXT_WINDOW_DETAIL_CSV)
    generated_at = now_text()
    rows: list[dict[str, str]] = []

    for event_key, group in source.groupby("source_event_key", dropna=False):
        contexts = context_by_window(group)
        base = first_row_for_event(contexts)
        filter_45 = window_value(contexts, 45, "auto_context_filter_result")
        filter_90 = window_value(contexts, 90, "auto_context_filter_result")
        risk_status = long_window_risk_status(filter_90)

        for rule_id in RULE_IDS:
            accepted, status = evaluate_rule(rule_id, filter_45, filter_90)
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_context_window_research_id": SOURCE_CONTEXT_WINDOW_RESEARCH_ID,
                    "source_context_window_parameter_set_id": SOURCE_CONTEXT_WINDOW_PARAMETER_SET_ID,
                    "source_context_window_grid_scope_id": SOURCE_CONTEXT_WINDOW_GRID_SCOPE_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "dual_window_rule_scope_id": DUAL_WINDOW_RULE_SCOPE_ID,
                    "candidate_rule_id": rule_id,
                    "candidate_accept": "true" if accepted else "false",
                    "candidate_rule_status": status,
                    "long_window_risk_status": risk_status,
                    "source_event_key": safe_str(event_key),
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
                    "context_30": window_value(contexts, 30, "auto_pre_signal_context"),
                    "filter_30": window_value(contexts, 30, "auto_context_filter_result"),
                    "return_30": window_value(contexts, 30, "auto_context_return_pct"),
                    "slope20_30": window_value(contexts, 30, "auto_context_slope_pct_per_20d"),
                    "drawdown_30": window_value(contexts, 30, "auto_context_max_drawdown_pct"),
                    "context_45": window_value(contexts, 45, "auto_pre_signal_context"),
                    "filter_45": filter_45,
                    "return_45": window_value(contexts, 45, "auto_context_return_pct"),
                    "slope20_45": window_value(contexts, 45, "auto_context_slope_pct_per_20d"),
                    "drawdown_45": window_value(contexts, 45, "auto_context_max_drawdown_pct"),
                    "context_60": window_value(contexts, 60, "auto_pre_signal_context"),
                    "filter_60": window_value(contexts, 60, "auto_context_filter_result"),
                    "return_60": window_value(contexts, 60, "auto_context_return_pct"),
                    "slope20_60": window_value(contexts, 60, "auto_context_slope_pct_per_20d"),
                    "drawdown_60": window_value(contexts, 60, "auto_context_max_drawdown_pct"),
                    "context_90": window_value(contexts, 90, "auto_pre_signal_context"),
                    "filter_90": filter_90,
                    "return_90": window_value(contexts, 90, "auto_context_return_pct"),
                    "slope20_90": window_value(contexts, 90, "auto_context_slope_pct_per_20d"),
                    "drawdown_90": window_value(contexts, 90, "auto_context_max_drawdown_pct"),
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
        "dual_window_rule_scope_id": DUAL_WINDOW_RULE_SCOPE_ID,
        "summary_scope_id": summary_scope_id,
        "analysis_scope_id": analysis_scope_id,
        "candidate_rule_id": safe_str(group["candidate_rule_id"].iloc[0]),
        "candidate_rule_status": safe_str(group["candidate_rule_status"].iloc[0])
        if summary_scope_id == "accepted_by_rule_status"
        else "all_accepted",
        "long_window_risk_status": safe_str(group["long_window_risk_status"].iloc[0])
        if summary_scope_id == "accepted_by_long_window_risk"
        else "all_long_window_statuses",
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
    accepted = detail.loc[detail["candidate_accept"].eq("true")].copy()
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
        for _, group in scope.groupby("candidate_rule_id", dropna=False):
            rows.append(summary_row("accepted_overall", analysis_scope_id, group))
        for _, group in scope.groupby(["candidate_rule_id", "candidate_rule_status"], dropna=False):
            rows.append(summary_row("accepted_by_rule_status", analysis_scope_id, group))
        for _, group in scope.groupby(["candidate_rule_id", "long_window_risk_status"], dropna=False):
            rows.append(summary_row("accepted_by_long_window_risk", analysis_scope_id, group))
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def build_manual_alignment(detail: pd.DataFrame) -> pd.DataFrame:
    manual = detail.loc[detail["manual_label_status"].isin(["manual_good", "manual_bad", "manual_conflict"])].copy()
    rows: list[dict[str, str]] = []
    for rule_id, group in manual.groupby("candidate_rule_id", dropna=False):
        good = group.loc[group["manual_label_status"].eq("manual_good")]
        bad = group.loc[group["manual_label_status"].eq("manual_bad")]
        conflict = group.loc[group["manual_label_status"].eq("manual_conflict")]
        good_accepted = int(good["candidate_accept"].eq("true").sum())
        bad_accepted = int(bad["candidate_accept"].eq("true").sum())
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "dual_window_rule_scope_id": DUAL_WINDOW_RULE_SCOPE_ID,
                "candidate_rule_id": safe_str(rule_id),
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


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, manual_alignment: pd.DataFrame) -> None:
    lines = [
        "# Structured-Neckline Dual Window Context Rule Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- dual_window_rule_scope_id: `{DUAL_WINDOW_RULE_SCOPE_ID}`",
        f"- candidate_rules: `{';'.join(RULE_IDS)}`",
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
    ].sort_values("candidate_rule_id")
    for _, row in low.iterrows():
        lines.append(
            "- "
            f"{row['candidate_rule_id']}: sample=`{row['sample_count']}`, "
            f"success=`{row['neutral_inclusive_success_rate_pct']}`, "
            f"avg_return_pct=`{row['avg_return_pct']}`, median_return_pct=`{row['median_return_pct']}`"
        )

    lines.extend(["", "## Manual Alignment", ""])
    for _, row in manual_alignment.sort_values("candidate_rule_id").iterrows():
        lines.append(
            "- "
            f"{row['candidate_rule_id']}: good_rejected=`{row['manual_good_rejected_rows']}`/"
            f"{row['manual_good_rows']}`, bad_accepted=`{row['manual_bad_accepted_rows']}`/"
            f"{row['manual_bad_rows']}`"
        )

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This compares research-only pre-signal context candidate rules.",
            "- It is not a production filter, score, rank, or model condition.",
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
        "structured neckline dual window context rule audit built "
        f"detail_rows={len(detail)} summary_rows={len(summary)} manual_alignment_rows={len(manual_alignment_df)}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV}")
    print(f"latest_summary={LATEST_SUMMARY_CSV}")
    print(f"latest_manual_alignment={LATEST_MANUAL_ALIGNMENT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
