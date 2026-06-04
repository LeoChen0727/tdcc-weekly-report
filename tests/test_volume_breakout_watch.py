from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_volume_breakout_watch import WATCH_COLUMNS, ensure_watch_schema, filter_latest_to_effective_signal_date  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
