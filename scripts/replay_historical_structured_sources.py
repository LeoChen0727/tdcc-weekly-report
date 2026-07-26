from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

import fetch_official_daily_price as price_fetcher  # noqa: E402
from scripts import repair_daily_price_range as price_repair  # noqa: E402
from scripts import validate_daily_price_history_continuity as continuity  # noqa: E402


REPLAY_HISTORY = Path("output/history/historical_source_replay")
LATEST_JSON = Path("output/latest/historical_structured_source_replay_latest.json")
LATEST_MD = Path("output/latest/historical_structured_source_replay_latest.md")
PRICE_STATUS_JSON = Path("output/latest/official_price_fetch_latest.json")
PRICE_STATUS_MD = Path("output/latest/official_price_fetch_latest.md")
PRICE_LATEST = Path("output/latest/official_daily_price_latest.csv")
MARKET_STATUS_JSON = Path("output/latest/market_index_source_status_latest.json")
TAIFEX_STATUS_JSON = Path("output/latest/futures_options_source_status_latest.json")
WARRANT_STATUS_JSON = Path("output/latest/warrant_source_status_latest.json")
FRESHNESS_CSV = Path("output/latest/data_freshness_latest.csv")
STOCK_HISTORY_MANIFEST = Path("output/latest/stock_price_history_manifest.csv")
WARRANT_FLOW_LATEST = Path("output/latest/warrant_flow_latest.csv")
TAIFEX_HISTORY_SPECS = {
    "institutional_fo": (
        Path("data/futures_options/taifex_institutional_fo_history.csv"),
        ["日期", "身份別"],
    ),
    "futures_contracts": (
        Path("data/futures_options/taifex_futures_contracts_history.csv"),
        ["日期", "商品名稱", "身份別"],
    ),
    "options_call_put": (
        Path("data/futures_options/taifex_options_call_put_history.csv"),
        ["日期", "商品名稱", "買賣權別", "身份別"],
    ),
    "put_call_ratio": (
        Path("data/futures_options/put_call_ratio_history.csv"),
        ["日期"],
    ),
    "taiwan_vix": (
        Path("data/futures_options/taiwan_vix_history.csv"),
        ["date"],
    ),
}


def parse_date(value: str, label: str) -> str:
    text = str(value or "").strip()
    if not re.fullmatch(r"20\d{6}", text):
        raise RuntimeError(f"{label} must be calendar-valid YYYYMMDD")
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise RuntimeError(f"{label} must be calendar-valid YYYYMMDD") from exc
    return text


def parse_replay_id(value: str) -> str:
    replay_id = str(value or "").strip()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", replay_id):
        raise RuntimeError(
            "--replay-id must be 1-128 characters using only letters, digits, dot, underscore, or dash"
        )
    return replay_id


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def aggregate_path_sha256(paths: list[Path]) -> str:
    rows = []
    for path in sorted({p.as_posix(): p for p in paths}.values(), key=lambda p: p.as_posix()):
        if path.is_file():
            rows.append({"path": path.as_posix(), "sha256": file_sha256(path)})
    return sha256_bytes(
        json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


def aggregate_response_hash(rows: list[dict[str, Any]], field: str) -> str:
    values = [str(row.get(field, "")) for row in rows if str(row.get(field, ""))]
    return sha256_bytes("\n".join(values).encode("utf-8")) if values else ""


def detect_date_column(frame: pd.DataFrame, path: Path) -> str:
    candidates = [col for col in ("date", "日期", "交易日期") if col in frame.columns]
    if len(candidates) != 1:
        raise RuntimeError(f"cannot resolve one date column for replay slice: {path} {candidates}")
    return candidates[0]


def canonical_target_slice(
    path: Path,
    target_date: str,
    *,
    pk_columns: list[str],
    filters: dict[str, str] | None = None,
) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"replay output slice path missing: {path}")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
    date_col = detect_date_column(frame, path)
    normalized_dates = frame[date_col].astype(str).str.replace(r"[^0-9]", "", regex=True).str[:8]
    filtered = frame.copy()
    filtered_dates = normalized_dates.copy()
    for column, expected in (filters or {}).items():
        if column not in filtered.columns:
            raise RuntimeError(f"replay output slice missing filter column {column}: {path}")
        mask = filtered[column].astype(str).eq(expected)
        filtered = filtered[mask].copy()
        filtered_dates = filtered_dates[mask]
    exact = filtered[filtered_dates.eq(target_date)].copy()
    if exact.empty:
        raise RuntimeError(f"replay output slice is empty for {target_date}: {path}")
    missing_pk = [column for column in pk_columns if column not in exact.columns]
    if missing_pk:
        raise RuntimeError(f"replay output slice missing PK columns {missing_pk}: {path}")
    pk_unique = not exact.duplicated(pk_columns).any()
    sort_columns = list(dict.fromkeys([*pk_columns, *sorted(exact.columns)]))
    canonical = exact.sort_values(sort_columns, kind="stable").reset_index(drop=True)
    payload = canonical.to_csv(index=False, lineterminator="\n").encode("utf-8")
    return {
        "path": path.as_posix(),
        "date_column": date_col,
        "target_date": target_date,
        "filters": dict(sorted((filters or {}).items())),
        "pk_columns": pk_columns,
        "row_count": int(len(canonical)),
        "pk_unique": bool(pk_unique),
        "future_row_count": int(filtered_dates.gt(target_date).sum()),
        "slice_sha256": sha256_bytes(payload),
    }


def build_component_evidence(
    component_id: str,
    specs: list[tuple[Path, list[str], dict[str, str]]],
    target_date: str,
) -> dict[str, Any]:
    members = [
        canonical_target_slice(
            path,
            target_date,
            pk_columns=pk_columns,
            filters=filters,
        )
        for path, pk_columns, filters in specs
    ]
    stable_members = [
        {key: value for key, value in member.items() if key != "future_row_count"}
        for member in members
    ]
    aggregate_payload = json.dumps(
        stable_members,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "component_id": component_id,
        "member_count": len(members),
        "row_count": sum(int(member["row_count"]) for member in members),
        "pk_unique": all(bool(member["pk_unique"]) for member in members),
        "future_row_count": sum(int(member["future_row_count"]) for member in members),
        "future_rows_excluded_from_slice": True,
        "slice_manifest_sha256": sha256_bytes(aggregate_payload),
    }


def supported_daily_stock_ids(target_date: str) -> list[str]:
    path = Path(f"data/daily_price/daily_price_{target_date}.csv")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
    if not {"date", "stock_id"}.issubset(frame.columns):
        raise RuntimeError(f"daily price schema cannot prove stock coverage: {path}")
    exact = frame[frame["date"].astype(str).eq(target_date)].copy()
    stock_ids = sorted(
        {
            continuity.normalize_stock_id(value)
            for value in exact["stock_id"]
            if continuity.is_supported_security_id(value)
        }
    )
    if len(stock_ids) < continuity.DEFAULT_MIN_FULL_ROWS:
        raise RuntimeError(
            f"daily price supported stock universe too small for {target_date}: {len(stock_ids)}"
        )
    return stock_ids


def validate_stock_history_date_coverage(target_date: str) -> dict[str, Any]:
    stock_ids = supported_daily_stock_ids(target_date)
    missing: list[str] = []
    for stock_id in stock_ids:
        path = Path("data/stock_price_history") / f"{stock_id}.csv"
        if not path.exists():
            missing.append(stock_id)
            continue
        frame = pd.read_csv(path, dtype=str, usecols=["date"], keep_default_na=False).fillna("")
        if target_date not in set(frame["date"].astype(str)):
            missing.append(stock_id)
    if missing:
        raise RuntimeError(
            f"stock histories missing {target_date} for {len(missing)} supported stocks: {missing[:20]}"
        )
    manifest = pd.read_csv(STOCK_HISTORY_MANIFEST, dtype=str, keep_default_na=False).fillna("")
    if not {"stock_id", "end_date"}.issubset(manifest.columns):
        raise RuntimeError("stock history manifest lacks stock_id/end_date")
    manifest["stock_id"] = manifest["stock_id"].map(continuity.normalize_stock_id)
    indexed = manifest.drop_duplicates("stock_id", keep="last").set_index("stock_id")
    bad_manifest = [
        stock_id
        for stock_id in stock_ids
        if stock_id not in indexed.index or str(indexed.at[stock_id, "end_date"]) != target_date
    ]
    if bad_manifest:
        raise RuntimeError(
            f"stock history manifest does not end at {target_date} for {len(bad_manifest)} stocks: "
            f"{bad_manifest[:20]}"
        )
    return {"supported_stock_count": len(stock_ids), "missing_history_rows": 0}


def build_source_output_evidence(
    source_id: str,
    target_date: str,
    *,
    market_index_codes: set[str] | None = None,
) -> dict[str, Any]:
    components: list[dict[str, Any]] = []
    if source_id == "official_daily_price":
        components.append(
            build_component_evidence(
                "dated_daily_price",
                [
                    (Path(f"data/daily_price/daily_price_{target_date}.csv"), ["date", "stock_id"], {}),
                    (Path(f"data/daily_price/{target_date}.csv"), ["date", "stock_id"], {}),
                ],
                target_date,
            )
        )
        history_specs = [
            (
                Path("data/stock_price_history") / f"{stock_id}.csv",
                ["date", "stock_id"],
                {},
            )
            for stock_id in supported_daily_stock_ids(target_date)
        ]
        components.append(
            build_component_evidence("stock_history_target_slices", history_specs, target_date)
        )
    elif source_id in {"market_index", "market_index_base_repair"}:
        codes = sorted(market_index_codes or {"TWSE", "TPEX"})
        specs = [
            (path, ["date", "index_code"], {"index_code": code})
            for path in (
                Path("data/market_index_history.csv"),
                Path("data/market_index_ohlc_history.csv"),
            )
            for code in codes
        ]
        components.append(build_component_evidence("market_index_target_rows", specs, target_date))
    elif source_id == "taifex_futures_options_vix":
        specs = [(path, pk_columns, {}) for path, pk_columns in TAIFEX_HISTORY_SPECS.values()]
        components.append(build_component_evidence("taifex_target_rows", specs, target_date))
    elif source_id == "official_warrant_daily":
        components.append(
            build_component_evidence(
                "warrant_raw_and_flow_dated",
                [
                    (
                        Path(f"output/history/warrant_daily/warrant_daily_{target_date}.csv"),
                        ["date", "market", "warrant_id"],
                        {},
                    ),
                    (
                        Path(f"output/history/warrant_flow/warrant_flow_{target_date}.csv"),
                        ["date", "stock_id"],
                        {},
                    ),
                ],
                target_date,
            )
        )
    else:
        raise RuntimeError(f"unknown replay source output evidence: {source_id}")
    stable_components = [
        {
            key: value
            for key, value in component.items()
            if key not in {"future_row_count", "future_rows_excluded_from_slice"}
        }
        for component in components
    ]
    evidence_payload = json.dumps(
        stable_components,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "target_date": target_date,
        "components": components,
        "row_count": sum(int(component["row_count"]) for component in components),
        "pk_unique": all(bool(component["pk_unique"]) for component in components),
        "future_row_count": sum(int(component["future_row_count"]) for component in components),
        "future_rows_excluded_from_slice": True,
        "output_sha256": sha256_bytes(evidence_payload),
    }


def write_json_immutable(path: Path, payload: dict[str, Any]) -> None:
    encoded = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if path.exists():
        if path.read_bytes() != encoded:
            raise RuntimeError(f"immutable replay manifest collision: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded)


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"required source status missing: {path}")
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"source status must be an object: {path}")
    return payload


def run_checked(command: list[str], *, env: dict[str, str] | None = None) -> None:
    merged_env = os.environ.copy()
    merged_env["PYTHONIOENCODING"] = "utf-8"
    if env:
        merged_env.update(env)
    completed = subprocess.run(command, cwd=ROOT, env=merged_env, check=False)
    if completed.returncode != 0:
        raise RuntimeError(
            f"historical source replay command failed rc={completed.returncode}: {' '.join(command)}"
        )


def git_output(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {completed.stderr.strip()}")
    return completed.stdout.strip()


def expected_trading_dates(start_date: str, end_date: str) -> list[str]:
    non_trading = continuity.load_non_trading_days(ROOT, continuity.NON_TRADING_DAYS)
    start = datetime.strptime(start_date, "%Y%m%d")
    end = datetime.strptime(end_date, "%Y%m%d")
    if end < start:
        raise RuntimeError("end_date must be >= start_date")
    dates = []
    current = start
    while current <= end:
        text = current.strftime("%Y%m%d")
        if current.weekday() < 5 and text not in non_trading:
            dates.append(text)
        current += timedelta(days=1)
    if not dates:
        raise RuntimeError("historical source replay window has no trading dates")
    return dates


def max_csv_date(path: Path, date_col: str = "date", *, index_code: str = "") -> str:
    if not path.exists():
        return ""
    try:
        frame = pd.read_csv(path, dtype=str, usecols=lambda col: col in {date_col, "index_code"})
    except Exception:
        return ""
    if frame.empty or date_col not in frame.columns:
        return ""
    if index_code and "index_code" in frame.columns:
        frame = frame[frame["index_code"].astype(str).eq(index_code)]
    dates = frame[date_col].astype(str).str.replace(r"[^0-9]", "", regex=True)
    dates = dates[dates.str.fullmatch(r"20\d{6}", na=False)]
    return str(dates.max()) if not dates.empty else ""


def stock_history_tail() -> dict[str, Any]:
    paths = sorted(Path("data/stock_price_history").glob("*.csv"))
    tails = [max_csv_date(path) for path in paths]
    tails = [date for date in tails if date]
    maximum = max(tails) if tails else ""
    return {
        "max_date": maximum,
        "files": len(paths),
        "files_at_max": sum(1 for date in tails if date == maximum),
    }


def source_tail_matrix() -> dict[str, Any]:
    daily_dates = []
    for path in Path("data/daily_price").glob("daily_price_*.csv"):
        match = re.fullmatch(r"daily_price_(20\d{6})\.csv", path.name)
        if match:
            daily_dates.append(match.group(1))
    warrant_dates = []
    for path in Path("output/history/warrant_daily").glob("warrant_daily_*.csv"):
        match = re.fullmatch(r"warrant_daily_(20\d{6})\.csv", path.name)
        if match:
            warrant_dates.append(match.group(1))
    warrant_flow_dates = []
    for path in Path("output/history/warrant_flow").glob("warrant_flow_*.csv"):
        match = re.fullmatch(r"warrant_flow_(20\d{6})\.csv", path.name)
        if match:
            warrant_flow_dates.append(match.group(1))
    return {
        "daily_price": max(daily_dates) if daily_dates else "",
        "stock_price_history": stock_history_tail(),
        "market_index": {
            "TWSE": max_csv_date(Path("data/market_index_history.csv"), index_code="TWSE"),
            "TPEX": max_csv_date(Path("data/market_index_history.csv"), index_code="TPEX"),
        },
        "market_index_ohlc": {
            "TWSE": max_csv_date(Path("data/market_index_ohlc_history.csv"), index_code="TWSE"),
            "TPEX": max_csv_date(Path("data/market_index_ohlc_history.csv"), index_code="TPEX"),
        },
        "taifex": {
            source_id: max_csv_date(path, pk_columns[0])
            for source_id, (path, pk_columns) in TAIFEX_HISTORY_SPECS.items()
        },
        "warrant_daily": max(warrant_dates) if warrant_dates else "",
        "warrant_flow": max(warrant_flow_dates) if warrant_flow_dates else "",
    }


def previous_trading_date(date_text: str) -> str:
    non_trading = continuity.load_non_trading_days(ROOT, continuity.NON_TRADING_DAYS)
    current = datetime.strptime(date_text, "%Y%m%d") - timedelta(days=1)
    while current.weekday() >= 5 or current.strftime("%Y%m%d") in non_trading:
        current -= timedelta(days=1)
    return current.strftime("%Y%m%d")


def validate_exact_baseline(matrix: dict[str, Any], base_date: str) -> None:
    expected_previous = previous_trading_date(base_date)
    errors: list[str] = []
    if matrix.get("daily_price") != base_date:
        errors.append(f"daily_price={matrix.get('daily_price')} expected={base_date}")
    stock_tail = matrix.get("stock_price_history", {})
    if stock_tail.get("max_date") != base_date:
        errors.append(f"stock_price_history={stock_tail.get('max_date')} expected={base_date}")
    expected_market = {"TWSE": base_date, "TPEX": expected_previous}
    for family in ("market_index", "market_index_ohlc"):
        if matrix.get(family) != expected_market:
            errors.append(f"{family}={matrix.get(family)} expected={expected_market}")
    if set(matrix.get("taifex", {}).values()) != {base_date}:
        errors.append(f"taifex={matrix.get('taifex')} expected all {base_date}")
    for family in ("warrant_daily", "warrant_flow"):
        if matrix.get(family) != base_date:
            errors.append(f"{family}={matrix.get(family)} expected={base_date}")
    if errors:
        raise RuntimeError("historical source replay baseline mismatch: " + "; ".join(errors))
    validate_stock_history_date_coverage(base_date)


def validate_price_frame(frame: pd.DataFrame, target_date: str, status: dict[str, Any]) -> None:
    dates = set(frame.get("date", pd.Series(dtype=str)).astype(str))
    if dates != {target_date}:
        raise RuntimeError(f"official price rows are not exact target date {target_date}: {dates}")
    if not bool(status.get("full_market_ok")):
        raise RuntimeError(f"official price source did not pass full-market gate: {status}")


def write_price_status(
    target_date: str,
    frame: pd.DataFrame,
    status: dict[str, Any],
    responses: list[dict[str, Any]],
) -> dict[str, Any]:
    canonical = Path(f"data/daily_price/daily_price_{target_date}.csv")
    legacy = Path(f"data/daily_price/{target_date}.csv")
    PRICE_LATEST.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(PRICE_LATEST, index=False, encoding="utf-8-sig")
    normalized_frame_dates = frame["date"].astype(str).str.replace(r"[^0-9]", "", regex=True).str[:8]
    future_row_count = int(normalized_frame_dates.gt(target_date).sum())
    payload = {
        "generated_at": datetime.now().astimezone().isoformat(),
        "mode": "reconstructed_source_tail_gap",
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "target_date": target_date,
        "saved_price_date": target_date,
        "is_target_date": True,
        "result": "success_target_full_market",
        "full_market_ok": True,
        "twse_rows": int(status.get("twse_rows", 0)),
        "tpex_rows": int(status.get("tpex_rows", 0)),
        "total_rows": int(status.get("total_rows", len(frame))),
        "fallback_used": False,
        "calculation_context_max_date": str(normalized_frame_dates.max()),
        "future_row_count": future_row_count,
        "future_rows_used": future_row_count > 0,
        "source_responses": responses,
        "paths": {
            "dated_csv": canonical.as_posix(),
            "dated_alt_csv": legacy.as_posix(),
            "latest_csv": PRICE_LATEST.as_posix(),
        },
        "output_sha256": aggregate_path_sha256([canonical, legacy, PRICE_LATEST]),
    }
    PRICE_STATUS_JSON.parent.mkdir(parents=True, exist_ok=True)
    PRICE_STATUS_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PRICE_STATUS_MD.write_text(
        "\n".join(
            [
                "# Official Price Historical Replay Status",
                "",
                f"- target_date: `{target_date}`",
                "- publication_status: `reconstructed_not_as_published`",
                "- as_published: `False`",
                "- fallback_used: `False`",
                f"- TWSE rows: `{payload['twse_rows']}`",
                f"- TPEx rows: `{payload['tpex_rows']}`",
                f"- total rows: `{payload['total_rows']}`",
                f"- source response count: `{len(responses)}`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return payload


def replay_price_date(target_date: str) -> dict[str, Any]:
    price_fetcher.MAX_WORKERS = 1
    price_fetcher.reset_fetch_response_provenance()
    previous_strict = price_fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
    price_fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = True
    try:
        frame, status, log = price_repair.fetch_with_retry(
            target_date,
            retries=3,
            sleep_seconds=5.0,
        )
    finally:
        price_fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = previous_strict
    validate_price_frame(frame, target_date, status)
    price_repair.write_daily_price_files(frame, target_date)
    selected_sources = set(frame["source"].astype(str))
    responses = [
        response
        for response in price_fetcher.fetch_response_provenance()
        if response.get("source_name") in selected_sources
        and response.get("exact_date_match") is True
        and response.get("observed_response_dates") == [target_date]
    ]
    proven_sources = {str(response.get("source_name", "")) for response in responses}
    if not selected_sources or proven_sources != selected_sources:
        raise RuntimeError(
            "official price historical replay lacks exact-date provenance for adopted sources: "
            f"selected={sorted(selected_sources)} proven={sorted(proven_sources)}"
        )
    price_status = write_price_status(target_date, frame, status, responses)
    run_checked([sys.executable, "scripts/build_stock_price_history.py", "--incremental-latest"])
    coverage = validate_stock_history_date_coverage(target_date)
    price_status["stock_history_coverage"] = coverage
    return price_status


def validate_exact_market_date(target_date: str, requested_codes: set[str]) -> None:
    for path in (Path("data/market_index_history.csv"), Path("data/market_index_ohlc_history.csv")):
        frame = pd.read_csv(path, dtype=str)
        exact = frame[
            frame["date"].astype(str).eq(target_date)
            & frame["index_code"].astype(str).isin(requested_codes)
        ]
        if len(exact) != len(requested_codes) or set(exact["index_code"].astype(str)) != requested_codes:
            raise RuntimeError(f"market index target rows invalid for {target_date}: {path}")


def run_market_date(
    target_date: str,
    requested_codes: set[str] | None = None,
) -> dict[str, Any]:
    requested_codes = set(requested_codes or {"TWSE", "TPEX"})
    command = [sys.executable, "scripts/update_market_index_history.py", "--target-date", target_date]
    for code in sorted(requested_codes):
        command.extend(["--target-index-code", code])
    run_checked(command)
    validate_exact_market_date(target_date, requested_codes)
    status = read_json(MARKET_STATUS_JSON)
    observed = status.get("observed_dates")
    if (
        status.get("requested_date") != target_date
        or set(status.get("requested_index_codes", [])) != requested_codes
        or observed != {code: target_date for code in sorted(requested_codes)}
        or status.get("fallback_used") is not False
    ):
        raise RuntimeError(f"market index replay status invalid for {target_date}")
    return status


def run_taifex_date(target_date: str) -> dict[str, Any]:
    run_checked(
        [
            sys.executable,
            "scripts/fetch_futures_options_indicators.py",
            "--start-date",
            target_date,
            "--end-date",
            target_date,
            "--require-exact-source-dates",
        ]
    )
    status = read_json(TAIFEX_STATUS_JSON)
    requested = status.get("requested_window", {})
    if requested != {"start_date": target_date, "end_date": target_date}:
        raise RuntimeError(f"TAIFEX replay status requested window mismatch: {requested}")
    for name, source in status.get("sources", {}).items():
        if source.get("status") != "ok" or source.get("latest_date") != target_date:
            raise RuntimeError(f"TAIFEX source {name} did not validate target_date={target_date}")
    latest_paths = [
        Path("output/latest/futures_options_institutional_fo_latest.csv"),
        Path("output/latest/futures_options_contracts_latest.csv"),
        Path("output/latest/futures_options_call_put_latest.csv"),
        Path("output/latest/futures_options_put_call_ratio_latest.csv"),
        Path("output/latest/taiwan_vix_latest.csv"),
    ]
    future_rows = 0
    for path in latest_paths:
        frame = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
        date_col = detect_date_column(frame, path)
        dates = frame[date_col].astype(str).str.replace(r"[^0-9]", "", regex=True).str[:8]
        future_rows += int(dates.gt(target_date).sum())
    status["latest_context_future_row_count"] = future_rows
    status["future_rows_used"] = future_rows > 0
    if status["future_rows_used"]:
        raise RuntimeError(f"TAIFEX target context used future rows for {target_date}: {future_rows}")
    TAIFEX_STATUS_JSON.write_text(
        json.dumps(status, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return status


def run_warrant_date(target_date: str) -> dict[str, Any]:
    before_daily_tail = source_tail_matrix().get("warrant_daily", "")
    before_flow_tail = source_tail_matrix().get("warrant_flow", "")
    if before_daily_tail > target_date or before_flow_tail >= target_date:
        raise RuntimeError(
            "warrant replay context is not strictly prior to target: "
            f"daily={before_daily_tail} flow={before_flow_tail} target={target_date}"
        )
    run_checked(
        [
            sys.executable,
            "scripts/fetch_official_warrant_daily.py",
            "--date",
            target_date,
            "--historical-replay",
            "--require-live-fetch",
            "--require-current-usable",
        ]
    )
    status = read_json(WARRANT_STATUS_JSON)
    if (
        status.get("status") != "ok"
        or status.get("requested_date") != target_date
        or status.get("observed_date") != target_date
        or status.get("fallback_used") is not False
    ):
        raise RuntimeError(f"warrant replay status invalid for {target_date}")
    history = Path(f"output/history/warrant_daily/warrant_daily_{target_date}.csv")
    frame = pd.read_csv(history, dtype=str)
    if frame.empty or set(frame["date"].astype(str)) != {target_date}:
        raise RuntimeError(f"warrant history is not exact target_date={target_date}")
    run_checked([sys.executable, "build_warrant_flow_latest.py"])
    flow_history = Path(f"output/history/warrant_flow/warrant_flow_{target_date}.csv")
    for path in (flow_history, WARRANT_FLOW_LATEST):
        flow = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
        if flow.empty or "date" not in flow.columns or set(flow["date"].astype(str)) != {target_date}:
            raise RuntimeError(f"warrant flow is not exact target_date={target_date}: {path}")
        if not {"date", "stock_id"}.issubset(flow.columns) or flow.duplicated(
            ["date", "stock_id"]
        ).any():
            raise RuntimeError(f"warrant flow PK invalid for target_date={target_date}: {path}")
    status["warrant_flow_date"] = target_date
    status["warrant_flow_rows"] = int(len(pd.read_csv(flow_history, dtype=str)))
    context_dates = [date for date in (before_daily_tail, before_flow_tail, target_date) if date]
    context_max = max(context_dates) if context_dates else ""
    future_row_count = sum(1 for date in context_dates if date > target_date)
    status["calculation_context_max_date"] = context_max
    status["prior_warrant_flow_context_max_date"] = before_flow_tail
    status["future_row_count"] = future_row_count
    status["future_rows_used"] = future_row_count > 0
    if status["future_rows_used"]:
        raise RuntimeError(f"warrant replay used future context for {target_date}")
    WARRANT_STATUS_JSON.write_text(
        json.dumps(status, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return status


def manifest_source_row(
    source_id: str,
    target_date: str,
    status: dict[str, Any],
    before_tail: Any,
    after_tail: Any,
    *,
    observed_dates: list[str],
    market_index_codes: set[str] | None = None,
) -> dict[str, Any]:
    responses = status.get("source_responses") or status.get("sources") or []
    if isinstance(responses, dict):
        flattened = []
        for name, info in responses.items():
            provenance = info.get("provenance", {}) if isinstance(info, dict) else {}
            if source_files := provenance.get("source_files"):
                flattened.extend(
                    {
                        **source_file,
                        "source": name,
                        "observed_response_dates": info.get("observed_dates", []),
                    }
                    for source_file in source_files
                )
            elif attempts := provenance.get("attempts"):
                flattened.extend(
                    {
                        **attempt,
                        "source": name,
                        "observed_response_dates": attempt.get("observed_dates", []),
                    }
                    for attempt in attempts
                )
            elif provenance:
                flattened.append(
                    {
                        "source": name,
                        **provenance,
                        "observed_response_dates": info.get("observed_dates", []),
                    }
                )
        responses = flattened
    responses = responses if isinstance(responses, list) else []
    source_response_attempts = list(responses)
    source_attempt_count = len(source_response_attempts)
    if source_id in {"official_daily_price", "official_warrant_daily"}:
        responses = [
            response
            for response in responses
            if response.get("exact_date_match") is True
            and response.get("observed_response_dates") == [target_date]
        ]
    elif source_id == "taifex_futures_options_vix":
        responses = [
            response
            for response in responses
            if response.get("status", "ok") == "ok"
            and response.get("observed_response_dates") == [target_date]
        ]
    output_evidence = build_source_output_evidence(
        source_id,
        target_date,
        market_index_codes=market_index_codes,
    )
    if "future_rows_used" not in status:
        raise RuntimeError(f"source status lacks computed future_rows_used: {source_id}")
    future_rows_used = bool(status["future_rows_used"])
    return {
        "source_id": source_id,
        "endpoint": [row.get("endpoint", "") for row in responses],
        "params": [row.get("params", {}) for row in responses],
        "fetched_at": [row.get("fetched_at", "") for row in responses],
        "source_attempt_count": source_attempt_count,
        "source_response_attempts": [
            {
                field: row.get(field, "")
                for field in (
                    "attempt",
                    "source",
                    "endpoint",
                    "params",
                    "status",
                    "http_status",
                    "raw_bytes",
                    "raw_sha256",
                    "normalized_sha256",
                    "encoding",
                    "requested_dates",
                    "observed_response_dates",
                    "rows",
                    "parse_metadata",
                    "error",
                    "fetched_at",
                )
            }
            for row in source_response_attempts
        ],
        "accepted_source_response_count": len(responses),
        "accepted_source_responses": [
            {
                field: row.get(field, "")
                for field in (
                    "endpoint",
                    "source_name",
                    "source",
                    "observed_response_dates",
                    "exact_date_match",
                    "raw_sha256",
                    "normalized_sha256",
                    "fetched_at",
                )
            }
            for row in responses
        ],
        "requested_dates": [target_date],
        "observed_dates": observed_dates,
        "pk_unique": bool(output_evidence["pk_unique"]),
        "row_count": int(output_evidence["row_count"]),
        "raw_sha256": aggregate_response_hash(responses, "raw_sha256"),
        "normalized_sha256": aggregate_response_hash(responses, "normalized_sha256"),
        "output_sha256": output_evidence["output_sha256"],
        "output_evidence": output_evidence,
        "fallback_used": bool(status.get("fallback_used", False)),
        "future_rows_used": future_rows_used,
        "before_tail": before_tail,
        "after_tail": after_tail,
        "validation_status": "pass",
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
    }


def write_day_manifest(
    replay_id: str,
    target_date: str,
    before: dict[str, Any],
    after: dict[str, Any],
    price_status: dict[str, Any],
    market_status: dict[str, Any],
    taifex_status: dict[str, Any],
    warrant_status: dict[str, Any],
) -> Path:
    sources = [
        manifest_source_row(
            "official_daily_price",
            target_date,
            price_status,
            before.get("daily_price"),
            after.get("daily_price"),
            observed_dates=sorted(
                {
                    date
                    for response in price_status.get("source_responses", [])
                    for date in response.get("observed_response_dates", [])
                }
            ),
        ),
        manifest_source_row(
            "market_index",
            target_date,
            market_status,
            before.get("market_index"),
            after.get("market_index"),
            observed_dates=sorted(set(market_status.get("observed_dates", {}).values())),
            market_index_codes={"TWSE", "TPEX"},
        ),
        manifest_source_row(
            "taifex_futures_options_vix",
            target_date,
            taifex_status,
            before.get("taifex"),
            after.get("taifex"),
            observed_dates=sorted(
                {
                    date
                    for info in taifex_status.get("sources", {}).values()
                    for date in info.get("observed_dates", [])
                }
            ),
        ),
        manifest_source_row(
            "official_warrant_daily",
            target_date,
            warrant_status,
            before.get("warrant_daily"),
            after.get("warrant_daily"),
            observed_dates=sorted(
                {
                    date
                    for response in warrant_status.get("source_responses", [])
                    if response.get("exact_date_match") is True
                    for date in response.get("observed_response_dates", [])
                }
                | {warrant_status.get("observed_date", ""), warrant_status.get("warrant_flow_date", "")}
                - {""}
            ),
        ),
    ]
    for row in sources:
        if row["observed_dates"] != [target_date]:
            raise RuntimeError(
                f"manifest observed_dates mismatch for {row['source_id']} {target_date}: "
                f"{row['observed_dates']}"
            )
        if row["pk_unique"] is not True or row["future_rows_used"] is not False:
            raise RuntimeError(f"manifest PK/future-row evidence failed for {row['source_id']} {target_date}")
        if not row["raw_sha256"] or not row["normalized_sha256"] or not row["output_sha256"]:
            raise RuntimeError(f"manifest provenance hash missing for {row['source_id']} {target_date}")
    payload = {
        "schema_version": "historical_structured_source_replay_v1",
        "replay_id": replay_id,
        "report_date": target_date,
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "pipeline_commit_sha": git_output("rev-parse", "HEAD"),
        "before_tail_matrix": before,
        "after_tail_matrix": after,
        "sources": sources,
        "forbidden_reconstruction": [
            "candidate_as_published",
            "model_as_published",
            "event_as_published",
            "catalyst_as_published",
            "pdf_as_published",
        ],
    }
    path = REPLAY_HISTORY / replay_id / target_date / "structured_source_manifest.json"
    write_json_immutable(path, payload)
    return path


def write_market_base_repair_manifest(
    replay_id: str,
    target_date: str,
    before: dict[str, Any],
    after: dict[str, Any],
    status: dict[str, Any],
) -> Path:
    row = manifest_source_row(
        "market_index_base_repair",
        target_date,
        status,
        before.get("market_index"),
        after.get("market_index"),
        observed_dates=sorted(set(status.get("observed_dates", {}).values())),
        market_index_codes={"TPEX"},
    )
    if row["observed_dates"] != [target_date]:
        raise RuntimeError("market-index base repair observed_dates mismatch")
    if row["pk_unique"] is not True or row["future_rows_used"] is not False:
        raise RuntimeError("market-index base repair PK/future-row evidence failed")
    if not row["raw_sha256"] or not row["normalized_sha256"] or not row["output_sha256"]:
        raise RuntimeError("market-index base repair lacks response hashes")
    payload = {
        "schema_version": "historical_structured_source_replay_v1",
        "replay_id": replay_id,
        "report_date": target_date,
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "pipeline_commit_sha": git_output("rev-parse", "HEAD"),
        "sources": [row],
        "twse_base_row_sha256_before": status.get("twse_base_row_sha256_before", {}),
        "twse_base_row_sha256_after": status.get("twse_base_row_sha256_after", {}),
        "before_tail_matrix": before,
        "after_tail_matrix": after,
    }
    path = REPLAY_HISTORY / replay_id / target_date / "market_index_base_repair_manifest.json"
    write_json_immutable(path, payload)
    return path


def refresh_truthful_freshness(expected_end_date: str) -> dict[str, Any]:
    run_checked([sys.executable, "build_data_freshness_latest.py"])
    frame = pd.read_csv(FRESHNESS_CSV, dtype=str).fillna("")
    if len(frame) != 1:
        raise RuntimeError("data_freshness_latest.csv must have exactly one row")
    row = frame.iloc[0].to_dict()
    if row.get("main_price_date") != expected_end_date:
        raise RuntimeError(
            f"freshness main_price_date must be {expected_end_date}: {row.get('main_price_date')}"
        )
    if str(row.get("report_ready", "")).lower() == "true":
        raise RuntimeError("historical structured-source replay must not claim stale publish artifacts ready")
    if str(row.get("daily_pdf_ready", "")).lower() == "true":
        raise RuntimeError("historical structured-source replay must keep stale daily PDFs not ready")
    return row


def write_latest_summary(
    replay_id: str,
    start_date: str,
    end_date: str,
    trading_dates: list[str],
    base_repair_date: str,
    before: dict[str, Any],
    after: dict[str, Any],
    manifests: list[Path],
    freshness: dict[str, Any],
) -> None:
    payload = {
        "schema_version": "historical_structured_source_replay_v1",
        "replay_id": replay_id,
        "pipeline_commit_sha": git_output("rev-parse", "HEAD"),
        "status": "pass",
        "start_date": start_date,
        "end_date": end_date,
        "trading_dates": trading_dates,
        "base_repair_date": base_repair_date,
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "before_tail_matrix": before,
        "after_tail_matrix": after,
        "manifest_paths": [path.as_posix() for path in manifests],
        "freshness": freshness,
        "single_commit_required": True,
        "forbidden_artifact_families": ["candidate", "model", "event", "catalyst", "pdf"],
    }
    LATEST_JSON.parent.mkdir(parents=True, exist_ok=True)
    LATEST_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    LATEST_MD.write_text(
        "\n".join(
            [
                "# Historical Structured Source Replay",
                "",
                "- status: `pass`",
                f"- trading_dates: `{', '.join(trading_dates)}`",
                f"- base_repair_date: `{base_repair_date}`",
                "- publication_status: `reconstructed_not_as_published`",
                "- as_published: `False`",
                f"- main_price_date: `{freshness.get('main_price_date', '')}`",
                f"- report_ready: `{freshness.get('report_ready', '')}`",
                "- candidate/model/event/catalyst/PDF historical publication artifacts: `not reconstructed`",
                "",
            ]
        ),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--repair-market-index-base-date", required=True)
    parser.add_argument(
        "--replay-id",
        default=os.environ.get("HISTORICAL_SOURCE_REPLAY_ID", ""),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    os.chdir(ROOT)
    start_date = parse_date(args.start_date, "--start-date")
    end_date = parse_date(args.end_date, "--end-date")
    base_repair_date = parse_date(
        args.repair_market_index_base_date,
        "--repair-market-index-base-date",
    )
    replay_id = parse_replay_id(args.replay_id)
    trading_dates = expected_trading_dates(start_date, end_date)
    if git_output("rev-parse", "--abbrev-ref", "HEAD") != "main":
        raise RuntimeError("historical structured-source replay is main-only")
    if git_output("status", "--porcelain"):
        raise RuntimeError("historical structured-source replay requires a clean checkout")

    initial = source_tail_matrix()
    validate_exact_baseline(initial, base_repair_date)
    manifests: list[Path] = []
    if base_repair_date:
        before_base = source_tail_matrix()
        twse_before = {
            path.as_posix(): canonical_target_slice(
                path,
                base_repair_date,
                pk_columns=["date", "index_code"],
                filters={"index_code": "TWSE"},
            )["slice_sha256"]
            for path in (
                Path("data/market_index_history.csv"),
                Path("data/market_index_ohlc_history.csv"),
            )
        }
        market_status = run_market_date(base_repair_date, {"TPEX"})
        after_base = source_tail_matrix()
        twse_after = {
            path.as_posix(): canonical_target_slice(
                path,
                base_repair_date,
                pk_columns=["date", "index_code"],
                filters={"index_code": "TWSE"},
            )["slice_sha256"]
            for path in (
                Path("data/market_index_history.csv"),
                Path("data/market_index_ohlc_history.csv"),
            )
        }
        if twse_after != twse_before:
            raise RuntimeError("TPEX-only base repair changed the TWSE base-date row")
        expected_market_after = {"TWSE": base_repair_date, "TPEX": base_repair_date}
        for family in ("market_index", "market_index_ohlc"):
            if after_base.get(family) != expected_market_after:
                raise RuntimeError(f"TPEX-only base repair tail mismatch: {family}={after_base.get(family)}")
        market_status["twse_base_row_sha256_before"] = twse_before
        market_status["twse_base_row_sha256_after"] = twse_after
        manifests.append(
            write_market_base_repair_manifest(
                replay_id,
                base_repair_date,
                before_base,
                after_base,
                market_status,
            )
        )

    previous_date = ""
    for target_date in trading_dates:
        if previous_date and target_date <= previous_date:
            raise RuntimeError("historical replay dates must be strictly ascending")
        before = source_tail_matrix()
        price_status = replay_price_date(target_date)
        market_status = run_market_date(target_date)
        taifex_status = run_taifex_date(target_date)
        warrant_status = run_warrant_date(target_date)
        after = source_tail_matrix()
        if after.get("daily_price") != target_date:
            raise RuntimeError(f"daily price tail did not advance to {target_date}")
        if after.get("stock_price_history", {}).get("max_date") != target_date:
            raise RuntimeError(f"stock history tail did not advance to {target_date}")
        manifests.append(
            write_day_manifest(
                replay_id,
                target_date,
                before,
                after,
                price_status,
                market_status,
                taifex_status,
                warrant_status,
            )
        )
        previous_date = target_date

    run_checked(
        [
            sys.executable,
            "scripts/validate_daily_price_history_continuity.py",
            "--main-price-date",
            end_date,
        ]
    )
    freshness = refresh_truthful_freshness(end_date)
    final = source_tail_matrix()
    write_latest_summary(
        replay_id,
        start_date,
        end_date,
        trading_dates,
        base_repair_date,
        initial,
        final,
        manifests,
        freshness,
    )
    print(
        "historical structured-source replay passed: "
        f"dates={','.join(trading_dates)} main_price_date={freshness.get('main_price_date')} "
        f"report_ready={freshness.get('report_ready')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
