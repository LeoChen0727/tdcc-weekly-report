from __future__ import annotations

import csv
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


SCHEMA_VERSION = "tdcc_dataset_manifest_v1"
HASH_MODE = "utf8_text_lf_normalized_sha256"
CANONICAL_HISTORY_DIR = Path("output/history/tdcc")
READINESS_JSON = Path("output/latest/tdcc_weekly_data_readiness_latest.json")
CONTINUITY_JSON = Path("output/latest/tdcc_weekly_history_continuity_latest.json")
LATEST_MANIFEST_JSON = Path("output/latest/tdcc_dataset_manifest_latest.json")
TAIPEI = ZoneInfo("Asia/Taipei")


def normalize_date(value: Any) -> str:
    digits = "".join(character for character in str(value or "") if character.isdigit())
    return digits[:8] if len(digits) >= 8 else digits


def normalize_code(value: Any) -> str:
    text = str(value or "").strip().replace(".0", "")
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalized_text_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def canonical_json_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"required TDCC contract artifact is missing: {path.as_posix()}")
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read TDCC contract artifact {path.as_posix()}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"TDCC contract artifact must be a JSON object: {path.as_posix()}")
    return value


def read_snapshot(path: Path, expected_date: str) -> tuple[list[dict[str, str]], set[str]]:
    if not path.exists() or path.stat().st_size <= 0:
        raise RuntimeError(f"canonical TDCC snapshot is missing or empty: {path.as_posix()}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing_fields = sorted({"code", "date"} - fields)
        if missing_fields:
            raise RuntimeError(
                f"canonical TDCC snapshot lacks required columns {missing_fields}: {path.as_posix()}"
            )
        rows = [{str(key): str(value or "") for key, value in row.items()} for row in reader]
    if not rows:
        raise RuntimeError(f"canonical TDCC snapshot has no data rows: {path.as_posix()}")

    codes: list[str] = []
    wrong_dates: set[str] = set()
    for row in rows:
        code = normalize_code(row.get("code", ""))
        date = normalize_date(row.get("date", ""))
        if not code:
            raise RuntimeError(f"canonical TDCC snapshot contains an empty stock code: {path.as_posix()}")
        codes.append(code)
        if date != expected_date:
            wrong_dates.add(date or "empty")
    if wrong_dates:
        raise RuntimeError(
            f"canonical TDCC snapshot contains dates other than {expected_date}: "
            f"{sorted(wrong_dates)} in {path.as_posix()}"
        )
    duplicates = sorted({code for code in codes if codes.count(code) > 1})
    if duplicates:
        raise RuntimeError(
            f"canonical TDCC snapshot contains duplicate stock codes: {duplicates[:10]} "
            f"in {path.as_posix()}"
        )
    return rows, set(codes)


def accepted_exception_pairs(continuity: dict[str, Any]) -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for item in continuity.get("confirmed_history_exceptions", []):
        if not isinstance(item, dict):
            continue
        date = normalize_date(item.get("date", ""))
        stock_id = normalize_code(item.get("stock_id", ""))
        if date and stock_id:
            pairs.add((date, stock_id))
    return pairs


def producer_metadata() -> dict[str, str]:
    return {
        "workflow": os.environ.get("GITHUB_WORKFLOW", "local"),
        "run_id": os.environ.get("GITHUB_RUN_ID", ""),
        "source_ref": os.environ.get("GITHUB_REF_NAME", ""),
        "source_commit_sha": os.environ.get("GITHUB_SHA", ""),
    }


def build_dataset_manifest(
    *,
    readiness_path: Path = READINESS_JSON,
    continuity_path: Path = CONTINUITY_JSON,
    history_dir: Path = CANONICAL_HISTORY_DIR,
    generated_at: str | None = None,
    producer: dict[str, str] | None = None,
) -> dict[str, Any]:
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

    signal_date = normalize_date(readiness.get("selected_official_date", ""))
    if len(signal_date) != 8:
        raise RuntimeError("TDCC readiness selected_official_date is invalid")
    if normalize_date(continuity.get("signal_date", "")) != signal_date:
        raise RuntimeError("TDCC readiness and continuity signal_date do not match")

    official_dates = sorted(
        {
            normalize_date(value)
            for value in readiness.get("official_dates", [])
            if len(normalize_date(value)) == 8
        }
    )
    required_dates = [normalize_date(value) for value in continuity.get("required_dates", [])]
    if not required_dates or required_dates != sorted(set(required_dates)):
        raise RuntimeError("TDCC continuity required_dates must be a non-empty ordered unique list")
    if signal_date != required_dates[-1] or any(date not in official_dates for date in required_dates):
        raise RuntimeError("TDCC continuity required_dates do not match the official date sequence")

    signal_path = history_dir / f"tdcc_holder_ratio_{signal_date}.csv"
    signal_rows, current_codes = read_snapshot(signal_path, signal_date)
    expected_current_count = int(continuity.get("current_stock_count", 0))
    if expected_current_count != len(current_codes):
        raise RuntimeError(
            "TDCC continuity current_stock_count does not match the canonical signal snapshot: "
            f"{expected_current_count} != {len(current_codes)}"
        )

    accepted_pairs = accepted_exception_pairs(continuity)
    snapshots: list[dict[str, Any]] = []
    observed_missing_pairs: set[tuple[str, str]] = set()
    for date in required_dates:
        path = history_dir / f"tdcc_holder_ratio_{date}.csv"
        rows, codes = (signal_rows, current_codes) if date == signal_date else read_snapshot(path, date)
        missing_codes = sorted(current_codes - codes)
        extra_codes = sorted(codes - current_codes)
        missing_pairs = {(date, stock_id) for stock_id in missing_codes}
        observed_missing_pairs.update(missing_pairs)
        unapproved_missing = sorted(missing_pairs - accepted_pairs)
        if unapproved_missing:
            raise RuntimeError(
                "canonical TDCC snapshot is missing current-universe stocks without approved exceptions: "
                + ", ".join(f"{date}:{stock_id}" for _, stock_id in unapproved_missing[:20])
            )
        snapshots.append(
            {
                "date": date,
                "path": path.as_posix(),
                "row_count": len(rows),
                "stock_count": len(codes),
                "current_universe_missing_count": len(missing_codes),
                "current_universe_missing_stock_ids": missing_codes,
                "current_universe_extra_count": len(extra_codes),
                "coverage_status": "accepted_exceptions" if missing_codes else "complete",
                "sha256": normalized_text_sha256(path),
            }
        )

    orphan_exceptions = sorted(accepted_pairs - observed_missing_pairs)
    if orphan_exceptions:
        raise RuntimeError(
            "TDCC continuity contains approved exceptions that are not missing from canonical snapshots: "
            + ", ".join(f"{date}:{stock_id}" for date, stock_id in orphan_exceptions[:20])
        )

    identity_payload = {
        "schema_version": SCHEMA_VERSION,
        "signal_date": signal_date,
        "official_date_source": str(readiness.get("official_date_source", "")),
        "required_dates": required_dates,
        "current_stock_count": len(current_codes),
        "snapshots": [
            {
                "date": item["date"],
                "row_count": item["row_count"],
                "stock_count": item["stock_count"],
                "current_universe_missing_stock_ids": item["current_universe_missing_stock_ids"],
                "sha256": item["sha256"],
            }
            for item in snapshots
        ],
        "accepted_history_exceptions": [
            {"date": date, "stock_id": stock_id}
            for date, stock_id in sorted(accepted_pairs)
        ],
    }
    dataset_hash = canonical_json_sha256(identity_payload)
    dataset_id = f"tdcc-{signal_date}-{dataset_hash[:16]}"
    return {
        "status": "pass",
        "schema_version": SCHEMA_VERSION,
        "dataset_id": dataset_id,
        "dataset_hash": dataset_hash,
        "hash_mode": HASH_MODE,
        "generated_at": generated_at or datetime.now(TAIPEI).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
        "signal_date": signal_date,
        "official_date_source": str(readiness.get("official_date_source", "")),
        "canonical_source_root": history_dir.as_posix(),
        "readiness_path": readiness_path.as_posix(),
        "continuity_path": continuity_path.as_posix(),
        "required_dates": required_dates,
        "current_stock_count": len(current_codes),
        "snapshot_count": len(snapshots),
        "snapshots": snapshots,
        "accepted_history_exceptions": identity_payload["accepted_history_exceptions"],
        "producer": producer if producer is not None else producer_metadata(),
    }


def versioned_manifest_path(signal_date: str, history_dir: Path = CANONICAL_HISTORY_DIR) -> Path:
    return history_dir / f"tdcc_dataset_manifest_{normalize_date(signal_date)}.json"


def write_dataset_manifest(
    manifest: dict[str, Any],
    *,
    latest_path: Path = LATEST_MANIFEST_JSON,
    history_dir: Path = CANONICAL_HISTORY_DIR,
) -> tuple[Path, Path]:
    signal_date = normalize_date(manifest.get("signal_date", ""))
    if len(signal_date) != 8:
        raise RuntimeError("cannot write TDCC dataset manifest with invalid signal_date")
    versioned_path = versioned_manifest_path(signal_date, history_dir)
    payload = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    for path in (latest_path, versioned_path):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding="utf-8")
    return latest_path, versioned_path


def load_tdcc_dataset_manifest(path: Path = LATEST_MANIFEST_JSON) -> dict[str, Any]:
    manifest = load_json(path)
    if manifest.get("status") != "pass":
        raise RuntimeError(f"TDCC dataset manifest is not pass: {manifest.get('status', '')}")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise RuntimeError(f"unsupported TDCC dataset manifest schema: {manifest.get('schema_version', '')}")
    signal_date = normalize_date(manifest.get("signal_date", ""))
    dataset_id = str(manifest.get("dataset_id", "")).strip()
    if len(signal_date) != 8 or not dataset_id.startswith(f"tdcc-{signal_date}-"):
        raise RuntimeError("TDCC dataset manifest identity is invalid")
    manifest["signal_date"] = signal_date
    manifest["dataset_id"] = dataset_id
    return manifest
