from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_high_position_improvement_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    BASE_MODEL_CONDITION_ID,
    BASE_CONDITION_ID,
    BASE_POSITION_BUCKET,
    BASE_SCOPE_ID,
    BASE_SHAPES,
    CANDIDATE_MODEL_ID,
    DETAIL_COLUMNS,
    DOCS_LATEST_CSV,
    DOCS_LATEST_MD,
    HISTORY_CSV,
    HISTORY_DETAIL_CSV,
    LATEST_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    PARENT_MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_RESEARCH_ID,
    SUMMARY_COLUMNS,
    UNIVERSE_CONDITION_ID,
)


FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
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


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def numeric_value(value: object) -> float:
    return float(pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0])


def validate_common(frame: pd.DataFrame, columns: list[str], name: str) -> None:
    if frame.empty:
        fail(f"{name} must not be empty")
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(frame.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} contains forbidden production fields: {forbidden}")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["parent_model_id"].astype(str)) != {PARENT_MODEL_ID}:
        fail(f"{name} parent_model_id must be {PARENT_MODEL_ID}")
    if set(frame["candidate_model_id"].astype(str)) != {CANDIDATE_MODEL_ID}:
        fail(f"{name} candidate_model_id must be {CANDIDATE_MODEL_ID}")
    if set(frame["analysis_scope_id"].astype(str)) != {BASE_SCOPE_ID}:
        fail(f"{name} analysis_scope_id must be {BASE_SCOPE_ID}")
    if set(frame["base_condition_id"].astype(str)) != {BASE_CONDITION_ID}:
        fail(f"{name} base_condition_id must be {BASE_CONDITION_ID}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame) -> None:
    validate_common(detail, DETAIL_COLUMNS, "detail")
    if detail["source_event_key"].duplicated().any():
        fail("detail source_event_key must be unique")
    if set(detail["shape_bucket"].astype(str)) != set(BASE_SHAPES):
        fail("detail must contain exactly high-position candidate shapes")
    if set(detail["return_valid"].astype(str).str.lower()) != {"true"}:
        fail("detail must contain return_valid=True rows only")
    if not set(detail["market_regime"].astype(str)) - {"", "missing"}:
        fail("detail must carry market_regime from raw market rerun")
    if not detail["position_in_120d_range_pct"].map(lambda value: numeric_value(value) > 75).all():
        fail(f"detail must stay in {BASE_POSITION_BUCKET}")
    role_counts = detail["source_scope_role"].astype(str).value_counts().to_dict()
    if role_counts.get("base_model_member", 0) <= 0:
        fail("detail must include base_model_member rows")
    if role_counts.get("reference_universe_only", 0) <= 0:
        fail("detail must keep reference_universe_only rows for before/after audit")
    base_member = detail["base_model_member"].astype(str)
    if set(base_member.unique()) - {"True", "False"}:
        fail("detail base_model_member must be True/False")
    if (detail["source_scope_role"].eq("base_model_member") != detail["base_model_member"].eq("True")).any():
        fail("detail source_scope_role must match base_model_member")
    technical_cols = [
        "signal_open",
        "signal_high",
        "signal_low",
        "signal_close",
        "confirmation_close",
        "signal_close_location_pct",
        "signal_close_location_bucket",
        "signal_body_pct",
        "signal_body_bucket",
        "confirmation_return_pct",
        "confirmation_return_bucket",
        "kd_k_signal",
        "kd_d_signal",
        "kd_j_signal",
        "kd_k_minus_d_signal",
        "kdj_k_signal",
        "kdj_d_signal",
        "kdj_j_signal",
        "kdj_k_minus_d_signal",
        "kdj_phase",
        "kdj_k_bucket",
        "kdj_j_bucket",
        "kd_phase",
        "kd_k_bucket",
        "kd_j_bucket",
        "pdf_add_score_combo_id",
        "pdf_add_score_features",
        "pdf_add_score_count",
    ]
    missing_or_blank = [col for col in technical_cols if col not in detail.columns or not detail[col].astype(str).str.len().gt(0).any()]
    if missing_or_blank:
        fail(f"detail missing technical-analysis evidence columns: {missing_or_blank}")
    if detail["base_model_member"].astype(str).eq("True").any():
        base = detail[detail["base_model_member"].astype(str).eq("True")]
        if base["pdf_add_score_combo_id"].astype(str).eq("").any():
            fail("base_model_member rows must carry pdf_add_score_combo_id")
        if base["pdf_add_score_features"].astype(str).eq("").any():
            fail("base_model_member rows must carry pdf_add_score_features")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_common(summary, SUMMARY_COLUMNS, "summary")
    if not set(summary["candidate_status"].astype(str)) <= {
        "research_only_not_candidate_metric",
        "research_only_positive_return_but_win_below_threshold",
        "research_only_candidate_metric_met",
    }:
        fail("summary candidate_status contains unexpected values")
    if set(summary["sample_count_context"].astype(str)) != {"reported_not_a_disqualifier"}:
        fail("sample_count_context must report sample count without disqualifying")
    if summary["condition_role"].astype(str).str.contains("hidden_gate", case=False, na=False).any():
        allowed = summary["condition_role"].astype(str).str.contains("not_hidden_gate", case=False, na=False)
        if not allowed.all():
            fail("condition_role must not create hidden gates")

    row_counts = summary["row_type"].value_counts().to_dict()
    for required in [
        "reference_universe",
        "baseline",
        "feature_slice",
        "feature_gap",
        "candidate_condition",
        "pdf_bonus_combo",
        "overlap_condition",
    ]:
        if row_counts.get(required, 0) <= 0:
            fail(f"summary missing row_type={required}")
    reference = summary[summary["row_type"].eq("reference_universe")]
    if len(reference) != 1:
        fail("summary must have exactly one reference_universe row")
    ref = reference.iloc[0]
    if ref["feature_id"] != UNIVERSE_CONDITION_ID:
        fail("reference_universe feature_id must preserve the pre-MA60 universe")
    if int(numeric_value(ref["sample_size"])) != len(detail):
        fail("reference_universe sample_size must equal detail row count")

    baseline = summary[summary["row_type"].eq("baseline")]
    if len(baseline) != 1:
        fail("summary must have exactly one baseline row")
    base = baseline.iloc[0]
    base_detail_count = int(detail["base_model_member"].astype(str).eq("True").sum())
    if base["feature_id"] != BASE_MODEL_CONDITION_ID:
        fail("baseline feature_id must be the MA60>MA120 base model")
    if int(numeric_value(base["sample_size"])) != base_detail_count:
        fail("baseline sample_size must equal base_model_member detail row count")
    if base_detail_count >= len(detail):
        fail("baseline must be narrower than the pre-MA60 reference universe")
    if numeric_value(base["win_rate_pct"]) < 60:
        fail("baseline win_rate_pct must stay above the high-position research threshold")

    required_families = {
        "tdcc",
        "market",
        "price_shape_60d",
        "technical",
        "technical_kdj",
        "combo",
        "pdf_bonus_combo",
        "overlap_pair",
    }
    families = set(summary["feature_family"].astype(str))
    missing_families = sorted(required_families - families)
    if missing_families:
        fail(f"summary missing feature families: {missing_families}")

    required_features = {
        UNIVERSE_CONDITION_ID,
        BASE_MODEL_CONDITION_ID,
        "tdcc_any_top20_bool",
        "tdcc_weekly_increase_top20_bool",
        "market_regime_bucket=mild_bull",
        "shape_bucket=wide_range",
        "shape_bucket=non_consolidation",
        "volume_bucket=volume_gt6",
        "signal_close_location_bucket=close_loc_gt95",
        "signal_body_bucket=body_3_7",
        "confirmation_return_bucket=confirm_ret_3_7",
        "confirmation_return_bucket=confirm_ret_gt7",
        "high_pos_base_plus_market_mild_bull",
        "high_pos_base_plus_tdcc_any_top20",
        "high_pos_base_plus_tdcc_weekly_increase_top20",
        "high_pos_base_plus_ma20_gt_ma60",
        "high_pos_base_plus_breakout_2_5",
        "high_pos_base_plus_volume_lt2",
        "high_pos_base_plus_close_location_gt95",
        "high_pos_base_plus_close_location_le80",
        "high_pos_base_plus_signal_body_le3",
        "high_pos_base_plus_confirmation_return_3_7",
        "high_pos_base_plus_kd_bullish_not_overheated",
        "high_pos_base_plus_kd_value_rising_3d",
        "high_pos_base_plus_kd_not_overheated",
        "high_pos_base_plus_kdj_bullish_not_overheated",
        "high_pos_base_plus_kdj_overheated",
        "high_pos_base_plus_kdj_j_gt100",
        "high_pos_base_plus_confirmation_return_gt3",
        "high_pos_base_exclude_volume_gt6",
        "kd_phase=kd_bullish_not_overheated",
        "kdj_phase=kdj_bullish_not_overheated",
        "kd_k_bucket=kd_k_50_80",
        "kdj_k_bucket=kdj_k_50_80",
        "kdj_j_bucket=kdj_j_gt100",
        "add_score_count_ge1",
        "add_score_count_ge2",
        "add_score_count_ge3",
    }
    features = set(summary["feature_id"].astype(str))
    missing_features = sorted(required_features - features)
    if missing_features:
        fail(f"summary missing required high-position features: {missing_features}")

    mild_bull = summary[summary["feature_id"].eq("high_pos_base_plus_market_mild_bull")]
    if len(mild_bull) != 1:
        fail("summary must have exactly one mild_bull add-score row")
    if mild_bull.iloc[0]["condition_role"] != "add_score_research_only_not_hidden_gate":
        fail("mild_bull must remain an add-score research row, not a hidden gate")

    overlap = summary[summary["row_type"].eq("overlap_condition")]
    if overlap.empty:
        fail("summary must include add-score overlap rows")
    if not overlap["condition_role"].astype(str).eq("overlap_research_only_not_hidden_gate").all():
        fail("overlap rows must remain research-only non-gate diagnostics")
    pair_rows = overlap[overlap["feature_family"].eq("overlap_pair")]
    if len(pair_rows) < 5:
        fail("summary must include enough pairwise overlap rows for selected add-score features")

    pdf_combos = summary[summary["row_type"].eq("pdf_bonus_combo")]
    if pdf_combos.empty:
        fail("summary must include PDF exact add-score combo metrics")
    if not pdf_combos["condition_role"].astype(str).eq("pdf_metric_combo_research_only_not_hidden_gate").all():
        fail("PDF exact combo rows must remain research-only non-gate diagnostics")
    if not pdf_combos["feature_id"].astype(str).str.startswith("pdf_combo__").all():
        fail("PDF exact combo feature_id must start with pdf_combo__")
    breakout_body = pdf_combos[
        pdf_combos["feature_id"].astype(str).str.contains("breakout_2_5", regex=False)
        & pdf_combos["feature_id"].astype(str).str.contains("signal_body_le3", regex=False)
    ]
    if breakout_body.empty:
        fail("summary must include an exact PDF combo containing breakout_2_5 and signal_body_le3")

    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "coverage_pct"]:
        vals = pd.to_numeric(summary[col], errors="coerce").dropna()
        if ((vals < 0) | (vals > 100)).any():
            fail(f"{col} out of percentage range")


def validate_mirrors() -> None:
    latest = LATEST_CSV.read_text(encoding="utf-8-sig")
    docs = DOCS_LATEST_CSV.read_text(encoding="utf-8-sig")
    history = HISTORY_CSV.read_text(encoding="utf-8-sig")
    if latest != docs:
        fail("docs latest CSV mirror must equal output latest CSV")
    if latest != history:
        fail("history summary CSV must equal latest CSV for this generated audit")
    latest_detail = LATEST_DETAIL_CSV.read_text(encoding="utf-8-sig")
    history_detail = HISTORY_DETAIL_CSV.read_text(encoding="utf-8-sig")
    if latest_detail != history_detail:
        fail("history detail CSV must equal latest detail CSV for this generated audit")
    if LATEST_MD.read_text(encoding="utf-8") != DOCS_LATEST_MD.read_text(encoding="utf-8"):
        fail("docs latest MD mirror must equal output latest MD")


def main() -> None:
    summary = read_csv(LATEST_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    for path in [DOCS_LATEST_CSV, DOCS_LATEST_MD, HISTORY_CSV, HISTORY_DETAIL_CSV, LATEST_MD]:
        if not path.exists():
            fail(f"missing mirror/output file: {path}")
    validate_detail(detail)
    validate_summary(summary, detail)
    validate_mirrors()
    print(
        "volume_range_breakout_v2_high_position_improvement_audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)}"
    )


if __name__ == "__main__":
    main()
