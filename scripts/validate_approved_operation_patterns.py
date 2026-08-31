from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_approved_operation_patterns import (  # noqa: E402
    DOCS_CSV,
    DOCS_MD,
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
    OUT_CSV,
    OUT_MD,
    PRICE_PULLBACK_APPROVAL_METRICS,
    PRICE_PULLBACK_APPROVAL_VERSION,
    PRICE_PULLBACK_BUY_FILTER_ID,
    PRICE_PULLBACK_ENTRY_RULE_ID,
    PRICE_PULLBACK_EXIT_RULE_ID,
    PRICE_PULLBACK_MIN_MATURE_SAMPLE_SIZE,
    PRICE_PULLBACK_MIN_WIN_RATE,
    PRICE_PULLBACK_MODEL_ID,
    PRICE_PULLBACK_OPERATION_MODULE_ID,
    PRICE_PULLBACK_SOURCE_RESEARCH_ID,
    PRICE_PULLBACK_SPEC_SOURCE,
    PRICE_PULLBACK_STOP_LOSS_RULE_ID,
    REVENUE_APPROVAL_METRICS,
    REVENUE_APPROVAL_STATUS,
    REVENUE_APPROVAL_VERSION,
    REVENUE_BUY_FILTER_ID,
    REVENUE_ENTRY_RULE_ID,
    REVENUE_EVIDENCE_SOURCE,
    REVENUE_EXIT_RULE_ID,
    REVENUE_MODEL_ID,
    REVENUE_OPERATION_MODULE_ID,
    REVENUE_SOURCE_RESEARCH_ID,
    REVENUE_STOP_LOSS_RULE_ID,
    V2_APPROVAL_METRICS,
    V2_APPROVAL_VERSION,
    V2_ENTRY_RULE_ID,
    V2_EXIT_RULE_ID,
    V2_FORMAL_MODEL_IDS,
    V2_HIGH_MODEL_ID,
    V2_LOW_MODEL_ID,
    V2_MID_MODEL_ID,
    V2_SOURCE_RESEARCH_ID,
    V2_STOP_LOSS_RULE_ID,
    W_BOTTOM_APPROVAL_METRICS,
    W_BOTTOM_APPROVAL_STATUS,
    W_BOTTOM_APPROVAL_VERSION,
    W_BOTTOM_BUY_FILTER_ID,
    W_BOTTOM_ENTRY_RULE_ID,
    W_BOTTOM_EXIT_RULE_ID,
    W_BOTTOM_MIN_MATURE_SAMPLE_SIZE,
    W_BOTTOM_MIN_POSITIVE_RETURN_RATE,
    W_BOTTOM_MODEL_ID,
    W_BOTTOM_OPERATION_MODULE_ID,
    W_BOTTOM_SOURCE_RESEARCH_ID,
    W_BOTTOM_SPEC_SOURCE,
    W_BOTTOM_STOP_LOSS_RULE_ID,
)
from tracking_utils import read_csv, to_number  # noqa: E402
from formal_model_evidence import evidence_pin_for_model  # noqa: E402


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
    "evidence_artifact_version",
    "evidence_canonical_sha256",
    "evidence_pin_source",
}

EXPECTED_APPROVED_MODELS = {
    V2_LOW_MODEL_ID,
    V2_MID_MODEL_ID,
    V2_HIGH_MODEL_ID,
    W_BOTTOM_MODEL_ID,
    NECKLINE_MODEL_ID,
    PRICE_PULLBACK_MODEL_ID,
    REVENUE_MODEL_ID,
}
LEGACY_MODEL_ID = "volume_range_breakout"
LEGACY_HIDDEN_EVIDENCE_BUY_FILTER_ID = "positive_evidence_oos_rank_v1"


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

    legacy_rows = df[df["model_id"].astype(str).eq(LEGACY_MODEL_ID)]
    if not legacy_rows.empty:
        errors.append(f"legacy {LEGACY_MODEL_ID} must not remain approved after v2 split")

    for _, row in df.iterrows():
        model_id = str(row.get("model_id", "")).strip()
        approval_version = str(row.get("approval_version", "")).strip()
        try:
            pin = evidence_pin_for_model(model_id, approval_version)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        expected_pin_fields = {
            "evidence_artifact_version": pin.evidence_version,
            "evidence_canonical_sha256": pin.canonical_sha256,
            "evidence_pin_source": pin.evidence_path,
        }
        for column, expected_value in expected_pin_fields.items():
            if str(row.get(column, "")).strip() != expected_value:
                errors.append(f"{model_id} {column} must match formal evidence pin")

    for model_id in V2_FORMAL_MODEL_IDS:
        rows = df[df["model_id"].astype(str).eq(model_id)]
        if len(rows) != 1:
            errors.append(f"approved operation artifact must contain exactly one {model_id} row")
            continue
        row = rows.iloc[0]
        metrics = V2_APPROVAL_METRICS[model_id]
        expected = {
            "model_id": model_id,
            "operation_module_id": metrics["operation_module_id"],
            "approval_version": metrics.get("approval_version", V2_APPROVAL_VERSION),
            "approved_for_daily": "True",
            "approval_status": "approved_for_daily_v1",
            "operation_directive_level": "approved_daily_operation_guidance",
            "source_research_id": metrics.get("source_research_id", V2_SOURCE_RESEARCH_ID),
            "entry_rule_id": V2_ENTRY_RULE_ID,
            "stop_loss_rule_id": V2_STOP_LOSS_RULE_ID,
            "exit_rule_id": V2_EXIT_RULE_ID,
            "buy_filter_id": metrics["buy_filter_id"],
            "evidence_source_kind": metrics.get("evidence_source_kind", "volume_range_breakout_v2_candidate_bucket_contract"),
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{model_id} {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("best_evidence_sample_size", "")) != metrics["best_evidence_sample_size"]:
            errors.append(f"{model_id} sample size must match v2 contract metrics")
        if str(row.get("best_evidence_win_rate", "")) != metrics["best_evidence_win_rate"]:
            errors.append(f"{model_id} win rate must match v2 contract metrics")
        if str(row.get("volume_v2_neutral_rate_pct", "")) != metrics["best_evidence_neutral_rate"]:
            errors.append(f"{model_id} neutral rate must match v2 contract metrics")
        if str(row.get("volume_v2_loss_rate_pct", "")) != metrics["best_evidence_loss_rate"]:
            errors.append(f"{model_id} loss rate must match v2 contract metrics")
        if str(row.get("volume_v2_avg_return_pct", "")) != metrics["volume_v2_avg_return_pct"]:
            errors.append(f"{model_id} average return must match v2 contract metrics")
        if str(row.get("best_evidence_median_return", "")) != metrics["best_evidence_median_return"]:
            errors.append(f"{model_id} median return must match v2 contract metrics")

    revenue_rows = df[df["model_id"].astype(str).eq(REVENUE_MODEL_ID)]
    if len(revenue_rows) != 1:
        errors.append(
            f"approved operation artifact must contain exactly one {REVENUE_MODEL_ID} row"
        )
    else:
        revenue_row = revenue_rows.iloc[0]
        expected_revenue = {
            "model_id": REVENUE_MODEL_ID,
            "operation_module_id": REVENUE_OPERATION_MODULE_ID,
            "approval_version": REVENUE_APPROVAL_VERSION,
            "approved_for_daily": "True",
            "approval_status": REVENUE_APPROVAL_STATUS,
            "operation_directive_level": "approved_daily_operation_guidance",
            "source_research_id": REVENUE_SOURCE_RESEARCH_ID,
            "entry_rule_id": REVENUE_ENTRY_RULE_ID,
            "stop_loss_rule_id": REVENUE_STOP_LOSS_RULE_ID,
            "exit_rule_id": REVENUE_EXIT_RULE_ID,
            "buy_filter_id": REVENUE_BUY_FILTER_ID,
            "min_sample_size": "0",
            "min_win_rate": "0.0",
            "min_median_return": "0.0",
            "require_out_of_sample_pass": "False",
            "evidence_summary_source": REVENUE_EVIDENCE_SOURCE,
            "evidence_rank_source": REVENUE_EVIDENCE_SOURCE,
            "evidence_source_kind": "frozen_rule_launch_evidence_manifest",
            "best_evidence_sample_size": REVENUE_APPROVAL_METRICS["sample_size"],
            "best_evidence_win_rate": REVENUE_APPROVAL_METRICS["win_rate_pct"],
            "best_evidence_median_return": REVENUE_APPROVAL_METRICS[
                "median_return_pct"
            ],
            "best_evidence_confidence_status": REVENUE_APPROVAL_STATUS,
            "best_evidence_out_of_sample_pass": "unconfirmed",
            "revenue_forward_holdout_status": REVENUE_APPROVAL_METRICS[
                "forward_holdout_status"
            ],
        }
        for col, value in expected_revenue.items():
            if str(revenue_row.get(col, "")) != value:
                errors.append(
                    f"{REVENUE_MODEL_ID} {col} must be {value!r}, "
                    f"got {revenue_row.get(col, '')!r}"
                )
        for col, key in {
            "revenue_sample_size": "sample_size",
            "revenue_win_count": "win_count",
            "revenue_neutral_count": "neutral_count",
            "revenue_failure_count": "failure_count",
            "revenue_win_rate_pct": "win_rate_pct",
            "revenue_neutral_rate_pct": "neutral_rate_pct",
            "revenue_failure_rate_pct": "failure_rate_pct",
            "revenue_avg_return_pct": "avg_return_pct",
            "revenue_median_return_pct": "median_return_pct",
            "revenue_chronological_status": "chronological_status",
            "revenue_transaction_cost_status": "transaction_cost_status",
            "revenue_relative_edge_status": "relative_edge_status",
            "revenue_regime_coverage_status": "regime_coverage_status",
        }.items():
            if str(revenue_row.get(col, "")) != REVENUE_APPROVAL_METRICS[key]:
                errors.append(
                    f"{REVENUE_MODEL_ID} {col} must match frozen launch evidence"
                )

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
        "approval_status": W_BOTTOM_APPROVAL_STATUS,
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
        errors.append("W-bottom approval mature sample size is weaker than the v2 gate")
    if to_number(w_row.get("best_evidence_win_rate")) < W_BOTTOM_MIN_POSITIVE_RETURN_RATE:
        errors.append("W-bottom approval positive-return rate is weaker than the v2 gate")
    if str(w_row.get("w_bottom_positive_return_rate_pct", "")) != W_BOTTOM_APPROVAL_METRICS["positive_return_rate_pct"]:
        errors.append("W-bottom approval positive_return_rate_pct does not match operation spec metrics")
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

    pullback_rows = df[df["model_id"].astype(str).eq(PRICE_PULLBACK_MODEL_ID)]
    if len(pullback_rows) != 1:
        errors.append(f"approved operation artifact must contain exactly one {PRICE_PULLBACK_MODEL_ID} row")
        return errors
    pullback_row = pullback_rows.iloc[0]
    expected_pullback = {
        "model_id": PRICE_PULLBACK_MODEL_ID,
        "operation_module_id": PRICE_PULLBACK_OPERATION_MODULE_ID,
        "approval_version": PRICE_PULLBACK_APPROVAL_VERSION,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "source_research_id": PRICE_PULLBACK_SOURCE_RESEARCH_ID,
        "entry_rule_id": PRICE_PULLBACK_ENTRY_RULE_ID,
        "stop_loss_rule_id": PRICE_PULLBACK_STOP_LOSS_RULE_ID,
        "exit_rule_id": PRICE_PULLBACK_EXIT_RULE_ID,
        "buy_filter_id": PRICE_PULLBACK_BUY_FILTER_ID,
        "evidence_source_kind": "price_pullback_23ema_promoted_operation_spec",
    }
    for col, value in expected_pullback.items():
        if str(pullback_row.get(col, "")) != value:
            errors.append(f"{PRICE_PULLBACK_MODEL_ID} {col} must be {value!r}, got {pullback_row.get(col, '')!r}")
    if not PRICE_PULLBACK_SPEC_SOURCE.exists():
        errors.append(f"missing price pullback operation spec source: {PRICE_PULLBACK_SPEC_SOURCE}")
    if to_number(pullback_row.get("best_evidence_sample_size")) < PRICE_PULLBACK_MIN_MATURE_SAMPLE_SIZE:
        errors.append("price_pullback approval mature sample size is weaker than the v1 gate")
    if to_number(pullback_row.get("best_evidence_win_rate")) < PRICE_PULLBACK_MIN_WIN_RATE:
        errors.append("price_pullback approval win rate is weaker than the v1 gate")
    for col, key in {
        "price_pullback_win_rate_pct": "win_rate_pct",
        "price_pullback_neutral_rate_pct": "neutral_rate_pct",
        "price_pullback_failure_rate_pct": "failure_rate_pct",
        "price_pullback_avg_return_pct": "avg_return_pct",
        "price_pullback_technical_package_win_rate_pct": "technical_package_win_rate_pct",
        "price_pullback_technical_package_avg_return_pct": "technical_package_avg_return_pct",
    }.items():
        if str(pullback_row.get(col, "")) != PRICE_PULLBACK_APPROVAL_METRICS[key]:
            errors.append(f"price_pullback approval {col} does not match promoted operation metrics")

    return errors


def validate_positive_rank_source() -> list[str]:
    errors: list[str] = []
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    if df.empty:
        return errors
    if LEGACY_MODEL_ID in set(df["model_id"].astype(str)):
        errors.append(f"legacy {LEGACY_MODEL_ID} approval row must be removed from approved operation artifact")
    for model_id in V2_FORMAL_MODEL_IDS:
        row = df[df["model_id"].astype(str).eq(model_id)]
        if row.empty:
            errors.append(f"missing v2 approved operation row: {model_id}")
            continue
        evidence_kind = str(row.iloc[0].get("evidence_source_kind", ""))
        expected_kind = V2_APPROVAL_METRICS[model_id].get(
            "evidence_source_kind",
            "volume_range_breakout_v2_candidate_bucket_contract",
        )
        if evidence_kind != expected_kind:
            errors.append(f"{model_id} must use {expected_kind} evidence, got {evidence_kind!r}")
        if str(row.iloc[0].get("buy_filter_id", "")) == LEGACY_HIDDEN_EVIDENCE_BUY_FILTER_ID:
            errors.append(
                f"{model_id} must not reuse legacy hidden evidence "
                f"buy_filter_id={LEGACY_HIDDEN_EVIDENCE_BUY_FILTER_ID}"
            )
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
