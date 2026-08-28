from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, RESEARCH_LATEST_DIR, now_text, read_csv, safe_str  # noqa: E402
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
from sync_revenue_unreacted_range_operation_readiness import (  # noqa: E402
    REVENUE_ANOMALY_DISPOSITION_POLICIES,
    REVENUE_ANOMALY_REGISTRY_CSV,
    REVENUE_EXPECTED_ANOMALIES,
    REVENUE_EXPECTED_PROMOTION_DECISION,
    REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_ID,
    REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
    REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV,
    REVENUE_FORWARD_HOLDOUT_V2_START_DATE,
    REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV,
    REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE,
    REVENUE_MODEL_ID,
    REVENUE_OPERATION_MODULE_STATUS,
    REVENUE_PROMOTION_CONTRACT_VERSION,
    REVENUE_PROMOTION_FINANCIAL_STATEMENT_SCOPE,
    REVENUE_PROMOTION_REGISTRY_CSV,
    REVENUE_RESEARCH_MATRIX_STATUS,
    REVENUE_SOURCE_PROJECTION_MANIFEST_CSV,
    REVENUE_SOURCE_VARIANT_ID,
    summarize_revenue_promotion_readiness,
    sync,
)
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


PARITY_CSV = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.csv"
REGISTRY_CSV = LATEST_DIR / "historical_pattern_operation_registry_latest.csv"
DAILY_VOLUME_ADAPTER_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
DAILY_W_BOTTOM_ADAPTER_CSV = LATEST_DIR / "daily_w_bottom_right_side_operation_section_latest.csv"
DAILY_NECKLINE_ADAPTER_CSV = LATEST_DIR / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"
DAILY_PRICE_PULLBACK_ADAPTER_CSV = LATEST_DIR / "daily_price_pullback_23ema_operation_section_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"
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
    revenue_forward_holdout_v2_detail: pd.DataFrame | None = None,
    revenue_forward_holdout_v2_summary: pd.DataFrame | None = None,
    revenue_forward_holdout_v2_replay_source: pd.DataFrame | None = None,
    revenue_source_projection_manifest: pd.DataFrame | None = None,
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
            holdout_detail=(
                revenue_forward_holdout_v2_detail
                if revenue_forward_holdout_v2_detail is not None
                else read_csv(REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV, dtype=str).fillna("")
            ),
            holdout_summary=(
                revenue_forward_holdout_v2_summary
                if revenue_forward_holdout_v2_summary is not None
                else read_csv(REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV, dtype=str).fillna("")
            ),
            replay_source=(
                revenue_forward_holdout_v2_replay_source
                if revenue_forward_holdout_v2_replay_source is not None
                else read_csv(
                    REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV, dtype=str
                ).fillna("")
            ),
            source_projection_manifest=(
                revenue_source_projection_manifest
                if revenue_source_projection_manifest is not None
                else read_csv(
                    REVENUE_SOURCE_PROJECTION_MANIFEST_CSV, dtype=str
                ).fillna("")
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
    for source_field in ("approved_for_daily", "presentation_allowed"):
        source_values = out[source_field].astype(str).str.strip()
        invalid_source_values = sorted(set(source_values) - {"True", "False"})
        if invalid_source_values:
            raise RuntimeError(
                f"readiness {source_field} contains non-canonical booleans: "
                f"{invalid_source_values}"
            )

    revenue_mask = out["model_id"].astype(str).eq(REVENUE_MODEL_ID)
    if revenue_mask.sum() > 1:
        raise RuntimeError(
            f"readiness must contain at most one {REVENUE_MODEL_ID} row before "
            "persisting revenue-only permission fields"
        )
    for persisted_field in (
        "formal_model_use_allowed",
        "production_allowed",
    ):
        if persisted_field not in out.columns:
            out[persisted_field] = ""
        values = out[persisted_field].fillna("").astype(str).str.strip()
        if revenue_mask.any() and not values[revenue_mask].eq("False").all():
            raise RuntimeError(
                f"{REVENUE_MODEL_ID} readiness {persisted_field} must be explicit False"
            )
        non_revenue_values = values[~revenue_mask]
        if not non_revenue_values.eq("").all():
            conflicting_ids = sorted(
                out.loc[~revenue_mask & values.ne(""), "model_id"]
                .astype(str)
                .tolist()
            )
            raise RuntimeError(
                f"readiness {persisted_field} is revenue-only; legacy model rows must "
                f"remain neutral blank: {conflicting_ids}"
            )
        out[persisted_field] = values

    ordered_columns = list(out.columns)
    for field_name in ("formal_model_use_allowed", "production_allowed"):
        ordered_columns.remove(field_name)
    approved_index = ordered_columns.index("approved_for_daily")
    ordered_columns.insert(approved_index, "formal_model_use_allowed")
    presentation_index = ordered_columns.index("presentation_allowed")
    ordered_columns.insert(presentation_index + 1, "production_allowed")
    out = out[ordered_columns]
    out["_order"] = out["model_id"].map(order).fillna(99)
    return out.sort_values(["_order", "model_id"]).drop(columns=["_order"]).reset_index(drop=True)


def main() -> int:
    # Compatibility entrypoint only. The model-owned sync performs the single
    # canonical exact gate immediately before its exact four-mirror write.
    readiness, diagnostics = sync(ROOT)
    for diagnostic in diagnostics:
        print(f"DIAGNOSTIC: {diagnostic}")
    print(
        "Saved exact four revenue-only readiness mirrors through the model-owned "
        f"sync; rows={len(readiness)}; model_id={REVENUE_MODEL_ID}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
