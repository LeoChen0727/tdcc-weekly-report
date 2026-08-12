from __future__ import annotations

from scripts import validate_recent_daily_price_repair_staged_paths as validator


def test_date_scoped_source_bundle_paths_are_exactly_allowed() -> None:
    prefix = "output/history/daily_source_bundles/20260811/daily-source-20260811-run-1/"
    entries = [
        ("A", (prefix + "manifest.json",)),
        ("A", (prefix + "state.json",)),
        ("A", (prefix + "market_session_status.json",)),
        ("A", (prefix + "files/01-20260811.csv",)),
        ("A", (prefix + "files/02-daily_price_20260811.csv",)),
        ("A", (prefix + "files/03-official_daily_price_latest.csv",)),
        ("A", (prefix + "files/04-exceptional_non_trading_days.csv",)),
        ("M", ("output/latest/official_daily_price_latest.csv",)),
    ]
    assert validator.validate_entries(entries) == []


def test_source_bundle_path_escape_and_extra_payload_are_rejected() -> None:
    prefix = "output/history/daily_source_bundles/20260811/daily-source-20260811-run-1/"
    errors = validator.validate_entries(
        [
            ("A", (prefix + "files/05-extra.csv",)),
            ("A", (prefix + "../escaped.json",)),
        ]
    )
    assert len(errors) == 2


def test_exact_data_only_repair_paths_are_allowed() -> None:
    entries = [
        ("A", ("data/daily_price/daily_price_20260730.csv",)),
        ("A", ("data/daily_price/20260730.csv",)),
        ("M", ("data/stock_price_history/2330.csv",)),
        ("M", ("data/market_calendar/exceptional_non_trading_days.csv",)),
        ("M", ("output/latest/recent_daily_price_gap_repair_latest.json",)),
        ("M", ("output/latest/repair_daily_" + "price_range_latest.csv",)),
        ("M", ("output/latest/stock_price_history_manifest.md",)),
        ("M", ("docs/latest/stock_price_history_manifest.json",)),
    ]

    assert validator.validate_entries(entries) == []


def test_model_pdf_and_unexpected_paths_are_rejected() -> None:
    entries = [
        ("M", ("output/latest/all_candidates_latest.csv",)),
        ("A", ("output/latest/daily_market_summary_latest.pdf",)),
        ("M", ("scripts/repair_recent_daily_" + "price_gaps.py",)),
    ]

    errors = validator.validate_entries(entries)

    assert len(errors) == 3
    assert all("not allowed" in error for error in errors)


def test_deletion_rename_copy_and_empty_index_are_rejected() -> None:
    assert validator.validate_entries([]) == [
        "recent daily-price repair has no staged paths to validate"
    ]
    for entry in (
        ("D", ("data/daily_price/20260730.csv",)),
        ("R", ("data/daily_price/20260730.csv", "data/daily_price/20260731.csv")),
        ("C", ("data/stock_price_history/2330.csv", "data/stock_price_history/2331.csv")),
    ):
        errors = validator.validate_entries([entry])
        assert len(errors) == 1
        assert "must be add/modify only" in errors[0]
