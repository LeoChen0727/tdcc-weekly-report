from __future__ import annotations

from scripts import validate_model_research_workflow_isolation as validator


def _inputs() -> tuple[str, list[validator.WorkflowEntrypoint], dict[str, str]]:
    text = validator.WORKFLOW.read_text(encoding="utf-8")
    return text, validator.load_registry(), validator.load_model_owned_producers()


def test_model_research_workflow_isolation_validator_passes() -> None:
    assert validator.main() == 0


def test_revenue_step_rejects_another_model_producer() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        "          python scripts/build_revenue_unreacted_range_research.py",
        "          python scripts/build_revenue_unreacted_range_research.py\n"
        "          python scripts/build_price_pullback_23ema_research.py",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("mixes producers" in error for error in errors)


def test_research_workflow_rejects_broad_history_stage() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        "          git status --short",
        "          git add output/history/research/ || true\n          git status --short",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("forbidden broad/formal stage path" in error for error in errors)


def test_revenue_step_rejects_embedded_shared_data_refresh() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        "          python scripts/build_revenue_unreacted_range_research.py",
        "          python scripts/build_revenue_unreacted_range_research.py\n"
        "          python scripts/build_monthly_revenue_point_in_time_panel.py",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("contains shared data refresh" in error for error in errors)


def test_research_workflow_rejects_default_true_model_input() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        '      run_revenue_unreacted_range_research:\n'
        '        description: "Run model-owned revenue lag and strength research only"\n'
        "        required: false\n"
        '        default: "false"',
        '      run_revenue_unreacted_range_research:\n'
        '        description: "Run model-owned revenue lag and strength research only"\n'
        "        required: false\n"
        '        default: "true"',
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("must default false" in error for error in errors)


def test_pr_validation_requires_each_registered_model_namespace() -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8").replace(
        '      - "scripts/revenue_unreacted_range_*.py"\n',
        "",
        1,
    )

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any("scripts/revenue_unreacted_range_*.py" in error for error in errors)
