from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_model_surface_registry as validator


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "model_surface_registry.csv"
STOCK_CONTRACT = ROOT / "config" / "stock_model_contract_registry.csv"


def registry_rows() -> list[dict[str, str]]:
    with REGISTRY.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def stock_contract_rows() -> list[dict[str, str]]:
    with STOCK_CONTRACT.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def test_model_surface_registry_validator_passes() -> None:
    assert validator.main() == 0


def test_model_surface_registry_has_required_schema() -> None:
    rows = registry_rows()

    assert rows
    assert list(rows[0]) == validator.REQUIRED_COLUMNS


def test_model_surface_registry_covers_stock_contract_models() -> None:
    surfaces = {row["surface_id"]: row for row in registry_rows()}

    for stock in stock_contract_rows():
        model_id = stock["model_id"]
        assert model_id in surfaces
        assert surfaces[model_id]["formal_contract_file"] == "config/stock_model_contract_registry.csv"
        assert surfaces[model_id]["stock_entry_signal"] == "true"
        for column in validator.STOCK_CONTRACT_APPROVAL_COLUMNS:
            assert surfaces[model_id][column] == stock[column]


def test_group_fund_rotation_is_not_stock_model_contract_surface() -> None:
    surfaces = {row["surface_id"]: row for row in registry_rows()}
    stock_ids = {row["model_id"] for row in stock_contract_rows()}

    group = surfaces["group_fund_rotation"]
    assert "group_fund_rotation" not in stock_ids
    assert group["surface_type"] == "theme_fund_rotation_model"
    assert group["selection_level"] == "theme_group"
    assert group["formal_contract_file"] == "pending_theme_model_contract"
    assert group["stock_entry_signal"] == "false"


def test_tdcc_weekly_stock_model_allowlist_stays_explicit() -> None:
    approved_stock_surfaces = sorted(
        row["surface_id"]
        for row in registry_rows()
        if row["formal_contract_file"] == "config/stock_model_contract_registry.csv"
        and row["approved_for_tdcc_weekly_pdf"] == "true"
    )

    assert approved_stock_surfaces == ["tdcc_short_term_continuation_d5_d10"]


def test_tdcc_weekly_ranking_formula_is_report_ranking_surface() -> None:
    surfaces = {row["surface_id"]: row for row in registry_rows()}
    stock_ids = {row["model_id"] for row in stock_contract_rows()}

    tdcc_ranking = surfaces["tdcc_weekly_ranking_formula"]
    assert "tdcc_weekly_ranking_formula" not in stock_ids
    assert tdcc_ranking["surface_type"] == "tdcc_weekly_ranking_model"
    assert tdcc_ranking["selection_level"] == "tdcc_weekly_report"
    assert tdcc_ranking["formal_contract_file"] == "pending_tdcc_ranking_contract"
    assert tdcc_ranking["primary_source_file"] == "scripts/build_tdcc_weekly_candidate_reports.py"
    assert "scripts/build_tdcc_weekly_ranking_backtest.py" in tdcc_ranking["implementation_sources"]
    assert tdcc_ranking["approved_for_tdcc_weekly_pdf"] == "true"
    assert tdcc_ranking["approved_for_daily_pdf"] == "false"
    assert tdcc_ranking["stock_entry_signal"] == "false"
    assert tdcc_ranking["research_parity_status"] == "research_backtest_advisory_only"


def test_script_declared_model_ids_are_registered() -> None:
    ids_by_path, errors = validator.collect_declared_script_model_ids()
    registered_ids = {row["surface_id"] for row in registry_rows()}

    assert errors == []
    assert "tdcc_weekly_ranking_formula" in ids_by_path["scripts/build_tdcc_weekly_ranking_backtest.py"]
    for path, model_ids in ids_by_path.items():
        assert model_ids <= registered_ids, path


def test_volume_v2_research_family_is_not_a_stock_or_pdf_surface() -> None:
    row = next(row for row in registry_rows() if row["surface_id"] == "volume_range_breakout_v2")
    assert row["surface_type"] == "model_research_family"
    assert row["selection_level"] == "research_backtest"
    assert row["stock_entry_signal"] == "false"
    assert row["approved_for_daily_pdf"] == "false"
    assert row["approved_for_tdcc_weekly_pdf"] == "false"
    assert row["approved_for_individual_pdf"] == "false"
    assert row["formal_contract_file"] == "config/model_research_artifact_ownership.csv"


def test_event_catalyst_overlay_is_not_stock_entry_signal() -> None:
    surfaces = {row["surface_id"]: row for row in registry_rows()}

    event = surfaces["event_catalyst_overlay"]
    assert event["formal_contract_file"] == "config/event_catalyst_overlay_contract.csv"
    assert event["surface_type"] == "event_catalyst_overlay_surface"
    assert event["stock_entry_signal"] == "false"
