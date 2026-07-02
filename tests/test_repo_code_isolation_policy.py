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
