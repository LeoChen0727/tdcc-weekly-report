from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from build_structured_neckline_auto_context_expansion_audit import (
    BASELINE_RULE_ID,
    LATEST_DETAIL_CSV as AUTO_CONTEXT_DETAIL_CSV,
    PARAMETER_SET_ID as AUTO_CONTEXT_PARAMETER_SET_ID,
    RESEARCH_ID as AUTO_CONTEXT_RESEARCH_ID,
)
from build_structured_neckline_manual_chart_label_audit import (
    LATEST_DETAIL_CSV as MANUAL_LABEL_DETAIL_CSV,
    MANUAL_LABEL_SCOPE_ID,
    PARAMETER_SET_ID as MANUAL_LABEL_PARAMETER_SET_ID,
    RESEARCH_ID as MANUAL_LABEL_RESEARCH_ID,
)


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_manual_label_context_classifier_audit"
PARAMETER_SET_ID = "structured_neckline_manual_label_context_classifier_audit_20260629"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
CLASSIFIER_AUDIT_SCOPE_ID = "manual_good_bad_vs_auto_pre_signal_context"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_manual_label_context_classifier_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_manual_label_context_classifier_audit_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_manual_label_context_classifier_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_manual_label_context_classifier_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_manual_label_context_classifier_audit_summary.csv"

DETAIL_COLUMNS = [
    "research_id",
    "source_manual_label_research_id",
    "source_manual_label_parameter_set_id",
    "source_auto_context_research_id",
    "source_auto_context_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "manual_label_scope_id",
    "classifier_audit_scope_id",
    "label_source_chart_packet",
    "manual_label",
    "label_conflict_for_event",
    "label_event_key",
    "source_match_status",
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
    "manual_visual_pre_signal_context",
    "auto_pre_signal_context",
    "auto_context_filter_result",
    "auto_context_return_pct",
    "auto_context_range_pct",
    "auto_context_slope_pct_per_20d",
    "auto_context_max_drawdown_pct",
    "manual_return_pct",
    "auto_return_pct",
    "classifier_alignment",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "manual_label_scope_id",
    "classifier_audit_scope_id",
    "summary_scope_id",
    "manual_label",
    "auto_context_filter_result",
    "auto_pre_signal_context",
    "classifier_alignment",
    "label_rows",
    "unique_events",
    "avg_manual_return_pct",
    "median_manual_return_pct",
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


def classifier_alignment(manual_label: str, conflict: str, auto_filter: str) -> str:
    if conflict == "true":
        return "manual_label_conflict_not_scored"
    if manual_label == "good" and auto_filter == "auto_non_bearish":
        return "manual_good_auto_non_bearish_match"
    if manual_label == "good" and auto_filter == "auto_bearish":
        return "manual_good_auto_bearish_false_negative"
    if manual_label == "bad" and auto_filter == "auto_bearish":
        return "manual_bad_auto_bearish_match"
    if manual_label == "bad" and auto_filter == "auto_non_bearish":
        return "manual_bad_auto_non_bearish_false_positive"
    return "unscored_or_unknown"


def build_auto_lookup() -> dict[str, pd.Series]:
    auto = read_csv(AUTO_CONTEXT_DETAIL_CSV)
    auto = auto.loc[
        auto["failure_exit_rule_id"].eq(BASELINE_RULE_ID)
        & auto["source_segment_id"].eq("all_retest_entries")
    ].copy()
    auto["label_event_key"] = auto.apply(event_key, axis=1)
    lookup: dict[str, pd.Series] = {}
    for _, row in auto.iterrows():
        lookup[str(row["label_event_key"])] = row
    return lookup


def build_detail() -> pd.DataFrame:
    generated_at = now_text()
    manual = read_csv(MANUAL_LABEL_DETAIL_CSV)
    auto_lookup = build_auto_lookup()
    rows: list[dict[str, str]] = []
    for _, label_row in manual.iterrows():
        key = str(label_row.get("label_event_key", ""))
        auto_row = auto_lookup.get(key)
        matched = auto_row is not None
        auto_filter = str(auto_row.get("auto_context_filter_result", "")) if matched else ""
        manual_label = str(label_row.get("manual_label", ""))
        conflict = str(label_row.get("label_conflict_for_event", ""))
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "source_manual_label_research_id": MANUAL_LABEL_RESEARCH_ID,
                "source_manual_label_parameter_set_id": MANUAL_LABEL_PARAMETER_SET_ID,
                "source_auto_context_research_id": AUTO_CONTEXT_RESEARCH_ID,
                "source_auto_context_parameter_set_id": AUTO_CONTEXT_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
                "classifier_audit_scope_id": CLASSIFIER_AUDIT_SCOPE_ID,
                "label_source_chart_packet": str(label_row.get("label_source_chart_packet", "")),
                "manual_label": manual_label,
                "label_conflict_for_event": conflict,
                "label_event_key": key,
                "source_match_status": "matched_auto_context" if matched else "missing_auto_context",
                "stock_id": str(label_row.get("stock_id", "")),
                "stock_name": str(label_row.get("stock_name", "")),
                "signal_date": str(label_row.get("signal_date", "")),
                "retest_date": str(label_row.get("retest_date", "")),
                "retest_attack_date": str(label_row.get("retest_attack_date", "")),
                "retest_entry_date": str(label_row.get("retest_entry_date", "")),
                "market_regime": str(auto_row.get("market_regime", "")) if matched else "",
                "low_position_120_pct": str(auto_row.get("low_position_120_pct", "")) if matched else "",
                "base_width_pct": str(auto_row.get("base_width_pct", "")) if matched else "",
                "support_touch_count": str(auto_row.get("support_touch_count", "")) if matched else "",
                "manual_visual_pre_signal_context": str(label_row.get("visual_pre_signal_context", "")),
                "auto_pre_signal_context": str(auto_row.get("auto_pre_signal_context", "")) if matched else "",
                "auto_context_filter_result": auto_filter,
                "auto_context_return_pct": str(auto_row.get("auto_context_return_pct", "")) if matched else "",
                "auto_context_range_pct": str(auto_row.get("auto_context_range_pct", "")) if matched else "",
                "auto_context_slope_pct_per_20d": str(auto_row.get("auto_context_slope_pct_per_20d", "")) if matched else "",
                "auto_context_max_drawdown_pct": str(auto_row.get("auto_context_max_drawdown_pct", "")) if matched else "",
                "manual_return_pct": str(label_row.get("return_pct", "")),
                "auto_return_pct": str(auto_row.get("return_pct", "")) if matched else "",
                "classifier_alignment": classifier_alignment(manual_label, conflict, auto_filter),
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def metric_text(value: float) -> str:
    if pd.isna(value):
        return ""
    return f"{value:.4f}"


def add_group(rows: list[dict[str, str]], generated_at: str, summary_scope_id: str, group: pd.DataFrame) -> None:
    numeric = pd.to_numeric(group["manual_return_pct"], errors="coerce")
    rows.append(
        {
            "research_id": RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
            "classifier_audit_scope_id": CLASSIFIER_AUDIT_SCOPE_ID,
            "summary_scope_id": summary_scope_id,
            "manual_label": str(group["manual_label"].iloc[0]) if "manual_label" in group else "",
            "auto_context_filter_result": str(group["auto_context_filter_result"].iloc[0])
            if "auto_context_filter_result" in group
            else "",
            "auto_pre_signal_context": str(group["auto_pre_signal_context"].iloc[0])
            if "auto_pre_signal_context" in group
            else "",
            "classifier_alignment": str(group["classifier_alignment"].iloc[0])
            if "classifier_alignment" in group
            else "",
            "label_rows": str(len(group)),
            "unique_events": str(group["label_event_key"].nunique()),
            "avg_manual_return_pct": metric_text(numeric.mean()),
            "median_manual_return_pct": metric_text(numeric.median()),
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
    )


def build_summary(detail: pd.DataFrame) -> pd.DataFrame:
    generated_at = now_text()
    if detail.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    rows: list[dict[str, str]] = []
    for _, group in detail.groupby(
        ["manual_label", "auto_context_filter_result", "auto_pre_signal_context"],
        dropna=False,
    ):
        add_group(rows, generated_at, "by_manual_label_and_auto_context", group)
    for _, group in detail.groupby(["classifier_alignment"], dropna=False):
        add_group(rows, generated_at, "by_classifier_alignment", group)
    clean = detail.loc[detail["label_conflict_for_event"].ne("true")]
    if not clean.empty:
        for _, group in clean.groupby(["classifier_alignment"], dropna=False):
            add_group(rows, generated_at, "non_conflict_by_classifier_alignment", group)
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame) -> None:
    lines = [
        "# Structured-Neckline Manual Label Context Classifier Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- classifier_audit_scope_id: `{CLASSIFIER_AUDIT_SCOPE_ID}`",
        f"- label_rows: `{len(detail)}`",
        f"- matched_auto_context_rows: `{detail['source_match_status'].eq('matched_auto_context').sum() if not detail.empty else 0}`",
        f"- conflict_rows: `{detail['label_conflict_for_event'].eq('true').sum() if not detail.empty else 0}`",
        "- approved_for_daily: `false`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "",
        "## Alignment Summary",
        "",
    ]
    if summary.empty:
        lines.append("- no classifier audit rows")
    else:
        alignment = summary.loc[summary["summary_scope_id"].eq("by_classifier_alignment")]
        for _, row in alignment.iterrows():
            lines.append(
                "- "
                f"{row['classifier_alignment']}: rows=`{row['label_rows']}`, "
                f"unique_events=`{row['unique_events']}`, "
                f"avg_manual_return_pct=`{row['avg_manual_return_pct']}`"
            )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This audit compares user chart labels with the research-only auto pre-signal context classifier.",
            "- It is not a production filter, score, rank, or model condition.",
            "- It does not write research variants back to production baseline.",
        ]
    )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    detail = build_detail()
    summary = build_summary(detail)
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    detail.to_csv(LATEST_DETAIL_CSV, index=False, encoding="utf-8")
    summary.to_csv(LATEST_SUMMARY_CSV, index=False, encoding="utf-8")
    detail.to_csv(HISTORY_DETAIL_CSV, index=False, encoding="utf-8")
    summary.to_csv(HISTORY_SUMMARY_CSV, index=False, encoding="utf-8")
    write_markdown(detail, summary)
    print(
        "structured neckline manual label context classifier audit built "
        f"label_rows={len(detail)} summary_rows={len(summary)} "
        f"matched_auto_context_rows={detail['source_match_status'].eq('matched_auto_context').sum() if not detail.empty else 0}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV}")
    print(f"latest_summary={LATEST_SUMMARY_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
