from __future__ import annotations

import argparse
import csv
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

PR_SAFE_BOOTSTRAP_SURFACES = frozenset(
    {
        PR_SAFE_HELPER_PATH,
        PR_VALIDATION_WORKFLOW_PATH,
        PR_BOUNDARY_VALIDATOR_PATH,
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
    }
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


def requires_strict_runtime_validation(
    path: str,
    *,
    repository_root: Path = ROOT,
) -> bool:
    normalized = normalize_repository_path(path)
    return normalized in STRICT_EXACT_PATHS or normalized in external_source_surface_paths(
        repository_root
    )


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
    base_boundary = git_blob_at_ref(
        base_ref,
        PR_BOUNDARY_VALIDATOR_PATH,
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
        current_boundary = (repository_root / PR_BOUNDARY_VALIDATOR_PATH).read_bytes()
        current_inventory = (repository_root / PRODUCTION_INVENTORY_PATH).read_bytes()
    except OSError:
        return False
    if (
        not current_helper
        or base_workflow is None
        or base_boundary is None
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
        and command not in base_boundary
        and command in current_boundary
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
