from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_buy_signal_grid import (  # noqa: E402
    SIGNAL_UNIVERSE_ID,
    feature_groups,
    summarize_grid,
)


def event_row(**overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "model_id": "volume_range_breakout",
        "event_filter_id": "current_model_hit_all",
        "model_hit_status": "current_model_hit",
        "pattern_id": "signal_close_hold_5d",
        "event_date": "20250507",
        "stock_id": "1234",
        "stock_name": "TEST",
        "market": "listed",
        "market_regime": "range_or_mixed",
        "entry_date": "20250508",
        "entry_price": "100",
        "exit_date": "20250514",
        "exit_price": "105",
        "exit_reason": "fixed_5d_close",
        "holding_days": "5",
        "return_pct": "5",
        "mfe_pct": "8",
        "mae_pct": "-2",
        "out_of_sample": "True",
        "volume_ratio": "1.5",
        "signal_return_1d_pct": "9.8",
        "signal_low": "90",
        "signal_high": "100",
        "previous_20d_high": "92",
        "range_width_40_pct": "18",
        "low_position_60_pct": "25",
        "limit_up_like": "True",
        "source_signal_universe_id": SIGNAL_UNIVERSE_ID,
        "feature_group_scope": "all_current_model_hits",
        "feature_group_id": "all",
        "feature_group_name_zh": "全部現行放量攻擊",
    }
    row.update(overrides)
    return row


def test_feature_groups_classifies_current_signal_without_duplicate_filter_rows() -> None:
    row = pd.Series(event_row())

    groups = feature_groups(row)
    keys = {(scope, group_id) for scope, group_id, _ in groups}

    assert ("all_current_model_hits", "all") in keys
    assert ("event_filter", "current_model_hit_all") in keys
    assert ("event_filter", "long_base_low_position") in keys
    assert ("event_filter", "limit_up_like_current_hit") in keys
    assert ("price_position", "low_position") in keys
    assert ("attack_method", "locked_limit_up") in keys
    assert ("volume_ratio", "lt_2") in keys
    assert ("consolidation", "long_tight_base") in keys


def test_summarize_grid_is_research_only_and_keeps_signal_universe() -> None:
    rows = []
    for idx in range(120):
        rows.append(
            event_row(
                event_date=f"2025{(idx % 12) + 1:02d}{(idx % 20) + 1:02d}",
                stock_id=f"{1000 + idx}",
                return_pct="4" if idx % 3 else "-1",
                out_of_sample="True" if idx >= 80 else "False",
                feature_group_scope="all_current_model_hits",
                feature_group_id="all",
                feature_group_name_zh="全部現行放量攻擊",
            )
        )
    expanded = pd.DataFrame(rows)

    grid = summarize_grid(expanded)

    assert not grid.empty
    row = grid.iloc[0]
    assert row["signal_universe_id"] == SIGNAL_UNIVERSE_ID
    assert row["approved_for_daily"] == "False"
    assert row["approved_for_daily_candidate"] == "True"
    assert row["candidate_status"] == "promotion_candidate"
    assert float(row["median_return"]) > 0


def test_summarize_grid_rejects_positive_average_with_negative_median() -> None:
    rows = []
    for idx in range(120):
        rows.append(
            event_row(
                event_date=f"2025{(idx % 12) + 1:02d}{(idx % 20) + 1:02d}",
                stock_id=f"{2000 + idx}",
                return_pct="50" if idx < 10 else "-1",
                out_of_sample="True" if idx >= 80 else "False",
                feature_group_scope="all_current_model_hits",
                feature_group_id="all",
                feature_group_name_zh="全部現行放量攻擊",
            )
        )
    expanded = pd.DataFrame(rows)

    grid = summarize_grid(expanded)

    assert not grid.empty
    row = grid.iloc[0]
    assert float(row["avg_return"]) > 0
    assert float(row["median_return"]) < 0
    assert row["candidate_status"] == "not_positive_expectancy"
    assert row["approved_for_daily_candidate"] == "False"
