from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_volume_breakout_confirmed_operation_backtest import (  # noqa: E402
    build_base_events,
    formal_operation_events,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_FORMAL_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_events.csv"
PRICE_HISTORY_MANIFEST_CSV = ROOT / "output" / "latest" / "stock_price_history_manifest.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_formal_source_sync_impact_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_formal_source_sync_impact_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_formal_source_sync_impact_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_formal_source_sync_impact.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_formal_source_sync_impact_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_formal_source_sync_impact"
ARTIFACT_VERSION = "volume_range_breakout_v2_formal_source_sync_impact_20260708"
SOURCE_RESEARCH_ID = "volume_breakout_formal_operation_events"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

KEY_COLUMNS = [
    "stock_id",
    "signal_date",
    "confirmation_date",
    "selected_trigger_id",
    "entry_date",
    "exit_date",
    "entry_price",
    "exit_price",
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
    "current_formal_rows",
    "existing_formal_rows",
    "current_minus_existing_unique_keys",
    "existing_minus_current_unique_keys",
    "current_minus_existing_rows",
    "inside_existing_window_rows",
    "after_existing_window_rows",
    "inside_existing_window_stocks",
    "existing_max_signal_date",
    "current_max_signal_date",
    "status",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "advisory_status",
    "model_id",
    "diff_side",
    "sync_impact_classification",
    "formal_row_key",
    "source_event_key",
    "overlay_model_id",
    "tdcc_list_type",
    "tdcc_signal_date",
    "tdcc_rank",
    "stock_id",
    "stock_name",
    "market",
    "signal_date",
    "confirmation_date",
    "selected_trigger_id",
    "matched_trigger_ids",
    "entry_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "return_pct",
    "exit_reason",
    "holding_days",
    "classification_id",
    "attack_method",
    "price_position_type",
    "follow_through_type",
    "volume_ratio",
    "signal_return_1d_pct",
    "price_history_rows",
    "price_history_start_date",
    "price_history_end_date",
    "existing_max_signal_date",
    "current_max_signal_date",
    "discussion_reason",
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


def normalize_events(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "stock_id" in out.columns:
        out["stock_id"] = out["stock_id"].map(normalize_code)
    for col in ["signal_date", "confirmation_date", "selected_confirmation_date", "entry_date", "exit_date"]:
        if col in out.columns:
            out[col] = out[col].map(normalize_date)
    return out


def event_key_df(df: pd.DataFrame) -> pd.Series:
    tmp = df.copy()
    for col in KEY_COLUMNS:
        if col not in tmp.columns:
            tmp[col] = ""
        tmp[col] = tmp[col].map(safe_str)
    return tmp[KEY_COLUMNS].agg("|".join, axis=1)


def formal_row_key_df(df: pd.DataFrame) -> pd.Series:
    overlay_cols = ["source_event_key", "overlay_model_id", "tdcc_list_type", "tdcc_signal_date", "tdcc_rank"]
    tmp = df.copy()
    for col in overlay_cols:
        if col not in tmp.columns:
            tmp[col] = ""
        tmp[col] = tmp[col].map(safe_str)
    return tmp[overlay_cols].agg("|".join, axis=1)


def load_manifest() -> pd.DataFrame:
    manifest = read_csv(PRICE_HISTORY_MANIFEST_CSV)
    if "stock_id" in manifest.columns:
        manifest["stock_id"] = manifest["stock_id"].map(normalize_code)
    return manifest


def attach_manifest(detail: pd.DataFrame, manifest: pd.DataFrame) -> pd.DataFrame:
    cols = ["stock_id", "rows", "start_date", "end_date"]
    if manifest.empty or not set(cols).issubset(manifest.columns):
        detail["price_history_rows"] = ""
        detail["price_history_start_date"] = ""
        detail["price_history_end_date"] = ""
        return detail
    lookup = manifest[cols].drop_duplicates("stock_id").rename(
        columns={
            "rows": "price_history_rows",
            "start_date": "price_history_start_date",
            "end_date": "price_history_end_date",
        }
    )
    return detail.merge(lookup, on="stock_id", how="left")


def build_current_formal_events() -> pd.DataFrame:
    current = formal_operation_events(build_base_events())
    return normalize_events(current)


def build_existing_formal_events() -> pd.DataFrame:
    existing = normalize_events(read_csv(SOURCE_FORMAL_EVENTS_CSV))
    if existing.empty:
        raise SystemExit("ERROR: existing formal operation events artifact is empty")
    return existing


def summary_row(
    row_type: str,
    audit_scope: str,
    audit_key: str,
    generated_at: str,
    note: str = "",
) -> dict[str, Any]:
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
        "current_formal_rows": "",
        "existing_formal_rows": "",
        "current_minus_existing_unique_keys": "",
        "existing_minus_current_unique_keys": "",
        "current_minus_existing_rows": "",
        "inside_existing_window_rows": "",
        "after_existing_window_rows": "",
        "inside_existing_window_stocks": "",
        "existing_max_signal_date": "",
        "current_max_signal_date": "",
        "status": "",
        "note": note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_detail(current: pd.DataFrame, existing: pd.DataFrame, generated_at: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    current = current.copy()
    existing = existing.copy()
    current["source_event_key"] = event_key_df(current)
    existing["source_event_key"] = event_key_df(existing)
    current_keys = set(current["source_event_key"].astype(str))
    existing_keys = set(existing["source_event_key"].astype(str))
    current_minus_keys = current_keys - existing_keys
    existing_minus_keys = existing_keys - current_keys
    existing_max_signal_date = safe_str(existing["signal_date"].astype(str).max())
    current_max_signal_date = safe_str(current["signal_date"].astype(str).max())

    detail = current[current["source_event_key"].astype(str).isin(current_minus_keys)].copy()
    detail["diff_side"] = "current_minus_existing"
    detail["formal_row_key"] = formal_row_key_df(detail)
    detail["sync_impact_classification"] = "after_existing_artifact_window_freshness_extension"
    inside_mask = detail["signal_date"].astype(str).le(existing_max_signal_date)
    inside_count = int(inside_mask.sum())
    after_count = int((~inside_mask).sum())
    inside_stock_count = detail[inside_mask]["stock_id"].astype(str).nunique()
    detail.loc[inside_mask, "sync_impact_classification"] = "inside_existing_artifact_window_source_sync_required"
    detail["existing_max_signal_date"] = existing_max_signal_date
    detail["current_max_signal_date"] = current_max_signal_date
    detail["discussion_reason"] = (
        "current formal producer row absent from existing formal artifact; research/backtest source sync required before v2 promotion"
    )
    detail["research_id"] = RESEARCH_ID
    detail["artifact_version"] = ARTIFACT_VERSION
    detail["source_research_id"] = SOURCE_RESEARCH_ID
    detail["advisory_status"] = ADVISORY_STATUS
    detail["model_id"] = MODEL_ID
    detail["approved_for_daily"] = false_text()
    detail["production_readiness"] = PRODUCTION_READINESS
    detail["generated_at"] = generated_at
    detail = attach_manifest(detail, load_manifest())
    detail = detail.sort_values(["signal_date", "stock_id", "confirmation_date", "selected_trigger_id"]).reset_index(drop=True)

    context = {
        "current_formal_rows": len(current),
        "existing_formal_rows": len(existing),
        "current_minus_existing_unique_keys": len(current_minus_keys),
        "existing_minus_current_unique_keys": len(existing_minus_keys),
        "current_minus_existing_rows": len(detail),
        "inside_existing_window_rows": inside_count,
        "after_existing_window_rows": after_count,
        "inside_existing_window_stocks": inside_stock_count,
        "existing_max_signal_date": existing_max_signal_date,
        "current_max_signal_date": current_max_signal_date,
    }
    return detail, context


def build_summary(detail: pd.DataFrame, context: dict[str, Any], generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    profile = summary_row(
        "source_profile",
        "formal_source_sync",
        "current_vs_existing_formal_events",
        generated_at,
        "non-writing current formal producer replay compared with existing formal operation events artifact",
    )
    profile.update(context)
    profile["sample_size"] = context["current_minus_existing_rows"]
    profile["status"] = (
        "source_sync_required_before_promotion"
        if context["current_minus_existing_unique_keys"] or context["existing_minus_current_unique_keys"]
        else "current_formal_source_matches_existing_artifact"
    )
    rows.append(profile)

    inside = detail[
        detail["sync_impact_classification"].astype(str).eq("inside_existing_artifact_window_source_sync_required")
    ]
    inside_row = summary_row(
        "discussion_item",
        "formal_source_sync",
        "inside_existing_artifact_window_rows",
        generated_at,
        "rows inside the existing artifact signal-date window that current formal producer would add",
    )
    inside_row.update(context)
    inside_row["sample_size"] = len(inside)
    inside_row["status"] = "requires_user_discussion_source_sync_scope" if len(inside) else "not_present"
    rows.append(inside_row)

    extension = detail[
        detail["sync_impact_classification"].astype(str).eq("after_existing_artifact_window_freshness_extension")
    ]
    extension_row = summary_row(
        "discussion_item",
        "formal_source_sync",
        "after_existing_artifact_window_rows",
        generated_at,
        "rows after the existing artifact max signal date that current formal producer would add",
    )
    extension_row.update(context)
    extension_row["sample_size"] = len(extension)
    extension_row["status"] = "expected_freshness_extension_requires_refresh" if len(extension) else "not_present"
    rows.append(extension_row)

    return pd.DataFrame(rows)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 40) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            values = [str(row[col]).replace("|", "/")[:180] for col in cols]
            lines.append("| " + " | ".join(values) + " |")
        return lines

    inside = detail[
        detail["sync_impact_classification"].astype(str).eq("inside_existing_artifact_window_source_sync_required")
    ]
    extension = detail[
        detail["sync_impact_classification"].astype(str).eq("after_existing_artifact_window_freshness_extension")
    ]
    lines = [
        "# Volume Range Breakout V2 Formal Source Sync Impact",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `False`",
        "- This is a non-writing research-only formal source sync impact audit.",
        "- It does not rewrite `volume_breakout_formal_operation_events.csv` and does not change `stock_model_contract_registry.csv`.",
        "- Discussion point: current formal producer would add rows absent from the existing formal artifact, including rows inside the existing artifact window.",
        "",
        "## Summary",
        "",
        *md_table(
            summary,
            [
                "audit_key",
                "sample_size",
                "current_formal_rows",
                "existing_formal_rows",
                "current_minus_existing_unique_keys",
                "existing_minus_current_unique_keys",
                "inside_existing_window_rows",
                "after_existing_window_rows",
                "status",
            ],
            10,
        ),
        "",
        "## Inside Existing Artifact Window",
        "",
        *md_table(
            inside,
            [
                "stock_id",
                "stock_name",
                "signal_date",
                "confirmation_date",
                "selected_trigger_id",
                "entry_date",
                "exit_date",
                "return_pct",
                "price_history_rows",
                "sync_impact_classification",
            ],
            50,
        ),
        "",
        "## Freshness Extension",
        "",
        *md_table(
            extension,
            [
                "stock_id",
                "stock_name",
                "signal_date",
                "confirmation_date",
                "selected_trigger_id",
                "entry_date",
                "exit_date",
                "return_pct",
                "price_history_rows",
                "sync_impact_classification",
            ],
            50,
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
    current = build_current_formal_events()
    existing = build_existing_formal_events()
    detail, context = build_detail(current, existing, generated_at)
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
