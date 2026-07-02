from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from scripts import run_chatgpt_daily_report_entrypoint as entrypoint
from scripts.resolve_daily_report_source_state import resolve_daily_report_source_state
from scripts.run_chatgpt_daily_report_entrypoint import add_source_worktree, remove_source_worktree


ROOT = Path(__file__).resolve().parents[1]


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


def commit_all(repo: Path, message: str) -> str:
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", message)
    return run_git(repo, "rev-parse", "HEAD")


def point_origin_main(repo: Path, commit: str) -> None:
    run_git(repo, "update-ref", "refs/remotes/origin/main", commit)


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


def test_entrypoint_writes_runtime_manifest(tmp_path: Path) -> None:
    state = {
        "source_ref": "origin/main",
        "source_commit_sha": "a" * 40,
        "main_price_date": "20260616",
        "report_ready": True,
        "warrant_ready": True,
        "daily_pdf_ready": True,
        "freshness_path": "origin/main:output/latest/data_freshness_latest.csv",
        "readme_path": "origin/main:output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "packet_path": "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt",
    }
    pdf_paths = [tmp_path / f"report_{idx}.pdf" for idx in range(6)]

    manifest_path = entrypoint.write_runtime_manifest(
        output_dir=tmp_path,
        entry_state=state,
        source_state=state,
        pdf_paths=pdf_paths,
        source_root=tmp_path / "source",
    )

    text = manifest_path.read_text(encoding="utf-8")
    assert "chatgpt_daily_report_runtime_manifest" in text
    assert '"main_price_date": "20260616"' in text
    assert "chatgpt_daily_report_packet_latest.txt" in text
    assert '"pdf_count": 6' in text
