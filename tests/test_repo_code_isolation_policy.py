from __future__ import annotations

from pathlib import Path

import pandas as pd

from scripts import validate_repo_code_isolation_policy as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_code_isolation_policy_validator_passes() -> None:
    assert validator.main() == 0


def test_model_research_isolation_policy_is_machine_enforced() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    rules = (ROOT / "rules/master_priority_rules.md").read_text(encoding="utf-8")
    assert "model-owned entrypoints" in agents
    assert "cross-model utility migration" in agents
    assert "canonical SHA-256" in rules
    assert "protected mature-model artifact hashes" in rules
    for path in (
        ROOT / "config/model_research_artifact_ownership.csv",
        ROOT / "config/model_research_protected_sentinels.csv",
        ROOT / "config/model_research_shared_utility_registry.csv",
        ROOT / "config/model_research_workflow_entrypoints.csv",
        ROOT / "config/formal_model_evidence_pins.csv",
        ROOT / "scripts/validate_model_research_artifact_ownership.py",
        ROOT / "scripts/validate_model_research_shared_utilities.py",
        ROOT / "scripts/validate_model_research_workflow_isolation.py",
        ROOT / "scripts/validate_formal_model_evidence_pins.py",
        ROOT / "config/daily_model_semantic_ownership.csv",
        ROOT / "config/daily_model_shared_semantic_registry.csv",
        ROOT / "config/daily_model_semantic_migrations.csv",
        ROOT / "config/daily_model_data_sharing_registry.csv",
        ROOT / "config/daily_model_data_sharing_migrations.csv",
        ROOT / "config/daily_model_validator_independence.csv",
        ROOT / "scripts/model_data_independence.py",
        ROOT / "scripts/validate_model_data_independence.py",
        ROOT / "scripts/build_model_data_independence_audit.py",
        ROOT / "config/daily_model_numerical_anomaly_disposition_contract.csv",
        ROOT / "config/daily_operation_adapter_protected_field_contract.csv",
        ROOT / "scripts/validate_daily_operation_adapter_protected_fields.py",
        ROOT / "tests/test_daily_operation_adapter_protected_fields.py",
    ):
        assert path.is_file()
    assert "New formal daily models must use a model-owned production module" in agents
    assert "daily_model_data_sharing_registry.csv" in rules
    assert "Independent promotion evidence validators must not import" in rules
    assert "Numerical magnitude is an investigation trigger, not an anomaly disposition." in rules
    assert "Formal operation-adapter status fields are protected contracts" in rules
    assert "An empty-state workflow run cannot prove non-empty lifecycle coverage." in rules


def test_numerical_anomaly_disposition_requires_bottom_level_evidence() -> None:
    assert validator.validate_numerical_anomaly_governance() == []

    contract = (ROOT / "config/daily_model_numerical_anomaly_disposition_contract.csv").read_text(
        encoding="utf-8"
    )
    assert "unresolved_anomaly_candidate" in contract
    assert "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only" in contract
    assert "verified_real_extreme,True,False,retain_in_primary_metrics" in contract
    assert "independent_source_corroboration" in contract

    artifact = pd.read_csv(
        ROOT
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_extreme_return_path_audit_latest.csv",
        dtype={"stock_id": str},
        keep_default_na=False,
    )
    assert set(artifact["statistical_trigger_status"]) == {"anomaly_candidate"}
    assert set(artifact["final_disposition"]) == {"unresolved_anomaly_candidate"}
    assert artifact["root_cause_checks_missing"].ne("").all()

    formal_pins = (ROOT / "config/formal_model_evidence_pins.csv").read_text(encoding="utf-8")
    for legacy_threshold_artifact in (
        "volume_range_breakout_v2_semantic_audit",
        "volume_range_breakout_v2_raw_market_rerun",
        "volume_range_breakout_v2_condition_matrix",
    ):
        assert legacy_threshold_artifact not in formal_pins


def test_daily_full_pipeline_preserves_pdf_runtime_isolation_gates() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_daily_pdf_shared_path_isolation.py" in workflow_text
    assert "python scripts/validate_daily_pdf_completion_hard_gate.py" in workflow_text


def test_pr_static_workflow_runs_code_isolation_policy() -> None:
    workflow_text = (ROOT / ".github/workflows/individual_stock_pr_validation.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_code_isolation_policy.py" in workflow_text


def test_research_pipeline_runs_model_parity_validator() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_daily_model_research_parity.py" in workflow_text
    assert "python scripts/validate_price_pullback_daily_row_parity.py" in workflow_text


def test_research_pipeline_does_not_refresh_formal_operation_state() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    for forbidden in (
        "python scripts/build_model_operation_readiness.py",
        "python scripts/build_approved_operation_patterns.py",
        "python scripts/build_daily_w_bottom_operation_sections.py",
        "python scripts/build_daily_price_pullback_23ema_operation_section.py",
        "python scripts/update_daily_published_model_snapshots.py",
        "git add output/history/daily_model_snapshots/",
    ):
        assert forbidden not in workflow_text


def test_research_pipeline_uses_model_owned_entrypoints_and_stage_allowlists() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    expected = {
        "run_price_pullback_23ema_research": "price_pullback_23ema",
        "run_revenue_unreacted_range_research": "revenue_unreacted_range",
        "run_volume_range_breakout_v2_research": "volume_range_breakout_v2",
    }
    for workflow_input, artifact_prefix in expected.items():
        assert workflow_input in workflow_text
        assert f"python scripts/build_{artifact_prefix}_research.py" in workflow_text
        assert f"git add output/latest/research_backtest/{artifact_prefix}_*" in workflow_text
        assert f"git add output/history/research/{artifact_prefix}_*" in workflow_text
        assert f"git add docs/latest/{artifact_prefix}_*" in workflow_text

    assert 'default: "true"' not in workflow_text
    assert "run_model_parameter_research" not in workflow_text
    assert "python scripts/build_daily_model_parameter_research.py" not in workflow_text
    assert "git add output/history/research/ || true" not in workflow_text


def test_research_workflow_isolation_validator_runs_on_all_required_surfaces() -> None:
    command = "python scripts/validate_model_research_workflow_isolation.py"
    for path in (
        ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml",
        ROOT / ".github" / "workflows" / "individual_stock_pr_validation.yml",
    ):
        assert command in path.read_text(encoding="utf-8")


def test_research_pipeline_routes_volume_v2_through_model_owned_entrypoint() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_volume_range_breakout_v2_research.py" in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_semantic_audit.py" not in workflow_text
    assert "python scripts/build_volume_range_breakout_v2_candidate_bucket_contract.py" not in workflow_text


def test_research_pipeline_does_not_run_w_bottom_research_or_adapters() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_w_bottom_research_overlap_guardrails.py" not in workflow_text
    assert "python scripts/build_daily_w_bottom_operation_sections.py" not in workflow_text
    assert "git add output/latest/research_backtest/w_bottom_" not in workflow_text


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
