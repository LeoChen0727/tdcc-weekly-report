from __future__ import annotations

import json
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
        "warrant_daily_publish_allowed": row["warrant_daily_publish_allowed"],
        "warrant_pdf_visibility": row["warrant_pdf_visibility"],
        "daily_pdf_ready": row["daily_pdf_ready"],
        "commit_sha": "1" * 40,
    }
    (repo / "output" / "latest" / "READ_ME_FIRST_DAILY_REPORT.txt").write_text(
        "\n".join(f"{key}={value}" for key, value in readme.items()) + "\n",
        encoding="utf-8",
    )

    packet = {
        "generated_at": "2026-06-15 20:31:25 Asia/Taipei",
        "repo": "LeoChen0727/tdcc-weekly-report",
        "main_price_date": row["main_price_date"],
        "report_ready": row["report_ready"],
        "all_candidates_date": row["all_candidates_date"],
        "official_price_fetch_date": row["official_price_fetch_date"],
        "stock_monitor_date": row["stock_monitor_price_date"],
        "warrant_flow_date": row["warrant_flow_date"],
        "warrant_ready": row["warrant_ready"],
        "warrant_daily_publish_allowed": row["warrant_daily_publish_allowed"],
        "warrant_pdf_visibility": row["warrant_pdf_visibility"],
        "daily_pdf_ready": row["daily_pdf_ready"],
    }
    packet_text = "\n".join(
        [
            "CHATGPT DAILY REPORT PACKET",
            "",
            *(f"{key}: {value}" for key, value in packet.items()),
            "",
            "CHATGPT_DELIVERY_CONTRACT",
            "official_chatgpt_side_pdf_entrypoint: official-entrypoint",
            "",
        ]
    )
    (repo / "output" / "latest" / "chatgpt_daily_report_packet_latest.txt").write_text(
        packet_text,
        encoding="utf-8",
    )
    market_status = {
        "schema_version": 1,
        "generated_at": "2026-06-15T20:31:25+08:00",
        "phase": "confirm",
        "assessment_date": row["market_session_date"],
        "market_session_date": row["market_session_date"],
        "market_status": row["market_session_status"],
        "expected_main_price_date": row["expected_main_price_date"],
        "should_run_daily_pipeline": row["market_session_status"] == "open_confirmed",
        "reason_code": row["market_session_reason_code"],
    }
    (repo / "output" / "latest" / "market_session_status_latest.json").write_text(
        json.dumps(market_status, ensure_ascii=False, indent=2) + "\n",
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


def test_resolver_allows_ignored_chatgpt_side_output_residue(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    (repo / ".gitignore").write_text("chatgpt_side_outputs*/\n", encoding="utf-8")
    write_sources(repo, date="20260615")
    head = commit_all(repo, "ready sources")
    point_origin_main(repo, head)
    output_dir = repo / "chatgpt_side_outputs_official"
    output_dir.mkdir()
    (output_dir / "old.pdf").write_text("not a real pdf", encoding="utf-8")

    state = resolve_daily_report_source_state(
        repo,
        fetch=False,
        require_git_clean=True,
        require_local_match=True,
    )

    assert state["main_price_date"] == "20260615"
    assert state["daily_pdf_ready"] is True


def test_resolver_allows_bounded_warrant_grace_when_warrant_effects_are_hidden(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(
        repo,
        date="20260615",
        warrant_ready="False",
        warrant_ready_note="warrant_flow_date matches main_price_date but stock-level warrant data is unavailable",
        warrant_source_status="warning_grace",
        warrant_source_status_note="current-date warrant source unavailable within bounded grace window",
        warrant_source_consecutive_unavailable_days="2",
        warrant_daily_publish_allowed="True",
        warrant_pdf_visibility="hidden_unavailable",
        warrant_model_effect_allowed="False",
        warrant_pdf_effect_allowed="False",
        daily_pdf_ready="True",
        daily_pdf_ready_note=(
            "core daily data is ready; warrant source unavailable within bounded grace, "
            "warrant_pdf_visibility=hidden_unavailable"
        ),
    )
    head = commit_all(repo, "ready sources with hidden warrant layer")
    point_origin_main(repo, head)

    state = resolve_daily_report_source_state(
        repo,
        fetch=False,
        require_git_clean=True,
        require_local_match=True,
    )

    assert state["warrant_ready"] is False
    assert state["warrant_daily_publish_allowed"] is True
    assert state["warrant_pdf_visibility"] == "hidden_unavailable"
    assert state["allow_report_generation"] is True


def test_resolver_still_rejects_non_output_dirty_files(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    (repo / ".gitignore").write_text("chatgpt_side_outputs*/\n", encoding="utf-8")
    write_sources(repo, date="20260615")
    head = commit_all(repo, "ready sources")
    point_origin_main(repo, head)
    (repo / "unexpected.txt").write_text("dirty", encoding="utf-8")

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(
            repo,
            fetch=False,
            require_git_clean=True,
            require_local_match=True,
        )

    assert any("local checkout is dirty" in error for error in excinfo.value.errors)
    assert any("unexpected.txt" in error for error in excinfo.value.errors)


def test_resolver_rejects_not_ready_origin_main(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, daily_pdf_ready="False")
    head = commit_all(repo, "not ready")
    point_origin_main(repo, head)

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(repo, fetch=False, require_git_clean=True)

    assert any("daily_pdf_ready" in error for error in excinfo.value.errors)


def test_resolver_rejects_closed_market_even_when_previous_freshness_is_ready(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, date="20260709")
    status_path = repo / "output" / "latest" / "market_session_status_latest.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    status.update(
        {
            "phase": "preflight",
            "assessment_date": "20260710",
            "market_session_date": "20260710",
            "market_status": "closed_emergency",
            "expected_main_price_date": "20260709",
            "should_run_daily_pipeline": False,
            "reason_code": "taipei_full_day_or_morning_work_suspension",
        }
    )
    status_path.write_text(json.dumps(status), encoding="utf-8")
    head = commit_all(repo, "market closed")
    point_origin_main(repo, head)

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(repo, fetch=False, require_git_clean=True)

    assert any("market_status must be open_confirmed" in error for error in excinfo.value.errors)

    with pytest.raises(DailyReportSourceError) as replay_excinfo:
        resolve_daily_report_source_state(
            repo,
            fetch=False,
            require_git_clean=True,
            validation_replay_main_price_date="20260709",
        )

    assert any(
        "market_status must be open_confirmed" in error
        for error in replay_excinfo.value.errors
    )


def test_resolver_allows_exact_closed_market_validation_replay_only(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, date="20260717")
    status_path = repo / "output" / "latest" / "market_session_status_latest.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    status.update(
        {
            "phase": "preflight",
            "assessment_date": "20260718",
            "market_session_date": "20260718",
            "market_status": "closed_scheduled",
            "expected_main_price_date": "20260717",
            "should_run_daily_pipeline": False,
            "reason_code": "weekend",
        }
    )
    status_path.write_text(json.dumps(status), encoding="utf-8")
    head = commit_all(repo, "scheduled closure after ready data")
    point_origin_main(repo, head)

    state = resolve_daily_report_source_state(
        repo,
        fetch=False,
        require_git_clean=True,
        validation_replay_main_price_date="20260717",
    )

    assert state["market_session_status"] == "closed_scheduled"
    assert state["market_session_date"] == "20260718"
    assert state["expected_main_price_date"] == "20260717"
    assert state["main_price_date"] == "20260717"
    assert state["validation_replay_main_price_date"] == "20260717"

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(
            repo,
            fetch=False,
            require_git_clean=True,
            validation_replay_main_price_date="20260716",
        )

    assert any(
        "validation_replay_main_price_date=20260716 does not match main_price_date=20260717"
        in error
        for error in excinfo.value.errors
    )

    status["market_session_date"] = "20260716"
    status_path.write_text(json.dumps(status), encoding="utf-8")
    boundary_head = commit_all(repo, "invalid scheduled closure date boundary")
    point_origin_main(repo, boundary_head)

    with pytest.raises(DailyReportSourceError) as boundary_excinfo:
        resolve_daily_report_source_state(
            repo,
            fetch=False,
            require_git_clean=True,
            validation_replay_main_price_date="20260717",
        )

    assert any(
        "market_session_date=20260716 precedes validation_replay_main_price_date=20260717"
        in error
        for error in boundary_excinfo.value.errors
    )


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


def test_resolver_can_ignore_stale_local_latest_when_entrypoint_uses_origin_main_only(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, date="20260612")
    old_commit = commit_all(repo, "old local")
    write_sources(repo, date="20260615")
    new_commit = commit_all(repo, "new origin")
    point_origin_main(repo, new_commit)
    run_git(repo, "checkout", "--detach", old_commit)

    state = resolve_daily_report_source_state(
        repo,
        fetch=False,
        require_git_clean=True,
        require_local_match=False,
    )

    assert state["main_price_date"] == "20260615"
    assert state["packet_path"] == "origin/main:output/latest/chatgpt_daily_report_packet_latest.txt"


def test_resolver_rejects_packet_that_does_not_match_freshness(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write_sources(repo, date="20260615")
    packet_path = repo / "output" / "latest" / "chatgpt_daily_report_packet_latest.txt"
    packet_path.write_text(
        packet_path.read_text(encoding="utf-8").replace("main_price_date: 20260615", "main_price_date: 20260605"),
        encoding="utf-8",
    )
    head = commit_all(repo, "stale packet")
    point_origin_main(repo, head)

    with pytest.raises(DailyReportSourceError) as excinfo:
        resolve_daily_report_source_state(repo, fetch=False, require_git_clean=True)

    assert any("packet main_price_date=20260605" in error for error in excinfo.value.errors)
    assert any("freshness main_price_date=20260615" in error for error in excinfo.value.errors)


def test_resolver_rejects_onedrive_helper_source() -> None:
    with pytest.raises(DailyReportSourceError) as excinfo:
        forbid_helper_source(Path("C:/Users/example/OneDrive/helper-copy"))

    assert any("OneDrive/helper" in error for error in excinfo.value.errors)
