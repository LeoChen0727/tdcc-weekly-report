from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import replay_historical_structured_sources as replay  # noqa: E402


REQUIRED_SOURCES = {
    "official_daily_price",
    "market_index",
    "taifex_futures_options_vix",
    "official_warrant_daily",
}


def validate_pipeline_commit_sha(
    payload: dict[str, Any],
    label: str,
    expected_sha: str,
) -> list[str]:
    if payload.get("pipeline_commit_sha") != expected_sha:
        return [f"{label}: pipeline_commit_sha does not match replay base code SHA"]
    return []


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"missing replay artifact: {path}")
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"replay artifact must be an object: {path}")
    return payload


def csv_dates(path: Path, date_col: str = "date") -> set[str]:
    if not path.exists():
        return set()
    frame = pd.read_csv(path, dtype=str)
    if date_col not in frame.columns:
        return set()
    return {
        re.sub(r"[^0-9]", "", str(value))[:8]
        for value in frame[date_col].tolist()
        if re.fullmatch(r"20\d{6}", re.sub(r"[^0-9]", "", str(value))[:8])
    }


def validate_manifest(
    path: Path,
    target_date: str,
    replay_id: str,
    expected_pipeline_sha: str,
) -> list[str]:
    errors: list[str] = []
    payload = load_json(path)
    if payload.get("schema_version") != "historical_structured_source_replay_v1":
        errors.append(f"{path}: invalid schema_version")
    if payload.get("report_date") != target_date:
        errors.append(f"{path}: report_date mismatch")
    if payload.get("replay_id") != replay_id:
        errors.append(f"{path}: replay_id mismatch")
    errors.extend(
        validate_pipeline_commit_sha(
            payload,
            str(path),
            expected_pipeline_sha,
        )
    )
    if payload.get("publication_status") != "reconstructed_not_as_published":
        errors.append(f"{path}: publication_status must be reconstructed_not_as_published")
    if payload.get("as_published") is not False:
        errors.append(f"{path}: as_published must be false")
    sources = payload.get("sources") or []
    source_ids = {str(row.get("source_id", "")) for row in sources if isinstance(row, dict)}
    if source_ids != REQUIRED_SOURCES:
        errors.append(f"{path}: source set mismatch {sorted(source_ids)}")
    for row in sources:
        source_id = row.get("source_id", "")
        for field in ("raw_sha256", "normalized_sha256", "output_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", str(row.get(field, ""))):
                errors.append(f"{path}: {source_id} missing valid {field}")
        if row.get("requested_dates") != [target_date]:
            errors.append(f"{path}: {source_id} requested_dates mismatch")
        if row.get("observed_dates") != [target_date]:
            errors.append(f"{path}: {source_id} observed_dates mismatch")
        if row.get("fallback_used") is not False:
            errors.append(f"{path}: {source_id} fallback_used must be false")
        if row.get("future_rows_used") is not False:
            errors.append(f"{path}: {source_id} future_rows_used must be false")
        if row.get("as_published") is not False:
            errors.append(f"{path}: {source_id} as_published must be false")
        if row.get("validation_status") != "pass":
            errors.append(f"{path}: {source_id} validation_status must be pass")
        if row.get("pk_unique") is not True:
            errors.append(f"{path}: {source_id} pk_unique must be true")
        accepted = row.get("accepted_source_responses") or []
        if not isinstance(accepted, list) or not accepted:
            errors.append(f"{path}: {source_id} accepted source response evidence missing")
        for index, response in enumerate(accepted):
            for field in ("raw_sha256", "normalized_sha256"):
                if not re.fullmatch(r"[0-9a-f]{64}", str(response.get(field, ""))):
                    errors.append(f"{path}: {source_id} accepted response {index} invalid {field}")
        if source_id in {"official_daily_price", "official_warrant_daily"}:
            for index, response in enumerate(accepted):
                if response.get("observed_response_dates") != [target_date]:
                    errors.append(
                        f"{path}: {source_id} accepted response {index} observed date mismatch"
                    )
                if response.get("exact_date_match") is not True:
                    errors.append(
                        f"{path}: {source_id} accepted response {index} lacks exact-date match"
                    )
        if source_id == "official_warrant_daily":
            families = set()
            logical_groups = set()
            for response in accepted:
                source_name = str(response.get("source_name", ""))
                if source_name.startswith("TWSE_WARRANT_STOCK_"):
                    families.add("mapping")
                if source_name.startswith("TWSE_MI_INDEX_"):
                    families.add("quote")
                logical_groups.add(str(response.get("logical_group", "")))
                if response.get("accepted") is not True:
                    errors.append(f"{path}: warrant accepted response lacks accepted=true")
                if int(response.get("accepted_rows", 0) or 0) < 1:
                    errors.append(f"{path}: warrant accepted response lacks parsed rows")
            if families != {"mapping", "quote"}:
                errors.append(f"{path}: warrant accepted mapping/quote evidence incomplete")
            if logical_groups != {"mapping", "quote-0999", "quote-0999P"}:
                errors.append(f"{path}: warrant accepted logical source groups incomplete")
        try:
            expected_evidence = replay.build_source_output_evidence(source_id, target_date)
        except Exception as exc:
            errors.append(f"{path}: {source_id} output parity recompute failed: {exc}")
        else:
            if row.get("output_sha256") != expected_evidence.get("output_sha256"):
                errors.append(f"{path}: {source_id} target-slice output_sha256 parity mismatch")
            if int(row.get("row_count", -1)) != int(expected_evidence.get("row_count", -2)):
                errors.append(f"{path}: {source_id} target-slice row_count parity mismatch")
            stored_evidence = row.get("output_evidence") or {}
            if stored_evidence.get("future_rows_excluded_from_slice") is not True:
                errors.append(f"{path}: {source_id} must record future rows excluded from slice")
    return errors


def validate_context_latest(path: Path, date_col: str, end_date: str, minimum_rows: int) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing historical chart context latest: {path}"]
    frame = pd.read_csv(path, dtype=str)
    if date_col not in frame.columns:
        try:
            date_col = replay.detect_date_column(frame, path)
        except Exception:
            return [f"historical chart context missing {date_col}: {path}"]
    dates = frame[date_col].astype(str).str.replace(r"[^0-9]", "", regex=True).str[:8]
    if len(frame) < minimum_rows:
        errors.append(f"historical chart context too short: {path} rows={len(frame)}")
    if dates.max() != end_date:
        errors.append(f"historical chart context max date mismatch: {path} {dates.max()} != {end_date}")
    if dates.gt(end_date).any():
        errors.append(f"historical chart context contains future rows: {path}")
    return errors


def validate_final_stock_history_coverage(target_date: str) -> list[str]:
    errors: list[str] = []
    try:
        stock_ids = replay.supported_daily_stock_ids(target_date)
    except Exception as exc:
        return [f"cannot resolve supported stock universe for {target_date}: {exc}"]
    for stock_id in stock_ids:
        path = Path("data/stock_price_history") / f"{stock_id}.csv"
        if target_date not in csv_dates(path):
            errors.append(f"stock history missing {target_date}: {stock_id}")
            if len(errors) >= 30:
                break
    return errors


def validate_exact_dated_artifact(path: Path, target_date: str, label: str) -> list[str]:
    if csv_dates(path) != {target_date}:
        return [f"{label} date mismatch: {path}"]
    return []


def validate_freshness_frame(freshness: pd.DataFrame, end_date: str) -> list[str]:
    errors: list[str] = []
    if len(freshness) != 1:
        return ["data freshness must have exactly one row"]
    row = freshness.iloc[0]
    if row.get("main_price_date") != end_date:
        errors.append("data freshness main_price_date mismatch")
    if str(row.get("report_ready", "")).lower() == "true":
        errors.append("data freshness must keep stale publish artifacts not ready")
    if str(row.get("daily_pdf_ready", "")).lower() == "true":
        errors.append("data freshness must keep stale daily PDFs not ready")
    return errors


def validate_base_twse_sha_payload(base: dict[str, Any]) -> list[str]:
    twse_before = base.get("twse_base_row_sha256_before") or {}
    twse_after = base.get("twse_base_row_sha256_after") or {}
    if not twse_before or twse_before != twse_after:
        return ["market index base repair TWSE row SHA preservation mismatch"]
    return []


def validate(
    start_date: str,
    end_date: str,
    base_repair_date: str,
    replay_id: str,
    expected_pipeline_sha: str,
) -> list[str]:
    errors: list[str] = []
    trading_dates = replay.expected_trading_dates(start_date, end_date)
    latest = load_json(replay.LATEST_JSON)
    if latest.get("status") != "pass":
        errors.append("historical replay latest status must be pass")
    if latest.get("trading_dates") != trading_dates:
        errors.append("historical replay latest trading_dates mismatch")
    if latest.get("publication_status") != "reconstructed_not_as_published":
        errors.append("historical replay latest publication_status mismatch")
    if latest.get("as_published") is not False:
        errors.append("historical replay latest as_published must be false")
    if latest.get("base_repair_date", "") != base_repair_date:
        errors.append("historical replay latest base_repair_date mismatch")
    if latest.get("replay_id") != replay_id:
        errors.append("historical replay latest replay_id mismatch")
    errors.extend(
        validate_pipeline_commit_sha(
            latest,
            "historical replay latest",
            expected_pipeline_sha,
        )
    )

    expected_manifest_paths = [
        (replay.REPLAY_HISTORY / replay_id / base_repair_date / "market_index_base_repair_manifest.json").as_posix(),
        *[
            (replay.REPLAY_HISTORY / replay_id / target_date / "structured_source_manifest.json").as_posix()
            for target_date in trading_dates
        ],
    ]
    if latest.get("manifest_paths") != expected_manifest_paths:
        errors.append("historical replay latest manifest_paths mismatch")

    for target_date in trading_dates:
        manifest = replay.REPLAY_HISTORY / replay_id / target_date / "structured_source_manifest.json"
        errors.extend(
            validate_manifest(
                manifest,
                target_date,
                replay_id,
                expected_pipeline_sha,
            )
        )
        errors.extend(
            validate_exact_dated_artifact(
                Path(f"data/daily_price/daily_price_{target_date}.csv"),
                target_date,
                "official daily price file",
            )
        )
        errors.extend(
            validate_exact_dated_artifact(
                Path(f"output/history/warrant_daily/warrant_daily_{target_date}.csv"),
                target_date,
                "official warrant history",
            )
        )
        errors.extend(
            validate_exact_dated_artifact(
                Path(f"output/history/warrant_flow/warrant_flow_{target_date}.csv"),
                target_date,
                "official warrant flow history",
            )
        )
        errors.extend(validate_final_stock_history_coverage(target_date))
        for market_path in (
            Path("data/market_index_history.csv"),
            Path("data/market_index_ohlc_history.csv"),
        ):
            frame = pd.read_csv(market_path, dtype=str)
            exact = frame[frame["date"].astype(str).eq(target_date)]
            if len(exact) != 2 or set(exact["index_code"].astype(str)) != {"TWSE", "TPEX"}:
                errors.append(f"market index exact-date pair missing: {market_path} {target_date}")
        for source_path, date_col in (
            (path, pk_columns[0])
            for path, pk_columns in replay.TAIFEX_HISTORY_SPECS.values()
        ):
            if target_date not in csv_dates(source_path, date_col):
                errors.append(f"TAIFEX source history missing target date: {source_path} {target_date}")

    if base_repair_date:
        base_path = (
            replay.REPLAY_HISTORY
            / replay_id
            / base_repair_date
            / "market_index_base_repair_manifest.json"
        )
        base = load_json(base_path)
        if base.get("publication_status") != "reconstructed_not_as_published":
            errors.append("market index base repair publication_status mismatch")
        if base.get("replay_id") != replay_id:
            errors.append("market index base repair replay_id mismatch")
        errors.extend(
            validate_pipeline_commit_sha(
                base,
                "market index base repair",
                expected_pipeline_sha,
            )
        )
        twse_before = base.get("twse_base_row_sha256_before") or {}
        twse_after = base.get("twse_base_row_sha256_after") or {}
        twse_payload_errors = validate_base_twse_sha_payload(base)
        errors.extend(twse_payload_errors)
        if not twse_payload_errors:
            current_twse = {
                path.as_posix(): replay.canonical_target_slice(
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
            if current_twse != twse_after:
                errors.append("market index base repair current TWSE row SHA parity mismatch")
        base_sources = base.get("sources") or []
        if len(base_sources) != 1 or base_sources[0].get("source_id") != "market_index_base_repair":
            errors.append("market index base repair source evidence mismatch")
        else:
            base_row = base_sources[0]
            expected_base_evidence = replay.build_source_output_evidence(
                "market_index_base_repair",
                base_repair_date,
                market_index_codes={"TPEX"},
            )
            if base_row.get("output_sha256") != expected_base_evidence.get("output_sha256"):
                errors.append("market index base repair target-slice output parity mismatch")
        for market_path in (
            Path("data/market_index_history.csv"),
            Path("data/market_index_ohlc_history.csv"),
        ):
            frame = pd.read_csv(market_path, dtype=str)
            exact = frame[
                frame["date"].astype(str).eq(base_repair_date)
                & frame["index_code"].astype(str).eq("TPEX")
            ]
            if len(exact) != 1:
                errors.append(f"TPEX base repair missing exact date: {market_path} {base_repair_date}")

    tails = replay.source_tail_matrix()
    if tails.get("daily_price") != end_date:
        errors.append(f"daily price tail mismatch: {tails.get('daily_price')} != {end_date}")
    if tails.get("stock_price_history", {}).get("max_date") != end_date:
        errors.append("stock price history tail mismatch")
    for family in ("market_index", "market_index_ohlc"):
        if tails.get(family) != {"TWSE": end_date, "TPEX": end_date}:
            errors.append(f"{family} tail mismatch: {tails.get(family)}")
    if set(tails.get("taifex", {}).values()) != {end_date}:
        errors.append(f"TAIFEX tail mismatch: {tails.get('taifex')}")
    if tails.get("warrant_daily") != end_date:
        errors.append(f"warrant daily tail mismatch: {tails.get('warrant_daily')}")
    if tails.get("warrant_flow") != end_date:
        errors.append(f"warrant flow tail mismatch: {tails.get('warrant_flow')}")

    errors.extend(
        validate_context_latest(
            Path("output/latest/futures_options_put_call_ratio_latest.csv"),
            replay.TAIFEX_HISTORY_SPECS["put_call_ratio"][1][0],
            end_date,
            minimum_rows=20,
        )
    )
    errors.extend(
        validate_context_latest(
            Path("output/latest/taiwan_vix_latest.csv"),
            "date",
            end_date,
            minimum_rows=60,
        )
    )
    freshness = pd.read_csv(replay.FRESHNESS_CSV, dtype=str).fillna("")
    errors.extend(validate_freshness_frame(freshness, end_date))
    continuity_report = load_json(Path("output/latest/daily_price_history_continuity_latest.json"))
    if continuity_report.get("status") != "pass":
        errors.append("daily price history continuity status must be pass")
    if continuity_report.get("main_price_date") != end_date:
        errors.append("daily price history continuity main_price_date mismatch")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--repair-market-index-base-date", required=True)
    parser.add_argument(
        "--replay-id",
        default=os.environ.get("HISTORICAL_SOURCE_REPLAY_ID", ""),
    )
    parser.add_argument(
        "--expected-pipeline-sha",
        default=os.environ.get("REPLAY_BASE_SHA", ""),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    start_date = replay.parse_date(args.start_date, "--start-date")
    end_date = replay.parse_date(args.end_date, "--end-date")
    base = replay.parse_date(
        args.repair_market_index_base_date,
        "--repair-market-index-base-date",
    )
    replay_id = replay.parse_replay_id(args.replay_id)
    expected_pipeline_sha = str(args.expected_pipeline_sha).strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", expected_pipeline_sha):
        raise RuntimeError("--expected-pipeline-sha must be an exact 40-character Git SHA")
    errors = validate(
        start_date,
        end_date,
        base,
        replay_id,
        expected_pipeline_sha,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "historical structured-source replay validated: "
        f"start={start_date} end={end_date} base_repair={base or 'none'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
