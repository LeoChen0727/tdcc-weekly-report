from __future__ import annotations

# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
import csv
import hashlib
import io
import json
import subprocess
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
import sys
from pathlib import Path

import pandas as pd

# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
ROOT = Path(__file__).resolve().parents[1]
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_model_operation_readiness import (  # noqa: E402
    APPROVAL_CSV,
    DAILY_NECKLINE_ADAPTER_CSV,
    DAILY_PRICE_PULLBACK_ADAPTER_CSV,
    DAILY_VOLUME_ADAPTER_CSV,
    DAILY_W_BOTTOM_ADAPTER_CSV,
    DOCS_CSV,
    DOCS_MD,
    OUT_CSV,
    OUT_MD,
    PARITY_CSV,
    NECKLINE_MODEL_ID,
    PRICE_PULLBACK_BUY_FILTER_ID,
    PRICE_PULLBACK_CANDIDATE_VERSION,
    PRICE_PULLBACK_DAILY_ROW_PARITY_CSV,
    PRICE_PULLBACK_MODEL_ID,
    PRICE_PULLBACK_OPERATION_MODULE_ID,
    PRICE_PULLBACK_SPEC_SOURCE,
    V2_HIGH_MODEL_ID,
    V2_LOW_MODEL_ID,
    V2_MID_MODEL_ID,
    V2_VOLUME_MODEL_IDS,
    W_BOTTOM_MODEL_ID,
)
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
from sync_revenue_unreacted_range_operation_readiness import (  # noqa: E402
    REVENUE_ANOMALY_REGISTRY_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV,
    REVENUE_MODEL_ID,
    REVENUE_PROMOTION_REGISTRY_CSV,
    REVENUE_SOURCE_PROJECTION_MANIFEST_CSV,
    summarize_revenue_promotion_readiness,
    validate_revenue_readiness_source_files,
)
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
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
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
REVENUE_PERMISSION_COLUMNS = {
    "formal_model_use_allowed",
    "production_allowed",
}
LEGACY_BOOTSTRAP_BASE_SHA = "7b05900722aa57df2271d8025da07aa0f81b74e0"
LEGACY_BOOTSTRAP_BLOB_IDS = {
    "output/latest/model_operation_readiness_latest.csv": (
        "eb60dc3f9852be994874e830d4c0e79cc3736ec5"
    ),
    "output/latest/model_operation_readiness_latest.md": (
        "108b744f3b4371ee7fa19edbe872a6d563af2a5b"
    ),
    "docs/latest/model_operation_readiness_latest.csv": (
        "eb60dc3f9852be994874e830d4c0e79cc3736ec5"
    ),
    "docs/latest/model_operation_readiness_latest.md": (
        "108b744f3b4371ee7fa19edbe872a6d563af2a5b"
    ),
}
LEGACY_BOOTSTRAP_CANONICAL_SHA256 = {
    "output/latest/model_operation_readiness_latest.csv": (
        "c84488e3878427fdf747b32de6aa0461039c15561980a0f82468aa4a384e972b"
    ),
    "output/latest/model_operation_readiness_latest.md": (
        "569851bc29f270c4115d7176cec97dedf679109877855d22815063c136e725a1"
    ),
    "docs/latest/model_operation_readiness_latest.csv": (
        "c84488e3878427fdf747b32de6aa0461039c15561980a0f82468aa4a384e972b"
    ),
    "docs/latest/model_operation_readiness_latest.md": (
        "569851bc29f270c4115d7176cec97dedf679109877855d22815063c136e725a1"
    ),
}
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

APPROVED_MODEL_IDS = {
    V2_LOW_MODEL_ID,
    V2_MID_MODEL_ID,
    V2_HIGH_MODEL_ID,
    W_BOTTOM_MODEL_ID,
    NECKLINE_MODEL_ID,
    PRICE_PULLBACK_MODEL_ID,
}
LEGACY_VOLUME_MODEL_ID = "volume_range_breakout"
PENDING_CANDIDATE_MODEL_IDS: set[str] = set()
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
PENDING_CANDIDATE_MODEL_IDS.add(REVENUE_MODEL_ID)
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def as_bool_text(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower()


# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
def _canonical_readiness_artifact_sha256(
    logical_path: str,
    data: bytes,
) -> str:
    if logical_path.endswith(".csv"):
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")))
        if not reader.fieldnames:
            raise ValueError("missing CSV header")
        rows = list(reader)
        if any(None in row for row in rows):
            raise ValueError("CSV row has more values than the header")
        canonical = json.dumps(
            {"fieldnames": reader.fieldnames, "rows": rows},
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    else:
        canonical = (
            data.decode("utf-8-sig")
            .replace("\r\n", "\n")
            .encode("utf-8")
        )
    return hashlib.sha256(canonical).hexdigest()


def _filtered_git_blob_id(logical_path: str, data: bytes) -> str:
    normalized_data = data.replace(b"\r\n", b"\n")
    result = subprocess.run(
        [
            "git",
            "-c",
            "core.autocrlf=false",
            "hash-object",
            f"--path={logical_path}",
            "--stdin",
        ],
        cwd=ROOT,
        input=normalized_data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            result.stderr.decode("utf-8", errors="replace").strip()
        )
    return result.stdout.decode("ascii", errors="strict").strip()


def _legacy_readiness_paths() -> dict[str, Path]:
    return {
        "output/latest/model_operation_readiness_latest.csv": OUT_CSV,
        "output/latest/model_operation_readiness_latest.md": OUT_MD,
        "docs/latest/model_operation_readiness_latest.csv": DOCS_CSV,
        "docs/latest/model_operation_readiness_latest.md": DOCS_MD,
    }


def validate_legacy_readiness_bootstrap_artifacts() -> list[str]:
    errors: list[str] = []
    for logical_path, path in _legacy_readiness_paths().items():
        try:
            data = path.read_bytes()
            filtered_blob_id = _filtered_git_blob_id(logical_path, data)
            canonical_sha256 = _canonical_readiness_artifact_sha256(
                logical_path,
                data,
            )
        except (OSError, RuntimeError, UnicodeDecodeError, ValueError) as exc:
            errors.append(
                f"legacy readiness bootstrap cannot inspect {logical_path}: {exc}"
            )
            continue
        expected_blob_id = LEGACY_BOOTSTRAP_BLOB_IDS[logical_path]
        if filtered_blob_id != expected_blob_id:
            errors.append(
                "legacy readiness bootstrap filtered Git blob drift: "
                f"{logical_path}; expected={expected_blob_id}; "
                f"actual={filtered_blob_id}"
            )
        expected_canonical = LEGACY_BOOTSTRAP_CANONICAL_SHA256[logical_path]
        if canonical_sha256 != expected_canonical:
            errors.append(
                "legacy readiness bootstrap canonical semantic drift: "
                f"{logical_path}; expected={expected_canonical}; "
                f"actual={canonical_sha256}"
            )
    return errors


def validate_persisted_revenue_permission_columns(
    readiness: pd.DataFrame,
) -> list[str]:
    errors: list[str] = []
    missing_permissions = sorted(
        REVENUE_PERMISSION_COLUMNS - set(readiness.columns)
    )
    if missing_permissions:
        return [
            "model operation readiness is missing revenue permission columns: "
            f"{missing_permissions}"
        ]

    for source_field in ("approved_for_daily", "presentation_allowed"):
        invalid_source = readiness[
            ~readiness[source_field].astype(str).isin({"True", "False"})
        ]
        if not invalid_source.empty:
            errors.append(
                f"readiness {source_field} must use exact canonical True/False values"
            )

    revenue_mask = readiness["model_id"].astype(str).eq(REVENUE_MODEL_ID)
    if int(revenue_mask.sum()) != 1:
        return [f"readiness must contain exactly one {REVENUE_MODEL_ID} row"]

    for persisted_field in sorted(REVENUE_PERMISSION_COLUMNS):
        values = readiness[persisted_field].fillna("").astype(str)
        bad_revenue = readiness[revenue_mask & values.ne("False")]
        if not bad_revenue.empty:
            errors.append(
                f"{REVENUE_MODEL_ID} readiness {persisted_field} must be explicit False"
            )
        bad_legacy = readiness[~revenue_mask & values.ne("")]
        if not bad_legacy.empty:
            errors.append(
                f"readiness {persisted_field} is revenue-only; non-revenue legacy rows "
                "must remain neutral blank: "
                + ", ".join(bad_legacy["model_id"].astype(str).tolist())
            )
    return errors
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def validate_revenue_readiness_row(
    readiness: pd.DataFrame,
    promotion_registry: pd.DataFrame,
    anomaly_registry: pd.DataFrame,
    forward_holdout_v2_manifest: pd.DataFrame,
    forward_holdout_v2_detail: pd.DataFrame | None = None,
    forward_holdout_v2_summary: pd.DataFrame | None = None,
    forward_holdout_v2_replay_source: pd.DataFrame | None = None,
    source_projection_manifest: pd.DataFrame | None = None,
) -> list[str]:
    errors: list[str] = []
    rows = readiness[readiness["model_id"].astype(str).eq(REVENUE_MODEL_ID)]
    if len(rows) != 1:
        return [f"readiness must contain exactly one {REVENUE_MODEL_ID} row"]
    try:
        expected = summarize_revenue_promotion_readiness(
            promotion_registry,
            anomaly_registry,
            forward_holdout_v2_manifest,
            holdout_detail=(
                forward_holdout_v2_detail
                if forward_holdout_v2_detail is not None
                else read_csv(REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV, dtype=str).fillna("")
            ),
            holdout_summary=(
                forward_holdout_v2_summary
                if forward_holdout_v2_summary is not None
                else read_csv(REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV, dtype=str).fillna("")
            ),
            replay_source=(
                forward_holdout_v2_replay_source
                if forward_holdout_v2_replay_source is not None
                else read_csv(
                    REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV, dtype=str
                ).fillna("")
            ),
            source_projection_manifest=(
                source_projection_manifest
                if source_projection_manifest is not None
                else read_csv(
                    REVENUE_SOURCE_PROJECTION_MANIFEST_CSV, dtype=str
                ).fillna("")
            ),
        )
    except RuntimeError as exc:
        return [f"{REVENUE_MODEL_ID} readiness source contract invalid: {exc}"]

    row = rows.iloc[0]
    compared_fields = {
        "parity_status",
        "blocker",
        "operation_module_status",
        "daily_adapter_status",
        "formal_model_use_allowed",
        "approved_for_daily",
        "approval_status",
        "operation_module_id",
        "approval_version",
        "presentation_allowed",
        "production_allowed",
        "operation_directive_level",
        "pdf_integration_status",
        "packet_integration_status",
        "registry_pattern_count",
        "registry_current_model_pattern_count",
        "registry_best_pattern_id",
        "registry_best_sample_size",
        "registry_best_win_rate",
        "registry_best_median_return",
        "daily_adapter_row_count",
        "daily_adapter_data_row_count",
        "daily_adapter_sections",
        "status_note_zh",
    }
    for field_name in sorted(compared_fields):
        actual = str(row.get(field_name, ""))
        wanted = str(expected[field_name])
        if actual != wanted:
            errors.append(
                f"{REVENUE_MODEL_ID} readiness {field_name} must be {wanted!r}, got {actual!r}"
            )
    return errors
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [OUT_CSV, OUT_MD, DOCS_CSV, DOCS_MD]:
        if not path.exists():
            errors.append(f"missing model operation readiness artifact: {path}")
    for path in [DAILY_VOLUME_ADAPTER_CSV, DAILY_W_BOTTOM_ADAPTER_CSV, DAILY_NECKLINE_ADAPTER_CSV, DAILY_PRICE_PULLBACK_ADAPTER_CSV]:
        if not path.exists():
            errors.append(f"missing approved daily operation adapter artifact: {path}")
    if not PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.exists():
        errors.append(f"missing price pullback daily row parity audit: {PRICE_PULLBACK_DAILY_ROW_PARITY_CSV}")
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    for path in [
        REVENUE_PROMOTION_REGISTRY_CSV,
        REVENUE_ANOMALY_REGISTRY_CSV,
        REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV,
        REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV,
        REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV,
        REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV,
        REVENUE_SOURCE_PROJECTION_MANIFEST_CSV,
    ]:
        if not path.exists():
            errors.append(f"missing revenue model readiness source: {path}")
    if REVENUE_PROMOTION_REGISTRY_CSV.exists() and REVENUE_ANOMALY_REGISTRY_CSV.exists():
        errors.extend(validate_revenue_readiness_source_files())
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
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

    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    present_permission_columns = REVENUE_PERMISSION_COLUMNS.intersection(df.columns)
    if present_permission_columns != REVENUE_PERMISSION_COLUMNS:
        if present_permission_columns:
            missing_permissions = sorted(
                REVENUE_PERMISSION_COLUMNS - present_permission_columns
            )
            return [
                "model operation readiness has a partial revenue permission schema: "
                f"missing={missing_permissions}"
            ]
        return validate_legacy_readiness_bootstrap_artifacts()

    permission_errors = validate_persisted_revenue_permission_columns(df)
    if permission_errors:
        return permission_errors
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

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

    legacy_volume = df[df["model_id"].astype(str).eq(LEGACY_VOLUME_MODEL_ID)]
    if not legacy_volume.empty:
        errors.append(f"readiness must not contain retired legacy {LEGACY_VOLUME_MODEL_ID} rows")

    for model_id in V2_VOLUME_MODEL_IDS:
        volume = df[df["model_id"].astype(str).eq(model_id)]
        if len(volume) != 1:
            errors.append(f"readiness must contain exactly one {model_id} row")
            continue
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
                errors.append(f"{model_id} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("daily_adapter_status", "")) not in {
            "ready_approved_operation_guidance",
            "ready_empty_no_operation_rows",
        }:
            errors.append(
                f"{model_id} daily_adapter_status must be ready approved or ready empty, "
                f"got {row.get('daily_adapter_status', '')!r}"
            )
        if not str(row.get("operation_module_id", "")):
            errors.append(f"{model_id} operation_module_id must be populated")
        if not str(row.get("approval_version", "")):
            errors.append(f"{model_id} approval_version must be populated")
        if not {"confirmed_operation", "active_operation"}.issubset(
            set(str(row.get("daily_adapter_sections", "")).split(","))
        ):
            errors.append(f"{model_id} daily_adapter_sections must include confirmed_operation and active_operation")

    w_bottom = df[df["model_id"].astype(str).eq(W_BOTTOM_MODEL_ID)]
    if len(w_bottom) != 1:
        errors.append(f"readiness must contain exactly one {W_BOTTOM_MODEL_ID} row")
    else:
        row = w_bottom.iloc[0]
        expected = {
            "operation_module_status": "approved_operation_v2",
            "approved_for_daily": "True",
            "approval_status": "approved_for_daily_v2",
            "presentation_allowed": "True",
            "operation_directive_level": "approved_daily_operation_guidance",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "packet_integration_status": "packet_integrated_daily_adapter",
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{W_BOTTOM_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("daily_adapter_status", "")) not in {
            "ready_approved_operation_guidance",
            "ready_empty_no_operation_rows",
        }:
            errors.append(
                f"{W_BOTTOM_MODEL_ID} daily_adapter_status must be ready approved or ready empty, "
                f"got {row.get('daily_adapter_status', '')!r}"
            )
        if str(row.get("operation_module_id", "")) != "w_bottom_early_entry_operation_v2":
            errors.append(f"{W_BOTTOM_MODEL_ID} operation_module_id must be w_bottom_early_entry_operation_v2")
        if str(row.get("approval_version", "")) != "w_bottom_early_entry_operation_v2_20260629":
            errors.append(f"{W_BOTTOM_MODEL_ID} approval_version must be w_bottom_early_entry_operation_v2_20260629")
        if not {"confirmed_operation", "active_operation"}.issubset(
            set(str(row.get("daily_adapter_sections", "")).split(","))
        ):
            errors.append(f"{W_BOTTOM_MODEL_ID} daily_adapter_sections must include confirmed_operation and active_operation")

    neckline = df[df["model_id"].astype(str).eq(NECKLINE_MODEL_ID)]
    if len(neckline) != 1:
        errors.append(f"readiness must contain exactly one {NECKLINE_MODEL_ID} row")
    else:
        row = neckline.iloc[0]
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
                errors.append(f"{NECKLINE_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("daily_adapter_status", "")) not in {
            "ready_approved_operation_guidance",
            "ready_empty_no_operation_rows",
        }:
            errors.append(
                f"{NECKLINE_MODEL_ID} daily_adapter_status must be ready approved or ready empty, "
                f"got {row.get('daily_adapter_status', '')!r}"
            )
        if str(row.get("operation_module_id", "")) != "neckline_strict_45_signal_90_score_v1":
            errors.append(f"{NECKLINE_MODEL_ID} operation_module_id must be neckline_strict_45_signal_90_score_v1")
        if str(row.get("approval_version", "")) != "neckline_strict_45_signal_90_score_v1_20260629":
            errors.append(f"{NECKLINE_MODEL_ID} approval_version must be neckline_strict_45_signal_90_score_v1_20260629")
        if not {"confirmed_operation", "active_operation"}.issubset(
            set(str(row.get("daily_adapter_sections", "")).split(","))
        ):
            errors.append(
                f"{NECKLINE_MODEL_ID} daily_adapter_sections must include confirmed_operation and active_operation"
            )

    price_pullback = df[df["model_id"].astype(str).eq(PRICE_PULLBACK_MODEL_ID)]
    if len(price_pullback) != 1:
        errors.append(f"readiness must contain exactly one {PRICE_PULLBACK_MODEL_ID} row")
    else:
        row = price_pullback.iloc[0]
        expected = {
            "operation_module_status": "approved_operation_v1",
            "operation_module_id": PRICE_PULLBACK_OPERATION_MODULE_ID,
            "approval_version": "price_pullback_23ema_operation_v1_20260703",
            "approved_for_daily": "True",
            "approval_status": "approved_for_daily_v1",
            "presentation_allowed": "True",
            "operation_directive_level": "approved_daily_operation_guidance",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "packet_integration_status": "packet_integrated_daily_adapter",
            "registry_best_pattern_id": PRICE_PULLBACK_BUY_FILTER_ID,
        }
        for col, value in expected.items():
            if str(row.get(col, "")) != value:
                errors.append(f"{PRICE_PULLBACK_MODEL_ID} readiness {col} must be {value!r}, got {row.get(col, '')!r}")
        if str(row.get("daily_adapter_status", "")) not in {
            "ready_approved_operation_guidance",
            "ready_empty_no_operation_rows",
        }:
            errors.append(
                f"{PRICE_PULLBACK_MODEL_ID} daily_adapter_status must be ready approved or ready empty, "
                f"got {row.get('daily_adapter_status', '')!r}"
            )
        if not {"confirmed_operation", "active_operation"}.issubset(
            set(str(row.get("daily_adapter_sections", "")).split(","))
        ):
            errors.append(
                f"{PRICE_PULLBACK_MODEL_ID} daily_adapter_sections must include confirmed_operation and active_operation"
            )
        if not PRICE_PULLBACK_SPEC_SOURCE.exists():
            errors.append(f"missing price pullback operation candidate spec source: {PRICE_PULLBACK_SPEC_SOURCE}")
        if int(float(row.get("registry_best_sample_size", 0) or 0)) < 1000:
            errors.append("price pullback approved sample size is weaker than the v1 gate")
        if float(row.get("registry_best_win_rate", 0) or 0) < 60.0:
            errors.append("price pullback approved win rate is weaker than the v1 gate")
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

    errors.extend(
        validate_revenue_readiness_row(
            df,
            read_csv(REVENUE_PROMOTION_REGISTRY_CSV, dtype=str).fillna(""),
            read_csv(REVENUE_ANOMALY_REGISTRY_CSV, dtype=str).fillna(""),
            read_csv(REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV, dtype=str).fillna(""),
            read_csv(REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV, dtype=str).fillna(""),
            read_csv(REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV, dtype=str).fillna(""),
            read_csv(
                REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV, dtype=str
            ).fillna(""),
            read_csv(REVENUE_SOURCE_PROJECTION_MANIFEST_CSV, dtype=str).fillna(""),
        )
    )
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

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
    if models != sorted(V2_VOLUME_MODEL_IDS):
        errors.append(f"daily volume breakout adapter must contain only {sorted(V2_VOLUME_MODEL_IDS)}, got {models}")
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
    for model_id in V2_VOLUME_MODEL_IDS:
        print(f"{model_id}_status={df.loc[df['model_id'].eq(model_id), 'daily_adapter_status'].iloc[0]}")
    print(f"w_bottom_status={df.loc[df['model_id'].eq(W_BOTTOM_MODEL_ID), 'daily_adapter_status'].iloc[0]}")
    print(f"neckline_status={df.loc[df['model_id'].eq(NECKLINE_MODEL_ID), 'daily_adapter_status'].iloc[0]}")
    print(f"price_pullback_status={df.loc[df['model_id'].eq(PRICE_PULLBACK_MODEL_ID), 'daily_adapter_status'].iloc[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
