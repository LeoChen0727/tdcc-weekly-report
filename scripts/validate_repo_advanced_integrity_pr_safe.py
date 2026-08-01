from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from . import validate_repo_advanced_integrity as strict_validator  # type: ignore
except ImportError:
    import validate_repo_advanced_integrity as strict_validator  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
FRESHNESS_RELATIVE_PATH = "output/latest/data_freshness_latest.csv"
EXTERNAL_SOURCE_CONTRACT_PATH = "config/external_data_source_contract.csv"
PRODUCTION_INVENTORY_PATH = "config/repo_production_inventory.csv"
LIFECYCLE_INVENTORY_PATH = "config/repo_file_lifecycle_inventory.csv"
CANONICAL_LINEAGE_REGISTRY_PATH = (
    "config/daily_model_canonical_field_lineage_registry.csv"
)
CANONICAL_LINEAGE_MIGRATIONS_PATH = (
    "config/daily_model_canonical_field_lineage_migrations.csv"
)
CANONICAL_LINEAGE_VALIDATOR_PATH = (
    "scripts/validate_daily_canonical_field_lineage.py"
)
PR_SAFE_HELPER_PATH = "scripts/validate_repo_advanced_integrity_pr_safe.py"
STRICT_VALIDATOR_PATH = "scripts/validate_repo_advanced_integrity.py"
PR_VALIDATION_WORKFLOW_PATH = (
    ".github/workflows/daily_model_maintenance_pr_validation.yml"
)
PR_BOUNDARY_VALIDATOR_PATH = "scripts/validate_daily_production_boundaries.py"

PR_SAFE_COMMAND = (
    'python scripts/validate_repo_advanced_integrity_pr_safe.py --base-ref "$BASE_SHA"'
)
STRICT_RUNTIME_TEST = (
    "tests/test_repo_advanced_integrity.py::"
    "test_repo_advanced_integrity_validator_passes"
)
STRICT_RUNTIME_TEST_DESELECT = f"--deselect {STRICT_RUNTIME_TEST}"

SOURCE_IDENTITY_GATE_SELF_UPDATE_ID = "registered-source-identity-pr-safe-v1"
SOURCE_IDENTITY_GATE_SELF_UPDATE_BASE_HELPER_SHA256 = (
    "aa21f0ed72eca64232b253a1818df7a60cf8433baf57fb6b8f06edff89cdcf7a"
)
SOURCE_IDENTITY_GATE_TEST_PATH = "tests/test_repo_advanced_integrity_pr_safe.py"
SOURCE_IDENTITY_GATE_SELF_UPDATE_TEST_MARKER = (
    "def test_registered_source_identity_gate_self_update_is_exact_and_one_time"
)
SOURCE_IDENTITY_GATE_SELF_UPDATE_PATHS = frozenset(
    {
        LIFECYCLE_INVENTORY_PATH,
        PR_SAFE_HELPER_PATH,
        SOURCE_IDENTITY_GATE_TEST_PATH,
    }
)
SOURCE_IDENTITY_ARTIFACT_ROLE = "canonical_source_identity_projection"
SOURCE_IDENTITY_MIGRATION_STATUS = "validated_user_approved_migration"
CANONICAL_LINEAGE_PR_COMMAND = (
    'python scripts/validate_daily_canonical_field_lineage.py --base-ref "$BASE_SHA"'
)

PR_SAFE_BOOTSTRAP_SURFACES = frozenset(
    {
        PR_SAFE_HELPER_PATH,
        PR_VALIDATION_WORKFLOW_PATH,
        PRODUCTION_INVENTORY_PATH,
    }
)

STRICT_EXACT_PATHS = frozenset(
    {
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/historical_structured_source_replay.yml",
        PR_VALIDATION_WORKFLOW_PATH,
        "build_data_freshness_latest.py",
        "docs/latest/data_freshness_latest.csv",
        "docs/latest/data_freshness_latest.md",
        EXTERNAL_SOURCE_CONTRACT_PATH,
        FRESHNESS_RELATIVE_PATH,
        "output/latest/data_freshness_latest.md",
        PRODUCTION_INVENTORY_PATH,
        PR_BOUNDARY_VALIDATOR_PATH,
        PR_SAFE_HELPER_PATH,
        "scripts/replay_historical_structured_sources.py",
        "scripts/resolve_daily_report_source_state.py",
        "scripts/run_chatgpt_daily_report_entrypoint.py",
        STRICT_VALIDATOR_PATH,
        "output/latest/chatgpt_daily_pdf_semantic_manifest.csv",
        "output/latest/chatgpt_daily_report_runtime_manifest.json",
        "output/latest/report_manifest_latest.json",
    }
)

STRICT_PATH_PREFIXES = (
    "docs/latest/published_reports/",
    "output/history/daily_model_snapshots/",
    "output/latest/chatgpt_side_outputs_official/",
    "output/latest/published_reports/",
)

HISTORICAL_REPLAY_REPORT_READY_NOTE = (
    "historical structured-source replay updates objective-source freshness only; "
    "publish artifacts remain stale"
)
HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE = (
    "historical structured-source replay must not mark stale daily PDFs ready"
)

EXPECTED_REPLAY_SOURCE_COLUMNS = {
    "official_daily_price": ("official_price_fetch_date", "report_ready"),
    "daily_stock_monitor": ("stock_monitor_price_date", "report_ready"),
    "all_candidates": ("all_candidates_date", "report_ready"),
    "daily_pdf_source": ("main_price_date", "daily_pdf_ready"),
}
ALLOWED_STALE_DATE_SOURCES = frozenset(
    {"daily_stock_monitor", "all_candidates"}
)


def split_list(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [
                {key: str(value or "") for key, value in row.items()}
                for row in csv.DictReader(handle)
            ]
    except (OSError, UnicodeError, csv.Error):
        return []


def parse_csv_payload(
    payload: bytes | None,
    *,
    source: str,
) -> tuple[list[dict[str, str]], list[str]]:
    if payload is None:
        return [], [f"cannot read CSV evidence: {source}"]
    try:
        text = payload.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text, newline=""))
        if not reader.fieldnames:
            return [], [f"CSV evidence has no header: {source}"]
        rows: list[dict[str, str]] = []
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                return [], [
                    f"CSV evidence row has extra fields: {source}:{line_number}"
                ]
            rows.append(
                {str(key): str(value or "") for key, value in row.items()}
            )
        return rows, []
    except (UnicodeError, csv.Error) as exc:
        return [], [f"cannot parse CSV evidence {source}: {exc}"]


def append_only_csv_rows(
    base_ref: str,
    path: str,
    *,
    repository_root: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        path,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / path).read_bytes()
    except OSError as exc:
        return [], [f"cannot read current CSV evidence {path}: {exc}"]
    base_rows, base_errors = parse_csv_payload(
        base_payload,
        source=f"{base_ref}:{path}",
    )
    current_rows, current_errors = parse_csv_payload(
        current_payload,
        source=path,
    )
    if base_errors or current_errors:
        return [], [*base_errors, *current_errors]
    if len(current_rows) < len(base_rows) or current_rows[: len(base_rows)] != base_rows:
        return [], [
            f"registered source-identity evidence must be append-only: {path}"
        ]
    return current_rows[len(base_rows) :], []


def additive_csv_rows(
    base_ref: str,
    path: str,
    *,
    key: str,
    repository_root: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        path,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / path).read_bytes()
    except OSError as exc:
        return [], [f"cannot read current CSV evidence {path}: {exc}"]
    base_rows, base_errors = parse_csv_payload(
        base_payload,
        source=f"{base_ref}:{path}",
    )
    current_rows, current_errors = parse_csv_payload(
        current_payload,
        source=path,
    )
    if base_errors or current_errors:
        return [], [*base_errors, *current_errors]
    base_by_key = {row.get(key, "").strip(): row for row in base_rows}
    current_by_key = {row.get(key, "").strip(): row for row in current_rows}
    if (
        "" in base_by_key
        or "" in current_by_key
        or len(base_by_key) != len(base_rows)
        or len(current_by_key) != len(current_rows)
    ):
        return [], [f"additive CSV evidence has blank or duplicate {key}: {path}"]
    changed_base_keys = sorted(
        observed_key
        for observed_key, base_row in base_by_key.items()
        if current_by_key.get(observed_key) != base_row
    )
    if changed_base_keys:
        return [], [
            f"registered source-identity evidence may not change base {path} row(s): "
            + ", ".join(changed_base_keys)
        ]
    return [
        row for row in current_rows if row.get(key, "").strip() not in base_by_key
    ], []


def normalize_repository_path(path: str) -> str:
    normalized = str(path).replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def changed_paths_from_base(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
) -> tuple[set[str], list[str]]:
    if not str(base_ref or "").strip():
        return set(), ["PR-safe advanced-integrity validation requires a base ref"]
    try:
        proc = subprocess.run(
            [
                "git",
                "diff",
                "--name-only",
                "--no-renames",
                f"{base_ref}...{head_ref}",
                "--",
            ],
            cwd=repository_root,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return set(), [
            f"cannot inspect PR changed paths from base_ref={base_ref}: {exc}"
        ]
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "git diff failed"
        return set(), [
            f"cannot inspect PR changed paths from base_ref={base_ref}: {detail}"
        ]
    return {
        normalize_repository_path(line)
        for line in proc.stdout.splitlines()
        if normalize_repository_path(line)
    }, []


def git_blob_at_ref(
    ref: str,
    path: str,
    *,
    repository_root: Path,
) -> bytes | None:
    try:
        proc = subprocess.run(
            ["git", "show", f"{ref}:{path}"],
            cwd=repository_root,
            capture_output=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return proc.stdout if proc.returncode == 0 else None


def git_path_exists_at_ref(
    ref: str,
    path: str,
    *,
    repository_root: Path,
) -> bool | None:
    try:
        proc = subprocess.run(
            ["git", "ls-tree", "--name-only", ref, "--", path],
            cwd=repository_root,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    observed = {
        normalize_repository_path(line)
        for line in proc.stdout.splitlines()
        if normalize_repository_path(line)
    }
    return normalize_repository_path(path) in observed


def validate_historical_replay_not_ready_marker(
    freshness_path: Path,
) -> list[str]:
    rows = read_csv_rows(freshness_path)
    if len(rows) != 1:
        return [
            "historical-replay freshness marker must contain exactly one row; "
            f"observed={len(rows)}"
        ]
    row = rows[0]
    expected_values = {
        "main_price_date_source": "historical_replay_override",
        "report_ready": "False",
        "daily_pdf_ready": "False",
        "report_ready_note": HISTORICAL_REPLAY_REPORT_READY_NOTE,
        "daily_pdf_ready_note": HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE,
    }
    errors = [
        f"historical-replay freshness marker {column} mismatch: "
        f"expected={expected!r} observed={row.get(column, '').strip()!r}"
        for column, expected in expected_values.items()
        if row.get(column, "").strip() != expected
    ]

    main_price_date = row.get("main_price_date", "").strip()
    replay_date = row.get("historical_replay_main_price_date", "").strip()
    expected_high_water = row.get(
        "expected_price_history_high_water_date", ""
    ).strip()
    actual_high_water = row.get("actual_stock_price_history_date", "").strip()
    dates = {
        "main_price_date": main_price_date,
        "historical_replay_main_price_date": replay_date,
        "expected_price_history_high_water_date": expected_high_water,
        "actual_stock_price_history_date": actual_high_water,
    }
    for label, value in dates.items():
        if not re.fullmatch(r"20\d{6}", value):
            errors.append(
                f"historical-replay freshness marker {label} must be YYYYMMDD; "
                f"observed={value!r}"
            )
    if main_price_date and replay_date and main_price_date != replay_date:
        errors.append(
            "historical_replay_main_price_date must equal main_price_date; "
            f"observed={replay_date!r} main_price_date={main_price_date!r}"
        )
    if expected_high_water and actual_high_water and expected_high_water != actual_high_water:
        errors.append(
            "actual_stock_price_history_date must equal the replay expected high-water date; "
            f"observed={actual_high_water!r} expected={expected_high_water!r}"
        )
    if main_price_date and expected_high_water and expected_high_water < main_price_date:
        errors.append(
            "historical replay expected high-water date cannot precede main_price_date; "
            f"observed={expected_high_water!r} main_price_date={main_price_date!r}"
        )
    return errors


def validate_freshness_is_inherited_from_base(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
) -> list[str]:
    current_path = repository_root / FRESHNESS_RELATIVE_PATH
    try:
        current_payload = current_path.read_bytes()
    except OSError as exc:
        return [f"cannot read current {FRESHNESS_RELATIVE_PATH}: {exc}"]
    base_payload = git_blob_at_ref(
        base_ref,
        FRESHNESS_RELATIVE_PATH,
        repository_root=repository_root,
    )
    if base_payload is None:
        return [
            f"cannot read base freshness artifact from {base_ref}: "
            + FRESHNESS_RELATIVE_PATH
        ]
    if base_payload != current_payload:
        return [
            "PR-safe advanced-integrity validation cannot inherit a changed freshness "
            f"artifact; {FRESHNESS_RELATIVE_PATH} differs from base_ref={base_ref}"
        ]
    return []


def external_source_surface_paths(repository_root: Path) -> set[str]:
    paths: set[str] = set()
    for row in read_csv_rows(repository_root / EXTERNAL_SOURCE_CONTRACT_PATH):
        artifact = normalize_repository_path(row.get("status_artifact", ""))
        if artifact:
            paths.add(artifact)
        for column in ("producer", "validator"):
            paths.update(
                normalize_repository_path(path)
                for path in split_list(row.get(column, ""))
            )
    return paths


def external_source_producer_paths(repository_root: Path) -> set[str]:
    paths: set[str] = set()
    for row in read_csv_rows(repository_root / EXTERNAL_SOURCE_CONTRACT_PATH):
        paths.update(
            normalize_repository_path(path)
            for path in split_list(row.get("producer", ""))
        )
    return {path for path in paths if path}


def requires_strict_runtime_validation(
    path: str,
    *,
    repository_root: Path = ROOT,
) -> bool:
    normalized = normalize_repository_path(path)
    return (
        normalized in STRICT_EXACT_PATHS
        or any(normalized.startswith(prefix) for prefix in STRICT_PATH_PREFIXES)
        or normalized in external_source_surface_paths(repository_root)
    )


def is_registered_source_identity_gate_self_update(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> bool:
    if changed_paths != SOURCE_IDENTITY_GATE_SELF_UPDATE_PATHS:
        return False
    if strict_surface_changes != {PR_SAFE_HELPER_PATH}:
        return False
    base_helper = git_blob_at_ref(
        base_ref,
        PR_SAFE_HELPER_PATH,
        repository_root=repository_root,
    )
    if base_helper is None:
        return False
    if (
        hashlib.sha256(base_helper).hexdigest()
        != SOURCE_IDENTITY_GATE_SELF_UPDATE_BASE_HELPER_SHA256
    ):
        return False
    try:
        current_helper = (repository_root / PR_SAFE_HELPER_PATH).read_text(
            encoding="utf-8"
        )
        current_tests = (repository_root / SOURCE_IDENTITY_GATE_TEST_PATH).read_text(
            encoding="utf-8"
        )
    except (OSError, UnicodeError):
        return False
    return bool(
        SOURCE_IDENTITY_GATE_SELF_UPDATE_ID in current_helper
        and SOURCE_IDENTITY_GATE_SELF_UPDATE_TEST_MARKER in current_tests
    )


def validate_registered_source_identity_migration(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> tuple[bool, list[str]]:
    registered_producers = external_source_producer_paths(repository_root)
    changed_producers = strict_surface_changes & registered_producers
    if not changed_producers:
        return False, []
    allowed_strict_surfaces = set(changed_producers) | {PRODUCTION_INVENTORY_PATH}
    if strict_surface_changes != allowed_strict_surfaces:
        return False, []

    errors: list[str] = []
    required_evidence_paths = {
        CANONICAL_LINEAGE_MIGRATIONS_PATH,
        CANONICAL_LINEAGE_REGISTRY_PATH,
        PRODUCTION_INVENTORY_PATH,
    }
    missing_evidence_paths = sorted(required_evidence_paths - changed_paths)
    if missing_evidence_paths:
        errors.append(
            "registered source-identity migration is missing changed evidence path(s): "
            + ", ".join(missing_evidence_paths)
        )

    added_migrations, migration_errors = append_only_csv_rows(
        base_ref,
        CANONICAL_LINEAGE_MIGRATIONS_PATH,
        repository_root=repository_root,
    )
    added_registry_rows, registry_errors = append_only_csv_rows(
        base_ref,
        CANONICAL_LINEAGE_REGISTRY_PATH,
        repository_root=repository_root,
    )
    added_inventory_rows, inventory_errors = additive_csv_rows(
        base_ref,
        PRODUCTION_INVENTORY_PATH,
        key="path",
        repository_root=repository_root,
    )
    errors.extend(migration_errors)
    errors.extend(registry_errors)
    errors.extend(inventory_errors)
    if errors:
        return True, errors
    if not added_migrations:
        errors.append("registered source-identity migration adds no migration ledger row")
    if not added_registry_rows:
        errors.append("registered source-identity migration adds no lineage registry row")
    if not added_inventory_rows:
        errors.append("registered source-identity migration adds no test inventory row")

    migrations_by_id: dict[str, dict[str, str]] = {}
    migration_lineage_ids: set[str] = set()
    for migration in added_migrations:
        migration_id = migration.get("migration_id", "").strip()
        changed_ids = split_list(migration.get("changed_lineage_ids", ""))
        previous_hashes = split_list(
            migration.get("previous_contract_sha256s", "")
        )
        new_hashes = split_list(migration.get("new_contract_sha256s", ""))
        if not migration_id or migration_id in migrations_by_id:
            errors.append(
                "registered source-identity migration has blank or duplicate migration_id"
            )
            continue
        migrations_by_id[migration_id] = migration
        if migration.get("migration_status", "").strip() != SOURCE_IDENTITY_MIGRATION_STATUS:
            errors.append(
                f"registered source-identity migration is not validated: {migration_id}"
            )
        if not migration.get("user_approval_reference", "").strip():
            errors.append(
                f"registered source-identity migration lacks approval reference: {migration_id}"
            )
        if not changed_ids or not (
            len(changed_ids) == len(previous_hashes) == len(new_hashes)
        ):
            errors.append(
                f"registered source-identity migration SHA lists do not align: {migration_id}"
            )
            continue
        if any(value != "NEW" for value in previous_hashes):
            errors.append(
                f"registered source-identity migration must add new lineage rows only: {migration_id}"
            )
        if any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in new_hashes):
            errors.append(
                f"registered source-identity migration has invalid contract SHA: {migration_id}"
            )
        repeated_ids = migration_lineage_ids & set(changed_ids)
        if repeated_ids:
            errors.append(
                "registered source-identity migration repeats lineage id(s): "
                + ", ".join(sorted(repeated_ids))
            )
        migration_lineage_ids.update(changed_ids)

    registry_by_id: dict[str, dict[str, str]] = {}
    identity_producers: set[str] = set()
    for row in added_registry_rows:
        lineage_id = row.get("lineage_id", "").strip()
        if not lineage_id or lineage_id in registry_by_id:
            errors.append(
                "registered source-identity registry has blank or duplicate lineage_id"
            )
            continue
        registry_by_id[lineage_id] = row
        migration_id = row.get("last_migration_id", "").strip()
        migration = migrations_by_id.get(migration_id)
        if migration is None:
            errors.append(
                f"source-identity registry row lacks an added migration: {lineage_id}"
            )
            continue
        changed_ids = split_list(migration.get("changed_lineage_ids", ""))
        new_hashes = split_list(migration.get("new_contract_sha256s", ""))
        if lineage_id not in changed_ids:
            errors.append(
                f"source-identity registry row is absent from migration: {lineage_id}"
            )
            continue
        expected_sha = new_hashes[changed_ids.index(lineage_id)]
        if row.get("contract_sha256", "").strip() != expected_sha:
            errors.append(
                f"source-identity registry contract SHA mismatch: {lineage_id}"
            )
        if (
            row.get("approval_reference", "").strip()
            != migration.get("user_approval_reference", "").strip()
        ):
            errors.append(
                f"source-identity registry approval mismatch: {lineage_id}"
            )
        producer = normalize_repository_path(row.get("producer", ""))
        if producer in changed_producers:
            if row.get("artifact_role", "").strip() != SOURCE_IDENTITY_ARTIFACT_ROLE:
                errors.append(
                    f"changed producer lineage is not source-identity evidence: {lineage_id}"
                )
            required_values = {
                "identity_columns": row.get("identity_columns", "").strip(),
                "collision_policy": row.get("collision_policy", "").strip(),
                "parity_policy": row.get("parity_policy", "").strip(),
                "forbidden_use": row.get("forbidden_use", "").strip(),
            }
            missing_values = sorted(
                key for key, value in required_values.items() if not value
            )
            allowed_use = row.get("allowed_use", "").strip().lower()
            model_family = row.get("model_family", "").strip().lower()
            if missing_values or "identity" not in allowed_use or "source_identity" not in model_family:
                errors.append(
                    f"changed producer source-identity contract is incomplete: {lineage_id}"
                )
            identity_producers.add(producer)

    if set(registry_by_id) != migration_lineage_ids:
        errors.append(
            "registered source-identity migration and appended registry lineage sets differ"
        )

    added_test_paths: list[str] = []
    for row in added_inventory_rows:
        path = normalize_repository_path(row.get("path", ""))
        if (
            not path.startswith("tests/")
            or "source_identity" not in Path(path).name
            or "test_python" not in {value.strip() for value in row.values()}
        ):
            errors.append(
                "registered source-identity inventory additions must be source-identity tests"
            )
            continue
        if path not in changed_paths or not (repository_root / path).is_file():
            errors.append(
                f"registered source-identity test is not a changed current file: {path}"
            )
        existed_at_base = git_path_exists_at_ref(
            base_ref,
            path,
            repository_root=repository_root,
        )
        if existed_at_base is not False:
            errors.append(
                f"registered source-identity test must be newly added relative to base: {path}"
            )
        added_test_paths.append(path)

    for producer in sorted(changed_producers):
        if producer not in identity_producers:
            errors.append(
                f"changed external producer lacks canonical source-identity registry evidence: {producer}"
            )
        covering_migrations = [
            migration
            for migration in added_migrations
            if producer in split_list(migration.get("affected_consumers", ""))
        ]
        if not covering_migrations:
            errors.append(
                f"changed external producer lacks migration consumer evidence: {producer}"
            )
            continue
        for migration in covering_migrations:
            commands = migration.get("validation_commands", "")
            if CANONICAL_LINEAGE_VALIDATOR_PATH not in commands:
                errors.append(
                    f"source-identity migration omits canonical lineage validator: {producer}"
                )
            if not any(test_path in commands for test_path in added_test_paths):
                errors.append(
                    f"source-identity migration omits independent source-identity test: {producer}"
                )

    try:
        workflow_text = (repository_root / PR_VALIDATION_WORKFLOW_PATH).read_text(
            encoding="utf-8"
        )
    except (OSError, UnicodeError) as exc:
        errors.append(f"cannot read PR validation workflow for migration evidence: {exc}")
    else:
        if CANONICAL_LINEAGE_PR_COMMAND not in workflow_text:
            errors.append(
                "PR workflow omits append-only canonical lineage validation with base ref"
            )
    return True, errors


def expected_historical_replay_external_errors(
    *,
    repository_root: Path = ROOT,
) -> tuple[list[str], list[str]]:
    contract_rows = read_csv_rows(repository_root / EXTERNAL_SOURCE_CONTRACT_PATH)
    freshness_rows = read_csv_rows(repository_root / FRESHNESS_RELATIVE_PATH)
    if len(freshness_rows) != 1:
        return [], [
            "PR-safe advanced-integrity freshness input must contain exactly one row; "
            f"observed={len(freshness_rows)}"
        ]

    rows_by_source = {
        row.get("source_id", "").strip(): row
        for row in contract_rows
        if row.get("source_id", "").strip()
    }
    freshness = freshness_rows[0]
    main_date = freshness.get("main_price_date", "").strip()
    expected: list[str] = []
    contract_errors: list[str] = []

    for source_id, (expected_date_column, expected_readiness_column) in (
        EXPECTED_REPLAY_SOURCE_COLUMNS.items()
    ):
        row = rows_by_source.get(source_id)
        if row is None:
            contract_errors.append(
                f"historical-replay external source contract is missing {source_id}"
            )
            continue
        observed_date_column = row.get("freshness_date_column", "").strip()
        observed_readiness_column = row.get("readiness_column", "").strip()
        if observed_date_column != expected_date_column:
            contract_errors.append(
                f"historical-replay external source {source_id} freshness column drift: "
                f"expected={expected_date_column!r} observed={observed_date_column!r}"
            )
        if observed_readiness_column != expected_readiness_column:
            contract_errors.append(
                f"historical-replay external source {source_id} readiness column drift: "
                f"expected={expected_readiness_column!r} "
                f"observed={observed_readiness_column!r}"
            )
        if row.get("require_matches_main_price_date", "").strip() != "True":
            contract_errors.append(
                f"historical-replay external source {source_id} must require main-date parity"
            )
        if contract_errors:
            continue

        observed_date = freshness.get(expected_date_column, "").strip()
        if observed_date != main_date:
            if source_id not in ALLOWED_STALE_DATE_SOURCES:
                contract_errors.append(
                    f"historical-replay external source {source_id} cannot inherit a "
                    f"stale {expected_date_column}: observed={observed_date!r} "
                    f"main_price_date={main_date!r}"
                )
            elif not re.fullmatch(r"20\d{6}", observed_date) or observed_date >= main_date:
                contract_errors.append(
                    f"historical-replay external source {source_id} stale date must be a "
                    f"prior YYYYMMDD value: observed={observed_date!r} "
                    f"main_price_date={main_date!r}"
                )
            else:
                expected.append(
                    f"external source {source_id} date "
                    f"{expected_date_column}={observed_date} does not match "
                    f"main_price_date={main_date}"
                )

        readiness = freshness.get(expected_readiness_column, "").strip()
        if readiness != "True":
            expected.append(
                f"external source {source_id} readiness "
                f"{expected_readiness_column} is not True"
            )

    if not expected and not contract_errors:
        contract_errors.append(
            "historical-replay PR-safe path requires the strict external-source gate "
            "to report at least one inherited not-ready error"
        )
    return expected, contract_errors


def is_initial_pr_safe_gate_bootstrap(
    base_ref: str,
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> bool:
    if strict_surface_changes != PR_SAFE_BOOTSTRAP_SURFACES:
        return False
    helper_existed_at_base = git_path_exists_at_ref(
        base_ref,
        PR_SAFE_HELPER_PATH,
        repository_root=repository_root,
    )
    if helper_existed_at_base is not False:
        return False

    base_workflow = git_blob_at_ref(
        base_ref,
        PR_VALIDATION_WORKFLOW_PATH,
        repository_root=repository_root,
    )
    base_inventory = git_blob_at_ref(
        base_ref,
        PRODUCTION_INVENTORY_PATH,
        repository_root=repository_root,
    )
    try:
        current_helper = (repository_root / PR_SAFE_HELPER_PATH).read_bytes()
        current_workflow = (repository_root / PR_VALIDATION_WORKFLOW_PATH).read_bytes()
        current_inventory = (repository_root / PRODUCTION_INVENTORY_PATH).read_bytes()
    except OSError:
        return False
    if (
        not current_helper
        or base_workflow is None
        or base_inventory is None
    ):
        return False

    command = PR_SAFE_COMMAND.encode("utf-8")
    deselect = STRICT_RUNTIME_TEST_DESELECT.encode("utf-8")
    helper_path = PR_SAFE_HELPER_PATH.encode("utf-8")
    return bool(
        command not in base_workflow
        and command in current_workflow
        and deselect not in base_workflow
        and deselect in current_workflow
        and helper_path not in base_inventory
        and helper_path in current_inventory
    )


def validate_pr_safe_advanced_integrity_contract(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
) -> list[str]:
    changed_paths, git_errors = changed_paths_from_base(
        base_ref,
        repository_root=repository_root,
    )
    if git_errors:
        return git_errors

    static_errors = strict_validator.validate(include_external_sources=False)
    if static_errors:
        return [
            "PR-safe advanced-integrity validation cannot bypass static contract failures",
            *static_errors,
        ]

    external_errors = strict_validator.validate_external_source_contract()
    if not external_errors:
        return []

    strict_surface_changes = {
        path
        for path in changed_paths
        if requires_strict_runtime_validation(
            path,
            repository_root=repository_root,
        )
    }
    if is_initial_pr_safe_gate_bootstrap(
        base_ref,
        strict_surface_changes,
        repository_root=repository_root,
    ):
        strict_surface_changes = set()
    elif is_registered_source_identity_gate_self_update(
        base_ref,
        changed_paths,
        strict_surface_changes,
        repository_root=repository_root,
    ):
        strict_surface_changes = set()
    elif strict_surface_changes:
        is_source_identity_migration, migration_errors = (
            validate_registered_source_identity_migration(
                base_ref,
                changed_paths,
                strict_surface_changes,
                repository_root=repository_root,
            )
        )
        if is_source_identity_migration:
            if migration_errors:
                return [
                    "registered source-identity migration evidence is incomplete; "
                    "full runtime repo advanced-integrity validation remains required",
                    *migration_errors,
                    *external_errors,
                ]
            strict_surface_changes = set()
    if strict_surface_changes:
        return [
            "full runtime repo advanced-integrity validation is required because the PR "
            "changes protected external-source/readiness surface(s): "
            + ", ".join(sorted(strict_surface_changes)),
            *external_errors,
        ]

    marker_errors = validate_historical_replay_not_ready_marker(
        repository_root / FRESHNESS_RELATIVE_PATH
    )
    base_errors = validate_freshness_is_inherited_from_base(
        base_ref,
        repository_root=repository_root,
    )
    expected_errors, expected_contract_errors = (
        expected_historical_replay_external_errors(repository_root=repository_root)
    )
    if marker_errors or base_errors or expected_contract_errors:
        return [*marker_errors, *base_errors, *expected_contract_errors]
    if sorted(external_errors) != sorted(expected_errors):
        return [
            "PR-safe advanced-integrity validation may inherit only the exact external "
            "source errors caused by the legal historical-replay not-ready state",
            *external_errors,
        ]
    return []


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate repository advanced integrity in PR context without treating an "
            "unchanged legal historical-replay not-ready base as a PR regression"
        )
    )
    parser.add_argument("--base-ref", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_pr_safe_advanced_integrity_contract(args.base_ref)
    if errors:
        print("ERROR: PR-safe repo advanced-integrity validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "PR-safe repo advanced-integrity validation passed; "
        f"base_ref={args.base_ref}; strict production validator remains fail closed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
