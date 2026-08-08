from __future__ import annotations

import argparse
import ast
import csv
import fnmatch
import hashlib
import io
import json
import re
import subprocess
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable

from daily_snapshot_revision_utils import select_latest_snapshot_revisions

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = Path("config/daily_model_canonical_field_lineage_registry.csv")
MIGRATIONS_PATH = Path("config/daily_model_canonical_field_lineage_migrations.csv")
CONSUMER_EXCLUSIONS_PATH = Path(
    "config/daily_model_canonical_field_consumer_exclusions.csv"
)
CONSUMER_EXCLUSION_MIGRATIONS_PATH = Path(
    "config/daily_model_canonical_field_consumer_exclusion_migrations.csv"
)
MODEL_SOURCE_PATH = Path("scripts/build_daily_candidate_model_layer.py")
COLLISION_REGISTRY_PATH = Path(
    "config/daily_model_volume_v2_dispatcher_collision_registry.csv"
)
COLLISION_MIGRATIONS_PATH = Path(
    "config/daily_model_volume_v2_dispatcher_collision_migrations.csv"
)
LIVE_SOURCE_REVISION = "working_tree"

REGISTRY_COLUMNS = (
    "lineage_id",
    "field_name",
    "model_family",
    "artifact_path",
    "artifact_role",
    "producer",
    "identity_columns",
    "as_of_columns",
    "canonical_source_artifact",
    "allowed_consumer_modules",
    "allowed_use",
    "forbidden_use",
    "collision_policy",
    "parity_policy",
    "contract_sha256",
    "last_migration_id",
    "approval_reference",
    "required_validation_commands",
    "notes",
)
CONTRACT_HASH_COLUMNS = tuple(
    column for column in REGISTRY_COLUMNS if column != "contract_sha256"
)
MIGRATION_COLUMNS = (
    "migration_id",
    "changed_lineage_ids",
    "previous_contract_sha256s",
    "new_contract_sha256s",
    "affected_models",
    "affected_consumers",
    "validation_commands",
    "user_approval_reference",
    "migration_status",
    "notes",
)

CONSUMER_EXCLUSION_COLUMNS = (
    "exclusion_id",
    "lineage_id",
    "field_name",
    "artifact_path",
    "module",
    "classification",
    "evidence",
    "contract_sha256",
    "last_migration_id",
    "approval_reference",
    "required_validation_commands",
    "notes",
)
CONSUMER_EXCLUSION_HASH_COLUMNS = tuple(
    column
    for column in CONSUMER_EXCLUSION_COLUMNS
    if column != "contract_sha256"
)
CONSUMER_EXCLUSION_MIGRATION_COLUMNS = (
    "migration_id",
    "changed_exclusion_ids",
    "previous_contract_sha256s",
    "new_contract_sha256s",
    "affected_lineage_ids",
    "affected_modules",
    "validation_commands",
    "user_approval_reference",
    "migration_status",
    "notes",
)

COLLISION_REGISTRY_COLUMNS = (
    "collision_id",
    "field_name",
    "model_family",
    "canonical_artifact",
    "canonical_producer",
    "allowed_mirror_artifact",
    "allowed_mirror_producer",
    "dispatcher_consumer",
    "collision_policy",
    "source_precedence",
    "value_parity_policy",
    "contract_sha256",
    "last_migration_id",
    "approval_reference",
    "required_validation_commands",
    "notes",
)
COLLISION_CONTRACT_HASH_COLUMNS = tuple(
    column for column in COLLISION_REGISTRY_COLUMNS if column != "contract_sha256"
)
COLLISION_MIGRATION_COLUMNS = (
    "migration_id",
    "changed_collision_ids",
    "previous_contract_sha256s",
    "new_contract_sha256s",
    "affected_models",
    "affected_consumer",
    "validation_commands",
    "user_approval_reference",
    "migration_status",
    "notes",
)

APPEND_ONLY_MIGRATION_LEDGERS = (
    (
        MIGRATIONS_PATH,
        MIGRATION_COLUMNS,
        "daily canonical field lineage migrations",
    ),
    (
        CONSUMER_EXCLUSION_MIGRATIONS_PATH,
        CONSUMER_EXCLUSION_MIGRATION_COLUMNS,
        "daily canonical field consumer exclusion migrations",
    ),
    (
        COLLISION_MIGRATIONS_PATH,
        COLLISION_MIGRATION_COLUMNS,
        "daily volume-v2 dispatcher collision migrations",
    ),
)

FIELD_NAME = "warrant_flow_signal"
CURRENT_FAMILY = "volume_v2_warrant_current"
HISTORY_FAMILY = "volume_v2_warrant_history"
VALIDATOR_SCOPE = "all_registered_current_lineage_nodes"
VALID_MIGRATION_STATUS = "validated_user_approved_migration"
RETIRED_CONTRACT_SHA = "RETIRED"
CONSUMER_EXCLUSION_MIGRATION_STATUS = "validated_user_approved_migration"
CONSUMER_EXCLUSION_APPROVAL_REFERENCE = (
    "user_requested_formal_lineage_hardening_20260718"
)
SNAPSHOT_REVISION_LINEAGE_APPROVAL_REFERENCE = (
    "user_selected_option_1_daily_snapshot_revision_lineage_20260720"
)
CONSUMER_EXCLUSION_APPROVAL_REFERENCES = frozenset(
    {
        CONSUMER_EXCLUSION_APPROVAL_REFERENCE,
        SNAPSHOT_REVISION_LINEAGE_APPROVAL_REFERENCE,
    }
)
CONSUMER_EXCLUSION_CLASSIFICATIONS = frozenset(
    {
        "cross_artifact_literal",
        "forbidden_field_guard",
        "hash_lineage_proof_only",
        "model_scope_mismatch",
        "no_direct_field_read",
        "routing_metadata_only",
        "schema_or_renderer_guard",
        "unrelated_local_field",
    }
)
VOLUME_V2_MODELS = frozenset(
    {
        "volume_range_breakout_v2_high_position_volume_attack",
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
    }
)
BONUS_MODELS = frozenset(
    {
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
    }
)
BULLISH_WARRANT_SIGNALS = frozenset(
    {"call_inflow", "call_strong_inflow", "call_put_bullish"}
)
OVERLAY_GLOBAL = "VOLUME_V2_WATCH_OVERLAY_FIELDS"
NON_AUTHORITATIVE_GLOBAL = "VOLUME_V2_WATCH_NON_AUTHORITATIVE_COLLISION_FIELDS"
FORMAL_DISPATCH_FORBIDDEN_GLOBAL = "VOLUME_V2_FORMAL_DISPATCH_FORBIDDEN_FIELDS"
CANDIDATE_SCORE_GLOBAL = "VOLUME_V2_CANDIDATE_SCORE_FIELDS"
FORMAL_DISPATCH_FORBIDDEN_FIELDS = frozenset(
    {
        "score",
        "rank",
        "advisory_volume_breakout_score",
        "advisory_volume_breakout_rank",
        "volume_breakout_score",
        "volume_breakout_rank",
    }
)
FORBIDDEN_OVERLAY_FIELDS = frozenset({"call_warrant_count", "put_warrant_count"})
COLLISION_MODEL_FAMILY = "volume_v2_dispatcher_current"
COLLISION_MIGRATION_STATUS = "validated_user_approved_migration"
COLLISION_APPROVAL_REFERENCE = "user_requested_formal_lineage_hardening_20260718"
COLLISION_CANONICAL_CANDIDATE_POLICY = "canonical_candidate_preserved"
COLLISION_WATCH_OVERLAY_POLICY = "watch_overlay_allowlisted"
ALL_CANDIDATES_ARTIFACT = "output/latest/all_candidates_latest.csv"
ALL_CANDIDATES_PRODUCER = "build_all_candidates_latest.py"
FORMAL_SIGNAL_LOG_ARTIFACT = (
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
)
VOLUME_WATCH_ARTIFACT = "output/latest/volume_breakout_watch_latest.csv"
VOLUME_WATCH_PRODUCER = "scripts/build_volume_breakout_watch.py"
VOLUME_TAXONOMY_ARTIFACT = "output/latest/stock_theme_taxonomy_latest.csv"
FORMAL_PRESENTATION_PROJECTION_CONTRACT = "volume_v2_formal_presentation_v1"
VOLUME_DISPATCHER_CONSUMER = "scripts/build_daily_candidate_model_layer.py"
REQUIRED_ALL_CANDIDATE_WARRANT_CONSUMERS = frozenset(
    {
        "scripts/build_daily_theme_leadership_layer.py",
        "scripts/build_non_revenue_momentum_watch.py",
    }
)
THEME_ADVISORY_ARTIFACT = "output/latest/volume_attack_theme_stocks_latest.csv"
THEME_ADVISORY_PRODUCER = "scripts/build_volume_attack_theme_layer.py"
THEME_LINEAGE_COLUMNS = (
    "volume_breakout_score",
    "volume_breakout_rank",
    "volume_watch_as_of",
    "volume_watch_source_artifact",
    "volume_watch_source_sha256",
    "warrant_flow_as_of",
    "warrant_flow_source_artifact",
    "warrant_flow_source_sha256",
    "warrant_flow_official_source_artifact",
    "warrant_flow_official_source_sha256",
)

GOVERNED_ARTIFACTS = {
    "output/latest/warrant_flow_latest.csv": (CURRENT_FAMILY, "canonical", "canonical_only"),
    "output/latest/all_candidates_latest.csv": (
        CURRENT_FAMILY,
        "canonical_projection",
        "registered_projection_only",
    ),
    "output/latest/volume_breakout_watch_latest.csv": (
        CURRENT_FAMILY,
        "forbidden_same_name",
        "column_must_be_absent",
    ),
    "output/latest/daily_candidate_model_signals_latest.csv": (
        CURRENT_FAMILY,
        "formal_projection",
        "registered_projection_only",
    ),
    "output/latest/daily_candidate_model_signals_for_report_latest.csv": (
        CURRENT_FAMILY,
        "formal_projection",
        "registered_projection_only",
    ),
    THEME_ADVISORY_ARTIFACT: (
        CURRENT_FAMILY,
        "advisory_projection",
        "registered_projection_only",
    ),
    "output/history/warrant_flow/warrant_flow_*.csv": (
        HISTORY_FAMILY,
        "canonical",
        "canonical_only",
    ),
    "output/history/daily_model_snapshots/all_candidates_*.csv": (
        HISTORY_FAMILY,
        "historical_projection",
        "registered_projection_only",
    ),
    "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv": (
        HISTORY_FAMILY,
        "historical_projection",
        "registered_projection_only",
    ),
}

SCORE_RANK_GOVERNED_NODES = {
    ("advisory_volume_breakout_score", VOLUME_WATCH_ARTIFACT): (
        "volume_v2_watch_score_rank_current",
        "canonical_advisory_source",
        "canonical_only",
    ),
    ("volume_breakout_score", THEME_ADVISORY_ARTIFACT): (
        "volume_v2_watch_score_rank_current",
        "advisory_projection",
        "registered_projection_only",
    ),
    ("advisory_volume_breakout_rank", VOLUME_WATCH_ARTIFACT): (
        "volume_v2_watch_score_rank_current",
        "canonical_advisory_source",
        "canonical_only",
    ),
    ("volume_breakout_rank", THEME_ADVISORY_ARTIFACT): (
        "volume_v2_watch_score_rank_current",
        "advisory_projection",
        "registered_projection_only",
    ),
    ("score", ALL_CANDIDATES_ARTIFACT): (
        "volume_v2_candidate_score_rank_current",
        "candidate_source_context",
        "formal_dispatch_forbidden",
    ),
    ("score", "output/history/daily_model_snapshots/all_candidates_*.csv"): (
        "volume_v2_candidate_score_rank_history",
        "historical_candidate_source_context",
        "formal_dispatch_forbidden",
    ),
    ("rank", ALL_CANDIDATES_ARTIFACT): (
        "volume_v2_candidate_score_rank_current",
        "candidate_source_context",
        "formal_dispatch_forbidden",
    ),
    ("rank", "output/history/daily_model_snapshots/all_candidates_*.csv"): (
        "volume_v2_candidate_score_rank_history",
        "historical_candidate_source_context",
        "formal_dispatch_forbidden",
    ),
    ("final_rank_score", "output/latest/daily_candidate_model_signals_latest.csv"): (
        "volume_v2_formal_score_rank_current",
        "formal_canonical",
        "canonical_only",
    ),
    (
        "final_rank_score",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    ): (
        "volume_v2_formal_score_rank_current",
        "formal_projection",
        "registered_projection_only",
    ),
    (
        "final_rank_score",
        "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv",
    ): (
        "volume_v2_formal_score_rank_history",
        "historical_formal_projection",
        "immutable_historical_audit_only",
    ),
    (
        "final_rank_score",
        "output/latest/daily_volume_breakout_operation_section_latest.csv",
    ): (
        "volume_v2_formal_operation_current",
        "direct_operation_projection",
        "registered_projection_only",
    ),
    (
        "final_rank_score",
        "output/history/daily_model_snapshots/daily_volume_breakout_operation_section_*.csv",
    ): (
        "volume_v2_formal_operation_history",
        "historical_operation_projection",
        "immutable_historical_audit_only",
    ),
    ("model_score", "output/latest/daily_candidate_model_signals_latest.csv"): (
        "volume_v2_formal_score_rank_current",
        "formal_canonical",
        "canonical_only",
    ),
    (
        "model_score",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    ): (
        "volume_v2_formal_score_rank_current",
        "formal_projection",
        "registered_projection_only",
    ),
    (
        "model_score",
        "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv",
    ): (
        "volume_v2_formal_score_rank_history",
        "historical_formal_projection",
        "immutable_historical_audit_only",
    ),
    ("model_rank", "output/latest/daily_candidate_model_signals_latest.csv"): (
        "volume_v2_formal_score_rank_current",
        "formal_canonical",
        "canonical_only",
    ),
    (
        "model_rank",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    ): (
        "volume_v2_formal_score_rank_current",
        "formal_projection",
        "registered_projection_only",
    ),
    (
        "model_rank",
        "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv",
    ): (
        "volume_v2_formal_score_rank_history",
        "historical_formal_projection",
        "immutable_historical_audit_only",
    ),
}

SOURCE_IDENTITY_FAMILY = "volume_v2_candidate_source_identity_current"
SOURCE_IDENTITY_FIELDS = (
    "candidate_source_raw_stock_id",
    "candidate_source_normalized_stock_id",
    "candidate_source_identity_columns",
    "candidate_source_artifact",
    "candidate_source_producer",
    "candidate_source_artifact_sha256",
    "candidate_source_record_number",
    "candidate_source_row_sha256",
    "candidate_source_row_id",
)
SOURCE_IDENTITY_IN_PLACE_WRITER_MIRRORS = frozenset(
    {
        "merge_warrant_flow_into_candidates.py",
        "scripts/apply_revenue_industry_applicability.py",
        "scripts/apply_fundamental_catalyst_layer.py",
        "scripts/build_candidate_repeat_appearance.py",
        "scripts/build_daily_theme_leadership_layer.py",
    }
)
SOURCE_IDENTITY_EFFECTIVE_FROM = "20260731"
SOURCE_ARTIFACT_ENCODINGS = ("utf-8-sig", "utf-8", "cp950")
SOURCE_IDENTITY_ALIAS_COLUMNS = (
    "stock_id",
    "code",
    "ticker",
    "證券代號",
    "股票代號",
)
ALL_CANDIDATE_SOURCE_ARTIFACTS = frozenset(
    {
        "output/latest/breakout_latest.csv",
        "output/latest/range_rebound_watch_latest.csv",
        "output/latest/revenue_breakout_low_response_latest.csv",
        "output/latest/revenue_pullback_latest.csv",
        "output/latest/pullback_rebound_latest.csv",
        "output/latest/daily_pattern_watch_latest.csv",
    }
)
ALL_CANDIDATE_SOURCE_PRODUCERS = {
    "output/latest/breakout_latest.csv": "stock_daily_monitor.py",
    "output/latest/range_rebound_watch_latest.csv": "stock_daily_monitor.py",
    "output/latest/revenue_breakout_low_response_latest.csv": (
        "scripts/build_revenue_breakout_low_response.py"
    ),
    "output/latest/revenue_pullback_latest.csv": "stock_daily_monitor.py",
    "output/latest/pullback_rebound_latest.csv": "stock_daily_monitor.py",
    "output/latest/daily_pattern_watch_latest.csv": "stock_daily_monitor.py",
}
SOURCE_IDENTITY_GOVERNED_NODES = {
    (field_name, ALL_CANDIDATES_ARTIFACT): (
        SOURCE_IDENTITY_FAMILY,
        "canonical_source_identity_projection",
        "candidate_source_row_id_unique_and_strict_equity_normalization",
    )
    for field_name in SOURCE_IDENTITY_FIELDS
}

FORMAL_RESOLUTION_FIELDS = (
    "candidate_source_row_ids",
    "candidate_source_row_sha256s",
    "candidate_source_categories",
    "candidate_formal_outcome_sha256",
    "candidate_presentation_source_artifact",
    "candidate_presentation_source_artifact_sha256",
    "candidate_presentation_source_row_sha256",
)
FORMAL_RESOLUTION_EFFECTIVE_FROM = SOURCE_IDENTITY_EFFECTIVE_FROM
FORMAL_RESOLUTION_SURFACES = {
    "output/latest/daily_candidate_model_signals_latest.csv": (
        "volume_v2_candidate_resolution_formal_current",
        "formal_resolution_projection",
        "multi_source_outcome_and_presentation_exact_parity",
    ),
    "output/latest/daily_candidate_model_signals_for_report_latest.csv": (
        "volume_v2_candidate_resolution_formal_current",
        "formal_resolution_projection",
        "multi_source_outcome_and_presentation_exact_parity",
    ),
    (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_*.csv"
    ): (
        "volume_v2_candidate_resolution_formal_history",
        "historical_formal_resolution_projection",
        "immutable_historical_audit_only",
    ),
    FORMAL_SIGNAL_LOG_ARTIFACT: (
        "volume_v2_candidate_resolution_lifecycle_history",
        "formal_lifecycle_resolution_history",
        "effective_volume_v2_formal_identity_unique",
    ),
}
FORMAL_RESOLUTION_GOVERNED_NODES = {
    (field_name, artifact_path): spec
    for artifact_path, spec in FORMAL_RESOLUTION_SURFACES.items()
    for field_name in FORMAL_RESOLUTION_FIELDS
}

GOVERNED_FIELD_NODES = {
    **{
        (FIELD_NAME, artifact_path): spec
        for artifact_path, spec in GOVERNED_ARTIFACTS.items()
    },
    **SCORE_RANK_GOVERNED_NODES,
    **SOURCE_IDENTITY_GOVERNED_NODES,
    **FORMAL_RESOLUTION_GOVERNED_NODES,
}


def _text(value: object) -> str:
    text = str(value or "").strip()
    return "" if text.lower() in {"<na>", "nan", "null"} else text


def _split(value: object) -> list[str]:
    return [item.strip() for item in _text(value).split(";") if item.strip()]


def _normalize_stock_id(value: object) -> str:
    text = _text(value)
    return text.zfill(4) if text else ""


def _normalize_signal(value: object) -> str:
    return _text(value).lower()


def _number(value: object) -> Decimal | None:
    try:
        number = Decimal(_text(value))
    except (InvalidOperation, ValueError):
        return None
    return number if number.is_finite() else None


def contract_sha256(row: dict[str, str]) -> str:
    payload = {column: _text(row.get(column)) for column in CONTRACT_HASH_COLUMNS}
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def collision_contract_sha256(row: dict[str, str]) -> str:
    payload = {
        column: _text(row.get(column)) for column in COLLISION_CONTRACT_HASH_COLUMNS
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def consumer_exclusion_contract_sha256(row: dict[str, str]) -> str:
    payload = {
        column: _text(row.get(column))
        for column in CONSUMER_EXCLUSION_HASH_COLUMNS
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _strict_csv_rows(
    path: Path,
    expected_columns: tuple[str, ...],
    errors: list[str],
) -> list[dict[str, str]]:
    if not path.is_file():
        errors.append(f"missing contract file: {path.as_posix()}")
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        actual_columns = tuple(reader.fieldnames or ())
        if actual_columns != expected_columns:
            errors.append(
                f"contract columns mismatch {path.as_posix()}: "
                f"expected={list(expected_columns)} actual={list(actual_columns)}"
            )
            return []
        rows = [
            {column: _text(row.get(column)) for column in expected_columns}
            for row in reader
        ]
    for index, row in enumerate(rows, start=2):
        blank = [column for column in expected_columns if not row[column]]
        if blank:
            errors.append(
                f"blank contract values {path.as_posix()}:{index}: {','.join(blank)}"
            )
    return rows


def _migration_ledger_records(
    payload: bytes,
    *,
    expected_columns: tuple[str, ...],
    source: str,
) -> tuple[list[tuple[bytes, ...]], list[str]]:
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        return [], [f"{source}: migration ledger is not valid UTF-8: {exc}"]
    try:
        parsed = list(csv.reader(io.StringIO(text, newline="")))
    except csv.Error as exc:
        return [], [f"{source}: migration ledger cannot be parsed: {exc}"]
    if not parsed:
        return [], [f"{source}: migration ledger is empty"]
    header = tuple(parsed[0])
    if header != expected_columns:
        return [], [
            f"{source}: migration ledger schema drift: "
            f"expected={expected_columns!r} actual={header!r}"
        ]
    records: list[tuple[bytes, ...]] = []
    errors: list[str] = []
    for line_number, values in enumerate(parsed[1:], start=2):
        if len(values) != len(header):
            errors.append(
                f"{source}: migration ledger row {line_number} field count "
                f"{len(values)} does not match header count {len(header)}"
            )
            continue
        records.append(tuple(value.encode("utf-8") for value in values))
    return records, errors


def _run_git(
    root: Path,
    args: list[str],
    *,
    operation: str,
) -> tuple[subprocess.CompletedProcess[bytes] | None, list[str]]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, [f"cannot {operation}: {exc}"]
    return result, []


def _validate_append_only_base(root: Path, base_ref: str) -> list[str]:
    if not base_ref.strip():
        return ["append-only migration validation base ref is blank"]
    result, errors = _run_git(
        root,
        ["cat-file", "-e", f"{base_ref}^{{commit}}"],
        operation=f"resolve append-only migration validation base {base_ref!r}",
    )
    if errors:
        return errors
    assert result is not None
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        return [
            f"cannot resolve append-only migration validation base {base_ref!r}"
            + (f": {detail}" if detail else "")
        ]
    result, errors = _run_git(
        root,
        ["merge-base", "--is-ancestor", base_ref, "HEAD"],
        operation=(
            f"verify append-only migration validation base {base_ref!r} "
            "is an ancestor of HEAD"
        ),
    )
    if errors:
        return errors
    assert result is not None
    if result.returncode != 0:
        return [
            f"append-only migration validation base {base_ref!r} "
            "is not an ancestor of HEAD"
        ]
    return []


def _validate_migration_ledger_append_only(
    root: Path,
    base_ref: str,
    relative_path: Path,
    expected_columns: tuple[str, ...],
    label: str,
) -> list[str]:
    path = root / relative_path
    if not path.is_file():
        return [f"missing {label}: {relative_path.as_posix()}"]
    current_bytes = path.read_bytes()
    current_records, errors = _migration_ledger_records(
        current_bytes,
        expected_columns=expected_columns,
        source=f"current worktree {relative_path.as_posix()}",
    )
    if errors:
        return errors

    relative = relative_path.as_posix()
    tree_result, git_errors = _run_git(
        root,
        ["ls-tree", "-z", "--full-tree", base_ref, "--", relative],
        operation=f"inspect base migration ledger {base_ref}:{relative}",
    )
    if git_errors:
        return git_errors
    assert tree_result is not None
    if tree_result.returncode != 0:
        detail = tree_result.stderr.decode("utf-8", errors="replace").strip()
        return [
            f"cannot inspect base migration ledger {base_ref}:{relative}"
            + (f": {detail}" if detail else "")
        ]
    if not tree_result.stdout:
        # The base commit is already proven to exist and to be an ancestor of
        # HEAD.  An empty ls-tree result therefore means this ledger was not
        # yet present in that real repository history, not that Git lookup
        # failed.  There are no base rows to preserve in this one case.
        return []

    show_result, git_errors = _run_git(
        root,
        ["show", f"{base_ref}:{relative}"],
        operation=f"read base migration ledger {base_ref}:{relative}",
    )
    if git_errors:
        return git_errors
    assert show_result is not None
    if show_result.returncode != 0:
        detail = show_result.stderr.decode("utf-8", errors="replace").strip()
        return [
            f"cannot read base migration ledger {base_ref}:{relative}"
            + (f": {detail}" if detail else "")
        ]
    base_bytes = show_result.stdout
    base_records, base_errors = _migration_ledger_records(
        base_bytes,
        expected_columns=expected_columns,
        source=f"base_ref {base_ref}:{relative}",
    )
    errors.extend(base_errors)
    if errors:
        return errors

    normalized_base = base_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    normalized_current = current_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if not normalized_current.startswith(normalized_base):
        errors.append(
            f"{relative} is append-only: base CSV bytes are not an exact "
            "current prefix after line-ending normalization"
        )
    if len(current_records) < len(base_records):
        errors.append(
            f"{relative} is append-only: current row count {len(current_records)} "
            f"deleted base rows from {len(base_records)}"
        )
        return errors
    for offset, base_record in enumerate(base_records):
        current_record = current_records[offset]
        if current_record == base_record:
            continue
        base_id = base_record[0].decode("utf-8", errors="replace") if base_record else ""
        current_id = (
            current_record[0].decode("utf-8", errors="replace")
            if current_record
            else ""
        )
        errors.append(
            f"{relative} is append-only: base row {offset + 2} is not an exact "
            f"current row prefix (base migration_id={base_id!r}, "
            f"current migration_id={current_id!r})"
        )
    return errors


def validate_migration_ledgers_append_only(root: Path, base_ref: str) -> list[str]:
    root = root.resolve()
    errors = _validate_append_only_base(root, base_ref)
    if errors:
        return errors
    for relative_path, expected_columns, label in APPEND_ONLY_MIGRATION_LEDGERS:
        errors.extend(
            _validate_migration_ledger_append_only(
                root,
                base_ref,
                relative_path,
                expected_columns,
                label,
            )
        )
    return errors


def _artifact_paths(root: Path, pattern: str) -> list[Path]:
    paths: set[Path] = set()
    if "*" not in pattern and "?" not in pattern and "[" not in pattern:
        path = root / pattern
        if path.is_file():
            paths.add(path)
    else:
        paths.update(path for path in root.glob(pattern) if path.is_file())

    try:
        completed = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError:
        completed = None
    if completed is not None and completed.returncode == 0:
        for raw_path in completed.stdout.decode("utf-8", errors="replace").split("\0"):
            relative = raw_path.strip().replace("\\", "/")
            if relative and fnmatch.fnmatch(relative, pattern):
                paths.add(root / relative)
    return sorted(paths)


def _artifact_payload(path: Path, root: Path | None = None) -> bytes:
    if path.is_file():
        return path.read_bytes()
    if root is None:
        raise FileNotFoundError(path)
    relative = path.relative_to(root).as_posix()
    completed = subprocess.run(
        ["git", "show", f"HEAD:{relative}"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise FileNotFoundError(
            f"tracked artifact is unavailable from working tree and HEAD: "
            f"{relative}: {detail}"
        )
    return completed.stdout


def _canonical_text_sha256(payload: bytes) -> str:
    text = payload.decode("utf-8-sig")
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()


def _read_csv_payload(payload: bytes) -> tuple[list[str], list[dict[str, str]]]:
    handle = io.StringIO(payload.decode("utf-8-sig"), newline="")
    reader = csv.DictReader(handle)
    columns = list(reader.fieldnames or [])
    rows = [
        {column: _text(row.get(column)) for column in columns}
        for row in reader
    ]
    return columns, rows


def _resolve_pinned_canonical_source_revision(
    root: Path,
    artifact_path: str,
    declared_sha256: str,
    *,
    trusted_ref: str = "HEAD",
    allow_live: bool = True,
) -> tuple[bytes, str]:
    """Resolve an exact current or committed source payload by canonical SHA."""

    relative = Path(artifact_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise RuntimeError(
            f"pinned canonical source artifact path is unsafe: {artifact_path}"
        )
    if re.fullmatch(r"[0-9a-f]{64}", declared_sha256) is None:
        raise RuntimeError(
            "pinned canonical source SHA-256 is malformed: "
            f"artifact={artifact_path} sha256={declared_sha256!r}"
        )

    current_path = root / relative
    current_payload: bytes | None = None
    current_sha = "<missing>"
    if current_path.is_file():
        try:
            current_payload = current_path.read_bytes()
            current_sha = _canonical_text_sha256(current_payload)
        except (OSError, UnicodeError):
            current_payload = None
    if allow_live and current_payload is not None and current_sha == declared_sha256:
        head_payload = subprocess.run(
            ["git", "show", f"HEAD:{relative.as_posix()}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        current_is_committed_at_head = False
        if head_payload.returncode == 0:
            try:
                current_is_committed_at_head = (
                    _canonical_text_sha256(head_payload.stdout) == current_sha
                )
            except UnicodeError:
                current_is_committed_at_head = False
        if not current_is_committed_at_head:
            return current_payload, LIVE_SOURCE_REVISION

    completed = subprocess.run(
        [
            "git",
            "log",
            "--format=%H",
            trusted_ref,
            "--",
            relative.as_posix(),
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            "pinned canonical source revision history is unavailable: "
            f"artifact={artifact_path} trusted_ref={trusted_ref} "
            f"detail={detail or '<none>'}"
        )
    commits = [
        value.strip()
        for value in completed.stdout.decode("utf-8", errors="replace").splitlines()
        if value.strip()
    ]
    for commit_sha in commits:
        revision = subprocess.run(
            ["git", "show", f"{commit_sha}:{relative.as_posix()}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if revision.returncode != 0:
            continue
        try:
            revision_sha = _canonical_text_sha256(revision.stdout)
        except UnicodeError:
            continue
        if revision_sha == declared_sha256:
            return revision.stdout, commit_sha
    raise RuntimeError(
        "pinned canonical source revision is not reconstructable: "
        f"artifact={artifact_path} expected_sha256={declared_sha256} "
        f"current_sha256={current_sha} trusted_ref={trusted_ref} "
        f"searched_commits={len(commits)}"
    )


def _committed_artifact_revision(
    root: Path,
    artifact_path: str,
    payload: bytes,
    *,
    trusted_ref: str,
) -> str | None:
    relative = Path(artifact_path)
    committed = subprocess.run(
        ["git", "show", f"HEAD:{relative.as_posix()}"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if committed.returncode != 0:
        return None
    try:
        if _canonical_text_sha256(committed.stdout) != _canonical_text_sha256(payload):
            return None
    except UnicodeError:
        return None
    revision = subprocess.run(
        [
            "git",
            "log",
            "-1",
            "--format=%H",
            "HEAD",
            "--",
            relative.as_posix(),
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        text=True,
    )
    commit_sha = revision.stdout.strip() if revision.returncode == 0 else ""
    if not commit_sha:
        raise RuntimeError(
            "committed theme artifact revision cannot be identified: "
            f"artifact={artifact_path}"
        )
    trusted = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit_sha, trusted_ref],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if trusted.returncode != 0:
        raise RuntimeError(
            "committed theme artifact revision is outside trusted ref ancestry: "
            f"artifact={artifact_path} revision={commit_sha} "
            f"trusted_ref={trusted_ref}"
        )
    return commit_sha


def _source_precedes_consumer(
    root: Path,
    source_revision: str,
    consumer_revision: str,
) -> bool:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_revision, consumer_revision],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return completed.returncode == 0


def _artifact_columns(path: Path, root: Path | None = None) -> list[str]:
    payload = _artifact_payload(path, root)
    handle = io.StringIO(payload.decode("utf-8-sig"), newline="")
    return list(csv.DictReader(handle).fieldnames or [])


def _read_artifact(
    path: Path,
    root: Path | None = None,
) -> tuple[list[str], list[dict[str, str]]]:
    payload = _artifact_payload(path, root)
    return _read_csv_payload(payload)


def _validate_registry(root: Path, rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    by_id: dict[str, dict[str, str]] = {}
    by_node: dict[tuple[str, str], dict[str, str]] = {}
    canonical_by_family: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)

    for row in rows:
        lineage_id = row["lineage_id"]
        artifact_path = row["artifact_path"]
        field_name = row["field_name"]
        node = (field_name, artifact_path)
        if lineage_id in by_id:
            errors.append(f"duplicate canonical field lineage_id: {lineage_id}")
        by_id[lineage_id] = row
        if node in by_node:
            errors.append(
                "duplicate governed field/artifact node: "
                f"field={field_name} artifact={artifact_path}"
            )
        by_node[node] = row

        expected = GOVERNED_FIELD_NODES.get(node)
        if expected is None:
            errors.append(
                "field/artifact is outside registered volume-v2 lineage scope: "
                f"field={field_name} artifact={artifact_path}"
            )
        else:
            expected_family, expected_role, expected_collision = expected
            actual = (row["model_family"], row["artifact_role"], row["collision_policy"])
            if actual != expected:
                errors.append(
                    f"governed field role mismatch {field_name}:{artifact_path}: "
                    f"expected={expected} actual={actual}"
                )
        if (
            artifact_path == VOLUME_WATCH_ARTIFACT
            and field_name
            in {"advisory_volume_breakout_score", "advisory_volume_breakout_rank"}
            and _split(row["as_of_columns"]) != ["advisory_score_as_of"]
        ):
            errors.append(
                "watch advisory lineage must register advisory_score_as_of: "
                f"{lineage_id}"
            )
        if not row["model_family"].startswith("volume_v2_"):
            errors.append(
                f"canonical lineage row exceeds volume-v2 scope: {lineage_id}"
            )

        if row["artifact_role"] in {"canonical", "formal_canonical", "canonical_advisory_source"}:
            canonical_by_family[(row["field_name"], row["model_family"])].append(row)
            if row["canonical_source_artifact"] != artifact_path:
                errors.append(f"canonical row must self-reference source: {lineage_id}")

        actual_hash = contract_sha256(row)
        if row["contract_sha256"] != actual_hash:
            errors.append(
                f"canonical field contract SHA mismatch {lineage_id}: "
                f"expected={row['contract_sha256']} actual={actual_hash}"
            )

        producer = root / row["producer"]
        if not producer.is_file():
            errors.append(f"registered producer does not exist {lineage_id}: {row['producer']}")
        consumers = _split(row["allowed_consumer_modules"])
        if row["model_family"] == SOURCE_IDENTITY_FAMILY:
            missing_source_identity_mirrors = sorted(
                SOURCE_IDENTITY_IN_PLACE_WRITER_MIRRORS - set(consumers)
            )
            if missing_source_identity_mirrors:
                errors.append(
                    "all_candidates source identity lineage omits registered "
                    "in-place writer mirrors: "
                    f"{lineage_id}:" + ",".join(missing_source_identity_mirrors)
                )
        if lineage_id == "warrant_flow_signal__all_candidates_current":
            missing_required_consumers = sorted(
                REQUIRED_ALL_CANDIDATE_WARRANT_CONSUMERS - set(consumers)
            )
            if missing_required_consumers:
                errors.append(
                    "all_candidates warrant lineage omits registered volume-v2 consumers: "
                    + ",".join(missing_required_consumers)
                )
        if row["artifact_role"] == "forbidden_same_name":
            if consumers != ["none"]:
                errors.append(f"forbidden mirror must have no consumers: {lineage_id}")
        else:
            for consumer in consumers:
                if consumer == "none" or not (root / consumer).is_file():
                    errors.append(f"registered consumer does not exist {lineage_id}: {consumer}")

    if set(by_node) != set(GOVERNED_FIELD_NODES):
        errors.append(
            "canonical field registry governed volume-v2 node set mismatch: "
            f"missing={sorted(set(GOVERNED_FIELD_NODES) - set(by_node))} "
            f"extra={sorted(set(by_node) - set(GOVERNED_FIELD_NODES))}"
        )

    for family in (CURRENT_FAMILY, HISTORY_FAMILY):
        canonical = canonical_by_family.get((FIELD_NAME, family), [])
        if len(canonical) != 1:
            errors.append(
                f"field family must have exactly one canonical source: "
                f"field={FIELD_NAME} family={family} count={len(canonical)}"
            )
            continue
        canonical_path = canonical[0]["artifact_path"]
        for row in rows:
            if row["field_name"] != FIELD_NAME:
                continue
            if row["model_family"] != family or row["artifact_role"] == "canonical":
                continue
            if row["canonical_source_artifact"] != canonical_path:
                errors.append(
                    f"projection does not reference family canonical source {row['lineage_id']}: "
                    f"expected={canonical_path} actual={row['canonical_source_artifact']}"
                )
    return errors


def _python_literal_collisions(
    root: Path, rows: list[dict[str, str]], errors: list[str]
) -> set[tuple[str, str]]:
    """Return every current-node module with both field and artifact literals."""

    python_paths = sorted(
        set(root.glob("*.py")).union((root / "scripts").rglob("*.py"))
    )
    module_literals: dict[str, set[str]] = {}
    for path in python_paths:
        relative = path.relative_to(root).as_posix()
        try:
            tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=relative)
        except (OSError, SyntaxError, UnicodeError) as exc:
            errors.append(
                "unable to parse Python module during reverse consumer audit: "
                f"module={relative} error={exc}"
            )
            continue
        module_literals[relative] = {
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        }

    collisions: set[tuple[str, str]] = set()
    current_rows = sorted(
        (row for row in rows if "*" not in row["artifact_path"]),
        key=lambda row: row["lineage_id"],
    )
    for row in current_rows:
        artifact_basename = Path(row["artifact_path"]).name
        for module, literals in module_literals.items():
            if row["field_name"] not in literals:
                continue
            if any(
                artifact_basename in value.replace("\\", "/")
                for value in literals
            ):
                collisions.add((row["lineage_id"], module))
    return collisions


def _validate_consumer_exclusions(
    root: Path,
    registry_rows: list[dict[str, str]],
    exclusion_rows: list[dict[str, str]],
) -> tuple[list[str], set[tuple[str, str]]]:
    errors: list[str] = []
    registry_by_id = {row["lineage_id"]: row for row in registry_rows}
    exclusion_ids: set[str] = set()
    excluded_pairs: set[tuple[str, str]] = set()

    for row in exclusion_rows:
        exclusion_id = row["exclusion_id"]
        lineage_id = row["lineage_id"]
        module = row["module"]
        pair = (lineage_id, module)
        if exclusion_id in exclusion_ids:
            errors.append(f"duplicate canonical consumer exclusion_id: {exclusion_id}")
        exclusion_ids.add(exclusion_id)
        if pair in excluded_pairs:
            errors.append(
                "duplicate canonical consumer exclusion pair: "
                f"lineage_id={lineage_id} module={module}"
            )
        excluded_pairs.add(pair)

        lineage_row = registry_by_id.get(lineage_id)
        if lineage_row is None:
            errors.append(
                f"canonical consumer exclusion references unknown lineage_id: {exclusion_id}"
            )
            continue
        if "*" in lineage_row["artifact_path"]:
            errors.append(
                f"canonical consumer exclusion must reference a current node: {exclusion_id}"
            )
        if row["field_name"] != lineage_row["field_name"]:
            errors.append(
                f"canonical consumer exclusion field mismatch: {exclusion_id}"
            )
        if row["artifact_path"] != lineage_row["artifact_path"]:
            errors.append(
                f"canonical consumer exclusion artifact mismatch: {exclusion_id}"
            )
        if row["classification"] not in CONSUMER_EXCLUSION_CLASSIFICATIONS:
            errors.append(
                "unsupported canonical consumer exclusion classification: "
                f"{exclusion_id}:{row['classification']}"
            )
        if not (root / module).is_file():
            errors.append(
                f"canonical consumer exclusion module does not exist: {exclusion_id}:{module}"
            )
        allowed_modules = set(_split(lineage_row["allowed_consumer_modules"]))
        allowed_modules.add(lineage_row["producer"])
        allowed_modules.discard("none")
        if module in allowed_modules:
            errors.append(
                "canonical consumer exclusion masks a registered consumer: "
                f"{exclusion_id}:{module}"
            )
        if row["approval_reference"] not in CONSUMER_EXCLUSION_APPROVAL_REFERENCES:
            errors.append(
                f"canonical consumer exclusion approval mismatch: {exclusion_id}"
            )
        actual_hash = consumer_exclusion_contract_sha256(row)
        if row["contract_sha256"] != actual_hash:
            errors.append(
                f"canonical consumer exclusion contract SHA mismatch {exclusion_id}: "
                f"expected={row['contract_sha256']} actual={actual_hash}"
            )
    return errors, excluded_pairs


def _validate_reverse_current_consumers(
    root: Path,
    registry_rows: list[dict[str, str]],
    exclusion_rows: list[dict[str, str]],
) -> list[str]:
    """Fail closed for every unregistered current-node literal collision."""

    errors: list[str] = []
    collisions = _python_literal_collisions(root, registry_rows, errors)
    exclusion_errors, excluded_pairs = _validate_consumer_exclusions(
        root, registry_rows, exclusion_rows
    )
    errors.extend(exclusion_errors)

    registry_by_id = {row["lineage_id"]: row for row in registry_rows}
    for lineage_id, module in sorted(collisions):
        row = registry_by_id[lineage_id]
        allowed_modules = set(_split(row["allowed_consumer_modules"]))
        allowed_modules.add(row["producer"])
        allowed_modules.discard("none")
        if module in allowed_modules or (lineage_id, module) in excluded_pairs:
            continue
        errors.append(
            "unregistered current canonical field consumer collision: "
            f"lineage_id={lineage_id} field={row['field_name']} "
            f"artifact={row['artifact_path']} module={module}"
        )

    stale_exclusions = sorted(excluded_pairs - collisions)
    for lineage_id, module in stale_exclusions:
        errors.append(
            "stale canonical consumer exclusion: "
            f"lineage_id={lineage_id} module={module}"
        )
    return errors


def _validate_migrations(
    registry_rows: list[dict[str, str]],
    migration_rows: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    registry_by_id = {row["lineage_id"]: row for row in registry_rows}
    migration_ids: set[str] = set()
    latest_hash: dict[str, str] = {}
    latest_migration: dict[str, str] = {}

    for migration in migration_rows:
        migration_id = migration["migration_id"]
        if migration_id in migration_ids:
            errors.append(f"duplicate canonical field migration_id: {migration_id}")
        migration_ids.add(migration_id)
        if migration["migration_status"] != VALID_MIGRATION_STATUS:
            errors.append(f"canonical field migration is not validated: {migration_id}")

        changed = _split(migration["changed_lineage_ids"])
        previous = _split(migration["previous_contract_sha256s"])
        new = _split(migration["new_contract_sha256s"])
        if not changed or len(changed) != len(previous) or len(changed) != len(new):
            errors.append(f"canonical field migration SHA lists do not align: {migration_id}")
            continue
        if len(changed) != len(set(changed)):
            errors.append(f"canonical field migration repeats lineage ids: {migration_id}")
        for lineage_id, previous_hash, new_hash in zip(changed, previous, new):
            expected_previous = latest_hash.get(lineage_id, "NEW")
            if previous_hash != expected_previous:
                errors.append(
                    f"canonical field migration chain mismatch {migration_id}:{lineage_id}: "
                    f"expected={expected_previous} actual={previous_hash}"
                )
            latest_hash[lineage_id] = new_hash
            latest_migration[lineage_id] = migration_id

    for lineage_id, latest in sorted(latest_hash.items()):
        if lineage_id not in registry_by_id and latest != RETIRED_CONTRACT_SHA:
            errors.append(
                "canonical field migration leaves an unregistered lineage active: "
                f"{lineage_id} tip={latest}"
            )

    for lineage_id, row in registry_by_id.items():
        if latest_migration.get(lineage_id) != row["last_migration_id"]:
            errors.append(
                f"registry does not point to latest field migration {lineage_id}: "
                f"expected={latest_migration.get(lineage_id, '<missing>')} "
                f"actual={row['last_migration_id']}"
            )
        if latest_hash.get(lineage_id) != row["contract_sha256"]:
            errors.append(f"migration tip does not pin current field contract: {lineage_id}")
        migration = next(
            (
                candidate
                for candidate in migration_rows
                if candidate["migration_id"] == row["last_migration_id"]
            ),
            None,
        )
        if migration is not None and migration["user_approval_reference"] != row["approval_reference"]:
            errors.append(f"migration approval does not match registry: {lineage_id}")
        if migration is not None and not VOLUME_V2_MODELS <= set(_split(migration["affected_models"])):
            errors.append(f"migration omits volume v2 consumer models: {migration['migration_id']}")
    return errors


def _validate_consumer_exclusion_migrations(
    exclusion_rows: list[dict[str, str]],
    migration_rows: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    exclusions_by_id = {row["exclusion_id"]: row for row in exclusion_rows}
    migration_ids: set[str] = set()
    latest_hash: dict[str, str] = {}
    latest_migration: dict[str, str] = {}

    for migration in migration_rows:
        migration_id = migration["migration_id"]
        if migration_id in migration_ids:
            errors.append(
                f"duplicate canonical consumer exclusion migration_id: {migration_id}"
            )
        migration_ids.add(migration_id)
        if (
            migration["migration_status"]
            != CONSUMER_EXCLUSION_MIGRATION_STATUS
        ):
            errors.append(
                f"canonical consumer exclusion migration is not validated: {migration_id}"
            )
        if (
            migration["user_approval_reference"]
            not in CONSUMER_EXCLUSION_APPROVAL_REFERENCES
        ):
            errors.append(
                f"canonical consumer exclusion migration approval mismatch: {migration_id}"
            )

        changed = _split(migration["changed_exclusion_ids"])
        previous = _split(migration["previous_contract_sha256s"])
        new = _split(migration["new_contract_sha256s"])
        if not changed or len(changed) != len(previous) or len(changed) != len(new):
            errors.append(
                "canonical consumer exclusion migration SHA lists do not align: "
                f"{migration_id}"
            )
            continue
        if len(changed) != len(set(changed)):
            errors.append(
                "canonical consumer exclusion migration repeats exclusion ids: "
                f"{migration_id}"
            )
        if set(_split(migration["affected_lineage_ids"])) != {
            exclusions_by_id[exclusion_id]["lineage_id"]
            for exclusion_id in changed
            if exclusion_id in exclusions_by_id
        }:
            errors.append(
                "canonical consumer exclusion migration affected lineage set mismatch: "
                f"{migration_id}"
            )
        if set(_split(migration["affected_modules"])) != {
            exclusions_by_id[exclusion_id]["module"]
            for exclusion_id in changed
            if exclusion_id in exclusions_by_id
        }:
            errors.append(
                "canonical consumer exclusion migration affected module set mismatch: "
                f"{migration_id}"
            )
        for exclusion_id, previous_hash, new_hash in zip(changed, previous, new):
            if exclusion_id not in exclusions_by_id:
                errors.append(
                    "canonical consumer exclusion migration references unknown id: "
                    f"{exclusion_id}"
                )
                continue
            expected_previous = latest_hash.get(exclusion_id, "NEW")
            if previous_hash != expected_previous:
                errors.append(
                    "canonical consumer exclusion migration chain mismatch "
                    f"{migration_id}:{exclusion_id}: "
                    f"expected={expected_previous} actual={previous_hash}"
                )
            latest_hash[exclusion_id] = new_hash
            latest_migration[exclusion_id] = migration_id

    for exclusion_id, row in exclusions_by_id.items():
        if latest_migration.get(exclusion_id) != row["last_migration_id"]:
            errors.append(
                "canonical consumer exclusion does not point to latest migration: "
                f"{exclusion_id}"
            )
        if latest_hash.get(exclusion_id) != row["contract_sha256"]:
            errors.append(
                "canonical consumer exclusion migration tip does not pin contract: "
                f"{exclusion_id}"
            )
    return errors


def _literal_string_tuple(node: ast.AST) -> tuple[str, ...] | None:
    if not isinstance(node, ast.Tuple):
        return None
    values: list[str] = []
    for item in node.elts:
        if not isinstance(item, ast.Constant) or not isinstance(item.value, str):
            return None
        values.append(item.value)
    return tuple(values)


def _literal_string_collection(node: ast.AST) -> tuple[str, ...] | None:
    target = node
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "frozenset"
        and len(node.args) == 1
        and not node.keywords
    ):
        target = node.args[0]
    if not isinstance(target, (ast.Tuple, ast.List, ast.Set)):
        return None
    values: list[str] = []
    for item in target.elts:
        if not isinstance(item, ast.Constant) or not isinstance(item.value, str):
            return None
        values.append(item.value)
    return tuple(values)


def _dispatcher_collision_field_sets(
    root: Path,
) -> tuple[set[str], set[str], list[str]]:
    errors: list[str] = []
    source_path = root / MODEL_SOURCE_PATH
    if not source_path.is_file():
        return set(), set(), [
            f"missing model dispatcher source: {MODEL_SOURCE_PATH.as_posix()}"
        ]
    try:
        tree = ast.parse(
            source_path.read_text(encoding="utf-8-sig"), filename=str(source_path)
        )
    except (OSError, SyntaxError) as exc:
        return set(), set(), [f"unable to parse model dispatcher source: {exc}"]

    collections: dict[str, tuple[str, ...] | None] = {
        OVERLAY_GLOBAL: None,
        NON_AUTHORITATIVE_GLOBAL: None,
    }
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for target in targets:
            if not isinstance(target, ast.Name) or target.id not in collections:
                continue
            collections[target.id] = _literal_string_collection(node.value)

    for name, values in collections.items():
        if values is None:
            errors.append(f"{name} must be a literal string collection")
            continue
        if not values:
            errors.append(f"{name} must not be empty")
        if len(values) != len(set(values)):
            errors.append(f"{name} contains duplicate fields")

    overlay = set(collections[OVERLAY_GLOBAL] or ())
    non_authoritative = set(collections[NON_AUTHORITATIVE_GLOBAL] or ())
    duplicated = sorted(overlay.intersection(non_authoritative))
    if duplicated:
        errors.append(
            "volume-v2 dispatcher fields cannot have two collision policies: "
            f"{','.join(duplicated)}"
        )
    return overlay, non_authoritative, errors


def _validate_collision_registry(
    root: Path,
    rows: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    overlay, non_authoritative, ast_errors = _dispatcher_collision_field_sets(root)
    errors.extend(ast_errors)

    candidate_path = root / ALL_CANDIDATES_ARTIFACT
    watch_path = root / VOLUME_WATCH_ARTIFACT
    if not candidate_path.is_file():
        errors.append(f"missing dispatcher canonical artifact: {ALL_CANDIDATES_ARTIFACT}")
    if not watch_path.is_file():
        errors.append(f"missing dispatcher mirror artifact: {VOLUME_WATCH_ARTIFACT}")
    if not candidate_path.is_file() or not watch_path.is_file():
        return errors

    actual_collisions = set(_artifact_columns(candidate_path)).intersection(
        _artifact_columns(watch_path)
    )
    registered_fields: set[str] = set()
    collision_ids: set[str] = set()

    for row in rows:
        collision_id = row["collision_id"]
        field_name = row["field_name"]
        if collision_id in collision_ids:
            errors.append(f"duplicate volume-v2 dispatcher collision_id: {collision_id}")
        collision_ids.add(collision_id)
        if field_name in registered_fields:
            errors.append(
                f"duplicate volume-v2 dispatcher collision field: {field_name}"
            )
        registered_fields.add(field_name)

        if row["model_family"] != COLLISION_MODEL_FAMILY:
            errors.append(f"dispatcher collision model_family mismatch: {collision_id}")
        if row["approval_reference"] != COLLISION_APPROVAL_REFERENCE:
            errors.append(f"dispatcher collision approval mismatch: {collision_id}")
        if row["dispatcher_consumer"] != VOLUME_DISPATCHER_CONSUMER:
            errors.append(f"dispatcher collision consumer mismatch: {collision_id}")

        policy = row["collision_policy"]
        if policy == COLLISION_WATCH_OVERLAY_POLICY:
            expected = {
                "canonical_artifact": VOLUME_WATCH_ARTIFACT,
                "canonical_producer": VOLUME_WATCH_PRODUCER,
                "allowed_mirror_artifact": ALL_CANDIDATES_ARTIFACT,
                "allowed_mirror_producer": ALL_CANDIDATES_PRODUCER,
                "source_precedence": "watch_overlays_candidate",
                "value_parity_policy": "no_value_parity_watch_recomputes_price_volume",
            }
            if field_name not in overlay:
                errors.append(
                    f"watch-overlay collision is absent from {OVERLAY_GLOBAL}: {field_name}"
                )
            if field_name in non_authoritative:
                errors.append(
                    f"watch-overlay collision is also non-authoritative: {field_name}"
                )
        elif policy == COLLISION_CANONICAL_CANDIDATE_POLICY:
            expected = {
                "canonical_artifact": ALL_CANDIDATES_ARTIFACT,
                "canonical_producer": ALL_CANDIDATES_PRODUCER,
                "allowed_mirror_artifact": VOLUME_WATCH_ARTIFACT,
                "allowed_mirror_producer": VOLUME_WATCH_PRODUCER,
                "source_precedence": "candidate_preserved_watch_ignored",
                "value_parity_policy": "no_value_parity_watch_mirror_is_advisory",
            }
            if field_name not in non_authoritative:
                errors.append(
                    "candidate-preserved collision is absent from "
                    f"{NON_AUTHORITATIVE_GLOBAL}: {field_name}"
                )
            if field_name in overlay:
                errors.append(
                    f"candidate-preserved collision is also a watch overlay: {field_name}"
                )
        else:
            errors.append(
                f"unsupported volume-v2 dispatcher collision policy {collision_id}: {policy}"
            )
            expected = {}

        for column, expected_value in expected.items():
            if row[column] != expected_value:
                errors.append(
                    f"dispatcher collision lineage mismatch {collision_id}:{column}: "
                    f"expected={expected_value} actual={row[column]}"
                )

        for module_column in (
            "canonical_producer",
            "allowed_mirror_producer",
            "dispatcher_consumer",
        ):
            if not (root / row[module_column]).is_file():
                errors.append(
                    f"dispatcher collision module does not exist "
                    f"{collision_id}:{row[module_column]}"
                )

        actual_hash = collision_contract_sha256(row)
        if row["contract_sha256"] != actual_hash:
            errors.append(
                f"dispatcher collision contract SHA mismatch {collision_id}: "
                f"expected={row['contract_sha256']} actual={actual_hash}"
            )

    missing = sorted(actual_collisions - registered_fields)
    extra = sorted(registered_fields - actual_collisions)
    if missing:
        errors.append(
            "unregistered volume-v2 dispatcher same-name collision: "
            f"{','.join(missing)}"
        )
    if extra:
        errors.append(
            "volume-v2 dispatcher collision registry contains non-colliding fields: "
            f"{','.join(extra)}"
        )

    ast_registered = overlay.union(non_authoritative)
    ast_missing = sorted(actual_collisions - ast_registered)
    if ast_missing:
        errors.append(
            "volume-v2 dispatcher AST allowlists omit actual collisions: "
            f"{','.join(ast_missing)}"
        )
    for field_name in sorted(actual_collisions.intersection(registered_fields)):
        policy_count = int(field_name in overlay) + int(field_name in non_authoritative)
        if policy_count != 1:
            errors.append(
                "volume-v2 dispatcher collision must map to exactly one AST policy: "
                f"{field_name} count={policy_count}"
            )
    return errors


def _validate_collision_migrations(
    registry_rows: list[dict[str, str]],
    migration_rows: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    registry_by_id = {row["collision_id"]: row for row in registry_rows}
    seen_migrations: set[str] = set()
    latest_hash: dict[str, str] = {}
    latest_migration: dict[str, str] = {}

    for migration in migration_rows:
        migration_id = migration["migration_id"]
        if migration_id in seen_migrations:
            errors.append(f"duplicate dispatcher collision migration_id: {migration_id}")
        seen_migrations.add(migration_id)
        if migration["migration_status"] != COLLISION_MIGRATION_STATUS:
            errors.append(f"dispatcher collision migration is not validated: {migration_id}")
        if migration["user_approval_reference"] != COLLISION_APPROVAL_REFERENCE:
            errors.append(f"dispatcher collision migration approval mismatch: {migration_id}")
        if migration["affected_consumer"] != VOLUME_DISPATCHER_CONSUMER:
            errors.append(f"dispatcher collision migration consumer mismatch: {migration_id}")
        if not VOLUME_V2_MODELS <= set(_split(migration["affected_models"])):
            errors.append(f"dispatcher collision migration omits volume v2 models: {migration_id}")

        changed = _split(migration["changed_collision_ids"])
        previous = _split(migration["previous_contract_sha256s"])
        new = _split(migration["new_contract_sha256s"])
        if not changed or len(changed) != len(previous) or len(changed) != len(new):
            errors.append(f"dispatcher collision migration SHA lists do not align: {migration_id}")
            continue
        if len(changed) != len(set(changed)):
            errors.append(f"dispatcher collision migration repeats collision ids: {migration_id}")
        for collision_id, previous_hash, new_hash in zip(changed, previous, new):
            if collision_id not in registry_by_id:
                errors.append(
                    f"dispatcher collision migration references unknown id: {collision_id}"
                )
                continue
            expected_previous = latest_hash.get(collision_id, "NEW")
            if previous_hash != expected_previous:
                errors.append(
                    f"dispatcher collision migration chain mismatch {migration_id}:"
                    f"{collision_id}: expected={expected_previous} actual={previous_hash}"
                )
            latest_hash[collision_id] = new_hash
            latest_migration[collision_id] = migration_id

    for collision_id, row in registry_by_id.items():
        if latest_migration.get(collision_id) != row["last_migration_id"]:
            errors.append(
                f"dispatcher registry does not point to latest migration {collision_id}: "
                f"expected={latest_migration.get(collision_id, '<missing>')} "
                f"actual={row['last_migration_id']}"
            )
        if latest_hash.get(collision_id) != row["contract_sha256"]:
            errors.append(
                f"dispatcher collision migration tip does not pin current contract: {collision_id}"
            )
    return errors


def _subscript_key(node: ast.Subscript) -> str:
    key = node.slice
    if isinstance(key, ast.Constant) and isinstance(key.value, str):
        return key.value
    return ""


def _is_forbidden_overlay_field(field: str) -> bool:
    return field.startswith("warrant_") or field in FORBIDDEN_OVERLAY_FIELDS


def _dict_comp_uses_global(node: ast.AST, global_name: str) -> bool:
    return isinstance(node, ast.DictComp) and any(
        isinstance(generator.iter, ast.Name) and generator.iter.id == global_name
        for generator in node.generators
    )


def _subscript_root_name(node: ast.AST) -> str:
    current = node
    while isinstance(current, ast.Subscript):
        current = current.value
    return current.id if isinstance(current, ast.Name) else ""


def _validate_score_source_mutations(
    dispatcher: ast.FunctionDef | ast.AsyncFunctionDef,
) -> list[str]:
    """Prove that score_source has only the four approved write operations."""

    errors: list[str] = []
    parent_by_id: dict[int, ast.AST] = {}
    for parent in ast.walk(dispatcher):
        for child in ast.iter_child_nodes(parent):
            parent_by_id[id(child)] = parent

    candidate_initializations: list[int] = []
    watch_updates: list[int] = []
    warrant_assignments: list[int] = []
    derived_feature_updates: list[int] = []

    for node in ast.walk(dispatcher):
        if isinstance(node, ast.Assign):
            score_targets = [
                target
                for target in node.targets
                if isinstance(target, ast.Name) and target.id == "score_source"
            ]
            if score_targets:
                if _dict_comp_uses_global(node.value, CANDIDATE_SCORE_GLOBAL):
                    candidate_initializations.append(node.lineno)
                else:
                    errors.append(
                        "append_volume_breakout_signals has an unregistered score_source "
                        f"assignment at line {node.lineno}"
                    )
            for target in node.targets:
                if not isinstance(target, ast.Subscript):
                    continue
                if _subscript_root_name(target) != "score_source":
                    continue
                if (
                    isinstance(target.value, ast.Name)
                    and target.value.id == "score_source"
                    and _subscript_key(target) == FIELD_NAME
                    and isinstance(node.value, ast.Name)
                    and node.value.id == "authoritative_warrant_signal"
                ):
                    warrant_assignments.append(node.lineno)
                else:
                    errors.append(
                        "append_volume_breakout_signals has an unregistered score_source "
                        f"subscript write at line {node.lineno}"
                    )
        if isinstance(node, ast.AnnAssign):
            target = node.target
            if (
                isinstance(target, ast.Name) and target.id == "score_source"
            ) or (
                isinstance(target, ast.Subscript)
                and _subscript_root_name(target) == "score_source"
            ):
                errors.append(
                    "append_volume_breakout_signals has an unregistered annotated "
                    f"score_source write at line {node.lineno}"
                )
        if isinstance(node, ast.AugAssign):
            target = node.target
            if (
                isinstance(target, ast.Name) and target.id == "score_source"
            ) or (
                isinstance(target, ast.Subscript)
                and _subscript_root_name(target) == "score_source"
            ):
                errors.append(
                    "append_volume_breakout_signals must not use augmented score_source "
                    f"mutation at line {node.lineno}"
                )
        if isinstance(node, (ast.Delete, ast.NamedExpr)):
            targets = node.targets if isinstance(node, ast.Delete) else [node.target]
            if any(
                (isinstance(target, ast.Name) and target.id == "score_source")
                or (
                    isinstance(target, ast.Subscript)
                    and _subscript_root_name(target) == "score_source"
                )
                for target in targets
            ):
                errors.append(
                    "append_volume_breakout_signals has an unregistered score_source "
                    f"mutation at line {node.lineno}"
                )
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if not isinstance(node.func.value, ast.Name) or node.func.value.id != "score_source":
            continue
        if node.func.attr != "update":
            if node.func.attr in {
                "clear",
                "pop",
                "popitem",
                "setdefault",
                "__ior__",
                "__setitem__",
            }:
                errors.append(
                    "append_volume_breakout_signals uses an unregistered score_source "
                    f"mutator {node.func.attr} at line {node.lineno}"
                )
            continue
        if len(node.args) != 1 or node.keywords:
            errors.append(
                "append_volume_breakout_signals has a non-canonical score_source.update "
                f"signature at line {node.lineno}"
            )
            continue
        argument = node.args[0]
        if _dict_comp_uses_global(argument, OVERLAY_GLOBAL):
            watch_updates.append(node.lineno)
        elif isinstance(argument, ast.Name) and argument.id == "v2_features":
            derived_feature_updates.append(node.lineno)
        else:
            errors.append(
                "append_volume_breakout_signals has an unregistered score_source.update "
                f"source at line {node.lineno}"
            )

    for node in ast.walk(dispatcher):
        if not isinstance(node, ast.Name) or node.id != "score_source":
            continue
        if not isinstance(node.ctx, ast.Load):
            continue
        parent = parent_by_id.get(id(node))
        allowed_load = False
        if isinstance(parent, ast.Attribute) and parent.value is node:
            allowed_load = True
        elif isinstance(parent, ast.Subscript) and parent.value is node:
            allowed_load = True
        elif isinstance(parent, ast.Call) and node in parent.args:
            allowed_load = (
                isinstance(parent.func, ast.Name) and parent.func.id == "set"
            ) or (
                isinstance(parent.func, ast.Attribute)
                and isinstance(parent.func.value, ast.Name)
                and parent.func.value.id == "pd"
                and parent.func.attr == "Series"
            )
        if not allowed_load:
            errors.append(
                "append_volume_breakout_signals exposes score_source through an "
                f"unregistered load context at line {node.lineno}"
            )

    expected_counts = {
        "candidate allowlist initialization": candidate_initializations,
        "watch allowlist update": watch_updates,
        "authoritative warrant assignment": warrant_assignments,
        "derived volume-v2 feature update": derived_feature_updates,
    }
    for label, lines in expected_counts.items():
        if len(lines) != 1:
            errors.append(
                "append_volume_breakout_signals must contain exactly one approved "
                f"{label}; found={len(lines)} lines={lines}"
            )
    if all(len(lines) == 1 for lines in expected_counts.values()):
        ordered = [
            candidate_initializations[0],
            watch_updates[0],
            warrant_assignments[0],
            derived_feature_updates[0],
        ]
        if ordered != sorted(ordered):
            errors.append(
                "append_volume_breakout_signals score_source write order must be "
                "candidate_allowlist,watch_allowlist,authoritative_warrant,v2_features"
            )
    return errors


def _validate_dispatcher_ast(root: Path) -> list[str]:
    errors: list[str] = []
    source_path = root / MODEL_SOURCE_PATH
    if not source_path.is_file():
        return [f"missing model dispatcher source: {MODEL_SOURCE_PATH.as_posix()}"]
    try:
        tree = ast.parse(source_path.read_text(encoding="utf-8-sig"), filename=str(source_path))
    except (OSError, SyntaxError) as exc:
        return [f"unable to parse model dispatcher source: {exc}"]

    overlay_fields: tuple[str, ...] | None = None
    non_authoritative_fields: tuple[str, ...] | None = None
    formal_dispatch_forbidden_fields: tuple[str, ...] | None = None
    candidate_score_fields: tuple[str, ...] | None = None
    dispatcher: ast.FunctionDef | ast.AsyncFunctionDef | None = None
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == OVERLAY_GLOBAL for target in targets):
                overlay_fields = _literal_string_tuple(node.value)
            if any(
                isinstance(target, ast.Name)
                and target.id == NON_AUTHORITATIVE_GLOBAL
                for target in targets
            ):
                non_authoritative_fields = _literal_string_collection(node.value)
            if any(
                isinstance(target, ast.Name)
                and target.id == FORMAL_DISPATCH_FORBIDDEN_GLOBAL
                for target in targets
            ):
                formal_dispatch_forbidden_fields = _literal_string_collection(node.value)
            if any(
                isinstance(target, ast.Name) and target.id == CANDIDATE_SCORE_GLOBAL
                for target in targets
            ):
                candidate_score_fields = _literal_string_tuple(node.value)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "append_volume_breakout_signals":
            dispatcher = node

    if overlay_fields is None:
        errors.append(f"{OVERLAY_GLOBAL} must be a literal tuple")
    else:
        if not overlay_fields:
            errors.append(f"{OVERLAY_GLOBAL} must not be empty")
        if len(overlay_fields) != len(set(overlay_fields)):
            errors.append(f"{OVERLAY_GLOBAL} contains duplicate fields")
        forbidden = sorted(field for field in overlay_fields if _is_forbidden_overlay_field(field))
        if forbidden:
            errors.append(
                f"{OVERLAY_GLOBAL} contains forbidden warrant fields: {','.join(forbidden)}"
            )
    if non_authoritative_fields is None:
        errors.append(f"{NON_AUTHORITATIVE_GLOBAL} must be a literal string collection")
    else:
        if not non_authoritative_fields:
            errors.append(f"{NON_AUTHORITATIVE_GLOBAL} must not be empty")
        if len(non_authoritative_fields) != len(set(non_authoritative_fields)):
            errors.append(f"{NON_AUTHORITATIVE_GLOBAL} contains duplicate fields")
        if FIELD_NAME not in non_authoritative_fields:
            errors.append(
                f"{NON_AUTHORITATIVE_GLOBAL} must retain forbidden watch field {FIELD_NAME}"
            )
    if overlay_fields is not None and non_authoritative_fields is not None:
        duplicated = sorted(set(overlay_fields).intersection(non_authoritative_fields))
        if duplicated:
            errors.append(
                "dispatcher fields cannot be registered in both collision globals: "
                f"{','.join(duplicated)}"
            )
    if formal_dispatch_forbidden_fields is None:
        errors.append(
            f"{FORMAL_DISPATCH_FORBIDDEN_GLOBAL} must be a literal string collection"
        )
    elif set(formal_dispatch_forbidden_fields) != set(FORMAL_DISPATCH_FORBIDDEN_FIELDS):
        errors.append(
            f"{FORMAL_DISPATCH_FORBIDDEN_GLOBAL} must equal the registered volume-v2 "
            "score/rank forbidden set: "
            f"expected={sorted(FORMAL_DISPATCH_FORBIDDEN_FIELDS)} "
            f"actual={sorted(formal_dispatch_forbidden_fields)}"
        )
    if overlay_fields is not None:
        forbidden_score_rank_overlay = sorted(
            set(overlay_fields).intersection(FORMAL_DISPATCH_FORBIDDEN_FIELDS)
        )
        if forbidden_score_rank_overlay:
            errors.append(
                f"{OVERLAY_GLOBAL} contains formal-dispatch forbidden score/rank fields: "
                + ",".join(forbidden_score_rank_overlay)
            )
    if candidate_score_fields is None:
        errors.append(f"{CANDIDATE_SCORE_GLOBAL} must be a literal tuple")
    else:
        if not candidate_score_fields:
            errors.append(f"{CANDIDATE_SCORE_GLOBAL} must not be empty")
        if len(candidate_score_fields) != len(set(candidate_score_fields)):
            errors.append(f"{CANDIDATE_SCORE_GLOBAL} contains duplicate fields")
        forbidden_candidate_score_fields = sorted(
            set(candidate_score_fields).intersection(FORMAL_DISPATCH_FORBIDDEN_FIELDS)
        )
        if forbidden_candidate_score_fields:
            errors.append(
                f"{CANDIDATE_SCORE_GLOBAL} contains formal-dispatch forbidden fields: "
                + ",".join(forbidden_candidate_score_fields)
            )

    if dispatcher is None:
        errors.append("missing append_volume_breakout_signals dispatcher")
        return errors

    errors.extend(_validate_score_source_mutations(dispatcher))

    has_registered_watch_dict_comprehension = False
    has_registered_candidate_dict_comprehension = False
    has_non_authoritative_collision_guard = False
    has_formal_dispatch_forbidden_guard = False
    has_authoritative_score_assignment = False
    has_authoritative_output_projection = False
    for node in ast.walk(dispatcher):
        if isinstance(node, ast.Name) and node.id == NON_AUTHORITATIVE_GLOBAL:
            has_non_authoritative_collision_guard = True
        if isinstance(node, ast.Name) and node.id == FORMAL_DISPATCH_FORBIDDEN_GLOBAL:
            has_formal_dispatch_forbidden_guard = True
        if isinstance(node, ast.DictComp):
            for generator in node.generators:
                if isinstance(generator.iter, ast.Name) and generator.iter.id == OVERLAY_GLOBAL:
                    has_registered_watch_dict_comprehension = True
                if (
                    isinstance(generator.iter, ast.Name)
                    and generator.iter.id == CANDIDATE_SCORE_GLOBAL
                ):
                    has_registered_candidate_dict_comprehension = True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == "score_source"
                and node.func.attr == "update"
            ):
                for argument in node.args:
                    if (
                        isinstance(argument, ast.Call)
                        and isinstance(argument.func, ast.Attribute)
                        and isinstance(argument.func.value, ast.Name)
                        and argument.func.value.id == "row"
                        and argument.func.attr == "to_dict"
                    ):
                        errors.append(
                            "append_volume_breakout_signals must not apply row.to_dict() through score_source.update"
                        )
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name):
            if node.value.id != "authoritative_warrant_signal":
                continue
            for target in node.targets:
                if (
                    isinstance(target, ast.Subscript)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == "score_source"
                    and _subscript_key(target) == FIELD_NAME
                ):
                    has_authoritative_score_assignment = True
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == "score_source"
                for target in node.targets
            ) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute):
                if node.value.func.attr == "to_dict":
                    errors.append(
                        "append_volume_breakout_signals must not initialize score_source "
                        "from an unfiltered to_dict() payload"
                    )
        if isinstance(node, ast.Dict):
            for key, value in zip(node.keys, node.values):
                if (
                    isinstance(key, ast.Constant)
                    and key.value == FIELD_NAME
                    and isinstance(value, ast.Name)
                    and value.id == "authoritative_warrant_signal"
                ):
                    has_authoritative_output_projection = True

    if not has_registered_watch_dict_comprehension:
        errors.append(
            f"append_volume_breakout_signals must overlay watch fields with a dict comprehension over {OVERLAY_GLOBAL}"
        )
    if not has_registered_candidate_dict_comprehension:
        errors.append(
            "append_volume_breakout_signals must select candidate scoring fields with a "
            f"dict comprehension over {CANDIDATE_SCORE_GLOBAL}"
        )
    if not has_non_authoritative_collision_guard:
        errors.append(
            "append_volume_breakout_signals must include "
            f"{NON_AUTHORITATIVE_GLOBAL} in its collision guard"
        )
    if not has_formal_dispatch_forbidden_guard:
        errors.append(
            "append_volume_breakout_signals must enforce "
            f"{FORMAL_DISPATCH_FORBIDDEN_GLOBAL}"
        )
    if not has_authoritative_score_assignment:
        errors.append("score_source warrant_flow_signal must come from authoritative_warrant_signal")
    if not has_authoritative_output_projection:
        errors.append("formal warrant_flow_signal output must come from authoritative_warrant_signal")
    return errors


def _validate_artifact_headers(root: Path, rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    artifact_paths_cache: dict[str, list[Path]] = {}
    artifact_columns_cache: dict[Path, list[str]] = {}
    artifact_rows_cache: dict[Path, list[dict[str, str]]] = {}
    registered_nodes = {
        (row["field_name"], row["artifact_path"]): row for row in rows
    }
    for (field_name, pattern), (family, _role, _collision) in GOVERNED_FIELD_NODES.items():
        registry_row = registered_nodes.get((field_name, pattern))
        if pattern not in artifact_paths_cache:
            artifact_paths_cache[pattern] = _artifact_paths(root, pattern)
        for path in artifact_paths_cache[pattern]:
            relative = path.relative_to(root).as_posix()
            try:
                if path not in artifact_columns_cache:
                    artifact_columns_cache[path] = _artifact_columns(path, root)
                columns = artifact_columns_cache[path]
            except (FileNotFoundError, OSError, UnicodeError) as exc:
                errors.append(f"unable to read governed artifact header: {relative}: {exc}")
                continue
            effective_from = ""
            if family == SOURCE_IDENTITY_FAMILY:
                effective_from = SOURCE_IDENTITY_EFFECTIVE_FROM
            elif family in {
                "volume_v2_candidate_resolution_formal_current",
                "volume_v2_candidate_resolution_formal_history",
                "volume_v2_candidate_resolution_lifecycle_history",
            }:
                effective_from = FORMAL_RESOLUTION_EFFECTIVE_FROM
            if effective_from and field_name not in columns:
                try:
                    if path not in artifact_rows_cache:
                        _, artifact_rows_cache[path] = _read_artifact(path, root)
                    artifact_rows = artifact_rows_cache[path]
                except (FileNotFoundError, OSError, UnicodeError):
                    artifact_rows = []
                artifact_dates = sorted(
                    {
                        re.sub(
                            r"[^0-9]",
                            "",
                            _text(row.get("signal_date") or row.get("date")),
                        )[:8]
                        for row in artifact_rows
                        if len(
                            re.sub(
                                r"[^0-9]",
                                "",
                                _text(row.get("signal_date") or row.get("date")),
                            )
                        )
                        >= 8
                    }
                )
                if (
                    artifact_dates
                    and artifact_dates[-1] < effective_from
                ):
                    continue
            if registry_row is None and field_name in columns:
                errors.append(
                    f"unregistered same-name field collision: {relative}:{field_name}"
                )
                continue
            if registry_row is None:
                continue
            collision_policy = registry_row["collision_policy"]
            required_lineage_columns = set(_split(registry_row["identity_columns"])) | set(
                _split(registry_row["as_of_columns"])
            )
            missing_lineage_columns = sorted(required_lineage_columns - set(columns))
            if missing_lineage_columns:
                errors.append(
                    "registered lineage identity/as-of columns are missing: "
                    f"{relative}:{field_name} missing={missing_lineage_columns}"
                )
            if collision_policy == "column_must_be_absent":
                if field_name in columns:
                    errors.append(
                        f"forbidden same-name field collision: {relative}:{field_name}"
                    )
            elif field_name not in columns:
                if collision_policy == "immutable_historical_audit_only":
                    try:
                        if path not in artifact_rows_cache:
                            _, artifact_rows_cache[path] = _read_artifact(path, root)
                        historical_rows = artifact_rows_cache[path]
                    except (FileNotFoundError, OSError, UnicodeError):
                        historical_rows = []
                    if not any(
                        _text(row.get("model_id")) in VOLUME_V2_MODELS
                        for row in historical_rows
                    ):
                        # Old immutable snapshots that predate volume-v2 rows are
                        # retained as-is; this scoped hardening does not backfill them.
                        continue
                errors.append(
                    f"registered canonical field is missing: {relative}:{field_name} family={family}"
                )
    return errors


def _validate_all_candidates_source_identity(root: Path) -> list[str]:
    path = root / ALL_CANDIDATES_ARTIFACT
    if not path.is_file():
        return []
    errors: list[str] = []
    try:
        columns, rows = _read_artifact(path, root)
    except (FileNotFoundError, OSError, UnicodeError) as exc:
        return [f"unable to read all_candidates source identity: {exc}"]
    required = {"stock_id", *SOURCE_IDENTITY_FIELDS}
    missing = sorted(required - set(columns))
    if missing:
        artifact_dates = sorted(
            {
                re.sub(r"[^0-9]", "", _text(row.get("signal_date") or row.get("date")))[:8]
                for row in rows
                if len(
                    re.sub(
                        r"[^0-9]",
                        "",
                        _text(row.get("signal_date") or row.get("date")),
                    )
                )
                >= 8
            }
        )
        if artifact_dates and artifact_dates[-1] < SOURCE_IDENTITY_EFFECTIVE_FROM:
            return []
        return [f"all_candidates source identity columns are missing: {missing}"]

    seen_source_row_ids: set[str] = set()
    source_cache: dict[str, tuple[str, list[str], list[list[str]]]] = {}

    def normalize_source_identity(value: object) -> str:
        normalized = _text(value)
        normalized = re.sub(r"\.0$", "", normalized)
        normalized = re.sub(r"[^0-9A-Za-z]", "", normalized)
        return normalized.zfill(4) if normalized.isdigit() else normalized

    def load_source_artifact(
        source_artifact: str,
    ) -> tuple[str, list[str], list[list[str]]] | None:
        if source_artifact in source_cache:
            return source_cache[source_artifact]
        source_path = root / source_artifact
        if not source_path.is_file():
            errors.append(
                "all_candidates source artifact is missing: "
                f"source_artifact={source_artifact!r}"
            )
            return None
        try:
            source_bytes = source_path.read_bytes()
        except OSError as exc:
            errors.append(
                "all_candidates source artifact is unreadable: "
                f"source_artifact={source_artifact!r} error={exc}"
            )
            return None
        source_records: list[list[str]] | None = None
        decode_errors: list[str] = []
        for encoding in SOURCE_ARTIFACT_ENCODINGS:
            try:
                source_text = source_bytes.decode(encoding)
            except UnicodeError as exc:
                decode_errors.append(f"{encoding}:{type(exc).__name__}")
                continue
            try:
                parsed_source_records = list(
                    csv.reader(io.StringIO(source_text, newline=""), strict=True)
                )
            except csv.Error as exc:
                errors.append(
                    "all_candidates source artifact CSV parse failed: "
                    f"source_artifact={source_artifact!r} "
                    f"encoding={encoding} error={exc}"
                )
                return None
            source_records = [
                record
                for record in parsed_source_records
                if record and not (len(record) == 1 and not record[0].strip())
            ]
            break
        if source_records is None:
            errors.append(
                "all_candidates source artifact cannot be decoded with bounded "
                "encodings: "
                f"source_artifact={source_artifact!r} "
                f"encodings={list(SOURCE_ARTIFACT_ENCODINGS)} "
                f"errors={decode_errors}"
            )
            return None
        if not source_records:
            errors.append(
                "all_candidates source artifact is empty: "
                f"source_artifact={source_artifact!r}"
            )
            return None
        header = source_records[0]
        payload = (
            hashlib.sha256(source_bytes).hexdigest(),
            header,
            source_records[1:],
        )
        source_cache[source_artifact] = payload
        return payload

    for row_number, row in enumerate(rows, start=2):
        stock_id = _text(row.get("stock_id"))
        raw_stock_id = _text(row.get("candidate_source_raw_stock_id"))
        normalized_stock_id = _text(
            row.get("candidate_source_normalized_stock_id")
        )
        identity_columns = _text(row.get("candidate_source_identity_columns"))
        source_artifact = _text(row.get("candidate_source_artifact"))
        source_producer = _text(row.get("candidate_source_producer"))
        source_artifact_sha256 = _text(
            row.get("candidate_source_artifact_sha256")
        )
        source_record_number = _text(
            row.get("candidate_source_record_number")
        )
        source_row_sha256 = _text(row.get("candidate_source_row_sha256"))
        source_row_id = _text(row.get("candidate_source_row_id"))
        if not all(
            (
                stock_id,
                raw_stock_id,
                normalized_stock_id,
                identity_columns,
                source_artifact,
                source_producer,
                source_artifact_sha256,
                source_record_number,
                source_row_sha256,
                source_row_id,
            )
        ):
            errors.append(
                f"all_candidates source identity is incomplete: row={row_number}"
            )
            continue
        if not re.fullmatch(r"[0-9]{4}", normalized_stock_id):
            errors.append(
                "all_candidates normalized identity is not a four-digit equity code: "
                f"row={row_number} normalized_stock_id={normalized_stock_id!r}"
            )
        if stock_id != normalized_stock_id:
            errors.append(
                "all_candidates normalized identity parity mismatch: "
                f"row={row_number} stock_id={stock_id!r} "
                f"normalized_stock_id={normalized_stock_id!r}"
            )
        if normalize_source_identity(raw_stock_id) != normalized_stock_id:
            errors.append(
                "all_candidates raw-to-normalized identity parity mismatch: "
                f"row={row_number} raw_stock_id={raw_stock_id!r} "
                f"normalized_stock_id={normalized_stock_id!r}"
            )
        if source_artifact not in ALL_CANDIDATE_SOURCE_ARTIFACTS:
            errors.append(
                "all_candidates source artifact is not registered: "
                f"row={row_number} source_artifact={source_artifact!r}"
            )
        expected_producer = ALL_CANDIDATE_SOURCE_PRODUCERS.get(source_artifact)
        if expected_producer and source_producer != expected_producer:
            errors.append(
                "all_candidates source producer parity mismatch: "
                f"row={row_number} expected={expected_producer!r} "
                f"actual={source_producer!r}"
            )
        if not re.fullmatch(r"[0-9a-f]{64}", source_artifact_sha256):
            errors.append(
                "all_candidates source artifact SHA-256 is invalid: "
                f"row={row_number} sha256={source_artifact_sha256!r}"
            )
        if not re.fullmatch(r"[0-9a-f]{64}", source_row_sha256):
            errors.append(
                "all_candidates source row SHA-256 is invalid: "
                f"row={row_number} sha256={source_row_sha256!r}"
            )
        if not source_record_number.isdigit() or int(source_record_number) < 2:
            errors.append(
                "all_candidates source record number is invalid: "
                f"row={row_number} record_number={source_record_number!r}"
            )
        expected_source_row_id = (
            f"{source_artifact}@{source_artifact_sha256}#"
            f"{source_record_number}:{normalized_stock_id}:{source_row_sha256}"
        )
        if source_row_id != expected_source_row_id:
            errors.append(
                "all_candidates source row id parity mismatch: "
                f"row={row_number} expected={expected_source_row_id!r} "
                f"actual={source_row_id!r}"
            )
        if source_row_id in seen_source_row_ids:
            errors.append(
                "all_candidates source row id is duplicated: "
                f"row={row_number} source_row_id={source_row_id!r}"
            )
        seen_source_row_ids.add(source_row_id)
        source_payload = load_source_artifact(source_artifact)
        if source_payload is None or not source_record_number.isdigit():
            continue
        actual_artifact_sha256, source_header, source_records = source_payload
        if actual_artifact_sha256 != source_artifact_sha256:
            errors.append(
                "all_candidates source artifact SHA-256 mismatch: "
                f"row={row_number} source_artifact={source_artifact!r} "
                f"expected={source_artifact_sha256} actual={actual_artifact_sha256}"
            )
        source_record_index = int(source_record_number) - 2
        if not 0 <= source_record_index < len(source_records):
            errors.append(
                "all_candidates source record is out of range: "
                f"row={row_number} source_artifact={source_artifact!r} "
                f"record_number={source_record_number}"
            )
            continue
        source_values = source_records[source_record_index]
        if len(source_values) != len(source_header):
            errors.append(
                "all_candidates source record field count mismatch: "
                f"row={row_number} source_artifact={source_artifact!r}"
            )
            continue
        identity_column_names = [
            item.strip() for item in identity_columns.split(";") if item.strip()
        ]
        if not identity_column_names or len(identity_column_names) != len(
            set(identity_column_names)
        ):
            errors.append(
                "all_candidates source identity column list is invalid: "
                f"row={row_number} identity_columns={identity_columns!r}"
            )
        source_record = dict(zip(source_header, source_values))
        missing_identity_columns = sorted(
            set(identity_column_names) - set(source_header)
        )
        if missing_identity_columns:
            errors.append(
                "all_candidates source identity columns are absent from raw source: "
                f"row={row_number} missing={missing_identity_columns}"
            )
        derived_identity_aliases = [
            (column, _text(source_record.get(column)))
            for column in SOURCE_IDENTITY_ALIAS_COLUMNS
            if column in source_header and _text(source_record.get(column))
        ]
        derived_identity_columns = [
            column for column, _value in derived_identity_aliases
        ]
        if identity_column_names != derived_identity_columns:
            errors.append(
                "all_candidates source identity alias declaration mismatch: "
                f"row={row_number} declared={identity_column_names} "
                f"derived={derived_identity_columns}"
            )
        if not derived_identity_aliases:
            errors.append(
                "all_candidates raw source identity alias is blank: "
                f"row={row_number}"
            )
        elif raw_stock_id != derived_identity_aliases[0][1]:
            errors.append(
                "all_candidates raw stock identity is not the first source alias: "
                f"row={row_number} expected={derived_identity_aliases[0][1]!r} "
                f"actual={raw_stock_id!r}"
            )
        for column, value in derived_identity_aliases:
            if normalize_source_identity(value) != normalized_stock_id:
                errors.append(
                    "all_candidates raw source alias normalization mismatch: "
                    f"row={row_number} column={column} value={value!r} "
                    f"normalized_stock_id={normalized_stock_id!r}"
                )
        canonical_row_payload = [
            [column, _text(value)]
            for column, value in zip(source_header, source_values)
        ]
        actual_row_sha256 = hashlib.sha256(
            json.dumps(
                canonical_row_payload,
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        if actual_row_sha256 != source_row_sha256:
            errors.append(
                "all_candidates source row SHA-256 mismatch: "
                f"row={row_number} source_artifact={source_artifact!r} "
                f"record_number={source_record_number} "
                f"expected={source_row_sha256} actual={actual_row_sha256}"
            )
    return errors


def _validate_formal_source_crosswalk(
    candidate_rows: Iterable[dict[str, str]],
    formal_rows: Iterable[dict[str, str]],
    label: str,
) -> list[str]:
    """Require every formal source tuple to resolve to the exact candidate row.

    The formal arrays are ordered projections.  Merely embedding a row hash in
    a syntactically valid ID is not lineage: the referenced row must exist in
    the paired all_candidates artifact, belong to the same stock, and carry
    the exact hash and category at the same array position.
    """

    errors: list[str] = []
    candidate_rows = list(candidate_rows)
    formal_rows = list(formal_rows)
    has_effective_formal_rows = any(
        _text(row.get("model_id")) in VOLUME_V2_MODELS
        and re.sub(
            r"[^0-9]",
            "",
            _text(row.get("signal_date") or row.get("date")),
        )[:8]
        >= FORMAL_RESOLUTION_EFFECTIVE_FROM
        for row in formal_rows
    )
    candidates_by_id: dict[str, dict[str, str]] = {}
    candidate_ids_by_stock: dict[str, list[str]] = defaultdict(list)
    for row_number, row in enumerate(candidate_rows, start=2):
        source_row_id = _text(row.get("candidate_source_row_id"))
        if not source_row_id:
            if has_effective_formal_rows:
                errors.append(
                    "formal source crosswalk candidate row is missing source identity: "
                    f"label={label} row={row_number} "
                    f"stock_id={_normalize_stock_id(row.get('stock_id'))!r}"
                )
            continue
        stock_id = _normalize_stock_id(
            row.get("candidate_source_normalized_stock_id")
            or row.get("stock_id")
        )
        if source_row_id in candidates_by_id:
            errors.append(
                "formal source crosswalk candidate ID is ambiguous: "
                f"label={label} row={row_number} source_row_id={source_row_id!r}"
            )
            continue
        candidates_by_id[source_row_id] = row
        candidate_ids_by_stock[stock_id].append(source_row_id)

    for stock_id in candidate_ids_by_stock:
        candidate_ids_by_stock[stock_id].sort()

    for row_number, row in enumerate(formal_rows, start=2):
        model_id = _text(row.get("model_id"))
        signal_date = re.sub(
            r"[^0-9]",
            "",
            _text(row.get("signal_date") or row.get("date")),
        )[:8]
        if (
            model_id not in VOLUME_V2_MODELS
            or signal_date < FORMAL_RESOLUTION_EFFECTIVE_FROM
        ):
            continue
        stock_id = _normalize_stock_id(row.get("stock_id"))
        source_ids_text = _text(row.get("candidate_source_row_ids"))
        source_hashes_text = _text(row.get("candidate_source_row_sha256s"))
        source_categories_text = _text(row.get("candidate_source_categories"))
        source_ids = source_ids_text.split("|") if source_ids_text else []
        source_hashes = source_hashes_text.split("|") if source_hashes_text else []
        source_categories = (
            source_categories_text.split("|") if source_categories_text else []
        )
        expected_source_ids = candidate_ids_by_stock.get(stock_id, [])
        if source_ids != expected_source_ids:
            errors.append(
                "formal source crosswalk membership/order mismatch: "
                f"label={label} row={row_number} stock_id={stock_id} "
                f"expected={expected_source_ids} actual={source_ids}"
            )

        for position, (source_id, source_sha, source_category) in enumerate(
            zip(source_ids, source_hashes, source_categories),
            start=1,
        ):
            candidate = candidates_by_id.get(source_id)
            if candidate is None:
                errors.append(
                    "formal source crosswalk references an unknown candidate row: "
                    f"label={label} row={row_number} position={position} "
                    f"source_row_id={source_id!r}"
                )
                continue
            candidate_stock_id = _normalize_stock_id(
                candidate.get("candidate_source_normalized_stock_id")
                or candidate.get("stock_id")
            )
            if candidate_stock_id != stock_id:
                errors.append(
                    "formal source crosswalk stock mismatch: "
                    f"label={label} row={row_number} position={position} "
                    f"formal_stock_id={stock_id!r} "
                    f"candidate_stock_id={candidate_stock_id!r}"
                )
            candidate_sha = _text(candidate.get("candidate_source_row_sha256"))
            if source_sha != candidate_sha:
                errors.append(
                    "formal source crosswalk row SHA-256 mismatch: "
                    f"label={label} row={row_number} position={position} "
                    f"source_row_id={source_id!r} expected={candidate_sha!r} "
                    f"actual={source_sha!r}"
                )
            candidate_category = _text(
                candidate.get("original_category") or candidate.get("category")
            ) or "<blank>"
            if source_category != candidate_category:
                errors.append(
                    "formal source crosswalk category mismatch: "
                    f"label={label} row={row_number} position={position} "
                    f"source_row_id={source_id!r} expected={candidate_category!r} "
                    f"actual={source_category!r}"
                )
    return errors


def _canonical_payload_sha256(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _formal_outcome_envelope(row: dict[str, str]) -> dict[str, str]:
    has_candidate_sources = bool(_text(row.get("candidate_source_row_ids")))
    return {
        "model_id": _text(row.get("model_id")),
        "candidate_signal_date": (
            _text(row.get("signal_date") or row.get("date"))
            if has_candidate_sources
            else ""
        ),
        "authoritative_warrant_signal": _text(row.get("warrant_flow_signal")),
        "base_model_score": _text(row.get("base_model_score")),
        "operation_score": _text(row.get("operation_score")),
        "tdcc_score": _text(row.get("tdcc_score")),
        "pattern_score": _text(row.get("pattern_score")),
        "risk_penalty": _text(row.get("risk_penalty")),
        "final_rank_score": _text(row.get("final_rank_score")),
        "rank_reason_zh": _text(row.get("rank_reason_zh")),
        "model_score": _text(row.get("model_score")),
        "score_components": _text(row.get("score_components")),
        "risk_penalty_tags": _text(row.get("risk_penalty_tags")),
        "tdcc_status": _text(row.get("tdcc_status")),
        "next_confirmation": _text(row.get("next_confirmation")),
    }


def _formal_presentation_envelope(row: dict[str, str]) -> dict[str, str]:
    return {
        "stock_name": _text(row.get("stock_name")),
        "industry": _text(row.get("industry")),
        "primary_theme": _text(row.get("primary_theme")),
        "secondary_themes": _text(row.get("secondary_themes")),
        "effective_structural_theme_bucket": _text(
            row.get("effective_structural_theme_bucket")
        ),
        "effective_mainstream_label": _text(
            row.get("effective_mainstream_label")
        ),
        "report_line_memberships": _text(row.get("report_line_memberships")),
        "mainstream_report_eligible": _text(
            row.get("mainstream_report_eligible")
        ),
        "non_mainstream_report_eligible": _text(
            row.get("non_mainstream_report_eligible")
        ),
        "dual_report_membership_flag": _text(
            row.get("dual_report_membership_flag")
        ),
        "report_bucket": _text(row.get("report_line") or row.get("report_bucket")),
    }


def _ordered_row_sha256(columns: Iterable[str], row: dict[str, str]) -> str:
    return hashlib.sha256(
        json.dumps(
            [[_text(column), _text(row.get(column))] for column in columns],
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _validate_current_presentation_descriptor_sources(
    root: Path,
    row: dict[str, str],
    descriptor: dict[str, object],
    label: str,
    row_number: int,
) -> list[str]:
    errors: list[str] = []
    stock_id = _normalize_stock_id(row.get("stock_id"))

    watch = descriptor.get("watch")
    if isinstance(watch, dict):
        artifact = _text(watch.get("artifact"))
        if artifact != VOLUME_WATCH_ARTIFACT:
            errors.append(
                "formal presentation watch artifact is not canonical: "
                f"artifact={label} row={row_number} value={artifact!r}"
            )
        else:
            path = root / artifact
            try:
                payload = _artifact_payload(path, root)
                actual_artifact_sha = _canonical_text_sha256(payload)
                columns, rows = _read_artifact(path, root)
            except (FileNotFoundError, OSError, UnicodeError) as exc:
                errors.append(
                    "unable to read formal presentation watch source: "
                    f"artifact={label} row={row_number} error={exc}"
                )
            else:
                expected_artifact_sha = _text(watch.get("artifact_sha256"))
                if actual_artifact_sha != expected_artifact_sha:
                    errors.append(
                        "formal presentation watch artifact SHA-256 mismatch: "
                        f"artifact={label} row={row_number} "
                        f"expected={expected_artifact_sha!r} "
                        f"actual={actual_artifact_sha!r}"
                    )
                record_number = watch.get("record_number")
                if not isinstance(record_number, int) or record_number < 2:
                    errors.append(
                        "formal presentation watch record number is invalid: "
                        f"artifact={label} row={row_number} "
                        f"value={record_number!r}"
                    )
                else:
                    source_index = record_number - 2
                    if not 0 <= source_index < len(rows):
                        errors.append(
                            "formal presentation watch record is out of range: "
                            f"artifact={label} row={row_number} "
                            f"record_number={record_number}"
                        )
                    else:
                        watch_row = rows[source_index]
                        watch_stock_id = _normalize_stock_id(watch_row.get("stock_id"))
                        if watch_stock_id != stock_id:
                            errors.append(
                                "formal presentation watch stock mismatch: "
                                f"artifact={label} row={row_number} "
                                f"formal_stock_id={stock_id!r} "
                                f"watch_stock_id={watch_stock_id!r}"
                            )
                        actual_row_sha = _ordered_row_sha256(columns, watch_row)
                        expected_row_sha = _text(watch.get("row_sha256"))
                        if actual_row_sha != expected_row_sha:
                            errors.append(
                                "formal presentation watch row SHA-256 mismatch: "
                                f"artifact={label} row={row_number} "
                                f"expected={expected_row_sha!r} "
                                f"actual={actual_row_sha!r}"
                            )

    taxonomy = descriptor.get("taxonomy")
    if isinstance(taxonomy, dict):
        artifact = _text(taxonomy.get("artifact"))
        if artifact != VOLUME_TAXONOMY_ARTIFACT:
            errors.append(
                "formal presentation taxonomy artifact is not canonical: "
                f"artifact={label} row={row_number} value={artifact!r}"
            )
        else:
            path = root / artifact
            try:
                payload = _artifact_payload(path, root)
                actual_artifact_sha = _canonical_text_sha256(payload)
                columns, rows = _read_artifact(path, root)
            except (FileNotFoundError, OSError, UnicodeError) as exc:
                errors.append(
                    "unable to read formal presentation taxonomy source: "
                    f"artifact={label} row={row_number} error={exc}"
                )
            else:
                expected_artifact_sha = _text(taxonomy.get("artifact_sha256"))
                if actual_artifact_sha != expected_artifact_sha:
                    errors.append(
                        "formal presentation taxonomy artifact SHA-256 mismatch: "
                        f"artifact={label} row={row_number} "
                        f"expected={expected_artifact_sha!r} "
                        f"actual={actual_artifact_sha!r}"
                    )
                matches = [
                    source_row
                    for source_row in rows
                    if _normalize_stock_id(source_row.get("stock_id")) == stock_id
                ]
                if len(matches) != 1:
                    errors.append(
                        "formal presentation taxonomy stock row is not unique: "
                        f"artifact={label} row={row_number} stock_id={stock_id} "
                        f"matches={len(matches)}"
                    )
                else:
                    actual_row_sha = _ordered_row_sha256(columns, matches[0])
                    expected_row_sha = _text(taxonomy.get("row_sha256"))
                    if actual_row_sha != expected_row_sha:
                        errors.append(
                            "formal presentation taxonomy row SHA-256 mismatch: "
                            f"artifact={label} row={row_number} "
                            f"expected={expected_row_sha!r} "
                            f"actual={actual_row_sha!r}"
                        )
    return errors


def _validate_formal_projection_hashes(
    row: dict[str, str],
    label: str,
    row_number: int,
    *,
    root: Path | None = None,
    validate_current_sources: bool = False,
) -> list[str]:
    errors: list[str] = []
    source_ids_text = _text(row.get("candidate_source_row_ids"))
    source_hashes_text = _text(row.get("candidate_source_row_sha256s"))
    source_categories_text = _text(row.get("candidate_source_categories"))
    source_ids = source_ids_text.split("|") if source_ids_text else []
    source_hashes = source_hashes_text.split("|") if source_hashes_text else []
    source_categories = (
        source_categories_text.split("|") if source_categories_text else []
    )
    if source_ids != sorted(source_ids) or len(source_ids) != len(
        set(source_ids)
    ):
        errors.append(
            "formal resolution source row IDs are not sorted unique: "
            f"artifact={label} row={row_number}"
        )
    if not (
        len(source_ids) == len(source_hashes) == len(source_categories)
    ):
        errors.append(
            "formal resolution source lineage arrays are not paired: "
            f"artifact={label} row={row_number} "
            f"ids={len(source_ids)} hashes={len(source_hashes)} "
            f"categories={len(source_categories)}"
        )
    for position, source_id in enumerate(source_ids, start=1):
        source_sha = (
            source_hashes[position - 1]
            if position <= len(source_hashes)
            else ""
        )
        match = re.search(r":([0-9a-f]{64})$", source_id)
        if not match or match.group(1) != source_sha:
            errors.append(
                "formal resolution source row ID/hash pairing mismatch: "
                f"artifact={label} row={row_number} position={position} "
                f"source_id={source_id!r} source_sha={source_sha!r}"
            )

    outcome_sha = _text(row.get("candidate_formal_outcome_sha256"))
    descriptor_text = _text(row.get("candidate_presentation_source_artifact"))
    descriptor_sha = _text(
        row.get("candidate_presentation_source_artifact_sha256")
    )
    presentation_row_sha = _text(
        row.get("candidate_presentation_source_row_sha256")
    )
    for field_name, field_value in (
        ("candidate_formal_outcome_sha256", outcome_sha),
        ("candidate_presentation_source_artifact_sha256", descriptor_sha),
        ("candidate_presentation_source_row_sha256", presentation_row_sha),
    ):
        if not re.fullmatch(r"[0-9a-f]{64}", field_value):
            errors.append(
                f"formal resolution SHA-256 is invalid: artifact={label} "
                f"row={row_number} field={field_name} value={field_value!r}"
            )

    expected_outcome_sha = _canonical_payload_sha256(
        _formal_outcome_envelope(row)
    )
    if outcome_sha != expected_outcome_sha:
        errors.append(
            "formal outcome SHA-256 does not match the independent row projection: "
            f"artifact={label} row={row_number} "
            f"expected={expected_outcome_sha} actual={outcome_sha}"
        )
    expected_presentation_row_sha = _canonical_payload_sha256(
        _formal_presentation_envelope(row)
    )
    if presentation_row_sha != expected_presentation_row_sha:
        errors.append(
            "formal presentation row SHA-256 does not match the independent row "
            f"projection: artifact={label} row={row_number} "
            f"expected={expected_presentation_row_sha} "
            f"actual={presentation_row_sha}"
        )

    if not descriptor_text:
        errors.append(
            f"formal resolution presentation source is blank: artifact={label} "
            f"row={row_number}"
        )
        return errors
    actual_descriptor_sha = hashlib.sha256(
        descriptor_text.encode("utf-8")
    ).hexdigest()
    if descriptor_sha != actual_descriptor_sha:
        errors.append(
            "formal presentation descriptor SHA-256 mismatch: "
            f"artifact={label} row={row_number} "
            f"expected={actual_descriptor_sha} actual={descriptor_sha}"
        )
    try:
        descriptor = json.loads(descriptor_text)
    except (TypeError, ValueError) as exc:
        errors.append(
            "formal presentation descriptor is not valid JSON: "
            f"artifact={label} row={row_number} error={exc}"
        )
        return errors
    if not isinstance(descriptor, dict):
        errors.append(
            "formal presentation descriptor must be a JSON object: "
            f"artifact={label} row={row_number}"
        )
        return errors
    canonical_descriptor_text = json.dumps(
        descriptor,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    if descriptor_text != canonical_descriptor_text:
        errors.append(
            "formal presentation descriptor is not canonical JSON: "
            f"artifact={label} row={row_number}"
        )
    expected_keys = {
        "contract",
        "mode",
        "candidate_source_row_ids",
        "candidate_source_row_sha256s",
        "candidate_source_categories",
        "watch",
        "taxonomy",
        "presentation_row_sha256",
    }
    if set(descriptor) != expected_keys:
        errors.append(
            "formal presentation descriptor schema mismatch: "
            f"artifact={label} row={row_number} "
            f"missing={sorted(expected_keys - set(descriptor))} "
            f"extra={sorted(set(descriptor) - expected_keys)}"
        )
    if descriptor.get("contract") != FORMAL_PRESENTATION_PROJECTION_CONTRACT:
        errors.append(
            "formal presentation descriptor contract mismatch: "
            f"artifact={label} row={row_number} "
            f"value={descriptor.get('contract')!r}"
        )
    if descriptor.get("mode") not in {"all_candidates", "taxonomy"}:
        errors.append(
            "formal presentation descriptor mode is invalid: "
            f"artifact={label} row={row_number} value={descriptor.get('mode')!r}"
        )
    expected_arrays = {
        "candidate_source_row_ids": (
            _text(row.get("candidate_source_row_ids")).split("|")
            if _text(row.get("candidate_source_row_ids"))
            else []
        ),
        "candidate_source_row_sha256s": (
            _text(row.get("candidate_source_row_sha256s")).split("|")
            if _text(row.get("candidate_source_row_sha256s"))
            else []
        ),
        "candidate_source_categories": (
            _text(row.get("candidate_source_categories")).split("|")
            if _text(row.get("candidate_source_categories"))
            else []
        ),
    }
    for field_name, expected_value in expected_arrays.items():
        if descriptor.get(field_name) != expected_value:
            errors.append(
                "formal presentation descriptor source array mismatch: "
                f"artifact={label} row={row_number} field={field_name} "
                f"expected={expected_value!r} actual={descriptor.get(field_name)!r}"
            )
    expected_mode = (
        "all_candidates"
        if expected_arrays["candidate_source_row_ids"]
        else "taxonomy"
    )
    if descriptor.get("mode") != expected_mode:
        errors.append(
            "formal presentation descriptor mode/source mismatch: "
            f"artifact={label} row={row_number} expected={expected_mode!r} "
            f"actual={descriptor.get('mode')!r}"
        )
    if descriptor.get("presentation_row_sha256") != presentation_row_sha:
        errors.append(
            "formal presentation descriptor row SHA-256 mismatch: "
            f"artifact={label} row={row_number} "
            f"expected={presentation_row_sha!r} "
            f"actual={descriptor.get('presentation_row_sha256')!r}"
        )
    for source_name, expected_artifact, expected_keys_for_source in (
        (
            "watch",
            VOLUME_WATCH_ARTIFACT,
            {"artifact", "artifact_sha256", "record_number", "row_sha256"},
        ),
        (
            "taxonomy",
            VOLUME_TAXONOMY_ARTIFACT,
            {"artifact", "artifact_sha256", "row_sha256"},
        ),
    ):
        source_descriptor = descriptor.get(source_name)
        if not isinstance(source_descriptor, dict):
            errors.append(
                "formal presentation descriptor source is not an object: "
                f"artifact={label} row={row_number} source={source_name}"
            )
            continue
        if set(source_descriptor) != expected_keys_for_source:
            errors.append(
                "formal presentation descriptor source schema mismatch: "
                f"artifact={label} row={row_number} source={source_name}"
            )
        if source_descriptor.get("artifact") != expected_artifact:
            errors.append(
                "formal presentation descriptor source artifact mismatch: "
                f"artifact={label} row={row_number} source={source_name} "
                f"value={source_descriptor.get('artifact')!r}"
            )
        for hash_field in ("artifact_sha256", "row_sha256"):
            if not re.fullmatch(
                r"[0-9a-f]{64}", _text(source_descriptor.get(hash_field))
            ):
                errors.append(
                    "formal presentation descriptor source SHA-256 is invalid: "
                    f"artifact={label} row={row_number} source={source_name} "
                    f"field={hash_field}"
                )
    if validate_current_sources and root is not None:
        errors.extend(
            _validate_current_presentation_descriptor_sources(
                root,
                row,
                descriptor,
                label,
                row_number,
            )
        )
    return errors


def _validate_formal_resolution_lineage(root: Path) -> list[str]:
    errors: list[str] = []
    artifacts = {
        "raw": root / "output/latest/daily_candidate_model_signals_latest.csv",
        "report": (
            root
            / "output/latest/daily_candidate_model_signals_for_report_latest.csv"
        ),
    }
    indexed: dict[
        str,
        dict[tuple[str, str, str, str, str], dict[str, str]],
    ] = {}

    def normalized_date(row: dict[str, str]) -> str:
        return re.sub(
            r"[^0-9]",
            "",
            _text(row.get("signal_date") or row.get("date")),
        )[:8]

    candidate_rows: list[dict[str, str]] = []
    candidate_path = root / ALL_CANDIDATES_ARTIFACT
    if candidate_path.is_file():
        try:
            _, candidate_rows = _read_artifact(candidate_path, root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(
                f"unable to read current all_candidates formal crosswalk: {exc}"
            )

    for label, path in artifacts.items():
        if not path.is_file():
            indexed[label] = {}
            continue
        try:
            columns, rows = _read_artifact(path, root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(f"unable to read formal resolution artifact {label}: {exc}")
            indexed[label] = {}
            continue
        effective_rows = [
            row
            for row in rows
            if _text(row.get("model_id")) in VOLUME_V2_MODELS
            and normalized_date(row) >= FORMAL_RESOLUTION_EFFECTIVE_FROM
        ]
        if not effective_rows:
            indexed[label] = {}
            continue
        errors.extend(
            _validate_formal_source_crosswalk(
                candidate_rows,
                effective_rows,
                f"current_{label}",
            )
        )
        missing = sorted(set(FORMAL_RESOLUTION_FIELDS) - set(columns))
        if missing:
            errors.append(
                f"formal resolution artifact is missing lineage fields: "
                f"artifact={label} missing={missing}"
            )
            indexed[label] = {}
            continue
        artifact_index: dict[
            tuple[str, str, str, str, str], dict[str, str]
        ] = {}
        for row_number, row in enumerate(effective_rows, start=2):
            identity = (
                normalized_date(row),
                _text(row.get("report_line") or row.get("report_bucket")),
                _text(row.get("source_row_index")),
                _text(row.get("stock_id")),
                _text(row.get("model_id")),
            )
            if identity in artifact_index:
                errors.append(
                    f"formal resolution artifact has duplicate identity: "
                    f"artifact={label} identity={identity}"
                )
            artifact_index[identity] = row
            errors.extend(
                _validate_formal_projection_hashes(
                    row,
                    f"current_{label}",
                    row_number,
                    root=root,
                    validate_current_sources=True,
                )
            )

            current_source_ids_text = _text(
                row.get("candidate_source_row_ids")
            )
            current_source_ids = (
                current_source_ids_text.split("|")
                if current_source_ids_text
                else []
            )
            if len(current_source_ids) > 1 and _text(
                row.get("original_category")
            ) != "volume_breakout":
                errors.append(
                    f"formal multi-source resolution category is not canonical: "
                    f"artifact={label} row={row_number}"
                )
        indexed[label] = artifact_index

    raw_index = indexed.get("raw", {})
    report_index = indexed.get("report", {})
    if raw_index or report_index:
        if set(raw_index) != set(report_index):
            errors.append(
                "formal raw/report resolution identity mismatch: "
                f"raw_only={sorted(set(raw_index) - set(report_index))} "
                f"report_only={sorted(set(report_index) - set(raw_index))}"
            )
        for identity in sorted(set(raw_index).intersection(report_index)):
            raw_row = raw_index[identity]
            report_row = report_index[identity]
            for field_name in (*FORMAL_RESOLUTION_FIELDS, "original_category"):
                if _text(raw_row.get(field_name)) != _text(
                    report_row.get(field_name)
                ):
                    errors.append(
                        f"formal raw/report resolution lineage mismatch: "
                        f"identity={identity} field={field_name}"
                    )
    return errors


def _index_official(rows: Iterable[dict[str, str]], label: str, errors: list[str]) -> dict[str, str]:
    indexed: dict[str, str] = {}
    for row in rows:
        stock_id = _normalize_stock_id(row.get("stock_id"))
        if not stock_id:
            continue
        signal = _normalize_signal(row.get(FIELD_NAME))
        if stock_id in indexed and indexed[stock_id] != signal:
            errors.append(f"{label} has duplicate conflicting warrant rows: stock_id={stock_id}")
        indexed[stock_id] = signal
    return indexed


def _index_candidates(
    rows: Iterable[dict[str, str]],
    label: str,
    errors: list[str],
) -> tuple[dict[tuple[str, str], str], dict[str, str]]:
    by_source: dict[tuple[str, str], str] = {}
    signals_by_stock: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        stock_id = _normalize_stock_id(row.get("stock_id"))
        source_row_index = _text(row.get("source_row_index"))
        if not stock_id:
            continue
        signal = _normalize_signal(row.get(FIELD_NAME))
        if source_row_index:
            key = (source_row_index, stock_id)
            if key in by_source and by_source[key] != signal:
                errors.append(f"{label} has conflicting candidate source rows: key={key}")
            by_source[key] = signal
        signals_by_stock[stock_id].add(signal)
    by_stock: dict[str, str] = {}
    for stock_id, signals in signals_by_stock.items():
        if len(signals) != 1:
            errors.append(
                f"{label} has inconsistent warrant projection by stock: "
                f"stock_id={stock_id} signals={sorted(signals)}"
            )
        else:
            by_stock[stock_id] = next(iter(signals))
    return by_source, by_stock


def _signal_identity(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    return (
        _text(row.get("signal_date")),
        _text(row.get("report_line")) or _text(row.get("report_bucket")),
        _text(row.get("source_row_index")),
        _normalize_stock_id(row.get("stock_id")),
        _text(row.get("model_id")),
    )


def _validate_bonus_marker(row: dict[str, str], label: str) -> list[str]:
    model_id = _text(row.get("model_id"))
    signal = _normalize_signal(row.get(FIELD_NAME))
    markers = [
        part.strip().lower()
        for part in _text(row.get("score_components")).split("|")
        if part.strip().lower().startswith("warrant bullish +")
    ]
    expected = ["warrant bullish +2"] if model_id in BONUS_MODELS and signal in BULLISH_WARRANT_SIGNALS else []
    if markers != expected:
        return [
            f"volume v2 warrant bonus marker mismatch {label}: "
            f"model_id={model_id} stock_id={_normalize_stock_id(row.get('stock_id'))} "
            f"expected={expected} actual={markers}"
        ]
    return []


def _validate_rank_order(rows: list[dict[str, str]], label: str) -> list[str]:
    errors: list[str] = []
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if _text(row.get("model_id")) not in VOLUME_V2_MODELS:
            continue
        key = (
            _text(row.get("report_line")) or _text(row.get("report_bucket")),
            _text(row.get("model_id")),
        )
        groups[key].append(row)
    for key, members in groups.items():
        invalid_scores = [
            _normalize_stock_id(row.get("stock_id"))
            for row in members
            if _number(row.get("model_score")) is None
        ]
        if invalid_scores:
            errors.append(
                f"volume v2 formal model_score is blank or non-numeric {label}: "
                f"group={key} stocks={invalid_scores}"
            )
            continue
        ordered = sorted(
            members,
            key=lambda row: (
                -(_number(row.get("model_score")) or Decimal("0")),
                _normalize_stock_id(row.get("stock_id")),
                _text(row.get("source_row_index")),
            ),
        )
        for expected_rank, row in enumerate(ordered, start=1):
            actual = _text(row.get("model_rank"))
            if actual != str(expected_rank):
                errors.append(
                    f"volume v2 rank parity mismatch {label}: group={key} "
                    f"stock_id={_normalize_stock_id(row.get('stock_id'))} "
                    f"expected={expected_rank} actual={actual}"
                )
    return errors


def _validate_formal_score_fields(
    rows: list[dict[str, str]], label: str
) -> list[str]:
    errors: list[str] = []
    for row in rows:
        if _text(row.get("model_id")) not in VOLUME_V2_MODELS:
            continue
        identity = _signal_identity(row)
        model_score = _number(row.get("model_score"))
        final_rank_score = _number(row.get("final_rank_score"))
        if model_score is None or final_rank_score is None:
            errors.append(
                f"volume v2 formal score field is blank or non-numeric {label}: {identity}"
            )
            continue
        if not (Decimal("0") <= model_score <= Decimal("100")):
            errors.append(
                f"volume v2 model_score is outside 0..100 {label}: "
                f"identity={identity} value={model_score}"
            )
        if model_score != final_rank_score:
            errors.append(
                f"volume v2 formal score direct-mirror mismatch {label}: "
                f"identity={identity} model_score={model_score} "
                f"final_rank_score={final_rank_score}"
            )
    return errors


def _validate_watch_score_rank_rows(
    rows: list[dict[str, str]], label: str
) -> list[str]:
    errors: list[str] = []
    identities: set[tuple[str, str]] = set()
    priority_order = {
        "A_bottom_volume_attack": 0,
        "B_bottom_volume_attack_with_risk": 1,
    }
    sortable: list[tuple[int, Decimal, Decimal, dict[str, str]]] = []
    for row_number, row in enumerate(rows, start=2):
        identity = (
            _text(row.get("signal_date")),
            _normalize_stock_id(row.get("stock_id")),
        )
        if not all(identity):
            errors.append(f"volume watch score/rank identity is blank {label}: row={row_number}")
        elif identity in identities:
            errors.append(f"duplicate volume watch score/rank identity {label}: {identity}")
        identities.add(identity)
        score = _number(row.get("advisory_volume_breakout_score"))
        ratio = _number(row.get("volume_ratio"))
        if score is None or ratio is None:
            errors.append(
                f"volume watch score/rank sort input is non-numeric {label}: "
                f"row={row_number} stock_id={identity[1]}"
            )
            continue
        sortable.append(
            (
                priority_order.get(_text(row.get("volume_breakout_priority")), 9),
                -score,
                -ratio,
                row,
            )
        )
    ordered = sorted(sortable, key=lambda item: item[:3])
    for expected_rank, (_priority, _score, _ratio, row) in enumerate(ordered, start=1):
        actual_rank = _text(row.get("advisory_volume_breakout_rank"))
        if actual_rank != str(expected_rank):
            errors.append(
                f"volume watch rank parity mismatch {label}: "
                f"stock_id={_normalize_stock_id(row.get('stock_id'))} "
                f"expected={expected_rank} actual={actual_rank}"
            )
    return errors


def _validate_operation_score_mirror(
    rows: list[dict[str, str]], label: str
) -> list[str]:
    errors: list[str] = []
    for row_number, row in enumerate(rows, start=2):
        if _text(row.get("model_id")) not in VOLUME_V2_MODELS:
            continue
        if _text(row.get("row_type")) != "data":
            continue
        final_score = _number(row.get("final_rank_score"))
        direct_mirror = _number(row.get("research_score"))
        if final_score is None or direct_mirror is None or final_score != direct_mirror:
            errors.append(
                "volume v2 operation final_rank_score direct mirror mismatch "
                f"{label}: row={row_number} stock_id={_normalize_stock_id(row.get('stock_id'))} "
                f"final_rank_score={_text(row.get('final_rank_score'))!r} "
                f"research_score={_text(row.get('research_score'))!r}"
            )
    return errors


def _validate_projection_set(
    official_rows: list[dict[str, str]],
    candidate_rows: list[dict[str, str]],
    signal_rows: list[dict[str, str]],
    label: str,
) -> tuple[list[str], dict[tuple[str, str, str, str, str], dict[str, str]]]:
    errors: list[str] = []
    official = _index_official(official_rows, label, errors)
    candidate_by_source, candidate_by_stock = _index_candidates(candidate_rows, label, errors)
    for stock_id, candidate_signal in sorted(candidate_by_stock.items()):
        if candidate_signal in BULLISH_WARRANT_SIGNALS and stock_id not in official:
            errors.append(
                "positive all_candidates warrant projection lacks official canonical row "
                f"{label}: stock_id={stock_id} signal={candidate_signal}"
            )
    indexed_signals: dict[tuple[str, str, str, str, str], dict[str, str]] = {}
    for row in signal_rows:
        model_id = _text(row.get("model_id"))
        if model_id not in VOLUME_V2_MODELS:
            continue
        identity = _signal_identity(row)
        if identity in indexed_signals:
            errors.append(f"duplicate volume v2 formal signal identity {label}: {identity}")
            continue
        indexed_signals[identity] = row
        source_key = (identity[2], identity[3])
        expected = candidate_by_source.get(source_key)
        if expected is None:
            expected = candidate_by_stock.get(identity[3])
        has_candidate_projection = expected is not None
        if expected is None:
            expected = ""
        actual = _normalize_signal(row.get(FIELD_NAME))
        if actual != expected:
            errors.append(
                f"formal volume warrant projection mismatch {label}: {identity} "
                f"expected={expected!r} actual={actual!r}"
            )
        if (
            has_candidate_projection
            and identity[3] in official
            and expected != official[identity[3]]
        ):
            errors.append(
                f"official/all_candidates warrant projection mismatch {label}: "
                f"stock_id={identity[3]} official={official[identity[3]]!r} candidate={expected!r}"
            )
        errors.extend(_validate_bonus_marker(row, label))
    errors.extend(_validate_formal_score_fields(list(indexed_signals.values()), label))
    errors.extend(_validate_rank_order(list(indexed_signals.values()), label))
    return errors, indexed_signals


def _validate_current_projection(
    root: Path,
    *,
    trusted_ref: str = "HEAD",
) -> list[str]:
    paths = {
        "official": root / "output/latest/warrant_flow_latest.csv",
        "candidate": root / "output/latest/all_candidates_latest.csv",
        "watch": root / VOLUME_WATCH_ARTIFACT,
        "raw": root / "output/latest/daily_candidate_model_signals_latest.csv",
        "report": root / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "theme": root / THEME_ADVISORY_ARTIFACT,
        "operation": root / "output/latest/daily_volume_breakout_operation_section_latest.csv",
    }
    errors: list[str] = []
    artifacts: dict[str, tuple[list[str], list[dict[str, str]]]] = {}
    for label, path in paths.items():
        try:
            artifacts[label] = _read_artifact(path, root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(f"missing or unreadable current lineage artifact: {label}: {exc}")
    if errors:
        return errors

    _, official_rows = artifacts["official"]
    _, candidate_rows = artifacts["candidate"]
    _, watch_rows = artifacts["watch"]
    _, raw_rows = artifacts["raw"]
    _, report_rows = artifacts["report"]
    theme_columns, theme_rows = artifacts["theme"]
    _, operation_rows = artifacts["operation"]
    errors.extend(_validate_watch_score_rank_rows(watch_rows, "current_watch"))
    errors.extend(_validate_operation_score_mirror(operation_rows, "current_operation"))
    raw_errors, raw_index = _validate_projection_set(
        official_rows, candidate_rows, raw_rows, "current_raw"
    )
    report_errors, report_index = _validate_projection_set(
        official_rows, candidate_rows, report_rows, "current_report"
    )
    errors.extend(raw_errors)
    errors.extend(report_errors)
    if set(raw_index) != set(report_index):
        errors.append("current raw/report volume v2 signal membership mismatch")
    for identity in sorted(set(raw_index) & set(report_index)):
        raw = raw_index[identity]
        report = report_index[identity]
        for column in (
            FIELD_NAME,
            "final_rank_score",
            "model_score",
            "model_rank",
            "score_components",
        ):
            if _text(raw.get(column)) != _text(report.get(column)):
                errors.append(
                    f"current raw/report volume v2 parity mismatch: identity={identity} column={column}"
                )

    missing_theme_columns = [
        column for column in THEME_LINEAGE_COLUMNS if column not in theme_columns
    ]
    if missing_theme_columns:
        errors.append(
            "theme advisory warrant lineage columns are missing: "
            + ",".join(missing_theme_columns)
        )
        return errors

    _, candidate_index = _index_candidates(candidate_rows, "current_theme", errors)
    declared_official_artifacts = {
        _text(row.get("warrant_flow_official_source_artifact"))
        for row in theme_rows
    }
    declared_official_shas = {
        _text(row.get("warrant_flow_official_source_sha256"))
        for row in theme_rows
    }
    expected_official_artifact = "output/latest/warrant_flow_latest.csv"
    theme_official_rows: list[dict[str, str]] = []
    theme_revision_invalid = False
    try:
        theme_payload = _artifact_payload(paths["theme"], root)
        theme_revision = _committed_artifact_revision(
            root,
            THEME_ADVISORY_ARTIFACT,
            theme_payload,
            trusted_ref=trusted_ref,
        )
    except (FileNotFoundError, OSError, RuntimeError, UnicodeError) as exc:
        errors.append(f"theme advisory revision cannot be identified: {exc}")
        theme_revision = None
        theme_revision_invalid = True
    if theme_rows and declared_official_artifacts != {expected_official_artifact}:
        errors.append(
            "theme advisory official warrant source artifact is not singular canonical: "
            f"expected={expected_official_artifact!r} "
            f"actual={sorted(declared_official_artifacts)}"
        )
    if theme_rows and len(declared_official_shas) != 1:
        errors.append(
            "theme advisory official warrant source revision is not singular: "
            f"actual={sorted(declared_official_shas)}"
        )
    elif (
        theme_rows
        and declared_official_artifacts == {expected_official_artifact}
        and not theme_revision_invalid
    ):
        declared_official_sha = next(iter(declared_official_shas))
        try:
            official_payload, official_revision = _resolve_pinned_canonical_source_revision(
                root,
                expected_official_artifact,
                declared_official_sha,
                trusted_ref=trusted_ref,
                allow_live=theme_revision is None,
            )
            if theme_revision is None and official_revision != LIVE_SOURCE_REVISION:
                errors.append(
                    "live theme advisory artifact cannot consume a historical official "
                    f"warrant revision: source_revision={official_revision}"
                )
            elif theme_revision is not None and (
                official_revision == LIVE_SOURCE_REVISION
                or not _source_precedes_consumer(
                    root,
                    official_revision,
                    theme_revision,
                )
            ):
                errors.append(
                    "theme advisory official warrant revision is not available before "
                    "the consumer artifact: "
                    f"source_revision={official_revision} "
                    f"theme_revision={theme_revision}"
                )
            official_columns, theme_official_rows = _read_csv_payload(official_payload)
            missing_official_columns = sorted(
                {"stock_id", FIELD_NAME} - set(official_columns)
            )
            if missing_official_columns:
                errors.append(
                    "theme advisory pinned official warrant revision is missing columns: "
                    + ",".join(missing_official_columns)
                )
                theme_official_rows = []
            if not {"date", "signal_date"}.intersection(official_columns):
                errors.append(
                    "theme advisory pinned official warrant revision has no as-of column"
                )
                theme_official_rows = []
        except (RuntimeError, UnicodeError) as exc:
            errors.append(
                "theme advisory official warrant source revision cannot be validated: "
                f"{exc}"
            )

    official_index = _index_official(
        theme_official_rows,
        "current_theme_pinned_official_revision",
        errors,
    )
    official_dates: dict[str, str] = {}
    official_source_dates: set[str] = set()
    official_source_ids: set[str] = set()
    for row_number, row in enumerate(theme_official_rows, start=2):
        stock_id = _normalize_stock_id(row.get("stock_id"))
        source_date = _text(row.get("date")) or _text(row.get("signal_date"))
        if not source_date:
            errors.append(
                "theme advisory pinned official warrant revision row has no as-of: "
                f"row={row_number} stock_id={stock_id}"
            )
        else:
            if re.fullmatch(r"[0-9]{8}", source_date) is None:
                errors.append(
                    "theme advisory pinned official warrant revision row has invalid "
                    f"as-of: row={row_number} stock_id={stock_id} value={source_date!r}"
                )
            official_source_dates.add(source_date)
        if stock_id:
            if stock_id in official_source_ids:
                errors.append(
                    "theme advisory pinned official warrant revision has duplicate "
                    f"stock_id rows: stock_id={stock_id}"
                )
            official_source_ids.add(stock_id)
            official_dates[stock_id] = source_date
    if len(official_source_dates) > 1:
        errors.append(
            "theme advisory pinned official warrant revision has multiple as-of dates: "
            + ",".join(sorted(official_source_dates))
        )
    if theme_official_rows and not official_source_dates:
        errors.append(
            "theme advisory pinned official warrant revision has no verifiable as-of"
        )
    if not theme_official_rows and theme_rows:
        errors.append(
            "theme advisory pinned official warrant revision is empty; as-of cannot be verified"
        )
    candidate_dates: dict[str, set[str]] = defaultdict(set)
    for row in candidate_rows:
        stock_id = _normalize_stock_id(row.get("stock_id"))
        if stock_id:
            candidate_dates[stock_id].add(
                _text(row.get("signal_date")) or _text(row.get("date"))
            )

    expected_candidate_sha = _canonical_text_sha256(
        _artifact_payload(paths["candidate"], root)
    )
    expected_watch_sha = _canonical_text_sha256(
        _artifact_payload(paths["watch"], root)
    )
    expected_constants = {
        "volume_watch_source_artifact": VOLUME_WATCH_ARTIFACT,
        "volume_watch_source_sha256": expected_watch_sha,
        "warrant_flow_source_artifact": "output/latest/all_candidates_latest.csv",
        "warrant_flow_source_sha256": expected_candidate_sha,
        "warrant_flow_official_source_artifact": expected_official_artifact,
    }
    watch_index: dict[tuple[str, str], dict[str, str]] = {}
    for row in watch_rows:
        key = (
            _text(row.get("signal_date")),
            _normalize_stock_id(row.get("stock_id")),
        )
        if key in watch_index:
            errors.append(f"duplicate watch advisory lineage key current_theme: {key}")
        watch_index[key] = row
    theme_index: dict[tuple[str, str], dict[str, str]] = {}
    for row_number, row in enumerate(theme_rows, start=2):
        stock_id = _normalize_stock_id(row.get("stock_id"))
        watch_key = (_text(row.get("signal_date")), stock_id)
        if watch_key in theme_index:
            errors.append(f"duplicate theme advisory watch lineage key: {watch_key}")
        theme_index[watch_key] = row
        watch_row = watch_index.get(watch_key)
        if watch_row is None:
            errors.append(
                f"theme advisory watch score/rank row lacks canonical watch source: {watch_key}"
            )
        else:
            for source_column, projection_column in (
                ("advisory_volume_breakout_score", "volume_breakout_score"),
                ("advisory_volume_breakout_rank", "volume_breakout_rank"),
            ):
                if _text(row.get(projection_column)) != _text(
                    watch_row.get(source_column)
                ):
                    errors.append(
                        "theme advisory watch score/rank parity mismatch: "
                        f"key={watch_key} source_column={source_column} "
                        f"projection_column={projection_column} "
                        f"expected={_text(watch_row.get(source_column))!r} "
                        f"actual={_text(row.get(projection_column))!r}"
                    )
            expected_watch_as_of = _text(watch_row.get("advisory_score_as_of"))
            if expected_watch_as_of != watch_key[0]:
                errors.append(
                    "canonical watch advisory_score_as_of mismatch: "
                    f"key={watch_key} actual={expected_watch_as_of!r}"
                )
            if _text(row.get("volume_watch_as_of")) != expected_watch_as_of:
                errors.append(
                    "theme advisory volume_watch_as_of mismatch: "
                    f"key={watch_key} expected={expected_watch_as_of!r} "
                    f"actual={_text(row.get('volume_watch_as_of'))!r}"
                )
        actual = _normalize_signal(row.get(FIELD_NAME))
        expected = candidate_index.get(stock_id, "")
        if actual != expected:
            errors.append(
                "theme advisory warrant projection differs from all_candidates: "
                f"row={row_number} stock_id={stock_id} expected={expected!r} actual={actual!r}"
            )
        if stock_id in official_index and actual != official_index[stock_id]:
            errors.append(
                "theme advisory warrant projection differs from official warrant: "
                f"row={row_number} stock_id={stock_id} "
                f"official={official_index[stock_id]!r} actual={actual!r}"
            )
        elif actual and stock_id not in official_index:
            errors.append(
                "theme advisory positive warrant projection lacks pinned official row: "
                f"row={row_number} stock_id={stock_id} actual={actual!r}"
            )
        for column, expected_value in expected_constants.items():
            if _text(row.get(column)) != expected_value:
                errors.append(
                    "theme advisory warrant lineage metadata mismatch: "
                    f"row={row_number} stock_id={stock_id} column={column} "
                    f"expected={expected_value!r} actual={_text(row.get(column))!r}"
                )
        expected_dates = candidate_dates.get(stock_id, set())
        expected_dates.discard("")
        expected_as_of = official_dates.get(stock_id, "")
        if not expected_as_of and len(official_source_dates) == 1:
            expected_as_of = next(iter(official_source_dates))
        if not expected_as_of and len(expected_dates) == 1:
            expected_as_of = next(iter(expected_dates))
        actual_as_of = _text(row.get("warrant_flow_as_of"))
        if not actual_as_of:
            errors.append(
                f"theme advisory warrant_flow_as_of is blank: row={row_number} stock_id={stock_id}"
            )
        elif expected_as_of and actual_as_of != expected_as_of:
            errors.append(
                "theme advisory warrant_flow_as_of mismatch: "
                f"row={row_number} stock_id={stock_id} "
                f"expected={expected_as_of!r} actual={actual_as_of!r}"
            )
        signal_date = _text(row.get("signal_date"))
        if (
            actual_as_of
            and signal_date
            and re.fullmatch(r"[0-9]{8}", actual_as_of)
            and re.fullmatch(r"[0-9]{8}", signal_date)
            and actual_as_of > signal_date
        ):
            errors.append(
                "theme advisory warrant_flow_as_of is later than signal_date: "
                f"row={row_number} stock_id={stock_id} "
                f"signal_date={signal_date} warrant_flow_as_of={actual_as_of}"
            )
    if set(theme_index) != set(watch_index):
        errors.append(
            "theme advisory watch score/rank membership mismatch: "
            f"missing={sorted(set(watch_index) - set(theme_index))} "
            f"extra={sorted(set(theme_index) - set(watch_index))}"
        )
    return errors


def _dated_files(root: Path, pattern: str) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in _artifact_paths(root, pattern):
        match = re.search(r"([0-9]{8})(?=\.csv$)", path.name)
        if match:
            result[match.group(1)] = path
    return result


def _manifest_dated_files(root: Path, artifact_id: str) -> dict[str, Path]:
    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    return {
        snapshot.report_date: snapshot.path
        for snapshot in select_latest_snapshot_revisions(
            snapshot_dir,
            artifact_id,
            repository_root=root,
            payload_loader=lambda path: _artifact_payload(path, root),
        )
    }


def _validate_historical_formal_signal_log(
    root: Path,
    candidate_snapshots: dict[str, Path],
    report_snapshots: dict[str, Path],
) -> list[str]:
    errors: list[str] = []
    path = root / FORMAL_SIGNAL_LOG_ARTIFACT
    try:
        columns, rows = _read_artifact(path, root)
    except (FileNotFoundError, OSError, UnicodeError) as exc:
        return [f"unable to read formal signal log lineage: {exc}"]
    effective_rows = [
        row
        for row in rows
        if _text(row.get("model_id")) in VOLUME_V2_MODELS
        and re.sub(
            r"[^0-9]",
            "",
            _text(row.get("signal_date") or row.get("date")),
        )[:8]
        >= FORMAL_RESOLUTION_EFFECTIVE_FROM
    ]
    effective_report_rows: list[dict[str, str]] = []
    report_rows_with_context: list[tuple[str, int, dict[str, str]]] = []
    for snapshot_date, report_path in sorted(report_snapshots.items()):
        try:
            report_columns, report_rows = _read_artifact(report_path, root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(
                "unable to read formal signal log report snapshot parity: "
                f"snapshot_date={snapshot_date} error={exc}"
            )
            continue
        dated_effective_rows = [
            row
            for row in report_rows
            if _text(row.get("model_id")) in VOLUME_V2_MODELS
            and re.sub(
                r"[^0-9]",
                "",
                _text(row.get("signal_date") or row.get("date")),
            )[:8]
            >= FORMAL_RESOLUTION_EFFECTIVE_FROM
        ]
        if dated_effective_rows:
            missing_report_fields = sorted(
                set(FORMAL_RESOLUTION_FIELDS) - set(report_columns)
            )
            if missing_report_fields:
                errors.append(
                    "formal report snapshot is missing resolution lineage fields: "
                    f"snapshot_date={snapshot_date} missing={missing_report_fields}"
                )
        for row_number, row in enumerate(dated_effective_rows, start=2):
            effective_report_rows.append(row)
            report_rows_with_context.append((snapshot_date, row_number, row))

    if not effective_rows and not effective_report_rows:
        return errors

    missing_fields = sorted(set(FORMAL_RESOLUTION_FIELDS) - set(columns))
    if missing_fields:
        errors.append(
            "formal signal log is missing resolution lineage fields: "
            f"missing={missing_fields}"
        )

    seen_identities: set[tuple[str, str, str, str]] = set()
    signal_rows_by_identity: dict[
        tuple[str, str, str, str], dict[str, str]
    ] = {}
    rows_by_date: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row_number, row in enumerate(effective_rows, start=2):
        signal_date = re.sub(
            r"[^0-9]",
            "",
            _text(row.get("signal_date") or row.get("date")),
        )[:8]
        identity = (
            signal_date,
            _text(row.get("report_line") or row.get("report_bucket")),
            _normalize_stock_id(row.get("stock_id")),
            _text(row.get("model_id")),
        )
        if identity in seen_identities:
            errors.append(
                "formal signal log has duplicate effective identity: "
                f"row={row_number} identity={identity}"
            )
        seen_identities.add(identity)
        signal_rows_by_identity.setdefault(identity, row)
        rows_by_date[signal_date].append(row)
        errors.extend(
            _validate_formal_projection_hashes(
                row,
                f"formal_signal_log_{signal_date}",
                row_number,
            )
        )

    for signal_date, dated_rows in sorted(rows_by_date.items()):
        candidate_path = candidate_snapshots.get(signal_date)
        if candidate_path is None:
            errors.append(
                "formal signal log date is missing an all_candidates manifest snapshot: "
                f"signal_date={signal_date}"
            )
            continue
        try:
            _, candidate_rows = _read_artifact(candidate_path, root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(
                "unable to read formal signal log all_candidates snapshot: "
                f"signal_date={signal_date} error={exc}"
            )
            continue
        errors.extend(
            _validate_formal_source_crosswalk(
                candidate_rows,
                dated_rows,
                f"formal_signal_log_{signal_date}",
            )
        )

    report_rows_by_identity: dict[
        tuple[str, str, str, str], dict[str, str]
    ] = {}
    for snapshot_date, row_number, row in report_rows_with_context:
        signal_date = re.sub(
            r"[^0-9]",
            "",
            _text(row.get("signal_date") or row.get("date")),
        )[:8]
        identity = (
            signal_date,
            _text(row.get("report_line") or row.get("report_bucket")),
            _normalize_stock_id(row.get("stock_id")),
            _text(row.get("model_id")),
        )
        if signal_date != snapshot_date:
            errors.append(
                "formal report snapshot date does not match signal date: "
                f"snapshot_date={snapshot_date} row={row_number} identity={identity}"
            )
        if identity in report_rows_by_identity:
            errors.append(
                "formal report snapshot has duplicate effective identity: "
                f"snapshot_date={snapshot_date} row={row_number} identity={identity}"
            )
        report_rows_by_identity.setdefault(identity, row)

    signal_identities = set(signal_rows_by_identity)
    report_identities = set(report_rows_by_identity)
    if signal_identities != report_identities:
        errors.append(
            "formal signal log/report identity membership mismatch: "
            f"signal_log_only={sorted(signal_identities - report_identities)} "
            f"report_only={sorted(report_identities - signal_identities)}"
        )
    for identity in sorted(signal_identities & report_identities):
        signal_row = signal_rows_by_identity[identity]
        report_row = report_rows_by_identity[identity]
        for field_name in FORMAL_RESOLUTION_FIELDS:
            if _text(signal_row.get(field_name)) != _text(report_row.get(field_name)):
                errors.append(
                    "formal signal log/report lineage mismatch: "
                    f"identity={identity} field={field_name} "
                    f"signal_log={_text(signal_row.get(field_name))!r} "
                    f"report={_text(report_row.get(field_name))!r}"
                )
    return errors


def _validate_historical_projection(root: Path) -> list[str]:
    official = _dated_files(root, "output/history/warrant_flow/warrant_flow_*.csv")
    errors: list[str] = []
    try:
        candidates = _manifest_dated_files(root, "all_candidates_source_rows")
        reports = _manifest_dated_files(root, "model_signals_for_report")
    except RuntimeError as exc:
        return [f"historical parity cannot select manifest revisions: {exc}"]
    errors.extend(
        _validate_historical_formal_signal_log(root, candidates, reports)
    )
    if not reports:
        return ["historical parity has no formal report snapshots"]

    report_rows_by_date: dict[str, list[dict[str, str]]] = {}
    required_dates: set[str] = set()
    for date, path in sorted(reports.items()):
        try:
            _, report_rows = _read_artifact(path, root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(f"unable to read historical formal report snapshot {date}: {exc}")
            continue
        report_rows_by_date[date] = report_rows
        if any(_text(row.get("model_id")) in VOLUME_V2_MODELS for row in report_rows):
            required_dates.add(date)

    if not required_dates:
        errors.append("historical parity has zero volume v2 formal report dates")
        return errors

    missing_official = sorted(required_dates - set(official))
    missing_candidates = sorted(required_dates - set(candidates))
    if missing_official:
        errors.append(
            "historical volume v2 dates missing official warrant snapshots: "
            + ",".join(missing_official)
        )
    if missing_candidates:
        errors.append(
            "historical volume v2 dates missing all_candidates snapshots: "
            + ",".join(missing_candidates)
        )

    validated_pairs = 0
    for date in sorted(required_dates & set(official) & set(candidates)):
        try:
            _, official_rows = _read_artifact(official[date], root)
            _, candidate_rows = _read_artifact(candidates[date], root)
        except (FileNotFoundError, OSError, UnicodeError) as exc:
            errors.append(f"unable to read historical lineage pair {date}: {exc}")
            continue
        report_rows = report_rows_by_date[date]
        pair_errors, _ = _validate_projection_set(
            official_rows,
            candidate_rows,
            report_rows,
            f"historical_pair_{date}",
        )
        errors.extend(pair_errors)
        errors.extend(
            _validate_formal_source_crosswalk(
                candidate_rows,
                report_rows,
                f"historical_pair_{date}",
            )
        )
        for row_number, report_row in enumerate(report_rows, start=2):
            model_id = _text(report_row.get("model_id"))
            report_signal_date = re.sub(
                r"[^0-9]",
                "",
                _text(report_row.get("signal_date") or report_row.get("date")),
            )[:8]
            if (
                model_id in VOLUME_V2_MODELS
                and report_signal_date >= FORMAL_RESOLUTION_EFFECTIVE_FROM
            ):
                errors.extend(
                    _validate_formal_projection_hashes(
                        report_row,
                        f"historical_pair_{date}",
                        row_number,
                    )
                )
        validated_pairs += 1
    if validated_pairs == 0:
        errors.append("historical volume v2 parity validated zero complete snapshot pairs")
    return errors


def validate(root: Path = ROOT, *, base_ref: str | None = None) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    if base_ref is not None:
        errors.extend(validate_migration_ledgers_append_only(root, base_ref))
    registry_rows = _strict_csv_rows(root / REGISTRY_PATH, REGISTRY_COLUMNS, errors)
    migration_rows = _strict_csv_rows(root / MIGRATIONS_PATH, MIGRATION_COLUMNS, errors)
    consumer_exclusion_rows = _strict_csv_rows(
        root / CONSUMER_EXCLUSIONS_PATH,
        CONSUMER_EXCLUSION_COLUMNS,
        errors,
    )
    consumer_exclusion_migration_rows = _strict_csv_rows(
        root / CONSUMER_EXCLUSION_MIGRATIONS_PATH,
        CONSUMER_EXCLUSION_MIGRATION_COLUMNS,
        errors,
    )
    collision_rows = _strict_csv_rows(
        root / COLLISION_REGISTRY_PATH,
        COLLISION_REGISTRY_COLUMNS,
        errors,
    )
    collision_migration_rows = _strict_csv_rows(
        root / COLLISION_MIGRATIONS_PATH,
        COLLISION_MIGRATION_COLUMNS,
        errors,
    )
    if registry_rows:
        errors.extend(_validate_registry(root, registry_rows))
        errors.extend(_validate_artifact_headers(root, registry_rows))
        errors.extend(_validate_all_candidates_source_identity(root))
        errors.extend(_validate_formal_resolution_lineage(root))
    if registry_rows:
        errors.extend(
            _validate_reverse_current_consumers(
                root,
                registry_rows,
                consumer_exclusion_rows,
            )
        )
    if registry_rows and migration_rows:
        errors.extend(_validate_migrations(registry_rows, migration_rows))
    if consumer_exclusion_rows and consumer_exclusion_migration_rows:
        errors.extend(
            _validate_consumer_exclusion_migrations(
                consumer_exclusion_rows,
                consumer_exclusion_migration_rows,
            )
        )
    if collision_rows:
        errors.extend(_validate_collision_registry(root, collision_rows))
    if collision_rows and collision_migration_rows:
        errors.extend(
            _validate_collision_migrations(collision_rows, collision_migration_rows)
        )
    errors.extend(_validate_dispatcher_ast(root))
    errors.extend(
        _validate_current_projection(
            root,
            trusted_ref=base_ref or "HEAD",
        )
    )
    errors.extend(_validate_historical_projection(root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the explicitly registered volume-v2 warrant and score/rank "
            "canonical producers, mirrors, migrations, parity, and collision guards. "
            "Every current registered node is reverse-scanned across production Python "
            "and requires either a registered consumer or an exact reviewed exclusion."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument(
        "--base-ref",
        default=None,
        help=(
            "Git base commit/ref whose three migration ledgers must remain an "
            "exact append-only prefix"
        ),
    )
    args = parser.parse_args()
    errors = validate(args.repo_root, base_ref=args.base_ref)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "daily canonical field lineage validation passed: "
        f"scope={VALIDATOR_SCOPE} governed_nodes={len(GOVERNED_FIELD_NODES)} "
        "consumer_collisions=registered_or_reviewed_exclusion "
        "dispatcher_collisions=field_registry_exact"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
