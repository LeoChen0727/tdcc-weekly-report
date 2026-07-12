from __future__ import annotations

import ast
import csv
import fnmatch
import hashlib
import io
import os
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
STOCK_MODEL_REGISTRY = ROOT / "config" / "stock_model_contract_registry.csv"
CONDITION_SPEC = ROOT / "config" / "daily_model_condition_spec.csv"
MODEL_OWNERSHIP = ROOT / "config" / "daily_model_semantic_ownership.csv"
SHARED_SEMANTICS = ROOT / "config" / "daily_model_shared_semantic_registry.csv"
SEMANTIC_MIGRATIONS = ROOT / "config" / "daily_model_semantic_migrations.csv"
BACKGROUND_DATA_REGISTRY = ROOT / "config" / "daily_model_background_data_registry.csv"
DATA_SHARING_REGISTRY = ROOT / "config" / "daily_model_data_sharing_registry.csv"
DATA_SHARING_MIGRATIONS = ROOT / "config" / "daily_model_data_sharing_migrations.csv"
VALIDATOR_INDEPENDENCE = ROOT / "config" / "daily_model_validator_independence.csv"
RESEARCH_ARTIFACT_OWNERSHIP = ROOT / "config" / "model_research_artifact_ownership.csv"
FORMAL_EVIDENCE_PINS = ROOT / "config" / "formal_model_evidence_pins.csv"

BASELINE_REFERENCE_PREFIX = "baseline_"
BASELINE_MIGRATION_ID = "baseline_20260712"
VALID_MIGRATION_STATUS = "validated_user_approved_migration"
BASELINE_MIGRATION_ROW_SHA256 = "e1e0ec4ead5c146218815242ff005c25890dcfea8d7e20d75141c99312623ffc"
BASELINE_DATA_MIGRATION_ID = "baseline_data_20260712"
BASELINE_DATA_MIGRATION_ROW_SHA256 = "ee5d7ce4d274807e858e8d1f6206bfcf07765f074104c21b93d059b08d19c165"

MODEL_OWNERSHIP_COLUMNS = (
    "model_id",
    "production_source_file",
    "execution_entry_functions",
    "semantic_item_count",
    "semantic_sha256",
    "ownership_status",
    "shared_semantic_policy",
    "change_policy",
    "last_migration_id",
    "approval_reference",
    "required_validation_commands",
    "notes",
)
SHARED_SEMANTIC_COLUMNS = (
    "source_file",
    "semantic_item",
    "semantic_class",
    "consumer_models",
    "canonical_ast_sha256",
    "change_policy",
    "last_migration_id",
    "approval_reference",
    "required_validation_commands",
    "notes",
)
SEMANTIC_MIGRATION_COLUMNS = (
    "migration_id",
    "source_file",
    "changed_semantics",
    "previous_sha256s",
    "new_sha256s",
    "affected_models",
    "validation_commands",
    "user_approval_reference",
    "migration_status",
    "notes",
)
DATA_SHARING_COLUMNS = (
    "data_family_id",
    "ownership_mode",
    "owner_model_or_family",
    "registered_producers",
    "producer_write_scope",
    "consumer_access_mode",
    "approved_consumer_models",
    "data_contract_sha256",
    "last_migration_id",
    "sharing_decision_reference",
    "formal_evidence_policy",
    "new_consumer_policy",
    "notes",
)
DATA_SHARING_MIGRATION_COLUMNS = (
    "migration_id",
    "changed_data_families",
    "previous_contract_sha256s",
    "new_contract_sha256s",
    "affected_models",
    "validation_commands",
    "user_approval_reference",
    "migration_status",
    "notes",
)
VALIDATOR_INDEPENDENCE_COLUMNS = (
    "validator_path",
    "validator_role",
    "production_source_file",
    "imported_production_symbols",
    "independence_claim",
    "allowed_evidence_use",
    "notes",
)

VALID_MODEL_OWNERSHIP_STATUS = {
    "model_owned_module",
    "contained_legacy_monolith",
    "contained_model_family_dispatcher",
    "approved_shared_module",
}
VALID_SHARED_SEMANTIC_CLASS = {
    "shared_technical",
    "contained_model_family_semantic",
    "contained_legacy_cross_model_semantic",
}
VALID_DATA_OWNERSHIP_MODE = {
    "approved_shared_objective",
    "approved_shared_replay_read_only",
    "latest_context_not_historical",
    "model_owned_not_shared",
    "model_family_owned_not_shared",
    "cross_model_audit_not_model_evidence",
    "legacy_frozen_no_new_consumers",
}

VOLUME_MODEL_FAMILY = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
}
W_BOTTOM_MODEL_FAMILY = {
    "w_bottom_right_side",
    "neckline_volume_breakout_confirmation",
}
MODEL_FAMILIES = (VOLUME_MODEL_FAMILY, W_BOTTOM_MODEL_FAMILY)

# These helpers only convert, clamp, or retrieve values. Business gates, indicators,
# routing, scoring, and model interpretation are deliberately excluded.
SHARED_TECHNICAL_ITEMS = {
    "function:candidate_lookup",
    "function:category",
    "function:clamp",
    "function:flag",
    "function:load_volume_price_history",
    "function:num",
    "function:price_history_for_stock",
    "function:taxonomy_lookup",
    "function:taxonomy_or_source",
    "function:text",
    "function:truthy",
}

BACKGROUND_SCOPE_TO_OWNERSHIP_MODE = {
    "shared_objective": {"approved_shared_objective"},
    "shared_replay_evidence": {"approved_shared_replay_read_only"},
    "shared_replay_source": {"approved_shared_replay_read_only"},
    "latest_only_context": {"latest_context_not_historical"},
    "model_specific": {"model_owned_not_shared", "model_family_owned_not_shared"},
    "model_research_output": {
        "model_owned_not_shared",
        "model_family_owned_not_shared",
        "cross_model_audit_not_model_evidence",
        "legacy_frozen_no_new_consumers",
    },
}


@dataclass(frozen=True)
class ModelSemantic:
    model_id: str
    source_file: str
    entry_functions: tuple[str, ...]
    items: dict[str, str]
    semantic_sha256: str


class SourceSemanticGraph:
    def __init__(self, source_file: str, source_text: str) -> None:
        self.source_file = source_file
        self.tree = ast.parse(source_text, filename=source_file)
        self.functions: dict[str, ast.FunctionDef | ast.AsyncFunctionDef] = {}
        self.globals: dict[str, ast.AST] = {}
        for node in self.tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.functions[node.name] = node
            elif isinstance(node, ast.ClassDef):
                self.globals[node.name] = node
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    for name in _assigned_names(target):
                        self.globals[name] = node
            elif isinstance(node, ast.AnnAssign):
                for name in _assigned_names(node.target):
                    self.globals[name] = node

    def function_exists_anywhere(self, name: str, roots: Iterable[str]) -> bool:
        if name in self.functions:
            return True
        for root in roots:
            node = self.functions.get(root)
            if node is None:
                continue
            if any(
                isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name == name
                for child in ast.walk(node)
            ):
                return True
        return False

    def semantic_items(self, roots: Iterable[str]) -> dict[str, str]:
        missing = sorted({name for name in roots if name not in self.functions})
        if missing:
            raise ValueError(f"{self.source_file}: missing execution entry functions: {missing}")

        reachable_functions: set[str] = set()
        stack = list(roots)
        while stack:
            name = stack.pop()
            if name in reachable_functions:
                continue
            node = self.functions.get(name)
            if node is None:
                continue
            reachable_functions.add(name)
            for child in ast.walk(node):
                if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                    if child.func.id in self.functions:
                        stack.append(child.func.id)

        reachable_globals: set[str] = set()
        global_stack: list[str] = []
        for name in reachable_functions:
            global_stack.extend(_loaded_names(self.functions[name]))
        while global_stack:
            name = global_stack.pop()
            if name in reachable_globals or name not in self.globals:
                continue
            reachable_globals.add(name)
            global_stack.extend(_loaded_names(self.globals[name]))

        items: dict[str, str] = {}
        for name in sorted(reachable_functions):
            items[f"function:{name}"] = canonical_ast_sha256(self.functions[name])
        for name in sorted(reachable_globals):
            items[f"global:{name}"] = canonical_ast_sha256(self.globals[name])
        return items


def _assigned_names(target: ast.AST) -> list[str]:
    if isinstance(target, ast.Name):
        return [target.id]
    if isinstance(target, (ast.Tuple, ast.List)):
        names: list[str] = []
        for item in target.elts:
            names.extend(_assigned_names(item))
        return names
    return []


def _loaded_names(node: ast.AST) -> list[str]:
    return [
        child.id
        for child in ast.walk(node)
        if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load)
    ]


def canonical_ast_sha256(node: ast.AST) -> str:
    payload = ast.dump(node, annotate_fields=True, include_attributes=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def aggregate_semantic_sha256(items: dict[str, str]) -> str:
    payload = "\n".join(f"{key}={items[key]}" for key in sorted(items))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def semantic_record_sha256(semantic_key: str, row: dict[str, str]) -> str:
    if semantic_key.startswith("model:"):
        fields = (
            "model_id",
            "production_source_file",
            "execution_entry_functions",
            "semantic_item_count",
            "semantic_sha256",
            "ownership_status",
            "shared_semantic_policy",
            "change_policy",
        )
    elif semantic_key.startswith("item:"):
        fields = (
            "source_file",
            "semantic_item",
            "semantic_class",
            "consumer_models",
            "canonical_ast_sha256",
            "change_policy",
        )
    else:
        raise ValueError(f"unsupported semantic record key: {semantic_key}")
    payload = "\n".join([f"semantic_key={semantic_key}", *(f"{field}={row[field]}" for field in fields)])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def migration_row_sha256(row: dict[str, str]) -> str:
    payload = "\n".join(f"{field}={row[field]}" for field in SEMANTIC_MIGRATION_COLUMNS)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def data_contract_sha256(row: dict[str, str]) -> str:
    fields = (
        "data_family_id",
        "scope",
        "owner_lane",
        "producer",
        "artifact_path",
        "source_artifacts",
        "consumer_surfaces",
        "consumer_models",
        "point_in_time_status",
        "allowed_use",
        "forbidden_use",
        "validator",
        "retention_policy",
        "cleanup_status",
        "notes",
    )
    payload = "\n".join(f"{field}={row[field]}" for field in fields)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def data_migration_row_sha256(row: dict[str, str]) -> str:
    payload = "\n".join(f"{field}={row[field]}" for field in DATA_SHARING_MIGRATION_COLUMNS)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def split_list(value: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in str(value or "").split(";") if part.strip())


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def strict_csv_rows(
    path: Path,
    required_columns: Iterable[str],
    errors: list[str],
    *,
    text: str | None = None,
) -> list[dict[str, str]]:
    if text is None:
        if not path.is_file():
            errors.append(f"missing registry: {display_path(path)}")
            return []
        text = path.read_text(encoding="utf-8-sig")
    raw_rows = list(csv.reader(io.StringIO(text, newline="")))
    if not raw_rows:
        errors.append(f"empty registry: {display_path(path)}")
        return []
    header = raw_rows[0]
    required = tuple(required_columns)
    if set(header) != set(required):
        errors.append(
            f"{display_path(path)}: exact schema mismatch; "
            f"expected={list(required)}; actual={header}"
        )
        return []
    duplicate_headers = sorted({name for name in header if header.count(name) > 1})
    if duplicate_headers:
        errors.append(f"{display_path(path)}: duplicate columns: {duplicate_headers}")
        return []
    rows: list[dict[str, str]] = []
    for line_no, raw in enumerate(raw_rows[1:], start=2):
        if len(raw) != len(header):
            errors.append(
                f"{display_path(path)} row {line_no}: field count {len(raw)} "
                f"does not match header count {len(header)}"
            )
            continue
        rows.append({header[idx]: str(value or "").strip() for idx, value in enumerate(raw)})
    return rows


def _active_stock_models(errors: list[str], *, text: str | None = None) -> dict[str, dict[str, str]]:
    columns = (
        "model_id",
        "model_name",
        "contract_version",
        "owner_lane",
        "production_source_file",
        "condition_function",
        "score_function",
        "score_profile_id",
        "input_columns",
        "output_columns",
        "pdf_visibility",
        "approved_for_daily_pdf",
        "approved_for_tdcc_weekly_pdf",
        "approved_for_individual_pdf",
        "research_baseline_required",
        "promotion_required",
        "effective_from",
        "deprecated_after",
        "change_reason",
    )
    rows = strict_csv_rows(STOCK_MODEL_REGISTRY, columns, errors, text=text)
    active: dict[str, dict[str, str]] = {}
    for row in rows:
        if row["deprecated_after"].lower() not in {"", "none"}:
            continue
        model_id = row["model_id"]
        if model_id in active:
            errors.append(f"duplicate active stock model: {model_id}")
        active[model_id] = row
    return active


def build_current_model_semantics(
    ownership_rows: list[dict[str, str]],
    active_models: dict[str, dict[str, str]],
    errors: list[str],
    *,
    root: Path = ROOT,
) -> tuple[dict[str, ModelSemantic], dict[tuple[str, str], tuple[str, ...]]]:
    ownership_by_model: dict[str, dict[str, str]] = {}
    for row in ownership_rows:
        model_id = row["model_id"]
        if model_id in ownership_by_model:
            errors.append(f"duplicate daily model semantic ownership row: {model_id}")
        ownership_by_model[model_id] = row
    if set(ownership_by_model) != set(active_models):
        errors.append(
            "daily model semantic ownership must match active model registry exactly: "
            f"missing={sorted(set(active_models) - set(ownership_by_model))}; "
            f"extra={sorted(set(ownership_by_model) - set(active_models))}"
        )

    graph_cache: dict[str, SourceSemanticGraph] = {}
    semantics: dict[str, ModelSemantic] = {}
    item_consumers: dict[tuple[str, str], list[str]] = defaultdict(list)
    source_consumers: dict[str, set[str]] = defaultdict(set)
    for model_id in sorted(set(active_models) & set(ownership_by_model)):
        contract = active_models[model_id]
        owner = ownership_by_model[model_id]
        source_file = owner["production_source_file"]
        if source_file != contract["production_source_file"]:
            errors.append(
                f"{model_id}: semantic ownership source {source_file} does not match stock registry "
                f"{contract['production_source_file']}"
            )
        source = root / source_file
        if not source.is_file():
            errors.append(f"{model_id}: missing production source file: {source_file}")
            continue
        if source_file not in graph_cache:
            try:
                graph_cache[source_file] = SourceSemanticGraph(
                    source_file, source.read_text(encoding="utf-8")
                )
            except (SyntaxError, UnicodeError) as exc:
                errors.append(f"{source_file}: cannot parse production source: {exc}")
                continue
        graph = graph_cache[source_file]
        entries = split_list(owner["execution_entry_functions"])
        if not entries:
            errors.append(f"{model_id}: execution_entry_functions is empty")
            continue
        condition = contract["condition_function"]
        score = contract["score_function"]
        if condition not in entries:
            errors.append(f"{model_id}: condition_function must be an execution entry: {condition}")
        if not graph.function_exists_anywhere(score, entries):
            errors.append(f"{model_id}: score_function is not reachable from execution entries: {score}")
        elif score in graph.functions and score not in entries:
            errors.append(f"{model_id}: top-level score_function must be an execution entry: {score}")
        try:
            items = graph.semantic_items(entries)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        semantic_hash = aggregate_semantic_sha256(items)
        if owner["semantic_item_count"] != str(len(items)):
            errors.append(
                f"{model_id}: semantic_item_count drift; expected={owner['semantic_item_count']}; "
                f"actual={len(items)}"
            )
        if owner["semantic_sha256"] != semantic_hash:
            errors.append(
                f"{model_id}: semantic SHA drift; expected={owner['semantic_sha256']}; "
                f"actual={semantic_hash}"
            )
        if owner["ownership_status"] not in VALID_MODEL_OWNERSHIP_STATUS:
            errors.append(f"{model_id}: invalid ownership_status={owner['ownership_status']}")
        if not owner["change_policy"] or not owner["required_validation_commands"]:
            errors.append(f"{model_id}: missing change policy or required validators")
        source_consumers[source_file].add(model_id)
        semantics[model_id] = ModelSemantic(model_id, source_file, entries, items, semantic_hash)
        for item in items:
            item_consumers[(source_file, item)].append(model_id)

    for source_file, consumers in source_consumers.items():
        if len(consumers) < 2:
            continue
        for model_id in sorted(consumers):
            status = ownership_by_model[model_id]["ownership_status"]
            if status == "model_owned_module":
                errors.append(
                    f"{model_id}: model_owned_module cannot share production source {source_file} "
                    f"with {sorted(consumers - {model_id})}"
                )

    shared = {
        key: tuple(sorted(consumers))
        for key, consumers in item_consumers.items()
        if len(consumers) > 1
    }
    return semantics, shared


def expected_shared_semantic_class(item: str, consumers: Iterable[str]) -> str:
    consumer_set = set(consumers)
    if item in SHARED_TECHNICAL_ITEMS:
        return "shared_technical"
    if any(consumer_set <= family for family in MODEL_FAMILIES):
        return "contained_model_family_semantic"
    return "contained_legacy_cross_model_semantic"


def _load_base_file(base_ref: str, path: Path) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{base_ref}:{rel}"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def default_base_ref() -> str | None:
    explicit = os.environ.get("MODEL_DATA_INDEPENDENCE_BASE_REF", "").strip()
    if explicit:
        return explicit
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    branch = result.stdout.strip()
    if branch in {"", "HEAD", "main"}:
        return None
    exists = subprocess.run(
        ["git", "rev-parse", "--verify", "origin/main"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return "origin/main" if exists.returncode == 0 else None


def _validate_semantic_migration(
    *,
    semantic_key: str,
    previous_hash: str,
    new_hash: str,
    previous_row: dict[str, str] | None,
    current_row: dict[str, str],
    migrations: dict[str, dict[str, str]],
    affected_models: set[str],
    errors: list[str],
) -> None:
    migration_id = current_row.get("last_migration_id", "")
    if not migration_id or migration_id == (previous_row or {}).get("last_migration_id", ""):
        errors.append(f"{semantic_key}: changed semantics lack a new migration_id")
        return
    migration = migrations.get(migration_id)
    if migration is None:
        errors.append(f"{semantic_key}: missing semantic migration row {migration_id}")
        return
    changed = split_list(migration["changed_semantics"])
    previous_hashes = split_list(migration["previous_sha256s"])
    new_hashes = split_list(migration["new_sha256s"])
    if not (len(changed) == len(previous_hashes) == len(new_hashes)):
        errors.append(f"{migration_id}: changed_semantics and SHA lists must align")
        return
    change_map = {changed[idx]: (previous_hashes[idx], new_hashes[idx]) for idx in range(len(changed))}
    if change_map.get(semantic_key) != (previous_hash, new_hash):
        errors.append(
            f"{semantic_key}: migration {migration_id} does not pin exact previous/new semantic SHA"
        )
    if not affected_models <= set(split_list(migration["affected_models"])):
        errors.append(f"{semantic_key}: migration {migration_id} omits affected models")
    approval = migration["user_approval_reference"]
    if not approval or approval.startswith(BASELINE_REFERENCE_PREFIX):
        errors.append(f"{semantic_key}: migration {migration_id} lacks user approval reference")
    if current_row.get("approval_reference", "") != approval:
        errors.append(f"{semantic_key}: registry approval reference must match migration {migration_id}")
    if migration["migration_status"] != VALID_MIGRATION_STATUS:
        errors.append(f"{semantic_key}: migration {migration_id} is not validated")
    if not migration["validation_commands"]:
        errors.append(f"{semantic_key}: migration {migration_id} lacks validation commands")


def _migration_change_map(
    migration: dict[str, str], errors: list[str]
) -> dict[str, tuple[str, str]]:
    changed = split_list(migration["changed_semantics"])
    previous_hashes = split_list(migration["previous_sha256s"])
    new_hashes = split_list(migration["new_sha256s"])
    if not (len(changed) == len(previous_hashes) == len(new_hashes)):
        errors.append(
            f"{migration['migration_id']}: changed_semantics and previous/new SHA lists must align"
        )
        return {}
    if len(set(changed)) != len(changed):
        errors.append(f"{migration['migration_id']}: duplicate changed_semantics entries")
    return {
        changed[idx]: (previous_hashes[idx], new_hashes[idx])
        for idx in range(len(changed))
    }


def _validate_current_migration_chain(
    ownership_rows: list[dict[str, str]],
    shared_rows: list[dict[str, str]],
    migration_rows: list[dict[str, str]],
    errors: list[str],
) -> None:
    if not migration_rows or migration_rows[0]["migration_id"] != BASELINE_MIGRATION_ID:
        errors.append(f"{BASELINE_MIGRATION_ID} must be the first append-only semantic migration row")
        return
    baseline = migration_rows[0]
    if migration_row_sha256(baseline) != BASELINE_MIGRATION_ROW_SHA256:
        errors.append(
            f"immutable semantic baseline digest drift: expected={BASELINE_MIGRATION_ROW_SHA256}; "
            f"actual={migration_row_sha256(baseline)}"
        )
    baseline_map = _migration_change_map(baseline, errors)
    if baseline["migration_status"] != "baseline_registered":
        errors.append(f"{BASELINE_MIGRATION_ID}: invalid baseline status")
    if any(previous != "BASELINE" for previous, _new in baseline_map.values()):
        errors.append(f"{BASELINE_MIGRATION_ID}: every previous SHA must be BASELINE")

    migration_by_id: dict[str, dict[str, str]] = {}
    migration_maps: dict[str, dict[str, tuple[str, str]]] = {}
    latest_hash: dict[str, str] = {}
    latest_migration: dict[str, str] = {}
    for key, (_previous, new_hash) in baseline_map.items():
        latest_hash[key] = new_hash
        latest_migration[key] = BASELINE_MIGRATION_ID
    for index, migration in enumerate(migration_rows):
        migration_id = migration["migration_id"]
        if migration_id in migration_by_id:
            errors.append(f"duplicate semantic migration id: {migration_id}")
            continue
        migration_by_id[migration_id] = migration
        change_map = baseline_map if index == 0 else _migration_change_map(migration, errors)
        migration_maps[migration_id] = change_map
        if index == 0:
            continue
        if migration["migration_status"] != VALID_MIGRATION_STATUS:
            errors.append(f"{migration_id}: non-baseline migration is not validated")
        approval = migration["user_approval_reference"]
        if not approval or approval.startswith(BASELINE_REFERENCE_PREFIX):
            errors.append(f"{migration_id}: non-baseline migration lacks user approval reference")
        if not migration["validation_commands"]:
            errors.append(f"{migration_id}: non-baseline migration lacks validation commands")
        for key, (previous_hash, new_hash) in change_map.items():
            expected_previous = latest_hash.get(key, "NEW")
            if previous_hash != expected_previous:
                errors.append(
                    f"{migration_id}: {key} previous SHA does not match the latest append-only chain tip"
                )
            latest_hash[key] = new_hash
            latest_migration[key] = migration_id

    current_records: list[tuple[str, dict[str, str], set[str]]] = []
    for row in ownership_rows:
        model_key = f"model:{row['model_id']}"
        if model_key not in baseline_map and row["ownership_status"] not in {
            "model_owned_module",
            "approved_shared_module",
        }:
            errors.append(
                f"{model_key}: new formal model must use a model-owned module; "
                "contained legacy statuses are baseline-only"
            )
        current_records.append((model_key, row, {row["model_id"]}))
    for row in shared_rows:
        consumers = set(split_list(row["consumer_models"]))
        current_records.append(
            (f"item:{row['source_file']}::{row['semantic_item']}", row, consumers)
        )
    for key, row, affected_models in current_records:
        migration_id = row["last_migration_id"]
        migration = migration_by_id.get(migration_id)
        if migration is None:
            errors.append(f"{key}: last_migration_id does not resolve: {migration_id}")
            continue
        if latest_migration.get(key) != migration_id:
            errors.append(f"{key}: registry must point to latest migration {latest_migration.get(key)}")
        current_hash = semantic_record_sha256(key, row)
        change_map = migration_maps.get(migration_id, {})
        pair = change_map.get(key)
        if pair is None or pair[1] != current_hash:
            errors.append(f"{key}: current semantic record is not pinned by migration {migration_id}")
        if migration_id == BASELINE_MIGRATION_ID:
            if row["approval_reference"] != "baseline_inventory_not_share_approval_20260712":
                errors.append(f"{key}: baseline approval reference drift")
            continue
        if row["approval_reference"] != migration["user_approval_reference"]:
            errors.append(f"{key}: approval reference must match migration {migration_id}")
        if not affected_models <= set(split_list(migration["affected_models"])):
            errors.append(f"{key}: migration {migration_id} omits affected models")


def validate_model_semantic_ownership(*, base_ref: str | None = None) -> tuple[list[str], dict[str, ModelSemantic]]:
    errors: list[str] = []
    active_models = _active_stock_models(errors)
    ownership_rows = strict_csv_rows(MODEL_OWNERSHIP, MODEL_OWNERSHIP_COLUMNS, errors)
    shared_rows = strict_csv_rows(SHARED_SEMANTICS, SHARED_SEMANTIC_COLUMNS, errors)
    migration_rows = strict_csv_rows(SEMANTIC_MIGRATIONS, SEMANTIC_MIGRATION_COLUMNS, errors)
    if errors:
        return errors, {}
    semantics, actual_shared = build_current_model_semantics(ownership_rows, active_models, errors)

    condition_columns = (
        "model_id",
        "production_source",
        "condition_function",
        "score_function",
        "score_profile_id",
        "research_baseline_status",
        "operation_contract",
    )
    condition_rows = strict_csv_rows(CONDITION_SPEC, condition_columns, errors)
    condition_ids = {row["model_id"] for row in condition_rows}
    if condition_ids != set(active_models):
        errors.append(
            "daily_model_condition_spec must match active model registry exactly: "
            f"missing={sorted(set(active_models) - condition_ids)}; "
            f"extra={sorted(condition_ids - set(active_models))}"
        )

    shared_by_key: dict[tuple[str, str], dict[str, str]] = {}
    for row in shared_rows:
        key = (row["source_file"], row["semantic_item"])
        if key in shared_by_key:
            errors.append(f"duplicate shared semantic registry row: {key}")
        shared_by_key[key] = row
    if set(shared_by_key) != set(actual_shared):
        errors.append(
            "shared semantic registry must match the AST consumer graph exactly: "
            f"missing={sorted(set(actual_shared) - set(shared_by_key))}; "
            f"extra={sorted(set(shared_by_key) - set(actual_shared))}"
        )
    for key in sorted(set(shared_by_key) & set(actual_shared)):
        row = shared_by_key[key]
        source_file, item = key
        consumers = actual_shared[key]
        if split_list(row["consumer_models"]) != consumers:
            errors.append(
                f"{source_file}::{item}: shared consumer drift; "
                f"expected={split_list(row['consumer_models'])}; actual={consumers}"
            )
        expected_class = expected_shared_semantic_class(item, consumers)
        if row["semantic_class"] != expected_class:
            errors.append(
                f"{source_file}::{item}: semantic_class must be {expected_class}, "
                f"got {row['semantic_class']}"
            )
        if row["semantic_class"] not in VALID_SHARED_SEMANTIC_CLASS:
            errors.append(f"{source_file}::{item}: invalid semantic_class")
        actual_hash = semantics[consumers[0]].items[item]
        if row["canonical_ast_sha256"] != actual_hash:
            errors.append(
                f"{source_file}::{item}: shared semantic SHA drift; "
                f"expected={row['canonical_ast_sha256']}; actual={actual_hash}"
            )
        if not row["change_policy"] or not row["required_validation_commands"]:
            errors.append(f"{source_file}::{item}: missing change policy or validators")

    migrations = {row["migration_id"]: row for row in migration_rows}
    _validate_current_migration_chain(ownership_rows, shared_rows, migration_rows, errors)

    effective_base = base_ref if base_ref is not None else default_base_ref()
    if effective_base:
        base_ownership_text = _load_base_file(effective_base, MODEL_OWNERSHIP)
        base_shared_text = _load_base_file(effective_base, SHARED_SEMANTICS)
        if base_ownership_text is not None and base_shared_text is not None:
            base_errors: list[str] = []
            base_ownership = strict_csv_rows(
                MODEL_OWNERSHIP, MODEL_OWNERSHIP_COLUMNS, base_errors, text=base_ownership_text
            )
            base_shared = strict_csv_rows(
                SHARED_SEMANTICS, SHARED_SEMANTIC_COLUMNS, base_errors, text=base_shared_text
            )
            if base_errors:
                errors.extend(f"base_ref {effective_base}: {error}" for error in base_errors)
            else:
                current_owners = {row["model_id"]: row for row in ownership_rows}
                previous_owners = {row["model_id"]: row for row in base_ownership}
                for model_id, current in current_owners.items():
                    previous = previous_owners.get(model_id)
                    comparable = (
                        "production_source_file",
                        "execution_entry_functions",
                        "semantic_sha256",
                        "ownership_status",
                        "shared_semantic_policy",
                    )
                    if previous is not None and all(previous[key] == current[key] for key in comparable):
                        continue
                    previous_hash = (
                        semantic_record_sha256(f"model:{model_id}", previous)
                        if previous
                        else "NEW"
                    )
                    _validate_semantic_migration(
                        semantic_key=f"model:{model_id}",
                        previous_hash=previous_hash,
                        new_hash=semantic_record_sha256(f"model:{model_id}", current),
                        previous_row=previous,
                        current_row=current,
                        migrations=migrations,
                        affected_models={model_id},
                        errors=errors,
                    )
                    if previous is None:
                        same_source_models = {
                            other_id
                            for other_id, other in current_owners.items()
                            if other_id != model_id
                            and other["production_source_file"] == current["production_source_file"]
                        }
                        if same_source_models and current["ownership_status"] != "approved_shared_module":
                            errors.append(
                                f"new model {model_id} must use a model-owned source module; existing shared "
                                f"source consumers={sorted(same_source_models)}"
                            )

                current_shared = {
                    (row["source_file"], row["semantic_item"]): row for row in shared_rows
                }
                previous_shared = {
                    (row["source_file"], row["semantic_item"]): row for row in base_shared
                }
                for key, current in current_shared.items():
                    previous = previous_shared.get(key)
                    comparable = (
                        "semantic_class",
                        "consumer_models",
                        "canonical_ast_sha256",
                        "change_policy",
                    )
                    if previous is not None and all(previous[field] == current[field] for field in comparable):
                        continue
                    source_file, item = key
                    consumers = set(split_list(current["consumer_models"]))
                    _validate_semantic_migration(
                        semantic_key=f"item:{source_file}::{item}",
                        previous_hash=(
                            semantic_record_sha256(
                                f"item:{source_file}::{item}", previous
                            )
                            if previous
                            else "NEW"
                        ),
                        new_hash=semantic_record_sha256(
                            f"item:{source_file}::{item}", current
                        ),
                        previous_row=previous,
                        current_row=current,
                        migrations=migrations,
                        affected_models=consumers,
                        errors=errors,
                    )
    return errors, semantics


def _producer_paths_exist(producers: str, errors: list[str], family: str) -> None:
    for producer in split_list(producers):
        if not (ROOT / producer).is_file():
            errors.append(f"{family}: registered producer does not exist: {producer}")


def _glob_sample(pattern: str) -> str:
    return pattern.replace("*", "sample").replace("?", "x").replace("[", "").replace("]", "")


def _artifact_rule_matches(artifact_path: str, rule_glob: str) -> bool:
    return fnmatch.fnmatch(_glob_sample(artifact_path), rule_glob)


def _validate_data_migration_chain(
    sharing_rows: list[dict[str, str]],
    migration_rows: list[dict[str, str]],
    errors: list[str],
) -> None:
    if not migration_rows or migration_rows[0]["migration_id"] != BASELINE_DATA_MIGRATION_ID:
        errors.append(f"{BASELINE_DATA_MIGRATION_ID} must be the first data migration row")
        return
    baseline = migration_rows[0]
    if data_migration_row_sha256(baseline) != BASELINE_DATA_MIGRATION_ROW_SHA256:
        errors.append(
            f"immutable data baseline digest drift: expected={BASELINE_DATA_MIGRATION_ROW_SHA256}; "
            f"actual={data_migration_row_sha256(baseline)}"
        )

    migration_by_id: dict[str, dict[str, str]] = {}
    migration_maps: dict[str, dict[str, tuple[str, str]]] = {}
    latest_hash: dict[str, str] = {}
    latest_migration: dict[str, str] = {}
    for index, migration in enumerate(migration_rows):
        migration_id = migration["migration_id"]
        if migration_id in migration_by_id:
            errors.append(f"duplicate data migration id: {migration_id}")
            continue
        migration_by_id[migration_id] = migration
        families = split_list(migration["changed_data_families"])
        previous = split_list(migration["previous_contract_sha256s"])
        new = split_list(migration["new_contract_sha256s"])
        if not (len(families) == len(previous) == len(new)):
            errors.append(f"{migration_id}: data family and SHA lists must align")
            migration_maps[migration_id] = {}
            continue
        if len(set(families)) != len(families):
            errors.append(f"{migration_id}: duplicate changed_data_families entries")
        change_map = {families[pos]: (previous[pos], new[pos]) for pos in range(len(families))}
        migration_maps[migration_id] = change_map
        if index == 0:
            if migration["migration_status"] != "baseline_registered":
                errors.append(f"{migration_id}: invalid baseline status")
            if any(value != "BASELINE" for value in previous):
                errors.append(f"{migration_id}: baseline previous hashes must all be BASELINE")
            for family, (_old, new_hash) in change_map.items():
                latest_hash[family] = new_hash
                latest_migration[family] = migration_id
            continue
        if migration["migration_status"] != VALID_MIGRATION_STATUS:
            errors.append(f"{migration_id}: non-baseline data migration is not validated")
        approval = migration["user_approval_reference"]
        if not approval or approval.startswith(BASELINE_REFERENCE_PREFIX):
            errors.append(f"{migration_id}: non-baseline data migration lacks user approval reference")
        if not migration["validation_commands"]:
            errors.append(f"{migration_id}: non-baseline data migration lacks validators")
        for family, (old_hash, new_hash) in change_map.items():
            expected_old = latest_hash.get(family, "NEW")
            if old_hash != expected_old:
                errors.append(f"{migration_id}: {family} does not continue the data migration chain")
            latest_hash[family] = new_hash
            latest_migration[family] = migration_id

    for row in sharing_rows:
        family = row["data_family_id"]
        migration_id = row["last_migration_id"]
        migration = migration_by_id.get(migration_id)
        if migration is None:
            errors.append(f"{family}: last_migration_id does not resolve: {migration_id}")
            continue
        if latest_migration.get(family) != migration_id:
            errors.append(
                f"{family}: data sharing registry must point to latest migration "
                f"{latest_migration.get(family)}"
            )
        pair = migration_maps.get(migration_id, {}).get(family)
        if pair is None or pair[1] != row["data_contract_sha256"]:
            errors.append(f"{family}: current data contract is not pinned by migration {migration_id}")
        if migration_id == BASELINE_DATA_MIGRATION_ID:
            if row["sharing_decision_reference"] != "baseline_existing_contract_20260712":
                errors.append(f"{family}: baseline data decision reference drift")
            continue
        if row["sharing_decision_reference"] != migration["user_approval_reference"]:
            errors.append(f"{family}: decision reference must match migration {migration_id}")
        consumers = set(split_list(row["approved_consumer_models"]))
        required_consumers = {"all_models"} if "all_models" in consumers else consumers
        if not required_consumers <= set(split_list(migration["affected_models"])):
            errors.append(f"{family}: migration {migration_id} omits affected consumers")


def validate_data_sharing(*, base_ref: str | None = None) -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    background_columns = (
        "data_family_id",
        "scope",
        "owner_lane",
        "producer",
        "artifact_path",
        "source_artifacts",
        "consumer_surfaces",
        "consumer_models",
        "point_in_time_status",
        "allowed_use",
        "forbidden_use",
        "validator",
        "retention_policy",
        "cleanup_status",
        "notes",
    )
    background = strict_csv_rows(BACKGROUND_DATA_REGISTRY, background_columns, errors)
    sharing = strict_csv_rows(DATA_SHARING_REGISTRY, DATA_SHARING_COLUMNS, errors)
    data_migrations = strict_csv_rows(
        DATA_SHARING_MIGRATIONS, DATA_SHARING_MIGRATION_COLUMNS, errors
    )
    research_columns = (
        "owner_model_id",
        "producer",
        "artifact_glob",
        "artifact_class",
        "change_policy",
        "formal_evidence_status",
        "notes",
    )
    research_ownership = strict_csv_rows(
        RESEARCH_ARTIFACT_OWNERSHIP, research_columns, errors
    )
    active_models = _active_stock_models(errors)
    if errors:
        return errors, sharing

    background_by_id = {row["data_family_id"]: row for row in background}
    sharing_by_id: dict[str, dict[str, str]] = {}
    for row in sharing:
        family = row["data_family_id"]
        if family in sharing_by_id:
            errors.append(f"duplicate data sharing registry row: {family}")
        sharing_by_id[family] = row
    if set(background_by_id) != set(sharing_by_id):
        errors.append(
            "data sharing registry must match background data registry exactly: "
            f"missing={sorted(set(background_by_id) - set(sharing_by_id))}; "
            f"extra={sorted(set(sharing_by_id) - set(background_by_id))}"
        )

    active_or_legacy = set(active_models) | {"volume_range_breakout"}
    for family in sorted(set(background_by_id) & set(sharing_by_id)):
        bg = background_by_id[family]
        row = sharing_by_id[family]
        mode = row["ownership_mode"]
        if mode not in VALID_DATA_OWNERSHIP_MODE:
            errors.append(f"{family}: invalid ownership_mode={mode}")
        if mode not in BACKGROUND_SCOPE_TO_OWNERSHIP_MODE.get(bg["scope"], set()):
            errors.append(
                f"{family}: ownership_mode={mode} is inconsistent with scope={bg['scope']}"
            )
        if row["registered_producers"] != bg["producer"]:
            errors.append(f"{family}: registered producer does not match background registry")
        if row["producer_write_scope"] != bg["artifact_path"]:
            errors.append(f"{family}: producer_write_scope does not match artifact_path")
        expected_contract_sha = data_contract_sha256(bg)
        if row["data_contract_sha256"] != expected_contract_sha:
            errors.append(
                f"{family}: data contract SHA drift; expected={row['data_contract_sha256']}; "
                f"actual={expected_contract_sha}"
            )
        if split_list(row["approved_consumer_models"]) != split_list(bg["consumer_models"]):
            errors.append(f"{family}: approved consumers do not match background registry")
        _producer_paths_exist(row["registered_producers"], errors, family)
        if not row["sharing_decision_reference"]:
            errors.append(f"{family}: missing sharing_decision_reference")
        if not row["new_consumer_policy"] or not row["consumer_access_mode"]:
            errors.append(f"{family}: missing access or new-consumer policy")
        consumers = set(split_list(row["approved_consumer_models"]))
        if mode in {"model_owned_not_shared", "model_family_owned_not_shared"}:
            if "all_models" in consumers or not consumers:
                errors.append(f"{family}: model-owned data cannot use all_models or empty consumers")
            unknown = consumers - active_or_legacy
            if unknown:
                errors.append(f"{family}: unknown model consumers: {sorted(unknown)}")
        if mode == "latest_context_not_historical" and "historical" not in bg["forbidden_use"].lower():
            errors.append(f"{family}: latest-only data must explicitly forbid historical use")
        if mode == "legacy_frozen_no_new_consumers" and bg["cleanup_status"] != "deprecated_candidate":
            errors.append(f"{family}: legacy frozen data must be deprecated_candidate")
        if mode in {"model_owned_not_shared", "model_family_owned_not_shared"} and bg["scope"] == "model_research_output":
            owner = row["owner_model_or_family"]
            matching_rules = [
                rule
                for rule in research_ownership
                if rule["owner_model_id"] == owner
                and rule["producer"] == row["registered_producers"]
                and _artifact_rule_matches(row["producer_write_scope"], rule["artifact_glob"])
            ]
            if not matching_rules:
                errors.append(
                    f"{family}: model research write scope is not covered by model_research_artifact_ownership"
                )

    _validate_data_migration_chain(sharing, data_migrations, errors)

    rows = list(sharing_by_id.values())
    for idx, left in enumerate(rows):
        left_prefix = left["producer_write_scope"].split("*", 1)[0]
        for right in rows[idx + 1 :]:
            right_prefix = right["producer_write_scope"].split("*", 1)[0]
            if not left_prefix or not right_prefix:
                continue
            overlap = left_prefix.startswith(right_prefix) or right_prefix.startswith(left_prefix)
            if not overlap:
                continue
            same_owner = (
                left["owner_model_or_family"] == right["owner_model_or_family"]
                and left["registered_producers"] == right["registered_producers"]
            )
            if not same_owner:
                errors.append(
                    "overlapping data write scopes have different owners/producers: "
                    f"{left['data_family_id']}={left['producer_write_scope']} vs "
                    f"{right['data_family_id']}={right['producer_write_scope']}"
                )

    effective_base = base_ref if base_ref is not None else default_base_ref()
    if effective_base:
        base_text = _load_base_file(effective_base, DATA_SHARING_REGISTRY)
        if base_text is not None:
            base_errors: list[str] = []
            base_rows = strict_csv_rows(
                DATA_SHARING_REGISTRY, DATA_SHARING_COLUMNS, base_errors, text=base_text
            )
            errors.extend(f"base_ref {effective_base}: {error}" for error in base_errors)
            previous_by_id = {row["data_family_id"]: row for row in base_rows}
            compared_fields = (
                "ownership_mode",
                "owner_model_or_family",
                "registered_producers",
                "producer_write_scope",
                "consumer_access_mode",
                "approved_consumer_models",
                "data_contract_sha256",
                "formal_evidence_policy",
                "new_consumer_policy",
            )
            for family, current in sharing_by_id.items():
                previous = previous_by_id.get(family)
                changed = previous is None or any(
                    previous[field] != current[field] for field in compared_fields
                )
                if not changed:
                    continue
                reference = current["sharing_decision_reference"]
                if previous is not None and reference == previous["sharing_decision_reference"]:
                    errors.append(f"{family}: data ownership/consumer change lacks a new decision reference")
                if previous is None and reference.startswith(BASELINE_REFERENCE_PREFIX):
                    errors.append(f"{family}: new data family requires an explicit user-approved decision reference")
    return errors, sharing


def _production_imports(
    path: Path, production_modules: dict[str, str]
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=path.as_posix())
    except (SyntaxError, UnicodeError):
        return (), ()
    symbols: set[str] = set()
    sources: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module in production_modules:
            sources.add(production_modules[node.module])
            symbols.update(alias.name for alias in node.names)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in production_modules:
                    sources.add(production_modules[alias.name])
                    symbols.add("*")
    return tuple(sorted(sources)), tuple(sorted(symbols))


def validate_validator_independence() -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    rows = strict_csv_rows(
        VALIDATOR_INDEPENDENCE, VALIDATOR_INDEPENDENCE_COLUMNS, errors
    )
    registered = {row["validator_path"]: row for row in rows}
    if len(registered) != len(rows):
        errors.append("daily_model_validator_independence.csv has duplicate validator_path rows")

    active_models = _active_stock_models(errors)
    production_modules: dict[str, str] = {}
    for contract in active_models.values():
        source = contract["production_source_file"]
        stem = Path(source).stem
        production_modules[stem] = source
        production_modules[f"scripts.{stem}"] = source

    discovered: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {}
    for pattern in ("audit_*.py", "validate_*.py"):
        for path in (ROOT / "scripts").rglob(pattern):
            sources, symbols = _production_imports(path, production_modules)
            if symbols:
                discovered[path.relative_to(ROOT).as_posix()] = (sources, symbols)
    independent_guard = "scripts/validate_model_data_independence.py"
    required_paths = set(discovered) | {independent_guard}
    if set(registered) != required_paths:
        errors.append(
            "validator independence registry must match production-importing audits plus the independent guard: "
            f"missing={sorted(required_paths - set(registered))}; "
            f"extra={sorted(set(registered) - required_paths)}"
        )
    for path, (sources, symbols) in discovered.items():
        row = registered.get(path)
        if row is None:
            continue
        if split_list(row["production_source_file"]) != sources:
            errors.append(f"{path}: imported production source set drift")
        if split_list(row["imported_production_symbols"]) != symbols:
            errors.append(f"{path}: imported production symbols drift")
        if row["independence_claim"].lower() != "false":
            errors.append(f"{path}: a validator importing production business logic cannot claim independence")
        if "independent" in row["allowed_evidence_use"].lower():
            errors.append(f"{path}: implementation consistency audit cannot be cited as independent evidence")
    independent_row = registered.get(independent_guard)
    if independent_row:
        if independent_row["independence_claim"].lower() != "true":
            errors.append(f"{independent_guard}: independent guard must claim independence")
        _guard_sources, guard_symbols = _production_imports(
            ROOT / independent_guard, production_modules
        )
        if guard_symbols:
            errors.append(f"{independent_guard}: independent guard must parse contracts, not import production logic")
    return errors, rows


def validate_formal_evidence_coverage() -> list[str]:
    errors: list[str] = []
    condition_columns = (
        "model_id",
        "production_source",
        "condition_function",
        "score_function",
        "score_profile_id",
        "research_baseline_status",
        "operation_contract",
    )
    condition_rows = strict_csv_rows(CONDITION_SPEC, condition_columns, errors)
    pin_columns = (
        "model_id",
        "approval_version",
        "evidence_path",
        "evidence_format",
        "evidence_version",
        "evidence_version_column",
        "canonical_sha256",
        "owner_lane",
        "pin_status",
        "notes",
    )
    pins = strict_csv_rows(FORMAL_EVIDENCE_PINS, pin_columns, errors)
    operation_models = {
        row["model_id"] for row in condition_rows if row["operation_contract"].lower() not in {"", "none"}
    }
    pinned_models = {row["model_id"] for row in pins if row["pin_status"] == "pinned_formal_evidence"}
    if operation_models != pinned_models:
        errors.append(
            "formal operation models must match evidence pins exactly: "
            f"missing={sorted(operation_models - pinned_models)}; "
            f"extra={sorted(pinned_models - operation_models)}"
        )
    return errors


def comprehensive_validation(*, base_ref: str | None = None) -> tuple[list[str], dict[str, ModelSemantic]]:
    errors, semantics = validate_model_semantic_ownership(base_ref=base_ref)
    data_errors, _ = validate_data_sharing(base_ref=base_ref)
    validator_errors, _ = validate_validator_independence()
    errors.extend(data_errors)
    errors.extend(validator_errors)
    errors.extend(validate_formal_evidence_coverage())
    return errors, semantics
