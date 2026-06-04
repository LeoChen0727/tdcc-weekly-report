from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
STOCK_PRICE_HISTORY_DIR = Path("data/stock_price_history")

ACTION_DISPLAY_REQUIRED_FIELDS = [
    "action_rating_display_zh",
    "action_summary_zh",
    "entry_strategy_zh",
    "position_sizing_zh",
    "add_position_strategy_zh",
    "take_profit_strategy_zh",
    "risk_control_zh",
    "post_entry_watch_zh",
    "final_decision_zh",
    "score_interpretation_zh",
    "model_category_display_zh",
]

FORBIDDEN_REPORT_TOKENS = [
    "ACTION_DECISION",
    "action_rating",
    "starter_position",
    "scale_in",
    "buy_now",
    "wait_pullback",
    "wait_reclaim",
    "decision_score",
    "daily_candidate_decision",
    "model_slug",
    "raw field",
    "raw field name",
    "already_priced_in=True",
    "insufficient_sample",
    "report_ready",
    "\u7a0b\u5f0f\u7aef\u6b04\u4f4d",
]

MOJIBAKE_MARKER_CODEPOINTS = {
    0xFFFD,
    0x5697, 0x876F, 0x7508, 0x9788, 0x96FF, 0x6498, 0x95AE, 0x6468,
    0x7485, 0x61BF, 0x981D, 0x8751, 0x875A, 0x876C, 0x9908, 0x922D, 0x929D,
}


def has_mojibake(text: str) -> bool:
    if "?" * 4 in text:
        return True
    for ch in text:
        codepoint = ord(ch)
        if codepoint in MOJIBAKE_MARKER_CODEPOINTS:
            return True
        if 0xE000 <= codepoint <= 0xF8FF:
            return True
    return False


def normalize_date(value: object) -> str:
    text = str(value or "").strip()
    digits = re.sub(r"\D", "", text)
    if len(digits) >= 8:
        return digits[:8]
    return ""


def read_main_price_date() -> str:
    if DATA_FRESHNESS_CSV.exists():
        with DATA_FRESHNESS_CSV.open("r", encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.DictReader(fh))
        if rows:
            for key in [
                "main_price_date",
                "actual_stock_price_history_date",
                "stock_monitor_price_date",
                "all_candidates_date",
            ]:
                value = normalize_date(rows[0].get(key))
                if value:
                    return value

    readme = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("main_price_date="):
                value = normalize_date(line.split("=", 1)[1])
                if value:
                    return value

    raise SystemExit("ERROR: Cannot resolve main_price_date from latest outputs.")


def latest_price_date_from_packet(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"latest_price_date:\s*([0-9]{8})", text)
    return match.group(1) if match else ""


def latest_price_date_from_txt_window(path: Path) -> str:
    if not path.exists():
        return ""
    latest = ""
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = re.match(r"PRICE_WINDOW_180_ROW_\d+=([0-9]{8}),", line.strip())
        if match:
            latest = match.group(1)
    return latest


def latest_price_date_from_csv_window(path: Path) -> str:
    if not path.exists():
        return ""
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        date_col = None
        latest = ""
        for row in reader:
            if date_col is None:
                for key in ["date", "trade_date", "signal_date"]:
                    if key in row:
                        date_col = key
                        break
            if date_col:
                value = normalize_date(row.get(date_col))
                if value:
                    latest = value
        return latest


def latest_price_date_from_stock_history(stock_id: str) -> str:
    path = STOCK_PRICE_HISTORY_DIR / f"{stock_id}_stock_price_history.csv"
    if not path.exists():
        path = STOCK_PRICE_HISTORY_DIR / f"{stock_id}.csv"
    return latest_price_date_from_csv_window(path)


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency failure should be visible in CI.
        raise RuntimeError(f"pypdf unavailable while validating {path}: {exc}") from exc
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def validate_action_display_packet(stock_id: str, path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return errors
    text = path.read_text(encoding="utf-8", errors="replace")
    if "## ACTION_DISPLAY" not in text:
        errors.append(f"{stock_id}: packet missing ACTION_DISPLAY section: {path}")
    for field in ACTION_DISPLAY_REQUIRED_FIELDS:
        if f"- {field}:" not in text:
            errors.append(f"{stock_id}: packet ACTION_DISPLAY missing {field}: {path}")
    return errors


def validate_report_display_text(stock_id: str, path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return errors
    if path.suffix.lower() == ".pdf":
        try:
            text = extract_pdf_text(path)
        except Exception as exc:
            return [f"{stock_id}: cannot extract PDF text from {path}: {exc}"]
    else:
        text = path.read_text(encoding="utf-8", errors="replace")
    for token in FORBIDDEN_REPORT_TOKENS:
        if token and token in text:
            errors.append(f"{stock_id}: formal report exposes internal token {token!r}: {path}")
    if has_mojibake(text):
        errors.append(f"{stock_id}: formal report contains mojibake/private-use text: {path}")
    return errors


def validate_stock(stock_id: str, main_price_date: str) -> list[str]:
    errors: list[str] = []
    checks = [
        (
            "output packet latest_price_date",
            LATEST_DIR / "individual_stock_chatgpt_packets" / f"{stock_id}_packet_latest.md",
            latest_price_date_from_packet,
        ),
        (
            "docs packet latest_price_date",
            DOCS_LATEST_DIR / "individual_stock_chatgpt_packets" / f"{stock_id}_packet_latest.md",
            latest_price_date_from_packet,
        ),
        (
            "output 180d txt price window",
            LATEST_DIR / "individual_stock_price_windows" / f"{stock_id}_price_window_180_latest.txt",
            latest_price_date_from_txt_window,
        ),
        (
            "docs 180d txt price window",
            DOCS_LATEST_DIR / "individual_stock_price_windows" / f"{stock_id}_price_window_180_latest.txt",
            latest_price_date_from_txt_window,
        ),
        (
            "output 180d csv price window",
            LATEST_DIR / "individual_stock_price_windows" / f"{stock_id}_price_window_180_latest.csv",
            latest_price_date_from_csv_window,
        ),
        (
            "docs 180d csv price window",
            DOCS_LATEST_DIR / "individual_stock_price_windows" / f"{stock_id}_price_window_180_latest.csv",
            latest_price_date_from_csv_window,
        ),
    ]

    for label, path, reader in checks:
        actual = reader(path)
        if not actual:
            errors.append(f"{stock_id}: {label} missing or unreadable: {path}")
        elif actual != main_price_date:
            errors.append(
                f"{stock_id}: {label} date mismatch: expected {main_price_date}, got {actual} ({path})"
            )

    packet_paths = [
        LATEST_DIR / "individual_stock_chatgpt_packets" / f"{stock_id}_packet_latest.md",
        DOCS_LATEST_DIR / "individual_stock_chatgpt_packets" / f"{stock_id}_packet_latest.md",
    ]
    for path in packet_paths:
        errors.extend(validate_action_display_packet(stock_id, path))

    report_paths = [
        LATEST_DIR / "individual_stock_reports" / f"{stock_id}_latest.md",
        DOCS_LATEST_DIR / "individual_stock_reports" / f"{stock_id}_latest.md",
        LATEST_DIR / "individual_stock_reports" / f"{stock_id}_latest.pdf",
        DOCS_LATEST_DIR / "individual_stock_reports" / f"{stock_id}_latest.pdf",
    ]
    for path in report_paths:
        errors.extend(validate_report_display_text(stock_id, path))

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate per-stock ChatGPT packet, price windows, and investor-facing report display text."
    )
    parser.add_argument("--stock-id", action="append", default=[], help="Stock id. May be repeated.")
    parser.add_argument("--all", action="store_true", help="Validate every stock id in the packet index.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    main_price_date = read_main_price_date()
    stock_ids = [str(x).strip() for x in args.stock_id if str(x).strip()]
    if args.all:
        index_path = LATEST_DIR / "individual_stock_chatgpt_packet_index.csv"
        if not index_path.exists():
            raise SystemExit(f"ERROR: Missing packet index: {index_path}")
        with index_path.open("r", encoding="utf-8-sig", newline="") as fh:
            stock_ids.extend(str(row.get("stock_id", "")).strip() for row in csv.DictReader(fh))
    stock_ids = sorted(set(x for x in stock_ids if x))
    if not stock_ids:
        raise SystemExit("ERROR: Provide --stock-id or --all.")

    skipped_non_current: list[str] = []
    if args.all and not args.stock_id:
        current_stock_ids: list[str] = []
        for stock_id in stock_ids:
            history_latest = latest_price_date_from_stock_history(stock_id)
            if history_latest == main_price_date:
                current_stock_ids.append(stock_id)
            else:
                skipped_non_current.append(stock_id)
        stock_ids = current_stock_ids

    errors: list[str] = []
    for stock_id in stock_ids:
        errors.extend(validate_stock(stock_id, main_price_date))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Individual stock outputs validated against main_price_date={main_price_date}; "
        f"validated={len(stock_ids)} skipped_non_current={len(skipped_non_current)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
