from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_source_first_condition_audit import (  # noqa: E402
    BASELINE_VARIANT_ID,
    DETAIL_CSV,
    LATEST_CSV,
    PRIMARY_VARIANT_ID,
    load_stock_price,
)
from validate_revenue_unreacted_range_source_first_condition_audit import validate  # noqa: E402
import validate_revenue_unreacted_range_source_first_condition_audit as validator  # noqa: E402


MonthlyRevenueLineage = tuple[
    int,
    str,
    dict[tuple[str, str], dict[str, str]],
    dict[str, str],
]


@pytest.fixture(scope="module")
def current_monthly_revenue_lineage() -> MonthlyRevenueLineage:
    return validator._current_monthly_revenue_lineage(
        validator.REVENUE_HISTORY_CSV,
        validator.MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    )


def _bind_outputs_to_current_full_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    lineage: dict[str, str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary_path = tmp_path / "summary.csv"
    detail_path = tmp_path / "detail.csv"
    markdown_path = tmp_path / "summary.md"
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    for column, value in lineage.items():
        summary.loc[:, column] = value
        detail.loc[:, column] = value
    summary.to_csv(summary_path, index=False)
    detail.to_csv(detail_path, index=False)
    markdown_path.write_bytes(validator.LATEST_MD.read_bytes())
    monkeypatch.setattr(validator, "LATEST_CSV", summary_path)
    monkeypatch.setattr(validator, "DETAIL_CSV", detail_path)
    monkeypatch.setattr(validator, "LATEST_MD", markdown_path)
    return summary, detail


def _lineage_distinct_from(captured: dict[str, str]) -> dict[str, str]:
    current = {
        column: character * 64
        for column, character in zip(
            validator.RUN_LINEAGE_COLUMNS,
            ("a", "b", "c"),
        )
    }
    for column in validator.RUN_LINEAGE_COLUMNS:
        if current[column] == captured[column]:
            current[column] = "d" * 64
    return current


def test_source_first_condition_audit_passes() -> None:
    assert validate() == []


def test_selected_condition_covers_both_known_successes_without_counting_overlap() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str, "launch_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    selected = detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["episode_status"].eq("launch_within_active_horizon")
        & detail["stock_id"].isin(["4916", "1303"])
    ]
    assert set(selected["stock_id"]) == {"4916", "1303"}
    assert selected.loc[selected["stock_id"].eq("4916"), "launch_date"].tolist() == ["20260518"]
    assert selected.loc[selected["stock_id"].eq("1303"), "launch_date"].tolist() == ["20260527"]
    for stock_id, rows in detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
    ].groupby("stock_id", sort=False):
        ordered = rows.sort_values("episode_start_sequence_index", kind="mergesort")
        starts = pd.to_numeric(ordered["episode_start_sequence_index"], errors="coerce")
        prior_ends = pd.to_numeric(ordered["episode_end_sequence_index"], errors="coerce").shift(1)
        assert not starts.le(prior_ends).fillna(False).any(), stock_id


def test_retrospective_launch_rate_is_not_misreported_as_first_breakout_win_rate() -> None:
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    selected = summary.loc[summary["condition_variant_id"].eq(PRIMARY_VARIANT_ID)].iloc[0]
    baseline = summary.loc[summary["condition_variant_id"].eq(BASELINE_VARIANT_ID)].iloc[0]
    assert float(selected["retrospective_launch_rate_pct"]) > float(
        baseline["retrospective_launch_rate_pct"]
    )
    assert float(selected["retrospective_launch_rate_excluding_candidates_pct"]) > float(
        baseline["retrospective_launch_rate_excluding_candidates_pct"]
    )
    assert float(selected["first_breakout_strict_success_rate_pct"]) < float(
        selected["retrospective_launch_rate_pct"]
    )


def test_4916_keeps_the_confirmation_gap_visible() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    row = detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["stock_id"].eq("4916")
        & detail["episode_status"].eq("launch_within_active_horizon")
    ].iloc[0]
    assert row["first_breakout_outcome"] == "mature_failure"
    assert row["launch_date"] == "20260518"


def test_source_first_condition_preserves_aligned_qualifying_revenue_lineage() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    for row in detail.itertuples(index=False):
        periods = str(row.qualifying_revenue_periods).split("|")
        source_dates = str(row.qualifying_source_dates).split("|")
        resolution_ids = str(row.qualifying_cross_market_resolution_ids).split("|")
        source_hashes = str(row.qualifying_source_row_canonical_sha256s).split("|")
        canonical_dates = str(row.qualifying_canonical_source_table_dates).split("|")
        trade_dates = str(row.qualifying_trade_dates).split("|")
        sequence_indices = str(row.qualifying_sequence_indices).split("|")
        assert (
            len(periods)
            == len(source_dates)
            == len(resolution_ids)
            == len(source_hashes)
            == len(canonical_dates)
            == len(trade_dates)
            == len(sequence_indices)
        )
        assert len(periods) == int(row.qualifying_update_count)
        assert all(resolution_ids)
        assert all(len(value) == 64 for value in source_hashes)
        assert periods[0] == str(row.episode_start_revenue_period)
        assert source_dates[0] == str(row.episode_start_source_date)
        assert resolution_ids[0] == str(row.episode_start_cross_market_resolution_id)
        assert source_hashes[0] == str(row.episode_start_source_row_canonical_sha256)
        assert canonical_dates[0] == str(row.episode_start_canonical_source_table_date)
        assert trade_dates[0] == str(row.episode_start_trade_date)
        assert periods[-1] == str(row.latest_qualifying_revenue_period)
        assert source_dates[-1] == str(row.latest_qualifying_source_date)
        assert resolution_ids[-1] == str(
            row.latest_qualifying_cross_market_resolution_id
        )
        assert source_hashes[-1] == str(
            row.latest_qualifying_source_row_canonical_sha256
        )
        assert canonical_dates[-1] == str(
            row.latest_qualifying_canonical_source_table_date
        )
        assert trade_dates[-1] == str(row.latest_qualifying_trade_date)


def test_source_first_condition_emits_current_run_level_monthly_revenue_hashes(
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
) -> None:
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(DETAIL_CSV, keep_default_na=False, low_memory=False)
    current_full_lineage = current_monthly_revenue_lineage[3]
    for frame in (summary, detail):
        for column, expected in current_full_lineage.items():
            assert frame[column].astype(str).str.fullmatch(r"[0-9a-f]{64}").all()
            assert set(frame[column].astype(str)) == {expected}


def test_source_first_validator_allows_current_blob_rewrite_when_canonical_rows_unchanged(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
) -> None:
    revenue_path = tmp_path / "monthly_revenue_history.csv"
    original = validator.REVENUE_HISTORY_CSV.read_bytes()
    canonical_lf = original.replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    expected_blob_sha = current_monthly_revenue_lineage[3][
        "monthly_revenue_history_blob_sha256"
    ]
    rewritten = next(
        candidate
        for extra_blank_lines in range(1, 4)
        if (candidate := canonical_lf + (b"\n" * extra_blank_lines)) != original
        and hashlib.sha256(candidate).hexdigest() != expected_blob_sha
    )
    revenue_path.write_bytes(rewritten)

    assert revenue_path.read_bytes() != original
    current = validator._current_monthly_revenue_lineage(
        revenue_path,
        validator.MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    )
    assert current[:2] == current_monthly_revenue_lineage[:2]
    assert current[3]["monthly_revenue_history_blob_sha256"] != (
        current_monthly_revenue_lineage[3]["monthly_revenue_history_blob_sha256"]
    )
    assert current[3]["monthly_revenue_canonical_table_sha256"] == (
        current_monthly_revenue_lineage[3]["monthly_revenue_canonical_table_sha256"]
    )
    _bind_outputs_to_current_full_lineage(
        tmp_path,
        monkeypatch,
        current_monthly_revenue_lineage[3],
    )
    diagnostics: list[str] = []
    assert validator.validate(
        revenue_path=revenue_path,
        diagnostics=diagnostics,
    ) == []
    assert any("provenance-only" in diagnostic for diagnostic in diagnostics)


def test_source_first_validator_allows_post_cutoff_revenue_append(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
) -> None:
    revenue_path = tmp_path / "monthly_revenue_history.csv"
    revenue_path.write_bytes(validator.REVENUE_HISTORY_CSV.read_bytes())
    future = pd.read_csv(
        validator.REVENUE_HISTORY_CSV,
        dtype=str,
        keep_default_na=False,
        nrows=1,
    )
    future.loc[0, "stock_id"] = "9998"
    future.loc[0, "stock_name"] = "post-cutoff-only"
    future.loc[0, "source_table_date"] = "20260714"
    future.to_csv(revenue_path, mode="a", header=False, index=False)

    current = validator._current_monthly_revenue_lineage(
        revenue_path,
        validator.MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    )
    assert current[:2] == current_monthly_revenue_lineage[:2]
    assert current[3]["monthly_revenue_history_blob_sha256"] != (
        current_monthly_revenue_lineage[3]["monthly_revenue_history_blob_sha256"]
    )
    assert current[3]["monthly_revenue_canonical_table_sha256"] != (
        current_monthly_revenue_lineage[3]["monthly_revenue_canonical_table_sha256"]
    )
    summary, detail = _bind_outputs_to_current_full_lineage(
        tmp_path,
        monkeypatch,
        current[3],
    )
    assert validator.validate(revenue_path=revenue_path) == []
    for frame in (summary, detail):
        for column, expected in current[3].items():
            assert set(frame[column].astype(str)) == {expected}


def test_source_first_validator_does_not_bind_current_outputs_to_manifest_full_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
) -> None:
    manifest_path = tmp_path / "projection_manifest.csv"
    manifest = pd.read_csv(
        validator.SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    manifest.to_csv(manifest_path, index=False)
    manifest_lineage = {
        column: str(manifest.iloc[0][column]).strip().lower()
        for column in validator.RUN_LINEAGE_COLUMNS
    }
    current_full_lineage = _lineage_distinct_from(manifest_lineage)
    _bind_outputs_to_current_full_lineage(
        tmp_path,
        monkeypatch,
        current_full_lineage,
    )
    monkeypatch.setattr(
        validator,
        "_current_monthly_revenue_lineage",
        lambda *_args: (
            current_monthly_revenue_lineage[0],
            current_monthly_revenue_lineage[1],
            current_monthly_revenue_lineage[2],
            current_full_lineage,
        ),
    )

    errors = validator.validate(projection_manifest_path=manifest_path)

    assert errors == []


def test_source_first_validator_rejects_manifest_full_lineage_in_current_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
) -> None:
    manifest = pd.read_csv(
        validator.SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    manifest_lineage = {
        column: str(manifest.iloc[0][column]).strip().lower()
        for column in validator.RUN_LINEAGE_COLUMNS
    }
    current_full_lineage = _lineage_distinct_from(manifest_lineage)
    _bind_outputs_to_current_full_lineage(
        tmp_path,
        monkeypatch,
        manifest_lineage,
    )
    monkeypatch.setattr(
        validator,
        "_current_monthly_revenue_lineage",
        lambda *_args: (
            current_monthly_revenue_lineage[0],
            current_monthly_revenue_lineage[1],
            current_monthly_revenue_lineage[2],
            current_full_lineage,
        ),
    )

    diagnostics: list[str] = []
    errors = validator.validate(diagnostics=diagnostics)

    for column in (
        "monthly_revenue_canonical_table_sha256",
        "cross_market_resolution_registry_canonical_sha256",
    ):
        assert any(
            f"current full monthly revenue lineage drift: {column}" in error
            for error in errors
        )
    assert not any(
        "current full monthly revenue lineage drift: "
        "monthly_revenue_history_blob_sha256" in error
        for error in errors
    )
    assert any(
        "monthly_revenue_history_blob_sha256 differs from the current mutable blob"
        in diagnostic
        for diagnostic in diagnostics
    )


@pytest.mark.parametrize(
    ("column", "value", "expected_error"),
    (
        ("cutoff_date", "20260714", "projection cutoff drift"),
        ("cutoff_date", "20260713garbage", "projection cutoff drift"),
        (
            "cutoff_revenue_subset_row_count",
            "49024",
            "current cutoff monthly revenue row count drift",
        ),
        (
            "cutoff_revenue_subset_semantic_sha256",
            "f" * 64,
            "current cutoff monthly revenue semantic lineage drift",
        ),
        (
            "formal_model_use_allowed",
            "True",
            "formal-use flags must remain canonical false",
        ),
        (
            "formal_model_use_allowed",
            "garbage",
            "formal-use flags must remain canonical false",
        ),
        (
            "research_only",
            "yes",
            "research_only must be canonical true",
        ),
    ),
)
def test_source_first_validator_rejects_projection_contract_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
    column: str,
    value: str,
    expected_error: str,
) -> None:
    manifest_path = tmp_path / "projection_manifest.csv"
    manifest = pd.read_csv(
        validator.SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    manifest.loc[0, column] = value
    manifest.to_csv(manifest_path, index=False)
    monkeypatch.setattr(
        validator,
        "_current_monthly_revenue_lineage",
        lambda *_args: current_monthly_revenue_lineage,
    )

    errors = validator.validate(projection_manifest_path=manifest_path)

    assert any(expected_error in error for error in errors)


def test_source_first_validator_rejects_pre_cutoff_source_payload_mutation(
    tmp_path: Path,
) -> None:
    revenue_path = tmp_path / "monthly_revenue_history.csv"
    raw = pd.read_csv(
        validator.REVENUE_HISTORY_CSV,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    target = (
        raw["stock_id"].eq("1101")
        & raw["revenue_period"].eq("202405")
        & raw["source_table_date"].eq("20240617")
    )
    assert int(target.sum()) == 1
    original_value = raw.loc[target, "monthly_revenue"].iloc[0]
    raw.loc[target, "monthly_revenue"] = str(int(original_value) + 1)
    raw.to_csv(revenue_path, index=False)

    errors = validator.validate(revenue_path=revenue_path)

    assert any(
        "current cutoff monthly revenue semantic lineage drift" in error
        for error in errors
    )


def test_price_projection_excludes_future_rows_and_future_resolution(
    tmp_path: Path,
) -> None:
    price_path = tmp_path / "9999.csv"
    pd.DataFrame(
        {
            "date": ["20260711", "20260713", "20260714"],
            "open": [10.0, 11.0, 12.0],
            "high": [10.5, 11.5, 12.5],
            "low": [9.5, 10.5, 11.5],
            "close": [10.0, 11.0, 12.0],
            "volume": [1_000_000, 1_000_000, 1_000_000],
            "volume_ratio": [1.0, 1.0, 1.0],
        }
    ).to_csv(price_path, index=False)
    resolutions = pd.DataFrame(
        {
            "stock_id": ["9999"],
            "resume_date": ["20260714"],
            "exchange_ratio": [0.5],
            "resolution_id": ["future_resolution"],
        }
    )

    projected = load_stock_price(
        "9999",
        price_path,
        resolutions,
        observation_cutoff_date="20260713",
    )

    assert projected["date"].tolist() == ["20260711", "20260713"]
    assert projected["analysis_price_adjustment_factor"].eq(1.0).all()
    assert projected["price_resolution_ids_on_date"].eq("").all()


@pytest.mark.parametrize(
    "mutation",
    (
        "run_sha",
        "aligned_source_hash",
        "aligned_source_date",
        "aligned_resolution_id",
    ),
)
def test_source_first_validator_rejects_monthly_revenue_lineage_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    current_monthly_revenue_lineage: MonthlyRevenueLineage,
    mutation: str,
) -> None:
    summary_path = tmp_path / "summary.csv"
    detail_path = tmp_path / "detail.csv"
    markdown_path = tmp_path / "summary.md"
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={
            "stock_id": str,
            "qualifying_source_dates": str,
            "episode_start_source_date": str,
        },
        keep_default_na=False,
    )
    markdown_path.write_bytes(validator.LATEST_MD.read_bytes())
    if mutation == "run_sha":
        summary.loc[0, "monthly_revenue_history_blob_sha256"] = "0" * 64
    else:
        row = detail.index[0]
        if mutation == "aligned_source_hash":
            values = str(detail.at[row, "qualifying_source_row_canonical_sha256s"]).split("|")
            values[0] = "f" * 64
            detail.at[row, "qualifying_source_row_canonical_sha256s"] = "|".join(values)
            detail.at[row, "episode_start_source_row_canonical_sha256"] = values[0]
        elif mutation == "aligned_source_date":
            values = str(detail.at[row, "qualifying_source_dates"]).split("|")
            values[0] = "19990101"
            detail.at[row, "qualifying_source_dates"] = "|".join(values)
            detail.at[row, "episode_start_source_date"] = values[0]
        else:
            values = str(detail.at[row, "qualifying_cross_market_resolution_ids"]).split("|")
            values[0] = "mutated-resolution"
            detail.at[row, "qualifying_cross_market_resolution_ids"] = "|".join(values)
            detail.at[row, "episode_start_cross_market_resolution_id"] = values[0]
    summary.to_csv(summary_path, index=False)
    detail.to_csv(detail_path, index=False)
    monkeypatch.setattr(validator, "LATEST_CSV", summary_path)
    monkeypatch.setattr(validator, "DETAIL_CSV", detail_path)
    monkeypatch.setattr(validator, "LATEST_MD", markdown_path)
    monkeypatch.setattr(
        validator,
        "_current_monthly_revenue_lineage",
        lambda *_args: current_monthly_revenue_lineage,
    )
    diagnostics: list[str] = []
    errors = validator.validate(diagnostics=diagnostics)
    if mutation == "run_sha":
        assert errors == []
        assert any("provenance-only" in diagnostic for diagnostic in diagnostics)
    else:
        assert any("lineage drift" in error for error in errors)
def test_full_lineage_raw_blob_is_diagnostic_and_canonical_hashes_are_hard() -> None:
    current = {
        "monthly_revenue_history_blob_sha256": "a" * 64,
        "monthly_revenue_canonical_table_sha256": "b" * 64,
        "cross_market_resolution_registry_canonical_sha256": "c" * 64,
    }
    frame = pd.DataFrame(
        [
            {
                "monthly_revenue_history_blob_sha256": "d" * 64,
                "monthly_revenue_canonical_table_sha256": "b" * 64,
                "cross_market_resolution_registry_canonical_sha256": "c" * 64,
            }
        ]
    )
    diagnostics: list[str] = []

    assert validator._full_lineage_capture_errors(
        frame,
        name="summary",
        current_full_lineage=current,
        diagnostics=diagnostics,
    ) == []
    assert any("provenance-only" in diagnostic for diagnostic in diagnostics)

    frame.loc[0, "monthly_revenue_canonical_table_sha256"] = "e" * 64
    errors = validator._full_lineage_capture_errors(
        frame,
        name="summary",
        current_full_lineage=current,
    )
    assert any("monthly_revenue_canonical_table_sha256" in error for error in errors)
