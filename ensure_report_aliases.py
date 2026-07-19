from __future__ import annotations

from pathlib import Path
import shutil
import json
import re
import csv
from datetime import datetime
from zoneinfo import ZoneInfo


LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")
PUBLISHED_DAILY_MARKET_DIR = LATEST_DIR / "published_reports" / "daily_market"

CHINESE_SUMMARY_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
CHINESE_FULL_MD = LATEST_DIR / "完整候選股清單_完整版.md"
PUBLISHED_SUMMARY_PDF_STEM = "每日全市場候選股監測報告_精華版"
PUBLISHED_FULL_PDF_STEM = "完整候選股清單_完整版"

ALIAS_SUMMARY_MD = LATEST_DIR / "daily_market_summary_latest.md"
ALIAS_SUMMARY_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
ALIAS_FULL_MD = LATEST_DIR / "daily_market_full_latest.md"
ALIAS_FULL_PDF = LATEST_DIR / "daily_market_full_latest.pdf"

MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"
MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"

GITHUB_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"

LEGACY_HISTORY_REFERENCE_FRAGMENTS = (
    "_每日全市場候選股監測報告_精華版.",
    "_完整候選股清單_完整版.",
    "_完整候選股清單_完整版表格.",
)


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def raw_url(path: Path) -> str:
    return GITHUB_RAW_PREFIX + str(path).replace("\\", "/")


def published_summary_pdf(main_date: str) -> Path:
    return PUBLISHED_DAILY_MARKET_DIR / f"{PUBLISHED_SUMMARY_PDF_STEM}_{main_date}.pdf"


def published_full_pdf(main_date: str) -> Path:
    return PUBLISHED_DAILY_MARKET_DIR / f"{PUBLISHED_FULL_PDF_STEM}_{main_date}.pdf"


def contains_legacy_history_reference(text: str) -> bool:
    normalized = text.replace("\\", "/")
    if "output/history/reports/" not in normalized:
        return False
    return any(fragment in normalized for fragment in LEGACY_HISTORY_REFERENCE_FRAGMENTS)


def strip_history_url_sections(text: str) -> str:
    markers = (
        "## 英文 alias raw URLs",
        "## English alias raw URLs",
        "## Latest alias raw URLs",
        "## 中文檔名 raw URLs",
        "## Canonical history raw URLs",
    )
    positions = [text.index(marker) for marker in markers if marker in text]
    base = text if not positions else text[: min(positions)]
    base = base.replace("5. 日期版英文 MD / PDF", "5. canonical history MD / PDF")
    base = base.replace(
        "6. 中文檔名僅作人類閱讀備援",
        "6. 中文 PDF 檔名僅保留於 published human-delivery surface",
    )
    return base.rstrip()


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

    return ""


DATE_STAMPED_README_RE = re.compile(r"READ_ME_FIRST_DAILY_REPORT_\d{8}\.txt$")


def remove_stale_date_stamped_readmes(directory: Path, keep_date: str) -> None:
    if not directory.exists():
        return

    keep_name = f"READ_ME_FIRST_DAILY_REPORT_{keep_date}.txt"
    for path in directory.glob("READ_ME_FIRST_DAILY_REPORT_*.txt"):
        if path.name == keep_name:
            continue
        if DATE_STAMPED_README_RE.fullmatch(path.name):
            path.unlink()
            print(f"[OK] removed stale date-stamped daily README: {path}")


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
    published_summary = published_summary_pdf(main_date)
    published_full = published_full_pdf(main_date)

    alias_block = f"""

## Latest alias raw URLs

這些固定英文檔名供 ChatGPT / raw 讀取工具使用。

- latest summary md: {raw_url(ALIAS_SUMMARY_MD)}
- latest full md: {raw_url(ALIAS_FULL_MD)}
- latest summary pdf: {raw_url(ALIAS_SUMMARY_PDF)}
- latest full pdf: {raw_url(ALIAS_FULL_PDF)}

## Canonical history raw URLs

- history summary md: {raw_url(history_summary_md)}
- history full md: {raw_url(history_full_md)}
- history summary pdf: {raw_url(history_summary_pdf)}
- history full pdf: {raw_url(history_full_pdf)}

## Published human delivery PDFs

- published summary pdf: {raw_url(published_summary)}
- published full pdf: {raw_url(published_full)}
"""

    old = ""
    if MANIFEST_MD.exists():
        old = MANIFEST_MD.read_text(encoding="utf-8", errors="ignore")

    old = strip_history_url_sections(old)

    MANIFEST_MD.write_text(old + alias_block + "\n", encoding="utf-8")

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
            "history_path_contract": "canonical_daily_market_history_only",
            "recommended_read_order": [
                ALIAS_SUMMARY_MD.as_posix(),
                ALIAS_FULL_MD.as_posix(),
                ALIAS_SUMMARY_PDF.as_posix(),
                ALIAS_FULL_PDF.as_posix(),
                history_summary_md.as_posix(),
                history_full_md.as_posix(),
                history_summary_pdf.as_posix(),
                history_full_pdf.as_posix(),
                published_summary.as_posix(),
                published_full.as_posix(),
            ],
            "latest_summary_pdf": published_summary.as_posix(),
            "latest_full_pdf": published_full.as_posix(),
            "latest_summary_alias_md": ALIAS_SUMMARY_MD.as_posix(),
            "latest_summary_alias_pdf": ALIAS_SUMMARY_PDF.as_posix(),
            "latest_full_alias_md": ALIAS_FULL_MD.as_posix(),
            "latest_full_alias_pdf": ALIAS_FULL_PDF.as_posix(),
            "history_summary_md": history_summary_md.as_posix(),
            "history_summary_pdf": history_summary_pdf.as_posix(),
            "history_full_md": history_full_md.as_posix(),
            "history_full_pdf": history_full_pdf.as_posix(),
            "history_summary_alias_md": history_summary_md.as_posix(),
            "history_summary_alias_pdf": history_summary_pdf.as_posix(),
            "history_full_alias_md": history_full_md.as_posix(),
            "history_full_alias_pdf": history_full_pdf.as_posix(),
            "summary_alias_md_raw_url": raw_url(ALIAS_SUMMARY_MD),
            "summary_alias_pdf_raw_url": raw_url(ALIAS_SUMMARY_PDF),
            "full_alias_md_raw_url": raw_url(ALIAS_FULL_MD),
            "full_alias_pdf_raw_url": raw_url(ALIAS_FULL_PDF),
            "history_summary_alias_md_raw_url": raw_url(history_summary_md),
            "history_summary_alias_pdf_raw_url": raw_url(history_summary_pdf),
            "history_full_alias_md_raw_url": raw_url(history_full_md),
            "history_full_alias_pdf_raw_url": raw_url(history_full_pdf),
            "summary_md_raw_url": raw_url(history_summary_md),
            "summary_pdf_raw_url": raw_url(history_summary_pdf),
            "full_md_raw_url": raw_url(history_full_md),
            "full_pdf_raw_url": raw_url(history_full_pdf),
        }
    )

    manifest_json_text = json.dumps(manifest_data, ensure_ascii=False, indent=2)
    manifest_md_text = MANIFEST_MD.read_text(encoding="utf-8")
    if contains_legacy_history_reference(manifest_json_text) or contains_legacy_history_reference(
        manifest_md_text
    ):
        raise RuntimeError("report manifest still references retired Chinese history aliases")

    MANIFEST_JSON.write_text(
        manifest_json_text,
        encoding="utf-8",
    )
    print(f"[OK] updated {MANIFEST_MD}")
    print(f"[OK] updated {MANIFEST_JSON}")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    main_date = detect_main_date()
    if not main_date:
        raise RuntimeError(
            "main_date is required from freshness, manifest, or candidate artifacts; "
            "wall-clock date fallback is forbidden"
        )
    print(f"[INFO] main_date={main_date}")
    remove_stale_date_stamped_readmes(LATEST_DIR, main_date)
    remove_stale_date_stamped_readmes(DOCS_LATEST_DIR, main_date)

    ok = True

    ok &= copy_if_exists(CHINESE_SUMMARY_MD, ALIAS_SUMMARY_MD)
    ok &= copy_if_exists(CHINESE_FULL_MD, ALIAS_FULL_MD)
    ok &= copy_if_exists(published_summary_pdf(main_date), ALIAS_SUMMARY_PDF)
    ok &= copy_if_exists(published_full_pdf(main_date), ALIAS_FULL_PDF)

    history_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    history_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    history_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    history_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    ok &= copy_if_exists(ALIAS_SUMMARY_MD, history_summary_md)
    ok &= copy_if_exists(ALIAS_SUMMARY_PDF, history_summary_pdf)
    ok &= copy_if_exists(ALIAS_FULL_MD, history_full_md)
    ok &= copy_if_exists(ALIAS_FULL_PDF, history_full_pdf)

    if not ok:
        print("[ERROR] canonical report aliases are incomplete because source files are missing")
        return 1

    append_alias_to_manifest(main_date)

    print("[OK] report aliases created")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
