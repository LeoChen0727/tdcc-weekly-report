from pathlib import Path

import pandas as pd

from scripts.build_tdcc_weekly_candidate_reports import (
    TDCC_EFFECTIVE_INCREASE_THRESHOLD,
    TDCC_HIGH_PAIR_STREAK_BONUS_CAP,
    TDCC_HIGH_PAIR_STREAK_BONUS_STEP,
)
from scripts.build_tdcc_weekly_ranking_backtest import (
    MODEL_ID,
    RANKING_MODEL_VERSION,
    compute_score_columns,
    rank_weekly_models,
)


ROOT = Path(__file__).resolve().parents[1]


def test_tdcc_weekly_ranking_backtest_uses_current_formula_constants() -> None:
    assert TDCC_EFFECTIVE_INCREASE_THRESHOLD == 0.5
    assert TDCC_HIGH_PAIR_STREAK_BONUS_STEP == 5.0
    assert TDCC_HIGH_PAIR_STREAK_BONUS_CAP == 20.0


def test_compute_score_columns_matches_weekly_ranking_formula() -> None:
    df = pd.DataFrame(
        [
            {
                "signal_date": "20260612",
                "stock_id": "1234",
                "tdcc_1w_change_400": 0.6,
                "tdcc_1w_change_600": 0.7,
                "tdcc_1w_change_800": 0.8,
                "tdcc_1w_change_1000": 0.9,
                "tdcc_high_pair_effective_streak_weeks": 3,
                "theme_mainstream_status": "mainstream_latest_taxonomy",
                "volume_ma20_lots": 500,
            }
        ]
    )

    scored = compute_score_columns(df).iloc[0]

    assert scored["tdcc_effective_increase_count"] == 4
    assert scored["tdcc_weighted_weekly_increase_score"] == 8.0
    assert scored["tdcc_sync_bonus"] == 15.0
    assert scored["tdcc_theme_bonus"] == 5.0
    assert scored["tdcc_low_volume_penalty"] == 10.0
    assert scored["tdcc_high_pair_streak_bonus"] == 10.0
    assert scored["tdcc_weekly_increase_score"] == 18.0
    assert scored["tdcc_consecutive_accumulation_score"] == 28.0


def test_rank_weekly_models_uses_effective_threshold_and_high_pair_gate() -> None:
    df = pd.DataFrame(
        [
            {
                "model_id": MODEL_ID,
                "ranking_model_version": RANKING_MODEL_VERSION,
                "signal_date": "20260612",
                "stock_id": "1111",
                "stock_name": "A",
                "tdcc_1w_change_400": 0.51,
                "tdcc_1w_change_600": 0.0,
                "tdcc_1w_change_800": 0.0,
                "tdcc_1w_change_1000": 0.0,
                "tdcc_high_pair_effective_streak_weeks": 0,
                "theme_mainstream_status": "non_mainstream_latest_taxonomy",
                "volume_ma20_lots": 2000,
            },
            {
                "model_id": MODEL_ID,
                "ranking_model_version": RANKING_MODEL_VERSION,
                "signal_date": "20260612",
                "stock_id": "2222",
                "stock_name": "B",
                "tdcc_1w_change_400": 0.1,
                "tdcc_1w_change_600": 0.2,
                "tdcc_1w_change_800": 0.8,
                "tdcc_1w_change_1000": 0.9,
                "tdcc_high_pair_effective_streak_weeks": 2,
                "theme_mainstream_status": "mainstream_latest_taxonomy",
                "volume_ma20_lots": 2000,
            },
        ]
    )

    ranked = rank_weekly_models(compute_score_columns(df))

    weekly_ids = set(ranked.loc[ranked["tdcc_list_type"].eq("weekly_increase"), "stock_id"])
    consecutive_ids = set(ranked.loc[ranked["tdcc_list_type"].eq("consecutive_accumulation"), "stock_id"])

    assert weekly_ids == {"1111", "2222"}
    assert consecutive_ids == {"2222"}


def test_research_workflow_uses_tdcc_weekly_ranking_as_baseline() -> None:
    text = (ROOT / ".github/workflows/research_backtest_pipeline.yml").read_text(encoding="utf-8")

    assert "Run TDCC weekly ranking formula backtest" in text
    assert "python scripts/build_tdcc_weekly_ranking_backtest.py" in text
    assert "python scripts/validate_tdcc_weekly_ranking_backtest.py" in text
    assert "Build TDCC normalized signal performance and effectiveness" not in text
