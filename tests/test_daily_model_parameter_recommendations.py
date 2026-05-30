from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_model_parameter_recommendations import build_recommendations  # noqa: E402


def base_row(**kwargs: object) -> dict[str, object]:
    row = {
        "model_id": "tdcc_short_term_continuation_d5_d10",
        "model_name_zh": "TDCC short-term continuation",
        "parameter_set_id": "strict",
        "parameter_summary": "test",
        "pdf_visibility": "pdf_core_model",
        "entry_basis": "signal_date_next_open",
        "selected_stock_days": 120,
        "selected_unique_stocks": 80,
        "best_close_horizon_d1_d10": "D+10",
        "best_close_win_rate_pct": 75.0,
        "best_avg_close_return_pct": 12.0,
        "sample_status": "ok_first_pass",
    }
    row.update(kwargs)
    return row


def detail_row(**kwargs: object) -> dict[str, object]:
    row = {
        "model_id": "tdcc_short_term_continuation_d5_d10",
        "model_name_zh": "TDCC short-term continuation",
        "parameter_set_id": "strict",
        "horizon": "D+10",
        "entry_basis": "signal_date_next_open",
        "avg_high_return_pct": 15.0,
        "high_5pct_hit_rate_pct": 70.0,
        "avg_close_return_pct": 12.0,
        "close_win_rate_pct": 75.0,
    }
    row.update(kwargs)
    return row


def test_promote_strong_close_hold_edge() -> None:
    out = build_recommendations(pd.DataFrame([base_row()]), pd.DataFrame([detail_row()]))
    assert out.iloc[0]["recommended_usage"] == "promote_to_pdf_core"
    assert out.iloc[0]["recommended_close_exit_horizon"] == "D+10"


def test_research_only_visibility_stays_research_only() -> None:
    out = build_recommendations(
        pd.DataFrame([base_row(pdf_visibility="research_only_not_pdf_core")]),
        pd.DataFrame([detail_row()]),
    )
    assert out.iloc[0]["recommended_usage"] == "research_only"
    assert out.iloc[0]["recommendation_reason_code"] == "explicit_research_model"


def test_high_return_without_close_edge_is_intraday_watch() -> None:
    out = build_recommendations(
        pd.DataFrame(
            [
                base_row(
                    model_id="volume_range_breakout",
                    parameter_set_id="w20_vol1.5_width18",
                    best_close_win_rate_pct=41.0,
                    best_avg_close_return_pct=0.5,
                )
            ]
        ),
        pd.DataFrame(
            [
                detail_row(
                    model_id="volume_range_breakout",
                    parameter_set_id="w20_vol1.5_width18",
                    avg_high_return_pct=10.0,
                    high_5pct_hit_rate_pct=50.0,
                )
            ]
        ),
    )
    assert out.iloc[0]["recommended_usage"] == "intraday_target_watch"


def test_small_sample_is_not_promoted() -> None:
    out = build_recommendations(
        pd.DataFrame([base_row(selected_stock_days=20, sample_status="insufficient_sample")]),
        pd.DataFrame([detail_row()]),
    )
    assert out.iloc[0]["recommended_usage"] == "research_only"
    assert out.iloc[0]["recommendation_reason_code"] == "insufficient_sample"
