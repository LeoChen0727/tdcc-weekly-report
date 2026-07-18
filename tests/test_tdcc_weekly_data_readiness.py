from __future__ import annotations

import pytest

from scripts import tdcc_weekly_data_readiness as readiness


def test_typhoon_week_accepts_last_published_business_day() -> None:
    report = readiness.build_readiness_report(
        as_of_date="20260711",
        official_dates=["20260709", "20260703", "20260626"],
    )

    assert report["status"] == "pass"
    assert report["target_week_start"] == "20260706"
    assert report["target_week_end"] == "20260710"
    assert report["selected_official_date"] == "20260709"
    assert report["previous_official_date"] == "20260703"


def test_stale_previous_week_is_not_ready_for_current_report_week() -> None:
    report = readiness.build_readiness_report(
        as_of_date="20260711",
        official_dates=["20260703", "20260626"],
    )

    assert report["status"] == "waiting_for_official_period"
    assert report["selected_official_date"] == ""
    assert report["latest_official_date"] == "20260703"


def test_weekday_retry_targets_previous_completed_week() -> None:
    report = readiness.build_readiness_report(
        as_of_date="20260713",
        official_dates=["20260709", "20260703"],
    )

    assert report["status"] == "pass"
    assert report["target_week_start"] == "20260706"
    assert report["target_week_end"] == "20260710"
    assert report["selected_official_date"] == "20260709"


def test_ensure_ready_raises_instead_of_reusing_stale_snapshot() -> None:
    with pytest.raises(readiness.TdccWeeklyDataNotReadyError):
        readiness.ensure_weekly_data_ready(
            as_of_date="20260711",
            available_dates_func=lambda: ["20260703", "20260626"],
            write_report=False,
        )
