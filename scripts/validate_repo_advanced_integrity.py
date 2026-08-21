from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from daily_snapshot_revision_utils import (  # noqa: E402
    latest_snapshot_revision_for_date,
    select_latest_snapshot_revisions,
)

ROOT = SCRIPT_DIR.parent
INVENTORY_CSV = ROOT / "config" / "repo_production_inventory.csv"
LINEAGE_CSV = ROOT / "config" / "report_artifact_lineage.csv"
RUNTIME_LINEAGE_CONTRACT = ROOT / "config" / "runtime_file_lineage_contract.csv"
PDF_GOLDEN_CONTRACT = ROOT / "config" / "pdf_golden_regression_contract.csv"
HISTORICAL_REPLAY_CONTRACT = ROOT / "config" / "historical_replay_semantic_contract.csv"
STOCK_MODEL_CONTRACT_REGISTRY = ROOT / "config" / "stock_model_contract_registry.csv"
MODEL_CONDITION_SPEC = ROOT / "config" / "daily_model_condition_spec.csv"
EXTERNAL_SOURCE_CONTRACT = ROOT / "config" / "external_data_source_contract.csv"
DAILY_MODEL_LAYER = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
TRACER = ROOT / "scripts" / "trace_runtime_file_lineage.py"
FRESHNESS_CSV = ROOT / "output" / "latest" / "data_freshness_latest.csv"
MODEL_PARAMETERS_CSV = ROOT / "output" / "latest" / "daily_candidate_model_parameters_latest.csv"
DAILY_MODEL_SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
MODEL_PARITY_CSV = ROOT / "output" / "latest" / "research_backtest" / "daily_model_research_parity_latest.csv"
MODEL_REGISTRY_CSV = ROOT / "output" / "latest" / "daily_report_model_registry_latest.csv"

HISTORICAL_REPLAY_CONTRACT_COLUMNS = (
    "artifact_id",
    "artifact_glob",
    "window_days",
    "min_snapshots",
    "required_columns",
    "forbidden_columns",
    "allowed_report_lines",
    "allowed_report_buckets",
    "date_column",
    "file_date_regex",
)
MAX_HISTORICAL_REPLAY_WINDOW_DAYS = 3660


REQUIRED_CONFIGS = {
    RUNTIME_LINEAGE_CONTRACT,
    PDF_GOLDEN_CONTRACT,
    HISTORICAL_REPLAY_CONTRACT,
    STOCK_MODEL_CONTRACT_REGISTRY,
    MODEL_CONDITION_SPEC,
    EXTERNAL_SOURCE_CONTRACT,
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def load_historical_replay_contract(errors: list[str]) -> list[dict[str, str]]:
    if not HISTORICAL_REPLAY_CONTRACT.exists():
        errors.append(
            f"missing historical replay semantic contract: {rel(HISTORICAL_REPLAY_CONTRACT)}"
        )
        return []
    try:
        with HISTORICAL_REPLAY_CONTRACT.open(
            "r", encoding="utf-8-sig", newline=""
        ) as handle:
            reader = csv.DictReader(handle)
            actual_columns = tuple(reader.fieldnames or ())
            if actual_columns != HISTORICAL_REPLAY_CONTRACT_COLUMNS:
                errors.append(
                    "historical replay semantic contract schema drift: "
                    f"expected={HISTORICAL_REPLAY_CONTRACT_COLUMNS!r} "
                    f"actual={actual_columns!r}"
                )
                return []
            rows: list[dict[str, str]] = []
            for line_number, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    errors.append(
                        "historical replay semantic contract field count mismatch "
                        f"at line {line_number}"
                    )
                    continue
                rows.append({key: str(value) for key, value in row.items()})
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"cannot parse historical replay semantic contract: {exc}")
        return []
    if not rows:
        errors.append("historical replay semantic contract is empty")
    return rows


def split_list(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(read_text(path))


def dotted_get(data: dict[str, Any], path: str) -> Any:
    current: Any = data
    for part in split_list(path.replace(".", ";")):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def false_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value is False
    return str(value or "").strip().lower() in {"false", "0", "no", "n", ""}


def int_value(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def validate_degraded_external_source(source_id: str, data: dict[str, Any], observed_status: str) -> list[str]:
    errors: list[str] = []
    if source_id != "calendar_sources" or observed_status not in {"stale_ok", "degraded_blocked_effect"}:
        return errors

    twse = dotted_get(data, "sources.twse_ex_right_ex_dividend")
    if not isinstance(twse, dict):
        return [f"external source calendar_sources {observed_status} missing sources.twse_ex_right_ex_dividend object"]

    consecutive = int_value(twse.get("consecutive_live_failures"), 9999)
    max_consecutive = int_value(twse.get("max_consecutive_live_failures"), 0)
    if max_consecutive <= 0:
        errors.append(f"external source calendar_sources {observed_status} requires max_consecutive_live_failures > 0")
    if consecutive <= 0:
        errors.append(f"external source calendar_sources {observed_status} requires consecutive_live_failures > 0")
    if max_consecutive > 0 and consecutive > max_consecutive:
        errors.append(
            f"external source calendar_sources {observed_status} consecutive_live_failures={consecutive} exceeds max={max_consecutive}"
        )
    if not false_bool(twse.get("model_effect_allowed")):
        errors.append(f"external source calendar_sources {observed_status} requires model_effect_allowed=False")
    if not false_bool(twse.get("pdf_effect_allowed")):
        errors.append(f"external source calendar_sources {observed_status} requires pdf_effect_allowed=False")
    if not false_bool(twse.get("calendar_effect_allowed")):
        errors.append(f"external source calendar_sources {observed_status} requires calendar_effect_allowed=False")

    cached_count = int_value(twse.get("cached_rows"), 0)
    note = str(twse.get("note", ""))
    if observed_status == "stale_ok":
        stale_max = int_value(twse.get("stale_max_trading_days"), 0)
        cache_age_max = int_value(twse.get("cache_age_trading_days_max"), 9999)
        if cached_count <= 0:
            errors.append("external source calendar_sources stale_ok requires cached_rows > 0")
        if stale_max <= 0:
            errors.append("external source calendar_sources stale_ok requires stale_max_trading_days > 0")
        if cache_age_max > stale_max:
            errors.append(
                f"external source calendar_sources stale_ok cache_age_trading_days_max={cache_age_max} exceeds stale_max={stale_max}"
            )
        if "stale reminder-only" not in note and "stale reminder only" not in note:
            errors.append("external source calendar_sources stale_ok requires stale reminder-only note")
    elif observed_status == "degraded_blocked_effect":
        blocked_count = int_value(twse.get("blocked_rows"), 0)
        cached_total = int_value(twse.get("cached_total_rows"), 0)
        if max(blocked_count, cached_count, cached_total) <= 0:
            errors.append("external source calendar_sources degraded_blocked_effect requires cached or blocked rows > 0")
        if "blocked-effect" not in note and "blocked effect" not in note and "cannot affect" not in note:
            errors.append("external source calendar_sources degraded_blocked_effect requires blocked-effect note")
    return errors


def ast_tree(path: Path) -> ast.Module:
    return ast.parse(read_text(path), filename=rel(path))


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = call_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return ""


def string_literals(path: Path) -> list[str]:
    try:
        tree = ast_tree(path)
    except SyntaxError:
        return []
    values: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            values.append(node.value.replace("\\", "/"))
    return values


def function_names(path: Path) -> set[str]:
    return {node.name for node in ast.walk(ast_tree(path)) if isinstance(node, ast.FunctionDef)}


def validate_required_configs() -> list[str]:
    return [f"missing advanced integrity config: {rel(path)}" for path in REQUIRED_CONFIGS if not path.exists()]


def validate_runtime_file_lineage_contract() -> list[str]:
    errors: list[str] = []
    rows = read_csv_rows(RUNTIME_LINEAGE_CONTRACT)
    inventory = {row["path"]: row for row in read_csv_rows(INVENTORY_CSV)}
    lineage_rows = read_csv_rows(LINEAGE_CSV)
    lineage_producers = {
        part.strip()
        for row in lineage_rows
        for part in row.get("producer", "").split(";")
        if part.strip().endswith(".py")
    }
    if not rows:
        return [f"missing or empty runtime lineage contract: {rel(RUNTIME_LINEAGE_CONTRACT)}"]
    if not TRACER.exists():
        errors.append(f"missing runtime lineage tracer: {rel(TRACER)}")
    else:
        tracer_text = read_text(TRACER)
        for token in ("FileAccessTracer", "builtins.open", "Path.open", "runpy.run_path"):
            if token not in tracer_text:
                errors.append(f"runtime lineage tracer missing required hook token: {token}")

    covered_scripts = {row.get("script_path", "").strip() for row in rows}
    missing_producers = sorted(
        producer
        for producer in lineage_producers
        if producer in inventory
        and inventory[producer].get("status") == "active"
        and inventory[producer].get("owner") in {"daily_production", "repo_infrastructure", "tdcc_weekly", "individual_stock", "market_risk", "warrant"}
        and producer not in covered_scripts
        and not producer.startswith("tests/")
    )
    if missing_producers:
        errors.append(f"lineage producers missing runtime file contract rows: {missing_producers}")

    for row in rows:
        script = row.get("script_path", "").strip()
        if script not in inventory:
            errors.append(f"runtime lineage contract references non-inventoried script: {script}")
            continue
        if not (ROOT / script).exists():
            errors.append(f"runtime lineage contract references missing script: {script}")
            continue
        for artifact in split_list(row.get("required_read_artifacts", "")):
            if not (ROOT / artifact).exists():
                errors.append(f"{script} required runtime read artifact does not exist: {artifact}")
        required_writes = split_list(row.get("required_write_prefixes", ""))
        if not required_writes:
            errors.append(f"{script} has no required write prefix in runtime lineage contract")
        literals = string_literals(ROOT / script)
        forbidden = split_list(row.get("forbidden_read_prefixes", ""))
        for literal in literals:
            for prefix in forbidden:
                if literal.startswith(prefix) or prefix in literal:
                    errors.append(f"{script} contains forbidden runtime source literal {literal!r} matching {prefix!r}")
    return errors


def validate_pdf_golden_contract() -> list[str]:
    errors: list[str] = []
    rows = read_csv_rows(PDF_GOLDEN_CONTRACT)
    if len(rows) != 6:
        errors.append(f"PDF golden contract must define exactly 6 ChatGPT-side PDFs, got {len(rows)}")
    generator_text = read_text(PDF_GENERATOR)
    entrypoint_text = read_text(ENTRYPOINT)
    if "exactly 6 PDF paths" not in entrypoint_text:
        errors.append("official ChatGPT-side entrypoint must hard-stop unless exactly 6 PDFs are emitted")
    report_ids = {row.get("report_id", "") for row in rows}
    required_ids = {
        "mainstream_daily_recommendation_highlight",
        "mainstream_full_candidate_list",
        "non_mainstream_daily_recommendation_highlight",
        "non_mainstream_full_candidate_list",
        "warrant_market_auxiliary",
        "market_risk_background",
    }
    missing_ids = sorted(required_ids - report_ids)
    if missing_ids:
        errors.append(f"PDF golden contract missing report ids: {missing_ids}")
    for row in rows:
        report_id = row.get("report_id", "")
        builder = row.get("builder_function", "")
        literal = row.get("required_literal", "")
        if f"def {builder}(" not in generator_text:
            errors.append(f"PDF golden contract builder missing in generator for {report_id}: {builder}")
        if literal and literal not in generator_text:
            errors.append(f"PDF golden contract literal missing in generator for {report_id}: {literal}")
        if row.get("output_route") != "chatgpt_side_outputs":
            errors.append(f"PDF golden contract must route ChatGPT-side PDF to chatgpt_side_outputs: {report_id}")
        if not split_list(row.get("required_sections", "")):
            errors.append(f"PDF golden contract row has no required sections: {report_id}")
        try:
            min_pages = int(row.get("min_pages", "0"))
            max_pages = int(row.get("max_pages", "0"))
        except ValueError:
            errors.append(f"PDF golden contract page bounds are not integers: {report_id}")
            continue
        if min_pages < 1 or max_pages < min_pages:
            errors.append(f"PDF golden contract invalid page bounds: {report_id}")
    return errors


def latest_main_price_date() -> str:
    rows = read_csv_rows(FRESHNESS_CSV)
    if not rows:
        return ""
    return rows[0].get("main_price_date", "").strip()


def parse_contract_date(value: str) -> datetime | None:
    text = str(value or "").strip()
    if not text or text.lower() in {"none", "n/a", "na"}:
        return None
    for fmt in ("%Y-%m-%d", "%Y%m%d"):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return None


def model_contract_valid_on(row: dict[str, str], snapshot_dt: datetime) -> bool:
    effective_from = parse_contract_date(row.get("effective_from", ""))
    deprecated_after = parse_contract_date(row.get("deprecated_after", ""))
    if effective_from and snapshot_dt < effective_from:
        return False
    if deprecated_after and snapshot_dt > deprecated_after:
        return False
    return True


def historical_model_parameters_path(date_text: str) -> Path | None:
    record = latest_snapshot_revision_for_date(
        DAILY_MODEL_SNAPSHOT_DIR,
        "model_parameters",
        date_text,
        repository_root=ROOT,
    )
    return record.path if record is not None else None


def known_historical_models_for_date(
    date_text: str,
    current_models: set[str],
    contract_rows: list[dict[str, str]],
) -> set[str]:
    models: set[str] = set()
    parameter_snapshot = historical_model_parameters_path(date_text)
    if parameter_snapshot is not None:
        models.update(
            row.get("model_id", "").strip()
            for row in read_csv_rows(parameter_snapshot)
            if row.get("model_id", "").strip()
        )
    try:
        snapshot_dt = datetime.strptime(date_text, "%Y%m%d")
    except ValueError:
        return models or current_models
    models.update(
        row.get("model_id", "").strip()
        for row in contract_rows
        if row.get("model_id", "").strip() and model_contract_valid_on(row, snapshot_dt)
    )
    return models or current_models


def validate_historical_replay_semantics() -> list[str]:
    errors: list[str] = []
    contracts = load_historical_replay_contract(errors)
    if errors:
        return errors
    validated_contracts: list[
        tuple[dict[str, str], re.Pattern[str], int, int]
    ] = []
    seen_artifact_ids: dict[str, int] = {}
    seen_artifact_globs: dict[str, int] = {}
    for line_number, contract in enumerate(contracts, start=2):
        row_errors: list[str] = []
        artifact_id = contract["artifact_id"].strip()
        glob_pattern = contract["artifact_glob"].strip()
        if not artifact_id:
            row_errors.append(
                f"historical replay semantic contract line {line_number} has empty artifact_id"
            )
        elif artifact_id in seen_artifact_ids:
            row_errors.append(
                "historical replay semantic contract has duplicate artifact_id "
                f"{artifact_id!r} at lines {seen_artifact_ids[artifact_id]} and {line_number}"
            )
        else:
            seen_artifact_ids[artifact_id] = line_number
        if not glob_pattern:
            row_errors.append(
                f"historical replay semantic contract line {line_number} has empty artifact_glob"
            )
        elif glob_pattern in seen_artifact_globs:
            row_errors.append(
                "historical replay semantic contract has duplicate artifact_glob "
                f"{glob_pattern!r} at lines {seen_artifact_globs[glob_pattern]} and {line_number}"
            )
        else:
            seen_artifact_globs[glob_pattern] = line_number

        regex_text = contract["file_date_regex"].strip()
        try:
            file_date_regex = re.compile(regex_text)
        except (re.error, RecursionError, OverflowError) as exc:
            row_errors.append(
                "historical replay semantic contract has invalid file_date_regex "
                f"at line {line_number}: {exc}"
            )
            file_date_regex = re.compile(r"(?!)")
        else:
            if file_date_regex.groups < 1:
                row_errors.append(
                    "historical replay semantic contract file_date_regex must contain "
                    f"a report-date capture group at line {line_number}"
                )

        parsed_numbers: dict[str, int] = {}
        for column in ("window_days", "min_snapshots"):
            raw_value = contract[column].strip()
            if not re.fullmatch(r"[1-9][0-9]*", raw_value):
                row_errors.append(
                    f"historical replay semantic contract {column} must be a positive integer "
                    f"at line {line_number}: {raw_value!r}"
                )
                continue
            if len(raw_value) > 10:
                row_errors.append(
                    f"historical replay semantic contract {column} is too large "
                    f"to parse at line {line_number}"
                )
                continue
            try:
                parsed_numbers[column] = int(raw_value)
            except ValueError as exc:
                row_errors.append(
                    f"historical replay semantic contract {column} is too large "
                    f"to parse at line {line_number}: {exc}"
                )
        window_days = parsed_numbers.get("window_days", 0)
        min_snapshots = parsed_numbers.get("min_snapshots", 0)
        if window_days > MAX_HISTORICAL_REPLAY_WINDOW_DAYS:
            row_errors.append(
                "historical replay semantic contract window_days exceeds reasonable bound "
                f"{MAX_HISTORICAL_REPLAY_WINDOW_DAYS} at line {line_number}: {window_days}"
            )
        if window_days > 0 and min_snapshots > window_days + 1:
            row_errors.append(
                "historical replay semantic contract min_snapshots exceeds the maximum "
                f"calendar snapshots in its window at line {line_number}: "
                f"min_snapshots={min_snapshots} window_days={window_days}"
            )
        errors.extend(row_errors)
        if not row_errors:
            validated_contracts.append(
                (contract, file_date_regex, window_days, min_snapshots)
            )
    if errors:
        return errors

    parameters = read_csv_rows(MODEL_PARAMETERS_CSV)
    contract_rows = read_csv_rows(STOCK_MODEL_CONTRACT_REGISTRY)
    current_models = {row.get("model_id", "").strip() for row in parameters if row.get("model_id", "").strip()}
    main_date = latest_main_price_date()
    if not main_date:
        errors.append("cannot validate historical replay: missing main_price_date")
        return errors
    try:
        latest_dt = datetime.strptime(main_date, "%Y%m%d")
    except ValueError:
        errors.append(f"cannot validate historical replay: invalid main_price_date {main_date!r}")
        return errors

    for contract, file_date_regex, window_days, min_snapshots in validated_contracts:
        glob_pattern = contract["artifact_glob"].strip()
        artifact_id = contract["artifact_id"].strip()
        required_columns = set(split_list(contract.get("required_columns", "")))
        forbidden_columns = set(split_list(contract.get("forbidden_columns", "")))
        allowed_lines = set(split_list(contract.get("allowed_report_lines", "")))
        allowed_buckets = set(split_list(contract.get("allowed_report_buckets", "")))
        date_column = contract.get("date_column", "")
        cutoff = latest_dt - timedelta(days=window_days)
        matched: list[tuple[str, Path]] = []
        try:
            snapshots = select_latest_snapshot_revisions(
                DAILY_MODEL_SNAPSHOT_DIR,
                artifact_id,
                through_date=main_date,
                repository_root=ROOT,
            )
        except (RuntimeError, ValueError, OSError) as exc:
            errors.append(
                f"historical replay contract {glob_pattern} cannot select manifest revisions: {exc}"
            )
            continue
        for snapshot in snapshots:
            path = snapshot.path
            match = file_date_regex.fullmatch(path.name)
            if not match:
                errors.append(
                    "historical replay manifest-selected path does not match file_date_regex: "
                    f"artifact_id={artifact_id} path={rel(path)}"
                )
                continue
            date_text = match.group(1)
            if date_text != snapshot.report_date:
                errors.append(
                    "historical replay manifest date/path date mismatch: "
                    f"artifact_id={artifact_id} manifest_date={snapshot.report_date} "
                    f"path_date={date_text} path={rel(path)}"
                )
                continue
            try:
                file_dt = datetime.strptime(date_text, "%Y%m%d")
            except ValueError:
                errors.append(f"historical replay file has invalid date: {rel(path)}")
                continue
            if cutoff <= file_dt <= latest_dt:
                matched.append((date_text, path))
        if len(matched) < min_snapshots:
            errors.append(f"historical replay contract {glob_pattern} has {len(matched)} snapshots, needs {min_snapshots}")
        for date_text, path in sorted(matched):
            rows = read_csv_rows(path)
            if not rows:
                errors.append(f"historical replay snapshot is empty: {rel(path)}")
                continue
            known_models = known_historical_models_for_date(date_text, current_models, contract_rows)
            columns = set(rows[0])
            missing = sorted(required_columns - columns)
            if missing:
                errors.append(f"historical replay snapshot missing columns {missing}: {rel(path)}")
            leaked = sorted(forbidden_columns & columns)
            if leaked:
                errors.append(f"historical replay snapshot contains forbidden decision columns {leaked}: {rel(path)}")
            for idx, row in enumerate(rows, start=2):
                model_id = row.get("model_id", "").strip()
                stock_id = row.get("stock_id", "").strip()
                if not stock_id or not model_id:
                    errors.append(f"historical replay missing stock/model key at {rel(path)}:{idx}")
                    continue
                if model_id not in known_models:
                    errors.append(f"historical replay unknown model_id {model_id!r} at {rel(path)}:{idx}")
                if date_column and row.get(date_column, "").strip() != date_text:
                    errors.append(f"historical replay signal_date mismatch at {rel(path)}:{idx}")
                line = row.get("report_line", "").strip()
                bucket = row.get("report_bucket", "").strip()
                if line not in allowed_lines:
                    errors.append(f"historical replay invalid report_line {line!r} at {rel(path)}:{idx}")
                if bucket not in allowed_buckets:
                    errors.append(f"historical replay invalid report_bucket {bucket!r} at {rel(path)}:{idx}")
                if row.get("mainstream_report_eligible", "") != "True" and row.get("non_mainstream_report_eligible", "") != "True":
                    errors.append(f"historical replay stock has no report membership at {rel(path)}:{idx}: {stock_id}")
    return errors


def model_spec_calls() -> dict[str, dict[str, str]]:
    tree = ast_tree(DAILY_MODEL_LAYER)
    specs: dict[str, dict[str, str]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or call_name(node.func) != "ModelSpec":
            continue
        if len(node.args) < 10:
            continue
        model_id_node = node.args[0]
        if not isinstance(model_id_node, ast.Constant) or not isinstance(model_id_node.value, str):
            continue
        specs[model_id_node.value] = {
            "condition_function": call_name(node.args[8]),
            "score_function": call_name(node.args[9]),
        }
    return specs


def score_profile_ids() -> set[str]:
    tree = ast_tree(DAILY_MODEL_LAYER)
    ids: set[str] = set()
    for node in ast.walk(tree):
        value: ast.AST | None = None
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "MODEL_SCORE_PROFILES" for target in node.targets
        ):
            value = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == "MODEL_SCORE_PROFILES":
            value = node.value
        if isinstance(value, ast.Dict):
            for key in value.keys:
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    ids.add(key.value)
    return ids


def validate_model_condition_spec() -> list[str]:
    errors: list[str] = []
    rows = read_csv_rows(MODEL_CONDITION_SPEC)
    if not rows:
        return [f"missing or empty model condition spec: {rel(MODEL_CONDITION_SPEC)}"]
    specs = model_spec_calls()
    functions = function_names(DAILY_MODEL_LAYER)
    profiles = score_profile_ids()
    parity = {row.get("model_id", ""): row.get("research_baseline_status", "") for row in read_csv_rows(MODEL_PARITY_CSV)}
    registry_models = {
        row.get("model_id", "")
        for row in read_csv_rows(MODEL_REGISTRY_CSV)
        if row.get("model_registry_active", "") == "True"
    }
    spec_models = {row.get("model_id", "") for row in rows}
    missing = sorted(registry_models - spec_models)
    if missing:
        errors.append(f"machine-readable model condition spec missing active registry models: {missing}")
    source_text = read_text(DAILY_MODEL_LAYER)
    for row in rows:
        model_id = row.get("model_id", "").strip()
        production_source = row.get("production_source", "").strip()
        condition = row.get("condition_function", "").strip()
        score = row.get("score_function", "").strip()
        profile = row.get("score_profile_id", "").strip()
        expected_parity = row.get("research_baseline_status", "").strip()
        if model_id not in parity:
            errors.append(f"machine-readable spec model missing parity output: {model_id}")
        elif parity[model_id] != expected_parity:
            errors.append(f"machine-readable spec parity mismatch for {model_id}: {expected_parity} != {parity[model_id]}")
        if production_source == "ModelSpec":
            actual = specs.get(model_id)
            if not actual:
                errors.append(f"ModelSpec missing in AST for model: {model_id}")
                continue
            if actual["condition_function"] != condition:
                errors.append(f"condition function mismatch for {model_id}: {condition} != {actual['condition_function']}")
            if actual["score_function"] != score:
                errors.append(f"score function mismatch for {model_id}: {score} != {actual['score_function']}")
        else:
            if production_source not in functions:
                errors.append(f"production source function missing for {model_id}: {production_source}")
            if f'"model_id": "{model_id}"' not in source_text:
                errors.append(f"production source does not carry model_id literal for {model_id}")
        if condition not in functions:
            errors.append(f"condition function missing for {model_id}: {condition}")
        if score not in functions:
            errors.append(f"score function missing for {model_id}: {score}")
        if profile != "not_applicable" and profile not in profiles:
            errors.append(f"score profile missing for {model_id}: {profile}")
    return errors


def validate_external_source_contract(*, include_static_ownership: bool = True) -> list[str]:
    errors: list[str] = []
    rows = read_csv_rows(EXTERNAL_SOURCE_CONTRACT)
    if not rows:
        return [f"missing or empty external data source contract: {rel(EXTERNAL_SOURCE_CONTRACT)}"]
    freshness_rows = read_csv_rows(FRESHNESS_CSV)
    freshness = freshness_rows[0] if freshness_rows else {}
    main_date = freshness.get("main_price_date", "")
    inventory_paths = (
        {row["path"] for row in read_csv_rows(INVENTORY_CSV)}
        if include_static_ownership
        else set()
    )
    for row in rows:
        source_id = row.get("source_id", "")
        artifact = row.get("status_artifact", "")
        path = ROOT / artifact
        if not path.exists():
            errors.append(f"external source contract artifact missing for {source_id}: {artifact}")
            continue
        if include_static_ownership:
            for field in ("producer", "validator"):
                for entry in split_list(row.get(field, "")):
                    if entry.endswith(".py") and entry not in inventory_paths:
                        errors.append(
                            f"external source contract {source_id} references "
                            f"non-inventoried {field}: {entry}"
                        )
        date_col = row.get("freshness_date_column", "").strip()
        ready_col = row.get("readiness_column", "").strip()
        if date_col:
            observed = freshness.get(date_col, "")
            if row.get("require_matches_main_price_date", "") == "True" and observed != main_date:
                errors.append(f"external source {source_id} date {date_col}={observed} does not match main_price_date={main_date}")
        readiness = freshness.get(ready_col, "") if ready_col else ""
        if (
            source_id == "warrant_flow"
            and ready_col == "warrant_daily_publish_allowed"
            and not str(readiness).strip()
            and freshness.get("warrant_ready", "") == "True"
        ):
            readiness = "True"
        if ready_col and readiness != "True":
            errors.append(f"external source {source_id} readiness {ready_col} is not True")
        json_path = row.get("json_status_path", "").strip()
        if json_path:
            data = load_json(path)
            observed_status = dotted_get(data, json_path)
            allowed = set(split_list(row.get("allowed_statuses", "")))
            if str(observed_status) not in allowed:
                errors.append(f"external source {source_id} status {json_path}={observed_status!r} not in {sorted(allowed)}")
            else:
                errors.extend(validate_degraded_external_source(source_id, data, str(observed_status)))
    return errors


def validate(*, include_external_sources: bool = True) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_required_configs())
    errors.extend(validate_runtime_file_lineage_contract())
    errors.extend(validate_pdf_golden_contract())
    errors.extend(validate_historical_replay_semantics())
    errors.extend(validate_model_condition_spec())
    if include_external_sources:
        errors.extend(validate_external_source_contract())
    return errors


def validate_runtime_external_sources() -> list[str]:
    return validate_external_source_contract(include_static_ownership=False)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate repository advanced integrity contracts.")
    parser.add_argument(
        "--runtime-external-sources-only",
        action="store_true",
        help="Validate only runtime external-source artifacts, dates, readiness, and statuses.",
    )
    args = parser.parse_args([] if argv is None else argv)

    errors = validate_runtime_external_sources() if args.runtime_external_sources_only else validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if args.runtime_external_sources_only:
        print("runtime external-source integrity validation passed")
        print(f"validated_external_sources={rel(EXTERNAL_SOURCE_CONTRACT)}")
        return 0
    print("repo advanced integrity validation passed")
    print(f"validated_runtime_lineage={rel(RUNTIME_LINEAGE_CONTRACT)}")
    print(f"validated_pdf_golden={rel(PDF_GOLDEN_CONTRACT)}")
    print(f"validated_historical_replay={rel(HISTORICAL_REPLAY_CONTRACT)}")
    print(f"validated_model_condition_spec={rel(MODEL_CONDITION_SPEC)}")
    print(f"validated_external_sources={rel(EXTERNAL_SOURCE_CONTRACT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
