from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, normalize_code, normalize_date, now_text, write_csv  # noqa: E402
from daily_snapshot_revision_utils import select_latest_snapshot_revisions  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
HISTORY_CSV = ROOT / "data" / "monthly_revenue_history" / "monthly_revenue_history.csv"
SIGNAL_LOG_CSV = ROOT / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"
SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
PIT_PANEL_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_point_in_time_panel_latest.csv"

SUMMARY_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_coverage_backfill_audit_latest.csv"
DETAIL_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_coverage_backfill_audit_detail_latest.csv"
SUMMARY_MD = RESEARCH_LATEST_DIR / "monthly_revenue_coverage_backfill_audit_latest.md"
DOCS_SUMMARY_CSV = DOCS_LATEST_DIR / SUMMARY_CSV.name
DOCS_SUMMARY_MD = DOCS_LATEST_DIR / SUMMARY_MD.name

AUDIT_ID = "monthly_revenue_coverage_backfill_audit"
AUDIT_VERSION = "coverage_backfill_audit_v1"
REQUIRED_MIN_HISTORY_MONTHS = 24
REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT = 95.0
REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT = 95.0
TARGET_MODEL_IDS = ["price_pullback_23ema", "revenue_unreacted_range"]

SUMMARY_COLUMNS = [
    "generated_at",
    "audit_id",
    "audit_version",
    "scope",
    "source_artifact",
    "source_status",
    "history_rows",
    "history_unique_stocks",
    "history_revenue_period_count",
    "history_revenue_period_min",
    "history_revenue_period_max",
    "history_source_table_date_count",
    "history_source_table_date_min",
    "history_source_table_date_max",
    "signal_rows",
    "signal_unique_stocks",
    "signal_date_min",
    "signal_date_max",
    "asof_covered_rows",
    "asof_row_coverage_pct",
    "asof_covered_unique_stocks",
    "asof_stock_coverage_pct",
    "missing_history_stock_rows",
    "missing_asof_rows",
    "pre_first_source_table_rows",
    "required_min_history_months",
    "required_min_signal_row_coverage_pct",
    "required_min_signal_stock_coverage_pct",
    "formal_model_revenue_gate_ready",
    "backfill_required",
    "backfill_recommendation",
    "blocker_reason",
    "notes",
]

DETAIL_COLUMNS = [
    "generated_at",
    "audit_id",
    "audit_version",
    "source_artifact",
    "source_row_index",
    "signal_date",
    "model_id",
    "stock_id",
    "stock_name",
    "coverage_status",
    "matched_revenue_period",
    "matched_source_table_date",
    "history_rows_for_stock",
    "history_rows_asof",
    "matched_revenue_numerical_anomaly_flag",
    "research_join_allowed",
    "formal_model_revenue_gate_ready",
    "blocker_reason",
]


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def pct(numerator: int | float, denominator: int | float) -> str:
    if not denominator:
        return ""
    return f"{(float(numerator) / float(denominator) * 100):.2f}"


def bool_text(value: bool) -> str:
    return "True" if value else "False"


def rel_to_root(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def load_history(path: Path = HISTORY_CSV) -> pd.DataFrame:
    history = read_csv(path)
    if history.empty:
        return pd.DataFrame(columns=["stock_id", "revenue_period", "source_table_date"])
    for col in ["stock_id", "revenue_period", "source_table_date"]:
        if col not in history.columns:
            history[col] = ""
    history = history.copy()
    history["stock_id"] = history["stock_id"].map(normalize_code)
    history["source_table_date"] = history["source_table_date"].map(normalize_date)
    history = history[history["stock_id"].ne("") & history["source_table_date"].ne("")]
    return history.sort_values(["stock_id", "source_table_date", "revenue_period"]).reset_index(drop=True)


def load_signal_rows(
    snapshot_dir: Path = SNAPSHOT_DIR,
    repository_root: Path = ROOT,
) -> tuple[pd.DataFrame, str]:
    if SIGNAL_LOG_CSV.exists():
        df = read_csv(SIGNAL_LOG_CSV)
        source = rel_to_root(SIGNAL_LOG_CSV)
    else:
        frames: list[pd.DataFrame] = []
        snapshots = select_latest_snapshot_revisions(
            snapshot_dir,
            "model_signals_for_report",
            repository_root=repository_root,
        )
        for snapshot in snapshots:
            frame = read_csv(snapshot.path)
            if not frame.empty:
                frame["source_snapshot_file"] = rel_to_root(snapshot.path)
                frames.append(frame)
        df = pd.concat(frames, ignore_index=True, sort=False) if frames else pd.DataFrame()
        source = rel_to_root(snapshot_dir / "daily_published_model_snapshot_manifest.csv")
    for col in ["signal_date", "model_id", "stock_id", "stock_name"]:
        if col not in df.columns:
            df[col] = ""
    df = df.copy()
    df["signal_date"] = df["signal_date"].map(normalize_date)
    df["stock_id"] = df["stock_id"].map(normalize_code)
    df = df[df["signal_date"].ne("") & df["stock_id"].ne("")]
    return df.reset_index(drop=True), source


def latest_asof_for_stock(history_by_stock: dict[str, pd.DataFrame], stock_id: str, signal_date: str) -> tuple[pd.Series | None, int, int]:
    stock_history = history_by_stock.get(stock_id)
    if stock_history is None or stock_history.empty:
        return None, 0, 0
    asof = stock_history[stock_history["source_table_date"].astype(str) <= signal_date]
    if asof.empty:
        return None, len(stock_history), 0
    return asof.iloc[-1], len(stock_history), len(asof)


def build_detail(signals: pd.DataFrame, history: pd.DataFrame, source_artifact: str) -> pd.DataFrame:
    generated_at = now_text()
    history_by_stock = {
        stock_id: group.sort_values(["source_table_date", "revenue_period"]).reset_index(drop=True)
        for stock_id, group in history.groupby("stock_id", dropna=False)
    }
    rows: list[dict[str, Any]] = []
    for index, row in signals.iterrows():
        signal_date = safe_str(row.get("signal_date"))
        stock_id = normalize_code(row.get("stock_id"))
        matched, history_rows_for_stock, history_rows_asof = latest_asof_for_stock(history_by_stock, stock_id, signal_date)
        if not history_rows_for_stock:
            coverage_status = "missing_stock_in_monthly_revenue_history"
            blocker_reason = "stock has no canonical monthly revenue history row"
        elif not history_rows_asof:
            coverage_status = "missing_asof_revenue_on_or_before_signal_date"
            blocker_reason = "canonical monthly revenue source_table_date is after signal_date"
        else:
            coverage_status = "ready_asof_history_row"
            blocker_reason = "coverage row exists but formal gate still requires sufficient history coverage audit"
        rows.append(
            {
                "generated_at": generated_at,
                "audit_id": AUDIT_ID,
                "audit_version": AUDIT_VERSION,
                "source_artifact": source_artifact,
                "source_row_index": str(index),
                "signal_date": signal_date,
                "model_id": safe_str(row.get("model_id")),
                "stock_id": stock_id,
                "stock_name": safe_str(row.get("stock_name")),
                "coverage_status": coverage_status,
                "matched_revenue_period": safe_str(matched.get("revenue_period")) if matched is not None else "",
                "matched_source_table_date": safe_str(matched.get("source_table_date")) if matched is not None else "",
                "history_rows_for_stock": str(history_rows_for_stock),
                "history_rows_asof": str(history_rows_asof),
                "matched_revenue_numerical_anomaly_flag": safe_str(matched.get("revenue_numerical_anomaly_flag")) if matched is not None else "",
                "research_join_allowed": "True" if matched is not None else "False",
                "formal_model_revenue_gate_ready": "False",
                "blocker_reason": blocker_reason,
            }
        )
    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def readiness_from_metrics(
    history_months: int,
    row_coverage: float,
    stock_coverage: float,
    *,
    require_signal_coverage: bool = True,
) -> tuple[bool, str]:
    blockers: list[str] = []
    if history_months < REQUIRED_MIN_HISTORY_MONTHS:
        blockers.append(f"history_period_count_lt_{REQUIRED_MIN_HISTORY_MONTHS}")
    if require_signal_coverage:
        if row_coverage < REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT:
            blockers.append(f"signal_row_coverage_lt_{REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT:.0f}pct")
        if stock_coverage < REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT:
            blockers.append(f"signal_stock_coverage_lt_{REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT:.0f}pct")
    return (not blockers, ";".join(blockers))


def summarize_signal_scope(scope: str, detail: pd.DataFrame, history: pd.DataFrame, source_artifact: str) -> dict[str, Any]:
    signal_rows = len(detail)
    signal_unique_stocks = int(detail["stock_id"].nunique()) if signal_rows else 0
    covered = detail[detail["coverage_status"].eq("ready_asof_history_row")]
    covered_rows = len(covered)
    covered_unique_stocks = int(covered["stock_id"].nunique()) if not covered.empty else 0
    row_coverage = float(pct(covered_rows, signal_rows) or 0)
    stock_coverage = float(pct(covered_unique_stocks, signal_unique_stocks) or 0)
    history_months = int(history["revenue_period"].nunique()) if not history.empty and "revenue_period" in history.columns else 0
    ready, blocker = readiness_from_metrics(history_months, row_coverage, stock_coverage)
    first_source_date = history["source_table_date"].min() if not history.empty else ""
    pre_first_rows = (
        int(detail["signal_date"].astype(str).lt(first_source_date).sum())
        if first_source_date and not detail.empty
        else 0
    )
    return {
        "generated_at": now_text(),
        "audit_id": AUDIT_ID,
        "audit_version": AUDIT_VERSION,
        "scope": scope,
        "source_artifact": source_artifact,
        "source_status": "signal_rows_found" if signal_rows else "missing_signal_rows",
        "history_rows": str(len(history)),
        "history_unique_stocks": str(history["stock_id"].nunique() if not history.empty else 0),
        "history_revenue_period_count": str(history_months),
        "history_revenue_period_min": history["revenue_period"].min() if not history.empty else "",
        "history_revenue_period_max": history["revenue_period"].max() if not history.empty else "",
        "history_source_table_date_count": str(history["source_table_date"].nunique() if not history.empty else 0),
        "history_source_table_date_min": history["source_table_date"].min() if not history.empty else "",
        "history_source_table_date_max": history["source_table_date"].max() if not history.empty else "",
        "signal_rows": str(signal_rows),
        "signal_unique_stocks": str(signal_unique_stocks),
        "signal_date_min": detail["signal_date"].min() if signal_rows else "",
        "signal_date_max": detail["signal_date"].max() if signal_rows else "",
        "asof_covered_rows": str(covered_rows),
        "asof_row_coverage_pct": pct(covered_rows, signal_rows),
        "asof_covered_unique_stocks": str(covered_unique_stocks),
        "asof_stock_coverage_pct": pct(covered_unique_stocks, signal_unique_stocks),
        "missing_history_stock_rows": str(int(detail["coverage_status"].eq("missing_stock_in_monthly_revenue_history").sum())) if signal_rows else "0",
        "missing_asof_rows": str(int(detail["coverage_status"].eq("missing_asof_revenue_on_or_before_signal_date").sum())) if signal_rows else "0",
        "pre_first_source_table_rows": str(pre_first_rows),
        "required_min_history_months": str(REQUIRED_MIN_HISTORY_MONTHS),
        "required_min_signal_row_coverage_pct": f"{REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT:.2f}",
        "required_min_signal_stock_coverage_pct": f"{REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT:.2f}",
        "formal_model_revenue_gate_ready": bool_text(ready),
        "backfill_required": bool_text(not ready),
        "backfill_recommendation": "open_validated_historical_backfill_pr" if not ready else "no_backfill_required_for_this_scope",
        "blocker_reason": blocker,
        "notes": "Close as-of join is measured from source_table_date <= signal_date; formal gate remains blocked until coverage thresholds pass.",
    }


def summarize_history_scope(history: pd.DataFrame) -> dict[str, Any]:
    history_months = int(history["revenue_period"].nunique()) if not history.empty else 0
    ready, blocker = readiness_from_metrics(history_months, 0.0, 0.0, require_signal_coverage=False)
    return {
        "generated_at": now_text(),
        "audit_id": AUDIT_ID,
        "audit_version": AUDIT_VERSION,
        "scope": "canonical_monthly_revenue_history",
        "source_artifact": rel_to_root(HISTORY_CSV),
        "source_status": "history_found" if not history.empty else "missing_history",
        "history_rows": str(len(history)),
        "history_unique_stocks": str(history["stock_id"].nunique() if not history.empty else 0),
        "history_revenue_period_count": str(history_months),
        "history_revenue_period_min": history["revenue_period"].min() if not history.empty else "",
        "history_revenue_period_max": history["revenue_period"].max() if not history.empty else "",
        "history_source_table_date_count": str(history["source_table_date"].nunique() if not history.empty else 0),
        "history_source_table_date_min": history["source_table_date"].min() if not history.empty else "",
        "history_source_table_date_max": history["source_table_date"].max() if not history.empty else "",
        "signal_rows": "0",
        "signal_unique_stocks": "0",
        "signal_date_min": "",
        "signal_date_max": "",
        "asof_covered_rows": "0",
        "asof_row_coverage_pct": "",
        "asof_covered_unique_stocks": "0",
        "asof_stock_coverage_pct": "",
        "missing_history_stock_rows": "0",
        "missing_asof_rows": "0",
        "pre_first_source_table_rows": "0",
        "required_min_history_months": str(REQUIRED_MIN_HISTORY_MONTHS),
        "required_min_signal_row_coverage_pct": f"{REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT:.2f}",
        "required_min_signal_stock_coverage_pct": f"{REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT:.2f}",
        "formal_model_revenue_gate_ready": bool_text(ready),
        "backfill_required": bool_text(not ready),
        "backfill_recommendation": "open_validated_historical_backfill_pr" if not ready else "no_backfill_required",
        "blocker_reason": blocker or "signal_scope_not_evaluated_in_history_row",
        "notes": "Canonical full-market source history is evaluated for period depth only; model rows evaluate point-in-time signal coverage.",
    }


def summarize_pit_panel() -> dict[str, Any]:
    panel = read_csv(PIT_PANEL_CSV)
    return {
        "generated_at": now_text(),
        "audit_id": AUDIT_ID,
        "audit_version": AUDIT_VERSION,
        "scope": "monthly_revenue_point_in_time_panel",
        "source_artifact": rel_to_root(PIT_PANEL_CSV),
        "source_status": "panel_found" if not panel.empty else "missing_panel",
        "history_rows": str(len(panel)),
        "history_unique_stocks": str(panel["stock_id"].nunique() if not panel.empty and "stock_id" in panel.columns else 0),
        "history_revenue_period_count": str(panel["revenue_period"].nunique() if not panel.empty and "revenue_period" in panel.columns else 0),
        "history_revenue_period_min": panel["revenue_period"].min() if not panel.empty and "revenue_period" in panel.columns else "",
        "history_revenue_period_max": panel["revenue_period"].max() if not panel.empty and "revenue_period" in panel.columns else "",
        "history_source_table_date_count": str(panel["observed_as_of_date"].nunique() if not panel.empty and "observed_as_of_date" in panel.columns else 0),
        "history_source_table_date_min": panel["observed_as_of_date"].min() if not panel.empty and "observed_as_of_date" in panel.columns else "",
        "history_source_table_date_max": panel["observed_as_of_date"].max() if not panel.empty and "observed_as_of_date" in panel.columns else "",
        "signal_rows": "0",
        "signal_unique_stocks": "0",
        "signal_date_min": "",
        "signal_date_max": "",
        "asof_covered_rows": "0",
        "asof_row_coverage_pct": "",
        "asof_covered_unique_stocks": "0",
        "asof_stock_coverage_pct": "",
        "missing_history_stock_rows": "0",
        "missing_asof_rows": "0",
        "pre_first_source_table_rows": "0",
        "required_min_history_months": str(REQUIRED_MIN_HISTORY_MONTHS),
        "required_min_signal_row_coverage_pct": f"{REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT:.2f}",
        "required_min_signal_stock_coverage_pct": f"{REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT:.2f}",
        "formal_model_revenue_gate_ready": "False",
        "backfill_required": "True",
        "backfill_recommendation": "do_not_use_candidate_snapshot_panel_as_full_market_backfill",
        "blocker_reason": "coverage_limited_candidate_snapshot_observed_values_not_full_market_history",
        "notes": "This panel can help research discussion only; it is not a validated full-market historical backfill source.",
    }


def build_summary(history: pd.DataFrame, detail: pd.DataFrame, source_artifact: str) -> pd.DataFrame:
    rows = [summarize_history_scope(history), summarize_pit_panel()]
    rows.append(summarize_signal_scope("daily_model_signal_log_all_models", detail, history, source_artifact))
    for model_id in TARGET_MODEL_IDS:
        model_detail = detail[detail["model_id"].astype(str).eq(model_id)].copy()
        rows.append(summarize_signal_scope(f"model:{model_id}", model_detail, history, source_artifact))
    for model_id in sorted(set(detail["model_id"].astype(str)) - set(TARGET_MODEL_IDS) - {""}):
        model_detail = detail[detail["model_id"].astype(str).eq(model_id)].copy()
        rows.append(summarize_signal_scope(f"model:{model_id}", model_detail, history, source_artifact))
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    model_rows = summary[summary["scope"].astype(str).str.startswith("model:")].copy()
    model_rows["model_id"] = model_rows["scope"].str.replace("model:", "", regex=False)
    formal_scope_rows = summary[~summary["scope"].astype(str).eq("monthly_revenue_point_in_time_panel")].copy()
    lines = [
        "# Monthly Revenue Coverage / Backfill Audit",
        "",
        f"- generated_at: `{now_text()}`",
        f"- audit_id: `{AUDIT_ID}`",
        f"- audit_version: `{AUDIT_VERSION}`",
        f"- formal_model_revenue_gate_ready: `{summary['formal_model_revenue_gate_ready'].eq('True').any()}`",
        f"- formal_scope_backfill_required: `{formal_scope_rows['backfill_required'].eq('True').any()}`",
        f"- candidate_snapshot_pit_panel_full_market_ready: `{False}`",
        "- rule: canonical monthly revenue joins require `source_table_date <= signal_date`.",
        "- rule: candidate snapshot PIT revenue is coverage-limited and cannot be used as full-market historical backfill.",
        "",
        "## Coverage Summary",
        "",
        markdown_table(
            summary,
            [
                "scope",
                "source_status",
                "history_revenue_period_count",
                "history_revenue_period_min",
                "history_revenue_period_max",
                "signal_rows",
                "asof_row_coverage_pct",
                "asof_stock_coverage_pct",
                "formal_model_revenue_gate_ready",
                "backfill_required",
                "blocker_reason",
            ],
            limit=80,
        ),
        "",
        "## Target Models",
        "",
        markdown_table(
            model_rows,
            [
                "model_id",
                "signal_rows",
                "signal_date_min",
                "signal_date_max",
                "asof_covered_rows",
                "asof_row_coverage_pct",
                "missing_asof_rows",
                "formal_model_revenue_gate_ready",
                "backfill_recommendation",
            ],
            limit=20,
        )
        if not model_rows.empty
        else "No model-level rows.",
        "",
        "## Detail Sample",
        "",
        markdown_table(
            detail,
            [
                "signal_date",
                "model_id",
                "stock_id",
                "coverage_status",
                "matched_revenue_period",
                "matched_source_table_date",
                "blocker_reason",
            ],
            limit=30,
        )
        if not detail.empty
        else "No signal detail rows.",
    ]
    SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_SUMMARY_MD.write_text(SUMMARY_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    history = load_history()
    signals, signal_source = load_signal_rows()
    detail = build_detail(signals, history, signal_source)
    summary = build_summary(history, detail, signal_source)
    write_csv(summary, SUMMARY_CSV)
    write_csv(detail, DETAIL_CSV)
    write_csv(summary, DOCS_SUMMARY_CSV)
    write_markdown(summary, detail)
    formal_scope = summary[~summary["scope"].astype(str).eq("monthly_revenue_point_in_time_panel")]
    print(f"built_monthly_revenue_coverage_backfill_audit_rows={len(summary)}")
    print(f"built_monthly_revenue_coverage_backfill_audit_detail_rows={len(detail)}")
    print(f"formal_scope_backfill_required={formal_scope['backfill_required'].eq('True').any()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
