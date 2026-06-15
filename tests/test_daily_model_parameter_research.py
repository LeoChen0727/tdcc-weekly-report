from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_candidate_model_layer import build_parameter_table, build_specs  # noqa: E402
from build_daily_model_parameter_research import build_model_parity, rule_specs, sample_status  # noqa: E402
from validate_daily_model_research_parity import validate_rule_specs  # noqa: E402


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


def test_pdf_core_research_models_exist_in_current_daily_model_layer() -> None:
    current = build_parameter_table(build_specs())
    current_core = set(current[current["pdf_visibility"].eq("pdf_core_model")]["model_id"])
    research_core = {spec.model_id for spec in rule_specs() if spec.pdf_visibility == "pdf_core_model"}

    assert not sorted(research_core - current_core)


def test_every_daily_core_model_has_research_production_baseline() -> None:
    current = build_parameter_table(build_specs())
    current_core = set(current[current["pdf_visibility"].eq("pdf_core_model")]["model_id"])
    baselines = {spec.model_id for spec in rule_specs() if spec.parameter_role == "production_baseline"}

    assert current_core <= baselines


def test_research_baselines_are_labeled_as_parity_or_proxy() -> None:
    baselines = [spec for spec in rule_specs() if spec.parameter_role == "production_baseline"]

    assert baselines
    assert {spec.production_parity_status for spec in baselines} <= {
        "production_parity",
        "production_proxy",
        "proxy_only",
    }
    assert any(spec.production_parity_status == "production_parity" for spec in baselines)
    assert all(spec.variant_of == "production_current" for spec in baselines)
    assert all(
        spec.parity_blocker
        for spec in baselines
        if spec.production_parity_status in {"production_proxy", "proxy_only"}
    )


def test_model_parity_artifact_marks_proxy_blockers() -> None:
    summaries = pd.DataFrame(
        [
            {
                "model_id": spec.model_id,
                "parameter_set_id": spec.parameter_set_id,
                "parameter_role": spec.parameter_role,
                "production_parity_status": spec.production_parity_status,
                "parity_blocker": spec.parity_blocker,
                "selected_stock_days": 1,
                "selected_unique_stocks": 1,
            }
            for spec in rule_specs()
        ]
    )

    parity = build_model_parity(summaries)

    assert not parity.empty
    assert not parity["research_baseline_parameter_set_id"].eq("").any()
    assert set(parity["research_baseline_status"]) <= {"production_parity", "production_proxy", "proxy_only"}
    proxy_rows = parity[parity["research_baseline_status"].isin(["production_proxy", "proxy_only"])]
    assert not proxy_rows.empty
    assert not proxy_rows["parity_blocker"].eq("").any()


def test_daily_model_research_parity_validator_rule_specs_pass() -> None:
    assert validate_rule_specs() == []


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


def test_volume_range_breakout_has_locked_limit_up_parameter_set() -> None:
    spec = next(
        s for s in rule_specs()
        if s.model_id == "volume_range_breakout" and s.parameter_set_id == "locked_limit_up_breakout_no_volume_gate"
    )
    df = pd.DataFrame({"locked_limit_up_breakout": [True, False]})

    assert spec.condition(df).tolist() == [True, False]
    assert "鎖量漲停" in spec.parameter_summary
    assert "不要求量比或20日均量" in spec.parameter_summary


def test_parameter_research_no_longer_references_decision_layer() -> None:
    text = (ROOT / "scripts" / "build_daily_model_parameter_research.py").read_text(encoding="utf-8")

    assert "決策層" not in text
    assert "decision_layer" not in text
    assert "trade_decision" not in text


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
