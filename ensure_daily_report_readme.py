from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re
from typing import Any

import pandas as pd


REPO_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
REPORT_MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
PACKET_MANIFEST_JSON = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"

PACKET_LATEST = LATEST_DIR / "CHATGPT_DAILY_REPORT_PACKET.txt"

SUMMARY_LATEST_MD = LATEST_DIR / "daily_market_summary_latest.md"
FULL_LATEST_MD = LATEST_DIR / "daily_market_full_latest.md"
SUMMARY_LATEST_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
FULL_LATEST_PDF = LATEST_DIR / "daily_market_full_latest.pdf"

REPORT_MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"
REPORT_MANIFEST_JSON_PATH = LATEST_DIR / "report_manifest_latest.json"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
CHART_MANIFEST_CSV = LATEST_DIR / "chart_manifest.csv"
CONTACT_SHEET_MANIFEST_CSV = LATEST_DIR / "contact_sheet_manifest.csv"
OFFICIAL_PRICE_FETCH_MD = LATEST_DIR / "official_price_fetch_latest.md"
OFFICIAL_PRICE_FETCH_JSON = LATEST_DIR / "official_price_fetch_latest.json"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def cache_bust() -> str:
    return now_taipei().strftime("%Y%m%d%H%M%S")


def normalize_date(value: Any) -> str:
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass

    text = str(value).strip()
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    return ""


def raw_url(path: Path, bust: bool = False) -> str:
    url = f"{REPO_RAW_PREFIX}/{path.as_posix()}"
    if bust:
        url = f"{url}?v={cache_bust()}"
    return url


def file_status(path: Path) -> str:
    return "exists" if path.exists() else "missing"


def safe_read_text(path: Path) -> str:
    if not path.exists():
        return ""

    for enc in ["utf-8", "utf-8-sig", "cp950"]:
        try:
            return path.read_text(encoding=enc)
        except Exception:
            pass

    return ""


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    return {}


def extract_data_freshness() -> dict[str, str]:
    result = {
        "main_price_date": "",
        "report_ready": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "stock_monitor_date": "",
        "warrant_flow_date": "",
    }

    if DATA_FRESHNESS_CSV.exists():
        try:
            df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str)
            if not df.empty:
                row = df.iloc[0].to_dict()
                result["main_price_date"] = normalize_date(row.get("main_price_date", ""))
                result["report_ready"] = str(row.get("report_ready", "")).strip()
                result["all_candidates_date"] = normalize_date(row.get("all_candidates_date", ""))
                result["official_price_fetch_date"] = normalize_date(row.get("official_price_fetch_date", ""))
                result["stock_monitor_date"] = normalize_date(row.get("stock_monitor_price_date", ""))
                result["warrant_flow_date"] = normalize_date(row.get("warrant_flow_date", ""))
                return result
        except Exception:
            pass

    text = safe_read_text(DATA_FRESHNESS_MD)

    m = re.search(r"主資料日期[：:\s`]*([0-9/\-]{8,10})", text)
    if m:
        result["main_price_date"] = normalize_date(m.group(1))

    m = re.search(r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)", text)
    if m:
        result["report_ready"] = m.group(1)

    return result


def get_main_meta() -> dict[str, str]:
    freshness = extract_data_freshness()
    manifest = read_json(REPORT_MANIFEST_JSON)

    main_price_date = (
        normalize_date(manifest.get("main_price_date", ""))
        or normalize_date(manifest.get("price_date", ""))
        or normalize_date(manifest.get("date", ""))
        or freshness.get("main_price_date", "")
    )

    report_ready = (
        str(manifest.get("report_ready", "")).strip()
        or str(manifest.get("ready", "")).strip()
        or freshness.get("report_ready", "")
    )

    return {
        "main_price_date": main_price_date,
        "report_ready": report_ready,
        "all_candidates_date": freshness.get("all_candidates_date", ""),
        "official_price_fetch_date": freshness.get("official_price_fetch_date", ""),
        "stock_monitor_date": freshness.get("stock_monitor_date", ""),
        "warrant_flow_date": freshness.get("warrant_flow_date", ""),
    }


def build_file_block(label: str, path: Path) -> list[str]:
    return [
        f"- {label}",
        f"  path: {path.as_posix()}",
        f"  status: {file_status(path)}",
        f"  raw_url: {raw_url(path)}",
        f"  raw_url_cache_bust: {raw_url(path, bust=True)}",
    ]


def build_readme() -> str:
    meta = get_main_meta()
    main_date = meta.get("main_price_date", "")
    report_ready = meta.get("report_ready", "")

    dated_packet = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"
    dated_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    dated_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    dated_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    dated_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    packet_manifest = read_json(PACKET_MANIFEST_JSON)

    lines: list[str] = []

    lines.append("DAILY MARKET REPORT READ ME FIRST")
    lines.append("")
    lines.append(f"generated_at: {now_text()}")
    lines.append("repo: LeoChen0727/tdcc-weekly-report")
    lines.append(f"main_price_date: {main_date}")
    lines.append(f"report_ready: {report_ready}")
    lines.append(f"all_candidates_date: {meta.get('all_candidates_date', '')}")
    lines.append(f"official_price_fetch_date: {meta.get('official_price_fetch_date', '')}")
    lines.append(f"stock_monitor_date: {meta.get('stock_monitor_date', '')}")
    lines.append(f"warrant_flow_date: {meta.get('warrant_flow_date', '')}")
    lines.append("")
    lines.append("IMPORTANT")
    lines.append("")
    lines.append("This file is only the entry point.")
    lines.append("The most stable source is the dated CHATGPT_DAILY_REPORT_PACKET because it directly embeds the report content.")
    lines.append("Do not depend only on latest files because latest URLs are overwritten every trading day and may hit cache problems.")
    lines.append("")
    lines.append("READING PRIORITY")
    lines.append("")
    lines.append("1. Dated CHATGPT packet")
    lines.append("2. Latest CHATGPT packet")
    lines.append("3. Dated summary/full MD")
    lines.append("4. Dated summary/full PDF")
    lines.append("5. Latest English alias MD/PDF")
    lines.append("6. Manifest/freshness files only for status checking")
    lines.append("7. Chinese filenames are human-display backup only")
    lines.append("")
    lines.append("RULES FOR CHATGPT READER")
    lines.append("")
    lines.append("1. If main_price_date matches the requested date and report_ready=True, GitHub has produced the official report.")
    lines.append("2. If the packet or report files cannot be read, say the reading tool failed. Do NOT say GitHub data is not updated.")
    lines.append("3. Do NOT use older reports to recreate a newer report.")
    lines.append("4. Do NOT turn Cache miss into a market-data conclusion.")
    lines.append("5. If all GitHub reading fails, ask the user to paste CHATGPT_DAILY_REPORT_PACKET.txt.")
    lines.append("")
    lines.append("PRIMARY DATED PACKET")
    lines.append("")
    lines.extend(build_file_block("dated_chatgpt_packet", dated_packet))
    lines.append("")
    lines.append("LATEST PACKET")
    lines.append("")
    lines.extend(build_file_block("latest_chatgpt_packet", PACKET_LATEST))
    lines.append("")
    lines.append("DATED REPORT FILES")
    lines.append("")
    for label, path in [
        ("dated_summary_md", dated_summary_md),
        ("dated_full_md", dated_full_md),
        ("dated_summary_pdf", dated_summary_pdf),
        ("dated_full_pdf", dated_full_pdf),
    ]:
        lines.extend(build_file_block(label, path))
    lines.append("")
    lines.append("LATEST ENGLISH ALIAS FILES")
    lines.append("")
    for label, path in [
        ("latest_summary_md", SUMMARY_LATEST_MD),
        ("latest_full_md", FULL_LATEST_MD),
        ("latest_summary_pdf", SUMMARY_LATEST_PDF),
        ("latest_full_pdf", FULL_LATEST_PDF),
    ]:
        lines.extend(build_file_block(label, path))
    lines.append("")
    lines.append("STATUS FILES")
    lines.append("")
    for label, path in [
        ("report_manifest_latest_md", REPORT_MANIFEST_MD),
        ("report_manifest_latest_json", REPORT_MANIFEST_JSON_PATH),
        ("data_freshness_latest_md", DATA_FRESHNESS_MD),
        ("data_freshness_latest_csv", DATA_FRESHNESS_CSV),
        ("packet_manifest_json", PACKET_MANIFEST_JSON),
    ]:
        lines.extend(build_file_block(label, path))
    lines.append("")
    lines.append("SECONDARY DATA FILES")
    lines.append("")
    for label, path in [
        ("all_candidates_latest_csv", ALL_CANDIDATES_CSV),
        ("all_candidates_latest_xlsx", ALL_CANDIDATES_XLSX),
        ("chart_manifest_csv", CHART_MANIFEST_CSV),
        ("contact_sheet_manifest_csv", CONTACT_SHEET_MANIFEST_CSV),
        ("official_price_fetch_latest_md", OFFICIAL_PRICE_FETCH_MD),
        ("official_price_fetch_latest_json", OFFICIAL_PRICE_FETCH_JSON),
        ("warrant_flow_latest_csv", WARRANT_FLOW_CSV),
        ("stock_monitor_latest_md", STOCK_MONITOR_MD),
    ]:
        lines.extend(build_file_block(label, path))
    lines.append("")
    lines.append("PACKET MANIFEST SNAPSHOT")
    lines.append("")
    if packet_manifest:
        for key, value in packet_manifest.items():
            lines.append(f"{key}: {value}")
    else:
        lines.append("packet_manifest: missing")
    lines.append("")
    lines.append("EXPECTED RESPONSE IF TOOL FAILS")
    lines.append("")
    lines.append("讀取工具失敗，目前無法取得 GitHub 已產出的報告內容；請直接貼上 CHATGPT_DAILY_REPORT_PACKET.txt。")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    content = build_readme()
    README_TXT.write_text(content, encoding="utf-8")
    print(f"Saved: {README_TXT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
