from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from research_tdcc_dataset_consumer import (  # noqa: E402
    build_canonical_tdcc_history,
    load_research_tdcc_dataset_contract,
)
from tdcc_dataset_contract import build_dataset_manifest  # noqa: E402


DATES = ("20260703", "20260709", "20260717")


def write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def write_snapshot(path: Path, date: str, rows: list[tuple[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "date",
                "code",
                "name",
                "over_400_pct",
                "over_600_pct",
                "over_800_pct",
                "over_1000_pct",
            ],
        )
        writer.writeheader()
        for stock_id, base in rows:
            writer.writerow(
                {
                    "date": date,
                    "code": stock_id,
                    "name": f"stock-{stock_id}",
                    "over_400_pct": base,
                    "over_600_pct": base - 5,
                    "over_800_pct": base - 10,
                    "over_1000_pct": base - 15,
                }
            )


def fixture_contract(
    tmp_path: Path,
    *,
    missing_middle: bool = False,
    earlier_official_dates: tuple[str, ...] = (),
) -> Path:
    latest = tmp_path / "output/latest"
    history = tmp_path / "output/history/tdcc"
    readiness = latest / "readiness.json"
    continuity = latest / "continuity.json"
    write_json(
        readiness,
        {
            "status": "pass",
            "selected_official_date": "20260717",
            "official_dates": [*earlier_official_dates, *DATES],
            "official_date_source": "https://example.test/tdcc",
        },
    )
    write_json(
        continuity,
        {
            "status": "pass",
            "signal_date": "20260717",
            "required_dates": list(DATES),
            "current_stock_count": 2,
            "unresolved_missing_rows": 0,
            "systemic_history_exception": False,
            "confirmed_history_exceptions": (
                [{"date": "20260709", "stock_id": "1002"}] if missing_middle else []
            ),
        },
    )
    write_snapshot(history / "tdcc_holder_ratio_20260703.csv", "20260703", [("1001", 50), ("1002", 50)])
    write_snapshot(
        history / "tdcc_holder_ratio_20260709.csv",
        "20260709",
        [("1001", 51)] if missing_middle else [("1001", 51), ("1002", 51)],
    )
    write_snapshot(history / "tdcc_holder_ratio_20260717.csv", "20260717", [("1001", 52), ("1002", 52)])
    manifest = build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
        generated_at="fixture",
        producer={"workflow": "fixture"},
    )
    manifest_path = latest / "tdcc_dataset_manifest_latest.json"
    write_json(manifest_path, manifest)
    return manifest_path


def test_research_consumer_tracks_special_official_period_and_dataset_id(tmp_path: Path) -> None:
    manifest_path = fixture_contract(
        tmp_path,
        earlier_official_dates=("20260618", "20260626"),
    )

    contract = load_research_tdcc_dataset_contract(manifest_path)
    history = build_canonical_tdcc_history(contract)

    assert contract.required_dates == DATES
    assert contract.history_dates == DATES
    assert "20260709" in contract.required_dates
    assert set(history["source_tdcc_dataset_id"]) == {contract.dataset_id}
    latest = history[(history["stock_id"] == "1001") & (history["as_of_date"] == "20260717")].iloc[0]
    assert float(latest["over_400_change_1w"]) == pytest.approx(1.0)
    assert int(latest["tdcc_consecutive_up_weeks"]) == 2


def test_research_consumer_rejects_manifest_snapshot_hash_mismatch(tmp_path: Path) -> None:
    manifest_path = fixture_contract(tmp_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["history_snapshots"][1]["sha256"] = "0" * 64
    write_json(manifest_path, manifest)

    with pytest.raises(RuntimeError, match="snapshot hash mismatch"):
        load_research_tdcc_dataset_contract(manifest_path)


def test_research_consumer_requires_full_history_contract_fields(tmp_path: Path) -> None:
    manifest_path = fixture_contract(tmp_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.pop("history_snapshots")
    write_json(manifest_path, manifest)

    with pytest.raises(RuntimeError, match="history_snapshots"):
        load_research_tdcc_dataset_contract(manifest_path)


def test_approved_middle_gap_cannot_create_fake_one_week_change_or_streak(tmp_path: Path) -> None:
    manifest_path = fixture_contract(tmp_path, missing_middle=True)

    contract = load_research_tdcc_dataset_contract(manifest_path)
    history = build_canonical_tdcc_history(contract)

    missing = history[(history["stock_id"] == "1002") & (history["as_of_date"] == "20260709")].iloc[0]
    assert missing["tdcc_continuity_status"] == "accepted_history_exception"
    assert math.isnan(float(missing["over_400_change_1w"]))
    assert int(missing["tdcc_consecutive_up_weeks"]) == 0
    latest = history[(history["stock_id"] == "1002") & (history["as_of_date"] == "20260717")].iloc[0]
    assert math.isnan(float(latest["over_400_change_1w"]))
    assert float(latest["over_400_change_2w"]) == pytest.approx(2.0)
    assert int(latest["tdcc_consecutive_up_weeks"]) == 0
    assert latest["tdcc_continuity_status"] == "accepted_history_exception"
    assert latest["tdcc_missing_official_dates"] == "20260709"
