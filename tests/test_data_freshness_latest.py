import json
from types import SimpleNamespace
from pathlib import Path

import pandas as pd
import pytest

import build_data_freshness_latest as freshness


def test_warrant_flow_date_falls_back_to_by_stock_when_flow_is_header_only(tmp_path, monkeypatch):
    flow = tmp_path / "warrant_flow_latest.csv"
    by_stock = tmp_path / "warrant_flow_by_stock_latest.csv"
    market_report = tmp_path / "warrant_market_report_latest.md"
    fetch_report = tmp_path / "warrant_daily_fetch_latest.md"

    flow.write_text("date,stock_id,warrant_flow_signal\n", encoding="utf-8")
    by_stock.write_text(
        "date,stock_id,stock_name,warrant_flow_signal\n"
        "20260605,,,\n",
        encoding="utf-8",
    )
    market_report.write_text("", encoding="utf-8")
    fetch_report.write_text("", encoding="utf-8")

    monkeypatch.setattr(freshness, "WARRANT_FLOW_CSV", flow)
    monkeypatch.setattr(freshness, "WARRANT_FLOW_BY_STOCK_CSV", by_stock)
    monkeypatch.setattr(freshness, "WARRANT_MARKET_REPORT_MD", market_report)
    monkeypatch.setattr(freshness, "WARRANT_DAILY_FETCH_MD", fetch_report)

    assert freshness.extract_warrant_flow_date() == "20260605"
    assert freshness.extract_warrant_flow_state() == (
        "20260605",
        False,
        "warrant data date present but stock-level rows unavailable or observe-only in warrant_flow_by_stock_latest.csv",
    )


def test_warrant_flow_date_falls_back_to_market_report_when_csvs_have_no_rows(tmp_path, monkeypatch):
    flow = tmp_path / "warrant_flow_latest.csv"
    by_stock = tmp_path / "warrant_flow_by_stock_latest.csv"
    market_report = tmp_path / "warrant_market_report_latest.md"
    fetch_report = tmp_path / "warrant_daily_fetch_latest.md"

    flow.write_text("date,stock_id,warrant_flow_signal\n", encoding="utf-8")
    by_stock.write_text("date,stock_id,warrant_flow_signal\n", encoding="utf-8")
    market_report.write_text("- data_date: `20260605`\n- raw_rows: `0`\n", encoding="utf-8")
    fetch_report.write_text("", encoding="utf-8")

    monkeypatch.setattr(freshness, "WARRANT_FLOW_CSV", flow)
    monkeypatch.setattr(freshness, "WARRANT_FLOW_BY_STOCK_CSV", by_stock)
    monkeypatch.setattr(freshness, "WARRANT_MARKET_REPORT_MD", market_report)
    monkeypatch.setattr(freshness, "WARRANT_DAILY_FETCH_MD", fetch_report)

    assert freshness.extract_warrant_flow_date() == "20260605"
    assert freshness.extract_warrant_flow_state() == (
        "20260605",
        False,
        "warrant data date present but stock-level rows unavailable or observe-only in warrant_market_report_latest.md",
    )


def test_warrant_ready_requires_usable_stock_level_rows():
    ready, note = freshness.determine_warrant_ready(
        main_price_date="20260605",
        warrant_flow_date="20260605",
        warrant_data_ready=False,
        warrant_data_note="warrant data date present but stock-level rows unavailable or observe-only",
    )

    assert ready is False
    assert "stock-level warrant data is unavailable" in note


def test_warrant_flow_state_prefers_current_observe_only_over_stale_rows(tmp_path, monkeypatch):
    flow = tmp_path / "warrant_flow_latest.csv"
    by_stock = tmp_path / "warrant_flow_by_stock_latest.csv"
    market_report = tmp_path / "warrant_market_report_latest.md"
    fetch_report = tmp_path / "warrant_daily_fetch_latest.md"

    flow.write_text(
        "date,stock_id,warrant_flow_signal\n"
        "20260603,2330,call_inflow\n",
        encoding="utf-8",
    )
    by_stock.write_text(
        "date,stock_id,stock_name,warrant_flow_signal,data_quality_note\n"
        "20260605,,,,權證原始資料不足 / 僅能觀察\n",
        encoding="utf-8",
    )
    market_report.write_text("", encoding="utf-8")
    fetch_report.write_text("", encoding="utf-8")

    monkeypatch.setattr(freshness, "WARRANT_FLOW_CSV", flow)
    monkeypatch.setattr(freshness, "WARRANT_FLOW_BY_STOCK_CSV", by_stock)
    monkeypatch.setattr(freshness, "WARRANT_MARKET_REPORT_MD", market_report)
    monkeypatch.setattr(freshness, "WARRANT_DAILY_FETCH_MD", fetch_report)

    assert freshness.extract_warrant_flow_state() == (
        "20260605",
        False,
        "warrant data date present but stock-level rows unavailable or observe-only in warrant_flow_by_stock_latest.csv",
    )


def test_group_rotation_theme_state_rejects_unreadable_pdf_theme_values(tmp_path, monkeypatch):
    group_rotation = tmp_path / "daily_candidate_group_rotation_latest.csv"
    group_rotation.write_text(
        "theme,theme_display_zh,theme_resolution_status\n"
        "其他,其他,resolved\n"
        "91,91,resolved\n"
        "DR_or_foreign_listing,DR_or_foreign_listing,resolved\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(freshness, "GROUP_ROTATION_CSV", group_rotation)

    ready, note = freshness.group_rotation_theme_state()

    assert ready is False
    assert "unresolved/raw theme rows" in note


def test_daily_pdf_ready_requires_resolved_group_rotation_theme_display():
    ready, note = freshness.determine_daily_pdf_ready(
        report_ready=True,
        warrant_ready=True,
        warrant_publish_allowed=True,
        report_ready_note="core daily data dates match main_price_date",
        warrant_ready_note="warrant_flow_date matches main_price_date",
        warrant_source_status="ok",
        warrant_pdf_visibility="visible",
        group_rotation_theme_ready=False,
        group_rotation_theme_note="group rotation has unresolved/raw theme rows",
    )

    assert ready is False
    assert "group rotation theme display not ready" in note


def test_warrant_publish_policy_resets_to_ok_when_current_warrant_is_ready():
    result = freshness.warrant_publish_policy(
        True,
        {
            "status": "warning_grace",
            "warrant_pdf_visibility": "hidden_unavailable",
            "daily_publish_allowed": "True",
            "model_effect_allowed": "False",
            "pdf_effect_allowed": "False",
        },
    )

    assert result == (
        True,
        "ok",
        "current-date warrant layer ready",
        "visible",
        "True",
        "True",
        "0",
    )


def test_daily_pdf_ready_allows_bounded_warrant_grace_without_using_warrant_layer():
    ready, note = freshness.determine_daily_pdf_ready(
        report_ready=True,
        warrant_ready=False,
        warrant_publish_allowed=True,
        report_ready_note="core daily data dates match main_price_date",
        warrant_ready_note="warrant_flow_date matches main_price_date but stock-level warrant data is unavailable",
        warrant_source_status="warning_grace",
        warrant_pdf_visibility="hidden_unavailable",
        group_rotation_theme_ready=True,
        group_rotation_theme_note="group rotation themes resolved for PDF display",
    )

    assert ready is True
    assert "warrant source unavailable within bounded grace" in note
    assert "warrant_pdf_visibility=hidden_unavailable" in note


def test_daily_pdf_ready_rejects_warrant_failure_outside_bounded_grace():
    ready, note = freshness.determine_daily_pdf_ready(
        report_ready=True,
        warrant_ready=False,
        warrant_publish_allowed=False,
        report_ready_note="core daily data dates match main_price_date",
        warrant_ready_note="current-date warrant source failed beyond bounded grace",
        warrant_source_status="failed",
        warrant_pdf_visibility="blocked_unavailable",
        group_rotation_theme_ready=True,
        group_rotation_theme_note="group rotation themes resolved for PDF display",
    )

    assert ready is False
    assert "warrant layer not ready" in note


def test_market_session_gate_requires_expected_main_price_date_match() -> None:
    ready, note = freshness.apply_market_session_gate(
        report_ready=True,
        report_ready_note="core daily data dates match main_price_date",
        market_session_status="open_confirmed",
        market_session_date="20260713",
        expected_main_price_date="20260713",
        main_price_date="20260709",
    )

    assert ready is False
    assert "main_price_date=20260709" in note
    assert "expected_main_price_date=20260713" in note


def test_historical_replay_main_price_date_accepts_exact_paired_raw_high_water() -> None:
    assert freshness.validate_historical_replay_main_price_date(
        "20260724",
        "20260728",
        daily_price_high_water_date="20260728",
        stock_price_history_high_water_date="20260728",
    ) == "20260724"


def test_historical_replay_main_price_date_accepts_high_water_equality() -> None:
    assert freshness.validate_historical_replay_main_price_date(
        "20260728",
        "20260728",
        daily_price_high_water_date="20260728",
        stock_price_history_high_water_date="20260728",
    ) == "20260728"


@pytest.mark.parametrize(
    ("target", "expected", "daily", "history", "message"),
    [
        ("20260230", "20260728", "20260728", "20260728", "valid calendar date"),
        ("20260729", "20260728", "20260728", "20260728", "must not be later"),
        ("20260724", "20260728", "20260727", "20260728", "exact paired"),
    ],
)
def test_historical_replay_main_price_date_rejects_invalid_or_unpaired_inputs(
    target: str,
    expected: str,
    daily: str,
    history: str,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        freshness.validate_historical_replay_main_price_date(
            target,
            expected,
            daily_price_high_water_date=daily,
            stock_price_history_high_water_date=history,
        )


def _write_historical_replay_freshness_prerequisites(
    tmp_path: Path,
    monkeypatch,
    *,
    status_overrides: dict | None = None,
) -> None:
    monkeypatch.chdir(tmp_path)
    official = tmp_path / "official_daily_price_latest.csv"
    status_path = tmp_path / "official_price_fetch_latest.json"
    continuity_path = tmp_path / "daily_price_history_continuity_latest.json"
    rows = [
        {
            "date": "20260724",
            "stock_id": f"{index:04d}",
            "market": "TWSE" if index < 700 else "TPEx",
        }
        for index in range(freshness.MIN_HISTORICAL_REPLAY_OFFICIAL_PRICE_ROWS)
    ]
    official_frame = pd.DataFrame(rows)
    official_frame.to_csv(official, index=False)
    target_dir = tmp_path / "data" / "daily_price"
    target_dir.mkdir(parents=True)
    official_frame.to_csv(target_dir / "daily_price_20260724.csv", index=False)
    official_frame.iloc[::-1].to_csv(target_dir / "20260724.csv", index=False)
    status = {
        "mode": "reconstructed_source_tail_gap_preserve_existing_price_history",
        "target_date": "20260724",
        "saved_price_date": "20260724",
        "is_target_date": True,
        "result": "success_target_full_market",
        "full_market_ok": True,
        "publication_status": "reconstructed_not_as_published",
        "as_published": False,
        "fallback_used": False,
        "calculation_context_max_date": "20260724",
        "future_row_count": 0,
        "future_rows_used": False,
        "price_history_high_water_date": "20260728",
        "preserved_target_slice_evidence": {
            "mode": "preserve_existing_price_history",
            "price_history_high_water_date": "20260728",
        },
        "total_rows": freshness.MIN_HISTORICAL_REPLAY_OFFICIAL_PRICE_ROWS,
        "twse_rows": 700,
        "tpex_rows": freshness.MIN_HISTORICAL_REPLAY_OFFICIAL_PRICE_ROWS - 700,
        "paths": {
            "dated_csv": "data/daily_price/daily_price_20260724.csv",
            "dated_alt_csv": "data/daily_price/20260724.csv",
            "latest_csv": "output/latest/official_daily_price_latest.csv",
        },
    }
    status.update(status_overrides or {})
    status_path.write_text(json.dumps(status), encoding="utf-8")
    continuity_path.write_text(
        json.dumps(
            {
                "status": "pass",
                "main_price_date": "20260724",
                "expected_trading_dates": ["20260720", "20260721", "20260724"],
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(freshness, "OFFICIAL_DAILY_PRICE_CSV", official)
    monkeypatch.setattr(freshness, "OFFICIAL_PRICE_FETCH_JSON", status_path)
    monkeypatch.setattr(freshness, "DAILY_PRICE_HISTORY_CONTINUITY_JSON", continuity_path)


def test_historical_replay_freshness_prerequisites_accept_exact_preserve_contract(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_historical_replay_freshness_prerequisites(tmp_path, monkeypatch)

    freshness.validate_historical_replay_freshness_prerequisites(
        "20260724",
        "20260728",
    )


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"mode": "reconstructed_source_tail_gap"}, "status contract mismatch"),
        ({"fallback_used": True}, "status contract mismatch"),
        ({"future_row_count": 1, "future_rows_used": True}, "status contract mismatch"),
        ({"calculation_context_max_date": "20260728"}, "status contract mismatch"),
        ({"total_rows": 1299}, "count parity mismatch"),
        ({"price_history_high_water_date": "20260727"}, "status contract mismatch"),
    ],
)
def test_historical_replay_freshness_prerequisites_reject_unsafe_status(
    tmp_path: Path,
    monkeypatch,
    overrides: dict,
    message: str,
) -> None:
    _write_historical_replay_freshness_prerequisites(
        tmp_path,
        monkeypatch,
        status_overrides=overrides,
    )

    with pytest.raises(ValueError, match=message):
        freshness.validate_historical_replay_freshness_prerequisites(
            "20260724",
            "20260728",
        )


def test_historical_replay_freshness_prerequisites_reject_missing_preserved_target(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_historical_replay_freshness_prerequisites(tmp_path, monkeypatch)
    (tmp_path / "data" / "daily_price" / "20260724.csv").unlink()

    with pytest.raises(ValueError, match="preserved target file is missing"):
        freshness.validate_historical_replay_freshness_prerequisites(
            "20260724",
            "20260728",
        )


def test_historical_replay_freshness_prerequisites_reject_target_content_mismatch(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_historical_replay_freshness_prerequisites(tmp_path, monkeypatch)
    path = tmp_path / "data" / "daily_price" / "daily_price_20260724.csv"
    frame = pd.read_csv(path, dtype=str)
    frame.loc[0, "stock_id"] = "DIFF"
    frame.to_csv(path, index=False)

    with pytest.raises(ValueError, match="content differs"):
        freshness.validate_historical_replay_freshness_prerequisites(
            "20260724",
            "20260728",
        )


def test_historical_replay_freshness_prerequisites_reject_continuity_without_target_tail(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _write_historical_replay_freshness_prerequisites(tmp_path, monkeypatch)
    freshness.DAILY_PRICE_HISTORY_CONTINUITY_JSON.write_text(
        json.dumps(
            {
                "status": "pass",
                "main_price_date": "20260724",
                "expected_trading_dates": ["20260720", "20260721"],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="expected_trading_dates"):
        freshness.validate_historical_replay_freshness_prerequisites(
            "20260724",
            "20260728",
        )


def _patch_status_build_dependencies(monkeypatch, *, validated_history_date: str) -> None:
    monkeypatch.setattr(
        freshness,
        "latest_stock_price_history_date",
        lambda: validated_history_date,
    )
    monkeypatch.setattr(freshness, "raw_daily_price_high_water_date", lambda: "20260728")
    monkeypatch.setattr(
        freshness,
        "raw_stock_price_history_high_water_date",
        lambda: "20260728",
    )
    monkeypatch.setattr(
        freshness,
        "validate_historical_replay_freshness_prerequisites",
        lambda target_date, expected_high_water: None,
    )
    monkeypatch.setattr(freshness, "extract_stock_monitor_price_date", lambda: "20260717")
    monkeypatch.setattr(freshness, "extract_official_price_fetch_date", lambda: "20260724")
    monkeypatch.setattr(freshness, "extract_csv_max_date", lambda *args, **kwargs: "20260717")
    monkeypatch.setattr(
        freshness,
        "extract_warrant_flow_state",
        lambda: ("20260724", True, "ready"),
    )
    monkeypatch.setattr(
        freshness,
        "read_market_session_status",
        lambda: {
            "market_status": "open_confirmed",
            "market_session_date": "20260724",
            "expected_main_price_date": "20260724",
        },
    )
    monkeypatch.setattr(freshness, "read_warrant_source_status", lambda: {})
    monkeypatch.setattr(
        freshness,
        "warrant_publish_policy",
        lambda *args, **kwargs: (True, "ok", "ready", "visible", "True", "True", "0"),
    )
    monkeypatch.setattr(
        freshness,
        "group_rotation_theme_state",
        lambda: (True, "group rotation themes resolved"),
    )


def test_historical_replay_override_keeps_raw_actual_date_and_forces_readiness_false(
    monkeypatch,
) -> None:
    _patch_status_build_dependencies(monkeypatch, validated_history_date="20260728")

    frame = freshness.build_status(
        historical_replay_main_price_date="20260724",
        expected_price_history_high_water_date="20260728",
    )
    row = frame.iloc[0]

    assert row["main_price_date"] == "20260724"
    assert row["main_price_date_source"] == "historical_replay_override"
    assert row["historical_replay_main_price_date"] == "20260724"
    assert row["expected_price_history_high_water_date"] == "20260728"
    assert row["actual_stock_price_history_date"] == "20260728"
    assert bool(row["report_ready"]) is False
    assert bool(row["daily_pdf_ready"]) is False


def test_historical_replay_override_at_high_water_keeps_readiness_false(
    monkeypatch,
) -> None:
    _patch_status_build_dependencies(monkeypatch, validated_history_date="20260728")

    frame = freshness.build_status(
        historical_replay_main_price_date="20260728",
        expected_price_history_high_water_date="20260728",
    )
    row = frame.iloc[0]

    assert row["main_price_date"] == "20260728"
    assert row["main_price_date_source"] == "historical_replay_override"
    assert row["expected_price_history_high_water_date"] == "20260728"
    assert bool(row["report_ready"]) is False
    assert bool(row["daily_pdf_ready"]) is False


def test_historical_replay_override_rejects_expected_raw_tail_that_is_not_validated(
    monkeypatch,
) -> None:
    _patch_status_build_dependencies(monkeypatch, validated_history_date="20260727")

    with pytest.raises(ValueError, match="latest validated all-market"):
        freshness.build_status(
            historical_replay_main_price_date="20260724",
            expected_price_history_high_water_date="20260728",
        )


def test_default_status_build_keeps_original_main_price_date_priority(monkeypatch) -> None:
    _patch_status_build_dependencies(monkeypatch, validated_history_date="20260728")
    monkeypatch.setattr(
        freshness,
        "validate_historical_replay_freshness_prerequisites",
        lambda target_date, expected_high_water: pytest.fail(
            "default path called historical replay prerequisite"
        ),
    )

    frame = freshness.build_status()
    row = frame.iloc[0]

    assert row["main_price_date"] == "20260728"
    assert row["main_price_date_source"] == "validated_stock_history"
    assert row["historical_replay_main_price_date"] == ""
    assert row["expected_price_history_high_water_date"] == ""
    assert row["actual_stock_price_history_date"] == "20260728"


def test_historical_replay_markdown_exposes_two_date_contract(
    tmp_path: Path,
    monkeypatch,
) -> None:
    output_md = tmp_path / "data_freshness_latest.md"
    monkeypatch.setattr(freshness, "OUTPUT_MD", output_md)
    frame = pd.DataFrame(
        [
            {
                "main_price_date": "20260724",
                "main_price_date_source": "historical_replay_override",
                "historical_replay_main_price_date": "20260724",
                "expected_price_history_high_water_date": "20260728",
                "actual_stock_price_history_date": "20260728",
                "report_ready": False,
                "daily_pdf_ready": False,
            }
        ]
    )

    freshness.write_markdown(frame)
    markdown = output_md.read_text(encoding="utf-8")

    assert "- main_price_date: `20260724`" in markdown
    assert "- actual_stock_price_history_date: `20260728`" in markdown
    assert "Historical structured-source replay explicitly pins" in markdown
    assert "publish/PDF readiness must stay false" in markdown


@pytest.mark.parametrize(
    ("target", "high_water"),
    [("20260724", ""), ("", "20260728")],
)
def test_historical_replay_status_build_requires_target_and_high_water_together(
    monkeypatch,
    target: str,
    high_water: str,
) -> None:
    monkeypatch.setattr(freshness, "latest_stock_price_history_date", lambda: "20260728")

    with pytest.raises(ValueError, match="must be supplied together"):
        freshness.build_status(
            historical_replay_main_price_date=target,
            expected_price_history_high_water_date=high_water,
        )


def test_failed_historical_replay_override_does_not_replace_existing_freshness_files(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _patch_status_build_dependencies(monkeypatch, validated_history_date="20260727")
    output_csv = tmp_path / "data_freshness_latest.csv"
    output_md = tmp_path / "data_freshness_latest.md"
    output_csv.write_text("sentinel-csv", encoding="utf-8")
    output_md.write_text("sentinel-md", encoding="utf-8")
    monkeypatch.setattr(freshness, "LATEST_DIR", tmp_path)
    monkeypatch.setattr(freshness, "OUTPUT_CSV", output_csv)
    monkeypatch.setattr(freshness, "OUTPUT_MD", output_md)
    monkeypatch.setattr(
        freshness,
        "parse_args",
        lambda: SimpleNamespace(
            historical_replay_main_price_date="20260724",
            expected_price_history_high_water_date="20260728",
        ),
    )

    with pytest.raises(ValueError, match="latest validated all-market"):
        freshness.main()

    assert output_csv.read_text(encoding="utf-8") == "sentinel-csv"
    assert output_md.read_text(encoding="utf-8") == "sentinel-md"
