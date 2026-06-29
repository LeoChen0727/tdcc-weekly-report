from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_model_operation_readiness import build_model_operation_readiness  # noqa: E402


def parity_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            },
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "回測23EMA",
                "research_baseline_status": "production_proxy",
                "parity_blocker": "support flags not fully backfilled",
            },
            {
                "model_id": "w_bottom_right_side",
                "model_name_zh": "W bottom right side",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "model_name_zh": "Neckline breakout",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            },
        ]
    )


def registry_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "model_hit_status": "current_model_hit",
                "pattern_id": "pullback_10ma_hold_10d",
                "sample_size": "2400",
                "win_rate": "52.33",
                "avg_return": "3.69",
                "median_return": "0.55",
                "out_of_sample_pass": "True",
            }
        ]
    )


def approval_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "operation_module_id": "volume_breakout_confirmed_operation_v1",
                "approval_version": "volume_breakout_operation_v1_20260615",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_directive_level": "approved_daily_operation_guidance",
            },
            {
                "model_id": "w_bottom_right_side",
                "operation_module_id": "w_bottom_early_entry_operation_v2",
                "approval_version": "w_bottom_early_entry_operation_v2_20260629",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v2",
                "operation_directive_level": "approved_daily_operation_guidance",
                "best_evidence_sample_size": "31",
                "best_evidence_win_rate": "58.0645",
                "best_evidence_median_return": "6.2374",
                "best_evidence_id": "smooth_core_mainstream_right_rebound_5_20_bull",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "operation_module_id": "neckline_strict_45_signal_90_score_v1",
                "approval_version": "neckline_strict_45_signal_90_score_v1_20260629",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_directive_level": "approved_daily_operation_guidance",
                "best_evidence_sample_size": "51",
                "best_evidence_win_rate": "63.8889",
                "best_evidence_median_return": "4.4597",
                "best_evidence_id": "low_position_le60_market_bull",
            }
        ]
    )


def adapter_frame(with_approval_metadata: bool = False) -> pd.DataFrame:
    row = {
        "model_id": "volume_range_breakout",
        "row_type": "data",
        "pdf_section": "confirmed_operation",
        "adapter_source_status": "ready",
    }
    if with_approval_metadata:
        row["approved_for_daily"] = "True"
        row["operation_directive_level"] = "approved_daily_operation_guidance"
    return pd.DataFrame([row])


def test_volume_breakout_approval_promotes_only_volume_model() -> None:
    readiness = build_model_operation_readiness(
        parity_frame(),
        registry_frame(),
        adapter_frame(),
        approval_frame(),
        generated_at="2026-06-15 00:00:00 Asia/Taipei",
    )

    volume = readiness[readiness["model_id"].eq("volume_range_breakout")].iloc[0]
    assert volume["operation_module_status"] == "approved_operation_v1"
    assert volume["daily_adapter_status"] == "ready_pending_approval_metadata"
    assert volume["presentation_allowed"] == "True"
    assert volume["approved_for_daily"] == "True"
    assert volume["approval_status"] == "approved_for_daily_v1"
    assert volume["operation_directive_level"] == "approved_daily_operation_guidance"
    assert volume["pdf_integration_status"] == "pdf_integrated_daily_adapter"
    assert volume["packet_integration_status"] == "packet_integrated_daily_adapter"

    pullback = readiness[readiness["model_id"].eq("price_pullback_23ema")].iloc[0]
    assert pullback["operation_module_status"] == "baseline_only_no_validated_operation_module"
    assert pullback["daily_adapter_status"] == "not_started"
    assert pullback["presentation_allowed"] == "False"
    assert pullback["approved_for_daily"] == "False"
    assert pullback["operation_directive_level"] == "no_operation_directive"

    w_bottom = readiness[readiness["model_id"].eq("w_bottom_right_side")].iloc[0]
    assert w_bottom["operation_module_status"] == "approved_operation_v2"
    assert w_bottom["daily_adapter_status"] == "model_header_evidence_ready"
    assert w_bottom["presentation_allowed"] == "True"
    assert w_bottom["approved_for_daily"] == "True"
    assert w_bottom["operation_module_id"] == "w_bottom_early_entry_operation_v2"
    assert w_bottom["approval_version"] == "w_bottom_early_entry_operation_v2_20260629"
    assert w_bottom["operation_directive_level"] == "approved_daily_operation_guidance"
    assert w_bottom["pdf_integration_status"] == "pdf_model_header_evidence_ready"

    neckline = readiness[readiness["model_id"].eq("neckline_volume_breakout_confirmation")].iloc[0]
    assert neckline["operation_module_status"] == "approved_operation_v1"
    assert neckline["daily_adapter_status"] == "model_header_evidence_ready"
    assert neckline["presentation_allowed"] == "True"
    assert neckline["approved_for_daily"] == "True"
    assert neckline["operation_module_id"] == "neckline_strict_45_signal_90_score_v1"
    assert neckline["approval_version"] == "neckline_strict_45_signal_90_score_v1_20260629"
    assert neckline["operation_directive_level"] == "approved_daily_operation_guidance"
    assert neckline["pdf_integration_status"] == "pdf_model_header_evidence_ready"


def test_volume_adapter_approval_metadata_changes_adapter_status() -> None:
    readiness = build_model_operation_readiness(
        parity_frame().head(1),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        generated_at="2026-06-15 00:00:00 Asia/Taipei",
    )

    row = readiness.iloc[0]
    assert row["daily_adapter_status"] == "ready_approved_operation_guidance"
    assert row["approved_for_daily"] == "True"
    assert row["operation_directive_level"] == "approved_daily_operation_guidance"


def test_missing_volume_adapter_blocks_presentation_even_when_approved() -> None:
    readiness = build_model_operation_readiness(
        parity_frame().head(1),
        registry_frame(),
        pd.DataFrame(),
        approval_frame(),
        generated_at="2026-06-15 00:00:00 Asia/Taipei",
    )

    row = readiness.iloc[0]
    assert row["daily_adapter_status"] == "missing"
    assert row["presentation_allowed"] == "False"
    assert row["approved_for_daily"] == "True"
    assert row["operation_directive_level"] == "no_operation_directive"
