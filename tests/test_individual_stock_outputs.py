from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pandas as pd


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
