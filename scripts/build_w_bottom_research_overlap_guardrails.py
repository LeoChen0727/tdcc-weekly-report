from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_research_overlap_guardrails_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_research_overlap_guardrails_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_research_overlap_guardrails.csv"

RESEARCH_ID = "w_bottom_research_overlap_guardrails"
ARTIFACT_VERSION = "w_bottom_research_overlap_guardrails_20260708"
MODEL_ID = "w_bottom_right_side"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"

STRATEGY_COLUMNS = [
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "condition_set_id",
    "parameter_set_id",
    "signal_market_regime",
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "advisory_status",
    "model_id",
    "input_artifact_id",
    "source_path",
    "row_scope",
    "strategy_key",
    "strategy_key_columns",
    "input_rows",
    "checked_rows",
    "unique_stocks",
    "stocks_with_multiple_events",
    "max_rows_per_stock",
    "overlap_pair_count",
    "approved_for_daily_values",
    "production_readiness_values",
    "promotion_evidence_status",
    "required_followup",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
}


@dataclass(frozen=True)
class InputArtifact:
    artifact_id: str
    path: Path


INPUT_ARTIFACTS = [
    InputArtifact(
        "w_bottom_split_entry_outcome_backtest_detail",
        RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_detail_latest.csv",
    ),
    InputArtifact(
        "w_bottom_early_entry_parameter_grid_detail",
        RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv",
    ),
    InputArtifact(
        "w_bottom_early_entry_stop_loss_audit_detail",
        RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_detail_latest.csv",
    ),
    InputArtifact(
        "w_bottom_market_regime_gated_review",
        RESEARCH_LATEST_DIR / "w_bottom_market_regime_gated_review_latest.csv",
    ),
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


def false_text() -> str:
    return "False"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for column in SUMMARY_COLUMNS:
        if column not in out.columns:
            out[column] = ""
    out = out[SUMMARY_COLUMNS]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def parse_yyyymmdd(series: pd.Series) -> pd.Series:
    text = series.astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
    return pd.to_datetime(text, format="%Y%m%d", errors="coerce")


def joined_unique(series: pd.Series) -> str:
    values = sorted({safe_str(value) for value in series if safe_str(value)})
    return "|".join(values)


def strategy_key(row: pd.Series, columns: list[str]) -> str:
    values = [safe_str(row.get(column)) for column in columns]
    return "|".join(values) if values else "all_rows"


def overlap_metrics(frame: pd.DataFrame, stock_col: str, entry_col: str, exit_col: str) -> dict[str, int]:
    work = frame.copy()
    work["_entry_dt"] = parse_yyyymmdd(work[entry_col])
    work["_exit_dt"] = parse_yyyymmdd(work[exit_col])
    work = work[
        work[stock_col].astype(str).ne("") & work["_entry_dt"].notna() & work["_exit_dt"].notna()
    ].copy()
    if work.empty:
        return {
            "checked_rows": 0,
            "unique_stocks": 0,
            "stocks_with_multiple_events": 0,
            "max_rows_per_stock": 0,
            "overlap_pair_count": 0,
        }

    overlap_pairs = 0
    stocks_with_multiple = 0
    max_rows = 0
    for _, part in work.sort_values([stock_col, "_entry_dt", "_exit_dt"]).groupby(stock_col, dropna=False):
        max_rows = max(max_rows, len(part))
        if len(part) > 1:
            stocks_with_multiple += 1
        active: list[pd.Series] = []
        for _, row in part.iterrows():
            for prior in active:
                if row["_entry_dt"] <= prior["_exit_dt"]:
                    overlap_pairs += 1
            active = [prior for prior in active if prior["_exit_dt"] >= row["_entry_dt"]]
            active.append(row)

    return {
        "checked_rows": len(work),
        "unique_stocks": int(work[stock_col].nunique()),
        "stocks_with_multiple_events": stocks_with_multiple,
        "max_rows_per_stock": max_rows,
        "overlap_pair_count": overlap_pairs,
    }


def validate_input_schema(artifact: InputArtifact, df: pd.DataFrame) -> tuple[str, str]:
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: {artifact.artifact_id} contains forbidden production fields: {forbidden}")
    missing = sorted({"stock_id", "entry_date", "exit_date"} - set(df.columns))
    if missing:
        raise SystemExit(f"ERROR: {artifact.artifact_id} missing required operation window columns: {missing}")
    return "entry_date", "exit_date"


def audit_artifact(artifact: InputArtifact, generated_at: str) -> list[dict[str, Any]]:
    df = read_csv(artifact.path)
    entry_col, exit_col = validate_input_schema(artifact, df)
    row_scope = "mature_true_rows" if "mature" in df.columns else "all_rows"
    scoped = df.copy()
    if "mature" in scoped.columns and scoped["mature"].astype(str).str.lower().eq("true").any():
        scoped = scoped[scoped["mature"].astype(str).str.lower().eq("true")].copy()

    strategy_columns = [column for column in STRATEGY_COLUMNS if column in scoped.columns]
    if not strategy_columns:
        scoped["_all_rows"] = "all_rows"
        strategy_columns = ["_all_rows"]

    rows: list[dict[str, Any]] = []
    for key_values, part in scoped.groupby(strategy_columns, dropna=False, sort=False):
        metrics = overlap_metrics(part, "stock_id", entry_col, exit_col)
        key_row = part.iloc[0]
        key = strategy_key(key_row, strategy_columns)
        overlap_count = metrics["overlap_pair_count"]
        status = (
            "blocked_requires_same_stock_non_overlap_artifact"
            if overlap_count > 0
            else "no_overlap_detected_for_strategy"
        )
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "artifact_version": ARTIFACT_VERSION,
                "advisory_status": ADVISORY_STATUS,
                "model_id": MODEL_ID,
                "input_artifact_id": artifact.artifact_id,
                "source_path": str(artifact.path).replace("\\", "/"),
                "row_scope": row_scope,
                "strategy_key": key,
                "strategy_key_columns": "|".join(strategy_columns),
                "input_rows": len(df),
                "checked_rows": metrics["checked_rows"],
                "unique_stocks": metrics["unique_stocks"],
                "stocks_with_multiple_events": metrics["stocks_with_multiple_events"],
                "max_rows_per_stock": metrics["max_rows_per_stock"],
                "overlap_pair_count": overlap_count,
                "approved_for_daily_values": joined_unique(part["approved_for_daily"])
                if "approved_for_daily" in part.columns
                else "",
                "production_readiness_values": joined_unique(part["production_readiness"])
                if "production_readiness" in part.columns
                else "",
                "promotion_evidence_status": status,
                "required_followup": "publish_same_stock_non_overlap_basis_before_promotion_evidence"
                if overlap_count > 0
                else "none_for_overlap",
                "approved_for_daily": false_text(),
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    return rows


def write_markdown(summary: pd.DataFrame) -> None:
    total_overlap = int(pd.to_numeric(summary["overlap_pair_count"], errors="coerce").fillna(0).sum())
    blocked = summary[summary["promotion_evidence_status"].astype(str).eq("blocked_requires_same_stock_non_overlap_artifact")]
    lines = [
        "# W Bottom Research Overlap Guardrails",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        "- status: research-only guardrail; no production registry, daily adapter, or PDF behavior change.",
        "- rule: W-bottom event/grid research with same-stock active-window overlap cannot be cited as promotion evidence until a same-stock non-overlap basis is published.",
        f"- total_overlap_pair_count: `{total_overlap}`",
        f"- blocked_strategy_rows: `{len(blocked)}`",
        "",
        "## Blocked Strategy Examples",
        "",
    ]
    if blocked.empty:
        lines.append("_No blocked strategy rows._")
    else:
        lines.append(
            blocked[
                [
                    "input_artifact_id",
                    "strategy_key",
                    "checked_rows",
                    "unique_stocks",
                    "overlap_pair_count",
                    "promotion_evidence_status",
                ]
            ]
            .sort_values(["overlap_pair_count"], ascending=False)
            .head(12)
            .to_markdown(index=False)
        )
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    rows: list[dict[str, Any]] = []
    for artifact in INPUT_ARTIFACTS:
        rows.extend(audit_artifact(artifact, generated_at))
    summary = pd.DataFrame(rows)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
