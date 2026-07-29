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
import build_data_freshness_latest as freshness_builder  # noqa: E402


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
    price_history_high_water_date: str = "",
    expected_protected_fingerprints: dict[str, dict[str, Any]] | None = None,
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
    if payload.get("price_history_high_water_date", "") != price_history_high_water_date:
        errors.append(f"{path}: price_history_high_water_date mismatch")
    protected_fingerprints = payload.get("protected_price_history_fingerprints") or {}
    if price_history_high_water_date:
        if protected_fingerprints != (expected_protected_fingerprints or {}):
            errors.append(f"{path}: protected price/history fingerprint mismatch")
    elif protected_fingerprints:
        errors.append(f"{path}: legacy replay must not claim protected price/history fingerprints")
    try:
        replay.validate_replay_day_tail_matrix(
            payload.get("after_tail_matrix") or {},
            target_date,
            price_history_high_water_date,
        )
    except Exception as exc:
        errors.append(f"{path}: after_tail_matrix contract failed: {exc}")
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
            if source_id == "official_daily_price":
                expected_tail = price_history_high_water_date or target_date
                if row.get("after_tail") != expected_tail:
                    errors.append(f"{path}: official_daily_price after_tail mismatch")
                if price_history_high_water_date:
                    if row.get("before_tail") != price_history_high_water_date:
                        errors.append(f"{path}: preserved official_daily_price before_tail mismatch")
                    if row.get("price_history_high_water_date") != price_history_high_water_date:
                        errors.append(f"{path}: official_daily_price high-water evidence mismatch")
                    preserved = row.get("preserved_target_slice_evidence") or {}
                    if preserved.get("mode") != "preserve_existing_price_history":
                        errors.append(f"{path}: preserved daily-price mode evidence missing")
                    if preserved.get("price_history_high_water_date") != price_history_high_water_date:
                        errors.append(f"{path}: preserved daily-price high-water date mismatch")
                    fetched_sha = str(preserved.get("fetched_target_slice_sha256", ""))
                    if not re.fullmatch(r"[0-9a-f]{64}", fetched_sha):
                        errors.append(f"{path}: preserved daily-price fetched slice SHA invalid")
                    dated_shas = preserved.get("preserved_daily_price_target_slice_sha256") or {}
                    expected_dated_paths = {
                        f"data/daily_price/daily_price_{target_date}.csv",
                        f"data/daily_price/{target_date}.csv",
                    }
                    if set(dated_shas) != expected_dated_paths or set(dated_shas.values()) != {
                        fetched_sha
                    }:
                        errors.append(f"{path}: preserved daily-price canonical parity evidence mismatch")
                    try:
                        committed_dated_shas = replay.validate_daily_price_canonical_legacy_pair(
                            target_date
                        )
                    except Exception as exc:
                        errors.append(
                            f"{path}: preserved daily-price committed parity recompute failed: {exc}"
                        )
                    else:
                        if (
                            committed_dated_shas != dated_shas
                            or set(committed_dated_shas.values()) != {fetched_sha}
                        ):
                            errors.append(
                                f"{path}: preserved fetched SHA is not bound to committed target CSVs"
                            )
                    history_components = [
                        component
                        for component in expected_evidence.get("components", [])
                        if component.get("component_id") == "stock_history_target_slices"
                    ]
                    if len(history_components) != 1 or preserved.get(
                        "preserved_stock_history_target_slice_manifest_sha256"
                    ) != history_components[0].get("slice_manifest_sha256"):
                        errors.append(f"{path}: preserved stock-history target-slice parity mismatch")
                    if len(history_components) == 1 and int(
                        preserved.get("preserved_stock_history_target_slice_rows", -1)
                    ) != int(history_components[0].get("row_count", -2)):
                        errors.append(
                            f"{path}: preserved stock-history target-slice row count mismatch"
                        )
                    try:
                        expected_coverage = replay.validate_stock_history_date_coverage(
                            target_date,
                            manifest_end_date=price_history_high_water_date,
                        )
                    except Exception as exc:
                        errors.append(
                            f"{path}: preserved stock-history coverage recompute failed: {exc}"
                        )
                    else:
                        if preserved.get("stock_history_coverage") != expected_coverage:
                            errors.append(
                                f"{path}: preserved stock-history coverage evidence mismatch"
                            )
                elif row.get("price_history_high_water_date") or row.get(
                    "preserved_target_slice_evidence"
                ):
                    errors.append(f"{path}: legacy official_daily_price contains preserve evidence")
            elif source_id == "market_index":
                if row.get("after_tail") != {"TWSE": target_date, "TPEX": target_date}:
                    errors.append(f"{path}: market_index after_tail mismatch")
            elif source_id == "taifex_futures_options_vix":
                if set((row.get("after_tail") or {}).values()) != {target_date}:
                    errors.append(f"{path}: TAIFEX after_tail mismatch")
                if stored_evidence.get("taifex_raw_history_parity") != expected_evidence.get(
                    "taifex_raw_history_parity"
                ):
                    errors.append(f"{path}: TAIFEX dated raw/history parity evidence mismatch")
            elif source_id == "official_warrant_daily":
                if row.get("after_tail") != target_date:
                    errors.append(f"{path}: warrant after_tail mismatch")
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


def validate_freshness_frame(
    freshness: pd.DataFrame,
    end_date: str,
    price_history_high_water_date: str = "",
) -> list[str]:
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
    if price_history_high_water_date:
        expected_fields = {
            "main_price_date_source": "historical_replay_override",
            "historical_replay_main_price_date": end_date,
            "expected_price_history_high_water_date": price_history_high_water_date,
            "actual_stock_price_history_date": price_history_high_water_date,
            "official_price_fetch_date": end_date,
            "raw_official_price_fetch_date": end_date,
        }
        for field, expected in expected_fields.items():
            if row.get(field) != expected:
                errors.append(
                    f"data freshness {field} mismatch: {row.get(field)} != {expected}"
                )
    return errors


def validate_continuity_report(
    report: dict[str, Any],
    end_date: str,
    expected_dates: list[str],
    replay_trading_dates: list[str],
) -> list[str]:
    errors: list[str] = []
    if report.get("status") != "pass":
        errors.append("daily price history continuity status must be pass")
    if report.get("main_price_date") != end_date:
        errors.append("daily price history continuity main_price_date mismatch")
    if report.get("expected_trading_dates") != expected_dates:
        errors.append("daily price history continuity expected_trading_dates mismatch")
    missing_replay_dates = [
        date for date in replay_trading_dates if date not in set(expected_dates)
    ]
    if missing_replay_dates:
        errors.append(
            "daily price history continuity omits replay trading dates: "
            f"{missing_replay_dates}"
        )
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
    price_history_high_water_date: str = "",
) -> list[str]:
    errors: list[str] = []
    trading_dates = replay.expected_trading_dates(start_date, end_date)
    protected_fingerprints = (
        replay.protected_price_history_fingerprints()
        if price_history_high_water_date
        else {}
    )
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
    if latest.get("price_history_high_water_date", "") != price_history_high_water_date:
        errors.append("historical replay latest price_history_high_water_date mismatch")
    latest_fingerprints_before = (
        latest.get("protected_price_history_fingerprints_before") or {}
    )
    latest_fingerprints_after = latest.get("protected_price_history_fingerprints_after") or {}
    if price_history_high_water_date:
        if latest_fingerprints_before != protected_fingerprints:
            errors.append("historical replay latest protected before fingerprint mismatch")
        if latest_fingerprints_after != protected_fingerprints:
            errors.append("historical replay latest protected after fingerprint mismatch")
    elif latest_fingerprints_before or latest_fingerprints_after:
        errors.append("legacy historical replay must not claim protected price/history fingerprints")
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
                price_history_high_water_date,
                protected_fingerprints,
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
        if price_history_high_water_date:
            try:
                replay.validate_stock_history_date_coverage(
                    target_date,
                    manifest_end_date=price_history_high_water_date,
                )
            except Exception as exc:
                errors.append(
                    f"preserved stock-history target/high-water coverage failed for "
                    f"{target_date}: {exc}"
                )
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
        try:
            replay.validate_taifex_raw_history_parity(target_date)
        except Exception as exc:
            errors.append(
                f"TAIFEX dated raw/history parity failed for {target_date}: {exc}"
            )

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
    try:
        replay.validate_replay_day_tail_matrix(
            tails,
            end_date,
            price_history_high_water_date,
        )
    except Exception as exc:
        errors.append(f"final mixed-tail contract failed: {exc}")
    if price_history_high_water_date:
        try:
            replay.validate_stock_history_date_coverage(
                price_history_high_water_date,
                manifest_end_date=price_history_high_water_date,
            )
        except Exception as exc:
            errors.append(f"price/history high-water paired coverage failed: {exc}")

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
    errors.extend(
        validate_freshness_frame(
            freshness,
            end_date,
            price_history_high_water_date,
        )
    )
    if price_history_high_water_date:
        try:
            freshness_builder.validate_historical_replay_freshness_prerequisites(
                end_date,
                price_history_high_water_date,
            )
        except Exception as exc:
            errors.append(f"official replay latest/status contract failed: {exc}")
    continuity_report = load_json(Path("output/latest/daily_price_history_continuity_latest.json"))
    try:
        lookback_days = int(continuity_report.get("lookback_days", -1))
        if lookback_days < 1:
            raise ValueError("lookback_days must be positive")
        non_trading_days = replay.continuity.load_non_trading_days(
            replay.ROOT,
            replay.continuity.NON_TRADING_DAYS,
        )
        expected_continuity_dates = replay.continuity.expected_trading_dates(
            end_date,
            lookback_days,
            non_trading_days,
        )
    except Exception as exc:
        errors.append(f"daily price history continuity date recompute failed: {exc}")
        expected_continuity_dates = []
    errors.extend(
        validate_continuity_report(
            continuity_report,
            end_date,
            expected_continuity_dates,
            trading_dates,
        )
    )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--price-history-high-water-date", default="")
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
    price_history_high_water_date = replay.parse_optional_date(
        args.price_history_high_water_date,
        "--price-history-high-water-date",
    )
    if price_history_high_water_date and price_history_high_water_date <= end_date:
        raise RuntimeError("--price-history-high-water-date must be later than --end-date")
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
        price_history_high_water_date,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "historical structured-source replay validated: "
        f"start={start_date} end={end_date} base_repair={base or 'none'} "
        f"price_history_high_water={price_history_high_water_date or 'legacy'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
