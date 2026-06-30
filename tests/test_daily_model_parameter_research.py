from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_candidate_model_layer import build_parameter_table, build_specs  # noqa: E402
from build_daily_model_parameter_research import (  # noqa: E402
    add_price_structure_features,
    build_price_pullback_feature_confirmation_research,
    build_model_parity,
    build_price_pullback_operation_module_research,
    build_price_pullback_operation_research,
    build_price_pullback_time_cost_backtest,
    current_price_pullback_baseline_proxy,
    price_pullback_prior_extension_filter,
    rule_specs,
    sample_status,
)
from validate_daily_model_research_parity import validate_rule_specs  # noqa: E402
from validate_research_against_stock_model_contract import build_parity_rows  # noqa: E402


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
    assert "w_bottom_right_side" in model_ids
    assert "neckline_volume_breakout_confirmation" in model_ids
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
    proxy = {spec.model_id for spec in baselines if spec.production_parity_status == "production_proxy"}
    parity = {spec.model_id for spec in baselines if spec.production_parity_status == "production_parity"}
    assert "w_bottom_right_side" in parity
    assert "neckline_volume_breakout_confirmation" in parity
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


def test_contract_parity_monitor_excludes_deprecated_registry_only_models() -> None:
    rows, _, source_errors = build_parity_rows()
    model_ids = {row["model_id"] for row in rows}

    assert source_errors == []
    assert "neckline_volume_breakout_confirmation" in model_ids
    assert "near_high_neckline_challenge" not in model_ids
    assert "platform_strengthening" not in model_ids


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


def test_price_pullback_production_proxy_replay_accepts_trend_fallbacks() -> None:
    df = pd.DataFrame(
        {
            "distance_ema23_pct": [1.0, 12.0, 12.0],
            "platform_low": [0.0, 100.0, 80.0],
            "short_platform_low": [0.0, 0.0, 0.0],
            "previous_20d_low": [0.0, 100.0, 80.0],
            "low_20": [0.0, 100.0, 80.0],
            "range_low_20d_prev": [0.0, 100.0, 80.0],
            "close": [101.0, 104.0, 120.0],
            "ema23": [100.0, 90.0, 130.0],
            "ma20": [120.0, 100.0, 140.0],
            "ema23_slope_pct": [-1.0, -2.0, -2.0],
            "ema23_slope_5d_pct": [-1.0, -2.0, -2.0],
            "ma5_turning_up_flag": [False, False, False],
            "ma10_turning_up_flag": [False, False, False],
        }
    )

    assert current_price_pullback_baseline_proxy(df).tolist() == [True, True, False]


def test_price_pullback_has_research_only_volume_red_k_entry_variants() -> None:
    variants = {
        spec.parameter_set_id: spec
        for spec in rule_specs()
        if spec.model_id == "price_pullback_23ema" and "red_k" in spec.parameter_set_id
    }

    assert set(variants) == {
        "volume_red_k_vol1.2",
        "solid_volume_red_k_vol1.2",
        "solid_volume_red_k_vol1.5",
    }
    assert {spec.pdf_visibility for spec in variants.values()} == {"research_only_not_pdf_core"}

    df = pd.DataFrame(
        {
            "distance_ema23_pct": [1.0, 1.0],
            "platform_low": [0.0, 0.0],
            "short_platform_low": [0.0, 0.0],
            "previous_20d_low": [0.0, 0.0],
            "low_20": [0.0, 0.0],
            "range_low_20d_prev": [0.0, 0.0],
            "close": [101.0, 101.0],
            "ema23": [100.0, 100.0],
            "ma20": [100.0, 100.0],
            "ema23_slope_pct": [-1.0, -1.0],
            "ema23_slope_5d_pct": [-1.0, -1.0],
            "ma5_turning_up_flag": [False, False],
            "ma10_turning_up_flag": [False, False],
            "volume_ratio_prev20": [1.3, 1.6],
            "bullish_attack_candle": [True, True],
            "solid_red_candle": [False, True],
        }
    )

    assert variants["volume_red_k_vol1.2"].condition(df).tolist() == [True, True]
    assert variants["solid_volume_red_k_vol1.2"].condition(df).tolist() == [False, True]
    assert variants["solid_volume_red_k_vol1.5"].condition(df).tolist() == [False, True]


def test_price_pullback_prior_extension_filter_requires_extension_runup_and_pullback() -> None:
    df = pd.DataFrame(
        {
            "prior_extension_ema23_20d_pct": [12.0, 9.9, 12.0, 12.0],
            "prior_runup_20d_pct": [25.0, 25.0, 19.9, 25.0],
            "pullback_from_high_20d_pct": [-6.0, -6.0, -6.0, -4.9],
        }
    )

    mask = price_pullback_prior_extension_filter(df, 20, 10.0, 20.0, 5.0)

    assert mask.tolist() == [True, False, False, False]


def test_price_structure_features_add_45d_pattern_and_obv() -> None:
    close = [100.0 + i for i in range(50)]
    df = pd.DataFrame(
        {
            "stock_id": ["2330"] * 50,
            "date": [f"202601{i + 1:02d}" for i in range(50)],
            "open": [c - 0.5 for c in close],
            "high": [c + 1.0 for c in close],
            "low": [c - 1.0 for c in close],
            "close": close,
            "volume": [1000 + i * 10 for i in range(50)],
            "ema23": [c * 0.97 for c in close],
            "ma20": [c * 0.98 for c in close],
            "distance_ema23_pct": [c / (c * 0.97) * 100.0 - 100.0 for c in close],
            "start_day_volume_ratio_vs_prev20": [1.0] * 50,
            "next_open": [c + 0.2 for c in close],
        }
    )

    out = add_price_structure_features(df)
    latest = out.iloc[-1]

    assert "return_45d_pct" in out.columns
    assert latest["return_45d_pct"] > 40.0
    assert latest["range_width_45d_pct"] > 40.0
    assert 0.0 <= latest["close_position_45d_pct"] <= 110.0
    assert bool(latest["obv_above_ma20"])
    assert latest["obv_slope_5d"] > 0


def test_price_pullback_operation_research_stays_advisory_only() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2317", "2454"],
            "distance_ema23_pct": [1.0, 1.0, 1.0],
            "platform_low": [100.0, 100.0, 100.0],
            "short_platform_low": [100.0, 100.0, 100.0],
            "previous_20d_low": [100.0, 100.0, 100.0],
            "low_20": [100.0, 100.0, 100.0],
            "range_low_20d_prev": [100.0, 100.0, 100.0],
            "close": [101.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False],
            "ma10_turning_up_flag": [False, False, False],
            "volume_ratio_prev20": [1.3, 1.1, 1.6],
            "bullish_attack_candle": [True, True, True],
            "solid_red_candle": [True, False, True],
            "next_open_to_d10_close_return_pct": [6.0, -4.0, 1.0],
            "next_open_to_d20_close_return_pct": [6.0, -4.0, 1.0],
            "next_open_to_d20_high_return_pct": [6.0, 3.0, 9.0],
            "next_open_to_d20_low_return_pct": [-2.0, -6.0, -6.0],
        }
    )

    research = build_price_pullback_operation_research(df)
    assert not research.empty
    assert research["approved_for_daily"].eq(False).all()
    assert research["advisory_status"].eq("not_production_ready_research_only").all()

    high_target = research[
        research["entry_filter_id"].eq("baseline_replay")
        & research["operation_candidate_id"].eq("d20_high_target5_low_stop5_order_unresolved")
    ].iloc[0]
    assert high_target["win_count"] == 1
    assert high_target["loss_count"] == 1
    assert high_target["ambiguous_order_count"] == 1

    volume_high_target = research[
        research["entry_filter_id"].eq("volume_red_k_vol1.2")
        & research["operation_candidate_id"].eq("d20_high_target5_low_stop5_order_unresolved")
    ].iloc[0]
    assert volume_high_target["selected_stock_days"] == 2
    assert volume_high_target["win_count"] == 1
    assert volume_high_target["loss_count"] == 0
    assert volume_high_target["ambiguous_order_count"] == 1

    solid_high_target = research[
        research["entry_filter_id"].eq("solid_volume_red_k_vol1.5")
        & research["operation_candidate_id"].eq("d20_high_target5_low_stop5_order_unresolved")
    ].iloc[0]
    assert solid_high_target["selected_stock_days"] == 1
    assert solid_high_target["ambiguous_order_count"] == 1


def test_price_pullback_time_cost_backtest_tracks_first_target_stop_order() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2317", "2454", "2303"],
            "distance_ema23_pct": [1.0, 1.0, 1.0, 1.0],
            "platform_low": [100.0, 100.0, 100.0, 100.0],
            "short_platform_low": [100.0, 100.0, 100.0, 100.0],
            "previous_20d_low": [100.0, 100.0, 100.0, 100.0],
            "low_20": [100.0, 100.0, 100.0, 100.0],
            "range_low_20d_prev": [100.0, 100.0, 100.0, 100.0],
            "close": [101.0, 101.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False, False],
            "ma10_turning_up_flag": [False, False, False, False],
            "volume_ratio_prev20": [1.3, 1.1, 1.6, 0.9],
            "bullish_attack_candle": [True, True, True, False],
            "solid_red_candle": [True, False, True, False],
        }
    )
    for day in range(1, 21):
        df[f"next_open_to_d{day}_day_high_return_pct"] = [1.0, 1.0, 1.0, 1.0]
        df[f"next_open_to_d{day}_day_low_return_pct"] = [-1.0, -1.0, -1.0, -1.0]

    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 6.0
    df.loc[1, "next_open_to_d1_day_low_return_pct"] = -6.0
    df.loc[1, "next_open_to_d3_day_high_return_pct"] = 6.0
    df.loc[2, "next_open_to_d2_day_high_return_pct"] = 6.0
    df.loc[2, "next_open_to_d2_day_low_return_pct"] = -6.0

    backtest = build_price_pullback_time_cost_backtest(df)
    assert not backtest.empty
    assert backtest["approved_for_daily"].eq(False).all()

    baseline = backtest[backtest["entry_filter_id"].eq("baseline_replay")].iloc[0]
    assert baseline["mature_count"] == 4
    assert baseline["target_before_stop_count"] == 1
    assert baseline["stop_before_target_count"] == 1
    assert baseline["same_day_target_stop_count"] == 1
    assert baseline["no_decision_after_20d_count"] == 1
    assert baseline["target_before_stop_rate_pct"] == 25.0
    assert baseline["avg_holding_days_if_win"] == 2.0
    assert baseline["avg_holding_days_if_loss"] == 1.0

    volume = backtest[backtest["entry_filter_id"].eq("volume_red_k_vol1.2")].iloc[0]
    assert volume["mature_count"] == 2
    assert volume["target_before_stop_count"] == 1
    assert volume["same_day_target_stop_count"] == 1
    assert volume["no_decision_after_20d_count"] == 0


def test_price_pullback_operation_module_defines_win_neutral_failure() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2317", "2454", "2303", "2382"],
            "next_open": [100.0, 100.0, 100.0, 100.0, 100.0],
            "distance_ema23_pct": [1.0, 1.0, 1.0, 1.0, 1.0],
            "platform_low": [100.0, 100.0, 100.0, 100.0, 100.0],
            "short_platform_low": [100.0, 100.0, 100.0, 100.0, 100.0],
            "previous_20d_low": [100.0, 100.0, 100.0, 100.0, 100.0],
            "low_20": [100.0, 100.0, 100.0, 100.0, 100.0],
            "range_low_20d_prev": [100.0, 100.0, 100.0, 100.0, 100.0],
            "close": [101.0, 101.0, 101.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False, False, False],
            "ma10_turning_up_flag": [False, False, False, False, False],
            "volume_ratio_prev20": [1.3, 1.1, 1.6, 0.9, 1.0],
            "bullish_attack_candle": [True, True, True, False, True],
            "solid_red_candle": [True, False, True, False, False],
            "next_open_to_d20_close_return_pct": [6.0, -4.0, -2.0, -1.0, 1.0],
        }
    )
    for day in range(1, 21):
        df[f"next_open_to_d{day}_day_high_return_pct"] = [1.0, 1.0, 1.0, 1.0, 1.0]
        df[f"next_open_to_d{day}_day_low_return_pct"] = [-1.0, -1.0, -1.0, -1.0, -1.0]
        df[f"next_open_to_d{day}_day_close_return_pct"] = [1.0, 1.0, 1.0, 1.0, 1.0]

    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 6.0
    df.loc[1, "next_open_to_d1_day_low_return_pct"] = -6.0
    df.loc[1, "next_open_to_d1_day_close_return_pct"] = -3.0
    df.loc[2, "next_open_to_d2_day_high_return_pct"] = 6.0
    df.loc[2, "next_open_to_d2_day_low_return_pct"] = -6.0
    df.loc[2, "next_open_to_d2_day_close_return_pct"] = -3.0
    df.loc[3, "next_open_to_d20_day_close_return_pct"] = -1.0
    df.loc[4, "next_open_to_d20_day_close_return_pct"] = 1.0

    module = build_price_pullback_operation_module_research(df)
    assert not module.empty
    assert module["approved_for_daily"].eq(False).all()

    intraday = module[
        module["entry_filter_id"].eq("baseline_replay")
        & module["operation_module_candidate_id"].eq("next_open_tp5_intraday_stop5_d20_close_exit")
    ].iloc[0]
    assert intraday["win_count"] == 1
    assert intraday["neutral_count"] == 1
    assert intraday["failure_count"] == 2
    assert intraday["same_day_unresolved_count"] == 1

    structure = module[
        module["entry_filter_id"].eq("baseline_replay")
        & module["operation_module_candidate_id"].eq("next_open_tp5_structure_stop_d20_close_exit")
    ].iloc[0]
    assert structure["win_count"] == 1
    assert structure["neutral_count"] == 1
    assert structure["failure_count"] == 2
    assert structure["same_day_unresolved_count"] == 1


def test_price_pullback_operation_module_prior_high_monthline_stop() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2317", "2454", "2303"],
            "next_open": [100.0, 100.0, 100.0, 100.0],
            "distance_ema23_pct": [1.0, 1.0, 1.0, 1.0],
            "platform_low": [100.0, 100.0, 100.0, 100.0],
            "short_platform_low": [100.0, 100.0, 100.0, 100.0],
            "previous_20d_low": [100.0, 100.0, 100.0, 100.0],
            "low_20": [100.0, 100.0, 100.0, 100.0],
            "range_low_20d_prev": [100.0, 100.0, 100.0, 100.0],
            "range_high_20d_prev": [105.0, 105.0, 105.0, 105.0],
            "close": [101.0, 101.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False, False],
            "ma10_turning_up_flag": [False, False, False, False],
            "volume_ratio_prev20": [1.0, 1.0, 1.0, 1.0],
            "bullish_attack_candle": [True, True, True, True],
            "solid_red_candle": [False, False, False, False],
            "next_open_to_d20_close_return_pct": [2.0, -3.0, -3.0, 1.0],
        }
    )
    future_cols = {}
    for day in range(1, 21):
        future_cols[f"next_open_to_d{day}_day_high_return_pct"] = [1.0, 1.0, 1.0, 1.0]
        future_cols[f"next_open_to_d{day}_day_low_return_pct"] = [-1.0, -1.0, -1.0, -1.0]
        future_cols[f"next_open_to_d{day}_day_close_return_pct"] = [1.0, 1.0, 1.0, 1.0]
        future_cols[f"future_d{day}_ma20"] = [100.0, 100.0, 100.0, 100.0]
        future_cols[f"future_d{day}_ema23"] = [100.0, 100.0, 100.0, 100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)

    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 5.5
    df.loc[1, "next_open_to_d2_day_close_return_pct"] = -2.0
    df.loc[1, "next_open_to_d3_day_close_return_pct"] = -2.0
    df.loc[2, "next_open_to_d1_day_close_return_pct"] = -2.0
    df.loc[2, "next_open_to_d2_day_close_return_pct"] = -2.0
    df.loc[2, "next_open_to_d2_day_high_return_pct"] = 5.5
    df.loc[3, "next_open_to_d20_day_close_return_pct"] = 1.0

    module = build_price_pullback_operation_module_research(df)
    prior_high = module[
        module["entry_filter_id"].eq("baseline_replay")
        & module["operation_module_candidate_id"].eq(
            "next_open_prev20_high_breakout_monthline_stop1pct_2d_d20_close_exit"
        )
    ].iloc[0]

    assert prior_high["win_count"] == 1
    assert prior_high["neutral_count"] == 1
    assert prior_high["failure_count"] == 1
    assert prior_high["same_day_unresolved_count"] == 1
    assert prior_high["avg_realized_return_pct"] == 1.33
    assert prior_high["avg_win_realized_return_pct"] == 5.0
    assert prior_high["avg_failure_realized_return_pct"] == -2.0
    assert prior_high["avg_days_to_failure"] == 3.0


def test_price_pullback_operation_module_looser_lower_reference_stop_grid() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330"],
            "next_open": [100.0],
            "distance_ema23_pct": [1.0],
            "platform_low": [100.0],
            "short_platform_low": [100.0],
            "previous_20d_low": [100.0],
            "low_20": [100.0],
            "range_low_20d_prev": [100.0],
            "range_high_20d_prev": [110.0],
            "close": [101.0],
            "ema23": [100.0],
            "ma20": [105.0],
            "ema23_slope_pct": [1.0],
            "ema23_slope_5d_pct": [1.0],
            "ma5_turning_up_flag": [False],
            "ma10_turning_up_flag": [False],
            "volume_ratio_prev20": [1.0],
            "bullish_attack_candle": [True],
            "solid_red_candle": [False],
            "next_open_to_d20_close_return_pct": [-4.5],
        }
    )
    future_cols = {}
    for day in range(1, 21):
        future_cols[f"next_open_to_d{day}_day_high_return_pct"] = [1.0]
        future_cols[f"next_open_to_d{day}_day_low_return_pct"] = [-5.0]
        future_cols[f"next_open_to_d{day}_day_close_return_pct"] = [1.0]
        future_cols[f"future_d{day}_ma20"] = [105.0]
        future_cols[f"future_d{day}_ema23"] = [100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)
    for day in range(1, 5):
        df.loc[0, f"next_open_to_d{day}_day_close_return_pct"] = -4.5
    df.loc[0, "next_open_to_d20_day_close_return_pct"] = -4.5

    module = build_price_pullback_operation_module_research(df)
    looser_stop = module[
        module["entry_filter_id"].eq("baseline_replay")
        & module["operation_module_candidate_id"].eq(
            "next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit"
        )
    ].iloc[0]

    assert looser_stop["stop_reference_id"] == "lower_ma20_ema23"
    assert looser_stop["stop_buffer_pct"] == 4.0
    assert looser_stop["stop_consecutive_days"] == 4
    assert looser_stop["win_count"] == 0
    assert looser_stop["neutral_count"] == 0
    assert looser_stop["failure_count"] == 1
    assert looser_stop["avg_realized_return_pct"] == -4.5
    assert looser_stop["avg_failure_realized_return_pct"] == -4.5
    assert looser_stop["avg_days_to_failure"] == 4.0


def test_price_pullback_feature_confirmation_research_fixed_operation() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2317", "2454"],
            "next_open": [100.0, 100.0, 100.0],
            "distance_ema23_pct": [1.0, 1.0, 1.0],
            "platform_low": [100.0, 100.0, 100.0],
            "short_platform_low": [100.0, 100.0, 100.0],
            "previous_20d_low": [100.0, 100.0, 100.0],
            "low_20": [100.0, 100.0, 100.0],
            "range_low_20d_prev": [100.0, 100.0, 100.0],
            "range_high_20d_prev": [105.0, 105.0, 105.0],
            "close": [101.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False],
            "ma10_turning_up_flag": [False, False, False],
            "volume_ratio_prev20": [1.0, 1.0, 1.0],
            "bullish_attack_candle": [True, True, True],
            "solid_red_candle": [False, False, False],
            "macd_hist_gt0": [True, False, True],
            "kd_bullish_not_overheated": [True, True, False],
            "rsi14": [55.0, 75.0, 45.0],
            "bb_width_not_extreme": [True, False, True],
            "obv_above_ma20": [True, False, True],
            "tdcc_history_available": [True, True, False],
            "tdcc_consecutive_up_weeks": [1.0, 0.0, 0.0],
            "high_thresholds_up": [False, True, False],
            "all_thresholds_up": [False, False, False],
            "return_20d_pct": [10.0, 30.0, -5.0],
            "return_45d_pct": [12.0, 4.0, 20.0],
            "range_width_45d_pct": [20.0, 10.0, 25.0],
            "close_position_45d_pct": [50.0, 50.0, 90.0],
            "prior_extension_ema23_20d_pct": [12.0, 8.0, 15.0],
            "prior_runup_20d_pct": [25.0, 22.0, 18.0],
            "pullback_from_high_20d_pct": [-6.0, -6.0, -6.0],
            "next_open_to_d20_close_return_pct": [2.0, -4.5, 1.0],
        }
    )
    future_cols = {}
    for day in range(1, 21):
        future_cols[f"next_open_to_d{day}_day_high_return_pct"] = [1.0, 1.0, 1.0]
        future_cols[f"next_open_to_d{day}_day_low_return_pct"] = [-1.0, -1.0, -1.0]
        future_cols[f"next_open_to_d{day}_day_close_return_pct"] = [1.0, 1.0, 1.0]
        future_cols[f"future_d{day}_ma20"] = [101.0, 100.0, 100.0]
        future_cols[f"future_d{day}_ema23"] = [100.0, 100.0, 100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)
    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 6.0
    for day in range(1, 5):
        df.loc[1, f"next_open_to_d{day}_day_close_return_pct"] = -4.5
    df.loc[1, "next_open_to_d20_day_close_return_pct"] = -4.5

    feature = build_price_pullback_feature_confirmation_research(df)

    assert not feature.empty
    assert feature["approved_for_daily"].eq(False).all()
    assert feature["advisory_status"].eq("not_production_ready_research_only").all()
    assert set(feature["fixed_operation_module_candidate_id"]) == {
        "next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit"
    }

    baseline = feature[feature["feature_filter_id"].eq("baseline_replay")].iloc[0]
    assert baseline["mature_count"] == 3
    assert baseline["win_count"] == 1
    assert baseline["neutral_count"] == 1
    assert baseline["failure_count"] == 1
    assert baseline["win_rate_pct"] == 33.33

    macd_kd = feature[feature["feature_filter_id"].eq("macd_kd_confirm")].iloc[0]
    assert macd_kd["selected_stock_days"] == 1
    assert macd_kd["win_count"] == 1
    assert macd_kd["win_rate_pct"] == 100.0
    assert macd_kd["delta_vs_baseline_win_rate_pct"] == 66.67

    revenue = feature[feature["feature_filter_id"].eq("revenue_positive_or_strong")].iloc[0]
    market = feature[feature["feature_filter_id"].eq("market_background_regime")].iloc[0]
    assert revenue["feature_test_status"] == "blocked_data_panel_incomplete"
    assert market["feature_test_status"] == "deferred_join_required"
    assert revenue["mature_count"] == 0
    assert revenue["selected_stock_days"] == ""


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
