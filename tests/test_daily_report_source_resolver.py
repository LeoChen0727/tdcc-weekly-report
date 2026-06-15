from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts.resolve_daily_report_source_state import (
    DailyReportSourceError,
    forbid_helper_source,
    resolve_daily_report_source_state,
)


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


def write_sources(repo: Path, date: str = "20260615", **overrides: str) -> None:
    row = {
        "generated_at": "2026-06-15 20:31:25",
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
        "daily_pdf_ready": "True",
        "daily_pdf_ready_note": "core daily data and warrant layer are ready",
        "stock_monitor_note": "ready",
        "all_candidates_note": "ready",
        "official_fetch_note": "ready",
        "warrant_note": "ready",
    }
    row.update(overrides)

    csv_path = repo / "output" / "latest" / "data_freshness_latest.csv"
    csv_path.write_text(
        ",".join(row.keys()) + "\n" + ",".join(str(value) for value in row.values()) + "\n",
        encoding="utf-8",
    )

    readme = {
        "main_price_date": row["main_price_date"],
        "report_ready": row["report_ready"],
        "warrant_flow_date": row["warrant_flow_date"],
        "warrant_ready": row["warrant_ready"],
        "daily_pdf_ready": row["daily_pdf_ready"],
        "commit_sha": "1" * 40,
    }
    (repo / "output" / "latest" / "READ_ME_FIRST_DAILY_REPORT.txt").write_text(
        "\n".join(f"{key}={value}" for key, value in readme.items()) + "\n",
        encoding="utf-8",
    )


def commit_all(repo: Path, message: str) -> str:
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", message)
    return run_git(repo, "rev-parse", "HEAD")


def point_origin_main(repo: Path, commit: str) -> None:
    run_git(repo, "update-ref", "refs/remotes/origin/main", commit)


def test_resolver_reads_origin_main_without_wall_clock_date(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, date="20260615")
    head = commit_all(repo, "ready sources")
    point_origin_main(repo, head)

    state = resolve_daily_report_source_state(
        repo,
        fetch=False,
        require_git_clean=True,
        require_local_match=True,
    )

    assert state["source_ref"] == "origin/main"
    assert state["main_price_date"] == "20260615"
    assert state["report_ready"] is True
    assert state["warrant_ready"] is True
    assert state["daily_pdf_ready"] is True
    assert state["allow_report_generation"] is True


def test_resolver_rejects_not_ready_origin_main(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, daily_pdf_ready="False")
    head = commit_all(repo, "not ready")
    point_origin_main(repo, head)

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(repo, fetch=False, require_git_clean=True)

    assert any("daily_pdf_ready" in error for error in excinfo.value.errors)


def test_resolver_rejects_local_latest_that_does_not_match_origin_main(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, date="20260612")
    old_commit = commit_all(repo, "old local")
    write_sources(repo, date="20260615")
    new_commit = commit_all(repo, "new origin")
    point_origin_main(repo, new_commit)
    run_git(repo, "checkout", "--detach", old_commit)

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(repo, fetch=False, require_git_clean=True)

    assert any("local main_price_date=20260612" in error for error in excinfo.value.errors)
    assert any("origin/main main_price_date=20260615" in error for error in excinfo.value.errors)


def test_resolver_rejects_onedrive_helper_source() -> None:
    with pytest.raises(DailyReportSourceError) as excinfo:
        forbid_helper_source(Path("C:/Users/example/OneDrive/helper-copy"))

    assert any("OneDrive/helper" in error for error in excinfo.value.errors)
