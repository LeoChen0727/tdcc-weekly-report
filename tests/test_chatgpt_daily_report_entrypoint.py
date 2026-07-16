from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts import run_chatgpt_daily_report_entrypoint as entrypoint
from scripts.resolve_daily_report_source_state import resolve_daily_report_source_state
from scripts.run_chatgpt_daily_report_entrypoint import add_source_worktree, remove_source_worktree


ROOT = Path(__file__).resolve().parents[1]


def _runner_must_not_run(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
    raise AssertionError(f"DFKai installer must not run: args={args} kwargs={kwargs}")


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


def init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    run_git(tmp_path, "init", "repo")
    run_git(repo, "config", "user.email", "test@example.invalid")
    run_git(repo, "config", "user.name", "Test User")
    (repo / "output" / "latest").mkdir(parents=True)
    return repo


def write_ready_sources(repo: Path, date: str = "20260616") -> None:
    row = {
        "generated_at": "2026-06-16 20:31:25",
        "market_session_status": "open_confirmed",
        "market_session_date": date,
        "expected_main_price_date": date,
        "market_session_reason_code": "twse_tpex_target_date_confirmed",
        "main_price_date": date,
        "actual_stock_price_history_date": date,
        "stock_monitor_price_date": date,
        "all_candidates_date": date,
        "official_price_fetch_date": date,
        "warrant_flow_date": date,
        "raw_stock_monitor_price_date": date,
        "raw_all_candidates_date": date,
        "raw_official_price_fetch_date": date,
        "raw_warrant_flow_date": date,
        "report_ready": "True",
        "report_ready_note": "core daily data dates match main_price_date",
        "warrant_ready": "True",
        "warrant_ready_note": "warrant_flow_date matches main_price_date",
        "warrant_source_status": "ok",
        "warrant_source_status_note": "current-date warrant layer ready",
        "warrant_source_consecutive_unavailable_days": "0",
        "warrant_source_max_warning_days": "2",
        "warrant_daily_publish_allowed": "True",
        "warrant_pdf_visibility": "visible",
        "warrant_model_effect_allowed": "True",
        "warrant_pdf_effect_allowed": "True",
        "daily_pdf_ready": "True",
        "daily_pdf_ready_note": "core daily data and warrant layer are ready",
        "stock_monitor_note": "ready",
        "all_candidates_note": "ready",
        "official_fetch_note": "ready",
        "warrant_note": "ready",
    }
    (repo / "output" / "latest" / "data_freshness_latest.csv").write_text(
        ",".join(row.keys()) + "\n" + ",".join(row.values()) + "\n",
        encoding="utf-8",
    )
    readme = {
        "main_price_date": date,
        "report_ready": "True",
        "warrant_flow_date": date,
        "warrant_ready": "True",
        "warrant_daily_publish_allowed": "True",
        "warrant_pdf_visibility": "visible",
        "daily_pdf_ready": "True",
        "commit_sha": "1" * 40,
    }
    (repo / "output" / "latest" / "READ_ME_FIRST_DAILY_REPORT.txt").write_text(
        "\n".join(f"{key}={value}" for key, value in readme.items()) + "\n",
        encoding="utf-8",
    )
    packet = {
        "generated_at": "2026-06-16 20:31:25 Asia/Taipei",
        "repo": "LeoChen0727/tdcc-weekly-report",
        "main_price_date": date,
        "report_ready": "True",
        "all_candidates_date": date,
        "official_price_fetch_date": date,
        "stock_monitor_date": date,
        "warrant_flow_date": date,
        "warrant_ready": "True",
        "warrant_daily_publish_allowed": "True",
        "warrant_pdf_visibility": "visible",
        "daily_pdf_ready": "True",
    }
    packet_text = "\n".join(
        [
            "CHATGPT DAILY REPORT PACKET",
            "",
            *(f"{key}: {value}" for key, value in packet.items()),
            "",
            "CHATGPT_DELIVERY_CONTRACT",
            "official_chatgpt_side_pdf_entrypoint: python scripts/run_chatgpt_daily_report_entrypoint.py",
            "",
        ]
    )
    (repo / "output" / "latest" / "chatgpt_daily_report_packet_latest.txt").write_text(
        packet_text,
        encoding="utf-8",
    )
    (repo / "output" / "latest" / "market_session_status_latest.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "generated_at": "2026-06-16T20:31:25+08:00",
                "phase": "confirm",
                "assessment_date": date,
                "market_session_date": date,
                "market_status": "open_confirmed",
                "expected_main_price_date": date,
                "should_run_daily_pipeline": True,
                "reason_code": "twse_tpex_target_date_confirmed",
            }
        )
        + "\n",
        encoding="utf-8",
    )


def commit_all(repo: Path, message: str) -> str:
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", message)
    return run_git(repo, "rev-parse", "HEAD")


def point_origin_main(repo: Path, commit: str) -> None:
    run_git(repo, "update-ref", "refs/remotes/origin/main", commit)


@pytest.mark.parametrize("configured_font_path", [False, True])
def test_local_dfkai_preflight_reuses_valid_existing_font_without_install(
    tmp_path: Path,
    configured_font_path: bool,
) -> None:
    font_path = tmp_path / "kaiu.ttf"
    font_path.write_bytes(b"valid-for-mocked-validator")
    validated: list[Path] = []

    def fake_validator(path: Path) -> Path:
        validated.append(path)
        return path

    result = entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
        font_path=font_path,
        configured_font_path=configured_font_path,
        platform_name="win32",
        default_font_path=font_path,
        runner=_runner_must_not_run,
        validator=fake_validator,
    )

    assert result == font_path
    assert validated == [font_path]


def test_local_dfkai_preflight_rejects_invalid_existing_font_without_install(tmp_path: Path) -> None:
    font_path = tmp_path / "kaiu.ttf"
    font_path.write_bytes(b"invalid")

    def reject_font(path: Path) -> Path:
        raise RuntimeError(f"invalid font: {path}")

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="automatic install is forbidden"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            runner=_runner_must_not_run,
            validator=reject_font,
        )


def test_local_dfkai_preflight_rejects_missing_configured_path_without_install(tmp_path: Path) -> None:
    font_path = tmp_path / "configured" / "kaiu.ttf"

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="configured DFKai font path is missing"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=True,
            platform_name="win32",
            default_font_path=font_path,
            runner=_runner_must_not_run,
        )


def test_local_dfkai_preflight_derives_missing_configured_path_from_environment(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    font_path = tmp_path / "configured" / "kaiu.ttf"
    monkeypatch.setenv(entrypoint.CHATGPT_DAILY_DFKAI_FONT_PATH_ENV, str(font_path))

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="configured DFKai font path is missing"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            platform_name="win32",
            default_font_path=font_path,
            runner=_runner_must_not_run,
        )


def test_local_dfkai_preflight_rejects_missing_font_off_windows_without_install(tmp_path: Path) -> None:
    font_path = tmp_path / "kaiu.ttf"

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="supported only on Windows"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="linux",
            default_font_path=font_path,
            runner=_runner_must_not_run,
        )


def test_local_dfkai_preflight_rejects_unconfigured_noncanonical_target_without_install(
    tmp_path: Path,
) -> None:
    font_path = tmp_path / "other-fonts" / "kaiu.ttf"
    canonical_path = tmp_path / "Windows" / "Fonts" / "kaiu.ttf"

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="refuses a non-canonical target path"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=canonical_path,
            runner=_runner_must_not_run,
        )


def test_local_dfkai_preflight_installs_missing_windows_default_once(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"
    captured: list[tuple[list[str], dict[str, object]]] = []
    validated: list[Path] = []

    def fake_runner(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        captured.append((list(command), dict(kwargs)))
        font_path.parent.mkdir(parents=True)
        font_path.write_bytes(b"installed-for-mocked-validator")
        return subprocess.CompletedProcess(command, 0, stdout="installed", stderr="")

    def fake_validator(path: Path) -> Path:
        validated.append(path)
        return path

    system_root = tmp_path / "Windows"
    result = entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
        font_path=font_path,
        configured_font_path=False,
        platform_name="win32",
        default_font_path=font_path,
        system_root=system_root,
        runner=fake_runner,
        validator=fake_validator,
    )

    assert result == font_path
    assert validated == [font_path]
    assert len(captured) == 1
    command, kwargs = captured[0]
    assert command == [
        str(system_root / "System32" / "dism.exe"),
        "/Online",
        "/Add-Capability",
        "/CapabilityName:Language.Fonts.Hant~~~und-HANT~0.0.1.0",
        "/NoRestart",
    ]
    assert kwargs["timeout"] == 1200
    assert kwargs["check"] is False
    assert kwargs["shell"] is False


def test_local_dfkai_preflight_accepts_nonzero_when_final_font_is_valid(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"
    runner_calls = 0
    validated: list[Path] = []

    def completed_nonzero_runner(
        command: list[str],
        **kwargs: object,
    ) -> subprocess.CompletedProcess[str]:
        nonlocal runner_calls
        runner_calls += 1
        font_path.parent.mkdir(parents=True)
        font_path.write_bytes(b"installed-for-mocked-validator")
        return subprocess.CompletedProcess(
            command,
            183,
            stdout="The file already exists",
            stderr="",
        )

    def fake_validator(path: Path) -> Path:
        validated.append(path)
        return path

    result = entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
        font_path=font_path,
        configured_font_path=False,
        platform_name="win32",
        default_font_path=font_path,
        system_root=tmp_path / "Windows",
        runner=completed_nonzero_runner,
        validator=fake_validator,
    )

    captured = capsys.readouterr()
    assert result == font_path
    assert runner_calls == 1
    assert validated == [font_path]
    assert "dfkai_preflight_warning=nonzero_but_final_state_valid" in captured.err
    assert "exit_code=183" in captured.err
    assert "dfkai_preflight_action=installed_and_validated" in captured.out


def test_local_dfkai_preflight_fails_closed_on_dism_error(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"
    calls = 0

    def failed_runner(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        calls += 1
        return subprocess.CompletedProcess(command, 5, stdout="", stderr="access denied")

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="exit_code=5") as exc_info:
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            system_root=tmp_path / "Windows",
            runner=failed_runner,
            validator=_runner_must_not_run,
        )
    assert calls == 1
    assert "detail=access denied" in str(exc_info.value)


def test_local_dfkai_preflight_fails_closed_on_dism_timeout(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"

    def timeout_runner(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        raise subprocess.TimeoutExpired(command, kwargs["timeout"])

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="will not be retried"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            system_root=tmp_path / "Windows",
            runner=timeout_runner,
        )


def test_local_dfkai_preflight_fails_closed_when_dism_cannot_start(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"
    calls = 0

    def missing_dism_runner(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        calls += 1
        raise OSError("dism unavailable")

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="could not start"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            system_root=tmp_path / "Windows",
            runner=missing_dism_runner,
        )
    assert calls == 1


def test_local_dfkai_preflight_rejects_dism_success_without_font_file(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"

    def no_file_runner(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(command, 0, stdout="success", stderr="")

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="font file is still missing"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            system_root=tmp_path / "Windows",
            runner=no_file_runner,
        )


def test_local_dfkai_preflight_rejects_invalid_font_after_install(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"

    def install_invalid_font(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        font_path.parent.mkdir(parents=True)
        font_path.write_bytes(b"invalid")
        return subprocess.CompletedProcess(command, 0, stdout="success", stderr="")

    def reject_font(path: Path) -> Path:
        raise RuntimeError(f"invalid font: {path}")

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="failed validation after"):
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            system_root=tmp_path / "Windows",
            runner=install_invalid_font,
            validator=reject_font,
        )


def test_local_dfkai_preflight_rejects_nonzero_when_final_font_is_invalid(tmp_path: Path) -> None:
    font_path = tmp_path / "Fonts" / "kaiu.ttf"
    runner_calls = 0
    validator_calls = 0

    def install_invalid_font(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        nonlocal runner_calls
        runner_calls += 1
        font_path.parent.mkdir(parents=True)
        font_path.write_bytes(b"invalid")
        return subprocess.CompletedProcess(command, 183, stdout="already exists", stderr="")

    def reject_font(path: Path) -> Path:
        nonlocal validator_calls
        validator_calls += 1
        raise RuntimeError(f"invalid font identity or cmap: {path}")

    with pytest.raises(entrypoint.DailyReportEntrypointError, match="exit_code=183") as exc_info:
        entrypoint.ensure_local_dfkai_font_for_pdf_rendering(
            font_path=font_path,
            configured_font_path=False,
            platform_name="win32",
            default_font_path=font_path,
            system_root=tmp_path / "Windows",
            runner=install_invalid_font,
            validator=reject_font,
        )

    assert runner_calls == 1
    assert validator_calls == 1
    assert "validation_error=invalid font identity or cmap" in str(exc_info.value)


def test_direct_chatgpt_side_pdf_generator_cli_is_blocked() -> None:
    proc = subprocess.run(
        [sys.executable, "scripts/generate_chatgpt_side_daily_reports.py", "--help"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode != 0
    assert "direct ChatGPT-side daily PDF generator invocation is blocked" in proc.stderr
    assert "scripts/run_chatgpt_daily_report_entrypoint.py" in proc.stderr


def test_entrypoint_temp_source_worktree_matches_origin_main(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_ready_sources(repo, date="20260616")
    head = commit_all(repo, "ready daily sources")
    point_origin_main(repo, head)

    source_root = add_source_worktree(repo, "origin/main", tmp_path / "worktrees")
    try:
        state = resolve_daily_report_source_state(
            source_root,
            fetch=False,
            require_git_clean=True,
            require_local_match=True,
        )
    finally:
        remove_source_worktree(repo, source_root)

    assert state["source_ref"] == "origin/main"
    assert state["main_price_date"] == "20260616"
    assert state["report_ready"] is True
    assert state["warrant_ready"] is True
    assert state["daily_pdf_ready"] is True


def test_entrypoint_runs_generator_from_clean_source_worktree(tmp_path: Path, monkeypatch) -> None:
    captured: dict[str, object] = {}
    pdf_paths = "\n".join(str(tmp_path / f"report_{i}.pdf") for i in range(6))

    def fake_run_command(
        args: list[str],
        cwd: Path,
        env: dict[str, str] | None = None,
        capture_output: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        captured["args"] = list(args)
        captured["cwd"] = cwd
        captured["env"] = dict(env or {})
        return subprocess.CompletedProcess(args=args, returncode=0, stdout=pdf_paths, stderr="")

    monkeypatch.setattr(entrypoint, "run_command", fake_run_command)

    paths = entrypoint.run_generator(
        source_root=tmp_path,
        output_dir=tmp_path,
        source_ref="histlocal/codex/historical-report-source-20260615",
    )

    assert len(paths) == 6
    assert captured["args"] == [
        sys.executable,
        str(tmp_path / "scripts" / "generate_chatgpt_side_daily_reports.py"),
        "--repo-root",
        str(tmp_path),
        "--output-dir",
        str(tmp_path),
    ]
    assert captured["cwd"] == tmp_path
    env = captured["env"]
    assert isinstance(env, dict)
    assert env["CHATGPT_DAILY_REPORT_ENTRYPOINT"] == "1"
    assert env["CHATGPT_DAILY_REPO_ROOT"] == str(tmp_path)
    assert env["CHATGPT_DAILY_SOURCE_REF"] == "histlocal/codex/historical-report-source-20260615"


def _resolved_state(date: str) -> dict[str, object]:
    return {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "market_session_status": "open_confirmed",
        "market_session_date": date,
        "expected_main_price_date": date,
        "main_price_date": date,
    }


def test_source_gate_only_skips_dfkai_preflight_and_pdf_rendering(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_ref = "origin/main"
    date = "20260616"
    state = {
        "source_ref": source_ref,
        "source_commit_sha": "a" * 40,
        "market_session_status": "open_confirmed",
        "expected_main_price_date": date,
        "market_session_validation_scope": "test",
        "live_expected_main_price_date": date,
        "main_price_date": date,
        "report_ready": True,
        "warrant_ready": True,
        "daily_pdf_ready": True,
    }
    args = entrypoint.argparse.Namespace(
        repo_root=tmp_path,
        source_ref=source_ref,
        output_dir=None,
        source_gate_only=True,
        allow_dirty_code=True,
        keep_source_worktree=False,
    )
    source_root = tmp_path / "verified-source"

    monkeypatch.setattr(entrypoint, "parse_args", lambda: args)
    monkeypatch.setattr(entrypoint, "ensure_entrypoint_can_run", lambda **kwargs: state)
    monkeypatch.setattr(entrypoint, "add_source_worktree", lambda *args, **kwargs: source_root)
    monkeypatch.setattr(entrypoint, "resolve_daily_report_source_state", lambda **kwargs: state)
    monkeypatch.setattr(entrypoint, "remove_source_worktree", lambda *args, **kwargs: None)
    monkeypatch.setattr(entrypoint, "ensure_local_dfkai_font_for_pdf_rendering", _runner_must_not_run)
    monkeypatch.setattr(entrypoint, "run_generator", _runner_must_not_run)

    assert entrypoint.main() == 0


def test_normal_render_calls_dfkai_preflight_once_before_generator(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_ref = "origin/main"
    date = "20260616"
    state = {
        "source_ref": source_ref,
        "source_commit_sha": "a" * 40,
        "market_session_status": "open_confirmed",
        "expected_main_price_date": date,
        "market_session_validation_scope": "test",
        "live_expected_main_price_date": date,
        "main_price_date": date,
        "report_ready": True,
        "warrant_ready": True,
        "daily_pdf_ready": True,
    }
    output_dir = tmp_path / "official-output"
    args = entrypoint.argparse.Namespace(
        repo_root=tmp_path,
        source_ref=source_ref,
        output_dir=output_dir,
        source_gate_only=False,
        allow_dirty_code=True,
        keep_source_worktree=False,
    )
    source_root = tmp_path / "verified-source"
    events: list[str] = []

    monkeypatch.setattr(entrypoint, "parse_args", lambda: args)
    monkeypatch.setattr(
        entrypoint,
        "ensure_entrypoint_can_run",
        lambda **kwargs: events.append("source_gate") or state,
    )
    monkeypatch.setattr(
        entrypoint,
        "ensure_local_dfkai_font_for_pdf_rendering",
        lambda: events.append("preflight") or Path(r"C:\Windows\Fonts\kaiu.ttf"),
    )
    monkeypatch.setattr(
        entrypoint,
        "add_source_worktree",
        lambda *args, **kwargs: events.append("worktree") or source_root,
    )
    monkeypatch.setattr(entrypoint, "resolve_daily_report_source_state", lambda **kwargs: state)
    monkeypatch.setattr(
        entrypoint,
        "run_generator",
        lambda *args, **kwargs: events.append("generator") or [output_dir / f"report_{idx}.pdf" for idx in range(6)],
    )
    monkeypatch.setattr(
        entrypoint,
        "write_runtime_manifest",
        lambda *args, **kwargs: output_dir / entrypoint.RUNTIME_MANIFEST_NAME,
    )
    monkeypatch.setattr(entrypoint, "remove_source_worktree", lambda *args, **kwargs: None)

    assert entrypoint.main() == 0
    assert events.count("preflight") == 1
    assert events == ["source_gate", "preflight", "worktree", "generator"]


def test_dfkai_preflight_failure_stops_before_temp_worktree_and_generator(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source_ref = "origin/main"
    date = "20260616"
    state = {
        "source_ref": source_ref,
        "source_commit_sha": "a" * 40,
        "market_session_status": "open_confirmed",
        "expected_main_price_date": date,
        "market_session_validation_scope": "test",
        "live_expected_main_price_date": date,
        "main_price_date": date,
        "report_ready": True,
        "warrant_ready": True,
        "daily_pdf_ready": True,
    }
    args = entrypoint.argparse.Namespace(
        repo_root=tmp_path,
        source_ref=source_ref,
        output_dir=tmp_path / "official-output",
        source_gate_only=False,
        allow_dirty_code=True,
        keep_source_worktree=False,
    )

    def fail_preflight() -> Path:
        raise entrypoint.DailyReportEntrypointError("DFKai preflight test failure")

    monkeypatch.setattr(entrypoint, "parse_args", lambda: args)
    monkeypatch.setattr(entrypoint, "ensure_entrypoint_can_run", lambda **kwargs: state)
    monkeypatch.setattr(entrypoint, "ensure_local_dfkai_font_for_pdf_rendering", fail_preflight)
    monkeypatch.setattr(entrypoint.tempfile, "TemporaryDirectory", _runner_must_not_run)
    monkeypatch.setattr(entrypoint, "add_source_worktree", _runner_must_not_run)
    monkeypatch.setattr(entrypoint, "run_generator", _runner_must_not_run)

    assert entrypoint.main() == 1


def test_source_gate_failure_stops_before_dfkai_preflight_and_temp_worktree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    args = entrypoint.argparse.Namespace(
        repo_root=tmp_path,
        source_ref="origin/main",
        output_dir=tmp_path / "official-output",
        source_gate_only=False,
        allow_dirty_code=False,
        keep_source_worktree=False,
    )

    def fail_source_gate(**kwargs: object) -> dict[str, object]:
        raise entrypoint.DailyReportEntrypointError("source gate test failure")

    monkeypatch.setattr(entrypoint, "parse_args", lambda: args)
    monkeypatch.setattr(entrypoint, "ensure_entrypoint_can_run", fail_source_gate)
    monkeypatch.setattr(entrypoint, "ensure_local_dfkai_font_for_pdf_rendering", _runner_must_not_run)
    monkeypatch.setattr(entrypoint.tempfile, "TemporaryDirectory", _runner_must_not_run)
    monkeypatch.setattr(entrypoint, "add_source_worktree", _runner_must_not_run)
    monkeypatch.setattr(entrypoint, "run_generator", _runner_must_not_run)

    assert entrypoint.main() == 1


def _live_preflight(
    date: str,
    *,
    status: str = "unknown",
    reason_code: str = "awaiting_official_price_confirmation",
) -> dict[str, object]:
    return {
        "market_status": status,
        "market_session_date": date,
        "expected_main_price_date": date,
        "reason_code": reason_code,
        "reason": "test market-session result",
    }


def test_entrypoint_live_gate_rejects_stale_origin_main_date(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(
        entrypoint.market_session_calendar,
        "refresh_market_session_status",
        lambda *args, **kwargs: _live_preflight("20260713"),
    )
    monkeypatch.setattr(
        entrypoint,
        "resolve_daily_report_source_state",
        lambda **kwargs: _resolved_state("20260709"),
    )

    try:
        entrypoint.ensure_entrypoint_can_run(tmp_path, "origin/main", False)
    except entrypoint.DailyReportEntrypointError as exc:
        text = str(exc)
        assert "live_expected_main_price_date=20260713" in text
        assert "source_expected_main_price_date=20260709" in text
        assert "main_price_date=20260709" in text
    else:
        raise AssertionError("stale origin/main must not pass the live expected-date gate")


def test_entrypoint_live_gate_accepts_matching_origin_main_date(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(
        entrypoint.market_session_calendar,
        "refresh_market_session_status",
        lambda *args, **kwargs: _live_preflight("20260713"),
    )
    monkeypatch.setattr(
        entrypoint,
        "resolve_daily_report_source_state",
        lambda **kwargs: _resolved_state("20260713"),
    )

    state = entrypoint.ensure_entrypoint_can_run(tmp_path, "origin/main", False)

    assert state["market_session_validation_scope"] == "live_origin_main"
    assert state["live_expected_main_price_date"] == "20260713"


def test_entrypoint_live_gate_reports_closed_market_without_rendering(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(
        entrypoint.market_session_calendar,
        "refresh_market_session_status",
        lambda *args, **kwargs: _live_preflight(
            "20260710",
            status="closed_emergency",
            reason_code="taipei_work_suspension_full_day",
        ),
    )

    try:
        entrypoint.ensure_entrypoint_can_run(tmp_path, "origin/main", False)
    except entrypoint.DailyReportMarketClosed as exc:
        assert "market_status=closed_emergency" in str(exc)
        assert "market_session_date=20260710" in str(exc)
    else:
        raise AssertionError("closed market must stop before source resolution and rendering")


def test_entrypoint_branch_replay_uses_committed_branch_contract_without_live_gate(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        entrypoint.market_session_calendar,
        "refresh_market_session_status",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("live gate must not run")),
    )
    monkeypatch.setattr(
        entrypoint,
        "resolve_daily_report_source_state",
        lambda **kwargs: _resolved_state("20260709"),
    )

    state = entrypoint.ensure_entrypoint_can_run(
        tmp_path,
        "origin/codex/source-integrity-test",
        False,
    )

    assert state["market_session_validation_scope"] == "branch_source_ref"
    assert state["live_expected_main_price_date"] == ""


def test_entrypoint_writes_runtime_manifest(tmp_path: Path) -> None:
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "market_session_status": "open_confirmed",
        "market_session_date": "20260616",
        "expected_main_price_date": "20260616",
        "market_session_validation_scope": "live_origin_main",
        "live_market_session_status": "unknown",
        "live_market_session_date": "20260616",
        "live_expected_main_price_date": "20260616",
        "main_price_date": "20260616",
        "report_ready": True,
        "warrant_ready": True,
        "daily_pdf_ready": True,
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    pdf_paths = [tmp_path / f"report_{idx}.pdf" for idx in range(6)]
    (tmp_path / entrypoint.SEMANTIC_MANIFEST_NAME).write_text(
        "manifest_type\nchatgpt_daily_pdf_semantic_manifest\n",
        encoding="utf-8",
    )

    manifest_path = entrypoint.write_runtime_manifest(
        output_dir=tmp_path,
        entry_state=state,
        source_state=state,
        pdf_paths=pdf_paths,
        source_root=tmp_path / "source",
    )

    text = manifest_path.read_text(encoding="utf-8")
    assert "chatgpt_daily_report_runtime_manifest" in text
    assert '"expected_main_price_date": "20260616"' in text
    assert '"live_expected_main_price_date": "20260616"' in text
    assert '"main_price_date": "20260616"' in text
    assert "chatgpt_daily_report_packet_latest.txt" in text
    assert '"pdf_count": 6' in text
    manifest = json.loads(text)
    assert [output["pdf_role"] for output in manifest["pdf_outputs"]] == list(entrypoint.PDF_OUTPUT_ROLES)
    assert [output["pdf_index"] for output in manifest["pdf_outputs"]] == [1, 2, 3, 4, 5, 6]
    assert [output["path"] for output in manifest["pdf_outputs"]] == [str(path) for path in pdf_paths]
    assert manifest["semantic_manifest_path"] == str(tmp_path / entrypoint.SEMANTIC_MANIFEST_NAME)


def test_entrypoint_runtime_manifest_requires_semantic_manifest(tmp_path: Path) -> None:
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "market_session_status": "open_confirmed",
        "market_session_date": "20260616",
        "expected_main_price_date": "20260616",
        "main_price_date": "20260616",
        "report_ready": True,
        "warrant_ready": True,
        "daily_pdf_ready": True,
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    pdf_paths = [tmp_path / f"report_{idx}.pdf" for idx in range(6)]

    try:
        entrypoint.write_runtime_manifest(
            output_dir=tmp_path,
            entry_state=state,
            source_state=state,
            pdf_paths=pdf_paths,
            source_root=tmp_path / "source",
        )
    except entrypoint.DailyReportEntrypointError as exc:
        assert "semantic PDF manifest missing" in str(exc)
    else:  # pragma: no cover - explicit failure message for regressions.
        raise AssertionError("write_runtime_manifest must require the semantic manifest")
