from __future__ import annotations

import csv
import html
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from scripts import market_session_calendar as market_session


TAIPEI_TZ = ZoneInfo("Asia/Taipei")


def _annual_calendar() -> bytes:
    return json.dumps(
        [
            {
                "Name": "中華民國開國紀念日",
                "Date": "1150101",
                "Weekday": "四",
                "Description": "依規定放假1日。",
            },
            {
                "Name": "國曆新年開始交易日",
                "Date": "1150102",
                "Weekday": "五",
                "Description": "國曆新年開始交易。",
            },
        ],
        ensure_ascii=False,
    ).encode("utf-8")


def _feed(*entries: dict[str, str]) -> bytes:
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
    ]
    for entry in entries:
        parts.extend(
            [
                "<entry>",
                f"<id>{html.escape(entry['id'])}</id>",
                "<title>停班停課</title>",
                f"<updated>{html.escape(entry['updated'])}</updated>",
                f"<summary>{html.escape(entry['summary'])}</summary>",
                f"<link rel=\"alternate\" href=\"{html.escape(entry['url'])}\" />",
                "</entry>",
            ]
        )
    parts.append("</feed>")
    return "".join(parts).encode("utf-8")


def _closure_entry(date_text: str, *, scope_text: str = "停止上班、停止上課") -> dict[str, str]:
    month = int(date_text[4:6])
    day = int(date_text[6:8])
    return {
        "id": f"dgpa.gov.tw_workSchlClos_{date_text}_test",
        "updated": f"{date_text[:4]}-{date_text[4:6]}-{date_text[6:8]}T20:00:00+08:00",
        "summary": f"[停班停課通知]臺北市:{month}/{day}{scope_text}。行政院人事行政總處。",
        "url": f"https://alerts.ncdr.nat.gov.tw/test/{date_text}.cap",
    }


def _fetcher(feed_payload: bytes):
    def fetch(url: str, timeout: int) -> bytes:
        assert timeout > 0
        if url == market_session.TWSE_ANNUAL_CALENDAR_URL:
            return _annual_calendar()
        if url == market_session.DGPA_EMERGENCY_FEED_URL:
            return feed_payload
        raise AssertionError(url)

    return fetch


def _prepare_root(root: Path) -> None:
    config = root / "config"
    config.mkdir(parents=True, exist_ok=True)
    (config / "twse_non_trading_days.csv").write_text(
        "date,market,reason,source_url\n"
        "20260101,TWSE_TPEx,Republic Day,https://www.twse.com.tw/\n",
        encoding="utf-8",
    )


def test_taipei_full_day_closure_is_closed_emergency(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="preflight",
        as_of=datetime(2026, 7, 10, 19, 30, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(_feed(_closure_entry("20260710"))),
    )

    assert status["market_status"] == market_session.CLOSED_EMERGENCY
    assert status["market_session_date"] == "20260710"
    assert status["expected_main_price_date"] == "20260709"
    assert status["should_run_daily_pipeline"] is False

    evidence = list(
        csv.DictReader(
            (tmp_path / market_session.EXCEPTIONAL_NON_TRADING_DAYS).open(
                "r",
                encoding="utf-8-sig",
                newline="",
            )
        )
    )
    assert [row["date"] for row in evidence] == ["20260710"]
    assert evidence[0]["source_url"].endswith("/20260710.cap")
    assert evidence[0]["last_observed_at"] == "2026-07-10T19:30:00+08:00"


def test_live_twse_calendar_addition_is_closed_without_static_config_update(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    annual = json.dumps(
        [
            {"Name": "中華民國開國紀念日", "Date": "1150101", "Weekday": "四"},
            {"Name": "臨時年度休市日", "Date": "1150710", "Weekday": "五"},
        ],
        ensure_ascii=False,
    ).encode("utf-8")

    def fetch(url: str, timeout: int) -> bytes:
        if url == market_session.TWSE_ANNUAL_CALENDAR_URL:
            return annual
        if url == market_session.DGPA_EMERGENCY_FEED_URL:
            return _feed()
        raise AssertionError(url)

    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="preflight",
        as_of=datetime(2026, 7, 10, 19, 30, tzinfo=TAIPEI_TZ),
        fetch_bytes=fetch,
    )

    assert status["market_status"] == market_session.CLOSED_SCHEDULED
    assert status["reason_code"] == "twse_annual_holiday"
    assert status["expected_main_price_date"] == "20260709"


def test_weekend_emergency_notice_is_not_recorded_as_exceptional_market_closure(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    feed = _feed(_closure_entry("20260710"), _closure_entry("20260711"))
    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="preflight",
        as_of=datetime(2026, 7, 14, 3, 0, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(feed),
    )

    assert status["market_status"] == market_session.UNKNOWN
    assert status["reason_code"] == "awaiting_official_price_confirmation"
    assert status["market_session_date"] == "20260713"
    assert status["expected_main_price_date"] == "20260713"
    assert status["exceptional_non_trading_days"] == ["20260710"]


def test_confirm_requires_target_date_twse_and_tpex_prices(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    latest = tmp_path / "output" / "latest"
    latest.mkdir(parents=True)
    (latest / "official_price_fetch_latest.json").write_text(
        json.dumps(
            {
                "target_date": "20260713",
                "saved_price_date": "20260713",
                "is_target_date": True,
                "full_market_ok": True,
                "result": "success_target_full_market",
            }
        ),
        encoding="utf-8",
    )
    price_dir = tmp_path / "data" / "daily_price"
    price_dir.mkdir(parents=True)
    (price_dir / "daily_price_20260713.csv").write_text(
        "date,stock_id,market,close\n"
        "20260713,2330,TWSE,1000\n"
        "20260713,6488,TPEx,500\n",
        encoding="utf-8",
    )

    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="confirm",
        as_of=datetime(2026, 7, 14, 3, 0, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(_feed(_closure_entry("20260710"))),
    )

    assert status["market_status"] == market_session.OPEN_CONFIRMED
    assert status["expected_main_price_date"] == "20260713"
    assert status["price_confirmation"]["twse_rows"] == 1
    assert status["price_confirmation"]["tpex_rows"] == 1


def test_confirm_reuses_recent_successful_preflight_without_refetching_sources(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    feed = _feed(_closure_entry("20260710"))
    market_session.refresh_market_session_status(
        tmp_path,
        phase="preflight",
        as_of=datetime(2026, 7, 14, 3, 0, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(feed),
    )
    latest = tmp_path / "output" / "latest"
    (latest / "official_price_fetch_latest.json").write_text(
        json.dumps(
            {
                "target_date": "20260713",
                "saved_price_date": "20260713",
                "is_target_date": True,
                "full_market_ok": True,
            }
        ),
        encoding="utf-8",
    )
    price_dir = tmp_path / "data" / "daily_price"
    price_dir.mkdir(parents=True, exist_ok=True)
    (price_dir / "daily_price_20260713.csv").write_text(
        "date,stock_id,market\n20260713,2330,TWSE\n20260713,6488,TPEx\n",
        encoding="utf-8",
    )

    def must_not_fetch(url: str, timeout: int) -> bytes:
        raise AssertionError(f"unexpected refetch: {url}")

    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="confirm",
        as_of=datetime(2026, 7, 14, 3, 5, tzinfo=TAIPEI_TZ),
        fetch_bytes=must_not_fetch,
    )

    assert status["market_status"] == market_session.OPEN_CONFIRMED
    assert status["preflight_reused"] is True
    assert status["preflight_generated_at"] == "2026-07-14T03:00:00+08:00"


def test_confirm_rejects_previous_day_fallback(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    latest = tmp_path / "output" / "latest"
    latest.mkdir(parents=True)
    (latest / "official_price_fetch_latest.json").write_text(
        json.dumps(
            {
                "target_date": "20260713",
                "saved_price_date": "20260709",
                "is_target_date": False,
                "full_market_ok": False,
            }
        ),
        encoding="utf-8",
    )

    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="confirm",
        as_of=datetime(2026, 7, 14, 3, 0, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(_feed(_closure_entry("20260710"))),
    )

    assert status["market_status"] == market_session.UNKNOWN
    assert status["reason_code"] == "official_price_not_confirmed"
    assert "saved_price_date=20260709" in status["reason"]


def test_official_source_failure_is_unknown(tmp_path: Path) -> None:
    _prepare_root(tmp_path)

    def failing_fetch(url: str, timeout: int) -> bytes:
        if url == market_session.TWSE_ANNUAL_CALENDAR_URL:
            return _annual_calendar()
        raise OSError("NCDR unavailable")

    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="preflight",
        as_of=datetime(2026, 7, 10, 19, 30, tzinfo=TAIPEI_TZ),
        fetch_bytes=failing_fetch,
    )

    assert status["market_status"] == market_session.UNKNOWN
    assert status["reason_code"] == "official_source_unavailable"
    assert status["should_run_daily_pipeline"] is False


def test_afternoon_work_suspension_does_not_close_day_market(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    status = market_session.refresh_market_session_status(
        tmp_path,
        phase="preflight",
        as_of=datetime(2026, 7, 10, 19, 30, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(
            _feed(_closure_entry("20260710", scope_text="下午停止上班、停止上課"))
        ),
    )

    assert status["market_status"] == market_session.UNKNOWN
    assert status["reason_code"] == "awaiting_official_price_confirmation"
    assert status["expected_main_price_date"] == "20260710"
