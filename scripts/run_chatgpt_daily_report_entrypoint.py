from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.resolve_daily_report_source_state import (  # noqa: E402
    DEFAULT_SOURCE_REF,
    DailyReportSourceError,
    resolve_daily_report_source_state,
)


GENERATOR = REPO_ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "chatgpt_side_outputs"


class DailyReportEntrypointError(RuntimeError):
    pass


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def run_command(
    args: list[str],
    cwd: Path,
    env: dict[str, str] | None = None,
    capture_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd),
        env=env,
        check=False,
        capture_output=capture_output,
        encoding="utf-8",
        errors="replace",
        text=True,
    )


def require_success(proc: subprocess.CompletedProcess[str], action: str) -> str:
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or f"{action} failed").strip()
        raise DailyReportEntrypointError(f"{action} failed: {detail}")
    return proc.stdout


def ensure_entrypoint_can_run(repo_root: Path, source_ref: str, allow_dirty_code: bool) -> dict:
    try:
        return resolve_daily_report_source_state(
            repo_root=repo_root,
            source_ref=source_ref,
            fetch=True,
            require_git_clean=True,
            allow_dirty=allow_dirty_code,
            require_local_match=False,
        )
    except DailyReportSourceError as exc:
        raise DailyReportEntrypointError("\n".join(exc.errors)) from exc


def add_source_worktree(repo_root: Path, source_ref: str, temp_root: Path) -> Path:
    temp_root.mkdir(parents=True, exist_ok=True)
    source_root = temp_root / "origin_main_daily_report_source"
    proc = run_command(
        ["git", "worktree", "add", "--detach", str(source_root), source_ref],
        cwd=repo_root,
    )
    require_success(proc, f"git worktree add --detach {source_root} {source_ref}")
    return source_root


def remove_source_worktree(repo_root: Path, source_root: Path) -> None:
    if not source_root.exists():
        return
    proc = run_command(
        ["git", "worktree", "remove", "--force", str(source_root)],
        cwd=repo_root,
    )
    if proc.returncode != 0:
        print(
            "WARNING: failed to remove temporary source worktree: "
            f"{(proc.stderr or proc.stdout).strip()}",
            file=sys.stderr,
        )


def run_generator(source_root: Path, output_dir: Path) -> list[Path]:
    env = os.environ.copy()
    env["CHATGPT_DAILY_REPORT_ENTRYPOINT"] = "1"
    env["CHATGPT_DAILY_REPO_ROOT"] = str(source_root)
    env["CHATGPT_DAILY_OUTPUT_DIR"] = str(output_dir)
    env["PYTHONIOENCODING"] = "utf-8"
    proc = run_command(
        [
            sys.executable,
            str(GENERATOR),
            "--repo-root",
            str(source_root),
            "--output-dir",
            str(output_dir),
        ],
        cwd=REPO_ROOT,
        env=env,
    )
    stdout = require_success(proc, "ChatGPT-side daily PDF generator")
    if proc.stderr.strip():
        print(proc.stderr.strip(), file=sys.stderr)
    paths: list[Path] = []
    for line in stdout.splitlines():
        text = line.strip()
        if text.lower().endswith(".pdf"):
            paths.append(Path(text).expanduser().resolve())
        if text:
            print(text)
    if len(paths) != 6:
        raise DailyReportEntrypointError(f"generator must emit exactly 6 PDF paths, got {len(paths)}")
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Only official entrypoint for generating the six ChatGPT-side daily PDFs. "
            "It gates on origin/main with git fetch + git show, creates a clean temporary "
            "source worktree, and then invokes the renderer."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--source-gate-only",
        action="store_true",
        help="Validate origin/main and the temporary source worktree, then stop before PDF rendering.",
    )
    parser.add_argument(
        "--allow-dirty-code",
        action="store_true",
        help="Diagnostics only. Official PDF generation should start from a clean code checkout.",
    )
    parser.add_argument(
        "--keep-source-worktree",
        action="store_true",
        help="Diagnostics only. Leave the temporary clean source worktree on disk.",
    )
    return parser.parse_args()


def main() -> int:
    configure_stdio()
    args = parse_args()
    repo_root = args.repo_root.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    try:
        state = ensure_entrypoint_can_run(
            repo_root=repo_root,
            source_ref=args.source_ref,
            allow_dirty_code=args.allow_dirty_code,
        )
        print(
            "official daily report source gate passed: "
            f"source_ref={state['source_ref']} "
            f"source_commit_sha={state['source_commit_sha']} "
            f"main_price_date={state['main_price_date']} "
            f"report_ready={state['report_ready']} "
            f"warrant_ready={state['warrant_ready']} "
            f"daily_pdf_ready={state['daily_pdf_ready']}"
        )

        with tempfile.TemporaryDirectory(prefix="tdcc_daily_report_source_") as temp_name:
            temp_root = Path(temp_name)
            source_root = add_source_worktree(repo_root, args.source_ref, temp_root)
            try:
                temp_state = resolve_daily_report_source_state(
                    repo_root=source_root,
                    source_ref=args.source_ref,
                    fetch=False,
                    require_git_clean=True,
                    require_local_match=True,
                )
                print(
                    "temporary clean source worktree verified: "
                    f"path={source_root} "
                    f"main_price_date={temp_state['main_price_date']}"
                )
                if args.source_gate_only:
                    return 0
                output_dir.mkdir(parents=True, exist_ok=True)
                paths = run_generator(source_root, output_dir)
                print("official ChatGPT-side daily PDF generation completed")
                for path in paths:
                    print(path)
            finally:
                if args.keep_source_worktree:
                    print(f"temporary source worktree kept: {source_root}")
                else:
                    remove_source_worktree(repo_root, source_root)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
