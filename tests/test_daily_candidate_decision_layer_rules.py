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
    }
    base.update(overrides)
    return pd.Series(base)


class DailyCandidateDecisionLayerRuleTest(unittest.TestCase):
    def test_revenue_low_response_stale_no_warrant_no_breakout(self) -> None:
        result = evaluate_row(
            make_row(
                repeat_appear_label="stale_signal",
                warrant_flow_signal="no_signal",
                revenue_good_eps_unconfirmed_flag="True",
            )
        )
        self.assertEqual(result["decision_priority"], "B_confirm_needed")
        self.assertIn("反覆上榜但尚未突破", result["why_downgraded"])
        self.assertIn("權證資金未確認", result["why_downgraded"])
        self.assertIn("營收成長尚未由 EPS / 毛利", result["why_downgraded"])
        self.assertIn("等待放量突破平台 / 前高", result["next_confirmation"])

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

    def test_stale_signal_no_breakout_no_warrant(self) -> None:
        result = evaluate_row(
            make_row(
                category="range_rebound",
                category_cn="區間內轉強 / 挑戰前高觀察",
                repeat_appear_label="stale_signal",
                warrant_flow_signal="no_signal",
                distance_to_previous_60d_high_pct="-4",
            )
        )
        self.assertEqual(result["decision_priority"], "B_confirm_needed")
        self.assertIn("反覆上榜但尚未突破", result["why_downgraded"])
        self.assertIn("權證資金未確認", result["why_downgraded"])


if __name__ == "__main__":
    unittest.main()
