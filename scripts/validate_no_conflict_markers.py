from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess


CONFLICT_MARKER_RE = re.compile(r"^(<<<<<<< .+|=======|>>>>>>> .+)$")
DEFAULT_PATHS = [
    "data/theme_events",
    "data/company_calendar",
    "data/macro_events",
    "data/fundamental_catalysts",
    "data/event_catalysts",
    "output/latest",
    "docs/latest",
]


def tracked_files(paths: list[str]) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--", *paths],
        check=True,
        text=True,
        capture_output=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line.strip()]


def has_binary_marker(data: bytes) -> bool:
    return b"\x00" in data


def scan_file(path: Path) -> list[str]:
    data = path.read_bytes()
    if has_binary_marker(data):
        return []
    text = data.decode("utf-8", errors="ignore")
    issues: list[str] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if CONFLICT_MARKER_RE.match(line):
            issues.append(f"{path.as_posix()}:{line_no}:{line}")
    return issues


def validate(paths: list[str]) -> list[str]:
    issues: list[str] = []
    for path in tracked_files(paths):
        if path.exists():
            issues.extend(scan_file(path))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", default=DEFAULT_PATHS)
    args = parser.parse_args()

    issues = validate(args.paths)
    if issues:
        print("ERROR: conflict markers detected")
        for issue in issues:
            print(issue)
        return 1
    print("no conflict markers detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
