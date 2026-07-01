from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_text, read_csv, safe_str, write_csv  # noqa: E402


PARITY_CSV = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.csv"
REGISTRY_CSV = LATEST_DIR / "historical_pattern_operation_registry_latest.csv"
DAILY_VOLUME_ADAPTER_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
DAILY_W_BOTTOM_ADAPTER_CSV = LATEST_DIR / "daily_w_bottom_right_side_operation_section_latest.csv"
DAILY_NECKLINE_ADAPTER_CSV = LATEST_DIR / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"
APPROVAL_CSV = LATEST_DIR / "approved_operation_patterns_latest.csv"

OUT_CSV = LATEST_DIR / "model_operation_readiness_latest.csv"
OUT_MD = LATEST_DIR / "model_operation_readiness_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

VOLUME_MODEL_ID = "volume_range_breakout"
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
PRICE_PULLBACK_BUY_FILTER_ID = "tdcc_high_thresholds_up_return20_0_25"


def truthy(value: Any) -> bool:
    text = safe_str(value).lower()
    return text in {"true", "1", "1.0", "yes", "y"}


def summarize_volume_registry(registry: pd.DataFrame) -> dict[str, Any]:
    empty = {
        "operation_module_status": "registry_missing",
        "registry_pattern_count": 0,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": "",
        "registry_best_sample_size": 0,
        "registry_best_win_rate": "",
        "registry_best_median_return": "",
    }
    if registry.empty or "model_id" not in registry.columns:
        return empty

    part = registry[registry["model_id"].astype(str).eq(VOLUME_MODEL_ID)].copy()
    if part.empty:
        return empty

    current = part[part.get("model_hit_status", "").astype(str).eq("current_model_hit")].copy()
    if current.empty:
        current = part.copy()

    if "out_of_sample_pass" in current.columns:
        oos = current[current["out_of_sample_pass"].map(truthy)]
        if not oos.empty:
            current = oos

    for col in ["sample_size", "win_rate", "avg_return", "median_return", "profit_factor"]:
        if col in current.columns:
            current[col] = pd.to_numeric(current[col], errors="coerce")

    sort_cols = [col for col in ["median_return", "avg_return", "win_rate", "sample_size"] if col in current.columns]
    best = current.sort_values(sort_cols, ascending=[False] * len(sort_cols)).iloc[0] if sort_cols else current.iloc[0]

    return {
        "operation_module_status": "research_reference_ready",
        "registry_pattern_count": len(part),
        "registry_current_model_pattern_count": int(
            part.get("model_hit_status", pd.Series(dtype=str)).astype(str).eq("current_model_hit").sum()
        ),
        "registry_best_pattern_id": safe_str(best.get("pattern_id", "")),
        "registry_best_sample_size": int(float(best.get("sample_size", 0) or 0)),
        "registry_best_win_rate": safe_str(best.get("win_rate", "")),
        "registry_best_median_return": safe_str(best.get("median_return", "")),
    }


def summarize_volume_daily_adapter(adapter: pd.DataFrame) -> dict[str, Any]:
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
    data_source_statuses = sorted(
        set(adapter.loc[row_type.eq("data"), "adapter_source_status"].astype(str))
        if "adapter_source_status" in adapter.columns
        else set()
    )
    base_ready = models == [VOLUME_MODEL_ID] and data_rows > 0 and (
        not data_source_statuses or data_source_statuses == ["ready"]
    )
    empty_sections_ready = (
        models == [VOLUME_MODEL_ID]
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


def summarize_volume_approval(approval: pd.DataFrame) -> dict[str, Any]:
    if approval.empty or "model_id" not in approval.columns:
        return {
            "approved_for_daily": "False",
            "approval_status": "missing",
            "operation_module_id": "",
            "approval_version": "",
            "operation_directive_level": "no_operation_directive",
            "approval_note_zh": "尚未建立 approved operation artifact。",
        }
    part = approval[approval["model_id"].astype(str).eq(VOLUME_MODEL_ID)].copy()
    if part.empty:
        return {
            "approved_for_daily": "False",
            "approval_status": "missing",
            "operation_module_id": "",
            "approval_version": "",
            "operation_directive_level": "no_operation_directive",
            "approval_note_zh": "尚未批准放量攻擊操作模組。",
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
    price_pullback_feature_confirmation: pd.DataFrame | None = None,
    price_pullback_daily_row_parity: pd.DataFrame | None = None,
    generated_at: str | None = None,
) -> pd.DataFrame:
    if parity.empty:
        raise RuntimeError(f"missing required parity source: {PARITY_CSV}")
    required = {"model_id", "research_baseline_status", "parity_blocker"}
    missing = required - set(parity.columns)
    if missing:
        raise RuntimeError(f"parity source missing columns: {sorted(missing)}")

    generated = generated_at or now_text()
    volume_registry = summarize_volume_registry(registry)
    volume_adapter = summarize_volume_daily_adapter(adapter)
    w_bottom_adapter_summary = summarize_w_bottom_daily_adapter(
        w_bottom_adapter if w_bottom_adapter is not None else pd.DataFrame(),
        W_BOTTOM_MODEL_ID,
    )
    neckline_adapter_summary = summarize_w_bottom_daily_adapter(
        neckline_adapter if neckline_adapter is not None else pd.DataFrame(),
        NECKLINE_MODEL_ID,
    )
    approval_frame = approval if approval is not None else pd.DataFrame()
    volume_approval = summarize_volume_approval(approval_frame)
    w_bottom_approval = summarize_model_approval(approval_frame, W_BOTTOM_MODEL_ID)
    neckline_approval = summarize_model_approval(approval_frame, NECKLINE_MODEL_ID)
    price_pullback_candidate = summarize_price_pullback_candidate(
        price_pullback_feature_confirmation if price_pullback_feature_confirmation is not None else pd.DataFrame(),
        price_pullback_daily_row_parity,
    )
    volume_approved = volume_approval["approved_for_daily"] == "True"
    w_bottom_approved = w_bottom_approval["approved_for_daily"] == "True"
    neckline_approved = neckline_approval["approved_for_daily"] == "True"
    adapter_ready = volume_adapter["daily_adapter_status"] in {
        "ready_pending_approval_metadata",
        "ready_approved_operation_guidance",
        "ready_empty_no_operation_rows",
    }
    volume_presentation_allowed = volume_registry["operation_module_status"] == "research_reference_ready" and adapter_ready

    rows: list[dict[str, Any]] = []
    for _, row in parity.iterrows():
        model_id = safe_str(row.get("model_id", ""))
        model_name = safe_str(row.get("model_name_zh", ""))
        parity_status = safe_str(row.get("research_baseline_status", ""))
        parity_blocker = safe_str(row.get("parity_blocker", ""))

        if model_id == VOLUME_MODEL_ID:
            blocker = (
                "daily adapter approval metadata pending"
                if volume_adapter["daily_adapter_status"] == "ready_pending_approval_metadata"
                else "每日 adapter 目前無操作列；PDF/packet 顯示明確空狀態操作區塊"
                if volume_adapter["daily_adapter_status"] == "ready_empty_no_operation_rows"
                else "PDF/packet 已接每日 adapter 資料成品"
            )
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": model_name,
                    "parity_status": parity_status,
                    "blocker": blocker,
                    "operation_module_status": (
                        "approved_operation_v1" if volume_approved else volume_registry["operation_module_status"]
                    ),
                    "daily_adapter_status": volume_adapter["daily_adapter_status"],
                    "approved_for_daily": volume_approval["approved_for_daily"],
                    "approval_status": volume_approval["approval_status"],
                    "operation_module_id": volume_approval["operation_module_id"],
                    "approval_version": volume_approval["approval_version"],
                    "presentation_allowed": "True" if volume_presentation_allowed else "False",
                    "operation_directive_level": (
                        volume_approval["operation_directive_level"]
                        if volume_presentation_allowed and volume_approved
                        else ("research_reference_only" if volume_presentation_allowed else "no_operation_directive")
                    ),
                    "pdf_integration_status": "pdf_integrated_daily_adapter",
                    "packet_integration_status": "packet_integrated_daily_adapter",
                    "registry_pattern_count": volume_registry["registry_pattern_count"],
                    "registry_current_model_pattern_count": volume_registry["registry_current_model_pattern_count"],
                    "registry_best_pattern_id": volume_registry.get("registry_best_pattern_id", ""),
                    "registry_best_sample_size": volume_registry["registry_best_sample_size"],
                    "registry_best_win_rate": volume_registry["registry_best_win_rate"],
                    "registry_best_median_return": volume_registry["registry_best_median_return"],
                    "daily_adapter_row_count": volume_adapter["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": volume_adapter["daily_adapter_data_row_count"],
                    "daily_adapter_sections": volume_adapter["daily_adapter_sections"],
                    "status_note_zh": (
                        "放量攻擊 v1 已由 approved_operation_patterns 批准為 daily 操作建議；"
                        "只有已確認列可列買進排名，待確認列只作觀察。PDF/packet 仍只能讀每日 adapter 資料成品。"
                    ),
                }
            )
            continue

        if model_id == W_BOTTOM_MODEL_ID:
            adapter_ready = w_bottom_adapter_summary["daily_adapter_status"] in {
                "ready_pending_approval_metadata",
                "ready_approved_operation_guidance",
                "ready_empty_no_operation_rows",
            }
            presentation_allowed = w_bottom_approved and parity_status in {
                "production_parity",
                "production_proxy",
                "proxy_only",
            } and adapter_ready
            blocker = parity_blocker or (
                "W-bottom early-entry operation v2 adapter is ready; positive-return rate and average return must be labeled as D+20/D+40 operation metrics"
                if adapter_ready
                else "W-bottom early-entry operation v2 approval exists, but daily operation section adapter is not ready"
            )
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": model_name,
                    "parity_status": parity_status,
                    "blocker": blocker,
                    "operation_module_status": (
                        "approved_operation_v2" if w_bottom_approved else "baseline_only_no_validated_operation_module"
                    ),
                    "daily_adapter_status": w_bottom_adapter_summary["daily_adapter_status"] if w_bottom_approved else "not_started",
                    "approved_for_daily": w_bottom_approval["approved_for_daily"],
                    "approval_status": w_bottom_approval["approval_status"],
                    "operation_module_id": w_bottom_approval["operation_module_id"],
                    "approval_version": w_bottom_approval["approval_version"],
                    "presentation_allowed": "True" if presentation_allowed else "False",
                    "operation_directive_level": (
                        w_bottom_approval["operation_directive_level"] if presentation_allowed else "no_operation_directive"
                    ),
                    "pdf_integration_status": (
                        "pdf_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter"
                    ),
                    "packet_integration_status": (
                        "packet_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter"
                    ),
                    "registry_pattern_count": 1 if w_bottom_approved else 0,
                    "registry_current_model_pattern_count": 1 if w_bottom_approved else 0,
                    "registry_best_pattern_id": w_bottom_approval.get("best_evidence_id", ""),
                    "registry_best_sample_size": w_bottom_approval.get("best_evidence_sample_size", ""),
                    "registry_best_win_rate": w_bottom_approval.get("best_evidence_win_rate", ""),
                    "registry_best_median_return": w_bottom_approval.get("best_evidence_median_return", ""),
                    "daily_adapter_row_count": w_bottom_adapter_summary["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": w_bottom_adapter_summary["daily_adapter_data_row_count"],
                    "daily_adapter_sections": w_bottom_adapter_summary["daily_adapter_sections"],
                    "status_note_zh": (
                        "W底右低點早期進場 v2 已由 approved_operation_patterns 批准；"
                        "此模型使用標題下方證據，不共用放量攻擊 operation section adapter。"
                    ),
                }
            )
            continue

        if model_id == NECKLINE_MODEL_ID:
            adapter_ready = neckline_adapter_summary["daily_adapter_status"] in {
                "ready_pending_approval_metadata",
                "ready_approved_operation_guidance",
                "ready_empty_no_operation_rows",
            }
            presentation_allowed = neckline_approved and parity_status in {
                "production_parity",
                "production_proxy",
                "proxy_only",
            } and adapter_ready
            blocker = parity_blocker or (
                "neckline strict 45 signal / 90 score operation adapter is ready; operation-rule win rate and neutral-inclusive success rate must be labeled separately"
                if adapter_ready
                else "neckline strict 45 signal / 90 score operation approval exists, but daily operation section adapter is not ready"
            )
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": model_name,
                    "parity_status": parity_status,
                    "blocker": blocker,
                    "operation_module_status": (
                        "approved_operation_v1" if neckline_approved else "baseline_only_no_validated_operation_module"
                    ),
                    "daily_adapter_status": neckline_adapter_summary["daily_adapter_status"] if neckline_approved else "not_started",
                    "approved_for_daily": neckline_approval["approved_for_daily"],
                    "approval_status": neckline_approval["approval_status"],
                    "operation_module_id": neckline_approval["operation_module_id"],
                    "approval_version": neckline_approval["approval_version"],
                    "presentation_allowed": "True" if presentation_allowed else "False",
                    "operation_directive_level": (
                        neckline_approval["operation_directive_level"] if presentation_allowed else "no_operation_directive"
                    ),
                    "pdf_integration_status": (
                        "pdf_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter"
                    ),
                    "packet_integration_status": (
                        "packet_integrated_daily_adapter" if presentation_allowed else "pending_daily_operation_adapter"
                    ),
                    "registry_pattern_count": 1 if neckline_approved else 0,
                    "registry_current_model_pattern_count": 1 if neckline_approved else 0,
                    "registry_best_pattern_id": neckline_approval.get("best_evidence_id", ""),
                    "registry_best_sample_size": neckline_approval.get("best_evidence_sample_size", ""),
                    "registry_best_win_rate": neckline_approval.get("best_evidence_win_rate", ""),
                    "registry_best_median_return": neckline_approval.get("best_evidence_median_return", ""),
                    "daily_adapter_row_count": neckline_adapter_summary["daily_adapter_row_count"],
                    "daily_adapter_data_row_count": neckline_adapter_summary["daily_adapter_data_row_count"],
                    "daily_adapter_sections": neckline_adapter_summary["daily_adapter_sections"],
                    "status_note_zh": (
                        "W底頸線帶量突破 v1 已由 approved_operation_patterns 批准；45日 context 是入選訊號，"
                        "90日 context 只作分數與風險調整；此模型使用標題下方證據，不共用放量攻擊 operation section adapter，也不混入其他頸線型態。"
                    ),
                }
            )
            continue

        if model_id == PRICE_PULLBACK_MODEL_ID and price_pullback_candidate["candidate_ready"] == "True":
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": model_id,
                    "model_name_zh": model_name,
                    "parity_status": parity_status,
                    "blocker": price_pullback_candidate["row_parity_blocker"]
                    or (
                        "daily row parity audit has no failing rows, but an explicit promotion/sync PR and "
                        "formal daily operation-row adapter/PDF section contract are still required before "
                        "production operation guidance"
                    ),
                    "operation_module_status": price_pullback_candidate["operation_module_status"],
                    "daily_adapter_status": price_pullback_candidate["daily_adapter_status"],
                    "approved_for_daily": "False",
                    "approval_status": price_pullback_candidate["approval_status"],
                    "operation_module_id": price_pullback_candidate["operation_module_id"],
                    "approval_version": price_pullback_candidate["approval_version"],
                    "presentation_allowed": "False",
                    "operation_directive_level": "no_operation_directive",
                    "pdf_integration_status": price_pullback_candidate["pdf_integration_status"],
                    "packet_integration_status": price_pullback_candidate["packet_integration_status"],
                    "registry_pattern_count": price_pullback_candidate["registry_pattern_count"],
                    "registry_current_model_pattern_count": price_pullback_candidate[
                        "registry_current_model_pattern_count"
                    ],
                    "registry_best_pattern_id": price_pullback_candidate["registry_best_pattern_id"],
                    "registry_best_sample_size": price_pullback_candidate["registry_best_sample_size"],
                    "registry_best_win_rate": price_pullback_candidate["registry_best_win_rate"],
                    "registry_best_median_return": price_pullback_candidate["registry_best_median_return"],
                    "daily_adapter_row_count": 0,
                    "daily_adapter_data_row_count": 0,
                    "daily_adapter_sections": "",
                    "status_note_zh": price_pullback_candidate["status_note_zh"],
                }
            )
            continue

        blocker = parity_blocker or "operation module not validated yet"
        rows.append(
            {
                "generated_at": generated,
                "model_id": model_id,
                "model_name_zh": model_name,
                "parity_status": parity_status,
                "blocker": blocker,
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
                "status_note_zh": (
                    "目前只完成 research baseline/parameter 對照；尚未有 validated operation module，"
                    "不可產生買進、賣出、停損或排名操作建議。"
                ),
            }
        )

    order = {VOLUME_MODEL_ID: 0, W_BOTTOM_MODEL_ID: 1, NECKLINE_MODEL_ID: 2, PRICE_PULLBACK_MODEL_ID: 3}
    out = pd.DataFrame(rows)
    out["_order"] = out["model_id"].map(order).fillna(9)
    out = out.sort_values(["_order", "model_id"]).drop(columns=["_order"]).reset_index(drop=True)
    return out


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
    parity = read_csv(PARITY_CSV, dtype=str).fillna("")
    registry = read_csv(REGISTRY_CSV, dtype=str).fillna("")
    adapter = read_csv(DAILY_VOLUME_ADAPTER_CSV, dtype=str).fillna("")
    w_bottom_adapter = read_csv(DAILY_W_BOTTOM_ADAPTER_CSV, dtype=str).fillna("")
    neckline_adapter = read_csv(DAILY_NECKLINE_ADAPTER_CSV, dtype=str).fillna("")
    approval = read_csv(APPROVAL_CSV, dtype=str).fillna("")
    price_pullback_feature_confirmation = read_csv(PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV, dtype=str).fillna("")
    price_pullback_daily_row_parity = read_csv(PRICE_PULLBACK_DAILY_ROW_PARITY_CSV, dtype=str).fillna("")
    readiness = build_model_operation_readiness(
        parity,
        registry,
        adapter,
        approval,
        w_bottom_adapter=w_bottom_adapter,
        neckline_adapter=neckline_adapter,
        price_pullback_feature_confirmation=price_pullback_feature_confirmation,
        price_pullback_daily_row_parity=price_pullback_daily_row_parity,
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
