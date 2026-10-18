from __future__ import annotations

from copy import deepcopy
import csv
from pathlib import Path

import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_daily_model_background_data_registry import load_registry, validate_registry  # noqa: E402
from model_data_independence import strict_csv_rows  # noqa: E402
import validate_daily_model_background_data_registry as background_validator  # noqa: E402


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


def test_tdcc_stealth_accumulation_pit_replay_availability_audit_is_required() -> None:
    rows = [
        row
        for row in registry_rows()
        if row["data_family_id"]
        != "tdcc_stealth_accumulation_pit_replay_availability_audit"
    ]

    errors = validate_registry(rows, require_artifacts=False)

    assert any(
        "registry missing required background data families" in error
        for error in errors
    )
    assert any(
        "tdcc_stealth_accumulation_pit_replay_availability_audit" in error
        for error in errors
    )


def test_tdcc_stealth_historical_selector_replay_outputs_are_required() -> None:
    family = "tdcc_stealth_accumulation_historical_selector_replay_outputs"
    rows = [row for row in registry_rows() if row["data_family_id"] != family]

    errors = validate_registry(rows, require_artifacts=False)

    assert any(
        "registry missing required background data families" in error
        and family in error
        for error in errors
    )


def test_tdcc_short_term_continuation_d5_d10_research_outputs_are_required() -> None:
    rows = [
        row
        for row in registry_rows()
        if row["data_family_id"]
        != "tdcc_short_term_continuation_d5_d10_research_outputs"
    ]

    errors = validate_registry(rows, require_artifacts=False)

    assert any(
        "registry missing required background data families" in error
        for error in errors
    )
    assert any(
        "tdcc_short_term_continuation_d5_d10_research_outputs" in error
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


def write_forward_capture_csv(path: Path, columns: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


@pytest.fixture
def forward_capture_fixture(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, dict[str, str]]:
    family = "price_pullback_23ema_operation_section"
    row = deepcopy(next(item for item in registry_rows() if item["data_family_id"] == family))
    sharing_path = ROOT / "config/daily_model_data_sharing_registry.csv"
    with sharing_path.open(encoding="utf-8-sig", newline="") as stream:
        sharing_row = next(item for item in csv.DictReader(stream) if item["data_family_id"] == family)
    write_forward_capture_csv(
        tmp_path / "config/daily_model_data_sharing_registry.csv",
        background_validator.DATA_SHARING_COLUMNS, [sharing_row],
    )
    write_forward_capture_csv(
        tmp_path / "output/latest/data_freshness_latest.csv", ("main_price_date",),
        [{"main_price_date": "20261002"}],
    )
    validator_path = tmp_path / row["validator"]
    validator_path.parent.mkdir(parents=True)
    validator_path.write_text("# Synthetic validator-path fixture.\n", encoding="utf-8")
    monkeypatch.setattr(background_validator, "ROOT", tmp_path)
    monkeypatch.setattr(background_validator, "REQUIRED_FAMILIES", {family})
    return tmp_path, row


def write_forward_capture_snapshot(root: Path, snapshot_date: str) -> Path:
    path = root / "output/history/daily_model_snapshots" / (
        f"daily_price_pullback_23ema_operation_section_{snapshot_date}_r1_" + "a" * 12 + ".csv"
    )
    write_forward_capture_csv(path, ("operation_asof_date",), [{"operation_asof_date": snapshot_date}])
    return path


def test_forward_capture_before_official_date_allows_registered_absence(
    forward_capture_fixture: tuple[Path, dict[str, str]],
) -> None:
    root, row = forward_capture_fixture
    assert not list(root.glob(row["artifact_path"]))
    assert validate_registry([row], require_artifacts=True) == []


@pytest.mark.parametrize("report_date", ["20261019", "20261020"])
def test_forward_capture_at_or_after_official_date_requires_artifacts(
    forward_capture_fixture: tuple[Path, dict[str, str]], report_date: str,
) -> None:
    root, row = forward_capture_fixture
    write_forward_capture_csv(
        root / "output/latest/data_freshness_latest.csv", ("main_price_date",),
        [{"main_price_date": report_date}],
    )
    errors = validate_registry([row], require_artifacts=True)
    assert any("artifact_path does not exist or match files" in error for error in errors)


@pytest.mark.parametrize("payload", [
    None, "", "wrong_column\n20261002\n", "main_price_date\n", "main_price_date\n\"\"\n",
    "main_price_date\n20260230\n", "main_price_date\n2026-10-02\n", "main_price_date\n 20261002\n",
    "main_price_date\n20261002\n20261018\n", "main_price_date,main_price_date\n20261002,20261002\n",
])
def test_forward_capture_missing_or_invalid_freshness_fails_closed(
    forward_capture_fixture: tuple[Path, dict[str, str]], payload: str | None,
) -> None:
    root, row = forward_capture_fixture
    freshness = root / "output/latest/data_freshness_latest.csv"
    if payload is None:
        freshness.unlink()
    else:
        freshness.write_text(payload, encoding="utf-8")
    errors = validate_registry([row], require_artifacts=True)
    assert any("valid official data_freshness main_price_date is required" in error for error in errors)


@pytest.mark.parametrize("field,value", [
    ("point_in_time_status", "forward_capture_not_before_20261020_consumer_disabled_not_full_PIT"),
    ("consumer_models", "all_models"), ("producer", "scripts/other_writer.py"),
    ("artifact_path", "output/history/other_model/*.csv"),
])
@pytest.mark.parametrize("require_artifacts", [False, True])
def test_forward_capture_background_metadata_mismatch_fails_closed(
    forward_capture_fixture: tuple[Path, dict[str, str]], field: str, value: str, require_artifacts: bool,
) -> None:
    _, row = forward_capture_fixture
    row[field] = value
    errors = validate_registry([row], require_artifacts=require_artifacts)
    assert any("forward capture metadata mismatch" in error for error in errors)


@pytest.mark.parametrize("defect", ["missing", "consumer_access_mode", "approved_consumer_models"])
def test_forward_capture_sharing_metadata_mismatch_fails_closed(
    forward_capture_fixture: tuple[Path, dict[str, str]], defect: str,
) -> None:
    root, row = forward_capture_fixture
    sharing_path = root / "config/daily_model_data_sharing_registry.csv"
    with sharing_path.open(encoding="utf-8-sig", newline="") as stream:
        sharing_row = next(csv.DictReader(stream))
    if defect == "missing":
        sharing_path.unlink()
    else:
        sharing_row[defect] = "consumer_enabled_or_unregistered_model"
        write_forward_capture_csv(sharing_path, background_validator.DATA_SHARING_COLUMNS, [sharing_row])
    errors = validate_registry([row], require_artifacts=True)
    assert any("forward capture" in error and ("data-sharing" in error or "registration" in error) for error in errors)


@pytest.mark.parametrize("marker", [
    "forward_capture_not_before_20261019_consumer_enabled_not_full_PIT",
    "forward_capture_not_before_20260230_consumer_disabled_not_full_PIT",
])
def test_forward_capture_registry_activation_marker_contradiction_fails_closed(
    forward_capture_fixture: tuple[Path, dict[str, str]], marker: str,
) -> None:
    _, row = forward_capture_fixture
    row["point_in_time_status"] = marker
    errors = validate_registry([row], require_artifacts=True)
    assert any("invalid forward capture registry marker" in error for error in errors)


def test_forward_capture_validator_does_not_import_production_modules() -> None:
    import ast

    source = (ROOT / "scripts/validate_daily_model_background_data_registry.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    modules = {
        node.module if isinstance(node, ast.ImportFrom) else alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    assert modules == {"__future__", "argparse", "csv", "datetime", "pathlib", "re", "model_data_independence"}


def test_forward_capture_existing_pre_cutoff_file_is_never_skipped(
    forward_capture_fixture: tuple[Path, dict[str, str]],
) -> None:
    root, row = forward_capture_fixture
    write_forward_capture_snapshot(root, "20261002")
    errors = validate_registry([row], require_artifacts=True)
    assert any("historical backfill is forbidden" in error for error in errors)


def test_forward_capture_existing_file_cannot_override_official_logical_date(
    forward_capture_fixture: tuple[Path, dict[str, str]],
) -> None:
    root, row = forward_capture_fixture
    write_forward_capture_snapshot(root, "20261019")
    errors = validate_registry([row], require_artifacts=True)
    assert any("capture snapshot date exceeds official main_price_date" in error for error in errors)


def test_forward_capture_valid_physical_date_passes_after_cutoff(
    forward_capture_fixture: tuple[Path, dict[str, str]],
) -> None:
    root, row = forward_capture_fixture
    write_forward_capture_csv(
        root / "output/latest/data_freshness_latest.csv", ("main_price_date",),
        [{"main_price_date": "20261019"}],
    )
    write_forward_capture_snapshot(root, "20261019")
    assert validate_registry([row], require_artifacts=True) == []


@pytest.mark.parametrize("defect", ["missing_date", "mismatched_date", "invalid_date", "empty", "filename", "directory"])
def test_forward_capture_existing_physical_file_is_validated(
    forward_capture_fixture: tuple[Path, dict[str, str]], defect: str,
) -> None:
    root, row = forward_capture_fixture
    write_forward_capture_csv(
        root / "output/latest/data_freshness_latest.csv", ("main_price_date",),
        [{"main_price_date": "20261019"}],
    )
    path = write_forward_capture_snapshot(root, "20261019")
    if defect == "missing_date":
        path.write_text("stock_id\n1234\n", encoding="utf-8")
    elif defect == "mismatched_date":
        path.write_text("operation_asof_date\n20261018\n", encoding="utf-8")
    elif defect == "invalid_date":
        path.write_text("operation_asof_date\n20260230\n", encoding="utf-8")
    elif defect == "empty":
        path.write_text("operation_asof_date\n", encoding="utf-8")
    elif defect == "filename":
        path.rename(path.with_name("daily_price_pullback_23ema_operation_section_20261019_backup.csv"))
    else:
        path.unlink()
        path.mkdir()
    errors = validate_registry([row], require_artifacts=True)
    assert any("invalid physical capture artifact" in error for error in errors)


def test_forward_capture_does_not_relax_other_registered_family_artifact_guards(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    rows = registry_rows()
    monkeypatch.setattr(background_validator, "ROOT", tmp_path)
    monkeypatch.setattr(background_validator, "REQUIRED_FAMILIES", set())
    checked = []
    for row in rows:
        if row["data_family_id"] == "price_pullback_23ema_operation_section" or not row["artifact_path"]:
            continue
        errors = validate_registry([row], require_artifacts=True)
        assert any(f"{row['data_family_id']}: artifact_path does not exist or match files" in error for error in errors)
        checked.append(row["data_family_id"])
    assert len(checked) > 80


def test_forward_capture_family_registration_is_required(
    forward_capture_fixture: tuple[Path, dict[str, str]],
) -> None:
    errors = validate_registry([], require_artifacts=True)
    assert any("registry missing required background data families" in error and "price_pullback_23ema_operation_section" in error for error in errors)


def test_forward_capture_cannot_use_generic_missing_family_placeholder(
    forward_capture_fixture: tuple[Path, dict[str, str]],
) -> None:
    _, row = forward_capture_fixture
    row.update(
        scope="missing_shared_data_family", cleanup_status="blocked_missing_source_or_validator",
        artifact_path="", validator="not_implemented", allowed_use="none until implemented",
    )
    errors = validate_registry([row], require_artifacts=True)
    assert any("forward capture metadata mismatch for scope" in error for error in errors)
    assert any("forward capture metadata mismatch for artifact_path" in error for error in errors)
