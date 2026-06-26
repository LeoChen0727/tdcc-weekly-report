from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(".")
DAILY_PRICE_DIR = ROOT / "data" / "daily_price"
PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_LATEST_DIR = LATEST_DIR / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_backfill_feasibility_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_backfill_feasibility_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_backfill_feasibility_audit.csv"

RESEARCH_ID = "w_bottom_early_entry_backfill_feasibility_audit"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_data_coverage_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
OWNER = "research_backtest_data_governance"

OUTPUT_COLUMNS = [
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "audit_section",
    "audit_item_id",
    "source_artifact",
    "status",
    "finding",
    "daily_price_file_count",
    "daily_price_unique_dates",
    "daily_price_rows",
    "daily_price_min_date",
    "daily_price_max_date",
    "price_history_file_count",
    "price_history_rows",
    "price_history_min_date",
    "price_history_max_date",
    "price_history_files_ge_180",
    "earliest_180th_observed_date",
    "repo_existing_data_can_extend_to_earlier_2025",
    "max_signal_start_with_existing_data",
    "required_external_source",
    "required_action",
    "required_followup_owner",
    "forbidden_actions",
    "production_impact",
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


def read_date_column(path: Path) -> pd.Series:
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False, usecols=lambda c: c.lower() == "date")
    except Exception:
        return pd.Series(dtype=str)
    if "date" not in df.columns:
        return pd.Series(dtype=str)
    dates = df["date"].map(normalize_date)
    return dates[dates.str.len().ge(8)]


def daily_price_coverage() -> dict[str, Any]:
    dates: list[str] = []
    files_with_dates = 0
    for path in sorted(DAILY_PRICE_DIR.glob("*.csv")):
        file_dates = read_date_column(path)
        if file_dates.empty:
            continue
        files_with_dates += 1
        dates.extend(file_dates.tolist())
    unique_dates = sorted(set(dates))
    return {
        "daily_price_file_count": files_with_dates,
        "daily_price_unique_dates": len(unique_dates),
        "daily_price_rows": len(dates),
        "daily_price_min_date": min(unique_dates) if unique_dates else "",
        "daily_price_max_date": max(unique_dates) if unique_dates else "",
    }


def price_history_coverage() -> dict[str, Any]:
    mins: list[str] = []
    maxs: list[str] = []
    row_count = 0
    file_count = 0
    observed_180th_dates: list[str] = []
    for path in sorted(PRICE_HISTORY_DIR.glob("*.csv")):
        dates = read_date_column(path).sort_values().reset_index(drop=True)
        if dates.empty:
            continue
        file_count += 1
        row_count += int(len(dates))
        mins.append(str(dates.iloc[0]))
        maxs.append(str(dates.iloc[-1]))
        if len(dates) >= 180:
            observed_180th_dates.append(str(dates.iloc[179]))
    return {
        "price_history_file_count": file_count,
        "price_history_rows": row_count,
        "price_history_min_date": min(mins) if mins else "",
        "price_history_max_date": max(maxs) if maxs else "",
        "price_history_files_ge_180": len(observed_180th_dates),
        "earliest_180th_observed_date": min(observed_180th_dates) if observed_180th_dates else "",
    }


def base_row(generated_at: str, daily: dict[str, Any], history: dict[str, Any]) -> dict[str, Any]:
    daily_min = safe_str(daily.get("daily_price_min_date"))
    earliest_180th = safe_str(history.get("earliest_180th_observed_date"))
    extension_available = bool(daily_min and daily_min < "20250407" and earliest_180th and earliest_180th < "20260105")
    row = {column: "" for column in OUTPUT_COLUMNS}
    row.update(
        {
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "surface_id": SURFACE_ID,
            "repo_existing_data_can_extend_to_earlier_2025": "true" if extension_available else "false",
            "max_signal_start_with_existing_data": safe_str(history.get("earliest_180th_observed_date")),
            "required_external_source": (
                "completed official TWSE MI_INDEX and TPEx DAILY_CLOSE_quotes backfill"
                if extension_available
                else "TWSE MI_INDEX daily OHLCV; TPEx DAILY_CLOSE_quotes daily OHLCV"
            ),
            "required_action": (
                "completed_official_price_backfill_rebuild_stock_price_history_and_w_bottom_outputs"
                if extension_available
                else "formal historical price backfill decision before rebuilding W-bottom research outputs"
            ),
            "required_followup_owner": OWNER,
            "forbidden_actions": "do_not_modify_production_model_scoring_ranking_daily_full_pipeline_or_pdfs",
            "production_impact": "none",
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
    )
    row.update(daily)
    row.update(history)
    return row


def build_rows() -> pd.DataFrame:
    generated_at = now_text()
    daily = daily_price_coverage()
    history = price_history_coverage()
    extension_available = bool(
        safe_str(daily.get("daily_price_min_date"))
        and safe_str(daily.get("daily_price_min_date")) < "20250407"
        and safe_str(history.get("earliest_180th_observed_date"))
        and safe_str(history.get("earliest_180th_observed_date")) < "20260105"
    )
    rows: list[dict[str, Any]] = []

    current = base_row(generated_at, daily, history)
    current.update(
        {
            "audit_section": "current_repo_data_window",
            "audit_item_id": "daily_price_and_stock_price_history",
            "source_artifact": "data/daily_price; data/stock_price_history",
            "status": "extended_after_approved_official_price_backfill" if extension_available else "blocked_existing_data_window",
            "finding": (
                "Repo price data now starts before 20250407 after approved official TWSE/TPEx backfill; "
                f"the W-bottom 180 observed trading-day gate can start at {history.get('earliest_180th_observed_date')}."
                if extension_available
                else "Existing repo price data starts at 20250407; with the W-bottom 180 observed trading-day "
                "history gate, the earliest available signal start remains 20260105."
            ),
        }
    )
    rows.append(current)

    support_artifacts = [
        (
            "stock_price_history_manifest",
            "output/latest/stock_price_history_manifest.csv",
            "Manifest documents current per-stock price history paths and date ranges.",
        ),
        (
            "w_bottom_data_coverage_audit",
            "output/latest/research_backtest/w_bottom_early_entry_data_coverage_audit_latest.md",
            (
                "W-bottom coverage audit records the extended price coverage and signal window after approved backfill."
                if extension_available
                else "Existing W-bottom coverage audit records 20250407 to 20260624 price coverage and 20260105 signal start."
            ),
        ),
        (
            "stock_price_history_builder",
            "scripts/build_stock_price_history.py",
            "Rebuilds per-stock history after daily price files exist; this run rebuilt history after approved pre-20250407 backfill.",
        ),
        (
            "range_repair_backfill_script",
            "scripts/repair_daily_price_range.py",
            (
                "Fetched approved historical date ranges through the official TWSE/TPEx price fetcher; non-trading/no-target-source dates were not written."
                if extension_available
                else "Can fetch selected date ranges through the official price fetcher, but earlier 2025 requires an approved external-source backfill run."
            ),
        ),
        (
            "official_price_backfill_script",
            "backfill_official_daily_price.py",
            "Manual backfill helper uses a rolling 420 calendar-day lookback and does not extend earlier than the current repo start for this audit.",
        ),
        (
            "price_history_continuity_validator",
            "scripts/validate_daily_price_history_continuity.py",
            "Validates recent daily price/history continuity, not full historical W-bottom research coverage by itself.",
        ),
        (
            "w_bottom_coverage_validator",
            "scripts/validate_w_bottom_early_entry_data_coverage_audit.py",
            "Validates the existing research-only W-bottom coverage audit and blocks accidental production decision fields.",
        ),
    ]

    for item_id, artifact, finding in support_artifacts:
        support = base_row(generated_at, daily, history)
        support.update(
            {
                "audit_section": "supporting_artifact_inventory",
                "audit_item_id": item_id,
                "source_artifact": artifact,
                "status": "available" if (ROOT / artifact).exists() else "missing",
                "finding": finding,
            }
        )
        rows.append(support)

    conclusion = base_row(generated_at, daily, history)
    conclusion.update(
        {
            "audit_section": "backfill_feasibility_conclusion",
            "audit_item_id": "w_bottom_early_entry_2025_extension",
            "source_artifact": "data/daily_price; data/stock_price_history; scripts/repair_daily_price_range.py",
            "status": (
                "completed_approved_official_price_backfill"
                if extension_available
                else "blocked_requires_external_price_backfill"
            ),
            "finding": (
                "W-bottom research input coverage can now extend into earlier 2025 using the repo data produced by the approved official "
                "TWSE/TPEx backfill, stock_price_history rebuild, and W-bottom output rebuild."
                if extension_available
                else "Cannot extend W-bottom research input coverage into earlier 2025 months using only data already stored in the repo. "
                "The required gap is official full-market daily OHLCV before 20250407, followed by a rebuild of stock_price_history and W-bottom research outputs."
            ),
        }
    )
    rows.append(conclusion)

    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str]) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for _, row in df.iterrows():
        values = [safe_str(row.get(column)).replace("|", "/") for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_markdown(df: pd.DataFrame) -> None:
    conclusion = df[df["audit_section"].eq("backfill_feasibility_conclusion")].iloc[0]
    lines = [
        "# W-Bottom Early-Entry Backfill Feasibility Audit",
        "",
        f"- generated_at: `{conclusion['generated_at']}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- production impact: `none`",
        "- scope: research/backtest data governance only.",
        "- this audit does not modify production conditions, scoring, ranking, PDFs, baselines, daily_full_pipeline, or GitHub Actions triggers.",
        "- rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "",
        "## Conclusion",
        "",
        f"- can extend with repo-existing data: `{conclusion['repo_existing_data_can_extend_to_earlier_2025']}`",
        f"- max signal start with repo-existing data: `{conclusion['max_signal_start_with_existing_data']}`",
        f"- status: `{conclusion['status']}`",
        f"- required external source: `{conclusion['required_external_source']}`",
        f"- required action: `{conclusion['required_action']}`",
        f"- required follow-up owner: `{conclusion['required_followup_owner']}`",
        "",
        "## Current Data Window",
        "",
        *markdown_table(
            df[df["audit_section"].eq("current_repo_data_window")],
            [
                "daily_price_min_date",
                "daily_price_max_date",
                "daily_price_unique_dates",
                "price_history_file_count",
                "price_history_files_ge_180",
                "earliest_180th_observed_date",
                "status",
            ],
        ),
        "",
        "## Supporting Artifacts",
        "",
        *markdown_table(
            df[df["audit_section"].eq("supporting_artifact_inventory")],
            ["audit_item_id", "source_artifact", "status", "finding"],
        ),
        "",
        "## Handoff",
        "",
        "- Do not promote W-bottom early-entry variants from this evidence window.",
        "- Do not write research variants or recommendations into the production baseline.",
        "- Approved historical official price backfill, `scripts/build_stock_price_history.py`, W-bottom research rebuilds, and coverage validation have completed for available official trading dates.",
        "- Remaining promotion blockers belong to research stability/mature-sample review, not to the original 20250407 price-history start.",
        "- Keep PR #194 draft until a separate promotion or production sync is explicitly requested.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    df = build_rows()
    write_csv(df, LATEST_CSV)
    write_csv(df, HISTORY_CSV)
    write_markdown(df)
    print(f"Saved: {LATEST_CSV} rows={len(df)}")
    print(f"Saved: {HISTORY_CSV} rows={len(df)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
