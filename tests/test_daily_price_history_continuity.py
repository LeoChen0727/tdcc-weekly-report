from __future__ import annotations

from pathlib import Path

import pandas as pd

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
