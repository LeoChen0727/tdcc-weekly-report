from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail_latest.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_nm_anchor_chart_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_chart_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_chart_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay_chart_review.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_nearest_micro_anchor_chart_review"
SOURCE_RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"

EXPECTED_COMPARISON_COUNTS = {
    "baseline_only": 216,
    "common": 254,
    "variant_only": 118,
}

EXPECTED_CATEGORY_FOLDERS = {
    "01_v_win",
    "02_v_loss",
    "03_v_pending",
    "04_b_win",
    "05_b_loss",
    "06_b_pending",
    "07_c_win",
    "08_c_loss",
    "09_c_pending",
}

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "comparison_status",
    "selected_event_set_id",
    "outcome_bucket",
    "category_id",
    "category_folder",
    "chart_path",
    "chart_path_absolute",
    "baseline_present",
    "variant_present",
    "baseline_left_peak_date",
    "variant_left_peak_date",
    "baseline_left_low_date",
    "variant_left_low_date",
    "baseline_neckline_date",
    "variant_neckline_date",
    "baseline_right_low_date",
    "variant_right_low_date",
    "baseline_breakout_date",
    "variant_breakout_date",
    "baseline_signal_close",
    "variant_signal_close",
    "baseline_neckline_price",
    "variant_neckline_price",
    "baseline_a_mature",
    "variant_a_mature",
    "baseline_a_return_pct",
    "variant_a_return_pct",
    "baseline_tdcc_any_age7",
    "variant_tdcc_any_age7",
    "variant_left_anchor_rule_id",
    "variant_left_anchor_rule_reason",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
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


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def normalize_code(value: object) -> str:
    text = str(value).replace("\ufeff", "").strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def validate_constants(df: pd.DataFrame, require_approved: bool = False) -> None:
    expected = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, value in expected.items():
        values = set(df[column].astype(str))
        if values != {value}:
            fail(f"{column} must be {value}; got {sorted(values)}")
    if require_approved and not false_only(df["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def validate_index(latest: pd.DataFrame, history: pd.DataFrame, source: pd.DataFrame) -> None:
    validate_constants(latest, require_approved=True)
    validate_constants(history, require_approved=True)
    if len(latest) != len(history):
        fail("latest and history chart review row counts differ")
    if len(latest) != len(source):
        fail(f"chart review row count must match source detail {len(source)}; got {len(latest)}")
    if len(latest) != 588:
        fail(f"chart review row count must remain 588; got {len(latest)}")
    if set(latest["manual_review_status"].astype(str)) != {"pending_user_shape_review"}:
        fail("manual_review_status must remain pending_user_shape_review")
    if not set(latest["baseline_present"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("baseline_present must be true/false")
    if not set(latest["variant_present"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("variant_present must be true/false")
    if not set(latest["selected_event_set_id"].astype(str)).issubset({"baseline", "variant"}):
        fail("selected_event_set_id must be baseline/variant")
    if not set(latest["outcome_bucket"].astype(str)).issubset({"win", "loss", "pending_or_no_breakout"}):
        fail("outcome_bucket has unexpected values")

    comparison_counts = latest["comparison_status"].value_counts().to_dict()
    for status, expected in EXPECTED_COMPARISON_COUNTS.items():
        actual = int(comparison_counts.get(status, 0))
        if actual != expected:
            fail(f"{status} count must remain {expected}; got {actual}")

    source_keys = set(zip(source["stock_id"].map(normalize_code), source["signal_date"].astype(str)))
    latest_keys = set(zip(latest["stock_id"].map(normalize_code), latest["signal_date"].astype(str)))
    if source_keys != latest_keys:
        fail("chart review keys must match source detail keys")

    if latest[latest["comparison_status"].eq("baseline_only")]["selected_event_set_id"].ne("baseline").any():
        fail("baseline_only rows must select baseline event set")
    non_baseline = latest[~latest["comparison_status"].eq("baseline_only")]
    if non_baseline["selected_event_set_id"].ne("variant").any():
        fail("common and variant_only rows must select variant event set")


def validate_charts(index: pd.DataFrame) -> None:
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")
    folders = {path.name for path in CHART_ROOT.iterdir() if path.is_dir()}
    if folders != EXPECTED_CATEGORY_FOLDERS:
        fail(f"chart folders mismatch: {sorted(folders)}")
    png_paths = list(CHART_ROOT.glob("*/*.png"))
    if len(png_paths) != len(index):
        fail(f"PNG chart count must equal index rows {len(index)}; got {len(png_paths)}")
    for _, row in index.iterrows():
        chart_path = Path(row.get("chart_path", ""))
        if not chart_path.exists():
            fail(f"missing chart path from index: {chart_path}")
        if chart_path.suffix.lower() != ".png":
            fail(f"chart path must be png: {chart_path}")
        if chart_path.stat().st_size < 10_000:
            fail(f"chart file looks too small/non-rendered: {chart_path}")


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    source = read_csv(SOURCE_DETAIL_CSV)
    if not LATEST_INDEX_MD.exists():
        fail(f"missing required markdown file: {LATEST_INDEX_MD}")
    missing_latest = sorted(REQUIRED_COLUMNS - set(latest.columns))
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_latest:
        fail(f"{LATEST_INDEX_CSV} missing columns: {missing_latest}")
    if missing_history:
        fail(f"{HISTORY_INDEX_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"chart review packet must not emit production decision fields: {forbidden}")

    source["stock_id"] = source["stock_id"].map(normalize_code)
    source["signal_date"] = source["signal_date"].astype(str).str.strip()
    validate_index(latest, history, source)
    validate_charts(latest)

    md = LATEST_INDEX_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "variant_only",
        "baseline_only",
        "common",
        "Baseline markers are dashed",
        "manual shape-review packet only",
    ]
    for text in required_text:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    print(
        "W-bottom nearest-micro anchor chart review packet validation passed "
        f"charts={len(latest)} chart_root={CHART_ROOT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
