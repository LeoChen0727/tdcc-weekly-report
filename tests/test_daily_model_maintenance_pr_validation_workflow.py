from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"


def test_daily_model_maintenance_pr_workflow_exists_for_model_pdf_paths() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "pull_request:" in text
    assert "scripts/generate_chatgpt_side_daily_reports.py" in text
    assert "scripts/run_chatgpt_daily_report_entrypoint.py" in text
    assert "scripts/update_daily_published_model_snapshots.py" in text
    assert "config/daily_pdf_rendered_model_regression_contract.csv" in text
    assert "tests/test_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "tests/test_chatgpt_daily_report_entrypoint.py" in text


def test_daily_model_maintenance_pr_workflow_runs_contract_validators() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_commands = (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_stock_model_contract_registry.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_role_manifest_contract.py",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/validate_daily_published_model_snapshots.py",
        "python scripts/validate_research_against_stock_model_contract.py",
        "python scripts/validate_daily_model_research_parity.py",
        "python scripts/validate_repo_code_isolation_policy.py",
        "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
    )
    for command in required_commands:
        assert command in text


def test_daily_model_maintenance_pr_workflow_runs_focused_pdf_operation_tests() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_tests = (
        "tests/test_chatgpt_daily_report_new_conversation_replay.py",
        "tests/test_chatgpt_daily_report_entrypoint.py",
        "tests/test_daily_pdf_contract_consumers.py",
        "tests/test_daily_published_model_snapshots.py",
        "tests/test_daily_volume_breakout_operation_section.py",
        "tests/test_daily_w_bottom_operation_sections.py",
        "tests/test_daily_price_pullback_23ema_operation_section.py",
        "tests/test_daily_production_boundaries.py",
        "tests/test_stock_model_contract_registry.py",
    )
    for path in required_tests:
        assert path in text


def test_daily_model_maintenance_pr_workflow_runs_actual_pdf_replay_and_uploads_evidence() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "Replay ChatGPT-side daily PDF new conversation" in text
    assert "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "--source-ref \"$source_ref\"" in text
    assert "--output-dir chatgpt_side_outputs_pr_validation" in text
    assert "GITHUB_HEAD_REF" in text
    assert "source_ref=\"origin/${GITHUB_HEAD_REF}\"" in text
    assert "Upload PR daily PDF replay evidence" in text
    assert "actions/upload-artifact@v4" in text
    assert "daily-pdf-replay-pr-validation" in text
    assert "chatgpt_side_outputs_pr_validation/*.pdf" in text
    assert "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json" in text
