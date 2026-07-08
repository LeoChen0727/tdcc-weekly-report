from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_RAW_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_latest.csv"
SOURCE_RAW_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_detail_latest.csv"
SOURCE_TIMING_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit_detail_latest.csv"
)
SOURCE_SEMANTIC_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"
SOURCE_FORMAL_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_events.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_source_gap_reconciliation_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_source_gap_reconciliation_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_source_gap_reconciliation_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_source_gap_reconciliation.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_source_gap_reconciliation_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_source_gap_reconciliation"
ARTIFACT_VERSION = "volume_range_breakout_v2_source_gap_reconciliation_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_raw_market_rerun"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "advisory_status",
    "model_id",
    "gap_scope",
    "gap_classification",
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
    "return_bucket",
    "selected_trigger_id_current_v1",
    "matched_trigger_ids_current_v1",
    "present_in_raw_rerun",
    "present_in_timing_audit_60d",
    "present_in_semantic_audit",
    "present_in_formal_operation_events",
    "timing_audit_max_signal_date",
    "formal_events_max_signal_date",
    "raw_rerun_max_signal_date",
    "promotion_impact",
    "recommended_owner",
    "source_gap_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "advisory_status",
    "model_id",
    "row_type",
    "audit_scope",
    "audit_key",
    "sample_size",
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
    if text.isdigit() and len(text) < 4:
        return text.zfill(4)
    return text


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


def false_text() -> str:
    return "False"


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


def normalize_event_dates(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "stock_id" in out.columns:
        out["stock_id"] = out["stock_id"].map(normalize_code)
    for column in ["signal_date", "confirmation_date", "selected_confirmation_date", "entry_date", "exit_date"]:
        if column in out.columns:
            out[column] = out[column].map(normalize_date)
    return out


def load_timing_60d() -> pd.DataFrame:
    timing = normalize_event_dates(read_csv(SOURCE_TIMING_DETAIL_CSV))
    timing_60 = timing[
        timing.get("high_breakout_60d_met", pd.Series(dtype=str)).astype(str).eq("True")
        & timing.get("known_before_entry_open", pd.Series(dtype=str)).astype(str).eq("True")
    ].copy()
    if timing_60.empty:
        raise SystemExit("ERROR: timing audit 60d subset is empty")
    return timing_60


def load_formal_events() -> pd.DataFrame:
    events = normalize_event_dates(read_csv(SOURCE_FORMAL_EVENTS_CSV))
    events = events[
        events.get("selected_for_formal_operation", pd.Series(dtype=str)).astype(str).eq("True")
        & events.get("sample_maturity_status", pd.Series(dtype=str)).astype(str).eq("mature")
    ].copy()
    if events.empty:
        raise SystemExit("ERROR: no mature selected formal operation events found")
    events["source_event_key"] = events.apply(event_key, axis=1)
    return events


def summary_base(row_type: str, audit_scope: str, audit_key: str, generated_at: str, note: str = "") -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "audit_scope": audit_scope,
        "audit_key": audit_key,
        "sample_size": 0,
        "value_a": "",
        "value_b": "",
        "value_c": "",
        "status": "",
        "note": note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def detail_base(row: pd.Series, generated_at: str) -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "gap_scope": "",
        "gap_classification": "",
        "source_event_key": row.get("source_event_key", ""),
        "stock_id": normalize_code(row.get("stock_id", "")),
        "stock_name": row.get("stock_name", ""),
        "signal_date": normalize_date(row.get("signal_date", "")),
        "confirmation_date": normalize_date(row.get("confirmation_date", "")),
        "entry_date": normalize_date(row.get("entry_date", "")),
        "exit_date": normalize_date(row.get("exit_date", "")),
        "entry_price": safe_str(row.get("entry_price", "")),
        "exit_price": safe_str(row.get("exit_price", "")),
        "return_pct": safe_str(row.get("return_pct", "")),
        "return_bucket": row.get("return_bucket", ""),
        "selected_trigger_id_current_v1": row.get("selected_trigger_id_current_v1", ""),
        "matched_trigger_ids_current_v1": row.get("matched_trigger_ids_current_v1", ""),
        "present_in_raw_rerun": "True",
        "present_in_timing_audit_60d": "False",
        "present_in_semantic_audit": "False",
        "present_in_formal_operation_events": "False",
        "timing_audit_max_signal_date": "",
        "formal_events_max_signal_date": "",
        "raw_rerun_max_signal_date": "",
        "promotion_impact": "",
        "recommended_owner": "",
        "source_gap_reason": "",
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_detail(generated_at: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    raw_summary = read_csv(SOURCE_RAW_SUMMARY_CSV)
    raw_detail = normalize_event_dates(read_csv(SOURCE_RAW_DETAIL_CSV))
    timing_60 = load_timing_60d()
    semantic = normalize_event_dates(read_csv(SOURCE_SEMANTIC_DETAIL_CSV))
    formal = load_formal_events()

    if raw_detail.empty:
        raise SystemExit("ERROR: raw rerun detail is empty")
    if raw_detail["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: raw rerun detail has duplicate source_event_key values")

    raw_keys = set(raw_detail["source_event_key"].astype(str))
    timing_keys = set(timing_60["source_event_key"].astype(str))
    semantic_keys = set(semantic["source_event_key"].astype(str))
    formal_keys = set(formal["source_event_key"].astype(str))
    raw_minus_timing = raw_keys - timing_keys

    timing_max_signal_date = safe_str(timing_60["signal_date"].astype(str).max())
    formal_max_signal_date = safe_str(formal["signal_date"].astype(str).max())
    raw_max_signal_date = safe_str(raw_detail["signal_date"].astype(str).max())

    raw_minus = raw_detail[raw_detail["source_event_key"].astype(str).isin(raw_minus_timing)].copy()
    raw_minus = raw_minus.sort_values(["signal_date", "stock_id", "source_event_key"])

    rows: list[dict[str, Any]] = []
    for _, source_row in raw_minus.iterrows():
        row = detail_base(source_row, generated_at)
        key = row["source_event_key"]
        signal_date = row["signal_date"]
        row["present_in_timing_audit_60d"] = "True" if key in timing_keys else "False"
        row["present_in_semantic_audit"] = "True" if key in semantic_keys else "False"
        row["present_in_formal_operation_events"] = "True" if key in formal_keys else "False"
        row["timing_audit_max_signal_date"] = timing_max_signal_date
        row["formal_events_max_signal_date"] = formal_max_signal_date
        row["raw_rerun_max_signal_date"] = raw_max_signal_date
        if signal_date > timing_max_signal_date:
            row["gap_scope"] = "after_timing_artifact_window"
            row["gap_classification"] = "freshness_extension_after_timing_window"
            row["promotion_impact"] = "requires_research_artifact_refresh_before_promotion"
            row["recommended_owner"] = "research_backtest_source_refresh"
            row["source_gap_reason"] = (
                "raw price-history rerun includes a newer signal date than the current timing/semantic/formal artifacts"
            )
        else:
            row["gap_scope"] = "inside_timing_artifact_window"
            row["gap_classification"] = "source_gap_inside_timing_window_promotion_blocker"
            row["promotion_impact"] = "promotion_blocked_pending_research_source_sync"
            row["recommended_owner"] = "research_backtest_source_reconciliation"
            row["source_gap_reason"] = (
                "raw price-history rerun reconstructed an event absent from timing, semantic, and formal operation artifacts"
            )
        rows.append(row)

    context = {
        "raw_summary": raw_summary,
        "raw_detail_count": len(raw_detail),
        "timing_60_count": len(timing_60),
        "semantic_count": len(semantic),
        "formal_count": len(formal),
        "raw_minus_timing_count": len(raw_minus_timing),
        "timing_minus_raw_count": len(timing_keys - raw_keys),
        "timing_max_signal_date": timing_max_signal_date,
        "formal_max_signal_date": formal_max_signal_date,
        "raw_max_signal_date": raw_max_signal_date,
    }
    return pd.DataFrame(rows), context


def build_summary(detail: pd.DataFrame, context: dict[str, Any], generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    source_row = summary_base(
        "source_profile",
        "raw_market_rerun",
        "source_counts",
        generated_at,
        "source counts used by the reconciliation artifact",
    )
    source_row["sample_size"] = context["raw_detail_count"]
    source_row["value_a"] = f"raw_detail_count={context['raw_detail_count']};timing_60d_count={context['timing_60_count']}"
    source_row["value_b"] = f"semantic_detail_count={context['semantic_count']};formal_event_count={context['formal_count']}"
    source_row["value_c"] = (
        f"raw_max_signal_date={context['raw_max_signal_date']};"
        f"timing_max_signal_date={context['timing_max_signal_date']};"
        f"formal_max_signal_date={context['formal_max_signal_date']}"
    )
    source_row["status"] = "research_only_source_profile"
    rows.append(source_row)

    membership_row = summary_base(
        "membership_check",
        "raw_vs_timing_audit_60d",
        "raw_minus_timing_count",
        generated_at,
        "raw rerun rows absent from the current timing-audit 60d subset",
    )
    membership_row["sample_size"] = context["raw_minus_timing_count"]
    membership_row["value_a"] = f"raw_minus_timing_count={context['raw_minus_timing_count']}"
    membership_row["value_b"] = f"timing_minus_raw_count={context['timing_minus_raw_count']}"
    membership_row["value_c"] = f"timing_audit_max_signal_date={context['timing_max_signal_date']}"
    membership_row["status"] = "source_gap_plus_freshness_extension" if not detail.empty else "match"
    rows.append(membership_row)

    for classification in [
        "freshness_extension_after_timing_window",
        "source_gap_inside_timing_window_promotion_blocker",
    ]:
        subset = detail[detail["gap_classification"].astype(str).eq(classification)]
        row = summary_base(
            "gap_classification",
            "raw_minus_timing",
            classification,
            generated_at,
            "classification of raw-minus-timing rows",
        )
        row["sample_size"] = len(subset)
        row["value_a"] = ";".join(subset["source_event_key"].astype(str).head(10).tolist())
        row["value_b"] = f"timing_audit_max_signal_date={context['timing_max_signal_date']}"
        row["value_c"] = f"formal_events_max_signal_date={context['formal_max_signal_date']}"
        if classification == "source_gap_inside_timing_window_promotion_blocker":
            row["status"] = "promotion_blocked_pending_research_source_sync" if len(subset) > 0 else "not_present"
        else:
            row["status"] = "requires_research_artifact_refresh_before_promotion" if len(subset) > 0 else "not_present"
        rows.append(row)

    blocker = detail[detail["gap_classification"].astype(str).eq("source_gap_inside_timing_window_promotion_blocker")]
    blocker_row = summary_base(
        "promotion_gate",
        "promotion_readiness",
        "source_gap_blocker",
        generated_at,
        "v2 candidate remains research-only until raw/formal/timing sources are synchronized",
    )
    blocker_row["sample_size"] = len(blocker)
    blocker_row["value_a"] = f"inside_timing_window_gap_count={len(blocker)}"
    blocker_row["value_b"] = "expected_action=research_backtest_source_sync_or_exclusion_rule"
    blocker_row["value_c"] = "production_registry_changed=False"
    blocker_row["status"] = (
        "promotion_blocked_pending_research_source_sync" if len(blocker) > 0 else "research_source_membership_clean"
    )
    rows.append(blocker_row)

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

    profile = summary[summary["row_type"].eq("source_profile")]
    gap_rows = summary[summary["row_type"].eq("gap_classification")]
    blocker = summary[summary["row_type"].eq("promotion_gate")]
    lines = [
        "# Volume Range Breakout V2 Source-Gap Reconciliation",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `False`",
        "- This is a research-only source reconciliation artifact and does not change `stock_model_contract_registry.csv`.",
        "- It compares raw price-history v2 rerun rows against timing-audit 60d rows, semantic-audit rows, and formal operation events.",
        "- Rows after the timing artifact max signal date are classified as freshness extension, not promotion evidence.",
        "- Rows inside the timing artifact date window that exist only in the raw rerun are a source-gap blocker before promotion.",
        "",
        "## Source Profile",
        "",
        *md_table(profile, ["sample_size", "value_a", "value_b", "value_c", "status"], limit=5),
        "",
        "## Gap Classification",
        "",
        *md_table(gap_rows, ["audit_key", "sample_size", "status", "value_a"], limit=10),
        "",
        "## Promotion Gate",
        "",
        *md_table(blocker, ["sample_size", "status", "value_a", "value_b", "value_c"], limit=5),
        "",
        "## Gap Detail",
        "",
        *md_table(
            detail,
            [
                "stock_id",
                "signal_date",
                "confirmation_date",
                "entry_date",
                "return_pct",
                "gap_scope",
                "gap_classification",
                "present_in_semantic_audit",
                "present_in_formal_operation_events",
            ],
            limit=20,
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
    detail, context = build_detail(generated_at)
    summary = build_summary(detail, context, generated_at)
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
