from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_mature_model_row_level_metric_contract_audit as builder  # noqa: E402


def test_builder_covers_all_current_mature_operation_models() -> None:
    rows = builder.build_rows()
    mature = {row["model_id"]: row for row in rows if row["audit_scope"] == "mature_model"}

    assert set(mature) == {
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
        "volume_range_breakout_v2_high_position_volume_attack",
        "w_bottom_right_side",
        "neckline_volume_breakout_confirmation",
        "price_pullback_23ema",
    }
    assert all(row["issues"] == "" for row in mature.values())


def test_price_pullback_technical_strength_uses_row_level_package_metrics() -> None:
    rows = builder.build_rows()
    price = next(row for row in rows if row["model_id"] == "price_pullback_23ema")

    assert price["metric_scope"] == "baseline_plus_technical_package"
    assert price["row_level_metric_status"] == "pass_technical_package_metrics_present_for_technical_strength_rows"
    assert price["combo_recompute_policy_status"] == (
        "pass_exact_package_metric_required_for_multi_feature_technical_strength"
    )
    assert price["combo_worse_policy_status"] == "pass_improves_win_and_avg_vs_baseline"
    assert price["approved_metric_source_status"] == "pass_matches_approved_operation_patterns"
    assert int(price["technical_strength_row_count"]) > 0


def test_high_position_combo_rows_are_promoted_to_mature_row_level_policy() -> None:
    rows = builder.build_rows()
    high = next(row for row in rows if row["model_id"] == "volume_range_breakout_v2_high_position_volume_attack")

    assert high["audit_scope"] == "mature_model"
    assert high["production_readiness"] == "production_adapter_contract_checked"
    assert high["metric_scope"] == "baseline_plus_generic_row_level_combo"
    assert high["pdf_row_display_policy_status"] == (
        "pass_pdf_rows_must_use_row_level_metric_when_operation_quality_or_combo_id_matches"
    )


def test_generic_combo_policy_rejects_worse_promoted_combo() -> None:
    rows = pd.DataFrame(
        [
            {
                "win_rate_zh": "70.00%",
                "avg_return_zh": "+5.00%",
                "median_return_zh": "+3.00%",
                "pdf_bonus_combo_id": "pdf_combo__bad",
                "pdf_bonus_combo_sample_size": "10",
                "pdf_bonus_combo_win_rate_zh": "60.00%",
                "pdf_bonus_combo_avg_return_zh": "+1.00%",
                "pdf_bonus_combo_median_return_zh": "+0.50%",
            }
        ]
    )

    recompute_status, worse_status, issues = builder.generic_combo_policy_status(rows, ["pdf_bonus_combo"])

    assert recompute_status == "pdf_bonus_combo:pass_exact_row_level_metric_fields_present"
    assert worse_status == "pdf_bonus_combo:fail_combo_worse_than_baseline=win_rate;avg_return;median_return"
    assert issues == ["pdf_bonus_combo:pdf_combo__bad:combo_worse_than_baseline"]


def test_workflows_run_mature_model_metric_contract_audit() -> None:
    daily = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")
    pr = (ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml").read_text(
        encoding="utf-8"
    )

    for text in [daily, pr]:
        assert "python scripts/build_mature_model_row_level_metric_contract_audit.py" in text
        assert "python scripts/validate_mature_model_row_level_metric_contract_audit.py" in text
    assert "docs/latest/mature_model_row_level_metric_contract_audit_latest.*" in daily
