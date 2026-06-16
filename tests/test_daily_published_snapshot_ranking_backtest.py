from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_published_snapshot_ranking_backtest as builder  # noqa: E402


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def manifest_row(report_date: str, artifact_id: str, snapshot_path: Path) -> dict[str, str]:
    df = pd.read_csv(snapshot_path, dtype=str)
    return {
        "snapshot_report_date": report_date,
        "generated_at": "2026-06-16 18:00:00 Asia/Taipei",
        "pipeline_commit_sha": "test-sha",
        "main_price_date": report_date,
        "report_ready": "True",
        "warrant_ready": "True",
        "daily_pdf_ready": "True",
        "artifact_id": artifact_id,
        "source_path": (
            "output/latest/daily_candidate_model_signals_for_report_latest.csv"
            if artifact_id == "model_signals_for_report"
            else "output/latest/daily_volume_breakout_operation_section_latest.csv"
        ),
        "snapshot_path": snapshot_path.as_posix(),
        "source_sha256": builder.sha256_file(snapshot_path),
        "snapshot_sha256": builder.sha256_file(snapshot_path),
        "row_count": str(len(df)),
        "column_count": str(len(df.columns)),
        "purpose": "as_published_daily_model_snapshot",
    }


def write_price_history(price_dir: Path) -> None:
    write_csv(
        price_dir / "1234.csv",
        [
            {"date": "20260615", "open": "90", "high": "95", "low": "89", "close": "94"},
            {"date": "20260616", "open": "100", "high": "110", "low": "95", "close": "105"},
            {"date": "20260617", "open": "106", "high": "112", "low": "101", "close": "108"},
            {"date": "20260618", "open": "109", "high": "115", "low": "102", "close": "110"},
            {"date": "20260619", "open": "111", "high": "116", "low": "103", "close": "112"},
            {"date": "20260622", "open": "113", "high": "118", "low": "104", "close": "114"},
            {"date": "20260623", "open": "114", "high": "119", "low": "105", "close": "115"},
            {"date": "20260624", "open": "115", "high": "120", "low": "106", "close": "116"},
            {"date": "20260625", "open": "116", "high": "121", "low": "107", "close": "117"},
            {"date": "20260626", "open": "117", "high": "122", "low": "108", "close": "118"},
            {"date": "20260629", "open": "118", "high": "123", "low": "109", "close": "119"},
        ],
    )
    write_csv(
        price_dir / "5678.csv",
        [
            {"date": "20260615", "open": "50", "high": "52", "low": "49", "close": "51"},
            {"date": "20260616", "open": "50", "high": "51", "low": "46", "close": "47"},
            {"date": "20260617", "open": "47", "high": "48", "low": "44", "close": "45"},
            {"date": "20260618", "open": "45", "high": "46", "low": "42", "close": "43"},
        ],
    )


def write_snapshot_fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    report_date = "20260615"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    price_dir = tmp_path / "data" / "stock_price_history"

    signals = snapshot_dir / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    operations = snapshot_dir / f"daily_volume_breakout_operation_section_{report_date}.csv"
    manifest = snapshot_dir / "daily_published_model_snapshot_manifest.csv"

    write_csv(
        signals,
        [
            {
                "signal_date": report_date,
                "stock_id": "1234",
                "stock_name": "Alpha",
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "model_score": "91",
                "display_rank": "1",
                "model_rank": "1",
                "report_line": "mainstream",
                "report_bucket": "mainstream",
                "effective_mainstream_label": "core_mainstream",
            },
            {
                "signal_date": report_date,
                "stock_id": "5678",
                "stock_name": "Beta",
                "model_id": "hot_theme_pullback",
                "model_name_zh": "熱門族群回檔模型",
                "model_score": "73",
                "display_rank": "12",
                "model_rank": "12",
                "report_line": "non_mainstream",
                "report_bucket": "non_mainstream",
                "effective_mainstream_label": "non_mainstream",
            },
        ],
    )
    write_csv(
        operations,
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "stock_id": "1234",
                "stock_name": "Alpha",
                "signal_date": report_date,
                "confirmation_date": "",
                "display_order": "1",
                "research_score": "91",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "stock_id": "1234",
                "stock_name": "Alpha",
                "signal_date": report_date,
                "confirmation_date": "",
                "display_order": "1",
                "research_score": "91",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "confirmed_operation",
                "row_type": "data",
                "stock_id": "5678",
                "stock_name": "Beta",
                "signal_date": report_date,
                "confirmation_date": report_date,
                "display_order": "2",
                "research_score": "73",
                "row_action_status": "confirmed_buy_candidate",
                "buy_rank_eligible": "True",
            },
        ],
    )
    write_csv(manifest, [manifest_row(report_date, "model_signals_for_report", signals), manifest_row(report_date, "volume_breakout_operation_section", operations)])
    write_price_history(price_dir)
    return manifest, snapshot_dir, price_dir


def test_published_snapshot_ranking_backtest_uses_date_stamped_snapshots(tmp_path: Path) -> None:
    manifest, snapshot_dir, price_dir = write_snapshot_fixture(tmp_path)

    summary, events = builder.build_daily_published_snapshot_ranking_backtest(
        manifest_path=manifest,
        snapshot_root=snapshot_dir,
        price_dir=price_dir,
        generated_at="2026-06-16 18:00:00 Asia/Taipei",
    )

    model_events = events[events["source_artifact"].eq("model_signals_for_report")]
    assert len(model_events) == 2
    assert set(model_events["mainstream_segment"]) == {"mainstream", "non_mainstream"}
    assert set(model_events["score_decile"]) == {"score_90_100", "score_70_80"}
    assert set(model_events["rank_bucket"]) == {"rank_001_005", "rank_011_020"}
    assert set(model_events["ranking_evaluation_eligible"]) == {"True"}
    assert set(model_events["trade_eligible"]) == {"False"}

    operation_events = events[events["source_artifact"].eq("volume_breakout_operation_section")]
    assert len(operation_events) == 2
    pending = operation_events[operation_events["operation_section"].eq("pending_confirmation")]
    confirmed = operation_events[operation_events["operation_section"].eq("confirmed_operation")]
    assert set(operation_events["ranking_evaluation_eligible"]) == {"False"}
    assert set(pending["trade_eligible"]) == {"False"}
    assert set(confirmed["trade_eligible"]) == {"True"}

    volume_sections = summary[summary["segment_type"].eq("volume_operation_section")]
    assert "volume_range_breakout|active_operation" in set(volume_sections["segment_value"])
    assert set(summary["advisory_only"]) == {"True"}


def test_published_snapshot_manifest_hash_mismatch_blocks_build(tmp_path: Path) -> None:
    manifest, snapshot_dir, price_dir = write_snapshot_fixture(tmp_path)
    manifest_df = pd.read_csv(manifest, dtype=str)
    manifest_df.loc[0, "snapshot_sha256"] = "bad"
    manifest_df.to_csv(manifest, index=False, encoding="utf-8", lineterminator="\n")

    with pytest.raises(RuntimeError, match="snapshot_sha256 mismatch"):
        builder.build_daily_published_snapshot_ranking_backtest(
            manifest_path=manifest,
            snapshot_root=snapshot_dir,
            price_dir=price_dir,
            generated_at="2026-06-16 18:00:00 Asia/Taipei",
        )
