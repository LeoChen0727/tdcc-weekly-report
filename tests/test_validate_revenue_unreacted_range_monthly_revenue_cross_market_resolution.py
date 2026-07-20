from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (  # noqa: E402
    BUSINESS_PAYLOAD_COLUMNS,
    RESOLUTION_CSV,
    cross_market_resolution_registry_canonical_sha256,
)
from validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution import (  # noqa: E402
    VALIDATION_CLASSIFICATION,
    independent_cross_market_resolution_registry_canonical_sha256,
    independent_monthly_revenue_raw_row_sha256,
    validate,
)


def _row(
    market: str,
    source_market_name: str,
    source_table_date: str,
    *,
    stock_id: str = "5236",
    revenue_period: str = "202606",
    monthly_revenue: str = "192161",
) -> dict[str, str]:
    source_suffix = "L" if source_market_name == "TWSE" else "O"
    row = {column: "" for column in BUSINESS_PAYLOAD_COLUMNS}
    row.update(
        {
            "market": market,
            "source_market_name": source_market_name,
            "source_table_date": source_table_date,
            "source_kind": "official_mops_current_monthly_revenue_openapi",
            "source_url": (
                f"https://mopsfin.twse.com.tw/opendata/t187ap05_{source_suffix}.csv"
            ),
            "source_file": (
                "data/monthly_revenue_history/raw/"
                f"monthly_revenue_raw_{market}_{source_table_date}_{revenue_period}.csv"
            ),
            "stock_id": stock_id,
            "stock_name": "凌陽創新",
            "industry": "半導體業",
            "revenue_period": revenue_period,
            "revenue_period_roc": "11506",
            "monthly_revenue": monthly_revenue,
            "previous_month_revenue": "201026",
            "last_year_month_revenue": "170388",
            "month_over_month_pct": "-4.409877",
            "latest_revenue_yoy_pct": "12.778482",
            "cumulative_revenue": "1167421",
            "last_year_cumulative_revenue": "991235",
            "cumulative_revenue_yoy_pct": "17.774393",
            "note": "-",
            "revenue_positive_flag": "True",
            "revenue_strong_flag": "True",
            "revenue_numerical_anomaly_flag": "False",
            "point_in_time_status": "ready_official_source_table_date",
            "research_join_allowed": "True",
            "allowed_for_formal_historical_model_use": "False",
            "formal_use_blocker": "blocked_until_sufficient_history_coverage_and_model_promotion",
            "coverage_note": (
                "full_market_current_monthly_revenue_saved_from_official_openapi; "
                "historical coverage starts at the first saved source table date unless "
                "separately backfilled"
            ),
        }
    )
    return row


def _fixture_paths(tmp_path: Path) -> tuple[Path, Path, Path]:
    data_path = tmp_path / "monthly_revenue_history.csv"
    mirror_path = tmp_path / "monthly_revenue_history_latest.csv"
    resolution_path = tmp_path / "resolution.csv"
    pd.DataFrame(
        [
            _row("otc", "TPEX", "20260715"),
            _row("listed", "TWSE", "20260717"),
        ]
    ).to_csv(data_path, index=False, lineterminator="\n")
    shutil.copyfile(data_path, mirror_path)
    shutil.copyfile(RESOLUTION_CSV, resolution_path)
    return data_path, mirror_path, resolution_path


def test_independent_lineage_validator_passes_equal_blob_rows_and_exact_5236_identity(
    tmp_path: Path,
) -> None:
    paths = _fixture_paths(tmp_path)
    assert validate(*paths) == []
    assert VALIDATION_CLASSIFICATION.endswith("not_promotion_evidence")


def test_independent_lineage_validator_rejects_blob_drift(tmp_path: Path) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    mirror_path.write_bytes(mirror_path.read_bytes() + b"\n")
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("blob SHA-256 mismatch" in error for error in errors)


def test_independent_lineage_validator_rejects_payload_conflict(tmp_path: Path) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    frame = pd.read_csv(data_path, dtype=str, keep_default_na=False)
    frame.loc[1, "monthly_revenue"] = "192162"
    frame.to_csv(data_path, index=False, lineterminator="\n")
    shutil.copyfile(data_path, mirror_path)
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("business payload conflict" in error for error in errors)


def test_independent_lineage_validator_rejects_missing_registered_raw_side(
    tmp_path: Path,
) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    frame = pd.read_csv(data_path, dtype=str, keep_default_na=False).iloc[[0]]
    frame.to_csv(data_path, index=False, lineterminator="\n")
    shutil.copyfile(data_path, mirror_path)
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("absent from monthly history" in error for error in errors)
    assert any("exactly two registered mirror rows" in error for error in errors)


def test_independent_lineage_validator_rejects_raw_lineage_mutation(
    tmp_path: Path,
) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    frame = pd.read_csv(data_path, dtype=str, keep_default_na=False)
    frame.loc[1, "source_file"] = "data/monthly_revenue_history/raw/mutated.csv"
    frame.to_csv(data_path, index=False, lineterminator="\n")
    shutil.copyfile(data_path, mirror_path)
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("source row identities mismatch" in error for error in errors)


@pytest.mark.parametrize(
    ("column", "value"),
    (
        ("revenue_period", "2026069"),
        ("revenue_period", "202606x"),
        ("source_table_date", "202607159"),
        ("source_table_date", "20260715x"),
    ),
)
def test_independent_lineage_validator_rejects_date_and_period_aliases(
    tmp_path: Path,
    column: str,
    value: str,
) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    frame = pd.read_csv(data_path, dtype=str, keep_default_na=False)
    frame.loc[0, column] = value
    frame.to_csv(data_path, index=False, lineterminator="\n")
    shutil.copyfile(data_path, mirror_path)
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("must be exact digits" in error for error in errors)


def test_independent_lineage_validator_rejects_noncanonical_resolution_date(
    tmp_path: Path,
) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    registry = pd.read_csv(resolution_path, dtype=str, keep_default_na=False)
    registry.loc[0, "canonical_source_table_date"] = "20260717"
    registry.to_csv(resolution_path, index=False, lineterminator="\n")
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("canonical_source_table_date" in error for error in errors)
    assert any("not the earliest official" in error for error in errors)


def test_independent_registry_hash_matches_helper_and_binds_config_semantics() -> None:
    registry = pd.read_csv(RESOLUTION_CSV, dtype=str, keep_default_na=False)
    expected = cross_market_resolution_registry_canonical_sha256(registry)
    assert (
        independent_cross_market_resolution_registry_canonical_sha256(registry)
        == expected
    )
    mutated = registry.copy()
    mutated.loc[0, "evidence_url"] = "https://example.com/semantic-mutation"
    assert (
        independent_cross_market_resolution_registry_canonical_sha256(mutated)
        != expected
    )
    notes_only = registry.copy()
    notes_only.loc[0, "notes"] = "excluded note mutation"
    assert (
        independent_cross_market_resolution_registry_canonical_sha256(notes_only)
        == expected
    )


def test_independent_validator_rejects_registry_raw_hash_mutation(
    tmp_path: Path,
) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    registry = pd.read_csv(resolution_path, dtype=str, keep_default_na=False)
    registry.loc[0, "earlier_raw_row_canonical_sha256"] = "0" * 64
    registry.loc[0, "canonical_row_canonical_sha256"] = "0" * 64
    registry.to_csv(resolution_path, index=False, lineterminator="\n")
    errors = validate(data_path, mirror_path, resolution_path)
    assert any("earlier raw-row canonical SHA-256 mismatch" in error for error in errors)


def test_independent_validator_iterates_a_second_registration(
    tmp_path: Path,
) -> None:
    data_path, mirror_path, resolution_path = _fixture_paths(tmp_path)
    data = pd.read_csv(data_path, dtype=str, keep_default_na=False)
    second_rows = pd.DataFrame(
        [
            _row(
                "otc",
                "TPEX",
                "20260710",
                stock_id="9999",
                revenue_period="202605",
                monthly_revenue="100",
            ),
            _row(
                "listed",
                "TWSE",
                "20260712",
                stock_id="9999",
                revenue_period="202605",
                monthly_revenue="100",
            ),
        ]
    )
    second_rows.loc[:, "revenue_period_roc"] = "11505"
    data = pd.concat([data, second_rows], ignore_index=True)
    data.to_csv(data_path, index=False, lineterminator="\n")
    shutil.copyfile(data_path, mirror_path)

    registry = pd.read_csv(resolution_path, dtype=str, keep_default_na=False)
    second = registry.iloc[0].copy()
    earlier_hash = independent_monthly_revenue_raw_row_sha256(second_rows.iloc[0])
    later_hash = independent_monthly_revenue_raw_row_sha256(second_rows.iloc[1])
    second.update(
        {
            "resolution_id": "revenue_unreacted_range_9999_202605_cross_market_mirror",
            "stock_id": "9999",
            "revenue_period": "202605",
            "earlier_source_table_date": "20260710",
            "earlier_source_file": (
                "data/monthly_revenue_history/raw/"
                "monthly_revenue_raw_otc_20260710_202605.csv"
            ),
            "earlier_raw_row_canonical_sha256": earlier_hash,
            "later_source_table_date": "20260712",
            "later_source_file": (
                "data/monthly_revenue_history/raw/"
                "monthly_revenue_raw_listed_20260712_202605.csv"
            ),
            "later_raw_row_canonical_sha256": later_hash,
            "official_market_transition_date": "20260711",
            "canonical_source_table_date": "20260710",
            "canonical_row_canonical_sha256": earlier_hash,
            "evidence_url": "https://example.com/9999-market-transition",
            "notes": "second registered fixture",
        }
    )
    registry = pd.concat([registry, second.to_frame().T], ignore_index=True)
    registry.to_csv(resolution_path, index=False, lineterminator="\n")
    assert validate(data_path, mirror_path, resolution_path) == []

    registry.loc[1, "later_raw_row_canonical_sha256"] = "0" * 64
    registry.to_csv(resolution_path, index=False, lineterminator="\n")
    errors = validate(data_path, mirror_path, resolution_path)
    assert any(
        "9999/202605 later raw-row canonical SHA-256 mismatch" in error
        for error in errors
    )
