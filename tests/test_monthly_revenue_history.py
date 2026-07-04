from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_monthly_revenue_history import (  # noqa: E402
    FALLBACK_SOURCE_STATUS,
    SOURCE_FIELD_ORDER,
    load_recent_history_fallback,
    merge_history,
    official_current_sources_ready,
    parse_roc_or_yyyymm,
    parse_roc_or_yyyymmdd,
    standardize_source,
)
from backfill_monthly_revenue_history_from_mops_html import (  # noqa: E402
    conservative_source_table_date,
    parse_static_html,
)
from validate_monthly_revenue_history import validate_history, validate_source_status_rows  # noqa: E402


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


def standardized_market(raw: pd.DataFrame, market: str, source_market_name: str) -> pd.DataFrame:
    out, status = standardize_source(
        raw,
        market=market,
        source_market_name=source_market_name,
        source_url=f"https://example.test/{market}.csv",
        fetch_date="20260704",
        fetch_timestamp="2026-07-04 12:00:00 Asia/Taipei",
    )
    assert status["status"] == "ok"
    return out


def full_market_history() -> pd.DataFrame:
    listed = standardized_market(pd.DataFrame([source_row(stock_id="2330")]), "listed", "TWSE")
    otc = standardized_market(pd.DataFrame([source_row(stock_id="6547")]), "otc", "TPEX")
    return pd.concat([listed, otc], ignore_index=True)


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


def test_monthly_revenue_history_reuses_recent_validated_history_when_official_sources_empty(tmp_path: Path) -> None:
    history = full_market_history()
    history_path = tmp_path / "monthly_revenue_history.csv"
    history.to_csv(history_path, index=False, encoding="utf-8")
    statuses = [
        {
            "market": "listed",
            "source_market_name": "TWSE",
            "source_url": "https://example.test/listed.csv",
            "raw_rows": 0,
            "standardized_rows": 0,
            "status": "empty_source",
        },
        {
            "market": "otc",
            "source_market_name": "TPEX",
            "source_url": "https://example.test/otc.csv",
            "raw_rows": 0,
            "standardized_rows": 0,
            "status": "fetch_failed:temporary 503",
        },
    ]

    fallback_history, fallback_current, fallback_statuses = load_recent_history_fallback(
        statuses,
        history_path=history_path,
        fetch_date="20260705",
        max_age_days=45,
    )

    assert len(fallback_history) == 2
    assert len(fallback_current) == 2
    fallback = [row for row in fallback_statuses if row["status"] == FALLBACK_SOURCE_STATUS][0]
    assert fallback["fallback_max_source_table_date"] == "20260617"
    assert fallback["fallback_age_days"] == 18
    assert official_current_sources_ready(fallback_current, statuses) is False
    assert validate_source_status_rows(fallback_statuses) == []


def test_monthly_revenue_history_rejects_stale_fallback_cache(tmp_path: Path) -> None:
    history = full_market_history()
    history_path = tmp_path / "monthly_revenue_history.csv"
    history.to_csv(history_path, index=False, encoding="utf-8")
    statuses = [
        {
            "market": "listed",
            "source_market_name": "TWSE",
            "source_url": "https://example.test/listed.csv",
            "raw_rows": 0,
            "standardized_rows": 0,
            "status": "empty_source",
        },
        {
            "market": "otc",
            "source_market_name": "TPEX",
            "source_url": "https://example.test/otc.csv",
            "raw_rows": 0,
            "standardized_rows": 0,
            "status": "empty_source",
        },
    ]

    try:
        load_recent_history_fallback(statuses, history_path=history_path, fetch_date="20260820", max_age_days=45)
    except RuntimeError as exc:
        assert "cached history is stale" in str(exc)
    else:
        raise AssertionError("stale monthly revenue fallback cache should fail closed")


def test_monthly_revenue_source_status_rejects_stale_fallback_status() -> None:
    statuses = [
        {
            "market": "listed",
            "source_market_name": "TWSE",
            "source_url": "https://example.test/listed.csv",
            "raw_rows": 0,
            "standardized_rows": 0,
            "status": "empty_source",
        },
        {
            "market": "otc",
            "source_market_name": "TPEX",
            "source_url": "https://example.test/otc.csv",
            "raw_rows": 0,
            "standardized_rows": 0,
            "status": "empty_source",
        },
        {
            "market": "all",
            "source_market_name": "validated_history_cache",
            "source_url": "data/monthly_revenue_history/monthly_revenue_history.csv",
            "raw_rows": 2,
            "standardized_rows": 2,
            "status": FALLBACK_SOURCE_STATUS,
            "fallback_max_source_table_date": "20260617",
            "fallback_age_days": 46,
            "fallback_max_age_days": 45,
        },
    ]

    errors = validate_source_status_rows(statuses)

    assert any("cached history is stale" in error for error in errors)


def test_monthly_revenue_backfill_parses_static_html_with_conservative_source_date() -> None:
    html = """
    <html><body>
    <table><tr><th>產業別：半導體業</th><th>單位：千元</th></tr></table>
    <table>
      <tr><th>公司代號</th><th>公司名稱</th><th>當月營收</th><th>上月營收</th>
      <th>去年當月營收</th><th>上月比較增減(%)</th><th>去年同月增減(%)</th>
      <th>當月累計營收</th><th>去年累計營收</th><th>前期比較增減(%)</th><th>備註</th></tr>
      <tr><td>2330</td><td>台積電</td><td>320,000,000</td><td>300,000,000</td>
      <td>250,000,000</td><td>6.7</td><td>28.0</td><td>1,500,000,000</td>
      <td>1,200,000,000</td><td>25.0</td><td>-</td></tr>
    </table>
    </body></html>
    """

    out = parse_static_html(
        html,
        period="202605",
        market="listed",
        source_file="data/monthly_revenue_history/raw/mops_html/example.html",
        source_url_text="https://example.test/t21sc03_115_5_0.html",
        fetch_date="20260704",
        fetch_timestamp="2026-07-04 12:00:00 Asia/Taipei",
    )

    assert conservative_source_table_date("202605") == "20260617"
    assert validate_history(out.astype(str), require_source_files=False, require_all_markets=False) == []
    row = out.iloc[0]
    assert row["source_kind"] == "official_mops_static_monthly_revenue_html_conservative_available_date_v1"
    assert row["source_table_date"] == "20260617"
    assert row["source_table_date_raw"] == "conservative_next_month_17th"
    assert row["industry"] == "半導體業"
    assert row["latest_revenue_yoy_pct"] == "28"


def test_monthly_revenue_validator_rejects_formal_use_claim() -> None:
    raw = pd.DataFrame([source_row()])
    out, _ = standardize(raw)
    out.loc[0, "allowed_for_formal_historical_model_use"] = "True"

    errors = validate_history(out.astype(str), require_source_files=False, require_all_markets=False)

    assert any("must not claim formal model-use approval" in error for error in errors)
