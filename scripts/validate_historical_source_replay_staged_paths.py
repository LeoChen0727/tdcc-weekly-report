from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_PATTERNS = [
    r"data/daily_price/(?:daily_price_)?20\d{6}\.csv",
    r"data/stock_price_history/[^/]+\.csv",
    r"data/market_index(?:_ohlc)?_history\.csv",
    r"data/futures_options/(?:raw/)?[^/]+\.(?:csv|json)",
    r"output/history/warrant_daily/warrant_daily_20\d{6}\.csv",
    r"output/history/warrant_flow/warrant_flow_20\d{6}\.csv",
    r"output/history/historical_source_replay/[a-zA-Z0-9._-]+/20\d{6}/[^/]+\.json",
    r"output/latest/(?:official_daily_price_latest\.csv|official_price_fetch_latest\.(?:json|md))",
    r"output/latest/(?:market_index_source_status_latest\.(?:json|md)|market_benchmark_latest\.csv)",
    r"output/latest/futures_options_[^/]+\.(?:csv|json|md)",
    r"output/latest/taiwan_vix_latest\.csv",
    r"output/latest/warrant_(?:daily_raw|source_status)_latest\.(?:csv|json|md)",
    r"output/latest/warrant_daily_fetch_latest\.md",
    r"output/latest/warrant_flow_latest\.(?:csv|md)",
    r"output/latest/volume_attack_theme_(?:layer|stocks)_latest\.(?:csv|md)",
    r"output/latest/volume_attack_theme_layer_validation_latest\.(?:json|md)",
    r"output/latest/stock_price_history_manifest\.(?:csv|json|md)",
    r"output/latest/daily_price_history_continuity_latest\.(?:csv|json|md)",
    r"output/latest/data_freshness_latest\.(?:csv|md)",
    r"output/latest/historical_structured_source_replay_latest\.(?:json|md)",
    r"output/debug/warrant_fetch_debug_latest\.(?:csv|md)",
    r"docs/latest/stock_price_history_manifest\.(?:csv|json|md)",
    r"docs/latest/volume_attack_theme_(?:layer|stocks)_latest\.(?:csv|md)",
]

PRESERVE_PRICE_HISTORY_FORBIDDEN_PATTERNS = [
    r"data/daily_price/.+",
    r"data/stock_price_history/.+",
    r"output/latest/stock_price_history_manifest\.(?:csv|json|md)",
    r"docs/latest/stock_price_history_manifest\.(?:csv|json|md)",
]

FORBIDDEN_TOKENS = (
    "candidate",
    "daily_model",
    "model_snapshot",
    "event",
    "catalyst",
    ".pdf",
    "chatgpt_side_outputs",
    "published_reports",
)


ALLOWED_STATUSES = {"A", "C", "M"}


def _parse_name_status_z(raw: str) -> list[tuple[str, str]]:
    tokens = raw.split("\0")
    if tokens and not tokens[-1]:
        tokens.pop()
    changes: list[tuple[str, str]] = []
    index = 0
    while index < len(tokens):
        status = tokens[index].strip()
        index += 1
        if not status:
            continue
        path_count = 2 if status[:1] in {"C", "R"} else 1
        if index + path_count > len(tokens):
            raise RuntimeError(f"malformed git name-status record for status {status}")
        for path in tokens[index : index + path_count]:
            changes.append((status, path.replace("\\", "/")))
        index += path_count
    return changes


def _git_name_status(*args: str) -> list[tuple[str, str]]:
    completed = subprocess.run(
        ["git", *args, "--name-status", "-z"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "git path-state query failed")
    return _parse_name_status_z(completed.stdout)


def staged_changes() -> list[tuple[str, str]]:
    # Do not apply a diff filter here. Every Git status must be observed and
    # rejected unless it is explicitly in ALLOWED_STATUSES.
    return _git_name_status("diff", "--cached")


def unstaged_changes() -> list[tuple[str, str]]:
    return _git_name_status("diff")


def untracked_paths() -> list[str]:
    completed = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "git untracked-path query failed")
    return [path.replace("\\", "/") for path in completed.stdout.split("\0") if path]


def staged_paths() -> list[str]:
    return [path for _, path in staged_changes()]


def validate(
    paths: list[str],
    *,
    deleted_paths: list[str] | None = None,
    price_history_high_water_date: str = "",
) -> list[str]:
    errors: list[str] = []
    for path in deleted_paths or []:
        errors.append(f"historical source replay staged deletion is forbidden: {path}")
    for path in paths:
        if price_history_high_water_date and any(
            re.fullmatch(pattern, path)
            for pattern in PRESERVE_PRICE_HISTORY_FORBIDDEN_PATTERNS
        ):
            errors.append(
                "historical source replay preserve mode forbids protected price/history path: "
                f"{path}"
            )
            continue
        lower = path.lower()
        if any(token in lower for token in FORBIDDEN_TOKENS):
            errors.append(f"historical source replay staged forbidden artifact: {path}")
            continue
        if not any(re.fullmatch(pattern, path) for pattern in ALLOWED_PATTERNS):
            errors.append(f"historical source replay staged path is not allowlisted: {path}")
    return errors


def validate_changes(
    changes: list[tuple[str, str]],
    *,
    scope: str,
    price_history_high_water_date: str = "",
) -> list[str]:
    errors: list[str] = []
    paths: list[str] = []
    for status, path in changes:
        status_family = status[:1]
        if status_family not in ALLOWED_STATUSES:
            errors.append(
                f"historical source replay {scope} status is forbidden: {status} {path}"
            )
        paths.append(path)
    errors.extend(
        validate(
            paths,
            price_history_high_water_date=price_history_high_water_date,
        )
    )
    return errors


def validate_repository_state(
    staged: list[tuple[str, str]],
    unstaged: list[tuple[str, str]],
    untracked: list[str],
    *,
    price_history_high_water_date: str = "",
) -> list[str]:
    errors = validate_changes(
        staged,
        scope="staged",
        price_history_high_water_date=price_history_high_water_date,
    )
    for status, path in unstaged:
        errors.append(
            "historical source replay has an unstaged worktree change; "
            f"all worktree changes must equal the staged set: {status} {path}"
        )
    for path in untracked:
        errors.append(
            "historical source replay has an untracked worktree path; "
            f"all worktree changes must equal the staged set: {path}"
        )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--price-history-high-water-date", default="")
    parser.add_argument("paths", nargs="*")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    price_history_high_water_date = str(args.price_history_high_water_date or "").strip()
    if price_history_high_water_date:
        if not re.fullmatch(r"20\d{6}", price_history_high_water_date):
            raise RuntimeError("--price-history-high-water-date must be YYYYMMDD")
        try:
            datetime.strptime(price_history_high_water_date, "%Y%m%d")
        except ValueError as exc:
            raise RuntimeError(
                "--price-history-high-water-date must be calendar-valid"
            ) from exc
    if args.paths:
        paths = args.paths
        errors = validate(
            paths,
            price_history_high_water_date=price_history_high_water_date,
        )
    else:
        changes = staged_changes()
        paths = [path for _, path in changes]
        errors = validate_repository_state(
            changes,
            unstaged_changes(),
            untracked_paths(),
            price_history_high_water_date=price_history_high_water_date,
        )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"historical source replay staged paths validated: {len(paths)} paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
