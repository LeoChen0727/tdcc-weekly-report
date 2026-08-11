from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config/model_research_workflow_entrypoints.csv"
OWNERSHIP_REGISTRY = ROOT / "config/model_research_artifact_ownership.csv"
WORKFLOW = ROOT / ".github/workflows/research_backtest_pipeline.yml"
PR_VALIDATION_WORKFLOW = ROOT / ".github/workflows/daily_model_maintenance_pr_validation.yml"

REQUIRED_COLUMNS = {
    "workflow_path",
    "workflow_input",
    "model_id",
    "producer",
    "latest_stage_glob",
    "history_stage_glob",
    "docs_stage_glob",
    "default_enabled",
    "formal_sync_allowed",
}

FORBIDDEN_WORKFLOW_SCRIPTS = {
    "scripts/build_daily_model_parameter_research.py",
    "scripts/build_daily_w_bottom_operation_sections.py",
    "scripts/build_daily_price_pullback_23ema_operation_section.py",
    "scripts/build_model_operation_readiness.py",
    "scripts/build_approved_operation_patterns.py",
    "scripts/update_daily_published_model_snapshots.py",
}

FORBIDDEN_STAGE_SNIPPETS = {
    "git add output/history/research/ || true",
    "git add output/history/daily_model_snapshots/",
    "git add output/latest/model_operation_readiness_latest",
    "git add output/latest/approved_operation_patterns_latest",
    "git add output/latest/daily_w_bottom_",
    "git add output/latest/daily_neckline_",
    "git add output/latest/daily_price_pullback_23ema_",
    "git add output/latest/daily_volume_breakout_",
}

SHARED_DATA_INPUT = "run_shared_model_research_data_refresh"
SHARED_DATA_COMMANDS = {
    "python scripts/build_monthly_revenue_point_in_time_panel.py",
    "python scripts/build_daily_model_signal_background_features.py",
}
SHARED_DATA_STAGE_COMMANDS = {
    "git add output/latest/research_backtest/monthly_revenue_point_in_time_panel_latest.* || true",
    "git add output/history/research/monthly_revenue_point_in_time_panel.csv || true",
    "git add output/latest/research_backtest/daily_model_signal_background_feature_panel_latest.* || true",
    "git add output/latest/research_backtest/daily_model_background_feature_catalog_latest.* || true",
}

BACKGROUND_REGISTRY_STRUCTURE_COMMAND = (
    "python scripts/validate_daily_model_background_data_registry.py --structure-only"
)
BACKGROUND_REGISTRY_FULL_COMMAND = (
    "python scripts/validate_daily_model_background_data_registry.py"
)
COMMIT_STEP_MARKER = "- name: Commit research and backtest outputs"

REVENUE_WORKFLOW_INPUT = "run_revenue_unreacted_range_research"
REVENUE_PROJECTION_CHAIN_STAGE_INPUT = (
    "run_revenue_unreacted_range_source_snapshot_projection_chain_only"
)
REVENUE_FORWARD_HOLDOUT_STAGE_INPUT = (
    "run_revenue_unreacted_range_forward_holdout_only"
)
REVENUE_PRODUCER = "scripts/build_revenue_unreacted_range_research.py"
REVENUE_FULL_BUILD_COMMAND = f"python {REVENUE_PRODUCER}"
REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND = (
    f"{REVENUE_FULL_BUILD_COMMAND} --stage forward_holdout"
)
REVENUE_FORWARD_HOLDOUT_STAGE_COMMANDS = {
    "git add output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_* || true",
    "git add output/history/research/"
    "revenue_unreacted_range_forward_holdout_* || true",
    "git add docs/latest/revenue_unreacted_range_forward_holdout_* || true",
}
REVENUE_FULL_STAGE_COMMANDS = {
    "git add output/latest/research_backtest/revenue_unreacted_range_* || true",
    "git add output/history/research/revenue_unreacted_range_* || true",
    "git add docs/latest/revenue_unreacted_range_* || true",
}
REVENUE_PROJECTION_CHAIN_BUILD_COMMAND = (
    f"{REVENUE_FULL_BUILD_COMMAND} --stage source_snapshot_projection_chain"
)
REVENUE_PROJECTION_CHAIN_VALIDATOR_COMMANDS = {
    "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
    "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    "python scripts/validate_revenue_unreacted_range_lag_strength_matrix.py",
    "python scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py",
    "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
    "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
    "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
    "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py",
    "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
}

PUBLISH_COMMIT = 'git commit -m "Update research backtest outputs"'
PUBLISH_PUSH = 'git push origin "HEAD:$TARGET_BRANCH"'
PUBLISH_FAIL_CLOSED_SHELL = "set -euo pipefail"
PUBLISH_NO_CHANGE_GUARD = (
    "if git diff --cached --quiet; then\n"
    'echo "No changes to commit"\n'
    "exit 0\n"
    "fi"
)
FORBIDDEN_PUBLISH_REWRITE = re.compile(
    r"^git\s+(?:pull|fetch|rebase|merge|reset|checkout|switch)\b"
)


@dataclass(frozen=True)
class WorkflowEntrypoint:
    workflow_path: str
    workflow_input: str
    model_id: str
    producer: str
    latest_stage_glob: str
    history_stage_glob: str
    docs_stage_glob: str
    default_enabled: bool
    formal_sync_allowed: bool


def _as_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized not in {"true", "false"}:
        raise ValueError(f"invalid boolean value: {value}")
    return normalized == "true"


def load_registry(path: Path = REGISTRY) -> list[WorkflowEntrypoint]:
    if not path.is_file():
        raise RuntimeError(f"missing model research workflow registry: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not REQUIRED_COLUMNS.issubset(reader.fieldnames or []):
            raise RuntimeError("model research workflow registry schema is incomplete")
        rows = list(reader)
    if not rows:
        raise RuntimeError("model research workflow registry is empty")
    return [
        WorkflowEntrypoint(
            workflow_path=row["workflow_path"].strip(),
            workflow_input=row["workflow_input"].strip(),
            model_id=row["model_id"].strip(),
            producer=row["producer"].strip(),
            latest_stage_glob=row["latest_stage_glob"].strip(),
            history_stage_glob=row["history_stage_glob"].strip(),
            docs_stage_glob=row["docs_stage_glob"].strip(),
            default_enabled=_as_bool(row["default_enabled"]),
            formal_sync_allowed=_as_bool(row["formal_sync_allowed"]),
        )
        for row in rows
    ]


def load_model_owned_producers(path: Path = OWNERSHIP_REGISTRY) -> dict[str, str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[str, str] = {}
    for row in rows:
        if row.get("change_policy", "").strip() != "model_owned_write":
            continue
        model_id = row.get("owner_model_id", "").strip()
        producer = row.get("producer", "").strip()
        previous = result.setdefault(model_id, producer)
        if previous != producer:
            raise RuntimeError(f"model has multiple model-owned producers: {model_id}")
    return result


def workflow_input_defaults(text: str) -> dict[str, str]:
    match = re.search(r"(?ms)^    inputs:\s*\n(?P<body>.*?)(?=^permissions:)", text)
    if not match:
        return {}
    body = match.group("body")
    rows: dict[str, str] = {}
    for input_match in re.finditer(
        r'(?ms)^      (?P<name>[A-Za-z0-9_]+):\s*\n.*?^        default: '
        r'(?:(?:"(?P<quoted>true|false)")|(?P<plain>true|false))\s*$',
        body,
    ):
        rows[input_match.group("name")] = (
            input_match.group("quoted") or input_match.group("plain")
        )
    return rows


def workflow_step_blocks(text: str) -> list[str]:
    return [block for block in re.split(r"(?m)^      - name: ", text)[1:] if block.strip()]


def _normalized_shell_block(block: str) -> str:
    return "\n".join(line.strip() for line in block.splitlines() if line.strip())


def validate_publish_block(text: str, blocks: list[str]) -> list[str]:
    errors: list[str] = []
    shell_lines = [line.strip() for line in text.splitlines()]
    commit_lines = [line for line in shell_lines if line.startswith("git commit ")]
    push_lines = [line for line in shell_lines if line.startswith("git push ")]
    publish_blocks = [
        block
        for block in blocks
        if any(
            line.strip().startswith(("git commit ", "git push "))
            or "ci_push_with_retry.sh" in line
            for line in block.splitlines()
        )
    ]

    if len(publish_blocks) != 1:
        errors.append(
            "research workflow must contain exactly one commit/push publish block: "
            f"observed={len(publish_blocks)}"
        )
        publish_block = ""
    else:
        publish_block = _normalized_shell_block(publish_blocks[0])

    if len(commit_lines) != 1:
        errors.append(
            "research workflow must contain exactly one research output commit: "
            f"observed={len(commit_lines)}"
        )
    elif commit_lines[0] != PUBLISH_COMMIT:
        errors.append("research workflow must not swallow or alter research output commit failure")

    if len(push_lines) != 1:
        errors.append(
            "research workflow must contain exactly one direct research output push: "
            f"observed={len(push_lines)}"
        )
    elif push_lines[0] != PUBLISH_PUSH:
        errors.append("research workflow push must be direct, non-force, and fail closed")

    if "ci_push_with_retry.sh" in text:
        errors.append("research workflow must not retry or rebase after validation")

    if publish_block:
        if PUBLISH_FAIL_CLOSED_SHELL not in publish_block:
            errors.append("research workflow publish block missing fail-closed shell mode")
        if "continue-on-error: true" in publish_block or "set +e" in publish_block:
            errors.append("research workflow publish block must not mask shell failure")
        if PUBLISH_NO_CHANGE_GUARD not in publish_block:
            errors.append("research workflow publish block missing staged no-change exit guard")
        else:
            shell_position = publish_block.find(PUBLISH_FAIL_CLOSED_SHELL)
            guard_position = publish_block.index(PUBLISH_NO_CHANGE_GUARD)
            commit_position = publish_block.find(PUBLISH_COMMIT)
            push_position = publish_block.find(PUBLISH_PUSH)
            if not (shell_position < guard_position < commit_position < push_position):
                errors.append(
                    "research workflow publish order must be fail-closed shell, staged guard, "
                    "commit, then direct push"
                )
        for line in publish_block.splitlines():
            if FORBIDDEN_PUBLISH_REWRITE.match(line):
                errors.append(
                    "research workflow publish block must not rewrite or resynchronize the target branch: "
                    f"{line}"
                )

    return errors


def validate_pr_workflow_text(text: str, rows: list[WorkflowEntrypoint]) -> list[str]:
    errors: list[str] = []
    for model_id in sorted({row.model_id for row in rows}):
        required_patterns = {
            f'      - "scripts/{model_id}_*.py"',
            f'      - "tests/test_{model_id}_*.py"',
        }
        for pattern in sorted(required_patterns):
            if pattern not in text:
                errors.append(
                    "daily model PR validation path filter missing model research namespace: "
                    f"{pattern.strip()}"
                )
    return errors


def validate_workflow_text(
    text: str,
    rows: list[WorkflowEntrypoint],
    model_owned_producers: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    defaults = workflow_input_defaults(text)
    blocks = workflow_step_blocks(text)
    errors.extend(validate_publish_block(text, blocks))
    stripped_lines = [line.strip() for line in text.splitlines()]
    any_selected_line = next(
        (line for line in text.splitlines() if "ANY_RESEARCH_SELECTED:" in line),
        "",
    )
    model_selected_line = next(
        (line for line in text.splitlines() if "MODEL_RESEARCH_SELECTED:" in line),
        "",
    )

    if "run_model_parameter_research" in text:
        errors.append("legacy cross-model workflow input is forbidden: run_model_parameter_research")
    if 'git pull --rebase --autostash origin "$TARGET_BRANCH" || true' in text:
        errors.append("research workflow must not pull or ignore sync failure after producers run")
    pre_run_sync = 'git pull --ff-only origin "$TARGET_BRANCH"'
    if pre_run_sync not in text:
        errors.append("research workflow missing fail-closed pre-run branch synchronization")
    branch_sync_lines = [
        line.strip()
        for line in text.splitlines()
        if FORBIDDEN_PUBLISH_REWRITE.match(line.strip())
    ]
    if branch_sync_lines != [pre_run_sync]:
        errors.append(
            "research workflow must contain exactly one pre-run ff-only synchronization and no "
            f"post-validation branch rewrite: observed={branch_sync_lines}"
        )
    for name, default in sorted(defaults.items()):
        if default != "false":
            errors.append(f"research workflow input must default false: {name}={default}")
    for script in sorted(FORBIDDEN_WORKFLOW_SCRIPTS):
        if f"python {script}" in text:
            errors.append(f"research workflow must not invoke formal or cross-model producer: {script}")
    for snippet in sorted(FORBIDDEN_STAGE_SNIPPETS):
        if snippet in text:
            errors.append(f"research workflow contains forbidden broad/formal stage path: {snippet}")

    if defaults.get(SHARED_DATA_INPUT) != "false":
        errors.append(f"missing opt-in shared objective data input with false default: {SHARED_DATA_INPUT}")
    if f"github.event.inputs.{SHARED_DATA_INPUT} == 'true'" not in any_selected_line:
        errors.append(f"shared objective data input missing from ANY_RESEARCH_SELECTED: {SHARED_DATA_INPUT}")
    shared_blocks = [
        block for block in blocks if all(command in block for command in SHARED_DATA_COMMANDS)
    ]
    if len(shared_blocks) != 1:
        errors.append("shared objective data refresh must appear in exactly one workflow step")
    elif f"github.event.inputs.{SHARED_DATA_INPUT} == 'true'" not in shared_blocks[0]:
        errors.append("shared objective data refresh has wrong workflow input condition")
    for command in SHARED_DATA_STAGE_COMMANDS:
        if command not in text:
            errors.append(f"shared objective data stage allowlist missing from workflow: {command}")

    stage_inputs = (
        REVENUE_FORWARD_HOLDOUT_STAGE_INPUT,
        REVENUE_PROJECTION_CHAIN_STAGE_INPUT,
    )
    for stage_input in stage_inputs:
        if defaults.get(stage_input) != "false":
            errors.append(
                "missing opt-in revenue stage input with false default: "
                f"{stage_input}"
            )
        if any(row.workflow_input == stage_input for row in rows):
            errors.append(
                "revenue stage mode must not be registered as a second producer "
                f"entrypoint: {stage_input}"
            )
        stage_input_condition = f"github.event.inputs.{stage_input} == 'true'"
        if (
            stage_input_condition in any_selected_line
            or stage_input_condition in model_selected_line
        ):
            errors.append(
                "revenue stage mode must require the primary revenue workflow input "
                f"instead of selecting research independently: {stage_input}"
            )

    holdout_requires_primary = (
        'if [[ "${{ github.event.inputs.'
        f'{REVENUE_FORWARD_HOLDOUT_STAGE_INPUT}'
        ' }}" == "true" && "${{ github.event.inputs.'
        f'{REVENUE_WORKFLOW_INPUT}'
        ' }}" != "true" ]]; then'
    )
    mutually_exclusive_modes = (
        'if [[ "${{ github.event.inputs.'
        f'{REVENUE_FORWARD_HOLDOUT_STAGE_INPUT}'
        ' }}" == "true" && "${{ github.event.inputs.'
        f'{REVENUE_PROJECTION_CHAIN_STAGE_INPUT}'
        ' }}" == "true" ]]; then'
    )
    if holdout_requires_primary not in text:
        errors.append(
            "revenue forward holdout stage must fail closed unless the primary revenue "
            "workflow input is selected"
        )
    if mutually_exclusive_modes not in text:
        errors.append(
            "revenue forward holdout and source projection chain stage modes must be "
            "mutually exclusive"
        )

    revenue_blocks = [
        block
        for block in blocks
        if REVENUE_PROJECTION_CHAIN_BUILD_COMMAND in block
        or REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND in block
    ]
    if len(revenue_blocks) != 1:
        errors.append(
            "revenue stage commands must appear together in exactly one "
            "workflow step"
        )
    else:
        revenue_block = revenue_blocks[0]
        revenue_lines = [line.strip() for line in revenue_block.splitlines()]
        holdout_if = (
            'if [[ "${{ github.event.inputs.'
            f'{REVENUE_FORWARD_HOLDOUT_STAGE_INPUT}'
            ' }}" == "true" ]]; then'
        )
        projection_elif = (
            'elif [[ "${{ github.event.inputs.'
            f'{REVENUE_PROJECTION_CHAIN_STAGE_INPUT}'
            ' }}" == "true" ]]; then'
        )
        try:
            holdout_index = revenue_lines.index(holdout_if)
            projection_index = revenue_lines.index(projection_elif, holdout_index + 1)
            else_index = revenue_lines.index("else", projection_index + 1)
            fi_index = revenue_lines.index("fi", else_index + 1)
        except ValueError:
            errors.append(
                "revenue holdout and source projection stage modes are missing their "
                "guarded stage/full branches"
            )
        else:
            holdout_python = {
                line for line in revenue_lines[holdout_index + 1 : projection_index]
                if line.startswith("python ")
            }
            projection_python = {
                line for line in revenue_lines[projection_index + 1 : else_index]
                if line.startswith("python ")
            }
            full_python = {
                line for line in revenue_lines[else_index + 1 : fi_index]
                if line.startswith("python ")
            }
            expected_holdout_python = {
                REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND,
            }
            if holdout_python != expected_holdout_python:
                errors.append(
                    "revenue forward holdout stage mode must contain only its model-owned "
                    "producer stage with persisted independent replay: "
                    f"actual={sorted(holdout_python)}"
                )
            expected_projection_python = {
                REVENUE_PROJECTION_CHAIN_BUILD_COMMAND,
                *REVENUE_PROJECTION_CHAIN_VALIDATOR_COMMANDS,
            }
            if projection_python != expected_projection_python:
                errors.append(
                    "revenue source projection chain stage mode must contain only its "
                    "existing producer stage and cutoff-chain validators: "
                    f"actual={sorted(projection_python)}"
                )
            if REVENUE_FULL_BUILD_COMMAND not in full_python:
                errors.append(
                    "revenue full research branch must retain the existing producer"
                )
            if REVENUE_PROJECTION_CHAIN_BUILD_COMMAND in full_python:
                errors.append(
                    "revenue full research branch must not replace the full producer with "
                    "the source projection chain stage"
                )
            if REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND in full_python:
                errors.append(
                    "revenue full research branch must not replace the full producer with "
                    "the forward holdout stage"
                )
        revenue_condition = f"github.event.inputs.{REVENUE_WORKFLOW_INPUT} == 'true'"
        if revenue_condition not in revenue_block:
            errors.append(
                "revenue stage modes must remain nested under the "
                "primary revenue workflow input"
            )

    commit_step_name = COMMIT_STEP_MARKER.removeprefix("- name: ")
    commit_blocks = [
        block
        for block in blocks
        if block.splitlines() and block.splitlines()[0].strip() == commit_step_name
    ]
    if len(commit_blocks) != 1:
        errors.append("research artifact commit step must appear exactly once")
    else:
        commit_lines = [line.strip() for line in commit_blocks[0].splitlines()]
        revenue_stage_if = (
            'if [[ "${{ github.event.inputs.'
            f'{REVENUE_WORKFLOW_INPUT}'
            ' }}" == "true" ]]; then'
        )
        holdout_stage_if = (
            'if [[ "${{ github.event.inputs.'
            f'{REVENUE_FORWARD_HOLDOUT_STAGE_INPUT}'
            ' }}" == "true" ]]; then'
        )
        try:
            revenue_stage_index = commit_lines.index(revenue_stage_if)
            holdout_stage_index = commit_lines.index(
                holdout_stage_if, revenue_stage_index + 1
            )
            stage_else_index = commit_lines.index("else", holdout_stage_index + 1)
            stage_fi_index = commit_lines.index("fi", stage_else_index + 1)
        except ValueError:
            errors.append(
                "revenue forward holdout commit staging must be nested under the "
                "primary revenue artifact stage"
            )
        else:
            holdout_stage_commands = {
                line
                for line in commit_lines[holdout_stage_index + 1 : stage_else_index]
                if line.startswith("git add ")
            }
            full_stage_commands = {
                line
                for line in commit_lines[stage_else_index + 1 : stage_fi_index]
                if line.startswith("git add ")
            }
            if holdout_stage_commands != REVENUE_FORWARD_HOLDOUT_STAGE_COMMANDS:
                errors.append(
                    "revenue forward holdout commit stage must contain only its exact "
                    "latest/history/docs artifact prefixes: "
                    f"actual={sorted(holdout_stage_commands)}"
                )
            if full_stage_commands != REVENUE_FULL_STAGE_COMMANDS:
                errors.append(
                    "revenue full research commit stage must retain its existing "
                    "latest/history/docs artifact prefixes: "
                    f"actual={sorted(full_stage_commands)}"
                )

    volume_source = "python scripts/build_volume_breakout_confirmed_operation_backtest.py"
    volume_v2 = "python scripts/build_volume_range_breakout_v2_research.py"
    if volume_source in text and volume_v2 in text and text.index(volume_source) > text.index(volume_v2):
        errors.append("volume breakout source refresh must precede the model-owned v2 producer")

    registry_models = {row.model_id: row.producer for row in rows}
    if registry_models != model_owned_producers:
        errors.append(
            "workflow registry must cover every model_owned_write producer exactly: "
            f"workflow={registry_models}; ownership={model_owned_producers}"
        )

    inputs = [row.workflow_input for row in rows]
    producers = [row.producer for row in rows]
    if len(inputs) != len(set(inputs)):
        errors.append("duplicate workflow_input in model research workflow registry")
    if len(producers) != len(set(producers)):
        errors.append("duplicate producer in model research workflow registry")

    for row in rows:
        if row.workflow_path != ".github/workflows/research_backtest_pipeline.yml":
            errors.append(f"unsupported workflow path for model research entrypoint: {row.workflow_path}")
        if row.default_enabled:
            errors.append(f"model research workflow input must be opt-in: {row.workflow_input}")
        if row.formal_sync_allowed:
            errors.append(f"model research workflow must not perform formal sync: {row.workflow_input}")
        if defaults.get(row.workflow_input) != "false":
            errors.append(f"missing opt-in workflow input with false default: {row.workflow_input}")
        if f"github.event.inputs.{row.workflow_input} == 'true'" not in any_selected_line:
            errors.append(f"workflow input missing from ANY_RESEARCH_SELECTED: {row.workflow_input}")
        if f"github.event.inputs.{row.workflow_input} == 'true'" not in model_selected_line:
            errors.append(f"workflow input missing from MODEL_RESEARCH_SELECTED: {row.workflow_input}")

        command = f"python {row.producer}"
        producer_blocks = [block for block in blocks if command in block]
        if len(producer_blocks) != 1:
            errors.append(f"model-owned producer must appear in exactly one workflow step: {row.producer}")
        else:
            block = producer_blocks[0]
            condition = f"github.event.inputs.{row.workflow_input} == 'true'"
            if condition not in block:
                errors.append(f"model-owned producer has wrong workflow input condition: {row.producer}")
            other_producers = sorted(
                producer for producer in producers if producer != row.producer and f"python {producer}" in block
            )
            if other_producers:
                errors.append(
                    f"model-owned workflow step mixes producers: {row.model_id}; others={other_producers}"
                )
            mixed_shared_commands = sorted(command for command in SHARED_DATA_COMMANDS if command in block)
            if mixed_shared_commands:
                errors.append(
                    f"model-owned workflow step contains shared data refresh: "
                    f"{row.model_id}; commands={mixed_shared_commands}"
                )

        for stage_glob in (row.latest_stage_glob, row.history_stage_glob, row.docs_stage_glob):
            stage_command = f"git add {stage_glob} || true"
            if stage_command not in text:
                errors.append(f"model-owned stage allowlist missing from workflow: {stage_command}")

    shared_positions = [text.index(command) for command in SHARED_DATA_COMMANDS if command in text]
    model_positions = [
        text.index(f"python {row.producer}")
        for row in rows
        if f"python {row.producer}" in text
    ]
    if shared_positions and model_positions:
        shared_first = min(shared_positions)
        model_first = min(model_positions)
        if shared_first > model_first:
            errors.append("shared objective data refresh must precede model-owned producers")
    if model_positions and pre_run_sync in text and text.index(pre_run_sync) > min(model_positions):
        errors.append("target branch synchronization must precede model-owned producers")

    structure_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if line == BACKGROUND_REGISTRY_STRUCTURE_COMMAND
    ]
    full_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if line == BACKGROUND_REGISTRY_FULL_COMMAND
    ]
    producer_line_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if any(line == f"python {row.producer}" for row in rows)
    ]
    commit_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if line == COMMIT_STEP_MARKER
    ]
    structure_blocks = [
        block
        for block in blocks
        if BACKGROUND_REGISTRY_STRUCTURE_COMMAND in {
            line.strip() for line in block.splitlines()
        }
    ]
    full_blocks = [
        block
        for block in blocks
        if BACKGROUND_REGISTRY_FULL_COMMAND in {
            line.strip() for line in block.splitlines()
        }
    ]
    if len(structure_positions) != 1 or len(structure_blocks) != 1:
        errors.append(
            "research workflow must run background registry structure-only validation "
            "exactly once before model producers"
        )
    if len(full_positions) != 2 or len(full_blocks) != 2:
        errors.append(
            "research workflow must run full background artifact validation exactly "
            "once for non-model research and once after model producers"
        )
    else:
        non_model_blocks = [
            block
            for block in full_blocks
            if "env.MODEL_RESEARCH_SELECTED != 'true'" in block
        ]
        post_model_blocks = [
            block
            for block in full_blocks
            if "env.MODEL_RESEARCH_SELECTED == 'true'" in block
        ]
        if len(non_model_blocks) != 1:
            errors.append(
                "existing registered artifacts full validation must be conditional on "
                "MODEL_RESEARCH_SELECTED != true"
            )
        if len(post_model_blocks) != 1:
            errors.append(
                "post-run full background artifact validation must be conditional on "
                "MODEL_RESEARCH_SELECTED == true"
            )
    if producer_line_positions:
        if not structure_positions or structure_positions[0] >= min(producer_line_positions):
            errors.append(
                "background registry structure-only validation must precede model-owned producers"
            )
        if not full_positions or max(full_positions) <= max(producer_line_positions):
            errors.append(
                "full background artifact validation must run after model-owned producers"
            )
        if not commit_positions or not full_positions or max(full_positions) >= min(commit_positions):
            errors.append(
                "full background artifact validation must pass before research artifacts are committed"
            )
    post_run_parity = "python scripts/validate_daily_model_research_parity.py"
    if model_positions and (
        post_run_parity not in text or text.index(post_run_parity) < max(model_positions)
    ):
        errors.append("daily model research parity validation must run after model-owned producers")

    return errors


def validate() -> list[str]:
    errors: list[str] = []
    try:
        rows = load_registry()
        model_owned_producers = load_model_owned_producers()
    except (OSError, RuntimeError, ValueError) as exc:
        return [str(exc)]
    if not WORKFLOW.is_file():
        return [f"missing research workflow: {WORKFLOW}"]
    errors.extend(validate_workflow_text(WORKFLOW.read_text(encoding="utf-8"), rows, model_owned_producers))
    if not PR_VALIDATION_WORKFLOW.is_file():
        errors.append(f"missing daily model PR validation workflow: {PR_VALIDATION_WORKFLOW}")
    else:
        errors.extend(validate_pr_workflow_text(PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8"), rows))
    for row in rows:
        if not (ROOT / row.producer).is_file():
            errors.append(f"missing model-owned workflow producer: {row.producer}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"model research workflow isolation validation passed: {WORKFLOW.relative_to(ROOT)}")
    print(f"validated_entrypoints={len(load_registry())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
