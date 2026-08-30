from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_candidate_model_layer import build_parameter_table, build_specs  # noqa: E402
from build_daily_model_parameter_research import (  # noqa: E402
    ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
    _add_feature_confirmation_deltas,
    _revenue_benchmark_index,
    _revenue_feature_context_anomaly_candidate_mask,
    _revenue_future_close_path_audit,
    active_price_attack_proxy,
    add_price_structure_features,
    attach_full_monthly_revenue_history_features,
    attach_signal_background_features,
    add_price_pullback_high_return_feature_score_columns,
    add_price_pullback_research_score_columns,
    build_price_pullback_continuation_win_profile,
    build_price_pullback_exit_rule_comparison,
    build_price_pullback_feature_confirmation_research,
    build_price_pullback_high_return_feature_score_grid,
    build_price_pullback_revenue_condition_matrix,
    build_model_parity,
    build_price_pullback_model_decision_audit,
    build_price_pullback_operation_module_research,
    build_price_pullback_operation_research,
    build_price_pullback_lifecycle_replay,
    build_price_pullback_ordered_condition_matrix,
    build_price_pullback_promotion_matrix,
    build_price_pullback_research_score_bucket,
    build_price_pullback_time_cost_backtest,
    build_revenue_unreacted_range_feature_contrast_audit,
    build_revenue_unreacted_range_operation_candidate_matrix,
    build_revenue_unreacted_range_revenue_condition_matrix,
    current_price_pullback_baseline_proxy,
    PRIMARY_ANOMALY_BASIS,
    price_pullback_prior_extension_filter,
    REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
    REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
    revenue_unreacted_active_attack_proxy,
    rule_specs,
    sample_status,
)
from revenue_unreacted_range_close_confirmation_timing import (  # noqa: E402
    ANOMALY_CANDIDATE_SENSITIVITY_BASIS as REVENUE_TIMING_SOURCE_SENSITIVITY_BASIS,
    DECISION_BASIS as REVENUE_TIMING_DECISION_BASIS,
    build_close_confirmation_timing_audit,
)
from revenue_unreacted_range_fixed_confirmation_feature_contrast import (  # noqa: E402
    RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
    build_fixed_confirmation_feature_contrast,
)
from validate_daily_model_research_parity import validate_rule_specs  # noqa: E402
from validate_daily_model_revenue_condition_matrix import validate_price_pullback, validate_revenue_unreacted  # noqa: E402
from validate_price_pullback_promotion_matrix import validate_matrix as validate_promotion_matrix  # noqa: E402
from validate_revenue_unreacted_range_operation_candidate_matrix import (  # noqa: E402
    validate_matrix as validate_revenue_operation_candidate_matrix,
)
from validate_revenue_unreacted_range_feature_contrast_audit import validate_frames as validate_revenue_feature_contrast  # noqa: E402
from validate_revenue_unreacted_range_close_confirmation_timing_audit import (  # noqa: E402
    validate_frames as validate_revenue_close_confirmation_timing,
)
from validate_revenue_unreacted_range_fixed_confirmation_feature_contrast import (  # noqa: E402
    validate_frames as validate_revenue_fixed_feature_contrast,
)
from validate_research_against_stock_model_contract import (  # noqa: E402
    REVENUE_DETAIL_PATH,
    REVENUE_EVIDENCE_PATH,
    REVENUE_EVIDENCE_PERMISSION_STATUS,
    REVENUE_EVIDENCE_STATUS,
    REVENUE_EVIDENCE_VERSION,
    REVENUE_EXPECTED_OPERATION_COUNT,
    REVENUE_EXPECTED_UNIQUE_STOCK_COUNT,
    REVENUE_LEGACY_PROXY_BLOCKER,
    REVENUE_LEGACY_PROXY_ID,
    REVENUE_MATRIX_PATH,
    REVENUE_PRE_PROMOTION_BLOCKER,
    REVENUE_RULE_CANONICAL_SHA256,
    REVENUE_RULE_SPEC_ID,
    build_parity_rows,
    load_revenue_frozen_evidence,
)


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


# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
def test_shared_revenue_research_baseline_remains_advisory_proxy() -> None:
    revenue_specs = [
        spec for spec in rule_specs() if spec.model_id == "revenue_unreacted_range"
    ]
    baselines = [
        spec for spec in revenue_specs if spec.parameter_role == "production_baseline"
    ]

    assert len(baselines) == 1
    assert baselines[0].parameter_set_id == REVENUE_LEGACY_PROXY_ID
    assert baselines[0].production_parity_status == "proxy_only"
    assert baselines[0].parity_blocker == REVENUE_LEGACY_PROXY_BLOCKER


def test_revenue_frozen_evidence_loader_binds_exact_rule_and_permissions() -> None:
    evidence = load_revenue_frozen_evidence()

    assert evidence["evidence_version"] == REVENUE_EVIDENCE_VERSION
    assert evidence["rule_spec_id"] == REVENUE_RULE_SPEC_ID
    assert evidence["rule_canonical_sha256"] == REVENUE_RULE_CANONICAL_SHA256
    assert evidence["launch_evidence_status"] == REVENUE_EVIDENCE_STATUS
    assert evidence["selected_operation_count"] == str(
        REVENUE_EXPECTED_OPERATION_COUNT
    )
    assert evidence["selected_unique_stock_count"] == str(
        REVENUE_EXPECTED_UNIQUE_STOCK_COUNT
    )
    assert evidence["evidence_permission_status"] == REVENUE_EVIDENCE_PERMISSION_STATUS
    assert {
        evidence["formal_model_use_allowed"],
        evidence["approved_for_daily"],
        evidence["presentation_allowed"],
        evidence["production_allowed"],
    } == {"False"}


def test_revenue_frozen_evidence_loader_rejects_permission_drift(
    tmp_path: Path,
) -> None:
    for relative_path in (
        REVENUE_EVIDENCE_PATH,
        REVENUE_DETAIL_PATH,
        REVENUE_MATRIX_PATH,
    ):
        target = tmp_path / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / relative_path).read_bytes())
    manifest_path = tmp_path / REVENUE_EVIDENCE_PATH
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[0, "production_allowed"] = "True"
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    with pytest.raises(RuntimeError, match="canonical pin mismatch"):
        load_revenue_frozen_evidence(
            root=tmp_path,
        )


def test_shared_revenue_parity_artifact_stays_generic_proxy_only() -> None:
    source = pd.read_csv(
        ROOT / "output/latest/research_backtest/daily_model_research_parity_latest.csv",
        dtype=str,
        keep_default_na=False,
    )
    revenue = source[source["model_id"].eq("revenue_unreacted_range")]

    assert len(revenue) == 1
    assert revenue.iloc[0]["research_baseline_status"] == "proxy_only"
    assert revenue.iloc[0]["research_baseline_parameter_set_id"] == (
        REVENUE_LEGACY_PROXY_ID
    )
    assert revenue.iloc[0]["parity_blocker"] == REVENUE_LEGACY_PROXY_BLOCKER
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def test_daily_model_research_parity_validator_rule_specs_pass() -> None:
    assert validate_rule_specs() == []


def test_contract_parity_monitor_excludes_deprecated_registry_only_models() -> None:
    rows, _, source_errors = build_parity_rows()
    model_ids = {row["model_id"] for row in rows}

    assert source_errors == []
    assert "neckline_volume_breakout_confirmation" in model_ids
    assert "near_high_neckline_challenge" not in model_ids
    assert "platform_strengthening" not in model_ids


# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
def test_contract_parity_monitor_uses_revenue_frozen_evidence_not_legacy_proxy() -> None:
    rows, _, source_errors = build_parity_rows()
    revenue = next(row for row in rows if row["model_id"] == "revenue_unreacted_range")

    assert source_errors == []
    assert revenue["research_contract_version"] == (
        f"research:{REVENUE_EVIDENCE_VERSION}"
    )
    assert revenue["parity_status"] == "warning_research_variant_only"
    assert revenue["approved_research_variant"] == "True"
    assert revenue["promotion_required"] == "True"
    assert revenue["parity_blocker"] == REVENUE_PRE_PROMOTION_BLOCKER
    assert revenue["recommended_action"] == (
        "exact_frozen_evidence_ready_do_not_promote_until_model_contract_sync"
    )
    assert revenue["research_evidence_path"] == (
        REVENUE_EVIDENCE_PATH
    )
    assert revenue["research_evidence_status"] == (
        REVENUE_EVIDENCE_STATUS
    )
    assert revenue["research_permission_status"] == (
        REVENUE_EVIDENCE_PERMISSION_STATUS
    )
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


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


def test_price_structure_rolling_windows_do_not_cross_stock_boundaries() -> None:
    rows: list[dict[str, object]] = []
    dates = pd.date_range("2026-01-01", periods=30, freq="B").strftime("%Y%m%d")
    for stock_id, base_price, daily_volume in (
        ("1111", 10.0, 10_000.0),
        ("2222", 1_000.0, 2_000_000.0),
    ):
        for position, date in enumerate(dates):
            close = base_price + position
            rows.append(
                {
                    "stock_id": stock_id,
                    "date": date,
                    "open": close - 0.5,
                    "high": close + 1.0,
                    "low": close - 1.0,
                    "close": close,
                    "volume": daily_volume,
                    "ma20": close * 0.98,
                    "ema23": close * 0.99,
                    "distance_ema23_pct": close / (close * 0.99) * 100.0 - 100.0,
                    "start_day_volume_ratio_vs_prev20": 1.0,
                    "next_open": close + 0.2,
                }
            )

    out = add_price_structure_features(pd.DataFrame(rows))
    second = out[out["stock_id"].eq("2222")].reset_index(drop=True)

    assert second.loc[10, "range_low_10d_prev"] == 999.0
    assert second.loc[10, "range_high_10d_prev"] == 1_010.0
    assert second.loc[10, "range_width_10d_pct"] < 1.2
    assert second.loc[10, "volume_ma20_lots"] == 2_000.0


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
                "monthly_revenue_context_as_of_date": "20260313",
                "monthly_revenue_rows_as_of": "1",
                "monthly_revenue_future_rows_ignored": "0",
                "monthly_revenue_data_status": "ready_previous_snapshot_date",
                "monthly_revenue_period": "202602",
                "monthly_revenue_latest_yoy_pct": "10.5",
                "monthly_revenue_cumulative_yoy_pct": "8.0",
                "monthly_revenue_positive_flag": "true",
                "monthly_revenue_strong_flag": "false",
                "monthly_revenue_good_eps_unconfirmed_flag": "false",
                "monthly_revenue_numerical_anomaly_flag": "false",
                "monthly_revenue_source_artifact": "output/history/daily_model_snapshots/all_candidates_20260313.csv",
                "monthly_revenue_formal_model_use_allowed": "false",
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
    assert bool(out.loc[0, "monthly_revenue_context_ready"]) is True
    assert bool(out.loc[0, "monthly_revenue_positive_or_strong"]) is True
    assert out.loc[0, "monthly_revenue_latest_yoy_pct"] == 10.5
    assert out.loc[1, "theme_context_data_status"] == "no_signal_background_row"
    assert bool(out.loc[1, "theme_context_ready"]) is False
    assert bool(out.loc[1, "monthly_revenue_context_ready"]) is False


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
    for day in range(1, 22):
        future_cols[f"future_d{day}_open"] = [100.0, 100.0, 100.0, 100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)

    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 5.5
    df.loc[1, "next_open_to_d2_day_close_return_pct"] = -2.0
    df.loc[1, "next_open_to_d3_day_close_return_pct"] = -2.0
    df.loc[1, "future_d4_open"] = 97.5
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
    assert prior_high["avg_realized_return_pct"] == 1.17
    assert prior_high["avg_win_realized_return_pct"] == 5.0
    assert prior_high["avg_failure_realized_return_pct"] == -2.5
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
    for day in range(1, 22):
        future_cols[f"future_d{day}_open"] = [100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)
    for day in range(1, 5):
        df.loc[0, f"next_open_to_d{day}_day_close_return_pct"] = -4.5
    df.loc[0, "next_open_to_d20_day_close_return_pct"] = -4.5
    df.loc[0, "future_d5_open"] = 94.0

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
    assert looser_stop["avg_realized_return_pct"] == -6.0
    assert looser_stop["avg_failure_realized_return_pct"] == -6.0
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
            "monthly_revenue_context_ready": [True, True, False],
            "monthly_revenue_positive_or_strong": [True, False, False],
            "monthly_revenue_formal_model_use_allowed": [False, False, False],
            "monthly_revenue_numerical_anomaly_flag": [False, False, False],
            "monthly_revenue_latest_yoy_pct": [10.5, -3.0, ""],
            "monthly_revenue_cumulative_yoy_pct": [8.0, -1.0, ""],
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
    for day in range(1, 22):
        future_cols[f"future_d{day}_open"] = [100.0, 100.0, 100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)
    df.loc[0, "next_open_to_d2_day_high_return_pct"] = 6.0
    for day in range(1, 5):
        df.loc[1, f"next_open_to_d{day}_day_close_return_pct"] = -4.5
    df.loc[1, "next_open_to_d20_day_close_return_pct"] = -4.5
    df.loc[1, "future_d5_open"] = 95.0

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
        "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20_revenue_positive_or_strong",
    }
    assert combo_ids <= set(feature["feature_filter_id"])
    for combo_id in combo_ids:
        combo = feature[feature["feature_filter_id"].eq(combo_id)].iloc[0]
        assert combo["selected_stock_days"] >= 1
        assert combo["advisory_status"] == "not_production_ready_research_only"

    revenue = feature[feature["feature_filter_id"].eq("revenue_positive_or_strong")].iloc[0]
    market = feature[feature["feature_filter_id"].eq("market_background_regime")].iloc[0]
    assert revenue["feature_test_status"] == "tested_point_in_time"
    assert revenue["data_status"] == "joined_from_monthly_revenue_pit_panel_coverage_limited_research_only"
    assert market["feature_test_status"] == "deferred_join_required"
    assert revenue["mature_count"] == 1
    assert revenue["selected_stock_days"] == 1

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
    assert revenue_decision["decision_status"] == "coverage_limited_score_discussion_not_required_gate"
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
    df.loc[4, "future_d5_open"] = 94.0

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
    assert intraday["avg_realized_return_pct"] == 2.0

    assert close_confirmed["formal_price_rule_status"] == "close_confirmed_candidate"
    assert close_confirmed["win_count"] == 3
    assert close_confirmed["neutral_count"] == 1
    assert close_confirmed["failure_count"] == 1
    assert close_confirmed["avg_realized_return_pct"] == 2.1

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

    high_return_scored = add_price_pullback_high_return_feature_score_columns(df)
    assert high_return_scored.loc[0, "price_pullback_high_return_feature_score"] == 4
    assert "prev20_target_space_5_to_8" in high_return_scored.loc[
        0, "price_pullback_high_return_feature_score_components"
    ]

    score_bucket = build_price_pullback_research_score_bucket(df)
    assert not score_bucket.empty
    assert score_bucket["approved_for_daily"].eq(False).all()
    assert score_bucket["production_change"].eq("none").all()
    assert "research_only_not_production_score" in set(score_bucket["score_use"])
    assert "score_6_plus" in set(score_bucket["score_bucket"])
    assert "close_prev20_high_break_next_open" in set(score_bucket["exit_rule_id"])

    high_return_grid = build_price_pullback_high_return_feature_score_grid(df)
    assert not high_return_grid.empty
    assert high_return_grid["approved_for_daily"].eq(False).all()
    assert high_return_grid["production_change"].eq("none").all()
    assert "research_high_return_feature_score_v1" in set(high_return_grid["score_draft_id"])
    assert {PRIMARY_ANOMALY_BASIS, ANOMALY_CANDIDATE_SENSITIVITY_BASIS} <= set(
        high_return_grid["anomaly_exclusion_basis"]
    )
    assert "score_threshold" in set(high_return_grid["score_bucket_type"])
    assert "score_ge_4" in set(high_return_grid["score_bucket"])
    threshold = high_return_grid[
        high_return_grid["score_bucket"].eq("score_ge_4")
        & high_return_grid["exit_rule_id"].eq("close_prev20_high_break_next_open")
        & high_return_grid["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ].iloc[0]
    assert threshold["score_use"] == "research_only_not_production_score"
    assert threshold["accepted_trade_count"] >= 1

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


def test_full_monthly_revenue_history_join_uses_source_table_date_asof(tmp_path: Path) -> None:
    history = pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "revenue_period": "202601",
                "source_table_date": "20260217",
                "source_kind": "official_test",
                "latest_revenue_yoy_pct": "40",
                "cumulative_revenue_yoy_pct": "25",
                "month_over_month_pct": "5",
                "revenue_numerical_anomaly_flag": "False",
                "revenue_numerical_anomaly_reason": "",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
            }
        ]
    )
    path = tmp_path / "monthly_revenue_history.csv"
    history.to_csv(path, index=False)
    frame = pd.DataFrame(
        [
            {"stock_id": "2330", "date": "20260216"},
            {"stock_id": "2330", "date": "20260217"},
            {"stock_id": "9999", "date": "20260217"},
        ]
    )

    joined = attach_full_monthly_revenue_history_features(frame, path)

    assert list(joined["full_monthly_revenue_data_status"]) == [
        "missing_asof_revenue_on_or_before_signal_date",
        "ready_asof_history_row",
        "missing_stock_in_full_monthly_revenue_history",
    ]
    assert bool(joined.loc[1, "full_monthly_revenue_context_ready"]) is True
    assert bool(joined.loc[1, "full_monthly_revenue_strong_flag"]) is True
    assert bool(joined.loc[1, "full_monthly_revenue_formal_model_use_allowed"]) is False


def test_full_monthly_revenue_history_join_adds_lagged_turnaround_context(tmp_path: Path) -> None:
    history = pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "revenue_period": "202511",
                "source_table_date": "20251217",
                "source_kind": "official_test",
                "latest_revenue_yoy_pct": "-10",
                "cumulative_revenue_yoy_pct": "-6",
                "month_over_month_pct": "1",
                "revenue_numerical_anomaly_flag": "False",
                "revenue_numerical_anomaly_reason": "",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
            },
            {
                "stock_id": "2330",
                "revenue_period": "202512",
                "source_table_date": "20260117",
                "source_kind": "official_test",
                "latest_revenue_yoy_pct": "-5",
                "cumulative_revenue_yoy_pct": "-2",
                "month_over_month_pct": "2",
                "revenue_numerical_anomaly_flag": "False",
                "revenue_numerical_anomaly_reason": "",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
            },
            {
                "stock_id": "2330",
                "revenue_period": "202601",
                "source_table_date": "20260217",
                "source_kind": "official_test",
                "latest_revenue_yoy_pct": "8",
                "cumulative_revenue_yoy_pct": "1",
                "month_over_month_pct": "3",
                "revenue_numerical_anomaly_flag": "False",
                "revenue_numerical_anomaly_reason": "",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
            },
        ]
    )
    path = tmp_path / "monthly_revenue_history.csv"
    history.to_csv(path, index=False)
    frame = pd.DataFrame([{"stock_id": "2330", "date": "20260217"}])

    joined = attach_full_monthly_revenue_history_features(frame, path)

    assert bool(joined.loc[0, "full_monthly_revenue_context_ready"]) is True
    assert joined.loc[0, "full_monthly_revenue_period"] == "202601"
    assert joined.loc[0, "full_monthly_revenue_prev1_period"] == "202512"
    assert joined.loc[0, "full_monthly_revenue_prev2_period"] == "202511"
    assert joined.loc[0, "full_monthly_revenue_prev1_latest_yoy_pct"] == -5.0
    assert joined.loc[0, "full_monthly_revenue_prev2_latest_yoy_pct"] == -10.0
    assert joined.loc[0, "full_monthly_revenue_latest_yoy_delta_1m_pct_points"] == 13.0
    assert joined.loc[0, "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points"] == 3.0


def _price_pullback_revenue_matrix_fixture() -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2330", "2317"],
            "date": ["20260101", "20260102", "20260101"],
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
            "obv_above_ma20": [True, True, True],
            "tdcc_history_available": [True, True, True],
            "high_thresholds_up": [True, True, True],
            "return_20d_pct": [10.0, 10.0, 10.0],
            "return_45d_pct": [18.0, 18.0, 18.0],
            "range_width_45d_pct": [25.0, 25.0, 25.0],
            "prior_extension_ema23_20d_pct": [12.0, 12.0, 12.0],
            "prior_runup_20d_pct": [22.0, 22.0, 22.0],
            "pullback_from_high_20d_pct": [-6.0, -6.0, -6.0],
            "full_monthly_revenue_context_ready": [True, True, True],
            "full_monthly_revenue_latest_yoy_pct": [40.0, 40.0, -5.0],
            "full_monthly_revenue_cumulative_yoy_pct": [25.0, 25.0, -2.0],
            "full_monthly_revenue_prev1_latest_yoy_pct": [-5.0, -5.0, -8.0],
            "full_monthly_revenue_prev2_latest_yoy_pct": [-10.0, -10.0, -6.0],
            "full_monthly_revenue_prev3_latest_yoy_pct": [-15.0, -15.0, -4.0],
            "full_monthly_revenue_prev1_cumulative_yoy_pct": [-2.0, -2.0, -3.0],
            "full_monthly_revenue_prev2_cumulative_yoy_pct": [-6.0, -6.0, -2.0],
            "full_monthly_revenue_prev3_cumulative_yoy_pct": [-8.0, -8.0, -1.0],
            "full_monthly_revenue_latest_yoy_delta_1m_pct_points": [45.0, 45.0, 3.0],
            "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points": [27.0, 27.0, 1.0],
            "full_monthly_revenue_positive_flag": [True, True, False],
            "full_monthly_revenue_strong_flag": [True, True, False],
            "full_monthly_revenue_positive_or_strong": [True, True, False],
            "full_monthly_revenue_numerical_anomaly_flag": [False, False, False],
            "next_open_to_d20_close_return_pct": [6.0, 6.0, -2.0],
        }
    )
    future_cols = {}
    for day in range(1, 21):
        future_cols[f"next_open_to_d{day}_day_close_return_pct"] = [1.0, 1.0, -2.0]
        future_cols[f"future_d{day}_ma20"] = [100.0, 100.0, 100.0]
        future_cols[f"future_d{day}_ema23"] = [100.0, 100.0, 100.0]
        future_cols[f"future_d{day}_ma5"] = [90.0, 90.0, 90.0]
    for day in range(2, 22):
        future_cols[f"future_d{day}_open"] = [100.0, 100.0, 100.0]
    df = pd.concat([df, pd.DataFrame(future_cols)], axis=1)
    df.loc[[0, 1], "next_open_to_d2_day_close_return_pct"] = 6.0
    df.loc[[0, 1], "future_d3_open"] = 107.0
    return df


def test_price_pullback_revenue_condition_matrix_is_research_only_and_uses_lifecycle() -> None:
    matrix = build_price_pullback_revenue_condition_matrix(_price_pullback_revenue_matrix_fixture())

    assert not matrix.empty
    assert validate_price_pullback(matrix.astype(str)) == []
    assert matrix["approved_for_daily"].eq(False).all()
    assert matrix["production_change"].eq("none").all()
    assert set(matrix["exit_rule_id"]) == {"close_prev20_high_break_next_open"}
    assert "revenue_production_strong" in set(matrix["condition_test_id"])
    strong = matrix[
        matrix["condition_test_id"].eq("revenue_production_strong")
        & matrix["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ].iloc[0]
    assert strong["lifecycle_replay_scope"] == "trade_level_same_stock_active_position_suppressed_after_condition"
    assert strong["source_mature_signal_stock_days"] == 2
    assert strong["accepted_trade_count"] == 1
    assert strong["suppressed_signal_count"] == 1
    assert strong["promotion_readiness"] == "blocked_model_specific_promotion_pr_required"
    turnaround = matrix[
        matrix["condition_test_id"].eq("latest_yoy_turn_positive_after_2_negative")
        & matrix["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ].iloc[0]
    assert turnaround["source_mature_signal_stock_days"] == 2
    assert turnaround["accepted_trade_count"] == 1
    assert turnaround["suppressed_signal_count"] == 1
    combo = matrix[
        matrix["condition_test_id"].eq("latest_improving_2m_and_cumulative_improving")
        & matrix["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ].iloc[0]
    assert combo["accepted_trade_count"] == 1
    assert combo["avg_revenue_latest_yoy_delta_1m_pct_points"] == 45.0
    tampered = matrix.astype(str).copy()
    tampered.loc[0, "approved_for_daily"] = "True"
    assert any("approved_for_daily" in error for error in validate_price_pullback(tampered))


def test_price_pullback_promotion_matrix_keeps_research_decisions_separated() -> None:
    exit_rule_id = "close_prev20_high_break_next_open"
    lifecycle = pd.DataFrame(
        [
            {
                "condition_test_id": "baseline_replay",
                "exit_rule_id": exit_rule_id,
                "condition_rule": "production proxy replay only",
                "data_status": "available_point_in_time_research_frame",
                "anomaly_exclusion_basis": PRIMARY_ANOMALY_BASIS,
                "unresolved_data_quality_candidate_count_in_sample": 1,
                "unresolved_data_quality_candidate_count_in_baseline": 1,
                "unresolved_data_quality_candidate_ids": "fixture_candidate",
                "formal_price_rule_status": "close_confirmed_candidate",
                "entry_rule_id": "signal_date_next_open",
                "source_mature_signal_stock_days": 1000,
                "accepted_trade_count": 200,
                "accepted_avg_trades_per_research_day": 8.0,
                "accepted_trade_share_of_baseline_pct": 100.0,
                "win_rate_pct": 20.0,
                "neutral_rate_pct": 30.0,
                "failure_rate_pct": 50.0,
                "avg_realized_return_pct": 1.0,
                "median_realized_return_pct": 0.5,
            },
            {
                "condition_test_id": "v1_gate_return20_tdcc_high_obv",
                "exit_rule_id": exit_rule_id,
                "condition_rule": "return20_0_25 plus TDCC high thresholds up plus OBV above MA20",
                "data_status": "available_point_in_time_research_frame",
                "anomaly_exclusion_basis": PRIMARY_ANOMALY_BASIS,
                "unresolved_data_quality_candidate_count_in_sample": 1,
                "unresolved_data_quality_candidate_count_in_baseline": 1,
                "unresolved_data_quality_candidate_ids": "fixture_candidate",
                "formal_price_rule_status": "close_confirmed_candidate",
                "entry_rule_id": "signal_date_next_open",
                "source_mature_signal_stock_days": 100,
                "accepted_trade_count": 80,
                "accepted_avg_trades_per_research_day": 3.0,
                "accepted_trade_share_of_baseline_pct": 40.0,
                "win_rate_pct": 35.0,
                "neutral_rate_pct": 30.0,
                "failure_rate_pct": 35.0,
                "avg_realized_return_pct": 3.0,
                "median_realized_return_pct": 2.0,
            },
        ]
    )
    ordered = pd.DataFrame(
        [
            {
                "condition_test_id": condition_id,
                "exit_rule_id": exit_rule_id,
                "condition_rule": f"rule for {condition_id}",
                "data_status": "available_point_in_time_research_frame",
                "anomaly_exclusion_basis": PRIMARY_ANOMALY_BASIS,
                "unresolved_data_quality_candidate_count_in_sample": 1,
                "unresolved_data_quality_candidate_count_in_baseline": 1,
                "unresolved_data_quality_candidate_ids": "fixture_candidate",
                "formal_price_rule_status": "close_confirmed_candidate",
                "entry_rule_id": "signal_date_next_open",
                "mature_count": 50,
                "accepted_trade_count": 50,
                "win_rate_pct": 30.0,
                "neutral_rate_pct": 30.0,
                "failure_rate_pct": 40.0,
                "avg_realized_return_pct": 2.0,
                "median_realized_return_pct": 1.0,
            }
            for condition_id in [
                "return20_0_25",
                "tdcc_high_thresholds_up",
                "obv_above_ma20",
                "macd_kd_confirm",
                "pattern45_bull_pullback",
                "research_score_ge6",
                "theme_context_mainstream_supported",
            ]
        ]
    )
    high_return = pd.DataFrame(
        [
            {
                "score_bucket": score_bucket,
                "exit_rule_id": exit_rule_id,
                "anomaly_exclusion_basis": PRIMARY_ANOMALY_BASIS,
                "score_rule_summary": "score rule",
                "formal_price_rule_status": "close_confirmed_candidate",
                "unresolved_data_quality_candidate_count_in_bucket": 1,
                "unresolved_data_quality_candidate_count_in_baseline": 1,
                "unresolved_data_quality_candidate_ids": "fixture_candidate",
                "entry_rule_id": "signal_date_next_open",
                "source_mature_signal_stock_days": 40,
                "accepted_trade_count": 40,
                "win_rate_pct": 40.0,
                "neutral_rate_pct": 20.0,
                "failure_rate_pct": 40.0,
                "avg_realized_return_pct": 5.0,
                "median_realized_return_pct": 4.0,
                "high_return_10_rate_pct": 30.0,
                "loss_5_rate_pct": 20.0,
            }
            for score_bucket in ["all_scores", "score_ge_2", "score_ge_3", "score_ge_5"]
        ]
    )
    revenue = pd.DataFrame(
        [
            {
                "condition_test_id": condition_id,
                "anomaly_exclusion_basis": PRIMARY_ANOMALY_BASIS,
                "condition_rule": f"revenue rule for {condition_id}",
                "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
                "revenue_or_price_anomaly_candidate_count_in_sample": 1,
                "revenue_or_price_anomaly_candidate_count_in_baseline": 1,
                "formal_price_rule_status": "close_confirmed_candidate",
                "entry_rule_id": "signal_date_next_open",
                "source_mature_signal_stock_days": 30,
                "accepted_trade_count": 30,
                "accepted_avg_trades_per_research_day": 1.0,
                "win_rate_pct": 40.0,
                "neutral_rate_pct": 20.0,
                "failure_rate_pct": 40.0,
                "avg_realized_return_pct": 4.0,
                "median_realized_return_pct": 3.0,
                "high_return_10_rate_pct": 30.0,
                "loss_5_rate_pct": 20.0,
            }
            for condition_id in [
                "base_v1_without_revenue_gate",
                "latest30_and_cumulative20",
                "latest_revenue_yoy_ge50",
                "latest_yoy_delta_ge20",
                "latest_yoy_turn_positive_after_2_negative",
                "revenue_negative_both_risk",
            ]
        ]
    )

    matrix = build_price_pullback_promotion_matrix(lifecycle, ordered, high_return, revenue)

    assert not matrix.empty
    assert validate_promotion_matrix(matrix.astype(str)) == []
    assert matrix["approved_for_daily"].eq(False).all()
    assert matrix["production_change"].eq("none").all()
    roles = dict(zip(matrix["promotion_candidate_id"], matrix["proposed_contract_role"]))
    assert roles["base_package:v1_gate_return20_tdcc_high_obv"] == "base_model_candidate_required_gate_package"
    assert roles["revenue_package:latest30_and_cumulative20"] == "strong_add_score_package_candidate_not_required_gate"
    assert roles["revenue_reject:latest_yoy_turn_positive_after_2_negative"] == "reject_as_required_gate_or_add_score"
    assert roles["score_component:volume_red_or_solid_red_risk"] == "risk_tag_candidate_review"
    assert roles["deferred_context:theme_leadership"] == "defer_until_mature_point_in_time_theme_samples"

    tampered = matrix.astype(str).copy()
    tampered.loc[tampered["promotion_candidate_id"].eq("base_package:v1_gate_return20_tdcc_high_obv"), "exit_rule_id"] = (
        "close_prev20_break_then_tp10_or_5ma_next_open"
    )
    assert any("approved close-confirmed prev20 breakout" in error for error in validate_promotion_matrix(tampered))
    tampered_anomaly = matrix.astype(str).copy()
    tampered_anomaly.loc[
        tampered_anomaly["promotion_candidate_id"].eq("base_package:v1_gate_return20_tdcc_high_obv"),
        "anomaly_exclusion_basis",
    ] = ANOMALY_CANDIDATE_SENSITIVITY_BASIS
    assert any("primary basis" in error for error in validate_promotion_matrix(tampered_anomaly))


def test_revenue_unreacted_range_revenue_matrix_stays_advisory_without_operation_contract() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2317"],
            "date": ["20260101", "20260101"],
            "close": [100.0, 100.0],
            "range_low_23d_prev": [95.0, 95.0],
            "range_high_23d_prev": [105.0, 105.0],
            "volume_ratio_prev20": [1.0, 1.0],
            "range_breakout_20d_pct": [0.0, 0.0],
            "volume_ma20_lots": [100.0, 100.0],
            "bullish_attack_candle": [False, False],
            "locked_limit_up_breakout": [False, False],
            "return_5d_pct": [1.0, 1.0],
            "return_20d_pct": [5.0, 5.0],
            "full_monthly_revenue_context_ready": [True, True],
            "full_monthly_revenue_latest_yoy_pct": [60.0, -5.0],
            "full_monthly_revenue_cumulative_yoy_pct": [30.0, -2.0],
            "full_monthly_revenue_positive_flag": [True, False],
            "full_monthly_revenue_strong_flag": [True, False],
            "full_monthly_revenue_positive_or_strong": [True, False],
            "full_monthly_revenue_numerical_anomaly_flag": [False, False],
            "next_open_to_d20_close_return_pct": [8.0, -3.0],
        }
    )

    matrix = build_revenue_unreacted_range_revenue_condition_matrix(df)

    assert not matrix.empty
    assert validate_revenue_unreacted(matrix.astype(str)) == []
    assert matrix["approved_for_daily"].eq(False).all()
    assert matrix["production_change"].eq("none").all()
    strong = matrix[
        matrix["condition_test_id"].eq("revenue_production_strong")
        & matrix["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ].iloc[0]
    assert strong["formal_price_rule_status"] == "research_only_no_formal_operation_contract"
    assert strong["operation_basis"] == "research_only_d20_close_not_operation_contract"
    assert strong["accepted_trade_count"] == 1
    assert strong["win_rate_pct"] == 100.0
    assert strong["promotion_readiness"] == "blocked_operation_rule_and_model_specific_promotion_pr_required"


def test_revenue_unreacted_range_operation_candidate_matrix_is_research_only_non_overlap() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2330", "2317"],
            "date": ["20260101", "20260102", "20260101"],
            "close": [100.0, 101.0, 80.0],
            "range_low_23d_prev": [95.0, 95.0, 75.0],
            "range_high_23d_prev": [105.0, 105.0, 85.0],
            "range_width_23d_pct": [10.0, 10.0, 12.0],
            "distance_to_range_high_23d_pct": [-4.8, -3.8, -5.9],
            "close_position_120d_pct": [50.0, 52.0, 40.0],
            "volume_ratio_prev20": [1.0, 1.0, 1.0],
            "range_breakout_20d_pct": [0.0, 0.0, 0.0],
            "volume_ma20_lots": [100.0, 100.0, 100.0],
            "bullish_attack_candle": [False, False, False],
            "locked_limit_up_breakout": [False, False, False],
            "return_5d_pct": [1.0, 1.0, 1.0],
            "return_20d_pct": [5.0, 5.0, 5.0],
            "next_open": [100.0, 101.0, 80.0],
            "close_above_ma20": [True, True, True],
            "close_above_ema23": [True, True, True],
            "high_thresholds_up": [True, True, False],
            "full_monthly_revenue_context_ready": [True, True, True],
            "full_monthly_revenue_latest_yoy_pct": [60.0, 70.0, 80.0],
            "full_monthly_revenue_cumulative_yoy_pct": [30.0, 35.0, 40.0],
            "full_monthly_revenue_prev1_latest_yoy_pct": [50.0, 55.0, 70.0],
            "full_monthly_revenue_prev2_latest_yoy_pct": [40.0, 50.0, 60.0],
            "full_monthly_revenue_prev1_cumulative_yoy_pct": [25.0, 30.0, 35.0],
            "full_monthly_revenue_prev2_cumulative_yoy_pct": [20.0, 25.0, 30.0],
            "full_monthly_revenue_positive_flag": [True, True, True],
            "full_monthly_revenue_strong_flag": [True, True, True],
            "full_monthly_revenue_positive_or_strong": [True, True, True],
            "full_monthly_revenue_numerical_anomaly_flag": [False, False, False],
        }
    )
    for day in range(1, 21):
        df[f"next_open_to_d{day}_day_close_return_pct"] = [6.0, 7.0, 8.0]
        df[f"future_d{day}_ma20"] = [90.0, 91.0, 72.0]
        df[f"future_d{day}_ema23"] = [92.0, 93.0, 74.0]
    for day in range(2, 22):
        df[f"future_d{day}_open"] = [100.0, 101.0, 80.0]
    df["next_open_to_d10_close_return_pct"] = [6.0, 7.0, 8.0]
    df["next_open_to_d20_close_return_pct"] = [6.0, 7.0, 8.0]

    matrix = build_revenue_unreacted_range_operation_candidate_matrix(df)

    assert not matrix.empty
    assert validate_revenue_operation_candidate_matrix(matrix.astype(str)) == []
    assert matrix["approved_for_daily"].eq(False).all()
    assert matrix["production_change"].eq("none").all()
    strong = matrix[
        matrix["condition_test_id"].eq("revenue_production_strong")
        & matrix["exit_rule_id"].eq("d10_close_no_stop")
        & matrix["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ].iloc[0]
    assert strong["operation_basis"] == "research_only_close_confirmed_operation_candidate"
    assert strong["accepted_trade_count"] == 2
    assert strong["suppressed_signal_count"] == 1
    assert strong["same_stock_overlap_pair_count"] == 0
    assert strong["win_rate_pct"] == 100.0
    assert strong["promotion_readiness"] == "research_only_operation_candidate_not_promotion_ready"


def test_revenue_unreacted_feature_contrast_recomputes_success_and_failure_features_without_overlap() -> None:
    df = pd.DataFrame(
        {
            "stock_id": ["2330", "2330", "2317", "2454", "3008"],
            "stock_name": ["台積電", "台積電", "鴻海", "聯發科", "大立光"],
            "market": ["TWSE"] * 5,
            "date": ["20260101", "20260102", "20260101", "20260101", "20260101"],
            "close": [100.0, 101.0, 80.0, 90.0, 120.0],
            "range_low_23d_prev": [95.0, 95.0, 75.0, 85.0, 115.0],
            "range_high_23d_prev": [105.0, 105.0, 85.0, 95.0, 125.0],
            "range_width_23d_pct": [10.0, 10.0, 12.0, 11.0, 9.0],
            "distance_to_range_high_23d_pct": [-4.8, -3.8, -5.9, -5.3, -4.0],
            "close_position_120d_pct": [50.0, 52.0, 40.0, 65.0, 35.0],
            "volume_ratio_prev20": [1.0, 1.0, 1.2, 1.4, 1.1],
            "range_breakout_20d_pct": [0.0] * 5,
            "volume_ma20_lots": [100.0] * 5,
            "bullish_attack_candle": [True, True, False, True, False],
            "solid_red_candle": [True, True, False, True, False],
            "locked_limit_up_breakout": [False] * 5,
            "return_5d_pct": [1.0, 2.0, -1.0, 3.0, 0.0],
            "return_20d_pct": [5.0, 6.0, -2.0, 10.0, 1.0],
            "next_open": [100.0, 101.0, 80.0, 90.0, 120.0],
            "close_above_ma20": [True, True, False, True, True],
            "close_above_ema23": [True, True, False, True, True],
            "high_thresholds_up": [True, True, False, True, False],
            "all_thresholds_up": [True, True, False, False, False],
            "four_thresholds_sync_up": [True, True, False, False, False],
            "tdcc_history_available": [True] * 5,
            "tdcc_consecutive_up_weeks": [2.0, 2.0, 0.0, 1.0, 0.0],
            "macd_hist": [1.0, 1.2, -0.5, 0.4, -0.1],
            "rsi14": [65.0, 68.0, 42.0, 58.0, 50.0],
            "k_value": [70.0, 72.0, 35.0, 60.0, 50.0],
            "d_value": [60.0, 62.0, 40.0, 55.0, 52.0],
            "kd_bullish_not_overheated": [True, True, False, True, False],
            "bb_width_pct": [12.0, 13.0, 20.0, 15.0, 10.0],
            "bb_width_not_extreme": [True, True, False, True, True],
            "ema23_slope_5d_pct": [2.0, 2.1, -1.0, 1.0, 0.5],
            "distance_to_ema23_pct": [3.0, 3.5, -2.0, 2.0, 1.0],
            "obv_above_ma20": [True, True, False, True, False],
            "ma20": [98.0, 99.0, 82.0, 88.0, 118.0],
            "ma60": [95.0, 96.0, 85.0, 87.0, 119.0],
            "full_monthly_revenue_context_ready": [True] * 5,
            "full_monthly_revenue_period": ["202512"] * 5,
            "full_monthly_revenue_source_table_date": ["20260110"] * 5,
            "full_monthly_revenue_data_status": ["ready"] * 5,
            "full_monthly_revenue_latest_yoy_pct": [60.0, 70.0, 40.0, 80.0, 100.0],
            "full_monthly_revenue_cumulative_yoy_pct": [30.0, 35.0, 25.0, 40.0, 50.0],
            "full_monthly_revenue_prev1_latest_yoy_pct": [40.0, 50.0, 45.0, 60.0, 80.0],
            "full_monthly_revenue_prev2_latest_yoy_pct": [30.0, 40.0, 50.0, 50.0, 70.0],
            "full_monthly_revenue_prev1_cumulative_yoy_pct": [20.0, 25.0, 30.0, 30.0, 40.0],
            "full_monthly_revenue_prev2_cumulative_yoy_pct": [15.0, 20.0, 35.0, 20.0, 30.0],
            "full_monthly_revenue_latest_yoy_delta_1m_pct_points": [20.0] * 5,
            "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points": [10.0] * 5,
            "full_monthly_revenue_positive_flag": [True] * 5,
            "full_monthly_revenue_strong_flag": [True] * 5,
            "full_monthly_revenue_positive_or_strong": [True] * 5,
            "full_monthly_revenue_numerical_anomaly_flag": [False, False, False, False, True],
        }
    )
    for day in range(1, 21):
        df[f"next_open_to_d{day}_day_close_return_pct"] = [12.0, 20.0, -4.0, 6.0, 1.0]

    summary, detail, anomaly = build_revenue_unreacted_range_feature_contrast_audit(
        df,
        market_history=pd.DataFrame(),
    )

    assert validate_revenue_feature_contrast(
        summary.astype(str),
        detail.astype(str),
        anomaly.astype(str),
    ) == []
    decision = summary[
        summary["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)
    ]
    baseline = decision[decision["row_type"].eq("baseline")].iloc[0]
    assert baseline["accepted_trade_count"] == 4
    assert baseline["unresolved_anomaly_candidate_count_in_source"] == 1
    assert baseline["same_stock_overlap_pair_count"] == 0
    sensitivity_baseline = summary[
        summary["anomaly_exclusion_basis"].eq(ANOMALY_CANDIDATE_SENSITIVITY_BASIS)
        & summary["row_type"].eq("baseline")
    ].iloc[0]
    assert sensitivity_baseline["accepted_trade_count"] == 3
    macd = decision[decision["feature_id"].eq("technical_macd_hist_gt0")].iloc[0]
    assert macd["high_return_feature_hit_rate_pct"] == 100.0
    assert macd["failure_feature_hit_rate_pct"] == 0.0
    assert macd["win_rate_pct"] == 100.0
    assert macd["evidence_interpretation"] == "positive_discriminator_single_feature_candidate"
    tdcc_four = decision[decision["feature_id"].eq("tdcc_four_thresholds_sync_up")].iloc[0]
    assert tdcc_four["feature_independence_status"] == "duplicate_mask_not_independent_evidence"
    assert tdcc_four["equivalent_to_feature_id"] == "tdcc_all_thresholds_up"
    assert set(summary["combination_policy"]) == {
        "single_features_only_in_this_audit_no_arbitrary_condition_stacking"
    }


def test_revenue_future_close_path_audit_separates_discontinuity_from_continuous_large_return() -> None:
    frame = pd.DataFrame(index=["discontinuous", "continuous"])
    discontinuous = [0.0, 100.0] + [100.0] * 18
    continuous = [10.0 * day for day in range(1, 21)]
    for day in range(1, 21):
        frame[f"next_open_to_d{day}_day_close_return_pct"] = [
            discontinuous[day - 1],
            continuous[day - 1],
        ]

    audited = _revenue_future_close_path_audit(frame)

    assert bool(audited.loc["discontinuous", "future_close_discontinuity_flag"]) is True
    assert audited.loc["discontinuous", "future_close_discontinuity_reason"] == "upward_close_discontinuity_ge_1_5x"
    assert bool(audited.loc["continuous", "future_close_discontinuity_flag"]) is False
    assert audited.loc["continuous", "future_close_discontinuity_reason"] == "none"


def test_revenue_market_mapping_covers_listed_and_otc_source_labels() -> None:
    assert _revenue_benchmark_index("listed") == "TWSE"
    assert _revenue_benchmark_index("TWSE") == "TWSE"
    assert _revenue_benchmark_index("otc") == "TPEX"
    assert _revenue_benchmark_index("TPEX") == "TPEX"


def test_revenue_feature_context_anomaly_candidate_mask_checks_lagged_values_and_deltas() -> None:
    frame = pd.DataFrame(
        {
            "full_monthly_revenue_numerical_anomaly_flag": [False, False, False],
            "full_monthly_revenue_latest_yoy_pct": [50.0, 50.0, 50.0],
            "full_monthly_revenue_cumulative_yoy_pct": [30.0, 30.0, 30.0],
            "full_monthly_revenue_prev1_latest_yoy_pct": [40.0, 800.0, 40.0],
            "full_monthly_revenue_prev2_latest_yoy_pct": [30.0, 30.0, 30.0],
            "full_monthly_revenue_prev3_latest_yoy_pct": [20.0, 20.0, 20.0],
            "full_monthly_revenue_prev1_cumulative_yoy_pct": [25.0, 25.0, 25.0],
            "full_monthly_revenue_prev2_cumulative_yoy_pct": [20.0, 20.0, 20.0],
            "full_monthly_revenue_prev3_cumulative_yoy_pct": [15.0, 15.0, 15.0],
            "full_monthly_revenue_latest_yoy_delta_1m_pct_points": [10.0, -750.0, 400.0],
            "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points": [5.0, 5.0, 5.0],
        }
    )

    assert _revenue_feature_context_anomaly_candidate_mask(frame).tolist() == [False, True, True]


def test_revenue_unreacted_active_attack_proxy_is_behaviorally_isolated_from_legacy_name() -> None:
    frame = pd.DataFrame(
        {
            "volume_ratio_prev20": [1.0, 2.1, 3.0, 1.0],
            "range_breakout_20d_pct": [0.0, 2.5, 0.0, 0.0],
            "volume_ma20_lots": [2000.0, 2000.0, 2000.0, 2000.0],
            "bullish_attack_candle": [False, True, False, False],
            "locked_limit_up_breakout": [False, False, False, False],
            "return_5d_pct": [0.0, 0.0, 0.0, 9.0],
            "return_20d_pct": [0.0, 0.0, 0.0, 0.0],
        }
    )

    assert revenue_unreacted_active_attack_proxy(frame).tolist() == active_price_attack_proxy(frame).tolist()


def test_revenue_close_confirmation_timing_replays_three_variants_without_overlap() -> None:
    rows: list[dict[str, object]] = []
    source_positions = {
        "2330": {0, 1, 2, 25},
        "2317": {0, 10, 30},
    }
    for stock_id, base_close in (("2330", 100.0), ("2317", 80.0)):
        for position in range(50):
            close = base_close + (position % 4) - 1.0
            rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_id,
                    "market": "TWSE",
                    "date": f"2026{position // 28 + 1:02d}{position % 28 + 1:02d}",
                    "open": close,
                    "close": close,
                    "ma20": base_close - 0.5,
                    "ema23": base_close - 0.25,
                    "_revenue_signal_date": f"2026{position // 28 + 1:02d}{position % 28 + 1:02d}",
                    "_revenue_stock_sequence_index": position,
                    "_revenue_range23_highest_close_prev": base_close + 1.5,
                    "_revenue_timing_source_flag": position in source_positions[stock_id],
                    "_revenue_timing_source_anomaly_candidate_flag": False,
                    "full_monthly_revenue_period": "202512",
                    "full_monthly_revenue_source_table_date": "20260101",
                    "full_monthly_revenue_latest_yoy_pct": 60.0,
                    "full_monthly_revenue_cumulative_yoy_pct": 30.0,
                }
            )
    prepared = pd.DataFrame(rows)
    summary, detail, anomaly = build_close_confirmation_timing_audit(
        prepared,
        expected_control={"basis_source_signal_count": 7, "accepted_trade_count": 3},
    )

    assert validate_revenue_close_confirmation_timing(
        summary.astype(str),
        detail.astype(str),
        anomaly.astype(str),
    ) == []
    generated_at = str(summary["generated_at"].iloc[0])
    assert validate_revenue_close_confirmation_timing(
        summary.astype(str),
        detail.astype(str),
        anomaly.astype(str),
        f"- generated_at: `{generated_at}`",
    ) == []
    assert "markdown generated_at must match" in " ".join(
        validate_revenue_close_confirmation_timing(
            summary.astype(str),
            detail.astype(str),
            anomaly.astype(str),
            "- generated_at: `stale-run`",
        )
    )
    decision = summary[summary["anomaly_exclusion_basis"].eq(REVENUE_TIMING_DECISION_BASIS)]
    assert set(decision[decision["row_type"].eq("variant_performance")]["confirmation_variant_name_zh"]) == {
        "隔日續強確認型",
        "區間突破確認型",
        "均線站回確認型",
    }
    assert decision[decision["row_type"].isin({"control_baseline", "variant_performance"})][
        "same_stock_overlap_pair_count"
    ].eq(0).all()
    assert decision[decision["row_type"].eq("source_partition")]["partition_count"].sum() == 7
    included = detail[detail["metric_included"].astype(bool)]
    assert (included["confirmation_sequence_index"].astype(int) < included["entry_sequence_index"].astype(int)).all()
    assert included["known_before_entry_open"].astype(bool).all()

    tampered = summary.astype(str).copy()
    partition_index = tampered[tampered["row_type"].eq("source_partition")].index[0]
    tampered.loc[partition_index, "partition_count"] = "999"
    assert any(
        "source partition does not cover all source signals" in error
        for error in validate_revenue_close_confirmation_timing(tampered, detail.astype(str), anomaly.astype(str))
    )


def test_revenue_fixed_confirmation_feature_contrast_separates_signal_and_confirmation_context() -> None:
    rows: list[dict[str, object]] = []
    dates = pd.date_range("2026-01-01", periods=35, freq="B").strftime("%Y%m%d").tolist()
    for stock_id, base_close, winner in (("2330", 100.0, True), ("2317", 80.0, False)):
        for position, date in enumerate(dates):
            close = base_close
            if position == 1:
                close = base_close + 2.0
            elif position >= 2:
                close = base_close + 3.0
            if position == 21:
                close = 115.0 if winner else 72.0
            open_price = base_close if position < 2 else (103.0 if winner else 83.0)
            macd = 1.0 if winner or position == 0 else -1.0
            market_regime = "mild_bull" if winner or position == 0 else "high_risk"
            rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_id,
                    "market": "TWSE",
                    "date": date,
                    "open": open_price,
                    "close": close,
                    "previous_close": base_close,
                    "ma20": base_close - 1.0,
                    "ma60": base_close - (2.0 if winner else 0.5),
                    "ema23": base_close - 0.5,
                    "_revenue_signal_date": date,
                    "_revenue_stock_sequence_index": position,
                    "_revenue_range23_highest_close_prev": base_close + 1.0,
                    "_revenue_timing_source_flag": position == 0,
                    "_revenue_timing_source_anomaly_candidate_flag": False,
                    "range_width_23d_pct": 10.0 if winner else 20.0,
                    "distance_to_range_high_23d_pct": -1.0,
                    "close_position_120d_pct": 60.0 if winner else 85.0,
                    "return_5d_pct": 4.0 if winner else -2.0,
                    "return_20d_pct": 10.0 if winner else -5.0,
                    "volume_ratio_prev20": 1.2,
                    "bullish_attack_candle": winner,
                    "solid_red_candle": winner,
                    "macd_hist": macd,
                    "rsi14": 65.0 if winner else 42.0,
                    "k_value": 70.0 if winner else 35.0,
                    "d_value": 60.0 if winner else 45.0,
                    "kd_bullish_not_overheated": winner,
                    "bb_width_pct": 12.0,
                    "bb_width_not_extreme": True,
                    "ema23_slope_5d_pct": 2.0 if winner else -1.0,
                    "distance_to_ema23_pct": 2.0,
                    "obv": 120.0 if winner else 80.0,
                    "obv_ma20": 100.0,
                    "obv_above_ma20": winner,
                    "tdcc_history_available": True,
                    "tdcc_as_of_date": "20251226",
                    "tdcc_consecutive_up_weeks": 2.0 if winner else 0.0,
                    "high_thresholds_up": winner,
                    "all_thresholds_up": winner,
                    "four_thresholds_sync_up": winner,
                    "full_monthly_revenue_context_ready": True,
                    "full_monthly_revenue_period": "202512",
                    "full_monthly_revenue_source_table_date": "20251231",
                    "full_monthly_revenue_latest_yoy_pct": 80.0 if winner else 40.0,
                    "full_monthly_revenue_cumulative_yoy_pct": 40.0 if winner else 25.0,
                    "full_monthly_revenue_prev1_latest_yoy_pct": 50.0 if winner else 45.0,
                    "full_monthly_revenue_prev2_latest_yoy_pct": 30.0 if winner else 50.0,
                    "full_monthly_revenue_prev3_latest_yoy_pct": 20.0,
                    "full_monthly_revenue_prev1_cumulative_yoy_pct": 30.0 if winner else 30.0,
                    "full_monthly_revenue_prev2_cumulative_yoy_pct": 20.0 if winner else 35.0,
                    "full_monthly_revenue_prev3_cumulative_yoy_pct": 15.0,
                    "full_monthly_revenue_latest_yoy_delta_1m_pct_points": 30.0 if winner else -5.0,
                    "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points": 10.0 if winner else -5.0,
                    "full_monthly_revenue_numerical_anomaly_flag": bool(
                        not winner and position >= 1
                    ),
                    "benchmark_index": "TWSE",
                    "signal_market_regime": market_regime,
                }
            )
    prepared = pd.DataFrame(rows)
    timing_summary, _, _ = build_close_confirmation_timing_audit(prepared)
    summary, detail, anomaly = build_fixed_confirmation_feature_contrast(
        prepared,
        timing_summary,
        binary_specs=REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
        numeric_specs=REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
    )

    assert validate_revenue_fixed_feature_contrast(
        summary.astype(str),
        detail.astype(str),
        anomaly.astype(str),
        timing_summary.astype(str),
    ) == []
    decision = summary[summary["anomaly_exclusion_basis"].eq(REVENUE_TIMING_DECISION_BASIS)]
    baselines = decision[decision["row_type"].eq("baseline")]
    assert set(baselines["feature_time_basis"]) == {"signal_date_close", "confirmation_date_close"}
    assert baselines["accepted_trade_count"].eq(2).all()
    assert baselines["same_stock_overlap_pair_count"].eq(0).all()
    assert baselines["same_stock_revenue_period_repeat_count"].eq(0).all()
    signal_macd = decision[
        decision["feature_time_basis"].eq("signal_date_close")
        & decision["feature_id"].eq("technical_macd_hist_gt0")
    ].iloc[0]
    confirmation_macd = decision[
        decision["feature_time_basis"].eq("confirmation_date_close")
        & decision["feature_id"].eq("technical_macd_hist_gt0")
    ].iloc[0]
    assert signal_macd["feature_hit_count"] == 2
    assert confirmation_macd["feature_hit_count"] == 1
    assert confirmation_macd["win_rate_pct"] == 100.0
    close_above_ma_rows = decision[
        decision["feature_id"].eq("technical_close_above_ma20_ema23")
    ]
    assert set(close_above_ma_rows["feature_time_basis"]) == {
        "signal_date_close",
        "confirmation_date_close",
    }
    assert close_above_ma_rows["feature_hit_count"].eq(2).all()
    revenue_feature = decision[
        decision["feature_id"].eq("revenue_latest30_and_cumulative20")
    ].set_index("feature_time_basis")
    assert revenue_feature.loc["signal_date_close", "feature_observed_count"] == 2
    assert revenue_feature.loc["confirmation_date_close", "feature_observed_count"] == 2
    assert revenue_feature.loc["confirmation_date_close", "feature_hit_count"] == 2
    revenue_numeric = decision[
        decision["feature_id"].eq("revenue_latest_yoy_pct")
    ].set_index("feature_time_basis")
    assert revenue_numeric.loc["signal_date_close", "failure_feature_value_count"] == 1
    assert revenue_numeric.loc["confirmation_date_close", "failure_feature_value_count"] == 1
    source_sensitivity = summary[
        summary["anomaly_exclusion_basis"].eq(REVENUE_TIMING_SOURCE_SENSITIVITY_BASIS)
    ]
    return_sensitivity = summary[
        summary["anomaly_exclusion_basis"].eq(RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS)
    ]
    assert not source_sensitivity.empty
    assert not return_sensitivity.empty


def test_research_workflow_routes_revenue_feature_contrast_through_model_owned_producer() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(encoding="utf-8")

    assert "python scripts/build_revenue_unreacted_range_research.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_feature_contrast_audit.py" in workflow
    assert "git add output/latest/research_backtest/revenue_unreacted_range_* || true" in workflow
    assert "git add output/history/research/revenue_unreacted_range_* || true" in workflow
    assert "git add docs/latest/revenue_unreacted_range_* || true" in workflow


def test_research_workflow_has_opt_in_revenue_projection_chain_stage_mode() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(encoding="utf-8")
    input_contract = (
        "      run_revenue_unreacted_range_source_snapshot_projection_chain_only:\n"
        "        description: \"When revenue research is selected, rebuild only its "
        "downstream chain from the pinned 20260713 source snapshot projection\"\n"
        "        required: false\n"
        "        default: \"false\""
    )
    stage_command = (
        "python scripts/build_revenue_unreacted_range_research.py "
        "--stage source_snapshot_projection_chain"
    )
    stage_start = workflow.index(stage_command)
    full_branch = workflow.index("          else", stage_start)
    stage_branch = workflow[stage_start:full_branch]

    assert input_contract in workflow
    assert stage_command in workflow
    assert "python scripts/build_revenue_unreacted_range_research.py\n" in workflow
    source_snapshot_validator = (
        "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py"
    )
    lag_validator = (
        "python scripts/validate_revenue_unreacted_range_lag_strength_matrix.py"
    )
    launch_validator = (
        "python scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py"
    )
    forward_validator = (
        "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py"
    )
    assert lag_validator in stage_branch
    assert launch_validator in stage_branch
    assert forward_validator in stage_branch
    assert stage_branch.index(source_snapshot_validator) < stage_branch.index(lag_validator)
    assert stage_branch.index(lag_validator) < stage_branch.index(launch_validator)
    assert stage_branch.index(launch_validator) < stage_branch.index(forward_validator)
    assert stage_branch.index(forward_validator) < stage_branch.index(
        "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py"
    )


def test_research_workflow_validates_revenue_close_confirmation_timing_artifacts() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(encoding="utf-8")

    assert "python scripts/validate_revenue_unreacted_range_close_confirmation_timing_audit.py" in workflow
    assert "run_revenue_unreacted_range_research" in workflow
    assert "git add output/history/research/ || true" not in workflow


def test_research_workflow_validates_revenue_fixed_confirmation_and_lag_artifacts() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(encoding="utf-8")

    assert "python scripts/validate_revenue_unreacted_range_fixed_confirmation_feature_contrast.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_extreme_return_path_audit.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_lag_strength_matrix.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py" in workflow
    assert "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py" in workflow
    assert (
        "python scripts/validate_revenue_unreacted_range_promotion_preparation.py "
        "--require-source-artifacts"
    ) not in workflow


def test_research_workflow_does_not_refresh_formal_adapters_or_snapshots() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(encoding="utf-8")

    for forbidden in (
        "python scripts/build_daily_w_bottom_operation_sections.py",
        "python scripts/build_daily_price_pullback_23ema_operation_section.py",
        "python scripts/build_model_operation_readiness.py",
        "python scripts/update_daily_published_model_snapshots.py",
        "git add output/history/daily_model_snapshots/",
    ):
        assert forbidden not in workflow


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
