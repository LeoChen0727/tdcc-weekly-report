from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

from scripts import validate_daily_production_boundaries as boundaries
from scripts import detect_daily_model_pr_validation_scope as model_scope
from scripts.update_daily_published_model_snapshots import ARTIFACTS_BY_ID


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
WARRANT_WORKFLOW = ROOT / ".github" / "workflows" / "warrant_flow.yml"
PDF_REPLAY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_pdf_replay_pr_validation.yml"


JOB_LINE = re.compile(
    r"(?m)^  (?P<quote>['\"]?)(?P<job_id>[A-Za-z0-9_-]+)(?P=quote):"
    r"[ \t]*(?:#.*)?$"
)
STEP_LINE = re.compile(r"(?m)^      -(?:[ \t].*)?$")


def key_pattern(key: str) -> str:
    escaped = re.escape(key)
    return rf'''(?:{escaped}|'{escaped}'|"{escaped}")'''


def workflow_jobs(text: str | None = None) -> dict[str, str]:
    workflow_text = text if text is not None else WORKFLOW.read_text(encoding="utf-8")
    jobs = re.search(r"(?m)^jobs:[ \t]*(?:#.*)?$", workflow_text)
    matches = list(JOB_LINE.finditer(workflow_text, jobs.end())) if jobs else []
    ids = [match.group("job_id") for match in matches]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate active workflow job id")
    ends = [match.start() for match in matches[1:]] + [len(workflow_text)]
    return {
        job_id: workflow_text[match.start() : end]
        for job_id, match, end in zip(ids, matches, ends)
    }


def job_block(job_id: str, text: str | None = None) -> str:
    return workflow_jobs(text).get(job_id, "")


def active_field(block: str, key: str, indent: int = 8) -> str | None:
    first_line, separator, remainder = block.partition("\n")
    if first_line.startswith("      - "):
        block = "        " + first_line[8:] + separator + remainder
    matches = list(
        re.finditer(
            rf"(?m)^{' ' * indent}{key_pattern(key)}:"
            r"[ \t]*(?P<value>.*)$",
            block,
        )
    )
    if not matches:
        return None
    if len(matches) != 1:
        return ""
    match = matches[0]
    value = match.group("value").strip()
    if value not in {">", ">-", "|", "|-"}:
        return value.strip("'\"")
    content: list[str] = []
    for line in block[match.end() :].lstrip("\n").splitlines():
        line_indent = len(line) - len(line.lstrip())
        if line.strip() and line_indent <= indent:
            break
        if line_indent >= indent + 2:
            content.append(line[indent + 2 :])
    return (
        " ".join(line.strip() for line in content if line.strip())
        if value.startswith(">")
        else "\n".join(content)
    )


def active_list(block: str, key: str, indent: int = 4) -> tuple[str, ...]:
    markers = list(re.finditer(
        rf"(?m)^{' ' * indent}{key_pattern(key)}:[ \t]*(?:#.*)?$", block
    ))
    if len(markers) != 1:
        return ()
    marker = markers[0]
    values: list[str] = []
    for line in block[marker.end() :].lstrip("\n").splitlines():
        line_indent = len(line) - len(line.lstrip())
        if line.strip() and line_indent <= indent:
            break
        item = re.match(rf"^{' ' * (indent + 2)}-\s*(?P<value>.+)$", line)
        if item:
            values.append(item.group("value").strip().strip("'\""))
    return tuple(values)


def active_step_blocks(job_block: str) -> tuple[str, ...]:
    markers = list(re.finditer(
        rf"(?m)^    {key_pattern('steps')}:[ \t]*(?:#.*)?$", job_block
    ))
    if len(markers) != 1:
        return ()
    steps_text = job_block[markers[0].end() :]
    next_job_field = re.search(r"(?m)^    (?![ #\r\n])", steps_text)
    steps_text = steps_text[: next_job_field.start()] if next_job_field else steps_text
    starts = list(STEP_LINE.finditer(steps_text))
    ends = [match.start() for match in starts[1:]] + [len(steps_text)]
    blocks = tuple(
        steps_text[match.start() : end] for match, end in zip(starts, ends)
    )
    key_token = r'''(?:[A-Za-z0-9_-]+|'[A-Za-z0-9_-]+'|"[A-Za-z0-9_-]+")'''
    valid_head = re.compile(rf"^      -(?:[ \t]+{key_token}:[ \t]*.*)?$")
    if any(not valid_head.fullmatch(block.splitlines()[0]) for block in blocks):
        return ()
    return blocks


def job_step(job_id: str, step_name: str, text: str | None = None) -> str:
    return next(
        (
            block
            for block in active_step_blocks(workflow_jobs(text)[job_id])
            if active_field(block, "name") == step_name
        ),
        "",
    )


def run_commands(run_text: str) -> tuple[str, ...]:
    commands: list[str] = []
    current: list[str] = []
    for raw_line in run_text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        continued = stripped.endswith("\\")
        current.append(stripped[:-1].rstrip() if continued else stripped)
        if not continued:
            commands.append(" ".join(current))
            current = []
    if current:
        commands.append(" ".join(current))
    return tuple(commands)


def job_run_text(job_id: str, text: str | None = None) -> str:
    return "\n".join(
        active_field(step, "run") or ""
        for step in active_step_blocks(workflow_jobs(text)[job_id])
    )


def workflow_run_text(text: str | None = None) -> str:
    return "\n".join(job_run_text(job_id, text) for job_id in workflow_jobs(text))


def scope_job_contract_ok(text: str) -> bool:
    steps = active_step_blocks(job_block("scope", text))
    block = job_run_text("scope", text)
    required = (
        "git --no-replace-objects init .",
        'remote add origin "$REPOSITORY_URL"',
        "config remote.origin.promisor true",
        "config remote.origin.partialclonefilter blob:none",
        "--depth=\"$fetch_depth\"",
        "--filter=blob:none",
        '"+$FETCH_REF:refs/remotes/origin/pr-scope"',
        'if [ "$fetched_sha" != "$MERGE_SHA" ]; then',
        '"$MERGE_SHA:scripts/detect_daily_model_pr_validation_scope.py"',
    )
    forbidden = (
        "actions/checkout@",
        "fetch-depth: 0",
        "persist-credentials: true",
        "GITHUB_TOKEN",
        "github.token",
        "secrets.",
        "pip install",
        "pytest",
        "python scripts/validate_",
        "python scripts/build_",
        "update-ref",
        "rev-parse HEAD",
    )
    return (
        all(literal in block for literal in required)
        and not any(literal in block for literal in forbidden)
        and all(active_field(step, "uses") is None for step in steps)
    )


def aggregate_contract_ok(text: str) -> bool:
    job = job_block("daily-model-maintenance-pr-validation", text)
    steps = active_step_blocks(job)
    block = job_run_text("daily-model-maintenance-pr-validation", text)
    executable_lines = {
        line.strip() for line in block.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    expected_needs = (
        "scope",
        "repo_current_contracts",
        "shared_model_research",
        "volume_v2_research",
        "revenue_research",
        "financial_statement_research",
    )
    required = (
        'if [ "$SCOPE_RESULT" != "success" ]; then',
        'if [ "$result" != "success" ]; then',
        'if [ "$result" != "skipped" ]; then',
        'require_domain_result repo-current-contracts "$CORE_SELECTED" "$CORE_RESULT"',
        'require_domain_result shared-model-research "$SHARED_SELECTED" "$SHARED_RESULT"',
        'require_domain_result volume-v2-research "$VOLUME_SELECTED" "$VOLUME_RESULT"',
        'require_domain_result revenue-research "$REVENUE_SELECTED" "$REVENUE_RESULT"',
        'require_domain_result financial-statement-research "$FINANCIAL_SELECTED" "$FINANCIAL_RESULT"',
    )
    return (
        active_field(job, "name", 4) == "daily-model-maintenance-pr-validation"
        and active_field(job, "if", 4) == "always()"
        and active_list(job, "needs") == expected_needs
        and all(literal in executable_lines for literal in required)
        and active_field(job, "continue-on-error", 4) is None
        and all(
            active_field(step, "continue-on-error") is None for step in steps
        )
    )


VOLUME_GENERATED_TARGETS = tuple(
    f"{root}/volume_v2_warrant_lineage_history_audit_latest.{suffix}"
    for root in ("docs/latest", "output/latest")
    for suffix in ("csv", "md")
)

FINANCIAL_GENERATED_TARGETS = tuple(
    f"{root}/financial_statement_historical_pit_source_audit_latest.{suffix}"
    for root in ("docs/latest", "output/latest/research_backtest")
    for suffix in ("csv", "md")
)

REVENUE_VALIDATOR_COMMANDS = (
    "python scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
    "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
    "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
    "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
    "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
    "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py",
    "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
    "python scripts/validate_revenue_unreacted_range_promotion_preparation.py",
    "python scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py",
)

SHARED_VALIDATION_COMMANDS = (
    "python scripts/validate_daily_model_background_data_registry.py",
    'python scripts/validate_model_data_independence.py --base-ref "$BASE_SHA"',
    'python scripts/validate_model_research_shared_utilities.py --base-ref "$BASE_SHA"',
    "python scripts/build_mature_model_row_level_metric_contract_audit.py",
    "python scripts/validate_mature_model_row_level_metric_contract_audit.py",
    "python scripts/validate_research_against_stock_model_contract.py",
    "python scripts/validate_daily_model_research_parity.py",
)

VOLUME_VALIDATION_COMMANDS = (
    "python scripts/validate_volume_breakout_watch.py --latest-only",
    "python scripts/validate_volume_attack_theme_layer.py",
    'python scripts/validate_daily_canonical_field_lineage.py --base-ref "$BASE_SHA" $LINEAGE_HISTORY_MODE',
    "python scripts/build_volume_v2_warrant_lineage_history_audit.py",
    "python scripts/validate_volume_v2_warrant_lineage_history_audit.py",
    "git --no-replace-objects diff --exit-code -- "
    + " ".join(VOLUME_GENERATED_TARGETS),
)

FINANCIAL_VALIDATION_COMMANDS = (
    "python scripts/validate_financial_statement_pit.py",
    "python scripts/build_financial_statement_historical_pit_source_audit.py",
    "python scripts/validate_financial_statement_historical_pit_source_audit.py",
    "git --no-replace-objects diff --exit-code -- "
    + " ".join(FINANCIAL_GENERATED_TARGETS),
)

DOMAIN_CONTRACTS = {
    "repo_current_contracts": (model_scope.REPO_CURRENT_CONTRACTS, "", ()),
    "shared_model_research": (
        model_scope.SHARED_MODEL_RESEARCH,
        "Validate shared model research contracts",
        SHARED_VALIDATION_COMMANDS,
    ),
    "volume_v2_research": (
        model_scope.VOLUME_V2_RESEARCH,
        "Validate Volume V2 research contracts",
        VOLUME_VALIDATION_COMMANDS,
    ),
    "revenue_research": (
        model_scope.REVENUE_RESEARCH,
        "Validate revenue research contracts",
        REVENUE_VALIDATOR_COMMANDS,
    ),
    "financial_statement_research": (
        model_scope.FINANCIAL_STATEMENT_RESEARCH,
        "Validate financial-statement research contracts",
        FINANCIAL_VALIDATION_COMMANDS,
    ),
}

def domain_workload_contract_ok(text: str) -> bool:
    core = job_run_text("repo_current_contracts", text)
    for job_id, (_, step_name, expected_commands) in DOMAIN_CONTRACTS.items():
        if not step_name:
            continue
        step = job_step(job_id, step_name, text)
        job_commands = run_commands(job_run_text(job_id, text))
        workload_commands = tuple(
            command
            for command in job_commands
            if command.startswith(
                (
                    "python scripts/build_",
                    "python scripts/validate_",
                    "git --no-replace-objects diff --exit-code",
                )
            )
        )
        if (
            not step
            or active_field(step, "if") is not None
            or active_field(step, "continue-on-error") is not None
            or run_commands(active_field(step, "run") or "") != expected_commands
            or workload_commands != expected_commands
        ):
            return False
    all_runs = workflow_run_text(text)
    return (
        not re.search(r"(?m)^\s*python scripts/build_", core)
        and "diff --exit-code" not in core
        and all(all_runs.count(command) == 1 for command in REVENUE_VALIDATOR_COMMANDS)
    )


def direct_dependency_closure_ok(text: str) -> bool:
    path_pattern = re.compile(
        r"(?P<path>(?:scripts|tests|docs/latest|output/latest)/"
        r"[A-Za-z0-9_.*{}/$-]+\.(?:py|csv|json|md))"
    )
    for job_id, (expected_domain, _, _) in DOMAIN_CONTRACTS.items():
        block = job_run_text(job_id, text)
        paths = sorted({match.group("path") for match in path_pattern.finditer(block)})
        if not paths:
            return False
        for path in paths:
            if not (
                model_scope.is_watched_path(path)
                or model_scope.is_model_like_path(path)
            ):
                return False
            try:
                domains = model_scope.domains_for_path(path)
            except model_scope.ScopeDetectionError:
                return False
            if expected_domain not in domains:
                return False
    return True


def git_invocation_contract_ok(text: str) -> bool:
    runs = workflow_run_text(text)
    for match in re.finditer(r"(?<![A-Za-z0-9_./-])git\s+", runs):
        tail = runs[match.start() : match.start() + 80]
        if not tail.startswith("git --no-replace-objects "):
            return False
    return True


def test_every_formal_snapshot_workflow_pins_an_explicit_revision_reason() -> None:
    expected_callers = {
        "daily_full_pipeline.yml": (
            "daily_full_volume_v2_audit_sources",
            "daily_full_post_audit_artifacts",
            "daily_authority_release_final",
        ),
        "weekly_theme_review.yml": ("weekly_theme_formal_sync",),
        "warrant_flow.yml": ("warrant_formal_sync",),
    }
    workflow_dir = ROOT / ".github" / "workflows"
    publisher = "python scripts/update_daily_published_model_snapshots.py"
    actual_callers = {
        path.name
        for path in workflow_dir.glob("*.yml")
        if publisher in path.read_text(encoding="utf-8")
    }

    assert actual_callers == set(expected_callers)
    for filename, revision_reasons in expected_callers.items():
        text = (workflow_dir / filename).read_text(encoding="utf-8")
        assert text.count(publisher) == len(revision_reasons)
        for revision_reason in revision_reasons:
            assert text.count(f"--revision-reason {revision_reason}") == 1


def test_every_formal_snapshot_workflow_uses_registered_artifact_ids() -> None:
    workflow_dir = ROOT / ".github" / "workflows"
    publisher = "python scripts/update_daily_published_model_snapshots.py"
    for path in workflow_dir.glob("*.yml"):
        text = path.read_text(encoding="utf-8")
        if publisher not in text:
            continue
        observed = set(re.findall(r"--artifact-id ([A-Za-z0-9_]+)", text))
        assert observed
        assert observed <= set(ARTIFACTS_BY_ID), path.name


def test_daily_full_stages_only_exact_manifest_snapshot_revisions() -> None:
    text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    finalization_block = text[
        text.index(
            "- name: Prepare daily authority release before immutable snapshot finalization"
        ) : text.index("- name: Commit report artifacts, packets, and rules first")
    ]
    assert 're.sub(r"[^0-9]", ""' in finalization_block
    assert (
        'if [[ ! "$snapshot_report_date" =~ ^[0-9]{8}$ ]]; then'
        in finalization_block
    )
    assert "git add output/history/daily_model_snapshots/ || true" not in text
    stage_block = text[
        text.index("- name: Stage immutable published snapshot revisions") :
        text.index("- name: Validate immutable published snapshot revisions")
    ]

    artifact_ids = (
        "data_freshness",
        "model_signals_for_report",
        "all_candidates_source_rows",
        "model_summary_for_report",
        "model_registry",
        "model_parameters",
        "volume_breakout_operation_section",
        "volume_breakout_operation_evidence_audit",
        "w_bottom_right_side_operation_section",
        "neckline_volume_breakout_confirmation_operation_section",
    )
    assert stage_block.count(
        "python scripts/stage_daily_published_snapshot_revisions.py"
    ) == 1
    for artifact_id in artifact_ids:
        assert stage_block.count(f"--artifact-id {artifact_id}") == 1
    assert (
        'daily_model_snapshots/data_freshness_${snapshot_report_date}"*.csv'
        not in finalization_block
    )


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


def test_daily_model_maintenance_pr_workflow_exists_for_model_pdf_paths() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "pull_request:" in text
    assert "workflow_dispatch:" in text
    assert "fetch-depth: 0" in text
    assert "scripts/generate_chatgpt_side_daily_reports.py" in model_scope.WATCHED_PATH_PATTERNS
    assert "scripts/run_chatgpt_daily_report_entrypoint.py" in model_scope.WATCHED_PATH_PATTERNS
    assert "scripts/update_daily_published_model_snapshots.py" in model_scope.WATCHED_PATH_PATTERNS
    assert (
        "config/daily_pdf_rendered_model_regression_contract.csv"
        in model_scope.WATCHED_PATH_PATTERNS
    )
    assert (
        "config/daily_pdf_semantic_golden_cases.csv"
        in model_scope.WATCHED_PATH_PATTERNS
    )
    assert "tests/test_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "tests/test_chatgpt_daily_report_entrypoint.py" in text
    assert model_scope.is_watched_path(
        "docs/specs/daily_mature_model_row_level_metric_contract.md"
    )
    assert "scripts/build_mature_model_row_level_metric_contract_audit.py" in text
    assert "scripts/validate_mature_model_row_level_metric_contract_audit.py" in text
    assert "tests/test_mature_model_row_level_metric_contract_audit.py" in text


def test_scope_aggregate_and_domain_contracts_are_exact_and_fail_closed() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    block = job_run_text("scope", text)

    assert scope_job_contract_ok(text)
    assert aggregate_contract_ok(text)
    assert domain_workload_contract_ok(text)
    assert direct_dependency_closure_ok(text)
    assert git_invocation_contract_ok(text)
    assert tuple(workflow_jobs(text)) == (
        "scope", *DOMAIN_CONTRACTS, "daily-model-maintenance-pr-validation"
    )
    assert "fetch_depth=1" in block
    assert 'fetch_depth=2' in block
    scope_first_step = active_step_blocks(job_block("scope", text))[0]
    assert "public merge ref" in (active_field(scope_first_step, "name") or "")
    assert (
        "          REPOSITORY_URL: ${{ github.server_url }}/${{ github.repository }}.git"
        in scope_first_step
    )
    for job_id in DOMAIN_CONTRACTS:
        job = job_block(job_id, text)
        assert active_field(job, "needs", 4) == "scope"
        condition = active_field(job, "if", 4) or ""
        assert "needs.scope.result == 'success'" in condition
        assert f"needs.scope.outputs.{job_id} == 'true'" in condition
        assert active_field(job, "continue-on-error", 4) is None
        assert not any(
            active_field(step, "continue-on-error")
            for step in active_step_blocks(job)
        )


def test_active_node_scanner_ignores_comments() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    commented = text.replace(
        "jobs:\n",
        "jobs:\n#  fake_job:\n#      - name: fake step\n#        run: false\n",
        1,
    )
    assert tuple(workflow_jobs(commented)) == tuple(workflow_jobs(text))
    assert "fake step" not in workflow_run_text(commented)
    with pytest.raises(ValueError, match="duplicate active workflow job id"):
        workflow_jobs(text + '\n  "scope":\n    steps: []\n')


@pytest.mark.parametrize(
    "active_step",
    (
        "      - run: python scripts/build_fake_research.py\n",
        "      - if: ${{ false }}\n"
        "        run: python scripts/build_fake_research.py\n",
        "      - uses: actions/cache@v4\n"
        "        run: python scripts/build_fake_research.py\n",
    ),
)
def test_anonymous_or_if_first_core_step_cannot_hide_a_research_builder(
    active_step: str,
) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    marker = "      - name: Checkout repository\n"
    mutated = text.replace(marker, active_step + marker, 1)

    assert "python scripts/build_fake_research.py" in workflow_run_text(mutated)
    assert not domain_workload_contract_ok(mutated)


def test_anonymous_research_step_cannot_extend_exact_workload() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    marker = "      - name: Validate Volume V2 research contracts\n"
    mutated = text.replace(
        marker,
        "      - id: hidden-extra\n"
        "        run: python scripts/build_volume_v2_extra.py\n"
        + marker,
        1,
    )

    assert "python scripts/build_volume_v2_extra.py" in workflow_run_text(mutated)
    assert not domain_workload_contract_ok(mutated)


@pytest.mark.parametrize(
    ("needle", "replacement"),
    (
        ("            --filter=blob:none \\\n", ""),
        ("          fetch_depth=1", "          fetch-depth: 0"),
        (
            "          set -euo pipefail",
            "          set -euo pipefail\n          echo $GITHUB_TOKEN",
        ),
        ("git --no-replace-objects init .", "git init ."),
        (
            "          set -euo pipefail",
            "          set -euo pipefail\n          pip install pandas",
        ),
    ),
)
def test_scope_job_contract_rejects_expensive_or_credentialed_mutations(
    needle: str, replacement: str
) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert needle in text
    assert not scope_job_contract_ok(text.replace(needle, replacement, 1))


@pytest.mark.parametrize(
    ("needle", "replacement"),
    (
        ("      - revenue_research\n", ""),
        ("    if: always()\n", "    if: always()\n    \"if\": false\n"),
        (
            "      - financial_statement_research\n    runs-on: ubuntu-latest",
            "      - financial_statement_research\n    needs:\n"
            "      - scope\n    runs-on: ubuntu-latest",
        ),
        (
            "    steps:\n      - name: Validate selected and skipped domain results",
            "    steps:\n      - run: exit 0\n    \"steps\":\n"
            "      - name: Validate selected and skipped domain results",
        ),
        ('if [ "$result" != "skipped" ]; then', 'if [ "$result" != "success" ]; then'),
        (
            'require_domain_result volume-v2-research "$VOLUME_SELECTED" "$VOLUME_RESULT"',
            "echo volume-result-ignored",
        ),
        (
            'require_domain_result financial-statement-research "$FINANCIAL_SELECTED" "$FINANCIAL_RESULT"',
            '# require_domain_result financial-statement-research "$FINANCIAL_SELECTED" "$FINANCIAL_RESULT"',
        ),
    ),
)
def test_stable_aggregate_rejects_missing_or_weakened_domain_contract(
    needle: str, replacement: str
) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert needle in text

    assert not aggregate_contract_ok(text.replace(needle, replacement, 1))


@pytest.mark.parametrize(
    ("needle", "replacement"),
    (
        (
            "          python scripts/validate_repo_file_lifecycle_inventory.py\n",
            "          python scripts/validate_repo_file_lifecycle_inventory.py\n"
            "          python scripts/build_fake_research.py\n",
        ),
        (
            "          python scripts/validate_repo_production_inventory.py\n",
            "          python scripts/validate_repo_production_inventory.py\n"
            "          git --no-replace-objects diff --exit-code -- output/latest/fake.csv\n",
        ),
        ("git --no-replace-objects diff --exit-code --", "echo diff-disabled --"),
        (
            "python scripts/build_volume_v2_warrant_lineage_history_audit.py",
            "python scripts/build_volume_v2_warrant_lineage_history_audit.py || true",
        ),
        (
            "python scripts/build_financial_statement_historical_pit_source_audit.py\n"
            "          python scripts/validate_financial_statement_historical_pit_source_audit.py",
            "python scripts/validate_financial_statement_historical_pit_source_audit.py\n"
            "          python scripts/build_financial_statement_historical_pit_source_audit.py",
        ),
        (
            "python scripts/validate_financial_statement_historical_pit_source_audit.py",
            "python scripts/validate_financial_statement_historical_pit_source_audit.py || :",
        ),
        (
            "financial_statement_historical_pit_source_audit_latest.md\n",
            "financial_statement_historical_pit_source_audit_latest.md \\\n"
            "            output/latest/research_backtest/extra_volatile_audit.csv\n",
        ),
        (f"          {REVENUE_VALIDATOR_COMMANDS[0]}\n", ""),
        (
            f"{REVENUE_VALIDATOR_COMMANDS[0]}\n          {REVENUE_VALIDATOR_COMMANDS[1]}",
            f"{REVENUE_VALIDATOR_COMMANDS[1]}\n          {REVENUE_VALIDATOR_COMMANDS[0]}",
        ),
        (
            "          python scripts/validate_repo_production_inventory.py\n",
            "          python scripts/validate_repo_production_inventory.py\n"
            f"          {REVENUE_VALIDATOR_COMMANDS[0]}\n",
        ),
        (
            f"          {REVENUE_VALIDATOR_COMMANDS[0]}\n",
            f"          {REVENUE_VALIDATOR_COMMANDS[0]}\n"
            "          python scripts/build_revenue_unreacted_range_extra.py\n",
        ),
        (
            "      - name: Validate shared model research contracts\n",
            "      - name: Validate shared model research contracts\n"
            "        \"if\": ${{ false }}\n",
        ),
        (
            "      - name: Validate shared model research contracts\n",
            "      - {run: python scripts/build_fake.py}\n"
            "      - name: Validate shared model research contracts\n",
        ),
    ),
)
def test_domain_workload_contract_rejects_representative_mutations(
    needle: str, replacement: str
) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert needle in text
    assert not domain_workload_contract_ok(text.replace(needle, replacement, 1))


def test_direct_dependency_closure_rejects_unclassified_new_core_validator() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    marker = "          python scripts/validate_repo_file_lifecycle_inventory.py\n"
    assert marker in text
    mutated = text.replace(
        marker,
        marker + "          python scripts/unclassified_repo_gate.py\n",
        1,
    )

    assert not direct_dependency_closure_ok(mutated)


def test_git_invocation_contract_catches_command_substitution_without_protection() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    protected = 'fetched_sha="$(git --no-replace-objects rev-parse FETCH_HEAD)"'
    assert protected in text
    mutated = text.replace(
        protected,
        'fetched_sha="$(git rev-parse FETCH_HEAD)"',
        1,
    )

    assert not git_invocation_contract_ok(mutated)


def test_production_snapshot_updates_are_followed_by_dynamic_lineage_parity() -> None:
    for workflow_path in (DAILY_WORKFLOW, WARRANT_WORKFLOW):
        text = workflow_path.read_text(encoding="utf-8")
        snapshot_update_index = text.index(
            "python scripts/update_daily_published_model_snapshots.py"
        )
        snapshot_validation_index = text.index(
            "python scripts/validate_daily_published_model_snapshots.py",
            snapshot_update_index,
        )
        canonical_validation_index = text.index(
            "python scripts/validate_daily_canonical_field_lineage.py",
            snapshot_validation_index,
        )
        history_validation_index = text.index(
            "python scripts/validate_volume_v2_warrant_lineage_history_audit.py",
            canonical_validation_index,
        )

        assert (
            snapshot_update_index
            < snapshot_validation_index
            < canonical_validation_index
            < history_validation_index
        )

    pr_workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "python scripts/update_daily_published_model_snapshots.py" not in pr_workflow
    assert "Validate production lineage parity ordering contract" in pr_workflow
    assert (
        "-k production_snapshot_updates_are_followed_by_dynamic_lineage_parity"
        in pr_workflow
    )


def test_pdf_replay_pr_workflow_is_renderer_contract_only_and_manually_dispatchable() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    observed_paths = boundaries.workflow_pull_request_paths(text)

    assert "pull_request:" in text
    assert "workflow_dispatch:" in text
    assert observed_paths == boundaries.DAILY_PDF_REPLAY_AUTOMATIC_PATHS
    assert not (
        observed_paths & boundaries.MODEL_OUTPUT_PATHS_FORBIDDEN_FROM_DFKAI_REPLAY
    )
    for source_gate_path in (
        "config/git_worktree_materialization_contract.csv",
        "scripts/git_worktree_safety.py",
        "scripts/market_session_calendar.py",
        "scripts/resolve_daily_report_source_state.py",
        "scripts/run_chatgpt_daily_report_entrypoint.py",
        "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
        "scripts/validate_daily_publish_freshness_gate.py",
    ):
        assert source_gate_path not in observed_paths


def test_daily_production_boundary_rejects_model_output_dfkai_auto_trigger() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    marker = '      - "scripts/validate_chatgpt_side_pdf_contract.py"\n'
    assert marker in text
    mutated = text.replace(
        marker,
        marker + '      - "output/latest/model_operation_readiness_latest.csv"\n',
        1,
    )

    errors = boundaries.validate_pdf_replay_automatic_paths(mutated)

    assert any("model_operation_readiness_latest.csv" in error for error in errors)
    assert any("no-font model validation" in error for error in errors)


def test_daily_model_pr_workflow_does_not_install_dfkai_or_render_pdfs() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "daily-pdf-dfkai-replay:" not in text
    assert "Install and validate DFKai-SB" not in text
    assert "Replay ChatGPT-side daily PDF new conversation" not in text


def test_daily_model_maintenance_pr_workflow_triggers_on_independence_guard_changes() -> None:
    required_paths = (
        "config/daily_model_*.csv",
        "config/revenue_unreacted_range_*.csv",
        "data/financial_statement_history/*.csv",
        "config/runtime_file_lineage_contract.csv",
        "scripts/build_model_data_independence_audit.py",
        "scripts/model_data_independence.py",
        "scripts/validate_model_data_independence.py",
        "scripts/validate_model_surface_registry.py",
        "scripts/validate_repo_code_isolation_policy.py",
        "tests/test_model_data_independence.py",
        "tests/test_model_surface_registry.py",
        "tests/test_repo_code_isolation_policy.py",
        "tests/test_validate_revenue_unreacted_range_*.py",
        "docs/specs/revenue_unreacted_range_*.md",
        "docs/latest/model_data_independence_audit_latest.*",
        "output/latest/model_data_independence_audit_latest.*",
        "output/latest/research_backtest/financial_statement_pit_coverage_latest.*",
        "scripts/build_financial_statement_pit.py",
        "scripts/build_volume_breakout_watch.py",
        "scripts/build_volume_attack_theme_layer.py",
        "scripts/validate_financial_statement_pit.py",
        "scripts/validate_volume_breakout_watch.py",
        "scripts/validate_volume_attack_theme_layer.py",
        "scripts/validate_daily_canonical_field_lineage.py",
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "scripts/build_daily_published_snapshot_ranking_backtest.py",
        "scripts/backfill_historical_all_candidates_snapshots_from_git_history.py",
        "scripts/stage_daily_published_snapshot_revisions.py",
        "scripts/validate_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_financial_statement_pit.py",
        "tests/test_volume_breakout_watch.py",
        "tests/test_daily_canonical_field_lineage.py",
        "tests/test_daily_model_maintenance_pr_validation_workflow.py",
        "tests/test_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_daily_published_snapshot_ranking_backtest.py",
        "tests/test_backfill_historical_all_candidates_snapshots.py",
        "tests/test_stage_daily_published_snapshot_revisions.py",
    )
    for path in required_paths:
        assert model_scope.is_watched_path(path)


def test_daily_model_maintenance_pr_workflow_pins_append_only_validation_base() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "fetch-depth: 0" in text
    assert "BASE_SHA: ${{ github.event.pull_request.base.sha || 'origin/main' }}" in text
    assert '--base-sha "$BASE_SHA"' in text
    assert '--head-sha "$HEAD_SHA"' in text
    assert '--merge-sha "$MERGE_SHA"' in text
    assert "git --no-replace-objects" in text
    assert (
        'python scripts/validate_model_data_independence.py --base-ref "$BASE_SHA"'
        in text
    )
    assert (
        'python scripts/validate_model_research_shared_utilities.py '
        '--base-ref "$BASE_SHA"'
        in text
    )
    assert (
        "LINEAGE_HISTORY_MODE: ${{ github.event_name == 'pull_request' && "
        "'--pr-safe-base-history' || '' }}"
        in text
    )
    assert (
        'python scripts/validate_daily_canonical_field_lineage.py --base-ref "$BASE_SHA" '
        "$LINEAGE_HISTORY_MODE"
        in text
    )
    assert "python scripts/validate_model_data_independence.py\n" not in text
    assert "python scripts/validate_model_research_shared_utilities.py\n" not in text
    assert "python scripts/validate_daily_canonical_field_lineage.py\n" not in text


def test_daily_model_pr_lineage_base_history_is_pull_request_only() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    job = job_block("volume_v2_research", text)
    block = job_run_text("volume_v2_research", text)

    assert job.count("--pr-safe-base-history") == 1
    assert (
        "      LINEAGE_HISTORY_MODE: ${{ github.event_name == 'pull_request' && "
        "'--pr-safe-base-history' || '' }}"
        in job
    )
    assert (
        'python scripts/validate_daily_canonical_field_lineage.py --base-ref "$BASE_SHA" '
        "$LINEAGE_HISTORY_MODE"
        in block
    )
    assert 'if [ "$GITHUB_EVENT_NAME" = "pull_request" ]; then' not in block
    assert "eval " not in block


def test_daily_model_maintenance_pr_workflow_runs_contract_validators() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_commands = (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_stock_model_contract_registry.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_role_manifest_contract.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_daily_production_boundaries.py",
        'python scripts/validate_daily_published_model_snapshots_pr_safe.py --base-ref "$BASE_SHA"',
        'python scripts/validate_repo_advanced_integrity_pr_safe.py --base-ref "$BASE_SHA"',
        "python scripts/validate_daily_model_background_data_registry.py",
        "python scripts/validate_model_data_independence.py",
        'python scripts/validate_model_research_shared_utilities.py --base-ref "$BASE_SHA"',
        "python scripts/validate_volume_breakout_watch.py --latest-only",
        "python scripts/validate_volume_attack_theme_layer.py",
        "python scripts/validate_daily_canonical_field_lineage.py",
        "python scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "python scripts/validate_volume_v2_warrant_lineage_history_audit.py",
        "python scripts/validate_financial_statement_pit.py",
        "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
        "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
        "python scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
        "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
        "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
        "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
        "python scripts/validate_revenue_unreacted_range_promotion_preparation.py",
        "python scripts/build_mature_model_row_level_metric_contract_audit.py",
        "python scripts/validate_mature_model_row_level_metric_contract_audit.py",
        "python scripts/validate_research_against_stock_model_contract.py",
        "python scripts/validate_daily_model_research_parity.py",
        "python scripts/validate_repo_hidden_coupling_audit.py",
        "python scripts/validate_repo_code_isolation_policy.py",
        "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
    )
    for command in required_commands:
        assert command in text

    revenue_validator_order = (
        "python scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
        "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
        "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
        "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
        "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
        "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py",
        "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
        "python scripts/validate_revenue_unreacted_range_promotion_preparation.py",
    )
    positions = [text.index(command) for command in revenue_validator_order]
    assert positions == sorted(positions)
    assert "python scripts/validate_revenue_unreacted_range_forward_holdout.py" not in text


def test_daily_model_maintenance_pr_workflow_runs_focused_pdf_operation_tests() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_tests = (
        "tests/test_chatgpt_daily_report_new_conversation_replay.py",
        "tests/test_chatgpt_daily_report_entrypoint.py",
        "tests/test_daily_report_source_resolver.py",
        "tests/test_daily_pdf_contract_consumers.py",
        "tests/test_daily_pdf_completion_hard_gate.py",
        "tests/test_daily_published_model_snapshots.py",
        "tests/test_repo_advanced_integrity_pr_safe.py",
        "tests/test_backfill_historical_all_candidates_snapshots.py",
        "tests/test_daily_published_snapshot_ranking_backtest.py",
        "tests/test_stage_daily_published_snapshot_revisions.py",
        "tests/test_daily_operation_adapter_protected_fields.py",
        "tests/test_daily_volume_breakout_operation_section.py",
        "tests/test_daily_w_bottom_operation_sections.py",
        "tests/test_daily_price_pullback_23ema_operation_section.py",
        "tests/test_mature_model_row_level_metric_contract_audit.py",
        "tests/test_daily_report_model_summary.py",
        "tests/test_daily_production_boundaries.py",
        "tests/test_model_data_independence.py",
        "tests/test_volume_breakout_watch.py",
        "tests/test_daily_canonical_field_lineage.py",
        "tests/test_daily_model_maintenance_pr_validation_workflow.py",
        "tests/test_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_financial_statement_pit.py",
        "tests/test_revenue_unreacted_range_source_first_condition_audit.py",
        "tests/test_revenue_unreacted_range_source_snapshot_projection.py",
        "tests/test_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "tests/test_validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "tests/test_revenue_unreacted_range_forward_confirmation_feature_audit.py",
        "tests/test_revenue_unreacted_range_rearmed_operation_grid.py",
        "tests/test_revenue_unreacted_range_operation_lag_bucket_audit.py",
        "tests/test_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
        "tests/test_validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
        "tests/test_validate_revenue_unreacted_range_promotion_preparation.py",
        "tests/test_revenue_unreacted_range_forward_holdout.py",
        "tests/test_validate_revenue_unreacted_range_forward_holdout.py",
        "tests/test_repo_hidden_coupling_audit.py",
        "tests/test_stock_model_contract_registry.py",
    )
    for path in required_tests:
        assert path in text


def test_daily_model_pr_focused_suite_replaces_only_strict_runtime_integrity_test() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    strict_node = (
        "tests/test_repo_advanced_integrity.py::"
        "test_repo_advanced_integrity_validator_passes"
    )

    assert "tests/test_repo_advanced_integrity.py" in text
    assert f"--deselect {strict_node}" in text
    assert text.count("--deselect") == 1
    assert "--ignore=tests/test_repo_advanced_integrity.py" not in text


def test_pdf_impact_pr_workflow_runs_actual_pdf_replay_and_uploads_evidence() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    replay_job = boundaries.workflow_job_block(text, "daily-pdf-dfkai-replay")

    assert "Replay ChatGPT-side daily PDF new conversation" in text
    assert "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "timeout-minutes: 20" in text
    assert "timeout 20m python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "PDF replay source_ref=$source_ref" in text
    assert "PDF replay output_dir=chatgpt_side_outputs_pr_validation" in text
    assert "--source-ref \"$source_ref\"" in text
    assert "--output-dir chatgpt_side_outputs_pr_validation" in text
    assert "--require-output-dir chatgpt_side_outputs_pr_validation" in text
    assert "PDF_REPLAY_SOURCE_SHA: ${{ github.event.pull_request.head.sha || github.sha }}" in replay_job
    assert 'checkout_sha="$(git rev-parse HEAD)"' in replay_job
    assert 'if [ "$checkout_sha" != "$GITHUB_SHA" ]; then' in replay_job
    assert 'source_sha="$PDF_REPLAY_SOURCE_SHA"' in replay_job
    assert 'git fetch --no-tags --depth=1 origin "$source_sha"' in replay_job
    assert 'fetched_source_sha="$(git rev-parse FETCH_HEAD)"' in replay_job
    assert 'if [ "$fetched_source_sha" != "$source_sha" ]; then' in replay_job
    assert 'pinned_remote="pinned-replay"' in replay_job
    assert 'pinned_branch="workflow-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}"' in replay_job
    assert 'git branch --force "$pinned_branch" "$source_sha"' in replay_job
    assert 'git remote add "$pinned_remote" "$PWD"' in replay_job
    assert 'git fetch "$pinned_remote" "$pinned_branch"' in replay_job
    assert 'source_ref="$pinned_remote/$pinned_branch"' in replay_job
    assert 'resolved_source_sha="$(git rev-parse "$source_ref")"' in replay_job
    assert 'if [ "$resolved_source_sha" != "$source_sha" ]; then' in replay_job
    assert "PDF replay workflow_checkout_sha=$GITHUB_SHA" in replay_job
    assert "PDF replay source_sha=$source_sha" in replay_job
    assert "GITHUB_HEAD_REF" not in replay_job
    assert "GITHUB_REF_NAME" not in replay_job
    assert 'source_ref="origin/' not in replay_job
    assert "Upload PR daily PDF replay evidence" in text
    assert "actions/upload-artifact@v4" in text
    assert "daily-pdf-replay-pr-validation" in text
    assert "chatgpt_side_outputs_pr_validation/*.pdf" in text
    assert "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json" in text
    assert "chatgpt_side_outputs_pr_validation/chatgpt_daily_pdf_semantic_manifest.csv" in text
    assert "if-no-files-found: error" in text


def test_pdf_replay_local_remote_ref_stays_pinned_when_checked_out_branch_advances(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "workflow-test@example.invalid")
    run_git(repo, "config", "user.name", "Workflow Test")
    marker = repo / "marker.txt"
    marker.write_text("pinned\n", encoding="utf-8")
    run_git(repo, "add", "marker.txt")
    run_git(repo, "commit", "-m", "pinned source")

    source_sha = run_git(repo, "rev-parse", "HEAD")
    pinned_remote = "pinned-replay"
    pinned_branch = "workflow-123-1"
    run_git(repo, "branch", "--force", pinned_branch, source_sha)
    run_git(repo, "remote", "add", pinned_remote, str(repo))
    run_git(repo, "fetch", pinned_remote, pinned_branch)
    source_ref = f"{pinned_remote}/{pinned_branch}"
    assert run_git(repo, "rev-parse", source_ref) == source_sha

    marker.write_text("moving main\n", encoding="utf-8")
    run_git(repo, "add", "marker.txt")
    run_git(repo, "commit", "-m", "advance main")
    assert run_git(repo, "rev-parse", "HEAD") != source_sha
    run_git(repo, "fetch", pinned_remote, pinned_branch)
    assert run_git(repo, "rev-parse", source_ref) == source_sha


def test_daily_production_boundary_accepts_immutable_pr_pdf_replay_source_pin() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    assert boundaries.validate_pr_pdf_replay_source_pin(text) == []


def test_daily_production_boundary_rejects_moving_pr_pdf_replay_source_ref() -> None:
    invalid = """
jobs:
  daily-pdf-dfkai-replay:
    steps:
      - name: Replay ChatGPT-side daily PDF new conversation
        run: |
          source_ref="origin/${GITHUB_HEAD_REF}"
          git fetch origin "${source_ref#origin/}"
          python scripts/validate_chatgpt_daily_report_new_conversation_replay.py --source-ref "$source_ref"
"""
    errors = boundaries.validate_pr_pdf_replay_source_pin(invalid)
    assert any("moving pull-request branch ref" in error for error in errors)
    assert any("moving origin ref" in error for error in errors)
    assert any("immutable PR head SHA" in error for error in errors)


def test_pr_pdf_replay_requires_windows_dfkai_runtime_without_daily_full_hard_job() -> None:
    daily_text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    pr_text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")

    assert boundaries.workflow_job_block(daily_text, "daily-pdf-dfkai-replay") == ""
    assert "Install and validate DFKai-SB" not in daily_text
    assert "chatgpt_side_outputs_new_conversation_replay" not in daily_text
    assert boundaries.validate_dfkai_pdf_replay_job(
        pr_text,
        workflow_label="daily_pdf_replay_pr_validation",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    ) == []
    assert "Replay ChatGPT-side daily PDF" not in boundaries.workflow_job_block(
        daily_text,
        "daily-full-pipeline",
    )
    assert "Replay ChatGPT-side daily PDF" not in boundaries.workflow_job_block(
        pr_text,
        "daily-model-maintenance-pr-validation",
    )


def test_dfkai_replay_job_validator_rejects_generic_or_ubuntu_job() -> None:
    invalid = """
jobs:
  daily-pdf-dfkai-replay:
    needs: upstream
    runs-on: ubuntu-latest
    steps:
      - name: Replay ChatGPT-side daily PDF new conversation
        run: python scripts/validate_chatgpt_daily_report_new_conversation_replay.py
"""

    errors = boundaries.validate_dfkai_pdf_replay_job(
        invalid,
        workflow_label="fixture",
        needs_job="upstream",
        output_dir="expected-output",
        upload_step="Upload evidence",
    )

    assert any("windows-2025" in error for error in errors)
    assert any("Language.Fonts.Hant" in error for error in errors)
    assert any("Windows Update" in error for error in errors)
    assert any("DISM" in error for error in errors)
    assert any("long-path" in error for error in errors)
    assert any("temporary" in error for error in errors)
    assert any("kaiu.ttf" in error for error in errors)
    assert any("DFKai-SB" in error for error in errors)


def test_dfkai_replay_job_validator_requires_post_validation_dism_recovery() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    recovery_block = """          if ($dismExitCode -ne 0) {
            Write-Warning "DISM returned exit code $dismExitCode, but canonical DFKai-SB passed final file, identity, and glyph validation"
          }
"""
    env_line = (
        '          "CHATGPT_DAILY_DFKAI_FONT_PATH=$fontPath" | '
        "Out-File -FilePath $env:GITHUB_ENV -Append -Encoding utf8\n"
    )
    assert recovery_block in text
    assert env_line in text

    reordered = text.replace(recovery_block, "", 1).replace(
        env_line,
        recovery_block + env_line,
        1,
    )
    errors = boundaries.validate_dfkai_pdf_replay_job(
        reordered,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("final-state validation order" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_immediate_dism_exit_failure() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    capture = "              $dismExitCode = $LASTEXITCODE\n"
    assert capture in text
    immediate_failure = (
        capture
        + '              throw "DFKai-SB capability installation failed with DISM exit code $LASTEXITCODE"\n'
    )
    mutated = text.replace(capture, immediate_failure, 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("before rejecting a DISM exit code" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_missing_font_warning_only() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    fail_closed = (
        'throw "Required DFKai-SB font file is missing after capability install: '
        '$fontPath (DISM exit code $dismExitCode)"'
    )
    assert fail_closed in text
    mutated = text.replace(fail_closed, fail_closed.replace("throw", "Write-Warning"), 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("canonical font file remains missing" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_font_validation_warning_only() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    fail_closed = (
        'throw "DFKai-SB final font validation failed with exit code '
        '$fontValidationExitCode (DISM exit code $dismExitCode)"'
    )
    assert fail_closed in text
    mutated = text.replace(fail_closed, fail_closed.replace("throw", "Write-Warning"), 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("font identity or glyph validation fails" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_disabled_font_identity_assertion() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    assert "assert names & accepted" in text
    mutated = text.replace("assert names & accepted", "print(names & accepted)", 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("unexpected font identity" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_disabled_glyph_assertion() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    assert "assert not missing" in text
    mutated = text.replace("assert not missing", "print(missing)", 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("canary glyphs are missing" in error for error in errors)
