from __future__ import annotations

import argparse
from collections.abc import Callable
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.resolve_daily_report_source_state import (  # noqa: E402
    DEFAULT_SOURCE_REF,
    DailyReportSourceError,
    resolve_daily_report_source_state,
)
from scripts.git_worktree_safety import (  # noqa: E402
    GitWorktreeSafetyError,
    create_registered_full_temp_worktree,
)
from scripts import market_session_calendar  # noqa: E402
from scripts.validate_chatgpt_side_pdf_contract import (  # noqa: E402
    CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH,
    CHATGPT_DAILY_DFKAI_FONT_PATH_ENV,
    chatgpt_daily_dfkai_font_path,
    validate_dfkai_font_file,
)


GENERATOR_RELATIVE_PATH = Path("scripts") / "generate_chatgpt_side_daily_reports.py"
GENERATOR = REPO_ROOT / GENERATOR_RELATIVE_PATH
DEFAULT_OUTPUT_ROOT_NAME = "chatgpt_side_outputs_official"
RUNTIME_MANIFEST_NAME = "chatgpt_daily_report_runtime_manifest.json"
SEMANTIC_MANIFEST_NAME = "chatgpt_daily_pdf_semantic_manifest.csv"
PDF_OUTPUT_ROLES = (
    "mainstream_highlight",
    "mainstream_full",
    "non_mainstream_highlight",
    "non_mainstream_full",
    "warrant_market_auxiliary",
    "market_risk_background",
)
WINDOWS_DFKAI_CAPABILITY_NAME = "Language.Fonts.Hant~~~und-HANT~0.0.1.0"
WINDOWS_DFKAI_INSTALL_TIMEOUT_SECONDS = 20 * 60
WINDOWS_DFKAI_INSTALL_DETAIL_LIMIT = 2000


class DailyReportEntrypointError(RuntimeError):
    pass


class DailyReportMarketClosed(DailyReportEntrypointError):
    pass


def ensure_local_dfkai_font_for_pdf_rendering(
    *,
    font_path: Path | None = None,
    configured_font_path: bool | None = None,
    platform_name: str | None = None,
    default_font_path: Path = CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH,
    system_root: Path | None = None,
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
    validator: Callable[[Path], Path] = validate_dfkai_font_file,
) -> Path:
    path = font_path or chatgpt_daily_dfkai_font_path()
    has_configured_path = (
        bool(os.environ.get(CHATGPT_DAILY_DFKAI_FONT_PATH_ENV, "").strip())
        if configured_font_path is None
        else configured_font_path
    )

    if path.exists():
        try:
            validated_path = validator(path)
        except Exception as exc:
            raise DailyReportEntrypointError(
                "existing DFKai font failed validation; automatic install is forbidden when a file exists: "
                f"font_path={path}: {exc}"
            ) from exc
        print(f"dfkai_preflight_action=reuse_existing font_path={validated_path}")
        return validated_path

    if has_configured_path:
        raise DailyReportEntrypointError(
            "configured DFKai font path is missing; automatic install is allowed only for the unconfigured "
            f"canonical Windows path: env={CHATGPT_DAILY_DFKAI_FONT_PATH_ENV} font_path={path}"
        )

    current_platform = platform_name or sys.platform
    if current_platform != "win32":
        raise DailyReportEntrypointError(
            "DFKai font is missing and automatic capability install is supported only on Windows: "
            f"platform={current_platform} font_path={path}"
        )
    if path != default_font_path:
        raise DailyReportEntrypointError(
            "DFKai automatic install refuses a non-canonical target path: "
            f"font_path={path} canonical_path={default_font_path}"
        )

    windows_root = system_root or Path(os.environ.get("SystemRoot", r"C:\Windows"))
    dism_path = windows_root / "System32" / "dism.exe"
    command = [
        str(dism_path),
        "/Online",
        "/Add-Capability",
        f"/CapabilityName:{WINDOWS_DFKAI_CAPABILITY_NAME}",
        "/NoRestart",
    ]
    print(
        "dfkai_preflight_action=install_missing_windows_capability "
        f"font_path={path} timeout_seconds={WINDOWS_DFKAI_INSTALL_TIMEOUT_SECONDS}"
    )
    try:
        proc = runner(
            command,
            check=False,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            text=True,
            shell=False,
            timeout=WINDOWS_DFKAI_INSTALL_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise DailyReportEntrypointError(
            "DFKai Windows capability install exceeded the bounded timeout and will not be retried: "
            f"timeout_seconds={WINDOWS_DFKAI_INSTALL_TIMEOUT_SECONDS}"
        ) from exc
    except OSError as exc:
        raise DailyReportEntrypointError(
            "DFKai Windows capability install could not start; use an elevated Windows session or install "
            f"Traditional Chinese supplemental fonts in Windows Settings: dism_path={dism_path}: {exc}"
        ) from exc

    install_exit_code = proc.returncode
    install_detail = (proc.stderr or proc.stdout or "no DISM output").strip()[
        -WINDOWS_DFKAI_INSTALL_DETAIL_LIMIT:
    ]
    if not path.exists():
        raise DailyReportEntrypointError(
            "DFKai Windows capability install completed but the canonical font file is still missing: "
            f"font_path={path} exit_code={install_exit_code} detail={install_detail}"
        )

    try:
        validated_path = validator(path)
    except Exception as exc:
        raise DailyReportEntrypointError(
            "DFKai font failed validation after Windows capability install: "
            f"font_path={path} exit_code={install_exit_code} detail={install_detail} "
            f"validation_error={exc}"
        ) from exc
    if install_exit_code != 0:
        print(
            "WARNING: dfkai_preflight_warning=nonzero_but_final_state_valid "
            "canonical DFKai passed final file, identity, and glyph validation: "
            f"font_path={validated_path} exit_code={install_exit_code} detail={install_detail}",
            file=sys.stderr,
        )
    print(f"dfkai_preflight_action=installed_and_validated font_path={validated_path}")
    return validated_path


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


def normalize_validation_replay_main_price_date(value: object) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    normalized = market_session_calendar.normalize_date(text)
    if normalized != text:
        raise DailyReportEntrypointError(
            "validation replay date must use exact YYYYMMDD format: "
            f"validation_replay_main_price_date={text!r}"
        )
    try:
        market_session_calendar.parse_date(normalized)
    except ValueError as exc:
        raise DailyReportEntrypointError(
            "validation replay date is not a valid calendar date: "
            f"validation_replay_main_price_date={text!r}"
        ) from exc
    return normalized


def resolve_live_market_session_for_entrypoint(
    repo_root: Path,
    source_ref: str,
    validation_replay_main_price_date: str = "",
) -> dict | None:
    if source_ref != DEFAULT_SOURCE_REF:
        return None
    try:
        live_status = market_session_calendar.refresh_market_session_status(
            repo_root,
            phase="preflight",
            write_files=False,
        )
    except Exception as exc:
        raise DailyReportEntrypointError(
            f"live market-session preflight failed; PDF generation is blocked: {exc}"
        ) from exc

    market_status = str(live_status.get("market_status") or "")
    reason_code = str(live_status.get("reason_code") or "")
    if market_status in {
        market_session_calendar.CLOSED_SCHEDULED,
        market_session_calendar.CLOSED_EMERGENCY,
    }:
        if not validation_replay_main_price_date:
            raise DailyReportMarketClosed(
                f"market_status={market_status} "
                f"market_session_date={live_status.get('market_session_date', '')} "
                f"reason_code={reason_code}"
            )
        if market_status != market_session_calendar.CLOSED_SCHEDULED:
            raise DailyReportEntrypointError(
                "closed-market validation replay is allowed only for closed_scheduled; "
                f"market_status={market_status} reason_code={reason_code}"
            )
        live_expected = market_session_calendar.normalize_date(
            live_status.get("expected_main_price_date")
        )
        if validation_replay_main_price_date != live_expected:
            raise DailyReportEntrypointError(
                "closed-market validation replay date does not match the live official expectation; "
                f"validation_replay_main_price_date={validation_replay_main_price_date} "
                f"live_expected_main_price_date={live_expected or '<missing>'} "
                f"market_status={market_status}"
            )
        return live_status
    if not (
        market_status == market_session_calendar.OPEN_CONFIRMED
        or (
            market_status == market_session_calendar.UNKNOWN
            and reason_code == "awaiting_official_price_confirmation"
        )
    ):
        raise DailyReportEntrypointError(
            "live market-session state is unknown; PDF generation is blocked: "
            f"market_status={market_status or '<missing>'} "
            f"reason_code={reason_code or '<missing>'} "
            f"reason={live_status.get('reason', '')}"
        )
    return live_status


def require_live_expected_date_match(
    state: dict,
    live_status: dict | None,
    validation_replay_main_price_date: str = "",
) -> dict:
    if live_status is None:
        state.update(
            {
                "market_session_validation_scope": (
                    "branch_source_ref_validation_replay"
                    if validation_replay_main_price_date
                    else "branch_source_ref"
                ),
                "live_market_session_status": "",
                "live_market_session_date": "",
                "live_expected_main_price_date": "",
                "validation_replay_main_price_date": validation_replay_main_price_date,
            }
        )
        return state

    live_expected = market_session_calendar.normalize_date(
        live_status.get("expected_main_price_date")
    )
    source_expected = market_session_calendar.normalize_date(
        state.get("expected_main_price_date")
    )
    main_price_date = market_session_calendar.normalize_date(state.get("main_price_date"))
    if not live_expected:
        raise DailyReportEntrypointError(
            "live market-session preflight did not produce expected_main_price_date"
        )
    if source_expected != live_expected or main_price_date != live_expected:
        raise DailyReportEntrypointError(
            "current official market-session expectation does not match origin/main; "
            f"live_expected_main_price_date={live_expected} "
            f"source_expected_main_price_date={source_expected or '<missing>'} "
            f"main_price_date={main_price_date or '<missing>'}"
        )
    if (
        validation_replay_main_price_date
        and validation_replay_main_price_date != live_expected
    ):
        raise DailyReportEntrypointError(
            "validation replay date does not match the live official expectation; "
            f"validation_replay_main_price_date={validation_replay_main_price_date} "
            f"live_expected_main_price_date={live_expected}"
        )
    state.update(
        {
            "market_session_validation_scope": (
                "live_origin_main_validation_replay"
                if validation_replay_main_price_date
                else "live_origin_main"
            ),
            "live_market_session_status": str(live_status.get("market_status") or ""),
            "live_market_session_date": market_session_calendar.normalize_date(
                live_status.get("market_session_date")
            ),
            "live_expected_main_price_date": live_expected,
            "validation_replay_main_price_date": validation_replay_main_price_date,
        }
    )
    return state


def ensure_entrypoint_can_run(
    repo_root: Path,
    source_ref: str,
    allow_dirty_code: bool,
    validation_replay_main_price_date: str = "",
) -> dict:
    validation_replay_date = normalize_validation_replay_main_price_date(
        validation_replay_main_price_date
    )
    live_status = resolve_live_market_session_for_entrypoint(
        repo_root,
        source_ref,
        validation_replay_date,
    )
    try:
        state = resolve_daily_report_source_state(
            repo_root=repo_root,
            source_ref=source_ref,
            fetch=True,
            require_git_clean=True,
            allow_dirty=allow_dirty_code,
            require_local_match=False,
            validation_replay_main_price_date=validation_replay_date,
        )
    except DailyReportSourceError as exc:
        raise DailyReportEntrypointError("\n".join(exc.errors)) from exc
    return require_live_expected_date_match(
        state,
        live_status,
        validation_replay_date,
    )


def add_source_worktree(repo_root: Path, source_ref: str, temp_root: Path) -> Path:
    temp_root.mkdir(parents=True, exist_ok=True)
    try:
        return create_registered_full_temp_worktree(
            repo_root,
            source_ref,
            temp_root,
            leaf_name="origin_main_daily_report_source",
            consumer_id="chatgpt_daily_report_entrypoint",
        )
    except GitWorktreeSafetyError as exc:
        raise DailyReportEntrypointError(str(exc)) from exc


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


def run_generator(source_root: Path, output_dir: Path, source_ref: str) -> list[Path]:
    source_generator = source_root / GENERATOR_RELATIVE_PATH
    env = os.environ.copy()
    env["CHATGPT_DAILY_REPORT_ENTRYPOINT"] = "1"
    env["CHATGPT_DAILY_REPO_ROOT"] = str(source_root)
    env["CHATGPT_DAILY_OUTPUT_DIR"] = str(output_dir)
    env["CHATGPT_DAILY_SOURCE_REF"] = source_ref
    env["PYTHONIOENCODING"] = "utf-8"
    proc = run_command(
        [
            sys.executable,
            str(source_generator),
            "--repo-root",
            str(source_root),
            "--output-dir",
            str(output_dir),
        ],
        cwd=source_root,
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


def pdf_outputs_for_manifest(pdf_paths: list[Path]) -> list[dict[str, object]]:
    if len(pdf_paths) != len(PDF_OUTPUT_ROLES):
        raise DailyReportEntrypointError(
            f"runtime manifest requires {len(PDF_OUTPUT_ROLES)} PDF outputs, got {len(pdf_paths)}"
        )
    return [
        {
            "pdf_role": role,
            "pdf_index": index,
            "path": str(path),
        }
        for index, (role, path) in enumerate(zip(PDF_OUTPUT_ROLES, pdf_paths), start=1)
    ]


def write_runtime_manifest(
    output_dir: Path,
    entry_state: dict,
    source_state: dict,
    pdf_paths: list[Path],
    source_root: Path,
) -> Path:
    semantic_manifest_path = output_dir / SEMANTIC_MANIFEST_NAME
    if not semantic_manifest_path.exists():
        raise DailyReportEntrypointError(f"semantic PDF manifest missing: {semantic_manifest_path}")
    manifest = {
        "manifest_type": "chatgpt_daily_report_runtime_manifest",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "official_entrypoint": "scripts/run_chatgpt_daily_report_entrypoint.py",
        "renderer": "scripts/generate_chatgpt_side_daily_reports.py",
        "source_ref": entry_state["source_ref"],
        "source_commit_sha": entry_state["source_commit_sha"],
        "clean_source_commit_sha": source_state["source_commit_sha"],
        "market_session_status": entry_state["market_session_status"],
        "market_session_date": entry_state["market_session_date"],
        "expected_main_price_date": entry_state["expected_main_price_date"],
        "market_session_validation_scope": entry_state.get("market_session_validation_scope", ""),
        "live_market_session_status": entry_state.get("live_market_session_status", ""),
        "live_market_session_date": entry_state.get("live_market_session_date", ""),
        "live_expected_main_price_date": entry_state.get("live_expected_main_price_date", ""),
        "validation_replay_main_price_date": entry_state.get(
            "validation_replay_main_price_date", ""
        ),
        "main_price_date": entry_state["main_price_date"],
        "report_ready": entry_state["report_ready"],
        "warrant_ready": entry_state["warrant_ready"],
        "daily_pdf_ready": entry_state["daily_pdf_ready"],
        "freshness_path": entry_state["freshness_path"],
        "readme_path": entry_state["readme_path"],
        "packet_path": entry_state["packet_path"],
        "source_worktree": str(source_root),
        "output_dir": str(output_dir),
        "pdf_count": len(pdf_paths),
        "pdf_paths": [str(path) for path in pdf_paths],
        "pdf_outputs": pdf_outputs_for_manifest(pdf_paths),
        "semantic_manifest_path": str(semantic_manifest_path),
    }
    manifest_path = output_dir / RUNTIME_MANIFEST_NAME
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest_path


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
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Output directory. Defaults to "
            f"<repo-root>/{DEFAULT_OUTPUT_ROOT_NAME}/<main_price_date> after the source gate passes."
        ),
    )
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
    parser.add_argument(
        "--validation-replay-main-price-date",
        default="",
        help=(
            "CI validation only. Permit an exact report-date replay after the clock crosses into "
            "a scheduled closed market day. For origin/main the value must also equal the live "
            "expected date; every source ref must match its committed expected/main price dates."
        ),
    )
    return parser.parse_args()


def main() -> int:
    configure_stdio()
    args = parse_args()
    repo_root = args.repo_root.expanduser().resolve()

    try:
        state = ensure_entrypoint_can_run(
            repo_root=repo_root,
            source_ref=args.source_ref,
            allow_dirty_code=args.allow_dirty_code,
            validation_replay_main_price_date=args.validation_replay_main_price_date,
        )
        output_dir = (
            args.output_dir.expanduser().resolve()
            if args.output_dir is not None
            else (repo_root / DEFAULT_OUTPUT_ROOT_NAME / str(state["main_price_date"])).resolve()
        )
        print(
            "official daily report source gate passed: "
            f"source_ref={state['source_ref']} "
            f"source_commit_sha={state['source_commit_sha']} "
            f"market_session_status={state['market_session_status']} "
            f"expected_main_price_date={state['expected_main_price_date']} "
            f"market_session_validation_scope={state['market_session_validation_scope']} "
            f"live_expected_main_price_date={state['live_expected_main_price_date']} "
            f"validation_replay_main_price_date={state.get('validation_replay_main_price_date', '')} "
            f"main_price_date={state['main_price_date']} "
            f"report_ready={state['report_ready']} "
            f"warrant_ready={state['warrant_ready']} "
            f"daily_pdf_ready={state['daily_pdf_ready']}"
        )
        if not args.source_gate_only:
            ensure_local_dfkai_font_for_pdf_rendering()

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
                    validation_replay_main_price_date=state.get(
                        "validation_replay_main_price_date", ""
                    ),
                )
                print(
                    "temporary clean source worktree verified: "
                    f"path={source_root} "
                    f"main_price_date={temp_state['main_price_date']}"
                )
                if args.source_gate_only:
                    return 0
                output_dir.mkdir(parents=True, exist_ok=True)
                paths = run_generator(source_root, output_dir, args.source_ref)
                manifest_path = write_runtime_manifest(output_dir, state, temp_state, paths, source_root)
                print("official ChatGPT-side daily PDF generation completed")
                print(f"runtime_manifest={manifest_path}")
                for path in paths:
                    print(path)
            finally:
                if args.keep_source_worktree:
                    print(f"temporary source worktree kept: {source_root}")
                else:
                    remove_source_worktree(repo_root, source_root)
    except DailyReportMarketClosed as exc:
        print(f"休市，無新報告: {exc}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
