from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import shutil

import pandas as pd

from build_w_bottom_candidate_chart_review_packet import (
    bool_text,
    draw_chart,
    normalize_code,
    normalize_date,
    safe_str,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_TAXONOMY_CSV = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"

CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_core_mainstream_exclude_wv_review.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_core_mainstream_exclude_wv_review"
SOURCE_RESEARCH_ID = "w_bottom_wv_filter_stability_grid"
SOURCE_DETAIL_RESEARCH_ID = "w_bottom_path_quality_filter_audit"
SOURCE_QUALITY_RESEARCH_ID = "w_bottom_candidate_quality_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_core_mainstream_exclude_wv_review_20260625"

TARGET_TRANSITION_STATUS = "observation_to_volume_confirmation"
TARGET_SEGMENT_DIMENSION = "effective_mainstream_label"
TARGET_SEGMENT_VALUE = "core_mainstream"
TARGET_FILTER_ID = "exclude_wv_multiple_turn"
EXCLUDED_PATH_CATEGORY = "wv_multiple_turn_risk"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

OUTPUT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "source_detail_research_id",
    "source_quality_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "segment_dimension",
    "segment_value",
    "filter_id",
    "transition_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "slope_curvature_category",
    "slope_issue_reasons",
    "path_days",
    "full_path_significant_turn_count",
    "full_path_direction_switch_count",
    "left_descent_wrong_direction_rate",
    "first_rebound_wrong_direction_rate",
    "second_decline_wrong_direction_rate",
    "right_rebound_wrong_direction_rate",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "signal_close",
    "neckline_price",
    "right_low_value",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "second_arc_volume_ratio",
    "primary_review_flag",
    "sym1_5_quality_bucket",
    "sym1_5_w_shape_completed",
    "sym1_5_completion_date",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_breakout_date",
    "sym1_5_right_low_broken",
    "sym1_5_right_low_broken_date",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "effective_mainstream_label",
    "has_hot_theme",
    "structural_theme_bucket",
    "primary_theme",
    "taxonomy_source",
    "taxonomy_confidence",
    "chart_path",
    "chart_path_absolute",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def normalize_keys(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_code)
    if "signal_date" in df.columns:
        df["signal_date"] = df["signal_date"].map(normalize_date)
    return df


def read_taxonomy() -> pd.DataFrame:
    taxonomy = read_csv(SOURCE_TAXONOMY_CSV)
    if "stock_id" not in taxonomy.columns:
        raise SystemExit(f"ERROR: taxonomy missing stock_id column: {SOURCE_TAXONOMY_CSV}")
    taxonomy = normalize_keys(taxonomy)
    wanted = [
        "stock_id",
        "effective_mainstream_label",
        "has_hot_theme",
        "structural_theme_bucket",
        "primary_theme",
        "taxonomy_source",
        "confidence",
    ]
    for column in wanted:
        if column not in taxonomy.columns:
            taxonomy[column] = ""
    taxonomy = taxonomy[wanted].drop_duplicates("stock_id", keep="first")
    taxonomy = taxonomy.rename(columns={"confidence": "taxonomy_confidence"})
    return taxonomy


def read_selected_source() -> pd.DataFrame:
    detail = normalize_keys(read_csv(SOURCE_DETAIL_CSV))
    quality = normalize_keys(read_csv(SOURCE_QUALITY_CSV))
    taxonomy = read_taxonomy()

    required_detail = {
        "stock_id",
        "signal_date",
        "transition_status",
        "slope_curvature_category",
        "a_mature",
        "a_return_pct",
        "c_mature",
        "c_return_pct",
        "approved_for_daily",
    }
    required_quality = {
        "stock_id",
        "signal_date",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "signal_distance_to_neckline_pct",
        "signal_rebound_from_right_low_pct",
        "second_arc_volume_ratio",
        "primary_review_flag",
        "sym1_5_quality_bucket",
    }
    missing_detail = sorted(required_detail - set(detail.columns))
    missing_quality = sorted(required_quality - set(quality.columns))
    if missing_detail:
        raise SystemExit(f"ERROR: path quality detail missing columns: {missing_detail}")
    if missing_quality:
        raise SystemExit(f"ERROR: quality audit missing columns: {missing_quality}")

    selected = detail.merge(taxonomy, on="stock_id", how="left")
    selected = selected[
        selected["transition_status"].eq(TARGET_TRANSITION_STATUS)
        & ~selected["slope_curvature_category"].eq(EXCLUDED_PATH_CATEGORY)
        & selected["effective_mainstream_label"].eq(TARGET_SEGMENT_VALUE)
    ].copy()
    if selected.empty:
        raise SystemExit("ERROR: target core-mainstream exclude-WV selection produced no rows")

    quality_columns = [
        "stock_id",
        "stock_name",
        "signal_date",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "signal_close",
        "neckline_price",
        "right_low_value",
        "signal_distance_to_neckline_pct",
        "signal_rebound_from_right_low_pct",
        "second_arc_volume_ratio",
        "primary_review_flag",
        "sym1_5_quality_bucket",
        "sym1_5_w_shape_completed",
        "sym1_5_completion_date",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_breakout_date",
        "sym1_5_right_low_broken",
        "sym1_5_right_low_broken_date",
    ]
    for column in quality_columns:
        if column not in quality.columns:
            quality[column] = ""
    merged = selected.merge(quality[quality_columns], on=["stock_id", "signal_date"], how="left", suffixes=("", "_quality"))
    if merged["left_peak_date"].astype(str).eq("").any():
        missing = merged.loc[merged["left_peak_date"].astype(str).eq(""), ["stock_id", "signal_date"]]
        raise SystemExit(f"ERROR: selected rows missing quality audit chart fields:\n{missing.to_string(index=False)}")
    return merged.sort_values(["signal_date", "stock_id"]).reset_index(drop=True)


def chart_filename(row: pd.Series) -> str:
    return f"{normalize_date(row.get('signal_date'))}_{normalize_code(row.get('stock_id'))}_{safe_str(row.get('slope_curvature_category'))}.png"


def build_packet(generated_at: str) -> pd.DataFrame:
    source = read_selected_source()
    clean_chart_root()
    rows: list[dict[str, Any]] = []
    for _, source_row in source.iterrows():
        chart_path = CHART_ROOT / chart_filename(source_row)
        draw_chart(source_row, chart_path)
        row = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "source_detail_research_id": SOURCE_DETAIL_RESEARCH_ID,
            "source_quality_research_id": SOURCE_QUALITY_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "segment_dimension": TARGET_SEGMENT_DIMENSION,
            "segment_value": TARGET_SEGMENT_VALUE,
            "filter_id": TARGET_FILTER_ID,
            "transition_status": safe_str(source_row.get("transition_status")),
            "stock_id": normalize_code(source_row.get("stock_id")),
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": normalize_date(source_row.get("signal_date")),
            "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
            "slope_issue_reasons": safe_str(source_row.get("slope_issue_reasons")),
            "path_days": safe_str(source_row.get("path_days")),
            "full_path_significant_turn_count": safe_str(source_row.get("full_path_significant_turn_count")),
            "full_path_direction_switch_count": safe_str(source_row.get("full_path_direction_switch_count")),
            "left_descent_wrong_direction_rate": safe_str(source_row.get("left_descent_wrong_direction_rate")),
            "first_rebound_wrong_direction_rate": safe_str(source_row.get("first_rebound_wrong_direction_rate")),
            "second_decline_wrong_direction_rate": safe_str(source_row.get("second_decline_wrong_direction_rate")),
            "right_rebound_wrong_direction_rate": safe_str(source_row.get("right_rebound_wrong_direction_rate")),
            "left_peak_date": normalize_date(source_row.get("left_peak_date")),
            "left_low_date": normalize_date(source_row.get("left_low_date")),
            "neckline_date": normalize_date(source_row.get("neckline_date")),
            "right_low_date": normalize_date(source_row.get("right_low_date")),
            "signal_close": safe_str(source_row.get("signal_close")),
            "neckline_price": safe_str(source_row.get("neckline_price")),
            "right_low_value": safe_str(source_row.get("right_low_value")),
            "signal_distance_to_neckline_pct": safe_str(source_row.get("signal_distance_to_neckline_pct")),
            "signal_rebound_from_right_low_pct": safe_str(source_row.get("signal_rebound_from_right_low_pct")),
            "second_arc_volume_ratio": safe_str(source_row.get("second_arc_volume_ratio")),
            "primary_review_flag": safe_str(source_row.get("primary_review_flag")),
            "sym1_5_quality_bucket": safe_str(source_row.get("sym1_5_quality_bucket")),
            "sym1_5_w_shape_completed": bool_text(source_row.get("sym1_5_w_shape_completed")),
            "sym1_5_completion_date": normalize_date(source_row.get("sym1_5_completion_date")),
            "sym1_5_neckline_volume_breakout": bool_text(source_row.get("sym1_5_neckline_volume_breakout")),
            "sym1_5_breakout_date": normalize_date(source_row.get("sym1_5_breakout_date")),
            "sym1_5_right_low_broken": bool_text(source_row.get("sym1_5_right_low_broken")),
            "sym1_5_right_low_broken_date": normalize_date(source_row.get("sym1_5_right_low_broken_date")),
            "a_mature": bool_text(source_row.get("a_mature")),
            "a_return_pct": safe_str(source_row.get("a_return_pct")),
            "c_mature": bool_text(source_row.get("c_mature")),
            "c_return_pct": safe_str(source_row.get("c_return_pct")),
            "tdcc_any_age7": bool_text(source_row.get("tdcc_any_age7")),
            "tdcc_any_age14": bool_text(source_row.get("tdcc_any_age14")),
            "effective_mainstream_label": safe_str(source_row.get("effective_mainstream_label")),
            "has_hot_theme": safe_str(source_row.get("has_hot_theme")).lower(),
            "structural_theme_bucket": safe_str(source_row.get("structural_theme_bucket")),
            "primary_theme": safe_str(source_row.get("primary_theme")),
            "taxonomy_source": safe_str(source_row.get("taxonomy_source")),
            "taxonomy_confidence": safe_str(source_row.get("taxonomy_confidence")),
            "chart_path": chart_path.as_posix(),
            "chart_path_absolute": str(chart_path.resolve()),
            "manual_review_status": "pending_user_shape_review",
            "approved_for_daily": "false",
            "production_readiness": "not_production_ready_research_only",
            "generated_at": generated_at,
        }
        rows.append(row)
    index = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in index.columns:
            index[column] = ""
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in review packet: {forbidden}")
    return index[OUTPUT_COLUMNS]


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(index: pd.DataFrame, generated_at: str) -> None:
    matured = index[index["a_mature"].astype(str).str.lower().eq("true")].copy()
    returns = pd.to_numeric(matured["a_return_pct"], errors="coerce").dropna()
    win_count = int(returns.gt(0).sum())
    win_rate = win_count / len(returns) * 100 if len(returns) else 0.0
    avg_return = float(returns.mean()) if len(returns) else 0.0
    median_return = float(returns.median()) if len(returns) else 0.0
    category_counts = (
        index.groupby("slope_curvature_category", dropna=False)
        .size()
        .reset_index(name="candidate_count")
        .sort_values(["slope_curvature_category"])
    )
    sample = index[
        [
            "stock_id",
            "stock_name",
            "signal_date",
            "slope_curvature_category",
            "a_mature",
            "a_return_pct",
            "tdcc_any_age7",
            "structural_theme_bucket",
            "chart_path",
        ]
    ]
    lines = [
        "# W-Bottom Core-Mainstream Exclude-WV Review Packet",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- segment: `{TARGET_SEGMENT_DIMENSION}={TARGET_SEGMENT_VALUE}`",
        f"- filter: `{TARGET_FILTER_ID}`",
        f"- transition_status: `{TARGET_TRANSITION_STATUS}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- candidate_count: `{len(index)}`",
        f"- mature_sample_size: `{len(returns)}`",
        f"- win_rate: `{win_rate:.2f}%`",
        f"- avg_a_return_pct: `{avg_return:.4f}`",
        f"- median_a_return_pct: `{median_return:.4f}`",
        f"- tdcc_any_age7_count: `{int(index['tdcc_any_age7'].astype(str).str.lower().eq('true').sum())}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this packet does not update production model conditions, scoring, ranking, or baseline.",
        "- promotion boundary: `not_production_ready_research_only`; this is a manual chart-review packet for candidate quality.",
        "",
        "## Why This Packet Exists",
        "",
        "The prior WV/WVV stability grid showed the broad `exclude_wv_multiple_turn` filter is not stable enough for production.",
        "The only segment with a useful research lead was `core_mainstream`, so this packet isolates those rows for manual shape review before any further model discussion.",
        "",
        "## Path Category Counts",
        "",
        *markdown_table(category_counts, ["slope_curvature_category", "candidate_count"], limit=20),
        "",
        "## Review Index",
        "",
        *markdown_table(sample, list(sample.columns), limit=30),
        "",
        "## Reading Notes",
        "",
        "- Confirm whether each chart is visually close enough to a real W-bottom path.",
        "- Pay special attention to `sharp_v_bottom_risk` and `slope_break_discontinuous`; they are allowed here only because this packet excludes WV/WVV, not every other path issue.",
        "- `tdcc_any_age7_count=0` means this packet does not prove TDCC support for the W-bottom observation stage.",
        "- Keep this research-only unless a separate promotion PR is explicitly requested.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_packet(generated_at)
    if index.empty:
        raise SystemExit("ERROR: review packet produced no rows")
    write_csv(index, LATEST_INDEX_CSV)
    write_csv(index, HISTORY_INDEX_CSV)
    write_markdown(index, generated_at)
    print(f"Saved: {LATEST_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {LATEST_INDEX_MD}")
    print(f"Saved chart root: {CHART_ROOT}")
    print(f"Saved: {HISTORY_INDEX_CSV} rows={len(index)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
