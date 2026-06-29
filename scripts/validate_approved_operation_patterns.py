from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_approved_operation_patterns import (  # noqa: E402
    BUY_FILTER_ID,
    DOCS_CSV,
    DOCS_MD,
    ENTRY_RULE_ID,
    EXIT_RULE_ID,
    MIN_MEDIAN_RETURN,
    MIN_RESEARCH_SCORE,
    MIN_SAMPLE_SIZE,
    MIN_WIN_RATE,
    MODEL_ID,
    NECKLINE_APPROVAL_METRICS,
    NECKLINE_APPROVAL_VERSION,
    NECKLINE_BUY_FILTER_ID,
    NECKLINE_ENTRY_RULE_ID,
    NECKLINE_EXIT_RULE_ID,
    NECKLINE_MIN_MATURE_SAMPLE_SIZE,
    NECKLINE_MIN_NEUTRAL_INCLUSIVE_SUCCESS_RATE,
    NECKLINE_MIN_PURE_WIN_RATE,
    NECKLINE_MODEL_ID,
    NECKLINE_OPERATION_MODULE_ID,
    NECKLINE_SOURCE_RESEARCH_ID,
    NECKLINE_SPEC_SOURCE,
    NECKLINE_STOP_LOSS_RULE_ID,
    OPERATION_MODULE_ID,
    OUT_CSV,
    OUT_MD,
    STOP_LOSS_RULE_ID,
    W_BOTTOM_APPROVAL_METRICS,
    W_BOTTOM_APPROVAL_VERSION,
    W_BOTTOM_BUY_FILTER_ID,
    W_BOTTOM_ENTRY_RULE_ID,
    W_BOTTOM_EXIT_RULE_ID,
    W_BOTTOM_MIN_MATURE_SAMPLE_SIZE,
    W_BOTTOM_MIN_NEUTRAL_INCLUSIVE_SUCCESS_RATE,
    W_BOTTOM_MIN_PURE_WIN_RATE,
    W_BOTTOM_MODEL_ID,
    W_BOTTOM_OPERATION_MODULE_ID,
    W_BOTTOM_SOURCE_RESEARCH_ID,
    W_BOTTOM_SPEC_SOURCE,
    W_BOTTOM_STOP_LOSS_RULE_ID,
    positive_rank_rows,
)
from tracking_utils import read_csv, to_number  # noqa: E402


REQUIRED_COLUMNS = {
    "model_id",
    "operation_module_id",
    "approval_version",
    "approved_for_daily",
    "approval_status",
    "operation_directive_level",
    "entry_rule_id",
    "stop_loss_rule_id",
    "exit_rule_id",
    "buy_filter_id",
    "min_sample_size",
    "min_win_rate",
    "min_median_return",
    "require_out_of_sample_pass",
    "min_research_score",
    "evidence_rank_source",
    "evidence_source_kind",
    "evidence_total_rank_rows",
    "evidence_positive_rank_rows",
    "risk_notes_zh",
}

EXPECTED_APPROVED_MODELS = {MODEL_ID, W_BOTTOM_MODEL_ID, NECKLINE_MODEL_ID}


def bool_text(value: object) -> str:
    return str(value).strip().lower()


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [OUT_CSV, OUT_MD, DOCS_CSV, DOCS_MD]:
        if not path.exists():
            errors.append(f"missing approved operation artifact: {path}")
    if OUT_CSV.exists() and DOCS_CSV.exists() and OUT_CSV.read_text(encoding="utf-8") != DOCS_CSV.read_text(encoding="utf-8"):
        errors.append("docs/latest CSV copy does not match output/latest approved operation CSV")
    if OUT_MD.exists() and DOCS_MD.exists() and OUT_MD.read_text(encoding="utf-8") != DOCS_MD.read_text(encoding="utf-8"):
        errors.append("docs/latest MD copy does not match output/latest approved operation MD")
    return errors


def validate_approval() -> list[str]:
    errors: list[str] = []
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    if df.empty:
        return [f"empty approved operation artifact: {OUT_CSV}"]
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        return [f"approved operation artifact missing columns: {missing}"]
    approved_models = set(df["model_id"].astype(str))
    missing_models = sorted(EXPECTED_APPROVED_MODELS - approved_models)
    extra_models = sorted(approved_models - EXPECTED_APPROVED_MODELS)
    if missing_models:
        errors.append(f"approved operation artifact missing approved models: {missing_models}")
    if extra_models:
        errors.append(f"approved operation artifact has unexpected models: {extra_models}")

    volume_rows = df[df["model_id"].astype(str).eq(MODEL_ID)]
    if len(volume_rows) != 1:
        errors.append(f"approved operation artifact must contain exactly one {MODEL_ID} row")
        return errors
    row = volume_rows.iloc[0]
    expected = {
        "model_id": MODEL_ID,
        "operation_module_id": OPERATION_MODULE_ID,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "entry_rule_id": ENTRY_RULE_ID,
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "buy_filter_id": BUY_FILTER_ID,
        "require_out_of_sample_pass": "True",
    }
    for col, value in expected.items():
        if str(row.get(col, "")) != value:
            errors.append(f"{col} must be {value!r}, got {row.get(col, '')!r}")

    if to_number(row.get("min_sample_size")) < MIN_SAMPLE_SIZE:
        errors.append("approval min_sample_size is weaker than the v1 gate")
    if to_number(row.get("min_win_rate")) < MIN_WIN_RATE:
        errors.append("approval min_win_rate is weaker than the v1 gate")
    if to_number(row.get("min_median_return")) < MIN_MEDIAN_RETURN:
        errors.append("approval min_median_return is weaker than the v1 gate")
    if to_number(row.get("min_research_score")) < MIN_RESEARCH_SCORE:
        errors.append("approval min_research_score is weaker than the v1 gate")
    if int(to_number(row.get("evidence_positive_rank_rows"), 0)) <= 0:
        errors.append("approval must have at least one positive confirmed rank row")

    w_rows = df[df["model_id"].astype(str).eq(W_BOTTOM_MODEL_ID)]
    if len(w_rows) != 1:
        errors.append(f"approved operation artifact must contain exactly one {W_BOTTOM_MODEL_ID} row")
        return errors
    w_row = w_rows.iloc[0]
    expected_w = {
        "model_id": W_BOTTOM_MODEL_ID,
        "operation_module_id": W_BOTTOM_OPERATION_MODULE_ID,
        "approval_version": W_BOTTOM_APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": W_BOTTOM_SOURCE_RESEARCH_ID,
        "entry_rule_id": W_BOTTOM_ENTRY_RULE_ID,
        "stop_loss_rule_id": W_BOTTOM_STOP_LOSS_RULE_ID,
        "exit_rule_id": W_BOTTOM_EXIT_RULE_ID,
        "buy_filter_id": W_BOTTOM_BUY_FILTER_ID,
        "evidence_source_kind": "w_bottom_early_entry_operation_spec",
    }
    for col, value in expected_w.items():
        if str(w_row.get(col, "")) != value:
            errors.append(f"{W_BOTTOM_MODEL_ID} {col} must be {value!r}, got {w_row.get(col, '')!r}")
    if not W_BOTTOM_SPEC_SOURCE.exists():
        errors.append(f"missing W-bottom operation spec source: {W_BOTTOM_SPEC_SOURCE}")
    if to_number(w_row.get("best_evidence_sample_size")) < W_BOTTOM_MIN_MATURE_SAMPLE_SIZE:
        errors.append("W-bottom approval mature sample size is weaker than the v1 gate")
    if to_number(w_row.get("best_evidence_win_rate")) < W_BOTTOM_MIN_PURE_WIN_RATE:
        errors.append("W-bottom approval pure win rate is weaker than the v1 gate")
    if to_number(w_row.get("w_bottom_neutral_inclusive_success_rate_pct")) < W_BOTTOM_MIN_NEUTRAL_INCLUSIVE_SUCCESS_RATE:
        errors.append("W-bottom approval inclusive success rate is weaker than the v1 gate")
    if str(w_row.get("w_bottom_win_count", "")) != W_BOTTOM_APPROVAL_METRICS["win_count"]:
        errors.append("W-bottom approval win_count does not match operation spec metrics")
    if str(w_row.get("w_bottom_neutral_count", "")) != W_BOTTOM_APPROVAL_METRICS["neutral_count"]:
        errors.append("W-bottom approval neutral_count does not match operation spec metrics")
    if str(w_row.get("w_bottom_loss_count", "")) != W_BOTTOM_APPROVAL_METRICS["loss_count"]:
        errors.append("W-bottom approval loss_count does not match operation spec metrics")

    neckline_rows = df[df["model_id"].astype(str).eq(NECKLINE_MODEL_ID)]
    if len(neckline_rows) != 1:
        errors.append(f"approved operation artifact must contain exactly one {NECKLINE_MODEL_ID} row")
        return errors
    neckline_row = neckline_rows.iloc[0]
    expected_neckline = {
        "model_id": NECKLINE_MODEL_ID,
        "operation_module_id": NECKLINE_OPERATION_MODULE_ID,
        "approval_version": NECKLINE_APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": NECKLINE_SOURCE_RESEARCH_ID,
        "entry_rule_id": NECKLINE_ENTRY_RULE_ID,
        "stop_loss_rule_id": NECKLINE_STOP_LOSS_RULE_ID,
        "exit_rule_id": NECKLINE_EXIT_RULE_ID,
        "buy_filter_id": NECKLINE_BUY_FILTER_ID,
        "evidence_source_kind": "neckline_strict_45_signal_90_score_operation_spec",
    }
    for col, value in expected_neckline.items():
        if str(neckline_row.get(col, "")) != value:
            errors.append(f"{NECKLINE_MODEL_ID} {col} must be {value!r}, got {neckline_row.get(col, '')!r}")
    if not NECKLINE_SPEC_SOURCE.exists():
        errors.append(f"missing neckline operation spec source: {NECKLINE_SPEC_SOURCE}")
    if to_number(neckline_row.get("best_evidence_sample_size")) < NECKLINE_MIN_MATURE_SAMPLE_SIZE:
        errors.append("neckline approval mature sample size is weaker than the v1 gate")
    if to_number(neckline_row.get("best_evidence_win_rate")) < NECKLINE_MIN_PURE_WIN_RATE:
        errors.append("neckline approval pure win rate is weaker than the v1 gate")
    if to_number(neckline_row.get("neckline_neutral_inclusive_success_rate_pct")) < NECKLINE_MIN_NEUTRAL_INCLUSIVE_SUCCESS_RATE:
        errors.append("neckline approval inclusive success rate is weaker than the v1 gate")
    if str(neckline_row.get("neckline_win_count", "")) != NECKLINE_APPROVAL_METRICS["win_count"]:
        errors.append("neckline approval win_count does not match operation spec metrics")
    if str(neckline_row.get("neckline_neutral_count", "")) != NECKLINE_APPROVAL_METRICS["neutral_count"]:
        errors.append("neckline approval neutral_count does not match operation spec metrics")
    if str(neckline_row.get("neckline_loss_count", "")) != NECKLINE_APPROVAL_METRICS["loss_count"]:
        errors.append("neckline approval loss_count does not match operation spec metrics")
    if str(neckline_row.get("neckline_filter90_auto_bearish_confirmed_count", "")) != NECKLINE_APPROVAL_METRICS["filter90_auto_bearish_confirmed_count"]:
        errors.append("neckline approval must retain 90d bearish rows as score-only evidence")

    return errors


def validate_positive_rank_source() -> list[str]:
    errors: list[str] = []
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    if df.empty:
        return errors
    volume_rows = df[df["model_id"].astype(str).eq(MODEL_ID)]
    if volume_rows.empty:
        return [f"approval source must contain {MODEL_ID}: {OUT_CSV}"]
    row = volume_rows.iloc[0]
    source = Path("output/latest") / str(row.get("evidence_rank_source", ""))
    rank = read_csv(source, dtype=str).fillna("")
    if rank.empty:
        return [f"missing approval evidence rank source: {source}"]
    positive = positive_rank_rows(rank)
    expected_count = int(to_number(row.get("evidence_positive_rank_rows"), 0))
    if len(positive) != expected_count:
        errors.append(f"positive rank row count mismatch: artifact={expected_count}, recomputed={len(positive)}")
    if not positive.empty and "approved_for_daily" in positive.columns:
        raw_approved = set(positive["approved_for_daily"].astype(str).str.lower())
        if raw_approved != {"false"}:
            errors.append(f"raw rank rows should remain research evidence rows, got approved_for_daily={sorted(raw_approved)}")
    return errors


def main() -> int:
    errors = validate_files() + validate_approval() + validate_positive_rank_source()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    print("approved operation pattern validation passed")
    print(f"validated_output={OUT_CSV}")
    print(f"approved_models={df['model_id'].tolist()}")
    print(f"operation_module_ids={df['operation_module_id'].tolist()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
