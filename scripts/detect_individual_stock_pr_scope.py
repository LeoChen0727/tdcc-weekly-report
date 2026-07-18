from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

AFFECTED_EXACT_PATHS = frozenset(
    {
        ".github/workflows/current_holdings_pattern.yml",
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/individual_stock_data_refresh.yml",
        ".github/workflows/individual_stock_pr_validation.yml",
        ".github/workflows/individual_stock_report.yml",
        ".github/workflows/repair_daily_price_range.yml",
        ".github/workflows/repair_one_daily_price.yml",
        ".github/workflows/repair_recent_daily_price_gaps.yml",
        ".github/workflows/repair_tdcc_monthly_history_gaps.yml",
        ".github/workflows/research_backtest_pipeline.yml",
        ".github/workflows/tdcc_history_backfill.yml",
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/warrant_flow.yml",
        "config/repo_file_lifecycle_inventory.csv",
        "config/repo_production_inventory.csv",
        "docs/APPS_SCRIPT_WORKFLOW_TRIGGER.md",
        "scripts/detect_individual_stock_pr_scope.py",
        "scripts/individual_tdcc_dataset_consumer.py",
        "scripts/validate_individual_pdf_contract_consumers.py",
        "scripts/validate_repo_file_lifecycle_inventory.py",
        "scripts/validate_repo_production_inventory.py",
        "tests/test_individual_pdf_contract_consumers.py",
        "tests/test_individual_tdcc_dataset_consumer.py",
        "tests/test_individual_stock_pr_validation_workflow.py",
        "tests/test_repo_file_lifecycle_inventory.py",
        "tests/test_repo_production_inventory.py",
    }
)

AFFECTED_PATH_PREFIXES = (
    "config/individual_stock_",
    "docs/individual_stock_",
    "docs/latest/individual_stock_reports/",
    "output/history/individual_stock_reports/",
    "output/latest/individual_stock_reports/",
    "scripts/build_individual_stock_",
    "scripts/generate_individual_stock_",
    "scripts/validate_individual_stock_",
    "tests/test_individual_stock_",
)


def normalize_path(value: str) -> str:
    path = value.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def is_affected_path(value: str) -> bool:
    path = normalize_path(value)
    return path in AFFECTED_EXACT_PATHS or path.startswith(AFFECTED_PATH_PREFIXES)


def matched_affected_paths(paths: Iterable[str]) -> list[str]:
    return sorted({normalize_path(path) for path in paths if is_affected_path(path)})


def changed_paths_from_git(base_sha: str, head_sha: str) -> list[str]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-only",
            "--diff-filter=ACMRD",
            f"{base_sha}...{head_sha}",
            "--",
        ],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def write_github_output(path: Path, matched: list[str]) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(f"affected={'true' if matched else 'false'}\n")
        handle.write(f"matched_count={len(matched)}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Detect whether a pull request affects individual-stock contracts or "
            "production artifact-writer authentication."
        )
    )
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--github-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changed = changed_paths_from_git(args.base_sha, args.head_sha)
    matched = matched_affected_paths(changed)
    payload = {
        "affected": bool(matched),
        "changed_count": len(changed),
        "matched_count": len(matched),
        "matched_paths": matched,
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    if args.github_output:
        write_github_output(args.github_output, matched)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
