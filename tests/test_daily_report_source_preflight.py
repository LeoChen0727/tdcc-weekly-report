from __future__ import annotations

import subprocess
from pathlib import Path

import pandas as pd

from scripts import validate_daily_report_source_preflight as preflight


def write_freshness(path: Path, **overrides: object) -> None:
    row = {
        "generated_at": "2026-06-11 20:27:31",
        "main_price_date": "20260611",
        "actual_stock_price_history_date": "20260611",
        "stock_monitor_price_date": "20260611",
        "all_candidates_date": "20260611",
        "official_price_fetch_date": "20260611",
        "warrant_flow_date": "20260611",
        "raw_stock_monitor_price_date": "20260611",
        "raw_all_candidates_date": "20260611",
        "raw_official_price_fetch_date": "20260611",
        "raw_warrant_flow_date": "20260611",
        "report_ready": "True",
        "report_ready_note": "core daily data dates match main_price_date",
        "warrant_ready": "True",
        "warrant_ready_note": "warrant_flow_date matches main_price_date",
        "daily_pdf_ready": "True",
        "daily_pdf_ready_note": "core daily data and warrant layer are ready for daily PDF source use",
        "stock_monitor_note": "ready",
        "all_candidates_note": "ready",
        "official_fetch_note": "ready",
        "warrant_note": "ready",
    }
    row.update(overrides)
    pd.DataFrame([row]).to_csv(path, index=False, encoding="utf-8")


def write_readme(path: Path, **overrides: object) -> None:
    row = {
        "main_price_date": "20260611",
        "report_ready": "True",
        "warrant_flow_date": "20260611",
        "warrant_ready": "True",
        "daily_pdf_ready": "True",
        "daily_pdf_ready_note": "core daily data and warrant layer are ready for daily PDF source use",
        "commit_sha": "0" * 40,
    }
    row.update(overrides)
    path.write_text("\n".join(f"{key}={value}" for key, value in row.items()) + "\n", encoding="utf-8")


def run_git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True)


def init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "output" / "latest").mkdir(parents=True)
    run_git(tmp_path, "init", "repo")
    run_git(repo, "config", "user.email", "test@example.invalid")
    run_git(repo, "config", "user.name", "Test User")
    return repo


def commit_repo(repo: Path) -> None:
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "init")


def validate(repo: Path, **kwargs: object) -> tuple[list[str], list[str]]:
    return preflight.validate_daily_report_source_preflight(
        repo_root=repo,
        freshness_path=Path("output/latest/data_freshness_latest.csv"),
        readme_path=Path("output/latest/READ_ME_FIRST_DAILY_REPORT.txt"),
        **kwargs,
    )


def test_preflight_passes_clean_ready_repo_when_readme_commit_differs_from_head(tmp_path: Path):
    repo = init_repo(tmp_path)
    write_freshness(repo / "output/latest/data_freshness_latest.csv")
    write_readme(repo / "output/latest/READ_ME_FIRST_DAILY_REPORT.txt", commit_sha="1" * 40)
    commit_repo(repo)

    errors, info = validate(repo, expected_date="20260611")

    assert errors == []
    assert any("README commit_sha differs from checkout HEAD" in line for line in info)


def test_preflight_rejects_dirty_checkout(tmp_path: Path):
    repo = init_repo(tmp_path)
    write_freshness(repo / "output/latest/data_freshness_latest.csv")
    readme = repo / "output/latest/READ_ME_FIRST_DAILY_REPORT.txt"
    write_readme(readme)
    commit_repo(repo)
    write_readme(readme, daily_pdf_ready="False")

    errors, _info = validate(repo)

    assert any("local checkout is dirty" in error for error in errors)


def test_preflight_allow_dirty_is_diagnostic_only(tmp_path: Path):
    repo = init_repo(tmp_path)
    write_freshness(repo / "output/latest/data_freshness_latest.csv")
    readme = repo / "output/latest/READ_ME_FIRST_DAILY_REPORT.txt"
    write_readme(readme)
    commit_repo(repo)
    write_readme(readme)

    errors, _info = validate(repo, allow_dirty=True)

    assert not any("local checkout is dirty" in error for error in errors)


def test_preflight_rejects_stale_date(tmp_path: Path):
    repo = init_repo(tmp_path)
    write_freshness(
        repo / "output/latest/data_freshness_latest.csv",
        main_price_date="20260605",
        actual_stock_price_history_date="20260605",
        stock_monitor_price_date="20260605",
        all_candidates_date="20260605",
        official_price_fetch_date="20260605",
        warrant_flow_date="20260605",
        raw_stock_monitor_price_date="20260605",
        raw_all_candidates_date="20260605",
        raw_official_price_fetch_date="20260605",
        raw_warrant_flow_date="20260605",
    )
    write_readme(
        repo / "output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        main_price_date="20260605",
        warrant_flow_date="20260605",
    )
    commit_repo(repo)

    errors, _info = validate(repo, expected_date="20260611")

    assert "main_price_date=20260605 does not match expected date 20260611" in errors


def test_preflight_rejects_daily_pdf_not_ready(tmp_path: Path):
    repo = init_repo(tmp_path)
    write_freshness(
        repo / "output/latest/data_freshness_latest.csv",
        daily_pdf_ready="False",
        daily_pdf_ready_note="warrant layer not ready",
    )
    write_readme(repo / "output/latest/READ_ME_FIRST_DAILY_REPORT.txt", daily_pdf_ready="False")
    commit_repo(repo)

    errors, _info = validate(repo)

    assert any("daily_pdf_ready must be True" in error for error in errors)


def test_preflight_rejects_readme_freshness_mismatch(tmp_path: Path):
    repo = init_repo(tmp_path)
    write_freshness(repo / "output/latest/data_freshness_latest.csv")
    write_readme(repo / "output/latest/READ_ME_FIRST_DAILY_REPORT.txt", main_price_date="20260605")
    commit_repo(repo)

    errors, _info = validate(repo)

    assert any("README main_price_date=20260605 does not match freshness" in error for error in errors)
