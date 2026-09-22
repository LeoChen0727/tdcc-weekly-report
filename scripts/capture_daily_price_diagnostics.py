"""Capture current-attempt diagnostics without changing producer exit semantics."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


DIAGNOSTIC_PATHS = (
    "output/latest/official_price_fetch_latest.json",
    "output/latest/official_price_fetch_latest.md",
    "output/debug/official_price_fetch_debug_latest.md",
    "output/latest/daily_price_source_recovery_latest.json",
    "output/latest/daily_price_source_recovery_latest.md",
    "output/latest/repair_daily_price_range_latest.json",
    "output/latest/repair_daily_price_range_latest.csv",
    "output/latest/repair_daily_price_range_latest.md",
    "output/latest/repair_daily_price_range_check_code_latest.csv",
)


def signature(path: Path) -> dict[str, object] | None:
    try:
        payload = path.read_bytes()
        stat = path.stat()
    except FileNotFoundError:
        return None
    return {
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "mtime_ns": stat.st_mtime_ns,
    }


def capture(root: Path, evidence_root: Path, attempt: str, command: list[str]) -> int:
    destination = evidence_root / attempt
    destination.mkdir(parents=True, exist_ok=False)
    before = {name: signature(root / name) for name in DIAGNOSTIC_PATHS}
    evidence = {
        "attempt": attempt,
        "github_run_id": os.environ.get("GITHUB_RUN_ID", ""),
        "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", ""),
        "source_sha": os.environ.get("GITHUB_SHA", ""),
        "expected_main_price_date": os.environ.get("EXPECTED_MAIN_PRICE_DATE", ""),
        "started_at": datetime.now(timezone.utc).isoformat(),
        "command": command,
        "exit_code": None,
    }
    metadata = destination / "attempt.json"
    metadata.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    log_path = destination / "command.log"
    exit_code = 1
    with log_path.open("w", encoding="utf-8") as log:
        try:
            exit_code = subprocess.run(
                command, cwd=root, stdout=log, stderr=subprocess.STDOUT, check=False,
            ).returncode
        except OSError as exc:
            log.write(f"Cannot execute diagnostic command: {exc}\n")
    print(log_path.read_text(encoding="utf-8", errors="replace"), end="")
    # Unchanged checked-out reports are not evidence of this run. A crash/timeout
    # leaves exit_code=null plus the current command log, never a false success.
    try:
        files = {}
        for name in DIAGNOSTIC_PATHS:
            observed = signature(root / name)
            written = observed is not None and observed != before[name]
            files[name] = {"written_this_attempt": written, "observed": observed}
            if written:
                target = destination / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((root / name).read_bytes())
        evidence.update(exit_code=exit_code, files=files)
        metadata.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    except OSError as exc:
        print(f"::warning::Cannot finish price diagnostic snapshot: {exc}")
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--attempt", required=True,
        choices=("initial-fetch", "recovery-fetch", "missing-file-repair"),
    )
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a producer command is required")
    return capture(
        Path.cwd(), Path(os.environ["RUNNER_TEMP"]) / "daily-price-source-recovery",
        args.attempt, command,
    )


if __name__ == "__main__":
    sys.exit(main())
