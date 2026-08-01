from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_daily_published_model_snapshots import (  # noqa: E402
    ARTIFACTS,
    validate_current_report_snapshots,
)


ROOT = Path(__file__).resolve().parents[1]
FRESHNESS_RELATIVE_PATH = "output/latest/data_freshness_latest.csv"
PR_SAFE_HELPER_PATH = "scripts/validate_daily_published_model_snapshots_pr_safe.py"
PR_VALIDATION_WORKFLOW_PATH = (
    ".github/workflows/daily_model_maintenance_pr_validation.yml"
)
PR_BOUNDARY_VALIDATOR_PATH = "scripts/validate_daily_production_boundaries.py"
STRICT_SNAPSHOT_COMMAND = "python scripts/validate_daily_published_model_snapshots.py"
PR_SAFE_SNAPSHOT_COMMAND = (
    'python scripts/validate_daily_published_model_snapshots_pr_safe.py --base-ref "$BASE_SHA"'
)
PR_SAFE_BOOTSTRAP_SURFACES = frozenset(
    {
        PR_SAFE_HELPER_PATH,
        PR_VALIDATION_WORKFLOW_PATH,
        PR_BOUNDARY_VALIDATOR_PATH,
    }
)

EXPECTED_STRICT_NOT_READY_ERROR = (
    "report_ready must be True before publishing model snapshots; observed=False"
)
HISTORICAL_REPLAY_REPORT_READY_NOTE = (
    "historical structured-source replay updates objective-source freshness only; "
    "publish artifacts remain stale"
)
HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE = (
    "historical structured-source replay must not mark stale daily PDFs ready"
)

# These files can change publication readiness, immutable snapshot identity, or
# a production publisher. A PR touching any of them must pass the original full
# runtime validator. The PR-only wrapper and its workflow are control-plane
# surfaces covered by dedicated regression tests; they do not publish artifacts.
STRICT_EXACT_PATHS = frozenset(
    {
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/historical_structured_source_replay.yml",
        PR_VALIDATION_WORKFLOW_PATH,
        ".github/workflows/warrant_flow.yml",
        ".github/workflows/weekly_theme_review.yml",
        "build_data_freshness_latest.py",
        "docs/latest/data_freshness_latest.csv",
        "docs/latest/data_freshness_latest.md",
        FRESHNESS_RELATIVE_PATH,
        "output/latest/data_freshness_latest.md",
        "scripts/backfill_historical_all_candidates_snapshots_from_git_history.py",
        "scripts/daily_snapshot_revision_utils.py",
        "scripts/replay_historical_structured_sources.py",
        "scripts/stage_daily_published_snapshot_revisions.py",
        "scripts/update_daily_published_model_snapshots.py",
        PR_BOUNDARY_VALIDATOR_PATH,
        "scripts/validate_daily_published_model_snapshots.py",
        PR_SAFE_HELPER_PATH,
        *(f"output/latest/{artifact.source_name}" for artifact in ARTIFACTS),
    }
)
STRICT_PATH_PREFIXES = ("output/history/daily_model_snapshots/",)


def safe_str(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    return str(value).strip()


def normalize_repository_path(path: str) -> str:
    normalized = str(path).replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def requires_strict_runtime_validation(path: str) -> bool:
    normalized = normalize_repository_path(path)
    return normalized in STRICT_EXACT_PATHS or normalized.startswith(
        STRICT_PATH_PREFIXES
    )


def changed_paths_from_base(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
) -> tuple[set[str], list[str]]:
    if not safe_str(base_ref):
        return set(), ["PR-safe snapshot validation requires a non-empty base ref"]
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
        return set(), [f"cannot inspect PR changed paths from base_ref={base_ref}: {exc}"]
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


def validate_historical_replay_not_ready_marker(
    freshness_path: Path,
) -> list[str]:
    try:
        freshness = pd.read_csv(freshness_path, dtype=str).fillna("")
    except Exception as exc:
        return [f"cannot read historical-replay freshness marker: {exc}"]
    if len(freshness) != 1:
        return [
            "historical-replay freshness marker must contain exactly one row; "
            f"observed={len(freshness)}"
        ]

    row = freshness.iloc[0]
    expected_values = {
        "main_price_date_source": "historical_replay_override",
        "report_ready": "False",
        "daily_pdf_ready": "False",
        "report_ready_note": HISTORICAL_REPLAY_REPORT_READY_NOTE,
        "daily_pdf_ready_note": HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE,
    }
    errors = [
        f"historical-replay freshness marker {column} mismatch: "
        f"expected={expected!r} observed={safe_str(row.get(column, ''))!r}"
        for column, expected in expected_values.items()
        if safe_str(row.get(column, "")) != expected
    ]

    main_price_date = safe_str(row.get("main_price_date", ""))
    replay_date = safe_str(row.get("historical_replay_main_price_date", ""))
    expected_high_water = safe_str(
        row.get("expected_price_history_high_water_date", "")
    )
    actual_high_water = safe_str(row.get("actual_stock_price_history_date", ""))
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
    try:
        proc = subprocess.run(
            ["git", "show", f"{base_ref}:{FRESHNESS_RELATIVE_PATH}"],
            cwd=repository_root,
            capture_output=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [
            f"cannot read base freshness artifact from {base_ref}: "
            f"{FRESHNESS_RELATIVE_PATH}: {exc}"
        ]
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", errors="replace").strip()
        return [
            f"cannot read base freshness artifact from {base_ref}: "
            f"{FRESHNESS_RELATIVE_PATH}: {detail or 'git show failed'}"
        ]
    if proc.stdout != current_payload:
        return [
            "PR-safe snapshot validation cannot inherit a changed freshness artifact; "
            f"{FRESHNESS_RELATIVE_PATH} differs from base_ref={base_ref}"
        ]
    return []


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


def is_initial_pr_safe_gate_bootstrap(
    base_ref: str,
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> bool:
    """Allow only the one-time migration from the old unconditional PR command."""

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
    try:
        current_workflow = (repository_root / PR_VALIDATION_WORKFLOW_PATH).read_bytes()
        current_boundary = (repository_root / PR_BOUNDARY_VALIDATOR_PATH).read_bytes()
        current_helper = (repository_root / PR_SAFE_HELPER_PATH).read_bytes()
    except OSError:
        return False
    if not current_helper or base_workflow is None or base_boundary is None:
        return False

    strict_command = STRICT_SNAPSHOT_COMMAND.encode("utf-8")
    pr_safe_command = PR_SAFE_SNAPSHOT_COMMAND.encode("utf-8")
    return bool(
        strict_command in base_workflow
        and pr_safe_command not in base_workflow
        and pr_safe_command in current_workflow
        and strict_command not in current_workflow
        and strict_command in base_boundary
        and pr_safe_command not in base_boundary
        and pr_safe_command in current_boundary
    )


def validate_pr_safe_snapshot_contract(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
    latest_dir: Path | None = None,
) -> list[str]:
    changed_paths, git_errors = changed_paths_from_base(
        base_ref,
        repository_root=repository_root,
    )
    if git_errors:
        return git_errors

    strict_surface_changes = {
        path for path in changed_paths if requires_strict_runtime_validation(path)
    }
    if is_initial_pr_safe_gate_bootstrap(
        base_ref,
        strict_surface_changes,
        repository_root=repository_root,
    ):
        strict_surface_changes = set()
    effective_latest_dir = latest_dir or repository_root / "output" / "latest"
    strict_errors = validate_current_report_snapshots(
        latest_dir=effective_latest_dir,
        snapshot_dir=repository_root / "output" / "history" / "daily_model_snapshots",
        manifest_path=(
            repository_root
            / "output"
            / "history"
            / "daily_model_snapshots"
            / "daily_published_model_snapshot_manifest.csv"
        ),
    )
    if not strict_errors:
        return []
    if strict_surface_changes:
        return [
            "full runtime daily published model snapshot validation is required because "
            "the PR changes protected snapshot surface(s): "
            + ", ".join(sorted(strict_surface_changes)),
            *strict_errors,
        ]
    if strict_errors != [EXPECTED_STRICT_NOT_READY_ERROR]:
        return [
            "PR-safe snapshot validation may inherit only the exact legal historical-replay "
            "report_ready=False state; the strict validator reported other failures",
            *strict_errors,
        ]

    marker_errors = validate_historical_replay_not_ready_marker(
        effective_latest_dir / "data_freshness_latest.csv"
    )
    base_errors = validate_freshness_is_inherited_from_base(
        base_ref,
        repository_root=repository_root,
    )
    return [*marker_errors, *base_errors]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate daily published snapshots in PR context without treating an unchanged "
            "legal historical-replay not-ready base artifact as a PR regression"
        )
    )
    parser.add_argument("--base-ref", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_pr_safe_snapshot_contract(args.base_ref)
    if errors:
        print("ERROR: PR-safe daily published model snapshot validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "PR-safe daily published model snapshot validation passed; "
        f"base_ref={args.base_ref}; strict publish validator remains fail closed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
