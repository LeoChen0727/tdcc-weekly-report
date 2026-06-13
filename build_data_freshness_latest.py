from __future__ import annotations

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

STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"
OFFICIAL_PRICE_FETCH_MD = LATEST_DIR / "official_price_fetch_latest.md"
OFFICIAL_PRICE_FETCH_JSON = LATEST_DIR / "official_price_fetch_latest.json"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
WARRANT_FLOW_BY_STOCK_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
WARRANT_DAILY_FETCH_MD = LATEST_DIR / "warrant_daily_fetch_latest.md"
WARRANT_MARKET_REPORT_MD = LATEST_DIR / "warrant_market_report_latest.md"
GROUP_ROTATION_CSV = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"

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
    report_ready_note: str,
    warrant_ready_note: str,
    group_rotation_theme_ready: bool = True,
    group_rotation_theme_note: str = "",
) -> tuple[bool, str]:
    if not report_ready:
        return False, f"core daily data not ready: {report_ready_note}"
    if not warrant_ready:
        return False, f"warrant layer not ready: {warrant_ready_note}"
    if not group_rotation_theme_ready:
        return False, f"group rotation theme display not ready: {group_rotation_theme_note}"
    suffix = f"; {group_rotation_theme_note}" if group_rotation_theme_note else ""
    return True, f"core daily data, warrant layer, and PDF theme display are ready for daily PDF source use{suffix}"


def build_status() -> pd.DataFrame:
    actual_price_date = latest_stock_price_history_date()

    raw_stock_monitor_date = extract_stock_monitor_price_date()
    raw_official_fetch_date = extract_official_price_fetch_date()
    raw_all_candidates_date = extract_csv_max_date(ALL_CANDIDATES_CSV, ("signal_date",))
    raw_warrant_flow_date, raw_warrant_data_ready, raw_warrant_data_note = extract_warrant_flow_state()

    stock_monitor_date = cap_to_actual_trading_date(raw_stock_monitor_date, actual_price_date)
    official_fetch_date = cap_to_actual_trading_date(raw_official_fetch_date, actual_price_date)
    all_candidates_date = cap_to_actual_trading_date(raw_all_candidates_date, actual_price_date)
    warrant_flow_date = cap_to_actual_trading_date(raw_warrant_flow_date, actual_price_date)

    main_price_date = determine_main_price_date(
        stock_monitor_date=stock_monitor_date,
        all_candidates_date=all_candidates_date,
        official_fetch_date=official_fetch_date,
        actual_price_date=actual_price_date,
    )

    report_ready, report_ready_note = determine_report_ready(
        main_price_date=main_price_date,
        all_candidates_date=all_candidates_date,
        official_fetch_date=official_fetch_date,
    )
    warrant_ready, warrant_ready_note = determine_warrant_ready(
        main_price_date=main_price_date,
        warrant_flow_date=warrant_flow_date,
        warrant_data_ready=raw_warrant_data_ready,
        warrant_data_note=raw_warrant_data_note,
    )
    group_rotation_theme_ready, group_rotation_theme_note = group_rotation_theme_state()
    daily_pdf_ready, daily_pdf_ready_note = determine_daily_pdf_ready(
        report_ready=report_ready,
        warrant_ready=warrant_ready,
        report_ready_note=report_ready_note,
        warrant_ready_note=warrant_ready_note,
        group_rotation_theme_ready=group_rotation_theme_ready,
        group_rotation_theme_note=group_rotation_theme_note,
    )

    row = {
        "generated_at": now_taipei(),
        "main_price_date": main_price_date,
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
    lines = [
        "# Data Freshness Status",
        "",
        f"- generated_at: `{row.get('generated_at', '')}` Asia/Taipei",
        f"- main_price_date: `{row.get('main_price_date', '')}`",
        f"- actual_stock_price_history_date: `{row.get('actual_stock_price_history_date', '')}`",
        f"- report_ready: `{row.get('report_ready', '')}`",
        f"- report_ready_note: {row.get('report_ready_note', '')}",
        f"- warrant_ready: `{row.get('warrant_ready', '')}`",
        f"- warrant_ready_note: {row.get('warrant_ready_note', '')}",
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
        (
            "When an upstream daily snapshot has a raw date newer than the latest validated all-market "
            "price history date, the effective report date is capped to the validated price date. "
            "A stock price history date is rejected when many symbols have the exact same OHLCV as "
            "recent prior rows, because that indicates a copied or stale upstream snapshot rather than "
            "a trustworthy trading-day close."
        ),
        "",
    ]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    df = build_status()
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    write_markdown(df)
    print(f"Saved: {OUTPUT_CSV}")
    print(f"Saved: {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
