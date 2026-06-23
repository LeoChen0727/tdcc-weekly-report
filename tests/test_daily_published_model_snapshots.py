from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_daily_published_model_snapshots as update_snapshots  # noqa: E402
import validate_daily_published_model_snapshots as validate_snapshots  # noqa: E402


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def rewrite_with_crlf(path: Path) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))


def write_minimal_latest_artifacts(latest_dir: Path, report_date: str = "20260615") -> None:
    write_csv(
        latest_dir / "data_freshness_latest.csv",
        [
            {
                "main_price_date": report_date,
                "report_ready": "True",
                "warrant_ready": "True",
                "warrant_source_status": "ok",
                "warrant_daily_publish_allowed": "True",
                "warrant_pdf_visibility": "visible",
                "warrant_model_effect_allowed": "True",
                "warrant_pdf_effect_allowed": "True",
                "daily_pdf_ready": "True",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        [
            {
                "signal_date": report_date,
                "stock_id": "6153",
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "model_score": "70.0",
                "base_model_score": "55.0",
                "operation_score": "6.0",
                "tdcc_score": "4.0",
                "pattern_score": "8.0",
                "risk_penalty": "3.0",
                "final_rank_score": "70.0",
                "rank_reason_zh": "test evidence",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_candidate_model_summary_for_report_latest.csv",
        [
            {
                "signal_date": report_date,
                "report_line": "mainstream",
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_report_model_registry_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "model_registry_order": "1",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_candidate_model_parameters_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_volume_breakout_operation_section_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "buy_rank_eligible": "False",
                "operation_asof_date": report_date,
                "selected_trigger_id": "",
                "operation_score": "6.0",
                "tdcc_score": "4.0",
                "pattern_score": "8.0",
                "risk_penalty": "3.0",
                "final_rank_score": "70.0",
                "entry_rule_id": "pending_confirmation",
                "stop_loss_rule_id": "signal_low_stop_after_confirmation",
                "stop_loss_price": "",
                "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
                "planned_holding_days": "10",
            }
        ],
    )


def test_daily_published_model_snapshot_builder_and_validator_use_report_date(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    manifest_rows = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    assert set(manifest_rows["artifact_id"]) == {
        "data_freshness",
        "model_parameters",
        "model_registry",
        "model_signals_for_report",
        "model_summary_for_report",
        "volume_breakout_operation_section",
    }
    assert set(manifest_rows["snapshot_report_date"]) == {"20260615"}
    assert (snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv").exists()
    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_daily_published_model_snapshot_hashes_tolerate_windows_crlf_checkout(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )
    manifest = pd.read_csv(manifest_path, dtype=str)
    for _, row in manifest.iterrows():
        rewrite_with_crlf(Path(row["source_path"]))
        rewrite_with_crlf(Path(row["snapshot_path"]))

    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_daily_published_model_snapshot_builder_rejects_not_ready_freshness(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    write_csv(
        latest_dir / "data_freshness_latest.csv",
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "warrant_ready": "False",
                "warrant_source_status": "failed",
                "warrant_daily_publish_allowed": "False",
                "warrant_pdf_visibility": "blocked_unavailable",
                "warrant_model_effect_allowed": "False",
                "warrant_pdf_effect_allowed": "False",
                "daily_pdf_ready": "True",
            }
        ],
    )

    with pytest.raises(RuntimeError, match="warrant_ready must be True before publishing model snapshots"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=tmp_path / "history",
            manifest_path=tmp_path / "history" / "manifest.csv",
            generated_at="2026-06-16 08:00:00 Asia/Taipei",
            commit_sha="test-sha",
        )


def test_daily_published_model_snapshot_builder_allows_bounded_warrant_grace(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    write_csv(
        latest_dir / "data_freshness_latest.csv",
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "warrant_ready": "False",
                "warrant_source_status": "warning_grace",
                "warrant_daily_publish_allowed": "True",
                "warrant_pdf_visibility": "hidden_unavailable",
                "warrant_model_effect_allowed": "False",
                "warrant_pdf_effect_allowed": "False",
                "daily_pdf_ready": "True",
            }
        ],
    )

    manifest_rows = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    freshness_row = manifest_rows[manifest_rows["artifact_id"] == "data_freshness"].iloc[0]
    assert freshness_row["warrant_ready"] == "False"
    assert freshness_row["warrant_pdf_visibility"] == "hidden_unavailable"


def test_daily_published_model_snapshot_builder_rejects_wrong_model_signal_date(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    signals = pd.read_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        dtype=str,
    )
    signals.loc[0, "signal_date"] = "20260612"
    signals.to_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    with pytest.raises(RuntimeError, match="signal_date must match report date 20260615"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=tmp_path / "history",
            manifest_path=tmp_path / "history" / "manifest.csv",
            generated_at="2026-06-16 08:00:00 Asia/Taipei",
            commit_sha="test-sha",
        )
