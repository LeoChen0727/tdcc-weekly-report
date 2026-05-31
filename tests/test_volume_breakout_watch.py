from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_volume_breakout_watch import filter_latest_to_effective_signal_date  # noqa: E402


class VolumeBreakoutWatchTest(unittest.TestCase):
    def test_filter_falls_back_to_latest_trading_signal_before_report_date(self) -> None:
        latest = pd.DataFrame(
            [
                {"signal_date": "20260529", "stock_id": "2317"},
                {"signal_date": "20260528", "stock_id": "2330"},
            ]
        )

        out, effective_date = filter_latest_to_effective_signal_date(latest, "20260530")

        self.assertEqual(effective_date, "20260529")
        self.assertEqual(out["stock_id"].tolist(), ["2317"])

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
