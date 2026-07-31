from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


LATEST_DIR = Path("output/latest")
STOCK_PRICE_HISTORY_DIR = Path("data/stock_price_history")
PRICE_DUPLICATE_CHECK_COLUMNS = ("open", "high", "low", "close", "volume")
MIN_PRICE_QUALITY_SAMPLE = 100
MAX_ALLOWED_RECENT_DUPLICATE_RATIO = 0.20
MIN_HISTORICAL_REPLAY_OFFICIAL_PRICE_ROWS = 1300

STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"
OFFICIAL_PRICE_FETCH_MD = LATEST_DIR / "official_price_fetch_latest.md"
OFFICIAL_PRICE_FETCH_JSON = LATEST_DIR / "official_price_fetch_latest.json"
OFFICIAL_DAILY_PRICE_CSV = LATEST_DIR / "official_daily_price_latest.csv"
DAILY_PRICE_HISTORY_CONTINUITY_JSON = LATEST_DIR / "daily_price_history_continuity_latest.json"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
WARRANT_FLOW_BY_STOCK_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
WARRANT_DAILY_FETCH_MD = LATEST_DIR / "warrant_daily_fetch_latest.md"
WARRANT_SOURCE_STATUS_JSON = LATEST_DIR / "warrant_source_status_latest.json"
WARRANT_MARKET_REPORT_MD = LATEST_DIR / "warrant_market_report_latest.md"
GROUP_ROTATION_CSV = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"
MARKET_SESSION_STATUS_JSON = LATEST_DIR / "market_session_status_latest.json"

OUTPUT_MD = LATEST_DIR / "data_freshness_latest.md"
OUTPUT_CSV = LATEST_DIR / "data_freshness_latest.csv"


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_date(value) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    digits = re.sub(r"[^0-9]", "", str(value).strip())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    for encoding in ("utf-8", "utf-8-sig", "cp950"):
        try:
            return path.read_text(encoding=encoding)
        except Exception:
            continue
    return ""


def read_market_session_status() -> dict[str, str]:
    if not MARKET_SESSION_STATUS_JSON.exists():
        return {}
    try:
        payload = json.loads(MARKET_SESSION_STATUS_JSON.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}
    if not isinstance(payload, dict):
        return {}
    return {str(key): str(value or "") for key, value in payload.items() if not isinstance(value, (dict, list))}


def extract_first_date_by_patterns(text: str, patterns: list[str]) -> str:
    if not text:
        return ""
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            date = normalize_date(match.group(1))
            if date:
                return date
    return ""


def extract_stock_monitor_price_date() -> str:
    text = read_text(STOCK_MONITOR_MD)
    return extract_first_date_by_patterns(
        text,
        [
            r"latest[_ ]price[_ ]date[^\d]{0,20}([0-9/\-]{8,10})",
            r"main[_ ]price[_ ]date[^\d]{0,20}([0-9/\-]{8,10})",
            r"price[_ ]date[^\d]{0,20}([0-9/\-]{8,10})",
            r"資料日期[^\d]{0,20}([0-9/\-]{8,10})",
            r"主資料日[^\d]{0,20}([0-9/\-]{8,10})",
        ],
    )


def extract_official_price_fetch_date() -> str:
    if OFFICIAL_PRICE_FETCH_JSON.exists():
        try:
            data = json.loads(OFFICIAL_PRICE_FETCH_JSON.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        for key in ("saved_price_date", "main_price_date", "target_date"):
            date = normalize_date(data.get(key, ""))
            if date:
                return date

    text = read_text(OFFICIAL_PRICE_FETCH_MD)
    return extract_first_date_by_patterns(
        text,
        [
            r"saved_price_date[^\d]{0,20}([0-9/\-]{8,10})",
            r"main_price_date[^\d]{0,20}([0-9/\-]{8,10})",
            r"target_date[^\d]{0,20}([0-9/\-]{8,10})",
            r"資料日期[^\d]{0,20}([0-9/\-]{8,10})",
        ],
    )


def extract_csv_max_date(path: Path, preferred_columns: tuple[str, ...] = ()) -> str:
    if not path.exists():
        return ""
    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        return ""
    if df.empty:
        return ""

    columns = list(preferred_columns) + [
        "signal_date",
        "date",
        "trade_date",
        "main_price_date",
        "資料日期",
    ]
    for col in columns:
        if col not in df.columns:
            continue
        dates = df[col].map(normalize_date)
        dates = dates[dates.astype(str).str.len() == 8]
        if not dates.empty:
            return str(dates.max())
    return ""


def read_csv_text(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str).fillna("")
    except Exception:
        return pd.DataFrame()


RAW_THEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_ -]*$")
UNRESOLVED_THEME_VALUES = {"", "其他", "其他業", "other", "theme_unknown", "unclassified", "needs_manual_review"}


def has_cjk_text(value: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", value))


def unresolved_theme_value(value: object) -> bool:
    text = str(value).strip()
    if text in UNRESOLVED_THEME_VALUES:
        return True
    if text.isdigit():
        return True
    if RAW_THEME_PATTERN.fullmatch(text) and not has_cjk_text(text):
        return True
    return False


def group_rotation_theme_state() -> tuple[bool, str]:
    df = read_csv_text(GROUP_ROTATION_CSV)
    if df.empty:
        return True, "group rotation table empty; no theme rows to validate"
    required = {"theme", "theme_display_zh", "theme_resolution_status"}
    missing = sorted(required - set(df.columns))
    if missing:
        return False, f"group rotation missing theme display columns: {missing}"
    bad = df[
        df["theme_resolution_status"].astype(str).ne("resolved")
        | df["theme"].map(unresolved_theme_value)
        | df["theme_display_zh"].map(unresolved_theme_value)
    ]
    if not bad.empty:
        sample = bad[["theme", "theme_display_zh", "theme_resolution_status"]].head(5).to_dict("records")
        return False, f"group rotation has unresolved/raw theme rows: count={len(bad)} sample={sample}"
    return True, "group rotation themes resolved for PDF display"


def csv_date_and_usable_rows(path: Path, preferred_columns: tuple[str, ...] = ()) -> tuple[str, bool]:
    df = read_csv_text(path)
    if df.empty:
        return "", False

    columns = list(preferred_columns) + [
        "signal_date",
        "date",
        "trade_date",
        "main_price_date",
        "資料日期",
    ]
    date = ""
    for col in columns:
        if col not in df.columns:
            continue
        dates = df[col].map(normalize_date)
        dates = dates[dates.astype(str).str.len() == 8]
        if not dates.empty:
            date = str(dates.max())
            break

    if "stock_id" not in df.columns:
        return date, False

    stock_ids = df["stock_id"].astype(str).str.strip()
    usable_rows = bool((stock_ids != "").any())
    return date, usable_rows


def latest_stock_price_history_date() -> str:
    dates: set[str] = set()
    if not STOCK_PRICE_HISTORY_DIR.exists():
        return ""
    for path in STOCK_PRICE_HISTORY_DIR.glob("*.csv"):
        try:
            df = pd.read_csv(path, dtype=str, usecols=["date"])
        except Exception:
            continue
        if df.empty:
            continue
        series = df["date"].map(normalize_date)
        series = series[series.astype(str).str.len() == 8]
        if not series.empty:
            dates.update(str(x) for x in series.unique() if str(x))
    for date in sorted(dates, reverse=True):
        if is_valid_stock_price_history_date(date):
            return date
    return max(dates) if dates else ""


def raw_stock_price_history_high_water_date() -> str:
    dates: set[str] = set()
    if not STOCK_PRICE_HISTORY_DIR.exists():
        return ""
    for path in STOCK_PRICE_HISTORY_DIR.glob("*.csv"):
        try:
            frame = pd.read_csv(path, dtype=str, usecols=["date"])
        except Exception:
            continue
        normalized = frame["date"].map(normalize_date)
        dates.update(str(value) for value in normalized if len(str(value)) == 8)
    return max(dates) if dates else ""


def raw_daily_price_high_water_date() -> str:
    daily_price_dir = Path("data/daily_price")
    dates = []
    for path in daily_price_dir.glob("daily_price_*.csv"):
        match = re.fullmatch(r"daily_price_(20\d{6})\.csv", path.name)
        if match:
            dates.append(match.group(1))
    return max(dates) if dates else ""


def validate_historical_replay_main_price_date(
    main_price_date: str,
    expected_price_history_high_water_date: str,
    *,
    daily_price_high_water_date: str,
    stock_price_history_high_water_date: str,
) -> str:
    values = {
        "historical replay main price date": str(main_price_date or "").strip(),
        "expected price/history high-water date": str(
            expected_price_history_high_water_date or ""
        ).strip(),
        "daily price high-water date": str(daily_price_high_water_date or "").strip(),
        "stock price history high-water date": str(
            stock_price_history_high_water_date or ""
        ).strip(),
    }
    for label, value in values.items():
        if not re.fullmatch(r"20\d{6}", value):
            raise ValueError(f"{label} must be YYYYMMDD")
        try:
            datetime.strptime(value, "%Y%m%d")
        except ValueError as exc:
            raise ValueError(f"{label} must be a valid calendar date") from exc
    expected = values["expected price/history high-water date"]
    paired = {
        values["daily price high-water date"],
        values["stock price history high-water date"],
    }
    if paired != {expected}:
        raise ValueError(
            "historical replay requires exact paired raw price/history high-water dates: "
            f"daily={values['daily price high-water date']} "
            f"stock_history={values['stock price history high-water date']} "
            f"expected={expected}"
        )
    override = values["historical replay main price date"]
    if override > expected:
        raise ValueError(
            "historical replay main price date must not be later than raw paired high-water date"
        )
    return override


def validate_historical_replay_freshness_prerequisites(
    target_date: str,
    expected_price_history_high_water_date: str,
) -> None:
    if not OFFICIAL_DAILY_PRICE_CSV.exists():
        raise ValueError(f"historical replay official latest is missing: {OFFICIAL_DAILY_PRICE_CSV}")
    frame = pd.read_csv(OFFICIAL_DAILY_PRICE_CSV, dtype=str, keep_default_na=False).fillna("")
    required_columns = {"date", "stock_id", "market"}
    if not required_columns.issubset(frame.columns):
        raise ValueError(
            f"historical replay official latest missing schema columns: "
            f"{sorted(required_columns - set(frame.columns))}"
        )
    if frame.empty or set(frame["date"].astype(str)) != {target_date}:
        raise ValueError(
            "historical replay official latest must contain only the exact target date"
        )
    supported_rows = frame["stock_id"].astype(str).str.strip().ne("")
    markets = {str(value).strip().lower() for value in frame["market"] if str(value).strip()}
    if (
        len(frame) < MIN_HISTORICAL_REPLAY_OFFICIAL_PRICE_ROWS
        or int(supported_rows.sum()) < MIN_HISTORICAL_REPLAY_OFFICIAL_PRICE_ROWS
        or not {"twse", "tpex"}.issubset(markets)
    ):
        raise ValueError(
            "historical replay official latest does not satisfy the full-market row/market gate"
        )

    if not OFFICIAL_PRICE_FETCH_JSON.exists():
        raise ValueError(
            f"historical replay official price status is missing: {OFFICIAL_PRICE_FETCH_JSON}"
        )
    price_status = json.loads(OFFICIAL_PRICE_FETCH_JSON.read_text(encoding="utf-8-sig"))
    required_status = {
        "mode": "reconstructed_source_tail_gap_preserve_existing_price_history",
        "target_date": target_date,
        "saved_price_date": target_date,
        "is_target_date": True,
        "result": "success_target_full_market",
        "full_market_ok": True,
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "fallback_used": False,
        "calculation_context_max_date": target_date,
        "future_row_count": 0,
        "future_rows_used": False,
        "price_history_high_water_date": expected_price_history_high_water_date,
    }
    mismatches = {
        key: {"observed": price_status.get(key), "expected": expected}
        for key, expected in required_status.items()
        if price_status.get(key) != expected
    }
    if mismatches:
        raise ValueError(
            f"historical replay official price status contract mismatch: {mismatches}"
        )
    preserved_evidence = price_status.get("preserved_target_slice_evidence") or {}
    if (
        preserved_evidence.get("mode") != "preserve_existing_price_history"
        or preserved_evidence.get("price_history_high_water_date")
        != expected_price_history_high_water_date
    ):
        raise ValueError(
            "historical replay official price status lacks exact preserve-tail evidence"
        )
    normalized_markets = frame["market"].astype(str).str.strip().str.lower()
    observed_counts = {
        "total_rows": int(len(frame)),
        "twse_rows": int(normalized_markets.eq("twse").sum()),
        "tpex_rows": int(normalized_markets.eq("tpex").sum()),
    }
    status_counts = {
        key: int(price_status.get(key, -1) or -1)
        for key in ("total_rows", "twse_rows", "tpex_rows")
    }
    if status_counts != observed_counts:
        raise ValueError(
            "historical replay official price status count parity mismatch: "
            f"status={status_counts} observed={observed_counts}"
        )
    expected_paths = {
        "dated_csv": f"data/daily_price/daily_price_{target_date}.csv",
        "dated_alt_csv": f"data/daily_price/{target_date}.csv",
        "latest_csv": "output/latest/official_daily_price_latest.csv",
    }
    if price_status.get("paths") != expected_paths:
        raise ValueError(
            "historical replay official price status path contract mismatch: "
            f"{price_status.get('paths')} != {expected_paths}"
        )
    canonical_latest = frame.copy().fillna("")
    for column in canonical_latest.columns:
        canonical_latest[column] = canonical_latest[column].astype(str)
    canonical_latest = canonical_latest[sorted(canonical_latest.columns)]
    canonical_latest = canonical_latest.sort_values(
        list(dict.fromkeys(["date", "stock_id", *sorted(canonical_latest.columns)])),
        kind="stable",
    ).reset_index(drop=True)
    if canonical_latest.duplicated(["date", "stock_id"]).any():
        raise ValueError("historical replay official latest contains duplicate date/stock PK rows")
    for key in ("dated_csv", "dated_alt_csv"):
        target_path = Path(expected_paths[key])
        if not target_path.exists():
            raise ValueError(f"historical replay preserved target file is missing: {target_path}")
        target_frame = pd.read_csv(
            target_path,
            dtype=str,
            keep_default_na=False,
        ).fillna("")
        if set(target_frame.columns) != set(frame.columns):
            raise ValueError(
                f"historical replay preserved target schema mismatch: {target_path}"
            )
        if set(target_frame["date"].astype(str)) != {target_date}:
            raise ValueError(
                f"historical replay preserved target is not exact date {target_date}: {target_path}"
            )
        for column in target_frame.columns:
            target_frame[column] = target_frame[column].astype(str)
        canonical_target = target_frame[sorted(target_frame.columns)].sort_values(
            list(dict.fromkeys(["date", "stock_id", *sorted(target_frame.columns)])),
            kind="stable",
        ).reset_index(drop=True)
        if not canonical_target.equals(canonical_latest):
            raise ValueError(
                f"historical replay preserved target content differs from official latest: {target_path}"
            )

    if not DAILY_PRICE_HISTORY_CONTINUITY_JSON.exists():
        raise ValueError(
            "historical replay daily price/history continuity report is missing: "
            f"{DAILY_PRICE_HISTORY_CONTINUITY_JSON}"
        )
    continuity = json.loads(
        DAILY_PRICE_HISTORY_CONTINUITY_JSON.read_text(encoding="utf-8-sig")
    )
    if continuity.get("status") != "pass" or continuity.get("main_price_date") != target_date:
        raise ValueError(
            "historical replay continuity must pass for the exact replay target date"
        )
    expected_trading_dates = continuity.get("expected_trading_dates") or []
    if (
        not isinstance(expected_trading_dates, list)
        or target_date not in expected_trading_dates
        or max(expected_trading_dates, default="") != target_date
    ):
        raise ValueError(
            "historical replay continuity expected_trading_dates must end at the replay target"
        )


def is_valid_stock_price_history_date(date: str) -> bool:
    """Reject copied/stale all-market snapshots.

    Some upstream sources can write a new calendar-date file while carrying old
    OHLCV values. A date is not a reliable all-market price date when many
    symbols have exactly the same OHLCV as one of the recent prior rows.
    """

    checked = 0
    duplicate_recent = 0
    for path in STOCK_PRICE_HISTORY_DIR.glob("*.csv"):
        try:
            usecols = ["date", *PRICE_DUPLICATE_CHECK_COLUMNS]
            df = pd.read_csv(path, dtype=str, usecols=usecols)
        except Exception:
            continue
        if df.empty or "date" not in df.columns:
            continue
        df = df.copy()
        df["_date"] = df["date"].map(normalize_date)
        target = df[df["_date"] == date]
        if target.empty:
            continue
        prior = df[df["_date"] < date].tail(5)
        if prior.empty:
            continue
        checked += 1
        target_row = target.iloc[-1]
        for _, prior_row in prior.iterrows():
            if all(
                str(target_row.get(col, "")).strip() == str(prior_row.get(col, "")).strip()
                for col in PRICE_DUPLICATE_CHECK_COLUMNS
            ):
                duplicate_recent += 1
                break

    if checked < MIN_PRICE_QUALITY_SAMPLE:
        return True
    duplicate_ratio = duplicate_recent / checked
    if duplicate_ratio > MAX_ALLOWED_RECENT_DUPLICATE_RATIO:
        print(
            "Rejected stock_price_history date "
            f"{date}: recent_duplicate_ratio={duplicate_ratio:.2%} "
            f"({duplicate_recent}/{checked})"
        )
        return False
    return True


def cap_to_actual_trading_date(date: str, actual_price_date: str) -> str:
    if date and actual_price_date and date > actual_price_date:
        return actual_price_date
    return date


def component_note(raw_date: str, effective_date: str, main_price_date: str) -> str:
    if not raw_date:
        return "missing_date"
    if raw_date != effective_date:
        return f"raw_date={raw_date}; capped_to_actual_trading_date={effective_date}"
    if effective_date == main_price_date:
        return "ready"
    if effective_date < main_price_date:
        return f"stale_date={effective_date}"
    return f"future_date={effective_date}"


def warrant_component_note(
    raw_date: str,
    effective_date: str,
    main_price_date: str,
    warrant_data_ready: bool,
    warrant_data_note: str,
) -> str:
    base = component_note(raw_date, effective_date, main_price_date)
    if base == "ready" and not warrant_data_ready:
        return warrant_data_note
    return base


def determine_main_price_date(
    stock_monitor_date: str,
    all_candidates_date: str,
    official_fetch_date: str,
    actual_price_date: str,
) -> str:
    # The daily report's canonical date is the latest validated all-market
    # stock price date. Candidate/report tables must be rebuilt to this date;
    # stale candidate dates are a readiness failure, not a reason to move the
    # report date backwards.
    for date in (actual_price_date, all_candidates_date, stock_monitor_date, official_fetch_date):
        if date:
            return cap_to_actual_trading_date(date, actual_price_date)
    return ""


def extract_warrant_flow_state() -> tuple[str, bool, str]:
    """Return warrant date and whether current stock-level rows are usable.

    `warrant_flow_latest.csv` can be header-only on days when the official
    warrant fetch succeeds in date terms but produces no usable warrant rows.
    In that case freshness should not say `missing_date`; downstream reports
    need to know the warrant layer is current but empty/unusable.
    """

    candidates: list[tuple[str, bool, str]] = []

    for path in (WARRANT_FLOW_CSV, WARRANT_FLOW_BY_STOCK_CSV):
        date, usable_rows = csv_date_and_usable_rows(path, ("date", "signal_date", "trade_date"))
        if date:
            candidates.append((date, usable_rows, path.name))

    for path in (WARRANT_MARKET_REPORT_MD, WARRANT_DAILY_FETCH_MD):
        text = read_text(path)
        date = extract_first_date_by_patterns(
            text,
            [
                r"data_date[^\d]{0,20}([0-9/\-]{8,10})",
                r"trade_date[^\d]{0,20}([0-9/\-]{8,10})",
                r"target_date[^\d]{0,20}([0-9/\-]{8,10})",
                r"鞈??交?[^\d]{0,20}([0-9/\-]{8,10})",
            ],
        )
        if date:
            candidates.append((date, False, path.name))

    if not candidates:
        return "", False, "missing warrant_flow_date"

    latest_date = max(date for date, _, _ in candidates)
    latest_sources = [(usable_rows, source) for date, usable_rows, source in candidates if date == latest_date]
    usable = any(usable_rows for usable_rows, _ in latest_sources)
    source_text = ",".join(source for _, source in latest_sources)
    if usable:
        return latest_date, True, f"usable stock-level warrant rows from {source_text}"
    return latest_date, False, f"warrant data date present but stock-level rows unavailable or observe-only in {source_text}"


def extract_warrant_flow_date() -> str:
    date, _, _ = extract_warrant_flow_state()
    return date


def true_text(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def read_warrant_source_status() -> dict[str, str]:
    if not WARRANT_SOURCE_STATUS_JSON.exists():
        return {}
    try:
        data = json.loads(WARRANT_SOURCE_STATUS_JSON.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}
    if not isinstance(data, dict):
        return {}
    return {str(key): str(value) for key, value in data.items()}


def warrant_publish_policy(
    warrant_ready: bool,
    source_status: dict[str, str],
) -> tuple[bool, str, str, str, str, str, str]:
    if warrant_ready:
        return (
            True,
            "ok",
            "current-date warrant layer ready",
            "visible",
            "True",
            "True",
            "0",
        )

    status = source_status.get("status", "")
    publish_allowed = true_text(source_status.get("daily_publish_allowed", ""))
    visibility = source_status.get("warrant_pdf_visibility", "")
    model_effect_allowed = source_status.get("model_effect_allowed", "")
    pdf_effect_allowed = source_status.get("pdf_effect_allowed", "")
    consecutive_days = source_status.get("consecutive_unavailable_trading_days", "")
    note = source_status.get("note", "")

    if status == "warning_grace" and publish_allowed and visibility == "hidden_unavailable":
        return (
            True,
            status,
            note or "current-date warrant source unavailable within bounded grace window",
            visibility,
            model_effect_allowed or "False",
            pdf_effect_allowed or "False",
            consecutive_days,
        )

    return (
        False,
        status or "missing_status",
        note or "current-date warrant source is not available for daily production",
        visibility or "blocked_unavailable",
        model_effect_allowed or "False",
        pdf_effect_allowed or "False",
        consecutive_days,
    )


def determine_report_ready(
    main_price_date: str,
    all_candidates_date: str,
    official_fetch_date: str,
) -> tuple[bool, str]:
    if not main_price_date:
        return False, "missing main_price_date"
    if all_candidates_date != main_price_date:
        return False, "all_candidates date does not match main_price_date"
    if official_fetch_date and official_fetch_date != main_price_date:
        return False, "official price fetch date does not match main_price_date"
    return True, "core daily data dates match main_price_date"


def apply_market_session_gate(
    *,
    report_ready: bool,
    report_ready_note: str,
    market_session_status: str,
    market_session_date: str,
    expected_main_price_date: str,
    main_price_date: str,
) -> tuple[bool, str]:
    if market_session_status != "open_confirmed":
        return False, (
            "market session is not open_confirmed: "
            f"market_session_status={market_session_status or '<missing>'}"
        )
    if not expected_main_price_date:
        return False, "expected_main_price_date is missing"
    if market_session_date != expected_main_price_date:
        return False, (
            f"market_session_date={market_session_date or '<missing>'} does not match "
            f"expected_main_price_date={expected_main_price_date}"
        )
    if main_price_date != expected_main_price_date:
        return False, (
            f"main_price_date={main_price_date or '<missing>'} does not match "
            f"expected_main_price_date={expected_main_price_date}"
        )
    return report_ready, report_ready_note


def determine_warrant_ready(
    main_price_date: str,
    warrant_flow_date: str,
    warrant_data_ready: bool,
    warrant_data_note: str,
) -> tuple[bool, str]:
    if not main_price_date:
        return False, "missing main_price_date"
    if not warrant_flow_date:
        return False, "missing warrant_flow_date"
    if warrant_flow_date != main_price_date:
        return False, (
            "warrant_flow_date does not match main_price_date "
            f"(warrant_flow_date={warrant_flow_date}, main_price_date={main_price_date})"
        )
    if not warrant_data_ready:
        return False, (
            "warrant_flow_date matches main_price_date but stock-level warrant data is unavailable "
            f"({warrant_data_note})"
        )
    return True, "warrant_flow_date matches main_price_date"


def determine_daily_pdf_ready(
    report_ready: bool,
    warrant_ready: bool,
    warrant_publish_allowed: bool,
    report_ready_note: str,
    warrant_ready_note: str,
    warrant_source_status: str = "",
    warrant_pdf_visibility: str = "",
    group_rotation_theme_ready: bool = True,
    group_rotation_theme_note: str = "",
) -> tuple[bool, str]:
    if not report_ready:
        return False, f"core daily data not ready: {report_ready_note}"
    if not group_rotation_theme_ready:
        return False, f"group rotation theme display not ready: {group_rotation_theme_note}"
    if not warrant_ready:
        if not warrant_publish_allowed:
            return False, f"warrant layer not ready: {warrant_ready_note}"
        return True, (
            "core daily data is ready; warrant source unavailable within bounded grace, "
            f"warrant_pdf_visibility={warrant_pdf_visibility or 'hidden_unavailable'}, "
            f"warrant_source_status={warrant_source_status or 'warning_grace'}"
        )
    suffix = f"; {group_rotation_theme_note}" if group_rotation_theme_note else ""
    return True, f"core daily data, warrant layer, and PDF theme display are ready for daily PDF source use{suffix}"


def build_status(
    historical_replay_main_price_date: str = "",
    expected_price_history_high_water_date: str = "",
) -> pd.DataFrame:
    actual_price_date = latest_stock_price_history_date()

    replay_override = ""
    if historical_replay_main_price_date or expected_price_history_high_water_date:
        if not historical_replay_main_price_date or not expected_price_history_high_water_date:
            raise ValueError(
                "historical replay main-price override and expected high-water date must be supplied together"
            )
        raw_daily_high_water = raw_daily_price_high_water_date()
        raw_stock_high_water = raw_stock_price_history_high_water_date()
        replay_override = validate_historical_replay_main_price_date(
            historical_replay_main_price_date,
            expected_price_history_high_water_date,
            daily_price_high_water_date=raw_daily_high_water,
            stock_price_history_high_water_date=raw_stock_high_water,
        )
        if actual_price_date != expected_price_history_high_water_date:
            raise ValueError(
                "historical replay expected high-water date does not equal the latest validated "
                "all-market stock price history date: "
                f"detected={actual_price_date or '<missing>'} "
                f"expected={expected_price_history_high_water_date}"
            )
        validate_historical_replay_freshness_prerequisites(
            replay_override,
            expected_price_history_high_water_date,
        )

    raw_stock_monitor_date = extract_stock_monitor_price_date()
    raw_official_fetch_date = extract_official_price_fetch_date()
    raw_all_candidates_date = extract_csv_max_date(ALL_CANDIDATES_CSV, ("signal_date",))
    raw_warrant_flow_date, raw_warrant_data_ready, raw_warrant_data_note = extract_warrant_flow_state()

    stock_monitor_date = cap_to_actual_trading_date(raw_stock_monitor_date, actual_price_date)
    official_fetch_date = cap_to_actual_trading_date(raw_official_fetch_date, actual_price_date)
    all_candidates_date = cap_to_actual_trading_date(raw_all_candidates_date, actual_price_date)
    warrant_flow_date = cap_to_actual_trading_date(raw_warrant_flow_date, actual_price_date)

    main_price_date = replay_override or determine_main_price_date(
        stock_monitor_date=stock_monitor_date,
        all_candidates_date=all_candidates_date,
        official_fetch_date=official_fetch_date,
        actual_price_date=actual_price_date,
    )

    market_session = read_market_session_status()
    market_session_status = market_session.get("market_status", "").strip()
    market_session_date = normalize_date(market_session.get("market_session_date", ""))
    expected_main_price_date = normalize_date(market_session.get("expected_main_price_date", ""))

    report_ready, report_ready_note = determine_report_ready(
        main_price_date=main_price_date,
        all_candidates_date=all_candidates_date,
        official_fetch_date=official_fetch_date,
    )
    report_ready, report_ready_note = apply_market_session_gate(
        report_ready=report_ready,
        report_ready_note=report_ready_note,
        market_session_status=market_session_status,
        market_session_date=market_session_date,
        expected_main_price_date=expected_main_price_date,
        main_price_date=main_price_date,
    )
    if replay_override:
        report_ready = False
        report_ready_note = (
            "historical structured-source replay updates objective-source freshness only; "
            "publish artifacts remain stale"
        )
    warrant_ready, warrant_ready_note = determine_warrant_ready(
        main_price_date=main_price_date,
        warrant_flow_date=warrant_flow_date,
        warrant_data_ready=raw_warrant_data_ready,
        warrant_data_note=raw_warrant_data_note,
    )
    warrant_source_status_data = read_warrant_source_status()
    (
        warrant_daily_publish_allowed,
        warrant_source_status,
        warrant_source_status_note,
        warrant_pdf_visibility,
        warrant_model_effect_allowed,
        warrant_pdf_effect_allowed,
        warrant_source_consecutive_unavailable_days,
    ) = warrant_publish_policy(warrant_ready, warrant_source_status_data)
    group_rotation_theme_ready, group_rotation_theme_note = group_rotation_theme_state()
    daily_pdf_ready, daily_pdf_ready_note = determine_daily_pdf_ready(
        report_ready=report_ready,
        warrant_ready=warrant_ready,
        warrant_publish_allowed=warrant_daily_publish_allowed,
        report_ready_note=report_ready_note,
        warrant_ready_note=warrant_ready_note,
        warrant_source_status=warrant_source_status,
        warrant_pdf_visibility=warrant_pdf_visibility,
        group_rotation_theme_ready=group_rotation_theme_ready,
        group_rotation_theme_note=group_rotation_theme_note,
    )
    if replay_override:
        daily_pdf_ready = False
        daily_pdf_ready_note = (
            "historical structured-source replay must not mark stale daily PDFs ready"
        )

    main_price_date_source = (
        "historical_replay_override"
        if replay_override
        else (
            "validated_stock_history"
            if actual_price_date and main_price_date == actual_price_date
            else "legacy_priority_fallback"
        )
    )
    row = {
        "generated_at": now_taipei(),
        "market_session_status": market_session_status,
        "market_session_date": market_session_date,
        "expected_main_price_date": expected_main_price_date,
        "market_session_reason_code": market_session.get("reason_code", ""),
        "market_session_generated_at": market_session.get("generated_at", ""),
        "main_price_date": main_price_date,
        "main_price_date_source": main_price_date_source,
        "historical_replay_main_price_date": replay_override,
        "expected_price_history_high_water_date": (
            expected_price_history_high_water_date if replay_override else ""
        ),
        "actual_stock_price_history_date": actual_price_date,
        "stock_monitor_price_date": stock_monitor_date,
        "all_candidates_date": all_candidates_date,
        "official_price_fetch_date": official_fetch_date,
        "warrant_flow_date": warrant_flow_date,
        "raw_stock_monitor_price_date": raw_stock_monitor_date,
        "raw_all_candidates_date": raw_all_candidates_date,
        "raw_official_price_fetch_date": raw_official_fetch_date,
        "raw_warrant_flow_date": raw_warrant_flow_date,
        "report_ready": report_ready,
        "report_ready_note": report_ready_note,
        "warrant_ready": warrant_ready,
        "warrant_ready_note": warrant_ready_note,
        "warrant_source_status": warrant_source_status,
        "warrant_source_status_note": warrant_source_status_note,
        "warrant_source_consecutive_unavailable_days": warrant_source_consecutive_unavailable_days,
        "warrant_source_max_warning_days": warrant_source_status_data.get("max_warning_days", ""),
        "warrant_daily_publish_allowed": warrant_daily_publish_allowed,
        "warrant_pdf_visibility": warrant_pdf_visibility,
        "warrant_model_effect_allowed": warrant_model_effect_allowed,
        "warrant_pdf_effect_allowed": warrant_pdf_effect_allowed,
        "daily_pdf_ready": daily_pdf_ready,
        "daily_pdf_ready_note": daily_pdf_ready_note,
        "stock_monitor_note": component_note(raw_stock_monitor_date, stock_monitor_date, main_price_date),
        "all_candidates_note": component_note(raw_all_candidates_date, all_candidates_date, main_price_date),
        "official_fetch_note": component_note(raw_official_fetch_date, official_fetch_date, main_price_date),
        "warrant_note": warrant_component_note(
            raw_warrant_flow_date,
            warrant_flow_date,
            main_price_date,
            raw_warrant_data_ready,
            raw_warrant_data_note,
        ),
    }
    return pd.DataFrame([row])


def write_markdown(df: pd.DataFrame) -> None:
    row = df.iloc[0].to_dict()
    if row.get("main_price_date_source") == "historical_replay_override":
        rule_text = (
            "Historical structured-source replay explicitly pins the canonical "
            "main_price_date while preserving the same or newer validated raw price/history "
            "high-water date. The two dates remain visible and publish/PDF readiness "
            "must stay false until current publication artifacts are rebuilt."
        )
    else:
        rule_text = (
            "When an upstream daily snapshot has a raw date newer than the latest validated all-market "
            "price history date, the effective report date is capped to the validated price date. "
            "A stock price history date is rejected when many symbols have the exact same OHLCV as "
            "recent prior rows, because that indicates a copied or stale upstream snapshot rather than "
            "a trustworthy trading-day close."
        )
    lines = [
        "# Data Freshness Status",
        "",
        f"- generated_at: `{row.get('generated_at', '')}` Asia/Taipei",
        f"- market_session_status: `{row.get('market_session_status', '')}`",
        f"- market_session_date: `{row.get('market_session_date', '')}`",
        f"- expected_main_price_date: `{row.get('expected_main_price_date', '')}`",
        f"- market_session_reason_code: `{row.get('market_session_reason_code', '')}`",
        f"- main_price_date: `{row.get('main_price_date', '')}`",
        f"- main_price_date_source: `{row.get('main_price_date_source', '')}`",
        f"- historical_replay_main_price_date: `{row.get('historical_replay_main_price_date', '')}`",
        f"- expected_price_history_high_water_date: `{row.get('expected_price_history_high_water_date', '')}`",
        f"- actual_stock_price_history_date: `{row.get('actual_stock_price_history_date', '')}`",
        f"- report_ready: `{row.get('report_ready', '')}`",
        f"- report_ready_note: {row.get('report_ready_note', '')}",
        f"- warrant_ready: `{row.get('warrant_ready', '')}`",
        f"- warrant_ready_note: {row.get('warrant_ready_note', '')}",
        f"- warrant_source_status: `{row.get('warrant_source_status', '')}`",
        f"- warrant_source_status_note: {row.get('warrant_source_status_note', '')}",
        f"- warrant_source_consecutive_unavailable_days: `{row.get('warrant_source_consecutive_unavailable_days', '')}`",
        f"- warrant_daily_publish_allowed: `{row.get('warrant_daily_publish_allowed', '')}`",
        f"- warrant_pdf_visibility: `{row.get('warrant_pdf_visibility', '')}`",
        f"- warrant_model_effect_allowed: `{row.get('warrant_model_effect_allowed', '')}`",
        f"- warrant_pdf_effect_allowed: `{row.get('warrant_pdf_effect_allowed', '')}`",
        f"- daily_pdf_ready: `{row.get('daily_pdf_ready', '')}`",
        f"- daily_pdf_ready_note: {row.get('daily_pdf_ready_note', '')}",
        "",
        "## Component Dates",
        "",
        "| source | effective_date | raw_date | note |",
        "|---|---:|---:|---|",
        (
            f"| all_candidates_latest.csv | {row.get('all_candidates_date', '')} | "
            f"{row.get('raw_all_candidates_date', '')} | {row.get('all_candidates_note', '')} |"
        ),
        (
            f"| official_price_fetch_latest | {row.get('official_price_fetch_date', '')} | "
            f"{row.get('raw_official_price_fetch_date', '')} | {row.get('official_fetch_note', '')} |"
        ),
        (
            f"| stock_monitor_latest.md | {row.get('stock_monitor_price_date', '')} | "
            f"{row.get('raw_stock_monitor_price_date', '')} | {row.get('stock_monitor_note', '')} |"
        ),
        (
            f"| warrant_flow_latest.csv | {row.get('warrant_flow_date', '')} | "
            f"{row.get('raw_warrant_flow_date', '')} | {row.get('warrant_note', '')} |"
        ),
        "",
        "## Rule",
        "",
        rule_text,
        "",
    ]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--historical-replay-main-price-date", default="")
    parser.add_argument("--expected-price-history-high-water-date", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    df = build_status(
        historical_replay_main_price_date=args.historical_replay_main_price_date,
        expected_price_history_high_water_date=args.expected_price_history_high_water_date,
    )
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    write_markdown(df)
    print(f"Saved: {OUTPUT_CSV}")
    print(f"Saved: {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
