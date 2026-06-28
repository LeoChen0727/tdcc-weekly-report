from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_auto_context_expansion_audit import (
    BASELINE_RULE_ID,
    LATEST_DETAIL_CSV as AUTO_CONTEXT_DETAIL_CSV,
    PARAMETER_SET_ID as AUTO_CONTEXT_PARAMETER_SET_ID,
    RESEARCH_ID as AUTO_CONTEXT_RESEARCH_ID,
    classify_context,
    context_filter_result,
    max_drawdown_pct,
    pct_change,
    read_price_file,
    safe_float,
    slope_pct_per_20d,
)
from build_structured_neckline_manual_chart_label_audit import (
    LATEST_DETAIL_CSV as MANUAL_LABEL_DETAIL_CSV,
    MANUAL_LABEL_SCOPE_ID,
    PARAMETER_SET_ID as MANUAL_LABEL_PARAMETER_SET_ID,
    RESEARCH_ID as MANUAL_LABEL_RESEARCH_ID,
)
from build_structured_neckline_retest_entry_exit_grid import metric_text, normalize_date, safe_str


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_context_window_grid_audit"
PARAMETER_SET_ID = "structured_neckline_context_window_grid_audit_20260629"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
CONTEXT_WINDOW_GRID_SCOPE_ID = "pre_signal_context_window_grid_30_45_60_90"
WINDOWS = [30, 45, 60, 90]

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_context_window_grid_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_context_window_grid_audit_summary_latest.csv"
LATEST_MANUAL_ALIGNMENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_context_window_grid_manual_alignment_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_context_window_grid_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_context_window_grid_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_context_window_grid_audit_summary.csv"
HISTORY_MANUAL_ALIGNMENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_context_window_grid_manual_alignment.csv"

DETAIL_COLUMNS = [
    "research_id",
    "source_auto_context_research_id",
    "source_auto_context_parameter_set_id",
    "source_manual_label_research_id",
    "source_manual_label_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "context_window_grid_scope_id",
    "window_sessions_requested",
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
    "manual_label_packets",
    "manual_label_rows",
    "manual_label_conflict_for_event",
    "auto_pre_signal_context",
    "auto_context_filter_result",
    "auto_context_start",
    "auto_context_end",
    "auto_context_sessions",
    "auto_context_return_pct",
    "auto_context_range_pct",
    "auto_context_slope_pct_per_20d",
    "auto_context_max_drawdown_pct",
    "manual_classifier_alignment",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "context_window_grid_scope_id",
    "analysis_scope_id",
    "window_sessions_requested",
    "auto_pre_signal_context",
    "auto_context_filter_result",
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
    "context_window_grid_scope_id",
    "manual_label_scope_id",
    "window_sessions_requested",
    "alignment_scope_id",
    "manual_classifier_alignment",
    "label_rows",
    "unique_events",
    "manual_good_rows",
    "manual_bad_rows",
    "manual_conflict_rows",
    "manual_good_false_negative_rows",
    "manual_bad_false_positive_rows",
    "manual_good_false_negative_rate_pct",
    "manual_bad_false_positive_rate_pct",
    "avg_return_pct",
    "median_return_pct",
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


def event_key(row: pd.Series) -> str:
    return f"{row.get('stock_id', '')}|{row.get('signal_date', '')}|{row.get('retest_entry_date', '')}"


def pct_text(numerator: int | float, denominator: int | float) -> str:
    if denominator == 0:
        return ""
    return f"{float(numerator) / float(denominator) * 100.0:.4f}"


def event_manual_label_lookup() -> dict[str, dict[str, str]]:
    manual = read_csv(MANUAL_LABEL_DETAIL_CSV)
    lookup: dict[str, dict[str, str]] = {}
    for key, group in manual.groupby("label_event_key", dropna=False):
        labels = sorted(set(group["manual_label"].astype(str)))
        packets = sorted(
            f"{row.label_source_chart_packet}:{row.manual_label}"
            for row in group[["label_source_chart_packet", "manual_label"]].itertuples(index=False)
        )
        conflict = "true" if len(labels) > 1 or group["label_conflict_for_event"].eq("true").any() else "false"
        if conflict == "true":
            status = "manual_conflict"
        elif labels == ["good"]:
            status = "manual_good"
        elif labels == ["bad"]:
            status = "manual_bad"
        else:
            status = "manual_unscored"
        lookup[str(key)] = {
            "manual_label_status": status,
            "manual_label_values": ";".join(labels),
            "manual_label_packets": ";".join(packets),
            "manual_label_rows": str(len(group)),
            "manual_label_conflict_for_event": conflict,
        }
    return lookup


def empty_manual_label() -> dict[str, str]:
    return {
        "manual_label_status": "unlabeled",
        "manual_label_values": "",
        "manual_label_packets": "",
        "manual_label_rows": "0",
        "manual_label_conflict_for_event": "false",
    }


def index_for_date(price: pd.DataFrame, date_value: object) -> int | None:
    target = normalize_date(date_value)
    if not target or "date" not in price.columns:
        return None
    matches = price.index[price["date"].astype(str).map(normalize_date) == target]
    if len(matches) == 0:
        return None
    return int(matches[0])


def compute_context_window(price: pd.DataFrame, signal_date: object, window_sessions: int) -> dict[str, str]:
    if price.empty or "date" not in price.columns:
        return {
            "auto_pre_signal_context": "unknown",
            "auto_context_filter_result": "unknown",
            "auto_context_start": "",
            "auto_context_end": "",
            "auto_context_sessions": "0",
            "auto_context_return_pct": "",
            "auto_context_range_pct": "",
            "auto_context_slope_pct_per_20d": "",
            "auto_context_max_drawdown_pct": "",
        }
    signal_idx = index_for_date(price, signal_date)
    if signal_idx is None or signal_idx <= 1:
        return {
            "auto_pre_signal_context": "unknown",
            "auto_context_filter_result": "unknown",
            "auto_context_start": "",
            "auto_context_end": "",
            "auto_context_sessions": "0",
            "auto_context_return_pct": "",
            "auto_context_range_pct": "",
            "auto_context_slope_pct_per_20d": "",
            "auto_context_max_drawdown_pct": "",
        }

    start_idx = max(0, signal_idx - window_sessions)
    end_idx = signal_idx - 1
    window = price.iloc[start_idx : end_idx + 1].copy()
    if len(window) < 20:
        context = "unknown"
        return_pct = range_pct = slope20 = drawdown = math.nan
    else:
        closes = [safe_float(value) for value in window.get("close", [])]
        highs = pd.to_numeric(window.get("high", ""), errors="coerce").dropna()
        lows = pd.to_numeric(window.get("low", ""), errors="coerce").dropna()
        return_pct = pct_change(closes[-1], closes[0])
        range_pct = (
            (float(highs.max()) / float(lows.min()) - 1.0) * 100.0
            if len(highs) and len(lows) and float(lows.min()) > 0
            else math.nan
        )
        slope20 = slope_pct_per_20d(closes)
        drawdown = max_drawdown_pct(closes)
        context = classify_context(return_pct, range_pct, slope20, drawdown)

    return {
        "auto_pre_signal_context": context,
        "auto_context_filter_result": context_filter_result(context),
        "auto_context_start": normalize_date(price.iloc[start_idx].get("date")),
        "auto_context_end": normalize_date(price.iloc[end_idx].get("date")),
        "auto_context_sessions": str(len(window)),
        "auto_context_return_pct": metric_text(return_pct),
        "auto_context_range_pct": metric_text(range_pct),
        "auto_context_slope_pct_per_20d": metric_text(slope20),
        "auto_context_max_drawdown_pct": metric_text(drawdown),
    }


def manual_classifier_alignment(manual_status: str, auto_filter: str) -> str:
    if manual_status == "manual_conflict":
        return "manual_label_conflict_not_scored"
    if manual_status == "manual_good" and auto_filter == "auto_non_bearish":
        return "manual_good_auto_non_bearish_match"
    if manual_status == "manual_good" and auto_filter == "auto_bearish":
        return "manual_good_auto_bearish_false_negative"
    if manual_status == "manual_bad" and auto_filter == "auto_bearish":
        return "manual_bad_auto_bearish_match"
    if manual_status == "manual_bad" and auto_filter == "auto_non_bearish":
        return "manual_bad_auto_non_bearish_false_positive"
    if manual_status == "unlabeled":
        return "unlabeled_not_scored"
    return "unscored_or_unknown"


def source_events() -> pd.DataFrame:
    source = read_csv(AUTO_CONTEXT_DETAIL_CSV)
    source = source.loc[
        source["failure_exit_rule_id"].eq(BASELINE_RULE_ID)
        & source["source_segment_id"].eq("all_retest_entries")
    ].copy()
    source["source_event_key"] = source.apply(event_key, axis=1)
    source = source.drop_duplicates("source_event_key")
    return source


def build_detail() -> pd.DataFrame:
    generated_at = now_text()
    source = source_events()
    manual_lookup = event_manual_label_lookup()
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, str]] = []

    for _, item in source.iterrows():
        stock_id = safe_str(item.get("stock_id"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        key = safe_str(item.get("source_event_key"))
        manual = manual_lookup.get(key, empty_manual_label())
        for window_sessions in WINDOWS:
            context = compute_context_window(price, item.get("signal_date"), window_sessions)
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_auto_context_research_id": AUTO_CONTEXT_RESEARCH_ID,
                    "source_auto_context_parameter_set_id": AUTO_CONTEXT_PARAMETER_SET_ID,
                    "source_manual_label_research_id": MANUAL_LABEL_RESEARCH_ID,
                    "source_manual_label_parameter_set_id": MANUAL_LABEL_PARAMETER_SET_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "context_window_grid_scope_id": CONTEXT_WINDOW_GRID_SCOPE_ID,
                    "window_sessions_requested": str(window_sessions),
                    "source_event_key": key,
                    "event_family_id": safe_str(item.get("event_family_id")),
                    "source_segment_id": safe_str(item.get("source_segment_id")),
                    "stock_id": stock_id,
                    "stock_name": safe_str(item.get("stock_name")),
                    "signal_date": safe_str(item.get("signal_date")),
                    "retest_date": safe_str(item.get("retest_date")),
                    "retest_attack_date": safe_str(item.get("retest_attack_date")),
                    "retest_entry_date": safe_str(item.get("retest_entry_date")),
                    "market_regime": safe_str(item.get("market_regime")),
                    "low_position_120_pct": safe_str(item.get("low_position_120_pct")),
                    "base_width_pct": safe_str(item.get("base_width_pct")),
                    "support_touch_count": safe_str(item.get("support_touch_count")),
                    "in_low_position_le60_market_bull": safe_str(item.get("in_low_position_le60_market_bull")),
                    "failure_exit_rule_id": BASELINE_RULE_ID,
                    "entry_price": safe_str(item.get("entry_price")),
                    "exit_date": safe_str(item.get("exit_date")),
                    "exit_price": safe_str(item.get("exit_price")),
                    "holding_days": safe_str(item.get("holding_days")),
                    "return_pct": safe_str(item.get("return_pct")),
                    "max_close_return_pct": safe_str(item.get("max_close_return_pct")),
                    "min_close_return_pct": safe_str(item.get("min_close_return_pct")),
                    "outcome_result": safe_str(item.get("outcome_result")),
                    "exit_reason": safe_str(item.get("exit_reason")),
                    "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
                    **manual,
                    **context,
                    "manual_classifier_alignment": manual_classifier_alignment(
                        manual["manual_label_status"],
                        context["auto_context_filter_result"],
                    ),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )

    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def numeric_return(frame: pd.DataFrame) -> pd.Series:
    return pd.to_numeric(frame["return_pct"], errors="coerce")


def summarize_group(analysis_scope_id: str, window_sessions: str, context: str, filter_result: str, group: pd.DataFrame) -> dict[str, str]:
    returns = numeric_return(group)
    outcomes = group["outcome_result"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    other = len(group) - win - neutral - loss
    pure_denominator = win + loss
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "context_window_grid_scope_id": CONTEXT_WINDOW_GRID_SCOPE_ID,
        "analysis_scope_id": analysis_scope_id,
        "window_sessions_requested": window_sessions,
        "auto_pre_signal_context": context,
        "auto_context_filter_result": filter_result,
        "sample_count": str(len(group)),
        "unique_events": str(group["source_event_key"].nunique()),
        "win_count": str(win),
        "neutral_count": str(neutral),
        "loss_count": str(loss),
        "other_count": str(other),
        "pure_win_rate_pct": pct_text(win, pure_denominator),
        "neutral_inclusive_success_rate_pct": pct_text(win + neutral, len(group)),
        "positive_return_rate_pct": pct_text(int((returns > 0).sum()), int(returns.notna().sum())),
        "avg_return_pct": metric_text(float(returns.mean())) if returns.notna().any() else "",
        "median_return_pct": metric_text(float(returns.median())) if returns.notna().any() else "",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": now_text(),
    }


def build_summary(detail: pd.DataFrame) -> pd.DataFrame:
    scopes = [
        ("all_retest_entries", detail),
        ("low_position_le60_market_bull", detail.loc[detail["in_low_position_le60_market_bull"].eq("true")]),
        ("manual_labeled_non_conflict", detail.loc[detail["manual_label_status"].isin(["manual_good", "manual_bad"])]),
        ("manual_good_non_conflict", detail.loc[detail["manual_label_status"].eq("manual_good")]),
        ("manual_bad_non_conflict", detail.loc[detail["manual_label_status"].eq("manual_bad")]),
    ]
    rows: list[dict[str, str]] = []
    for analysis_scope_id, scope in scopes:
        if scope.empty:
            continue
        for (window_sessions, context, filter_result), group in scope.groupby(
            ["window_sessions_requested", "auto_pre_signal_context", "auto_context_filter_result"],
            dropna=False,
        ):
            rows.append(summarize_group(analysis_scope_id, str(window_sessions), str(context), str(filter_result), group))
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def manual_alignment_group(window_sessions: str, alignment_scope_id: str, alignment: str, group: pd.DataFrame) -> dict[str, str]:
    returns = numeric_return(group)
    good = int(group["manual_label_status"].eq("manual_good").sum())
    bad = int(group["manual_label_status"].eq("manual_bad").sum())
    conflict = int(group["manual_label_status"].eq("manual_conflict").sum())
    good_false_negative = int(group["manual_classifier_alignment"].eq("manual_good_auto_bearish_false_negative").sum())
    bad_false_positive = int(group["manual_classifier_alignment"].eq("manual_bad_auto_non_bearish_false_positive").sum())
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "context_window_grid_scope_id": CONTEXT_WINDOW_GRID_SCOPE_ID,
        "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
        "window_sessions_requested": window_sessions,
        "alignment_scope_id": alignment_scope_id,
        "manual_classifier_alignment": alignment,
        "label_rows": str(len(group)),
        "unique_events": str(group["source_event_key"].nunique()),
        "manual_good_rows": str(good),
        "manual_bad_rows": str(bad),
        "manual_conflict_rows": str(conflict),
        "manual_good_false_negative_rows": str(good_false_negative),
        "manual_bad_false_positive_rows": str(bad_false_positive),
        "manual_good_false_negative_rate_pct": pct_text(good_false_negative, good),
        "manual_bad_false_positive_rate_pct": pct_text(bad_false_positive, bad),
        "avg_return_pct": metric_text(float(returns.mean())) if returns.notna().any() else "",
        "median_return_pct": metric_text(float(returns.median())) if returns.notna().any() else "",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": now_text(),
    }


def build_manual_alignment(detail: pd.DataFrame) -> pd.DataFrame:
    manual = detail.loc[detail["manual_label_status"].ne("unlabeled")].copy()
    rows: list[dict[str, str]] = []
    for window_sessions, window_group in manual.groupby("window_sessions_requested", dropna=False):
        rows.append(manual_alignment_group(str(window_sessions), "window_total", "all_manual_labels", window_group))
        non_conflict = window_group.loc[window_group["manual_label_status"].isin(["manual_good", "manual_bad"])]
        if not non_conflict.empty:
            rows.append(manual_alignment_group(str(window_sessions), "window_non_conflict_total", "manual_non_conflict_total", non_conflict))
            for alignment, group in non_conflict.groupby("manual_classifier_alignment", dropna=False):
                rows.append(manual_alignment_group(str(window_sessions), "window_non_conflict_by_alignment", str(alignment), group))
        conflict = window_group.loc[window_group["manual_label_status"].eq("manual_conflict")]
        if not conflict.empty:
            rows.append(manual_alignment_group(str(window_sessions), "window_conflict_total", "manual_label_conflict_not_scored", conflict))
    return pd.DataFrame(rows, columns=MANUAL_ALIGNMENT_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, manual_alignment: pd.DataFrame) -> None:
    lines = [
        "# Structured-Neckline Context Window Grid Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- context_window_grid_scope_id: `{CONTEXT_WINDOW_GRID_SCOPE_ID}`",
        f"- windows: `{';'.join(str(item) for item in WINDOWS)}`",
        f"- detail_rows: `{len(detail)}`",
        f"- source_events: `{detail['source_event_key'].nunique() if not detail.empty else 0}`",
        "- approved_for_daily: `false`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "",
        "## Manual Alignment",
        "",
    ]
    totals = manual_alignment.loc[manual_alignment["alignment_scope_id"].eq("window_non_conflict_total")]
    if totals.empty:
        lines.append("- no non-conflict manual labels")
    else:
        for _, row in totals.sort_values("window_sessions_requested").iterrows():
            lines.append(
                "- "
                f"window `{row['window_sessions_requested']}`: "
                f"good_false_negative=`{row['manual_good_false_negative_rows']}` / good=`{row['manual_good_rows']}`, "
                f"bad_false_positive=`{row['manual_bad_false_positive_rows']}` / bad=`{row['manual_bad_rows']}`, "
                f"avg_return_pct=`{row['avg_return_pct']}`"
            )

    lines.extend(["", "## Low-Position Bull Context Summary", ""])
    low_position = summary.loc[
        summary["analysis_scope_id"].eq("low_position_le60_market_bull")
        & summary["auto_context_filter_result"].eq("auto_non_bearish")
    ]
    if low_position.empty:
        lines.append("- no low-position bull non-bearish rows")
    else:
        for _, row in low_position.sort_values(["window_sessions_requested", "auto_pre_signal_context"]).iterrows():
            lines.append(
                "- "
                f"window `{row['window_sessions_requested']}` / `{row['auto_pre_signal_context']}`: "
                f"sample=`{row['sample_count']}`, success=`{row['neutral_inclusive_success_rate_pct']}`, "
                f"avg_return_pct=`{row['avg_return_pct']}`"
            )

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This grid changes only the research pre-signal context observation window.",
            "- It uses the same classifier thresholds as the previous auto context audit to isolate window-length effects.",
            "- It is not a production filter, score, rank, or model condition.",
            "- It does not write research variants back to production baseline.",
        ]
    )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    detail = build_detail()
    summary = build_summary(detail)
    manual_alignment = build_manual_alignment(detail)
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    detail.to_csv(LATEST_DETAIL_CSV, index=False, encoding="utf-8")
    summary.to_csv(LATEST_SUMMARY_CSV, index=False, encoding="utf-8")
    manual_alignment.to_csv(LATEST_MANUAL_ALIGNMENT_CSV, index=False, encoding="utf-8")
    detail.to_csv(HISTORY_DETAIL_CSV, index=False, encoding="utf-8")
    summary.to_csv(HISTORY_SUMMARY_CSV, index=False, encoding="utf-8")
    manual_alignment.to_csv(HISTORY_MANUAL_ALIGNMENT_CSV, index=False, encoding="utf-8")
    write_markdown(detail, summary, manual_alignment)
    print(
        "structured neckline context window grid audit built "
        f"detail_rows={len(detail)} summary_rows={len(summary)} manual_alignment_rows={len(manual_alignment)}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV}")
    print(f"latest_summary={LATEST_SUMMARY_CSV}")
    print(f"latest_manual_alignment={LATEST_MANUAL_ALIGNMENT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
