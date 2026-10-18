from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.build_stock_price_history as history
import scripts.repair_daily_price_range as repair


def git_head(root: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True, encoding="utf-8"
    ).strip()


def capture_contracts(
    root: Path,
    dates: list[str],
    source_base_sha: str,
    capture_root: Path,
    *,
    retries: int = 2,
    sleep_seconds: float = 5,
    fetch_func: Callable | None = None,
) -> dict:
    """先保存官方正規化來源，再由同一份 bytes 測量既有修復契約。"""
    if git_head(root) != source_base_sha:
        raise ValueError("selected recovery source_base_sha does not equal repository HEAD")
    name_sources = repair.validate_selected_canonical_name_sources(root, source_base_sha)
    capture_root.mkdir(parents=True, exist_ok=True)
    fetch_func = fetch_func or repair.fetch_with_retry
    contracts: list[dict] = []
    selected_stock_ids: set[str] = set()
    selected_keys: set[tuple[str, str]] = set()
    prior_exact = repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
    repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = True
    try:
        for date in dates:
            receipt_path = capture_root / f"official_capture_{date}.json"
            try:
                frame, status, log = fetch_func(date, retries, sleep_seconds)
            except Exception as exc:
                receipt_path.write_text(json.dumps({"date": date, "error": str(exc)}) + "\n", encoding="utf-8")
                raise
            receipt_path.write_text(
                json.dumps({"date": date, "status": status, "log": log}, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            if not status.get("full_market_ok"):
                raise ValueError(f"official capture failed {date}: {'; '.join(log[-5:])}")
            payload = repair.dataframe_csv_bytes(frame)
            projection = repair.fetcher._price_projection(payload, date)
            if (
                projection["twse_rows"] < repair.fetcher.MIN_TWSE_ROWS
                or projection["tpex_rows"] < repair.fetcher.MIN_TPEX_ROWS
                or projection["total_rows"] < repair.fetcher.MIN_FULL_ROWS
            ):
                raise ValueError(f"official full-market capture is insufficient: {date}")
            path = capture_root / f"daily_price_{date}.csv"
            path.write_bytes(payload)
            normalized = history.normalize_daily_price_file(path)
            selected_stock_ids.update(normalized["stock_id"].tolist())
            selected_keys.update(zip(normalized["stock_id"], normalized["date"]))
            contracts.append(
                {
                    "date": date,
                    "sha256": hashlib.sha256(payload).hexdigest(),
                    "row_count": int(projection["total_rows"]),
                    "twse_rows": int(projection["twse_rows"]),
                    "tpex_rows": int(projection["tpex_rows"]),
                    "capture_path": str(path),
                    "fetch_response_provenance": status.get("fetch_response_provenance", []),
                }
            )
    finally:
        repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = prior_exact
    existing = {
        history.normalize_stock_id(path.stem)
        for path in (root / "data/stock_price_history").glob("*.csv")
        if path.is_file() and not path.is_symlink()
    }
    result = {
        "source_base_sha": source_base_sha,
        "selected_dates": dates,
        "canonical_stock_name_source_bindings": name_sources,
        "date_contracts": contracts,
        "expected_stock_union_count": len(selected_stock_ids),
        "expected_selected_row_count": len(selected_keys),
        "expected_existing_history_count": len(selected_stock_ids & existing),
        "expected_created_history_count": len(selected_stock_ids - existing),
        "expected_untouched_history_count": len(existing - selected_stock_ids),
        "created_stock_ids": sorted(selected_stock_ids - existing),
    }
    (capture_root / "contracts.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return result


def apply_contracts(root: Path, capture_root: Path, contracts: dict, *, runner=None) -> None:
    """只調用既有 selected repair、history 與獨立 continuity 驗收。"""
    runner = runner or subprocess.run
    dates = contracts["selected_dates"]
    date_contracts = [
        f"{row['date']}:{row['sha256']}:{row['row_count']}"
        for row in contracts["date_contracts"]
    ]
    count_args = []
    for key in (
        "expected_stock_union_count",
        "expected_selected_row_count",
        "expected_existing_history_count",
        "expected_created_history_count",
        "expected_untouched_history_count",
    ):
        count_args.extend(["--" + key.replace("_", "-"), str(contracts[key])])
    source_args = []
    validator_sources = []
    for value in date_contracts:
        source_args.extend(["--expected-date-contract", value])
        validator_sources.extend(["--selected-date-contract", value])
    source_command = [
        sys.executable, "scripts/repair_daily_price_range.py",
        "--dates", ",".join(dates),
        "--source-base-sha", contracts["source_base_sha"],
        "--max-days", str(len(dates)),
        *source_args,
    ]
    history_command = [sys.executable, "scripts/build_stock_price_history.py"]
    for date in dates:
        history_command.extend(["--repair-date", date])
    validator_command = [
        sys.executable, "scripts/validate_daily_price_history_continuity.py",
        "--selected-repair-report", "output/latest/repair_daily_price_range_latest.json",
        "--selected-source-base-sha", contracts["source_base_sha"],
        *validator_sources,
        *count_args,
        "--require-all-eligible-changed",
        "--pathspec-nul-output", str(capture_root / "selected-paths.nul"),
        "--pathspec-json-output", str(capture_root / "selected-paths.json"),
        "--history-stock-id-output", str(capture_root / "selected-stock-ids.txt"),
        "--no-write-report",
    ]
    for stock_id in contracts["created_stock_ids"]:
        history_command.extend(["--allow-create-stock-id", stock_id])
        validator_command.extend(["--expected-created-stock-id", stock_id])
    for command in (source_command, [*history_command, *count_args], validator_command):
        runner(command, cwd=root, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="保存官方 selected-date 契約並執行隔離來源修復。")
    parser.add_argument("--dates", required=True)
    parser.add_argument("--source-base-sha", required=True)
    parser.add_argument("--capture-root", type=Path, required=True)
    parser.add_argument("--max-days", type=int, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    dates = repair.parse_selected_dates(args.dates)
    if not dates or len(dates) > args.max_days:
        parser.error("selected dates must be non-empty and within max-days")
    contracts = capture_contracts(ROOT, dates, args.source_base_sha, args.capture_root.resolve())
    if args.apply:
        apply_contracts(ROOT, args.capture_root.resolve(), contracts)
    print(json.dumps(contracts, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
