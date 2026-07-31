from __future__ import annotations

from scripts.validate_event_catalyst_source_refresh_scope import validate_paths


def test_source_refresh_scope_accepts_only_event_catalyst_artifacts() -> None:
    paths = [
        "data/event_catalysts/event_catalyst_log.csv",
        "data/company_calendar/company_event_calendar.csv",
        "output/latest/catalyst_data_source_status_latest.json",
        "docs/latest/catalyst_data_source_status_latest.json",
        "output/history/event_catalyst_recovery/run/20260720/event_catalyst_recovery_manifest.json",
        "output/latest/event_catalyst_historical_recovery_latest.json",
        "docs/latest/event_catalyst_historical_recovery_latest.json",
    ]

    assert validate_paths(paths) == []


def test_source_refresh_scope_rejects_model_ranking_and_cross_lane_paths() -> None:
    paths = [
        "output/latest/daily_candidate_model_signals_latest.csv",
        "output/history/daily_model_snapshots/data_freshness_20260730.csv",
        "output/latest/tdcc_weekly_report_latest.json",
        "output/latest/research_backtest/result.csv",
    ]

    errors = validate_paths(paths)

    for path in paths:
        assert any(path in error for error in errors)
