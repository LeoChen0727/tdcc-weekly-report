from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import pandas as pd
import pytest

from scripts import build_stock_price_history as history_builder
from scripts import repair_recent_daily_price_gaps as recent_repair
from scripts import repair_missing_daily_price_files as recovery
from scripts import validate_daily_price_history_continuity as validator

ROOT = Path(__file__).resolve().parents[1]


def _write_freshness(root: Path, main_price_date: str) -> None:
    path = root / "output" / "latest" / "data_freshness_latest.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"main_price_date": main_price_date}]).to_csv(path, index=False)


def _write_daily_price(root: Path, date_text: str, rows: list[dict[str, object]]) -> None:
    path = root / "data" / "daily_price" / f"daily_price_{date_text}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False)


def _write_official_fetch_json(root: Path, saved_price_date: str) -> None:
    path = root / "output" / "latest" / "official_price_fetch_latest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        (
            "{\n"
            f'  "saved_price_date": "{saved_price_date}",\n'
            '  "is_target_date": true,\n'
            '  "result": "success_target_full_market"\n'
            "}\n"
        ),
        encoding="utf-8",
    )


def _market_rows(date_text: str, stock_ids: list[str] | None = None) -> list[dict[str, object]]:
    stock_ids = stock_ids or ["1001", "1002"]
    rows: list[dict[str, object]] = []
    for market, offset in [("TWSE", 0), ("TPEx", 100)]:
        for index, stock_id in enumerate(stock_ids):
            rows.append(
                {
                    "date": date_text,
                    "stock_id": f"{int(stock_id) + offset + index:04d}"[-4:],
                    "stock_name": "Test",
                    "market": market,
                    "open": 10,
                    "high": 11,
                    "low": 9,
                    "close": 10,
                    "volume": 1000,
                    "trading_value": 10000,
                    "source": "TEST",
                }
            )
    return rows


def test_missing_weekday_daily_price_files_fail(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260611")
    _write_daily_price(tmp_path, "20260605", _market_rows("20260605"))
    _write_daily_price(tmp_path, "20260611", _market_rows("20260611"))

    result = validator.validate(tmp_path, lookback_days=6, min_full_rows=1)

    assert result.status == "fail"
    assert "20260608: missing daily price file" in result.errors
    assert "20260609: missing daily price file" in result.errors
    assert "20260610: missing daily price file" in result.errors


def test_configured_non_trading_day_is_not_required(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260622")
    holidays = tmp_path / "config" / "twse_non_trading_days.csv"
    holidays.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"date": "20260619", "market": "TWSE_TPEx", "reason": "holiday"}]).to_csv(
        holidays, index=False
    )
    _write_daily_price(tmp_path, "20260618", _market_rows("20260618"))
    _write_daily_price(tmp_path, "20260622", _market_rows("20260622"))

    result = validator.validate(tmp_path, lookback_days=4, min_full_rows=1)

    assert result.status == "pass"
    assert not any("20260619" in error for error in result.errors)


def test_explicit_main_price_date_overrides_stale_freshness(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260717")
    for date_text in ("20260720", "20260721"):
        _write_daily_price(tmp_path, date_text, _market_rows(date_text))

    result = validator.validate(
        tmp_path,
        main_price_date_override="20260721",
        lookback_days=1,
        min_full_rows=1,
    )

    assert result.status == "pass"
    assert result.report["main_price_date"] == "20260721"
    assert result.report["expected_trading_dates"] == ["20260720", "20260721"]


def test_explicit_main_price_date_must_be_calendar_valid(tmp_path: Path) -> None:
    result = validator.validate(
        tmp_path,
        main_price_date_override="20260230",
        lookback_days=1,
        min_full_rows=1,
    )

    assert result.status == "fail"
    assert "day is out of range for month" in result.errors[0]


def test_exceptional_non_trading_day_is_not_required(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260713")
    exceptional = tmp_path / "data" / "market_calendar" / "exceptional_non_trading_days.csv"
    exceptional.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        [
            {
                "date": "20260710",
                "market_status": "closed_emergency",
                "reason": "Taipei City full-day work suspension",
            }
        ]
    ).to_csv(exceptional, index=False)
    for date_text in ("20260708", "20260709", "20260713"):
        _write_daily_price(tmp_path, date_text, _market_rows(date_text))

    result = validator.validate(tmp_path, lookback_days=5, min_full_rows=1)

    assert result.status == "pass"
    assert "20260710" in result.report["non_trading_days_in_window"]
    assert "20260710" not in result.report["expected_trading_dates"]


def test_stock_history_must_cover_daily_price_file_for_target_stocks(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260611")
    rows = _market_rows("20260610", stock_ids=["2243"])
    rows[0]["stock_id"] = "2243"
    _write_daily_price(tmp_path, "20260610", rows)
    rows = _market_rows("20260611", stock_ids=["2243"])
    rows[0]["stock_id"] = "2243"
    _write_daily_price(tmp_path, "20260611", rows)

    signal_path = tmp_path / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv"
    signal_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"stock_id": "2243"}]).to_csv(signal_path, index=False)

    history_path = tmp_path / "data" / "stock_price_history" / "2243.csv"
    history_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"date": "20260611", "stock_id": "2243"}]).to_csv(history_path, index=False)

    result = validator.validate(tmp_path, lookback_days=1, min_full_rows=1)

    assert result.status == "fail"
    assert "20260610: stock history missing row for 2243" in result.errors


def test_warrant_like_daily_price_id_does_not_alias_target_stock_history(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260604")
    _write_daily_price(
        tmp_path,
        "20260604",
        [
            {
                "date": "20260604",
                "stock_id": "707631",
                "stock_name": "Warrant",
                "market": "TPEx",
                "open": 0.61,
                "high": 0.65,
                "low": 0.61,
                "close": 0.64,
                "volume": 1,
                "trading_value": 47000,
                "source": "TPEX_OLD_DAILY_JSON",
            },
            {
                "date": "20260604",
                "stock_id": "00713",
                "stock_name": "ETF",
                "market": "TWSE",
                "open": 59.6,
                "high": 60.35,
                "low": 59.45,
                "close": 60.2,
                "volume": 12948905,
                "trading_value": 776313074,
                "source": "TWSE_RWD_JSON_MI_INDEX",
            },
        ],
    )

    signal_path = tmp_path / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv"
    signal_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"stock_id": "7631"}]).to_csv(signal_path, index=False)

    result = validator.validate(tmp_path, lookback_days=0, min_full_rows=1)

    assert result.status == "pass"
    assert result.report["stock_history_missing_row_count"] == 0
    assert not any("7631" in error for error in result.errors)


def test_missing_intermediate_daily_price_is_repaired_before_history_build(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260624")
    _write_official_fetch_json(tmp_path, "20260626")
    _write_daily_price(tmp_path, "20260624", _market_rows("20260624"))
    _write_daily_price(tmp_path, "20260626", _market_rows("20260626"))
    repaired_dates: list[str] = []

    def fake_repair(root: Path, date_text: str, args: object) -> int:
        repaired_dates.append(date_text)
        _write_daily_price(root, date_text, _market_rows(date_text))
        return 0

    result = recovery.recover(
        tmp_path,
        lookback_days=2,
        min_full_rows=1,
        max_repair_dates=3,
        repair_func=fake_repair,
    )

    assert result.status == "repaired"
    assert result.report["required_end_date"] == "20260626"
    assert result.report["missing_before"] == ["20260625"]
    assert result.report["missing_after"] == []
    assert repaired_dates == ["20260625"]
    assert (tmp_path / "data" / "daily_price" / "daily_price_20260625.csv").exists()


def test_recent_gap_repair_excludes_as_of_date_and_configured_holidays(tmp_path: Path) -> None:
    holidays = tmp_path / "config" / "twse_non_trading_days.csv"
    holidays.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"date": "20260619", "market": "TWSE_TPEx", "reason": "holiday"}]).to_csv(
        holidays, index=False
    )
    for date_text in ["20260618", "20260622"]:
        _write_daily_price(tmp_path, date_text, _market_rows(date_text))

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date="20260623",
        lookback_days=4,
        min_full_rows=1,
        non_trading_days_path=Path("config/twse_non_trading_days.csv"),
        max_repair_dates=2,
        include_as_of_date=False,
    )

    assert result.status == "pass"
    assert result.report["target_end_date"] == "20260622"
    assert result.report["date_boundary"] == "exclude_as_of_date"
    assert result.report["expected_trading_dates"] == ["20260618", "20260622"]
    assert "20260623" not in result.report["expected_trading_dates"]
    assert "20260619" in result.report["non_trading_days_in_window"]


def test_recent_gap_repair_uses_as_of_date_when_freshness_is_stale(tmp_path: Path) -> None:
    _write_freshness(tmp_path, "20260624")
    holidays = tmp_path / "config" / "twse_non_trading_days.csv"
    holidays.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"date": "20260619", "market": "TWSE_TPEx", "reason": "holiday"}]).to_csv(
        holidays, index=False
    )
    for date_text in ["20260622", "20260623", "20260624"]:
        _write_daily_price(tmp_path, date_text, _market_rows(date_text))
    repaired_dates: list[str] = []
    rebuilt: list[str] = []

    def fake_repair(root: Path, date_text: str, args: object) -> int:
        repaired_dates.append(date_text)
        _write_daily_price(root, date_text, _market_rows(date_text))
        return 0

    def fake_rebuild(root: Path, args: object) -> int:
        rebuilt.append(root.as_posix())
        return 0

    result = recent_repair.repair_recent_gaps(
        tmp_path,
        as_of_date="20260627",
        lookback_days=7,
        min_full_rows=1,
        non_trading_days_path=Path("config/twse_non_trading_days.csv"),
        max_repair_dates=5,
        rebuild_history_if_repaired=True,
        repair_func=fake_repair,
        build_history_func=fake_rebuild,
    )

    assert result.status == "repaired"
    assert result.report["target_end_date"] == "20260626"
    assert result.report["missing_before"] == ["20260625", "20260626"]
    assert result.report["missing_after"] == []
    assert repaired_dates == ["20260625", "20260626"]
    assert result.report["rebuild_history_status"] == "completed"
    assert len(rebuilt) == 1


def test_daily_workflow_runs_price_history_continuity_gate() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    repair_at = workflow.index("python scripts/repair_missing_daily_price_files.py")
    evidence_at = workflow.index("daily-price-source-recovery")
    build_at = workflow.index("python scripts/build_stock_price_history.py --incremental-latest")
    gate_at = workflow.index("python scripts/validate_daily_price_history_continuity.py")
    monitor_at = workflow.index("python stock_daily_monitor.py")

    assert "--full-rebuild-if-source-recovered" in workflow
    assert repair_at < evidence_at < build_at < gate_at < monitor_at


def test_repair_workflows_use_shared_repair_script_not_deleted_fetch_functions() -> None:
    for rel_path in [
        ".github/workflows/repair_one_daily_price.yml",
        ".github/workflows/repair_daily_price_range.yml",
    ]:
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        assert "python scripts/repair_daily_price_range.py" in text
        assert "python scripts/build_stock_price_history.py" in text
        assert "python scripts/validate_daily_price_history_continuity.py" in text
        assert "fetch_twse_daily_price" not in text
        assert "fetch_tpex_daily_price" not in text
        assert "is_valid_trading_day_data" not in text


def _selected_history(rows: list[dict[str, object]]) -> pd.DataFrame:
    return history_builder.round_numeric_columns(
        history_builder.add_indicators(
            history_builder.normalize_base_frame(pd.DataFrame(rows))
        )
    )


def _selected_row(
    date_text: str,
    stock_id: str,
    *,
    close: float,
    source: str,
) -> dict[str, object]:
    return {
        "date": date_text,
        "stock_id": stock_id,
        "stock_name": f"Name {stock_id}",
        "market": "TWSE" if source.startswith("TWSE") else "TPEx",
        "open": close - 1,
        "high": close + 1,
        "low": close - 2,
        "close": close,
        "volume": 1000,
        "trading_value": 100000,
        "source": source,
        "source_file": f"data/daily_price/daily_price_{date_text}.csv",
    }


def _selected_manifest_frame(root: Path) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in sorted((root / "data" / "stock_price_history").glob("*.csv")):
        frame = pd.read_csv(path, dtype=str).fillna("").sort_values("date")
        latest = frame.iloc[-1]
        stock_id = path.stem
        rows.append(
            {
                "stock_id": stock_id,
                "stock_name": latest["stock_name"],
                "market": latest["market"],
                "rows": len(frame),
                "start_date": frame["date"].iloc[0],
                "end_date": frame["date"].iloc[-1],
                "latest_close": latest["close"],
                "latest_volume": latest["volume"],
                "file_path": f"data/stock_price_history/{stock_id}.csv",
                "raw_url": (
                    "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"
                    f"data/stock_price_history/{stock_id}.csv"
                ),
            }
        )
    return pd.DataFrame(rows)


def _write_selected_manifest_mirrors(
    root: Path,
    *,
    generated_at: str,
    status: str,
) -> dict[str, str]:
    latest = root / "output" / "latest"
    docs_latest = root / "docs" / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    docs_latest.mkdir(parents=True, exist_ok=True)
    manifest = _selected_manifest_frame(root)
    payloads = {
        "stock_price_history_manifest.csv": manifest.to_csv(
            index=False, lineterminator="\n"
        ).encode("utf-8"),
        "stock_price_history_manifest.json": (
            json.dumps(
                {
                    "generated_at": generated_at,
                    "status": status,
                    "stock_count": len(manifest),
                    "daily_price_file_count": len(
                        list((root / "data" / "daily_price").glob("*.csv"))
                    ),
                    "manifest_csv": "output/latest/stock_price_history_manifest.csv",
                    "manifest_raw_url": (
                        "https://raw.githubusercontent.com/LeoChen0727/"
                        "tdcc-weekly-report/main/output/latest/"
                        "stock_price_history_manifest.csv"
                    ),
                    "manifest_pages_url": (
                        "https://LeoChen0727.github.io/tdcc-weekly-report/"
                        "latest/stock_price_history_manifest.csv"
                    ),
                    "history_dir": "data/stock_price_history",
                    "preserved_extension": {"source": "base"},
                },
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8"),
        "stock_price_history_manifest.md": (
            "# manifest\n\n" + ",".join(manifest["stock_id"].astype(str)) + "\n"
        ).encode("utf-8"),
    }
    hashes: dict[str, str] = {}
    for name, payload in payloads.items():
        for directory, prefix in ((latest, "output/latest"), (docs_latest, "docs/latest")):
            (directory / name).write_bytes(payload)
            hashes[f"{prefix}/{name}"] = hashlib.sha256(payload).hexdigest()
    return hashes


def _setup_selected_validator_case(tmp_path: Path) -> tuple[str, str, dict[str, tuple[str, int]]]:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=tmp_path, check=True)
    history_dir = tmp_path / "data" / "stock_price_history"
    history_dir.mkdir(parents=True)
    base_2330 = _selected_history(
        [_selected_row("20250410", "2330", close=100, source="TWSE_TEST")]
    )
    base_9999 = _selected_history(
        [_selected_row("20250410", "9999", close=50, source="TWSE_TEST")]
    )
    base_2330.to_csv(history_dir / "2330.csv", index=False, lineterminator="\n")
    base_9999.to_csv(history_dir / "9999.csv", index=False, lineterminator="\n")
    _write_selected_manifest_mirrors(tmp_path, generated_at="before", status="generated")
    for index, path_text in enumerate(
        validator.SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS
    ):
        path = tmp_path / path_text
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(
            f"stock_id,stock_name\n{1000 + index},Name {index}\n".encode("utf-8")
        )
    subprocess.run(
        ["git", "add", "data/stock_price_history", "output/latest", "docs/latest"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(["git", "commit", "-qm", "base"], cwd=tmp_path, check=True)
    base_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=tmp_path, text=True).strip()
    canonical_name_bindings = []
    for path_text in validator.SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS:
        blob_sha = subprocess.check_output(
            ["git", "rev-parse", f"{base_sha}:{path_text}"], cwd=tmp_path, text=True
        ).strip()
        blob_payload = subprocess.check_output(
            ["git", "show", f"{base_sha}:{path_text}"], cwd=tmp_path
        )
        canonical_name_bindings.append(
            {
                "path": path_text,
                "git_blob_sha": blob_sha,
                "git_blob_raw_sha256": hashlib.sha256(blob_payload).hexdigest(),
            }
        )

    date_text = "20250411"
    selected_rows = [
        _selected_row(date_text, "2330", close=105, source="TWSE_TEST"),
        _selected_row(date_text, "00925", close=20, source="TPEX_TEST"),
    ]
    raw_rows = selected_rows + [
        _selected_row(date_text, "707631", close=1, source="TPEX_TEST"),
        _selected_row(date_text, "ABC1234", close=2, source="TWSE_TEST"),
    ]
    daily = pd.DataFrame(raw_rows).drop(columns=["source_file"])
    daily_dir = tmp_path / "data" / "daily_price"
    daily_dir.mkdir(parents=True)
    canonical = daily_dir / f"daily_price_{date_text}.csv"
    daily.to_csv(canonical, index=False, encoding="utf-8-sig", lineterminator="\n")
    (daily_dir / f"{date_text}.csv").write_bytes(canonical.read_bytes())
    daily_sha = hashlib.sha256(canonical.read_bytes()).hexdigest()

    current_2330 = _selected_history(
        [
            _selected_row("20250410", "2330", close=100, source="TWSE_TEST"),
            selected_rows[0],
        ]
    )
    created_00925 = _selected_history([selected_rows[1]])
    current_2330.to_csv(history_dir / "2330.csv", index=False, lineterminator="\n")
    created_00925.to_csv(history_dir / "00925.csv", index=False, lineterminator="\n")

    latest = tmp_path / "output" / "latest"
    manifest_hashes = _write_selected_manifest_mirrors(
        tmp_path, generated_at="after", status="selected_date_repair"
    )

    changed_hashes = {
        "data/stock_price_history/00925.csv": hashlib.sha256(
            (history_dir / "00925.csv").read_bytes()
        ).hexdigest(),
        "data/stock_price_history/2330.csv": hashlib.sha256(
            (history_dir / "2330.csv").read_bytes()
        ).hexdigest(),
    }
    report = {
        "schema_version": "repair_daily_price_range_v2",
        "mode": "selected_dates",
        "source_base_sha": base_sha,
        "selected_dates": [date_text],
        "expected_date_contracts": [
            {"date": date_text, "sha256": daily_sha, "row_count": 4}
        ],
        "canonical_stock_name_source_bindings": canonical_name_bindings,
        "rows": [
            {
                "date": date_text,
                "status": "repaired",
                "total_rows": 4,
                "saved_files": (
                    f"data/daily_price/{date_text}.csv;"
                    f"data/daily_price/daily_price_{date_text}.csv"
                ),
                "canonical_path": f"data/daily_price/daily_price_{date_text}.csv",
                "legacy_path": f"data/daily_price/{date_text}.csv",
                "price_sha256": daily_sha,
                "fetch_response_provenance": [
                    {
                        "source_name": "TWSE_TEST",
                        "endpoint": "https://example.test/twse",
                        "attempt": 1,
                        "status_code": 200,
                        "expected_response_date": date_text,
                        "exact_date_match": True,
                        "raw_sha256": "a" * 64,
                        "normalized_sha256": "b" * 64,
                    },
                    {
                        "source_name": "TPEX_TEST",
                        "endpoint": "https://example.test/tpex",
                        "attempt": 1,
                        "status_code": 200,
                        "expected_response_date": date_text,
                        "exact_date_match": True,
                        "raw_sha256": "c" * 64,
                        "normalized_sha256": "d" * 64,
                    },
                ],
            }
        ],
        "history_repair": {
            "eligible_stock_union_count": 2,
            "eligible_stock_date_row_count": 2,
            "existing_history_count": 1,
            "created_history_count": 1,
            "created_history_stock_ids": ["00925"],
            "eligible_history_paths": sorted(changed_hashes),
            "changed_history_paths": sorted(changed_hashes),
            "changed_history_sha256s": changed_hashes,
            "selected_rows_injected_existing_histories": 1,
            "selected_rows_created_histories": 1,
            "new_history_source_coverage": [
                {
                    "stock_id": "00925",
                    "new_history_source_coverage": "target_dates_only",
                    "source_rows": 1,
                    "outside_selected_date_source_rows": 0,
                }
            ],
            "non_selected_base_before_sha256": "a" * 64,
            "non_selected_base_after_sha256": "a" * 64,
            "pre_repair_indicator_before_sha256": "b" * 64,
            "pre_repair_indicator_after_sha256": "b" * 64,
            "untouched_history_count": 1,
            "untouched_history_before_sha256": "c" * 64,
            "untouched_history_after_sha256": "c" * 64,
            "manifest_sha256s": manifest_hashes,
            "manifest_paths": sorted(manifest_hashes),
            "generated_at": "after",
        },
    }
    report_path = latest / "repair_daily_price_range_latest.json"
    report_path.write_text(json.dumps(report), encoding="utf-8")
    for name in (
        "repair_daily_price_range_latest.csv",
        "repair_daily_price_range_check_code_latest.csv",
        "repair_daily_price_range_latest.md",
    ):
        (latest / name).write_text("test\n", encoding="utf-8")
    return base_sha, date_text, {date_text: (daily_sha, 4)}


def test_selected_repair_validator_independently_replays_and_writes_exact_pathspec(
    tmp_path: Path,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    pathspec_nul = tmp_path / "temp" / "paths.nul"
    pathspec_json = tmp_path / "temp" / "paths.json"
    stock_ids = tmp_path / "temp" / "stock-ids.txt"

    summary = validator.validate_selected_repair(
        tmp_path,
        report_path=Path("output/latest/repair_daily_price_range_latest.json"),
        source_base_sha=base_sha,
        date_contracts=contracts,
        expected_stock_union_count=2,
        expected_selected_row_count=2,
        expected_existing_history_count=1,
        expected_created_history_count=1,
        expected_untouched_history_count=1,
        expected_created_stock_ids={"00925"},
        require_all_eligible_changed=True,
        pathspec_nul_output=pathspec_nul,
        pathspec_json_output=pathspec_json,
        history_stock_id_output=stock_ids,
    )

    assert summary["selected_row_count"] == 2
    assert summary["stock_union_count"] == 2
    assert summary["changed_history_count"] == 2
    expected_paths = json.loads(pathspec_json.read_text(encoding="utf-8"))
    assert len(expected_paths) == 14
    assert pathspec_nul.read_bytes().endswith(b"\0")
    assert stock_ids.read_text(encoding="ascii") == "00925\n2330\n"


def test_selected_repair_validator_rejects_canonical_name_source_drift(
    tmp_path: Path,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    source_path = tmp_path / validator.SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS[0]
    source_path.write_bytes(source_path.read_bytes() + b"9999,Drift\n")

    with pytest.raises(
        ValueError, match="canonical stock-name source differs from source base"
    ):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


@pytest.mark.parametrize(
    ("mutation", "expected_message"),
    [
        ("missing_report_binding", "canonical stock-name bindings are missing"),
        ("forged_blob_sha", "canonical stock-name evidence mismatch"),
        ("forged_blob_raw_sha", "canonical stock-name evidence mismatch"),
        ("missing_materialized_source", "canonical stock-name source is not materialized"),
    ],
)
def test_selected_repair_validator_rejects_canonical_name_binding_failures(
    tmp_path: Path,
    mutation: str,
    expected_message: str,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    report_path = tmp_path / "output/latest/repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if mutation == "missing_report_binding":
        report.pop("canonical_stock_name_source_bindings")
        report_path.write_text(json.dumps(report), encoding="utf-8")
    elif mutation == "forged_blob_sha":
        report["canonical_stock_name_source_bindings"][0]["git_blob_sha"] = "f" * 40
        report_path.write_text(json.dumps(report), encoding="utf-8")
    elif mutation == "forged_blob_raw_sha":
        report["canonical_stock_name_source_bindings"][0][
            "git_blob_raw_sha256"
        ] = "f" * 64
        report_path.write_text(json.dumps(report), encoding="utf-8")
    else:
        source_path = (
            tmp_path / validator.SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS[0]
        )
        source_path.unlink()

    with pytest.raises(ValueError, match=expected_message):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_validator_rejects_crlf_even_when_hash_contract_is_updated(
    tmp_path: Path,
) -> None:
    base_sha, date_text, contracts = _setup_selected_validator_case(tmp_path)
    canonical = tmp_path / f"data/daily_price/daily_price_{date_text}.csv"
    legacy = tmp_path / f"data/daily_price/{date_text}.csv"
    crlf_payload = canonical.read_bytes().replace(b"\n", b"\r\n")
    assert crlf_payload.startswith(b"\xef\xbb\xbf")
    canonical.write_bytes(crlf_payload)
    legacy.write_bytes(crlf_payload)
    crlf_sha = hashlib.sha256(crlf_payload).hexdigest()

    report_path = tmp_path / "output/latest/repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["expected_date_contracts"][0]["sha256"] = crlf_sha
    report["rows"][0]["price_sha256"] = crlf_sha
    report_path.write_text(json.dumps(report), encoding="utf-8")
    contracts[date_text] = (crlf_sha, contracts[date_text][1])

    with pytest.raises(ValueError, match="source encoding/line-ending mismatch"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_validator_rejects_missing_bom_even_when_hash_contract_is_updated(
    tmp_path: Path,
) -> None:
    base_sha, date_text, contracts = _setup_selected_validator_case(tmp_path)
    canonical = tmp_path / f"data/daily_price/daily_price_{date_text}.csv"
    legacy = tmp_path / f"data/daily_price/{date_text}.csv"
    payload = canonical.read_bytes()
    assert payload.startswith(b"\xef\xbb\xbf")
    no_bom_payload = payload[3:]
    assert b"\r\n" not in no_bom_payload
    canonical.write_bytes(no_bom_payload)
    legacy.write_bytes(no_bom_payload)
    no_bom_sha = hashlib.sha256(no_bom_payload).hexdigest()

    report_path = tmp_path / "output/latest/repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["expected_date_contracts"][0]["sha256"] = no_bom_sha
    report["rows"][0]["price_sha256"] = no_bom_sha
    report_path.write_text(json.dumps(report), encoding="utf-8")
    contracts[date_text] = (no_bom_sha, contracts[date_text][1])

    with pytest.raises(ValueError, match="source encoding/line-ending mismatch"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_validator_rejects_independent_indicator_drift(
    tmp_path: Path,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    path = tmp_path / "data" / "stock_price_history" / "2330.csv"
    frame = pd.read_csv(path, dtype=str).fillna("")
    frame.loc[frame["date"].eq("20250411"), "return_1d"] = "999"
    frame.to_csv(path, index=False, lineterminator="\n")
    report_path = tmp_path / "output" / "latest" / "repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["history_repair"]["changed_history_sha256s"][
        "data/stock_price_history/2330.csv"
    ] = hashlib.sha256(path.read_bytes()).hexdigest()
    report_path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="independent indicator replay mismatch"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_validator_rejects_missing_final_market_provenance(
    tmp_path: Path,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    report_path = tmp_path / "output/latest/repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["rows"][0]["fetch_response_provenance"] = [
        item
        for item in report["rows"][0]["fetch_response_provenance"]
        if not item["source_name"].startswith("TPEX_")
    ]
    report_path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="TWSE/TPEx provenance is incomplete"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_validator_rejects_hidden_raw_outside_date_for_created_id(
    tmp_path: Path,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    hidden = tmp_path / "data/daily_price/daily_price_20250410.csv"
    pd.DataFrame(
        [
            {
                "date": "20250410",
                "stock_id": "00925",
                "close": "",
                "source": "TPEX_TEST",
            }
        ]
    ).to_csv(hidden, index=False)

    with pytest.raises(ValueError, match="raw source rows outside selected dates"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_validator_rejects_manifest_identity_mutation(
    tmp_path: Path,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    output_csv = tmp_path / "output/latest/stock_price_history_manifest.csv"
    docs_csv = tmp_path / "docs/latest/stock_price_history_manifest.csv"
    manifest = pd.read_csv(output_csv, dtype=str).fillna("")
    manifest.loc[manifest["stock_id"].eq("9999"), "stock_id"] = "00925"
    payload = manifest.to_csv(index=False, lineterminator="\n").encode("utf-8")
    output_csv.write_bytes(payload)
    docs_csv.write_bytes(payload)
    report_path = tmp_path / "output/latest/repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256(payload).hexdigest()
    report["history_repair"]["manifest_sha256s"][
        "output/latest/stock_price_history_manifest.csv"
    ] = digest
    report["history_repair"]["manifest_sha256s"][
        "docs/latest/stock_price_history_manifest.csv"
    ] = digest
    report_path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="manifest stock identity is invalid"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("generated_at", "different"),
        ("manifest_raw_url", "https://example.invalid/manifest.csv"),
        ("preserved_extension", {"source": "mutated"}),
    ],
)
def test_selected_repair_validator_rejects_manifest_json_semantic_mutation(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    base_sha, _, contracts = _setup_selected_validator_case(tmp_path)
    output_json = tmp_path / "output/latest/stock_price_history_manifest.json"
    docs_json = tmp_path / "docs/latest/stock_price_history_manifest.json"
    manifest = json.loads(output_json.read_text(encoding="utf-8"))
    manifest[field] = value
    payload = (json.dumps(manifest, sort_keys=True) + "\n").encode("utf-8")
    output_json.write_bytes(payload)
    docs_json.write_bytes(payload)
    report_path = tmp_path / "output/latest/repair_daily_price_range_latest.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256(payload).hexdigest()
    report["history_repair"]["manifest_sha256s"][
        "output/latest/stock_price_history_manifest.json"
    ] = digest
    report["history_repair"]["manifest_sha256s"][
        "docs/latest/stock_price_history_manifest.json"
    ] = digest
    report_path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(ValueError, match="manifest JSON semantic contract mismatch"):
        validator.validate_selected_repair(
            tmp_path,
            report_path=Path("output/latest/repair_daily_price_range_latest.json"),
            source_base_sha=base_sha,
            date_contracts=contracts,
            expected_stock_union_count=2,
            expected_selected_row_count=2,
            expected_existing_history_count=1,
            expected_created_history_count=1,
            expected_untouched_history_count=1,
            expected_created_stock_ids={"00925"},
            require_all_eligible_changed=True,
        )


def test_selected_repair_staged_path_validator_rejects_untracked_residue(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    path = repo / "bounded.txt"
    path.write_text("before\n", encoding="utf-8")
    subprocess.run(["git", "add", "bounded.txt"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)
    path.write_text("after\n", encoding="utf-8")
    subprocess.run(["git", "add", "bounded.txt"], cwd=repo, check=True)
    plan = tmp_path / "paths.json"
    plan.write_text(json.dumps(["bounded.txt"]), encoding="utf-8")

    assert validator.verify_selected_repair_staged_paths(repo, plan) == 1
    (repo / "unexpected.txt").write_text("unexpected\n", encoding="utf-8")
    with pytest.raises(ValueError, match="unstaged or untracked"):
        validator.verify_selected_repair_staged_paths(repo, plan)


def test_exact_selected_workflow_is_opt_in_bounded_and_no_full_rebuild() -> None:
    workflow = (ROOT / ".github" / "workflows" / "repair_daily_price_range.yml").read_text(
        encoding="utf-8"
    )
    dates_input = workflow.split("      dates:", 1)[1].split("      start_date:", 1)[0]
    exact_step = workflow.split(
        "      - name: Repair exact selected daily prices and controlled stock histories", 1
    )[1].split("      - name: Validate selected repair continuity", 1)[0]
    stage_step = workflow.split(
        "      - name: Stage only exact selected-date repair paths", 1
    )[1].split("      - name: Stage legacy range repair outputs", 1)[0]
    validator_step = workflow.split(
        "      - name: Validate exact seven-date source and history repair", 1
    )[1].split(
        "      - name: Prove controlled history repair second apply is byte-identical", 1
    )[0]

    assert 'default: ""' in dates_input
    assert "daily-full-pipeline-${{ github.ref }}" in workflow
    assert exact_step.count("--expected-date-contract ") == 7
    expected_contracts = {
        "20250411": ("89f2177b6f31537294434dbafa7bde0a51954771e0c750e7bff84a2bd0ad0abc", 2031),
        "20250521": ("77bb957bdcd1392fa0340cbb552bdb8205ba3b96d979fd72783dfe0368170e04", 2035),
        "20250908": ("66a92ce32f3bbba70f8d83ce557e81190d168e814c0c17dad0da697f4f73db45", 2050),
        "20250912": ("7a32b61ed136a15efc519fcae09c85943e4d21c75ea4cbfcfc358eb11e5afb32", 2059),
        "20250916": ("115c35a00dba8dc2d2047d6645d8c20332d80639469d40238564eeb11258067d", 2052),
        "20251015": ("671a17fe97895eaf62274f5798a2c4b1b575fa7b68510ffdad1f5bd3ba307a4d", 2055),
        "20251017": ("2ea87b045021603d89c28ad73645fe7b88b33d0030c7e7f4179b9fe053db7ac2", 2052),
    }
    for date_text, (expected_sha, expected_rows) in expected_contracts.items():
        assert workflow.count(f"{date_text}:{expected_sha}:{expected_rows}") == 3
    assert "--repair-date 20250411" in exact_step
    assert "--repair-date 20251017" in exact_step
    assert "--expected-stock-union-count 2064" in exact_step
    assert "python scripts/build_stock_price_history.py\n" not in exact_step
    assert "--full-rebuild" not in exact_step
    assert "--market-session-already-refreshed" not in exact_step
    assert "--main-price-date 20260811" in workflow
    assert "--lookback-days 500" not in workflow
    assert "--no-write-report" in workflow
    assert "--selected-repair-report" in workflow
    assert "python - <<'PY'" not in workflow
    assert workflow.count("--repair-date 20250411") == 2
    assert workflow.count("--selected-repair-report") == 2
    assert "selected-before.sha256" in workflow
    assert "selected-after.sha256" in workflow
    assert workflow.count("cmp \"") >= 2
    assert "git add --pathspec-from-file=" not in stage_step
    assert 'git add -- "data/stock_price_history/${stock_id}.csv"' in stage_step
    assert stage_step.count("data/daily_price/") == 14
    assert "--history-stock-id-output" in validator_step
    assert "--verify-staged-paths-json" in stage_step
    assert "git add data/daily_price/" not in stage_step
