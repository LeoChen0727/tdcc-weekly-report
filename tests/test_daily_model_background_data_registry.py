from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_daily_model_background_data_registry import load_registry, validate_registry  # noqa: E402
from model_data_independence import strict_csv_rows  # noqa: E402


def registry_rows() -> list[dict[str, str]]:
    errors: list[str] = []
    rows = load_registry(errors)
    assert errors == []
    return rows


def test_daily_model_background_data_registry_passes() -> None:
    assert validate_registry(registry_rows()) == []


def test_snapshot_revision_manifest_is_a_required_background_data_family() -> None:
    rows = [
        row
        for row in registry_rows()
        if row["data_family_id"] != "daily_model_snapshot_revision_manifest"
    ]

    errors = validate_registry(rows)

    assert any("registry missing required background data families" in error for error in errors)
    assert any("daily_model_snapshot_revision_manifest" in error for error in errors)


def test_hot_theme_pullback_research_outputs_are_required() -> None:
    rows = [
        row
        for row in registry_rows()
        if row["data_family_id"]
        != "hot_theme_pullback_published_signal_research_outputs"
    ]

    errors = validate_registry(rows, require_artifacts=False)

    assert any(
        "registry missing required background data families" in error
        for error in errors
    )
    assert any(
        "hot_theme_pullback_published_signal_research_outputs" in error
        for error in errors
    )


def test_pullback_short_reclaim_research_outputs_are_required() -> None:
    rows = [
        row
        for row in registry_rows()
        if row["data_family_id"] != "pullback_short_reclaim_research_outputs"
    ]

    errors = validate_registry(rows, require_artifacts=False)

    assert any(
        "registry missing required background data families" in error
        for error in errors
    )
    assert any(
        "pullback_short_reclaim_research_outputs" in error
        for error in errors
    )


def test_tdcc_stealth_accumulation_research_outputs_are_required() -> None:
    rows = [
        row
        for row in registry_rows()
        if row["data_family_id"]
        != "tdcc_stealth_accumulation_published_signal_research_outputs"
    ]

    errors = validate_registry(rows, require_artifacts=False)

    assert any(
        "registry missing required background data families" in error
        for error in errors
    )
    assert any(
        "tdcc_stealth_accumulation_published_signal_research_outputs" in error
        for error in errors
    )


def test_model_specific_family_cannot_be_all_models() -> None:
    rows = deepcopy(registry_rows())
    for row in rows:
        if row["data_family_id"] == "neckline_context_interpretation":
            row["consumer_models"] = "all_models"
            break

    errors = validate_registry(rows)

    assert any("neckline_context_interpretation" in error for error in errors)
    assert any("model-specific family must list specific consumer_models" in error for error in errors)


def test_revenue_panel_must_stay_coverage_limited() -> None:
    rows = deepcopy(registry_rows())
    for row in rows:
        if row["data_family_id"] == "monthly_revenue_point_in_time_panel":
            row["forbidden_use"] = "use as a formal gate"
            row["validator"] = "not_ready_validator.py"
            break

    errors = validate_registry(rows)

    assert any("monthly_revenue_point_in_time_panel" in error for error in errors)
    assert any("validator path missing" in error for error in errors)


def test_structure_only_mode_allows_registered_artifact_bootstrap_but_full_mode_fails() -> None:
    rows = deepcopy(registry_rows())
    target = next(
        row
        for row in rows
        if row["data_family_id"] == "revenue_unreacted_range_position_shape_transition_matrix"
    )
    target["artifact_path"] = (
        "output/latest/research_backtest/"
        "registered_but_not_yet_built_revenue_artifact_latest.csv"
    )

    full_errors = validate_registry(rows)
    structure_errors = validate_registry(rows, require_artifacts=False)

    assert any("artifact_path does not exist" in error for error in full_errors)
    assert not any("artifact_path does not exist" in error for error in structure_errors)


def test_research_workflow_pre_registers_then_requires_full_artifact_validation() -> None:
    workflow = (ROOT / ".github/workflows/research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )
    structure_command = (
        "python scripts/validate_daily_model_background_data_registry.py --structure-only"
    )
    producer_command = "python scripts/build_revenue_unreacted_range_research.py"
    post_run_marker = "- name: Validate post-run model research contracts"
    full_command = "python scripts/validate_daily_model_background_data_registry.py"
    commit_marker = "- name: Commit research and backtest outputs"

    structure_index = workflow.index(structure_command)
    producer_index = workflow.index(producer_command)
    post_run_index = workflow.index(post_run_marker)
    full_index = workflow.index(full_command, post_run_index)
    commit_index = workflow.index(commit_marker)

    assert structure_index < producer_index < post_run_index < full_index < commit_index


def test_revenue_forward_holdout_is_model_owned_right_censored_and_formal_use_blocked() -> None:
    by_id = {row["data_family_id"]: row for row in registry_rows()}
    row = by_id["revenue_unreacted_range_forward_holdout"]

    assert row["scope"] == "model_research_output"
    assert row["consumer_models"] == "revenue_unreacted_range"
    assert row["validator"] == (
        "scripts/validate_revenue_unreacted_range_forward_holdout.py"
    )
    assert "20260804" in row["point_in_time_status"]
    assert "right_censored" in row["point_in_time_status"]
    assert "bridge-period" in row["forbidden_use"]
    assert "promotion evidence" in row["forbidden_use"]
    assert "quarterly or annual financial statements are excluded" in row["forbidden_use"]
    assert "436c25cd0d037c3425ab2ac4fa76cb464cf96de4" in row["notes"]
    assert row["source_artifacts"].split(";") == [
        "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv",
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
        "data/monthly_revenue_history/monthly_revenue_history.csv",
        "data/stock_price_history/*.csv",
        "config/revenue_unreacted_range_price_comparability_resolution.csv",
        "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv",
    ]
    assert "current exact replay source detail" in row["notes"]
    assert "historical captures do not claim archived independent input replay" in row[
        "notes"
    ]


def test_financial_statement_data_families_are_registered_and_formal_use_is_blocked() -> None:
    by_id = {row["data_family_id"]: row for row in registry_rows()}
    required = {
        "financial_statement_point_in_time_history",
        "financial_statement_source_manifest",
        "financial_statement_pit_coverage_audit",
    }

    assert required <= set(by_id)
    assert by_id["financial_statement_point_in_time_history"]["scope"] == "shared_objective"
    assert "exact company filing availability" in by_id[
        "financial_statement_point_in_time_history"
    ]["forbidden_use"]
    assert by_id["financial_statement_pit_coverage_audit"]["point_in_time_status"] == (
        "coverage_gate_current_snapshot_only_historical_verifier_and_revision_normalizer_unavailable"
    )
    assert "source-specific official evidence parser" in by_id[
        "financial_statement_source_manifest"
    ]["notes"]
    assert "formal_model_use_allowed=False" in by_id[
        "financial_statement_pit_coverage_audit"
    ]["notes"]


def test_registry_loader_fails_on_unquoted_comma_overflow(tmp_path: Path) -> None:
    path = tmp_path / "background.csv"
    path.write_text("data_family_id,notes\nexample,first,second\n", encoding="utf-8")
    errors: list[str] = []
    rows = strict_csv_rows(path, ("data_family_id", "notes"), errors)
    assert rows == []
    assert any("field count 3 does not match header count 2" in error for error in errors)
