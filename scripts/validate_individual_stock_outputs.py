from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
INDIVIDUAL_STOCK_REPORTS_DIR = LATEST_DIR / "individual_stock_reports"
DOCS_INDIVIDUAL_STOCK_REPORTS_DIR = DOCS_LATEST_DIR / "individual_stock_reports"
PACKET_DIR = INDIVIDUAL_STOCK_REPORTS_DIR / "chatgpt_packets"
PRICE_WINDOW_DIR = INDIVIDUAL_STOCK_REPORTS_DIR / "price_windows"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
STOCK_PRICE_HISTORY_DIR = Path("data/stock_price_history")
OFFICIAL_TDCC_CONTRACT_JSON = LATEST_DIR / "tdcc_weekly_candidate_report_validation_latest.json"
OFFICIAL_TDCC_DATE_SOURCE = "report_ready_csv_signal_date"

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


def read_official_tdcc_signal_date(path: Path | None = None) -> str:
    contract_path = path or OFFICIAL_TDCC_CONTRACT_JSON
    if not contract_path.exists():
        raise SystemExit(f"ERROR: Missing official TDCC date contract: {contract_path}")
    try:
        payload = json.loads(contract_path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERROR: Cannot read official TDCC date contract {contract_path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise SystemExit(f"ERROR: Official TDCC date contract must be a JSON object: {contract_path}")
    status = str(payload.get("status", "")).strip()
    if status != "pass":
        raise SystemExit(
            f"ERROR: Official TDCC date contract status must be pass, got {status or 'missing'}: {contract_path}"
        )
    date_contract = payload.get("date_contract")
    if not isinstance(date_contract, dict):
        raise SystemExit(f"ERROR: Official TDCC date contract missing date_contract object: {contract_path}")
    date_source = str(date_contract.get("date_source", "")).strip()
    if date_source != OFFICIAL_TDCC_DATE_SOURCE:
        raise SystemExit(
            f"ERROR: Official TDCC date_source must be {OFFICIAL_TDCC_DATE_SOURCE}, got {date_source or 'missing'}: "
            f"{contract_path}"
        )
    signal_date = str(payload.get("signal_date", "")).strip()
    if not re.fullmatch(r"20[0-9]{6}", signal_date):
        raise SystemExit(f"ERROR: Official TDCC date contract missing valid signal_date: {contract_path}")
    return signal_date


def read_packet_metadata(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    metadata: dict[str, str] = {}
    in_metadata = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip() == "## Metadata":
            in_metadata = True
            continue
        if in_metadata and line.startswith("## "):
            break
        if not in_metadata:
            continue
        match = re.match(r"-\s+([A-Za-z0-9_]+):\s*(.*)$", line.strip())
        if match:
            metadata[match.group(1)] = match.group(2).strip()
    return metadata


def validate_tdcc_packet_freshness(
    stock_id: str,
    packet_path: Path,
    index_row: dict[str, str],
    official_tdcc_signal_date: str,
) -> list[str]:
    errors: list[str] = []
    metadata = read_packet_metadata(packet_path)
    if not metadata:
        return [f"{stock_id}: packet missing or Metadata unreadable: {packet_path}"]

    packet_official_date = normalize_date(metadata.get("official_tdcc_signal_date"))
    packet_latest_date = normalize_date(metadata.get("latest_tdcc_date"))
    packet_history_status = metadata.get("tdcc_history_status", "")
    packet_freshness_status = metadata.get("tdcc_freshness_status", "")
    try:
        packet_tdcc_rows = int(metadata.get("tdcc_rows", ""))
    except ValueError:
        packet_tdcc_rows = -1

    if packet_official_date != official_tdcc_signal_date:
        errors.append(
            f"{stock_id}: packet official_tdcc_signal_date mismatch: expected {official_tdcc_signal_date}, "
            f"got {packet_official_date or 'missing'} ({packet_path})"
        )
    if packet_tdcc_rows < 0:
        errors.append(f"{stock_id}: packet tdcc_rows missing or invalid: {packet_path}")
    if packet_tdcc_rows == 0:
        expected_latest_date = ""
        expected_history_status = "tdcc_missing"
        expected_freshness_status = "tdcc_missing"
    else:
        expected_latest_date = official_tdcc_signal_date
        expected_history_status = "tdcc_history_ready" if packet_tdcc_rows >= 8 else "insufficient_tdcc_history"
        expected_freshness_status = "tdcc_window_fresh"
    if packet_latest_date != expected_latest_date:
        errors.append(
            f"{stock_id}: packet latest_tdcc_date mismatch: expected {expected_latest_date or 'blank for tdcc_missing'}, "
            f"got {packet_latest_date or 'blank'} ({packet_path})"
        )
    if packet_history_status != expected_history_status:
        errors.append(
            f"{stock_id}: packet tdcc_history_status mismatch: expected {expected_history_status}, "
            f"got {packet_history_status or 'missing'} ({packet_path})"
        )
    if packet_freshness_status != expected_freshness_status:
        errors.append(
            f"{stock_id}: packet tdcc_freshness_status mismatch: expected {expected_freshness_status}, "
            f"got {packet_freshness_status or 'missing'} ({packet_path})"
        )

    if index_row:
        index_checks = {
            "official_tdcc_signal_date": official_tdcc_signal_date,
            "latest_tdcc_date": expected_latest_date,
            "tdcc_history_status": expected_history_status,
            "tdcc_freshness_status": expected_freshness_status,
        }
        for field, expected in index_checks.items():
            actual = str(index_row.get(field, "")).strip()
            if field.endswith("_date"):
                actual = normalize_date(actual)
            if actual != expected:
                errors.append(
                    f"{stock_id}: packet index {field} mismatch: expected {expected}, got {actual or 'missing'}"
                )
        index_rows = str(index_row.get("tdcc_rows", "")).strip()
        if index_rows != str(packet_tdcc_rows):
            errors.append(
                f"{stock_id}: packet index tdcc_rows mismatch: expected packet value {packet_tdcc_rows}, "
                f"got {index_rows or 'missing'}"
            )
    return errors


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
    if has_mojibake(text):
        errors.append(f"{stock_id}: packet contains mojibake/private-use text: {path}")
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


def validate_stock(
    stock_id: str,
    main_price_date: str,
    official_tdcc_signal_date: str,
    index_row: dict[str, str],
    validate_current_price: bool = True,
) -> list[str]:
    errors: list[str] = []
    checks = [
        (
            "output packet latest_price_date",
            PACKET_DIR / f"{stock_id}_packet_latest.md",
            latest_price_date_from_packet,
        ),
        (
            "output 180d txt price window",
            PRICE_WINDOW_DIR / f"{stock_id}_price_window_180_latest.txt",
            latest_price_date_from_txt_window,
        ),
        (
            "output 180d csv price window",
            PRICE_WINDOW_DIR / f"{stock_id}_price_window_180_latest.csv",
            latest_price_date_from_csv_window,
        ),
    ]

    if validate_current_price:
        for label, path, reader in checks:
            actual = reader(path)
            if not actual:
                errors.append(f"{stock_id}: {label} missing or unreadable: {path}")
            elif actual != main_price_date:
                errors.append(
                    f"{stock_id}: {label} date mismatch: expected {main_price_date}, got {actual} ({path})"
                )

    packet_path = PACKET_DIR / f"{stock_id}_packet_latest.md"
    errors.extend(
        validate_tdcc_packet_freshness(stock_id, packet_path, index_row, official_tdcc_signal_date)
    )

    packet_paths = [
        PACKET_DIR / f"{stock_id}_packet_latest.md",
    ]
    for path in packet_paths:
        errors.extend(validate_action_display_packet(stock_id, path))

    report_paths = [
        INDIVIDUAL_STOCK_REPORTS_DIR / f"{stock_id}_latest.md",
        DOCS_INDIVIDUAL_STOCK_REPORTS_DIR / f"{stock_id}_latest.md",
        INDIVIDUAL_STOCK_REPORTS_DIR / f"{stock_id}_latest.pdf",
        DOCS_INDIVIDUAL_STOCK_REPORTS_DIR / f"{stock_id}_latest.pdf",
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
    official_tdcc_signal_date = read_official_tdcc_signal_date()
    main_price_date = read_main_price_date()
    stock_ids = [str(x).strip() for x in args.stock_id if str(x).strip()]
    index_path = INDIVIDUAL_STOCK_REPORTS_DIR / "individual_stock_chatgpt_packet_index.csv"
    index_rows_by_stock: dict[str, dict[str, str]] = {}
    duplicate_index_stock_ids: set[str] = set()
    if index_path.exists():
        with index_path.open("r", encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                stock_id = str(row.get("stock_id", "")).strip()
                if stock_id:
                    if stock_id in index_rows_by_stock:
                        duplicate_index_stock_ids.add(stock_id)
                    index_rows_by_stock[stock_id] = row
    elif args.all:
        raise SystemExit(f"ERROR: Missing packet index: {index_path}")
    if args.all:
        stock_ids.extend(index_rows_by_stock)
        stock_ids.extend(
            path.name.removesuffix("_packet_latest.md")
            for path in PACKET_DIR.glob("*_packet_latest.md")
        )
    stock_ids = sorted(set(x for x in stock_ids if x))
    if not stock_ids:
        raise SystemExit("ERROR: Provide --stock-id or --all.")

    errors: list[str] = []
    for stock_id in sorted(duplicate_index_stock_ids):
        errors.append(f"{stock_id}: duplicate packet index row: {index_path}")
    non_current_price_count = 0
    for stock_id in stock_ids:
        index_row = index_rows_by_stock.get(stock_id, {})
        if args.all and not index_row:
            errors.append(f"{stock_id}: packet missing index row: {index_path}")
        validate_current_price = not index_row or normalize_date(index_row.get("latest_price_date")) == main_price_date
        if not validate_current_price:
            non_current_price_count += 1
        errors.extend(
            validate_stock(
                stock_id,
                main_price_date,
                official_tdcc_signal_date,
                index_row,
                validate_current_price=validate_current_price,
            )
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    history_status_counts = Counter(
        str(index_rows_by_stock.get(stock_id, {}).get("tdcc_history_status", "")).strip() or "blank"
        for stock_id in stock_ids
    )
    freshness_status_counts = Counter(
        str(index_rows_by_stock.get(stock_id, {}).get("tdcc_freshness_status", "")).strip() or "blank"
        for stock_id in stock_ids
    )
    latest_tdcc_date_counts = Counter(
        normalize_date(index_rows_by_stock.get(stock_id, {}).get("latest_tdcc_date")) or "blank"
        for stock_id in stock_ids
    )
    print(
        f"Individual stock outputs validated against main_price_date={main_price_date}; "
        f"official_tdcc_signal_date={official_tdcc_signal_date}; validated={len(stock_ids)} "
        f"non_current_price_packets_checked_for_tdcc={non_current_price_count}"
    )
    print("tdcc_history_status_distribution=" + ",".join(f"{key}:{history_status_counts[key]}" for key in sorted(history_status_counts)))
    print("tdcc_freshness_status_distribution=" + ",".join(f"{key}:{freshness_status_counts[key]}" for key in sorted(freshness_status_counts)))
    print("latest_tdcc_date_distribution=" + ",".join(f"{key}:{latest_tdcc_date_counts[key]}" for key in sorted(latest_tdcc_date_counts)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
