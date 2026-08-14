from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
from datetime import datetime
import sys
import time
import urllib.error
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo


TAIPEI_TZ = ZoneInfo("Asia/Taipei")

OPEN_CONFIRMED = "open_confirmed"
CLOSED_SCHEDULED = "closed_scheduled"
CLOSED_EMERGENCY = "closed_emergency"
UNKNOWN = "unknown"
MARKET_STATUSES = {OPEN_CONFIRMED, CLOSED_SCHEDULED, CLOSED_EMERGENCY, UNKNOWN}

TWSE_ANNUAL_CALENDAR_URL = "https://openapi.twse.com.tw/v1/holidaySchedule/holidaySchedule"
DGPA_EMERGENCY_FEED_URL = "https://alerts.ncdr.nat.gov.tw/RssAtomFeed.ashx?AlertType=33"
TWSE_EMERGENCY_RULE_URL = "https://www.twse.com.tw/zh/about/suspended_faq.html"

STATIC_NON_TRADING_DAYS = Path("config/twse_non_trading_days.csv")
EXCEPTIONAL_NON_TRADING_DAYS = Path("data/market_calendar/exceptional_non_trading_days.csv")
MARKET_SESSION_STATUS = Path("output/latest/market_session_status_latest.json")
OFFICIAL_PRICE_FETCH_STATUS = Path("output/latest/official_price_fetch_latest.json")
OFFICIAL_PRICE_FETCH_MARKDOWN = Path("output/latest/official_price_fetch_latest.md")
DAILY_PRICE_DIR = Path("data/daily_price")

DEFAULT_DATA_READY_HOUR = 18
DEFAULT_TIMEOUT_SECONDS = 30
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
EXCEPTIONAL_FIELDS = (
    "date",
    "market_status",
    "market",
    "reason",
    "government_area",
    "closure_scope",
    "source_name",
    "source_url",
    "source_record_id",
    "source_updated_at",
    "twse_rule_url",
    "first_observed_at",
    "last_observed_at",
)


class MarketSessionError(RuntimeError):
    pass


def materialize_market_session_preflight_artifact(
    *,
    repo_root: Path,
    runner_temp: Path,
    artifact_root: Path,
    expected_source_sha: str,
    expected_recovery: dict[str, str],
    fail_after_replace: int = 0,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    runner_temp = runner_temp.resolve()
    artifact_root = artifact_root.resolve()
    if artifact_root != runner_temp / "daily-market-session-preflight":
        raise MarketSessionError(
            "market-session preflight artifact root must be the exact runner-temp location"
        )
    if not artifact_root.is_dir() or artifact_root.is_symlink():
        raise MarketSessionError(
            "market-session preflight artifact root is missing or unsafe"
        )
    expected_files = {
        "market_session_preflight_identity.json",
        "output/latest/market_session_status_latest.json",
        "data/market_calendar/exceptional_non_trading_days.csv",
    }
    observed_files: set[str] = set()
    for path in artifact_root.rglob("*"):
        if path.is_symlink():
            raise MarketSessionError(
                f"market-session preflight artifact contains a symlink: {path}"
            )
        if path.is_file():
            observed_files.add(path.relative_to(artifact_root).as_posix())
    if observed_files != expected_files:
        raise MarketSessionError(
            "market-session preflight artifact file set mismatch: "
            f"expected={sorted(expected_files)} observed={sorted(observed_files)}"
        )
    identity_path = artifact_root / "market_session_preflight_identity.json"
    try:
        identity = json.loads(identity_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise MarketSessionError(
            f"market-session preflight identity is unreadable: {exc}"
        ) from exc
    if identity.get("schema_version") != "daily_market_session_preflight_identity_v1":
        raise MarketSessionError("invalid market-session preflight identity schema")
    source_sha = str(expected_source_sha).strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        raise MarketSessionError(
            "market-session preflight source SHA must be an exact 40-character Git SHA"
        )
    if identity.get("source_sha") != source_sha:
        raise MarketSessionError("market-session preflight source SHA mismatch")
    if identity.get("recovery_source_bundle") != expected_recovery:
        raise MarketSessionError(
            "market-session preflight recovery bundle identity mismatch"
        )
    payload_identities = identity.get("files")
    expected_payloads = expected_files - {"market_session_preflight_identity.json"}
    if (
        not isinstance(payload_identities, dict)
        or set(payload_identities) != expected_payloads
    ):
        raise MarketSessionError(
            "market-session preflight identity file set mismatch"
        )
    repo_identity = repo_root / "market_session_preflight_identity.json"
    if repo_identity.exists() or repo_identity.is_symlink():
        raise MarketSessionError(
            "market-session preflight identity must remain outside the repository"
        )

    snapshots: dict[Path, tuple[bool, bytes]] = {}
    staged: dict[Path, Path] = {}
    try:
        for relative_path in sorted(expected_payloads):
            source = artifact_root / relative_path
            source_payload = source.read_bytes()
            observed_sha = hashlib.sha256(source_payload).hexdigest()
            if observed_sha != payload_identities[relative_path]:
                raise MarketSessionError(
                    f"market-session preflight artifact SHA mismatch: {relative_path}"
                )
            target = (repo_root / relative_path).resolve()
            try:
                target.relative_to(repo_root)
            except ValueError as exc:
                raise MarketSessionError(
                    f"market-session preflight destination escapes repository: {relative_path}"
                ) from exc
            if target.exists() and (not target.is_file() or target.is_symlink()):
                raise MarketSessionError(
                    f"market-session preflight destination is unsafe: {relative_path}"
                )
            target.parent.mkdir(parents=True, exist_ok=True)
            snapshots[target] = (
                target.exists(),
                target.read_bytes() if target.exists() else b"",
            )
            temporary = target.with_name(
                f".{target.name}.preflight-{uuid.uuid4().hex}"
            )
            staged[target] = temporary
            temporary.write_bytes(source_payload)

        replaced = 0
        for target, temporary in staged.items():
            os.replace(temporary, target)
            replaced += 1
            if fail_after_replace and replaced >= fail_after_replace:
                raise OSError(
                    "injected market-session preflight materialization failure"
                )
        if repo_identity.exists() or repo_identity.is_symlink():
            raise MarketSessionError(
                "market-session preflight identity must remain outside the repository"
            )
    except Exception:
        for target, (existed, previous_payload) in reversed(
            tuple(snapshots.items())
        ):
            if existed:
                rollback = target.with_name(
                    f".{target.name}.rollback-{uuid.uuid4().hex}"
                )
                rollback.write_bytes(previous_payload)
                os.replace(rollback, target)
            else:
                target.unlink(missing_ok=True)
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)
    return {
        "artifact_root": str(artifact_root),
        "source_sha": source_sha,
        "materialized_paths": sorted(expected_payloads),
    }


@dataclass(frozen=True)
class EmergencyNotice:
    date: str
    scope: str
    summary: str
    source_record_id: str
    source_url: str
    source_updated_at: str


FetchBytes = Callable[[str, int], bytes]


def normalize_date(value: object) -> str:
    digits = re.sub(r"[^0-9]", "", str(value or "").strip())
    if re.fullmatch(r"20\d{6}", digits):
        return digits
    return ""


def market_session_transition_errors(
    previous: dict[str, Any],
    candidate: dict[str, Any],
) -> list[str]:
    if not previous:
        return []
    errors: list[str] = []
    previous_date = normalize_date(previous.get("market_session_date"))
    candidate_date = normalize_date(candidate.get("market_session_date"))
    if not previous_date or not candidate_date:
        return ["market_session_date must be present on both states"]
    previous_generated = str(previous.get("generated_at") or "").strip()
    candidate_generated = str(candidate.get("generated_at") or "").strip()
    try:
        previous_timestamp = datetime.fromisoformat(previous_generated.replace("Z", "+00:00"))
        candidate_timestamp = datetime.fromisoformat(candidate_generated.replace("Z", "+00:00"))
        if previous_timestamp.tzinfo is None or candidate_timestamp.tzinfo is None:
            raise ValueError("timezone offset is required")
        if candidate_timestamp < previous_timestamp:
            errors.append(
                "market-session generated_at cannot move backward within one session: "
                f"{previous_generated} -> {candidate_generated}"
            )
    except ValueError as exc:
        errors.append(f"market-session generated_at must be timezone-aware ISO-8601: {exc}")
    if candidate_date < previous_date:
        errors.append(f"market_session_date cannot move backward: {previous_date} -> {candidate_date}")
    if candidate_date != previous_date:
        return errors

    previous_status = str(previous.get("market_status") or "")
    candidate_status = str(candidate.get("market_status") or "")
    previous_phase = str(previous.get("phase") or "")
    candidate_phase = str(candidate.get("phase") or "")
    previous_expected = normalize_date(previous.get("expected_main_price_date"))
    candidate_expected = normalize_date(candidate.get("expected_main_price_date"))
    if previous_expected != candidate_expected:
        errors.append(
            "expected_main_price_date cannot change within one market session: "
            f"{previous_expected} -> {candidate_expected}"
        )
    terminal = {OPEN_CONFIRMED, CLOSED_SCHEDULED, CLOSED_EMERGENCY}
    if previous_status in terminal and (
        candidate_status != previous_status or candidate_phase != previous_phase
    ):
        errors.append(
            "terminal market session state cannot transition: "
            f"{previous_status}/{previous_phase} -> {candidate_status}/{candidate_phase}"
        )
    phase_rank = {"preflight": 0, "confirm": 1}
    if phase_rank.get(candidate_phase, -1) < phase_rank.get(previous_phase, -1):
        errors.append(f"market session phase cannot move backward: {previous_phase} -> {candidate_phase}")
    return errors


def write_market_session_status(root: Path, status: dict[str, Any]) -> None:
    status_path = root / MARKET_SESSION_STATUS
    previous: dict[str, Any] = {}
    if status_path.exists():
        try:
            loaded = json.loads(status_path.read_text(encoding="utf-8-sig"))
            if isinstance(loaded, dict):
                previous = loaded
        except Exception as exc:
            raise MarketSessionError(f"existing market-session state is unreadable: {exc}") from exc
    errors = market_session_transition_errors(previous, status)
    if errors:
        raise MarketSessionError("; ".join(errors))
    status_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = status_path.with_name(f".{status_path.name}.tmp")
    try:
        temporary.write_text(
            json.dumps(status, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        temporary.replace(status_path)
    finally:
        temporary.unlink(missing_ok=True)


def parse_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def now_taipei() -> datetime:
    return datetime.now(TAIPEI_TZ)


def iso_taipei(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=TAIPEI_TZ)
    return value.astimezone(TAIPEI_TZ).replace(microsecond=0).isoformat()


def parse_as_of(value: str) -> datetime:
    if not value:
        return now_taipei()
    text = value.strip()
    if re.fullmatch(r"20\d{6}", text):
        parsed = datetime.strptime(text, "%Y%m%d")
    else:
        parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=TAIPEI_TZ)
    return parsed.astimezone(TAIPEI_TZ)


def fetch_url_bytes(url: str, timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json, application/atom+xml, application/xml, text/xml, */*",
            "User-Agent": "tdcc-weekly-report-market-session/1.0",
        },
    )
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt == 3:
                raise
            retry_after = str(exc.headers.get("Retry-After") or "").strip()
            delay = int(retry_after) if retry_after.isdigit() else 5 * attempt
            time.sleep(min(max(delay, 1), 30))
        except (TimeoutError, urllib.error.URLError):
            if attempt == 3:
                raise
            time.sleep(5 * attempt)
    raise AssertionError("unreachable official source retry loop")


def roc_date_to_yyyymmdd(value: object) -> str:
    digits = re.sub(r"[^0-9]", "", str(value or ""))
    if not re.fullmatch(r"\d{7}", digits):
        return ""
    year = int(digits[:3]) + 1911
    date_text = f"{year:04d}{digits[3:]}"
    try:
        parse_date(date_text)
    except ValueError:
        return ""
    return date_text


def parse_twse_annual_calendar(payload: bytes) -> tuple[dict[str, str], set[int]]:
    data = json.loads(payload.decode("utf-8-sig"))
    if not isinstance(data, list) or not data:
        raise MarketSessionError("TWSE annual calendar returned no rows")

    closed: dict[str, str] = {}
    covered_years: set[int] = set()
    for row in data:
        if not isinstance(row, dict):
            continue
        date_text = roc_date_to_yyyymmdd(row.get("Date"))
        if not date_text:
            continue
        covered_years.add(int(date_text[:4]))
        date_value = parse_date(date_text)
        if date_value.weekday() >= 5:
            continue
        name = str(row.get("Name") or "").strip()
        if "開始交易日" in name or "最後交易日" in name:
            continue
        reason = name or str(row.get("Description") or "").strip() or "TWSE scheduled market holiday"
        closed[date_text] = reason

    if not covered_years:
        raise MarketSessionError("TWSE annual calendar has no valid ROC dates")
    return closed, covered_years


def infer_notice_year(updated_text: str, month: int) -> int:
    try:
        updated = datetime.fromisoformat(updated_text)
    except ValueError as exc:
        raise MarketSessionError(f"invalid DGPA notice updated time: {updated_text!r}") from exc
    year = updated.year
    if updated.month == 12 and month == 1:
        year += 1
    elif updated.month == 1 and month == 12:
        year -= 1
    return year


def classify_taipei_closure_scope(detail: str) -> str:
    normalized = re.sub(r"\s+", "", detail)
    if "照常上班" in normalized or "正常上班" in normalized:
        return "open"
    if "停止上班" not in normalized:
        return "unknown"
    if "上午" in normalized:
        return "morning"
    if re.search(r"下午|晚上|晚間|中午|夜間|\d{1,2}[:：]\d{2}.*起", normalized):
        return "partial_day"
    return "full_day"


def parse_dgpa_emergency_feed(payload: bytes) -> list[EmergencyNotice]:
    root = ET.fromstring(payload)
    notices: list[EmergencyNotice] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        record_id = (entry.findtext("atom:id", default="", namespaces=ATOM_NS) or "").strip()
        summary = (entry.findtext("atom:summary", default="", namespaces=ATOM_NS) or "").strip()
        updated = (entry.findtext("atom:updated", default="", namespaces=ATOM_NS) or "").strip()
        if not record_id.startswith("dgpa.gov.tw_") and "行政院人事行政總處" not in summary:
            continue
        location_match = re.search(r"臺北市\s*[:：]\s*([^。]+)", summary)
        if not location_match:
            continue
        detail = location_match.group(1).strip()
        date_match = re.match(r"(?P<month>\d{1,2})/(?P<day>\d{1,2})(?P<decision>.*)", detail)
        if not date_match:
            continue
        month = int(date_match.group("month"))
        day = int(date_match.group("day"))
        year = infer_notice_year(updated, month)
        try:
            date_text = datetime(year, month, day).strftime("%Y%m%d")
        except ValueError:
            continue
        link = ""
        for link_node in entry.findall("atom:link", ATOM_NS):
            if link_node.attrib.get("rel", "alternate") == "alternate":
                link = str(link_node.attrib.get("href") or "").strip()
                if link:
                    break
        notices.append(
            EmergencyNotice(
                date=date_text,
                scope=classify_taipei_closure_scope(date_match.group("decision")),
                summary=summary,
                source_record_id=record_id,
                source_url=link or DGPA_EMERGENCY_FEED_URL,
                source_updated_at=updated,
            )
        )
    return notices


def consolidate_emergency_notices(
    notices: list[EmergencyNotice],
) -> tuple[dict[str, EmergencyNotice], dict[str, str]]:
    grouped: dict[str, list[EmergencyNotice]] = defaultdict(list)
    for notice in notices:
        grouped[notice.date].append(notice)

    latest: dict[str, EmergencyNotice] = {}
    conflicts: dict[str, str] = {}
    for date_text, rows in grouped.items():
        latest_updated = max(row.source_updated_at for row in rows)
        newest = [row for row in rows if row.source_updated_at == latest_updated]
        scopes = {row.scope for row in newest}
        if len(scopes) != 1 or "unknown" in scopes:
            conflicts[date_text] = (
                f"conflicting or unrecognized latest DGPA Taipei notices: scopes={sorted(scopes)}"
            )
            continue
        latest[date_text] = sorted(newest, key=lambda row: row.source_record_id)[-1]
    return latest, conflicts


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [
            {str(key): str(value or "") for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]


def read_date_set(path: Path) -> set[str]:
    rows = read_csv_rows(path)
    dates = {normalize_date(row.get("date")) for row in rows}
    return {date for date in dates if date}


def write_exceptional_evidence(
    root: Path,
    latest_notices: dict[str, EmergencyNotice],
    observed_at: str,
    observed_notice_dates: set[str] | None = None,
) -> list[dict[str, str]]:
    path = root / EXCEPTIONAL_NON_TRADING_DAYS
    existing = read_csv_rows(path)
    latest_dates = set(latest_notices) | set(observed_notice_dates or set())
    preserved = [row for row in existing if normalize_date(row.get("date")) not in latest_dates]
    existing_by_record = {
        str(row.get("source_record_id") or ""): row
        for row in existing
        if str(row.get("source_record_id") or "").strip()
    }

    refreshed: list[dict[str, str]] = []
    for date_text, notice in sorted(latest_notices.items()):
        if notice.scope not in {"full_day", "morning"} or parse_date(date_text).weekday() >= 5:
            continue
        previous = existing_by_record.get(notice.source_record_id, {})
        refreshed.append(
            {
                "date": date_text,
                "market_status": CLOSED_EMERGENCY,
                "market": "TWSE_TPEx",
                "reason": "Taipei City full-day or morning work suspension; TWSE emergency closure rule applies",
                "government_area": "Taipei City",
                "closure_scope": notice.scope,
                "source_name": "DGPA emergency work and school closure feed via NCDR",
                "source_url": notice.source_url,
                "source_record_id": notice.source_record_id,
                "source_updated_at": notice.source_updated_at,
                "twse_rule_url": TWSE_EMERGENCY_RULE_URL,
                "first_observed_at": previous.get("first_observed_at") or observed_at,
                "last_observed_at": observed_at,
            }
        )

    rows = sorted([*preserved, *refreshed], key=lambda row: (row.get("date", ""), row.get("source_record_id", "")))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=EXCEPTIONAL_FIELDS)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in EXCEPTIONAL_FIELDS} for row in rows)
    return rows


def previous_trading_date(
    date_text: str,
    scheduled_non_trading_days: set[str],
    exceptional_non_trading_days: set[str],
    max_backtrack_days: int = 45,
) -> str:
    current = parse_date(date_text) - timedelta(days=1)
    non_trading = scheduled_non_trading_days | exceptional_non_trading_days
    for _ in range(max_backtrack_days):
        candidate = current.strftime("%Y%m%d")
        if current.weekday() < 5 and candidate not in non_trading:
            return candidate
        current -= timedelta(days=1)
    raise MarketSessionError(
        f"no prior trading date found before {date_text} within {max_backtrack_days} days"
    )


def read_official_price_confirmation(root: Path, expected_date: str) -> tuple[bool, dict[str, Any], str]:
    report_path = root / OFFICIAL_PRICE_FETCH_STATUS
    markdown_path = root / OFFICIAL_PRICE_FETCH_MARKDOWN
    if not report_path.is_file() or report_path.is_symlink():
        return False, {}, f"missing {OFFICIAL_PRICE_FETCH_STATUS.as_posix()}"
    if not markdown_path.is_file() or markdown_path.is_symlink():
        return False, {}, f"missing {OFFICIAL_PRICE_FETCH_MARKDOWN.as_posix()}"
    report_payload = report_path.read_bytes()
    try:
        report = json.loads(report_payload.decode("utf-8-sig"))
    except Exception as exc:
        return False, {}, f"unreadable official price fetch status: {exc}"

    report_target = normalize_date(report.get("target_date"))
    report_saved = normalize_date(report.get("saved_price_date"))
    if report_target != expected_date:
        return False, report, f"official fetch target_date={report_target or '<missing>'} expected={expected_date}"
    if report_saved != expected_date:
        return False, report, f"official fetch saved_price_date={report_saved or '<missing>'} expected={expected_date}"
    if report.get("is_target_date") is not True or report.get("full_market_ok") is not True:
        return False, report, "official fetch did not confirm target-date full-market data"

    price_path = root / DAILY_PRICE_DIR / f"daily_price_{expected_date}.csv"
    if not price_path.is_file() or price_path.is_symlink():
        return False, report, f"missing {price_path.relative_to(root).as_posix()}"
    price_payload = price_path.read_bytes()
    expected_price_path = price_path.relative_to(root).as_posix()
    if str(report.get("price_path") or "") != expected_price_path:
        return False, report, "official fetch price_path does not identify the canonical target-date file"
    if int(report.get("price_bytes") or -1) != len(price_payload):
        return False, report, "official fetch price byte count does not match the canonical target-date file"
    price_sha256 = hashlib.sha256(price_payload).hexdigest()
    if str(report.get("price_sha256") or "").lower() != price_sha256:
        return False, report, "official fetch price SHA-256 does not match the canonical target-date file"
    latest_price_path = root / "output/latest/official_daily_price_latest.csv"
    if not latest_price_path.is_file() or latest_price_path.is_symlink():
        return False, report, "official daily price latest path is missing or unsafe"
    latest_price_payload = latest_price_path.read_bytes()
    if latest_price_payload != price_payload:
        return False, report, "official daily price latest bytes differ from the canonical target-date file"
    if str(report.get("latest_price_path") or "") != "output/latest/official_daily_price_latest.csv":
        return False, report, "official fetch latest_price_path is not canonical"
    if int(report.get("latest_price_bytes") or -1) != len(latest_price_payload):
        return False, report, "official fetch latest price byte count mismatch"
    if str(report.get("latest_price_sha256") or "").lower() != hashlib.sha256(
        latest_price_payload
    ).hexdigest():
        return False, report, "official fetch latest price SHA-256 mismatch"
    markdown_payload = markdown_path.read_bytes()
    if str(report.get("fetch_markdown_path") or "") != OFFICIAL_PRICE_FETCH_MARKDOWN.as_posix():
        return False, report, "official fetch markdown path is not canonical"
    if int(report.get("fetch_markdown_bytes") or -1) != len(markdown_payload):
        return False, report, "official fetch markdown byte count mismatch"
    if str(report.get("fetch_markdown_sha256") or "").lower() != hashlib.sha256(
        markdown_payload
    ).hexdigest():
        return False, report, "official fetch markdown SHA-256 mismatch"

    market_rows = {"TWSE": 0, "TPEx": 0}
    wrong_date_rows = 0
    with price_path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            row_date = normalize_date(row.get("date"))
            if row_date != expected_date:
                wrong_date_rows += 1
                continue
            market = str(row.get("market") or "").strip().lower()
            if market in {"twse", "listed"}:
                market_rows["TWSE"] += 1
            elif market in {"tpex", "otc", "emerging"}:
                market_rows["TPEx"] += 1

    confirmation = {
        "path": price_path.relative_to(root).as_posix(),
        "price_bytes": len(price_payload),
        "price_sha256": price_sha256,
        "twse_rows": market_rows["TWSE"],
        "tpex_rows": market_rows["TPEx"],
        "total_rows": market_rows["TWSE"] + market_rows["TPEx"],
        "wrong_date_rows": wrong_date_rows,
        "fetch_result": str(report.get("result") or ""),
        "fetch_status_path": OFFICIAL_PRICE_FETCH_STATUS.as_posix(),
        "fetch_status_bytes": len(report_payload),
        "fetch_status_sha256": hashlib.sha256(report_payload).hexdigest(),
        "fetch_markdown_path": OFFICIAL_PRICE_FETCH_MARKDOWN.as_posix(),
        "fetch_markdown_bytes": len(markdown_payload),
        "fetch_markdown_sha256": hashlib.sha256(markdown_payload).hexdigest(),
    }
    if market_rows["TWSE"] <= 0 or market_rows["TPEx"] <= 0 or wrong_date_rows:
        return False, confirmation, (
            "target-date price file does not contain clean TWSE and TPEx rows: "
            f"TWSE={market_rows['TWSE']} TPEx={market_rows['TPEx']} wrong_date_rows={wrong_date_rows}"
        )
    for field in ("twse_rows", "tpex_rows", "total_rows"):
        if int(report.get(field) or -1) != confirmation[field]:
            return False, confirmation, (
                f"official fetch {field} does not match the canonical target-date file: "
                f"reported={report.get(field)!r} observed={confirmation[field]}"
            )
    return True, confirmation, "TWSE and TPEx target-date prices confirmed"


def build_unknown_status(
    *,
    generated_at: str,
    phase: str,
    assessment_date: str,
    reason_code: str,
    reason: str,
    official_sources: dict[str, Any],
    scheduled_days: set[str],
    exceptional_days: set[str],
    expected_main_price_date: str = "",
    market_session_date: str = "",
    should_run: bool = False,
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_at": generated_at,
        "phase": phase,
        "assessment_date": assessment_date,
        "market_session_date": market_session_date,
        "market_status": UNKNOWN,
        "expected_main_price_date": expected_main_price_date,
        "should_run_daily_pipeline": should_run,
        "reason_code": reason_code,
        "reason": reason,
        "official_sources": official_sources,
        "scheduled_non_trading_days": sorted(scheduled_days),
        "exceptional_non_trading_days": sorted(exceptional_days),
        "price_confirmation": {},
    }


def load_reusable_preflight(
    root: Path,
    *,
    assessment_date: str,
    as_of: datetime,
    max_age_seconds: int = 1800,
) -> dict[str, Any] | None:
    path = root / MARKET_SESSION_STATUS
    if not path.exists():
        return None
    try:
        status = json.loads(path.read_text(encoding="utf-8-sig"))
        generated_at = datetime.fromisoformat(str(status.get("generated_at") or ""))
    except Exception:
        return None
    if generated_at.tzinfo is None:
        generated_at = generated_at.replace(tzinfo=TAIPEI_TZ)
    age_seconds = (as_of - generated_at.astimezone(TAIPEI_TZ)).total_seconds()
    sources = status.get("official_sources")
    if not isinstance(sources, dict):
        return None
    annual = sources.get("twse_annual_calendar")
    emergency = sources.get("dgpa_emergency_closure")
    if not isinstance(annual, dict) or not isinstance(emergency, dict):
        return None
    if not (
        status.get("phase") == "preflight"
        and status.get("market_status") == UNKNOWN
        and status.get("reason_code") == "awaiting_official_price_confirmation"
        and status.get("assessment_date") == assessment_date
        and status.get("should_run_daily_pipeline") is True
        and annual.get("status") == "ok"
        and emergency.get("status") == "ok"
        and 0 <= age_seconds <= max_age_seconds
    ):
        return None
    return status


def confirm_reusable_preflight(
    root: Path,
    preflight: dict[str, Any],
    *,
    generated_at: str,
    write_files: bool,
) -> dict[str, Any]:
    expected_date = normalize_date(preflight.get("expected_main_price_date"))
    confirmed, confirmation, confirmation_reason = read_official_price_confirmation(root, expected_date)
    status = dict(preflight)
    status.update(
        {
            "generated_at": generated_at,
            "phase": "confirm",
            "preflight_reused": True,
            "preflight_generated_at": preflight.get("generated_at", ""),
            "price_confirmation": confirmation,
        }
    )
    if confirmed:
        status.update(
            {
                "market_status": OPEN_CONFIRMED,
                "should_run_daily_pipeline": True,
                "reason_code": "twse_tpex_target_date_confirmed",
                "reason": confirmation_reason,
            }
        )
    else:
        status.update(
            {
                "market_status": UNKNOWN,
                "should_run_daily_pipeline": False,
                "reason_code": "official_price_not_confirmed",
                "reason": confirmation_reason,
            }
        )
    if write_files:
        write_market_session_status(root, status)
    return status


def refresh_market_session_status(
    root: Path,
    *,
    phase: str,
    as_of: datetime | None = None,
    assessment_date: str = "",
    data_ready_hour: int = DEFAULT_DATA_READY_HOUR,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    fetch_bytes: FetchBytes = fetch_url_bytes,
    write_files: bool = True,
) -> dict[str, Any]:
    if phase not in {"preflight", "confirm"}:
        raise ValueError(f"unsupported phase: {phase!r}")
    if not 0 <= data_ready_hour <= 23:
        raise ValueError("data_ready_hour must be between 0 and 23")

    root = root.resolve()
    as_of = (as_of or now_taipei()).astimezone(TAIPEI_TZ)
    generated_at = iso_taipei(as_of)
    if assessment_date:
        normalized_assessment_date = normalize_date(assessment_date)
        if not normalized_assessment_date:
            raise ValueError("assessment_date must be YYYYMMDD")
        assessment_date = normalized_assessment_date
    else:
        assessment_date = as_of.strftime("%Y%m%d")

    if phase == "confirm":
        reusable_preflight = load_reusable_preflight(
            root,
            assessment_date=assessment_date,
            as_of=as_of,
        )
        if reusable_preflight is not None:
            return confirm_reusable_preflight(
                root,
                reusable_preflight,
                generated_at=generated_at,
                write_files=write_files,
            )
    static_days = read_date_set(root / STATIC_NON_TRADING_DAYS)

    official_sources: dict[str, Any] = {
        "twse_annual_calendar": {
            "url": TWSE_ANNUAL_CALENDAR_URL,
            "status": "error",
            "queried_at": generated_at,
        },
        "dgpa_emergency_closure": {
            "url": DGPA_EMERGENCY_FEED_URL,
            "status": "error",
            "queried_at": generated_at,
        },
        "twse_emergency_rule": {
            "url": TWSE_EMERGENCY_RULE_URL,
            "status": "reference",
        },
    }

    scheduled_reasons: dict[str, str] = {}
    covered_years: set[int] = set()
    annual_error = ""
    try:
        scheduled_reasons, covered_years = parse_twse_annual_calendar(
            fetch_bytes(TWSE_ANNUAL_CALENDAR_URL, timeout_seconds)
        )
        official_sources["twse_annual_calendar"].update(
            {
                "status": "ok",
                "closed_weekday_count": len(scheduled_reasons),
                "covered_years": sorted(covered_years),
            }
        )
    except Exception as exc:
        annual_error = str(exc)
        official_sources["twse_annual_calendar"]["error"] = annual_error

    latest_notices: dict[str, EmergencyNotice] = {}
    notice_conflicts: dict[str, str] = {}
    feed_error = ""
    try:
        notices = parse_dgpa_emergency_feed(fetch_bytes(DGPA_EMERGENCY_FEED_URL, timeout_seconds))
        latest_notices, notice_conflicts = consolidate_emergency_notices(notices)
        official_sources["dgpa_emergency_closure"].update(
            {
                "status": "ok",
                "taipei_notice_count": len(notices),
                "latest_taipei_notice_dates": sorted(latest_notices),
                "conflict_dates": sorted(notice_conflicts),
            }
        )
    except Exception as exc:
        feed_error = str(exc)
        official_sources["dgpa_emergency_closure"]["error"] = feed_error

    if not feed_error and write_files:
        evidence_rows = write_exceptional_evidence(
            root,
            latest_notices,
            generated_at,
            observed_notice_dates=set(latest_notices) | set(notice_conflicts),
        )
    else:
        evidence_rows = read_csv_rows(root / EXCEPTIONAL_NON_TRADING_DAYS)
    exceptional_days = {
        normalize_date(row.get("date"))
        for row in evidence_rows
        if str(row.get("market_status") or "").strip() == CLOSED_EMERGENCY
    }
    exceptional_days.discard("")
    scheduled_days = set(scheduled_reasons) | {
        date_text for date_text in static_days if int(date_text[:4]) not in covered_years
    }

    if annual_error or feed_error:
        status = build_unknown_status(
            generated_at=generated_at,
            phase=phase,
            assessment_date=assessment_date,
            reason_code="official_source_unavailable",
            reason="; ".join(part for part in (annual_error, feed_error) if part),
            official_sources=official_sources,
            scheduled_days=scheduled_days,
            exceptional_days=exceptional_days,
        )
    else:
        assessment_year = int(assessment_date[:4])
        if assessment_year not in covered_years:
            status = build_unknown_status(
                generated_at=generated_at,
                phase=phase,
                assessment_date=assessment_date,
                reason_code="annual_calendar_year_not_covered",
                reason=f"TWSE annual calendar does not cover {assessment_year}",
                official_sources=official_sources,
                scheduled_days=scheduled_days,
                exceptional_days=exceptional_days,
            )
        elif assessment_date in notice_conflicts:
            status = build_unknown_status(
                generated_at=generated_at,
                phase=phase,
                assessment_date=assessment_date,
                reason_code="emergency_notice_conflict",
                reason=notice_conflicts[assessment_date],
                official_sources=official_sources,
                scheduled_days=scheduled_days,
                exceptional_days=exceptional_days,
            )
        else:
            assessment_dt = parse_date(assessment_date)
            assessment_notice = latest_notices.get(assessment_date)
            if assessment_dt.weekday() >= 5 or assessment_date in scheduled_reasons:
                expected_date = previous_trading_date(
                    assessment_date,
                    scheduled_days,
                    exceptional_days,
                )
                status = {
                    "schema_version": 1,
                    "generated_at": generated_at,
                    "phase": phase,
                    "assessment_date": assessment_date,
                    "market_session_date": assessment_date,
                    "market_status": CLOSED_SCHEDULED,
                    "expected_main_price_date": expected_date,
                    "should_run_daily_pipeline": False,
                    "reason_code": "weekend" if assessment_dt.weekday() >= 5 else "twse_annual_holiday",
                    "reason": scheduled_reasons.get(assessment_date, "weekend"),
                    "official_sources": official_sources,
                    "scheduled_non_trading_days": sorted(scheduled_days),
                    "exceptional_non_trading_days": sorted(exceptional_days),
                    "price_confirmation": {},
                }
            elif assessment_notice and assessment_notice.scope in {"full_day", "morning"}:
                expected_date = previous_trading_date(
                    assessment_date,
                    scheduled_days,
                    exceptional_days,
                )
                status = {
                    "schema_version": 1,
                    "generated_at": generated_at,
                    "phase": phase,
                    "assessment_date": assessment_date,
                    "market_session_date": assessment_date,
                    "market_status": CLOSED_EMERGENCY,
                    "expected_main_price_date": expected_date,
                    "should_run_daily_pipeline": False,
                    "reason_code": "taipei_full_day_or_morning_work_suspension",
                    "reason": assessment_notice.summary,
                    "official_sources": official_sources,
                    "scheduled_non_trading_days": sorted(scheduled_days),
                    "exceptional_non_trading_days": sorted(exceptional_days),
                    "price_confirmation": {},
                    "emergency_notice": asdict(assessment_notice),
                }
            else:
                as_of_date = as_of.strftime("%Y%m%d")
                if assessment_date < as_of_date or (
                    assessment_date == as_of_date and as_of.hour >= data_ready_hour
                ):
                    expected_date = assessment_date
                else:
                    expected_date = previous_trading_date(
                        assessment_date,
                        scheduled_days,
                        exceptional_days,
                    )

                if expected_date in notice_conflicts:
                    status = build_unknown_status(
                        generated_at=generated_at,
                        phase=phase,
                        assessment_date=assessment_date,
                        market_session_date=expected_date,
                        expected_main_price_date=expected_date,
                        reason_code="expected_session_emergency_notice_conflict",
                        reason=notice_conflicts[expected_date],
                        official_sources=official_sources,
                        scheduled_days=scheduled_days,
                        exceptional_days=exceptional_days,
                    )
                elif phase == "preflight":
                    status = build_unknown_status(
                        generated_at=generated_at,
                        phase=phase,
                        assessment_date=assessment_date,
                        market_session_date=expected_date,
                        expected_main_price_date=expected_date,
                        reason_code="awaiting_official_price_confirmation",
                        reason="TWSE and TPEx target-date prices must be fetched before open status is confirmed",
                        official_sources=official_sources,
                        scheduled_days=scheduled_days,
                        exceptional_days=exceptional_days,
                        should_run=True,
                    )
                else:
                    confirmed, confirmation, confirmation_reason = read_official_price_confirmation(
                        root,
                        expected_date,
                    )
                    if confirmed:
                        status = {
                            "schema_version": 1,
                            "generated_at": generated_at,
                            "phase": phase,
                            "assessment_date": assessment_date,
                            "market_session_date": expected_date,
                            "market_status": OPEN_CONFIRMED,
                            "expected_main_price_date": expected_date,
                            "should_run_daily_pipeline": True,
                            "reason_code": "twse_tpex_target_date_confirmed",
                            "reason": confirmation_reason,
                            "official_sources": official_sources,
                            "scheduled_non_trading_days": sorted(scheduled_days),
                            "exceptional_non_trading_days": sorted(exceptional_days),
                            "price_confirmation": confirmation,
                        }
                    else:
                        status = build_unknown_status(
                            generated_at=generated_at,
                            phase=phase,
                            assessment_date=assessment_date,
                            market_session_date=expected_date,
                            expected_main_price_date=expected_date,
                            reason_code="official_price_not_confirmed",
                            reason=confirmation_reason,
                            official_sources=official_sources,
                            scheduled_days=scheduled_days,
                            exceptional_days=exceptional_days,
                        )
                        status["price_confirmation"] = confirmation

    if status["market_status"] not in MARKET_STATUSES:
        raise AssertionError(f"invalid market status: {status['market_status']}")
    if write_files:
        write_market_session_status(root, status)
    return status


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Resolve the official Taiwan market session state from the live TWSE annual calendar, "
            "DGPA/NCDR emergency closure notices, and target-date TWSE/TPEx price evidence."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--phase", choices=("preflight", "confirm"), required=True)
    parser.add_argument("--as-of", default="", help="Asia/Taipei ISO datetime or YYYYMMDD. Default: now.")
    parser.add_argument("--assessment-date", default="", help="Optional YYYYMMDD assessment date.")
    parser.add_argument("--data-ready-hour", type=int, default=DEFAULT_DATA_READY_HOUR)
    parser.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--no-write", action="store_true", help="Diagnostics/tests only.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        status = refresh_market_session_status(
            args.repo_root,
            phase=args.phase,
            as_of=parse_as_of(args.as_of),
            assessment_date=args.assessment_date,
            data_ready_hour=args.data_ready_hour,
            timeout_seconds=args.timeout_seconds,
            write_files=not args.no_write,
        )
    except Exception as exc:
        print(f"ERROR: market session resolution failed: {exc}", file=sys.stderr)
        return 1

    print(
        "market session resolved: "
        f"market_status={status['market_status']} "
        f"assessment_date={status['assessment_date']} "
        f"market_session_date={status['market_session_date']} "
        f"expected_main_price_date={status['expected_main_price_date']} "
        f"should_run_daily_pipeline={status['should_run_daily_pipeline']} "
        f"reason_code={status['reason_code']}"
    )
    if status["market_status"] == UNKNOWN and status["reason_code"] != "awaiting_official_price_confirmation":
        print(f"ERROR: market session remains unknown: {status['reason']}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
