from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import duckdb
import pandas as pd

try:
    from tdcc_dataset_contract import (
        LATEST_MANIFEST_JSON,
        load_tdcc_dataset_manifest,
        normalize_code,
        normalize_date,
        normalized_text_sha256,
        read_snapshot,
    )
except ModuleNotFoundError:  # Package import used by pytest.
    from scripts.tdcc_dataset_contract import (
        LATEST_MANIFEST_JSON,
        load_tdcc_dataset_manifest,
        normalize_code,
        normalize_date,
        normalized_text_sha256,
        read_snapshot,
    )


ANALYTICS_SCHEMA_VERSION = "tdcc_analytics_manifest_v1"
DEFAULT_OUTPUT_DIR = Path("output/latest/tdcc_analytics")
PARQUET_FILENAME = "tdcc_holder_ratio_history_latest.parquet"
DUCKDB_FILENAME = "tdcc_analytics_latest.duckdb"
MANIFEST_FILENAME = "tdcc_analytics_manifest_latest.json"
TAIPEI = ZoneInfo("Asia/Taipei")

RATIO_COLUMNS = (
    "over_400_pct",
    "over_600_pct",
    "over_800_pct",
    "over_1000_pct",
)
HISTORY_COLUMNS = (
    "source_tdcc_dataset_id",
    "signal_date",
    "snapshot_date",
    "period_index",
    "code",
    "name",
    *RATIO_COLUMNS,
    "source_snapshot_sha256",
    "source_snapshot_path",
)
REQUIRED_SNAPSHOT_COLUMNS = {"date", "code", "name", *RATIO_COLUMNS}
EXPECTED_TABLES = (
    "tdcc_holder_ratio_history",
    "tdcc_dataset_metadata",
    "tdcc_snapshot_metadata",
)
EXPECTED_VIEWS = (
    "tdcc_holder_ratio_latest",
    "tdcc_holder_ratio_previous_official",
    "tdcc_holder_ratio_latest_comparison",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _parse_optional_float(value: Any, *, field: str, path: Path, row_number: int) -> float | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        parsed = float(text)
    except ValueError as exc:
        raise RuntimeError(
            f"canonical TDCC snapshot has non-numeric {field} at {path.as_posix()}:{row_number}"
        ) from exc
    if not math.isfinite(parsed):
        raise RuntimeError(
            f"canonical TDCC snapshot has non-finite {field} at {path.as_posix()}:{row_number}"
        )
    return parsed


def _verified_history_rows(
    source_manifest_path: Path,
) -> tuple[dict[str, Any], list[tuple[Any, ...]], list[dict[str, Any]]]:
    manifest = load_tdcc_dataset_manifest(source_manifest_path)
    dataset_id = str(manifest["dataset_id"])
    signal_date = str(manifest["signal_date"])
    canonical_root = Path(str(manifest.get("canonical_source_root", ""))).resolve()
    if not canonical_root.exists() or not canonical_root.is_dir():
        raise RuntimeError(
            f"canonical TDCC source root is missing: {canonical_root.as_posix()}"
        )

    history_rows: list[tuple[Any, ...]] = []
    snapshot_metadata: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str]] = set()
    required_dates = set(str(value) for value in manifest["required_dates"])

    for period_index, item in enumerate(manifest["history_snapshots"]):
        snapshot_date = normalize_date(item.get("date", ""))
        snapshot_path = Path(str(item.get("path", "")))
        resolved_path = snapshot_path.resolve()
        if not resolved_path.is_relative_to(canonical_root):
            raise RuntimeError(
                "TDCC analytics source snapshot escapes canonical_source_root: "
                f"{snapshot_path.as_posix()}"
            )
        expected_sha = str(item.get("sha256", "")).strip().lower()
        actual_sha = normalized_text_sha256(snapshot_path)
        if actual_sha != expected_sha:
            raise RuntimeError(
                "canonical TDCC snapshot hash does not match dataset manifest: "
                f"{snapshot_path.as_posix()} expected={expected_sha} actual={actual_sha}"
            )

        rows, codes = read_snapshot(snapshot_path, snapshot_date)
        with snapshot_path.open("r", encoding="utf-8-sig", newline="") as handle:
            fields = set(csv.DictReader(handle).fieldnames or [])
        missing_columns = sorted(REQUIRED_SNAPSHOT_COLUMNS - fields)
        if missing_columns:
            raise RuntimeError(
                f"canonical TDCC snapshot lacks analytics columns {missing_columns}: "
                f"{snapshot_path.as_posix()}"
            )
        expected_rows = int(item.get("row_count", -1))
        expected_stocks = int(item.get("stock_count", -1))
        if expected_rows != len(rows) or expected_stocks != len(codes):
            raise RuntimeError(
                "canonical TDCC snapshot row/stock counts do not match dataset manifest: "
                f"{snapshot_path.as_posix()}"
            )

        previous_date = (
            str(manifest["history_dates"][period_index - 1]) if period_index > 0 else None
        )
        snapshot_metadata.append(
            {
                "source_tdcc_dataset_id": dataset_id,
                "period_index": period_index,
                "snapshot_date": snapshot_date,
                "previous_snapshot_date": previous_date,
                "row_count": len(rows),
                "stock_count": len(codes),
                "source_snapshot_sha256": actual_sha,
                "source_snapshot_path": snapshot_path.as_posix(),
                "is_signal_period": snapshot_date == signal_date,
                "is_continuity_window": snapshot_date in required_dates,
            }
        )

        for row_number, row in enumerate(rows, start=2):
            code = normalize_code(row.get("code", ""))
            key = (snapshot_date, code)
            if key in seen_keys:
                raise RuntimeError(
                    f"duplicate TDCC analytics key snapshot_date={snapshot_date} code={code}"
                )
            seen_keys.add(key)
            history_rows.append(
                (
                    dataset_id,
                    signal_date,
                    snapshot_date,
                    period_index,
                    code,
                    str(row.get("name", "")).strip(),
                    *(
                        _parse_optional_float(
                            row.get(field, ""),
                            field=field,
                            path=snapshot_path,
                            row_number=row_number,
                        )
                        for field in RATIO_COLUMNS
                    ),
                    actual_sha,
                    snapshot_path.as_posix(),
                )
            )

    if not history_rows:
        raise RuntimeError("canonical TDCC history produced no analytics rows")
    return manifest, history_rows, snapshot_metadata


def _sql_path(path: Path) -> str:
    return path.resolve().as_posix().replace("'", "''")


def _create_database(
    database_path: Path,
    parquet_path: Path,
    *,
    source_manifest_path: Path,
    manifest: dict[str, Any],
    history_rows: list[tuple[Any, ...]],
    snapshot_metadata: list[dict[str, Any]],
) -> None:
    connection = duckdb.connect(str(database_path))
    try:
        connection.execute(
            """
            CREATE TABLE tdcc_holder_ratio_history (
                source_tdcc_dataset_id VARCHAR NOT NULL,
                signal_date VARCHAR NOT NULL,
                snapshot_date VARCHAR NOT NULL,
                period_index INTEGER NOT NULL,
                code VARCHAR NOT NULL,
                name VARCHAR NOT NULL,
                over_400_pct DOUBLE,
                over_600_pct DOUBLE,
                over_800_pct DOUBLE,
                over_1000_pct DOUBLE,
                source_snapshot_sha256 VARCHAR NOT NULL,
                source_snapshot_path VARCHAR NOT NULL,
                PRIMARY KEY (snapshot_date, code)
            )
            """
        )
        history_frame = pd.DataFrame.from_records(history_rows, columns=HISTORY_COLUMNS)
        connection.register("_tdcc_history_frame", history_frame)
        try:
            connection.execute(
                "INSERT INTO tdcc_holder_ratio_history SELECT * FROM _tdcc_history_frame"
            )
        finally:
            connection.unregister("_tdcc_history_frame")

        connection.execute(
            """
            CREATE TABLE tdcc_dataset_metadata (
                analytics_schema_version VARCHAR NOT NULL,
                source_tdcc_dataset_id VARCHAR NOT NULL,
                source_tdcc_dataset_hash VARCHAR NOT NULL,
                signal_date VARCHAR NOT NULL,
                history_snapshot_count INTEGER NOT NULL,
                history_start_date VARCHAR NOT NULL,
                history_end_date VARCHAR NOT NULL,
                source_manifest_path VARCHAR NOT NULL,
                source_manifest_sha256 VARCHAR NOT NULL,
                duckdb_version VARCHAR NOT NULL
            )
            """
        )
        connection.execute(
            "INSERT INTO tdcc_dataset_metadata VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                ANALYTICS_SCHEMA_VERSION,
                str(manifest["dataset_id"]),
                str(manifest["dataset_hash"]),
                str(manifest["signal_date"]),
                int(manifest["history_snapshot_count"]),
                str(manifest["history_dates"][0]),
                str(manifest["history_dates"][-1]),
                source_manifest_path.as_posix(),
                normalized_text_sha256(source_manifest_path),
                duckdb.__version__,
            ],
        )

        connection.execute(
            """
            CREATE TABLE tdcc_snapshot_metadata (
                source_tdcc_dataset_id VARCHAR NOT NULL,
                period_index INTEGER NOT NULL,
                snapshot_date VARCHAR NOT NULL,
                previous_snapshot_date VARCHAR,
                row_count INTEGER NOT NULL,
                stock_count INTEGER NOT NULL,
                source_snapshot_sha256 VARCHAR NOT NULL,
                source_snapshot_path VARCHAR NOT NULL,
                is_signal_period BOOLEAN NOT NULL,
                is_continuity_window BOOLEAN NOT NULL,
                PRIMARY KEY (period_index)
            )
            """
        )
        connection.executemany(
            "INSERT INTO tdcc_snapshot_metadata VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    item["source_tdcc_dataset_id"],
                    item["period_index"],
                    item["snapshot_date"],
                    item["previous_snapshot_date"],
                    item["row_count"],
                    item["stock_count"],
                    item["source_snapshot_sha256"],
                    item["source_snapshot_path"],
                    item["is_signal_period"],
                    item["is_continuity_window"],
                )
                for item in snapshot_metadata
            ],
        )

        connection.execute(
            """
            CREATE VIEW tdcc_holder_ratio_latest AS
            SELECT history.*
            FROM tdcc_holder_ratio_history AS history
            WHERE period_index = (SELECT MAX(period_index) FROM tdcc_snapshot_metadata)
            """
        )
        connection.execute(
            """
            CREATE VIEW tdcc_holder_ratio_previous_official AS
            SELECT history.*
            FROM tdcc_holder_ratio_history AS history
            WHERE period_index = (SELECT MAX(period_index) - 1 FROM tdcc_snapshot_metadata)
            """
        )
        connection.execute(
            """
            CREATE VIEW tdcc_holder_ratio_latest_comparison AS
            SELECT
                current.source_tdcc_dataset_id,
                current.signal_date,
                current.snapshot_date,
                current.period_index,
                current.code,
                current.name,
                current.over_400_pct,
                current.over_600_pct,
                current.over_800_pct,
                current.over_1000_pct,
                previous.snapshot_date AS previous_snapshot_date,
                previous.period_index AS previous_period_index,
                previous.over_400_pct AS previous_over_400_pct,
                previous.over_600_pct AS previous_over_600_pct,
                previous.over_800_pct AS previous_over_800_pct,
                previous.over_1000_pct AS previous_over_1000_pct,
                current.over_400_pct - previous.over_400_pct AS change_over_400_pct,
                current.over_600_pct - previous.over_600_pct AS change_over_600_pct,
                current.over_800_pct - previous.over_800_pct AS change_over_800_pct,
                current.over_1000_pct - previous.over_1000_pct AS change_over_1000_pct
            FROM tdcc_holder_ratio_latest AS current
            LEFT JOIN tdcc_holder_ratio_history AS previous
              ON previous.period_index = current.period_index - 1
             AND previous.code = current.code
            """
        )

        connection.execute(
            f"""
            COPY (
                SELECT *
                FROM tdcc_holder_ratio_history
                ORDER BY period_index, code
            ) TO '{_sql_path(parquet_path)}'
            (FORMAT PARQUET, COMPRESSION ZSTD)
            """
        )
        connection.execute("CHECKPOINT")
    finally:
        connection.close()


def build_analytics_store(
    *,
    source_manifest_path: Path = LATEST_MANIFEST_JSON,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    generated_at: str | None = None,
) -> dict[str, Any]:
    manifest, history_rows, snapshot_metadata = _verified_history_rows(source_manifest_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    parquet_path = output_dir / PARQUET_FILENAME
    database_path = output_dir / DUCKDB_FILENAME
    analytics_manifest_path = output_dir / MANIFEST_FILENAME

    with tempfile.TemporaryDirectory(prefix=".tdcc_analytics_", dir=output_dir.parent) as temp_name:
        staging_dir = Path(temp_name)
        staging_parquet = staging_dir / PARQUET_FILENAME
        staging_database = staging_dir / DUCKDB_FILENAME
        _create_database(
            staging_database,
            staging_parquet,
            source_manifest_path=source_manifest_path,
            manifest=manifest,
            history_rows=history_rows,
            snapshot_metadata=snapshot_metadata,
        )

        artifacts = {
            "parquet": {
                "path": parquet_path.as_posix(),
                "size_bytes": staging_parquet.stat().st_size,
                "sha256": sha256_file(staging_parquet),
            },
            "duckdb": {
                "path": database_path.as_posix(),
                "size_bytes": staging_database.stat().st_size,
                "sha256": sha256_file(staging_database),
            },
        }
        analytics_manifest = {
            "status": "pass",
            "schema_version": ANALYTICS_SCHEMA_VERSION,
            "generated_at": generated_at
            or datetime.now(TAIPEI).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
            "source_manifest_path": source_manifest_path.as_posix(),
            "source_manifest_sha256": normalized_text_sha256(source_manifest_path),
            "source_tdcc_dataset_id": str(manifest["dataset_id"]),
            "source_tdcc_dataset_hash": str(manifest["dataset_hash"]),
            "signal_date": str(manifest["signal_date"]),
            "history_snapshot_count": int(manifest["history_snapshot_count"]),
            "history_dates": list(manifest["history_dates"]),
            "history_snapshots": [
                {
                    "date": str(item["date"]),
                    "path": str(item["path"]),
                    "row_count": int(item["row_count"]),
                    "stock_count": int(item["stock_count"]),
                    "sha256": str(item["sha256"]),
                }
                for item in manifest["history_snapshots"]
            ],
            "row_count": len(history_rows),
            "latest_stock_count": snapshot_metadata[-1]["stock_count"],
            "history_columns": list(HISTORY_COLUMNS),
            "duckdb_version": duckdb.__version__,
            "tables": list(EXPECTED_TABLES),
            "views": list(EXPECTED_VIEWS),
            "artifacts": artifacts,
        }
        staging_manifest = staging_dir / MANIFEST_FILENAME
        staging_manifest.write_text(
            json.dumps(analytics_manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        os.replace(staging_parquet, parquet_path)
        os.replace(staging_database, database_path)
        os.replace(staging_manifest, analytics_manifest_path)
    return analytics_manifest


def _load_analytics_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"TDCC analytics manifest is missing: {path.as_posix()}")
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read TDCC analytics manifest: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError("TDCC analytics manifest must be a JSON object")
    return value


def _assert_equal(actual: Any, expected: Any, message: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{message}: expected={expected!r} actual={actual!r}")


def validate_analytics_store(
    *,
    source_manifest_path: Path = LATEST_MANIFEST_JSON,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> dict[str, Any]:
    source = load_tdcc_dataset_manifest(source_manifest_path)
    analytics_path = output_dir / MANIFEST_FILENAME
    analytics = _load_analytics_manifest(analytics_path)
    _assert_equal(analytics.get("status"), "pass", "TDCC analytics status mismatch")
    _assert_equal(
        analytics.get("schema_version"),
        ANALYTICS_SCHEMA_VERSION,
        "TDCC analytics schema mismatch",
    )
    for field, expected in (
        ("source_manifest_path", source_manifest_path.as_posix()),
        ("source_tdcc_dataset_id", source["dataset_id"]),
        ("source_tdcc_dataset_hash", source["dataset_hash"]),
        ("signal_date", source["signal_date"]),
        ("history_snapshot_count", source["history_snapshot_count"]),
        ("history_dates", source["history_dates"]),
        ("source_manifest_sha256", normalized_text_sha256(source_manifest_path)),
        ("history_columns", list(HISTORY_COLUMNS)),
        ("tables", list(EXPECTED_TABLES)),
        ("views", list(EXPECTED_VIEWS)),
    ):
        _assert_equal(analytics.get(field), expected, f"TDCC analytics {field} mismatch")

    expected_snapshots = [
        {
            "date": str(item["date"]),
            "path": str(item["path"]),
            "row_count": int(item["row_count"]),
            "stock_count": int(item["stock_count"]),
            "sha256": str(item["sha256"]),
        }
        for item in source["history_snapshots"]
    ]
    _assert_equal(
        analytics.get("history_snapshots"),
        expected_snapshots,
        "TDCC analytics snapshot lineage mismatch",
    )
    for item in source["history_snapshots"]:
        snapshot_path = Path(str(item["path"]))
        if not snapshot_path.exists():
            raise RuntimeError(
                f"canonical TDCC snapshot is missing during analytics validation: {snapshot_path.as_posix()}"
            )
        _assert_equal(
            normalized_text_sha256(snapshot_path),
            str(item["sha256"]),
            f"canonical TDCC snapshot hash drift during analytics validation: {snapshot_path.as_posix()}",
        )

    artifacts = analytics.get("artifacts", {})
    if not isinstance(artifacts, dict):
        raise RuntimeError("TDCC analytics artifacts must be an object")
    parquet_path = output_dir / PARQUET_FILENAME
    database_path = output_dir / DUCKDB_FILENAME
    for key, path in (("parquet", parquet_path), ("duckdb", database_path)):
        item = artifacts.get(key, {})
        if not isinstance(item, dict):
            raise RuntimeError(f"TDCC analytics artifact metadata is missing: {key}")
        if not path.exists() or path.stat().st_size <= 0:
            raise RuntimeError(f"TDCC analytics artifact is missing or empty: {path.as_posix()}")
        _assert_equal(item.get("path"), path.as_posix(), f"TDCC analytics {key} path mismatch")
        _assert_equal(item.get("size_bytes"), path.stat().st_size, f"TDCC analytics {key} size mismatch")
        _assert_equal(item.get("sha256"), sha256_file(path), f"TDCC analytics {key} hash mismatch")

    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        table_names = {
            str(row[0])
            for row in connection.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'"
            ).fetchall()
        }
        for name in [*EXPECTED_TABLES, *EXPECTED_VIEWS]:
            if name not in table_names:
                raise RuntimeError(f"TDCC analytics database object is missing: {name}")

        columns = [
            str(row[1])
            for row in connection.execute("PRAGMA table_info('tdcc_holder_ratio_history')").fetchall()
        ]
        _assert_equal(columns, list(HISTORY_COLUMNS), "TDCC analytics history columns mismatch")
        row_count = int(connection.execute("SELECT COUNT(*) FROM tdcc_holder_ratio_history").fetchone()[0])
        _assert_equal(row_count, int(analytics["row_count"]), "TDCC analytics row count mismatch")

        dataset_ids = connection.execute(
            "SELECT DISTINCT source_tdcc_dataset_id FROM tdcc_holder_ratio_history"
        ).fetchall()
        _assert_equal(dataset_ids, [(source["dataset_id"],)], "TDCC analytics dataset id mismatch")
        observed_dates = [
            str(row[0])
            for row in connection.execute(
                "SELECT DISTINCT snapshot_date FROM tdcc_holder_ratio_history ORDER BY snapshot_date"
            ).fetchall()
        ]
        _assert_equal(observed_dates, list(source["history_dates"]), "TDCC analytics dates mismatch")

        metadata_rows = connection.execute("SELECT * FROM tdcc_dataset_metadata").fetchall()
        if len(metadata_rows) != 1:
            raise RuntimeError("TDCC analytics dataset metadata must contain exactly one row")
        _assert_equal(
            metadata_rows[0],
            (
                ANALYTICS_SCHEMA_VERSION,
                source["dataset_id"],
                source["dataset_hash"],
                source["signal_date"],
                int(source["history_snapshot_count"]),
                source["history_dates"][0],
                source["history_dates"][-1],
                source_manifest_path.as_posix(),
                normalized_text_sha256(source_manifest_path),
                analytics["duckdb_version"],
            ),
            "TDCC analytics dataset metadata mismatch",
        )

        snapshot_rows = connection.execute(
            """
            SELECT period_index, snapshot_date, previous_snapshot_date, row_count, stock_count,
                   source_snapshot_sha256, source_snapshot_path,
                   is_signal_period, is_continuity_window
            FROM tdcc_snapshot_metadata
            ORDER BY period_index
            """
        ).fetchall()
        expected_metadata = []
        for index, item in enumerate(source["history_snapshots"]):
            expected_metadata.append(
                (
                    index,
                    str(item["date"]),
                    str(source["history_dates"][index - 1]) if index > 0 else None,
                    int(item["row_count"]),
                    int(item["stock_count"]),
                    str(item["sha256"]),
                    str(item["path"]),
                    str(item["date"]) == source["signal_date"],
                    str(item["date"]) in set(source["required_dates"]),
                )
            )
        _assert_equal(snapshot_rows, expected_metadata, "TDCC analytics snapshot metadata mismatch")

        escaped_parquet = _sql_path(parquet_path)
        parquet_count = int(
            connection.execute(f"SELECT COUNT(*) FROM read_parquet('{escaped_parquet}')").fetchone()[0]
        )
        _assert_equal(parquet_count, row_count, "TDCC analytics parquet row count mismatch")
        parquet_only = int(
            connection.execute(
                f"""
                SELECT COUNT(*) FROM (
                    SELECT * FROM read_parquet('{escaped_parquet}')
                    EXCEPT ALL
                    SELECT * FROM tdcc_holder_ratio_history
                )
                """
            ).fetchone()[0]
        )
        database_only = int(
            connection.execute(
                f"""
                SELECT COUNT(*) FROM (
                    SELECT * FROM tdcc_holder_ratio_history
                    EXCEPT ALL
                    SELECT * FROM read_parquet('{escaped_parquet}')
                )
                """
            ).fetchone()[0]
        )
        if parquet_only or database_only:
            raise RuntimeError(
                "TDCC analytics Parquet and DuckDB contents differ: "
                f"parquet_only={parquet_only} database_only={database_only}"
            )

        max_period = len(source["history_dates"]) - 1
        latest_periods = connection.execute(
            "SELECT DISTINCT period_index, snapshot_date FROM tdcc_holder_ratio_latest"
        ).fetchall()
        _assert_equal(
            latest_periods,
            [(max_period, source["signal_date"])],
            "TDCC analytics latest view period mismatch",
        )
        if max_period > 0:
            previous_periods = connection.execute(
                "SELECT DISTINCT period_index, snapshot_date FROM tdcc_holder_ratio_previous_official"
            ).fetchall()
            _assert_equal(
                previous_periods,
                [(max_period - 1, source["history_dates"][-2])],
                "TDCC analytics previous official view period mismatch",
            )
            invalid_comparison = int(
                connection.execute(
                    """
                    SELECT COUNT(*)
                    FROM tdcc_holder_ratio_latest_comparison
                    WHERE previous_period_index IS NOT NULL
                      AND previous_period_index <> period_index - 1
                    """
                ).fetchone()[0]
            )
            if invalid_comparison:
                raise RuntimeError(
                    "TDCC analytics comparison view skips the immediately previous official period"
                )
        latest_count = int(connection.execute("SELECT COUNT(*) FROM tdcc_holder_ratio_latest").fetchone()[0])
        _assert_equal(
            latest_count,
            int(source["history_snapshots"][-1]["row_count"]),
            "TDCC analytics latest view row count mismatch",
        )
        _assert_equal(
            int(analytics["latest_stock_count"]),
            int(source["history_snapshots"][-1]["stock_count"]),
            "TDCC analytics latest stock count mismatch",
        )
        comparison_count = int(
            connection.execute("SELECT COUNT(*) FROM tdcc_holder_ratio_latest_comparison").fetchone()[0]
        )
        _assert_equal(comparison_count, latest_count, "TDCC analytics comparison row count mismatch")
    finally:
        connection.close()

    return {
        "status": "pass",
        "source_tdcc_dataset_id": source["dataset_id"],
        "signal_date": source["signal_date"],
        "history_snapshot_count": source["history_snapshot_count"],
        "row_count": analytics["row_count"],
        "parquet_path": parquet_path.as_posix(),
        "duckdb_path": database_path.as_posix(),
        "manifest_path": analytics_path.as_posix(),
    }
