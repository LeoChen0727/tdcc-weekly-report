from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_daily_theme_leadership_layer import build_layer  # noqa: E402


def row(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "signal_date": "20260526",
        "stock_id": "1000",
        "stock_name": "Test",
        "category": "revenue_breakout_low_response",
        "industry": "test_theme",
        "theme_group": "",
        "decision_priority": "B_confirm_needed",
        "decision_score": "72",
        "tdcc_status": "mild_accumulation",
        "warrant_flow_signal": "no_signal",
        "volume_ratio": "1.1",
        "distance_to_previous_60d_high_pct": "-10",
        "repeat_appear_label": "",
        "downgrade_flags": "",
        "return_20d": "3",
    }
    base.update(overrides)
    return base


class DailyThemeLeadershipLayerTest(unittest.TestCase):
    def build(self, rows: list[dict[str, object]]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        return build_layer(pd.DataFrame(rows), "20260526")

    def test_mainstream_and_individual_overlap(self) -> None:
        enriched, theme, two_line = self.build(
            [
                row(stock_id="2001", stock_name="Leader", industry="AI server", category="true_breakout", decision_priority="A_priority_watch", true_breakout="True", volume_ratio="2.0", warrant_flow_signal="call_inflow"),
                row(stock_id="2002", stock_name="Follower", industry="AI server", category="range_rebound", decision_priority="A_priority_watch", platform_breakout_flag="True", volume_ratio="1.8"),
                row(stock_id="2003", stock_name="Breadth", industry="AI server", category="pattern", decision_priority="B_confirm_needed", distance_to_previous_60d_high_pct="-1", volume_ratio="1.3"),
            ]
        )
        self.assertIn(theme.iloc[0]["theme_final_status"], {"mainstream_leader", "mainstream_follow_through"})
        leader = enriched[enriched["stock_id"].eq("2001")].iloc[0]
        self.assertEqual(leader["candidate_line_group"], "breakout_attack_stock")
        self.assertEqual(leader["two_line_overlap_flag"], "True")

    def test_mainstream_only_candidate(self) -> None:
        enriched, _, _ = self.build(
            [
                row(stock_id="2101", stock_name="Leader", industry="PCB", category="true_breakout", decision_priority="A_priority_watch", true_breakout="True", volume_ratio="2.1"),
                row(stock_id="2102", stock_name="Unconfirmed", industry="PCB", category="pattern", decision_priority="C_watch_only", volume_ratio="1.4", distance_to_previous_60d_high_pct="-2"),
                row(stock_id="2103", stock_name="Follower", industry="PCB", category="range_rebound", decision_priority="C_watch_only", volume_ratio="1.2"),
            ]
        )
        unconfirmed = enriched[enriched["stock_id"].eq("2102")].iloc[0]
        self.assertEqual(unconfirmed["candidate_source_type"], "mainstream_theme_candidate")
        self.assertEqual(unconfirmed["candidate_line_group"], "range_near_high_watch")

    def test_individual_quality_non_mainstream(self) -> None:
        enriched, _, _ = self.build(
            [
                row(stock_id="2201", stock_name="Solo", industry="niche", category="revenue_breakout_low_response", decision_priority="A_priority_watch", tdcc_status="mild_accumulation"),
            ]
        )
        solo = enriched.iloc[0]
        self.assertEqual(solo["theme_final_status"], "single_name_signal")
        self.assertIn(solo["candidate_source_type"], {"latent_watch_candidate", "individual_quality_candidate"})
        self.assertNotIn(solo["candidate_line_group"], {"mainstream_leader_stock", "mainstream_follow_through_stock"})

    def test_stale_revenue_low_response_no_warrant(self) -> None:
        enriched, _, _ = self.build(
            [
                row(stock_id="2301", stock_name="StaleRev", industry="channel", category="revenue_breakout_low_response", decision_priority="B_confirm_needed", repeat_appear_label="stale_signal", warrant_flow_signal="no_signal", distance_to_previous_60d_high_pct="-8"),
            ]
        )
        stale = enriched.iloc[0]
        self.assertEqual(stale["candidate_source_type"], "latent_watch_candidate")
        self.assertEqual(stale["candidate_line_group"], "individual_revenue_low_response_watch")
        self.assertIn("\u71df\u6536\u7206\u767c\u80a1\u50f9\u5c1a\u672a\u53cd\u61c9", stale["theme_leadership_note"])

    def test_weak_theme_candidate(self) -> None:
        enriched, _, _ = self.build(
            [
                row(stock_id="2401", stock_name="Risk1", industry="weak", decision_priority="D_risk_downgrade", tdcc_status="distribution_warning", return_20d="35"),
                row(stock_id="2402", stock_name="Risk2", industry="weak", decision_priority="C_watch_only", tdcc_status="distribution_warning", return_20d="36"),
                row(stock_id="2403", stock_name="Risk3", industry="weak", decision_priority="C_watch_only", tdcc_status="distribution_warning", return_20d="40"),
            ]
        )
        self.assertTrue(enriched["candidate_source_type"].eq("risk_downgraded_candidate").all())
        self.assertTrue(enriched["candidate_line_group"].eq("risk").all())

    def test_overlap_flag_does_not_create_separate_priority_bucket(self) -> None:
        enriched, _, two_line = self.build(
            [
                row(stock_id="2501", stock_name="Leader", industry="AI server", category="true_breakout", decision_priority="A_priority_watch", true_breakout="True", volume_ratio="2.4"),
                row(stock_id="2502", stock_name="Overlap", industry="AI server", category="range_rebound", decision_priority="A_priority_watch", warrant_flow_signal="call_inflow", distance_to_previous_60d_high_pct="-1", volume_ratio="1.4"),
                row(stock_id="2503", stock_name="Breadth", industry="AI server", category="pattern", decision_priority="B_confirm_needed", tdcc_status="strong_accumulation", volume_ratio="1.3"),
            ]
        )
        overlap = enriched[enriched["stock_id"].eq("2502")].iloc[0]
        self.assertEqual(overlap["two_line_overlap_flag"], "True")
        self.assertNotEqual(overlap["candidate_line_group"], "two_line_overlap")
        self.assertNotIn("two_line_overlap", set(two_line["candidate_line_group"]))


if __name__ == "__main__":
    unittest.main()
