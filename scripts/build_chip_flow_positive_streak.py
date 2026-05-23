from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import json
import math
import re

import pandas as pd
import requests

from tracking_utils import (
    append_update_csv,
    latest_price_date,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/chip_flow")
DATA_DIR = Path("data")
DAILY_PRICE_DIR = DATA_DIR / "daily_price"
INSTITUTIONAL_DIR = DATA_DIR / "institutional_investor_flow"
BROKER_BRANCH_DIR = DATA_DIR / "broker_branch_trading"
CONFIG_EIGHT_BANKS = Path("config/eight_public_bank_brokers.csv")

OUTPUT_CSV = LATEST_DIR / "chip_flow_positive_streak_latest.csv"
OUTPUT_MD = LATEST_DIR / "chip_flow_positive_streak_latest.md"
STATUS_JSON = LATEST_DIR / "chip_flow_source_status_latest.json"
STATUS_MD = LATEST_DIR / "chip_flow_source_status_latest.md"
INSTITUTIONAL_LATEST = LATEST_DIR / "institutional_investor_flow_latest.csv"
HISTORY_CSV = HISTORY_DIR / "chip_flow_positive_streak_history.csv"

CATEGORY = "chip_flow_positive_streak"
CATEGORY_CN = "主力-三大法人-八大行庫連續轉強"
CONSECUTIVE_DAYS = 3
TOP_N_BRANCHES = 15

OUTPUT_COLUMNS = [
    "date",
    "category",
    "category_cn",
    "stock_id",
    "stock_name",
    "market",
    "main_force_net_lots",
    "institutional_net_lots",
    "eight_banks_net_lots",
    "chip_flow_adjusted_net_lots",
    "positive_streak_days",
    "latest_positive",
    "signal_source_file",
    "note",
]


def roc_date(date: str) -> str:
    date = normalize_date(date)
    if len(date) != 8:
        return ""
    year = int(date[:4]) - 1911
    return f"{year}/{date[4:6]}/{date[6:8]}"


def number(value: Any) -> float:
    num = to_number(value)
    return 0.0 if math.isnan(num) else float(num)


def maybe_lots(series: pd.Series, source_name: str = "") -> pd.Series:
    values = pd.to_numeric(series.astype(str).str.replace(",", "", regex=False), errors="coerce").fillna(0)
    source_name = source_name.lower()
    if "share" in source_name or "股" in source_name:
        return values / 1000.0
    non_zero = values[values.abs() > 0]
    if not non_zero.empty and non_zero.abs().median() > 10000:
        return values / 1000.0
    return values


def latest_trade_dates(limit: int = 10) -> list[str]:
    dates: list[str] = []
    for path in DAILY_PRICE_DIR.glob("*.csv"):
        date = normalize_date(path.stem)
        if date:
            dates.append(date)
    if not dates:
        dates.append(latest_price_date())
    dates = sorted(set(dates))
    return dates[-limit:]


def read_table_from_json(payload: dict[str, Any]) -> pd.DataFrame:
    fields = payload.get("fields") or payload.get("tables", [{}])[0].get("fields", [])
    data = payload.get("data") or payload.get("tables", [{}])[0].get("data", [])
    if fields and data:
        return pd.DataFrame(data, columns=fields)
    return pd.DataFrame()


def normalize_institutional(df: pd.DataFrame, date: str, market: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    out = df.copy()
    rename: dict[str, str] = {}
    for col in out.columns:
        text = safe_str(col)
        if text in {"證券代號", "代號", "股票代號", "Code", "SecuritiesCompanyCode"}:
            rename[col] = "stock_id"
        elif text in {"證券名稱", "名稱", "股票名稱", "Name", "CompanyName"}:
            rename[col] = "stock_name"
        elif "三大法人買賣超" in text or text in {"institutional_net_lots", "three_institution_net_lots"}:
            rename[col] = "institutional_net_raw"
    out = out.rename(columns=rename)
    if "stock_id" not in out.columns:
        return pd.DataFrame()
    if "institutional_net_raw" not in out.columns:
        numeric_cols = [c for c in out.columns if "買賣超" in safe_str(c)]
        if numeric_cols:
            out["institutional_net_raw"] = out[numeric_cols[-1]]
        else:
            out["institutional_net_raw"] = 0
    if "stock_name" not in out.columns:
        out["stock_name"] = ""
    out["date"] = date
    out["stock_id"] = out["stock_id"].map(normalize_code)
    out["stock_name"] = out["stock_name"].map(safe_str)
    out["market"] = market
    out["institutional_net_lots"] = maybe_lots(out["institutional_net_raw"], "shares")
    keep = ["date", "stock_id", "stock_name", "market", "institutional_net_lots"]
    out = out[keep].copy()
    out = out[out["stock_id"] != ""].drop_duplicates(["date", "stock_id"], keep="last")
    return out


def fetch_twse_institutional(date: str) -> pd.DataFrame:
    url = "https://www.twse.com.tw/rwd/zh/fund/T86"
    params = {"date": date, "selectType": "ALLBUT0999", "response": "json"}
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        payload = resp.json()
        return normalize_institutional(read_table_from_json(payload), date, "TWSE")
    except Exception as exc:
        print(f"WARNING: TWSE institutional fetch failed for {date}: {exc}")
        return pd.DataFrame()


def fetch_tpex_institutional(date: str) -> pd.DataFrame:
    candidates = [
        (
            "https://www.tpex.org.tw/www/zh-tw/insti/dailyTrade",
            {"date": roc_date(date), "type": "Daily", "response": "json"},
        ),
        (
            "https://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge_result.php",
            {"l": "zh-tw", "o": "json", "se": "EW", "t": "D", "d": roc_date(date), "s": "0,asc"},
        ),
    ]
    for url, params in candidates:
        try:
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            payload = resp.json()
            df = normalize_institutional(read_table_from_json(payload), date, "TPEX")
            if not df.empty:
                return df
        except Exception as exc:
            print(f"WARNING: TPEx institutional fetch failed for {date} via {url}: {exc}")
    return pd.DataFrame()


def institutional_path(date: str) -> Path:
    return INSTITUTIONAL_DIR / f"{date}.csv"


def load_or_fetch_institutional(date: str) -> pd.DataFrame:
    path = institutional_path(date)
    existing = read_csv(path, dtype=str)
    if not existing.empty:
        return existing
    frames = [fetch_twse_institutional(date), fetch_tpex_institutional(date)]
    out = pd.concat([df for df in frames if not df.empty], ignore_index=True, sort=False) if any(not df.empty for df in frames) else pd.DataFrame()
    if not out.empty:
        write_csv(out, path)
    return out


def normalize_broker_branch(df: pd.DataFrame, date: str, source_path: Path) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    out = df.copy()
    normalized_cols = {safe_str(c).lower(): c for c in out.columns}

    def pick(candidates: list[str]) -> str:
        for key in candidates:
            for lower, original in normalized_cols.items():
                if lower == key.lower() or key.lower() in lower:
                    return original
        return ""

    code_col = pick(["stock_id", "code", "stock_no", "證券代號", "股票代號"])
    name_col = pick(["stock_name", "name", "證券名稱", "股票名稱"])
    broker_col = pick(["broker_name", "branch_name", "securities_broker", "券商", "分點", "券商名稱"])
    buy_col = pick(["buy_lots", "buy_shares", "buy", "買進張數", "買進股數", "買進"])
    sell_col = pick(["sell_lots", "sell_shares", "sell", "賣出張數", "賣出股數", "賣出"])
    market_col = pick(["market", "市場"])

    required = [code_col, broker_col, buy_col, sell_col]
    if any(not col for col in required):
        print(f"WARNING: broker branch source missing required columns: {source_path}")
        return pd.DataFrame()

    normalized = pd.DataFrame()
    normalized["date"] = date
    normalized["stock_id"] = out[code_col].map(normalize_code)
    normalized["stock_name"] = out[name_col].map(safe_str) if name_col else ""
    normalized["broker_name"] = out[broker_col].map(safe_str)
    normalized["buy_lots"] = maybe_lots(out[buy_col], buy_col)
    normalized["sell_lots"] = maybe_lots(out[sell_col], sell_col)
    normalized["market"] = out[market_col].map(safe_str) if market_col else ""
    normalized["net_lots"] = normalized["buy_lots"] - normalized["sell_lots"]
    normalized = normalized[(normalized["stock_id"] != "") & (normalized["broker_name"] != "")]
    return normalized


def broker_branch_path(date: str) -> Path:
    return BROKER_BRANCH_DIR / f"{date}.csv"


def load_broker_branch(date: str) -> pd.DataFrame:
    path = broker_branch_path(date)
    return normalize_broker_branch(read_csv(path, dtype=str), date, path)


def load_eight_bank_patterns() -> pd.DataFrame:
    df = read_csv(CONFIG_EIGHT_BANKS, dtype=str)
    if df.empty:
        return pd.DataFrame(columns=["broker_family", "broker_name_pattern", "note"])
    return df.fillna("")


def is_eight_bank_broker(name: str, patterns: pd.DataFrame) -> bool:
    name = safe_str(name)
    if not name or patterns.empty:
        return False
    for _, row in patterns.iterrows():
        pattern = safe_str(row.get("broker_name_pattern", ""))
        if pattern and re.search(pattern, name):
            return True
    return False


def compute_daily_branch_flows(date: str, branch: pd.DataFrame, institutional: pd.DataFrame) -> pd.DataFrame:
    patterns = load_eight_bank_patterns()
    rows: list[dict[str, Any]] = []
    inst = institutional.copy()
    if not inst.empty:
        inst["stock_id"] = inst["stock_id"].map(normalize_code)
        inst = inst.drop_duplicates("stock_id", keep="last").set_index("stock_id")

    for stock_id, part in branch.groupby("stock_id"):
        part = part.copy()
        stock_name = safe_str(part["stock_name"].replace("", pd.NA).dropna().iloc[0]) if "stock_name" in part.columns and not part["stock_name"].replace("", pd.NA).dropna().empty else ""
        market = safe_str(part["market"].replace("", pd.NA).dropna().iloc[0]) if "market" in part.columns and not part["market"].replace("", pd.NA).dropna().empty else ""
        buy_sum = part[part["net_lots"] > 0].nlargest(TOP_N_BRANCHES, "net_lots")["net_lots"].sum()
        sell_abs = abs(part[part["net_lots"] < 0].nsmallest(TOP_N_BRANCHES, "net_lots")["net_lots"].sum())
        main_force = float(buy_sum - sell_abs)
        eight_bank = float(part[part["broker_name"].map(lambda x: is_eight_bank_broker(x, patterns))]["net_lots"].sum())
        inst_net = 0.0
        if not inst.empty and stock_id in inst.index:
            inst_net = number(inst.loc[stock_id].get("institutional_net_lots", 0))
            if not stock_name:
                stock_name = safe_str(inst.loc[stock_id].get("stock_name", ""))
            if not market:
                market = safe_str(inst.loc[stock_id].get("market", ""))
        adjusted = main_force - inst_net - eight_bank
        rows.append(
            {
                "date": date,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "market": market,
                "main_force_net_lots": round(main_force, 3),
                "institutional_net_lots": round(inst_net, 3),
                "eight_banks_net_lots": round(eight_bank, 3),
                "chip_flow_adjusted_net_lots": round(adjusted, 3),
                "latest_positive": adjusted > 0,
            }
        )
    return pd.DataFrame(rows)


def compute_streak(daily_frames: list[pd.DataFrame]) -> pd.DataFrame:
    frames = [df for df in daily_frames if not df.empty]
    if not frames:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    all_days = pd.concat(frames, ignore_index=True, sort=False)
    latest_date = str(all_days["date"].max())
    rows: list[dict[str, Any]] = []
    for stock_id, part in all_days.sort_values("date").groupby("stock_id"):
        part = part.sort_values("date").copy()
        streak = 0
        for _, row in part.iloc[::-1].iterrows():
            if bool(row.get("latest_positive", False)):
                streak += 1
            else:
                break
        latest = part.iloc[-1].to_dict()
        if latest.get("date") == latest_date and streak >= CONSECUTIVE_DAYS and bool(latest.get("latest_positive", False)):
            rows.append(
                {
                    "date": latest_date,
                    "category": CATEGORY,
                    "category_cn": CATEGORY_CN,
                    "stock_id": stock_id,
                    "stock_name": safe_str(latest.get("stock_name", "")),
                    "market": safe_str(latest.get("market", "")),
                    "main_force_net_lots": latest.get("main_force_net_lots", ""),
                    "institutional_net_lots": latest.get("institutional_net_lots", ""),
                    "eight_banks_net_lots": latest.get("eight_banks_net_lots", ""),
                    "chip_flow_adjusted_net_lots": latest.get("chip_flow_adjusted_net_lots", ""),
                    "positive_streak_days": streak,
                    "latest_positive": "True",
                    "signal_source_file": BROKER_BRANCH_DIR.as_posix(),
                    "note": (
                        f"主力買賣超前{TOP_N_BRANCHES}分點差額 - 三大法人買賣超 - "
                        f"八大行庫買賣超 > 0，且連續{streak}個交易日為正。"
                    ),
                }
            )
    out = pd.DataFrame(rows)
    for col in OUTPUT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    if not out.empty:
        out = out[OUTPUT_COLUMNS].sort_values(["positive_streak_days", "chip_flow_adjusted_net_lots"], ascending=[False, False])
    return out[OUTPUT_COLUMNS]


def build_markdown(df: pd.DataFrame, status: dict[str, Any]) -> str:
    lines = [
        "# 主力-三大法人-八大行庫連續轉強股",
        "",
        f"- generated_at: `{now_text()}`",
        f"- main_price_date: `{status.get('main_price_date', '')}`",
        f"- status: `{status.get('status', '')}`",
        f"- broker_branch_data_required: `True`",
        f"- broker_branch_source_dir: `{BROKER_BRANCH_DIR.as_posix()}`",
        "",
        "## 定義",
        "",
        f"- 主力買賣超：每檔股票當日買超前 {TOP_N_BRANCHES} 名券商分點合計 - 賣超前 {TOP_N_BRANCHES} 名券商分點合計。",
        "- 三大法人買賣超：TWSE / TPEx 官方三大法人個股買賣超。",
        "- 八大行庫買賣超：依 config/eight_public_bank_brokers.csv 對券商名稱做家族比對後加總。",
        f"- 入選條件：主力買賣超 - 三大法人買賣超 - 八大行庫買賣超 > 0，且最新資料日往前連續 {CONSECUTIVE_DAYS} 個交易日以上都為正。",
        "",
    ]
    if status.get("status") != "ready":
        lines.extend(
            [
                "## 今日狀態",
                "",
                "此分類今日未啟用，因為尚未取得可計算主力與八大行庫的券商分點買賣日報資料。",
                "ChatGPT 不得自行推算或編造此分類。",
                "",
            ]
        )
        return "\n".join(lines)
    lines.extend(["## 入選股票", ""])
    if df.empty:
        lines.append("今日無符合條件股票。")
        return "\n".join(lines)
    display = [
        "date",
        "stock_id",
        "stock_name",
        "main_force_net_lots",
        "institutional_net_lots",
        "eight_banks_net_lots",
        "chip_flow_adjusted_net_lots",
        "positive_streak_days",
        "note",
    ]
    lines.append("| " + " | ".join(display) + " |")
    lines.append("| " + " | ".join(["---"] * len(display)) + " |")
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(col, "")).replace("|", "/") for col in display) + " |")
    return "\n".join(lines)


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    INSTITUTIONAL_DIR.mkdir(parents=True, exist_ok=True)
    BROKER_BRANCH_DIR.mkdir(parents=True, exist_ok=True)

    dates = latest_trade_dates(limit=8)
    main_date = dates[-1] if dates else latest_price_date()
    status: dict[str, Any] = {
        "generated_at": now_text(),
        "main_price_date": main_date,
        "status": "not_ready",
        "reason": "",
        "trade_dates_checked": dates,
        "required_broker_branch_files": [broker_branch_path(d).as_posix() for d in dates[-CONSECUTIVE_DAYS:]],
        "institutional_source": "TWSE T86 + TPEx 3insti daily trade",
        "broker_branch_source": BROKER_BRANCH_DIR.as_posix(),
    }

    institutional_frames: list[pd.DataFrame] = []
    daily_frames: list[pd.DataFrame] = []
    missing_branch_dates: list[str] = []
    missing_institutional_dates: list[str] = []

    for date in dates:
        institutional = load_or_fetch_institutional(date)
        if not institutional.empty:
            institutional_frames.append(institutional)
        elif date in dates[-CONSECUTIVE_DAYS:]:
            missing_institutional_dates.append(date)
        branch = load_broker_branch(date)
        if branch.empty:
            if date in dates[-CONSECUTIVE_DAYS:]:
                missing_branch_dates.append(date)
            continue
        daily_frames.append(compute_daily_branch_flows(date, branch, institutional))

    if institutional_frames:
        institutional_all = pd.concat(institutional_frames, ignore_index=True, sort=False)
        latest_inst = institutional_all[institutional_all["date"] == str(institutional_all["date"].max())].copy()
        write_csv(latest_inst, INSTITUTIONAL_LATEST)
    else:
        write_csv(pd.DataFrame(columns=["date", "stock_id", "stock_name", "market", "institutional_net_lots"]), INSTITUTIONAL_LATEST)

    if missing_branch_dates or missing_institutional_dates:
        status["status"] = "disabled_missing_required_data"
        reasons = []
        if missing_branch_dates:
            reasons.append("missing broker branch trading daily report files")
        if missing_institutional_dates:
            reasons.append("missing official three-institution data")
        status["reason"] = "; ".join(reasons) + " for latest consecutive trading dates."
        status["missing_broker_branch_dates"] = missing_branch_dates
        status["missing_institutional_dates"] = missing_institutional_dates
        out = pd.DataFrame(columns=OUTPUT_COLUMNS)
    else:
        out = compute_streak(daily_frames)
        status["status"] = "ready"
        status["reason"] = "Broker branch data available; chip-flow streak computed."
        status["row_count"] = int(len(out))

    write_csv(out, OUTPUT_CSV)
    OUTPUT_MD.write_text(build_markdown(out, status), encoding="utf-8")
    STATUS_JSON.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    STATUS_MD.write_text(build_markdown(pd.DataFrame(columns=OUTPUT_COLUMNS), status), encoding="utf-8")

    if status["status"] == "ready" and not out.empty:
        append_update_csv(out, HISTORY_CSV, ["date", "category", "stock_id"], ["date", "stock_id"])

    print(f"[OK] saved {OUTPUT_CSV} rows={len(out)} status={status['status']}")
    print(f"[OK] saved {STATUS_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
