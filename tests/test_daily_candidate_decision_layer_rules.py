from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_daily_candidate_decision_layer import evaluate_row  # noqa: E402


def make_row(**overrides: object) -> pd.Series:
    base: dict[str, object] = {
        "stock_id": "9999",
        "stock_name": "測試股",
        "category": "revenue_breakout_low_response",
        "category_cn": "營收爆發低反應股",
        "score": "100",
        "pattern_stage": "",
        "volume_ratio": "1.0",
        "return_5d": "1",
        "return_20d": "3",
        "distance_to_ma20_pct": "1",
        "distance_to_previous_60d_high_pct": "-5",
        "repeat_appear_label": "",
        "warrant_flow_signal": "no_signal",
        "fundamental_catalyst_tags": "",
        "revenue_good_eps_unconfirmed_flag": "",
        "tdcc_judgement": "strong_accumulation",
        "revaluation_priority": "A_優先追蹤",
        "structural_theme_bucket": "ai_server_ipc_theme",
        "theme_structural_status": "core_mainstream_theme",
        "theme_mainstream_label": "core_mainstream_supported",
    }
    base.update(overrides)
    return pd.Series(base)


class DailyCandidateDecisionLayerRuleTest(unittest.TestCase):
    def test_revenue_low_response_repeat_no_warrant_no_breakout_is_not_repeat_penalty(self) -> None:
        result = evaluate_row(
            make_row(
                repeat_appear_label="stale_signal",
                warrant_flow_signal="no_signal",
                revenue_good_eps_unconfirmed_flag="",
            )
        )
        self.assertNotIn("stale_no_warrant_no_breakout", result["downgrade_flags"])
        self.assertNotIn("revenue_no_warrant_stale_no_breakout", result["downgrade_flags"])
        self.assertNotIn("反覆上榜", result["why_downgraded"])

    def test_revenue_low_response_with_true_breakout(self) -> None:
        result = evaluate_row(
            make_row(
                repeat_appear_label="stale_signal",
                warrant_flow_signal="no_signal",
                revenue_good_eps_unconfirmed_flag="True",
                true_breakout="True",
                pattern_stage="breakout_confirmed",
            )
        )
        self.assertEqual(result["decision_priority"], "A_priority_watch")
        self.assertNotIn("stale_no_warrant_no_breakout", result["downgrade_flags"])

    def test_revenue_low_response_with_call_strong_inflow(self) -> None:
        result = evaluate_row(
            make_row(
                warrant_flow_signal="call_strong_inflow",
                revenue_good_eps_unconfirmed_flag="True",
            )
        )
        self.assertIn(result["decision_priority"], {"A_priority_watch", "B_confirm_needed"})
        self.assertNotIn("revenue_eps_unconfirmed_no_attack", result["downgrade_flags"])

    def test_stale_signal_but_breakout_confirmed(self) -> None:
        result = evaluate_row(
            make_row(
                category="range_rebound",
                category_cn="區間內轉強 / 挑戰前高觀察",
                repeat_appear_label="stale_signal",
                warrant_flow_signal="no_signal",
                pattern_stage="platform_breakout",
                platform_breakout_flag="True",
                volume_ratio="1.8",
            )
        )
        self.assertIn(result["decision_priority"], {"A_priority_watch", "B_confirm_needed"})
        self.assertNotIn("stale_no_warrant_no_breakout", result["downgrade_flags"])

    def test_stale_signal_no_breakout_no_warrant_does_not_cap_priority(self) -> None:
        result = evaluate_row(
            make_row(
                category="range_rebound",
                category_cn="區間內轉強 / 挑戰前高觀察",
                repeat_appear_label="stale_signal",
                warrant_flow_signal="no_signal",
                distance_to_previous_60d_high_pct="-4",
            )
        )
        self.assertNotIn("stale_no_warrant_no_breakout", result["downgrade_flags"])
        self.assertNotIn("反覆上榜", result["why_downgraded"])

    def test_non_mainstream_is_display_group_not_score_cap(self) -> None:
        result = evaluate_row(
            make_row(
                category="true_breakout",
                pattern_stage="breakout_confirmed",
                true_breakout="True",
                volume_ratio="2.0",
                structural_theme_bucket="",
                theme_structural_status="non_mainstream_theme",
                theme_mainstream_label="non_mainstream_flow_active",
            )
        )
        self.assertEqual(result["decision_priority"], "A_priority_watch")
        self.assertEqual(result["risk_handling_bucket"], "normal")
        self.assertEqual(result["theme_group"], "non_mainstream")
        self.assertEqual(result["display_section"], "non_mainstream_selected_priority")
        self.assertNotIn("non_ai_non_mainstream_cap", result["downgrade_flags"])

    def test_missing_taxonomy_is_unknown_not_non_mainstream(self) -> None:
        result = evaluate_row(
            make_row(
                structural_theme_bucket="",
                theme_structural_status="",
                theme_mainstream_label="",
                candidate_line_group="",
            )
        )
        self.assertEqual(result["theme_group"], "theme_unknown")

    def test_selected_risk_rows_are_ranked_not_no_buy_vetoed(self) -> None:
        result = evaluate_row(
            make_row(
                category="true_breakout",
                pattern_stage="breakout_confirmed",
                true_breakout="True",
                volume_ratio="2.2",
                tdcc_judgement="distribution_warning",
                return_20d="85",
                already_priced_in="True",
            )
        )
        self.assertIn(result["decision_priority"], {"A_priority_watch", "B_confirm_needed", "C_watch_only"})
        self.assertNotEqual(result["trade_decision"], "no_buy")
        self.assertNotEqual(result["display_section"], "risk_no_buy")
        self.assertIn(result["risk_handling_bucket"], {"high_momentum_risk_follow", "risk_watch"})

    def test_taxonomy_suffix_override_prevents_robotics_non_mainstream_cap(self) -> None:
        result = evaluate_row(
            make_row(
                category="revenue_pullback",
                structural_theme_bucket="",
                theme_structural_status="non_mainstream_theme",
                theme_mainstream_label="non_mainstream_overheated",
                taxonomy_structural_theme_bucket_y="robotics_automation_theme",
                taxonomy_theme_structural_status_y="core_mainstream_theme",
                taxonomy_theme_mainstream_label_y="mainstream_growth_theme",
            )
        )
        self.assertEqual(result["theme_group"], "core_mainstream")
        self.assertNotIn("non_ai_non_mainstream_cap", result["downgrade_flags"])

    def test_action_rating_allows_first_tranche_when_model_recommended_structure_intact(self) -> None:
        result = evaluate_row(
            make_row(
                category="true_breakout",
                pattern_stage="breakout_confirmed",
                true_breakout="True",
                volume_ratio="2.0",
                distance_to_ma20_pct="2",
                return_20d="8",
            )
        )
        self.assertIn(result["action_rating"], {"buy_now", "scale_in", "starter_position"})
        self.assertIn(result["action_rating_label_zh"], {"建議買進", "可分批買進", "可小量試單"})
        self.assertIn("model_recommended", result["entry_prerequisites"])
        self.assertIn("next_monthly_revenue", result["post_entry_watch_items"])
        self.assertNotIn("next_monthly_revenue", result["entry_prerequisites"])

    def test_action_rating_wait_reclaim_when_structure_is_broken(self) -> None:
        result = evaluate_row(
            make_row(
                category="range_rebound",
                score="75",
                risk_tags="below_23ema_not_reclaimed",
                distance_to_ma20_pct="-7",
            )
        )
        self.assertEqual(result["action_rating"], "wait_reclaim")
        self.assertIn("below_23ema_not_reclaimed", result["downgrade_reason"])

    def test_tdcc_distribution_is_downgrade_reason_not_implicit_wait_confirm(self) -> None:
        result = evaluate_row(
            make_row(
                category="true_breakout",
                pattern_stage="breakout_confirmed",
                true_breakout="True",
                volume_ratio="2.5",
                tdcc_judgement="distribution_warning",
            )
        )
        self.assertIn("tdcc_distribution_warning", result["downgrade_reason"])
        self.assertIn("action_rating", result)


if __name__ == "__main__":
    unittest.main()
