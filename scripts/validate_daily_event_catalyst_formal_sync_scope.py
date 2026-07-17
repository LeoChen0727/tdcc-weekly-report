from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "daily_event_catalyst_formal_sync_scope_v1"
ALLOWED_MUTABLE_MODEL_IDS = frozenset({"revenue_unreacted_range"})
FORMAL_SIGNAL_ARTIFACTS = (
    "output/latest/daily_candidate_model_signals_latest.csv",
    "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv",
)


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_scope_snapshot(root: Path) -> tuple[dict[str, Any], list[str]]:
    artifacts: dict[str, dict[str, Any]] = {}
    errors: list[str] = []

    for relative_path in FORMAL_SIGNAL_ARTIFACTS:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing formal signal artifact: {relative_path}")
            continue

        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = list(reader.fieldnames or [])
            if "model_id" not in columns:
                errors.append(f"formal signal artifact missing model_id: {relative_path}")
                continue

            protected_rows: list[str] = []
            protected_model_ids: set[str] = set()
            mutable_row_count = 0
            total_row_count = 0
            for row in reader:
                total_row_count += 1
                normalized = {column: str(row.get(column) or "") for column in columns}
                model_id = normalized["model_id"].strip()
                if model_id in ALLOWED_MUTABLE_MODEL_IDS:
                    mutable_row_count += 1
                    continue
                protected_model_ids.add(model_id or "__blank__")
                protected_rows.append(
                    json.dumps(
                        normalized,
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    )
                )

        protected_rows.sort()
        protected_payload = {
            "columns": columns,
            "rows": protected_rows,
        }
        artifacts[relative_path] = {
            "columns": columns,
            "total_row_count": total_row_count,
            "mutable_row_count": mutable_row_count,
            "protected_row_count": len(protected_rows),
            "protected_model_ids": sorted(protected_model_ids),
            "protected_sha256": _canonical_sha256(protected_payload),
        }

    aggregate_payload = {
        path: {
            "columns": record["columns"],
            "protected_row_count": record["protected_row_count"],
            "protected_sha256": record["protected_sha256"],
        }
        for path, record in sorted(artifacts.items())
    }
    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "allowed_mutable_model_ids": sorted(ALLOWED_MUTABLE_MODEL_IDS),
        "artifact_count": len(artifacts),
        "aggregate_sha256": _canonical_sha256(aggregate_payload),
        "artifacts": artifacts,
    }
    return snapshot, errors


def compare_scope_snapshots(before: dict[str, Any], after: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if before.get("schema_version") != SCHEMA_VERSION:
        errors.append("formal sync scope snapshot schema_version mismatch")
    expected_mutable = sorted(ALLOWED_MUTABLE_MODEL_IDS)
    if before.get("allowed_mutable_model_ids") != expected_mutable:
        errors.append("formal sync scope snapshot allowed_mutable_model_ids mismatch")

    before_artifacts = before.get("artifacts")
    after_artifacts = after.get("artifacts")
    if not isinstance(before_artifacts, dict):
        errors.append("formal sync scope before snapshot artifacts must be an object")
        before_artifacts = {}
    if not isinstance(after_artifacts, dict):
        errors.append("formal sync scope after snapshot artifacts must be an object")
        after_artifacts = {}

    for relative_path in sorted(set(before_artifacts) | set(after_artifacts)):
        if relative_path not in before_artifacts:
            errors.append(f"protected formal signal artifact added: {relative_path}")
            continue
        if relative_path not in after_artifacts:
            errors.append(f"protected formal signal artifact removed: {relative_path}")
            continue
        before_record = before_artifacts[relative_path]
        after_record = after_artifacts[relative_path]
        if before_record.get("columns") != after_record.get("columns"):
            errors.append(f"formal signal schema drift outside approved sync scope: {relative_path}")
        if before_record.get("protected_row_count") != after_record.get("protected_row_count"):
            errors.append(f"non-revenue formal signal row-count drift: {relative_path}")
        if before_record.get("protected_sha256") != after_record.get("protected_sha256"):
            errors.append(f"non-revenue formal signal hash drift: {relative_path}")

    return errors


def _write_snapshot(path: Path, snapshot: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fail closed when event-catalyst formal sync changes non-revenue model rows."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write-snapshot", type=Path)
    action.add_argument("--compare-snapshot", type=Path)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()

    snapshot, errors = build_scope_snapshot(args.repo_root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if args.write_snapshot is not None:
        _write_snapshot(args.write_snapshot, snapshot)
        print(
            "event-catalyst formal sync scope snapshot captured "
            f"artifacts={snapshot['artifact_count']} "
            f"aggregate_sha256={snapshot['aggregate_sha256']}"
        )
        return 0

    try:
        before = json.loads(args.compare_snapshot.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: unable to read formal sync scope snapshot: {exc}")
        return 1

    compare_errors = compare_scope_snapshots(before, snapshot)
    if compare_errors:
        for error in compare_errors:
            print(f"ERROR: {error}")
        return 1

    print(f"formal_sync_scope_before_sha256={before.get('aggregate_sha256', '')}")
    print(f"formal_sync_scope_after_sha256={snapshot['aggregate_sha256']}")
    for relative_path, record in sorted(snapshot["artifacts"].items()):
        print(
            "formal_sync_scope_artifact "
            f"path={relative_path} protected_rows={record['protected_row_count']} "
            f"mutable_rows={record['mutable_row_count']} "
            f"protected_sha256={record['protected_sha256']}"
        )
    print("event-catalyst formal sync scope validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
