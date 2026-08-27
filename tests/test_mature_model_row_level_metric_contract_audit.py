from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_mature_model_row_level_metric_contract_audit as builder  # noqa: E402
import validate_mature_model_row_level_metric_contract_audit as validator  # noqa: E402


def generic_combo_adapter_row() -> dict[str, str]:
    return {
        "model_id": "synthetic_combo_model",
        "row_type": "data",
        "pdf_view": "highlight",
        "pdf_section": "confirmed_operation",
        "report_line": "mainstream",
        "operation_asof_date": "20260824",
        "stock_id": "9999",
        "stock_name": "合成測試",
        "signal_date": "20260823",
        "operation_quality": "base",
        "win_rate_zh": "70.00%",
        "avg_return_zh": "+5.00%",
        "median_return_zh": "+3.00%",
        "pdf_bonus_combo_id": "pdf_combo__bad",
        "pdf_bonus_combo_sample_size": "10",
        "pdf_bonus_combo_win_rate_zh": "60.00%",
        "pdf_bonus_combo_avg_return_zh": "+1.00%",
        "pdf_bonus_combo_median_return_zh": "+0.50%",
        "row_metric_status": "ready",
        "row_metric_scope": "exact_combo",
        "row_metric_id": "pdf_combo__bad",
        "row_metric_label_zh": "合成組合指標",
        "row_metric_matched_add_score_ids": "synthetic_a|synthetic_b",
        "row_metric_sample_size": "10",
        "row_metric_win_rate_zh": "60.00%",
        "row_metric_neutral_rate_zh": "10.00%",
        "row_metric_failure_rate_zh": "30.00%",
        "row_metric_avg_return_zh": "+1.00%",
        "row_metric_median_return_zh": "+0.50%",
        "row_metric_source": "synthetic_contract_fixture",
        "row_metric_selection_status": "synthetic_exact_combo",
    }


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
    for row in mature.values():
        operation_row_count = int(row["mature_operation_data_row_count"])
        unique_lifecycle_count = int(row["unique_stock_lifecycle_count"])

        # Each formal lifecycle row is represented once in highlight and once
        # in full-view semantic evidence. Daily market data changes the row
        # count, so the contract test must protect view parity, not a snapshot.
        assert operation_row_count == unique_lifecycle_count * 2


def test_price_pullback_technical_strength_uses_row_level_package_metrics() -> None:
    rows = builder.build_rows()
    price = next(row for row in rows if row["model_id"] == "price_pullback_23ema")

    assert price["metric_scope"] == "exact_combo"
    assert price["row_level_metric_status"] == "pass_ready_rows_use_formal_row_metric"
    assert price["combo_recompute_policy_status"] == (
        "pass_exact_package_metric_required_for_multi_feature_technical_strength"
    )
    assert price["combo_worse_policy_status"] == "pass_improves_win_and_avg_vs_baseline"
    assert price["approved_metric_source_status"] == "pass_matches_approved_operation_patterns"
    assert int(price["technical_strength_row_count"]) > 0
    assert int(price["row_metric_ready_count"]) == int(price["technical_strength_row_count"])
    assert int(price["row_metric_baseline_misuse_count"]) == 0


def test_high_position_combo_rows_are_promoted_to_mature_row_level_policy() -> None:
    rows = builder.build_rows()
    high = next(row for row in rows if row["model_id"] == "volume_range_breakout_v2_high_position_volume_attack")

    assert high["audit_scope"] == "mature_model"
    assert high["production_readiness"] == builder.INTEGRATED_CONSUMER_READINESS
    ready_count = int(high["row_metric_ready_count"])
    if ready_count:
        assert high["metric_scope"] in {
            "single_add_score",
            "exact_combo",
            "exact_combo|single_add_score",
        }
    else:
        assert high["metric_scope"] == "no_current_formal_row_metric"
    assert high["pdf_row_display_policy_status"] == (
        "pass_adapter_exposes_row_metric_and_forbids_baseline_substitution"
    )
    assert high["metric_source_parity_status"] == (
        "pass_all_promoted_high_position_metrics_match_research_source"
    )
    assert high["combo_worse_policy_status"] == "pass_exact_combo_or_best_single_fallback_policy"
    assert str(high["non_overlap_status"]).startswith("pass_")
    assert str(high["numerical_anomaly_status"]).startswith("pass_")


@pytest.mark.parametrize(
    "guard_name",
    [
        "validate_operation_row_metric_renderer_contract",
        "validate_daily_operation_packet_row_metric_contract",
    ],
)
def test_integrated_consumer_readiness_fails_closed_on_consumer_regression(
    monkeypatch: pytest.MonkeyPatch,
    guard_name: str,
) -> None:
    monkeypatch.setattr(validator, guard_name, lambda: ["forced row_metric consumer regression"])

    with pytest.raises(SystemExit):
        validator.validate_promoted_high_position(pd.DataFrame(builder.build_rows()))


def test_row_audit_blocks_baseline_substitution_and_uses_only_formal_metrics() -> None:
    rows = builder.build_row_rows("test")

    assert rows
    assert all(row["validation_status"] == "pass" for row in rows)
    assert all(not str(row["baseline_misuse_status"]).startswith("fail") for row in rows)

    w_bottom = [row for row in rows if row["model_id"] == "w_bottom_right_side"]
    assert w_bottom
    assert {row["row_metric_status"] for row in w_bottom} == {
        "unavailable_no_approved_add_score_metric"
    }
    assert all(row["row_metric_id"] == "" for row in w_bottom)

    price = [row for row in rows if row["model_id"] == "price_pullback_23ema"]
    technical = [row for row in price if row["operation_quality"] == "technical_strength"]
    base = [row for row in price if row["operation_quality"] == "base"]
    assert technical and base
    assert {row["row_metric_scope"] for row in technical} == {"exact_combo"}
    assert {row["row_metric_status"] for row in base} == {
        "unavailable_no_approved_add_score_metric"
    }


def test_high_position_promoted_metrics_match_non_overlapping_research_source() -> None:
    source_status, source_issues = builder.high_position_metric_source_parity()
    selection_status, selection_issues = builder.high_position_selection_policy_status()
    non_overlap_status, anomaly_status, detail_issues = builder.high_position_detail_quality_status()

    assert source_status == "pass_all_promoted_high_position_metrics_match_research_source"
    assert source_issues == []
    assert selection_status == "pass_exact_combo_or_best_single_fallback_policy"
    assert selection_issues == []
    assert non_overlap_status == "pass_source_event_key_unique_same_stock_non_overlap_basis"
    assert anomaly_status.startswith("pass_no_single_return_dominates")
    assert detail_issues == []


def test_generic_combo_policy_reports_worse_daily_comparison_as_advisory() -> None:
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
    assert worse_status == (
        "pdf_bonus_combo:advisory_combo_worse_than_baseline="
        "win_rate;avg_return;median_return"
    )
    assert issues == []


def test_generic_combo_policy_keeps_unparseable_metrics_fail_closed() -> None:
    rows = pd.DataFrame(
        [
            {
                "win_rate_zh": "70.00%",
                "avg_return_zh": "+5.00%",
                "median_return_zh": "+3.00%",
                "pdf_bonus_combo_id": "pdf_combo__malformed",
                "pdf_bonus_combo_sample_size": "ten",
                "pdf_bonus_combo_win_rate_zh": "invalid",
                "pdf_bonus_combo_avg_return_zh": "+1.00%",
                "pdf_bonus_combo_median_return_zh": "+0.50%",
            }
        ]
    )

    recompute_status, worse_status, issues = builder.generic_combo_policy_status(rows, ["pdf_bonus_combo"])

    assert recompute_status == "pdf_bonus_combo:fail_unparseable_metric_values"
    assert worse_status == ""
    assert issues == [
        "pdf_bonus_combo:pdf_combo__malformed:unparseable_metric_columns="
        "pdf_bonus_combo_sample_size;pdf_bonus_combo_win_rate_zh"
    ]


def test_technical_package_daily_comparison_is_advisory_but_malformed_is_blocking() -> None:
    worse = pd.DataFrame(
        [
            {
                "win_rate_zh": "70.00%",
                "avg_return_zh": "+5.00%",
                "technical_package_sample_size": "10",
                "technical_package_win_rate_zh": "60.00%",
                "technical_package_neutral_rate_zh": "10.00%",
                "technical_package_failure_rate_zh": "30.00%",
                "technical_package_avg_return_zh": "+1.00%",
            }
        ]
    )
    malformed = worse.copy()
    malformed.loc[0, "technical_package_win_rate_zh"] = "invalid"
    later_row_malformed = pd.concat(
        [
            worse,
            worse.assign(technical_package_neutral_rate_zh="not-a-number"),
        ],
        ignore_index=True,
    )

    assert builder.technical_package_worse_status(worse) == (
        "advisory_technical_package_worse_than_baseline"
    )
    assert builder.technical_package_worse_status(malformed) == (
        "fail_non_numeric_technical_or_base_metric"
    )
    assert builder.technical_package_worse_status(later_row_malformed) == (
        "fail_non_numeric_technical_or_base_metric"
    )


def test_price_pullback_source_status_checks_every_technical_package_row() -> None:
    approved = pd.Series(
        {
            "price_pullback_mature_sample_size": "10",
            "price_pullback_win_rate_pct": "70.00%",
            "price_pullback_neutral_rate_pct": "10.00%",
            "price_pullback_failure_rate_pct": "20.00%",
            "price_pullback_avg_return_pct": "+5.00%",
            "price_pullback_technical_package_sample_size": "10",
            "price_pullback_technical_package_win_rate_pct": "60.00%",
            "price_pullback_technical_package_neutral_rate_pct": "10.00%",
            "price_pullback_technical_package_failure_rate_pct": "30.00%",
            "price_pullback_technical_package_avg_return_pct": "+1.00%",
        }
    )
    valid = pd.DataFrame(
        [
            {
                "sample_size": "10",
                "win_rate_zh": "70.00%",
                "neutral_rate_zh": "10.00%",
                "failure_rate_zh": "20.00%",
                "avg_return_zh": "+5.00%",
                "technical_package_sample_size": "10",
                "technical_package_win_rate_zh": "60.00%",
                "technical_package_neutral_rate_zh": "10.00%",
                "technical_package_failure_rate_zh": "30.00%",
                "technical_package_avg_return_zh": "+1.00%",
            }
        ]
    )
    later_row_conflict = pd.concat(
        [
            valid,
            valid.assign(technical_package_avg_return_zh="+2.00%"),
        ],
        ignore_index=True,
    )

    assert builder.price_pullback_source_status(approved, valid) == (
        "pass_matches_approved_operation_patterns"
    )
    assert "mismatch:technical_package_avg_return_zh" in (
        builder.price_pullback_source_status(approved, later_row_conflict)
    )


def test_validator_does_not_block_advisory_combo_comparison_but_blocks_schema_error(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    adapter_path = tmp_path / "synthetic_combo_adapter.csv"
    row = generic_combo_adapter_row()
    pd.DataFrame([row]).to_csv(adapter_path, index=False, encoding="utf-8-sig")
    monkeypatch.setitem(validator.ADAPTER_BY_MODEL, row["model_id"], adapter_path)

    validator.validate_adapter_model(row["model_id"], pd.DataFrame())

    malformed = dict(row)
    del malformed["pdf_bonus_combo_avg_return_zh"]
    pd.DataFrame([malformed]).to_csv(adapter_path, index=False, encoding="utf-8-sig")
    with pytest.raises(SystemExit):
        validator.validate_adapter_model(row["model_id"], pd.DataFrame())


def test_workflows_run_mature_model_metric_contract_audit() -> None:
    daily = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")
    pr = (ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml").read_text(
        encoding="utf-8"
    )

    for text in [daily, pr]:
        assert "python scripts/build_mature_model_row_level_metric_contract_audit.py" in text
        assert "python scripts/validate_mature_model_row_level_metric_contract_audit.py" in text
    assert "docs/latest/mature_model_row_level_metric_contract_audit_latest.*" in daily
    assert "docs/latest/mature_model_row_level_metric_row_audit_latest.*" in daily
