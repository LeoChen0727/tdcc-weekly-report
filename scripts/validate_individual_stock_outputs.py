from __future__ import annotations

import argparse
import csv
import math
import re
from collections import Counter
from pathlib import Path

import pandas as pd

from individual_tdcc_dataset_consumer import (
    IndividualTdccDatasetContract,
    StockTdccAssessment,
    load_individual_tdcc_dataset_contract,
    prepare_and_validate_stock_tdcc_history,
)

LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
INDIVIDUAL_STOCK_REPORTS_DIR = LATEST_DIR / "individual_stock_reports"
DOCS_INDIVIDUAL_STOCK_REPORTS_DIR = DOCS_LATEST_DIR / "individual_stock_reports"
PACKET_DIR = INDIVIDUAL_STOCK_REPORTS_DIR / "chatgpt_packets"
PRICE_WINDOW_DIR = INDIVIDUAL_STOCK_REPORTS_DIR / "price_windows"
TDCC_WINDOW_DIR = INDIVIDUAL_STOCK_REPORTS_DIR / "tdcc_windows"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
STOCK_PRICE_HISTORY_DIR = Path("data/stock_price_history")
TDCC_HISTORY_DIR = Path("data/tdcc_stock_history")
OFFICIAL_TDCC_DATASET_MANIFEST_JSON = LATEST_DIR / "tdcc_dataset_manifest_latest.json"
OFFICIAL_DAILY_PRICE_CSV = LATEST_DIR / "official_daily_price_latest.csv"
CURRENT_UNIVERSE_SOURCE = "official_daily_price_latest_main_price_date"
LISTING_STATUS_SOURCE_STATUS = "formal_listing_status_source_unavailable"
TDCC_WINDOW_VALUE_FIELDS = (
    "as_of_date",
    *(
        field
        for threshold in (400, 600, 800, 1000)
        for field in (
            f"over_{threshold}_ratio",
            f"over_{threshold}_change_1w",
            f"over_{threshold}_change_2w",
            f"over_{threshold}_change_3w",
        )
    ),
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "four_thresholds_sync_up",
    "retail_ratio",
    "total_shareholders",
)

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
    try:
        return load_individual_tdcc_dataset_contract(path or OFFICIAL_TDCC_DATASET_MANIFEST_JSON).signal_date
    except RuntimeError as exc:
        raise SystemExit(f"ERROR: Cannot load canonical TDCC dataset contract: {exc}") from exc


def read_current_main_price_universe(main_price_date: str, path: Path | None = None) -> set[str]:
    universe_path = path or OFFICIAL_DAILY_PRICE_CSV
    if not universe_path.exists():
        raise SystemExit(f"ERROR: Missing current main-price universe artifact: {universe_path}")
    with universe_path.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        raise SystemExit(f"ERROR: Current main-price universe artifact is empty: {universe_path}")
    universe_dates = {normalize_date(row.get("date") or row.get("trade_date")) for row in rows}
    universe_dates.discard("")
    if universe_dates != {main_price_date}:
        raise SystemExit(
            f"ERROR: Current main-price universe date mismatch: expected only {main_price_date}, "
            f"got {sorted(universe_dates) or ['missing']} ({universe_path})"
        )
    stock_ids = {
        re.sub(r"[^0-9A-Z]", "", str(row.get("stock_id") or row.get("code") or "").upper())
        for row in rows
    }
    return {stock_id for stock_id in stock_ids if re.fullmatch(r"[0-9]{4,6}", stock_id)}


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


def read_tdcc_source_stats(stock_id: str, path: Path | None = None) -> tuple[int, str]:
    source_path = path or TDCC_HISTORY_DIR / f"{stock_id}.csv"
    if not source_path.exists():
        return 0, ""
    with source_path.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    latest_date = ""
    for row in rows:
        value = normalize_date(row.get("as_of_date") or row.get("date"))
        if value:
            latest_date = max(latest_date, value)
    return len(rows), latest_date


def read_tdcc_source_frame(stock_id: str, path: Path | None = None) -> pd.DataFrame:
    source_path = path or TDCC_HISTORY_DIR / f"{stock_id}.csv"
    if not source_path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(source_path, dtype=str, encoding="utf-8-sig").fillna("")
    except Exception as exc:
        raise RuntimeError(f"{stock_id}: cannot read TDCC materialized history {source_path}: {exc}") from exc


def validate_tdcc_packet_freshness(
    stock_id: str,
    packet_path: Path,
    index_row: dict[str, str],
    official_tdcc_signal_date: str,
    main_price_date: str = "",
    is_current_main_price_universe: bool = True,
    source_tdcc_rows: int | None = None,
    source_latest_tdcc_date: str | None = None,
    source_tdcc_dataset_id: str = "",
    source_tdcc_continuity_status: str = "",
    source_tdcc_missing_official_dates: tuple[str, ...] = (),
) -> list[str]:
    errors: list[str] = []
    metadata = read_packet_metadata(packet_path)
    if not metadata:
        return [f"{stock_id}: packet missing or Metadata unreadable: {packet_path}"]

    packet_official_date = normalize_date(metadata.get("official_tdcc_signal_date"))
    packet_latest_date = normalize_date(metadata.get("latest_tdcc_date"))
    packet_history_status = metadata.get("tdcc_history_status", "")
    packet_freshness_status = metadata.get("tdcc_freshness_status", "")
    packet_main_price_date = normalize_date(metadata.get("current_main_price_date"))
    packet_universe_status = metadata.get("current_main_price_universe_status", "")
    packet_universe_source = metadata.get("current_main_price_universe_source", "")
    packet_listing_source_status = metadata.get("listing_status_source_status", "")
    packet_dataset_id = metadata.get("source_tdcc_dataset_id", "")
    packet_continuity_status = metadata.get("tdcc_continuity_status", "")
    packet_missing_dates = tuple(
        value for value in metadata.get("tdcc_missing_official_dates", "").split("|") if value
    )
    try:
        packet_tdcc_rows = int(metadata.get("tdcc_rows", ""))
    except ValueError:
        packet_tdcc_rows = -1

    expected_tdcc_rows = packet_tdcc_rows if source_tdcc_rows is None else source_tdcc_rows
    expected_source_latest_date = (
        packet_latest_date if source_latest_tdcc_date is None else normalize_date(source_latest_tdcc_date)
    )
    if source_tdcc_rows is not None and packet_tdcc_rows != source_tdcc_rows:
        errors.append(
            f"{stock_id}: packet tdcc_rows source mismatch: expected {source_tdcc_rows}, "
            f"got {packet_tdcc_rows} ({packet_path})"
        )
    if source_latest_tdcc_date is not None and packet_latest_date != expected_source_latest_date:
        errors.append(
            f"{stock_id}: packet latest_tdcc_date source mismatch: expected "
            f"{expected_source_latest_date or 'blank'}, got {packet_latest_date or 'blank'} ({packet_path})"
        )

    if packet_official_date != official_tdcc_signal_date:
        errors.append(
            f"{stock_id}: packet official_tdcc_signal_date mismatch: expected {official_tdcc_signal_date}, "
            f"got {packet_official_date or 'missing'} ({packet_path})"
        )
    if source_tdcc_dataset_id and packet_dataset_id != source_tdcc_dataset_id:
        errors.append(
            f"{stock_id}: packet source_tdcc_dataset_id mismatch: expected {source_tdcc_dataset_id}, "
            f"got {packet_dataset_id or 'missing'} ({packet_path})"
        )
    if source_tdcc_continuity_status and packet_continuity_status != source_tdcc_continuity_status:
        errors.append(
            f"{stock_id}: packet tdcc_continuity_status mismatch: expected {source_tdcc_continuity_status}, "
            f"got {packet_continuity_status or 'missing'} ({packet_path})"
        )
    if source_tdcc_continuity_status and packet_missing_dates != source_tdcc_missing_official_dates:
        errors.append(
            f"{stock_id}: packet tdcc_missing_official_dates mismatch: expected "
            f"{'|'.join(source_tdcc_missing_official_dates) or 'blank'}, "
            f"got {'|'.join(packet_missing_dates) or 'blank'} ({packet_path})"
        )
    if packet_tdcc_rows < 0:
        errors.append(f"{stock_id}: packet tdcc_rows missing or invalid: {packet_path}")
    expected_universe_status = "current" if is_current_main_price_universe else "historical_only_noncurrent"
    if main_price_date and packet_main_price_date != main_price_date:
        errors.append(
            f"{stock_id}: packet current_main_price_date mismatch: expected {main_price_date}, "
            f"got {packet_main_price_date or 'missing'} ({packet_path})"
        )
    if packet_universe_status != expected_universe_status:
        errors.append(
            f"{stock_id}: packet current_main_price_universe_status mismatch: expected {expected_universe_status}, "
            f"got {packet_universe_status or 'missing'} ({packet_path})"
        )
    if packet_universe_source != CURRENT_UNIVERSE_SOURCE:
        errors.append(
            f"{stock_id}: packet current_main_price_universe_source mismatch: expected {CURRENT_UNIVERSE_SOURCE}, "
            f"got {packet_universe_source or 'missing'} ({packet_path})"
        )
    if packet_listing_source_status != LISTING_STATUS_SOURCE_STATUS:
        errors.append(
            f"{stock_id}: packet listing_status_source_status mismatch: expected {LISTING_STATUS_SOURCE_STATUS}, "
            f"got {packet_listing_source_status or 'missing'} ({packet_path})"
        )

    if expected_tdcc_rows == 0:
        expected_latest_date = ""
        expected_history_status = "tdcc_missing"
        expected_freshness_status = "tdcc_missing"
    elif not is_current_main_price_universe:
        expected_latest_date = expected_source_latest_date
        expected_history_status = "historical_only_noncurrent"
        expected_freshness_status = "historical_only_noncurrent"
        if not expected_source_latest_date:
            errors.append(f"{stock_id}: historical-only packet must preserve a real latest_tdcc_date: {packet_path}")
    elif source_tdcc_continuity_status == "accepted_history_exception":
        expected_latest_date = official_tdcc_signal_date
        expected_history_status = "tdcc_history_degraded_exception"
        expected_freshness_status = "tdcc_window_degraded"
    else:
        expected_latest_date = official_tdcc_signal_date
        expected_history_status = "tdcc_history_ready" if expected_tdcc_rows >= 8 else "insufficient_tdcc_history"
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
            "current_main_price_date": main_price_date,
            "current_main_price_universe_status": expected_universe_status,
            "current_main_price_universe_source": CURRENT_UNIVERSE_SOURCE,
            "listing_status_source_status": LISTING_STATUS_SOURCE_STATUS,
            "tdcc_history_status": expected_history_status,
            "tdcc_freshness_status": expected_freshness_status,
        }
        if source_tdcc_dataset_id:
            index_checks["source_tdcc_dataset_id"] = source_tdcc_dataset_id
        if source_tdcc_continuity_status:
            index_checks["tdcc_continuity_status"] = source_tdcc_continuity_status
            index_checks["tdcc_missing_official_dates"] = "|".join(source_tdcc_missing_official_dates)
        for field, expected in index_checks.items():
            actual = str(index_row.get(field, "")).strip()
            if field.endswith("_date"):
                actual = normalize_date(actual)
            if actual != expected:
                errors.append(
                    f"{stock_id}: packet index {field} mismatch: expected {expected}, got {actual or 'missing'}"
                )
        index_rows = str(index_row.get("tdcc_rows", "")).strip()
        if index_rows != str(expected_tdcc_rows):
            errors.append(
                f"{stock_id}: packet index tdcc_rows mismatch: expected source value {expected_tdcc_rows}, "
                f"got {index_rows or 'missing'}"
            )
    return errors


def validate_tdcc_window(
    stock_id: str,
    source_frame: pd.DataFrame,
    source_assessment: StockTdccAssessment,
    window_weeks: int = 12,
) -> list[str]:
    path = TDCC_WINDOW_DIR / f"{stock_id}_tdcc_window_latest.csv"
    if not path.exists():
        return [f"{stock_id}: TDCC window is missing: {path}"]
    try:
        window = pd.read_csv(path, dtype=str, encoding="utf-8-sig").fillna("")
    except Exception as exc:
        return [f"{stock_id}: cannot read TDCC window {path}: {exc}"]

    expected_window = source_frame.tail(window_weeks).reset_index(drop=True)
    expected_dates = expected_window["as_of_date"].astype(str).tolist() if not source_frame.empty else []
    actual_dates = (
        [normalize_date(value) for value in window.get("as_of_date", pd.Series(dtype=str)).tolist()]
        if not window.empty
        else []
    )
    errors: list[str] = []
    if actual_dates != expected_dates:
        errors.append(
            f"{stock_id}: TDCC window date sequence mismatch: expected {expected_dates}, got {actual_dates} ({path})"
        )
    if source_frame.empty:
        if not window.empty:
            errors.append(f"{stock_id}: TDCC window must be empty when materialized history is empty: {path}")
        return errors

    required_metadata = {
        "source_tdcc_dataset_id": source_assessment.dataset_id,
        "tdcc_continuity_status": source_assessment.continuity_status,
        "tdcc_missing_official_dates": "|".join(source_assessment.missing_official_dates),
    }
    for field, expected in required_metadata.items():
        if field not in window.columns:
            errors.append(f"{stock_id}: TDCC window missing {field}: {path}")
            continue
        values = {str(value).strip() for value in window[field].tolist()}
        if values != {expected}:
            errors.append(
                f"{stock_id}: TDCC window {field} mismatch: expected {expected or 'blank'}, "
                f"got {sorted(values)} ({path})"
            )
    missing_value_fields = sorted(set(TDCC_WINDOW_VALUE_FIELDS) - set(window.columns))
    if missing_value_fields:
        errors.append(f"{stock_id}: TDCC window missing required value fields {missing_value_fields}: {path}")
    numeric_fields = {
        field
        for field in TDCC_WINDOW_VALUE_FIELDS
        if "_ratio" in field or "_change_" in field or field == "tdcc_consecutive_up_weeks"
    }
    boolean_fields = {"all_thresholds_up", "high_thresholds_up", "four_thresholds_sync_up"}
    for field in TDCC_WINDOW_VALUE_FIELDS:
        if field not in expected_window.columns or field not in window.columns:
            continue
        expected_values = expected_window[field].tolist()
        actual_values = window[field].tolist()
        if len(expected_values) != len(actual_values):
            continue
        for row_number, (expected, actual) in enumerate(zip(expected_values, actual_values), start=1):
            if field in numeric_fields:
                try:
                    expected_number = float(expected) if str(expected).strip() else math.nan
                    actual_number = float(actual) if str(actual).strip() else math.nan
                except (TypeError, ValueError):
                    errors.append(f"{stock_id}: TDCC window {field} row {row_number} is not numeric ({path})")
                    break
                if not (
                    (math.isnan(expected_number) and math.isnan(actual_number))
                    or math.isclose(expected_number, actual_number, rel_tol=0.0, abs_tol=1e-9)
                ):
                    errors.append(
                        f"{stock_id}: TDCC window {field} row {row_number} source mismatch: "
                        f"expected {expected}, got {actual} ({path})"
                    )
                    break
            elif field in boolean_fields:
                if str(expected).strip().lower() != str(actual).strip().lower():
                    errors.append(
                        f"{stock_id}: TDCC window {field} row {row_number} source mismatch: "
                        f"expected {expected}, got {actual} ({path})"
                    )
                    break
            elif str(expected).strip() != str(actual).strip():
                errors.append(
                    f"{stock_id}: TDCC window {field} row {row_number} source mismatch: "
                    f"expected {expected}, got {actual} ({path})"
                )
                break
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
    tdcc_contract: IndividualTdccDatasetContract,
    index_row: dict[str, str],
    validate_current_price: bool = True,
    is_current_main_price_universe: bool = True,
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
    try:
        source_frame, source_assessment = prepare_and_validate_stock_tdcc_history(
            stock_id,
            read_tdcc_source_frame(stock_id),
            tdcc_contract,
        )
    except RuntimeError as exc:
        errors.append(str(exc))
        source_frame = read_tdcc_source_frame(stock_id)
        source_tdcc_rows, source_latest_tdcc_date = read_tdcc_source_stats(stock_id)
        source_assessment = StockTdccAssessment(
            stock_id=stock_id,
            dataset_id=tdcc_contract.dataset_id,
            signal_date=tdcc_contract.signal_date,
            row_count=source_tdcc_rows,
            latest_date=source_latest_tdcc_date,
            is_current_tdcc_universe=stock_id in tdcc_contract.current_stock_ids,
            continuity_status="invalid",
            missing_official_dates=(),
        )
    errors.extend(
        validate_tdcc_packet_freshness(
            stock_id,
            packet_path,
            index_row,
            tdcc_contract.signal_date,
            main_price_date,
            is_current_main_price_universe,
            source_assessment.row_count,
            source_assessment.latest_date,
            tdcc_contract.dataset_id,
            source_assessment.continuity_status,
            source_assessment.missing_official_dates,
        )
    )
    if source_assessment.continuity_status != "invalid":
        errors.extend(validate_tdcc_window(stock_id, source_frame, source_assessment))

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
    try:
        tdcc_contract = load_individual_tdcc_dataset_contract(OFFICIAL_TDCC_DATASET_MANIFEST_JSON)
    except RuntimeError as exc:
        raise SystemExit(f"ERROR: Cannot load canonical TDCC dataset contract: {exc}") from exc
    main_price_date = read_main_price_date()
    current_main_price_universe = read_current_main_price_universe(main_price_date)
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
        is_current_main_price_universe = stock_id in current_main_price_universe
        validate_current_price = not index_row or is_current_main_price_universe
        if not validate_current_price:
            non_current_price_count += 1
        errors.extend(
            validate_stock(
                stock_id,
                main_price_date,
                tdcc_contract,
                index_row,
                validate_current_price=validate_current_price,
                is_current_main_price_universe=is_current_main_price_universe,
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
        f"official_tdcc_signal_date={tdcc_contract.signal_date}; "
        f"source_tdcc_dataset_id={tdcc_contract.dataset_id}; validated={len(stock_ids)} "
        f"current_main_price_universe={len(current_main_price_universe)} "
        f"non_current_price_packets_checked_for_tdcc={non_current_price_count}"
    )
    print("tdcc_history_status_distribution=" + ",".join(f"{key}:{history_status_counts[key]}" for key in sorted(history_status_counts)))
    print("tdcc_freshness_status_distribution=" + ",".join(f"{key}:{freshness_status_counts[key]}" for key in sorted(freshness_status_counts)))
    print("latest_tdcc_date_distribution=" + ",".join(f"{key}:{latest_tdcc_date_counts[key]}" for key in sorted(latest_tdcc_date_counts)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
