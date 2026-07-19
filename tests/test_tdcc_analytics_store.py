from __future__ import annotations

import csv
import json
from pathlib import Path

import duckdb
import pytest

from scripts import tdcc_dataset_contract as dataset_contract
from scripts import tdcc_analytics_store as analytics


def write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def write_snapshot(path: Path, date: str, rows: list[tuple[str, str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["date", "code", "name", *analytics.RATIO_COLUMNS],
        )
        writer.writeheader()
        for code, name, base in rows:
            writer.writerow(
                {
                    "date": date,
                    "code": code,
                    "name": name,
                    "over_400_pct": base,
                    "over_600_pct": base - 1,
                    "over_800_pct": base - 2,
                    "over_1000_pct": base - 3,
                }
            )


def fixture_contract(tmp_path: Path) -> tuple[Path, Path]:
    latest = tmp_path / "output/latest"
    history = tmp_path / "output/history/tdcc"
    readiness = latest / "readiness.json"
    continuity = latest / "continuity.json"
    manifest_path = latest / "tdcc_dataset_manifest_latest.json"
    dates = ["20260703", "20260709", "20260717"]
    write_json(
        readiness,
        {
            "status": "pass",
            "selected_official_date": dates[-1],
            "official_dates": dates,
            "official_date_source": "https://example.test/tdcc",
        },
    )
    write_json(
        continuity,
        {
            "status": "pass",
            "signal_date": dates[-1],
            "required_dates": dates,
            "current_stock_count": 2,
            "unresolved_missing_rows": 0,
            "systemic_history_exception": False,
            "confirmed_history_exceptions": [{"date": "20260709", "stock_id": "1002"}],
        },
    )
    write_snapshot(
        history / "tdcc_holder_ratio_20260703.csv",
        "20260703",
        [("1001", "甲", 50.0), ("1002", "乙", 40.0)],
    )
    write_snapshot(
        history / "tdcc_holder_ratio_20260709.csv",
        "20260709",
        [("1001", "甲", 51.0)],
    )
    write_snapshot(
        history / "tdcc_holder_ratio_20260717.csv",
        "20260717",
        [("1001", "甲", 52.0), ("1002", "乙", 42.0)],
    )
    manifest = dataset_contract.build_dataset_manifest(
        readiness_path=readiness,
        continuity_path=continuity,
        history_dir=history,
        generated_at="fixture",
        producer={"run_id": "fixture"},
        previous_manifest_path=tmp_path / "missing_previous_manifest.json",
    )
    dataset_contract.write_dataset_manifest(
        manifest,
        latest_path=manifest_path,
        history_dir=history,
    )
    return manifest_path, tmp_path / "output/latest/tdcc_analytics"


def test_build_and_validate_analytics_store(tmp_path: Path) -> None:
    source_manifest, output_dir = fixture_contract(tmp_path)

    built = analytics.build_analytics_store(
        source_manifest_path=source_manifest,
        output_dir=output_dir,
        generated_at="fixture",
    )
    result = analytics.validate_analytics_store(
        source_manifest_path=source_manifest,
        output_dir=output_dir,
    )

    assert built["source_tdcc_dataset_id"].startswith("tdcc-20260717-")
    assert built["history_snapshot_count"] == 3
    assert built["row_count"] == 5
    assert result["status"] == "pass"
    assert (output_dir / analytics.PARQUET_FILENAME).stat().st_size > 0
    assert (output_dir / analytics.DUCKDB_FILENAME).stat().st_size > 0

    connection = duckdb.connect(str(output_dir / analytics.DUCKDB_FILENAME), read_only=True)
    try:
        missing_previous = connection.execute(
            """
            SELECT previous_snapshot_date, previous_period_index, previous_over_400_pct
            FROM tdcc_holder_ratio_latest_comparison
            WHERE code = '1002'
            """
        ).fetchone()
        assert missing_previous == (None, None, None)
        exact_previous = connection.execute(
            """
            SELECT previous_snapshot_date, previous_period_index, change_over_400_pct
            FROM tdcc_holder_ratio_latest_comparison
            WHERE code = '1001'
            """
        ).fetchone()
        assert exact_previous == ("20260709", 1, 1.0)
    finally:
        connection.close()


def test_builder_rejects_snapshot_hash_drift(tmp_path: Path) -> None:
    source_manifest, output_dir = fixture_contract(tmp_path)
    manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
    snapshot = Path(manifest["history_snapshots"][1]["path"])
    snapshot.write_text(
        snapshot.read_text(encoding="utf-8").replace("51.0", "53.0"),
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="hash does not match"):
        analytics.build_analytics_store(
            source_manifest_path=source_manifest,
            output_dir=output_dir,
        )


def test_validator_rejects_foreign_dataset_manifest(tmp_path: Path) -> None:
    source_manifest, output_dir = fixture_contract(tmp_path)
    analytics.build_analytics_store(
        source_manifest_path=source_manifest,
        output_dir=output_dir,
    )
    value = json.loads(source_manifest.read_text(encoding="utf-8"))
    value["dataset_id"] = "tdcc-20260717-ffffffffffffffff"
    source_manifest.write_text(json.dumps(value), encoding="utf-8")

    with pytest.raises(RuntimeError, match="source_tdcc_dataset_id mismatch"):
        analytics.validate_analytics_store(
            source_manifest_path=source_manifest,
            output_dir=output_dir,
        )


def test_validator_rejects_source_snapshot_drift_after_build(tmp_path: Path) -> None:
    source_manifest, output_dir = fixture_contract(tmp_path)
    analytics.build_analytics_store(
        source_manifest_path=source_manifest,
        output_dir=output_dir,
    )
    manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
    snapshot = Path(manifest["history_snapshots"][0]["path"])
    snapshot.write_text(
        snapshot.read_text(encoding="utf-8").replace("50.0", "54.0"),
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="snapshot hash drift"):
        analytics.validate_analytics_store(
            source_manifest_path=source_manifest,
            output_dir=output_dir,
        )


def test_validator_rejects_parquet_drift(tmp_path: Path) -> None:
    source_manifest, output_dir = fixture_contract(tmp_path)
    analytics.build_analytics_store(
        source_manifest_path=source_manifest,
        output_dir=output_dir,
    )
    parquet_path = output_dir / analytics.PARQUET_FILENAME
    parquet_path.write_bytes(parquet_path.read_bytes() + b"drift")

    with pytest.raises(RuntimeError, match="parquet size mismatch"):
        analytics.validate_analytics_store(
            source_manifest_path=source_manifest,
            output_dir=output_dir,
        )


def test_tdcc_workflows_build_and_validate_analytics_store() -> None:
    root = Path(__file__).resolve().parents[1]
    production = (root / ".github/workflows/tdcc_weekly.yml").read_text(encoding="utf-8")
    pr_validation = (root / ".github/workflows/tdcc_weekly_pr_validation.yml").read_text(
        encoding="utf-8"
    )

    build = "python scripts/build_tdcc_analytics_store.py"
    validate = "python scripts/validate_tdcc_analytics_store.py"
    assert production.index(build) < production.index(validate)
    assert production.index(validate) < production.index(
        "Build TDCC weekly report from continuous history"
    )
    assert build in pr_validation
    assert validate in pr_validation
    assert "$RUNNER_TEMP/tdcc_analytics" in pr_validation
    assert "duckdb==1.5.4" in production
    assert "duckdb==1.5.4" in pr_validation
    assert "rm -rf docs/latest/tdcc_analytics" in production
    assert (
        "cp -R output/latest/tdcc_analytics/. docs/latest/tdcc_analytics/"
        in production
    )
    assert '(output_dir / "tdcc_analytics").rglob("*")' in production
    assert "git add output/latest/tdcc_*" in production
    assert "git add docs/latest/tdcc_*" in production
