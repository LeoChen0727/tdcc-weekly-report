from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_model_parameter_research import rule_specs, sample_status  # noqa: E402


def test_sample_status_thresholds() -> None:
    assert sample_status(129) == "ok_first_pass"
    assert sample_status(30) == "small_sample_review_only"
    assert sample_status(29) == "insufficient_sample"


def test_required_model_families_exist() -> None:
    model_ids = {spec.model_id for spec in rule_specs()}
    assert "volume_range_breakout" in model_ids
    assert "price_pullback_23ema" in model_ids
    assert "hot_theme_pullback" in model_ids
    assert "revenue_unreacted_range" in model_ids
    assert "tdcc_short_term_continuation_d5_d10" in model_ids
    assert "explosive_volume_red_candle" in model_ids
    assert "revenue_unreacted_range_proxy" not in model_ids


def test_research_only_rule_not_pdf_core() -> None:
    explosive = [spec for spec in rule_specs() if spec.model_id == "explosive_volume_red_candle"]
    assert explosive
    assert {spec.pdf_visibility for spec in explosive} == {"research_only_not_pdf_core"}


def test_volume_range_breakout_does_not_veto_large_prior_gain() -> None:
    spec = next(
        s for s in rule_specs()
        if s.model_id == "volume_range_breakout" and s.parameter_set_id == "prior20x1.02_vol2_minvol1000"
    )
    df = pd.DataFrame(
        {
            "volume_ratio_prev20": [2.0],
            "range_breakout_20d_pct": [2.5],
            "volume_ma20_lots": [1200.0],
            "bullish_attack_candle": [True],
            "return_5d_pct": [55.0],
            "return_10d_pct": [80.0],
        }
    )
    assert bool(spec.condition(df).iloc[0])


def test_price_pullback_does_not_require_breakout() -> None:
    spec = next(
        s for s in rule_specs()
        if s.model_id == "price_pullback_23ema" and s.parameter_set_id == "ema-2.5_5_volmax1.2"
    )
    df = pd.DataFrame(
        {
            "distance_ema23_pct": [1.0],
            "ema23_slope_5d_pct": [1.5],
            "volume_ratio_prev20": [0.8],
            "range_breakout_20d_pct": [-3.0],
        }
    )
    assert bool(spec.condition(df).iloc[0])


def test_hot_theme_pullback_uses_strict_historical_theme_gate() -> None:
    spec = next(
        s for s in rule_specs()
        if s.model_id == "hot_theme_pullback"
        and s.parameter_set_id == "strict_mainstream_supported_ema-2.5_5_support8"
    )
    df = pd.DataFrame(
        {
            "strict_theme_status_group": ["mainstream_supported", "unlabeled"],
            "latest_theme_status_group": ["unlabeled", "mainstream_supported"],
            "distance_ema23_pct": [1.0, 1.0],
            "range_low_20d_prev": [100.0, 100.0],
            "close": [101.0, 101.0],
        }
    )
    result = spec.condition(df).tolist()
    assert result == [True, False]
