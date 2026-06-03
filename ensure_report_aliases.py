from __future__ import annotations

from pathlib import Path
import shutil
import json
import re
import csv
from datetime import datetime
from zoneinfo import ZoneInfo


LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

CHINESE_SUMMARY_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
CHINESE_SUMMARY_PDF = LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf"
CHINESE_FULL_MD = LATEST_DIR / "完整候選股清單_完整版.md"
CHINESE_FULL_PDF = LATEST_DIR / "完整候選股清單_完整版表格.pdf"

ALIAS_SUMMARY_MD = LATEST_DIR / "daily_market_summary_latest.md"
ALIAS_SUMMARY_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
ALIAS_FULL_MD = LATEST_DIR / "daily_market_full_latest.md"
ALIAS_FULL_PDF = LATEST_DIR / "daily_market_full_latest.pdf"

MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"
MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"

GITHUB_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def raw_url(path: Path) -> str:
    return GITHUB_RAW_PREFIX + str(path).replace("\\", "/")


def normalize_date(value) -> str:
    digits = re.sub(r"[^0-9]", "", str(value or "").strip())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def first_csv_row(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            return next(reader, {}) or {}
    except Exception:
        return {}


def max_csv_date(path: Path, columns: list[str]) -> str:
    if not path.exists():
        return ""
    dates: list[str] = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for col in columns:
                    date = normalize_date(row.get(col, ""))
                    if date:
                        dates.append(date)
                        break
    except Exception:
        return ""
    return max(dates) if dates else ""


def detect_main_date() -> str:
    freshness_row = first_csv_row(DATA_FRESHNESS_CSV)
    for col in ("main_price_date", "all_candidates_date", "stock_monitor_price_date"):
        date = normalize_date(freshness_row.get(col, ""))
        if date:
            return date

    if MANIFEST_JSON.exists():
        try:
            manifest_data = json.loads(MANIFEST_JSON.read_text(encoding="utf-8"))
        except Exception:
            manifest_data = {}
        date = normalize_date(manifest_data.get("main_price_date", ""))
        if date:
            return date

    candidate_date = max_csv_date(ALL_CANDIDATES_CSV, ["main_price_date", "signal_date", "date"])
    if candidate_date:
        return candidate_date

    candidates = [
        LATEST_DIR / "data_freshness_latest.md",
        MANIFEST_MD,
        LATEST_DIR / "stock_monitor_latest.md",
        LATEST_DIR / "all_candidates_latest.md",
    ]

    for path in candidates:
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        matches = re.findall(r"20\d{6}", text)

        if matches:
            return max(matches)

    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")


def copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        print(f"[WARN] source missing: {src}")
        return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"[OK] copied {src} -> {dst}")
    return True


def append_alias_to_manifest(main_date: str) -> None:
    history_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    history_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    history_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    history_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    alias_block = f"""

## English alias raw URLs

這些英文檔名是給 ChatGPT / raw 讀取工具優先使用，避免中文檔名 Cache miss。

- latest summary md: {raw_url(ALIAS_SUMMARY_MD)}
- latest full md: {raw_url(ALIAS_FULL_MD)}
- latest summary pdf: {raw_url(ALIAS_SUMMARY_PDF)}
- latest full pdf: {raw_url(ALIAS_FULL_PDF)}
- history summary md: {raw_url(history_summary_md)}
- history full md: {raw_url(history_full_md)}
- history summary pdf: {raw_url(history_summary_pdf)}
- history full pdf: {raw_url(history_full_pdf)}
"""

    old = ""
    if MANIFEST_MD.exists():
        old = MANIFEST_MD.read_text(encoding="utf-8", errors="ignore")

    marker = "## English alias raw URLs"
    if marker in old:
        old = old.split(marker)[0].rstrip()

    MANIFEST_MD.write_text(old + alias_block + "\n", encoding="utf-8")
    print(f"[OK] updated {MANIFEST_MD}")

    manifest_data = {}
    if MANIFEST_JSON.exists():
        try:
            manifest_data = json.loads(MANIFEST_JSON.read_text(encoding="utf-8"))
        except Exception:
            manifest_data = {}

    manifest_data.update(
        {
            "alias_generated_at": now_taipei(),
            "main_price_date": main_date,
            "latest_summary_alias_md": str(ALIAS_SUMMARY_MD),
            "latest_summary_alias_pdf": str(ALIAS_SUMMARY_PDF),
            "latest_full_alias_md": str(ALIAS_FULL_MD),
            "latest_full_alias_pdf": str(ALIAS_FULL_PDF),
            "history_summary_alias_md": str(history_summary_md),
            "history_summary_alias_pdf": str(history_summary_pdf),
            "history_full_alias_md": str(history_full_md),
            "history_full_alias_pdf": str(history_full_pdf),
            "summary_alias_md_raw_url": raw_url(ALIAS_SUMMARY_MD),
            "summary_alias_pdf_raw_url": raw_url(ALIAS_SUMMARY_PDF),
            "full_alias_md_raw_url": raw_url(ALIAS_FULL_MD),
            "full_alias_pdf_raw_url": raw_url(ALIAS_FULL_PDF),
            "history_summary_alias_md_raw_url": raw_url(history_summary_md),
            "history_summary_alias_pdf_raw_url": raw_url(history_summary_pdf),
            "history_full_alias_md_raw_url": raw_url(history_full_md),
            "history_full_alias_pdf_raw_url": raw_url(history_full_pdf),
        }
    )

    MANIFEST_JSON.write_text(
        json.dumps(manifest_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[OK] updated {MANIFEST_JSON}")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    main_date = detect_main_date()
    print(f"[INFO] main_date={main_date}")

    ok = True

    ok &= copy_if_exists(CHINESE_SUMMARY_MD, ALIAS_SUMMARY_MD)
    ok &= copy_if_exists(CHINESE_SUMMARY_PDF, ALIAS_SUMMARY_PDF)
    ok &= copy_if_exists(CHINESE_FULL_MD, ALIAS_FULL_MD)
    ok &= copy_if_exists(CHINESE_FULL_PDF, ALIAS_FULL_PDF)

    history_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    history_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    history_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    history_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    ok &= copy_if_exists(ALIAS_SUMMARY_MD, history_summary_md)
    ok &= copy_if_exists(ALIAS_SUMMARY_PDF, history_summary_pdf)
    ok &= copy_if_exists(ALIAS_FULL_MD, history_full_md)
    ok &= copy_if_exists(ALIAS_FULL_PDF, history_full_pdf)

    append_alias_to_manifest(main_date)

    if not ok:
        print("[WARN] some alias files were not created because source files were missing")
        return 0

    print("[OK] report aliases created")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
