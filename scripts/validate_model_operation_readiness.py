from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_model_operation_readiness import (  # noqa: E402
    APPROVAL_CSV,
    DAILY_VOLUME_ADAPTER_CSV,
    DOCS_CSV,
    DOCS_MD,
    OUT_CSV,
    OUT_MD,
    PARITY_CSV,
    NECKLINE_MODEL_ID,
    PRICE_PULLBACK_BUY_FILTER_ID,
    PRICE_PULLBACK_CANDIDATE_VERSION,
    PRICE_PULLBACK_MODEL_ID,
    PRICE_PULLBACK_OPERATION_MODULE_ID,
    PRICE_PULLBACK_SPEC_SOURCE,
    VOLUME_MODEL_ID,
    W_BOTTOM_MODEL_ID,
)
from tracking_utils import read_csv  # noqa: E402


REQUIRED_COLUMNS = {
    "model_id",
    "parity_status",
    "blocker",
    "operation_module_status",
    "daily_adapter_status",
    "approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "presentation_allowed",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
    "status_note_zh",
}

APPROVED_MODEL_IDS = {VOLUME_MODEL_ID, W_BOTTOM_MODEL_ID, NECKLINE_MODEL_ID}
PENDING_CANDIDATE_MODEL_IDS = {PRICE_PULLBACK_MODEL_ID}


def as_bool_text(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower()


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [OUT_CSV, OUT_MD, DOCS_CSV, DOCS_MD]:
        if not path.exists():
            errors.append(f"missing model operation readiness artifact: {path}")
    if OUT_CSV.exists() and DOCS_CSV.exists():
        if OUT_CSV.read_text(encoding="utf-8") != DOCS_CSV.read_text(encoding="utf-8"):
            errors.append("docs/latest CSV copy does not match output/latest readiness CSV")
    if OUT_MD.exists() and DOCS_MD.exists():
        if OUT_MD.read_text(encoding="utf-8") != DOCS_MD.read_text(encoding="utf-8"):
            errors.append("docs/latest MD copy does not match output/latest readiness MD")
    return errors


def validate_readiness_csv() -> list[str]:
    errors: list[str] = []
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    if df.empty:
        return [f"empty model operation readiness artifact: {OUT_CSV}"]

    missing_cols = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing_cols:
        return [f"model operation readiness missing columns: {missing_cols}"]

    parity = read_csv(PARITY_CSV, dtype=str).fillna("")
    if parity.empty or "model_id" not in parity.columns:
        errors.append(f"missing parity source for readiness validation: {PARITY_CSV}")
    else:
        parity_ids = set(parity["model_id"].astype(str))
        readiness_ids = set(df["model_id"].astype(str))
        missing = sorted(parity_ids - readiness_ids)
        extra = sorted(readiness_ids - parity_ids)
        if missing:
            errors.append(f"readiness missing parity model_ids: {missing}")
        if extra:
            errors.append(f"readiness has model_ids not in parity artifact: {extra}")

    approved = df[as_bool_text(df["approved_for_daily"]).eq("true")]
    approved_ids = sorted(approved["model_id"].astype(str).tolist())
    if approved_ids != sorted(APPROVED_MODEL_IDS):
        errors.append(f"approved_for_daily=True must be limited to {sorted(APPROVED_MODEL_IDS)}, got {approved_ids}")

    volume = df[df["model_id"].astype(str).eq(VOLUME_MODEL_ID)]
    if len(volume) != 1:
        errors.append(f"readiness must contain exactly one {VOLUME_MODEL_ID} row")
    else:
        row = volume.iloc[0]
        expected = {
            "operation_module_status": "approved_operation_v1",
            "approved_for_daily": "True",
            "approval_status": "approved_for_daily_v1",
            "presentation_allowed": "True",
            "operation_directive_level": "approved_daily_operation_guidance",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "packet_integration_status": "packet_integrated_daily_adapter",
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{VOLUME_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("daily_adapter_status", "")) not in {
            "ready_pending_approval_metadata",
            "ready_approved_operation_guidance",
            "ready_empty_no_operation_rows",
        }:
            errors.append(
                f"{VOLUME_MODEL_ID} daily_adapter_status must be renderable pending/ready/empty adapter metadata, "
                f"got {row.get('daily_adapter_status', '')!r}"
            )
        if not str(row.get("operation_module_id", "")):
            errors.append(f"{VOLUME_MODEL_ID} operation_module_id must be populated")
        if not str(row.get("approval_version", "")):
            errors.append(f"{VOLUME_MODEL_ID} approval_version must be populated")

    w_bottom = df[df["model_id"].astype(str).eq(W_BOTTOM_MODEL_ID)]
    if len(w_bottom) != 1:
        errors.append(f"readiness must contain exactly one {W_BOTTOM_MODEL_ID} row")
    else:
        row = w_bottom.iloc[0]
        expected = {
            "operation_module_status": "approved_operation_v2",
            "daily_adapter_status": "model_header_evidence_ready",
            "approved_for_daily": "True",
            "approval_status": "approved_for_daily_v2",
            "presentation_allowed": "True",
            "operation_directive_level": "approved_daily_operation_guidance",
            "pdf_integration_status": "pdf_model_header_evidence_ready",
            "packet_integration_status": "packet_model_header_evidence_ready",
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{W_BOTTOM_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("operation_module_id", "")) != "w_bottom_early_entry_operation_v2":
            errors.append(f"{W_BOTTOM_MODEL_ID} operation_module_id must be w_bottom_early_entry_operation_v2")
        if str(row.get("approval_version", "")) != "w_bottom_early_entry_operation_v2_20260629":
            errors.append(f"{W_BOTTOM_MODEL_ID} approval_version must be w_bottom_early_entry_operation_v2_20260629")

    neckline = df[df["model_id"].astype(str).eq(NECKLINE_MODEL_ID)]
    if len(neckline) != 1:
        errors.append(f"readiness must contain exactly one {NECKLINE_MODEL_ID} row")
    else:
        row = neckline.iloc[0]
        expected = {
            "operation_module_status": "approved_operation_v1",
            "daily_adapter_status": "model_header_evidence_ready",
            "approved_for_daily": "True",
            "approval_status": "approved_for_daily_v1",
            "presentation_allowed": "True",
            "operation_directive_level": "approved_daily_operation_guidance",
            "pdf_integration_status": "pdf_model_header_evidence_ready",
            "packet_integration_status": "packet_model_header_evidence_ready",
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{NECKLINE_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("operation_module_id", "")) != "neckline_strict_45_signal_90_score_v1":
            errors.append(f"{NECKLINE_MODEL_ID} operation_module_id must be neckline_strict_45_signal_90_score_v1")
        if str(row.get("approval_version", "")) != "neckline_strict_45_signal_90_score_v1_20260629":
            errors.append(f"{NECKLINE_MODEL_ID} approval_version must be neckline_strict_45_signal_90_score_v1_20260629")

    price_pullback = df[df["model_id"].astype(str).eq(PRICE_PULLBACK_MODEL_ID)]
    if len(price_pullback) != 1:
        errors.append(f"readiness must contain exactly one {PRICE_PULLBACK_MODEL_ID} row")
    else:
        row = price_pullback.iloc[0]
        expected = {
            "operation_module_status": "operation_candidate_v1_pending_exact_row_parity",
            "daily_adapter_status": "blocked_exact_daily_row_parity",
            "approved_for_daily": "False",
            "approval_status": "pending_exact_daily_row_parity",
            "operation_module_id": PRICE_PULLBACK_OPERATION_MODULE_ID,
            "approval_version": PRICE_PULLBACK_CANDIDATE_VERSION,
            "presentation_allowed": "False",
            "operation_directive_level": "no_operation_directive",
            "pdf_integration_status": "blocked_exact_daily_row_parity",
            "packet_integration_status": "blocked_exact_daily_row_parity",
            "registry_best_pattern_id": PRICE_PULLBACK_BUY_FILTER_ID,
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{PRICE_PULLBACK_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if not PRICE_PULLBACK_SPEC_SOURCE.exists():
            errors.append(f"missing price pullback operation candidate spec source: {PRICE_PULLBACK_SPEC_SOURCE}")
        if int(float(row.get("registry_best_sample_size", 0) or 0)) < 5000:
            errors.append("price pullback candidate mature sample size is weaker than the v1 candidate gate")
        if float(row.get("registry_best_win_rate", 0) or 0) < 60.0:
            errors.append("price pullback candidate win rate is weaker than the v1 candidate gate")
        if float(row.get("registry_best_median_return", 0) or 0) <= 0.0:
            errors.append("price pullback candidate median D+20 close return must stay positive")

    others = df[~df["model_id"].astype(str).isin(APPROVED_MODEL_IDS | PENDING_CANDIDATE_MODEL_IDS)]
    if not others.empty:
        bad_operation = others[~others["operation_module_status"].eq("baseline_only_no_validated_operation_module")]
        if not bad_operation.empty:
            errors.append(
                "non-volume models must not claim validated operation modules: "
                + ", ".join(bad_operation["model_id"].astype(str).tolist())
            )
        bad_adapter = others[~others["daily_adapter_status"].eq("not_started")]
        if not bad_adapter.empty:
            errors.append(
                "non-volume models must not claim daily adapters: "
                + ", ".join(bad_adapter["model_id"].astype(str).tolist())
            )
        bad_approval = others[as_bool_text(others["approved_for_daily"]).ne("false")]
        if not bad_approval.empty:
            errors.append(
                "non-volume models must not be approved: "
                + ", ".join(bad_approval["model_id"].astype(str).tolist())
            )
        bad_presentation = others[as_bool_text(others["presentation_allowed"]).ne("false")]
        if not bad_presentation.empty:
            errors.append(
                "non-volume models must not be presentation_allowed: "
                + ", ".join(bad_presentation["model_id"].astype(str).tolist())
            )
        bad_directive = others[~others["operation_directive_level"].eq("no_operation_directive")]
        if not bad_directive.empty:
            errors.append(
                "non-volume models must not have operation directive levels: "
                + ", ".join(bad_directive["model_id"].astype(str).tolist())
            )

    return errors


def validate_daily_adapter_boundary() -> list[str]:
    errors: list[str] = []
    adapter = read_csv(DAILY_VOLUME_ADAPTER_CSV, dtype=str).fillna("")
    if adapter.empty:
        return [f"missing daily volume breakout adapter source: {DAILY_VOLUME_ADAPTER_CSV}"]
    if "model_id" not in adapter.columns:
        return [f"daily volume breakout adapter source missing model_id: {DAILY_VOLUME_ADAPTER_CSV}"]
    models = sorted(set(adapter["model_id"].astype(str)))
    if models != [VOLUME_MODEL_ID]:
        errors.append(f"daily volume breakout adapter must contain only {VOLUME_MODEL_ID}, got {models}")
    required_sections = {
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
        "active_operation",
    }
    if "pdf_section" not in adapter.columns:
        errors.append("daily volume breakout adapter missing pdf_section")
    else:
        sections = set(adapter["pdf_section"].astype(str))
        missing_sections = sorted(required_sections - sections)
        if missing_sections:
            errors.append(f"daily volume breakout adapter missing sections: {missing_sections}")
    if {"buy_rank_eligible", "pdf_section", "row_type", "row_action_status"}.issubset(adapter.columns):
        buy_rows = adapter[adapter["buy_rank_eligible"].astype(str).eq("True")]
        bad_buy = buy_rows[
            ~(
                buy_rows["pdf_section"].astype(str).eq("confirmed_operation")
                & buy_rows["row_type"].astype(str).eq("data")
                & buy_rows["row_action_status"].astype(str).eq("confirmed_buy_candidate")
            )
        ]
        if not bad_buy.empty:
            errors.append("buy_rank_eligible=True must be limited to confirmed operation data rows")
    return errors


def validate_approval_source() -> list[str]:
    approval = read_csv(APPROVAL_CSV, dtype=str).fillna("")
    if approval.empty:
        return [f"missing approval source for readiness validation: {APPROVAL_CSV}"]
    approved_ids = set(approval["model_id"].astype(str))
    missing = sorted(APPROVED_MODEL_IDS - approved_ids)
    if missing:
        return [f"approval source missing approved model rows: {missing}"]
    return []


def main() -> int:
    errors = validate_files() + validate_readiness_csv() + validate_daily_adapter_boundary() + validate_approval_source()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    print("model operation readiness validation passed")
    print(f"validated_output={OUT_CSV}")
    print(f"rows={len(df)}")
    print(f"volume_status={df.loc[df['model_id'].eq(VOLUME_MODEL_ID), 'daily_adapter_status'].iloc[0]}")
    print(f"w_bottom_status={df.loc[df['model_id'].eq(W_BOTTOM_MODEL_ID), 'daily_adapter_status'].iloc[0]}")
    print(f"neckline_status={df.loc[df['model_id'].eq(NECKLINE_MODEL_ID), 'daily_adapter_status'].iloc[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
