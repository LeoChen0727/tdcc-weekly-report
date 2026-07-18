from __future__ import annotations

import math
from pathlib import Path

import pandas as pd
import pytest

from scripts import repair_tdcc_weekly_history_continuity as repair
from scripts import tdcc_stock_history_utils as history_utils
from scripts import validate_tdcc_weekly_history_continuity as continuity_validator
import tdcc_holder_ratio_top10 as holder_report


OFFICIAL_DATES = ["20260703", "20260709", "20260717"]
RATIO_COLS = [f"over_{threshold}_ratio" for threshold in history_utils.THRESHOLDS]


def history_rows(dates: list[str], values: list[float]) -> pd.DataFrame:
    rows = []
    for date, value in zip(dates, values):
        row = {"as_of_date": date}
        for col in RATIO_COLS:
            row[col] = value
        rows.append(row)
    return pd.DataFrame(rows)


def test_missing_official_period_cannot_be_labeled_change_1w() -> None:
    rows = history_rows(["20260703", "20260717"], [10.0, 12.0])

    change = history_utils.threshold_change(
        rows,
        "over_400_ratio",
        current_idx=1,
        weeks=1,
        official_dates=OFFICIAL_DATES,
    )

    assert math.isnan(change)
    assert history_utils.consecutive_up_weeks(rows, RATIO_COLS, 1, OFFICIAL_DATES) == 0


def test_backfilled_period_restores_adjacent_change_and_streak() -> None:
    rows = history_rows(OFFICIAL_DATES, [10.0, 11.0, 12.0])

    assert history_utils.threshold_change(
        rows,
        "over_400_ratio",
        current_idx=2,
        weeks=1,
        official_dates=OFFICIAL_DATES,
    ) == 1.0
    assert history_utils.threshold_change(
        rows,
        "over_400_ratio",
        current_idx=2,
        weeks=2,
        official_dates=OFFICIAL_DATES,
    ) == 2.0
    assert history_utils.consecutive_up_weeks(rows, RATIO_COLS, 2, OFFICIAL_DATES) == 2


def test_previous_snapshot_requires_exact_official_period(tmp_path: Path, monkeypatch) -> None:
    history_dir = tmp_path / "output" / "history" / "tdcc"
    history_dir.mkdir(parents=True)
    (history_dir / "tdcc_holder_ratio_20260703.csv").write_text(
        "date,code\n20260703,6409\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(holder_report, "TDCC_HISTORY_DIR", history_dir)

    with pytest.raises(RuntimeError, match="previous official TDCC snapshot is missing"):
        holder_report.find_previous_snapshot("20260717", OFFICIAL_DATES)


def test_required_periods_are_selected_from_official_dates_not_filenames() -> None:
    dates = ["20260618", "20260626", "20260703", "20260709", "20260717"]

    selected = repair.required_official_dates(dates, "20260717", required_periods=4)

    assert selected == ["20260626", "20260703", "20260709", "20260717"]


def test_single_holder_placeholder_is_not_written_as_valid_backfill() -> None:
    rows = []
    for level in range(1, 17):
        rows.append(
            {
                "level": level,
                "range": "",
                "holders": 1 if level in {15, 16} else 0,
                "shares": 60_000_000 if level in {15, 16} else 0,
                "pct": 100.0 if level in {15, 16} else 0.0,
            }
        )

    assert repair.is_invalid_single_holder_table(pd.DataFrame(rows)) is True


def test_official_no_data_requires_every_retry_to_be_empty(monkeypatch) -> None:
    outcomes: list[object] = [pd.DataFrame(), RuntimeError("network"), RuntimeError("network")]

    def fetcher(_session, _stock_id: str, _date: str) -> pd.DataFrame:
        outcome = outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(repair.backfill, "stock_date_already_present", lambda *_args: False)
    actions = repair.fetch_missing_with_retries(
        [repair.monthly_repair.MissingTdccRows("20260709", ["6409"], 0)],
        {"6409": "悅城"},
        retry_attempts=3,
        sleep_seconds=0,
        workers=1,
        fetch_func=fetcher,
    )

    assert actions[0]["status"] == "failed"


def test_repeated_empty_official_response_is_explicit_exception(monkeypatch) -> None:
    monkeypatch.setattr(repair.backfill, "stock_date_already_present", lambda *_args: False)
    actions = repair.fetch_missing_with_retries(
        [repair.monthly_repair.MissingTdccRows("20260709", ["3152"], 0)],
        {"3152": "璟德"},
        retry_attempts=3,
        sleep_seconds=0,
        workers=1,
        fetch_func=lambda *_args: pd.DataFrame(),
    )

    assert actions[0]["status"] == "official_no_data"


def test_weekly_workflow_repairs_history_before_derived_build() -> None:
    workflow = Path(".github/workflows/tdcc_weekly.yml").read_text(encoding="utf-8")
    expected_steps = [
        "Wait for expected TDCC period",
        "Fetch current TDCC snapshot",
        "Repair TDCC weekly history continuity",
        "Build TDCC weekly report from continuous history",
        "Build per-stock TDCC history",
        "Validate TDCC weekly history continuity",
        "Build TDCC weekly candidate reports",
    ]
    positions = [workflow.index(step) for step in expected_steps]

    assert positions == sorted(positions)
    assert "target_as_of_date:" in workflow
    assert '--as-of-date "${{ github.event.inputs.target_as_of_date }}"' in workflow
    assert "python tdcc_holder_ratio_top10.py --fetch-only --use-existing-readiness" in workflow
    assert "python scripts/build_tdcc_stock_history.py --use-existing-readiness" in workflow
    assert "using latest cached TDCC snapshot" not in Path("tdcc_holder_ratio_top10.py").read_text(
        encoding="utf-8"
    )


def test_apps_script_retries_only_named_tdcc_data_steps() -> None:
    source = Path("docs/apps_script_workflow_trigger.gs").read_text(encoding="utf-8")

    assert '"Wait for expected TDCC period"' in source
    assert '"Fetch current TDCC snapshot"' in source
    assert '"Repair TDCC weekly history continuity"' in source
    assert 'state.phase = "tdcc_data_retry_wait"' in source
    assert "failedSteps.length > 0 && failedSteps.every" in source
    assert "isRetryableTdccDataFailure_(tdccRun.id)" in source
    assert "dispatchScheduledTdccRetry_(state)" in source
    assert "target_as_of_date: taipeiYyyyMmDd_()" in source
    assert source.count("target_as_of_date: state.target_as_of_date") >= 2


def test_non_build_phase_refreshes_readiness_instead_of_reusing_stale_artifact(
    monkeypatch,
) -> None:
    expected = {"selected_official_date": "20260717", "official_dates": OFFICIAL_DATES}
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.ensure_weekly_data_ready",
        lambda *, as_of_date: expected,
    )
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.load_readiness",
        lambda: pytest.fail("non-build phase must not load a stale readiness artifact"),
    )
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.taipei_today",
        lambda: "20260718",
    )

    assert holder_report.resolve_readiness(build_only=False, use_existing_readiness=False) == expected


def test_fetch_phase_uses_pinned_same_run_readiness_artifact(monkeypatch) -> None:
    expected = {"selected_official_date": "20260717", "official_dates": OFFICIAL_DATES}
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.load_readiness",
        lambda: expected,
    )
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.ensure_weekly_data_ready",
        lambda **_kwargs: pytest.fail("fetch phase must preserve the pinned same-run readiness artifact"),
    )

    assert holder_report.resolve_readiness(
        build_only=False,
        use_existing_readiness=True,
    ) == expected


def test_build_only_phase_uses_same_run_readiness_artifact(monkeypatch) -> None:
    expected = {"selected_official_date": "20260717", "official_dates": OFFICIAL_DATES}
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.load_readiness",
        lambda: expected,
    )
    monkeypatch.setattr(
        "scripts.tdcc_weekly_data_readiness.ensure_weekly_data_ready",
        lambda **_kwargs: pytest.fail("build-only phase must use the gated same-run artifact"),
    )

    assert holder_report.resolve_readiness(build_only=True) == expected


def test_validator_rejects_wrong_two_period_change(tmp_path: Path, monkeypatch) -> None:
    history_dir = tmp_path / "output" / "history" / "tdcc"
    stock_history_dir = tmp_path / "data" / "tdcc_stock_history"
    history_dir.mkdir(parents=True)
    stock_history_dir.mkdir(parents=True)
    for date, value in zip(OFFICIAL_DATES, [10.0, 11.0, 12.0]):
        row = {
            "date": date,
            "code": "6409",
            **{f"over_{threshold}_pct": value for threshold in history_utils.THRESHOLDS},
        }
        pd.DataFrame([row]).to_csv(
            history_dir / f"tdcc_holder_ratio_{date}.csv",
            index=False,
        )

    rows = history_rows(OFFICIAL_DATES, [10.0, 11.0, 12.0])
    for threshold in history_utils.THRESHOLDS:
        rows[f"over_{threshold}_change_1w"] = [math.nan, 1.0, 1.0]
        rows[f"over_{threshold}_change_2w"] = [math.nan, math.nan, 1.0]
        rows[f"over_{threshold}_change_3w"] = math.nan
    rows["tdcc_consecutive_up_weeks"] = [0, 1, 2]
    rows.to_csv(stock_history_dir / "6409.csv", index=False)

    monkeypatch.setattr(continuity_validator, "HISTORY_DIR", history_dir)
    monkeypatch.setattr(continuity_validator, "STOCK_HISTORY_DIR", stock_history_dir)
    monkeypatch.setattr(
        continuity_validator,
        "load_readiness",
        lambda: {"selected_official_date": "20260717", "official_dates": OFFICIAL_DATES},
    )
    monkeypatch.setattr(
        continuity_validator,
        "load_continuity_report",
        lambda: {
            "signal_date": "20260717",
            "unresolved_missing_rows": 0,
            "confirmed_history_exceptions": [],
        },
    )

    errors = continuity_validator.validate()

    assert any("change_2w" in error for error in errors)
