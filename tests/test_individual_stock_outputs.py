from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_script(module_name: str):
    return importlib.import_module(module_name)


def test_packet_stock_id_collection_ignores_report_support_files(tmp_path, monkeypatch):
    module = load_script("build_individual_stock_chatgpt_packets")
    price_dir = tmp_path / "price"
    tdcc_dir = tmp_path / "tdcc"
    report_dir = tmp_path / "reports"
    price_dir.mkdir()
    tdcc_dir.mkdir()
    report_dir.mkdir()

    (price_dir / "2330.csv").write_text("date,close\n20260618,100\n", encoding="utf-8")
    (tdcc_dir / "1101.csv").write_text("date,value\n20260612,1\n", encoding="utf-8")
    (report_dir / "8299_latest.md").write_text("# report\n", encoding="utf-8")
    (report_dir / "individual_stock_read_protocol_latest.md").write_text("# protocol\n", encoding="utf-8")

    monkeypatch.setattr(module, "DATA_PRICE_DIR", price_dir)
    monkeypatch.setattr(module, "DATA_TDCC_DIR", tdcc_dir)
    monkeypatch.setattr(module, "REPORT_DIR", report_dir)

    ids = module.collect_stock_ids(
        [
            pd.DataFrame(
                {
                    "stock_id": [
                        "2353",
                        "006208",
                        "INDIVIDUAL",
                        "stock_id",
                        "123",
                        "1234567",
                    ]
                }
            )
        ]
    )

    assert "INDIVIDUAL" not in ids
    assert "INDIVIDUALSTOCKREADPROTOCOL" not in ids
    assert "1234567" not in ids
    assert ids == ["006208", "0123", "1101", "2330", "2353", "8299"]


def test_raw_index_stock_id_collection_ignores_report_support_files(tmp_path, monkeypatch):
    module = load_script("build_individual_stock_raw_data_index")
    price_dir = tmp_path / "price"
    tdcc_dir = tmp_path / "tdcc"
    report_dir = tmp_path / "reports"
    sell_dir = tmp_path / "sell"
    price_dir.mkdir()
    tdcc_dir.mkdir()
    report_dir.mkdir()
    sell_dir.mkdir()

    (price_dir / "2330.csv").write_text("date,close\n20260618,100\n", encoding="utf-8")
    (tdcc_dir / "1101.csv").write_text("date,value\n20260612,1\n", encoding="utf-8")
    (report_dir / "8299_latest.md").write_text("# report\n", encoding="utf-8")
    (report_dir / "individual_stock_read_protocol_latest.md").write_text("# protocol\n", encoding="utf-8")
    (sell_dir / "2353_sell_strategy_summary.md").write_text("# sell\n", encoding="utf-8")
    candidates_csv = tmp_path / "all_candidates.csv"
    candidates_csv.write_text("stock_id\n2484\nINDIVIDUAL\n123\n1234567\n", encoding="utf-8")

    monkeypatch.setattr(module, "DATA_PRICE_DIR", price_dir)
    monkeypatch.setattr(module, "DATA_TDCC_DIR", tdcc_dir)
    monkeypatch.setattr(module, "REPORT_DIR", report_dir)
    monkeypatch.setattr(module, "SELL_DIR", sell_dir)
    monkeypatch.setattr(module, "ALL_CANDIDATES_CSV", candidates_csv)
    monkeypatch.setattr(module, "WARRANT_FLOW_CSV", tmp_path / "missing_warrant.csv")
    monkeypatch.setattr(module, "DAILY_CANDIDATE_LOG", tmp_path / "missing_daily_log.csv")

    ids = module.collect_stock_ids()

    assert "INDIVIDUAL" not in ids
    assert "INDIVIDUALSTOCKREADPROTOCOL" not in ids
    assert "1234567" not in ids
    assert ids == {"0123", "1101", "2330", "2353", "2484", "8299"}


def write_tdcc_contract(
    path: Path,
    *,
    status: str = "pass",
    signal_date: str = "20260717",
    dataset_id: str = "tdcc-20260717-0123456789abcdef",
) -> None:
    snapshot = path.parent / "tdcc_holder_ratio_20260717.csv"
    readiness = path.parent / "readiness.json"
    snapshot.write_text("code,date\n2330,20260717\n", encoding="utf-8")
    readiness.write_text(
        json.dumps({"official_dates": ["20260703", signal_date]}),
        encoding="utf-8",
    )
    path.write_text(
        json.dumps(
            {
                "status": status,
                "schema_version": "tdcc_dataset_manifest_v1",
                "dataset_id": dataset_id,
                "signal_date": signal_date,
                "required_dates": ["20260703", signal_date],
                "current_stock_count": 1,
                "readiness_path": readiness.as_posix(),
                "snapshots": [
                    {
                        "date": signal_date,
                        "path": snapshot.as_posix(),
                    }
                ],
                "accepted_history_exceptions": [],
            }
        ),
        encoding="utf-8",
    )


def packet_text(
    *,
    latest_tdcc_date: str,
    history_status: str,
    freshness_status: str,
    tdcc_rows: int = 12,
    universe_status: str = "current",
    dataset_id: str = "tdcc-20260717-0123456789abcdef",
    continuity_status: str = "complete",
    missing_official_dates: str = "",
) -> str:
    return "\n".join(
        [
            "# packet",
            "",
            "## Metadata",
            "- stock_id: 2330",
            "- current_main_price_date: 20260717",
            f"- current_main_price_universe_status: {universe_status}",
            "- current_main_price_universe_source: official_daily_price_latest_main_price_date",
            "- listing_status_source_status: formal_listing_status_source_unavailable",
            f"- source_tdcc_dataset_id: {dataset_id}",
            "- official_tdcc_signal_date: 20260717",
            f"- latest_tdcc_date: {latest_tdcc_date}",
            f"- tdcc_rows: {tdcc_rows}",
            f"- tdcc_history_status: {history_status}",
            f"- tdcc_freshness_status: {freshness_status}",
            f"- tdcc_continuity_status: {continuity_status}",
            f"- tdcc_missing_official_dates: {missing_official_dates}",
            "",
            "## Stable Read URLs",
        ]
    )


def test_official_tdcc_contract_loaders_fail_closed(tmp_path):
    builder = load_script("build_individual_stock_chatgpt_packets")
    validator = load_script("validate_individual_stock_outputs")
    missing = tmp_path / "missing.json"
    for loader in [builder.load_official_tdcc_signal_date, validator.read_official_tdcc_signal_date]:
        with pytest.raises(SystemExit, match="Cannot load canonical TDCC dataset contract"):
            loader(missing)

    failed_contract = tmp_path / "failed.json"
    write_tdcc_contract(failed_contract, status="fail")
    for loader in [builder.load_official_tdcc_signal_date, validator.read_official_tdcc_signal_date]:
        with pytest.raises(SystemExit, match="manifest is not pass"):
            loader(failed_contract)

    wrong_identity_contract = tmp_path / "wrong-identity.json"
    write_tdcc_contract(wrong_identity_contract, dataset_id="wrong")
    for loader in [builder.load_official_tdcc_signal_date, validator.read_official_tdcc_signal_date]:
        with pytest.raises(SystemExit, match="manifest identity is invalid"):
            loader(wrong_identity_contract)

    valid_contract = tmp_path / "valid.json"
    write_tdcc_contract(valid_contract)
    for loader in [builder.load_official_tdcc_signal_date, validator.read_official_tdcc_signal_date]:
        assert loader(valid_contract) == "20260717"


def test_current_main_price_universe_is_dated_and_fail_closed(tmp_path):
    builder = load_script("build_individual_stock_chatgpt_packets")
    validator = load_script("validate_individual_stock_outputs")
    universe_path = tmp_path / "official_daily_price_latest.csv"
    universe_path.write_text(
        "date,stock_id,stock_name\n20260717,2330,TSMC\n",
        encoding="utf-8",
    )
    for loader in [builder.load_current_main_price_universe, validator.read_current_main_price_universe]:
        assert loader("20260717", universe_path) == {"2330"}
        with pytest.raises(SystemExit, match="Current main-price universe date mismatch"):
            loader("20260716", universe_path)


def test_tdcc_packet_20260703_fails_then_rebuilt_20260717_passes(tmp_path):
    builder = load_script("build_individual_stock_chatgpt_packets")
    validator = load_script("validate_individual_stock_outputs")
    packet_path = tmp_path / "2330_packet_latest.md"

    _, stale_history_status, stale_freshness_status, _ = builder.status_from_rows(
        180, 12, "20260703", "20260717"
    )
    assert stale_history_status == "tdcc_window_stale"
    assert stale_freshness_status == "tdcc_window_stale"
    packet_path.write_text(
        packet_text(
            latest_tdcc_date="20260703",
            history_status=stale_history_status,
            freshness_status=stale_freshness_status,
        ),
        encoding="utf-8",
    )
    stale_index_row = {
        "current_main_price_date": "20260717",
        "current_main_price_universe_status": "current",
        "current_main_price_universe_source": "official_daily_price_latest_main_price_date",
        "listing_status_source_status": "formal_listing_status_source_unavailable",
        "official_tdcc_signal_date": "20260717",
        "latest_tdcc_date": "20260703",
        "tdcc_rows": "12",
        "tdcc_history_status": stale_history_status,
        "tdcc_freshness_status": stale_freshness_status,
    }
    stale_errors = validator.validate_tdcc_packet_freshness(
        "2330", packet_path, stale_index_row, "20260717", main_price_date="20260717"
    )
    assert any("packet latest_tdcc_date mismatch" in error for error in stale_errors)
    assert any("expected tdcc_history_ready" in error for error in stale_errors)

    _, fresh_history_status, fresh_freshness_status, _ = builder.status_from_rows(
        180, 12, "20260717", "20260717"
    )
    assert fresh_history_status == "tdcc_history_ready"
    assert fresh_freshness_status == "tdcc_window_fresh"
    packet_path.write_text(
        packet_text(
            latest_tdcc_date="20260717",
            history_status=fresh_history_status,
            freshness_status=fresh_freshness_status,
        ),
        encoding="utf-8",
    )
    fresh_index_row = {
        "current_main_price_date": "20260717",
        "current_main_price_universe_status": "current",
        "current_main_price_universe_source": "official_daily_price_latest_main_price_date",
        "listing_status_source_status": "formal_listing_status_source_unavailable",
        "official_tdcc_signal_date": "20260717",
        "latest_tdcc_date": "20260717",
        "tdcc_rows": "12",
        "tdcc_history_status": fresh_history_status,
        "tdcc_freshness_status": fresh_freshness_status,
    }
    assert validator.validate_tdcc_packet_freshness(
        "2330", packet_path, fresh_index_row, "20260717", main_price_date="20260717"
    ) == []


@pytest.mark.parametrize(
    ("tdcc_rows", "latest_tdcc_date", "expected_history_status", "expected_freshness_status"),
    [
        (0, "", "tdcc_missing", "tdcc_missing"),
        (7, "20260717", "insufficient_tdcc_history", "tdcc_window_fresh"),
        (8, "20260717", "tdcc_history_ready", "tdcc_window_fresh"),
    ],
)
def test_tdcc_missing_and_fresh_history_states_are_accepted(
    tmp_path,
    tdcc_rows,
    latest_tdcc_date,
    expected_history_status,
    expected_freshness_status,
):
    builder = load_script("build_individual_stock_chatgpt_packets")
    validator = load_script("validate_individual_stock_outputs")
    packet_path = tmp_path / "2330_packet_latest.md"
    _, history_status, freshness_status, _ = builder.status_from_rows(
        180, tdcc_rows, latest_tdcc_date, "20260717"
    )
    assert history_status == expected_history_status
    assert freshness_status == expected_freshness_status
    packet_path.write_text(
        packet_text(
            latest_tdcc_date=latest_tdcc_date,
            history_status=history_status,
            freshness_status=freshness_status,
            tdcc_rows=tdcc_rows,
        ),
        encoding="utf-8",
    )
    index_row = {
        "current_main_price_date": "20260717",
        "current_main_price_universe_status": "current",
        "current_main_price_universe_source": "official_daily_price_latest_main_price_date",
        "listing_status_source_status": "formal_listing_status_source_unavailable",
        "official_tdcc_signal_date": "20260717",
        "latest_tdcc_date": latest_tdcc_date,
        "tdcc_rows": str(tdcc_rows),
        "tdcc_history_status": history_status,
        "tdcc_freshness_status": freshness_status,
    }
    assert validator.validate_tdcc_packet_freshness(
        "2330", packet_path, index_row, "20260717", main_price_date="20260717"
    ) == []


def test_noncurrent_main_price_universe_preserves_historical_tdcc(tmp_path):
    builder = load_script("build_individual_stock_chatgpt_packets")
    validator = load_script("validate_individual_stock_outputs")
    packet_path = tmp_path / "3426_packet_latest.md"
    _, history_status, freshness_status, _ = builder.status_from_rows(
        180, 5, "20260529", "20260717", is_current_main_price_universe=False
    )
    assert history_status == "historical_only_noncurrent"
    assert freshness_status == "historical_only_noncurrent"
    packet_path.write_text(
        packet_text(
            latest_tdcc_date="20260529",
            history_status=history_status,
            freshness_status=freshness_status,
            tdcc_rows=5,
            universe_status="historical_only_noncurrent",
        ),
        encoding="utf-8",
    )
    index_row = {
        "current_main_price_date": "20260717",
        "current_main_price_universe_status": "historical_only_noncurrent",
        "current_main_price_universe_source": "official_daily_price_latest_main_price_date",
        "listing_status_source_status": "formal_listing_status_source_unavailable",
        "official_tdcc_signal_date": "20260717",
        "latest_tdcc_date": "20260529",
        "tdcc_rows": "5",
        "tdcc_history_status": history_status,
        "tdcc_freshness_status": freshness_status,
    }
    assert validator.validate_tdcc_packet_freshness(
        "3426",
        packet_path,
        index_row,
        "20260717",
        main_price_date="20260717",
        is_current_main_price_universe=False,
        source_tdcc_rows=5,
        source_latest_tdcc_date="20260529",
    ) == []


def test_accepted_canonical_gap_is_degraded_and_disclosed(tmp_path):
    builder = load_script("build_individual_stock_chatgpt_packets")
    validator = load_script("validate_individual_stock_outputs")
    packet_path = tmp_path / "2380_packet_latest.md"
    dataset_id = "tdcc-20260717-0123456789abcdef"
    _, history_status, freshness_status, notes = builder.status_from_rows(
        180,
        11,
        "20260717",
        "20260717",
        tdcc_continuity_status="accepted_history_exception",
        missing_official_dates=("20260626",),
    )
    assert history_status == "tdcc_history_degraded_exception"
    assert freshness_status == "tdcc_window_degraded"
    assert "20260626" in notes
    packet_path.write_text(
        packet_text(
            latest_tdcc_date="20260717",
            history_status=history_status,
            freshness_status=freshness_status,
            tdcc_rows=11,
            dataset_id=dataset_id,
            continuity_status="accepted_history_exception",
            missing_official_dates="20260626",
        ),
        encoding="utf-8",
    )
    index_row = {
        "current_main_price_date": "20260717",
        "current_main_price_universe_status": "current",
        "current_main_price_universe_source": "official_daily_price_latest_main_price_date",
        "listing_status_source_status": "formal_listing_status_source_unavailable",
        "source_tdcc_dataset_id": dataset_id,
        "official_tdcc_signal_date": "20260717",
        "latest_tdcc_date": "20260717",
        "tdcc_rows": "11",
        "tdcc_history_status": history_status,
        "tdcc_freshness_status": freshness_status,
        "tdcc_continuity_status": "accepted_history_exception",
        "tdcc_missing_official_dates": "20260626",
    }
    assert validator.validate_tdcc_packet_freshness(
        "2380",
        packet_path,
        index_row,
        "20260717",
        main_price_date="20260717",
        source_tdcc_rows=11,
        source_latest_tdcc_date="20260717",
        source_tdcc_dataset_id=dataset_id,
        source_tdcc_continuity_status="accepted_history_exception",
        source_tdcc_missing_official_dates=("20260626",),
    ) == []


def test_historical_packet_and_index_cannot_share_wrong_tdcc_source_date(tmp_path):
    validator = load_script("validate_individual_stock_outputs")
    packet_path = tmp_path / "3426_packet_latest.md"
    packet_path.write_text(
        packet_text(
            latest_tdcc_date="20260530",
            history_status="historical_only_noncurrent",
            freshness_status="historical_only_noncurrent",
            tdcc_rows=6,
            universe_status="historical_only_noncurrent",
        ),
        encoding="utf-8",
    )
    wrong_index_row = {
        "current_main_price_date": "20260717",
        "current_main_price_universe_status": "historical_only_noncurrent",
        "current_main_price_universe_source": "official_daily_price_latest_main_price_date",
        "listing_status_source_status": "formal_listing_status_source_unavailable",
        "official_tdcc_signal_date": "20260717",
        "latest_tdcc_date": "20260530",
        "tdcc_rows": "6",
        "tdcc_history_status": "historical_only_noncurrent",
        "tdcc_freshness_status": "historical_only_noncurrent",
    }
    errors = validator.validate_tdcc_packet_freshness(
        "3426",
        packet_path,
        wrong_index_row,
        "20260717",
        main_price_date="20260717",
        is_current_main_price_universe=False,
        source_tdcc_rows=5,
        source_latest_tdcc_date="20260529",
    )
    assert any("packet latest_tdcc_date source mismatch" in error for error in errors)
    assert any("packet tdcc_rows source mismatch" in error for error in errors)
    assert any("packet index latest_tdcc_date mismatch" in error for error in errors)
    assert any("packet index tdcc_rows mismatch" in error for error in errors)
