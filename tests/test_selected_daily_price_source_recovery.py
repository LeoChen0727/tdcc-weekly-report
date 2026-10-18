from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

import pandas as pd
import pytest
import yaml

import scripts.run_selected_daily_price_source_recovery as recovery


SOURCE_BASE = "a" * 40
DATES = ["20261005", "20261006"]
EXACT_EIGHT = "20261005,20261006,20261007,20261008,20261012,20261013,20261014,20261015"


@pytest.fixture
def capture_setup(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    histories = root / "data/stock_price_history"
    histories.mkdir(parents=True)
    (histories / "1000.csv").write_text("preserved", encoding="utf-8")
    (histories / "4000.csv").write_text("untouched", encoding="utf-8")
    monkeypatch.setattr(recovery, "git_head", lambda root: SOURCE_BASE)
    monkeypatch.setattr(recovery.repair, "validate_selected_canonical_name_sources", lambda *a: [])
    return root, tmp_path / "capture"


def official_frame(date):
    return pd.DataFrame(
        {
            "date": [date] * 1300,
            "stock_id": [str(1000 + n) for n in range(1300)],
            "stock_name": ["測試"] * 1300,
            "market": ["TWSE"] * 700 + ["TPEx"] * 600,
            "open": [10] * 1300,
            "high": [11] * 1300,
            "low": [9] * 1300,
            "close": [10] * 1300,
            "volume": [1000] * 1300,
            "trading_value": [10000] * 1300,
            "source": ["official_fixture"] * 1300,
        }
    )


def test_capture_binds_normalized_csv_and_measures_real_eligible_history_counts(capture_setup):
    root, target = capture_setup
    seen = []

    def fetch(date, retries, sleep):
        assert recovery.repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
        seen.append(date)
        return official_frame(date), {
            "full_market_ok": True,
            "fetch_response_provenance": [{"response_sha256": "b" * 64}],
        }, []

    prior = recovery.repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
    result = recovery.capture_contracts(root, DATES, SOURCE_BASE, target, fetch_func=fetch)
    assert seen == DATES
    assert recovery.repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES == prior
    first = result["date_contracts"][0]
    payload = (target / "daily_price_20261005.csv").read_bytes()
    assert payload.startswith(b"\xef\xbb\xbf")
    assert first["sha256"] == hashlib.sha256(payload).hexdigest()
    assert first["sha256"] != "b" * 64
    assert first["row_count"] == 1300
    assert result["expected_stock_union_count"] == 1300
    assert result["expected_selected_row_count"] == 2600
    assert result["expected_existing_history_count"] == 1
    assert result["expected_created_history_count"] == 1299
    assert result["expected_untouched_history_count"] == 1
    assert "1000" not in result["created_stock_ids"]
    assert (root / "data/stock_price_history/1000.csv").read_text() == "preserved"
    assert not (root / "data/daily_price").exists()
    assert not (root / "output").exists()


def test_capture_rejects_base_drift_before_network(capture_setup):
    root, target = capture_setup
    with pytest.raises(ValueError, match="source_base_sha"):
        recovery.capture_contracts(root, DATES, "c" * 40, target, fetch_func=lambda *a: pytest.fail())
    assert not target.exists()


def test_failed_official_capture_restores_exact_mode_without_source_writes(capture_setup):
    root, target = capture_setup
    prior = recovery.repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
    with pytest.raises(ValueError, match="official capture failed"):
        recovery.capture_contracts(
            root, DATES, SOURCE_BASE, target,
            fetch_func=lambda *a: (pd.DataFrame(), {"full_market_ok": False}, ["unavailable"]),
        )
    assert recovery.repair.fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES == prior
    assert not (root / "data/daily_price").exists()
    assert not (target / "contracts.json").exists()
    receipt = json.loads((target / "official_capture_20261005.json").read_text(encoding="utf-8"))
    assert receipt["status"]["full_market_ok"] is False


def test_incomplete_market_capture_is_rejected(capture_setup):
    root, target = capture_setup
    with pytest.raises(ValueError, match="full-market capture is insufficient"):
        recovery.capture_contracts(
            root, DATES, SOURCE_BASE, target,
            fetch_func=lambda date, *a: (official_frame(date).iloc[:1200], {"full_market_ok": True}, []),
        )
    assert not (root / "data/daily_price").exists()


def sample_contracts():
    return {
        "source_base_sha": SOURCE_BASE, "selected_dates": DATES,
        "date_contracts": [{"date": d, "sha256": "d" * 64, "row_count": 1300} for d in DATES],
        "expected_stock_union_count": 1300, "expected_selected_row_count": 2600,
        "expected_existing_history_count": 1299, "expected_created_history_count": 1,
        "expected_untouched_history_count": 5, "created_stock_ids": ["2299"],
    }


def test_apply_uses_existing_selected_producers_and_independent_validator_only(tmp_path):
    calls = []
    recovery.apply_contracts(tmp_path, tmp_path / "capture", sample_contracts(), runner=lambda cmd, **kw: calls.append((cmd, kw)))
    assert [cmd[1] for cmd, _ in calls] == [
        "scripts/repair_daily_price_range.py", "scripts/build_stock_price_history.py",
        "scripts/validate_daily_price_history_continuity.py",
    ]
    source, history, validator = [cmd for cmd, _ in calls]
    assert source[source.index("--dates") + 1] == ",".join(DATES)
    assert source.count("--expected-date-contract") == 2
    assert history.count("--repair-date") == 2
    assert history[history.index("--allow-create-stock-id") + 1] == "2299"
    assert validator.count("--selected-date-contract") == 2
    assert "--no-write-report" in validator
    assert "--pathspec-nul-output" in validator
    assert "--expected-created-stock-id" in validator
    for cmd, kw in calls:
        assert kw == {"cwd": tmp_path, "check": True}
        assert "--incremental-latest" not in cmd
        assert "--full-rebuild-if-source-recovered" not in cmd


def test_apply_stops_at_first_producer_failure(tmp_path):
    calls = []

    def failed(cmd, **kwargs):
        calls.append(cmd)
        raise subprocess.CalledProcessError(1, cmd)

    with pytest.raises(subprocess.CalledProcessError):
        recovery.apply_contracts(tmp_path, tmp_path / "capture", sample_contracts(), runner=failed)
    assert len(calls) == 1


def test_source_only_profile_preserves_legacy_and_has_exact_eight_scope():
    path = Path(__file__).resolve().parents[1] / ".github/workflows/repair_daily_price_range.yml"
    text = path.read_text(encoding="utf-8")
    workflow = yaml.safe_load(text)
    inputs = workflow.get("on", workflow.get(True))["workflow_dispatch"]["inputs"]
    assert inputs["source_profile"]["default"] == "legacy"
    steps = workflow["jobs"]["repair-daily-price-range"]["steps"]
    source_step = next(s for s in steps if s["name"] == "Recover approved selected sources without production resume")
    assert source_step["if"] == "inputs.source_profile == 'selected_source_only'"
    assert EXACT_EIGHT in source_step["run"]
    assert "20261016" not in source_step["run"]
    assert "--max-days 8" in source_step["run"]
    assert "--no-write-report" in source_step["run"]
    assert "--incremental-latest" not in source_step["run"]
    assert "gh workflow run" not in text
    for step in steps:
        if step.get("name") in {
            "Repair exact selected daily prices and controlled stock histories",
            "Repair legacy daily price range and rebuild histories",
            "Stage only exact selected-date repair paths",
        }:
            assert "inputs.source_profile == 'legacy'" in step["if"]
    stage = next(s for s in steps if s["name"] == "Stage only validated selected source-only paths")
    assert "--pathspec-from-file=" in stage["run"]
    assert "--verify-staged-paths-json" in stage["run"]
