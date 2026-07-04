from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_monthly_revenue_history import (  # noqa: E402
    SOURCE_FIELD_ORDER,
    merge_history,
    parse_roc_or_yyyymm,
    parse_roc_or_yyyymmdd,
    standardize_source,
)
from validate_monthly_revenue_history import validate_history  # noqa: E402


def source_row(
    *,
    stock_id: str = "2330",
    stock_name: str = "TSMC",
    industry: str = "semiconductor",
    latest_revenue_yoy_pct: str = "28.0",
    cumulative_revenue_yoy_pct: str = "25.0",
    monthly_revenue: str = "320000000",
    month_over_month_pct: str = "6.7",
    note: str = "",
) -> dict[str, str]:
    return {
        "source_table_date": "1150617",
        "revenue_period": "11505",
        "stock_id": stock_id,
        "stock_name": stock_name,
        "industry": industry,
        "monthly_revenue": monthly_revenue,
        "previous_month_revenue": "300000000",
        "last_year_month_revenue": "250000000",
        "month_over_month_pct": month_over_month_pct,
        "latest_revenue_yoy_pct": latest_revenue_yoy_pct,
        "cumulative_revenue": "1500000000",
        "last_year_cumulative_revenue": "1200000000",
        "cumulative_revenue_yoy_pct": cumulative_revenue_yoy_pct,
        "note": note,
    }


def standardize(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    return standardize_source(
        raw,
        market="listed",
        source_market_name="TWSE",
        source_url="https://example.test/monthly.csv",
        fetch_date="20260704",
        fetch_timestamp="2026-07-04 12:00:00 Asia/Taipei",
    )


def test_monthly_revenue_history_parses_roc_period_and_source_table_date() -> None:
    assert parse_roc_or_yyyymm("11505") == ("202605", "11505")
    assert parse_roc_or_yyyymm("202605") == ("202605", "202605")
    assert parse_roc_or_yyyymmdd("1150617") == ("20260617", "1150617")
    assert parse_roc_or_yyyymmdd("20260617") == ("20260617", "20260617")


def test_monthly_revenue_history_standardizes_full_market_source_rows() -> None:
    raw = pd.DataFrame(
        [
            source_row(),
            source_row(
                stock_id="9946",
                stock_name="sample anomaly",
                latest_revenue_yoy_pct="312.1",
                cumulative_revenue_yoy_pct="4900",
                monthly_revenue="10",
                month_over_month_pct="900",
                note="test anomaly",
            ),
        ]
    )

    out, status = standardize(raw)

    assert status["status"] == "ok"
    assert status["selected_column_mode"] == "standard_alias"
    assert status["selected_column_indexes"]["stock_id"] == 2
    assert status["raw_rows"] == 2
    assert status["standardized_rows"] == 2
    assert validate_history(out.astype(str), require_source_files=False, require_all_markets=False) == []
    tsmc = out[out["stock_id"].eq("2330")].iloc[0]
    assert tsmc["revenue_period"] == "202605"
    assert tsmc["source_table_date"] == "20260617"
    assert tsmc["research_join_allowed"] == "True"
    assert tsmc["allowed_for_formal_historical_model_use"] == "False"
    anomaly = out[out["stock_id"].eq("9946")].iloc[0]
    assert anomaly["revenue_numerical_anomaly_flag"] == "True"
    assert "latest_revenue_yoy_abs_ge_300pct" in anomaly["revenue_numerical_anomaly_reason"]
    assert "cumulative_revenue_yoy_abs_ge_500pct" in anomaly["revenue_numerical_anomaly_reason"]


def test_monthly_revenue_history_supports_official_position_fallback() -> None:
    raw_values = source_row()
    raw = pd.DataFrame(
        [[raw_values[key] for key in SOURCE_FIELD_ORDER]],
        columns=[f"official_col_{index}" for index in range(len(SOURCE_FIELD_ORDER))],
    )

    out, status = standardize(raw)

    assert status["status"] == "ok"
    assert status["selected_column_mode"] == "official_position_fallback"
    assert status["selected_column_indexes"]["latest_revenue_yoy_pct"] == 9
    assert out.iloc[0]["stock_id"] == "2330"
    assert out.iloc[0]["stock_name"] == "TSMC"
    assert out.iloc[0]["latest_revenue_yoy_pct"] == "28"


def test_monthly_revenue_history_merge_preserves_old_periods(tmp_path: Path) -> None:
    old = pd.DataFrame(
        [
            {
                "generated_at": "old",
                "history_id": "monthly_revenue_history",
                "history_version": "official_mops_monthly_revenue_v1",
                "source_kind": "official_mops_current_monthly_revenue_openapi",
                "market": "listed",
                "source_market_name": "TWSE",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "industry": "semiconductor",
                "revenue_period": "202604",
                "revenue_period_roc": "11504",
                "source_table_date": "20260517",
                "source_table_date_raw": "1150517",
                "fetch_date": "20260518",
                "fetch_timestamp": "2026-05-18 12:00:00 Asia/Taipei",
                "source_url": "old",
                "source_file": "data/monthly_revenue_history/raw/old.csv",
                "monthly_revenue": "1",
                "previous_month_revenue": "1",
                "last_year_month_revenue": "1",
                "month_over_month_pct": "0",
                "latest_revenue_yoy_pct": "10",
                "cumulative_revenue": "1",
                "last_year_cumulative_revenue": "1",
                "cumulative_revenue_yoy_pct": "10",
                "note": "",
                "revenue_positive_flag": "True",
                "revenue_strong_flag": "True",
                "revenue_numerical_anomaly_flag": "False",
                "revenue_numerical_anomaly_reason": "",
                "point_in_time_status": "ready_official_source_table_date",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
                "formal_use_blocker": "blocked_until_sufficient_history_coverage_and_model_promotion",
                "coverage_note": "old",
            }
        ]
    )
    path = tmp_path / "history.csv"
    old.to_csv(path, index=False, encoding="utf-8")
    current = old.copy()
    current.loc[0, "revenue_period"] = "202605"
    current.loc[0, "revenue_period_roc"] = "11505"
    current.loc[0, "source_table_date"] = "20260617"

    merged = merge_history(current, path)

    assert list(merged["revenue_period"]) == ["202604", "202605"]


def test_monthly_revenue_validator_rejects_formal_use_claim() -> None:
    raw = pd.DataFrame([source_row()])
    out, _ = standardize(raw)
    out.loc[0, "allowed_for_formal_historical_model_use"] = "True"

    errors = validate_history(out.astype(str), require_source_files=False, require_all_markets=False)

    assert any("must not claim formal model-use approval" in error for error in errors)
