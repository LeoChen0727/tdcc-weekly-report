from __future__ import annotations

import io
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_taipei, now_text, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "monthly_revenue_history"
RAW_DIR = DATA_DIR / "raw"
HISTORY_CSV = DATA_DIR / "monthly_revenue_history.csv"
LATEST_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_history_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "monthly_revenue_history_latest.md"
SOURCE_STATUS_JSON = RESEARCH_LATEST_DIR / "monthly_revenue_history_source_status_latest.json"
DOCS_LATEST_CSV = DOCS_LATEST_DIR / LATEST_CSV.name
DOCS_LATEST_MD = DOCS_LATEST_DIR / LATEST_MD.name

HISTORY_ID = "monthly_revenue_history"
HISTORY_VERSION = "official_mops_monthly_revenue_v1"
SOURCE_KIND = "official_mops_current_monthly_revenue_openapi"

SOURCE_DEFS = [
    ("listed", "TWSE", "https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv"),
    ("otc", "TPEX", "https://mopsfin.twse.com.tw/opendata/t187ap05_O.csv"),
]

SOURCE_FIELD_ORDER = [
    "source_table_date",
    "revenue_period",
    "stock_id",
    "stock_name",
    "industry",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
]

SOURCE_STANDARD_ALIASES = {
    "source_table_date": ["source_table_date", "table_date"],
    "revenue_period": ["revenue_period"],
    "stock_id": ["stock_id", "ticker", "code"],
    "stock_name": ["stock_name", "name", "company_name"],
    "industry": ["industry"],
    "monthly_revenue": ["monthly_revenue"],
    "previous_month_revenue": ["previous_month_revenue"],
    "last_year_month_revenue": ["last_year_month_revenue"],
    "month_over_month_pct": ["month_over_month_pct"],
    "latest_revenue_yoy_pct": ["latest_revenue_yoy_pct", "revenue_yoy_pct"],
    "cumulative_revenue": ["cumulative_revenue"],
    "last_year_cumulative_revenue": ["last_year_cumulative_revenue"],
    "cumulative_revenue_yoy_pct": ["cumulative_revenue_yoy_pct", "cumulative_yoy_pct"],
    "note": ["note"],
}

OUTPUT_COLUMNS = [
    "generated_at",
    "history_id",
    "history_version",
    "source_kind",
    "market",
    "source_market_name",
    "stock_id",
    "stock_name",
    "industry",
    "revenue_period",
    "revenue_period_roc",
    "source_table_date",
    "source_table_date_raw",
    "fetch_date",
    "fetch_timestamp",
    "source_url",
    "source_file",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "revenue_numerical_anomaly_reason",
    "point_in_time_status",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
    "formal_use_blocker",
    "coverage_note",
]

NUMERIC_COLUMNS = [
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
]


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>", "null"}:
        return ""
    return text


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = re.sub(r"\D", "", text)
    if not digits:
        return ""
    return digits.zfill(4) if len(digits) <= 4 else digits


def clean_numeric_text(value: Any) -> str:
    text = safe_str(value).replace(",", "").replace("%", "").replace("+", "")
    if text in {"", "-", "--"}:
        return ""
    if re.fullmatch(r"-?\d+\.0", text):
        text = text[:-2]
    return text


def to_float(value: Any) -> float:
    text = clean_numeric_text(value)
    if not text:
        return math.nan
    try:
        num = float(text)
    except ValueError:
        return math.nan
    return num if math.isfinite(num) else math.nan


def format_number(value: Any) -> str:
    num = to_float(value)
    if math.isnan(num):
        return ""
    if num.is_integer():
        return str(int(num))
    return f"{num:.6f}".rstrip("0").rstrip(".")


def parse_roc_or_yyyymm(value: Any) -> tuple[str, str]:
    raw = clean_numeric_text(value)
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "", ""
    if len(digits) in {5, 6}:
        padded = digits.zfill(6)
        year = int(padded[:-2])
        month = int(padded[-2:])
        if year < 1911:
            year += 1911
        if 1 <= month <= 12:
            return f"{year:04d}{month:02d}", digits
    if len(digits) >= 6:
        year = int(digits[:4])
        month = int(digits[4:6])
        if year >= 1911 and 1 <= month <= 12:
            return digits[:6], digits
    return "", digits


def parse_roc_or_yyyymmdd(value: Any) -> tuple[str, str]:
    raw = clean_numeric_text(value)
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "", ""
    if len(digits) == 7:
        year = int(digits[:3]) + 1911
        month = int(digits[3:5])
        day = int(digits[5:7])
    elif len(digits) == 8:
        year = int(digits[:4])
        month = int(digits[4:6])
        day = int(digits[6:8])
    else:
        return "", digits
    try:
        return f"{year:04d}{month:02d}{day:02d}", digits
    except ValueError:
        return "", digits


def pick_column(df: pd.DataFrame, candidates: list[str]) -> str:
    for col in candidates:
        if col in df.columns:
            return col
    return ""


def select_source_columns(df: pd.DataFrame) -> tuple[dict[str, str], str]:
    selected: dict[str, str] = {}
    for key, aliases in SOURCE_STANDARD_ALIASES.items():
        selected[key] = pick_column(df, aliases)
    missing = [key for key, column in selected.items() if not column]
    if missing and len(df.columns) >= len(SOURCE_FIELD_ORDER):
        for index, key in enumerate(SOURCE_FIELD_ORDER):
            selected.setdefault(key, "")
            if not selected[key]:
                selected[key] = str(df.columns[index])
        return selected, "official_position_fallback"
    return selected, "standard_alias"


def revenue_flags(latest_yoy: Any, cumulative_yoy: Any) -> tuple[str, str]:
    latest = to_float(latest_yoy)
    cumulative = to_float(cumulative_yoy)
    positive = (
        (not math.isnan(latest) and latest > 0)
        or (not math.isnan(cumulative) and cumulative > 0)
    )
    strong = (
        (not math.isnan(latest) and latest >= 20)
        or (not math.isnan(cumulative) and cumulative >= 10)
    )
    return ("True" if positive else "False", "True" if strong else "False")


def anomaly_flag(latest_yoy: Any, cumulative_yoy: Any, monthly_revenue: Any) -> tuple[str, str]:
    latest = to_float(latest_yoy)
    cumulative = to_float(cumulative_yoy)
    monthly = to_float(monthly_revenue)
    reasons: list[str] = []
    if not math.isnan(latest) and abs(latest) >= 300:
        reasons.append("latest_revenue_yoy_abs_ge_300pct")
    if not math.isnan(cumulative) and abs(cumulative) >= 500:
        reasons.append("cumulative_revenue_yoy_abs_ge_500pct")
    if not math.isnan(monthly) and monthly < 0:
        reasons.append("monthly_revenue_negative")
    return ("True" if reasons else "False", ";".join(reasons))


def raw_file_name(market: str, source_table_date: str, revenue_period: str) -> str:
    date_part = source_table_date or "unknown_date"
    period_part = revenue_period or "unknown_period"
    return f"monthly_revenue_raw_{market}_{date_part}_{period_part}.csv"


def fetch_source(url: str, timeout: int = 30) -> pd.DataFrame:
    response = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    response.encoding = "utf-8-sig"
    return pd.read_csv(io.StringIO(response.text), dtype=str, keep_default_na=False)


def standardize_source(
    df: pd.DataFrame,
    *,
    market: str,
    source_market_name: str,
    source_url: str,
    fetch_date: str,
    fetch_timestamp: str,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    status: dict[str, Any] = {
        "market": market,
        "source_market_name": source_market_name,
        "source_url": source_url,
        "raw_rows": int(len(df)),
        "standardized_rows": 0,
        "status": "ok",
    }
    if df.empty:
        status["status"] = "empty_source"
        return pd.DataFrame(columns=OUTPUT_COLUMNS), status

    selected, selected_column_mode = select_source_columns(df)
    status["selected_columns"] = selected
    status["selected_column_indexes"] = {
        key: int(df.columns.get_loc(column))
        for key, column in selected.items()
        if column in df.columns
    }
    status["selected_column_mode"] = selected_column_mode
    required = ["stock_id", "revenue_period", "source_table_date", "latest_revenue_yoy_pct"]
    missing = [key for key in required if not selected.get(key)]
    if missing:
        status["status"] = f"missing_required_columns:{';'.join(missing)}"
        return pd.DataFrame(columns=OUTPUT_COLUMNS), status

    rows: list[dict[str, Any]] = []
    generated_at = now_text()
    for _, row in df.iterrows():
        stock_id = normalize_code(row.get(selected["stock_id"], ""))
        revenue_period, revenue_period_roc = parse_roc_or_yyyymm(row.get(selected["revenue_period"], ""))
        source_table_date, source_table_date_raw = parse_roc_or_yyyymmdd(row.get(selected["source_table_date"], ""))
        if not stock_id or not revenue_period or not source_table_date:
            continue
        values = {
            col: format_number(row.get(selected[col], "")) if selected.get(col) else ""
            for col in NUMERIC_COLUMNS
        }
        positive, strong = revenue_flags(
            values["latest_revenue_yoy_pct"],
            values["cumulative_revenue_yoy_pct"],
        )
        anomaly, anomaly_reason = anomaly_flag(
            values["latest_revenue_yoy_pct"],
            values["cumulative_revenue_yoy_pct"],
            values["monthly_revenue"],
        )
        source_file = RAW_DIR / raw_file_name(market, source_table_date, revenue_period)
        rows.append(
            {
                "generated_at": generated_at,
                "history_id": HISTORY_ID,
                "history_version": HISTORY_VERSION,
                "source_kind": SOURCE_KIND,
                "market": market,
                "source_market_name": source_market_name,
                "stock_id": stock_id,
                "stock_name": safe_str(row.get(selected.get("stock_name", ""), "")),
                "industry": safe_str(row.get(selected.get("industry", ""), "")),
                "revenue_period": revenue_period,
                "revenue_period_roc": revenue_period_roc,
                "source_table_date": source_table_date,
                "source_table_date_raw": source_table_date_raw,
                "fetch_date": fetch_date,
                "fetch_timestamp": fetch_timestamp,
                "source_url": source_url,
                "source_file": source_file.relative_to(ROOT).as_posix(),
                **values,
                "note": safe_str(row.get(selected.get("note", ""), "")),
                "revenue_positive_flag": positive,
                "revenue_strong_flag": strong,
                "revenue_numerical_anomaly_flag": anomaly,
                "revenue_numerical_anomaly_reason": anomaly_reason,
                "point_in_time_status": "ready_official_source_table_date",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
                "formal_use_blocker": "blocked_until_sufficient_history_coverage_and_model_promotion",
                "coverage_note": (
                    "full_market_current_monthly_revenue_saved_from_official_openapi; "
                    "historical coverage starts at the first saved source table date unless separately backfilled"
                ),
            }
        )

    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    status["standardized_rows"] = int(len(out))
    status["revenue_periods"] = sorted(out["revenue_period"].dropna().astype(str).unique().tolist()) if not out.empty else []
    status["source_table_dates"] = sorted(out["source_table_date"].dropna().astype(str).unique().tolist()) if not out.empty else []
    return out, status


def fetch_current_sources() -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    fetch_dt = now_taipei()
    fetch_date = fetch_dt.strftime("%Y%m%d")
    fetch_timestamp = fetch_dt.strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")
    frames: list[pd.DataFrame] = []
    statuses: list[dict[str, Any]] = []
    for market, source_market_name, url in SOURCE_DEFS:
        try:
            raw = fetch_source(url)
        except Exception as exc:
            statuses.append(
                {
                    "market": market,
                    "source_market_name": source_market_name,
                    "source_url": url,
                    "raw_rows": 0,
                    "standardized_rows": 0,
                    "status": f"fetch_failed:{exc}",
                }
            )
            continue
        standardized, status = standardize_source(
            raw,
            market=market,
            source_market_name=source_market_name,
            source_url=url,
            fetch_date=fetch_date,
            fetch_timestamp=fetch_timestamp,
        )
        statuses.append(status)
        if not standardized.empty:
            frames.append(standardized)
            for source_file in sorted(standardized["source_file"].unique()):
                target = ROOT / source_file
                target.parent.mkdir(parents=True, exist_ok=True)
                subset = raw.copy()
                subset.to_csv(target, index=False, encoding="utf-8-sig", lineterminator="\n")
    if not frames:
        return pd.DataFrame(columns=OUTPUT_COLUMNS), statuses
    current = pd.concat(frames, ignore_index=True)
    current = current.drop_duplicates(["market", "stock_id", "revenue_period"], keep="last")
    return current[OUTPUT_COLUMNS].sort_values(["revenue_period", "market", "stock_id"]).reset_index(drop=True), statuses


def merge_history(current: pd.DataFrame, history_path: Path = HISTORY_CSV) -> pd.DataFrame:
    if history_path.exists():
        existing = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    else:
        existing = pd.DataFrame(columns=OUTPUT_COLUMNS)
    for col in OUTPUT_COLUMNS:
        if col not in existing.columns:
            existing[col] = ""
        if col not in current.columns:
            current[col] = ""
    combined = pd.concat([existing[OUTPUT_COLUMNS], current[OUTPUT_COLUMNS]], ignore_index=True, sort=False)
    combined = combined.drop_duplicates(["market", "stock_id", "revenue_period"], keep="last")
    return combined[OUTPUT_COLUMNS].sort_values(["revenue_period", "market", "stock_id"]).reset_index(drop=True)


def write_markdown(history: pd.DataFrame, current: pd.DataFrame, statuses: list[dict[str, Any]]) -> None:
    period_coverage = (
        history.groupby("revenue_period", dropna=False)
        .agg(rows=("stock_id", "size"), unique_stocks=("stock_id", "nunique"), source_table_date=("source_table_date", "max"))
        .reset_index()
        .sort_values("revenue_period")
        if not history.empty
        else pd.DataFrame(columns=["revenue_period", "rows", "unique_stocks", "source_table_date"])
    )
    market_coverage = (
        history.groupby(["revenue_period", "market"], dropna=False)
        .agg(rows=("stock_id", "size"), unique_stocks=("stock_id", "nunique"))
        .reset_index()
        .sort_values(["revenue_period", "market"])
        if not history.empty
        else pd.DataFrame(columns=["revenue_period", "market", "rows", "unique_stocks"])
    )
    anomalies = (
        history[history["revenue_numerical_anomaly_flag"].astype(str).eq("True")]
        .groupby("revenue_numerical_anomaly_reason", dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values("rows", ascending=False)
        if not history.empty
        else pd.DataFrame(columns=["revenue_numerical_anomaly_reason", "rows"])
    )
    status_df = pd.DataFrame(statuses)
    lines = [
        "# Monthly Revenue History Data Layer",
        "",
        f"- generated_at: `{now_text()}`",
        f"- history_id: `{HISTORY_ID}`",
        f"- history_version: `{HISTORY_VERSION}`",
        f"- source_kind: `{SOURCE_KIND}`",
        f"- current_fetch_rows: `{len(current)}`",
        f"- total_history_rows: `{len(history)}`",
        f"- unique_stocks: `{history['stock_id'].nunique() if not history.empty else 0}`",
        f"- revenue_period_min: `{history['revenue_period'].min() if not history.empty else ''}`",
        f"- revenue_period_max: `{history['revenue_period'].max() if not history.empty else ''}`",
        "- allowed_use: save full-market official monthly revenue rows and join research rows where `source_table_date <= signal_date`.",
        "- forbidden_use: do not label older historical signals with the latest saved revenue period; formal model gates require sufficient coverage audit and promotion.",
        "- current_limitation: the current official OpenAPI returns the latest available revenue period only; older periods require separate validated backfill or accumulation over future runs.",
        "",
        "## Source Fetch Status",
        "",
        markdown_table(status_df, ["market", "source_market_name", "raw_rows", "standardized_rows", "status"], limit=10)
        if not status_df.empty
        else "No source status rows.",
        "",
        "## Period Coverage",
        "",
        markdown_table(period_coverage, ["revenue_period", "rows", "unique_stocks", "source_table_date"], limit=60)
        if not period_coverage.empty
        else "No period coverage rows.",
        "",
        "## Market Coverage",
        "",
        markdown_table(market_coverage, ["revenue_period", "market", "rows", "unique_stocks"], limit=80)
        if not market_coverage.empty
        else "No market coverage rows.",
        "",
        "## Numerical Anomaly Labels",
        "",
        markdown_table(anomalies, ["revenue_numerical_anomaly_reason", "rows"], limit=30)
        if not anomalies.empty
        else "No numerical anomaly labels.",
        "",
        "## Current Sample",
        "",
        markdown_table(
            current,
            [
                "market",
                "stock_id",
                "stock_name",
                "revenue_period",
                "source_table_date",
                "latest_revenue_yoy_pct",
                "cumulative_revenue_yoy_pct",
                "revenue_strong_flag",
                "allowed_for_formal_historical_model_use",
            ],
            limit=30,
        )
        if not current.empty
        else "No current rows.",
    ]
    LATEST_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_LATEST_MD.write_text(LATEST_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    current, statuses = fetch_current_sources()
    if current.empty:
        raise RuntimeError("No monthly revenue rows fetched from official sources")
    history = merge_history(current)
    write_csv(history, HISTORY_CSV)
    write_csv(history, LATEST_CSV)
    write_csv(history, DOCS_LATEST_CSV)
    SOURCE_STATUS_JSON.write_text(json.dumps(statuses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(history, current, statuses)
    print(f"Saved {HISTORY_CSV} rows={len(history)}")
    print(f"Saved {LATEST_CSV} rows={len(history)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
