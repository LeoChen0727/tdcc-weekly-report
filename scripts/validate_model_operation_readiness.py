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
    VOLUME_MODEL_ID,
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
    if approved_ids != [VOLUME_MODEL_ID]:
        errors.append(f"only {VOLUME_MODEL_ID} may currently be approved_for_daily=True, got {approved_ids}")

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
        }:
            errors.append(
                f"{VOLUME_MODEL_ID} daily_adapter_status must be pending/ready approved metadata, "
                f"got {row.get('daily_adapter_status', '')!r}"
            )
        if not str(row.get("operation_module_id", "")):
            errors.append(f"{VOLUME_MODEL_ID} operation_module_id must be populated")
        if not str(row.get("approval_version", "")):
            errors.append(f"{VOLUME_MODEL_ID} approval_version must be populated")

    others = df[~df["model_id"].astype(str).eq(VOLUME_MODEL_ID)]
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
    if "adapter_note_zh" in adapter.columns:
        joined = " ".join(adapter["adapter_note_zh"].astype(str).head(10).tolist())
        if "must not recalculate operation rules" not in joined:
            errors.append("daily adapter note must state that PDF renderers must not recalculate operation rules")
    return errors


def validate_approval_source() -> list[str]:
    approval = read_csv(APPROVAL_CSV, dtype=str).fillna("")
    if approval.empty:
        return [f"missing approval source for readiness validation: {APPROVAL_CSV}"]
    approved = approval[approval["model_id"].astype(str).eq(VOLUME_MODEL_ID)]
    if approved.empty:
        return [f"approval source must contain {VOLUME_MODEL_ID}: {APPROVAL_CSV}"]
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
