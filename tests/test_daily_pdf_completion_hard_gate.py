from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_pdf_completion_hard_gate as validator


ROOT = Path(__file__).resolve().parents[1]


def test_daily_pdf_completion_hard_gate_passes_current_repo() -> None:
    assert validator.validate() == []


def test_completion_gate_rejects_missing_runtime_manifest(tmp_path: Path) -> None:
    output_dir = tmp_path / "chatgpt_side_outputs"
    output_dir.mkdir()

    errors = validator.validate_output_dir(output_dir)

    assert any("runtime manifest" in error for error in errors)


def test_completion_gate_requires_operation_model_regression_contract() -> None:
    assert validator.validate_regression_contract() == []


def test_completion_gate_rejects_pr_workflow_without_post_replay_gate(
    tmp_path: Path, monkeypatch
) -> None:
    full_workflow = tmp_path / "daily_full_pipeline.yml"
    pr_workflow = tmp_path / "daily_model_maintenance_pr_validation.yml"
    gate_file = tmp_path / "validate_daily_pdf_completion_hard_gate.py"
    replay_file = tmp_path / "validate_chatgpt_daily_report_new_conversation_replay.py"
    gate_file.write_text("# gate\n", encoding="utf-8")
    replay_file.write_text("# replay\n", encoding="utf-8")

    full_workflow.write_text(
        "\n".join(
            [
                *validator.REQUIRED_STATIC_VALIDATORS,
                validator.STATIC_COMPLETION_GATE_COMMAND,
                "- name: Replay ChatGPT-side daily PDF new conversation",
                validator.REPLAY_COMMAND,
                "PDF replay output_dir=chatgpt_side_outputs_new_conversation_replay",
                "--output-dir chatgpt_side_outputs_new_conversation_replay",
                validator.DAILY_FULL_OUTPUT_GATE_COMMAND,
                "- name: Dispatch and wait for GitHub Pages deploy",
            ]
        ),
        encoding="utf-8",
    )
    pr_workflow.write_text(
        "\n".join(
            [
                *validator.REQUIRED_PR_VALIDATORS,
                validator.STATIC_COMPLETION_GATE_COMMAND,
                "tests/test_daily_pdf_completion_hard_gate.py",
                "- name: Replay ChatGPT-side daily PDF new conversation",
                validator.REPLAY_COMMAND,
                "PDF replay output_dir=chatgpt_side_outputs_pr_validation",
                "--output-dir chatgpt_side_outputs_pr_validation",
                "- name: Upload PR daily PDF replay evidence",
                "chatgpt_side_outputs_pr_validation/*.pdf",
                "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json",
                "if-no-files-found: error",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(validator, "DAILY_FULL_WORKFLOW", full_workflow)
    monkeypatch.setattr(validator, "DAILY_MODEL_PR_WORKFLOW", pr_workflow)
    monkeypatch.setattr(validator, "COMPLETION_GATE", gate_file)
    monkeypatch.setattr(validator, "REPLAY_VALIDATOR", replay_file)

    errors = validator.validate_workflow_gates()

    assert any(validator.PR_OUTPUT_GATE_COMMAND in error for error in errors)
