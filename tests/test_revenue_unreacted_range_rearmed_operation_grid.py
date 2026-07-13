from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_rearmed_operation_grid import (  # noqa: E402
    NO_STOP_POLICY_ID,
    PRIMARY_ANALYSIS_BASIS,
    SENSITIVITY_ANALYSIS_BASIS,
    STOP_POLICY_ID,
    STOP_RULE_ID,
    _overlap_pair_count,
    build_operation_detail,
    build_operation_return_review,
    build_operation_summary,
)
from revenue_unreacted_range_source_first_condition_audit import (  # noqa: E402
    PRICE_HISTORY_DIR,
    _load_price_resolutions,
    load_stock_price,
)
from validate_revenue_unreacted_range_rearmed_operation_grid import (  # noqa: E402
    validate,
)


def _stock_frame(
    stock_id: str,
    *,
    triggers: tuple[int, ...],
    next_closes: dict[int, float] | None = None,
    length: int = 140,
) -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-02", periods=length).strftime("%Y%m%d")
    close = np.full(length, 100.0)
    cross = np.zeros(length, dtype=bool)
    next_closes = next_closes or {}
    for trigger in triggers:
        close[trigger] = 110.0
        close[trigger + 1] = next_closes.get(trigger, 111.0)
        cross[trigger] = True
    return pd.DataFrame(
        {
            "stock_id": stock_id,
            "date": dates,
            "open": close,
            "high": close,
            "low": close,
            "close": close,
            "analysis_open": close + 0.25,
            "analysis_close": close,
            "ma60": 105.0,
            "ma120": 100.0,
            "cross_breakout_prev20": cross,
            "price_resolution_ids_on_date": "",
        }
    )


def _source_row(
    stock: pd.DataFrame,
    stock_id: str,
    *,
    first_trigger: int,
    start: int = 30,
    end: int = 100,
    source_anomaly: bool = False,
) -> dict[str, object]:
    return {
        "condition_variant_id": "absolute_or_two_month_yoy_ge15",
        "episode_key": f"episode-{stock_id}",
        "stock_id": stock_id,
        "stock_name": stock_id,
        "episode_start_trade_date": stock.at[start, "date"],
        "episode_start_source_date": stock.at[start, "date"],
        "episode_end_date": stock.at[end, "date"],
        "episode_status": "launch_within_active_horizon",
        "first_breakout_date": stock.at[first_trigger, "date"],
        "first_breakout_outcome": "strict_success",
        "launch_date": stock.at[first_trigger, "date"],
        "qualifying_source_revenue_anomaly_candidate_flag": source_anomaly,
        "unresolved_price_path_candidate_flag": False,
        "same_stock_non_overlap_applied": True,
    }


def _build_detail(
    stocks: dict[str, pd.DataFrame],
    source_rows: list[dict[str, object]],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    source = pd.DataFrame(source_rows)
    detail = build_operation_detail(source, stocks, "2026-07-13 00:00:00 Asia/Taipei")
    return detail, source


def test_base_and_delayed_confirmation_use_distinct_information_cutoffs_and_entries() -> None:
    stock = _stock_frame("4916", triggers=(40,))
    detail, _ = _build_detail(
        {"4916": stock},
        [_source_row(stock, "4916", first_trigger=40)],
    )
    common = (
        detail["lifecycle_policy_id"].eq("episode_first_match_once")
        & detail["holding_days"].eq(20)
        & detail["stop_policy_id"].eq(NO_STOP_POLICY_ID)
    )
    base = detail.loc[common & detail["confirmation_variant_id"].eq("base_close_confirmed")].iloc[0]
    delayed = detail.loc[
        common
        & detail["confirmation_variant_id"].eq("delayed_next_close_continuation_bonus")
    ].iloc[0]

    assert base["trigger_date"] == stock.at[40, "date"]
    assert base["confirmation_date"] == stock.at[40, "date"]
    assert base["entry_date"] == stock.at[41, "date"]
    assert base["bonus_timing_role"] == (
        "next_day_continuation_is_post_entry_observation_not_available_for_d1_open_buy_ranking"
    )
    assert delayed["confirmation_date"] == stock.at[41, "date"]
    assert delayed["entry_date"] == stock.at[42, "date"]
    assert delayed["entry_rule_id"] == "next_day_close_confirmed_following_trading_day_open"


def test_failed_next_close_continuation_remains_in_base_but_not_delayed_bonus() -> None:
    stock = _stock_frame("1303", triggers=(40,), next_closes={40: 109.0})
    detail, _ = _build_detail(
        {"1303": stock},
        [_source_row(stock, "1303", first_trigger=40)],
    )

    assert len(
        detail.loc[
            detail["stock_id"].eq("1303")
            & detail["confirmation_variant_id"].eq("base_close_confirmed")
        ]
    ) > 0
    assert detail.loc[
        detail["stock_id"].eq("1303")
        & detail["confirmation_variant_id"].eq("delayed_next_close_continuation_bonus")
    ].empty


def test_rearmed_lifecycle_selects_later_signal_only_after_realized_exit() -> None:
    stock = _stock_frame("4916", triggers=(40, 65))
    detail, _ = _build_detail(
        {"4916": stock},
        [_source_row(stock, "4916", first_trigger=40)],
    )
    common = (
        detail["stock_id"].eq("4916")
        & detail["confirmation_variant_id"].eq("base_close_confirmed")
        & detail["holding_days"].eq(20)
        & detail["stop_policy_id"].eq(NO_STOP_POLICY_ID)
    )
    benchmark = detail.loc[common & detail["lifecycle_policy_id"].eq("episode_first_match_once")]
    rearmed = detail.loc[
        common & detail["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
    ].sort_values("trigger_date")

    assert len(benchmark) == 1
    assert list(rearmed["trigger_date"]) == [stock.at[40, "date"], stock.at[65, "date"]]
    assert list(rearmed["episode_trade_sequence"]) == [1, 2]
    assert list(rearmed["rearmed_trade_flag"].map(bool)) == [False, True]
    assert rearmed.iloc[1]["entry_date"] > rearmed.iloc[0]["exit_date"]
    assert _overlap_pair_count(rearmed) == 0


def test_four_close_stop_exits_at_next_open_and_does_not_use_intraday_prices() -> None:
    stock = _stock_frame("9998", triggers=(40,))
    stock.loc[41:44, ["open", "high", "low", "close", "analysis_close"]] = 90.0
    stock.loc[45, ["open", "analysis_open"]] = 89.0
    detail, _ = _build_detail(
        {"9998": stock},
        [_source_row(stock, "9998", first_trigger=40)],
    )
    common = (
        detail["lifecycle_policy_id"].eq("episode_first_match_once")
        & detail["confirmation_variant_id"].eq("base_close_confirmed")
        & detail["holding_days"].eq(20)
    )
    stopped = detail.loc[common & detail["stop_policy_id"].eq(STOP_POLICY_ID)].iloc[0]
    no_stop = detail.loc[common & detail["stop_policy_id"].eq(NO_STOP_POLICY_ID)].iloc[0]

    assert stopped["stop_confirmation_date"] == stock.at[44, "date"]
    assert stopped["exit_date"] == stock.at[45, "date"]
    assert float(stopped["exit_price"]) == 89.0
    assert stopped["exit_price_basis"] == "next_trading_day_open_after_stop_close_confirmation"
    assert stopped["exit_reason"] == STOP_RULE_ID
    assert int(stopped["stop_confirmed_days"]) == 4
    assert no_stop["exit_date"] == stock.at[60, "date"]
    assert no_stop["exit_price_basis"] == "fixed_future_close"


def test_return_review_is_a_trigger_not_an_anomaly_disposition_and_sensitivity_excludes_it() -> None:
    stock = _stock_frame("9999", triggers=(40,))
    stock.loc[50:, ["open", "high", "low", "close", "analysis_open", "analysis_close"]] = 220.0
    detail, source = _build_detail(
        {"9999": stock},
        [_source_row(stock, "9999", first_trigger=40)],
    )
    review = build_operation_return_review(detail, {"9999": stock})
    summary = build_operation_summary(detail, source)

    assert not review.empty
    assert pd.to_numeric(review["realized_return_pct"], errors="coerce").abs().ge(80.0).all()
    assert set(review["review_disposition"]) == {
        "unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly"
    }
    grid = (
        summary["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
        & summary["confirmation_variant_id"].eq("base_close_confirmed")
        & summary["holding_days"].eq(10)
        & summary["stop_policy_id"].eq(NO_STOP_POLICY_ID)
    )
    primary = summary.loc[grid & summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)].iloc[0]
    sensitivity = summary.loc[grid & summary["analysis_basis"].eq(SENSITIVITY_ANALYSIS_BASIS)].iloc[0]
    assert int(primary["mature_operation_count"]) > int(sensitivity["mature_operation_count"])
    assert int(primary["operation_return_review_candidate_count"]) > 0


def test_all_grid_rows_are_research_only_and_all_summary_grids_are_nonoverlapping() -> None:
    stock = _stock_frame("4916", triggers=(40, 65))
    detail, source = _build_detail(
        {"4916": stock},
        [_source_row(stock, "4916", first_trigger=40)],
    )
    summary = build_operation_summary(detail, source)

    assert not detail["approved_for_daily"].map(bool).any()
    assert not detail["production_change"].map(bool).any()
    assert len(summary) == 64
    assert pd.to_numeric(summary["same_stock_overlap_pair_count"], errors="coerce").eq(0).all()
    assert set(summary["financial_statement_scope"]) == {
        "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
        "non_operating_income_net_income_excluded"
    }


def test_2380_capital_reduction_is_replayed_on_a_comparable_price_scale() -> None:
    stock = load_stock_price(
        "2380",
        PRICE_HISTORY_DIR / "2380.csv",
        _load_price_resolutions(),
    )
    before = stock.loc[stock["date"].eq("20260616")].iloc[0]
    resumed = stock.loc[stock["date"].eq("20260629")].iloc[0]

    assert float(before["raw_close"]) == 6.6
    assert abs(float(before["analysis_close"]) - 23.8627) < 0.0001
    assert float(resumed["raw_close"]) == 21.5
    assert float(resumed["analysis_close"]) == 21.5
    assert abs(float(resumed["analysis_close"]) / float(before["analysis_close"]) - 1.0) < 0.20
    assert resumed["price_resolution_ids_on_date"] == (
        "2380_20260629_loss_offset_capital_reduction"
    )


def test_generated_rearmed_operation_grid_passes() -> None:
    assert validate() == []
