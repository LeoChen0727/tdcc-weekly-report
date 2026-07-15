from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_financial_statement_pit import (  # noqa: E402
    HISTORY_COLUMNS,
    SourceCapture,
    assign_revision_lineage,
    build_and_write,
    build_coverage,
    load_metric_mapping,
    load_source_registry,
    normalize_capture,
)
from validate_financial_statement_pit import (  # noqa: E402
    _read_rows,
    validate,
    validate_history,
)


def payload_bytes(row: dict[str, str]) -> bytes:
    return json.dumps([row], ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def capture(
    source_id: str,
    row: dict[str, str],
    *,
    observed_at: str = "2026-07-16T10:00:00+08:00",
    source_available_at: str = "2026-07-16T10:00:00+08:00",
    availability_precision: str = "first_observed_at",
    statement_scope: str = "official_endpoint_reported_scope",
    historical_pit_eligible: bool = False,
    historical_source_fixture: bool = False,
) -> SourceCapture:
    payload = payload_bytes(row)
    source = load_source_registry()[source_id].copy()
    if historical_source_fixture:
        source.update(
            {
                "source_id": "mops_historical_fixture",
                "source_kind": "official_mops_xbrl_historical_filing",
                "source_url": "https://mops.twse.com.tw/mops/",
                "history_mode": "historical_point_in_time",
                "availability_semantics": "exact_company_filing_availability",
            }
        )
    return SourceCapture(
        source=source,
        payload=payload,
        observed_at=observed_at,
        source_available_at=source_available_at,
        availability_precision=availability_precision,
        statement_scope=statement_scope,
        period_basis="cumulative_ytd",
        raw_archive_ref=f"sha256://{hashlib.sha256(payload).hexdigest()}",
        archive_status="external_content_addressed_archive_verified",
        declared_historical_pit_eligible=historical_pit_eligible,
    )


def general_row(*, net_income: str = "150") -> dict[str, str]:
    return {
        "出表日期": "1150715",
        "年度": "115",
        "季別": "1",
        "公司代號": "2330",
        "公司名稱": "台積電",
        "營業收入": "1,000",
        "營業成本": "600",
        "營業毛利（毛損）淨額": "400",
        "營業費用": "180",
        "營業利益（損失）": "220",
        "營業外收入及支出": "20",
        "稅前淨利（淨損）": "240",
        "所得稅費用（利益）": "90",
        "本期淨利（淨損）": net_income,
        "淨利（淨損）歸屬於母公司業主": net_income,
        "基本每股盈餘（元）": "5.79",
    }


def normalize(one_capture: SourceCapture) -> tuple[pd.DataFrame, dict[str, object]]:
    aliases, required = load_metric_mapping()
    return normalize_capture(one_capture, aliases, required)


def test_general_schema_builds_objective_metrics_and_cumulative_margins() -> None:
    history, manifest = normalize(capture("twse_general", general_row()))

    assert len(history) == 1
    row = history.iloc[0]
    assert row["fiscal_period"] == "2026Q1"
    assert row["source_table_date"] == "2026-07-15"
    assert row["operating_revenue"] == "1000"
    assert row["non_operating_income_expense"] == "20"
    assert row["basic_eps"] == "5.79"
    assert row["gross_margin_pct"] == "40.0000"
    assert row["operating_margin_pct"] == "22.0000"
    assert row["net_margin_pct"] == "15.0000"
    assert row["period_basis"] == "cumulative_ytd"
    assert row["pit_status"] == "current_snapshot_first_observed_only"
    assert row["historical_pit_eligible"] == "False"
    assert row["allowed_for_formal_model_use"] == "False"
    assert row["numerical_anomaly_candidate"] == "False"
    assert row["primary_metric_retained"] == "True"
    assert manifest["availability_precision"] == "first_observed_at"
    assert manifest["normalized_row_count"] == 1
    assert manifest["dropped_invalid_identity_row_count"] == 0


def test_tpex_english_identity_fields_are_not_silently_dropped() -> None:
    row = general_row()
    row["Date"] = row.pop("出表日期")
    row["Year"] = row.pop("年度")
    row["Season"] = row.pop("季別")
    row["SecuritiesCompanyCode"] = row.pop("公司代號")
    row["CompanyName"] = row.pop("公司名稱")

    history, manifest = normalize(capture("tpex_general", row))

    assert len(history) == 1
    assert history.iloc[0]["stock_id"] == "2330"
    assert manifest["normalized_row_count"] == 1
    assert manifest["dropped_invalid_identity_row_count"] == 0


def test_banking_schema_never_inherits_general_margin_formulas() -> None:
    banking = {
        "出表日期": "1150715",
        "年度": "115",
        "季別": "1",
        "公司代號": "2882",
        "公司名稱": "國泰金",
        "淨收益": "1000",
        "營業費用": "500",
        "本期淨利（淨損）": "300",
        "基本每股盈餘（元）": "2.1",
    }
    history, _manifest = normalize(capture("twse_banking", banking))
    row = history.iloc[0]

    assert row["operating_revenue"] == "1000"
    assert row["net_income"] == "300"
    assert row["gross_margin_pct"] == ""
    assert row["operating_margin_pct"] == ""
    assert row["net_margin_pct"] == ""
    assert row["margin_derivation_status"] == "not_applicable_non_general_schema"


def test_revision_history_preserves_both_versions_and_links_lineage() -> None:
    first, _ = normalize(
        capture(
            "twse_general",
            general_row(net_income="150"),
            observed_at="2026-05-15T10:00:00+08:00",
            source_available_at="2026-05-15T10:00:00+08:00",
        )
    )
    revised, _ = normalize(
        capture(
            "twse_general",
            general_row(net_income="145"),
            observed_at="2026-06-20T10:00:00+08:00",
            source_available_at="2026-06-20T10:00:00+08:00",
        )
    )

    history = assign_revision_lineage(pd.concat([first, revised], ignore_index=True))

    assert len(history) == 2
    assert list(history["revision_number"]) == ["1", "2"]
    assert set(history["revision_count"]) == {"2"}
    assert history.iloc[1]["supersedes_revision_id"] == history.iloc[0]["revision_id"]
    assert list(history["is_latest_known_revision"]) == ["False", "True"]
    assert list(history["net_income"]) == ["150", "145"]


def test_global_table_date_change_does_not_create_false_financial_revision() -> None:
    first_row = general_row()
    second_row = general_row()
    second_row["出表日期"] = "1150716"
    first, _ = normalize(capture("twse_general", first_row))
    second, _ = normalize(
        capture(
            "twse_general",
            second_row,
            observed_at="2026-07-17T10:00:00+08:00",
            source_available_at="2026-07-17T10:00:00+08:00",
        )
    )

    history = assign_revision_lineage(pd.concat([first, second], ignore_index=True))

    assert len(history) == 1
    assert history.iloc[0]["revision_count"] == "1"


def test_current_snapshot_source_cannot_self_declare_historical_pit() -> None:
    with pytest.raises(ValueError, match="registry-owned historical source"):
        normalize(
            capture(
                "twse_general",
                general_row(),
                source_available_at="2026-05-15T14:31:22+08:00",
                availability_precision="exact_company_filing_timestamp",
                statement_scope="consolidated",
                historical_pit_eligible=True,
            )
        )


def test_registered_exact_historical_filing_remains_formal_use_blocked() -> None:
    historical, _ = normalize(
        capture(
            "twse_general",
            general_row(),
            observed_at="2026-05-16T10:00:00+08:00",
            source_available_at="2026-05-15T14:31:22+08:00",
            availability_precision="exact_company_filing_timestamp",
            statement_scope="consolidated",
            historical_pit_eligible=True,
            historical_source_fixture=True,
        )
    )
    row = historical.iloc[0]

    assert row["pit_status"] == "historical_pit_exact_company_filing_available"
    assert row["historical_pit_eligible"] == "True"
    assert row["research_asof_join_allowed"] == "True"
    assert row["allowed_for_formal_model_use"] == "False"


def test_numerical_extremes_are_unresolved_candidates_and_remain_primary() -> None:
    extreme = general_row(net_income="-107754")
    extreme["公司代號"] = "6919"
    extreme["營業收入"] = "2"
    extreme["營業成本"] = "1"
    extreme["營業毛利（毛損）淨額"] = "1"
    extreme["營業費用"] = "245832"
    extreme["營業利益（損失）"] = "-245831"
    extreme["基本每股盈餘（元）"] = "-0.07"
    history, _manifest = normalize(capture("twse_general", extreme))
    row = history.iloc[0]

    assert row["operating_margin_pct"] == "-12291550.0000"
    assert row["numerical_anomaly_candidate"] == "True"
    assert "operating_margin_abs_ge_500pct" in row["numerical_anomaly_triggers"]
    assert row["anomaly_disposition"] == "unresolved_anomaly_candidate"
    assert row["primary_metric_retained"] == "True"
    assert row["anomaly_evidence_status"].endswith("independent_corroboration_pending")


def test_validator_rejects_table_date_as_company_availability() -> None:
    history, manifest_row = normalize(capture("twse_general", general_row()))
    history = assign_revision_lineage(history)
    manifest = pd.DataFrame([manifest_row])
    history.loc[0, "availability_precision"] = "official_table_date"

    errors = validate_history(
        history.astype(str),
        manifest.astype(str),
        set(load_source_registry()),
    )

    assert any("global table date cannot become company filing availability" in error for error in errors)


def test_producer_write_allowlist_does_not_touch_mature_model_artifacts(tmp_path: Path) -> None:
    sentinel = tmp_path / "output" / "latest" / "daily_w_bottom_right_side_operation_section_latest.csv"
    sentinel.parent.mkdir(parents=True)
    sentinel.write_text("sentinel\n", encoding="utf-8")
    before = sentinel.read_bytes()

    paths = build_and_write([capture("twse_general", general_row())], tmp_path)

    assert sentinel.read_bytes() == before
    assert len(paths) == 6
    assert all(path.exists() for path in paths.values())


def test_complete_fixture_passes_independent_validator() -> None:
    history, manifest_row = normalize(capture("twse_general", general_row()))
    history = assign_revision_lineage(history)
    manifest = pd.DataFrame([manifest_row])
    coverage = build_coverage(history, manifest)
    source_rows = _read_rows(ROOT / "config" / "daily_model_financial_statement_pit_sources.csv")
    mapping_rows = _read_rows(ROOT / "config" / "daily_model_financial_statement_metric_mapping.csv")

    assert validate(
        history.astype(str),
        manifest.astype(str),
        coverage.astype(str),
        source_rows,
        mapping_rows,
    ) == []
