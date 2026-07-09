from __future__ import annotations

from pathlib import Path

from scripts import validate_repo_code_isolation_policy as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_code_isolation_policy_validator_passes() -> None:
    assert validator.main() == 0


def test_daily_full_pipeline_runs_code_isolation_gates() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_code_isolation_policy.py" in workflow_text
    assert "python scripts/validate_chatgpt_side_pdf_layout_independence.py" in workflow_text
    assert "python scripts/validate_daily_pdf_shared_path_isolation.py" in workflow_text
    assert "python scripts/validate_daily_pdf_completion_hard_gate.py" in workflow_text


def test_daily_boundary_validator_runs_code_isolation_policy() -> None:
    boundary_text = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "validate_repo_code_isolation_policy.py" in boundary_text


def test_research_pipeline_runs_model_parity_validator() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_daily_model_research_parity.py" in workflow_text
    assert "python scripts/validate_price_pullback_daily_row_parity.py" in workflow_text


def test_research_pipeline_runs_model_operation_readiness_validator() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_model_operation_readiness.py" in workflow_text
    assert "python scripts/validate_model_operation_readiness.py" in workflow_text


def test_research_pipeline_stages_price_pullback_feature_confirmation_outputs() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "output/latest/research_backtest/price_pullback_23ema_feature_confirmation_research_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_feature_confirmation_research_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_feature_confirmation_research_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_feature_confirmation_research_latest.md" in workflow_text
    assert "output/history/research/price_pullback_23ema_feature_confirmation_research.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_daily_row_parity_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_daily_row_parity_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_daily_row_parity_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_daily_row_parity_latest.md" in workflow_text
    assert "output/history/research/price_pullback_23ema_daily_row_parity.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_model_decision_audit_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_model_decision_audit_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_model_decision_audit_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_model_decision_audit_latest.md" in workflow_text
    assert "output/history/research/price_pullback_23ema_model_decision_audit.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_high_return_feature_score_grid_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_high_return_feature_score_grid_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_high_return_feature_score_grid_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_high_return_feature_score_grid_latest.md" in workflow_text
    assert "output/history/research/price_pullback_23ema_high_return_feature_score_grid.csv" in workflow_text
    assert "python scripts/validate_daily_model_revenue_condition_matrix.py" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_revenue_condition_matrix_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_revenue_condition_matrix_latest.md" in workflow_text
    assert "python scripts/validate_price_pullback_promotion_matrix.py" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_promotion_matrix_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_promotion_matrix_latest.md" in workflow_text
    assert "output/latest/research_backtest/revenue_unreacted_range_revenue_condition_matrix_latest.csv" in workflow_text
    assert "output/latest/research_backtest/revenue_unreacted_range_revenue_condition_matrix_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_revenue_condition_matrix_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_revenue_condition_matrix_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_promotion_matrix_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_promotion_matrix_latest.md" in workflow_text
    assert "docs/latest/revenue_unreacted_range_revenue_condition_matrix_latest.csv" in workflow_text
    assert "docs/latest/revenue_unreacted_range_revenue_condition_matrix_latest.md" in workflow_text
    assert "output/history/research/price_pullback_23ema_revenue_condition_matrix.csv" in workflow_text
    assert "output/history/research/price_pullback_23ema_promotion_matrix.csv" in workflow_text
    assert "output/history/research/revenue_unreacted_range_revenue_condition_matrix.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_lifecycle_replay_latest.csv" in workflow_text
    assert "output/latest/research_backtest/price_pullback_23ema_lifecycle_replay_latest.md" in workflow_text
    assert "docs/latest/price_pullback_23ema_lifecycle_replay_latest.csv" in workflow_text
    assert "docs/latest/price_pullback_23ema_lifecycle_replay_latest.md" in workflow_text
    assert "output/history/research/price_pullback_23ema_lifecycle_replay.csv" in workflow_text


def test_research_pipeline_runs_approved_operation_validator() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_approved_operation_patterns.py" in workflow_text
    assert "python scripts/validate_approved_operation_patterns.py" in workflow_text


def test_research_pipeline_runs_volume_range_breakout_v2_overlap_sensitivity_validator() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_volume_range_breakout_v2_semantic_audit.py" in workflow_text
    assert "python scripts/validate_volume_range_breakout_v2_semantic_audit.py" in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_overlap_sensitivity.py" in workflow_text
    assert "python scripts/validate_volume_range_breakout_v2_overlap_sensitivity.py" in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_split_feature_audit.py" in workflow_text
    assert "python scripts/validate_volume_range_breakout_v2_split_feature_audit.py" in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_research_contract.py" in workflow_text
    assert "python scripts/validate_volume_range_breakout_v2_research_contract.py" in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_promotion_readiness_audit.py" in workflow_text
    assert "python scripts/validate_volume_range_breakout_v2_promotion_readiness_audit.py" in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_position_shape_matrix.py" in workflow_text
    assert "python scripts/validate_volume_range_breakout_v2_position_shape_matrix.py" in workflow_text
    assert "output/latest/research_backtest/volume_range_breakout_v2_*_latest.csv" in workflow_text
    assert "output/latest/research_backtest/volume_range_breakout_v2_*_latest.md" in workflow_text


def test_research_pipeline_runs_w_bottom_overlap_guardrail_validator() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_w_bottom_research_overlap_guardrails.py" in workflow_text
    assert "python scripts/validate_w_bottom_research_overlap_guardrails.py" in workflow_text
    assert "output/latest/research_backtest/w_bottom_research_overlap_guardrails_latest.csv" in workflow_text
    assert "output/latest/research_backtest/w_bottom_research_overlap_guardrails_latest.md" in workflow_text
    assert "output/history/research/w_bottom_research_overlap_guardrails.csv" in workflow_text


def test_research_pipeline_does_not_stage_daily_route_files() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python build_chatgpt_daily_report_packet.py" not in workflow_text
    assert "python build_chatgpt_daily_report_rules.py" not in workflow_text
    assert "python publish_chatgpt_report_readme_and_check.py" not in workflow_text
    assert "git add output/latest/CHATGPT_DAILY_REPORT" not in workflow_text
    assert "git add output/latest/READ_ME_FIRST_DAILY_REPORT" not in workflow_text
    assert "git add docs/latest/ || true" not in workflow_text
