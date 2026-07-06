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
SEMANTIC_GOLDEN_CASES_CONTRACT = REPO_ROOT / "config" / "daily_pdf_semantic_golden_cases.csv"
STALE_RESIDUE_NAME = "20260612_requested_repo20260612_stale_residue_current_rules.pdf"
RUNTIME_MANIFEST_NAME = "chatgpt_daily_report_runtime_manifest.json"
SEMANTIC_MANIFEST_NAME = "chatgpt_daily_pdf_semantic_manifest.csv"
EXPECTED_PDF_ROLES = (
    "mainstream_highlight",
    "mainstream_full",
    "non_mainstream_highlight",
    "non_mainstream_full",
    "warrant_market_auxiliary",
    "market_risk_background",
)
HIGHLIGHT_LAYOUT_ROLES = (
    "mainstream_highlight",
    "non_mainstream_highlight",
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
HIGHLIGHT_STOCK_MODEL_SECTION_TEXT = '股價回檔模型'


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


def normalized_path_text(path: Path) -> str:
    return str(path.expanduser().resolve())


def read_runtime_manifest(output_dir: Path) -> tuple[dict | None, list[str]]:
    manifest_path = output_dir / RUNTIME_MANIFEST_NAME
    if not manifest_path.exists():
        return None, [f"runtime manifest is missing: {manifest_path}"]

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, [f"runtime manifest is unreadable JSON: {manifest_path}: {exc}"]
    if not isinstance(manifest, dict):
        return None, [f"runtime manifest root must be an object: {manifest_path}"]
    return manifest, []


def role_to_pdf_paths_from_manifest(manifest: dict, paths: list[Path]) -> tuple[dict[str, Path], list[str]]:
    pdf_outputs = manifest.get("pdf_outputs")
    if not isinstance(pdf_outputs, list):
        return {}, ["runtime manifest pdf_outputs must be a list of role/path objects"]

    emitted_paths = {normalized_path_text(path): path.expanduser().resolve() for path in paths}
    role_to_path: dict[str, Path] = {}
    errors: list[str] = []
    for index, output in enumerate(pdf_outputs, start=1):
        if not isinstance(output, dict):
            errors.append(f"runtime manifest pdf_outputs[{index}] must be an object")
            continue

        role = str(output.get("pdf_role", "")).strip()
        if role not in EXPECTED_PDF_ROLES:
            errors.append(f"runtime manifest pdf_outputs[{index}] has unknown pdf_role={role!r}")
            continue
        if role in role_to_path:
            errors.append(f"runtime manifest pdf_outputs contains duplicate pdf_role={role}")
            continue

        path_text = str(output.get("path", "")).strip()
        resolved_path = normalized_path_text(Path(path_text)) if path_text else ""
        if resolved_path not in emitted_paths:
            errors.append(f"runtime manifest pdf_outputs[{index}] path is not an emitted PDF path: {path_text}")
            continue
        role_to_path[role] = emitted_paths[resolved_path]

    missing_roles = [role for role in EXPECTED_PDF_ROLES if role not in role_to_path]
    if missing_roles:
        errors.append(f"runtime manifest pdf_outputs missing pdf_role values: {', '.join(missing_roles)}")

    return role_to_path, errors


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


def validate_highlight_layout_texts(role_to_pages: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    for role in HIGHLIGHT_LAYOUT_ROLES:
        pages = role_to_pages.get(role, [])
        if not pages:
            errors.append(f"{role}: missing text pages for daily highlight layout validation")
            continue
        first_page = pages[0]
        full_text = "\n".join(pages)
        for token in HIGHLIGHT_FIRST_PAGE_REQUIRED_TEXT:
            if token not in first_page:
                errors.append(f"{role}: first page missing required layout text: {token}")
        if HIGHLIGHT_STOCK_MODEL_SECTION_TEXT in first_page:
            errors.append(f"{role}: first page must not start with stock-model tables before volume operations")
        for token in HIGHLIGHT_FULL_TEXT_FORBIDDEN_TEXT:
            if token in full_text:
                errors.append(f"{role}: highlight PDF contains forbidden operation-layer text: {token}")
    return errors


def validate_pdf_highlight_layout_contract(paths: list[Path], output_dir: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency is installed in CI.
        return [f"pypdf import failed for highlight layout validation: {exc}"]

    manifest, manifest_errors = read_runtime_manifest(output_dir)
    if manifest_errors:
        return manifest_errors
    assert manifest is not None
    role_to_paths, manifest_errors = role_to_pdf_paths_from_manifest(manifest, paths)
    if manifest_errors:
        return manifest_errors

    role_to_pages: dict[str, list[str]] = {}
    errors: list[str] = []
    for role in HIGHLIGHT_LAYOUT_ROLES:
        path = role_to_paths.get(role)
        if path is None:
            continue
        try:
            reader = PdfReader(str(path))
            role_to_pages[role] = [page.extract_text() or "" for page in reader.pages]
        except Exception as exc:
            errors.append(f"{role}: pypdf text extraction failed for {path}: {exc}")
    errors.extend(validate_highlight_layout_texts(role_to_pages))
    return errors


def split_contract_tokens(value: object) -> list[str]:
    return [token.strip() for token in str(value or "").replace(";", "|").split("|") if token.strip()]


def compact_contract_text(value: object) -> str:
    return "".join(str(value or "").split())


def read_rendered_model_regression_contract(path: Path = RENDERED_MODEL_REGRESSION_CONTRACT) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def boolish(value: object) -> bool:
    return str(value or "").strip().lower() in {"true", "1", "yes", "y"}


def read_semantic_manifest(output_dir: Path, manifest: dict) -> tuple[list[dict[str, str]], list[str]]:
    path_text = str(manifest.get("semantic_manifest_path", "")).strip()
    if not path_text:
        return [], ["runtime manifest missing semantic_manifest_path"]
    manifest_path = Path(path_text).expanduser()
    if not manifest_path.is_absolute():
        manifest_path = output_dir / manifest_path
    manifest_path = manifest_path.resolve()
    expected_path = (output_dir / SEMANTIC_MANIFEST_NAME).resolve()
    if manifest_path != expected_path:
        return [], [f"semantic manifest path must be {expected_path}, observed={manifest_path}"]
    if not manifest_path.exists():
        return [], [f"semantic manifest is missing: {manifest_path}"]
    with manifest_path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return [], [f"semantic manifest is empty: {manifest_path}"]
    return rows, []


SEMANTIC_MANIFEST_REQUIRED_COLUMNS = {
    "manifest_type",
    "main_price_date",
    "pdf_role",
    "pdf_view",
    "report_line",
    "model_id",
    "pdf_section",
    "rendered_row_type",
    "rendered_order",
    "stock_id",
    "stock_name",
    "operation_status",
    "row_action_status",
    "buy_rank_eligible",
    "source_artifact",
    "source_sha256",
}
FORBIDDEN_SEMANTIC_SOURCE_TOKENS = (
    "volume_breakout_operation_pdf_preview",
)


def validate_semantic_manifest_schema(rows: list[dict[str, str]], main_price_date: str) -> list[str]:
    errors: list[str] = []
    observed_columns = set(rows[0])
    missing = sorted(SEMANTIC_MANIFEST_REQUIRED_COLUMNS - observed_columns)
    if missing:
        errors.append(f"semantic manifest missing columns: {missing}")
    for index, row in enumerate(rows, start=2):
        if str(row.get("manifest_type", "")).strip() != "chatgpt_daily_pdf_semantic_manifest":
            errors.append(f"semantic manifest row {index} has invalid manifest_type")
        if str(row.get("main_price_date", "")).strip() != main_price_date:
            errors.append(f"semantic manifest row {index} main_price_date mismatch")
        if str(row.get("pdf_role", "")).strip() not in EXPECTED_PDF_ROLES:
            errors.append(f"semantic manifest row {index} has unknown pdf_role={row.get('pdf_role')!r}")
        if str(row.get("rendered_row_type", "")).strip() not in {"data", "empty_state"}:
            errors.append(f"semantic manifest row {index} has invalid rendered_row_type")
        if str(row.get("rendered_row_type", "")).strip() == "data" and not str(row.get("stock_id", "")).strip():
            errors.append(f"semantic manifest data row {index} missing stock_id")
        source_sha = str(row.get("source_sha256", "")).strip()
        if len(source_sha) != 64 and str(row.get("model_id", "")).strip():
            errors.append(f"semantic manifest row {index} source_sha256 must be a sha256 hex digest")
        source_artifact = str(row.get("source_artifact", "")).strip()
        if str(row.get("model_id", "")).strip() and not source_artifact:
            errors.append(f"semantic manifest row {index} missing source_artifact")
        for token in FORBIDDEN_SEMANTIC_SOURCE_TOKENS:
            if token in source_artifact:
                errors.append(
                    f"semantic manifest row {index} uses forbidden legacy/preview source artifact: {source_artifact}"
                )
    return errors


def semantic_rows_matching(rows: list[dict[str, str]], case: dict[str, str]) -> list[dict[str, str]]:
    def value(name: str) -> str:
        return str(case.get(name, "") or "").strip()

    rendered_row_type = value("rendered_row_type") or "data"
    empty_state_text = value("empty_state_text")
    filters = {
        "pdf_role": value("pdf_role"),
        "model_id": value("model_id"),
        "pdf_section": value("pdf_section"),
        "stock_id": value("stock_id"),
    }
    matched = []
    for row in rows:
        if str(row.get("rendered_row_type", "")).strip() != rendered_row_type:
            continue
        if empty_state_text and str(row.get("empty_state_text", "")).strip() != empty_state_text:
            continue
        if all(not expected or str(row.get(column, "")).strip() == expected for column, expected in filters.items()):
            matched.append(row)
    return matched


def read_semantic_golden_cases(path: Path = SEMANTIC_GOLDEN_CASES_CONTRACT) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def validate_semantic_golden_cases(
    rows: list[dict[str, str]],
    main_price_date: str,
    cases: list[dict[str, str]] | None = None,
) -> list[str]:
    errors: list[str] = []
    for case in cases if cases is not None else read_semantic_golden_cases():
        if not boolish(case.get("active")):
            continue
        report_date = str(case.get("report_date", "")).strip()
        if report_date not in {main_price_date, "*"}:
            continue
        case_id = str(case.get("case_id", "")).strip() or "<missing_case_id>"
        expectation = str(case.get("expectation", "")).strip()
        matched = semantic_rows_matching(rows, case)
        if expectation == "present":
            if len(matched) != 1:
                errors.append(f"{case_id}: expected exactly one semantic row, observed={len(matched)}")
        elif expectation == "absent":
            if matched:
                errors.append(f"{case_id}: expected absent semantic row, observed={len(matched)}")
        elif expectation == "count_equals":
            expected_count_text = str(case.get("expected_count", "")).strip()
            try:
                expected_count = int(expected_count_text)
            except ValueError:
                errors.append(f"{case_id}: invalid expected_count={expected_count_text!r}")
                continue
            if len(matched) != expected_count:
                errors.append(
                    f"{case_id}: expected semantic row count={expected_count}, observed={len(matched)}"
                )
        else:
            errors.append(f"{case_id}: unsupported expectation={expectation!r}")
    return errors


def validate_semantic_manifest_contract(output_dir: Path, main_price_date: str) -> list[str]:
    manifest, errors = read_runtime_manifest(output_dir)
    if errors:
        return errors
    assert manifest is not None
    rows, semantic_errors = read_semantic_manifest(output_dir, manifest)
    errors.extend(semantic_errors)
    if rows:
        errors.extend(validate_semantic_manifest_schema(rows, main_price_date))
        errors.extend(validate_semantic_golden_cases(rows, main_price_date))
    return errors


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

        compact_text = compact_contract_text("\n".join(scoped_pages))
        for stock_id in split_contract_tokens(row.get("required_stock_ids")):
            if stock_id not in compact_text:
                errors.append(f"{contract_id}: required stock_id={stock_id} missing from {pdf_role} {page_scope}")
        for stock_id in split_contract_tokens(row.get("forbidden_stock_ids")):
            if stock_id in compact_text:
                errors.append(f"{contract_id}: forbidden stock_id={stock_id} appeared in {pdf_role} {page_scope}")
        for token in split_contract_tokens(row.get("required_text_tokens")):
            compact_token = compact_contract_text(token)
            if compact_token and compact_token not in compact_text:
                errors.append(f"{contract_id}: required text token={token!r} missing from {pdf_role} {page_scope}")
        for token in split_contract_tokens(row.get("forbidden_text_tokens")):
            compact_token = compact_contract_text(token)
            if compact_token and compact_token in compact_text:
                errors.append(f"{contract_id}: forbidden text token={token!r} appeared in {pdf_role} {page_scope}")
    return errors


def validate_rendered_model_regression_contract(paths: list[Path], main_price_date: str, output_dir: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency is installed in CI.
        return [f"pypdf import failed for rendered model regression validation: {exc}"]

    contract_rows = read_rendered_model_regression_contract()
    if not contract_rows:
        return []

    manifest, manifest_errors = read_runtime_manifest(output_dir)
    if manifest_errors:
        return manifest_errors
    assert manifest is not None
    role_to_paths, manifest_errors = role_to_pdf_paths_from_manifest(manifest, paths)
    if manifest_errors:
        return manifest_errors

    role_to_pages: dict[str, list[str]] = {}
    errors: list[str] = []
    for matched_role, path in role_to_paths.items():
        try:
            reader = PdfReader(str(path))
            role_to_pages[matched_role] = [page.extract_text() or "" for page in reader.pages]
        except Exception as exc:
            errors.append(f"{matched_role}: pypdf text extraction failed for {path}: {exc}")

    errors.extend(validate_rendered_model_regression_texts(role_to_pages, main_price_date, contract_rows))
    return errors


def validate_runtime_manifest(paths: list[Path], output_dir: Path, state: dict) -> list[str]:
    manifest, errors = read_runtime_manifest(output_dir)
    if errors:
        return errors
    assert manifest is not None

    expected_pdf_paths = [normalized_path_text(path) for path in paths]
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

    expected_semantic_manifest_path = normalized_path_text(output_dir / SEMANTIC_MANIFEST_NAME)
    observed_semantic_manifest_path = str(manifest.get("semantic_manifest_path", "")).strip()
    if not observed_semantic_manifest_path:
        errors.append("runtime manifest semantic_manifest_path is missing")
    elif normalized_path_text(Path(observed_semantic_manifest_path)) != expected_semantic_manifest_path:
        errors.append(
            "runtime manifest semantic_manifest_path does not match expected output_dir manifest: "
            f"{observed_semantic_manifest_path}"
        )

    pdf_outputs = manifest.get("pdf_outputs")
    if not isinstance(pdf_outputs, list):
        errors.append("runtime manifest pdf_outputs must be a list of role/path objects")
    else:
        roles = [str(output.get("pdf_role", "")).strip() if isinstance(output, dict) else "" for output in pdf_outputs]
        indices = [output.get("pdf_index") if isinstance(output, dict) else None for output in pdf_outputs]
        output_paths = [
            normalized_path_text(Path(str(output.get("path", "")))) if isinstance(output, dict) else ""
            for output in pdf_outputs
        ]
        if roles != list(EXPECTED_PDF_ROLES):
            errors.append(
                f"runtime manifest pdf_outputs roles do not match expected order: {roles!r}"
            )
        if indices != list(range(1, len(EXPECTED_PDF_ROLES) + 1)):
            errors.append("runtime manifest pdf_outputs pdf_index values do not match expected 1-based order")
        if output_paths != expected_pdf_paths:
            errors.append("runtime manifest pdf_outputs paths do not match emitted PDF paths")
        _role_to_paths, role_errors = role_to_pdf_paths_from_manifest(manifest, paths)
        errors.extend(role_errors)

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
    runtime_errors = validate_runtime_manifest(paths, output_dir, state)
    errors.extend(runtime_errors)
    if not runtime_errors:
        errors.extend(validate_pdf_highlight_layout_contract(paths, output_dir))
        errors.extend(validate_rendered_model_regression_contract(paths, main_price_date, output_dir))
        errors.extend(validate_semantic_manifest_contract(output_dir, main_price_date))

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
