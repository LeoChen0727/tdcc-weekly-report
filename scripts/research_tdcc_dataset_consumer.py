from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import pandas as pd

from tdcc_dataset_contract import (
    LATEST_MANIFEST_JSON,
    build_dataset_manifest,
    load_json,
    load_tdcc_dataset_manifest,
    normalize_code,
    normalize_date,
    normalized_text_sha256,
)


THRESHOLDS = (400, 600, 800, 1000)
CHANGE_WINDOWS = (1, 2, 3)
VOLATILE_MANIFEST_FIELDS = {"generated_at", "producer"}


@dataclass(frozen=True)
class ResearchTdccSnapshot:
    date: str
    path: Path
    sha256: str


@dataclass(frozen=True)
class ResearchTdccDatasetContract:
    dataset_id: str
    dataset_hash: str
    signal_date: str
    required_dates: tuple[str, ...]
    history_dates: tuple[str, ...]
    official_dates: tuple[str, ...]
    accepted_history_exceptions: frozenset[tuple[str, str]]
    snapshots: tuple[ResearchTdccSnapshot, ...]
    continuity_snapshots: tuple[ResearchTdccSnapshot, ...]
    manifest_path: Path


def _stable_manifest(value: dict[str, Any]) -> dict[str, Any]:
    return {key: item for key, item in value.items() if key not in VOLATILE_MANIFEST_FIELDS}


def _read_snapshot(path: Path, expected_date: str) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"canonical TDCC snapshot is missing or empty: {path.as_posix()}")
    try:
        frame = pd.read_csv(path, dtype=str, encoding="utf-8-sig", keep_default_na=False)
    except Exception as exc:
        raise RuntimeError(f"cannot read canonical TDCC snapshot {path.as_posix()}: {exc}") from exc
    required = {"date", "code", *(f"over_{threshold}_pct" for threshold in THRESHOLDS)}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"canonical TDCC snapshot lacks required columns {missing}: {path.as_posix()}")
    frame = frame.copy()
    frame["date"] = frame["date"].map(normalize_date)
    frame["code"] = frame["code"].map(normalize_code)
    observed_dates = set(frame["date"])
    if observed_dates != {expected_date}:
        raise RuntimeError(
            f"canonical TDCC snapshot date mismatch: expected {expected_date}, got {sorted(observed_dates)}"
        )
    if frame["code"].eq("").any() or frame["code"].duplicated().any():
        raise RuntimeError(f"canonical TDCC snapshot contains an empty or duplicate stock id: {path.as_posix()}")
    for threshold in THRESHOLDS:
        frame[f"over_{threshold}_pct"] = pd.to_numeric(
            frame[f"over_{threshold}_pct"], errors="coerce"
        )
    return frame.sort_values("code").reset_index(drop=True)


def load_research_tdcc_dataset_contract(
    manifest_path: Path = LATEST_MANIFEST_JSON,
) -> ResearchTdccDatasetContract:
    manifest = load_tdcc_dataset_manifest(manifest_path)
    required_dates = tuple(normalize_date(value) for value in manifest.get("required_dates", []))
    if not required_dates or list(required_dates) != sorted(set(required_dates)):
        raise RuntimeError("TDCC dataset manifest required_dates must be an ordered unique list")
    signal_date = normalize_date(manifest.get("signal_date", ""))
    if signal_date != required_dates[-1]:
        raise RuntimeError("TDCC dataset manifest signal_date must equal the final required date")

    readiness_path = Path(str(manifest.get("readiness_path", "")).strip())
    continuity_path = Path(str(manifest.get("continuity_path", "")).strip())
    readiness = load_json(readiness_path)
    continuity = load_json(continuity_path)
    if readiness.get("status") != "pass":
        raise RuntimeError(f"TDCC readiness is not pass: {readiness.get('status', '')}")
    if continuity.get("status") not in {"pass", "repaired"}:
        raise RuntimeError(f"TDCC continuity is not pass: {continuity.get('status', '')}")
    if int(continuity.get("unresolved_missing_rows", -1)) != 0:
        raise RuntimeError("TDCC continuity contains unresolved missing rows")
    if bool(continuity.get("systemic_history_exception", False)):
        raise RuntimeError("TDCC continuity contains a systemic history exception")

    official_dates = tuple(
        normalize_date(value)
        for value in readiness.get("official_dates", [])
        if len(normalize_date(value)) == 8
    )
    if not official_dates or list(official_dates) != sorted(set(official_dates)):
        raise RuntimeError("TDCC readiness official_dates must be an ordered unique list")
    continuity_dates = tuple(normalize_date(value) for value in continuity.get("required_dates", []))
    if continuity_dates != required_dates:
        raise RuntimeError("TDCC manifest and continuity required_dates do not match")
    if signal_date != official_dates[-1] or any(date not in official_dates for date in required_dates):
        raise RuntimeError("TDCC dataset required_dates do not match readiness official_dates")

    history_dates = tuple(normalize_date(value) for value in manifest.get("history_dates", []))
    raw_history_snapshots = manifest.get("history_snapshots", [])
    history_snapshot_count = int(manifest.get("history_snapshot_count", -1))
    if not history_dates or list(history_dates) != sorted(set(history_dates)):
        raise RuntimeError("TDCC dataset manifest history_dates must be an ordered unique list")
    official_history_dates = tuple(
        date for date in official_dates if history_dates[0] <= date <= signal_date
    )
    if history_dates != official_history_dates:
        raise RuntimeError(
            "TDCC dataset manifest history_dates must match the official sequence from archive start"
        )
    if signal_date != history_dates[-1]:
        raise RuntimeError("TDCC dataset manifest signal_date must equal the final history date")
    if not isinstance(raw_history_snapshots, list):
        raise RuntimeError("TDCC dataset manifest history_snapshots must be a list")
    history_snapshot_dates = tuple(
        normalize_date(item.get("date", ""))
        for item in raw_history_snapshots
        if isinstance(item, dict)
    )
    if (
        history_snapshot_dates != history_dates
        or len(raw_history_snapshots) != len(history_dates)
        or history_snapshot_count != len(history_dates)
    ):
        raise RuntimeError("TDCC dataset manifest history_snapshots must exactly match history_dates")

    raw_snapshots = manifest.get("snapshots", [])
    if not isinstance(raw_snapshots, list):
        raise RuntimeError("TDCC dataset manifest snapshots must be a list")
    snapshot_dates = tuple(
        normalize_date(item.get("date", ""))
        for item in raw_snapshots
        if isinstance(item, dict)
    )
    if snapshot_dates != required_dates or len(raw_snapshots) != len(required_dates):
        raise RuntimeError("TDCC dataset manifest snapshots must exactly match required_dates")

    snapshots: list[ResearchTdccSnapshot] = []
    snapshot_by_date: dict[str, ResearchTdccSnapshot] = {}
    for item in raw_history_snapshots:
        if not isinstance(item, dict):
            raise RuntimeError("TDCC dataset manifest history_snapshots must contain objects")
        date = normalize_date(item.get("date", ""))
        path = Path(str(item.get("path", "")).strip())
        expected_hash = str(item.get("sha256", "")).strip()
        actual_hash = normalized_text_sha256(path)
        if actual_hash != expected_hash:
            raise RuntimeError(
                f"canonical TDCC snapshot hash mismatch: {path.as_posix()} expected={expected_hash} actual={actual_hash}"
            )
        frame = _read_snapshot(path, date)
        if len(frame) != int(item.get("row_count", -1)):
            raise RuntimeError(f"canonical TDCC snapshot row_count mismatch: {path.as_posix()}")
        snapshot = ResearchTdccSnapshot(date=date, path=path, sha256=expected_hash)
        snapshots.append(snapshot)
        snapshot_by_date[date] = snapshot

    continuity_snapshots: list[ResearchTdccSnapshot] = []
    for item in raw_snapshots:
        date = normalize_date(item.get("date", ""))
        history_snapshot = snapshot_by_date.get(date)
        if history_snapshot is None:
            raise RuntimeError(f"TDCC continuity snapshot is absent from full history: {date}")
        if (
            Path(str(item.get("path", "")).strip()) != history_snapshot.path
            or str(item.get("sha256", "")).strip() != history_snapshot.sha256
        ):
            raise RuntimeError(f"TDCC continuity/full-history snapshot mismatch: {date}")
        continuity_snapshots.append(history_snapshot)

    expected = build_dataset_manifest(
        readiness_path=readiness_path,
        continuity_path=continuity_path,
        history_dir=Path(str(manifest.get("canonical_source_root", "")).strip()),
        generated_at=str(manifest.get("generated_at", "")),
        producer={str(key): str(value) for key, value in dict(manifest.get("producer", {})).items()},
    )
    expected_stable = _stable_manifest(expected)
    actual_stable = _stable_manifest(manifest)
    mismatched_common_fields = [
        key for key, value in expected_stable.items() if actual_stable.get(key) != value
    ]
    if mismatched_common_fields:
        raise RuntimeError("TDCC dataset manifest does not match canonical snapshot contents")

    accepted: set[tuple[str, str]] = set()
    for item in manifest.get("accepted_history_exceptions", []):
        if not isinstance(item, dict):
            raise RuntimeError("TDCC accepted_history_exceptions must contain objects")
        accepted.add((normalize_date(item.get("date", "")), normalize_code(item.get("stock_id", ""))))

    return ResearchTdccDatasetContract(
        dataset_id=str(manifest["dataset_id"]),
        dataset_hash=str(manifest.get("dataset_hash", "")),
        signal_date=signal_date,
        required_dates=required_dates,
        history_dates=history_dates,
        official_dates=official_dates,
        accepted_history_exceptions=frozenset(accepted),
        snapshots=tuple(snapshots),
        continuity_snapshots=tuple(continuity_snapshots),
        manifest_path=manifest_path,
    )


def load_canonical_tdcc_snapshots(
    contract: ResearchTdccDatasetContract,
    *,
    max_dates: int | None = None,
) -> list[tuple[str, pd.DataFrame]]:
    snapshots = list(contract.snapshots)
    if max_dates and max_dates > 0:
        snapshots = snapshots[-max_dates:]
    return [(item.date, _read_snapshot(item.path, item.date)) for item in snapshots]


def build_canonical_tdcc_history(
    contract: ResearchTdccDatasetContract,
) -> pd.DataFrame:
    snapshots = load_canonical_tdcc_snapshots(contract)
    rows_by_date: dict[str, dict[str, pd.Series]] = {
        date: {str(row["code"]): row for _, row in frame.iterrows()}
        for date, frame in snapshots
    }
    rows: list[dict[str, Any]] = []
    stock_ids = sorted({stock_id for by_stock in rows_by_date.values() for stock_id in by_stock})
    for stock_id in stock_ids:
        streak = 0
        for position, date in enumerate(contract.history_dates):
            row = rows_by_date.get(date, {}).get(stock_id)
            if row is None:
                streak = 0
                if (date, stock_id) in contract.accepted_history_exceptions:
                    item: dict[str, Any] = {
                        "as_of_date": date,
                        "stock_id": stock_id,
                        "stock_name": "",
                        "source_tdcc_dataset_id": contract.dataset_id,
                        "tdcc_consecutive_up_weeks": 0,
                        "all_thresholds_up": False,
                        "high_thresholds_up": False,
                        "four_thresholds_sync_up": False,
                        "tdcc_continuity_status": "accepted_history_exception",
                        "tdcc_missing_official_dates": date,
                    }
                    for threshold in THRESHOLDS:
                        item[f"over_{threshold}_ratio"] = math.nan
                        for weeks in CHANGE_WINDOWS:
                            item[f"over_{threshold}_change_{weeks}w"] = math.nan
                    rows.append(item)
                continue
            item: dict[str, Any] = {
                "as_of_date": date,
                "stock_id": stock_id,
                "stock_name": str(row.get("name", "")),
                "source_tdcc_dataset_id": contract.dataset_id,
            }
            one_week_changes: dict[int, float] = {}
            for threshold in THRESHOLDS:
                ratio = _as_float(row.get(f"over_{threshold}_pct"))
                item[f"over_{threshold}_ratio"] = ratio
                for weeks in CHANGE_WINDOWS:
                    change = math.nan
                    if position >= weeks:
                        previous_date = contract.history_dates[position - weeks]
                        previous_row = rows_by_date.get(previous_date, {}).get(stock_id)
                        if previous_row is not None:
                            previous = _as_float(previous_row.get(f"over_{threshold}_pct"))
                            if not math.isnan(ratio) and not math.isnan(previous):
                                change = ratio - previous
                    item[f"over_{threshold}_change_{weeks}w"] = change
                    if weeks == 1:
                        one_week_changes[threshold] = change
            improved = any(not math.isnan(value) and value > 0 for value in one_week_changes.values())
            streak = streak + 1 if improved else 0
            item["tdcc_consecutive_up_weeks"] = streak
            item["all_thresholds_up"] = all(
                not math.isnan(value) and value > 0 for value in one_week_changes.values()
            )
            item["high_thresholds_up"] = any(
                not math.isnan(one_week_changes[threshold]) and one_week_changes[threshold] > 0
                for threshold in (800, 1000)
            )
            item["four_thresholds_sync_up"] = item["all_thresholds_up"]
            missing_dates = sorted(
                date_value
                for date_value, exception_stock_id in contract.accepted_history_exceptions
                if exception_stock_id == stock_id
            )
            item["tdcc_continuity_status"] = (
                "accepted_history_exception" if missing_dates else "complete"
            )
            item["tdcc_missing_official_dates"] = "|".join(missing_dates)
            rows.append(item)
    return pd.DataFrame(rows).sort_values(["stock_id", "as_of_date"]).reset_index(drop=True)


def require_dataset_id(
    frame: pd.DataFrame,
    contract: ResearchTdccDatasetContract,
    *,
    label: str,
) -> None:
    if frame.empty:
        raise RuntimeError(f"{label} is empty")
    if "source_tdcc_dataset_id" not in frame.columns:
        raise RuntimeError(f"{label} lacks source_tdcc_dataset_id")
    values = sorted({str(value).strip() for value in frame["source_tdcc_dataset_id"] if str(value).strip()})
    if values != [contract.dataset_id]:
        raise RuntimeError(
            f"{label} source_tdcc_dataset_id mismatch: expected {contract.dataset_id}, got {values}"
        )


def attach_dataset_id(
    frames: Iterable[pd.DataFrame],
    contract: ResearchTdccDatasetContract,
) -> None:
    for frame in frames:
        if not frame.empty:
            frame["source_tdcc_dataset_id"] = contract.dataset_id


def _as_float(value: Any) -> float:
    try:
        if value is None or str(value).strip() == "":
            return math.nan
        return float(value)
    except (TypeError, ValueError):
        return math.nan
