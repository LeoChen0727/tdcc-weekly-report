from __future__ import annotations

from datetime import date, datetime, timedelta
from io import StringIO
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import json
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

from tracking_utils import LATEST_DIR, now_text, normalize_code, normalize_date, read_csv, safe_str, write_csv


DATA_DIR = Path("data")
COMPANY_CALENDAR_DIR = DATA_DIR / "company_calendar"
MACRO_EVENTS_DIR = DATA_DIR / "macro_events"
THEME_EVENTS_DIR = DATA_DIR / "theme_events"

COMPANY_EVENT_CALENDAR = COMPANY_CALENDAR_DIR / "company_event_calendar.csv"
MACRO_EVENT_CALENDAR = MACRO_EVENTS_DIR / "macro_event_calendar.csv"
THEME_EVENT_CALENDAR = THEME_EVENTS_DIR / "theme_event_calendar.csv"
EVENT_CATALYST_LOG = DATA_DIR / "event_catalysts" / "event_catalyst_log.csv"

UPCOMING_COMPANY_CALENDAR = LATEST_DIR / "upcoming_catalyst_calendar_latest.csv"
UPCOMING_COMPANY_MD = LATEST_DIR / "upcoming_catalyst_calendar_latest.md"
UPCOMING_MACRO_CALENDAR = LATEST_DIR / "upcoming_macro_event_calendar_latest.csv"
UPCOMING_MACRO_MD = LATEST_DIR / "upcoming_macro_event_calendar_latest.md"
STATUS_JSON = LATEST_DIR / "calendar_data_source_status_latest.json"
STATUS_MD = LATEST_DIR / "calendar_data_source_status_latest.md"
NEEDS_REVIEW_CSV = LATEST_DIR / "catalyst_needs_review_latest.csv"
NEEDS_REVIEW_MD = LATEST_DIR / "catalyst_needs_review_latest.md"

ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
COMPANY_THEME_MAPPING = THEME_EVENTS_DIR / "company_theme_mapping.csv"

TWSE_EX_RIGHT_URL = "https://www.twse.com.tw/rwd/zh/exRight/TWT48U?response=json"
TWSE_EX_RIGHT_SOURCE = "TWSE ex-right/ex-dividend calendar"
TWSE_EX_RIGHT_STALE_MAX_TRADING_DAYS = 3
TWSE_EX_RIGHT_MAX_CONSECUTIVE_FAILURES = 2
TWSE_EX_RIGHT_CACHE_LOOKBACK_DAYS = 7
TWSE_EX_RIGHT_CACHE_LOOKAHEAD_DAYS = 60
TWSE_EX_RIGHT_LIVE_FAILURE_STATUSES = {"stale_ok", "degraded_blocked_effect", "failed", "degraded_ok"}
TWSE_DIVIDEND_DISTRIBUTION_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap45_L"
FED_FOMC_URL = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
BEA_SCHEDULE_URL = "https://www.bea.gov/news/schedule"
BLS_CPI_URL = "https://www.bls.gov/schedule/news_release/cpi.htm"
BLS_EMPSIT_URL = "https://www.bls.gov/schedule/news_release/empsit.htm"
MOPS_SHAREHOLDER_MEETING_URL = "https://mops.twse.com.tw/mops/web/t108sb31new"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; tdcc-weekly-report calendar fetcher)",
    "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
}

COMPANY_COLUMNS = [
    "event_date",
    "event_end_date",
    "stock_id",
    "stock_name",
    "market",
    "event_type",
    "event_name",
    "event_status",
    "event_confidence",
    "catalyst_tags",
    "source",
    "source_url",
    "days_to_event",
    "proximity_bucket",
    "expected_impact",
    "notes",
    "last_updated",
]

MACRO_COLUMNS = [
    "event_date",
    "event_end_date",
    "event_name",
    "event_type",
    "region",
    "importance",
    "source",
    "source_url",
    "days_to_event",
    "proximity_bucket",
    "related_themes",
    "market_report_section",
    "notes",
    "last_updated",
]

THEME_EVENT_COLUMNS = [
    "event_date",
    "event_end_date",
    "event_name",
    "event_type",
    "theme_tags",
    "related_industries",
    "related_stock_ids",
    "importance",
    "source_url",
    "last_updated",
]

NEEDS_REVIEW_COLUMNS = [
    "item_id",
    "detected_at",
    "source_area",
    "requested_data",
    "current_status",
    "owner",
    "required_evidence",
    "model_effect_allowed",
    "pdf_effect_allowed",
    "next_action",
    "source_url",
    "last_checked_at",
    "notes",
]

MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

MONTH_ALIASES = {
    **MONTHS,
    "Jan.": 1,
    "Feb.": 2,
    "Mar.": 3,
    "Apr.": 4,
    "Jun.": 6,
    "Jul.": 7,
    "Aug.": 8,
    "Sep.": 9,
    "Sept.": 9,
    "Oct.": 10,
    "Nov.": 11,
    "Dec.": 12,
}


def today_taipei() -> date:
    return datetime.now(ZoneInfo("Asia/Taipei")).date()


def ymd(day: date | datetime | str | Any) -> str:
    if isinstance(day, datetime):
        return day.strftime("%Y%m%d")
    if isinstance(day, date):
        return day.strftime("%Y%m%d")
    return normalize_date(day)


def parse_roc_date(value: Any) -> str:
    text = safe_str(value)
    nums = re.findall(r"\d+", text)
    if len(nums) == 1 and len(nums[0]) in {6, 7}:
        raw = nums[0].zfill(7)
        year = int(raw[:-4])
        month = int(raw[-4:-2])
        day = int(raw[-2:])
        if year < 1911:
            year += 1911
        try:
            return date(year, month, day).strftime("%Y%m%d")
        except ValueError:
            return ""
    if len(nums) >= 3:
        year = int(nums[0])
        if year < 1911:
            year += 1911
        month = int(nums[1])
        day = int(nums[2])
        try:
            return date(year, month, day).strftime("%Y%m%d")
        except ValueError:
            return ""
    return normalize_date(text)


def parse_english_release_date(value: Any) -> str:
    text = safe_str(value).replace(",", "")
    match = re.search(
        r"\b(?P<month>Jan\.|Feb\.|Mar\.|Apr\.|May|Jun\.|Jul\.|Aug\.|Sep\.|Sept\.|Oct\.|Nov\.|Dec\.|"
        r"January|February|March|April|June|July|August|September|October|November|December)\s+"
        r"(?P<day>\d{1,2})\s+(?P<year>20\d{2})",
        text,
    )
    if not match:
        return ""
    month = MONTH_ALIASES.get(match.group("month"))
    if not month:
        return ""
    try:
        return date(int(match.group("year")), month, int(match.group("day"))).strftime("%Y%m%d")
    except ValueError:
        return ""


def parse_ymd(value: Any) -> date | None:
    text = ymd(value)
    if not text:
        return None
    try:
        return datetime.strptime(text, "%Y%m%d").date()
    except ValueError:
        return None


def parse_date_from_text(value: Any) -> date | None:
    text = safe_str(value)
    match = re.search(r"\b(20\d{2})-(\d{2})-(\d{2})\b", text)
    if not match:
        return parse_ymd(text)
    try:
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError:
        return None


def add_semicolon_tag(value: Any, tag: str) -> str:
    tags = [safe_str(item) for item in safe_str(value).replace(",", ";").split(";") if safe_str(item)]
    if tag not in tags:
        tags.append(tag)
    return ";".join(tags)


def trading_days_between(start: date, end: date) -> int:
    if start >= end:
        return 0
    days = 0
    current = start
    while current < end:
        current += timedelta(days=1)
        if current.weekday() < 5:
            days += 1
    return days


def previous_twse_ex_right_status() -> dict[str, Any]:
    if not STATUS_JSON.exists():
        return {}
    try:
        data = json.loads(STATUS_JSON.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}
    source = data.get("sources", {}).get("twse_ex_right_ex_dividend", {})
    return source if isinstance(source, dict) else {}


def twse_live_failure_metadata() -> dict[str, Any]:
    previous = previous_twse_ex_right_status()
    previous_status = safe_str(previous.get("status"))
    previous_count = 0
    if previous_status in TWSE_EX_RIGHT_LIVE_FAILURE_STATUSES:
        try:
            previous_count = int(previous.get("consecutive_live_failures", 0))
        except Exception:
            previous_count = 0
    first_failure = (
        safe_str(previous.get("first_live_failure_at"))
        if previous_count > 0 and previous_status in TWSE_EX_RIGHT_LIVE_FAILURE_STATUSES
        else now_text()
    )
    return {
        "consecutive_live_failures": previous_count + 1,
        "max_consecutive_live_failures": TWSE_EX_RIGHT_MAX_CONSECUTIVE_FAILURES,
        "first_live_failure_at": first_failure,
    }


def days_to(value: Any, base: date | None = None) -> str:
    day = parse_ymd(value)
    if day is None:
        return ""
    base = base or today_taipei()
    return str((day - base).days)


def proximity_bucket(value: Any, base: date | None = None) -> str:
    text = days_to(value, base)
    if text == "":
        return "unknown"
    delta = int(text)
    if delta < -7:
        return "past"
    if delta < 0:
        return "recent"
    if delta <= 3:
        return "within_3d"
    if delta <= 7:
        return "within_7d"
    if delta <= 14:
        return "within_14d"
    if delta <= 30:
        return "within_30d"
    if delta <= 60:
        return "within_60d"
    return "future"


def ensure_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def fetch_json(url: str) -> tuple[Any | None, dict[str, Any]]:
    status = {"url": url, "status": "not_run", "rows": 0, "error": ""}
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        status["http_status"] = response.status_code
        response.raise_for_status()
        data = response.json()
        status["status"] = "ok"
        return data, status
    except Exception as exc:
        status["status"] = "failed"
        status["error"] = str(exc)
        return None, status


def fetch_text(url: str) -> tuple[str, dict[str, Any]]:
    status = {"url": url, "status": "not_run", "rows": 0, "error": ""}
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        status["http_status"] = response.status_code
        response.raise_for_status()
        status["status"] = "ok"
        return response.text, status
    except Exception as exc:
        status["status"] = "failed"
        status["error"] = str(exc)
        return "", status


def stock_universe() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    candidates = read_csv(ALL_CANDIDATES, dtype=str)
    if not candidates.empty:
        frames.append(candidates)
    mapping = read_csv(COMPANY_THEME_MAPPING, dtype=str)
    if not mapping.empty:
        frames.append(mapping.rename(columns={"stock_id": "stock_id", "stock_name": "stock_name"}))
    if not frames:
        return pd.DataFrame(columns=["stock_id", "stock_name", "market", "industry"])
    combined = pd.concat(frames, ignore_index=True, sort=False)
    code_col = next((c for c in ["stock_id", "code", "ticker"] if c in combined.columns), "")
    name_col = next((c for c in ["stock_name", "name"] if c in combined.columns), "")
    if not code_col:
        return pd.DataFrame(columns=["stock_id", "stock_name", "market", "industry"])
    combined["stock_id"] = combined[code_col].map(normalize_code)
    combined["stock_name"] = combined[name_col].map(safe_str) if name_col else ""
    for col in ["market", "industry"]:
        if col not in combined.columns:
            combined[col] = ""
    combined = combined[combined["stock_id"] != ""]
    return (
        combined[["stock_id", "stock_name", "market", "industry"]]
        .drop_duplicates("stock_id", keep="first")
        .sort_values("stock_id")
        .reset_index(drop=True)
    )


def cached_twse_ex_right_rows(base: date, failed_status: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    existing = read_csv(COMPANY_EVENT_CALENDAR, dtype=str)
    status = dict(failed_status)
    status.setdefault("url", TWSE_EX_RIGHT_URL)
    status.update(twse_live_failure_metadata())
    status["live_rows"] = 0
    status["cached_rows"] = 0
    status["stale_max_trading_days"] = TWSE_EX_RIGHT_STALE_MAX_TRADING_DAYS
    status["cache_window_days"] = {
        "lookback": TWSE_EX_RIGHT_CACHE_LOOKBACK_DAYS,
        "lookahead": TWSE_EX_RIGHT_CACHE_LOOKAHEAD_DAYS,
    }
    status["model_effect_allowed"] = False
    status["pdf_effect_allowed"] = False
    status["calendar_effect_allowed"] = False
    original_error = safe_str(status.get("error")) or "TWSE live fetch did not return parseable rows."

    def hard_fail(note: str) -> tuple[pd.DataFrame, dict[str, Any]]:
        status["status"] = "failed"
        status["note"] = note
        return pd.DataFrame(columns=COMPANY_COLUMNS), status

    if existing.empty:
        return hard_fail("TWSE live fetch failed and no cached ex-right/ex-dividend rows are available.")

    cached = ensure_columns(existing, COMPANY_COLUMNS).copy()
    cached = cached[cached["source"].map(safe_str) == TWSE_EX_RIGHT_SOURCE]
    if cached.empty:
        return hard_fail("TWSE live fetch failed and no cached TWSE ex-right/ex-dividend rows are available.")

    status["cached_total_rows"] = int(len(cached))
    if status["consecutive_live_failures"] > TWSE_EX_RIGHT_MAX_CONSECUTIVE_FAILURES:
        return hard_fail(
            "TWSE live fetch failed too many consecutive times; bounded degradation expired and must hard fail."
        )

    min_event_date = base - timedelta(days=TWSE_EX_RIGHT_CACHE_LOOKBACK_DAYS)
    max_event_date = base + timedelta(days=TWSE_EX_RIGHT_CACHE_LOOKAHEAD_DAYS)
    cached["_event_day"] = cached["event_date"].map(parse_ymd)
    cached["_cache_day"] = cached["last_updated"].map(parse_date_from_text)
    cached["_cache_age_trading_days"] = cached["_cache_day"].map(
        lambda day: trading_days_between(day, base) if day is not None else 9999
    )
    in_event_window = cached[
        cached["_event_day"].map(lambda day: day is not None and min_event_date <= day <= max_event_date)
    ]
    if in_event_window.empty:
        return hard_fail(
            "TWSE live fetch failed and cached rows are outside the trusted reminder event window."
        )

    stale = in_event_window[
        in_event_window["_cache_age_trading_days"] <= TWSE_EX_RIGHT_STALE_MAX_TRADING_DAYS
    ].copy()
    if stale.empty:
        blocked = in_event_window.sort_values(["stock_id", "_event_day"]).drop_duplicates(
            ["stock_id", "event_type", "event_date"], keep="last"
        )
        blocked = blocked[COMPANY_COLUMNS].copy()
        blocked["days_to_event"] = blocked["event_date"].map(lambda value: days_to(value, base))
        blocked["proximity_bucket"] = blocked["event_date"].map(lambda value: proximity_bucket(value, base))
        blocked["event_status"] = "source_degraded_blocked"
        blocked["event_confidence"] = "low"
        blocked["catalyst_tags"] = blocked["catalyst_tags"].map(
            lambda value: add_semicolon_tag(value, "calendar_source_degraded")
        )
        blocked["expected_impact"] = "calendar_event_degraded_blocked_no_effect"
        blocked["notes"] = blocked["notes"].map(
            lambda value: (
                f"{safe_str(value)}; source_status=degraded_blocked_effect; "
                "cached_rows_not_trusted_for_effect=True; model_effect_allowed=False; pdf_effect_allowed=False; "
                f"live_fetch_error={original_error}"
            ).strip("; ")
        )
        status["status"] = "degraded_blocked_effect"
        status["rows"] = int(len(blocked))
        status["blocked_rows"] = int(len(blocked))
        status["cached_rows"] = int(len(blocked))
        status["cache_age_trading_days_min"] = int(in_event_window["_cache_age_trading_days"].min())
        status["cache_age_trading_days_max"] = int(in_event_window["_cache_age_trading_days"].max())
        status["note"] = (
            "TWSE live fetch failed and cached rows are older than the stale_ok trading-day window. "
            "Rows are retained only as degraded blocked-effect context and cannot affect score, rank, "
            "event_proximity_score, upgrade/downgrade, or formal PDF recommendation reasons."
        )
        return blocked, status

    cached = stale[COMPANY_COLUMNS].copy()
    cached["days_to_event"] = cached["event_date"].map(lambda value: days_to(value, base))
    cached["proximity_bucket"] = cached["event_date"].map(lambda value: proximity_bucket(value, base))
    cached["event_status"] = "source_stale_cached"
    cached["event_confidence"] = "low"
    cached["catalyst_tags"] = cached["catalyst_tags"].map(
        lambda value: add_semicolon_tag(add_semicolon_tag(value, "calendar_source_stale"), "calendar_source_degraded")
    )
    cached["expected_impact"] = "calendar_event_stale_reminder_only"
    cached["notes"] = cached["notes"].map(
        lambda value: (
            f"{safe_str(value)}; source_status=stale_ok; cached_reminder_only=True; "
            "model_effect_allowed=False; pdf_effect_allowed=False; "
            f"live_fetch_error={original_error}"
        ).strip("; ")
    )

    status["status"] = "stale_ok"
    status["rows"] = int(len(cached))
    status["cached_rows"] = int(len(cached))
    status["cached_last_updated_min"] = safe_str(cached["last_updated"].min()) if "last_updated" in cached else ""
    status["cached_last_updated_max"] = safe_str(cached["last_updated"].max()) if "last_updated" in cached else ""
    status["cache_age_trading_days_min"] = int(stale["_cache_age_trading_days"].min())
    status["cache_age_trading_days_max"] = int(stale["_cache_age_trading_days"].max())
    status["note"] = (
        "TWSE live fetch failed; using recent cached ex-right/ex-dividend rows as stale reminder-only data. "
        "Rows are low-confidence and cannot affect model score, rank, event_proximity_score, upgrade/downgrade, "
        "or formal PDF recommendation reasons."
    )
    return cached, status


def twse_ex_right_rows(base: date) -> tuple[pd.DataFrame, dict[str, Any]]:
    data, status = fetch_json(TWSE_EX_RIGHT_URL)
    if not isinstance(data, dict):
        return cached_twse_ex_right_rows(base, status)
    fields = data.get("fields") or []
    rows: list[dict[str, str]] = []
    for raw in data.get("data") or []:
        if isinstance(raw, dict):
            values = raw.get("value") or raw.get("data") or []
        else:
            values = raw
        item = dict(zip(fields, values))
        event_date = parse_roc_date(item.get("除權除息日期", ""))
        stock_id = normalize_code(item.get("股票代號", ""))
        stock_name = safe_str(item.get("名稱", ""))
        event_mark = safe_str(item.get("除權息", ""))
        if not event_date or not stock_id:
            continue
        has_right = "權" in event_mark
        has_dividend = "息" in event_mark
        if has_right and has_dividend:
            event_type = "ex_right_dividend"
            event_name = "除權息"
        elif has_right:
            event_type = "ex_right"
            event_name = "除權"
        else:
            event_type = "ex_dividend"
            event_name = "除息"
        cash_dividend = safe_str(item.get("現金股利", ""))
        rows.append(
            {
                "event_date": event_date,
                "event_end_date": event_date,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "market": "TWSE",
                "event_type": event_type,
                "event_name": event_name,
                "event_status": "confirmed",
                "event_confidence": "high",
                "catalyst_tags": "dividend_calendar",
                "source": TWSE_EX_RIGHT_SOURCE,
                "source_url": TWSE_EX_RIGHT_URL,
                "days_to_event": days_to(event_date, base),
                "proximity_bucket": proximity_bucket(event_date, base),
                "expected_impact": "calendar_event_not_standalone_catalyst",
                "notes": f"cash_dividend={cash_dividend}; ex_right_dividend_flag={event_mark}",
                "last_updated": now_text(),
            }
        )
    status["rows"] = len(rows)
    status["live_rows"] = len(rows)
    if not rows:
        status["status"] = "failed"
        status["error"] = "TWSE payload was reachable but parsed zero ex-right/ex-dividend rows."
        return cached_twse_ex_right_rows(base, status)
    status["consecutive_live_failures"] = 0
    status["calendar_effect_allowed"] = True
    return pd.DataFrame(rows, columns=COMPANY_COLUMNS), status


def twse_shareholder_meeting_rows(base: date) -> tuple[pd.DataFrame, dict[str, Any]]:
    data, status = fetch_json(TWSE_DIVIDEND_DISTRIBUTION_URL)
    if not isinstance(data, list):
        return pd.DataFrame(columns=COMPANY_COLUMNS), status
    rows: list[dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        event_date = parse_roc_date(item.get("股東會日期", ""))
        stock_id = normalize_code(item.get("公司代號", ""))
        stock_name = safe_str(item.get("公司名稱", ""))
        if not event_date or not stock_id:
            continue
        rows.append(
            {
                "event_date": event_date,
                "event_end_date": event_date,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "market": "TWSE",
                "event_type": "shareholder_meeting",
                "event_name": "股東會日期",
                "event_status": "confirmed",
                "event_confidence": "high",
                "catalyst_tags": "shareholder_meeting_calendar",
                "source": "TWSE OpenAPI dividend distribution shareholder meeting date",
                "source_url": TWSE_DIVIDEND_DISTRIBUTION_URL,
                "days_to_event": days_to(event_date, base),
                "proximity_bucket": proximity_bucket(event_date, base),
                "expected_impact": "calendar_event_not_standalone_catalyst",
                "notes": (
                    "股東會日期欄位來自 TWSE OpenAPI t187ap45_L。"
                    "This is a governance calendar reminder, not a standalone recommendation catalyst."
                ),
                "last_updated": now_text(),
            }
        )
    status["rows"] = len(rows)
    status["note"] = "TWSE-listed shareholder meeting dates parsed from official OpenAPI t187ap45_L when available."
    return pd.DataFrame(rows, columns=COMPANY_COLUMNS), status


def next_month_revenue_window(base: date) -> tuple[date, date, str]:
    first_this_month = base.replace(day=1)
    if base.day <= 10:
        window_start = first_this_month
        target_month = first_this_month - timedelta(days=1)
    else:
        next_month = (first_this_month + timedelta(days=32)).replace(day=1)
        window_start = next_month
        target_month = first_this_month
    window_end = window_start.replace(day=10)
    revenue_month = target_month.strftime("%Y%m")
    return window_start, window_end, revenue_month


def monthly_revenue_expected_rows(base: date) -> pd.DataFrame:
    universe = stock_universe()
    if universe.empty:
        return pd.DataFrame(columns=COMPANY_COLUMNS)
    start, end, revenue_month = next_month_revenue_window(base)
    rows: list[dict[str, str]] = []
    for _, stock in universe.iterrows():
        code = normalize_code(stock.get("stock_id"))
        if not code:
            continue
        rows.append(
            {
                "event_date": ymd(start),
                "event_end_date": ymd(end),
                "stock_id": code,
                "stock_name": safe_str(stock.get("stock_name")),
                "market": safe_str(stock.get("market")),
                "event_type": "monthly_revenue_expected_window",
                "event_name": f"{revenue_month} monthly revenue expected window",
                "event_status": "expected_window",
                "event_confidence": "medium",
                "catalyst_tags": "monthly_revenue_calendar",
                "source": "rule_based_from_Taiwan_monthly_revenue_deadline",
                "source_url": "https://mops.twse.com.tw/mops/web/t05st10_ifrs",
                "days_to_event": days_to(start, base),
                "proximity_bucket": proximity_bucket(start, base),
                "expected_impact": "scheduled_data_update_not_confirmation",
                "notes": "Most listed companies publish monthly revenue by the 10th of the following month. This is an expected window, not a confirmed catalyst.",
                "last_updated": now_text(),
            }
        )
    return pd.DataFrame(rows, columns=COMPANY_COLUMNS)


def parse_fomc_events(base: date) -> tuple[pd.DataFrame, dict[str, Any]]:
    text, status = fetch_text(FED_FOMC_URL)
    if not text:
        return pd.DataFrame(columns=MACRO_COLUMNS), status
    rows: list[dict[str, str]] = []
    for year_match in re.finditer(r"(?P<year>20\d{2}) FOMC Meetings(?P<section>.*?)(?=20\d{2} FOMC Meetings|</div>\s*</div>\s*<div class=\"panel)", text, re.S):
        year = int(year_match.group("year"))
        section = year_match.group("section")
        for item in re.finditer(
            r"<strong>(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)</strong>.*?"
            r"fomc-meeting__date[^>]*>(?P<date>[^<]+)</div>",
            section,
            re.S,
        ):
            month_name = item.group("month")
            date_text = re.sub(r"[^0-9\\-]", "", item.group("date"))
            if not date_text:
                continue
            day_end = int(date_text.split("-")[-1])
            event_day = date(year, MONTHS[month_name], day_end)
            if event_day < base - timedelta(days=7):
                continue
            rows.append(
                {
                    "event_date": ymd(event_day),
                    "event_end_date": ymd(event_day),
                    "event_name": f"FOMC decision ({month_name} {date_text}, {year})",
                    "event_type": "FOMC",
                    "region": "US",
                    "importance": "high",
                    "source": "Federal Reserve FOMC calendar",
                    "source_url": FED_FOMC_URL,
                    "days_to_event": days_to(event_day, base),
                    "proximity_bucket": proximity_bucket(event_day, base),
                    "related_themes": "macro_liquidity;USD_rates;global_risk",
                    "market_report_section": "macro_calendar",
                    "notes": "Market-risk calendar reminder. It is not a stock-specific catalyst by itself.",
                    "last_updated": now_text(),
                }
            )
    status["rows"] = len(rows)
    return pd.DataFrame(rows, columns=MACRO_COLUMNS), status


def parse_bea_events(base: date) -> tuple[pd.DataFrame, dict[str, Any]]:
    text, status = fetch_text(BEA_SCHEDULE_URL)
    if not text:
        return pd.DataFrame(columns=MACRO_COLUMNS), status
    rows: list[dict[str, str]] = []
    try:
        tables = pd.read_html(StringIO(text))
    except Exception as exc:
        status["status"] = "failed"
        status["error"] = f"read_html failed: {exc}"
        return pd.DataFrame(columns=MACRO_COLUMNS), status
    if not tables:
        status["status"] = "failed"
        status["error"] = "no schedule table found"
        return pd.DataFrame(columns=MACRO_COLUMNS), status
    table = tables[0].copy()
    table.columns = [safe_str(col) for col in table.columns]
    date_col = next((col for col in table.columns if "Year" in col), table.columns[0])
    release_col = next((col for col in table.columns if "Release" in col), table.columns[-1])
    year_match = re.search(r"20\d{2}", date_col)
    year = int(year_match.group(0)) if year_match else base.year
    for _, row in table.iterrows():
        raw_date = safe_str(row.get(date_col))
        release = safe_str(row.get(release_col))
        if not raw_date or not release:
            continue
        date_match = re.search(r"([A-Za-z]+)\s+(\d{1,2})", raw_date)
        if not date_match or date_match.group(1) not in MONTHS:
            continue
        event_day = date(year, MONTHS[date_match.group(1)], int(date_match.group(2)))
        if event_day < base - timedelta(days=7):
            continue
        lowered = release.lower()
        if "personal income" in lowered or "outlays" in lowered:
            event_type = "US_PCE_personal_income"
            importance = "high"
            themes = "US_PCE;inflation;consumption;global_risk"
        elif "gdp" in lowered:
            event_type = "US_GDP"
            importance = "medium"
            themes = "US_GDP;global_growth;global_risk"
        elif "international trade" in lowered:
            event_type = "US_trade"
            importance = "medium"
            themes = "US_trade;export_cycle;global_growth"
        else:
            continue
        rows.append(
            {
                "event_date": ymd(event_day),
                "event_end_date": ymd(event_day),
                "event_name": release,
                "event_type": event_type,
                "region": "US",
                "importance": importance,
                "source": "BEA release schedule",
                "source_url": BEA_SCHEDULE_URL,
                "days_to_event": days_to(event_day, base),
                "proximity_bucket": proximity_bucket(event_day, base),
                "related_themes": themes,
                "market_report_section": "macro_calendar",
                "notes": "Market-risk calendar reminder. It is not a stock-specific catalyst by itself.",
                "last_updated": now_text(),
            }
        )
    status["rows"] = len(rows)
    return pd.DataFrame(rows, columns=MACRO_COLUMNS), status


def parse_bls_release_events(
    url: str,
    label: str,
    event_type: str,
    related_themes: str,
    importance: str,
    base: date,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    text, status = fetch_text(url)
    if not text:
        status["status"] = "blocked_or_unavailable"
        status["note"] = f"{label} was not stored because the official endpoint did not return usable data in this environment."
        return pd.DataFrame(columns=MACRO_COLUMNS), status

    soup = BeautifulSoup(text, "html.parser")
    rows: list[dict[str, str]] = []
    for table in soup.find_all("table"):
        headers = [cell.get_text(" ", strip=True) for cell in table.find_all("th")]
        if not {"Reference Month", "Release Date", "Release Time"}.issubset(set(headers)):
            continue
        for tr in table.find_all("tr"):
            values = [cell.get_text(" ", strip=True) for cell in tr.find_all(["td", "th"])]
            if len(values) < 3 or values[:3] == ["Reference Month", "Release Date", "Release Time"]:
                continue
            release_date = parse_english_release_date(values[1])
            if not release_date:
                continue
            event_day = parse_ymd(release_date)
            if event_day is None or event_day < base - timedelta(days=7):
                continue
            rows.append(
                {
                    "event_date": release_date,
                    "event_end_date": release_date,
                    "event_name": f"{label}: {values[0]}",
                    "event_type": event_type,
                    "region": "US",
                    "importance": importance,
                    "source": f"BLS {label}",
                    "source_url": url,
                    "days_to_event": days_to(release_date, base),
                    "proximity_bucket": proximity_bucket(release_date, base),
                    "related_themes": related_themes,
                    "market_report_section": "macro_calendar",
                    "notes": f"Release time: {values[2]}. Market-risk calendar reminder, not a stock-specific catalyst.",
                    "last_updated": now_text(),
                }
            )
        if rows:
            break

    if rows:
        status["status"] = "ok"
        status["rows"] = len(rows)
        status["note"] = f"Parsed {len(rows)} release rows from the official BLS schedule table."
    else:
        status["status"] = "reachable_not_parsed"
        status["rows"] = 0
        status["note"] = f"{label} was reachable, but no stable release-date rows were parsed."
    return pd.DataFrame(rows, columns=MACRO_COLUMNS), status


def blocked_source_status(url: str, label: str) -> dict[str, Any]:
    _, status = fetch_text(url)
    if status.get("status") == "ok":
        status["status"] = "reachable_not_parsed"
        status["note"] = f"{label} was reachable, but this pipeline has not found a stable parser/output format yet. No rows were stored."
    else:
        status["status"] = "blocked_or_unavailable"
        status["note"] = f"{label} was not stored because the official endpoint did not return usable data in this environment."
    status["rows"] = 0
    return status


def append_update(path: Path, new_df: pd.DataFrame, columns: list[str], key_cols: list[str]) -> pd.DataFrame:
    existing = read_csv(path, dtype=str)
    if existing.empty:
        combined = new_df.copy()
    else:
        combined = pd.concat([existing, new_df], ignore_index=True, sort=False)
    combined = ensure_columns(combined, columns)
    for col in key_cols:
        if col not in combined.columns:
            combined[col] = ""
    combined = combined.drop_duplicates(key_cols, keep="last")
    sort_cols = [col for col in ["event_date", "stock_id", "event_type", "event_name"] if col in combined.columns]
    combined = combined.sort_values(sort_cols).reset_index(drop=True) if sort_cols else combined.reset_index(drop=True)
    write_csv(combined, path)
    return combined


def upcoming(df: pd.DataFrame, columns: list[str], base: date, max_days: int = 60) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=columns)
    out = ensure_columns(df, columns).copy()
    out["days_to_event"] = out["event_date"].map(lambda x: days_to(x, base))
    out["proximity_bucket"] = out["event_date"].map(lambda x: proximity_bucket(x, base))
    numeric_days = pd.to_numeric(out["days_to_event"], errors="coerce")
    out = out[(numeric_days >= -7) & (numeric_days <= max_days)]
    sort_cols = [col for col in ["event_date", "stock_id", "event_type", "event_name"] if col in out.columns]
    return out.sort_values(sort_cols).reset_index(drop=True) if sort_cols else out.reset_index(drop=True)


def markdown_table(df: pd.DataFrame, cols: list[str], limit: int = 50) -> list[str]:
    if df.empty:
        return ["No rows."]
    cols = [col for col in cols if col in df.columns]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.head(limit).iterrows():
        values = []
        for col in cols:
            text = safe_str(row.get(col)).replace("|", "/").replace("\n", " ")
            if len(text) > 80:
                text = text[:80] + "..."
            values.append(text)
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_upcoming_reports(company: pd.DataFrame, macro: pd.DataFrame, status: dict[str, Any]) -> None:
    company_lines = [
        "# Upcoming Catalyst Calendar",
        "",
        f"- generated_at: `{now_text()}`",
        f"- rows: `{len(company)}`",
        "- note: Calendar proximity is a reminder, not a confirmed bullish catalyst.",
        "",
        "## Company / Stock Calendar",
        "",
    ]
    company_lines.extend(
        markdown_table(
            company,
            [
                "event_date",
                "event_end_date",
                "stock_id",
                "stock_name",
                "event_type",
                "event_status",
                "days_to_event",
                "proximity_bucket",
                "catalyst_tags",
                "notes",
            ],
            80,
        )
    )
    UPCOMING_COMPANY_MD.write_text("\n".join(company_lines) + "\n", encoding="utf-8")

    macro_lines = [
        "# Upcoming Macro Event Calendar",
        "",
        f"- generated_at: `{now_text()}`",
        f"- rows: `{len(macro)}`",
        "- note: Macro events are market-risk reminders for the market dashboard. They are not individual stock catalysts by themselves.",
        "",
        "## Macro Calendar",
        "",
    ]
    macro_lines.extend(
        markdown_table(
            macro,
            [
                "event_date",
                "event_name",
                "event_type",
                "region",
                "importance",
                "days_to_event",
                "proximity_bucket",
                "related_themes",
            ],
            80,
        )
    )
    UPCOMING_MACRO_MD.write_text("\n".join(macro_lines) + "\n", encoding="utf-8")

    status_lines = [
        "# Calendar Data Source Status",
        "",
        f"- generated_at: `{status['generated_at']}`",
        "- policy: Official/known-calendar sources are stored. Missing or blocked sources remain pending instead of being fabricated.",
        "",
        "| source | status | rows | url | note |",
        "|---|---|---:|---|---|",
    ]
    for name, info in status["sources"].items():
        status_lines.append(
            f"| {name} | {info.get('status', '')} | {info.get('rows', 0)} | {info.get('url', '')} | {info.get('note', info.get('error', ''))} |"
        )
    status_lines.extend(
        [
            "",
            "## What Is Already Stored",
            "",
            "- TWSE ex-right/ex-dividend calendar is stored when the official endpoint returns rows.",
            "- Monthly revenue expected windows are generated from Taiwan reporting rules for tracked stocks.",
            "- FOMC and BEA macro dates are stored when official pages are reachable.",
            "",
            "## Pending Sources",
            "",
            "- TWSE shareholder meeting dates are stored from official OpenAPI where available; MOPS/TPEX coverage remains pending if blocked.",
            "- BLS CPI/employment schedules are stored when official schedule tables are reachable and parseable.",
            "- Company-specific technology validation, exhibitions, law conferences, and news catalysts need explicit source rows in event_catalyst_log.csv before they can affect stock ranking.",
        ]
    )
    STATUS_MD.write_text("\n".join(status_lines) + "\n", encoding="utf-8")


def needs_review_rows(status: dict[str, Any]) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    generated_at = safe_str(status.get("generated_at")) or now_text()
    sources = status.get("sources", {})
    event_log = read_csv(EVENT_CATALYST_LOG)
    traceable_event_rows = 0
    if not event_log.empty:
        required_cols = ["event_date", "stock_id", "event_type", "source", "source_url", "catalyst_confidence"]
        if all(col in event_log.columns for col in required_cols):
            traceable = event_log.copy()
            for col in required_cols:
                traceable[col] = traceable[col].map(safe_str)
            traceable_event_rows = int((traceable[required_cols] != "").all(axis=1).sum())

    def add(
        *,
        item_id: str,
        source_area: str,
        requested_data: str,
        current_status: str,
        owner: str,
        required_evidence: str,
        next_action: str,
        source_url: str,
        notes: str,
    ) -> None:
        rows.append(
            {
                "item_id": item_id,
                "detected_at": generated_at,
                "source_area": source_area,
                "requested_data": requested_data,
                "current_status": current_status,
                "owner": owner,
                "required_evidence": required_evidence,
                "model_effect_allowed": "False",
                "pdf_effect_allowed": "False",
                "next_action": next_action,
                "source_url": source_url,
                "last_checked_at": generated_at,
                "notes": notes,
            }
        )

    twse_ex_right = sources.get("twse_ex_right_ex_dividend", {})
    twse_status = safe_str(twse_ex_right.get("status"))
    if twse_status and twse_status != "ok":
        if twse_status == "stale_ok":
            next_action = (
                "Restore live TWSE fetch before the stale fallback exceeds the trading-day or consecutive-failure limit. "
                "Stale rows remain low-confidence reminder-only data and must not affect score/rank/PDF recommendation reasons."
            )
        elif twse_status == "degraded_blocked_effect":
            next_action = (
                "Restore live TWSE fetch. Cached rows are outside the stale_ok window and are blocked from all model/PDF effects."
            )
        else:
            next_action = "Fix TWSE fetch/parser or remove event calendar effects when no trusted cached rows are available."
        add(
            item_id="twse_ex_right_ex_dividend_degraded",
            source_area="company_calendar",
            requested_data="TWSE ex-right/ex-dividend calendar",
            current_status=twse_status,
            owner="codex_data_source_work",
            required_evidence=(
                "Live TWSE response with parseable rows, or bounded stale/degraded rows explicitly blocked from model/PDF effects."
            ),
            next_action=next_action,
            source_url=safe_str(twse_ex_right.get("url")) or TWSE_EX_RIGHT_URL,
            notes=safe_str(twse_ex_right.get("note"))
            or safe_str(twse_ex_right.get("error"))
            or "TWSE ex-right/ex-dividend source is not confirmed ok.",
        )

    shareholder = sources.get("mops_shareholder_meeting_calendar", {})
    add(
        item_id="mops_shareholder_meeting_calendar",
        source_area="company_calendar",
        requested_data="Stock-level shareholder meeting dates",
        current_status=safe_str(shareholder.get("status")) or "partial_coverage_twse_only",
        owner="codex_data_source_work",
        required_evidence="Stable MOPS/TPEX machine-readable endpoint or a maintained official export with stock_id and meeting date.",
        next_action="Keep TWSE OpenAPI rows; find and test a stable MOPS/TPEX endpoint before claiming full-market coverage.",
        source_url=safe_str(shareholder.get("url")) or MOPS_SHAREHOLDER_MEETING_URL,
        notes=safe_str(shareholder.get("note")) or "TWSE-listed rows may be stored, but this does not prove full listed/OTC shareholder-meeting coverage.",
    )

    for key, label, url in [
        ("bls_cpi_release_schedule", "BLS CPI release schedule", BLS_CPI_URL),
        ("bls_employment_release_schedule", "BLS employment release schedule", BLS_EMPSIT_URL),
    ]:
        info = sources.get(key, {})
        if safe_str(info.get("status")) == "ok" and int(info.get("rows") or 0) > 0:
            continue
        add(
            item_id=key,
            source_area="macro_calendar",
            requested_data=label,
            current_status=safe_str(info.get("status")) or "needs_parser",
            owner="codex_data_source_work",
            required_evidence="Reliable official parser or alternate official machine-readable release calendar.",
            next_action="Build and validate parser before storing CPI/employment rows.",
            source_url=safe_str(info.get("url")) or url,
            notes=safe_str(info.get("note")) or "Keep out of market-risk report logic until parsed rows exist.",
        )

    add(
        item_id="company_specific_event_sources",
        source_area="event_catalyst",
        requested_data="Company-specific technology validation, exhibitions, news, investor conference, material information, and order/customer-win events",
        current_status="partial_official_material_info_rows" if traceable_event_rows else "needs_explicit_source_rows",
        owner="program_auto_confirm_after_source_integration",
        required_evidence="Rows in data/event_catalysts/event_catalyst_log.csv with source, source_url, confidence, and event_type.",
        next_action=(
            "Broaden beyond official material-information rows to company releases, exhibition pages, and reliable news before claiming full company-specific coverage."
            if traceable_event_rows
            else "Load explicit source rows from official announcements, MOPS, company releases, exhibition pages, or reliable news before scoring."
        ),
        source_url="data/event_catalysts/event_catalyst_log.csv",
        notes=(
            f"{traceable_event_rows} traceable event source rows are present; uncovered company-specific catalyst categories remain blocked."
            if traceable_event_rows
            else "Theme labels or calendar proximity alone must not upgrade stocks or appear as formal PDF recommendation reasons."
        ),
    )

    return pd.DataFrame(rows, columns=NEEDS_REVIEW_COLUMNS)


def write_needs_review_report(df: pd.DataFrame) -> None:
    write_csv(ensure_columns(df, NEEDS_REVIEW_COLUMNS), NEEDS_REVIEW_CSV)

    lines = [
        "# Catalyst Needs Review",
        "",
        f"- generated_at: `{now_text()}`",
        f"- rows: `{len(df)}`",
        "- policy: Rows in this table are not confirmed catalyst data.",
        "- model_effect_allowed: `False` means the item cannot affect score, rank, upgrade, downgrade, or similar_to_shihsinko_flag.",
        "- pdf_effect_allowed: `False` means the item cannot appear as a formal recommendation reason in the PDF.",
        "",
        "## Data-Source Priority",
        "",
        "1. Use original structured data first: CSV, packet fields, source logs, signal logs, warrant tables, market tables, and validated raw links.",
        "2. Use Markdown/PDF reports only as auxiliary readable summaries.",
        "3. If raw/source tables cannot be read and only PDF content is used, the report must start by saying: `本次僅使用 PDF 報告資料，未讀取原始 CSV / packet / source tables，因此只能做摘要型分析。`",
        "",
        "## Items Pending Source Confirmation",
        "",
    ]
    lines.extend(
        markdown_table(
            df,
            [
                "item_id",
                "source_area",
                "requested_data",
                "current_status",
                "owner",
                "model_effect_allowed",
                "pdf_effect_allowed",
                "next_action",
            ],
            50,
        )
    )
    NEEDS_REVIEW_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    base = today_taipei()
    COMPANY_CALENDAR_DIR.mkdir(parents=True, exist_ok=True)
    MACRO_EVENTS_DIR.mkdir(parents=True, exist_ok=True)
    THEME_EVENTS_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    twse_rows, twse_status = twse_ex_right_rows(base)
    shareholder_rows, shareholder_twse_status = twse_shareholder_meeting_rows(base)
    revenue_rows = monthly_revenue_expected_rows(base)
    fomc_rows, fomc_status = parse_fomc_events(base)
    bea_rows, bea_status = parse_bea_events(base)
    bls_cpi_rows, bls_cpi_status = parse_bls_release_events(
        BLS_CPI_URL,
        "CPI release schedule",
        "US_CPI",
        "US_CPI;inflation;Fed_policy;global_risk",
        "high",
        base,
    )
    bls_empsit_rows, bls_empsit_status = parse_bls_release_events(
        BLS_EMPSIT_URL,
        "Employment Situation release schedule",
        "US_employment_situation",
        "US_jobs;Fed_policy;global_growth;global_risk",
        "high",
        base,
    )
    shareholder_status = {
        "url": MOPS_SHAREHOLDER_MEETING_URL,
        "status": "partial_coverage_twse_only" if len(shareholder_rows) else "blocked_or_unavailable",
        "rows": int(len(shareholder_rows)),
        "note": (
            "TWSE-listed shareholder meeting dates are stored from t187ap45_L. "
            "Direct MOPS shareholder pages are blocked or unavailable from this environment, and OTC coverage still needs a stable official endpoint."
        ),
    }

    revenue_status = {
        "url": "https://mops.twse.com.tw/mops/web/t05st10_ifrs",
        "status": "rule_based_expected_window",
        "rows": int(len(revenue_rows)),
        "note": "Expected monthly revenue publication window generated for tracked stocks; not a confirmed company catalyst.",
    }

    company_new = pd.concat([twse_rows, shareholder_rows, revenue_rows], ignore_index=True, sort=False)
    macro_new = pd.concat([fomc_rows, bea_rows, bls_cpi_rows, bls_empsit_rows], ignore_index=True, sort=False)

    company_all = append_update(
        COMPANY_EVENT_CALENDAR,
        company_new,
        COMPANY_COLUMNS,
        ["event_date", "stock_id", "event_type", "source"],
    )
    macro_all = append_update(
        MACRO_EVENT_CALENDAR,
        macro_new,
        MACRO_COLUMNS,
        ["event_date", "event_name", "event_type", "source"],
    )

    if not THEME_EVENT_CALENDAR.exists():
        write_csv(pd.DataFrame(columns=THEME_EVENT_COLUMNS), THEME_EVENT_CALENDAR)

    upcoming_company = upcoming(company_all, COMPANY_COLUMNS, base, max_days=60)
    upcoming_macro = upcoming(macro_all, MACRO_COLUMNS, base, max_days=90)
    write_csv(upcoming_company, UPCOMING_COMPANY_CALENDAR)
    write_csv(upcoming_macro, UPCOMING_MACRO_CALENDAR)

    status = {
        "generated_at": now_text(),
        "files": {
            "company_event_calendar": {"path": COMPANY_EVENT_CALENDAR.as_posix(), "rows": int(len(company_all))},
            "macro_event_calendar": {"path": MACRO_EVENT_CALENDAR.as_posix(), "rows": int(len(macro_all))},
            "upcoming_catalyst_calendar": {"path": UPCOMING_COMPANY_CALENDAR.as_posix(), "rows": int(len(upcoming_company))},
            "upcoming_macro_event_calendar": {"path": UPCOMING_MACRO_CALENDAR.as_posix(), "rows": int(len(upcoming_macro))},
        },
        "sources": {
            "twse_ex_right_ex_dividend": twse_status,
            "twse_shareholder_meeting_from_dividend_distribution": shareholder_twse_status,
            "monthly_revenue_expected_window": revenue_status,
            "federal_reserve_fomc": fomc_status,
            "bea_release_schedule": bea_status,
            "bls_cpi_release_schedule": bls_cpi_status,
            "bls_employment_release_schedule": bls_empsit_status,
            "mops_shareholder_meeting_calendar": shareholder_status,
        },
    }
    STATUS_JSON.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    write_upcoming_reports(upcoming_company, upcoming_macro, status)
    needs_review = needs_review_rows(status)
    write_needs_review_report(needs_review)

    print(f"Saved: {COMPANY_EVENT_CALENDAR} rows={len(company_all)}")
    print(f"Saved: {MACRO_EVENT_CALENDAR} rows={len(macro_all)}")
    print(f"Saved: {UPCOMING_COMPANY_CALENDAR} rows={len(upcoming_company)}")
    print(f"Saved: {UPCOMING_MACRO_CALENDAR} rows={len(upcoming_macro)}")
    print(f"Saved: {STATUS_JSON}")
    print(f"Saved: {NEEDS_REVIEW_CSV} rows={len(needs_review)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
