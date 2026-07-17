from __future__ import annotations

import subprocess
from pathlib import Path

try:
    from validate_daily_staged_paths import registered_mirror_files
except ModuleNotFoundError:
    from scripts.validate_daily_staged_paths import registered_mirror_files


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"


def collect_mirror_paths() -> tuple[list[str], list[str]]:
    paths: list[str] = []
    errors: list[str] = []
    for name in registered_mirror_files():
        output_path = LATEST_DIR / name
        docs_path = DOCS_LATEST_DIR / name
        if not output_path.exists() and not docs_path.exists():
            errors.append(f"missing registered mirror pair: output/latest/{name}")
            continue
        if not output_path.exists():
            errors.append(f"missing registered output mirror source: output/latest/{name}")
            continue
        if not docs_path.exists():
            errors.append(f"missing registered docs mirror: docs/latest/{name}")
            continue
        if output_path.read_bytes() != docs_path.read_bytes():
            errors.append(f"registered mirror bytes differ: docs/latest/{name}")
            continue
        paths.extend(
            [
                output_path.relative_to(ROOT).as_posix(),
                docs_path.relative_to(ROOT).as_posix(),
            ]
        )
    return paths, errors


def main() -> int:
    paths, errors = collect_mirror_paths()
    if errors:
        print("ERROR: daily latest mirror registry staging preflight failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if paths:
        result = subprocess.run(
            ["git", "add", "--", *paths],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print("ERROR: failed to stage daily latest mirror registry")
            if result.stdout.strip():
                print(result.stdout.strip())
            if result.stderr.strip():
                print(result.stderr.strip())
            return result.returncode

    print(
        "daily latest mirror registry staging passed: "
        f"registered={len(registered_mirror_files())} staged_pairs={len(paths) // 2}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
