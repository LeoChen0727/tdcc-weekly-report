from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import subprocess
from decimal import Decimal, InvalidOperation
from pathlib import Path

import pytest

from scripts import repair_historical_tpex_prices as repair
from scripts import detect_daily_model_pr_validation_scope as scope


OCTOBER_DATES = tuple(
    "20251001 20251002 20251003 20251007 20251008 20251009 "
    "20251013 20251014 20251016 20251020 20251021 20251022 "
    "20251023 20251027 20251028 20251029 20251030 20251031".split()
)


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


def test_october_batch_is_exact_and_does_not_replace_september_registration():
    assert set(repair.BATCHES) == {"202509", "202510"}
    old_dates, old_evidence, old_manifest = repair.batch_spec("202509")
    new_dates, new_evidence, new_manifest = repair.batch_spec("202510")
    assert old_dates == repair.DATES
    assert old_evidence == repair.EVIDENCE
    assert old_manifest == repair.MANIFEST
    assert len(old_dates) == 17
    assert new_dates == OCTOBER_DATES
    assert not set(old_dates).intersection(new_dates)
    assert new_evidence == Path("retained-evidence/tpex-history-repair-202510")
    assert new_manifest == Path("config/tpex_historical_price_repair_202510.csv")


@pytest.mark.parametrize("batch", ["", "202511", "all", "../202510"])
def test_unknown_batch_fails_closed(batch):
    with pytest.raises(ValueError):
        repair.batch_spec(batch)


def test_october_authorized_paths_select_repository_contracts_only():
    paths = [f"data/daily_price/{date}.csv" for date in OCTOBER_DATES]
    paths.append("config/tpex_historical_price_repair_202510.csv")
    paths.extend(
        f"retained-evidence/tpex-history-repair-202510/raw/{date}_TPEx_{kind}.json"
        for date in OCTOBER_DATES for kind in ("raw", "receipt")
    )
    for path in paths:
        assert scope.domains_for_path(path) == frozenset({scope.REPO_CURRENT_CONTRACTS}), path


@pytest.mark.parametrize("date", ["20251006", "20251010", "20251015", "20251103"])
def test_non_authorized_price_days_are_not_added_to_repair_scope(date):
    assert scope.domains_for_path(f"data/daily_price/{date}.csv") != frozenset({scope.REPO_CURRENT_CONTRACTS})


def test_read_only_workflow_runs_repair_validation_and_regressions():
    path = Path(__file__).resolve().parents[1] / ".github/workflows/daily_model_maintenance_pr_validation.yml"
    text = path.read_text(encoding="utf-8")
    assert "python scripts/repair_historical_tpex_prices.py" not in text
    assert "tests/test_backfill_official_daily_price.py" in text
    assert "tests/test_historical_tpex_price_repair.py" in text
    assert "--apply" not in text
    assert "--collect" not in text


@pytest.mark.parametrize("batch", ["202509", "202510"])
def test_registered_repair_replays_official_raw(batch):
    results = repair.validate(Path(__file__).resolve().parents[1], batch=batch)
    assert [row["date"] for row in results] == list(repair.batch_spec(batch)[0])
    assert all(row["official_parity"] for row in results)


def _independent_csv_rows(payload):
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))


def _independent_decimal(value):
    try:
        number = Decimal(str(value).strip().replace(",", ""))
    except InvalidOperation:
        return None
    return number if number.is_finite() else None


@pytest.mark.parametrize("date", OCTOBER_DATES)
def test_october_rows_match_official_fields_without_producer_parser(date):
    """Read source fields directly so a shared parser defect cannot self-confirm."""
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "config/tpex_historical_price_repair_202510.csv"
    manifest = _independent_csv_rows(manifest_path.read_bytes())
    entries = [row for row in manifest if row["date"] == date]
    assert len(entries) == 1
    entry = entries[0]
    raw = (root / entry["raw_path"]).read_bytes()
    receipt = json.loads((root / entry["receipt_path"]).read_bytes())
    raw_sha = hashlib.sha256(raw).hexdigest()
    assert raw_sha == entry["raw_sha256"] == receipt["sha256"]
    assert len(raw) == receipt["bytes"]
    assert receipt["requested_date"] == date
    assert receipt["original_publication_version_verified"] is False
    assert receipt["current_retrieval_of_historical_data"] is True
    assert entry["original_publication_version_verified"] == "false"
    source = json.loads(raw)
    assert source["stat"] == "ok" and source["date"] == date
    tables = [table for table in source["tables"]
              if table.get("title") == "上櫃股票每日收盤行情(不含定價)"]
    assert len(tables) == 1
    table = tables[0]
    assert table["date"] == f"{int(date[:4]) - 1911}/{date[4:6]}/{date[6:]}"
    fields = [field.strip() for field in table["fields"]]
    assert len(fields) == len(set(fields))
    assert all(len(values) == len(fields) for values in table["data"])
    source_rows = [dict(zip(fields, values)) for values in table["data"]]
    codes = [row["代號"].strip() for row in source_rows]
    assert len(codes) == len(set(codes))
    expected = {
        row["代號"].strip(): row for row in source_rows
        if re.fullmatch(r"[0-9]{4}", row["代號"].strip())
        and not row["代號"].strip().startswith("00")
        and _independent_decimal(row["收盤"]) is not None
        and _independent_decimal(row["成交股數"]) is not None
    }
    actual_payload = (root / entry["path"]).read_bytes()
    actual_rows = _independent_csv_rows(actual_payload)
    actual_otc = [row for row in actual_rows if row["market"] == "otc"]
    assert len(actual_otc) == len(expected) == int(entry["otc_after_rows"])
    assert {row["ticker"] for row in actual_otc} == set(expected)
    numeric_fields = {
        "open": "開盤", "high": "最高", "low": "最低", "close": "收盤",
        "volume": "成交股數", "turnover": "成交金額(元)",
    }
    for actual in actual_otc:
        official = expected[actual["ticker"]]
        assert actual["date"] == date
        assert actual["name"] == official["名稱"]
        for target, source_field in numeric_fields.items():
            assert _independent_decimal(actual[target]) == _independent_decimal(official[source_field]), (
                date, actual["ticker"], target, actual[target], official[source_field]
            )
    before = subprocess.check_output(
        ["git", "show", f"{entry['source_sha']}:{entry['path']}"], cwd=root,
    )
    assert hashlib.sha256(before).hexdigest() == entry["before_sha256"]
    assert hashlib.sha256(actual_payload).hexdigest() == entry["after_sha256"]
    listed_payloads = []
    for payload in (before, actual_payload):
        physical_rows = payload.decode("utf-8-sig").splitlines(keepends=True)
        parsed_rows = _independent_csv_rows(payload)
        assert len(physical_rows) == len(parsed_rows) + 1
        listed = [(line, row) for line, row in zip(physical_rows[1:], parsed_rows)
                  if row["market"] == "listed"]
        assert len(listed) == int(entry["listed_rows"])
        listed_payloads.append("".join(line for line, _ in listed).encode("utf-8"))
    assert listed_payloads[0] == listed_payloads[1]
    assert hashlib.sha256(listed_payloads[0]).hexdigest() == entry["listed_sha256"]
