from __future__ import annotations

import argparse
import csv
import json
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
RENDERED_MODEL_REGRESSION_CONTRACT = REPO_ROOT / "config" / "daily_pdf_rendered_model_regression_contract.csv"
STALE_RESIDUE_NAME = "20260612_requested_repo20260612_stale_residue_current_rules.pdf"
RUNTIME_MANIFEST_NAME = "chatgpt_daily_report_runtime_manifest.json"
EXPECTED_TITLES = (
    "主流股每日推薦精華",
    "主流股完整候選清單",
    "非主流股每日推薦精華",
    "非主流股完整候選清單",
    "權證市場輔助分析",
    "市場風險與大盤期權背景",
)
HIGHLIGHT_LAYOUT_TITLES = (
    "非主流股每日推薦精華",
    "主流股每日推薦精華",
)
HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT = (
    "放量攻擊模型",
    "本日可買 / 已確認買入候選",
    "操作中",
)
HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT = (
    "待確認",
    "未達買入排名證據",
    "lifecycle_suppressed",
    "程式推薦買進",
)


PDF_ROLE_TITLE_TOKENS = {
    "mainstream_highlight": EXPECTED_TITLES[0],
    "mainstream_full": EXPECTED_TITLES[1],
    "non_mainstream_highlight": EXPECTED_TITLES[2],
    "non_mainstream_full": EXPECTED_TITLES[3],
    "warrant_market_auxiliary": EXPECTED_TITLES[4],
    "market_risk_background": EXPECTED_TITLES[5],
}


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


def validate_highlight_layout_texts(title_to_pages: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    for title in HIGHLIGHT_LAYOUT_TITLES:
        pages = title_to_pages.get(title, [])
        if not pages:
            errors.append(f"{title}: missing text pages for daily highlight layout validation")
            continue
        first_page = pages[0]
        full_text = "\n".join(pages)
        for token in HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT:
            if token not in first_page:
                errors.append(f"{title}: first page missing required layout text: {token}")
        if "股價回檔模型" in first_page:
            errors.append(f"{title}: first page must not start with stock-model tables before volume operations")
        for token in HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT:
            if token in full_text:
                errors.append(f"{title}: highlight PDF contains forbidden operation-layer text: {token}")
    return errors


def validate_pdf_highlight_layout_contract(paths: list[Path]) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency is installed in CI.
        return [f"pypdf import failed for highlight layout validation: {exc}"]

    title_to_pages: dict[str, list[str]] = {}
    errors: list[str] = []
    for path in paths:
        matched_title = next((title for title in HIGHLIGHT_LAYOUT_TITLES if title in path.name), "")
        if not matched_title:
            continue
        try:
            reader = PdfReader(str(path))
            title_to_pages[matched_title] = [page.extract_text() or "" for page in reader.pages]
        except Exception as exc:
            errors.append(f"{matched_title}: pypdf text extraction failed for {path}: {exc}")
    errors.extend(validate_highlight_layout_texts(title_to_pages))
    return errors


def split_contract_tokens(value: object) -> list[str]:
    return [token.strip() for token in str(value or "").replace(";", "|").split("|") if token.strip()]


def read_rendered_model_regression_contract(path: Path = RENDERED_MODEL_REGRESSION_CONTRACT) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def validate_rendered_model_regression_texts(
    role_to_pages: dict[str, list[str]],
    main_price_date: str,
    contract_rows: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    for row in contract_rows:
        if str(row.get("active", "")).strip().lower() not in {"true", "1", "yes", "y"}:
            continue
        report_date = str(row.get("report_date", "")).strip()
        if report_date not in {main_price_date, "*"}:
            continue

        contract_id = str(row.get("contract_id", "")).strip() or "<missing_contract_id>"
        pdf_role = str(row.get("pdf_role", "")).strip()
        pages = role_to_pages.get(pdf_role)
        if not pages:
            errors.append(f"{contract_id}: missing rendered PDF text for pdf_role={pdf_role}")
            continue

        page_scope = str(row.get("page_scope", "all_pages")).strip() or "all_pages"
        if page_scope == "first_page":
            scoped_pages = pages[:1]
        elif page_scope == "all_pages":
            scoped_pages = pages
        else:
            errors.append(f"{contract_id}: unsupported page_scope={page_scope}")
            continue

        compact_text = "".join("\n".join(scoped_pages).split())
        for stock_id in split_contract_tokens(row.get("required_stock_ids")):
            if stock_id not in compact_text:
                errors.append(f"{contract_id}: required stock_id={stock_id} missing from {pdf_role} {page_scope}")
        for stock_id in split_contract_tokens(row.get("forbidden_stock_ids")):
            if stock_id in compact_text:
                errors.append(f"{contract_id}: forbidden stock_id={stock_id} appeared in {pdf_role} {page_scope}")
    return errors


def rendered_model_regression_pdf_role(name: str) -> str:
    matches = [
        (role, title)
        for role, title in PDF_ROLE_TITLE_TOKENS.items()
        if title in name
    ]
    if not matches:
        return ""
    role, _title = max(matches, key=lambda item: len(item[1]))
    return role


def validate_rendered_model_regression_contract(paths: list[Path], main_price_date: str) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency is installed in CI.
        return [f"pypdf import failed for rendered model regression validation: {exc}"]

    contract_rows = read_rendered_model_regression_contract()
    if not contract_rows:
        return []

    role_to_pages: dict[str, list[str]] = {}
    errors: list[str] = []
    for path in paths:
        matched_role = rendered_model_regression_pdf_role(path.name)
        if not matched_role:
            continue
        try:
            reader = PdfReader(str(path))
            role_to_pages[matched_role] = [page.extract_text() or "" for page in reader.pages]
        except Exception as exc:
            errors.append(f"{matched_role}: pypdf text extraction failed for {path}: {exc}")

    errors.extend(validate_rendered_model_regression_texts(role_to_pages, main_price_date, contract_rows))
    return errors


def validate_runtime_manifest(paths: list[Path], output_dir: Path, state: dict) -> list[str]:
    errors: list[str] = []
    manifest_path = output_dir / RUNTIME_MANIFEST_NAME
    if not manifest_path.exists():
        return [f"runtime manifest is missing: {manifest_path}"]

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"runtime manifest is unreadable JSON: {manifest_path}: {exc}"]

    expected_pdf_paths = [str(path) for path in paths]
    checks = {
        "manifest_type": "chatgpt_daily_report_runtime_manifest",
        "source_ref": state["source_ref"],
        "source_commit_sha": state["source_commit_sha"],
        "clean_source_commit_sha": state["source_commit_sha"],
        "main_price_date": state["main_price_date"],
        "freshness_path": state["freshness_path"],
        "readme_path": state["readme_path"],
        "packet_path": state["packet_path"],
        "pdf_count": len(paths),
    }
    for key, expected in checks.items():
        if manifest.get(key) != expected:
            errors.append(
                f"runtime manifest {key}={manifest.get(key)!r} does not match expected {expected!r}"
            )

    if manifest.get("pdf_paths") != expected_pdf_paths:
        errors.append("runtime manifest pdf_paths do not match emitted PDF paths")

    if output_dir.resolve() != Path(str(manifest.get("output_dir", ""))).expanduser().resolve():
        errors.append("runtime manifest output_dir does not match replay output_dir")

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
    errors.extend(validate_pdf_highlight_layout_contract(paths))
    errors.extend(validate_rendered_model_regression_contract(paths, main_price_date))
    errors.extend(validate_runtime_manifest(paths, output_dir, state))

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
