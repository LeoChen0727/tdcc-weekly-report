import csv
import os
from pathlib import Path
import subprocess
import sys
import textwrap

import pytest


ROOT = Path(__file__).resolve().parents[1]
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
MONITORING_WORKFLOW_RELATIVE = (
    ".github/workflows/revenue_unreacted_range_post_launch_monitoring.yml"
)
MONITORING_WORKFLOW = ROOT / MONITORING_WORKFLOW_RELATIVE
RESOLVER_CASES = (
    (
        DAILY_WORKFLOW,
        "- name: Resolve revenue v2 formal operation readiness",
        "- name: Build revenue v2 formal operation adapter",
    ),
    (
        MONITORING_WORKFLOW,
        "- name: Resolve formal launch readiness",
        "- name: Skip monitoring before formal launch",
    ),
)
PERMISSION_FIELDS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
)
EXPECTED_IDENTITY = {
    "approval_status": "provisional_backtest_supported_oos_unconfirmed",
    "approval_version": "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830",
    "operation_module_id": "revenue_unreacted_range_source_mid_falling_v2_operation_v2",
    "adapter_schema_version": "revenue_unreacted_range_operation_section_schema_v2",
    "lifecycle_contract_version": "revenue_unreacted_range_lifecycle_v2",
    "pdf_integration_status": "pdf_integrated_daily_adapter",
}
EXPECTED_SECTIONS = (
    "active_operation",
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
)


def _block(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    return text[start_index:end_index]


def _resolver_source(workflow: Path, start: str, end: str) -> str:
    resolver = _block(workflow.read_text(encoding="utf-8"), start, end)
    marker = "          python - <<'PY'\n"
    source_start = resolver.index(marker) + len(marker)
    source_end = resolver.index("\n          PY", source_start)
    return textwrap.dedent(resolver[source_start:source_end])


def _ready_row() -> dict[str, str]:
    row = {
        "model_id": "revenue_unreacted_range",
        "daily_adapter_sections": ",".join(EXPECTED_SECTIONS),
        **EXPECTED_IDENTITY,
    }
    row.update({field: "True" for field in PERMISSION_FIELDS})
    return row


def _run_resolver(
    root: Path,
    workflow: Path,
    start: str,
    end: str,
    rows: list[dict[str, str]] | None,
    *,
    updater_output: str = "revenue_unreacted_range_operation_section",
    updater_exit_code: int = 0,
) -> subprocess.CompletedProcess[str]:
    readiness_path = root / "output" / "latest" / "model_operation_readiness_latest.csv"
    if rows is not None:
        readiness_path.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = sorted({field for row in rows for field in row}) or ["model_id"]
        with readiness_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    scripts = root / "scripts"
    scripts.mkdir(parents=True, exist_ok=True)
    (scripts / "update_daily_published_model_snapshots.py").write_text(
        "import sys\n"
        f"print({updater_output!r})\n"
        f"raise SystemExit({updater_exit_code})\n",
        encoding="utf-8",
    )
    output_path = root / "github-output.txt"
    environment_path = root / "github-environment.txt"
    env = os.environ.copy()
    env["GITHUB_OUTPUT"] = str(output_path)
    env["GITHUB_ENV"] = str(environment_path)
    return subprocess.run(
        [sys.executable, "-c", _resolver_source(workflow, start, end)],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def test_daily_full_revenue_adapter_is_fail_closed_on_four_readiness_flags() -> None:
    text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    resolver = _block(
        text,
        "- name: Resolve revenue v2 formal operation readiness",
        "- name: Build revenue v2 formal operation adapter",
    )
    builder = _block(
        text,
        "- name: Build revenue v2 formal operation adapter",
        "- name: Record disabled revenue v2 formal operation skip",
    )
    disabled = _block(
        text,
        "- name: Record disabled revenue v2 formal operation skip",
        "- name: Publish and validate volume v2 audit-source snapshots",
    )

    assert 'Path("output/latest/model_operation_readiness_latest.csv")' in resolver
    assert 'row.get("model_id", "").strip() == "revenue_unreacted_range"' in resolver
    for field in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        assert f'"{field}"' in resolver
    assert "duplicate revenue_unreacted_range readiness rows" in resolver
    assert "readiness permissions must be" in resolver
    assert "atomically all True or all False" in resolver
    for field, expected in EXPECTED_IDENTITY.items():
        assert f'"{field}": "{expected}"' in resolver
    for section in (
        "active_operation",
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
    ):
        assert f'"{section}"' in resolver
    assert "len(observed_section_tokens) != len(expected_sections)" in resolver
    assert "set(observed_section_tokens) != expected_sections" in resolver
    assert "if: steps.revenue-v2-readiness.outputs.enabled == 'true'" in builder
    assert (
        "python scripts/build_daily_revenue_unreacted_range_operation_section.py"
        in builder
    )
    assert '--report-date "$EXPECTED_MAIN_PRICE_DATE"' in builder
    assert (
        "python scripts/validate_daily_revenue_unreacted_range_operation_section.py"
        in builder
    )
    assert "no runtime artifact was produced" in disabled
    assert "build_daily_revenue_unreacted_range_operation_section.py" not in disabled


@pytest.mark.parametrize(
    ("workflow", "start", "end"),
    RESOLVER_CASES,
    ids=("daily-full", "post-launch-monitoring"),
)
def test_revenue_readiness_resolvers_execute_exact_enabled_and_disabled_states(
    tmp_path: Path,
    workflow: Path,
    start: str,
    end: str,
) -> None:
    enabled_root = tmp_path / "enabled"
    enabled_result = _run_resolver(
        enabled_root,
        workflow,
        start,
        end,
        [_ready_row()],
    )
    assert enabled_result.returncode == 0, enabled_result.stderr
    assert "enabled=true" in (enabled_root / "github-output.txt").read_text(
        encoding="utf-8"
    )

    disabled_row = _ready_row()
    disabled_row.update({field: "False" for field in PERMISSION_FIELDS})
    for field in EXPECTED_IDENTITY:
        disabled_row.pop(field)
    disabled_row.pop("daily_adapter_sections")
    disabled_root = tmp_path / "disabled"
    disabled_result = _run_resolver(
        disabled_root,
        workflow,
        start,
        end,
        [disabled_row],
    )
    assert disabled_result.returncode == 0, disabled_result.stderr
    assert "enabled=false" in (disabled_root / "github-output.txt").read_text(
        encoding="utf-8"
    )


@pytest.mark.parametrize(
    ("workflow", "start", "end"),
    RESOLVER_CASES,
    ids=("daily-full", "post-launch-monitoring"),
)
@pytest.mark.parametrize(
    ("rows", "case_id"),
    (
        (None, "missing-readiness-file"),
        ([], "header-only-readiness-file"),
    ),
    ids=("missing-readiness-file", "header-only-readiness-file"),
)
def test_revenue_readiness_resolvers_safely_disable_on_missing_or_zero_rows(
    tmp_path: Path,
    workflow: Path,
    start: str,
    end: str,
    rows: list[dict[str, str]] | None,
    case_id: str,
) -> None:
    root = tmp_path / case_id
    result = _run_resolver(
        root,
        workflow,
        start,
        end,
        rows,
        updater_output="",
        updater_exit_code=2,
    )
    assert result.returncode == 0, result.stderr
    assert "enabled=false" in (root / "github-output.txt").read_text(
        encoding="utf-8"
    )


@pytest.mark.parametrize(
    ("workflow", "start", "end"),
    RESOLVER_CASES,
    ids=("daily-full", "post-launch-monitoring"),
)
@pytest.mark.parametrize(
    ("updater_output", "updater_exit_code"),
    (
        ("revenue_unreacted_range_operation_section", 2),
        ("other_registered_artifact", 0),
    ),
    ids=("updater-help-nonzero", "artifact-unregistered"),
)
def test_revenue_readiness_resolvers_fail_closed_when_snapshot_registry_unavailable(
    tmp_path: Path,
    workflow: Path,
    start: str,
    end: str,
    updater_output: str,
    updater_exit_code: int,
) -> None:
    result = _run_resolver(
        tmp_path,
        workflow,
        start,
        end,
        [_ready_row()],
        updater_output=updater_output,
        updater_exit_code=updater_exit_code,
    )
    assert result.returncode != 0
    assert "published snapshot artifact id is not registered" in result.stderr


@pytest.mark.parametrize(
    ("workflow", "start", "end"),
    RESOLVER_CASES,
    ids=("daily-full", "post-launch-monitoring"),
)
@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    (
        ("duplicate", "duplicate revenue_unreacted_range readiness rows"),
        ("mixed_permissions", "atomically all True or all False"),
        ("invalid_boolean", "invalid revenue_unreacted_range readiness booleans"),
        ("approval_status", "readiness identity mismatch"),
        ("approval_version", "readiness identity mismatch"),
        ("operation_module_id", "readiness identity mismatch"),
        ("adapter_schema_version", "readiness identity mismatch"),
        ("lifecycle_contract_version", "readiness identity mismatch"),
        ("pdf_integration_status", "readiness identity mismatch"),
        ("duplicate_sections", "readiness adapter sections mismatch"),
        ("wrong_sections", "readiness adapter sections mismatch"),
    ),
)
def test_revenue_readiness_resolvers_fail_closed_on_non_atomic_or_wrong_identity(
    tmp_path: Path,
    workflow: Path,
    start: str,
    end: str,
    mutation: str,
    expected_error: str,
) -> None:
    row = _ready_row()
    rows = [row]
    if mutation == "duplicate":
        rows.append(dict(row))
    elif mutation == "mixed_permissions":
        row["production_allowed"] = "False"
    elif mutation == "invalid_boolean":
        row["formal_model_use_allowed"] = "true"
    elif mutation in EXPECTED_IDENTITY:
        row[mutation] = "wrong_identity"
    elif mutation == "duplicate_sections":
        row["daily_adapter_sections"] += ",active_operation"
    elif mutation == "wrong_sections":
        row["daily_adapter_sections"] = row["daily_adapter_sections"].replace(
            "pending_confirmation", "wrong_section"
        )
    else:  # pragma: no cover - test table integrity
        raise AssertionError(mutation)

    result = _run_resolver(
        tmp_path / mutation,
        workflow,
        start,
        end,
        rows,
    )
    assert result.returncode != 0
    assert expected_error in result.stderr


def test_daily_full_revenue_artifact_copy_snapshot_and_stage_are_conditional() -> None:
    text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    publish = _block(
        text,
        "- name: Publish and validate post-audit daily model snapshots",
        "- name: Validate catalyst layer",
    )
    pages = _block(
        text,
        "- name: Prepare GitHub Pages packet and rules files",
        "- name: Prepare daily authority release before immutable snapshot finalization",
    )
    staging = _block(
        text,
        "- name: Stage immutable published snapshot revisions",
        "- name: Validate immutable published snapshot revisions",
    )
    commit = _block(
        text,
        "- name: Commit report artifacts, packets, and rules first",
        "- name: Wait briefly for GitHub Pages and raw propagation",
    )

    assert "$REVENUE_UNREACTED_RANGE_V2_SNAPSHOT_ARGS" in publish
    assert "$REVENUE_UNREACTED_RANGE_V2_SNAPSHOT_ARGS" in staging
    assert (
        "--artifact-id revenue_unreacted_range_operation_section" in text
    )
    assert "if enabled and snapshot_registered" in text
    assert "if enabled and not snapshot_registered" in text
    assert "published snapshot artifact id is not registered" in text
    for suffix in ("csv", "md"):
        artifact = (
            "daily_revenue_unreacted_range_operation_section_latest."
            f"{suffix}"
        )
        assert artifact in pages
        assert artifact in commit
    assert 'if [ "$REVENUE_UNREACTED_RANGE_V2_ENABLED" = "true" ]' in pages
    assert 'if [ "$REVENUE_UNREACTED_RANGE_V2_ENABLED" = "true" ]' in commit
    assert (
        "output/history/daily_model_snapshots/"
        "daily_revenue_unreacted_range_operation_section_*.csv"
        in commit
    )


def test_post_launch_monitoring_dispatches_only_frozen_revenue_v2_inputs() -> None:
    text = MONITORING_WORKFLOW.read_text(encoding="utf-8")

    assert 'cron: "30 13 * * 1-5"' in text
    assert "workflow_dispatch:" in text
    assert "contents: read" in text
    assert "actions: write" in text
    assert "ref: main" in text
    assert 'Path("output/latest/model_operation_readiness_latest.csv")' in text
    for field in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        assert f'"{field}"' in text
    assert "duplicate revenue_unreacted_range readiness rows" in text
    assert "atomically all True or all False" in text
    for field, expected in EXPECTED_IDENTITY.items():
        assert f'"{field}": "{expected}"' in text
    for section in (
        "active_operation",
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
    ):
        assert f'"{section}"' in text
    assert "len(observed_section_tokens) != len(expected_sections)" in text
    assert "set(observed_section_tokens) != expected_sections" in text
    assert "gh workflow run research_backtest_pipeline.yml" in text
    assert "--ref main" in text
    assert "-f run_revenue_unreacted_range_research=true" in text
    assert (
        "-f run_revenue_unreacted_range_forward_holdout_v2_only=true" in text
    )
    assert text.count("gh workflow run") == 1
    assert "git commit" not in text
    assert "git push" not in text
    assert "run_shared_model_research_data_refresh=true" not in text
    assert "apps_script" not in text.lower()
    assert "triggerdaily" not in text.lower()
