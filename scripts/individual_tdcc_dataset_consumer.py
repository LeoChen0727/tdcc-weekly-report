from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

from tdcc_dataset_contract import (
    LATEST_MANIFEST_JSON,
    load_json,
    load_tdcc_dataset_manifest,
    normalize_code,
    normalize_date,
)


THRESHOLDS = (400, 600, 800, 1000)
CHANGE_WINDOWS = (1, 2, 3)
DERIVED_BOOLEAN_FIELDS = (
    "all_thresholds_up",
    "high_thresholds_up",
    "four_thresholds_sync_up",
)
FLOAT_TOLERANCE = 1e-9


@dataclass(frozen=True)
class IndividualTdccDatasetContract:
    dataset_id: str
    signal_date: str
    required_dates: tuple[str, ...]
    official_dates: tuple[str, ...]
    current_stock_ids: frozenset[str]
    accepted_history_exceptions: frozenset[tuple[str, str]]
    manifest_path: Path


@dataclass(frozen=True)
class StockTdccAssessment:
    stock_id: str
    dataset_id: str
    signal_date: str
    row_count: int
    latest_date: str
    is_current_tdcc_universe: bool
    continuity_status: str
    missing_official_dates: tuple[str, ...]


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"required TDCC source is missing or empty: {path.as_posix()}")
    try:
        return pd.read_csv(path, dtype=str, encoding="utf-8-sig").fillna("")
    except Exception as exc:
        raise RuntimeError(f"cannot read TDCC source {path.as_posix()}: {exc}") from exc


def load_individual_tdcc_dataset_contract(
    path: Path = LATEST_MANIFEST_JSON,
) -> IndividualTdccDatasetContract:
    manifest = load_tdcc_dataset_manifest(path)
    required_dates = tuple(normalize_date(value) for value in manifest.get("required_dates", []))
    if not required_dates or list(required_dates) != sorted(set(required_dates)):
        raise RuntimeError("TDCC dataset manifest required_dates must be an ordered unique list")
    signal_date = normalize_date(manifest.get("signal_date", ""))
    if signal_date != required_dates[-1]:
        raise RuntimeError("TDCC dataset manifest signal_date must equal the final required date")

    readiness_path = Path(str(manifest.get("readiness_path", "")).strip())
    readiness = load_json(readiness_path)
    official_dates = tuple(
        normalize_date(value)
        for value in readiness.get("official_dates", [])
        if len(normalize_date(value)) == 8
    )
    if not official_dates or list(official_dates) != sorted(set(official_dates)):
        raise RuntimeError("TDCC readiness official_dates must be an ordered unique list")
    if signal_date != official_dates[-1] or any(date not in official_dates for date in required_dates):
        raise RuntimeError("TDCC dataset required_dates do not match readiness official_dates")

    snapshots = manifest.get("snapshots", [])
    signal_snapshot = next(
        (
            item
            for item in snapshots
            if isinstance(item, dict) and normalize_date(item.get("date", "")) == signal_date
        ),
        None,
    )
    if signal_snapshot is None:
        raise RuntimeError("TDCC dataset manifest does not identify the signal-date snapshot")
    signal_path = Path(str(signal_snapshot.get("path", "")).strip())
    signal_frame = _read_csv(signal_path)
    if "code" not in signal_frame.columns or "date" not in signal_frame.columns:
        raise RuntimeError(f"TDCC signal snapshot lacks code/date columns: {signal_path.as_posix()}")
    signal_dates = {normalize_date(value) for value in signal_frame["date"].tolist()}
    if signal_dates != {signal_date}:
        raise RuntimeError(
            f"TDCC signal snapshot date mismatch: expected {signal_date}, got {sorted(signal_dates)}"
        )
    current_stock_ids = frozenset(normalize_code(value) for value in signal_frame["code"].tolist())
    if "" in current_stock_ids or len(current_stock_ids) != len(signal_frame):
        raise RuntimeError("TDCC signal snapshot contains an empty or duplicate stock id")
    if len(current_stock_ids) != int(manifest.get("current_stock_count", -1)):
        raise RuntimeError("TDCC dataset manifest current_stock_count does not match signal snapshot")

    accepted: set[tuple[str, str]] = set()
    for item in manifest.get("accepted_history_exceptions", []):
        if not isinstance(item, dict):
            raise RuntimeError("TDCC dataset manifest accepted_history_exceptions must contain objects")
        date = normalize_date(item.get("date", ""))
        stock_id = normalize_code(item.get("stock_id", ""))
        if date not in required_dates or stock_id not in current_stock_ids:
            raise RuntimeError(
                f"TDCC dataset manifest contains an invalid accepted history exception: {date}:{stock_id}"
            )
        accepted.add((date, stock_id))

    return IndividualTdccDatasetContract(
        dataset_id=str(manifest["dataset_id"]),
        signal_date=signal_date,
        required_dates=required_dates,
        official_dates=official_dates,
        current_stock_ids=current_stock_ids,
        accepted_history_exceptions=frozenset(accepted),
        manifest_path=path,
    )


def _as_float(value: Any) -> float:
    try:
        if value is None or str(value).strip() == "":
            return math.nan
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def _as_bool(value: Any) -> bool | None:
    text = "" if value is None else str(value).strip().lower()
    if text in {"true", "1", "yes"}:
        return True
    if text in {"false", "0", "no"}:
        return False
    return None


def _numeric_matches(actual: Any, expected: float) -> bool:
    actual_number = _as_float(actual)
    if math.isnan(expected):
        return math.isnan(actual_number)
    return not math.isnan(actual_number) and math.isclose(
        actual_number,
        expected,
        rel_tol=0.0,
        abs_tol=FLOAT_TOLERANCE,
    )


def _expected_change(
    rows_by_date: dict[str, pd.Series],
    required_dates: tuple[str, ...],
    date: str,
    ratio_col: str,
    weeks: int,
) -> float:
    position = required_dates.index(date)
    if position < weeks:
        return math.nan
    prior_date = required_dates[position - weeks]
    if prior_date not in rows_by_date:
        return math.nan
    current = _as_float(rows_by_date[date].get(ratio_col))
    previous = _as_float(rows_by_date[prior_date].get(ratio_col))
    if math.isnan(current) or math.isnan(previous):
        return math.nan
    return current - previous


def _expected_streak(
    rows_by_date: dict[str, pd.Series],
    required_dates: tuple[str, ...],
    date: str,
) -> int:
    streak = 0
    position = required_dates.index(date)
    while position > 0:
        current_date = required_dates[position]
        prior_date = required_dates[position - 1]
        if current_date not in rows_by_date or prior_date not in rows_by_date:
            break
        improved = any(
            not math.isnan(_as_float(rows_by_date[current_date].get(f"over_{threshold}_ratio")))
            and not math.isnan(_as_float(rows_by_date[prior_date].get(f"over_{threshold}_ratio")))
            and _as_float(rows_by_date[current_date].get(f"over_{threshold}_ratio"))
            > _as_float(rows_by_date[prior_date].get(f"over_{threshold}_ratio"))
            for threshold in THRESHOLDS
        )
        if not improved:
            break
        streak += 1
        position -= 1
    return streak


def prepare_and_validate_stock_tdcc_history(
    stock_id: str,
    frame: pd.DataFrame,
    contract: IndividualTdccDatasetContract,
) -> tuple[pd.DataFrame, StockTdccAssessment]:
    stock_id = normalize_code(stock_id)
    current = stock_id in contract.current_stock_ids
    if frame.empty:
        if current:
            raise RuntimeError(
                f"{stock_id}: current TDCC dataset stock is missing its materialized history view"
            )
        return frame.copy(), StockTdccAssessment(
            stock_id=stock_id,
            dataset_id=contract.dataset_id,
            signal_date=contract.signal_date,
            row_count=0,
            latest_date="",
            is_current_tdcc_universe=False,
            continuity_status="not_current_tdcc_universe",
            missing_official_dates=(),
        )

    result = frame.copy()
    date_col = "as_of_date" if "as_of_date" in result.columns else "date" if "date" in result.columns else ""
    if not date_col:
        raise RuntimeError(f"{stock_id}: TDCC materialized history lacks as_of_date/date")
    result["as_of_date"] = result[date_col].map(normalize_date)
    if result["as_of_date"].eq("").any():
        raise RuntimeError(f"{stock_id}: TDCC materialized history contains an invalid date")
    if result["as_of_date"].duplicated().any():
        duplicates = sorted(result.loc[result["as_of_date"].duplicated(False), "as_of_date"].unique())
        raise RuntimeError(f"{stock_id}: TDCC materialized history contains duplicate dates: {duplicates}")
    if "stock_id" in result.columns:
        observed_ids = {normalize_code(value) for value in result["stock_id"].tolist()}
        if observed_ids != {stock_id}:
            raise RuntimeError(
                f"{stock_id}: TDCC materialized history contains different stock ids: {sorted(observed_ids)}"
            )
    else:
        result["stock_id"] = stock_id
    result = result.sort_values("as_of_date").reset_index(drop=True)

    actual_dates = set(result["as_of_date"].tolist())
    missing_dates: tuple[str, ...] = ()
    continuity_status = "not_current_tdcc_universe"
    if current:
        approved_for_stock = {
            date
            for date, exception_stock_id in contract.accepted_history_exceptions
            if exception_stock_id == stock_id
        }
        missing = set(contract.required_dates) - actual_dates
        unapproved_missing = sorted(missing - approved_for_stock)
        if unapproved_missing:
            raise RuntimeError(
                f"{stock_id}: TDCC materialized history is missing required official dates: {unapproved_missing}"
            )
        exception_rows_present = sorted(approved_for_stock & actual_dates)
        if exception_rows_present:
            raise RuntimeError(
                f"{stock_id}: TDCC materialized history contradicts accepted missing-row exceptions: "
                f"{exception_rows_present}"
            )
        if contract.signal_date not in actual_dates:
            raise RuntimeError(
                f"{stock_id}: TDCC materialized history does not contain signal_date={contract.signal_date}"
            )
        future_dates = sorted(date for date in actual_dates if date > contract.signal_date)
        if future_dates:
            raise RuntimeError(
                f"{stock_id}: TDCC materialized history contains dates after signal_date: {future_dates}"
            )
        missing_dates = tuple(sorted(missing))
        continuity_status = "accepted_history_exception" if missing_dates else "complete"

        rows_by_date = {
            str(row["as_of_date"]): row
            for _, row in result.iterrows()
        }
        errors: list[str] = []
        for date in contract.required_dates:
            if date not in rows_by_date:
                continue
            row_index = int(result.index[result["as_of_date"].eq(date)][0])
            one_week_changes: dict[int, float] = {}
            for threshold in THRESHOLDS:
                ratio_col = f"over_{threshold}_ratio"
                if ratio_col not in result.columns or math.isnan(_as_float(rows_by_date[date].get(ratio_col))):
                    errors.append(f"{date}:{ratio_col}=missing")
                    continue
                for weeks in CHANGE_WINDOWS:
                    field = f"over_{threshold}_change_{weeks}w"
                    if field not in result.columns:
                        errors.append(f"{date}:{field}=column_missing")
                        continue
                    expected = _expected_change(rows_by_date, contract.official_dates, date, ratio_col, weeks)
                    if not _numeric_matches(rows_by_date[date].get(field), expected):
                        errors.append(
                            f"{date}:{field}=expected({expected if not math.isnan(expected) else 'blank'})"
                        )
                    result.at[row_index, field] = expected
                    if weeks == 1:
                        one_week_changes[threshold] = expected

            expected_streak = _expected_streak(rows_by_date, contract.official_dates, date)
            if "tdcc_consecutive_up_weeks" not in result.columns or not _numeric_matches(
                rows_by_date[date].get("tdcc_consecutive_up_weeks"), float(expected_streak)
            ):
                errors.append(f"{date}:tdcc_consecutive_up_weeks=expected({expected_streak})")
            result.at[row_index, "tdcc_consecutive_up_weeks"] = expected_streak

            expected_all = all(
                threshold in one_week_changes
                and not math.isnan(one_week_changes[threshold])
                and one_week_changes[threshold] > 0
                for threshold in THRESHOLDS
            )
            expected_high = any(
                threshold in one_week_changes
                and not math.isnan(one_week_changes[threshold])
                and one_week_changes[threshold] > 0
                for threshold in (800, 1000)
            )
            expected_booleans = {
                "all_thresholds_up": expected_all,
                "high_thresholds_up": expected_high,
                "four_thresholds_sync_up": expected_all,
            }
            for field in DERIVED_BOOLEAN_FIELDS:
                if field not in result.columns or _as_bool(rows_by_date[date].get(field)) != expected_booleans[field]:
                    errors.append(f"{date}:{field}=expected({str(expected_booleans[field]).lower()})")
                result.at[row_index, field] = expected_booleans[field]
        if errors:
            raise RuntimeError(
                f"{stock_id}: TDCC materialized derived fields do not match the canonical official-date sequence: "
                + ", ".join(errors[:20])
            )

    result["source_tdcc_dataset_id"] = contract.dataset_id
    result["tdcc_continuity_status"] = continuity_status
    result["tdcc_missing_official_dates"] = "|".join(missing_dates)
    latest_date = max(actual_dates) if actual_dates else ""
    return result, StockTdccAssessment(
        stock_id=stock_id,
        dataset_id=contract.dataset_id,
        signal_date=contract.signal_date,
        row_count=len(result),
        latest_date=latest_date,
        is_current_tdcc_universe=current,
        continuity_status=continuity_status,
        missing_official_dates=missing_dates,
    )
