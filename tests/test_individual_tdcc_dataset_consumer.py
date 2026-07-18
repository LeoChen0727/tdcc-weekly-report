from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from individual_tdcc_dataset_consumer import (  # noqa: E402
    IndividualTdccDatasetContract,
    prepare_and_validate_stock_tdcc_history,
)


DATES = ("20260703", "20260709", "20260717")
DATASET_ID = "tdcc-20260717-0123456789abcdef"


def contract(*, accepted: tuple[tuple[str, str], ...] = ()) -> IndividualTdccDatasetContract:
    return IndividualTdccDatasetContract(
        dataset_id=DATASET_ID,
        signal_date="20260717",
        required_dates=DATES,
        official_dates=DATES,
        current_stock_ids=frozenset({"6409"}),
        accepted_history_exceptions=frozenset(accepted),
        manifest_path=Path("output/latest/tdcc_dataset_manifest_latest.json"),
    )


def history_frame(*, include_20260709: bool = True) -> pd.DataFrame:
    ratio_by_date = {
        "20260703": (65.42, 59.45, 54.29, 50.01),
        "20260709": (66.59, 59.38, 53.95, 50.70),
        "20260717": (66.17, 58.98, 53.61, 51.39),
    }
    dates = [date for date in DATES if include_20260709 or date != "20260709"]
    rows: list[dict[str, object]] = []
    for position, date in enumerate(dates):
        row: dict[str, object] = {
            "as_of_date": date,
            "stock_id": "6409",
            "stock_name": "6409 fixture",
        }
        official_position = DATES.index(date)
        one_week_changes: dict[int, float] = {}
        for threshold, ratio in zip((400, 600, 800, 1000), ratio_by_date[date]):
            row[f"over_{threshold}_ratio"] = ratio
            for weeks in (1, 2, 3):
                if official_position < weeks:
                    expected = math.nan
                else:
                    prior_date = DATES[official_position - weeks]
                    if prior_date not in dates:
                        expected = math.nan
                    else:
                        prior_ratio = ratio_by_date[prior_date][(400, 600, 800, 1000).index(threshold)]
                        expected = ratio - prior_ratio
                row[f"over_{threshold}_change_{weeks}w"] = expected
                if weeks == 1:
                    one_week_changes[threshold] = expected
        if position == 0 or DATES[official_position - 1] not in dates:
            streak = 0
        else:
            prior_date = DATES[official_position - 1]
            improved = any(
                ratio_by_date[date][index] > ratio_by_date[prior_date][index]
                for index in range(4)
            )
            prior_streak = int(rows[-1]["tdcc_consecutive_up_weeks"])
            streak = prior_streak + 1 if improved else 0
        row["tdcc_consecutive_up_weeks"] = streak
        all_up = all(not math.isnan(value) and value > 0 for value in one_week_changes.values())
        high_up = any(
            not math.isnan(one_week_changes[threshold]) and one_week_changes[threshold] > 0
            for threshold in (800, 1000)
        )
        row["all_thresholds_up"] = all_up
        row["high_thresholds_up"] = high_up
        row["four_thresholds_sync_up"] = all_up
        rows.append(row)
    return pd.DataFrame(rows)


def test_6409_missing_typhoon_adjusted_official_date_cannot_be_fresh() -> None:
    stale = history_frame(include_20260709=False)
    stale.loc[stale["as_of_date"].eq("20260717"), "over_400_change_1w"] = 0.75

    with pytest.raises(RuntimeError, match="missing required official dates.*20260709"):
        prepare_and_validate_stock_tdcc_history("6409", stale, contract())


def test_6409_cross_period_change_cannot_be_labeled_one_week() -> None:
    stale = history_frame()
    stale.loc[stale["as_of_date"].eq("20260717"), "over_400_change_1w"] = 0.75

    with pytest.raises(RuntimeError, match="over_400_change_1w"):
        prepare_and_validate_stock_tdcc_history("6409", stale, contract())


def test_complete_history_gets_canonical_lineage_and_exact_changes() -> None:
    prepared, assessment = prepare_and_validate_stock_tdcc_history("6409", history_frame(), contract())

    assert assessment.continuity_status == "complete"
    assert assessment.missing_official_dates == ()
    assert set(prepared["source_tdcc_dataset_id"]) == {DATASET_ID}
    latest = prepared.iloc[-1]
    assert float(latest["over_400_change_1w"]) == pytest.approx(-0.42)
    assert float(latest["over_400_change_2w"]) == pytest.approx(0.75)
    assert int(latest["tdcc_consecutive_up_weeks"]) == 2


def test_strict_string_dtypes_are_normalized_before_derived_values_are_recomputed() -> None:
    strict = history_frame()
    derived_fields = [
        *(
            f"over_{threshold}_change_{weeks}w"
            for threshold in (400, 600, 800, 1000)
            for weeks in (1, 2, 3)
        ),
        "tdcc_consecutive_up_weeks",
        "all_thresholds_up",
        "high_thresholds_up",
        "four_thresholds_sync_up",
    ]
    for field in derived_fields:
        strict[field] = strict[field].astype("string")

    prepared, assessment = prepare_and_validate_stock_tdcc_history("6409", strict, contract())

    assert assessment.continuity_status == "complete"
    latest = prepared.iloc[-1]
    assert float(latest["over_400_change_1w"]) == pytest.approx(-0.42)
    assert int(latest["tdcc_consecutive_up_weeks"]) == 2
    assert bool(latest["high_thresholds_up"]) is True


def test_canonical_stock_level_exception_degrades_only_that_stock() -> None:
    prepared, assessment = prepare_and_validate_stock_tdcc_history(
        "6409",
        history_frame(include_20260709=False),
        contract(accepted=(("20260709", "6409"),)),
    )

    assert assessment.continuity_status == "accepted_history_exception"
    assert assessment.missing_official_dates == ("20260709",)
    latest = prepared.iloc[-1]
    assert math.isnan(float(latest["over_400_change_1w"]))
    assert float(latest["over_400_change_2w"]) == pytest.approx(0.75)
    assert int(latest["tdcc_consecutive_up_weeks"]) == 0
    assert latest["tdcc_continuity_status"] == "accepted_history_exception"
    assert latest["tdcc_missing_official_dates"] == "20260709"


def test_unapproved_exception_row_cannot_reappear_in_materialized_view() -> None:
    with pytest.raises(RuntimeError, match="contradicts accepted missing-row exceptions"):
        prepare_and_validate_stock_tdcc_history(
            "6409",
            history_frame(),
            contract(accepted=(("20260709", "6409"),)),
        )
