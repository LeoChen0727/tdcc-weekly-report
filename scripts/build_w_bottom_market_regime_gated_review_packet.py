from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import re
import shutil

import pandas as pd

from build_w_bottom_candidate_chart_review_packet import (
    draw_chart,
    normalize_code,
    normalize_date,
    safe_str,
)
from build_w_bottom_early_entry_stability_audit import load_market_regime_map, segment_specs


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_market_regime_gated_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_market_regime_gated_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_market_regime_gated_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_market_regime_gated_review.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_market_regime_gated_review"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
SOURCE_STABILITY_RESEARCH_ID = "w_bottom_early_entry_stability_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
PARAMETER_SET_ID = "w_bottom_market_regime_gated_review_20260627"
SURFACE_ID = "w_bottom_right_low_early_entry"
EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
OUTCOME_RULE_ID = "tp10_or_neutral_after_5pct_close_40d"

TARGET_SEGMENT_IDS = [
    "smooth_right_rebound_5_20_strong_bull",
    "smooth_right_rebound_5_20_bull",
    "smooth_core_mainstream_right_rebound_5_20_strong_bull",
    "smooth_core_mainstream_right_rebound_5_20_bull",
    "core_mainstream_price_le30_rebound_3_20_volume_red_bull",
]
SEGMENT_FOLDER_CODES = {
    "smooth_right_rebound_5_20_strong_bull": "s01_smooth_rebound_strong",
    "smooth_right_rebound_5_20_bull": "s02_smooth_rebound_bull",
    "smooth_core_mainstream_right_rebound_5_20_strong_bull": "s03_core_smooth_strong",
    "smooth_core_mainstream_right_rebound_5_20_bull": "s04_core_smooth_bull",
    "core_mainstream_price_le30_rebound_3_20_volume_red_bull": "s05_core_low_volred_bull",
}

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
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "source_stability_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "segment_id",
    "segment_description",
    "outcome_bucket",
    "chart_path",
    "chart_path_absolute",
    "stock_id",
    "stock_name",
    "source_signal_date",
    "entry_signal_date",
    "entry_date",
    "entry_open_price",
    "exit_date",
    "exit_close_price",
    "exit_reason",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "neutral_outcome",
    "outcome_result",
    "signal_market_regime",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "signal_close",
    "neckline_price",
    "right_low_price",
    "second_low_gap_pct",
    "signal_rebound_from_right_low_pct",
    "neckline_distance_pct",
    "second_arc_volume_ratio",
    "first_arc_red_ratio_pct",
    "second_arc_red_ratio_pct",
    "red_ratio_delta_pct",
    "price_position_252_pct",
    "price_level_bucket",
    "slope_curvature_category",
    "effective_mainstream_label",
    "has_hot_theme",
    "tdcc_any_age7",
    "tdcc_any_age14",
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


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def bool_text(value: Any) -> str:
    return "true" if safe_str(value).lower() in {"true", "1", "yes", "y"} else "false"


def pct_text(value: float) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.4f}"


def safe_path_part(value: Any) -> str:
    text = safe_str(value)
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text)
    return text.strip("_") or "unknown"


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def source_detail() -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    required = {
        "event_set_id",
        "entry_rule_id",
        "outcome_rule_id",
        "source_signal_date",
        "stock_id",
        "stock_name",
        "outcome_result",
        "return_pct",
        "mature",
        "success",
        "neutral_outcome",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "neckline_price",
        "signal_close",
        "right_low_price",
        "signal_rebound_from_right_low_pct",
        "neckline_distance_pct",
        "second_arc_volume_ratio",
        "red_ratio_delta_pct",
        "price_position_252_pct",
        "price_level_bucket",
        "slope_curvature_category",
        "effective_mainstream_label",
        "has_hot_theme",
        "tdcc_any_age7",
        "tdcc_any_age14",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source detail missing columns: {missing}")
    detail = source[
        source["event_set_id"].eq(EVENT_SET_ID)
        & source["outcome_rule_id"].eq(OUTCOME_RULE_ID)
    ].copy()
    if detail.empty:
        raise SystemExit("ERROR: no rows after event_set/outcome filter")
    detail["stock_id"] = detail["stock_id"].map(normalize_code)
    detail["source_signal_date"] = detail["source_signal_date"].map(normalize_date)
    market_regimes = load_market_regime_map()
    detail["signal_market_regime"] = detail["source_signal_date"].map(lambda date: market_regimes.get(date, "unknown"))
    return detail.reset_index(drop=True)


def segment_map() -> dict[str, tuple[str, Any]]:
    return {segment_id: (description, selector) for segment_id, description, selector in segment_specs()}


def outcome_folder(value: Any) -> str:
    outcome = safe_str(value) or "unknown"
    order = {
        "win": "01_win",
        "neutral": "02_neutral",
        "loss": "03_loss",
        "incomplete": "04_incomplete",
    }
    return order.get(outcome, f"99_{safe_path_part(outcome)}")


def chart_source_row(row: pd.Series) -> pd.Series:
    chart_row = row.copy()
    chart_row["signal_date"] = normalize_date(row.get("source_signal_date"))
    chart_row["signal_distance_to_neckline_pct"] = safe_str(row.get("neckline_distance_pct"))
    chart_row["right_low_value"] = safe_str(row.get("right_low_price"))
    chart_row["primary_review_flag"] = safe_str(row.get("outcome_result"))
    return chart_row


def chart_filename(segment_id: str, row: pd.Series) -> str:
    signal_date = normalize_date(row.get("source_signal_date"))
    stock_id = normalize_code(row.get("stock_id"))
    outcome = safe_path_part(row.get("outcome_result"))
    return f"{signal_date}_{stock_id}_{outcome}.png"


def build_packet(generated_at: str) -> pd.DataFrame:
    detail = source_detail()
    segments = segment_map()
    missing = [segment_id for segment_id in TARGET_SEGMENT_IDS if segment_id not in segments]
    if missing:
        raise SystemExit(f"ERROR: missing target segments from stability specs: {missing}")
    clean_chart_root()
    rows: list[dict[str, Any]] = []
    for segment_id in TARGET_SEGMENT_IDS:
        description, selector = segments[segment_id]
        sample = detail[selector(detail)].copy()
        sample = sample.sort_values(["source_signal_date", "stock_id"]).reset_index(drop=True)
        if sample.empty:
            raise SystemExit(f"ERROR: target segment produced no rows: {segment_id}")
        for _, source_row in sample.iterrows():
            folder = CHART_ROOT / SEGMENT_FOLDER_CODES[segment_id] / outcome_folder(source_row.get("outcome_result"))
            chart_path = folder / chart_filename(segment_id, source_row)
            chart_path.parent.mkdir(parents=True, exist_ok=True)
            draw_chart(chart_source_row(source_row), chart_path)
            row = {
                "model_id": MODEL_ID,
                "confirmation_model_id": CONFIRMATION_MODEL_ID,
                "overlay_model_id": OVERLAY_MODEL_ID,
                "research_id": RESEARCH_ID,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_stability_research_id": SOURCE_STABILITY_RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "surface_id": SURFACE_ID,
                "event_set_id": EVENT_SET_ID,
                "entry_rule_id": safe_str(source_row.get("entry_rule_id")),
                "outcome_rule_id": OUTCOME_RULE_ID,
                "segment_id": segment_id,
                "segment_description": description,
                "outcome_bucket": safe_str(source_row.get("outcome_result")),
                "chart_path": chart_path.as_posix(),
                "chart_path_absolute": str(chart_path.resolve()),
                "stock_id": normalize_code(source_row.get("stock_id")),
                "stock_name": safe_str(source_row.get("stock_name")),
                "source_signal_date": normalize_date(source_row.get("source_signal_date")),
                "entry_signal_date": normalize_date(source_row.get("entry_signal_date")),
                "entry_date": normalize_date(source_row.get("entry_date")),
                "entry_open_price": safe_str(source_row.get("entry_open_price")),
                "exit_date": normalize_date(source_row.get("exit_date")),
                "exit_close_price": safe_str(source_row.get("exit_close_price")),
                "exit_reason": safe_str(source_row.get("exit_reason")),
                "return_pct": safe_str(source_row.get("return_pct")),
                "mature": bool_text(source_row.get("mature")),
                "success": bool_text(source_row.get("success")),
                "positive_return": bool_text(source_row.get("positive_return")),
                "neutral_outcome": bool_text(source_row.get("neutral_outcome")),
                "outcome_result": safe_str(source_row.get("outcome_result")),
                "signal_market_regime": safe_str(source_row.get("signal_market_regime")),
                "left_peak_date": normalize_date(source_row.get("left_peak_date")),
                "left_low_date": normalize_date(source_row.get("left_low_date")),
                "neckline_date": normalize_date(source_row.get("neckline_date")),
                "right_low_date": normalize_date(source_row.get("right_low_date")),
                "signal_close": safe_str(source_row.get("signal_close")),
                "neckline_price": safe_str(source_row.get("neckline_price")),
                "right_low_price": safe_str(source_row.get("right_low_price")),
                "second_low_gap_pct": safe_str(source_row.get("second_low_gap_pct")),
                "signal_rebound_from_right_low_pct": safe_str(source_row.get("signal_rebound_from_right_low_pct")),
                "neckline_distance_pct": safe_str(source_row.get("neckline_distance_pct")),
                "second_arc_volume_ratio": safe_str(source_row.get("second_arc_volume_ratio")),
                "first_arc_red_ratio_pct": safe_str(source_row.get("first_arc_red_ratio_pct")),
                "second_arc_red_ratio_pct": safe_str(source_row.get("second_arc_red_ratio_pct")),
                "red_ratio_delta_pct": safe_str(source_row.get("red_ratio_delta_pct")),
                "price_position_252_pct": safe_str(source_row.get("price_position_252_pct")),
                "price_level_bucket": safe_str(source_row.get("price_level_bucket")),
                "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
                "effective_mainstream_label": safe_str(source_row.get("effective_mainstream_label")),
                "has_hot_theme": safe_str(source_row.get("has_hot_theme")).lower(),
                "tdcc_any_age7": bool_text(source_row.get("tdcc_any_age7")),
                "tdcc_any_age14": bool_text(source_row.get("tdcc_any_age14")),
                "manual_review_status": "pending_user_shape_review",
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
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


def metrics(sample: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(sample.loc[sample["outcome_result"].isin(["win", "neutral", "loss"]), "return_pct"], errors="coerce").dropna()
    mature = sample[sample["outcome_result"].isin(["win", "loss"])].copy()
    stock_counts = sample.groupby("stock_id", dropna=False).size().sort_values(ascending=False)
    max_stock_rows = int(stock_counts.iloc[0]) if len(stock_counts) else 0
    concentration = max_stock_rows / len(sample) * 100 if len(sample) else math.nan
    win_count = int(sample["outcome_result"].eq("win").sum())
    loss_count = int(sample["outcome_result"].eq("loss").sum())
    mature_size = win_count + loss_count
    return {
        "sample_size": len(sample),
        "mature_sample_size": mature_size,
        "win_count": win_count,
        "neutral_count": int(sample["outcome_result"].eq("neutral").sum()),
        "loss_count": loss_count,
        "incomplete_count": int(sample["outcome_result"].eq("incomplete").sum()),
        "win_rate_excl_neutral_pct": win_count / mature_size * 100 if mature_size else math.nan,
        "avg_return_pct": float(returns.mean()) if len(returns) else math.nan,
        "median_return_pct": float(returns.median()) if len(returns) else math.nan,
        "min_return_pct": float(returns.min()) if len(returns) else math.nan,
        "max_return_pct": float(returns.max()) if len(returns) else math.nan,
        "unique_stock_count": int(sample["stock_id"].nunique()),
        "max_rows_single_stock": max_stock_rows,
        "max_single_stock_row_share_pct": concentration,
    }


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(index: pd.DataFrame, generated_at: str) -> None:
    summary_rows: list[dict[str, Any]] = []
    for segment_id, group in index.groupby("segment_id", sort=False):
        row = {"segment_id": segment_id}
        row.update(metrics(group))
        summary_rows.append(row)
    summary = pd.DataFrame(summary_rows)
    for column in [
        "win_rate_excl_neutral_pct",
        "avg_return_pct",
        "median_return_pct",
        "min_return_pct",
        "max_return_pct",
        "max_single_stock_row_share_pct",
    ]:
        summary[column] = pd.to_numeric(summary[column], errors="coerce").map(pct_text)

    sample = index[
        [
            "segment_id",
            "outcome_result",
            "stock_id",
            "stock_name",
            "source_signal_date",
            "return_pct",
            "signal_market_regime",
            "price_position_252_pct",
            "slope_curvature_category",
            "chart_path",
        ]
    ].copy()
    sample = sample.sort_values(["segment_id", "outcome_result", "source_signal_date", "stock_id"])
    lines = [
        "# W-Bottom Market-Regime Gated Review Packet",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- overlay_model_id: `{OVERLAY_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_stability_research_id: `{SOURCE_STABILITY_RESEARCH_ID}`",
        f"- event_set_id: `{EVENT_SET_ID}`",
        f"- outcome_rule_id: `{OUTCOME_RULE_ID}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this packet does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        f"- promotion boundary: `{PRODUCTION_READINESS}`; this is a manual chart-review packet for research-only gated candidates.",
        "",
        "## Why This Packet Exists",
        "",
        "Month grouping is only a sample-distribution check. This packet isolates the market-regime gated W-bottom early-entry candidates so the next review can verify whether the higher win rates are supported by repeatable chart quality or by a few special cases.",
        "",
        "## Segment Summary",
        "",
        *markdown_table(
            summary,
            [
                "segment_id",
                "sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "win_rate_excl_neutral_pct",
                "avg_return_pct",
                "median_return_pct",
                "unique_stock_count",
                "max_rows_single_stock",
                "max_single_stock_row_share_pct",
            ],
            limit=20,
        ),
        "",
        "## Review Index",
        "",
        *markdown_table(sample, list(sample.columns), limit=80),
        "",
        "## Reading Notes",
        "",
        "- Review win, neutral, and loss folders side by side for each segment.",
        "- Do not promote from this packet alone; the better-looking segments still need repeatability beyond the current mature sample.",
        "- `core_mainstream` and market-regime gates are advisory overlays here, not production baseline changes.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_packet(generated_at)
    if index.empty:
        raise SystemExit("ERROR: market-regime gated review packet produced no rows")
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
