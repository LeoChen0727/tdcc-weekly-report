from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_PREFIXES = (
    "data/theme_events/",
    "data/company_calendar/",
    "data/macro_events/",
    "data/fundamental_catalysts/",
    "data/event_catalysts/",
    "output/history/event_catalyst_recovery/",
)

SOURCE_LATEST_ARTIFACTS = (
    "upcoming_catalyst_calendar_latest.csv",
    "upcoming_catalyst_calendar_latest.md",
    "upcoming_macro_event_calendar_latest.csv",
    "upcoming_macro_event_calendar_latest.md",
    "calendar_data_source_status_latest.json",
    "calendar_data_source_status_latest.md",
    "catalyst_data_source_status_latest.json",
    "catalyst_data_source_status_latest.md",
    "catalyst_needs_review_latest.csv",
    "catalyst_needs_review_latest.md",
    "event_calendar_validation_latest.json",
    "event_calendar_validation_latest.md",
    "catalyst_layer_validation_latest.json",
    "catalyst_layer_validation_latest.md",
    "event_catalyst_historical_recovery_latest.json",
    "event_catalyst_historical_recovery_latest.md",
)

ALLOWED_EXACT_PATHS = {
    *(f"output/latest/{name}" for name in SOURCE_LATEST_ARTIFACTS),
    *(f"docs/latest/{name}" for name in SOURCE_LATEST_ARTIFACTS),
}

FORBIDDEN_BUSINESS_TOKENS = (
    "daily_candidate",
    "daily_model",
    "model_snapshot",
    "ranking",
    "all_candidates",
    "tdcc_",
    "chatgpt_side_outputs",
    "research_backtest",
)


def staged_paths(root: Path = ROOT) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [
        line.strip().replace("\\", "/")
        for line in result.stdout.splitlines()
        if line.strip()
    ]


def validate_paths(paths: list[str]) -> list[str]:
    errors: list[str] = []
    for raw_path in paths:
        path = raw_path.replace("\\", "/")
        if path in ALLOWED_EXACT_PATHS or path.startswith(ALLOWED_PREFIXES):
            continue
        errors.append(f"path is outside event/catalyst source refresh scope: {path}")
    for path in paths:
        normalized = path.replace("\\", "/").lower()
        if any(token in normalized for token in FORBIDDEN_BUSINESS_TOKENS):
            errors.append(f"model/ranking or cross-lane path is forbidden: {path}")
    return errors


def index_bytes(root: Path, relative_path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f":{relative_path}"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    return result.stdout if result.returncode == 0 else None


def validate_staged_mirrors(root: Path, paths: list[str]) -> list[str]:
    errors: list[str] = []
    staged = set(paths)
    for name in SOURCE_LATEST_ARTIFACTS:
        output_path = f"output/latest/{name}"
        docs_path = f"docs/latest/{name}"
        if output_path not in staged and docs_path not in staged:
            continue
        output_bytes = index_bytes(root, output_path)
        docs_bytes = index_bytes(root, docs_path)
        if output_bytes is None or docs_bytes is None or output_bytes != docs_bytes:
            errors.append(f"output/docs staged mirror differs: {name}")
    return errors


def main() -> int:
    paths = staged_paths(ROOT)
    errors = validate_paths(paths)
    errors.extend(validate_staged_mirrors(ROOT, paths))
    if errors:
        print("ERROR: event/catalyst source refresh staged-path validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("event/catalyst source refresh staged-path validation passed")
    print(f"staged_path_count={len(paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
