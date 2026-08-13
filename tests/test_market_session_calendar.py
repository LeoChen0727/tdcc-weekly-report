from __future__ import annotations

import csv
import html
import json
import pytest
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


def _bind_official_price_evidence(root: Path, date_text: str = "20260713") -> bytes:
    from fetch_official_daily_price import publish_official_price_evidence_transaction

    payload = (
        "date,stock_id,market,open,high,low,close,volume\n"
        f"{date_text},2330,TWSE,990,1010,980,1000,1000\n"
        f"{date_text},6488,TPEx,490,510,480,500,1000\n"
    ).encode("utf-8")
    price_dir = root / "data" / "daily_price"
    price_dir.mkdir(parents=True, exist_ok=True)
    (price_dir / f"daily_price_{date_text}.csv").write_bytes(payload)
    publish_official_price_evidence_transaction(
        root,
        price_payload=payload,
        result={
            "target_date": date_text,
            "saved_price_date": date_text,
            "is_target_date": True,
            "full_market_ok": True,
            "result": "success_target_full_market",
            "twse_rows": 1,
            "tpex_rows": 1,
            "total_rows": 2,
        },
        log=["test evidence"],
    )
    return payload


def test_confirm_requires_target_date_twse_and_tpex_prices(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    _bind_official_price_evidence(tmp_path)

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
    _bind_official_price_evidence(tmp_path)

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


@pytest.mark.parametrize("mutation", ["wrong_date", "row_count", "price_hash", "markdown"])
def test_confirm_rejects_date_bound_official_price_evidence_drift(
    tmp_path: Path, mutation: str
) -> None:
    _prepare_root(tmp_path)
    _bind_official_price_evidence(tmp_path)
    latest = tmp_path / "output" / "latest"
    status_path = latest / "official_price_fetch_latest.json"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    if mutation == "wrong_date":
        status["saved_price_date"] = "20260710"
        status_path.write_text(json.dumps(status), encoding="utf-8")
    elif mutation == "row_count":
        status["twse_rows"] = 2
        status_path.write_text(json.dumps(status), encoding="utf-8")
    elif mutation == "price_hash":
        (latest / "official_daily_price_latest.csv").write_bytes(b"tampered\n")
    else:
        (latest / "official_price_fetch_latest.md").write_text(
            "tampered\n", encoding="utf-8"
        )

    observed = market_session.refresh_market_session_status(
        tmp_path,
        phase="confirm",
        as_of=datetime(2026, 7, 14, 3, 0, tzinfo=TAIPEI_TZ),
        fetch_bytes=_fetcher(_feed(_closure_entry("20260710"))),
    )
    assert observed["market_status"] == market_session.UNKNOWN
    assert observed["reason_code"] == "official_price_not_confirmed"


def test_current_day_repair_publishes_real_confirmation_and_verifiable_bundle(
    tmp_path: Path,
) -> None:
    import subprocess
    from scripts import daily_source_recovery_bundle as source_bundle
    from scripts import repair_recent_daily_price_gaps as recent_repair

    _prepare_root(tmp_path)
    subprocess.run(["git", "init", "-q", "--initial-branch=main"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "repair@example.invalid"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Repair Test"], cwd=tmp_path, check=True)

    def repair(root: Path, date_text: str, _args: object) -> int:
        lines = [
            "date,stock_id,market,open,high,low,close,volume,source"
        ]
        for index in range(1300):
            market = "TWSE" if index < 800 else "TPEx"
            lines.append(
                f"{date_text},{1000 + index},{market},9,11,8,10,1000,"
                f"{market}_TEST_SOURCE"
            )
        payload = ("\n".join(lines) + "\n").encode("utf-8")
        saved = [
            f"data/daily_price/{date_text}.csv",
            f"data/daily_price/daily_price_{date_text}.csv",
        ]
        for relative in saved:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
        report = root / "output/latest/repair_daily_price_range_latest.json"
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(
            json.dumps(
                {
                    "rows": [
                        {
                            "date": date_text,
                            "status": "repaired",
                            "saved_files": ";".join(saved),
                            "twse_rows": 800,
                            "tpex_rows": 500,
                            "total_rows": 1300,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        return 0

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date="20260713",
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        repair_func=repair,
        market_session_fetch_bytes=_fetcher(_feed(_closure_entry("20260710"))),
        authority_date="20260713",
    )
    confirmation = result.report["current_day_confirmation"]
    assert confirmation["market_session"]["market_status"] == market_session.OPEN_CONFIRMED
    assert confirmation["market_session"]["phase"] == "confirm"
    assert confirmation["market_session"]["market_session_date"] == "20260713"
    calendar_path = tmp_path / "data/market_calendar/exceptional_non_trading_days.csv"
    calendar_path.parent.mkdir(parents=True, exist_ok=True)
    calendar_path.write_bytes(b"date,reason\n")

    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "date-bound source"], cwd=tmp_path, check=True)
    source_sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True
    ).strip()
    built = source_bundle.build_bundle(
        tmp_path,
        trading_date="20260713",
        release_id="src-chain1",
        source_base_sha=source_sha,
        run_id="31596733427",
        run_attempt=1,
        market_session=confirmation["market_session"],
    )
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "immutable source bundle"], cwd=tmp_path, check=True)
    bundle_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True
    ).strip()
    verified = source_bundle.verify_bundle_from_git(
        tmp_path,
        source_commit_sha=bundle_commit,
        manifest_path=built["manifest_path"],
        manifest_sha256=built["manifest_sha256"],
        source_bundle_sha=built["manifest"]["source_bundle_sha"],
        trading_date="20260713",
    )
    assert verified["official_price_confirmation"]["total_rows"] == 1300

    reservation = source_bundle.create_dispatch_reservation(
        tmp_path,
        trading_date="20260713",
        source_commit_sha=bundle_commit,
        manifest_path=built["manifest_path"],
        manifest_sha256=built["manifest_sha256"],
        source_bundle_sha=built["manifest"]["source_bundle_sha"],
        baseline_run_id=100,
        dispatch_started_at="2026-07-13T12:30:00Z",
        expected_display_title="Daily Full Pipeline | recovery=daily-source-20260713",
    )
    subprocess.run(["git", "add", reservation["path"]], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "reserve resume"], cwd=tmp_path, check=True)
    reservation_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True
    ).strip()
    verified_reservation = source_bundle.verify_dispatch_reservation(
        tmp_path,
        trading_date="20260713",
        reservation_path=reservation["path"],
        reservation_sha256=reservation["sha256"],
        expected_head_sha=reservation_commit,
        source_commit_sha=bundle_commit,
        manifest_path=built["manifest_path"],
        manifest_sha256=built["manifest_sha256"],
        source_bundle_sha=built["manifest"]["source_bundle_sha"],
        correlation_id="daily-source-20260713",
    )
    assert verified_reservation["source_bundle_commit_sha"] == bundle_commit


def test_historical_repair_does_not_mutate_current_official_price_surfaces(
    tmp_path: Path,
) -> None:
    from scripts import repair_recent_daily_price_gaps as recent_repair

    _prepare_root(tmp_path)
    _bind_official_price_evidence(tmp_path, "20260710")
    latest = tmp_path / "output/latest"
    surfaces = [
        latest / "official_daily_price_latest.csv",
        latest / "official_price_fetch_latest.json",
        latest / "official_price_fetch_latest.md",
    ]
    before = {path: path.read_bytes() for path in surfaces}

    def repair(root: Path, date_text: str, _args: object) -> int:
        payload = (
            "date,stock_id,market\n"
            f"{date_text},2330,TWSE\n"
            f"{date_text},6488,TPEx\n"
        ).encode("utf-8")
        for relative in (
            f"data/daily_price/{date_text}.csv",
            f"data/daily_price/daily_price_{date_text}.csv",
        ):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
        return 0

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date="20260714",
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        include_as_of_date=False,
        repair_func=repair,
    )
    assert result.status == "repaired"
    assert {path: path.read_bytes() for path in surfaces} == before


def test_confirm_rejects_previous_day_fallback(tmp_path: Path) -> None:
    _prepare_root(tmp_path)
    _bind_official_price_evidence(tmp_path)
    latest = tmp_path / "output" / "latest"
    status_path = latest / "official_price_fetch_latest.json"
    payload = json.loads(status_path.read_text(encoding="utf-8"))
    payload["saved_price_date"] = "20260709"
    payload["is_target_date"] = False
    payload["full_market_ok"] = False
    status_path.write_text(json.dumps(payload), encoding="utf-8")

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


@pytest.mark.parametrize("existing_mode", ["legacy_only", "canonical"])
def test_current_day_existing_price_bytes_repair_stale_confirmation(
    tmp_path: Path,
    existing_mode: str,
) -> None:
    from scripts import repair_recent_daily_price_gaps as recent_repair

    _prepare_root(tmp_path)
    date_text = "20260713"
    lines = [
        "date,stock_id,market,open,high,low,close,volume,source"
    ]
    for index in range(1300):
        market = "TWSE" if index < 800 else "TPEx"
        lines.append(
            f"{date_text},{1000 + index},{market},9,11,8,10,1000,"
            f"{market}_TEST_SOURCE"
        )
    payload = ("\n".join(lines) + "\n").encode("utf-8")
    legacy = tmp_path / f"data/daily_price/{date_text}.csv"
    legacy.parent.mkdir(parents=True, exist_ok=True)
    legacy.write_bytes(payload)
    if existing_mode == "canonical":
        (legacy.parent / f"daily_price_{date_text}.csv").write_bytes(payload)
    output = tmp_path / "output/latest"
    output.mkdir(parents=True, exist_ok=True)
    (output / "official_price_fetch_latest.json").write_text(
        json.dumps(
            {"target_date": "20260710", "saved_price_date": "20260710"}
        ),
        encoding="utf-8",
    )
    (output / "official_price_fetch_latest.md").write_text(
        "# stale\n", encoding="utf-8"
    )

    def unexpected_repair(_root: Path, _date: str, _args: object) -> int:
        raise AssertionError("existing current-day bytes must not be refetched")

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date=date_text,
        authority_date=date_text,
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        repair_func=unexpected_repair,
        market_session_fetch_bytes=_fetcher(
            _feed(_closure_entry("20260710"))
        ),
    )
    assert result.status in {"pass", "repaired"}
    confirmation = result.report["current_day_confirmation"]
    assert confirmation["official_price_fetch"]["saved_price_date"] == date_text
    assert confirmation["official_price_fetch"]["total_rows"] == 1300
    assert (
        confirmation["market_session"]["market_status"]
        == market_session.OPEN_CONFIRMED
    )
    surfaces = [
        output / "official_daily_price_latest.csv",
        output / "official_price_fetch_latest.json",
        output / "official_price_fetch_latest.md",
    ]
    before_reinvoke = {path: path.read_bytes() for path in surfaces}
    reinvoked = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date=date_text,
        authority_date=date_text,
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        repair_func=unexpected_repair,
        market_session_fetch_bytes=_fetcher(
            _feed(_closure_entry("20260710"))
        ),
    )
    assert reinvoked.status == "pass"
    assert {path: path.read_bytes() for path in surfaces} == before_reinvoke


@pytest.mark.parametrize(
    "quality_failure",
    [
        "market_threshold",
        "stale_duplicate",
        "duplicate_stock_id",
        "non_numeric",
        "invalid_ohlc",
    ],
)
def test_current_day_existing_price_requires_official_full_market_quality(
    tmp_path: Path,
    quality_failure: str,
) -> None:
    from scripts import repair_recent_daily_price_gaps as recent_repair

    _prepare_root(tmp_path)
    date_text = "20260713"

    def payload(payload_date: str, twse_rows: int, tpex_rows: int) -> bytes:
        lines = [
            "date,stock_id,market,open,high,low,close,volume,source"
        ]
        for index in range(twse_rows + tpex_rows):
            market = "TWSE" if index < twse_rows else "TPEx"
            lines.append(
                f"{payload_date},{1000 + index},{market},9,11,8,10,1000,"
                f"{market}_TEST_SOURCE"
            )
        return ("\n".join(lines) + "\n").encode("utf-8")

    current_payload = payload(
        date_text,
        699 if quality_failure == "market_threshold" else 800,
        601 if quality_failure == "market_threshold" else 500,
    )
    current_lines = current_payload.decode("utf-8").splitlines()
    if quality_failure == "duplicate_stock_id":
        fields = current_lines[-1].split(",")
        fields[1] = "1000"
        current_lines[-1] = ",".join(fields)
        current_payload = ("\n".join(current_lines) + "\n").encode("utf-8")
    elif quality_failure == "non_numeric":
        fields = current_lines[1].split(",")
        fields[3] = "not-a-number"
        current_lines[1] = ",".join(fields)
        current_payload = ("\n".join(current_lines) + "\n").encode("utf-8")
    elif quality_failure == "invalid_ohlc":
        fields = current_lines[1].split(",")
        fields[4] = "7"
        current_lines[1] = ",".join(fields)
        current_payload = ("\n".join(current_lines) + "\n").encode("utf-8")
    price_dir = tmp_path / "data/daily_price"
    price_dir.mkdir(parents=True, exist_ok=True)
    for name in (date_text, f"daily_price_{date_text}"):
        (price_dir / f"{name}.csv").write_bytes(current_payload)
    if quality_failure == "stale_duplicate":
        previous_payload = payload("20260710", 800, 500)
        (price_dir / "daily_price_20260710.csv").write_bytes(previous_payload)

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date=date_text,
        authority_date=date_text,
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        repair_func=lambda *_args: (_ for _ in ()).throw(
            AssertionError("existing bytes must not be refetched")
        ),
        market_session_fetch_bytes=_fetcher(
            _feed(_closure_entry("20260710"))
        ),
    )
    assert result.status == "fail"
    assert result.report["current_day_confirmation"] == {}
    assert len(result.errors) == 1
    assert result.errors[0].startswith(
        "current-day official price confirmation failed:"
    )
    if quality_failure in {"market_threshold", "stale_duplicate"}:
        assert "full-market" in result.errors[0]
    else:
        assert "clean unique target-date TWSE/TPEx OHLCV rows" in result.errors[0]


def test_historical_repair_does_not_publish_current_latest_evidence(
    tmp_path: Path,
) -> None:
    from scripts import repair_recent_daily_price_gaps as recent_repair

    _prepare_root(tmp_path)
    output = tmp_path / "output/latest"
    output.mkdir(parents=True, exist_ok=True)
    protected = {
        output / "official_daily_price_latest.csv": b"current-price\n",
        output / "official_price_fetch_latest.json": b'{"current":true}\n',
        output / "official_price_fetch_latest.md": b"# current\n",
    }
    for path, payload in protected.items():
        path.write_bytes(payload)
    date_text = "20260713"

    def repair(root: Path, requested_date: str, _args: object) -> int:
        lines = ["date,stock_id,market,close,source"]
        for index in range(1300):
            market = "TWSE" if index < 800 else "TPEx"
            lines.append(
                f"{requested_date},{1000 + index},{market},10,"
                f"{market}_TEST_SOURCE"
            )
        payload = ("\n".join(lines) + "\n").encode("utf-8")
        saved = [
            f"data/daily_price/{requested_date}.csv",
            f"data/daily_price/daily_price_{requested_date}.csv",
        ]
        for relative in saved:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
        report = root / "output/latest/repair_daily_price_range_latest.json"
        report.write_text(
            json.dumps(
                {
                    "rows": [
                        {
                            "date": requested_date,
                            "status": "repaired",
                            "saved_files": ";".join(saved),
                            "twse_rows": 800,
                            "tpex_rows": 500,
                            "total_rows": 1300,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        return 0

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date=date_text,
        authority_date="20260813",
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        repair_func=repair,
    )
    assert result.report["current_day_confirmation"] == {}
    assert {path: path.read_bytes() for path in protected} == protected


def _full_market_repair_payload(date_text: str) -> bytes:
    lines = ["date,stock_id,market,open,high,low,close,volume,source"]
    for index in range(1300):
        market = "TWSE" if index < 800 else "TPEx"
        lines.append(
            f"{date_text},{1000 + index},{market},9,11,8,10,1000,"
            f"{market}_TEST_SOURCE"
        )
    return ("\n".join(lines) + "\n").encode("utf-8")


def _seed_zero_repair_current_day(root: Path, date_text: str) -> dict[Path, bytes]:
    _prepare_root(root)
    _bind_official_price_evidence(root, "20260710")
    payload = _full_market_repair_payload(date_text)
    price_dir = root / "data/daily_price"
    for name in (date_text, f"daily_price_{date_text}"):
        (price_dir / f"{name}.csv").write_bytes(payload)
    latest = root / "output/latest"
    authority = {
        latest / "market_session_status_latest.json": json.dumps(
            {
                "market_status": "open_confirmed",
                "phase": "confirm",
                "market_session_date": date_text,
                "expected_main_price_date": date_text,
                "should_run_daily_pipeline": True,
            },
            sort_keys=True,
        ).encode("utf-8"),
        latest / "data_freshness_latest.csv": (
            "market_session_status,market_session_date,expected_main_price_date,"
            "main_price_date,report_ready,daily_pdf_ready\n"
            f"open_confirmed,{date_text},{date_text},{date_text},True,True\n"
        ).encode("utf-8"),
        latest / "data_freshness_latest.md": b"# immutable authority\n",
    }
    for path, content in authority.items():
        path.write_bytes(content)
    return authority


def test_zero_raw_repair_rebuilds_missing_target_history_before_deferred_commit(
    tmp_path: Path,
) -> None:
    from scripts import repair_recent_daily_price_gaps as recent_repair

    date_text = "20260713"
    authority = _seed_zero_repair_current_day(tmp_path, date_text)
    calls: list[str] = []

    def validate(root: Path, **kwargs: object):
        assert kwargs["main_price_date_override"] == date_text
        calls.append("continuity")
        if calls.count("continuity") == 1:
            return recent_repair.continuity.ValidationResult(
                "fail", {}, ["target history missing"]
            )
        return recent_repair.continuity.ValidationResult("pass", {}, [])

    def build(root: Path, _args: object) -> int:
        calls.append("history")
        assert (root / recent_repair.official_price_fetch.OFFICIAL_PRICE_TRANSACTION_DIR).is_dir()
        assert json.loads(
            (root / "output/latest/official_price_fetch_latest.json").read_text(
                encoding="utf-8"
            )
        )["saved_price_date"] == date_text
        return 0

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date=date_text,
        authority_date=date_text,
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        rebuild_history_if_repaired=True,
        repair_func=lambda *_args: (_ for _ in ()).throw(
            AssertionError("zero raw repair must not refetch existing current-day prices")
        ),
        build_history_func=build,
        continuity_validate_func=validate,
        market_session_fetch_bytes=_fetcher(_feed(_closure_entry("20260710"))),
    )
    assert result.status == "pass"
    assert result.report["actions"] == []
    assert result.report["rebuild_history_status"] == "completed"
    assert calls == ["continuity", "history", "continuity"]
    assert result.report["current_day_confirmation"]["market_session"]["market_status"] == "open_confirmed"
    assert {
        path: path.read_bytes() for path in authority
    } == authority
    assert not (
        tmp_path / recent_repair.official_price_fetch.OFFICIAL_PRICE_TRANSACTION_DIR
    ).exists()


@pytest.mark.parametrize(
    "failure_kind",
    [
        "confirm_source_exception",
        "history_nonzero",
        "history_exception",
        "continuity_nonzero",
        "continuity_exception",
    ],
)
def test_current_day_deferred_confirmation_failures_restore_previous_latest(
    tmp_path: Path,
    failure_kind: str,
) -> None:
    from scripts import repair_recent_daily_price_gaps as recent_repair

    date_text = "20260713"
    _prepare_root(tmp_path)
    _bind_official_price_evidence(tmp_path, "20260710")
    payload = _full_market_repair_payload(date_text)
    price_dir = tmp_path / "data/daily_price"
    for name in (date_text, f"daily_price_{date_text}"):
        (price_dir / f"{name}.csv").write_bytes(payload)
    triplet = [
        tmp_path / recent_repair.official_price_fetch.LATEST_PRICE_CSV,
        tmp_path / recent_repair.official_price_fetch.LATEST_FETCH_JSON,
        tmp_path / recent_repair.official_price_fetch.LATEST_FETCH_MD,
    ]
    before = {path: path.read_bytes() for path in triplet}

    def validate(_root: Path, **_kwargs: object):
        if failure_kind == "continuity_exception":
            raise RuntimeError("injected continuity exception")
        if failure_kind in {"continuity_nonzero", "history_nonzero", "history_exception"}:
            return recent_repair.continuity.ValidationResult(
                "fail", {}, ["injected continuity failure"]
            )
        return recent_repair.continuity.ValidationResult("pass", {}, [])

    def build(_root: Path, _args: object) -> int:
        if failure_kind == "history_exception":
            raise RuntimeError("injected history exception")
        return 7 if failure_kind == "history_nonzero" else 0

    if failure_kind == "confirm_source_exception":
        def fetch_bytes(_url: str, _timeout: int) -> bytes:
            raise RuntimeError("injected official source exception")
    else:
        fetch_bytes = _fetcher(_feed(_closure_entry("20260710")))

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date=date_text,
        authority_date=date_text,
        lookback_days=1,
        min_full_rows=1,
        max_repair_dates=1,
        rebuild_history_if_repaired=failure_kind.startswith("history_"),
        repair_func=lambda *_args: (_ for _ in ()).throw(
            AssertionError("existing current-day bytes must not be refetched")
        ),
        build_history_func=build,
        continuity_validate_func=validate,
        market_session_fetch_bytes=fetch_bytes,
    )
    assert result.status == "fail"
    assert result.report["current_day_confirmation"] == {}
    assert {path: path.read_bytes() for path in triplet} == before
    assert not (
        tmp_path / recent_repair.official_price_fetch.OFFICIAL_PRICE_TRANSACTION_DIR
    ).exists()


def _seed_pending_exact_triplet_transaction(tmp_path: Path):
    import fetch_official_daily_price as official_price

    old_payloads = {
        official_price.LATEST_PRICE_CSV: b"old-price\n",
        official_price.LATEST_FETCH_JSON: b'{"old":true}\n',
        official_price.LATEST_FETCH_MD: b"# old\n",
    }
    next_payloads = {
        official_price.LATEST_PRICE_CSV: b"new-price\n",
        official_price.LATEST_FETCH_JSON: b'{"new":true}\n',
        official_price.LATEST_FETCH_MD: b"# new\n",
    }
    for relative, payload in old_payloads.items():
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
    official_price._begin_official_price_evidence_transaction(
        tmp_path,
        next_payloads,
        require_exact_triplet=True,
    )
    transaction_root = tmp_path / official_price.OFFICIAL_PRICE_TRANSACTION_DIR
    targets = [tmp_path / path for path in sorted(next_payloads)]
    return official_price, transaction_root, targets, old_payloads


def test_deferred_transaction_journal_binds_exact_triplet_and_recovers_all(
    tmp_path: Path,
) -> None:
    official_price, transaction_root, targets, old_payloads = (
        _seed_pending_exact_triplet_transaction(tmp_path)
    )
    journal = json.loads(
        (transaction_root / "journal.json").read_text(encoding="utf-8")
    )
    assert journal["schema_version"] == "official_price_evidence_transaction_v3"
    assert journal["transaction_kind"] == "deferred_official_latest_triplet"
    assert set(journal["required_paths"]) == {
        path.as_posix()
        for path in (
            official_price.LATEST_PRICE_CSV,
            official_price.LATEST_FETCH_JSON,
            official_price.LATEST_FETCH_MD,
        )
    }
    assert official_price.recover_official_price_evidence_transaction(tmp_path)
    assert {
        relative: (tmp_path / relative).read_bytes() for relative in old_payloads
    } == old_payloads
    assert not transaction_root.exists()


@pytest.mark.parametrize(
    "mutation",
    [
        "missing_journal",
        "truncated_entries",
        "extra_entry",
        "malformed_json",
        "journal_hash",
        "required_path",
        "backup_hash",
    ],
)
def test_invalid_deferred_transaction_journal_fails_before_target_write(
    tmp_path: Path,
    mutation: str,
) -> None:
    official_price, transaction_root, targets, _old_payloads = (
        _seed_pending_exact_triplet_transaction(tmp_path)
    )
    journal_path = transaction_root / "journal.json"
    journal = json.loads(journal_path.read_text(encoding="utf-8"))
    if mutation == "missing_journal":
        journal_path.unlink()
    elif mutation == "truncated_entries":
        journal["entries"].pop()
        official_price._write_official_price_transaction_journal(
            transaction_root, journal
        )
    elif mutation == "extra_entry":
        extra = dict(journal["entries"][0])
        extra["path"] = "output/latest/unapproved.json"
        extra["previous_file"] = "previous-3.bin"
        extra["next_file"] = "next-3.bin"
        journal["entries"].append(extra)
        official_price._write_official_price_transaction_journal(
            transaction_root, journal
        )
    elif mutation == "malformed_json":
        journal_path.write_bytes(b"{not-json")
    elif mutation == "journal_hash":
        journal["journal_sha256"] = "0" * 64
        journal_path.write_text(
            json.dumps(journal, sort_keys=True), encoding="utf-8"
        )
    elif mutation == "required_path":
        journal["required_paths"][0] = "output/latest/unapproved.json"
        official_price._write_official_price_transaction_journal(
            transaction_root, journal
        )
    else:
        (transaction_root / journal["entries"][0]["previous_file"]).write_bytes(
            b"tampered-backup"
        )
    before = {path: path.read_bytes() for path in targets}
    with pytest.raises(ValueError):
        official_price.recover_official_price_evidence_transaction(tmp_path)
    assert {path: path.read_bytes() for path in targets} == before
    assert transaction_root.exists()
