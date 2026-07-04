from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_REF = "origin/main"
VALIDATION_JSON = Path("output/latest/tdcc_weekly_candidate_report_validation_latest.json")
DELIVERY_DIR = Path("output/latest/published_reports/tdcc_weekly")
DOCS_DELIVERY_DIR = Path("docs/latest/published_reports/tdcc_weekly")
HIGHLIGHT_PDF = Path("output/latest/tdcc_weekly_candidate_highlight_latest.pdf")
FULL_PDF = Path("output/latest/tdcc_weekly_candidate_full_latest.pdf")
FORBIDDEN_PDF_TEXT = (
    "insufficient_data",
    "range_rebound",
    "short_term_specialty",
    "call_strong_inflow",
    "no_signal",
)
SYNC_GLOBS = (
    "output/latest/tdcc_weekly_*",
    "output/latest/tdcc_consecutive_accumulation_ranking_latest.*",
    "output/latest/tdcc_weekly_increase_ranking_latest.*",
    "output/latest/tdcc_invalid_holder_distribution_latest.csv",
    "output/latest/published_reports/tdcc_weekly/*.pdf",
    "output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
    "docs/latest/tdcc_weekly_*",
    "docs/latest/tdcc_consecutive_accumulation_ranking_latest.*",
    "docs/latest/tdcc_weekly_increase_ranking_latest.*",
    "docs/latest/tdcc_invalid_holder_distribution_latest.csv",
    "docs/latest/published_reports/tdcc_weekly/*.pdf",
    "docs/latest/READ_ME_FIRST_DAILY_REPORT.txt",
)


class TDCCWeeklyEntrypointError(RuntimeError):
    pass


@dataclass(frozen=True)
class PdfInspection:
    path: Path
    size: int
    pages: int
    text_chars: int


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def run_command(args: list[str], cwd: Path, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd),
        env=env,
        check=False,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        text=True,
    )


def require_success(proc: subprocess.CompletedProcess[str], action: str) -> str:
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or f"{action} failed").strip()
        raise TDCCWeeklyEntrypointError(f"{action} failed: {detail}")
    if proc.stderr.strip():
        print(proc.stderr.strip(), file=sys.stderr)
    return proc.stdout


def git(repo_root: Path, *args: str) -> str:
    proc = run_command(["git", *args], cwd=repo_root)
    return require_success(proc, "git " + " ".join(args)).strip()


def fetch_source(repo_root: Path) -> None:
    require_success(
        run_command(["git", "fetch", "origin", "main"], cwd=repo_root),
        "git fetch origin main",
    )


def resolve_commit(repo_root: Path, source_ref: str) -> str:
    return git(repo_root, "rev-parse", "--verify", f"{source_ref}^{{commit}}")


def is_generated_delivery_path(path_text: str) -> bool:
    normalized = path_text.replace("\\", "/")
    return normalized.startswith("output/latest/") or normalized.startswith("docs/latest/")


def dirty_non_generated_paths(repo_root: Path) -> list[str]:
    proc = run_command(["git", "status", "--porcelain=v1", "-z"], cwd=repo_root)
    require_success(proc, "git status --porcelain=v1 -z")
    parts = [part for part in proc.stdout.split("\0") if part]
    paths: list[str] = []
    index = 0
    while index < len(parts):
        record = parts[index]
        status = record[:2]
        path_text = record[3:] if len(record) > 3 else ""
        if status.startswith(("R", "C")) and index + 1 < len(parts):
            index += 1
        if path_text and not is_generated_delivery_path(path_text):
            paths.append(path_text)
        index += 1
    return sorted(paths)


def add_source_worktree(repo_root: Path, source_ref: str, temp_root: Path) -> Path:
    temp_root.mkdir(parents=True, exist_ok=True)
    source_root = temp_root / "origin_main_tdcc_weekly_source"
    proc = run_command(["git", "worktree", "add", "--detach", str(source_root), source_ref], cwd=repo_root)
    require_success(proc, f"git worktree add --detach {source_root} {source_ref}")
    return source_root


def remove_source_worktree(repo_root: Path, source_root: Path) -> None:
    if not source_root.exists():
        return
    proc = run_command(["git", "worktree", "remove", "--force", str(source_root)], cwd=repo_root)
    if proc.returncode != 0:
        print(
            "WARNING: failed to remove temporary TDCC source worktree: "
            f"{(proc.stderr or proc.stdout).strip()}",
            file=sys.stderr,
        )


def run_python_script(source_root: Path, script: str) -> None:
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    proc = run_command([sys.executable, script], cwd=source_root, env=env)
    stdout = require_success(proc, script)
    if stdout.strip():
        print(stdout.strip())


def load_validation(source_root: Path) -> dict[str, Any]:
    path = source_root / VALIDATION_JSON
    if not path.exists():
        raise TDCCWeeklyEntrypointError(f"TDCC validation JSON missing: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise TDCCWeeklyEntrypointError(f"TDCC validation did not pass: {data.get('errors', [])}")
    date_contract = data.get("date_contract", {})
    if date_contract.get("date_source") != "report_ready_csv_signal_date":
        raise TDCCWeeklyEntrypointError(f"unexpected TDCC date source: {date_contract.get('date_source', '')}")
    signal_date = str(data.get("signal_date", "")).strip()
    if not signal_date or signal_date != date_contract.get("report_date"):
        raise TDCCWeeklyEntrypointError("TDCC validation signal_date mismatch")
    return data


def delivery_pdf_paths(signal_date: str) -> dict[str, Path]:
    return {
        "highlight": DELIVERY_DIR / f"TDCC大戶籌碼週報_精華版_{signal_date}.pdf",
        "full": DELIVERY_DIR / f"TDCC大戶籌碼週報_完整版_{signal_date}.pdf",
    }


def required_pdf_paths(signal_date: str) -> list[Path]:
    delivery = delivery_pdf_paths(signal_date)
    return [HIGHLIGHT_PDF, FULL_PDF, delivery["highlight"], delivery["full"]]


def inspect_pdf(path: Path) -> PdfInspection:
    if not path.exists():
        raise TDCCWeeklyEntrypointError(f"missing TDCC PDF: {path}")
    size = path.stat().st_size
    if size < 10_000:
        raise TDCCWeeklyEntrypointError(f"TDCC PDF is too small: {path} size={size}")
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency absence is an environment failure.
        raise TDCCWeeklyEntrypointError(f"pypdf unavailable for TDCC PDF inspection: {exc}") from exc
    try:
        reader = PdfReader(str(path))
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception as exc:
        raise TDCCWeeklyEntrypointError(f"TDCC PDF cannot be opened: {path}: {exc}") from exc
    if not reader.pages:
        raise TDCCWeeklyEntrypointError(f"TDCC PDF has no pages: {path}")
    if not text.strip():
        raise TDCCWeeklyEntrypointError(f"TDCC PDF has no extractable text: {path}")
    leaked = [slug for slug in FORBIDDEN_PDF_TEXT if slug in text]
    if leaked:
        raise TDCCWeeklyEntrypointError(f"TDCC PDF leaks raw slugs {leaked}: {path}")
    return PdfInspection(path=path, size=size, pages=len(reader.pages), text_chars=len(text.strip()))


def inspect_required_pdfs(root: Path, signal_date: str) -> list[PdfInspection]:
    return [inspect_pdf(root / relative_path) for relative_path in required_pdf_paths(signal_date)]


def root_delivery_pdfs(root: Path) -> list[Path]:
    return sorted(path for path in (root / "output/latest").glob("*.pdf") if path.name.startswith("TDCC"))


def remove_root_delivery_pdfs(root: Path) -> None:
    for path in root_delivery_pdfs(root):
        path.unlink()
    docs_root = root / "docs/latest"
    for path in sorted(path for path in docs_root.glob("*.pdf") if path.name.startswith("TDCC")):
        path.unlink()


def collect_sync_files(source_root: Path) -> list[Path]:
    files: dict[str, Path] = {}
    for pattern in SYNC_GLOBS:
        for path in source_root.glob(pattern):
            if path.is_file():
                files[path.relative_to(source_root).as_posix()] = path
    return [files[key] for key in sorted(files)]


def sync_outputs(source_root: Path, target_root: Path) -> list[Path]:
    copied: list[Path] = []
    for source in collect_sync_files(source_root):
        relative = source.relative_to(source_root)
        target = target_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied.append(relative)
    remove_root_delivery_pdfs(target_root)
    return copied


def write_summary(
    source_ref: str,
    source_commit_sha: str,
    validation: dict[str, Any],
    inspections: list[PdfInspection],
    copied: list[Path],
) -> None:
    signal_date = validation.get("signal_date", "")
    print("tdcc_weekly_entrypoint_status=pass")
    print(f"source_ref={source_ref}")
    print(f"source_commit_sha={source_commit_sha}")
    print(f"signal_date={signal_date}")
    print("date_source=report_ready_csv_signal_date")
    print(f"synced_file_count={len(copied)}")
    for inspection in inspections:
        print(
            "pdf="
            f"{inspection.path.as_posix()}|pages={inspection.pages}|"
            f"size={inspection.size}|text_chars={inspection.text_chars}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Official TDCC weekly report entrypoint. Builds from a clean source worktree "
            "at origin/main, validates TDCC weekly PDFs, and syncs deliverables back to "
            "the configured holder-flow worktree."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF)
    parser.add_argument("--source-gate-only", action="store_true")
    parser.add_argument("--keep-source-worktree", action="store_true")
    return parser.parse_args()


def main() -> int:
    configure_stdio()
    args = parse_args()
    repo_root = args.repo_root.expanduser().resolve()
    try:
        fetch_source(repo_root)
        blockers = dirty_non_generated_paths(repo_root)
        if blockers:
            raise TDCCWeeklyEntrypointError(
                "fixed TDCC worktree has non-generated uncommitted changes: " + "; ".join(blockers)
            )
        source_commit_sha = resolve_commit(repo_root, args.source_ref)
        print(f"tdcc_weekly_source_gate_passed source_ref={args.source_ref} source_commit_sha={source_commit_sha}")

        with tempfile.TemporaryDirectory(prefix="tdcc_weekly_report_source_") as temp_name:
            source_root = add_source_worktree(repo_root, args.source_ref, Path(temp_name))
            try:
                actual_source_sha = resolve_commit(source_root, "HEAD")
                if actual_source_sha != source_commit_sha:
                    raise TDCCWeeklyEntrypointError(
                        f"temporary source commit mismatch: {actual_source_sha} != {source_commit_sha}"
                    )
                if dirty_non_generated_paths(source_root):
                    raise TDCCWeeklyEntrypointError("temporary TDCC source worktree is not clean")
                if args.source_gate_only:
                    return 0
                run_python_script(source_root, "scripts/build_tdcc_weekly_candidate_reports.py")
                run_python_script(source_root, "scripts/validate_tdcc_weekly_candidate_reports.py")
                run_python_script(source_root, "scripts/validate_tdcc_weekly_pdf_font_contract.py")
                run_python_script(source_root, "scripts/validate_pdf_facing_display_text.py")
                validation = load_validation(source_root)
                signal_date = str(validation["signal_date"])
                source_inspections = inspect_required_pdfs(source_root, signal_date)
                if root_delivery_pdfs(source_root):
                    raise TDCCWeeklyEntrypointError("TDCC Chinese delivery PDFs remain in source output/latest root")
                copied = sync_outputs(source_root, repo_root)
                target_inspections = inspect_required_pdfs(repo_root, signal_date)
                if root_delivery_pdfs(repo_root):
                    raise TDCCWeeklyEntrypointError("TDCC Chinese delivery PDFs remain in target output/latest root")
                if [(item.pages, item.size) for item in source_inspections] != [
                    (item.pages, item.size) for item in target_inspections
                ]:
                    raise TDCCWeeklyEntrypointError("synced TDCC PDF inspection mismatch")
                write_summary(args.source_ref, source_commit_sha, validation, target_inspections, copied)
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
