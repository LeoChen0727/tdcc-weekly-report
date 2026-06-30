from __future__ import annotations

from pathlib import Path
import subprocess
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import backfill_historical_all_candidates_snapshots_from_git_history as backfill  # noqa: E402
from update_daily_published_model_snapshots import ARTIFACTS, MANIFEST_COLUMNS  # noqa: E402


def run_git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def all_candidates_required_row(report_date: str, stock_id: str) -> dict[str, str]:
    artifact = next(artifact for artifact in ARTIFACTS if artifact.artifact_id == "all_candidates_source_rows")
    row = {column: "1" for column in artifact.required_columns}
    row.update(
        {
            "date": report_date,
            "signal_date": report_date,
            "main_price_date": report_date,
            "stock_id": stock_id,
            "stock_name": f"stock {stock_id}",
            "category": "pattern",
            "candidate_source_type": "individual_quality_candidate",
            "candidate_line": "pattern_watch",
            "candidate_line_group": "individual_pattern_watch",
            "source_row_index": "0",
            "close": "101",
            "ema23": "100",
            "ma20": "100",
            "distance_to_ema23_pct": "1.0",
            "gap_ema23_pct": "1.0",
            "platform_low": "95",
            "short_platform_low": "96",
            "previous_20d_low": "94",
            "low_20": "94",
            "ma5_turning_up_flag": "False",
            "ma10_turning_up_flag": "False",
            "volume_ratio": "1.2",
            "return_20d": "5.0",
            "latest_revenue_yoy": "10.0",
            "cumulative_revenue_yoy": "8.0",
            "off_60d_low_pct": "12.0",
            "tdcc_judgement": "mild_accumulation",
            "tdcc_accumulation_signal": "True",
            "warrant_flow_signal": "neutral",
            "false_breakout_risk": "False",
        }
    )
    return row


def manifest_template_row(report_date: str) -> dict[str, str]:
    row = {column: "" for column in MANIFEST_COLUMNS}
    row.update(
        {
            "snapshot_report_date": report_date,
            "generated_at": "2026-06-30 09:00:00 Asia/Taipei",
            "pipeline_commit_sha": "existing-report-commit",
            "main_price_date": report_date,
            "report_ready": "True",
            "warrant_ready": "True",
            "warrant_source_status": "ok",
            "warrant_daily_publish_allowed": "True",
            "warrant_pdf_visibility": "visible",
            "warrant_model_effect_allowed": "True",
            "warrant_pdf_effect_allowed": "True",
            "daily_pdf_ready": "True",
            "artifact_id": "model_signals_for_report",
            "source_path": "output/latest/daily_candidate_model_signals_for_report_latest.csv",
            "snapshot_path": f"output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_{report_date}.csv",
            "source_sha256": "existing-source",
            "snapshot_sha256": "existing-snapshot",
            "row_count": "1",
            "column_count": "2",
            "purpose": "as_published_daily_model_snapshot",
        }
    )
    return row


def test_backfills_historical_all_candidates_snapshots_from_git_history(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init")
    run_git(repo, "config", "user.email", "test@example.com")
    run_git(repo, "config", "user.name", "Test User")

    source = repo / "output" / "latest" / "all_candidates_latest.csv"
    write_csv(source, [all_candidates_required_row("20260615", "1234")])
    run_git(repo, "add", "output/latest/all_candidates_latest.csv")
    run_git(repo, "commit", "-m", "publish 20260615 all candidates")
    commit_20260615 = run_git(repo, "rev-parse", "HEAD")

    write_csv(source, [all_candidates_required_row("20260616", "5678")])
    run_git(repo, "add", "output/latest/all_candidates_latest.csv")
    run_git(repo, "commit", "-m", "publish 20260616 all candidates")
    commit_20260616 = run_git(repo, "rev-parse", "HEAD")

    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_csv(
        manifest_path,
        [
            manifest_template_row("20260615"),
            manifest_template_row("20260616"),
        ],
    )

    rows = backfill.backfill_historical_all_candidates_snapshots(
        repo_root=repo,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        dates=["20260615", "20260616"],
        generated_at="2026-06-30 10:00:00 Asia/Taipei",
    )

    assert list(rows["snapshot_report_date"]) == ["20260615", "20260616"]
    assert (snapshot_dir / "all_candidates_20260615.csv").exists()
    assert (snapshot_dir / "all_candidates_20260616.csv").exists()
    assert rows.loc[rows["snapshot_report_date"].eq("20260615"), "pipeline_commit_sha"].iloc[0] == commit_20260615
    assert rows.loc[rows["snapshot_report_date"].eq("20260616"), "pipeline_commit_sha"].iloc[0] == commit_20260616
    assert set(rows["source_path"]) == {"output/latest/all_candidates_latest.csv"}
    assert set(rows["purpose"]) == {"as_published_daily_model_snapshot"}

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    backfilled = manifest[manifest["artifact_id"].eq("all_candidates_source_rows")]
    assert set(backfilled["snapshot_report_date"]) == {"20260615", "20260616"}
    assert set(backfilled["report_ready"]) == {"True"}
    assert backfilled["snapshot_sha256"].str.len().min() == 64
