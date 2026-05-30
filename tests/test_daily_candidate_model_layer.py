from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_daily_candidate_model_layer import (  # noqa: E402
    attach_model_recommendations,
    build_parameter_table,
    build_signals,
    build_specs,
    cond_pullback,
    cond_tdcc_stealth,
    cond_volume_breakout,
    model_score_common,
    report_bucket,
)


def make_row(**overrides: object) -> pd.Series:
    base: dict[str, object] = {
        "stock_id": "9999",
        "stock_name": "TEST",
        "volume_ratio": "2.0",
        "volume_breakout_type": "range_breakout_volume",
        "close_above_range_high": "True",
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
        self.assertEqual(params.loc["tdcc_short_term_continuation_d5_d10", "pdf_visibility"], "pdf_specialty_section")
        self.assertEqual(params.loc["explosive_volume_red_candle", "pdf_visibility"], "research_only_not_pdf_core")
        self.assertEqual(params.loc["disposition_attention_event_tag", "pdf_visibility"], "pdf_risk_tag_only")

    def test_pdf_models_use_next_open_entry_basis(self) -> None:
        params = build_parameter_table(build_specs())
        pdf_rows = params[params["pdf_visibility"].isin(["pdf_core_model", "pdf_specialty_section"])]
        self.assertTrue((pdf_rows["entry_basis"] == "signal_date_next_open").all())

    def test_volume_breakout_condition_is_range_breakout_not_60d_only(self) -> None:
        row = make_row(
            volume_breakout_type="range_breakout_volume",
            close_above_range_high="True",
            distance_to_previous_60d_high_pct="-8",
        )
        self.assertTrue(cond_volume_breakout(row))

    def test_pullback_model_does_not_require_breakout(self) -> None:
        row = make_row(
            volume_breakout_type="",
            close_above_range_high="False",
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.3",
        )
        self.assertTrue(cond_pullback(row))

    def test_risk_penalty_does_not_cancel_model_entry(self) -> None:
        row = make_row(
            volume_breakout_type="range_breakout_volume",
            close_above_range_high="True",
            volume_ratio="2.2",
            tdcc_judgement="distribution_warning",
            false_breakout_risk="True",
            return_20d="85",
        )
        score, _components, risks = model_score_common(row)
        self.assertTrue(cond_volume_breakout(row))
        self.assertLess(score, 70)
        self.assertIn("tdcc_distribution_penalty", risks)
        self.assertIn("false_breakout_risk_penalty", risks)

    def test_same_stock_can_enter_multiple_models(self) -> None:
        row = make_row(
            volume_breakout_type="range_breakout_volume",
            close_above_range_high="True",
            volume_ratio="2.0",
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.8",
        )
        self.assertTrue(cond_volume_breakout(row))
        self.assertTrue(cond_pullback(row))

    def test_tdcc_stealth_excludes_late_and_overheated_phases(self) -> None:
        base = make_row(
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

    def test_mainstream_bucket_does_not_change_score(self) -> None:
        mainstream = make_row(
            structural_theme_bucket="ai_server_ipc_theme",
            theme_structural_status="core_mainstream_theme",
        )
        non_mainstream = make_row(
            structural_theme_bucket="traditional_textile_theme",
            theme_structural_status="non_mainstream_theme",
        )
        self.assertEqual(model_score_common(mainstream)[0], model_score_common(non_mainstream)[0])
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
                decision_score="10",
                report_line_memberships="mainstream",
                mainstream_report_eligible="True",
            ),
            make_row(
                source_row_index="b",
                stock_id="9999",
                category="pattern",
                decision_score="99",
                report_line_memberships="mainstream",
                mainstream_report_eligible="True",
            ),
        ]
        out = build_signals(pd.DataFrame(rows), build_specs(), "20260530")
        dup_count = out.duplicated(["model_id", "report_bucket", "stock_id"]).sum()
        self.assertEqual(dup_count, 0)

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
            next_confirmation="???????????????????? D+5/D+10 ???",
            effective_primary_theme="機器人自動化",
            structural_theme_bucket="robotics_automation_theme",
            mainstream_report_eligible="True",
        )
        out = build_signals(pd.DataFrame([row]), build_specs(), "20260530")
        self.assertIn("effective_primary_theme", out.columns)
        self.assertIn("effective_structural_theme_bucket", out.columns)
        self.assertIn("model_operation_guidance", out.columns)
        self.assertFalse(out["next_confirmation"].astype(str).str.contains(r"\?\?\?", regex=True).any())


if __name__ == "__main__":
    unittest.main()
