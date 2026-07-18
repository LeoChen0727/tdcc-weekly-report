from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

from scripts import tdcc_dataset_contract as contract


def write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def write_snapshot(path: Path, date: str, codes: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["date", "code", "over_400_pct"])
        writer.writeheader()
        for index, code in enumerate(codes):
            writer.writerow({"date": date, "code": code, "over_400_pct": str(50 + index)})


def fixture_paths(tmp_path: Path, *, missing_middle: bool = False, approve_missing: bool = False) -> tuple[Path, Path, Path]:
    readiness = tmp_path / "output/latest/readiness.json"
    continuity = tmp_path / "output/latest/continuity.json"
    history = tmp_path / "output/history/tdcc"
    history_dates = ["20260618", "20260626", "20260703", "20260709", "20260717"]
    required_dates = history_dates[-3:]
    write_json(
        readiness,
        {
            "status": "pass",
            "selected_official_date": "20260717",
            "official_dates": history_dates,
            "official_date_source": "https://example.test/tdcc",
        },
    )
    write_json(
        continuity,
        {
            "status": "pass",
            "signal_date": "20260717",
            "required_dates": required_dates,
            "current_stock_count": 2,
            "unresolved_missing_rows": 0,
            "systemic_history_exception": False,
            "confirmed_history_exceptions": (
                [{"date": "20260709", "stock_id": "1002"}] if approve_missing else []
            ),
        },
    )
    write_snapshot(history / "tdcc_holder_ratio_20260618.csv", "20260618", ["1001"])
    write_snapshot(history / "tdcc_holder_ratio_20260626.csv", "20260626", ["1001", "1002"])
    write_snapshot(history / "tdcc_holder_ratio_20260703.csv", "20260703", ["1001", "1002"])
    write_snapshot(
        history / "tdcc_holder_ratio_20260709.csv",
        "20260709",
        ["1001"] if missing_middle else ["1001", "1002"],
    )
    write_snapshot(history / "tdcc_holder_ratio_20260717.csv", "20260717", ["1001", "1002"])
    return readiness, continuity, history


def test_dataset_id_is_deterministic_and_content_addressed(tmp_path: Path) -> None:
    readiness, continuity, history = fixture_paths(tmp_path)

    first = contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
        generated_at="first",
        producer={"run_id": "1"},
    )
    second = contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
        generated_at="second",
        producer={"run_id": "2"},
    )

    assert first["dataset_id"] == second["dataset_id"]
    assert first["dataset_hash"] == second["dataset_hash"]
    assert first["signal_date"] == "20260717"
    assert first["required_dates"] == ["20260703", "20260709", "20260717"]
    assert first["history_dates"] == [
        "20260618",
        "20260626",
        "20260703",
        "20260709",
        "20260717",
    ]
    assert first["snapshot_count"] == 3
    assert first["history_snapshot_count"] == 5

    snapshot = history / "tdcc_holder_ratio_20260709.csv"
    snapshot.write_text(snapshot.read_text(encoding="utf-8").replace("51", "52"), encoding="utf-8")
    changed = contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
    )
    assert changed["dataset_id"] != first["dataset_id"]

    older_snapshot = history / "tdcc_holder_ratio_20260618.csv"
    older_snapshot.write_text(
        older_snapshot.read_text(encoding="utf-8").replace("50", "49"),
        encoding="utf-8",
    )
    changed_older_history = contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
    )
    assert changed_older_history["dataset_id"] != changed["dataset_id"]


def test_dataset_contract_rejects_unapproved_middle_period_gap(tmp_path: Path) -> None:
    readiness, continuity, history = fixture_paths(tmp_path, missing_middle=True)

    with pytest.raises(RuntimeError, match="without approved exceptions"):
        contract.build_dataset_manifest(
            readiness_path=readiness,
            continuity_path=continuity,
            history_dir=history,
        )


def test_dataset_contract_records_approved_history_exception(tmp_path: Path) -> None:
    readiness, continuity, history = fixture_paths(
        tmp_path,
        missing_middle=True,
        approve_missing=True,
    )

    manifest = contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
    )

    middle = next(item for item in manifest["snapshots"] if item["date"] == "20260709")
    assert middle["coverage_status"] == "accepted_exceptions"
    assert middle["current_universe_missing_stock_ids"] == ["1002"]
    assert manifest["accepted_history_exceptions"] == [{"date": "20260709", "stock_id": "1002"}]


def test_dataset_contract_rejects_snapshot_with_wrong_embedded_date(tmp_path: Path) -> None:
    readiness, continuity, history = fixture_paths(tmp_path)
    wrong = history / "tdcc_holder_ratio_20260709.csv"
    wrong.write_text(wrong.read_text(encoding="utf-8").replace("20260709", "20260710"), encoding="utf-8")

    with pytest.raises(RuntimeError, match="dates other than 20260709"):
        contract.build_dataset_manifest(
            readiness_path=readiness,
            continuity_path=continuity,
            history_dir=history,
        )


def test_dataset_contract_rejects_missing_official_archive_period(tmp_path: Path) -> None:
    readiness, continuity, history = fixture_paths(tmp_path)
    (history / "tdcc_holder_ratio_20260626.csv").unlink()

    with pytest.raises(RuntimeError, match="complete official date sequence"):
        contract.build_dataset_manifest(
            readiness_path=readiness,
            continuity_path=continuity,
            history_dir=history,
        )


def test_dataset_contract_preserves_history_after_official_window_rolls(tmp_path: Path) -> None:
    readiness, continuity, history = fixture_paths(tmp_path)
    previous_manifest = tmp_path / "previous_manifest.json"
    write_json(
        previous_manifest,
        {
            "history_dates": [
                "20260618",
                "20260626",
                "20260703",
                "20260709",
            ]
        },
    )
    readiness_value = json.loads(readiness.read_text(encoding="utf-8"))
    readiness_value["official_dates"] = ["20260703", "20260709", "20260717"]
    write_json(readiness, readiness_value)

    manifest = contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
        previous_manifest_path=previous_manifest,
    )
    assert manifest["history_dates"][0] == "20260618"
    assert manifest["history_snapshot_count"] == 5

    (history / "tdcc_holder_ratio_20260618.csv").unlink()
    with pytest.raises(RuntimeError, match="previous manifest"):
        contract.build_dataset_manifest(
            readiness_path=readiness,
            continuity_path=continuity,
            history_dir=history,
            previous_manifest_path=previous_manifest,
        )


def test_dataset_manifest_loader_requires_full_history_contract(tmp_path: Path) -> None:
    path = tmp_path / "manifest.json"
    write_json(
        path,
        {
            "status": "pass",
            "schema_version": contract.SCHEMA_VERSION,
            "dataset_id": "tdcc-20260717-0123456789abcdef",
            "signal_date": "20260717",
            "required_dates": ["20260717"],
            "snapshot_count": 1,
            "snapshots": [{"date": "20260717"}],
        },
    )

    with pytest.raises(RuntimeError, match="history_dates"):
        contract.load_tdcc_dataset_manifest(path)


def test_tdcc_weekly_workflow_builds_and_validates_manifest_before_report_consumer() -> None:
    workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/tdcc_weekly.yml").read_text(
        encoding="utf-8"
    )

    build_index = workflow.index("python scripts/build_tdcc_dataset_manifest.py")
    validate_index = workflow.index("python scripts/validate_tdcc_dataset_manifest.py")
    report_index = workflow.index("python scripts/build_tdcc_weekly_candidate_reports.py")

    assert build_index < validate_index < report_index
