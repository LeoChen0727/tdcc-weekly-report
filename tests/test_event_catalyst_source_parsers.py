from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_event_calendar_data as calendar  # noqa: E402
import update_event_catalyst_data as catalyst  # noqa: E402


def test_bls_release_table_parser_extracts_macro_rows(monkeypatch) -> None:
    html = """
    <html><body>
      <table>
        <tr><th>Reference Month</th><th>Release Date</th><th>Release Time</th></tr>
        <tr><td>May 2026</td><td>Jun. 10, 2026</td><td>08:30 AM</td></tr>
        <tr><td>June 2026</td><td>Jul. 14, 2026</td><td>08:30 AM</td></tr>
      </table>
    </body></html>
    """

    def fake_fetch_text(url: str):
        return html, {"url": url, "status": "ok", "rows": 0, "error": "", "http_status": 200}

    monkeypatch.setattr(calendar, "fetch_text", fake_fetch_text)

    rows, status = calendar.parse_bls_release_events(
        "https://www.bls.gov/schedule/news_release/cpi.htm",
        "CPI release schedule",
        "US_CPI",
        "US_CPI;inflation",
        "high",
        date(2026, 6, 14),
    )

    assert status["status"] == "ok"
    assert status["rows"] == 2
    assert rows["event_date"].tolist() == ["20260610", "20260714"]
    assert set(rows["event_type"]) == {"US_CPI"}


def test_twse_ex_right_failed_fetch_uses_protected_recent_cache(tmp_path, monkeypatch) -> None:
    cached_path = tmp_path / "company_event_calendar.csv"
    status_path = tmp_path / "calendar_data_source_status_latest.json"
    cached = {col: "" for col in calendar.COMPANY_COLUMNS}
    cached.update(
        {
            "event_date": "20260622",
            "event_end_date": "20260622",
            "stock_id": "2330",
            "stock_name": "\u53f0\u7a4d\u96fb",
            "market": "TWSE",
            "event_type": "ex_dividend",
            "event_name": "\u9664\u606f",
            "event_status": "confirmed",
            "event_confidence": "high",
            "catalyst_tags": "dividend_calendar",
            "source": calendar.TWSE_EX_RIGHT_SOURCE,
            "source_url": calendar.TWSE_EX_RIGHT_URL,
            "days_to_event": "3",
            "proximity_bucket": "within_3d",
            "expected_impact": "calendar_event_not_standalone_catalyst",
            "notes": "cash_dividend=1.0",
            "last_updated": "2026-06-18 10:00:00 Asia/Taipei",
        }
    )
    pd.DataFrame([cached], columns=calendar.COMPANY_COLUMNS).to_csv(cached_path, index=False, encoding="utf-8-sig")

    def fake_fetch_json(url: str):
        return None, {"url": url, "status": "failed", "rows": 0, "error": "timeout", "http_status": ""}

    monkeypatch.setattr(calendar, "COMPANY_EVENT_CALENDAR", cached_path)
    monkeypatch.setattr(calendar, "STATUS_JSON", status_path)
    monkeypatch.setattr(calendar, "fetch_json", fake_fetch_json)

    rows, status = calendar.twse_ex_right_rows(date(2026, 6, 19))

    assert status["status"] == "stale_ok"
    assert status["cached_rows"] == 1
    assert status["consecutive_live_failures"] == 1
    assert status["model_effect_allowed"] is False
    assert status["pdf_effect_allowed"] is False
    assert len(rows) == 1
    row = rows.iloc[0]
    assert row["event_status"] == "source_stale_cached"
    assert row["event_confidence"] == "low"
    assert str(row["days_to_event"]) == "3"
    assert "calendar_source_stale" in row["catalyst_tags"]
    assert "calendar_source_degraded" in row["catalyst_tags"]
    assert "model_effect_allowed=False" in row["notes"]
    assert "pdf_effect_allowed=False" in row["notes"]


def test_twse_ex_right_failed_fetch_without_recent_cache_stays_failed(tmp_path, monkeypatch) -> None:
    cached_path = tmp_path / "missing_company_event_calendar.csv"
    status_path = tmp_path / "calendar_data_source_status_latest.json"

    def fake_fetch_json(url: str):
        return None, {"url": url, "status": "failed", "rows": 0, "error": "timeout", "http_status": ""}

    monkeypatch.setattr(calendar, "COMPANY_EVENT_CALENDAR", cached_path)
    monkeypatch.setattr(calendar, "STATUS_JSON", status_path)
    monkeypatch.setattr(calendar, "fetch_json", fake_fetch_json)

    rows, status = calendar.twse_ex_right_rows(date(2026, 6, 19))

    assert status["status"] == "failed"
    assert status["cached_rows"] == 0
    assert rows.empty


def test_twse_ex_right_failed_fetch_expires_after_consecutive_failures(tmp_path, monkeypatch) -> None:
    cached_path = tmp_path / "company_event_calendar.csv"
    status_path = tmp_path / "calendar_data_source_status_latest.json"
    cached = {col: "" for col in calendar.COMPANY_COLUMNS}
    cached.update(
        {
            "event_date": "20260622",
            "event_end_date": "20260622",
            "stock_id": "2330",
            "stock_name": "\u53f0\u7a4d\u96fb",
            "market": "TWSE",
            "event_type": "ex_dividend",
            "event_name": "\u9664\u606f",
            "event_status": "confirmed",
            "event_confidence": "high",
            "catalyst_tags": "dividend_calendar",
            "source": calendar.TWSE_EX_RIGHT_SOURCE,
            "source_url": calendar.TWSE_EX_RIGHT_URL,
            "days_to_event": "3",
            "proximity_bucket": "within_3d",
            "expected_impact": "calendar_event_not_standalone_catalyst",
            "notes": "cash_dividend=1.0",
            "last_updated": "2026-06-18 10:00:00 Asia/Taipei",
        }
    )
    pd.DataFrame([cached], columns=calendar.COMPANY_COLUMNS).to_csv(cached_path, index=False, encoding="utf-8-sig")
    status_path.write_text(
        '{"sources":{"twse_ex_right_ex_dividend":{"status":"stale_ok","consecutive_live_failures":2,"first_live_failure_at":"2026-06-17 10:00:00 Asia/Taipei"}}}',
        encoding="utf-8",
    )

    def fake_fetch_json(url: str):
        return None, {"url": url, "status": "failed", "rows": 0, "error": "timeout", "http_status": ""}

    monkeypatch.setattr(calendar, "COMPANY_EVENT_CALENDAR", cached_path)
    monkeypatch.setattr(calendar, "STATUS_JSON", status_path)
    monkeypatch.setattr(calendar, "fetch_json", fake_fetch_json)

    rows, status = calendar.twse_ex_right_rows(date(2026, 6, 19))

    assert status["status"] == "failed"
    assert status["consecutive_live_failures"] == 3
    assert rows.empty


def test_twse_ex_right_stale_cache_becomes_blocked_effect(tmp_path, monkeypatch) -> None:
    cached_path = tmp_path / "company_event_calendar.csv"
    status_path = tmp_path / "calendar_data_source_status_latest.json"
    cached = {col: "" for col in calendar.COMPANY_COLUMNS}
    cached.update(
        {
            "event_date": "20260622",
            "event_end_date": "20260622",
            "stock_id": "2330",
            "stock_name": "\u53f0\u7a4d\u96fb",
            "market": "TWSE",
            "event_type": "ex_dividend",
            "event_name": "\u9664\u606f",
            "event_status": "confirmed",
            "event_confidence": "high",
            "catalyst_tags": "dividend_calendar",
            "source": calendar.TWSE_EX_RIGHT_SOURCE,
            "source_url": calendar.TWSE_EX_RIGHT_URL,
            "days_to_event": "3",
            "proximity_bucket": "within_3d",
            "expected_impact": "calendar_event_not_standalone_catalyst",
            "notes": "cash_dividend=1.0",
            "last_updated": "2026-06-12 10:00:00 Asia/Taipei",
        }
    )
    pd.DataFrame([cached], columns=calendar.COMPANY_COLUMNS).to_csv(cached_path, index=False, encoding="utf-8-sig")

    def fake_fetch_json(url: str):
        return None, {"url": url, "status": "failed", "rows": 0, "error": "timeout", "http_status": ""}

    monkeypatch.setattr(calendar, "COMPANY_EVENT_CALENDAR", cached_path)
    monkeypatch.setattr(calendar, "STATUS_JSON", status_path)
    monkeypatch.setattr(calendar, "fetch_json", fake_fetch_json)

    rows, status = calendar.twse_ex_right_rows(date(2026, 6, 19))

    assert status["status"] == "degraded_blocked_effect"
    assert status["blocked_rows"] == 1
    assert status["model_effect_allowed"] is False
    assert status["pdf_effect_allowed"] is False
    row = rows.iloc[0]
    assert row["event_status"] == "source_degraded_blocked"
    assert row["expected_impact"] == "calendar_event_degraded_blocked_no_effect"


def test_monthly_revenue_rows_are_eps_unconfirmed(monkeypatch) -> None:
    def fake_fetch_json_list(url: str):
        if "t187ap05_L" in url:
            return [
                {
                    "\u51fa\u8868\u65e5\u671f": "1150613",
                    "\u8cc7\u6599\u5e74\u6708": "11505",
                    "\u516c\u53f8\u4ee3\u865f": "2330",
                    "\u516c\u53f8\u540d\u7a31": "\u53f0\u7a4d\u96fb",
                    "\u71df\u696d\u6536\u5165-\u53bb\u5e74\u540c\u6708\u589e\u6e1b(%)": "39.6",
                    "\u7d2f\u8a08\u71df\u696d\u6536\u5165-\u524d\u671f\u6bd4\u8f03\u589e\u6e1b(%)": "42.1",
                }
            ], {"url": url, "status": "ok", "rows": 1, "error": "", "http_status": 200}
        return [], {"url": url, "status": "ok", "rows": 0, "error": "", "http_status": 200}

    monkeypatch.setattr(catalyst, "fetch_json_list", fake_fetch_json_list)

    rows, statuses = catalyst.build_monthly_revenue_fundamental_rows(
        {"2330": {"stock_name": "\u53f0\u7a4d\u96fb", "theme_tags": "semiconductor_theme"}}
    )

    assert len(rows) == 1
    row = rows.iloc[0]
    assert row["stock_id"] == "2330"
    assert row["quarter"] == "monthly_revenue_202605"
    assert row["announcement_date"] == "20260613"
    assert row["eps_surprise_flag"] == "False"
    assert row["revenue_good_eps_unconfirmed"] == "True"
    assert statuses["TWSE monthly revenue OpenAPI"]["matched_tracked_rows"] == 1


def test_material_information_rows_are_traceable_company_sources(monkeypatch) -> None:
    def fake_fetch_json_list(url: str):
        if "t187ap04_L" in url:
            return [
                {
                    "\u767c\u8a00\u65e5\u671f": "1150613",
                    "\u516c\u53f8\u4ee3\u865f": "2330",
                    "\u516c\u53f8\u540d\u7a31": "\u53f0\u7a4d\u96fb",
                    "\u4e3b\u65e8 ": "\u63a5\u7372\u5ba2\u6236\u8a02\u55ae",
                    "\u4e8b\u5be6\u767c\u751f\u65e5": "1150612",
                    "\u8aaa\u660e": "\u5df2\u53d6\u5f97\u5ba2\u6236\u63a1\u8cfc\u5408\u7d04",
                }
            ], {"url": url, "status": "ok", "rows": 1, "error": "", "http_status": 200}
        return [], {"url": url, "status": "ok", "rows": 0, "error": "", "http_status": 200}

    monkeypatch.setattr(catalyst, "fetch_json_list", fake_fetch_json_list)

    rows, statuses = catalyst.build_material_event_rows(
        {"2330": {"stock_name": "\u53f0\u7a4d\u96fb", "theme_tags": "semiconductor_theme"}}
    )

    assert len(rows) == 1
    row = rows.iloc[0]
    assert row["event_date"] == "20260612"
    assert row["stock_id"] == "2330"
    assert row["event_type"] == "new_order"
    assert row["source"] == "TWSE material information OpenAPI"
    assert row["is_confirmed"] == "True"
    assert row["is_speculative"] == "False"
    assert row["related_to_orders"] == "True"
    assert statuses["TWSE material information OpenAPI"]["matched_tracked_rows"] == 1


def test_material_classifier_keeps_governance_events_out_of_product_certification() -> None:
    governance_title = "\u516c\u544a\u672c\u516c\u53f8115\u5e74\u80a1\u6771\u5e38\u6703\u91cd\u8981\u6c7a\u8b70\u4e8b\u9805"
    governance_summary = "\u901a\u904e\u627f\u8a8d\u6848"
    product_title = "\u7522\u54c1\u901a\u904e\u5ba2\u6236\u8a8d\u8b49"

    assert catalyst.classify_material_event(governance_title, governance_summary) == ("shareholder_meeting", "low")
    assert catalyst.classify_material_event(product_title, "") == ("product_certification", "medium")


def test_event_merge_replaces_reclassified_official_rows() -> None:
    base = {col: "" for col in catalyst.EVENT_CATALYST_COLUMNS}
    base.update(
        {
            "event_date": "20260612",
            "stock_id": "3498",
            "title": "\u516c\u544a\u672c\u516c\u53f8115\u5e74\u80a1\u6771\u5e38\u6703\u91cd\u8981\u6c7a\u8b70\u4e8b\u9805",
            "source": "TPEX material information OpenAPI",
            "event_type": "product_certification",
        }
    )
    corrected = dict(base)
    corrected["event_type"] = "shareholder_meeting"

    merged = catalyst.merge_rows(
        pd.DataFrame([base], columns=catalyst.EVENT_CATALYST_COLUMNS),
        pd.DataFrame([corrected], columns=catalyst.EVENT_CATALYST_COLUMNS),
        catalyst.EVENT_CATALYST_COLUMNS,
        ["event_date", "stock_id", "title", "source"],
    )

    assert len(merged) == 1
    assert merged.iloc[0]["event_type"] == "shareholder_meeting"
