from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_model_operation_readiness import build_model_operation_readiness  # noqa: E402


def test_volume_breakout_presentation_does_not_change_daily_approval() -> None:
    parity = pd.DataFrame(
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
        ]
    )
    registry = pd.DataFrame(
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
    adapter = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "row_type": "data",
                "pdf_section": "confirmed_operation",
                "adapter_source_status": "ready",
            }
        ]
    )

    readiness = build_model_operation_readiness(parity, registry, adapter, generated_at="2026-06-15 00:00:00 Asia/Taipei")

    volume = readiness[readiness["model_id"].eq("volume_range_breakout")].iloc[0]
    assert volume["operation_module_status"] == "research_reference_ready"
    assert volume["daily_adapter_status"] == "ready_research_reference_only"
    assert volume["presentation_allowed"] == "True"
    assert volume["approved_for_daily"] == "False"
    assert volume["operation_directive_level"] == "research_reference_only"
    assert volume["pdf_integration_status"] == "pending_pdf_renderer"

    pullback = readiness[readiness["model_id"].eq("price_pullback_23ema")].iloc[0]
    assert pullback["operation_module_status"] == "baseline_only_no_validated_operation_module"
    assert pullback["daily_adapter_status"] == "not_started"
    assert pullback["presentation_allowed"] == "False"
    assert pullback["approved_for_daily"] == "False"
    assert pullback["operation_directive_level"] == "no_operation_directive"


def test_missing_volume_adapter_blocks_presentation_without_approval() -> None:
    parity = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            }
        ]
    )
    registry = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "model_hit_status": "current_model_hit",
                "pattern_id": "pullback_10ma_hold_10d",
                "sample_size": "2400",
                "out_of_sample_pass": "True",
            }
        ]
    )

    readiness = build_model_operation_readiness(parity, registry, pd.DataFrame(), generated_at="2026-06-15 00:00:00 Asia/Taipei")

    row = readiness.iloc[0]
    assert row["daily_adapter_status"] == "missing"
    assert row["presentation_allowed"] == "False"
    assert row["approved_for_daily"] == "False"
    assert row["operation_directive_level"] == "no_operation_directive"
