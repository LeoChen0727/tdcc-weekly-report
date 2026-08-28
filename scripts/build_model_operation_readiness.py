from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_text, read_csv, safe_str, write_csv  # noqa: E402
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
from validate_revenue_unreacted_range_forward_holdout_v2 import (  # noqa: E402
    ARTIFACT_VERSION as REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
    HOLDOUT_START_DATE as REVENUE_FORWARD_HOLDOUT_V2_START_DATE,
)
from validate_revenue_unreacted_range_promotion_preparation import (  # noqa: E402
    DISPOSITION_POLICIES as REVENUE_ANOMALY_DISPOSITION_POLICIES,
    EXPECTED_ANOMALIES_V2 as REVENUE_EXPECTED_ANOMALIES,
    EXPECTED_DECISION_V3 as REVENUE_EXPECTED_PROMOTION_DECISION,
    validate_anomalies as validate_revenue_anomaly_registry,
    validate_decision as validate_revenue_promotion_registry,
)
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


PARITY_CSV = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.csv"
REGISTRY_CSV = LATEST_DIR / "historical_pattern_operation_registry_latest.csv"
DAILY_VOLUME_ADAPTER_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
DAILY_W_BOTTOM_ADAPTER_CSV = LATEST_DIR / "daily_w_bottom_right_side_operation_section_latest.csv"
DAILY_NECKLINE_ADAPTER_CSV = LATEST_DIR / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"
DAILY_PRICE_PULLBACK_ADAPTER_CSV = LATEST_DIR / "daily_price_pullback_23ema_operation_section_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
REVENUE_PROMOTION_REGISTRY_CSV = Path(
    "config/revenue_unreacted_range_promotion_preparation_registry.csv"
)
REVENUE_ANOMALY_REGISTRY_CSV = Path(
    "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv"
)
REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV = (
    RESEARCH_LATEST_DIR / "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv"
)
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

OUT_CSV = LATEST_DIR / "model_operation_readiness_latest.csv"
OUT_MD = LATEST_DIR / "model_operation_readiness_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

LEGACY_VOLUME_MODEL_IDS = {"volume_range_breakout"}
V2_LOW_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
V2_MID_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
V2_HIGH_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
V2_VOLUME_MODEL_IDS = (V2_LOW_MODEL_ID, V2_MID_MODEL_ID, V2_HIGH_MODEL_ID)
W_BOTTOM_MODEL_ID = "w_bottom_right_side"
NECKLINE_MODEL_ID = "neckline_volume_breakout_confirmation"
PRICE_PULLBACK_MODEL_ID = "price_pullback_23ema"
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
REVENUE_MODEL_ID = "revenue_unreacted_range"
REVENUE_PROMOTION_CONTRACT_VERSION = REVENUE_EXPECTED_PROMOTION_DECISION[
    "contract_version"
]
REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_ID = "revenue_unreacted_range_forward_holdout_v2"
REVENUE_SOURCE_VARIANT_ID = "source_mid_falling"
REVENUE_PROMOTION_FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only_EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
REVENUE_RESEARCH_MATRIX_STATUS = "research_matrix_complete"
REVENUE_OPERATION_MODULE_STATUS = "research_matrix_complete_formal_adapter_not_started"
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_feature_confirmation_research_latest.csv"
)
PRICE_PULLBACK_DAILY_ROW_PARITY_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_daily_row_parity_latest.csv"
)
PRICE_PULLBACK_SPEC_SOURCE = Path("docs/specs/price_pullback_23ema_operation_candidate_spec.md")
PRICE_PULLBACK_OPERATION_MODULE_ID = "price_pullback_23ema_prev20_breakout_stop_v1"
PRICE_PULLBACK_CANDIDATE_VERSION = "price_pullback_23ema_operation_candidate_v1_20260630"
PRICE_PULLBACK_BUY_FILTER_ID = "v1_gate_return20_tdcc_high_obv"


def truthy(value: Any) -> bool:
    text = safe_str(value).lower()
    return text in {"true", "1", "1.0", "yes", "y"}
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def _required_columns(frame: pd.DataFrame, required: set[str], source_name: str) -> None:
    if frame.empty:
        raise RuntimeError(f"missing required revenue readiness source: {source_name}")
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"revenue readiness source {source_name} missing columns: {missing}")


def _strict_nonnegative_int(value: Any, field_name: str) -> int:
    text = safe_str(value)
    if not text.isdigit():
        raise RuntimeError(f"revenue readiness {field_name} must be a non-negative integer, got {text!r}")
    return int(text)


def _require_contract_bool(value: Any, expected: bool, field_name: str) -> None:
    text = safe_str(value).lower()
    expected_text = "true" if expected else "false"
    if text != expected_text:
        raise RuntimeError(
            f"revenue readiness {field_name} must be {expected_text!r}, got {text!r}"
        )


def validate_revenue_readiness_source_files() -> list[str]:
    """Run the canonical current-stage promotion and anomaly source validators."""

    _, decision_errors = validate_revenue_promotion_registry(
        REVENUE_PROMOTION_REGISTRY_CSV
    )
    _, anomaly_errors = validate_revenue_anomaly_registry(
        REVENUE_ANOMALY_REGISTRY_CSV,
        expected_anomalies=REVENUE_EXPECTED_ANOMALIES,
        version_label="v2",
    )
    return [
        *(f"revenue promotion readiness source: {error}" for error in decision_errors),
        *(f"revenue anomaly readiness source: {error}" for error in anomaly_errors),
    ]


def summarize_revenue_promotion_readiness(
    promotion_registry: pd.DataFrame,
    anomaly_registry: pd.DataFrame,
    forward_holdout_v2_manifest: pd.DataFrame,
) -> dict[str, Any]:
    """Build revenue-only readiness from decision v3 / promotion contract v4."""

    promotion_required = {
        "decision_id",
        "decision_date",
        "model_id",
        "contract_version",
        "source_variant_id",
        "candidate_variant_id",
        "operation_count",
        "win_rate_pct",
        "median_return_pct",
        "combined_exclusion_candidate_count",
        "forward_holdout_first_interpretation_min_mature",
        "formal_adapter_gate",
        "decision_status",
        "anomaly_disposition_gate",
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
        "financial_statement_scope",
        "promotion_scope",
    }
    _required_columns(promotion_registry, promotion_required, str(REVENUE_PROMOTION_REGISTRY_CSV))
    promotion_rows = promotion_registry[
        promotion_registry["model_id"].astype(str).eq(REVENUE_MODEL_ID)
    ].copy()
    if promotion_rows.empty:
        raise RuntimeError(
            f"revenue readiness source {REVENUE_PROMOTION_REGISTRY_CSV} has no {REVENUE_MODEL_ID} row"
        )
    if promotion_rows["decision_id"].astype(str).duplicated().any():
        raise RuntimeError("revenue promotion registry contains duplicate decision_id values")
    decision_dates = pd.to_datetime(promotion_rows["decision_date"], errors="coerce")
    if decision_dates.isna().any() or not decision_dates.is_monotonic_increasing:
        raise RuntimeError("revenue promotion registry decision_date must be valid and append-only")
    promotion = promotion_rows.iloc[-1]
    contract_version = safe_str(promotion.get("contract_version"))
    if contract_version != REVENUE_PROMOTION_CONTRACT_VERSION:
        raise RuntimeError(
            "revenue readiness requires latest decision v3 / promotion contract v4; "
            f"got {contract_version!r}"
        )
    if safe_str(promotion.get("candidate_variant_id")) != REVENUE_SOURCE_VARIANT_ID:
        raise RuntimeError(
            f"revenue readiness candidate_variant_id must be {REVENUE_SOURCE_VARIANT_ID!r}"
        )
    if (
        safe_str(promotion.get("financial_statement_scope"))
        != REVENUE_PROMOTION_FINANCIAL_STATEMENT_SCOPE
    ):
        raise RuntimeError("revenue readiness promotion scope must remain monthly-revenue-only")
    for field_name in (
        "decision_status",
        "anomaly_disposition_gate",
        "promotion_scope",
    ):
        expected_value = REVENUE_EXPECTED_PROMOTION_DECISION[field_name]
        actual_value = safe_str(promotion.get(field_name))
        if actual_value != expected_value:
            raise RuntimeError(
                f"revenue readiness promotion.{field_name} must be "
                f"{expected_value!r}, got {actual_value!r}"
            )
    for field_name in (
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
    ):
        _require_contract_bool(promotion.get(field_name), False, f"promotion.{field_name}")

    minimum_mature = _strict_nonnegative_int(
        promotion.get("forward_holdout_first_interpretation_min_mature"),
        "promotion.forward_holdout_first_interpretation_min_mature",
    )
    if minimum_mature <= 0:
        raise RuntimeError("revenue readiness forward holdout maturity threshold must be positive")
    candidate_count = _strict_nonnegative_int(
        promotion.get("combined_exclusion_candidate_count"),
        "promotion.combined_exclusion_candidate_count",
    )

    anomaly_required = {
        "model_id",
        "operation_key",
        "candidate_detail_row_sha256",
        "final_disposition",
        "primary_handling",
        "promotion_gate_status",
    }
    _required_columns(anomaly_registry, anomaly_required, str(REVENUE_ANOMALY_REGISTRY_CSV))
    anomaly_rows = anomaly_registry[
        anomaly_registry["model_id"].astype(str).eq(REVENUE_MODEL_ID)
    ].copy()
    if anomaly_rows.empty:
        raise RuntimeError(
            f"revenue readiness source {REVENUE_ANOMALY_REGISTRY_CSV} has no {REVENUE_MODEL_ID} rows"
        )
    if anomaly_rows["operation_key"].astype(str).str.strip().eq("").any():
        raise RuntimeError("revenue anomaly registry contains a blank operation_key")
    if anomaly_rows["candidate_detail_row_sha256"].astype(str).str.fullmatch(r"[0-9a-f]{64}").ne(True).any():
        raise RuntimeError("revenue anomaly registry contains an invalid candidate_detail_row_sha256")
    latest_anomalies = anomaly_rows.drop_duplicates(subset=["operation_key"], keep="last")
    if len(latest_anomalies) != candidate_count:
        raise RuntimeError(
            "revenue anomaly registry unique operation count does not match the latest promotion row: "
            f"registry={len(latest_anomalies)}, promotion={candidate_count}"
        )
    invalid_dispositions = sorted(
        set(latest_anomalies["final_disposition"].astype(str))
        - set(REVENUE_ANOMALY_DISPOSITION_POLICIES)
    )
    if invalid_dispositions:
        raise RuntimeError(
            f"revenue anomaly registry contains invalid final_disposition values: {invalid_dispositions}"
        )
    for _, anomaly in latest_anomalies.iterrows():
        disposition = safe_str(anomaly.get("final_disposition"))
        expected_handling, expected_gate = REVENUE_ANOMALY_DISPOSITION_POLICIES[
            disposition
        ]
        actual_policy = (
            safe_str(anomaly.get("primary_handling")),
            safe_str(anomaly.get("promotion_gate_status")),
        )
        if actual_policy != (expected_handling, expected_gate):
            raise RuntimeError(
                "revenue anomaly disposition policy mismatch for "
                f"{safe_str(anomaly.get('operation_key'))}: disposition={disposition!r}; "
                f"expected={(expected_handling, expected_gate)!r}; actual={actual_policy!r}"
            )
    unresolved_rows = latest_anomalies[
        latest_anomalies["final_disposition"].astype(str).eq("unresolved_anomaly_candidate")
    ]
    if not unresolved_rows.empty:
        if not unresolved_rows["primary_handling"].astype(str).eq(
            "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only"
        ).all():
            raise RuntimeError("unresolved revenue anomalies must remain in primary metrics")
        if not unresolved_rows["promotion_gate_status"].astype(str).eq(
            "blocked_pending_root_cause"
        ).all():
            raise RuntimeError("unresolved revenue anomalies must block promotion")
    unresolved_count = len(unresolved_rows)
    non_blocking_anomaly_gates = {
        REVENUE_ANOMALY_DISPOSITION_POLICIES["verified_real_extreme"][1]
    }
    blocking_anomaly_count = int(
        (
            ~latest_anomalies["promotion_gate_status"]
            .astype(str)
            .isin(non_blocking_anomaly_gates)
        ).sum()
    )

    holdout_required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "artifact_row_key",
        "holdout_start_date",
        "observed_through_date",
        "primary_mature_count",
        "holdout_status",
        "append_only_history",
        "research_only",
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
        "production_change",
        "financial_statement_scope",
    }
    _required_columns(
        forward_holdout_v2_manifest,
        holdout_required,
        str(REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV),
    )
    holdout_rows = forward_holdout_v2_manifest[
        forward_holdout_v2_manifest["model_id"].astype(str).eq(REVENUE_MODEL_ID)
        & forward_holdout_v2_manifest["artifact_id"]
        .astype(str)
        .eq(REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_ID)
        & forward_holdout_v2_manifest["artifact_row_key"].astype(str).eq("manifest")
    ]
    if len(holdout_rows) != 1 or len(forward_holdout_v2_manifest) != 1:
        raise RuntimeError("revenue forward holdout v2 latest manifest must contain exactly one manifest row")
    holdout = holdout_rows.iloc[0]
    artifact_version = safe_str(holdout.get("artifact_version"))
    if artifact_version != REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION:
        raise RuntimeError(
            "revenue forward holdout v2 artifact_version must be "
            f"{REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION!r}, got {artifact_version!r}"
        )
    holdout_start_date = safe_str(holdout.get("holdout_start_date"))
    if holdout_start_date != REVENUE_FORWARD_HOLDOUT_V2_START_DATE:
        raise RuntimeError(
            "revenue forward holdout v2 holdout_start_date must be "
            f"{REVENUE_FORWARD_HOLDOUT_V2_START_DATE!r}, got {holdout_start_date!r}"
        )
    observed_through_date = safe_str(holdout.get("observed_through_date"))
    if not observed_through_date.isdigit() or len(observed_through_date) != 8:
        raise RuntimeError(
            "revenue forward holdout v2 observed_through_date must be YYYYMMDD"
        )
    _require_contract_bool(holdout.get("append_only_history"), True, "holdout.append_only_history")
    _require_contract_bool(holdout.get("research_only"), True, "holdout.research_only")
    for field_name in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
        "production_change",
    ):
        _require_contract_bool(holdout.get(field_name), False, f"holdout.{field_name}")
    holdout_status = safe_str(holdout.get("holdout_status"))
    expected_holdout_status = (
        "preregistered_waiting_for_start"
        if observed_through_date < REVENUE_FORWARD_HOLDOUT_V2_START_DATE
        else "holdout_accumulating"
    )
    if holdout_status != expected_holdout_status:
        raise RuntimeError(
            "revenue forward holdout v2 holdout_status is inconsistent with maturity timing: "
            f"expected={expected_holdout_status!r}, got={holdout_status!r}"
        )
    if (
        safe_str(holdout.get("financial_statement_scope"))
        != REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE
    ):
        raise RuntimeError("revenue forward holdout v2 scope must remain monthly-revenue-only")
    mature_count = _strict_nonnegative_int(
        holdout.get("primary_mature_count"), "holdout.primary_mature_count"
    )
    if expected_holdout_status == "preregistered_waiting_for_start" and mature_count != 0:
        raise RuntimeError(
            "revenue forward holdout v2 pre-start manifest must have primary_mature_count=0"
        )

    formal_adapter_gate = safe_str(promotion.get("formal_adapter_gate"))
    expected_adapter_gate = REVENUE_EXPECTED_PROMOTION_DECISION["formal_adapter_gate"]
    if formal_adapter_gate != expected_adapter_gate:
        raise RuntimeError(
            f"revenue readiness formal_adapter_gate must remain {expected_adapter_gate!r} "
            f"until the disabled formal adapter contract lands, got {formal_adapter_gate!r}"
        )
    formal_adapter_status = "not_started"
    blocker = (
        f"anomaly_disposition_blockers={blocking_anomaly_count}; "
        f"unresolved_anomalies={unresolved_count}; "
        f"forward_holdout_v2_mature={mature_count}/{minimum_mature}; "
        f"formal_adapter={formal_adapter_status}"
    )
    return {
        "parity_status": REVENUE_RESEARCH_MATRIX_STATUS,
        "blocker": blocker,
        "operation_module_status": REVENUE_OPERATION_MODULE_STATUS,
        "daily_adapter_status": formal_adapter_status,
        "approved_for_daily": "False",
        "approval_status": "not_started",
        "operation_module_id": "",
        "approval_version": "",
        "presentation_allowed": "False",
        "operation_directive_level": "no_operation_directive",
        "pdf_integration_status": "not_started",
        "packet_integration_status": "not_started",
        "registry_pattern_count": 1,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": safe_str(promotion.get("candidate_variant_id")),
        "registry_best_sample_size": _strict_nonnegative_int(
            promotion.get("operation_count"), "promotion.operation_count"
        ),
        "registry_best_win_rate": safe_str(promotion.get("win_rate_pct")),
        "registry_best_median_return": safe_str(promotion.get("median_return_pct")),
        "daily_adapter_row_count": 0,
        "daily_adapter_data_row_count": 0,
        "daily_adapter_sections": "",
        "status_note_zh": (
            "revenue_unreacted_range／source_mid_falling v2 的模型專屬研究矩陣已完成；"
            f"目前仍有 {blocking_anomaly_count} 筆 anomaly disposition 阻擋項目（其中 "
            f"{unresolved_count} 筆尚未定案）、forward holdout v2 "
            f"成熟度 {mature_count}/{minimum_mature} 與 disabled formal adapter preparation 尚未完成。"
            "月營收以外的 EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報欄位均不在模型範圍；"
            "不得產生 production、PDF、packet 或操作指令。"
        ),
    }
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def summarize_volume_daily_adapter(adapter: pd.DataFrame, model_id: str) -> dict[str, Any]:
    if adapter.empty:
        return {
            "daily_adapter_status": "missing",
            "daily_adapter_row_count": 0,
            "daily_adapter_data_row_count": 0,
            "daily_adapter_sections": "",
        }
    if "model_id" not in adapter.columns:
        return {
            "daily_adapter_status": "invalid_missing_model_id",
            "daily_adapter_row_count": len(adapter),
            "daily_adapter_data_row_count": 0,
            "daily_adapter_sections": "",
        }
    adapter = adapter[adapter["model_id"].astype(str).eq(model_id)].copy()
    if adapter.empty:
        return {
            "daily_adapter_status": "missing",
            "daily_adapter_row_count": 0,
            "daily_adapter_data_row_count": 0,
            "daily_adapter_sections": "",
        }

    models = sorted(set(adapter["model_id"].astype(str)))
    row_type = adapter["row_type"].astype(str) if "row_type" in adapter.columns else pd.Series([""] * len(adapter))
    data_rows = int(row_type.eq("data").sum())
    sections = sorted(set(adapter.get("pdf_section", pd.Series(dtype=str)).astype(str)))
    source_statuses = sorted(set(adapter.get("adapter_source_status", pd.Series(dtype=str)).astype(str)))
    data_source_statuses = sorted(
        set(adapter.loc[row_type.eq("data"), "adapter_source_status"].astype(str))
        if "adapter_source_status" in adapter.columns
        else set()
    )
    base_ready = models == [model_id] and data_rows > 0 and (
        not data_source_statuses or data_source_statuses == ["ready"]
    )
    empty_sections_ready = (
        models == [model_id]
        and data_rows == 0
        and set(sections) >= {"confirmed_operation", "pending_confirmation", "active_operation"}
        and source_statuses == ["ready"]
    )

    approved_metadata_ready = False
    if (base_ready or empty_sections_ready) and {
        "approved_for_daily",
        "operation_directive_level",
    }.issubset(adapter.columns):
        approved_metadata_ready = (
            set(adapter["approved_for_daily"].astype(str)) == {"True"}
            and set(adapter["operation_directive_level"].astype(str)) == {"approved_daily_operation_guidance"}
        )

    if approved_metadata_ready:
        if empty_sections_ready:
            status = "ready_empty_no_operation_rows"
        else:
            status = "ready_approved_operation_guidance"
    elif base_ready:
        status = "ready_pending_approval_metadata"
    else:
        status = "blocked"

    return {
        "daily_adapter_status": status,
        "daily_adapter_row_count": len(adapter),
        "daily_adapter_data_row_count": data_rows,
        "daily_adapter_sections": ",".join(section for section in sections if section),
    }


def summarize_w_bottom_daily_adapter(adapter: pd.DataFrame, model_id: str) -> dict[str, Any]:
    if adapter.empty:
        return {
            "daily_adapter_status": "missing",
            "daily_adapter_row_count": 0,
            "daily_adapter_data_row_count": 0,
            "daily_adapter_sections": "",
        }
    if "model_id" not in adapter.columns:
        return {
            "daily_adapter_status": "invalid_missing_model_id",
            "daily_adapter_row_count": len(adapter),
            "daily_adapter_data_row_count": 0,
            "daily_adapter_sections": "",
        }

    models = sorted(set(adapter["model_id"].astype(str)))
    row_type = adapter["row_type"].astype(str) if "row_type" in adapter.columns else pd.Series([""] * len(adapter))
    data_rows = int(row_type.eq("data").sum())
    sections = sorted(set(adapter.get("pdf_section", pd.Series(dtype=str)).astype(str)))
    source_statuses = sorted(set(adapter.get("adapter_source_status", pd.Series(dtype=str)).astype(str)))
    source_ready = models == [model_id] and set(sections) >= {"confirmed_operation", "active_operation"}
    source_ready = source_ready and source_statuses == ["ready"]
    approved_metadata_ready = False
    if source_ready and {"approved_for_daily", "operation_directive_level"}.issubset(adapter.columns):
        approved_metadata_ready = (
            set(adapter["approved_for_daily"].astype(str)) == {"True"}
            and set(adapter["operation_directive_level"].astype(str)) == {"approved_daily_operation_guidance"}
        )

    if approved_metadata_ready:
        status = "ready_empty_no_operation_rows" if data_rows == 0 else "ready_approved_operation_guidance"
    elif source_ready:
        status = "ready_pending_approval_metadata"
    else:
        status = "blocked"

    return {
        "daily_adapter_status": status,
        "daily_adapter_row_count": len(adapter),
        "daily_adapter_data_row_count": data_rows,
        "daily_adapter_sections": ",".join(section for section in sections if section),
    }


def summarize_price_pullback_row_parity(row_parity: pd.DataFrame | None) -> dict[str, str]:
    if row_parity is None or row_parity.empty or "parity_status" not in row_parity.columns:
        return {
            "row_parity_status": "missing_artifact",
            "row_parity_blocker": "exact daily candidate row parity audit artifact is missing",
            "row_parity_note_zh": "尚未建立 published snapshot 對 research proxy 的 daily row parity audit。",
        }

    data = row_parity.copy()
    for col in [
        "published_not_in_proxy_rows",
        "proxy_not_published_rows",
        "published_unique_stock_count",
        "research_proxy_unique_stock_count",
    ]:
        series = data[col] if col in data.columns else pd.Series([0] * len(data), index=data.index)
        data[col] = pd.to_numeric(series, errors="coerce").fillna(0).astype(int)

    blocked = data[~data["parity_status"].astype(str).eq("exact_daily_row_parity_pass")]
    latest_date = safe_str(data["snapshot_report_date"].astype(str).max()) if "snapshot_report_date" in data.columns else ""
    published_gap = int(data["published_not_in_proxy_rows"].sum())
    proxy_gap = int(data["proxy_not_published_rows"].sum())
    missing_dates = int(data["parity_status"].astype(str).eq("blocked_missing_research_frame_date").sum())
    snapshot_count = len(data)
    candidate_replay_exact = False
    if "candidate_universe_replay_status" in data.columns:
        candidate_replay_exact = data["candidate_universe_replay_status"].astype(str).eq(
            "candidate_universe_replay_exact_match"
        ).all()
    if "parity_gap_driver" in data.columns:
        gap_drivers = ",".join(
            sorted(driver for driver in data["parity_gap_driver"].astype(str).unique().tolist() if driver)
        )
    else:
        gap_drivers = "not_classified"

    if blocked.empty:
        return {
            "row_parity_status": "exact_pass",
            "row_parity_blocker": "",
            "row_parity_note_zh": f"daily row parity audit 已通過 {snapshot_count} 個 published snapshots。",
        }

    blocked_statuses = set(blocked["parity_status"].astype(str).tolist())
    if (
        published_gap == 0
        and proxy_gap == 0
        and missing_dates > 0
        and candidate_replay_exact
        and blocked_statuses <= {"blocked_missing_research_frame_date"}
    ):
        return {
            "row_parity_status": "discussion_ready_pending_latest_research_frame",
            "row_parity_blocker": (
                "latest research frame freshness pending: "
                f"snapshots={snapshot_count}, latest_snapshot={latest_date}, "
                f"production_candidate_universe_replay_exact=True, missing_research_dates={missing_dates}"
            ),
            "row_parity_note_zh": (
                f"daily production row replay 已用 dated all_candidates/source-row 通過 {snapshot_count} 個 "
                f"published snapshots，published/proxy row gap=0；仍有 {missing_dates} 個 latest snapshot "
                "缺 research frame 日期，所以不能 promotion 或產生 production 操作建議，但可以開始模型決策討論。"
            ),
        }

    return {
        "row_parity_status": "blocked_row_gap",
        "row_parity_blocker": (
            "exact daily row parity audit failing: "
            f"snapshots={snapshot_count}, latest_snapshot={latest_date}, "
            f"published_not_proxy={published_gap}, proxy_not_published={proxy_gap}, "
            f"missing_research_dates={missing_dates}, gap_drivers={gap_drivers}"
        ),
        "row_parity_note_zh": (
            f"daily row parity audit 仍未通過：共 {snapshot_count} 個 published snapshots，"
            f"published 不在 research proxy 的股票數合計 {published_gap}，"
            f"research proxy 未出現在 published snapshot 的股票數合計 {proxy_gap}，"
            f"缺 research frame 日期 {missing_dates} 個。"
            "目前主要差異需用 dated all_candidates/source-row candidate universe replay 釐清，"
            "不能把 full-universe research proxy 視為 production baseline。"
        ),
    }


def summarize_price_pullback_candidate(
    feature_confirmation: pd.DataFrame,
    row_parity: pd.DataFrame | None = None,
) -> dict[str, Any]:
    row_parity_summary = summarize_price_pullback_row_parity(row_parity)
    row_parity_status = row_parity_summary["row_parity_status"]
    empty = {
        "candidate_ready": "False",
        "operation_module_status": "baseline_only_no_validated_operation_module",
        "daily_adapter_status": "not_started",
        "approval_status": "not_started",
        "operation_module_id": "",
        "approval_version": "",
        "registry_pattern_count": 0,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": "",
        "registry_best_sample_size": 0,
        "registry_best_win_rate": "",
        "registry_best_median_return": "",
        "row_parity_blocker": row_parity_summary["row_parity_blocker"],
        "status_note_zh": "目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。",
    }
    if feature_confirmation.empty or "model_id" not in feature_confirmation.columns:
        return empty

    rows = feature_confirmation[
        feature_confirmation["model_id"].astype(str).eq(PRICE_PULLBACK_MODEL_ID)
        & feature_confirmation.get("feature_filter_id", pd.Series(dtype=str))
        .astype(str)
        .eq(PRICE_PULLBACK_BUY_FILTER_ID)
    ].copy()
    if rows.empty:
        return empty
    row = rows.iloc[0]
    if safe_str(row.get("feature_test_status")) != "tested_point_in_time":
        return empty
    if safe_str(row.get("advisory_status")) != "not_production_ready_research_only":
        return empty
    if truthy(row.get("approved_for_daily")):
        return empty

    if row_parity_status == "exact_pass":
        operation_module_status = "operation_candidate_v1_pending_promotion_pr"
        daily_adapter_status = "blocked_explicit_promotion_pr_required"
        approval_status = "pending_explicit_promotion_pr"
        integration_status = "blocked_explicit_promotion_pr_required"
        parity_phrase = "daily row parity 已通過；仍需要獨立 promotion/sync PR 才能進 production。"
        daily_adapter_status = "blocked_promotion_pr_and_daily_operation_adapter_required"
        approval_status = "pending_promotion_pr_and_daily_adapter"
        integration_status = "blocked_promotion_pr_and_daily_operation_adapter_required"
        parity_phrase = (
            "daily row parity 已通過；仍需要獨立 promotion/sync PR 與正式 daily operation-row "
            "adapter/PDF section contract 才能進 production。PDF renderer 不得自行推論 23EMA 操作列。"
        )
    elif row_parity_status == "discussion_ready_pending_latest_research_frame":
        operation_module_status = "operation_candidate_v1_discussion_ready_pending_latest_research_frame"
        daily_adapter_status = "blocked_latest_research_frame"
        approval_status = "pending_research_freshness_and_promotion_pr"
        integration_status = "blocked_latest_research_frame"
        parity_phrase = "daily row replay 已足夠開始模型決策討論；仍需補 latest research frame freshness 與 promotion/sync PR。"
    else:
        operation_module_status = "operation_candidate_v1_pending_exact_row_parity"
        daily_adapter_status = "blocked_exact_daily_row_parity"
        approval_status = "pending_exact_daily_row_parity"
        integration_status = "blocked_exact_daily_row_parity"
        parity_phrase = "目前仍缺 exact daily candidate row parity。"

    return {
        "candidate_ready": "True",
        "operation_module_status": operation_module_status,
        "daily_adapter_status": daily_adapter_status,
        "approval_status": approval_status,
        "pdf_integration_status": integration_status,
        "packet_integration_status": integration_status,
        "operation_module_id": PRICE_PULLBACK_OPERATION_MODULE_ID,
        "approval_version": PRICE_PULLBACK_CANDIDATE_VERSION,
        "registry_pattern_count": 1,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": safe_str(row.get("feature_filter_id")),
        "registry_best_sample_size": int(float(row.get("mature_count", 0) or 0)),
        "registry_best_win_rate": safe_str(row.get("win_rate_pct")),
        "registry_best_median_return": safe_str(row.get("median_d20_close_return_pct")),
        "row_parity_blocker": row_parity_summary["row_parity_blocker"],
        "status_note_zh": (
            "price_pullback_23ema 已選出 operation candidate v1：先有 production proxy 訊號，"
            "且同日符合大戶高門檻增加與 20 日漲幅 0% 到 25%；買點為次日開盤，"
            "勝利為 D+20 前盤中突破訊號日前 20 日高點，失敗為連續 4 日收盤低於 "
            f"MA20/EMA23 較低者 4%。{parity_phrase}"
            f"{row_parity_summary['row_parity_note_zh']}所以不得產生 production 買進、賣出、停損或排名操作建議。"
        ),
    }


def summarize_model_approval(approval: pd.DataFrame, model_id: str) -> dict[str, Any]:
    if approval.empty or "model_id" not in approval.columns:
        return {
            "approved_for_daily": "False",
            "approval_status": "missing",
            "operation_module_id": "",
            "approval_version": "",
            "operation_directive_level": "no_operation_directive",
            "approval_note_zh": "missing approved operation artifact",
            "best_evidence_sample_size": "",
            "best_evidence_win_rate": "",
            "best_evidence_median_return": "",
            "best_evidence_id": "",
        }
    part = approval[approval["model_id"].astype(str).eq(model_id)].copy()
    if part.empty:
        return {
            "approved_for_daily": "False",
            "approval_status": "missing",
            "operation_module_id": "",
            "approval_version": "",
            "operation_directive_level": "no_operation_directive",
            "approval_note_zh": "approved operation artifact has no row for this model",
            "best_evidence_sample_size": "",
            "best_evidence_win_rate": "",
            "best_evidence_median_return": "",
            "best_evidence_id": "",
        }
    row = part.iloc[0]
    approved = "True" if truthy(row.get("approved_for_daily")) else "False"
    return {
        "approved_for_daily": approved,
        "approval_status": safe_str(row.get("approval_status")),
        "operation_module_id": safe_str(row.get("operation_module_id")),
        "approval_version": safe_str(row.get("approval_version")),
        "operation_directive_level": (
            safe_str(row.get("operation_directive_level")) if approved == "True" else "no_operation_directive"
        ),
        "approval_note_zh": safe_str(row.get("approval_note_zh")),
        "best_evidence_sample_size": safe_str(row.get("best_evidence_sample_size")),
        "best_evidence_win_rate": safe_str(row.get("best_evidence_win_rate")),
        "best_evidence_median_return": safe_str(row.get("best_evidence_median_return")),
        "best_evidence_id": safe_str(row.get("best_evidence_id")),
    }


def build_model_operation_readiness(
    parity: pd.DataFrame,
    registry: pd.DataFrame,
    adapter: pd.DataFrame,
    approval: pd.DataFrame | None = None,
    w_bottom_adapter: pd.DataFrame | None = None,
    neckline_adapter: pd.DataFrame | None = None,
    price_pullback_adapter: pd.DataFrame | None = None,
    price_pullback_feature_confirmation: pd.DataFrame | None = None,
    price_pullback_daily_row_parity: pd.DataFrame | None = None,
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    revenue_promotion_registry: pd.DataFrame | None = None,
    revenue_anomaly_registry: pd.DataFrame | None = None,
    revenue_forward_holdout_v2_manifest: pd.DataFrame | None = None,
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    generated_at: str | None = None,
) -> pd.DataFrame:
    if parity.empty:
        raise RuntimeError(f"missing required parity source: {PARITY_CSV}")
    required = {"model_id", "research_baseline_status", "parity_blocker"}
    missing = required - set(parity.columns)
    if missing:
        raise RuntimeError(f"parity source missing columns: {sorted(missing)}")

    generated = generated_at or now_text()
    approval_frame = approval if approval is not None else pd.DataFrame()
    parity_by_model = {
        safe_str(row.get("model_id")): row
        for _, row in parity.iterrows()
    }
    for model_id, model_name in {
        V2_LOW_MODEL_ID: "低位放量攻擊",
        V2_MID_MODEL_ID: "中位動能放量攻擊",
    }.items():
        if model_id not in parity_by_model:
            parity_by_model[model_id] = pd.Series(
                {
                    "model_id": model_id,
                    "model_name_zh": model_name,
                    "research_baseline_status": "production_parity",
                    "parity_blocker": "",
                }
            )

    if V2_HIGH_MODEL_ID not in parity_by_model:
        parity_by_model[V2_HIGH_MODEL_ID] = pd.Series(
            {
                "model_id": V2_HIGH_MODEL_ID,
                "model_name_zh": "高位階放量攻擊",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            }
        )

    volume_approvals = {
        model_id: summarize_model_approval(approval_frame, model_id)
        for model_id in V2_VOLUME_MODEL_IDS
    }
    volume_adapters = {
        model_id: summarize_volume_daily_adapter(adapter, model_id)
        for model_id in V2_VOLUME_MODEL_IDS
    }
    w_bottom_approval = summarize_model_approval(approval_frame, W_BOTTOM_MODEL_ID)
    neckline_approval = summarize_model_approval(approval_frame, NECKLINE_MODEL_ID)
    price_pullback_approval = summarize_model_approval(approval_frame, PRICE_PULLBACK_MODEL_ID)
    w_bottom_adapter_summary = summarize_w_bottom_daily_adapter(
        w_bottom_adapter if w_bottom_adapter is not None else pd.DataFrame(),
        W_BOTTOM_MODEL_ID,
    )
    neckline_adapter_summary = summarize_w_bottom_daily_adapter(
        neckline_adapter if neckline_adapter is not None else pd.DataFrame(),
        NECKLINE_MODEL_ID,
    )
    price_pullback_adapter_summary = summarize_w_bottom_daily_adapter(
        price_pullback_adapter if price_pullback_adapter is not None else pd.DataFrame(),
        PRICE_PULLBACK_MODEL_ID,
    )
    price_pullback_candidate = summarize_price_pullback_candidate(
        price_pullback_feature_confirmation if price_pullback_feature_confirmation is not None else pd.DataFrame(),
        price_pullback_daily_row_parity,
    )
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    revenue_readiness: dict[str, Any] | None = None
    if REVENUE_MODEL_ID in parity_by_model:
        revenue_readiness = summarize_revenue_promotion_readiness(
            revenue_promotion_registry if revenue_promotion_registry is not None else pd.DataFrame(),
            revenue_anomaly_registry if revenue_anomaly_registry is not None else pd.DataFrame(),
            (
                revenue_forward_holdout_v2_manifest
                if revenue_forward_holdout_v2_manifest is not None
                else pd.DataFrame()
            ),
        )
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    rows: list[dict[str, Any]] = []

    def base_from_parity(model_id: str) -> tuple[str, str, str]:
        row = parity_by_model.get(model_id, pd.Series(dtype=str))
        return (
            safe_str(row.get("model_name_zh", "")),
            safe_str(row.get("research_baseline_status", "")),
            safe_str(row.get("parity_blocker", "")),
        )

    def append_non_operation(model_id: str, row: pd.Series) -> None:
        rows.append(
            {
                "generated_at": generated,
                "model_id": model_id,
                "model_name_zh": safe_str(row.get("model_name_zh", "")),
                "parity_status": safe_str(row.get("research_baseline_status", "")),
                "blocker": safe_str(row.get("parity_blocker", "")) or "operation module not validated yet",
                "operation_module_status": "baseline_only_no_validated_operation_module",
                "daily_adapter_status": "not_started",
                "approved_for_daily": "False",
                "approval_status": "not_started",
                "operation_module_id": "",
                "approval_version": "",
                "presentation_allowed": "False",
                "operation_directive_level": "no_operation_directive",
                "pdf_integration_status": "not_started",
                "packet_integration_status": "not_started",
                "registry_pattern_count": 0,
                "registry_current_model_pattern_count": 0,
                "registry_best_pattern_id": "",
                "registry_best_sample_size": 0,
                "registry_best_win_rate": "",
                "registry_best_median_return": "",
                "daily_adapter_row_count": 0,
                "daily_adapter_data_row_count": 0,
                "daily_adapter_sections": "",
                "status_note_zh": "目前只有 research baseline/parameter 對照，沒有 validated operation module，不得產生買入、出場、停損或排序操作建議。",
            }
        )

    for model_id, row in parity_by_model.items():
        if model_id in LEGACY_VOLUME_MODEL_IDS:
            continue
        # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

        if model_id == REVENUE_MODEL_ID:
            if revenue_readiness is None:
                raise RuntimeError("revenue readiness summary was not built")
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": safe_str(row.get("model_name_zh", "")),
                    **revenue_readiness,
                }
            )
            continue
        # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

        if model_id in V2_VOLUME_MODEL_IDS:
            model_name, parity_status, parity_blocker = base_from_parity(model_id)
            approval_info = volume_approvals[model_id]
            adapter_info = volume_adapters[model_id]
            approved = approval_info["approved_for_daily"] == "True"
            adapter_ready = adapter_info["daily_adapter_status"] in {
                "ready_pending_approval_metadata",
                "ready_approved_operation_guidance",
                "ready_empty_no_operation_rows",
            }
            presentation_allowed = approved and adapter_ready and parity_status in {
                "production_parity",
                "production_proxy",
                "proxy_only",
            }
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": model_name,
                    "parity_status": parity_status,
                    "blocker": parity_blocker or ("v2 volume breakout operation adapter is ready" if adapter_ready else "v2 operation adapter is not ready"),
                    "operation_module_status": "approved_operation_v1" if approved else "baseline_only_no_validated_operation_module",
                    "daily_adapter_status": adapter_info["daily_adapter_status"] if approved else "not_started",
                    "approved_for_daily": approval_info["approved_for_daily"],
                    "approval_status": approval_info["approval_status"],
                    "operation_module_id": approval_info["operation_module_id"],
                    "approval_version": approval_info["approval_version"],
                    "presentation_allowed": "True" if presentation_allowed else "False",
                    "operation_directive_level": approval_info["operation_directive_level"] if presentation_allowed else "no_operation_directive",
                    "pdf_integration_status": "pdf_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "packet_integration_status": "packet_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "registry_pattern_count": 1 if approved else 0,
                    "registry_current_model_pattern_count": 1 if approved else 0,
                    "registry_best_pattern_id": approval_info.get("best_evidence_id", ""),
                    "registry_best_sample_size": approval_info.get("best_evidence_sample_size", ""),
                    "registry_best_win_rate": approval_info.get("best_evidence_win_rate", ""),
                    "registry_best_median_return": approval_info.get("best_evidence_median_return", ""),
                    "daily_adapter_row_count": adapter_info["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": adapter_info["daily_adapter_data_row_count"],
                    "daily_adapter_sections": adapter_info["daily_adapter_sections"],
                    "status_note_zh": "v2 放量攻擊正式模型：模型條件加 close-only 確認就是買入 gate；TDCC、MA60/MA120、EMA23 距離僅能作分層或加分，不得作 hidden gate。",
                }
            )
            continue

        if model_id == W_BOTTOM_MODEL_ID:
            adapter_ready = w_bottom_adapter_summary["daily_adapter_status"] in {
                "ready_pending_approval_metadata",
                "ready_approved_operation_guidance",
                "ready_empty_no_operation_rows",
            }
            approved = w_bottom_approval["approved_for_daily"] == "True"
            presentation_allowed = approved and adapter_ready
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": safe_str(row.get("model_name_zh", "")),
                    "parity_status": safe_str(row.get("research_baseline_status", "")),
                    "blocker": safe_str(row.get("parity_blocker", "")) or "W-bottom operation adapter is ready",
                    "operation_module_status": "approved_operation_v2" if approved else "baseline_only_no_validated_operation_module",
                    "daily_adapter_status": w_bottom_adapter_summary["daily_adapter_status"] if approved else "not_started",
                    "approved_for_daily": w_bottom_approval["approved_for_daily"],
                    "approval_status": w_bottom_approval["approval_status"],
                    "operation_module_id": w_bottom_approval["operation_module_id"],
                    "approval_version": w_bottom_approval["approval_version"],
                    "presentation_allowed": "True" if presentation_allowed else "False",
                    "operation_directive_level": w_bottom_approval["operation_directive_level"] if presentation_allowed else "no_operation_directive",
                    "pdf_integration_status": "pdf_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "packet_integration_status": "packet_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "registry_pattern_count": 1 if approved else 0,
                    "registry_current_model_pattern_count": 1 if approved else 0,
                    "registry_best_pattern_id": w_bottom_approval.get("best_evidence_id", ""),
                    "registry_best_sample_size": w_bottom_approval.get("best_evidence_sample_size", ""),
                    "registry_best_win_rate": w_bottom_approval.get("best_evidence_win_rate", ""),
                    "registry_best_median_return": w_bottom_approval.get("best_evidence_median_return", ""),
                    "daily_adapter_row_count": w_bottom_adapter_summary["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": w_bottom_adapter_summary["daily_adapter_data_row_count"],
                    "daily_adapter_sections": w_bottom_adapter_summary["daily_adapter_sections"],
                    "status_note_zh": "W底右側模型已核准為 daily operation guidance，PDF 僅能消費 model-owned operation adapter。",
                }
            )
            continue

        if model_id == NECKLINE_MODEL_ID:
            adapter_ready = neckline_adapter_summary["daily_adapter_status"] in {
                "ready_pending_approval_metadata",
                "ready_approved_operation_guidance",
                "ready_empty_no_operation_rows",
            }
            approved = neckline_approval["approved_for_daily"] == "True"
            presentation_allowed = approved and adapter_ready
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": safe_str(row.get("model_name_zh", "")),
                    "parity_status": safe_str(row.get("research_baseline_status", "")),
                    "blocker": safe_str(row.get("parity_blocker", "")) or "neckline operation adapter is ready",
                    "operation_module_status": "approved_operation_v1" if approved else "baseline_only_no_validated_operation_module",
                    "daily_adapter_status": neckline_adapter_summary["daily_adapter_status"] if approved else "not_started",
                    "approved_for_daily": neckline_approval["approved_for_daily"],
                    "approval_status": neckline_approval["approval_status"],
                    "operation_module_id": neckline_approval["operation_module_id"],
                    "approval_version": neckline_approval["approval_version"],
                    "presentation_allowed": "True" if presentation_allowed else "False",
                    "operation_directive_level": neckline_approval["operation_directive_level"] if presentation_allowed else "no_operation_directive",
                    "pdf_integration_status": "pdf_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "packet_integration_status": "packet_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "registry_pattern_count": 1 if approved else 0,
                    "registry_current_model_pattern_count": 1 if approved else 0,
                    "registry_best_pattern_id": neckline_approval.get("best_evidence_id", ""),
                    "registry_best_sample_size": neckline_approval.get("best_evidence_sample_size", ""),
                    "registry_best_win_rate": neckline_approval.get("best_evidence_win_rate", ""),
                    "registry_best_median_return": neckline_approval.get("best_evidence_median_return", ""),
                    "daily_adapter_row_count": neckline_adapter_summary["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": neckline_adapter_summary["daily_adapter_data_row_count"],
                    "daily_adapter_sections": neckline_adapter_summary["daily_adapter_sections"],
                    "status_note_zh": "W底頸線帶量突破確認模型已核准為 daily operation guidance，PDF 僅能消費 model-owned operation adapter。",
                }
            )
            continue

        if model_id == PRICE_PULLBACK_MODEL_ID and price_pullback_approval["approved_for_daily"] == "True":
            adapter_ready = price_pullback_adapter_summary["daily_adapter_status"] in {
                "ready_approved_operation_guidance",
                "ready_empty_no_operation_rows",
            }
            presentation_allowed = adapter_ready
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": "23EMA回檔模型",
                    "parity_status": safe_str(row.get("research_baseline_status", "")),
                    "blocker": safe_str(row.get("parity_blocker", ""))
                    or (
                        "price_pullback_23ema operation adapter is ready"
                        if adapter_ready
                        else "price_pullback_23ema approval exists, but daily operation adapter is not ready"
                    ),
                    "operation_module_status": "approved_operation_v1",
                    "daily_adapter_status": price_pullback_adapter_summary["daily_adapter_status"] if adapter_ready else "missing",
                    "approved_for_daily": price_pullback_approval["approved_for_daily"],
                    "approval_status": price_pullback_approval["approval_status"],
                    "operation_module_id": price_pullback_approval["operation_module_id"],
                    "approval_version": price_pullback_approval["approval_version"],
                    "presentation_allowed": "True" if presentation_allowed else "False",
                    "operation_directive_level": price_pullback_approval["operation_directive_level"] if presentation_allowed else "no_operation_directive",
                    "pdf_integration_status": "pdf_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "packet_integration_status": "packet_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter",
                    "registry_pattern_count": 1,
                    "registry_current_model_pattern_count": 1,
                    "registry_best_pattern_id": price_pullback_approval.get("best_evidence_id", ""),
                    "registry_best_sample_size": price_pullback_approval.get("best_evidence_sample_size", ""),
                    "registry_best_win_rate": price_pullback_approval.get("best_evidence_win_rate", ""),
                    "registry_best_median_return": price_pullback_approval.get("best_evidence_median_return", ""),
                    "daily_adapter_row_count": price_pullback_adapter_summary["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": price_pullback_adapter_summary["daily_adapter_data_row_count"],
                    "daily_adapter_sections": price_pullback_adapter_summary["daily_adapter_sections"],
                    "status_note_zh": "23EMA回檔模型已核准為 daily operation guidance，PDF 僅能消費 model-owned operation adapter。",
                }
            )
            continue

        if model_id == PRICE_PULLBACK_MODEL_ID and price_pullback_candidate["candidate_ready"] == "True":
            append_non_operation(model_id, row)
            continue

        append_non_operation(model_id, row)

    order = {
        V2_LOW_MODEL_ID: 0,
        V2_MID_MODEL_ID: 1,
        V2_HIGH_MODEL_ID: 2,
        W_BOTTOM_MODEL_ID: 4,
        NECKLINE_MODEL_ID: 5,
        PRICE_PULLBACK_MODEL_ID: 6,
    }
    out = pd.DataFrame(rows)
    out["_order"] = out["model_id"].map(order).fillna(99)
    return out.sort_values(["_order", "model_id"]).drop(columns=["_order"]).reset_index(drop=True)


def write_markdown(df: pd.DataFrame) -> None:
    lines: list[str] = [
        "# Model Operation Readiness",
        "",
        f"- generated_at: `{now_text()}`",
        "- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries",
        "- rule: `approved_for_daily=True` requires an explicit approved operation artifact",
        "- rule: raw research evidence rows can remain research-only even after an operation module is approved",
        "- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則",
        "",
    ]

    if df.empty:
        lines.extend(["sample_status: data_missing", ""])
    else:
        summary_cols = ["operation_module_status", "daily_adapter_status", "approved_for_daily", "presentation_allowed"]
        for col in summary_cols:
            counts = df[col].value_counts().reset_index()
            counts.columns = [col, "count"]
            lines.extend([f"## {col}", "", markdown_table(counts, [col, "count"]), ""])

        show_cols = [
            "model_id",
            "parity_status",
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
            "blocker",
            "status_note_zh",
        ]
        lines.extend(["## Status Table", "", markdown_table(df, show_cols, limit=200), ""])

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    revenue_source_errors = validate_revenue_readiness_source_files()
    if revenue_source_errors:
        raise RuntimeError("; ".join(revenue_source_errors))
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    parity = read_csv(PARITY_CSV, dtype=str).fillna("")
    registry = read_csv(REGISTRY_CSV, dtype=str).fillna("")
    adapter = read_csv(DAILY_VOLUME_ADAPTER_CSV, dtype=str).fillna("")
    w_bottom_adapter = read_csv(DAILY_W_BOTTOM_ADAPTER_CSV, dtype=str).fillna("")
    neckline_adapter = read_csv(DAILY_NECKLINE_ADAPTER_CSV, dtype=str).fillna("")
    price_pullback_adapter = read_csv(DAILY_PRICE_PULLBACK_ADAPTER_CSV, dtype=str).fillna("")
    approval = read_csv(APPROVAL_CSV, dtype=str).fillna("")
    price_pullback_feature_confirmation = read_csv(PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV, dtype=str).fillna("")
    price_pullback_daily_row_parity = read_csv(PRICE_PULLBACK_DAILY_ROW_PARITY_CSV, dtype=str).fillna("")
    # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    revenue_promotion_registry = read_csv(REVENUE_PROMOTION_REGISTRY_CSV, dtype=str).fillna("")
    revenue_anomaly_registry = read_csv(REVENUE_ANOMALY_REGISTRY_CSV, dtype=str).fillna("")
    revenue_forward_holdout_v2_manifest = read_csv(
        REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV, dtype=str
    ).fillna("")
    # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    readiness = build_model_operation_readiness(
        parity,
        registry,
        adapter,
        approval,
        w_bottom_adapter=w_bottom_adapter,
        neckline_adapter=neckline_adapter,
        price_pullback_adapter=price_pullback_adapter,
        price_pullback_feature_confirmation=price_pullback_feature_confirmation,
        price_pullback_daily_row_parity=price_pullback_daily_row_parity,
        # BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
        revenue_promotion_registry=revenue_promotion_registry,
        revenue_anomaly_registry=revenue_anomaly_registry,
        revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest,
        # END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
    )
    write_csv(readiness, OUT_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(readiness, DOCS_CSV)
    write_markdown(readiness)
    print(f"Saved {OUT_CSV} rows={len(readiness)}")
    print(f"Saved {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
