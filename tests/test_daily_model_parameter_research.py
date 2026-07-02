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
    _add_feature_confirmation_deltas,
    add_price_structure_features,
    attach_signal_background_features,
    add_price_pullback_research_score_columns,
    build_price_pullback_continuation_win_profile,
    build_price_pullback_exit_rule_comparison,
    build_price_pullback_feature_confirmation_research,
    build_model_parity,
    build_price_pullback_model_decision_audit,
    build_price_pullback_operation_module_research,
    build_price_pullback_operation_research,
    build_price_pullback_lifecycle_replay,
    build_price_pullback_ordered_condition_matrix,
    build_price_pullback_research_score_bucket,
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


def test_attach_signal_background_features_uses_point_in_time_theme_context(tmp_path: Path) -> None:
    panel_path = tmp_path / "daily_model_signal_background_feature_panel_latest.csv"
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "signal_date": "20260320",
                "theme_context_as_of_date": "20260313",
                "theme_context_data_status": "ready_previous_signal_date",
                "theme_context_name": "AI",
                "theme_context_final_status": "mainstream_follow_through",
                "theme_context_status_group": "mainstream_supported",
                "theme_context_source_type": "mainstream_theme_candidate",
                "theme_context_line_group": "breakout_attack_stock",
                "theme_context_line": "帶量突破",
                "theme_context_two_line_overlap": "true",
                "theme_context_priority": "2",
                "theme_context_tdcc_status": "up",
                "theme_context_warrant_flow_signal": "neutral",
                "theme_context_volume_ratio": "1.8",
                "theme_context_return_20d_pct": "12.5",
                "theme_context_repeat_label": "first_seen",
                "theme_context_volume_breakout_type": "confirmed",
                "theme_context_volume_bucket": "selected",
                "theme_context_volume_attack_status": "selected",
                "theme_context_volume_attack_selected": "true",
                "theme_context_volume_attack_watch": "false",
                "theme_context_volume_attack_failed": "false",
                "theme_context_source_artifact": "output/history/daily_signals/daily_theme_status_history.csv",
            }
        ]
    ).to_csv(panel_path, index=False)
    frame = pd.DataFrame(
        {
            "stock_id": ["2330", "2317"],
            "date": ["20260320", "20260320"],
            "close": [100.0, 100.0],
        }
    )

    out = attach_signal_background_features(frame, panel_path)

    assert bool(out.loc[0, "theme_context_ready"]) is True
    assert bool(out.loc[0, "theme_context_mainstream_supported"]) is True
    assert bool(out.loc[0, "theme_context_leadership_supported"]) is True
    assert bool(out.loc[0, "theme_context_overheated"]) is False
    assert bool(out.loc[0, "theme_context_volume_attack_selected_flag"]) is True
    assert out.loc[0, "theme_context_volume_ratio"] == 1.8
    assert out.loc[1, "theme_context_data_status"] == "no_signal_background_row"
    assert bool(out.loc[1, "theme_context_ready"]) is False


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
            "high_thresholds_up": [True, True, False],
            "all_thresholds_up": [False, False, False],
            "return_20d_pct": [10.0, 30.0, -5.0],
            "return_45d_pct": [12.0, 4.0, 20.0],
            "range_width_45d_pct": [20.0, 10.0, 25.0],
            "close_position_45d_pct": [50.0, 50.0, 90.0],
            "prior_extension_ema23_20d_pct": [12.0, 8.0, 15.0],
            "prior_runup_20d_pct": [25.0, 22.0, 18.0],
            "pullback_from_high_20d_pct": [-6.0, -6.0, -6.0],
            "theme_context_ready": [True, True, False],
            "theme_context_mainstream_supported": [True, True, False],
            "theme_context_leadership_supported": [True, False, False],
            "theme_context_overheated": [False, True, False],
            "theme_context_volume_attack_selected_flag": [True, False, False],
            "theme_context_volume_ratio": [1.8, 3.0, ""],
            "theme_context_return_20d_pct": [12.5, 42.0, ""],
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

    combo_ids = {
        "tdcc_high_thresholds_up_return20_0_25",
        "tdcc_consecutive_up_ge1_return20_0_25",
        "tdcc_high_thresholds_up_obv_above_ma20",
        "tdcc_high_thresholds_up_macd_kd_confirm",
        "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20",
        "theme_context_available",
        "theme_context_mainstream_supported",
        "theme_context_leadership_not_overheated",
        "theme_context_volume_attack_selected",
        "tdcc_high_thresholds_up_return20_0_25_theme_context_mainstream_supported",
        "tdcc_high_thresholds_up_return20_0_25_theme_context_leadership_not_overheated",
    }
    assert combo_ids <= set(feature["feature_filter_id"])
    for combo_id in combo_ids:
        combo = feature[feature["feature_filter_id"].eq(combo_id)].iloc[0]
        assert combo["selected_stock_days"] >= 1
        assert combo["advisory_status"] == "not_production_ready_research_only"

    revenue = feature[feature["feature_filter_id"].eq("revenue_positive_or_strong")].iloc[0]
    market = feature[feature["feature_filter_id"].eq("market_background_regime")].iloc[0]
    assert revenue["feature_test_status"] == "blocked_data_panel_incomplete"
    assert market["feature_test_status"] == "deferred_join_required"
    assert revenue["mature_count"] == 0
    assert revenue["selected_stock_days"] == ""

    module = build_price_pullback_operation_module_research(df)
    decision = build_price_pullback_model_decision_audit(
        module,
        feature,
        pd.DataFrame(
            [
                {
                    "parity_status": "exact_daily_row_parity_pass",
                    "parity_blocker": "",
                }
            ]
        ),
    )

    assert not decision.empty
    assert decision["approved_for_daily"].eq(False).all()
    assert decision["production_change"].eq("none").all()
    assert "baseline:production_replay_operation_anchor" in set(decision["decision_item_id"])
    assert "entry_filter:solid_volume_red_k_vol1.5" in set(decision["decision_item_id"])
    assert "feature_filter:revenue_positive_or_strong" in set(decision["decision_item_id"])
    assert "feature_filter:market_background_regime" in set(decision["decision_item_id"])

    baseline_decision = decision[
        decision["decision_item_id"].eq("baseline:production_replay_operation_anchor")
    ].iloc[0]
    assert baseline_decision["decision_status"] == "baseline_anchor"
    assert baseline_decision["selected_share_of_baseline_pct"] == 100.0

    revenue_decision = decision[decision["decision_item_id"].eq("feature_filter:revenue_positive_or_strong")].iloc[0]
    market_decision = decision[decision["decision_item_id"].eq("feature_filter:market_background_regime")].iloc[0]
    obv_combo_decision = decision[
        decision["decision_item_id"].eq("feature_filter:tdcc_high_thresholds_up_return20_0_25_obv_above_ma20")
    ].iloc[0]
    theme_decision = decision[
        decision["decision_item_id"].eq("feature_filter:theme_context_mainstream_supported")
    ].iloc[0]
    assert revenue_decision["decision_status"] == "blocked_data_gap_required_before_gate"
    assert market_decision["decision_status"] == "blocked_market_join_required"
    assert obv_combo_decision["condition_role"] == "score_bonus_candidate_not_required_gate"
    assert theme_decision["condition_role"] == "point_in_time_context_score_bonus_candidate_not_required_gate"


def test_price_pullback_exit_rule_comparison_separates_intraday_and_close_confirmed_exits() -> None:
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
            "range_high_20d_prev": [105.0, 105.0, 103.0, 103.0, 105.0],
            "close": [101.0, 101.0, 101.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False, False, False],
            "ma10_turning_up_flag": [False, False, False, False, False],
            "volume_ratio_prev20": [1.0, 1.0, 1.0, 1.0, 1.0],
            "bullish_attack_candle": [True, True, True, True, True],
            "solid_red_candle": [False, False, False, False, False],
            "macd_hist_gt0": [True, True, True, True, True],
            "kd_bullish_not_overheated": [True, True, True, True, True],
            "obv_above_ma20": [True, True, True, True, True],
            "tdcc_history_available": [True, True, True, True, True],
            "high_thresholds_up": [True, True, True, True, True],
            "return_20d_pct": [10.0, 10.0, 10.0, 10.0, 10.0],
            "return_45d_pct": [18.0, 12.0, 30.0, 8.0, -2.0],
            "range_width_45d_pct": [25.0, 20.0, 35.0, 15.0, 10.0],
            "close_position_45d_pct": [55.0, 50.0, 70.0, 45.0, 30.0],
            "prior_extension_ema23_20d_pct": [12.0, 9.0, 18.0, 6.0, 4.0],
            "prior_runup_20d_pct": [22.0, 15.0, 30.0, 12.0, 8.0],
            "pullback_from_high_20d_pct": [-6.0, -4.0, -8.0, -3.0, -2.0],
            "rsi14": [55.0, 58.0, 62.0, 50.0, 40.0],
            "obv_slope_5d": [1000.0, 800.0, 2000.0, -500.0, -1000.0],
            "tdcc_consecutive_up_weeks": [1.0, 1.0, 2.0, 1.0, 1.0],
            "theme_context_ready": [True, True, True, False, False],
            "theme_context_mainstream_supported": [True, True, True, False, False],
            "theme_context_leadership_supported": [True, False, True, False, False],
            "theme_context_overheated": [False, True, False, False, False],
            "theme_context_volume_attack_selected_flag": [True, False, True, False, False],
            "theme_context_volume_ratio": [1.8, 2.5, 2.0, "", ""],
            "theme_context_return_20d_pct": [12.5, 25.0, 18.0, "", ""],
            "next_open_to_d20_close_return_pct": [1.0, 6.0, 11.0, 2.5, -4.5],
        }
    )
    future_cols = {}
    for day in range(1, 21):
        future_cols[f"next_open_to_d{day}_day_high_return_pct"] = [1.0, 1.0, 1.0, 1.0, 1.0]
        future_cols[f"next_open_to_d{day}_day_close_return_pct"] = [1.0, 1.0, 1.0, 1.0, 1.0]
        future_cols[f"future_d{day}_ma20"] = [100.0, 100.0, 100.0, 100.0, 100.0]
        future_cols[f"future_d{day}_ema23"] = [100.0, 100.0, 100.0, 100.0, 100.0]
        future_cols[f"future_d{day}_ma5"] = [90.0, 90.0, 90.0, 90.0, 90.0]
    for day in range(1, 22):
        future_cols[f"future_d{day}_open"] = [100.0, 100.0, 100.0, 100.0, 100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)

    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 6.0
    df.loc[0, "next_open_to_d2_day_close_return_pct"] = 2.0
    df.loc[1, "next_open_to_d2_day_high_return_pct"] = 6.0
    df.loc[1, "next_open_to_d2_day_close_return_pct"] = 6.0
    df.loc[1, "future_d3_open"] = 107.0
    df.loc[2, "next_open_to_d1_day_high_return_pct"] = 4.0
    df.loc[2, "next_open_to_d1_day_close_return_pct"] = 4.0
    df.loc[2, "future_d2_open"] = 104.0
    df.loc[2, "next_open_to_d4_day_high_return_pct"] = 8.0
    df.loc[2, "next_open_to_d4_day_close_return_pct"] = 8.0
    df.loc[2, "future_d5_open"] = 109.0
    df.loc[2, "next_open_to_d6_day_high_return_pct"] = 11.0
    df.loc[2, "next_open_to_d6_day_close_return_pct"] = 11.0
    df.loc[2, "future_d7_open"] = 112.0
    df.loc[3, "next_open_to_d1_day_high_return_pct"] = 4.0
    df.loc[3, "next_open_to_d1_day_close_return_pct"] = 4.0
    df.loc[3, "future_d2_open"] = 104.5
    df.loc[3, "next_open_to_d2_day_close_return_pct"] = 2.5
    df.loc[3, "future_d2_ma5"] = 103.0
    df.loc[3, "future_d3_open"] = 103.5
    for day in range(1, 5):
        df.loc[4, f"next_open_to_d{day}_day_close_return_pct"] = -4.5

    comparison = build_price_pullback_exit_rule_comparison(df)

    assert not comparison.empty
    assert comparison["approved_for_daily"].eq(False).all()
    assert comparison["advisory_status"].eq("not_production_ready_research_only").all()
    assert "close_prev20_high_break_same_day_close" not in set(comparison["exit_rule_id"])

    intraday = comparison[
        comparison["entry_filter_id"].eq("baseline_replay")
        & comparison["exit_rule_id"].eq("intraday_prev20_high_touch_same_day_close")
    ].iloc[0]
    close_confirmed = comparison[
        comparison["entry_filter_id"].eq("baseline_replay")
        & comparison["exit_rule_id"].eq("close_prev20_high_break_next_open")
    ].iloc[0]
    tp8 = comparison[
        comparison["entry_filter_id"].eq("baseline_replay")
        & comparison["exit_rule_id"].eq("close_prev20_break_then_tp8_or_5ma_next_open")
    ].iloc[0]

    assert intraday["formal_price_rule_status"] == "research_only_intraday_trigger"
    assert intraday["win_count"] == 4
    assert intraday["failure_count"] == 1
    assert intraday["avg_realized_return_pct"] == 2.3

    assert close_confirmed["formal_price_rule_status"] == "close_confirmed_candidate"
    assert close_confirmed["win_count"] == 3
    assert close_confirmed["neutral_count"] == 1
    assert close_confirmed["failure_count"] == 1
    assert close_confirmed["avg_realized_return_pct"] == 2.4

    assert tp8["win_count"] == 1
    assert tp8["neutral_count"] == 3
    assert tp8["failure_count"] == 1
    assert tp8["ma5_exit_count"] == 1
    assert tp8["hard_stop_count"] == 1

    profile = build_price_pullback_continuation_win_profile(df)
    assert not profile.empty
    assert profile["approved_for_daily"].eq(False).all()
    assert profile["production_change"].eq("none").all()
    assert {"obv_above_ma20", "theme_context_mainstream_supported"} <= set(profile["feature_column"])
    assert set(profile["exit_rule_id"]) == {
        "close_prev20_break_then_tp5_or_5ma_next_open",
        "close_prev20_break_then_tp8_or_5ma_next_open",
        "close_prev20_break_then_tp10_or_5ma_next_open",
    }

    scored = add_price_pullback_research_score_columns(df)
    assert scored.loc[0, "price_pullback_research_score"] >= 6
    assert scored.loc[0, "price_pullback_research_score_bucket"] == "score_6_plus"
    assert "obv_above_ma20" in scored.loc[0, "price_pullback_research_score_components"]

    score_bucket = build_price_pullback_research_score_bucket(df)
    assert not score_bucket.empty
    assert score_bucket["approved_for_daily"].eq(False).all()
    assert score_bucket["production_change"].eq("none").all()
    assert "research_only_not_production_score" in set(score_bucket["score_use"])
    assert "score_6_plus" in set(score_bucket["score_bucket"])
    assert "close_prev20_high_break_next_open" in set(score_bucket["exit_rule_id"])

    condition_matrix = build_price_pullback_ordered_condition_matrix(df)
    assert not condition_matrix.empty
    assert condition_matrix["approved_for_daily"].eq(False).all()
    assert condition_matrix["production_change"].eq("none").all()
    assert "baseline_replay" in set(condition_matrix["condition_test_id"])
    assert "research_score_ge4" in set(condition_matrix["condition_test_id"])
    assert "prev20_space_ge3" in set(condition_matrix["condition_test_id"])
    assert "score_ge4_prev20_space_ge3_tdcc_or_obv" in set(condition_matrix["condition_test_id"])
    assert "v1_gate_return20_obv_or_tdcc" in set(condition_matrix["condition_test_id"])
    assert "v1_gate_return20_score_ge4_obv_or_tdcc" in set(condition_matrix["condition_test_id"])
    assert "close_prev20_high_break_next_open" in set(condition_matrix["exit_rule_id"])
    layered = condition_matrix[
        condition_matrix["condition_test_id"].eq("score_ge4_prev20_space_ge3_tdcc_or_obv")
        & condition_matrix["exit_rule_id"].eq("close_prev20_high_break_next_open")
    ].iloc[0]
    assert layered["score_use"] == "research_only_not_production_score"
    assert layered["selected_stock_days"] >= 1
    v1_candidate = condition_matrix[
        condition_matrix["condition_test_id"].eq("v1_gate_return20_score_ge4_obv_or_tdcc")
        & condition_matrix["exit_rule_id"].eq("close_prev20_high_break_next_open")
    ].iloc[0]
    assert v1_candidate["data_status"] == "research_only_v1_candidate_not_production"
    assert v1_candidate["selected_stock_days"] >= 1


def test_price_pullback_lifecycle_replay_suppresses_same_stock_active_signals() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2330", "2330", "2330", "2330", "2317"],
            "date": ["20260101", "20260102", "20260103", "20260104", "20260105", "20260101"],
            "next_open": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
            "distance_ema23_pct": [1.0, 1.0, 50.0, 50.0, 1.0, 1.0],
            "platform_low": [100.0, 100.0, 50.0, 50.0, 100.0, 100.0],
            "short_platform_low": [100.0, 100.0, 50.0, 50.0, 100.0, 100.0],
            "previous_20d_low": [100.0, 100.0, 50.0, 50.0, 100.0, 100.0],
            "low_20": [100.0, 100.0, 50.0, 50.0, 100.0, 100.0],
            "range_low_20d_prev": [100.0, 100.0, 50.0, 50.0, 100.0, 100.0],
            "range_high_20d_prev": [105.0, 105.0, 105.0, 105.0, 105.0, 105.0],
            "close": [101.0, 101.0, 200.0, 200.0, 101.0, 101.0],
            "ema23": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
            "ma20": [101.0, 101.0, 101.0, 101.0, 101.0, 101.0],
            "ema23_slope_pct": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "ema23_slope_5d_pct": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "ma5_turning_up_flag": [False, False, False, False, False, False],
            "ma10_turning_up_flag": [False, False, False, False, False, False],
            "volume_ratio_prev20": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "bullish_attack_candle": [True, True, True, True, True, True],
            "solid_red_candle": [False, False, False, False, False, False],
            "macd_hist_gt0": [True, True, True, True, True, True],
            "kd_bullish_not_overheated": [True, True, True, True, True, True],
            "obv_above_ma20": [True, True, True, True, True, True],
            "tdcc_history_available": [True, True, True, True, True, True],
            "high_thresholds_up": [True, True, True, True, True, True],
            "return_20d_pct": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
            "return_45d_pct": [18.0, 18.0, 18.0, 18.0, 18.0, 18.0],
            "range_width_45d_pct": [25.0, 25.0, 25.0, 25.0, 25.0, 25.0],
            "close_position_45d_pct": [55.0, 55.0, 55.0, 55.0, 55.0, 55.0],
            "prior_extension_ema23_20d_pct": [12.0, 12.0, 12.0, 12.0, 12.0, 12.0],
            "prior_runup_20d_pct": [22.0, 22.0, 22.0, 22.0, 22.0, 22.0],
            "pullback_from_high_20d_pct": [-6.0, -6.0, -6.0, -6.0, -6.0, -6.0],
            "rsi14": [55.0, 55.0, 55.0, 55.0, 55.0, 55.0],
            "obv_slope_5d": [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0],
            "tdcc_consecutive_up_weeks": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "theme_context_ready": [False, False, False, False, False, False],
            "theme_context_mainstream_supported": [False, False, False, False, False, False],
            "theme_context_leadership_supported": [False, False, False, False, False, False],
            "theme_context_overheated": [False, False, False, False, False, False],
            "theme_context_volume_attack_selected_flag": [False, False, False, False, False, False],
            "theme_context_volume_ratio": ["", "", "", "", "", ""],
            "theme_context_return_20d_pct": ["", "", "", "", "", ""],
            "next_open_to_d20_close_return_pct": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        }
    )
    future_cols = {}
    for day in range(1, 21):
        future_cols[f"next_open_to_d{day}_day_high_return_pct"] = [1.0] * len(df)
        future_cols[f"next_open_to_d{day}_day_close_return_pct"] = [1.0] * len(df)
        future_cols[f"future_d{day}_ma20"] = [100.0] * len(df)
        future_cols[f"future_d{day}_ema23"] = [100.0] * len(df)
        future_cols[f"future_d{day}_ma5"] = [90.0] * len(df)
    for day in range(1, 22):
        future_cols[f"future_d{day}_open"] = [100.0] * len(df)
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)
    signal_rows = [0, 1, 4, 5]
    for row_idx in signal_rows:
        df.loc[row_idx, "next_open_to_d2_day_close_return_pct"] = 6.0
        df.loc[row_idx, "future_d3_open"] = 107.0

    replay = build_price_pullback_lifecycle_replay(df)

    row = replay[
        replay["condition_test_id"].eq("v1_gate_return20_tdcc_high")
        & replay["exit_rule_id"].eq("close_prev20_high_break_next_open")
    ].iloc[0]
    assert row["lifecycle_replay_scope"] == "trade_level_same_stock_active_position_suppressed"
    assert row["source_mature_signal_stock_days"] == 4
    assert row["accepted_trade_count"] == 3
    assert row["suppressed_signal_count"] == 1
    assert row["accepted_avg_trades_per_signal_day"] == 1.5
    assert row["research_trading_day_count"] == 5
    assert row["accepted_avg_trades_per_research_day"] == 0.6
    assert row["win_rate_pct"] == 100.0
    assert bool(row["approved_for_daily"]) is False
    assert row["production_change"] == "none"
    assert row["pdf_metric_readiness"] == "blocked_until_formal_promotion_and_operation_adapter_contract"


def test_feature_confirmation_deltas_support_future_string_dtype() -> None:
    rows = [
        {
            "feature_filter_id": "baseline_replay",
            "feature_test_status": "tested_point_in_time",
            "selected_stock_days": 100,
            "mature_count": 80,
            "win_rate_pct": 40.0,
            "failure_rate_pct": 45.0,
            "avg_realized_return_pct": 0.5,
            "avg_realized_or_d20_days": 12.0,
        },
        {
            "feature_filter_id": "macd_hist_gt0",
            "feature_test_status": "tested_point_in_time",
            "selected_stock_days": 50,
            "mature_count": 40,
            "win_rate_pct": 55.0,
            "failure_rate_pct": 35.0,
            "avg_realized_return_pct": 0.8,
            "avg_realized_or_d20_days": 10.0,
        },
    ]

    with pd.option_context("future.infer_string", True):
        result = _add_feature_confirmation_deltas(pd.DataFrame(rows))

    macd = result[result["feature_filter_id"].eq("macd_hist_gt0")].iloc[0]
    assert macd["selected_share_of_baseline_pct"] == 50.0
    assert macd["mature_share_of_baseline_pct"] == 50.0
    assert macd["delta_vs_baseline_win_rate_pct"] == 15.0
    assert macd["delta_vs_baseline_failure_rate_pct"] == -10.0
    assert macd["delta_vs_baseline_avg_realized_return_pct"] == 0.3
    assert macd["delta_vs_baseline_avg_realized_or_d20_days"] == -2.0


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
