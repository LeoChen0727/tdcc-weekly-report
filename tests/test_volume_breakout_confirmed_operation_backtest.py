from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_confirmed_operation_backtest import (  # noqa: E402
    EVENT_COLUMNS,
    METRIC_SAMPLE_SCOPE,
    TRIGGER_MAP,
    add_operation_selection_columns,
    attach_tdcc_asof,
    find_confirmation,
    formal_operation_events,
    lifecycle_state_for_signal,
    selected_confirmation_for_signal,
    simulate_confirmed_trade,
    summarize,
)
import build_daily_volume_breakout_operation_section as daily_builder  # noqa: E402


def price_frame(stop_on_entry_day: bool = False) -> pd.DataFrame:
    rows = [
        {
            "date": "20260101",
            "stock_id": "1234",
            "stock_name": "TEST",
            "market": "TWSE",
            "open": 10.0,
            "high": 11.0,
            "low": 9.5,
            "close": 10.8,
            "ma5": 10.1,
            "ma10": 10.0,
        },
        {
            "date": "20260102",
            "stock_id": "1234",
            "stock_name": "TEST",
            "market": "TWSE",
            "open": 10.9,
            "high": 11.5,
            "low": 10.6,
            "close": 11.2,
            "ma5": 10.4,
            "ma10": 10.2,
        },
    ]
    for i in range(2, 13):
        day = i + 1
        low = 9.4 if stop_on_entry_day and i == 2 else 11.0 + i * 0.1
        rows.append(
            {
                "date": f"202601{day:02d}",
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 11.3 + i * 0.1,
                "high": 11.8 + i * 0.1,
                "low": low,
                "close": 11.5 + i * 0.1,
                "ma5": 10.8 + i * 0.1,
                "ma10": 10.6 + i * 0.1,
            }
        )
    return pd.DataFrame(rows)


def minimal_event(**overrides: str) -> dict[str, str]:
    row = {col: "" for col in EVENT_COLUMNS}
    row.update(
        {
            "model_id": "volume_range_breakout",
            "overlay_model_id": "tdcc_weekly_ranking_formula",
            "research_id": "volume_breakout_confirmed_operation",
            "signal_date": "20260601",
            "confirmation_date": "20260610",
            "confirmation_age_trading_days": "2",
            "stock_id": "1234",
            "stock_name": "TEST",
            "market": "TWSE",
            "trigger_id": "pullback_5ma_confirmed",
            "trigger_name_zh": "pullback",
            "entry_rule_id": "confirmation_next_open",
            "entry_date": "20260611",
            "entry_price": "100",
            "entry_price_source": "confirmation_next_open",
            "stop_loss_rule_id": "signal_low_stop",
            "stop_loss_level": "90",
            "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
            "exit_date": "20260624",
            "exit_price": "110",
            "exit_reason": "fixed_10d_close",
            "holding_days": "10",
            "return_pct": "10",
            "mfe_pct": "12",
            "mae_pct": "-2",
            "out_of_sample": "True",
            "classification_id": "standard_breakout",
            "classification_name_zh": "standard",
            "attack_method": "volume_attack",
            "attack_method_name_zh": "volume",
            "price_position_type": "low_position",
            "price_position_name_zh": "low",
            "tdcc_list_type": "no_tdcc",
            "approved_for_daily": "False",
        }
    )
    row.update(overrides)
    return row


def test_next_day_confirmation_enters_on_confirmation_next_open() -> None:
    price = price_frame()
    spec = TRIGGER_MAP["next_day_continuation_confirmed"]

    confirmation = find_confirmation(price, 0, spec)
    trade = simulate_confirmed_trade(price, 0, confirmation["confirmation_idx"])

    assert confirmation["confirmation_idx"] == 1
    assert trade["entry_date"] == "20260103"
    assert trade["entry_price_source"] == "confirmation_next_open"
    assert trade["exit_reason"] == "fixed_10d_close"


def test_signal_low_stop_is_explicit_exit_rule() -> None:
    price = price_frame(stop_on_entry_day=True)

    trade = simulate_confirmed_trade(price, 0, 1)

    assert trade["exit_date"] == "20260103"
    assert trade["exit_reason"] == "stop_signal_low"
    assert trade["exit_price"] == 9.5


def test_backtest_and_daily_selected_trigger_priority_match_same_day_tie() -> None:
    price = pd.DataFrame(
        [
            {"date": "20260101", "open": 10, "high": 11, "low": 9, "close": 10, "ma5": 10, "ma10": 10},
            {"date": "20260102", "open": 10.3, "high": 11.4, "low": 10.0, "close": 11.2, "ma5": 10.2, "ma10": 10.3},
        ]
    )

    backtest_selected = selected_confirmation_for_signal(price, 0, 1)
    daily_selected = daily_builder.selected_confirmation(price, 0, 1)

    assert backtest_selected["trigger_id"] == "next_day_continuation_confirmed"
    assert daily_selected["trigger_id"] == backtest_selected["trigger_id"]
    assert daily_selected["confirmation_date"] == backtest_selected["confirmation_date"]
    assert daily_selected["matched_trigger_ids"] == backtest_selected["matched_trigger_ids"]


def test_backtest_and_daily_select_next_day_signal_high_break() -> None:
    price = pd.DataFrame(
        [
            {"date": "20260101", "open": 10, "high": 11, "low": 9, "close": 10, "ma5": 9.5, "ma10": 9.3},
            {"date": "20260102", "open": 10.1, "high": 11.2, "low": 10.0, "close": 11.1, "ma5": 9.8, "ma10": 9.6},
        ]
    )

    backtest_selected = selected_confirmation_for_signal(price, 0, 1)
    daily_selected = daily_builder.selected_confirmation(price, 0, 1)

    assert backtest_selected["trigger_id"] == "next_day_continuation_confirmed"
    assert daily_selected["trigger_id"] == backtest_selected["trigger_id"]
    assert daily_selected["confirmation_date"] == backtest_selected["confirmation_date"]


def test_backtest_and_daily_do_not_confirm_late_pullback_after_v2_next_day_window() -> None:
    price = pd.DataFrame(
        [
            {"date": "20260101", "open": 10, "high": 11, "low": 9, "close": 10, "ma5": 10, "ma10": 10},
            {"date": "20260102", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.6, "ma5": 9.9, "ma10": 10.3},
            {"date": "20260103", "open": 10.5, "high": 11.3, "low": 10.0, "close": 11.2, "ma5": 10.2, "ma10": 10.4},
        ]
    )

    backtest_selected = selected_confirmation_for_signal(price, 0, 2)
    daily_selected = daily_builder.selected_confirmation(price, 0, 2)

    assert backtest_selected is None
    assert daily_selected is None


def test_backtest_lifecycle_marks_mature_samples_separately_from_active_state() -> None:
    price = price_frame()

    lifecycle = lifecycle_state_for_signal(price, 0, len(price) - 1)

    assert lifecycle["operation_lifecycle_state"] == "expired"
    assert lifecycle["sample_maturity_status"] == "mature"
    assert lifecycle["mature_sample_eligible"] is True


def test_tdcc_asof_uses_confirmation_date_not_future_weekly_signal() -> None:
    events = pd.DataFrame([minimal_event()])
    tdcc = pd.DataFrame(
        [
            {
                "model_id": "tdcc_weekly_ranking_formula",
                "signal_date": "20260605",
                "stock_id": "1234",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "8",
                "tdcc_ranking_score": "20",
            },
            {
                "model_id": "tdcc_weekly_ranking_formula",
                "signal_date": "20260612",
                "stock_id": "1234",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "1",
                "tdcc_ranking_score": "99",
            },
        ]
    )

    out = attach_tdcc_asof(events, tdcc, "confirmation_date")
    weekly = out[out["tdcc_list_type"].eq("weekly_increase")]

    assert len(weekly) == 1
    assert weekly.iloc[0]["tdcc_signal_date"] == "20260605"
    assert int(weekly.iloc[0]["tdcc_signal_age_days"]) == 5
    assert weekly.iloc[0]["tdcc_rank"] == "8"


def test_summary_keeps_research_only_and_operation_rules() -> None:
    events = pd.DataFrame(
        [
            minimal_event(tdcc_list_type="no_tdcc", return_pct="10", out_of_sample="True"),
            minimal_event(tdcc_list_type="no_tdcc", signal_date="20260602", confirmation_date="20260611", stock_id="5678", return_pct="-3", out_of_sample="False"),
        ]
    )

    summary = summarize(events)

    assert not summary.empty
    assert set(summary["approved_for_daily"].astype(str).str.lower()) == {"false"}
    assert set(summary["entry_rule_id"]) == {"confirmation_next_open"}
    assert set(summary["metric_sample_scope"]) == {METRIC_SAMPLE_SCOPE}
    assert "operation_trigger" in set(summary["confluence_scope"])


def test_formal_operation_selects_earliest_confirmation_then_priority() -> None:
    events = pd.DataFrame(
        [
            minimal_event(
                signal_date="20260601",
                confirmation_date="20260603",
                confirmation_age_trading_days="2",
                trigger_id="pullback_5ma_confirmed",
            ),
            minimal_event(
                signal_date="20260601",
                confirmation_date="20260602",
                confirmation_age_trading_days="1",
                trigger_id="next_day_continuation_confirmed",
            ),
            minimal_event(
                signal_date="20260601",
                confirmation_date="20260603",
                confirmation_age_trading_days="2",
                trigger_id="pullback_10ma_confirmed",
            ),
        ]
    )

    selected = formal_operation_events(add_operation_selection_columns(events))

    assert selected["trigger_id"].tolist() == ["next_day_continuation_confirmed"]
    assert selected.iloc[0]["matched_trigger_ids"] == (
        "next_day_continuation_confirmed|pullback_5ma_confirmed|pullback_10ma_confirmed"
    )
    assert selected.iloc[0]["selected_trigger_id"] == "next_day_continuation_confirmed"
    assert selected.iloc[0]["operation_selection_status"] == "selected_formal_operation"


def test_formal_operation_uses_priority_when_confirmation_date_ties() -> None:
    events = pd.DataFrame(
        [
            minimal_event(
                signal_date="20260601",
                confirmation_date="20260603",
                confirmation_age_trading_days="2",
                trigger_id="pullback_10ma_confirmed",
            ),
            minimal_event(
                signal_date="20260601",
                confirmation_date="20260603",
                confirmation_age_trading_days="2",
                trigger_id="pullback_5ma_confirmed",
            ),
        ]
    )

    selected = formal_operation_events(add_operation_selection_columns(events))

    assert selected["trigger_id"].tolist() == ["pullback_5ma_confirmed"]
    assert selected.iloc[0]["selected_trigger_priority"] == "1"
