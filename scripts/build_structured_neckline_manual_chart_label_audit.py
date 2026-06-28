from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from build_structured_neckline_selected_exit_loss_diagnostics import load_stock_name_lookup


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_manual_chart_label_audit"
PARAMETER_SET_ID = "structured_neckline_manual_chart_label_audit_20260629"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MANUAL_LABEL_SCOPE_ID = "user_good_bad_chart_folder_labels"

EVIDENCE_INDEX_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_evidence_shortlist_latest.csv"
REVIEW_INDEX_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_review_shortlist_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_manual_chart_label_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_manual_chart_label_audit_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_manual_chart_label_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_manual_chart_label_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_manual_chart_label_audit_summary.csv"

LABEL_SOURCES = [
    {
        "label_source_chart_packet": "evidence_shortlist",
        "chart_root": RESEARCH_LATEST_DIR / "structured_neckline_retest_evidence_shortlist",
        "index_csv": EVIDENCE_INDEX_CSV,
        "path_column": "evidence_chart_path",
        "source_research_id": "structured_neckline_retest_evidence_shortlist",
    },
    {
        "label_source_chart_packet": "review_shortlist",
        "chart_root": RESEARCH_LATEST_DIR / "structured_neckline_retest_shortlist",
        "index_csv": REVIEW_INDEX_CSV,
        "path_column": "shortlist_chart_path",
        "source_research_id": "structured_neckline_retest_review_shortlist",
    },
]

DETAIL_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "manual_label_scope_id",
    "label_source_chart_packet",
    "manual_label",
    "label_event_key",
    "label_conflict_for_event",
    "source_match_status",
    "manual_label_chart_path",
    "manual_label_chart_path_absolute",
    "source_chart_path",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "exit_date",
    "outcome_result",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "visual_pre_signal_context",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
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
    "summary_scope_id",
    "label_source_chart_packet",
    "manual_label",
    "label_rows",
    "unique_events",
    "conflicting_event_rows",
    "avg_return_pct",
    "median_return_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def file_stem_key(path: Path) -> str:
    return path.name.rsplit(".", 1)[0]


def parse_filename(path: Path) -> dict[str, str]:
    stem = file_stem_key(path)
    parts = stem.split("_")
    if len(parts) < 5:
        return {
            "signal_date": "",
            "stock_id": "",
            "retest_entry_date": "",
            "outcome_result": "",
            "return_pct": "",
        }
    return {
        "signal_date": parts[0],
        "stock_id": parts[1],
        "retest_entry_date": parts[2],
        "outcome_result": parts[3],
        "return_pct": parts[4],
    }


def event_key_from_values(stock_id: str, signal_date: str, retest_entry_date: str) -> str:
    return f"{stock_id}|{signal_date}|{retest_entry_date}"


def event_key_from_row(row: pd.Series) -> str:
    return event_key_from_values(
        str(row.get("stock_id", "")),
        str(row.get("signal_date", "")),
        str(row.get("retest_entry_date", "")),
    )


def label_files(chart_root: Path) -> list[tuple[str, Path]]:
    if not chart_root.exists():
        return []
    files: list[tuple[str, Path]] = []
    for path in sorted(chart_root.rglob("*.png")):
        label = path.parent.name.lower()
        if label in {"good", "bad"}:
            files.append((label, path))
    return files


def build_source_lookup(index: pd.DataFrame, path_column: str) -> dict[str, pd.Series]:
    lookup: dict[str, pd.Series] = {}
    for _, row in index.iterrows():
        source_path = Path(str(row.get(path_column, "")))
        if source_path.name:
            lookup[source_path.name] = row
    return lookup


def source_parameter_set(row: pd.Series) -> str:
    return str(row.get("parameter_set_id") or row.get("source_parameter_set_id") or "")


def build_detail() -> pd.DataFrame:
    generated_at = now_text()
    rows: list[dict[str, str]] = []

    for source in LABEL_SOURCES:
        index = read_csv(source["index_csv"])
        lookup = build_source_lookup(index, source["path_column"])
        for manual_label, chart_path in label_files(source["chart_root"]):
            parsed = parse_filename(chart_path)
            source_row = lookup.get(chart_path.name)
            if source_row is None:
                stock_id = parsed["stock_id"]
                signal_date = parsed["signal_date"]
                retest_entry_date = parsed["retest_entry_date"]
                row = {
                    "source_research_id": source["source_research_id"],
                    "source_parameter_set_id": "",
                    "source_match_status": "missing_source_index_match",
                    "source_chart_path": "",
                    "stock_id": stock_id,
                    "stock_name": "",
                    "signal_date": signal_date,
                    "retest_date": "",
                    "retest_attack_date": "",
                    "retest_entry_date": retest_entry_date,
                    "exit_date": "",
                    "outcome_result": parsed["outcome_result"],
                    "return_pct": parsed["return_pct"],
                    "mfe_pct": "",
                    "mae_pct": "",
                    "visual_pre_signal_context": "",
                    "market_regime": "",
                    "low_position_120_pct": "",
                    "base_width_pct": "",
                    "support_touch_count": "",
                }
            else:
                stock_id = str(source_row.get("stock_id", ""))
                signal_date = str(source_row.get("signal_date", ""))
                retest_entry_date = str(source_row.get("retest_entry_date", ""))
                row = {
                    "source_research_id": source["source_research_id"],
                    "source_parameter_set_id": source_parameter_set(source_row),
                    "source_match_status": "matched_source_index",
                    "source_chart_path": str(source_row.get(source["path_column"], "")),
                    "stock_id": stock_id,
                    "stock_name": str(source_row.get("stock_name", "")),
                    "signal_date": signal_date,
                    "retest_date": str(source_row.get("retest_date", "")),
                    "retest_attack_date": str(source_row.get("retest_attack_date", "")),
                    "retest_entry_date": retest_entry_date,
                    "exit_date": str(source_row.get("exit_date", "")),
                    "outcome_result": str(source_row.get("outcome_result", "")),
                    "return_pct": str(source_row.get("return_pct", "")),
                    "mfe_pct": str(source_row.get("mfe_pct", "")),
                    "mae_pct": str(source_row.get("mae_pct", "")),
                    "visual_pre_signal_context": str(source_row.get("visual_pre_signal_context", "")),
                    "market_regime": str(source_row.get("market_regime", "")),
                    "low_position_120_pct": str(source_row.get("low_position_120_pct", "")),
                    "base_width_pct": str(source_row.get("base_width_pct", "")),
                    "support_touch_count": str(source_row.get("support_touch_count", "")),
                }

            event_key = event_key_from_values(stock_id, signal_date, retest_entry_date)
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
                    "label_source_chart_packet": source["label_source_chart_packet"],
                    "manual_label": manual_label,
                    "label_event_key": event_key,
                    "label_conflict_for_event": "false",
                    "manual_label_chart_path": rel(chart_path),
                    "manual_label_chart_path_absolute": str(chart_path),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                    **row,
                }
            )

    detail = pd.DataFrame(rows, columns=DETAIL_COLUMNS)
    if detail.empty:
        return detail

    name_lookup = load_stock_name_lookup(detail["stock_id"].astype(str).tolist())
    detail["stock_name"] = detail.apply(
        lambda row: name_lookup.get(str(row["stock_id"]), str(row["stock_name"])),
        axis=1,
    )

    label_sets = detail.groupby("label_event_key")["manual_label"].agg(lambda values: set(values))
    conflict_keys = {key for key, values in label_sets.items() if len(values) > 1}
    detail["label_conflict_for_event"] = detail["label_event_key"].map(
        lambda key: "true" if key in conflict_keys else "false"
    )
    return detail


def metric_text(value: float) -> str:
    if pd.isna(value):
        return ""
    return f"{value:.4f}"


def build_summary(detail: pd.DataFrame) -> pd.DataFrame:
    generated_at = now_text()
    if detail.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)

    numeric_return = pd.to_numeric(detail["return_pct"], errors="coerce")
    working = detail.copy()
    working["_return_pct_num"] = numeric_return

    rows: list[dict[str, str]] = []
    scopes = [
        ("all_manual_labels", working),
        *[
            (f"packet_{packet}", group)
            for packet, group in working.groupby("label_source_chart_packet", dropna=False)
        ],
    ]
    for summary_scope_id, scope_frame in scopes:
        for (packet, manual_label), group in scope_frame.groupby(
            ["label_source_chart_packet", "manual_label"], dropna=False
        ):
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
                    "summary_scope_id": summary_scope_id,
                    "label_source_chart_packet": str(packet),
                    "manual_label": str(manual_label),
                    "label_rows": str(len(group)),
                    "unique_events": str(group["label_event_key"].nunique()),
                    "conflicting_event_rows": str(group["label_conflict_for_event"].eq("true").sum()),
                    "avg_return_pct": metric_text(group["_return_pct_num"].mean()),
                    "median_return_pct": metric_text(group["_return_pct_num"].median()),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame) -> None:
    lines = [
        "# Structured-Neckline Manual Chart Label Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- manual_label_scope_id: `{MANUAL_LABEL_SCOPE_ID}`",
        f"- label_rows: `{len(detail)}`",
        f"- unique_events: `{detail['label_event_key'].nunique() if not detail.empty else 0}`",
        f"- conflict_rows: `{detail['label_conflict_for_event'].eq('true').sum() if not detail.empty else 0}`",
        "- approved_for_daily: `false`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "",
        "## Summary",
        "",
    ]
    if summary.empty:
        lines.append("- no manual chart labels found")
    else:
        for _, row in summary.iterrows():
            lines.append(
                "- "
                f"{row['summary_scope_id']} / {row['label_source_chart_packet']} / {row['manual_label']}: "
                f"rows=`{row['label_rows']}`, unique_events=`{row['unique_events']}`, "
                f"conflicting_event_rows=`{row['conflicting_event_rows']}`, "
                f"avg_return_pct=`{row['avg_return_pct']}`, median_return_pct=`{row['median_return_pct']}`"
            )

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This audit records user chart-review labels from Good/Bad folders.",
            "- It is research/backtest evidence only.",
            "- It does not change production model conditions, scoring, ranking, PDF logic, or production baselines.",
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
        "structured neckline manual chart label audit built "
        f"label_rows={len(detail)} summary_rows={len(summary)} "
        f"conflict_rows={detail['label_conflict_for_event'].eq('true').sum() if not detail.empty else 0}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV}")
    print(f"latest_summary={LATEST_SUMMARY_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
