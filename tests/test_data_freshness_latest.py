from pathlib import Path

import build_data_freshness_latest as freshness


def test_warrant_flow_date_falls_back_to_by_stock_when_flow_is_header_only(tmp_path, monkeypatch):
    flow = tmp_path / "warrant_flow_latest.csv"
    by_stock = tmp_path / "warrant_flow_by_stock_latest.csv"
    market_report = tmp_path / "warrant_market_report_latest.md"
    fetch_report = tmp_path / "warrant_daily_fetch_latest.md"

    flow.write_text("date,stock_id,warrant_flow_signal\n", encoding="utf-8")
    by_stock.write_text(
        "date,stock_id,stock_name,warrant_flow_signal\n"
        "20260605,,,\n",
        encoding="utf-8",
    )
    market_report.write_text("", encoding="utf-8")
    fetch_report.write_text("", encoding="utf-8")

    monkeypatch.setattr(freshness, "WARRANT_FLOW_CSV", flow)
    monkeypatch.setattr(freshness, "WARRANT_FLOW_BY_STOCK_CSV", by_stock)
    monkeypatch.setattr(freshness, "WARRANT_MARKET_REPORT_MD", market_report)
    monkeypatch.setattr(freshness, "WARRANT_DAILY_FETCH_MD", fetch_report)

    assert freshness.extract_warrant_flow_date() == "20260605"
    assert freshness.extract_warrant_flow_state() == (
        "20260605",
        False,
        "warrant data date present but stock-level rows unavailable or observe-only in warrant_flow_by_stock_latest.csv",
    )


def test_warrant_flow_date_falls_back_to_market_report_when_csvs_have_no_rows(tmp_path, monkeypatch):
    flow = tmp_path / "warrant_flow_latest.csv"
    by_stock = tmp_path / "warrant_flow_by_stock_latest.csv"
    market_report = tmp_path / "warrant_market_report_latest.md"
    fetch_report = tmp_path / "warrant_daily_fetch_latest.md"

    flow.write_text("date,stock_id,warrant_flow_signal\n", encoding="utf-8")
    by_stock.write_text("date,stock_id,warrant_flow_signal\n", encoding="utf-8")
    market_report.write_text("- data_date: `20260605`\n- raw_rows: `0`\n", encoding="utf-8")
    fetch_report.write_text("", encoding="utf-8")

    monkeypatch.setattr(freshness, "WARRANT_FLOW_CSV", flow)
    monkeypatch.setattr(freshness, "WARRANT_FLOW_BY_STOCK_CSV", by_stock)
    monkeypatch.setattr(freshness, "WARRANT_MARKET_REPORT_MD", market_report)
    monkeypatch.setattr(freshness, "WARRANT_DAILY_FETCH_MD", fetch_report)

    assert freshness.extract_warrant_flow_date() == "20260605"
    assert freshness.extract_warrant_flow_state() == (
        "20260605",
        False,
        "warrant data date present but stock-level rows unavailable or observe-only in warrant_market_report_latest.md",
    )


def test_warrant_ready_requires_usable_stock_level_rows():
    ready, note = freshness.determine_warrant_ready(
        main_price_date="20260605",
        warrant_flow_date="20260605",
        warrant_data_ready=False,
        warrant_data_note="warrant data date present but stock-level rows unavailable or observe-only",
    )

    assert ready is False
    assert "stock-level warrant data is unavailable" in note


def test_warrant_flow_state_prefers_current_observe_only_over_stale_rows(tmp_path, monkeypatch):
    flow = tmp_path / "warrant_flow_latest.csv"
    by_stock = tmp_path / "warrant_flow_by_stock_latest.csv"
    market_report = tmp_path / "warrant_market_report_latest.md"
    fetch_report = tmp_path / "warrant_daily_fetch_latest.md"

    flow.write_text(
        "date,stock_id,warrant_flow_signal\n"
        "20260603,2330,call_inflow\n",
        encoding="utf-8",
    )
    by_stock.write_text(
        "date,stock_id,stock_name,warrant_flow_signal,data_quality_note\n"
        "20260605,,,,權證原始資料不足 / 僅能觀察\n",
        encoding="utf-8",
    )
    market_report.write_text("", encoding="utf-8")
    fetch_report.write_text("", encoding="utf-8")

    monkeypatch.setattr(freshness, "WARRANT_FLOW_CSV", flow)
    monkeypatch.setattr(freshness, "WARRANT_FLOW_BY_STOCK_CSV", by_stock)
    monkeypatch.setattr(freshness, "WARRANT_MARKET_REPORT_MD", market_report)
    monkeypatch.setattr(freshness, "WARRANT_DAILY_FETCH_MD", fetch_report)

    assert freshness.extract_warrant_flow_state() == (
        "20260605",
        False,
        "warrant data date present but stock-level rows unavailable or observe-only in warrant_flow_by_stock_latest.csv",
    )


def test_group_rotation_theme_state_rejects_unreadable_pdf_theme_values(tmp_path, monkeypatch):
    group_rotation = tmp_path / "daily_candidate_group_rotation_latest.csv"
    group_rotation.write_text(
        "theme,theme_display_zh,theme_resolution_status\n"
        "其他,其他,resolved\n"
        "91,91,resolved\n"
        "DR_or_foreign_listing,DR_or_foreign_listing,resolved\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(freshness, "GROUP_ROTATION_CSV", group_rotation)

    ready, note = freshness.group_rotation_theme_state()

    assert ready is False
    assert "unresolved/raw theme rows" in note


def test_daily_pdf_ready_requires_resolved_group_rotation_theme_display():
    ready, note = freshness.determine_daily_pdf_ready(
        report_ready=True,
        warrant_ready=True,
        warrant_publish_allowed=True,
        report_ready_note="core daily data dates match main_price_date",
        warrant_ready_note="warrant_flow_date matches main_price_date",
        warrant_source_status="ok",
        warrant_pdf_visibility="visible",
        group_rotation_theme_ready=False,
        group_rotation_theme_note="group rotation has unresolved/raw theme rows",
    )

    assert ready is False
    assert "group rotation theme display not ready" in note


def test_warrant_publish_policy_resets_to_ok_when_current_warrant_is_ready():
    result = freshness.warrant_publish_policy(
        True,
        {
            "status": "warning_grace",
            "warrant_pdf_visibility": "hidden_unavailable",
            "daily_publish_allowed": "True",
            "model_effect_allowed": "False",
            "pdf_effect_allowed": "False",
        },
    )

    assert result == (
        True,
        "ok",
        "current-date warrant layer ready",
        "visible",
        "True",
        "True",
        "0",
    )


def test_daily_pdf_ready_allows_bounded_warrant_grace_without_using_warrant_layer():
    ready, note = freshness.determine_daily_pdf_ready(
        report_ready=True,
        warrant_ready=False,
        warrant_publish_allowed=True,
        report_ready_note="core daily data dates match main_price_date",
        warrant_ready_note="warrant_flow_date matches main_price_date but stock-level warrant data is unavailable",
        warrant_source_status="warning_grace",
        warrant_pdf_visibility="hidden_unavailable",
        group_rotation_theme_ready=True,
        group_rotation_theme_note="group rotation themes resolved for PDF display",
    )

    assert ready is True
    assert "warrant source unavailable within bounded grace" in note
    assert "warrant_pdf_visibility=hidden_unavailable" in note


def test_daily_pdf_ready_rejects_warrant_failure_outside_bounded_grace():
    ready, note = freshness.determine_daily_pdf_ready(
        report_ready=True,
        warrant_ready=False,
        warrant_publish_allowed=False,
        report_ready_note="core daily data dates match main_price_date",
        warrant_ready_note="current-date warrant source failed beyond bounded grace",
        warrant_source_status="failed",
        warrant_pdf_visibility="blocked_unavailable",
        group_rotation_theme_ready=True,
        group_rotation_theme_note="group rotation themes resolved for PDF display",
    )

    assert ready is False
    assert "warrant layer not ready" in note
