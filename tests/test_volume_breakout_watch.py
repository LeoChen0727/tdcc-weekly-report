from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_volume_breakout_watch import (  # noqa: E402
    VOLUME_BREAKOUT_RULE_VERSION,
    WATCH_COLUMNS,
    add_price_metrics,
    detect_volume_breakout,
    ensure_watch_schema,
    event_log_has_formal_bottom_history,
    filter_latest_to_effective_signal_date,
)


class VolumeBreakoutWatchTest(unittest.TestCase):
    def test_empty_watch_schema_keeps_required_columns(self) -> None:
        out = ensure_watch_schema(pd.DataFrame())

        self.assertEqual(out.columns.tolist(), WATCH_COLUMNS)
        self.assertTrue(out.empty)

    def test_partial_watch_schema_adds_missing_columns_and_preserves_extra(self) -> None:
        out = ensure_watch_schema(pd.DataFrame([{"stock_id": "2317", "custom_note": "keep"}]))

        self.assertEqual(out.iloc[0]["stock_id"], "2317")
        self.assertEqual(out.iloc[0]["custom_note"], "keep")
        for col in WATCH_COLUMNS:
            self.assertIn(col, out.columns)

    def test_filter_does_not_fall_back_to_stale_signal_before_report_date(self) -> None:
        latest = pd.DataFrame(
            [
                {"signal_date": "20260529", "stock_id": "2317"},
                {"signal_date": "20260528", "stock_id": "2330"},
            ]
        )

        out, effective_date = filter_latest_to_effective_signal_date(latest, "20260530")

        self.assertEqual(effective_date, "20260530")
        self.assertTrue(out.empty)

    def test_filter_uses_exact_main_date_when_available(self) -> None:
        latest = pd.DataFrame(
            [
                {"signal_date": "20260529", "stock_id": "2317"},
                {"signal_date": "20260530", "stock_id": "2330"},
            ]
        )

        out, effective_date = filter_latest_to_effective_signal_date(latest, "20260530")

        self.assertEqual(effective_date, "20260530")
        self.assertEqual(out["stock_id"].tolist(), ["2330"])

    def test_old_broad_event_log_forces_formal_bottom_rebuild(self) -> None:
        old_events = pd.DataFrame(
            [
                {"volume_breakout_type": "loose_platform_volume_watch"},
                {"volume_breakout_type": "strict_60d_volume_breakout"},
            ]
        )
        formal_events = pd.DataFrame(
            [
                {
                    "volume_breakout_type": "bottom_volume_attack",
                    "volume_breakout_rule_version": VOLUME_BREAKOUT_RULE_VERSION,
                },
            ]
        )
        stale_formal_events = pd.DataFrame(
            [
                {"volume_breakout_type": "bottom_volume_attack"},
            ]
        )

        self.assertFalse(event_log_has_formal_bottom_history(old_events))
        self.assertFalse(event_log_has_formal_bottom_history(stale_formal_events))
        self.assertTrue(event_log_has_formal_bottom_history(formal_events))

    def test_locked_limit_up_low_volume_ratio_is_bottom_volume_attack(self) -> None:
        rows: list[dict[str, object]] = []
        for idx in range(25):
            rows.append(
                {
                    "date": f"202605{idx + 1:02d}",
                    "stock_id": "4916",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 72.0,
                    "high": 74.4,
                    "low": 70.0,
                    "close": 74.4,
                    "volume": 7_300_000,
                }
            )
        rows.append(
            {
                "date": "20260526",
                "stock_id": "4916",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 81.8,
                "high": 81.8,
                "low": 81.8,
                "close": 81.8,
                "volume": 3_578_609,
            }
        )
        df = add_price_metrics(pd.DataFrame(rows))
        signal = detect_volume_breakout(df.iloc[-1])

        self.assertIsNotNone(signal)
        assert signal is not None
        self.assertEqual(signal.event_type, "bottom_volume_attack")
        self.assertIn("locked_limit_up_breakout", signal.notes)
        self.assertIn("locked_limit_no_volume_gate", signal.notes)
        self.assertLess(float(df.iloc[-1]["volume_ratio"]), 2.0)

    def test_locked_limit_up_does_not_require_average_volume_gate(self) -> None:
        rows: list[dict[str, object]] = []
        for idx in range(25):
            rows.append(
                {
                    "date": f"202606{idx + 1:02d}",
                    "stock_id": "4916",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 72.0,
                    "high": 74.4,
                    "low": 70.0,
                    "close": 74.4,
                    "volume": 10,
                }
            )
        rows.append(
            {
                "date": "20260626",
                "stock_id": "4916",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 81.8,
                "high": 81.8,
                "low": 81.8,
                "close": 81.8,
                "volume": 10,
            }
        )
        df = add_price_metrics(pd.DataFrame(rows))
        signal = detect_volume_breakout(df.iloc[-1])

        self.assertIsNotNone(signal)
        assert signal is not None
        self.assertEqual(signal.event_type, "bottom_volume_attack")
        self.assertIn("locked_limit_up_breakout", signal.notes)
        self.assertIn("locked_limit_no_volume_gate", signal.notes)
        self.assertNotIn("volume_ma20_lots_ge_1000", signal.notes)

    def test_non_locked_low_volume_ratio_breakout_still_fails(self) -> None:
        rows: list[dict[str, object]] = []
        for idx in range(25):
            rows.append(
                {
                    "date": f"202604{idx + 1:02d}",
                    "stock_id": "1234",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 98.0,
                    "high": 100.0,
                    "low": 95.0,
                    "close": 98.0,
                    "volume": 2_000_000,
                }
            )
        rows.append(
            {
                "date": "20260501",
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 101.0,
                "high": 110.0,
                "low": 99.0,
                "close": 110.0,
                "volume": 3_000_000,
            }
        )
        df = add_price_metrics(pd.DataFrame(rows))

        self.assertIsNone(detect_volume_breakout(df.iloc[-1]))


if __name__ == "__main__":
    unittest.main()
