from __future__ import annotations

from pathlib import Path

import pytest

from scripts import repair_historical_tpex_prices as repair
from scripts import detect_daily_model_pr_validation_scope as scope


def document(date="20250919", close="13.70"):
    return {"date": date, "stat": "ok", "tables": [{
        "title": "上櫃股票每日收盤行情(不含定價)",
        "date": f"114/{date[4:6]}/{date[6:]}",
        "fields": ["代號", "名稱", "開盤", "最高", "最低", "收盤", "成交股數", "成交金額(元)"],
        "data": [["3191", "雲嘉南", "13.70", "14.00", "13.60", close, "25000", "344000"]],
    }]}


def original(date="20250919"):
    return ("\ufeffdate,ticker,name,market,open,high,low,close,volume,turnover\n"
            f'{date},2330,"台積電",listed,1.00,2.00,1.00,2.00,123.0,246.0\n'
            f"{date},3191,雲嘉南,otc,25.0,26.45,25.0,26.45,333,1234\n").encode("utf-8")


def test_repair_keeps_listed_physical_row_and_replaces_otc():
    before = original()
    result = repair.build_replacement(before, document(), "20250919")
    assert repair.listed_bytes(result) == repair.listed_bytes(before)
    parsed = repair.rows(result)
    assert len(parsed) == 2
    assert parsed[1]["ticker"] == "3191"
    assert float(parsed[1]["close"]) == 13.70
    assert float(parsed[1]["volume"]) == 25000
    assert float(parsed[1]["turnover"]) == 344000


def test_batch_repetition_rejects_relabelled_market():
    one = repair.build_replacement(original(), document(), "20250919")
    two = repair.build_replacement(original("20250926"), document("20250926"), "20250926")
    with pytest.raises(ValueError, match="repeats across dates"):
        repair.reject_repeated_batches({"20250919": one, "20250926": two})
    changed = repair.build_replacement(original("20250926"), document("20250926", "14.00"), "20250926")
    repair.reject_repeated_batches({"20250919": one, "20250926": changed})


def test_market_identity_collision_is_not_deduplicated():
    source = document()
    source["tables"][0]["data"][0][0] = "2330"
    with pytest.raises(ValueError, match="cross-market"):
        repair.build_replacement(original(), source, "20250919")


def test_wrong_source_day_does_not_modify_original():
    before = original()
    with pytest.raises(ValueError):
        repair.build_replacement(before, document("20250926"), "20250919")
    assert before == original()


def test_authorized_dates_scope_selects_only_repository_contracts():
    paths = [f"data/daily_price/{date}.csv" for date in repair.DATES]
    paths += ["backfill_official_daily_price.py", "scripts/repair_historical_tpex_prices.py",
              "tests/test_backfill_official_daily_price.py", "tests/test_historical_tpex_price_repair.py",
              "config/tpex_historical_price_repair_202509.csv", "docs/tpex_historical_price_repair.md",
              "retained-evidence/tpex-history-repair-202509/raw/20250919_TPEx_raw.json"]
    for path in paths:
        assert scope.domains_for_path(path) == frozenset({scope.REPO_CURRENT_CONTRACTS}), path


def test_read_only_workflow_runs_repair_validation_and_regressions():
    path = Path(__file__).resolve().parents[1] / ".github/workflows/daily_model_maintenance_pr_validation.yml"
    text = path.read_text(encoding="utf-8")
    assert "tests/test_backfill_official_daily_price.py" in text
    assert "tests/test_historical_tpex_price_repair.py" in text
    assert "--apply" not in text
    assert "--collect" not in text


def test_registered_repair_replays_official_raw():
    results = repair.validate(Path(__file__).resolve().parents[1])
    assert [row["date"] for row in results] == list(repair.DATES)
    assert all(row["official_parity"] for row in results)
