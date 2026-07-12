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
        r'(?ms)^      (?P<name>[A-Za-z0-9_]+):\s*\n.*?^        default: "(?P<default>true|false)"\s*$',
        body,
    ):
        rows[input_match.group("name")] = input_match.group("default")
    return rows


def workflow_step_blocks(text: str) -> list[str]:
    return [block for block in re.split(r"(?m)^      - name: ", text)[1:] if block.strip()]


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
