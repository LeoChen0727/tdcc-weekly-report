from __future__ import annotations

from pathlib import Path

import pandas as pd

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


def test_daily_workflow_runs_price_history_continuity_gate() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    build_at = workflow.index("python scripts/build_stock_price_history.py --incremental-latest")
    gate_at = workflow.index("python scripts/validate_daily_price_history_continuity.py")
    monitor_at = workflow.index("python stock_daily_monitor.py")

    assert build_at < gate_at < monitor_at


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
