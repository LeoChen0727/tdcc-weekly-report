from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_monthly_revenue_point_in_time_panel import build_panel, parse_reported_release_date, parse_revenue_period  # noqa: E402
from validate_monthly_revenue_point_in_time_panel import validate_panel  # noqa: E402


def test_revenue_period_parser_treats_roc_year_month_as_period_not_release_date() -> None:
    assert parse_revenue_period("11505.0") == ("202605", "11505")
    assert parse_reported_release_date("11505.0") == ("", "not_actual_release_date_year_month")
    assert parse_reported_release_date("1150613") == ("20260613", "parsed_release_date")


def test_monthly_revenue_panel_builds_snapshot_observed_asof_rows(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "snapshots"
    snapshot_dir.mkdir()
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "台積電",
                "revenue_period": "11505.0",
                "revenue_release_date": "11505.0",
                "revenue_yoy_pct": "39.6",
                "cumulative_yoy_pct": "42.1",
                "revenue_good_eps_unconfirmed_flag": "True",
            },
            {
                "stock_id": "2330",
                "stock_name": "台積電",
                "revenue_period": "11505.0",
                "revenue_release_date": "11505.0",
                "revenue_yoy_pct": "39.6",
                "cumulative_yoy_pct": "42.1",
                "revenue_good_eps_unconfirmed_flag": "True",
            },
            {
                "stock_id": "9946",
                "stock_name": "三發地產",
                "revenue_period": "11505.0",
                "revenue_release_date": "1150613",
                "revenue_yoy_pct": "312.1",
                "cumulative_yoy_pct": "4373.5",
                "revenue_signal_type": "營建認列型 / 交屋認列型",
            },
        ]
    ).to_csv(snapshot_dir / "all_candidates_20260615.csv", index=False, encoding="utf-8-sig")

    panel = build_panel(snapshot_dir)

    assert validate_panel(panel.astype(str)) == []
    assert len(panel) == 2
    tsmc = panel[panel["stock_id"].eq("2330")].iloc[0]
    assert tsmc["observed_as_of_date"] == "20260615"
    assert tsmc["reported_release_date"] == ""
    assert tsmc["reported_release_date_status"] == "not_actual_release_date_year_month"
    assert tsmc["research_join_allowed"] == "True"
    assert tsmc["allowed_for_formal_historical_model_use"] == "False"
    assert tsmc["source_row_count"] == 2
    anomalous = panel[panel["stock_id"].eq("9946")].iloc[0]
    assert anomalous["revenue_numerical_anomaly_flag"] == "True"
    assert "cumulative_revenue_yoy_abs_ge_500pct" in anomalous["revenue_numerical_anomaly_reason"]


def test_monthly_revenue_validator_rejects_formal_use_claim(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "snapshots"
    snapshot_dir.mkdir()
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "台積電",
                "revenue_period": "11505",
                "revenue_yoy_pct": "39.6",
            }
        ]
    ).to_csv(snapshot_dir / "all_candidates_20260615.csv", index=False, encoding="utf-8-sig")
    panel = build_panel(snapshot_dir)
    panel.loc[0, "allowed_for_formal_historical_model_use"] = "True"

    errors = validate_panel(panel.astype(str))

    assert any("must not allow formal historical model use" in error for error in errors)
