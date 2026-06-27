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

SOURCE_REVIEW_CSV = RESEARCH_LATEST_DIR / "w_bottom_market_regime_gated_review_latest.csv"
LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_candidate_spec_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_candidate_spec_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_candidate_spec.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_early_entry_candidate_spec"
SOURCE_RESEARCH_ID = "w_bottom_market_regime_gated_review"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
SELECTED_SEGMENT_ID = "smooth_core_mainstream_right_rebound_5_20_bull"

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
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "candidate_model_title_zh",
    "candidate_status",
    "selected_segment_id",
    "selected_segment_definition",
    "scope_boundary",
    "buy_point_definition",
    "sell_and_evaluation_rule",
    "pure_win_rate_definition",
    "neutral_inclusive_success_rate_definition",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "total_sample_win_or_neutral_rate_pct",
    "incomplete_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "unique_stock_count",
    "max_rows_single_stock",
    "max_single_stock_row_share_pct",
    "evidence_line_zh",
    "implementation_note",
    "next_review_focus",
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


def metric_text(value: float, digits: int = 4) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def metrics(sample: pd.DataFrame) -> dict[str, Any]:
    win_count = int(sample["outcome_result"].eq("win").sum())
    neutral_count = int(sample["outcome_result"].eq("neutral").sum())
    loss_count = int(sample["outcome_result"].eq("loss").sum())
    incomplete_count = int(sample["outcome_result"].eq("incomplete").sum())
    sample_size = int(len(sample))
    evaluated_sample_size = win_count + neutral_count + loss_count
    mature_sample_size = win_count + loss_count
    returns = pd.to_numeric(
        sample.loc[sample["outcome_result"].isin(["win", "neutral", "loss"]), "return_pct"],
        errors="coerce",
    ).dropna()
    stock_counts = sample.groupby("stock_id", dropna=False).size().sort_values(ascending=False)
    max_rows_single_stock = int(stock_counts.iloc[0]) if len(stock_counts) else 0
    return {
        "sample_size": sample_size,
        "evaluated_sample_size": evaluated_sample_size,
        "mature_sample_size": mature_sample_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "incomplete_count": incomplete_count,
        "pure_win_rate_pct": win_count / mature_sample_size * 100 if mature_sample_size else math.nan,
        "neutral_inclusive_success_rate_pct": (win_count + neutral_count) / evaluated_sample_size * 100
        if evaluated_sample_size
        else math.nan,
        "total_sample_win_or_neutral_rate_pct": (win_count + neutral_count) / sample_size * 100
        if sample_size
        else math.nan,
        "incomplete_rate_pct": incomplete_count / sample_size * 100 if sample_size else math.nan,
        "avg_return_pct": float(returns.mean()) if len(returns) else math.nan,
        "median_return_pct": float(returns.median()) if len(returns) else math.nan,
        "unique_stock_count": int(sample["stock_id"].nunique()),
        "max_rows_single_stock": max_rows_single_stock,
        "max_single_stock_row_share_pct": max_rows_single_stock / sample_size * 100 if sample_size else math.nan,
    }


def build(generated_at: str) -> pd.DataFrame:
    review = read_csv(SOURCE_REVIEW_CSV)
    required = {
        "segment_id",
        "outcome_result",
        "return_pct",
        "stock_id",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(review.columns))
    if missing:
        raise SystemExit(f"ERROR: source review missing columns: {missing}")
    sample = review[review["segment_id"].eq(SELECTED_SEGMENT_ID)].copy()
    if sample.empty:
        raise SystemExit(f"ERROR: selected segment has no rows: {SELECTED_SEGMENT_ID}")
    if not set(sample["approved_for_daily"].astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: candidate source must remain approved_for_daily=false")
    if set(sample["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        raise SystemExit("ERROR: candidate source must remain research-only")
    metric_row = metrics(sample)
    pure = metric_row["pure_win_rate_pct"]
    inclusive = metric_row["neutral_inclusive_success_rate_pct"]
    evaluated = metric_row["evaluated_sample_size"]
    incomplete = metric_row["incomplete_count"]
    evidence_line = (
        "目前回測：純勝率 "
        f"{pure:.1f}%，含平局成功率 {inclusive:.1f}%，"
        f"已評估 {evaluated} 筆，未成熟 {incomplete} 筆；"
        "買點為右低點觀察訊號後下一交易日開盤，40 個交易日內以收盤 +10% / +5% 平局規則評估。"
    )
    row = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "candidate_model_title_zh": "W底右低點早期進場",
        "candidate_status": "current_best_research_candidate",
        "selected_segment_id": SELECTED_SEGMENT_ID,
        "selected_segment_definition": (
            "Market regime is strong_bull or mild_bull; effective_mainstream_label=core_mainstream; "
            "slope_curvature_category=smooth_rounded_w_like; signal_rebound_from_right_low_pct is 5 to 20."
        ),
        "scope_boundary": (
            "Early-entry only. This does not define W-bottom neckline breakout, inverse head-and-shoulders, "
            "or generic neckline breakout confirmation."
        ),
        "buy_point_definition": "Buy next open after the right-low observation signal.",
        "sell_and_evaluation_rule": (
            "Within 40 trading days after entry: first close return >= +10% is a win; if close return first exceeds "
            "+5% but later returns to <= +5% before +10%, record neutral and exclude it from pure win/loss; "
            "otherwise sell day-40 close and record loss if +10% was not reached."
        ),
        "pure_win_rate_definition": "win_count / (win_count + loss_count); neutral and incomplete are excluded.",
        "neutral_inclusive_success_rate_definition": "(win_count + neutral_count) / (win_count + neutral_count + loss_count); incomplete is excluded.",
        "sample_size": str(metric_row["sample_size"]),
        "evaluated_sample_size": str(metric_row["evaluated_sample_size"]),
        "mature_sample_size": str(metric_row["mature_sample_size"]),
        "win_count": str(metric_row["win_count"]),
        "neutral_count": str(metric_row["neutral_count"]),
        "loss_count": str(metric_row["loss_count"]),
        "incomplete_count": str(metric_row["incomplete_count"]),
        "pure_win_rate_pct": metric_text(metric_row["pure_win_rate_pct"]),
        "neutral_inclusive_success_rate_pct": metric_text(metric_row["neutral_inclusive_success_rate_pct"]),
        "total_sample_win_or_neutral_rate_pct": metric_text(metric_row["total_sample_win_or_neutral_rate_pct"]),
        "incomplete_rate_pct": metric_text(metric_row["incomplete_rate_pct"]),
        "avg_return_pct": metric_text(metric_row["avg_return_pct"]),
        "median_return_pct": metric_text(metric_row["median_return_pct"]),
        "unique_stock_count": str(metric_row["unique_stock_count"]),
        "max_rows_single_stock": str(metric_row["max_rows_single_stock"]),
        "max_single_stock_row_share_pct": metric_text(metric_row["max_single_stock_row_share_pct"]),
        "evidence_line_zh": evidence_line,
        "implementation_note": (
            "signal_rebound_from_right_low_pct means the signal close is 5% to 20% above the detected right-low price; "
            "it is not neckline distance and not realized return."
        ),
        "next_review_focus": (
            "Review chart quality for s03/s04 folders, then optimize buy/sell points; do not promote before a separate "
            "production model-change PR."
        ),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    out = pd.DataFrame([row])
    for column in OUTPUT_COLUMNS:
        if column not in out.columns:
            out[column] = ""
    forbidden = sorted(set(out.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in candidate spec: {forbidden}")
    return out[OUTPUT_COLUMNS]


def write_markdown(spec: pd.DataFrame, generated_at: str) -> None:
    row = spec.iloc[0].to_dict()
    lines = [
        "# W-Bottom Early-Entry Candidate Spec",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- surface_id: `{SURFACE_ID}`",
        f"- candidate_status: `{row['candidate_status']}`",
        f"- selected_segment_id: `{SELECTED_SEGMENT_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this spec does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Boundary",
        "",
        row["scope_boundary"],
        "",
        "This spec is only for the W-bottom right-low early-entry candidate. W-bottom neckline breakout confirmation must be reviewed as a separate model surface.",
        "",
        "## Candidate Conditions",
        "",
        "- Market regime is `strong_bull` or `mild_bull`.",
        "- Stock is `core_mainstream`.",
        "- Path shape is `smooth_rounded_w_like`.",
        "- `signal_rebound_from_right_low_pct` is 5 to 20: the signal close is 5% to 20% above the detected right-low price.",
        "",
        "## Buy / Sell / Evaluation",
        "",
        f"- buy point: {row['buy_point_definition']}",
        f"- sell and evaluation: {row['sell_and_evaluation_rule']}",
        "",
        "## Evidence Line For Model Title",
        "",
        row["evidence_line_zh"],
        "",
        "## Metrics",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| sample_size | {row['sample_size']} |",
        f"| evaluated_sample_size | {row['evaluated_sample_size']} |",
        f"| mature_sample_size | {row['mature_sample_size']} |",
        f"| win_count | {row['win_count']} |",
        f"| neutral_count | {row['neutral_count']} |",
        f"| loss_count | {row['loss_count']} |",
        f"| incomplete_count | {row['incomplete_count']} |",
        f"| pure_win_rate_pct | {row['pure_win_rate_pct']} |",
        f"| neutral_inclusive_success_rate_pct | {row['neutral_inclusive_success_rate_pct']} |",
        f"| total_sample_win_or_neutral_rate_pct | {row['total_sample_win_or_neutral_rate_pct']} |",
        f"| incomplete_rate_pct | {row['incomplete_rate_pct']} |",
        f"| avg_return_pct | {row['avg_return_pct']} |",
        f"| median_return_pct | {row['median_return_pct']} |",
        f"| unique_stock_count | {row['unique_stock_count']} |",
        f"| max_rows_single_stock | {row['max_rows_single_stock']} |",
        f"| max_single_stock_row_share_pct | {row['max_single_stock_row_share_pct']} |",
        "",
        "## Next Review",
        "",
        row["next_review_focus"],
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    spec = build(generated_at)
    write_csv(spec, LATEST_CSV)
    write_csv(spec, HISTORY_CSV)
    write_markdown(spec, generated_at)
    print(f"Saved: {LATEST_CSV} rows={len(spec)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {HISTORY_CSV} rows={len(spec)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
