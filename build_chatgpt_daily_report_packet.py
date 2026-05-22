from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re
import shutil
from typing import Any

import pandas as pd


REPO_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
REPORT_MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
REPORT_MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"

SUMMARY_LATEST_MD = LATEST_DIR / "daily_market_summary_latest.md"
FULL_LATEST_MD = LATEST_DIR / "daily_market_full_latest.md"
SUMMARY_LATEST_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
FULL_LATEST_PDF = LATEST_DIR / "daily_market_full_latest.pdf"

SUMMARY_CN_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
FULL_CN_MD = LATEST_DIR / "完整候選股清單_完整版.md"
SUMMARY_CN_PDF = LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf"
FULL_CN_PDF = LATEST_DIR / "完整候選股清單_完整版表格.pdf"

PACKET_LATEST = LATEST_DIR / "CHATGPT_DAILY_REPORT_PACKET.txt"
PACKET_MANIFEST = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"


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


def safe_read_text(path: Path) -> str:
    if not path.exists():
        return ""

    for enc in ["utf-8", "utf-8-sig", "cp950"]:
        try:
            return path.read_text(encoding=enc)
        except Exception:
            pass

    return ""


def raw_url(path: Path, with_cache_bust: bool = False) -> str:
    url = f"{REPO_RAW_PREFIX}/{path.as_posix()}"
    if with_cache_bust:
        url = f"{url}?v={cache_bust()}"
    return url


def safe_copy(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return True


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


def extract_data_freshness() -> dict[str, Any]:
    result = {
        "main_price_date": "",
        "report_ready": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "stock_monitor_date": "",
        "warrant_flow_date": "",
        "report_ready_note": "",
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
                result["report_ready_note"] = str(row.get("report_ready_note", "")).strip()
                return result
        except Exception:
            pass

    text = safe_read_text(DATA_FRESHNESS_MD)

    date_patterns = [
        r"主資料日期[：:\s`]*([0-9/\-]{8,10})",
        r"main_price_date[：:\s`]*([0-9/\-]{8,10})",
    ]

    ready_patterns = [
        r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)",
        r"report_ready[：:\s`]*(True|False|true|false)",
    ]

    for pat in date_patterns:
        m = re.search(pat, text)
        if m:
            result["main_price_date"] = normalize_date(m.group(1))
            break

    for pat in ready_patterns:
        m = re.search(pat, text)
        if m:
            result["report_ready"] = m.group(1)
            break

    return result


def extract_main_meta() -> dict[str, Any]:
    freshness = extract_data_freshness()
    manifest = read_json(REPORT_MANIFEST_JSON)

    main_date = (
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
        "main_price_date": main_date,
        "report_ready": report_ready,
        "freshness": freshness,
        "manifest": manifest,
    }


def ensure_dated_artifacts(main_date: str) -> dict[str, Path]:
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    dated_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    dated_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    dated_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    dated_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    dated_summary_cn_md = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.md"
    dated_full_cn_md = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版.md"
    dated_summary_cn_pdf = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.pdf"
    dated_full_cn_pdf = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版表格.pdf"

    safe_copy(SUMMARY_LATEST_MD, dated_summary_md)
    safe_copy(FULL_LATEST_MD, dated_full_md)
    safe_copy(SUMMARY_LATEST_PDF, dated_summary_pdf)
    safe_copy(FULL_LATEST_PDF, dated_full_pdf)

    safe_copy(SUMMARY_CN_MD, dated_summary_cn_md)
    safe_copy(FULL_CN_MD, dated_full_cn_md)
    safe_copy(SUMMARY_CN_PDF, dated_summary_cn_pdf)
    safe_copy(FULL_CN_PDF, dated_full_cn_pdf)

    return {
        "dated_summary_md": dated_summary_md,
        "dated_full_md": dated_full_md,
        "dated_summary_pdf": dated_summary_pdf,
        "dated_full_pdf": dated_full_pdf,
        "dated_summary_cn_md": dated_summary_cn_md,
        "dated_full_cn_md": dated_full_cn_md,
        "dated_summary_cn_pdf": dated_summary_cn_pdf,
        "dated_full_cn_pdf": dated_full_cn_pdf,
    }


def build_packet_text(main_date: str, report_ready: str, paths: dict[str, Path], meta: dict[str, Any]) -> str:
    summary_text = safe_read_text(SUMMARY_LATEST_MD)
    full_text = safe_read_text(FULL_LATEST_MD)

    freshness = meta.get("freshness", {})

    lines: list[str] = []

    lines.append("CHATGPT DAILY REPORT PACKET")
    lines.append("")
    lines.append(f"generated_at: {now_text()}")
    lines.append("repo: LeoChen0727/tdcc-weekly-report")
    lines.append(f"main_price_date: {main_date}")
    lines.append(f"report_ready: {report_ready}")
    lines.append(f"all_candidates_date: {freshness.get('all_candidates_date', '')}")
    lines.append(f"official_price_fetch_date: {freshness.get('official_price_fetch_date', '')}")
    lines.append(f"stock_monitor_date: {freshness.get('stock_monitor_date', '')}")
    lines.append(f"warrant_flow_date: {freshness.get('warrant_flow_date', '')}")
    lines.append("")
    lines.append("PURPOSE")
    lines.append("")
    lines.append("This file directly embeds the daily market report content.")
    lines.append("If ChatGPT cannot read GitHub raw/latest/MD/PDF files, paste this packet into the daily report conversation.")
    lines.append("Do not recreate this report from stale older files.")
    lines.append("")
    lines.append("PRIMARY DATED RAW URLS")
    lines.append("")
    for key in ["dated_summary_md", "dated_full_md", "dated_summary_pdf", "dated_full_pdf"]:
        path = paths[key]
        lines.append(f"- {key}: {raw_url(path)}")
        lines.append(f"- {key}_cache_bust: {raw_url(path, with_cache_bust=True)}")
    lines.append("")
    lines.append("LATEST RAW URLS")
    lines.append("")
    for label, path in [
        ("latest_summary_md", SUMMARY_LATEST_MD),
        ("latest_full_md", FULL_LATEST_MD),
        ("latest_summary_pdf", SUMMARY_LATEST_PDF),
        ("latest_full_pdf", FULL_LATEST_PDF),
        ("latest_readme", LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"),
        ("latest_packet", PACKET_LATEST),
    ]:
        lines.append(f"- {label}: {raw_url(path)}")
        lines.append(f"- {label}_cache_bust: {raw_url(path, with_cache_bust=True)}")
    lines.append("")
    lines.append("READING RULES")
    lines.append("")
    lines.append("1. Prefer this packet first because it already contains the report content.")
    lines.append("2. If reading GitHub raw fails, say tool reading failed. Do not say GitHub data is not updated.")
    lines.append("3. Do not use older dates to recreate today's report.")
    lines.append("4. If this packet is pasted by the user, use the embedded content below as source of truth.")
    lines.append("")
    lines.append("=" * 80)
    lines.append("EMBEDDED SUMMARY REPORT")
    lines.append("=" * 80)
    lines.append("")
    if summary_text.strip():
        lines.append(summary_text)
    else:
        lines.append("[daily_market_summary_latest.md missing or empty]")
    lines.append("")
    lines.append("=" * 80)
    lines.append("EMBEDDED FULL REPORT")
    lines.append("=" * 80)
    lines.append("")
    if full_text.strip():
        lines.append(full_text)
    else:
        lines.append("[daily_market_full_latest.md missing or empty]")
    lines.append("")
    lines.append("=" * 80)
    lines.append("END OF PACKET")
    lines.append("=" * 80)
    lines.append("")

    return "\n".join(lines)


def write_packet_manifest(main_date: str, report_ready: str, paths: dict[str, Path]) -> None:
    manifest = {
        "generated_at": now_text(),
        "main_price_date": main_date,
        "report_ready": report_ready,
        "latest_packet_path": PACKET_LATEST.as_posix(),
        "latest_packet_raw_url": raw_url(PACKET_LATEST),
        "latest_packet_raw_url_cache_bust": raw_url(PACKET_LATEST, with_cache_bust=True),
        "history_packet_path": (HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt").as_posix(),
        "history_packet_raw_url": raw_url(HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"),
        "history_packet_raw_url_cache_bust": raw_url(HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt", with_cache_bust=True),
        "dated_summary_md_raw_url": raw_url(paths["dated_summary_md"]),
        "dated_full_md_raw_url": raw_url(paths["dated_full_md"]),
        "dated_summary_pdf_raw_url": raw_url(paths["dated_summary_pdf"]),
        "dated_full_pdf_raw_url": raw_url(paths["dated_full_pdf"]),
    }

    PACKET_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    meta = extract_main_meta()
    main_date = meta.get("main_price_date", "")

    if not main_date:
        main_date = now_taipei().strftime("%Y%m%d")

    report_ready = str(meta.get("report_ready", "")).strip()
    if not report_ready:
        report_ready = "False"

    paths = ensure_dated_artifacts(main_date)

    packet_text = build_packet_text(
        main_date=main_date,
        report_ready=report_ready,
        paths=paths,
        meta=meta,
    )

    PACKET_LATEST.write_text(packet_text, encoding="utf-8")

    history_packet = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"
    history_packet.write_text(packet_text, encoding="utf-8")

    write_packet_manifest(main_date, report_ready, paths)

    print(f"Saved: {PACKET_LATEST}")
    print(f"Saved: {history_packet}")
    print(f"Saved: {PACKET_MANIFEST}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
