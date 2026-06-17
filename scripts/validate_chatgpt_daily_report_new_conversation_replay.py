from __future__ import annotations

import argparse
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


DEFAULT_OUTPUT_DIR = REPO_ROOT / "chatgpt_side_outputs_new_conversation_replay"
STALE_RESIDUE_NAME = "20260612_requested_repo20260612_stale_residue_current_rules.pdf"
EXPECTED_TITLES = (
    "主流股每日推薦精華",
    "主流股完整候選清單",
    "非主流股每日推薦精華",
    "非主流股完整候選清單",
    "權證市場輔助分析",
    "市場風險與大盤期權背景",
)


class ReplayValidationError(RuntimeError):
    pass


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd),
        check=False,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        text=True,
    )


def require_success(proc: subprocess.CompletedProcess[str], action: str) -> str:
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or f"{action} failed").strip()
        raise ReplayValidationError(f"{action} failed: {detail}")
    return proc.stdout


def add_clean_entrypoint_worktree(repo_root: Path, source_ref: str, temp_root: Path) -> Path:
    source_root = temp_root / "new_conversation_clean_source"
    proc = run_command(
        ["git", "worktree", "add", "--detach", str(source_root), source_ref],
        cwd=repo_root,
    )
    require_success(proc, f"git worktree add --detach {source_root} {source_ref}")
    return source_root


def remove_clean_entrypoint_worktree(repo_root: Path, source_root: Path) -> None:
    if not source_root.exists():
        return
    proc = run_command(["git", "worktree", "remove", "--force", str(source_root)], cwd=repo_root)
    if proc.returncode != 0:
        print(
            "WARNING: failed to remove replay source worktree: "
            f"{(proc.stderr or proc.stdout).strip()}",
            file=sys.stderr,
        )


def pdf_paths_from_stdout(stdout: str) -> list[Path]:
    paths: list[Path] = []
    seen: set[str] = set()
    for line in stdout.splitlines():
        text = line.strip()
        if not text.lower().endswith(".pdf"):
            continue
        path = Path(text).expanduser().resolve()
        key = str(path).casefold()
        if key not in seen:
            seen.add(key)
            paths.append(path)
    return paths


def date_slash(value: str) -> str:
    if len(value) != 8 or not value.isdigit():
        return value
    return f"{int(value[:4])}/{int(value[4:6])}/{int(value[6:])}"


def create_stale_residue(output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    stale_path = output_dir / STALE_RESIDUE_NAME
    stale_path.write_bytes(
        b"%PDF-1.4\n"
        b"% stale residue intentionally created by replay validator\n"
        b"1 0 obj << /Type /Catalog >> endobj\n"
        b"trailer << /Root 1 0 R >>\n%%EOF\n"
    )
    return stale_path


def validate_source_gate_echo(stdout: str, state: dict, source_ref: str) -> list[str]:
    errors: list[str] = []
    required = {
        f"source_ref={source_ref}",
        f"source_commit_sha={state['source_commit_sha']}",
        f"main_price_date={state['main_price_date']}",
        "report_ready=True",
        "warrant_ready=True",
        "daily_pdf_ready=True",
    }
    for token in sorted(required):
        if token not in stdout:
            errors.append(f"entrypoint stdout missing source-gate token: {token}")
    if "official ChatGPT-side daily PDF generation completed" not in stdout:
        errors.append("entrypoint stdout missing official completion line")
    return errors


def validate_pdf_path_contract(paths: list[Path], output_dir: Path, main_price_date: str) -> list[str]:
    errors: list[str] = []
    if len(paths) != 6:
        errors.append(f"new-conversation replay must emit exactly 6 unique PDF paths, got {len(paths)}")
    output_root = output_dir.resolve()
    expected_fragment = f"{main_price_date}_requested_repo{main_price_date}_"
    titles_found = {title: False for title in EXPECTED_TITLES}

    for path in paths:
        try:
            path.relative_to(output_root)
        except ValueError:
            errors.append(f"emitted PDF path is outside replay output dir: {path}")

        name = path.name
        if expected_fragment not in name:
            errors.append(
                f"emitted PDF filename must use main_price_date={main_price_date} for both request and repo date: {name}"
            )
        if STALE_RESIDUE_NAME == name or "20260612_requested_repo20260612" in name:
            errors.append(f"emitted PDF path reused stale residue: {name}")
        if not name.endswith("_current_rules.pdf"):
            errors.append(f"emitted PDF filename must end with _current_rules.pdf: {name}")
        for title in titles_found:
            if title in name:
                titles_found[title] = True

    missing_titles = [title for title, found in titles_found.items() if not found]
    if missing_titles:
        errors.append(f"missing expected ChatGPT-side PDF titles: {', '.join(missing_titles)}")
    return errors


def validate_pdf_files_open(paths: list[Path]) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency is installed in CI.
        return [f"pypdf import failed: {exc}"]

    errors: list[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"emitted PDF path does not exist: {path}")
            continue
        try:
            reader = PdfReader(str(path))
            if len(reader.pages) <= 0:
                errors.append(f"emitted PDF has no pages: {path}")
        except Exception as exc:
            errors.append(f"emitted PDF cannot be opened by pypdf: {path}: {exc}")
    return errors


def run_replay(repo_root: Path, source_ref: str, output_dir: Path) -> tuple[str, dict, list[Path], Path]:
    try:
        current_source_state = resolve_daily_report_source_state(
            repo_root=repo_root,
            source_ref=source_ref,
            fetch=True,
            require_git_clean=False,
            allow_dirty=False,
            require_local_match=False,
        )
    except DailyReportSourceError as exc:
        raise ReplayValidationError("\n".join(exc.errors)) from exc

    stale_path = create_stale_residue(output_dir)
    with tempfile.TemporaryDirectory(prefix="tdcc_new_conversation_replay_") as temp_name:
        source_root = add_clean_entrypoint_worktree(repo_root, source_ref, Path(temp_name))
        try:
            state = resolve_daily_report_source_state(
                repo_root=source_root,
                source_ref=source_ref,
                fetch=False,
                require_git_clean=True,
                allow_dirty=False,
                require_local_match=True,
            )
            if state["source_commit_sha"] != current_source_state["source_commit_sha"]:
                raise ReplayValidationError(
                    "clean replay source changed unexpectedly: "
                    f"current={current_source_state['source_commit_sha']} clean={state['source_commit_sha']}"
                )
            entrypoint = source_root / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
            proc = run_command(
                [
                    sys.executable,
                    str(entrypoint),
                    "--repo-root",
                    str(source_root),
                    "--source-ref",
                    source_ref,
                    "--output-dir",
                    str(output_dir),
                ],
                cwd=source_root,
            )
            stdout = require_success(proc, "official ChatGPT-side daily PDF replay")
            if proc.stderr.strip():
                print(proc.stderr.strip(), file=sys.stderr)
            return stdout, state, pdf_paths_from_stdout(stdout), stale_path
        finally:
            remove_clean_entrypoint_worktree(repo_root, source_root)


def validate_replay(repo_root: Path, source_ref: str, output_dir: Path) -> tuple[dict, list[Path], Path]:
    stdout, state, paths, stale_path = run_replay(repo_root, source_ref, output_dir)
    main_price_date = str(state["main_price_date"])

    errors: list[str] = []
    errors.extend(validate_source_gate_echo(stdout, state, source_ref))
    errors.extend(validate_pdf_path_contract(paths, output_dir, main_price_date))
    errors.extend(validate_pdf_files_open(paths))

    if errors:
        raise ReplayValidationError("\n".join(errors))

    return state, paths, stale_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Replay the official ChatGPT-side daily PDF entrypoint as a random/new conversation would. "
            "The gate must use origin/main main_price_date and must emit exactly six current PDFs."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--keep-stale-residue",
        action="store_true",
        help="Leave the intentionally created stale residue PDF in the output folder for diagnostics.",
    )
    return parser.parse_args()


def main() -> int:
    configure_stdio()
    args = parse_args()
    repo_root = args.repo_root.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()

    try:
        state, paths, stale_path = validate_replay(repo_root, args.source_ref, output_dir)
        if stale_path.exists() and not args.keep_stale_residue:
            stale_path.unlink()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("new-conversation ChatGPT-side daily PDF replay passed")
    print(f"source_ref={args.source_ref}")
    print(f"source_commit_sha={state['source_commit_sha']}")
    print(f"main_price_date={state['main_price_date']}")
    print(f"report_date={date_slash(str(state['main_price_date']))}")
    print(f"output_dir={output_dir}")
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
