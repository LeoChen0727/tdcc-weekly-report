from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_daily_model_parameter_research import build_price_pullback_daily_row_parity_audit  # noqa: E402
from daily_snapshot_revision_utils import snapshot_file_sha256  # noqa: E402
from validate_price_pullback_daily_row_parity import validate_row_parity_frame  # noqa: E402


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def write_manifest(
    snapshot_dir: Path,
    rows: list[tuple[str, str, Path]],
) -> None:
    pd.DataFrame(
        [
            {
                "snapshot_report_date": report_date,
                "artifact_id": artifact_id,
                "snapshot_path": path.as_posix(),
                "snapshot_sha256": snapshot_file_sha256(path),
            }
            for artifact_id, report_date, path in rows
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )


def research_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "date": "20260615",
                "stock_id": "1234",
                "distance_ema23_pct": 1.0,
                "platform_low": 0.0,
                "short_platform_low": 0.0,
                "previous_20d_low": 0.0,
                "low_20": 0.0,
                "range_low_20d_prev": 0.0,
                "close": 101.0,
                "ema23": 100.0,
                "ma20": 100.0,
                "ema23_slope_pct": 0.1,
                "ema23_slope_5d_pct": 0.1,
                "ma5_turning_up_flag": False,
                "ma10_turning_up_flag": False,
                "return_20d_pct": 10.0,
                "tdcc_history_available": True,
                "high_thresholds_up": True,
                "obv_above_ma20": True,
            },
            {
                "date": "20260615",
                "stock_id": "5678",
                "distance_ema23_pct": 2.0,
                "platform_low": 0.0,
                "short_platform_low": 0.0,
                "previous_20d_low": 0.0,
                "low_20": 0.0,
                "range_low_20d_prev": 0.0,
                "close": 102.0,
                "ema23": 100.0,
                "ma20": 100.0,
                "ema23_slope_pct": 0.1,
                "ema23_slope_5d_pct": 0.1,
                "ma5_turning_up_flag": False,
                "ma10_turning_up_flag": False,
                "return_20d_pct": 10.0,
                "tdcc_history_available": True,
                "high_thresholds_up": True,
                "obv_above_ma20": True,
            },
        ]
    )


def parity_scope_fields() -> dict[str, str]:
    return {
        "published_surface": "daily_candidate_model_signals_for_report",
        "research_proxy_scope": "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay",
        "comparison_basis": "full_research_frame_proxy",
        "candidate_universe_snapshot_path": "",
        "candidate_universe_source_row_count": "",
        "candidate_universe_condition_stock_count": "",
        "candidate_universe_missing_required_columns": "",
        "published_selection_semantics_values": "model_condition_met_rank_by_score_no_theme_veto:1",
        "published_source_category_counts": "pattern:1",
        "published_report_bucket_counts": "mainstream:1",
        "candidate_universe_replay_status": "missing_historical_all_candidates_source_row_snapshot",
        "parity_gap_driver": "research_full_universe_proxy_exceeds_daily_candidate_publication_scope",
        "published_not_in_proxy_interpretation": "",
        "proxy_not_published_interpretation": "research proxy runs on the full stock-day frame, while daily production starts from all_candidates/source-row eligibility and then writes the published report surface",
        "next_required_replay_artifact": "historical all_candidates/source-row snapshot with candidate_source_type, candidate_line, report eligibility, source_row_index, and the exact model input columns",
    }


def test_price_pullback_daily_row_parity_audit_reports_bidirectional_gaps(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    write_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        [
            {
                "model_id": "price_pullback_23ema",
                "stock_id": "1234",
                "selection_semantics": "model_condition_met_rank_by_score_no_theme_veto",
                "original_category": "pattern",
                "report_bucket": "mainstream",
            },
            {
                "model_id": "price_pullback_23ema",
                "stock_id": "9999",
                "selection_semantics": "model_condition_met_rank_by_score_no_theme_veto",
                "original_category": "revenue_pullback",
                "report_bucket": "non_mainstream",
            },
            {"model_id": "volume_range_breakout", "stock_id": "5678"},
        ],
    )
    write_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        [{"model_id": "price_pullback_23ema", "stock_id": "1234"}],
    )
    write_manifest(
        snapshot_dir,
        [
            (
                "model_signals_for_report",
                "20260615",
                snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
            ),
            (
                "model_signals_for_report",
                "20260616",
                snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
            ),
        ],
    )

    audit = build_price_pullback_daily_row_parity_audit(
        research_frame(),
        snapshot_dir=snapshot_dir,
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    first = audit[audit["snapshot_report_date"].eq("20260615")].iloc[0]
    assert first["published_unique_stock_count"] == 2
    assert first["research_proxy_unique_stock_count"] == 2
    assert first["overlap_stock_count"] == 1
    assert first["published_not_in_proxy_rows"] == 1
    assert first["proxy_not_published_rows"] == 1
    assert first["parity_status"] == "blocked_not_exact_daily_row_parity"
    assert first["published_not_in_proxy_sample"] == "9999"
    assert first["proxy_not_published_sample"] == "5678"
    assert first["published_selection_semantics_values"] == "model_condition_met_rank_by_score_no_theme_veto:2"
    assert first["published_source_category_counts"] == "pattern:1;revenue_pullback:1"
    assert first["published_report_bucket_counts"] == "mainstream:1;non_mainstream:1"
    assert first["candidate_universe_replay_status"] == "missing_historical_all_candidates_source_row_snapshot"
    assert first["parity_gap_driver"] == "bidirectional_proxy_and_publication_gap"
    assert "feature parity" in first["published_not_in_proxy_interpretation"]
    assert "full stock-day frame" in first["proxy_not_published_interpretation"]
    assert "historical all_candidates/source-row snapshot" in first["next_required_replay_artifact"]

    second = audit[audit["snapshot_report_date"].eq("20260616")].iloc[0]
    assert second["research_frame_has_date"] == "False"
    assert second["outcome_research_frame_has_date"] == "False"
    assert second["source_row_research_frame_has_date"] == "False"
    assert second["research_frame_date_basis"] == "missing_research_frame_date"
    assert second["parity_status"] == "blocked_missing_research_frame_date"
    assert second["parity_gap_driver"] == "missing_research_frame_date"

    assert validate_row_parity_frame(audit) == []


def test_price_pullback_daily_row_parity_uses_all_candidates_replay_when_available(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    write_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        [
            {
                "model_id": "price_pullback_23ema",
                "stock_id": "1234",
                "selection_semantics": "model_condition_met_rank_by_score_no_theme_veto",
                "original_category": "pattern",
                "report_bucket": "mainstream",
            }
        ],
    )
    write_csv(
        snapshot_dir / "all_candidates_20260615.csv",
        [
            {
                "stock_id": "1234",
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
                "return_20d_pct": "10",
                "tdcc_history_available": "True",
                "high_thresholds_up": "True",
                "obv_above_ma20": "True",
                "price_pullback_tdcc_history_available": "True",
                "price_pullback_high_thresholds_up": "True",
                "price_pullback_obv_above_ma20": "True",
            }
        ],
    )
    write_manifest(
        snapshot_dir,
        [
            (
                "model_signals_for_report",
                "20260615",
                snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
            ),
            (
                "all_candidates_source_rows",
                "20260615",
                snapshot_dir / "all_candidates_20260615.csv",
            ),
        ],
    )

    audit = build_price_pullback_daily_row_parity_audit(
        research_frame(),
        snapshot_dir=snapshot_dir,
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    row = audit.iloc[0]
    assert row["comparison_basis"] == "production_all_candidates_source_row_replay"
    assert row["research_frame_has_date"] == "True"
    assert row["outcome_research_frame_has_date"] == "True"
    assert row["source_row_research_frame_has_date"] == "True"
    assert row["research_frame_date_basis"] == "outcome_research_frame;production_all_candidates_source_row_replay"
    assert row["research_proxy_scope"] == "production_all_candidates_source_row_cond_pullback_replay"
    assert row["research_proxy_unique_stock_count"] == 1
    assert row["candidate_universe_condition_stock_count"] == 1
    assert row["published_not_in_proxy_rows"] == 0
    assert row["proxy_not_published_rows"] == 0
    assert row["candidate_universe_replay_status"] == "candidate_universe_replay_exact_match"
    assert row["parity_status"] == "exact_daily_row_parity_pass"

    assert validate_row_parity_frame(audit) == []


def test_price_pullback_daily_row_parity_accepts_source_row_replay_without_outcome_frame_date(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    write_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        [
            {
                "model_id": "price_pullback_23ema",
                "stock_id": "1234",
                "selection_semantics": "model_condition_met_rank_by_score_no_theme_veto",
                "original_category": "pattern",
                "report_bucket": "mainstream",
            }
        ],
    )
    write_csv(
        snapshot_dir / "all_candidates_20260616.csv",
        [
            {
                "stock_id": "1234",
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
                "return_20d_pct": "10",
                "tdcc_history_available": "True",
                "high_thresholds_up": "True",
                "obv_above_ma20": "True",
                "price_pullback_tdcc_history_available": "True",
                "price_pullback_high_thresholds_up": "True",
                "price_pullback_obv_above_ma20": "True",
            }
        ],
    )
    write_manifest(
        snapshot_dir,
        [
            (
                "model_signals_for_report",
                "20260616",
                snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
            ),
            (
                "all_candidates_source_rows",
                "20260616",
                snapshot_dir / "all_candidates_20260616.csv",
            ),
        ],
    )

    audit = build_price_pullback_daily_row_parity_audit(
        research_frame(),
        snapshot_dir=snapshot_dir,
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    row = audit.iloc[0]
    assert row["research_frame_has_date"] == "True"
    assert row["outcome_research_frame_has_date"] == "False"
    assert row["source_row_research_frame_has_date"] == "True"
    assert row["research_frame_date_basis"] == "production_all_candidates_source_row_replay"
    assert row["comparison_basis"] == "production_all_candidates_source_row_replay"
    assert row["candidate_universe_replay_status"] == "candidate_universe_replay_exact_match"
    assert row["parity_status"] == "exact_daily_row_parity_pass"

    assert validate_row_parity_frame(audit) == []


def test_price_pullback_daily_row_parity_validator_rejects_inconsistent_pass() -> None:
    frame = pd.DataFrame(
        [
            {
                "generated_at": "2026-06-30 00:00:00 Asia/Taipei",
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260615",
                "research_frame_has_date": "True",
                "outcome_research_frame_has_date": "True",
                "source_row_research_frame_has_date": "False",
                "research_frame_date_basis": "outcome_research_frame",
                "published_row_count": "2",
                "published_unique_stock_count": "2",
                "published_duplicate_stock_count": "0",
                "research_proxy_unique_stock_count": "3",
                "overlap_stock_count": "2",
                "published_not_in_proxy_rows": "0",
                "proxy_not_published_rows": "1",
                "published_proxy_coverage_pct": "100",
                "proxy_publish_precision_pct": "66.67",
                "published_not_in_proxy_sample": "",
                "proxy_not_published_sample": "5678",
                "parity_scope": "signal_date_stock_id",
                **parity_scope_fields(),
                "parity_status": "exact_daily_row_parity_pass",
                "parity_blocker": "",
            }
        ]
    )

    errors = validate_row_parity_frame(frame)

    assert any("exact parity pass is inconsistent" in error for error in errors)
