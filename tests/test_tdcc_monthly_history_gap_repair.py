from __future__ import annotations

from pathlib import Path

import pandas as pd

from scripts import repair_tdcc_monthly_history_gaps as repair


def write_snapshot(path: Path, date: str, codes: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "date": date,
            "code": code,
            "name": code,
            "over_400_pct": "1.0",
            "over_600_pct": "1.0",
            "over_800_pct": "1.0",
            "over_1000_pct": "1.0",
        }
        for code in codes
    ]
    pd.DataFrame(rows).to_csv(path, index=False)


def test_tdcc_target_dates_use_current_month_and_exclude_current_week() -> None:
    dates = ["20260627", "20260620", "20260613", "20260606", "20260530", "20260704"]

    selected = repair.current_month_tdcc_dates_excluding_current_week(
        dates,
        as_of_date="20260623",
    )

    assert selected == ["20260606", "20260613", "20260620"]


def test_tdcc_missing_rows_detects_missing_stocks_only(tmp_path, monkeypatch) -> None:
    history_dir = tmp_path / "output" / "history" / "tdcc"
    monkeypatch.setattr(repair, "TDCC_HISTORY_DIR", history_dir)
    write_snapshot(history_dir / "tdcc_holder_ratio_20260613.csv", "20260613", ["1101"])

    missing = repair.find_missing_rows(["20260613", "20260620"], ["1101", "2330"])

    assert [(item.date, item.missing_stock_ids, item.existing_rows) for item in missing] == [
        ("20260613", ["2330"], 1),
        ("20260620", ["1101", "2330"], 0),
    ]


def test_tdcc_monthly_gap_repair_only_repairs_missing_rows(tmp_path, monkeypatch) -> None:
    history_dir = tmp_path / "output" / "history" / "tdcc"
    monkeypatch.setattr(repair, "TDCC_HISTORY_DIR", history_dir)
    monkeypatch.setattr(repair.backfill, "load_name_map", lambda: {"1101": "Stock A", "2330": "Stock B"})
    monkeypatch.setattr(
        repair.backfill,
        "load_universe",
        lambda name_map, universe, max_stocks, explicit_ids: ["1101", "2330"],
    )
    write_snapshot(history_dir / "tdcc_holder_ratio_20260613.csv", "20260613", ["1101"])

    repaired: list[tuple[str, str]] = []

    def fake_repair(session, missing_rows, name_map, max_requests, sleep_seconds):
        actions = []
        for item in missing_rows:
            existing_path = history_dir / f"tdcc_holder_ratio_{item.date}.csv"
            existing = pd.read_csv(existing_path, dtype=str) if existing_path.exists() else pd.DataFrame()
            new_rows = []
            for stock_id in item.missing_stock_ids:
                repaired.append((item.date, stock_id))
                actions.append({"date": item.date, "stock_id": stock_id, "status": "repaired", "message": ""})
                new_rows.append(
                    {
                        "date": item.date,
                        "code": stock_id,
                        "name": name_map.get(stock_id, ""),
                        "over_400_pct": "1.0",
                        "over_600_pct": "1.0",
                        "over_800_pct": "1.0",
                        "over_1000_pct": "1.0",
                    }
                )
            out = pd.concat([existing, pd.DataFrame(new_rows)], ignore_index=True, sort=False)
            out.to_csv(existing_path, index=False)
        return actions

    result = repair.repair_tdcc_monthly_gaps(
        as_of_date="20260623",
        universe="chatgpt-top",
        max_stocks=80,
        max_requests=500,
        sleep_seconds=0,
        dry_run=False,
        write_report_file=False,
        available_dates_func=lambda session: ["20260620", "20260613", "20260606", "20260530"],
        repair_func=fake_repair,
    )

    assert result["status"] == "repaired"
    assert result["target_dates"] == ["20260606", "20260613", "20260620"]
    assert result["missing_stock_rows_before"] == 5
    assert result["missing_stock_rows_after"] == 0
    assert repaired == [
        ("20260606", "1101"),
        ("20260606", "2330"),
        ("20260613", "2330"),
        ("20260620", "1101"),
        ("20260620", "2330"),
    ]
