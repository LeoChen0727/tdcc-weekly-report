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

MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"

README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"

DAILY_SUMMARY_MD = LATEST_DIR / "daily_market_summary_latest.md"
DAILY_FULL_MD = LATEST_DIR / "daily_market_full_latest.md"
DAILY_SUMMARY_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
DAILY_FULL_PDF = LATEST_DIR / "daily_market_full_latest.pdf"

CHINESE_SUMMARY_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
CHINESE_SUMMARY_PDF = LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf"
CHINESE_FULL_MD = LATEST_DIR / "完整候選股清單_完整版.md"
CHINESE_FULL_PDF = LATEST_DIR / "完整候選股清單_完整版表格.pdf"

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
CHART_MANIFEST_CSV = LATEST_DIR / "chart_manifest.csv"
CONTACT_SHEET_MANIFEST_CSV = LATEST_DIR / "contact_sheet_manifest.csv"

OFFICIAL_PRICE_FETCH_MD = LATEST_DIR / "official_price_fetch_latest.md"
OFFICIAL_PRICE_FETCH_JSON = LATEST_DIR / "official_price_fetch_latest.json"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


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


def safe_read_text(path: Path) -> str:
    if not path.exists():
        return ""

    for enc in ["utf-8", "utf-8-sig", "cp950"]:
        try:
            return path.read_text(encoding=enc)
        except Exception:
            pass

    return ""


def raw_url(path: Path) -> str:
    return f"{REPO_RAW_PREFIX}/{path.as_posix()}"


def file_status(path: Path) -> str:
    return "exists" if path.exists() else "missing"


def extract_from_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        return {}

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

    patterns = {
        "main_price_date": [
            r"主資料日期[：:\s`]*([0-9/\-]{8,10})",
            r"main_price_date[：:\s`]*([0-9/\-]{8,10})",
        ],
        "report_ready": [
            r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)",
            r"report_ready[：:\s`]*(True|False|true|false)",
        ],
    }

    for key, pats in patterns.items():
        for pat in pats:
            m = re.search(pat, text)
            if m:
                if key == "report_ready":
                    result[key] = m.group(1)
                else:
                    result[key] = normalize_date(m.group(1))
                break

    return result


def extract_manifest_info() -> dict[str, Any]:
    data = extract_from_json(MANIFEST_JSON)

    result = {
        "main_price_date": "",
        "report_ready": "",
        "summary_md": "",
        "full_md": "",
        "summary_pdf": "",
        "full_pdf": "",
    }

    if data:
        for key in ["main_price_date", "price_date", "date", "data_date"]:
            if key in data:
                result["main_price_date"] = normalize_date(data.get(key, ""))
                break

        for key in ["report_ready", "ready", "can_generate_report"]:
            if key in data:
                result["report_ready"] = str(data.get(key, ""))
                break

        # 嘗試支援不同 manifest 欄位命名
        for key in ["summary_md", "daily_market_summary_md", "summary_report_md"]:
            if key in data:
                result["summary_md"] = str(data.get(key, ""))
                break

        for key in ["full_md", "daily_market_full_md", "full_report_md"]:
            if key in data:
                result["full_md"] = str(data.get(key, ""))
                break

        for key in ["summary_pdf", "daily_market_summary_pdf", "summary_report_pdf"]:
            if key in data:
                result["summary_pdf"] = str(data.get(key, ""))
                break

        for key in ["full_pdf", "daily_market_full_pdf", "full_report_pdf"]:
            if key in data:
                result["full_pdf"] = str(data.get(key, ""))
                break

    # 不管 manifest 怎麼寫，固定 alias 一定補上
    if not result["summary_md"]:
        result["summary_md"] = DAILY_SUMMARY_MD.as_posix()

    if not result["full_md"]:
        result["full_md"] = DAILY_FULL_MD.as_posix()

    if not result["summary_pdf"]:
        result["summary_pdf"] = DAILY_SUMMARY_PDF.as_posix()

    if not result["full_pdf"]:
        result["full_pdf"] = DAILY_FULL_PDF.as_posix()

    if not result["main_price_date"]:
        freshness = extract_data_freshness()
        result["main_price_date"] = freshness.get("main_price_date", "")

    if not result["report_ready"]:
        freshness = extract_data_freshness()
        result["report_ready"] = freshness.get("report_ready", "")

    return result


def build_readme() -> str:
    manifest = extract_manifest_info()
    freshness = extract_data_freshness()

    main_price_date = manifest.get("main_price_date") or freshness.get("main_price_date", "")
    report_ready = manifest.get("report_ready") or freshness.get("report_ready", "")

    lines: list[str] = []

    lines.append("DAILY MARKET REPORT READ ME FIRST")
    lines.append("")
    lines.append(f"generated_at: {now_taipei()}")
    lines.append(f"repo: LeoChen0727/tdcc-weekly-report")
    lines.append(f"main_price_date: {main_price_date}")
    lines.append(f"report_ready: {report_ready}")
    lines.append("")
    lines.append("IMPORTANT RULES FOR CHATGPT READER")
    lines.append("")
    lines.append("1. This file is the first file to read before producing the daily Taiwan stock candidate report.")
    lines.append("2. If this file says report_ready=True and main_price_date is the target report date, GitHub has produced the official report.")
    lines.append("3. If the report files below cannot be read, say the reading tool failed. Do NOT say GitHub data is not updated.")
    lines.append("4. Do NOT reuse older reports such as 20260521 to recreate a newer report such as 20260522.")
    lines.append("5. Prefer English alias filenames first. Avoid relying on Chinese filenames when the reader tool has cache issues.")
    lines.append("6. If MD files fail, try PDF files. If both fail, ask the user to upload the MD/PDF files.")
    lines.append("")
    lines.append("PRIMARY FILES TO READ IN ORDER")
    lines.append("")

    primary_files = [
        ("report_manifest_latest.md", MANIFEST_MD),
        ("report_manifest_latest.json", MANIFEST_JSON),
        ("data_freshness_latest.md", DATA_FRESHNESS_MD),
        ("daily_market_summary_latest.md", DAILY_SUMMARY_MD),
        ("daily_market_full_latest.md", DAILY_FULL_MD),
        ("daily_market_summary_latest.pdf", DAILY_SUMMARY_PDF),
        ("daily_market_full_latest.pdf", DAILY_FULL_PDF),
    ]

    for label, path in primary_files:
        lines.append(f"- {label}")
        lines.append(f"  path: {path.as_posix()}")
        lines.append(f"  status: {file_status(path)}")
        lines.append(f"  raw_url: {raw_url(path)}")

    lines.append("")
    lines.append("SECONDARY DATA FILES")
    lines.append("")

    secondary_files = [
        ("all_candidates_latest.csv", ALL_CANDIDATES_CSV),
        ("all_candidates_latest.xlsx", ALL_CANDIDATES_XLSX),
        ("chart_manifest.csv", CHART_MANIFEST_CSV),
        ("contact_sheet_manifest.csv", CONTACT_SHEET_MANIFEST_CSV),
        ("official_price_fetch_latest.md", OFFICIAL_PRICE_FETCH_MD),
        ("official_price_fetch_latest.json", OFFICIAL_PRICE_FETCH_JSON),
        ("warrant_flow_latest.csv", WARRANT_FLOW_CSV),
        ("stock_monitor_latest.md", STOCK_MONITOR_MD),
    ]

    for label, path in secondary_files:
        lines.append(f"- {label}")
        lines.append(f"  path: {path.as_posix()}")
        lines.append(f"  status: {file_status(path)}")
        lines.append(f"  raw_url: {raw_url(path)}")

    lines.append("")
    lines.append("CHINESE DISPLAY FILES")
    lines.append("")

    chinese_files = [
        ("每日全市場候選股監測報告_精華版.md", CHINESE_SUMMARY_MD),
        ("每日全市場候選股監測報告_精華版.pdf", CHINESE_SUMMARY_PDF),
        ("完整候選股清單_完整版.md", CHINESE_FULL_MD),
        ("完整候選股清單_完整版表格.pdf", CHINESE_FULL_PDF),
    ]

    for label, path in chinese_files:
        lines.append(f"- {label}")
        lines.append(f"  path: {path.as_posix()}")
        lines.append(f"  status: {file_status(path)}")
        lines.append(f"  raw_url: {raw_url(path)}")

    lines.append("")
    lines.append("DATE CHECK")
    lines.append("")
    lines.append(f"main_price_date: {main_price_date}")
    lines.append(f"report_ready: {report_ready}")
    lines.append(f"all_candidates_date: {freshness.get('all_candidates_date', '')}")
    lines.append(f"official_price_fetch_date: {freshness.get('official_price_fetch_date', '')}")
    lines.append(f"stock_monitor_date: {freshness.get('stock_monitor_date', '')}")
    lines.append(f"warrant_flow_date: {freshness.get('warrant_flow_date', '')}")
    lines.append("")
    lines.append("EXPECTED BEHAVIOR")
    lines.append("")
    lines.append("If main_price_date matches the requested date and report_ready=True:")
    lines.append("- Produce the report from daily_market_summary_latest.md and daily_market_full_latest.md when readable.")
    lines.append("- If these files cannot be read due to Cache miss, report a tool-reading failure.")
    lines.append("- Do not claim the GitHub report has not been produced.")
    lines.append("- Do not use stale older files to recreate today's report.")
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
