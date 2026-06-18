from __future__ import annotations

import ast
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_candidate_model_layer as model_layer  # noqa: E402
from build_daily_candidate_model_layer import (  # noqa: E402
    MODEL_SCORE_PROFILES,
    VOLUME_RANGE_BREAKOUT_MAIN_CONDITIONS_ZH,
    annotate_frontpage_uniqueness,
    attach_model_recommendations,
    attach_same_model_repeat,
    build_parameter_table,
    build_frontpage_unique,
    build_report_ready_model_signals,
    build_signals,
    build_specs,
    cond_neckline_challenge,
    cond_platform_strength,
    cond_pullback,
    cond_revenue_unreacted,
    cond_tdcc_stealth,
    cond_volume_breakout,
    cond_w_bottom_right,
    report_bucket,
    score_pullback,
    score_volume_breakout,
    update_model_signal_log,
)
from audit_daily_candidate_model_selection_correctness import model_stock_key_set  # noqa: E402


def make_row(**overrides: object) -> pd.Series:
    base: dict[str, object] = {
        "stock_id": "9999",
        "stock_name": "TEST",
        "volume_ratio": "2.0",
        "volume_breakout_type": "bottom_volume_attack",
        "selection_status": "selected",
        "volume_breakout_priority": "A_bottom_volume_attack",
        "close": "103",
        "open": "100",
        "high": "104",
        "low": "95",
        "previous_close": "99",
        "previous_20d_high": "100",
        "volume_ma20": "2000",
        "close_above_range_high": "False",
        "distance_23ema_pct": "1.5",
        "ema23_slope_pct": "0.5",
        "return_20d": "5",
        "tdcc_judgement": "mild_accumulation",
        "warrant_flow_signal": "no_signal",
        "structural_theme_bucket": "",
        "theme_structural_status": "",
    }
    base.update(overrides)
    return pd.Series(base)


class DailyCandidateModelLayerTest(unittest.TestCase):
    def test_required_models_are_parameterized(self) -> None:
        model_ids = set(build_parameter_table(build_specs())["model_id"])
        self.assertTrue(
            {
                "volume_range_breakout",
                "price_pullback_23ema",
                "revenue_unreacted_range",
                "w_bottom_right_side",
                "near_high_neckline_challenge",
                "platform_strengthening",
                "pullback_short_reclaim",
                "tdcc_stealth_accumulation",
                "tdcc_short_term_continuation_d5_d10",
                "short_term_surge_d5_d10",
                "group_fund_rotation",
                "explosive_volume_red_candle",
                "five_day_20pct_precursor",
                "disposition_attention_event_tag",
                "msci_event_tag",
            }.issubset(model_ids)
        )

    def test_parameter_table_keeps_pdf_research_and_event_layers_separate(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        self.assertEqual(params.loc["volume_range_breakout", "pdf_visibility"], "pdf_core_model")
        self.assertEqual(params.loc["tdcc_short_term_continuation_d5_d10", "pdf_visibility"], "pdf_core_model")
        self.assertEqual(params.loc["short_term_surge_d5_d10", "pdf_visibility"], "research_only_not_pdf_core")
        self.assertEqual(params.loc["explosive_volume_red_candle", "pdf_visibility"], "research_only_not_pdf_core")
        self.assertEqual(params.loc["disposition_attention_event_tag", "pdf_visibility"], "pdf_risk_tag_only")

    def test_formal_pdf_models_do_not_keep_legacy_common_scoring(self) -> None:
        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        source = source_path.read_text(encoding="utf-8")

        self.assertNotIn("def model_score_common(", source)
        self.assertNotIn('"legacy_common"', source)

    def test_pdf_core_models_have_independent_condition_and_score_functions(self) -> None:
        specs = [spec for spec in build_specs() if spec.pdf_visibility == "pdf_core_model"]
        condition_names = [spec.condition_func.__name__ for spec in specs]
        score_names = [spec.score_func.__name__ for spec in specs]
        self.assertEqual(len(condition_names), len(set(condition_names)))
        self.assertEqual(len(score_names), len(set(score_names)))
        self.assertNotIn("model_score_common", score_names)
        self.assertEqual(
            {spec.model_id for spec in specs},
            {
                "volume_range_breakout",
                "price_pullback_23ema",
                "hot_theme_pullback",
                "revenue_unreacted_range",
                "w_bottom_right_side",
                "near_high_neckline_challenge",
                "platform_strengthening",
                "pullback_short_reclaim",
                "tdcc_stealth_accumulation",
            },
        )

    def test_pdf_core_models_do_not_call_each_other_conditions_or_scores(self) -> None:
        specs = [spec for spec in build_specs() if spec.pdf_visibility == "pdf_core_model"]
        condition_by_func = {spec.condition_func.__name__: spec.model_id for spec in specs}
        score_by_func = {spec.score_func.__name__: spec.model_id for spec in specs}
        all_condition_funcs = set(condition_by_func)
        all_score_funcs = set(score_by_func)

        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        funcs = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}

        cross_condition_calls: list[str] = []
        for func_name, model_id in condition_by_func.items():
            for node in ast.walk(funcs[func_name]):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    callee = node.func.id
                    if callee in condition_by_func and callee != func_name:
                        cross_condition_calls.append(f"{model_id}:{func_name}->{callee}")
                    if callee in all_score_funcs:
                        cross_condition_calls.append(f"{model_id}:{func_name}->{callee}")

        cross_score_calls: list[str] = []
        for func_name, model_id in score_by_func.items():
            for node in ast.walk(funcs[func_name]):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    callee = node.func.id
                    if callee in all_score_funcs and callee != func_name:
                        cross_score_calls.append(f"{model_id}:{func_name}->{callee}")
                    if callee in all_condition_funcs:
                        cross_score_calls.append(f"{model_id}:{func_name}->{callee}")

        self.assertEqual(cross_condition_calls, [])
        self.assertEqual(cross_score_calls, [])

    def test_pdf_facing_helpers_are_not_duplicated(self) -> None:
        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        names = [
            node.name
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name
            in {
                "same_model_repeat_status_zh",
                "same_model_repeat_note_zh",
                "apply_display_columns",
                "attach_report_contract_columns",
            }
        ]
        for name in set(names):
            self.assertEqual(names.count(name), 1, name)

    def test_model_score_profiles_are_independent_and_visible(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        self.assertEqual(params.loc["volume_range_breakout", "score_profile_id"], "volume_range_breakout")
        self.assertEqual(params.loc["price_pullback_23ema", "score_profile_id"], "price_pullback_23ema")
        self.assertEqual(params.loc["tdcc_stealth_accumulation", "score_profile_id"], "tdcc_stealth_accumulation")
        self.assertNotEqual(
            params.loc["volume_range_breakout", "volume_ratio_bonus_per_1x"],
            params.loc["price_pullback_23ema", "volume_ratio_bonus_per_1x"],
        )
        self.assertNotEqual(
            params.loc["tdcc_stealth_accumulation", "tdcc_positive_bonus"],
            params.loc["volume_range_breakout", "tdcc_positive_bonus"],
        )
        self.assertNotIn("legacy_common", MODEL_SCORE_PROFILES)

    def test_pdf_models_use_next_open_entry_basis(self) -> None:
        params = build_parameter_table(build_specs())
        pdf_rows = params[params["pdf_visibility"].isin(["pdf_core_model", "pdf_specialty_section"])]
        self.assertTrue((pdf_rows["entry_basis"] == "signal_date_next_open").all())

    def test_volume_breakout_main_condition_text_includes_locked_limit_bypass(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        condition_text = params.loc["volume_range_breakout", "main_conditions"]

        self.assertEqual(condition_text, VOLUME_RANGE_BREAKOUT_MAIN_CONDITIONS_ZH)
        self.assertIn("一般放量突破", condition_text)
        self.assertIn("量比 >= 2.0", condition_text)
        self.assertIn("鎖量漲停突破不要求量比或20日均量", condition_text)

    def test_volume_breakout_condition_is_bottom_volume_attack_not_60d_only(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="103",
            open="100",
            previous_close="99",
            previous_20d_high="100",
            volume_ratio="2.2",
            volume_ma20="2000",
            distance_to_previous_60d_high_pct="-8",
        )
        self.assertTrue(cond_volume_breakout(row))

    def test_locked_limit_up_low_volume_ratio_is_volume_breakout(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="81.8",
            open="81.8",
            high="81.8",
            low="81.8",
            previous_close="74.4",
            previous_20d_high="74.4",
            volume_ratio="0.504",
            volume_ma20="7099858.7",
        )

        score, components, _risks = score_volume_breakout(row)

        self.assertTrue(cond_volume_breakout(row))
        self.assertGreater(score, 0)
        self.assertTrue(any("locked_limit_up_breakout" in item for item in components))

    def test_locked_limit_up_does_not_require_volume_fields(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="81.8",
            open="81.8",
            high="81.8",
            low="81.8",
            previous_close="74.4",
            previous_20d_high="74.4",
            volume_ratio="",
            volume_ma20="",
        )

        self.assertTrue(cond_volume_breakout(row))

    def test_locked_limit_up_signal_row_uses_current_condition_text(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="81.8",
            open="81.8",
            high="81.8",
            low="81.8",
            previous_close="74.4",
            previous_20d_high="74.4",
            volume_ratio="0.504",
            volume_ma20="7099858.7",
        )

        out = build_signals(pd.DataFrame([row]), build_specs(), "20260612")
        volume_row = out[out["model_id"].eq("volume_range_breakout")].iloc[0]

        self.assertEqual(volume_row["model_main_conditions"], VOLUME_RANGE_BREAKOUT_MAIN_CONDITIONS_ZH)
        self.assertIn("鎖量漲停突破不要求量比或20日均量", volume_row["model_main_conditions"])

    def test_locked_limit_up_watch_row_uses_return_when_previous_close_missing(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="207",
            open="207",
            high="207",
            low="207",
            return_1d="9.8143",
            previous_20d_high="192",
            volume_ratio="0.43",
            volume_ma20="5956813.95",
        )

        self.assertTrue(cond_volume_breakout(row))

    def test_non_locked_low_volume_ratio_breakout_is_not_volume_breakout(self) -> None:
        row = make_row(
            close="110",
            open="101",
            high="110",
            low="99",
            previous_close="98",
            previous_20d_high="100",
            volume_ratio="1.5",
            volume_ma20="2000",
        )

        self.assertFalse(cond_volume_breakout(row))

    def test_dedicated_volume_breakout_table_is_independent_from_candidate_model(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "1617",
                    "stock_name": "榮星",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_score": "88",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_breakout_notes": "close_ge_prior20_high_102pct|volume_ratio_ge_2|volume_ma20_lots_ge_1000|bullish_candle",
                    "volume_ratio": "3.17",
                    "return_5d": "7.0",
                    "return_20d": "6.3",
                    "next_volume_breakout_confirmation": "confirm close above MA20/EMA23",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_path = Path(tmpdir) / "volume_breakout_watch_latest.csv"
            source.to_csv(temp_path, index=False, encoding="utf-8-sig")
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            try:
                out = model_layer.append_volume_breakout_signals(pd.DataFrame(), pd.DataFrame(), "20260530")
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path

        self.assertEqual(len(out), 1)
        row = out.iloc[0]
        self.assertEqual(row["stock_id"], "1617")
        self.assertEqual(row["model_id"], "volume_range_breakout")
        self.assertIn("operation_score", row.index)
        self.assertIn("tdcc_score", row.index)
        self.assertIn("pattern_score", row.index)
        self.assertIn("risk_penalty", row.index)
        self.assertIn("final_rank_score", row.index)
        self.assertEqual(float(row["model_score"]), float(row["final_rank_score"]))
        self.assertEqual(row["model_name_zh"], "放量攻擊模型")
        self.assertNotIn("底部", row["model_name_zh"])

    def test_pullback_model_does_not_require_breakout(self) -> None:
        row = make_row(
            volume_breakout_type="",
            close_above_range_high="False",
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.3",
        )
        self.assertTrue(cond_pullback(row))

    def test_pre_breakout_models_exclude_confirmed_breakouts(self) -> None:
        breakout = make_row(
            category="true_breakout",
            volume_breakout_type="bottom_volume_attack",
            platform_breakout_flag="True",
            neckline_breakout_flag="True",
            volume_confirmed_breakout="True",
            close_above_range_high="True",
            distance_to_previous_high_pct="1.0",
            platform_base_flag="True",
            platform_width_pct="10",
            volume_ratio="3.5",
            previous_20d_high="100",
            volume_ma20="2000",
            ema23_slope_pct="0.5",
            close="105",
            open="100",
        )
        self.assertFalse(cond_neckline_challenge(breakout))
        self.assertFalse(cond_platform_strength(breakout))
        self.assertTrue(cond_volume_breakout(breakout))

    def test_platform_strengthening_is_platform_inside_not_breakout(self) -> None:
        row = make_row(
            category="range_rebound",
            volume_breakout_type="",
            platform_breakout_flag="False",
            neckline_breakout_flag="False",
            volume_confirmed_breakout="False",
            close_above_range_high="False",
            platform_base_flag="True",
            platform_width_pct="9",
            platform_high="105",
            close="103",
            open="100",
            volume_ratio="1.8",
        )
        self.assertTrue(cond_platform_strength(row))

    def test_w_bottom_requires_double_bottom_geometry_not_generic_pattern_flag(self) -> None:
        broad_flag = make_row(
            category="range_rebound",
            w_bottom_flag="True",
            w_bottom_right_side_flag="True",
            pattern_stage="neckline_challenge",
            second_low_gap_pct="",
            distance_to_neckline_pct="",
        )
        self.assertFalse(cond_w_bottom_right(broad_flag))

        generic_platform = make_row(
            category="pattern",
            w_bottom_flag="True",
            w_bottom_right_side_flag="True",
            pattern_stage="platform_right_side",
            second_low_gap_pct="",
            distance_to_neckline_pct="",
        )
        self.assertFalse(cond_w_bottom_right(generic_platform))

        clean_w = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            w_bottom_flag="",
            w_bottom_right_side_flag="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
            red_body_ratio_2_vs_1="1.2",
        )
        self.assertTrue(cond_w_bottom_right(clean_w))

        higher_position_clean_w = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="58",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
            red_body_ratio_2_vs_1="1.2",
        )
        self.assertTrue(cond_w_bottom_right(higher_position_clean_w))

        slight_undercut = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="-0.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(slight_undercut))

        right_low_too_high = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="12.0",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(right_low_too_high))

        weak_second_attack = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.8",
            red_body_ratio_2_vs_1="2.0",
        )
        self.assertTrue(cond_w_bottom_right(weak_second_attack))

        high_level_pullback = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="62",
            w_bottom_base_width_pct="18",
            return_20d_pct="42",
            distance_to_previous_60d_high_pct="-0.5",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(high_level_pullback))

        no_base_context = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="",
            w_bottom_base_width_pct="",
            platform_width_pct="",
            short_platform_width_pct="",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(no_base_context))

        already_broken = make_row(
            category="pattern",
            pattern_stage="breakout_confirmed",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="1.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(already_broken))

        range_rebound_with_detected_w = make_row(
            stock_id="1618",
            category="range_rebound",
            pattern_stage="neckline_challenge",
            signal_date="20260529",
            volume_breakout_type="",
            close_above_range_high="",
        )
        self.assertTrue(cond_w_bottom_right(range_rebound_with_detected_w))

    def test_risk_penalty_does_not_cancel_model_entry(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            volume_ratio="2.2",
            tdcc_judgement="distribution_warning",
            return_20d="85",
        )
        score, _components, risks = score_volume_breakout(row)
        self.assertTrue(cond_volume_breakout(row))
        self.assertTrue(any(str(risk).startswith("tdcc_distribution_penalty") for risk in risks))
        self.assertFalse(any(str(risk).startswith("false_breakout_risk_penalty") for risk in risks))

    def test_same_stock_can_enter_multiple_models(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            volume_ratio="2.0",
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.8",
        )
        self.assertTrue(cond_volume_breakout(row))
        self.assertTrue(cond_pullback(row))

    def test_tdcc_stealth_excludes_late_and_overheated_phases(self) -> None:
        base = make_row(
            volume_ratio="1.0",
            volume_breakout_type="",
            tdcc_price_phase="tdcc_leading_price",
            return_20d="5",
            close="100",
            high_20="105",
            low_20="95",
        )
        self.assertTrue(cond_tdcc_stealth(base))
        late = base.copy()
        late["tdcc_price_phase"] = "price_leading_tdcc"
        overheated = base.copy()
        overheated["tdcc_price_phase"] = "overheated_after_tdcc"
        self.assertFalse(cond_tdcc_stealth(late))
        self.assertFalse(cond_tdcc_stealth(overheated))

    def test_active_volume_attack_is_not_stealth_or_unreacted_story(self) -> None:
        row = make_row(
            volume_ratio="3.98",
            volume_breakout_type="",
            volume_confirmed_breakout="True",
            latest_revenue_yoy="93",
            cumulative_yoy_pct="16",
            return_5d="8.18",
            return_20d="17.22",
            close="58.2",
            open="55.4",
            previous_close="53",
            previous_20d_high="55",
            volume_ma20="2000",
            high_20="59.8",
            low_20="49",
            tdcc_price_phase="tdcc_leading_price",
        )
        self.assertTrue(cond_volume_breakout(row))
        self.assertFalse(cond_revenue_unreacted(row))
        self.assertFalse(cond_tdcc_stealth(row))

    def test_model_signal_log_replaces_current_date_snapshot(self) -> None:
        current = pd.DataFrame(
            [
                {
                    "signal_date": "20260531",
                    "report_bucket": "mainstream",
                    "stock_id": "3046",
                    "stock_name": "建碁",
                    "model_id": "volume_range_breakout",
                    "model_name_zh": "放量攻擊模型",
                    "model_group": "pdf_core_model",
                    "model_score": "75.9",
                    "model_rank": "1",
                }
            ]
        )
        old_history = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "3046",
                    "stock_name": "建碁",
                    "model_id": "price_pullback_23ema",
                },
                {
                    "signal_date": "20260531",
                    "report_bucket": "mainstream",
                    "stock_id": "3046",
                    "stock_name": "建碁",
                    "model_id": "tdcc_stealth_accumulation",
                },
            ]
        )
        original_dir = model_layer.MODEL_HISTORY_DIR
        original_csv = model_layer.MODEL_SIGNAL_LOG_CSV
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_csv = temp_dir / "daily_candidate_model_signal_log.csv"
            old_history.to_csv(temp_csv, index=False, encoding="utf-8-sig")
            model_layer.MODEL_HISTORY_DIR = temp_dir
            model_layer.MODEL_SIGNAL_LOG_CSV = temp_csv
            try:
                out = update_model_signal_log(current)
            finally:
                model_layer.MODEL_HISTORY_DIR = original_dir
                model_layer.MODEL_SIGNAL_LOG_CSV = original_csv

        current_day = out[out["signal_date"].astype(str).eq("20260531")]
        self.assertEqual(set(current_day["model_id"]), {"volume_range_breakout"})
        self.assertIn("price_pullback_23ema", set(out["model_id"]))

    def test_mainstream_bucket_does_not_change_score(self) -> None:
        mainstream = make_row(
            structural_theme_bucket="ai_server_ipc_theme",
            theme_structural_status="core_mainstream_theme",
        )
        non_mainstream = make_row(
            structural_theme_bucket="traditional_textile_theme",
            theme_structural_status="non_mainstream_theme",
        )
        self.assertEqual(score_pullback(mainstream)[0], score_pullback(non_mainstream)[0])
        self.assertEqual(report_bucket(mainstream), "mainstream")
        self.assertEqual(report_bucket(non_mainstream), "non_mainstream")

    def test_model_recommendations_are_attached_to_signals(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "model_id": "tdcc_short_term_continuation_d5_d10",
                    "stock_id": "9999",
                    "model_score": 80,
                }
            ]
        )
        recs = pd.DataFrame(
            [
                {
                    "model_id": "tdcc_short_term_continuation_d5_d10",
                    "recommended_usage": "promote_to_pdf_core",
                    "recommended_close_exit_horizon": "D+10",
                    "best_close_win_rate_pct": "76.71",
                    "best_avg_close_return_pct": "15.56",
                    "recommended_high_exit_horizon": "D+10",
                    "best_avg_high_return_pct": "21.3",
                    "best_high_5pct_hit_rate_pct": "70.0",
                    "recommended_sample_size": "161",
                    "recommended_unique_stocks": "107",
                    "recommended_sample_status": "ok_first_pass",
                    "model_revision_note": "Promote to specialty table.",
                }
            ]
        )
        out = attach_model_recommendations(signals, recs)
        self.assertEqual(out.loc[0, "recommended_usage"], "promote_to_pdf_core")
        self.assertEqual(out.loc[0, "recommended_close_exit_horizon"], "D+10")
        self.assertEqual(out.loc[0, "best_close_win_rate_pct"], "76.71")

    def test_model_signals_dedupe_same_stock_same_model_bucket(self) -> None:
        rows = [
            make_row(
                source_row_index="a",
                stock_id="9999",
                category="range_rebound",
                score="10",
                report_line_memberships="mainstream",
                mainstream_report_eligible="True",
            ),
            make_row(
                source_row_index="b",
                stock_id="9999",
                category="pattern",
                score="99",
                report_line_memberships="mainstream",
                mainstream_report_eligible="True",
            ),
        ]
        out = build_signals(pd.DataFrame(rows), build_specs(), "20260530")
        dup_count = out.duplicated(["model_id", "report_bucket", "stock_id"]).sum()
        self.assertEqual(dup_count, 0)

    def test_audit_core_completeness_ignores_presentation_bucket(self) -> None:
        expected = pd.DataFrame(
            [{"report_bucket": "non_mainstream", "model_id": "price_pullback_23ema", "stock_id": "1503"}]
        )
        actual = pd.DataFrame(
            [{"report_bucket": "mainstream", "model_id": "price_pullback_23ema", "stock_id": "1503"}]
        )
        self.assertEqual(model_stock_key_set(expected), model_stock_key_set(actual))

    def test_report_ready_signals_merge_same_display_model_same_stock(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "CANON",
                    "model_id": "volume_breakout_range",
                    "model_name_zh": "放量攻擊模型",
                    "model_score": "80",
                    "model_rank": "2",
                    "original_category": "range_rebound",
                    "source_row_index": "46",
                    "next_confirmation": "A",
                    "score_components": "volume",
                    "risk_penalty_tags": "",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "CANON",
                    "model_id": "volume_range_breakout",
                    "model_name_zh": "放量攻擊模型",
                    "model_score": "90",
                    "model_rank": "1",
                    "original_category": "revenue_pullback",
                    "source_row_index": "175",
                    "next_confirmation": "B",
                    "score_components": "range",
                    "risk_penalty_tags": "risk_a",
                },
            ]
        )
        out = build_report_ready_model_signals(signals)
        self.assertEqual(len(out), 1)
        row = out.iloc[0]
        self.assertEqual(row["model_id"], "volume_range_breakout")
        self.assertEqual(row["model_rank"], 1)
        self.assertEqual(row["merged_same_model_source_count"], 2)
        self.assertIn("volume_breakout_range", row["merged_model_ids"])
        self.assertIn("volume_range_breakout", row["merged_model_ids"])
        self.assertIn("range_rebound", row["merged_source_categories"])
        self.assertIn("revenue_pullback", row["merged_source_categories"])

    def test_frontpage_unique_keeps_one_row_per_stock_but_preserves_model_hits(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "佳能",
                    "model_id": "range_rebound",
                    "model_name_zh": "區間內轉強",
                    "model_group": "pdf_core_model",
                    "model_score": "82",
                    "model_rank": "1",
                    "effective_primary_theme": "機器人",
                    "risk_penalty_tags": "repeated_but_no_breakout",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "佳能",
                    "model_id": "revenue_unreacted_range",
                    "model_name_zh": "營收爆發尚未反應",
                    "model_group": "pdf_core_model",
                    "model_score": "70",
                    "model_rank": "3",
                    "effective_primary_theme": "機器人",
                    "risk_penalty_tags": "needs_eps_confirmation",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "9999",
                    "stock_name": "測試股",
                    "model_id": "range_rebound",
                    "model_name_zh": "區間內轉強",
                    "model_group": "pdf_core_model",
                    "model_score": "75",
                    "model_rank": "2",
                    "effective_primary_theme": "測試族群",
                    "risk_penalty_tags": "",
                },
            ]
        )
        annotated = annotate_frontpage_uniqueness(signals)
        canons = annotated[annotated["stock_id"] == "2374"]
        self.assertEqual((canons["frontpage_display_allowed"] == "True").sum(), 1)
        self.assertEqual((canons["frontpage_duplicate_reason"] == "duplicate_stock_already_shown_on_frontpage").sum(), 1)

        frontpage = build_frontpage_unique(annotated)
        self.assertEqual((frontpage["stock_id"] == "2374").sum(), 1)
        row = frontpage[frontpage["stock_id"] == "2374"].iloc[0]
        self.assertEqual(row["model_hit_count"], 2)
        self.assertIn("區間內轉強", row["model_hits"])
        self.assertIn("營收爆發尚未反應", row["model_hits"])

    def test_same_model_repeat_is_separate_and_frontpage_prefers_new_signals(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2347",
                    "stock_name": "OLD",
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔",
                    "model_group": "pdf_core_model",
                    "model_score": "99",
                    "model_rank": "1",
                    "effective_primary_theme": "AI",
                    "risk_penalty_tags": "",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "9999",
                    "stock_name": "NEW",
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔",
                    "model_group": "pdf_core_model",
                    "model_score": "70",
                    "model_rank": "2",
                    "effective_primary_theme": "AI",
                    "risk_penalty_tags": "",
                },
            ]
        )
        model_log = pd.DataFrame(
            [
                {"signal_date": "20260529", "report_bucket": "mainstream", "stock_id": "2347", "model_id": "price_pullback_23ema"},
                {"signal_date": "20260530", "report_bucket": "mainstream", "stock_id": "2347", "model_id": "price_pullback_23ema"},
                {"signal_date": "20260530", "report_bucket": "mainstream", "stock_id": "9999", "model_id": "price_pullback_23ema"},
            ]
        )

        annotated, repeat = attach_same_model_repeat(signals, model_log)
        old = annotated[annotated["stock_id"] == "2347"].iloc[0]
        new = annotated[annotated["stock_id"] == "9999"].iloc[0]
        self.assertEqual(old["same_model_consecutive_days"], 2)
        self.assertEqual(old["same_model_repeat_status"], "repeated_same_model_signal")
        self.assertEqual(new["same_model_repeat_status"], "new_model_signal")
        self.assertEqual(len(repeat), 1)
        self.assertEqual(repeat.iloc[0]["stock_id"], "2347")

        annotated = annotate_frontpage_uniqueness(annotated)
        frontpage = build_frontpage_unique(annotated)
        self.assertEqual(frontpage.iloc[0]["stock_id"], "9999")
        self.assertNotIn("2347", set(frontpage["stock_id"].astype(str)))
        repeat_reason = annotated.loc[annotated["stock_id"].eq("2347"), "frontpage_duplicate_reason"].iloc[0]
        self.assertEqual(repeat_reason, "same_model_repeat_moved_to_persistence_table")

    def test_dual_report_membership_expands_without_score_change(self) -> None:
        row = make_row(
            stock_id="1303",
            report_line_memberships="mainstream,non_mainstream",
            mainstream_report_eligible="True",
            non_mainstream_report_eligible="True",
            dual_report_membership_flag="True",
        )
        out = build_signals(pd.DataFrame([row]), build_specs(), "20260530")
        model_rows = out[out["model_id"] == "volume_range_breakout"]
        self.assertEqual(set(model_rows["report_bucket"]), {"mainstream", "non_mainstream"})
        self.assertEqual(model_rows["model_score"].nunique(), 1)

    def test_output_has_effective_theme_fields_and_clean_guidance(self) -> None:
        row = make_row(
            stock_id="9998",
            next_confirmation="依D+5/D+10統計與短線支撐管理",
            effective_primary_theme="機器人自動化",
            structural_theme_bucket="robotics_automation_theme",
            mainstream_report_eligible="True",
        )
        out = build_signals(pd.DataFrame([row]), build_specs(), "20260530")
        self.assertIn("effective_primary_theme", out.columns)
        self.assertIn("effective_structural_theme_bucket", out.columns)
        self.assertIn("model_operation_guidance", out.columns)
        self.assertFalse(out["next_confirmation"].astype(str).str.contains(r"\?\?\?", regex=True).any())

    def test_report_ready_pdf_facing_columns_are_human_readable(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "佳能",
                    "model_id": "volume_breakout_range",
                    "model_name_zh": "volume_breakout_range",
                    "model_score": "80",
                    "model_rank": "2",
                    "original_category": "range_rebound",
                    "source_row_index": "46",
                    "next_confirmation": "call_strong_inflow / neckline",
                    "score_components": "volume_ratio=2.0|tdcc_status=strong_accumulation",
                    "risk_penalty_tags": "false_breakout_risk",
                    "tdcc_status": "strong_accumulation",
                    "warrant_flow_signal": "call_strong_inflow",
                }
            ]
        )
        report_ready = model_layer.attach_report_contract_columns(
            model_layer.build_report_ready_model_signals(signals)
        )
        self.assertEqual(model_layer.RISK_TAG_ZH["false_breakout_risk"], "漲幅過低")
        self.assertEqual(model_layer.RISK_TAG_ZH["false_breakout_risk_penalty"], "漲幅過低扣分")
        self.assertIn("漲幅過低", report_ready["risk_tags_zh"].iloc[0])
        self.assertNotIn("假突破風險", report_ready["risk_tags_zh"].iloc[0])
        for col in [
            "model_name_zh",
            "source_hit_labels_zh",
            "why_selected_zh",
            "why_selected_human_zh",
            "risk_tags_zh",
            "next_confirmation_zh",
            "recommended_usage_zh",
            "warrant_flow_signal_zh",
        ]:
            self.assertIn(col, report_ready.columns)
            text = " ".join(report_ready[col].astype(str))
            self.assertNotRegex(text, r"\?\?\?|[a-z]+(?:_[a-z0-9]+){1,}")
        self.assertIn("放量攻擊", report_ready["model_name_zh"].iloc[0])


    def test_rotation_theme_resolver_maps_known_raw_market_terms(self) -> None:
        for raw in ["ASIC", "DRAM IC", "DRAM/Flash", "MLCC", "MOSFET", "PCB", "optoelectronics"]:
            resolved = model_layer.resolve_rotation_theme(raw)
            self.assertEqual(resolved["theme_resolution_status"], "resolved")
            self.assertTrue(model_layer.has_cjk_text(resolved["theme_display_zh"]))

        unresolved = model_layer.resolve_rotation_theme("其他")
        self.assertEqual(unresolved["theme_resolution_status"], "unresolved")


    def test_group_rotation_outputs_pdf_safe_theme_display(self) -> None:
        taxonomy = pd.DataFrame(
            [
                {
                    "stock_id": "9103",
                    "stock_name": "美德醫療-DR",
                    "industry": "91",
                    "basic_theme": "91",
                    "primary_theme": "DR_or_foreign_listing",
                    "secondary_themes": "",
                },
                {
                    "stock_id": "9105",
                    "stock_name": "泰金寶-DR",
                    "industry": "91",
                    "basic_theme": "91",
                    "primary_theme": "DR_or_foreign_listing",
                    "secondary_themes": "",
                },
                {
                    "stock_id": "9136",
                    "stock_name": "巨騰-DR",
                    "industry": "91",
                    "basic_theme": "91",
                    "primary_theme": "DR_or_foreign_listing",
                    "secondary_themes": "",
                },
            ]
        )
        dates = pd.date_range("2026-04-01", periods=40, freq="B").strftime("%Y%m%d")
        history = pd.DataFrame(
            {
                "date": dates,
                "close": [100 + i for i in range(40)],
                "volume": [100] * 39 + [400],
                "volume_ma20": [100] * 40,
            }
        )

        original_path = model_layer.STOCK_THEME_TAXONOMY
        original_price_history = model_layer.price_history_for_stock
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_csv = Path(tmpdir) / "taxonomy.csv"
            taxonomy.to_csv(temp_csv, index=False, encoding="utf-8-sig")
            try:
                model_layer.STOCK_THEME_TAXONOMY = temp_csv
                model_layer.price_history_for_stock = lambda stock_id: history.copy()
                rotation = model_layer.build_rotation(pd.DataFrame(), dates[-1])
            finally:
                model_layer.STOCK_THEME_TAXONOMY = original_path
                model_layer.price_history_for_stock = original_price_history

        self.assertFalse(rotation.empty)
        self.assertIn("theme_display_zh", rotation.columns)
        self.assertIn("theme_resolution_status", rotation.columns)
        self.assertIn("theme_key", rotation.columns)
        self.assertEqual(set(rotation["theme"]), {"DR / 外國上市"})
        self.assertEqual(set(rotation["theme_display_zh"]), {"DR / 外國上市"})
        self.assertEqual(set(rotation["theme_resolution_status"]), {"resolved"})
        self.assertTrue(rotation["theme_key"].str.contains("DR_or_foreign_listing").any())
        self.assertFalse(rotation["theme"].str.contains(r"^\\d+$|DR_or_foreign_listing|其他", regex=True).any())


if __name__ == "__main__":
    unittest.main()
