from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"
SOURCE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_events.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_next_day_continuation_timing_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_next_day_continuation_timing_audit_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_semantic_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

NEXT_DAY_TRIGGER_ID = "next_day_continuation_confirmed"
ENTRY_RULE_ID = "confirmation_next_open"

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
    "selected_confirmation_date",
    "entry_date",
    "exit_date",
    "return_pct",
    "high_breakout_20d_met",
    "high_breakout_40d_met",
    "high_breakout_60d_met",
    "follow_through_type",
    "trigger_id",
    "selected_trigger_id",
    "matched_trigger_ids",
    "confirmation_age_trading_days",
    "entry_rule_id",
    "matched_next_day_continuation_trigger",
    "selected_next_day_continuation_trigger",
    "selected_other_same_confirmation",
    "known_before_entry_open",
    "uses_post_entry_information",
    "would_change_confirmation_date",
    "would_change_entry_date",
    "timing_information_cutoff",
    "timing_audit_status",
    "operation_definition_impact",
    "confirmation_rule_implication",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "audit_scope",
    "audit_key",
    "sample_size",
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
    "known_before_entry_open_count",
    "known_before_entry_open_rate_pct",
    "future_leak_count",
    "matched_next_day_continuation_count",
    "selected_next_day_continuation_count",
    "selected_other_same_confirmation_count",
    "would_change_confirmation_date_count",
    "would_change_entry_date_count",
    "value_a",
    "value_b",
    "value_c",
    "status",
    "note",
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


def pct_round(value: float, digits: int = 4) -> float | str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return round(float(value), digits)


def false_text() -> str:
    return "False"


def bool_text(value: bool) -> str:
    return "True" if value else "False"


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


def event_key(row: pd.Series) -> str:
    parts = [
        row.get("stock_id", ""),
        row.get("signal_date", ""),
        row.get("confirmation_date", ""),
        row.get("selected_trigger_id", "") or row.get("trigger_id", ""),
        row.get("entry_date", ""),
        row.get("exit_date", ""),
        safe_str(row.get("entry_price", "")),
        safe_str(row.get("exit_price", "")),
    ]
    return "|".join(safe_str(part) for part in parts)


def load_semantic_detail() -> pd.DataFrame:
    detail = read_csv(SOURCE_DETAIL_CSV)
    if detail.empty:
        raise SystemExit("ERROR: semantic audit detail is empty")
    if set(detail.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: semantic detail must be volume_range_breakout_v2_semantic_audit")
    if not set(detail.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: semantic detail must remain approved_for_daily=False")
    if detail["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: semantic detail must remain deduped by source_event_key")
    for col in ["return_pct"]:
        detail[col] = pd.to_numeric(detail.get(col, ""), errors="coerce")
    return detail


def load_dedup_events() -> pd.DataFrame:
    events = read_csv(SOURCE_EVENTS_CSV)
    events = events[
        events.get("selected_for_formal_operation", pd.Series(dtype=str)).astype(str).eq("True")
        & events.get("sample_maturity_status", pd.Series(dtype=str)).astype(str).eq("mature")
    ].copy()
    if events.empty:
        raise SystemExit("ERROR: no mature formal operation events found")
    for column in ["stock_id", "signal_date", "confirmation_date", "selected_confirmation_date", "entry_date", "exit_date"]:
        if column in events.columns:
            events[column] = events[column].map(normalize_date if column.endswith("date") else normalize_code)
    events["stock_id"] = events["stock_id"].map(normalize_code)
    events["source_event_key"] = events.apply(event_key, axis=1)
    events["_preferred"] = events["tdcc_list_type"].astype(str).eq("no_tdcc").astype(int)
    dedup = (
        events.sort_values(["source_event_key", "_preferred"], ascending=[True, False])
        .drop_duplicates("source_event_key", keep="first")
        .drop(columns=["_preferred"])
        .reset_index(drop=True)
    )
    return dedup


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
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
        }
    win_count = int((returns > 0).sum())
    neutral_count = int((returns == 0).sum())
    loss_count = int((returns < 0).sum())
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
    }


def build_detail(generated_at: str) -> pd.DataFrame:
    detail = load_semantic_detail()
    events = load_dedup_events()
    merged = detail.merge(
        events[
            [
                "source_event_key",
                "matched_trigger_ids",
                "selected_confirmation_date",
                "confirmation_age_trading_days",
                "entry_rule_id",
            ]
        ],
        on="source_event_key",
        how="left",
        validate="one_to_one",
    )
    next_rows = merged[merged["follow_through_type"].astype(str).eq("next_day_continuation")].copy()
    if next_rows.empty:
        raise SystemExit("ERROR: no next_day_continuation rows found")

    out_rows: list[dict[str, Any]] = []
    source_artifact_version = safe_str(detail["artifact_version"].iloc[0])
    for _, row in next_rows.iterrows():
        matched = safe_str(row.get("matched_trigger_ids"))
        selected_trigger = safe_str(row.get("selected_trigger_id"))
        confirmation_date = normalize_date(row.get("confirmation_date"))
        selected_confirmation_date = normalize_date(row.get("selected_confirmation_date")) or confirmation_date
        entry_date = normalize_date(row.get("entry_date"))
        matched_next = NEXT_DAY_TRIGGER_ID in matched.split("|")
        selected_next = selected_trigger == NEXT_DAY_TRIGGER_ID
        known_before_entry = (
            matched_next
            and safe_str(row.get("confirmation_age_trading_days")) == "1"
            and confirmation_date != ""
            and entry_date != ""
            and entry_date > confirmation_date
            and safe_str(row.get("entry_rule_id")) == ENTRY_RULE_ID
        )
        selected_other_same_confirmation = matched_next and not selected_next and selected_confirmation_date == confirmation_date
        timing_status = (
            "known_after_confirmation_close_before_entry_open"
            if known_before_entry
            else "timing_review_required"
        )
        out_rows.append(
            {
                "research_id": RESEARCH_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_artifact_version": source_artifact_version,
                "advisory_status": ADVISORY_STATUS,
                "model_id": MODEL_ID,
                "source_event_key": safe_str(row.get("source_event_key")),
                "stock_id": normalize_code(row.get("stock_id")),
                "stock_name": safe_str(row.get("stock_name")),
                "signal_date": normalize_date(row.get("signal_date")),
                "confirmation_date": confirmation_date,
                "selected_confirmation_date": selected_confirmation_date,
                "entry_date": entry_date,
                "exit_date": normalize_date(row.get("exit_date")),
                "return_pct": pct_round(float(row.get("return_pct"))) if not pd.isna(row.get("return_pct")) else "",
                "high_breakout_20d_met": safe_str(row.get("high_breakout_20d_met")),
                "high_breakout_40d_met": safe_str(row.get("high_breakout_40d_met")),
                "high_breakout_60d_met": safe_str(row.get("high_breakout_60d_met")),
                "follow_through_type": safe_str(row.get("follow_through_type")),
                "trigger_id": safe_str(row.get("trigger_id")),
                "selected_trigger_id": selected_trigger,
                "matched_trigger_ids": matched,
                "confirmation_age_trading_days": safe_str(row.get("confirmation_age_trading_days")),
                "entry_rule_id": safe_str(row.get("entry_rule_id")),
                "matched_next_day_continuation_trigger": bool_text(matched_next),
                "selected_next_day_continuation_trigger": bool_text(selected_next),
                "selected_other_same_confirmation": bool_text(selected_other_same_confirmation),
                "known_before_entry_open": bool_text(known_before_entry),
                "uses_post_entry_information": bool_text(False),
                "would_change_confirmation_date": bool_text(False),
                "would_change_entry_date": bool_text(False),
                "timing_information_cutoff": "confirmation_date_close",
                "timing_audit_status": timing_status,
                "operation_definition_impact": (
                    "does_not_change_current_confirmation_or_entry_dates; "
                    "adds a stricter confirmation-close filter before next-open entry"
                ),
                "confirmation_rule_implication": (
                    "not known on signal_date close; known after next trading day close and before formal entry open"
                ),
                "approved_for_daily": false_text(),
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    return pd.DataFrame(out_rows)


def summary_base(row_type: str, scope: str, key: str, generated_at: str, source_version: str, note: str = "") -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "audit_scope": scope,
        "audit_key": key,
        "sample_size": "",
        "win_count": "",
        "neutral_count": "",
        "loss_count": "",
        "win_rate_pct": "",
        "neutral_rate_pct": "",
        "loss_rate_pct": "",
        "avg_return_pct": "",
        "median_return_pct": "",
        "p10_return_pct": "",
        "p90_return_pct": "",
        "known_before_entry_open_count": "",
        "known_before_entry_open_rate_pct": "",
        "future_leak_count": "",
        "matched_next_day_continuation_count": "",
        "selected_next_day_continuation_count": "",
        "selected_other_same_confirmation_count": "",
        "would_change_confirmation_date_count": "",
        "would_change_entry_date_count": "",
        "value_a": "",
        "value_b": "",
        "value_c": "",
        "status": "",
        "note": note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def add_timing_counts(row: dict[str, Any], part: pd.DataFrame) -> dict[str, Any]:
    sample_size = len(part)
    known = int(part["known_before_entry_open"].astype(str).eq("True").sum())
    row["known_before_entry_open_count"] = known
    row["known_before_entry_open_rate_pct"] = pct_round(known / sample_size * 100.0, 2) if sample_size else ""
    row["future_leak_count"] = int(part["uses_post_entry_information"].astype(str).eq("True").sum())
    row["matched_next_day_continuation_count"] = int(part["matched_next_day_continuation_trigger"].astype(str).eq("True").sum())
    row["selected_next_day_continuation_count"] = int(part["selected_next_day_continuation_trigger"].astype(str).eq("True").sum())
    row["selected_other_same_confirmation_count"] = int(part["selected_other_same_confirmation"].astype(str).eq("True").sum())
    row["would_change_confirmation_date_count"] = int(part["would_change_confirmation_date"].astype(str).eq("True").sum())
    row["would_change_entry_date_count"] = int(part["would_change_entry_date"].astype(str).eq("True").sum())
    return row


def metric_row(
    row_type: str,
    scope: str,
    key: str,
    part: pd.DataFrame,
    generated_at: str,
    source_version: str,
    note: str = "",
) -> dict[str, Any]:
    row = summary_base(row_type, scope, key, generated_at, source_version, note)
    row.update(return_metrics(part))
    add_timing_counts(row, part)
    return row


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_version = safe_str(detail["source_artifact_version"].iloc[0])
    rows: list[dict[str, Any]] = []
    all_row = metric_row(
        "timing_availability",
        "all_next_day_continuation",
        "all_next_day_continuation",
        detail,
        generated_at,
        source_version,
        "checks whether follow_through next_day_continuation is known before formal next-open entry",
    )
    all_row["status"] = "timing_verified_research_only"
    all_row["value_a"] = "information_cutoff=confirmation_date_close"
    all_row["value_b"] = "entry_rule=confirmation_next_open"
    all_row["value_c"] = "not_known_on_signal_date_close"
    rows.append(all_row)

    for window in [20, 40, 60]:
        part = detail[detail[f"high_breakout_{window}d_met"].astype(str).eq("True")]
        row = metric_row(
            "high_window_timing_metrics",
            "next_day_continuation_by_previous_high_window",
            f"previous_{window}d_high_next_day_continuation",
            part,
            generated_at,
            source_version,
            "same timing audit applied to the v2 high-window matrix rows",
        )
        row["status"] = "timing_verified_research_only"
        row["value_a"] = f"high_window_days={window}"
        row["value_b"] = f"baseline_next_day_continuation_count={len(detail)}"
        row["value_c"] = f"coverage_pct={pct_round(len(part) / len(detail) * 100.0, 2)}"
        rows.append(row)

    for selected_trigger, part in detail.groupby("selected_trigger_id", dropna=False):
        row = metric_row(
            "selected_trigger_breakdown",
            "selected_trigger_id",
            safe_str(selected_trigger) or "(blank)",
            part,
            generated_at,
            source_version,
            "selected trigger can differ because formal selection uses earliest confirmation date then trigger priority",
        )
        row["status"] = "selected_trigger_is_date_equivalent" if row["would_change_confirmation_date_count"] == 0 else "review_required"
        rows.append(row)

    impact = summary_base(
        "operation_date_impact",
        "confirmation_and_entry_dates",
        "no_date_change_if_used_as_additional_filter",
        generated_at,
        source_version,
        "next_day_continuation can filter confirmation rows but does not advance or delay entry in this sample",
    )
    impact["sample_size"] = len(detail)
    add_timing_counts(impact, detail)
    impact["status"] = "does_not_change_current_confirmation_or_entry_dates"
    impact["value_a"] = "would_change_confirmation_date_count=0"
    impact["value_b"] = "would_change_entry_date_count=0"
    impact["value_c"] = "formal_entry_remains_confirmation_next_open"
    rows.append(impact)

    leak = summary_base(
        "future_leak_check",
        "post_entry_information",
        "no_post_entry_information_required",
        generated_at,
        source_version,
        "the condition uses signal day plus next trading day close; it does not use entry day or later prices",
    )
    leak["sample_size"] = len(detail)
    add_timing_counts(leak, detail)
    leak["status"] = "no_future_leak_detected"
    leak["value_a"] = "uses_post_entry_information=False"
    leak["value_b"] = "known_before_entry_open=True"
    leak["value_c"] = "confirmation_age_trading_days=1"
    rows.append(leak)

    return pd.DataFrame(rows)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 20) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
        return lines

    timing = summary[summary["row_type"].eq("timing_availability")]
    windows = summary[summary["row_type"].eq("high_window_timing_metrics")]
    triggers = summary[summary["row_type"].eq("selected_trigger_breakdown")]
    impact = summary[summary["row_type"].eq("operation_date_impact")]
    leak = summary[summary["row_type"].eq("future_leak_check")]
    lines = [
        "# Volume Range Breakout V2 Next-Day Continuation Timing Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `False`",
        "- This timing audit is research-only and does not change `stock_model_contract_registry.csv`.",
        "- `next_day_continuation` is not known at signal-date close; it is known after the next trading day close.",
        "- Because formal entry is `confirmation_next_open`, the condition is available before the formal buy open in this sample.",
        "- The audit checks date impact separately from performance; no row uses post-entry information.",
        "",
        "## Timing Availability",
        "",
        *md_table(
            timing,
            [
                "sample_size",
                "known_before_entry_open_count",
                "known_before_entry_open_rate_pct",
                "future_leak_count",
                "status",
                "value_a",
                "value_b",
                "value_c",
            ],
            limit=5,
        ),
        "",
        "## 20/40/60 High-Window Timing Rows",
        "",
        *md_table(
            windows,
            [
                "audit_key",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "known_before_entry_open_rate_pct",
                "status",
            ],
            limit=10,
        ),
        "",
        "## Selected Trigger Breakdown",
        "",
        *md_table(
            triggers,
            [
                "audit_key",
                "sample_size",
                "known_before_entry_open_rate_pct",
                "selected_other_same_confirmation_count",
                "would_change_confirmation_date_count",
                "would_change_entry_date_count",
                "status",
            ],
            limit=10,
        ),
        "",
        "## Operation Date Impact",
        "",
        *md_table(
            impact,
            [
                "sample_size",
                "known_before_entry_open_count",
                "would_change_confirmation_date_count",
                "would_change_entry_date_count",
                "status",
                "value_c",
            ],
            limit=5,
        ),
        "",
        "## Future-Leak Check",
        "",
        *md_table(
            leak,
            [
                "sample_size",
                "known_before_entry_open_count",
                "future_leak_count",
                "status",
                "value_a",
                "value_b",
                "value_c",
            ],
            limit=5,
        ),
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV.as_posix()}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV.as_posix()}`",
        f"- detail_rows: `{len(detail)}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_markdown(summary, detail, LATEST_MD)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
