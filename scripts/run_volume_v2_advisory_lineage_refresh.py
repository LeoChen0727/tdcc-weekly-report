from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
CONFIRMATION_TOKEN = "refresh_volume_v2_advisory_lineage"
OFFICIAL_WORKFLOW_PATH = ".github/workflows/volume_v2_advisory_lineage_refresh.yml"
OFFICIAL_REPOSITORY = "LeoChen0727/tdcc-weekly-report"
METADATA_ONLY_PATHS = (
    "output/latest/volume_breakout_watch_latest.md",
    "output/latest/volume_breakout_chatgpt_packet_latest.md",
    "output/latest/volume_attack_theme_layer_validation_latest.json",
    "output/latest/volume_attack_theme_layer_validation_latest.md",
)


class VolumeV2AdvisoryRefreshError(RuntimeError):
    pass


def _run(
    args: Sequence[str],
    *,
    root: Path,
    capture_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=str(root),
        check=False,
        capture_output=capture_output,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _require_command(
    args: Sequence[str],
    *,
    root: Path,
    label: str,
) -> str:
    proc = _run(args, root=root)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    if proc.returncode != 0:
        raise VolumeV2AdvisoryRefreshError(
            f"{label} failed with exit code {proc.returncode}"
        )
    return proc.stdout


def _git(root: Path, *args: str) -> str:
    proc = _run(("git", *args), root=root)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "git command failed").strip()
        raise VolumeV2AdvisoryRefreshError(detail)
    return proc.stdout


def validate_official_context(*, base_sha: str, root: Path) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", base_sha) is None:
        raise VolumeV2AdvisoryRefreshError("base SHA must be an exact lowercase commit SHA")
    expected_environment = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF_NAME": "main",
        "GITHUB_REPOSITORY": OFFICIAL_REPOSITORY,
        "VOLUME_V2_ADVISORY_REFRESH_CONFIRMATION": CONFIRMATION_TOKEN,
    }
    for name, expected in expected_environment.items():
        observed = os.environ.get(name, "")
        if observed != expected:
            raise VolumeV2AdvisoryRefreshError(
                f"official refresh environment mismatch: {name}={observed!r}"
            )
    workflow_ref = os.environ.get("GITHUB_WORKFLOW_REF", "").replace("\\", "/")
    expected_workflow_ref = (
        f"{OFFICIAL_REPOSITORY}/{OFFICIAL_WORKFLOW_PATH}@refs/heads/main"
    )
    if workflow_ref != expected_workflow_ref:
        raise VolumeV2AdvisoryRefreshError("official workflow ref is not the registered refresh workflow")

    head_sha = _git(root, "rev-parse", "HEAD").strip()
    if head_sha != base_sha:
        raise VolumeV2AdvisoryRefreshError(
            f"HEAD/base mismatch before refresh: head={head_sha} base={base_sha}"
        )
    event_sha = os.environ.get("GITHUB_SHA", "")
    if event_sha != base_sha:
        raise VolumeV2AdvisoryRefreshError(
            f"event/base mismatch before refresh: event={event_sha} base={base_sha}"
        )
    branch = _git(root, "branch", "--show-current").strip()
    if branch != "main":
        raise VolumeV2AdvisoryRefreshError(
            f"official refresh must run on checked-out main: observed={branch!r}"
        )
    if _git(root, "status", "--porcelain=v1"):
        raise VolumeV2AdvisoryRefreshError("official refresh checkout must start clean")


def run_refresh(*, base_sha: str, root: Path, python_executable: str) -> None:
    validate_official_context(base_sha=base_sha, root=root)
    commands = (
        (
            (python_executable, "-B", "scripts/build_volume_breakout_watch.py", "--latest-only"),
            "build latest-only volume breakout watch",
        ),
        (
            (python_executable, "-B", "scripts/validate_volume_breakout_watch.py", "--latest-only"),
            "validate refreshed volume breakout watch",
        ),
        (
            (python_executable, "-B", "scripts/build_volume_attack_theme_layer.py"),
            "build dependent volume attack theme layer",
        ),
        (
            (
                python_executable,
                "-B",
                "scripts/validate_volume_v2_advisory_lineage_refresh.py",
                "--repo-root",
                ".",
                "--base-sha",
                base_sha,
                "--phase",
                "post-build",
            ),
            "validate temporary refresh surface and business parity",
        ),
    )
    for command, label in commands:
        _require_command(command, root=root, label=label)

    _require_command(
        (
            "git",
            "restore",
            f"--source={base_sha}",
            "--worktree",
            "--",
            *METADATA_ONLY_PATHS,
        ),
        root=root,
        label="restore metadata-only artifacts",
    )
    _require_command(
        (
            python_executable,
            "-B",
            "scripts/validate_volume_v2_advisory_lineage_refresh.py",
            "--repo-root",
            ".",
            "--base-sha",
            base_sha,
            "--phase",
            "final",
        ),
        root=root,
        label="validate final refresh surface",
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the bounded official Volume V2 advisory lineage refresh."
    )
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--repo-root", default=str(ROOT))
    parser.add_argument("--python-executable", default=sys.executable)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    try:
        run_refresh(
            base_sha=args.base_sha,
            root=Path(args.repo_root).resolve(),
            python_executable=args.python_executable,
        )
    except VolumeV2AdvisoryRefreshError as exc:
        print(f"ERROR: {exc}")
        return 1
    print("Volume V2 advisory lineage refresh completed with bounded local changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
