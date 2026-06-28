from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_EVENTS_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_events_latest.csv"
LATEST_CSV = RESEARCH_LATEST_DIR / "neckline_volume_breakout_candidate_spec_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "neckline_volume_breakout_candidate_spec_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "neckline_volume_breakout_candidate_spec.csv"

MODEL_ID = "neckline_volume_breakout_confirmation"
SOURCE_MODEL_ID = "w_bottom_right_side"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "neckline_volume_breakout_candidate_spec"
SOURCE_RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
NECKLINE_PATTERN_SUBTYPE = "w_bottom"
PRIMARY_SYMMETRY_RATIO = "1.5"

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
    "source_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "neckline_pattern_subtype",
    "candidate_status",
    "segment_id",
    "segment_definition",
    "entry_rule_a",
    "entry_rule_c",
    "exit_rule",
    "future_leakage_warning",
    "sample_size",
    "unique_stock_count",
    "post_confirmation_count",
    "tdcc_any_age7_count",
    "second_arc_ratio_ge_1p5_count",
    "a_evaluated_sample_size",
    "a_win_count",
    "a_loss_count",
    "a_win_rate_pct",
    "a_avg_return_pct",
    "a_median_return_pct",
    "a_stop_signal_low_count",
    "a_fixed_10d_close_count",
    "c_evaluated_sample_size",
    "c_win_count",
    "c_loss_count",
    "c_win_rate_pct",
    "c_avg_return_pct",
    "c_median_return_pct",
    "c_stop_signal_low_count",
    "c_fixed_10d_close_count",
    "evidence_summary",
    "implementation_note",
    "next_review_focus",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class SegmentSpec:
    segment_id: str
    candidate_status: str
    segment_definition: str
    filter_fn: Callable[[pd.DataFrame], pd.Series]
    future_leakage_warning: str


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


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        return float(text)
    except Exception:
        return math.nan


def metric_text(value: float, digits: int = 4) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def true_mask(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def numeric_series(df: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(df[column], errors="coerce")


def base_breakout_sample(events: pd.DataFrame) -> pd.DataFrame:
    required = {
        "model_id",
        "confirmation_model_id",
        "overlay_model_id",
        "research_id",
        "research_variant_id",
        "advisory_status",
        "symmetry_ratio",
        "breakout_date",
        "late_breakout_not_w",
        "second_arc_volume_ratio",
        "tdcc_any_age7",
        "post_confirmation_trigger_id",
        "a_mature",
        "a_return_pct",
        "a_exit_reason",
        "c_mature",
        "c_return_pct",
        "c_exit_reason",
        "approved_for_daily",
        "production_readiness",
        "dedup_20d_eligible",
    }
    missing = sorted(required - set(events.columns))
    if missing:
        raise SystemExit(f"ERROR: source events missing columns: {missing}")
    expected = {
        "model_id": SOURCE_MODEL_ID,
        "confirmation_model_id": MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, value in expected.items():
        values = set(events[column].astype(str))
        if values != {value}:
            raise SystemExit(f"ERROR: source {column} must be {value}; got {sorted(values)}")
    if not false_only(events["approved_for_daily"]):
        raise SystemExit("ERROR: source events must remain approved_for_daily=false")

    sample = events[
        events["breakout_date"].astype(str).ne("")
        & events["symmetry_ratio"].astype(str).eq(PRIMARY_SYMMETRY_RATIO)
        & true_mask(events["dedup_20d_eligible"])
        & ~true_mask(events["late_breakout_not_w"])
    ].copy()
    if sample.empty:
        raise SystemExit("ERROR: source breakout sample is empty")
    sample["second_arc_volume_ratio_num"] = numeric_series(sample, "second_arc_volume_ratio")
    return sample


def segments() -> list[SegmentSpec]:
    return [
        SegmentSpec(
            segment_id="w_bottom_breakout_all_sym1p5",
            candidate_status="tradable_breakout_baseline_research_only",
            segment_definition=(
                "W-bottom neckline volume breakout; symmetry_ratio=1.5; dedup_20d_eligible=true; "
                "late_breakout_not_w=false."
            ),
            filter_fn=lambda df: pd.Series([True] * len(df), index=df.index),
            future_leakage_warning="",
        ),
        SegmentSpec(
            segment_id="w_bottom_breakout_post_confirmation_sym1p5",
            candidate_status="future_filter_leakage_for_a_entry_c_entry_not_improved",
            segment_definition=(
                "Same breakout sample, additionally requiring a post-confirmation trigger after the breakout."
            ),
            filter_fn=lambda df: df["post_confirmation_trigger_id"].astype(str).ne(""),
            future_leakage_warning=(
                "A-entry metrics for this segment are not tradable as a breakout-day rule if the segment requires "
                "a later post-confirmation trigger. Use C-entry metrics for the tradable post-confirmation entry."
            ),
        ),
        SegmentSpec(
            segment_id="w_bottom_breakout_second_arc_ge_1p5_sym1p5",
            candidate_status="comparison_only_research_only",
            segment_definition="Same breakout sample, additionally requiring second_arc_volume_ratio >= 1.5.",
            filter_fn=lambda df: df["second_arc_volume_ratio_num"].ge(1.5),
            future_leakage_warning="",
        ),
        SegmentSpec(
            segment_id="w_bottom_breakout_second_arc_ge_1p5_post_confirmation_sym1p5",
            candidate_status="future_filter_leakage_for_a_entry_c_entry_not_improved",
            segment_definition=(
                "Same breakout sample, requiring second_arc_volume_ratio >= 1.5 and a later post-confirmation trigger."
            ),
            filter_fn=lambda df: df["second_arc_volume_ratio_num"].ge(1.5)
            & df["post_confirmation_trigger_id"].astype(str).ne(""),
            future_leakage_warning=(
                "A-entry metrics for this segment are not tradable as a breakout-day rule if the segment requires "
                "a later post-confirmation trigger. Use C-entry metrics for the tradable post-confirmation entry."
            ),
        ),
        SegmentSpec(
            segment_id="w_bottom_breakout_tdcc_any_age7_sym1p5",
            candidate_status="small_sample_comparison_only",
            segment_definition="Same breakout sample, additionally requiring TDCC signal within 7 days.",
            filter_fn=lambda df: true_mask(df["tdcc_any_age7"]),
            future_leakage_warning="",
        ),
        SegmentSpec(
            segment_id="w_bottom_breakout_second_arc_ge_1p5_tdcc_any_age7_sym1p5",
            candidate_status="small_sample_comparison_only",
            segment_definition=(
                "Same breakout sample, requiring second_arc_volume_ratio >= 1.5 and TDCC signal within 7 days."
            ),
            filter_fn=lambda df: df["second_arc_volume_ratio_num"].ge(1.5) & true_mask(df["tdcc_any_age7"]),
            future_leakage_warning="",
        ),
    ]


def trade_metrics(sample: pd.DataFrame, prefix: str) -> dict[str, Any]:
    mature_col = f"{prefix}_mature"
    return_col = f"{prefix}_return_pct"
    exit_col = f"{prefix}_exit_reason"
    evaluated = sample[true_mask(sample[mature_col])].copy()
    returns = numeric_series(evaluated, return_col).dropna()
    win_count = int((returns > 0).sum()) if len(returns) else 0
    loss_count = int((returns <= 0).sum()) if len(returns) else 0
    exits = evaluated[exit_col].astype(str)
    return {
        f"{prefix}_evaluated_sample_size": int(len(returns)),
        f"{prefix}_win_count": win_count,
        f"{prefix}_loss_count": loss_count,
        f"{prefix}_win_rate_pct": win_count / len(returns) * 100.0 if len(returns) else math.nan,
        f"{prefix}_avg_return_pct": float(returns.mean()) if len(returns) else math.nan,
        f"{prefix}_median_return_pct": float(returns.median()) if len(returns) else math.nan,
        f"{prefix}_stop_signal_low_count": int(exits.eq("stop_signal_low").sum()),
        f"{prefix}_fixed_10d_close_count": int(exits.eq("fixed_10d_close").sum()),
    }


def build(generated_at: str) -> pd.DataFrame:
    events = read_csv(SOURCE_EVENTS_CSV)
    base = base_breakout_sample(events)
    rows: list[dict[str, Any]] = []
    for spec in segments():
        sample = base[spec.filter_fn(base)].copy()
        a_metrics = trade_metrics(sample, "a")
        c_metrics = trade_metrics(sample, "c")
        a_rate = metric_text(float(a_metrics["a_win_rate_pct"]), 1)
        c_rate = metric_text(float(c_metrics["c_win_rate_pct"]), 1)
        row = {
            "model_id": MODEL_ID,
            "source_model_id": SOURCE_MODEL_ID,
            "overlay_model_id": OVERLAY_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "neckline_pattern_subtype": NECKLINE_PATTERN_SUBTYPE,
            "candidate_status": spec.candidate_status,
            "segment_id": spec.segment_id,
            "segment_definition": spec.segment_definition,
            "entry_rule_a": "Buy next open after the neckline volume breakout date.",
            "entry_rule_c": "Buy next open after the selected post-confirmation date when a post-confirmation trigger exists.",
            "exit_rule": "Stop if signal-day low is broken; otherwise sell at the 10th trading-day close.",
            "future_leakage_warning": spec.future_leakage_warning,
            "sample_size": str(len(sample)),
            "unique_stock_count": str(sample["stock_id"].nunique() if "stock_id" in sample.columns else 0),
            "post_confirmation_count": str(int(sample["post_confirmation_trigger_id"].astype(str).ne("").sum())),
            "tdcc_any_age7_count": str(int(true_mask(sample["tdcc_any_age7"]).sum())),
            "second_arc_ratio_ge_1p5_count": str(int(sample["second_arc_volume_ratio_num"].ge(1.5).sum())),
            "evidence_summary": (
                f"A-entry win_rate={a_rate}% over {a_metrics['a_evaluated_sample_size']} evaluated rows; "
                f"C-entry win_rate={c_rate}% over {c_metrics['c_evaluated_sample_size']} evaluated rows."
            ),
            "implementation_note": (
                "This is W-bottom subtype research only. It uses the existing neckline volume breakout replay: "
                "close above neckline with normal volume confirmation or locked-limit-up exception. "
                "It does not define inverse head-and-shoulders or generic neckline breakouts."
            ),
            "next_review_focus": (
                "Do not promote yet. Optimize tradable breakout-day filters, candle-quality penalties, TDCC/revenue "
                "scoring inputs, and sell rules without using future post-confirmation as a breakout-day filter."
            ),
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
        for metric in [a_metrics, c_metrics]:
            for key, value in metric.items():
                row[key] = metric_text(value) if isinstance(value, float) else str(value)
        rows.append(row)

    out = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in out.columns:
            out[column] = ""
    forbidden = sorted(set(out.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in candidate spec: {forbidden}")
    return out[OUTPUT_COLUMNS]


def write_markdown(spec: pd.DataFrame, generated_at: str) -> None:
    lines = [
        "# Neckline Volume Breakout Candidate Spec",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source_model_id: `{SOURCE_MODEL_ID}`",
        f"- neckline_pattern_subtype: `{NECKLINE_PATTERN_SUBTYPE}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this spec does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Boundary",
        "",
        "This candidate spec covers only the W-bottom subtype of `neckline_volume_breakout_confirmation`.",
        "It does not define generic previous-high breakouts, descending-resistance breakouts, inverse head-and-shoulders, or triple-bottom logic.",
        "",
        "## Tradability Warning",
        "",
        "A-entry means buying next open after the breakout date. If a segment requires a later post-confirmation trigger, A-entry metrics use future information and are not tradable as breakout-day evidence.",
        "C-entry means waiting for that later confirmation and then buying next open, so C-entry is the tradable interpretation for post-confirmation segments.",
        "",
        "## Current Conclusion",
        "",
        "The current replay does not yet support promotion to production. The all-breakout A-entry sample is tradable but weak, and the post-confirmation filter improves only the non-tradable A-entry view while the tradable C-entry view does not improve enough.",
        "",
        "## Buy / Sell / Evaluation",
        "",
        "- A-entry: buy next open after the neckline volume breakout date.",
        "- C-entry: buy next open after selected post-confirmation date.",
        "- Exit: stop if signal-day low is broken; otherwise sell at the 10th trading-day close.",
        "- Win rate here means positive close/stop exit return over evaluated rows. It is not the early-entry +10%/+5% rule.",
        "",
        "## Metrics",
        "",
        "| segment_id | status | sample | A evaluated | A win rate | A avg return | C evaluated | C win rate | C avg return | warning |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for _, row in spec.iterrows():
        warning = row["future_leakage_warning"] or ""
        lines.append(
            "| "
            + " | ".join(
                [
                    safe_str(row["segment_id"]),
                    safe_str(row["candidate_status"]),
                    safe_str(row["sample_size"]),
                    safe_str(row["a_evaluated_sample_size"]),
                    safe_str(row["a_win_rate_pct"]),
                    safe_str(row["a_avg_return_pct"]),
                    safe_str(row["c_evaluated_sample_size"]),
                    safe_str(row["c_win_rate_pct"]),
                    safe_str(row["c_avg_return_pct"]),
                    warning,
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Next Review",
            "",
            "Next work should test tradable filters only: signal-day candle quality, false-breakout penalties, TDCC/revenue score inputs, and alternative sell rules. It should not promote this research variant into production baseline without a separate model-change PR.",
        ]
    )
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
