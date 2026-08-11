from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_EXACT = {
    "output/latest/recent_daily_price_gap_repair_latest.json",
    "output/latest/recent_daily_price_gap_repair_latest.md",
    "output/latest/repair_daily_price_range_check_code_latest.csv",
    "output/latest/stock_price_history_manifest.csv",
    "output/latest/stock_price_history_manifest.json",
    "output/latest/stock_price_history_manifest.md",
    "output/latest/daily_price_history_continuity_latest.json",
    "output/latest/daily_price_history_continuity_latest.md",
    "docs/latest/stock_price_history_manifest.csv",
    "docs/latest/stock_price_history_manifest.json",
    "docs/latest/stock_price_history_manifest.md",
}
ALLOWED_PATTERNS = (
    re.compile(r"^data/daily_price/(?:daily_price_)?20\d{6}\.csv$"),
    re.compile(r"^data/stock_price_history/[0-9A-Za-z_-]+\.csv$"),
    re.compile(r"^output/latest/repair_daily_price_range_latest\.(?:csv|json|md)$"),
)


def _is_allowed(path: str) -> bool:
    return path in ALLOWED_EXACT or any(pattern.fullmatch(path) for pattern in ALLOWED_PATTERNS)


def validate_entries(entries: list[tuple[str, tuple[str, ...]]]) -> list[str]:
    errors: list[str] = []
    if not entries:
        return ["recent daily-price repair has no staged paths to validate"]
    for status, paths in entries:
        if status not in {"A", "M"}:
            errors.append(
                "recent daily-price repair staged change must be add/modify only: "
                f"status={status} paths={list(paths)}"
            )
            continue
        if len(paths) != 1:
            errors.append(
                "recent daily-price repair staged change has unexpected path arity: "
                f"status={status} paths={list(paths)}"
            )
            continue
        path = paths[0].replace("\\", "/")
        if not _is_allowed(path):
            errors.append(f"recent daily-price repair staged path is not allowed: {path}")
    return errors


def staged_entries() -> list[tuple[str, tuple[str, ...]]]:
    raw = subprocess.check_output(
        ["git", "diff", "--cached", "--name-status", "-z"],
        cwd=ROOT,
    )
    tokens = raw.decode("utf-8", errors="strict").split("\0")
    if tokens and tokens[-1] == "":
        tokens.pop()
    entries: list[tuple[str, tuple[str, ...]]] = []
    index = 0
    while index < len(tokens):
        status_token = tokens[index]
        index += 1
        status = status_token[:1]
        path_count = 2 if status in {"R", "C"} else 1
        if index + path_count > len(tokens):
            raise RuntimeError("malformed staged name-status output")
        paths = tuple(tokens[index : index + path_count])
        index += path_count
        entries.append((status, paths))
    return entries


def main() -> int:
    errors = validate_entries(staged_entries())
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] recent daily-price repair staged paths are data-only and add/modify only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
