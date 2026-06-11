from __future__ import annotations

from pathlib import Path

import pandas as pd

from scripts import validate_daily_publish_freshness_gate as gate


def write_freshness(path: Path, **overrides: object) -> None:
    row = {
        "generated_at": "2026-06-11 16:13:26",
        "main_price_date": "20260611",
        "actual_stock_price_history_date": "20260611",
        "stock_monitor_price_date": "20260611",
        "all_candidates_date": "20260611",
        "official_price_fetch_date": "20260611",
        "warrant_flow_date": "20260611",
        "raw_stock_monitor_price_date": "20260611",
        "raw_all_candidates_date": "20260611",
        "raw_official_price_fetch_date": "20260611",
        "raw_warrant_flow_date": "20260611",
        "report_ready": "True",
        "report_ready_note": "core daily data dates match main_price_date",
        "warrant_ready": "True",
        "warrant_ready_note": "warrant_flow_date matches main_price_date",
        "daily_pdf_ready": "True",
        "daily_pdf_ready_note": "core daily data and warrant layer are ready for daily PDF source use",
        "stock_monitor_note": "ready",
        "all_candidates_note": "ready",
        "official_fetch_note": "ready",
        "warrant_note": "ready",
    }
    row.update(overrides)
    pd.DataFrame([row]).to_csv(path, index=False, encoding="utf-8")


def test_publish_gate_passes_ready_current_without_regression(tmp_path):
    baseline = tmp_path / "baseline.csv"
    current = tmp_path / "current.csv"
    write_freshness(baseline)
    write_freshness(current)

    assert gate.validate_daily_publish_freshness(current, baseline) == []


def test_publish_gate_rejects_raw_official_newer_than_usable_history(tmp_path):
    current = tmp_path / "current.csv"
    write_freshness(
        current,
        main_price_date="20260605",
        actual_stock_price_history_date="20260605",
        stock_monitor_price_date="20260605",
        all_candidates_date="20260605",
        official_price_fetch_date="20260605",
        warrant_flow_date="20260602",
        raw_stock_monitor_price_date="20260605",
        raw_all_candidates_date="20260605",
        raw_official_price_fetch_date="20260611",
        raw_warrant_flow_date="20260602",
        warrant_ready="False",
        warrant_ready_note="warrant_flow_date does not match main_price_date",
        daily_pdf_ready="False",
        daily_pdf_ready_note="warrant layer not ready",
        official_fetch_note="raw_date=20260611; capped_to_actual_trading_date=20260605",
        warrant_note="stale_date=20260602",
    )

    errors = gate.validate_daily_publish_freshness(current, None)

    assert any("raw_official_price_fetch_date is newer" in error for error in errors)
    assert any("daily_pdf_ready must be True" in error for error in errors)


def test_publish_gate_rejects_baseline_regression(tmp_path):
    baseline = tmp_path / "baseline.csv"
    current = tmp_path / "current.csv"
    write_freshness(baseline)
    write_freshness(
        current,
        main_price_date="20260605",
        actual_stock_price_history_date="20260605",
        stock_monitor_price_date="20260605",
        all_candidates_date="20260605",
        official_price_fetch_date="20260605",
        warrant_flow_date="20260605",
        raw_stock_monitor_price_date="20260605",
        raw_all_candidates_date="20260605",
        raw_official_price_fetch_date="20260605",
        raw_warrant_flow_date="20260605",
    )

    errors = gate.validate_daily_publish_freshness(current, baseline)

    assert "main_price_date regressed from 20260611 to 20260605" in errors
    assert "actual_stock_price_history_date regressed from 20260611 to 20260605" in errors
