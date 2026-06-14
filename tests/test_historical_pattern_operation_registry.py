from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_historical_pattern_operation_registry import (  # noqa: E402
    PATTERN_SPECS,
    add_research_features,
    current_model_hit,
    long_base_low_position,
    relaxed_limit_locked_low_volume,
    simulate_trade,
    summarize_registry,
)


def price_frame(rows: list[dict[str, object]]) -> pd.DataFrame:
    return add_research_features(pd.DataFrame(rows))


def base_history(signal_overrides: dict[str, object] | None = None) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for idx in range(70):
        high = 120 if 10 <= idx < 20 else 100
        rows.append(
            {
                "date": f"202601{idx + 1:02d}",
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 100,
                "high": high,
                "low": 95,
                "close": 98,
                "volume": 2_000_000,
            }
        )
    signal = {
        "date": "20260315",
        "stock_id": "1234",
        "stock_name": "TEST",
        "market": "TWSE",
        "open": 101,
        "high": 106,
        "low": 99,
        "close": 104,
        "volume": 5_000_000,
    }
    if signal_overrides:
        signal.update(signal_overrides)
    rows.append(signal)
    future = [
        ("20260316", 103, 105, 101, 104, 4_000_000),
        ("20260317", 104, 109, 102, 108, 4_200_000),
        ("20260318", 108, 111, 107, 110, 3_900_000),
        ("20260319", 110, 112, 109, 111, 3_800_000),
        ("20260320", 111, 113, 110, 112, 3_700_000),
        ("20260321", 112, 114, 111, 113, 3_600_000),
        ("20260322", 113, 115, 112, 114, 3_500_000),
        ("20260323", 114, 116, 113, 115, 3_400_000),
        ("20260324", 115, 117, 114, 116, 3_300_000),
        ("20260325", 116, 118, 115, 117, 3_200_000),
        ("20260326", 117, 119, 116, 118, 3_100_000),
    ]
    for date, open_, high, low, close, volume in future:
        rows.append(
            {
                "date": date,
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": open_,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
            }
        )
    return price_frame(rows)


class HistoricalPatternOperationRegistryTest(unittest.TestCase):
    def test_current_model_hit_keeps_volume_ratio_gate(self) -> None:
        df = base_history()
        signal = df.iloc[70]

        self.assertTrue(current_model_hit(signal))

        low_volume = base_history({"volume": 3_000_000, "close": 110, "high": 110, "open": 110})
        low_volume_signal = low_volume.iloc[70]

        self.assertFalse(current_model_hit(low_volume_signal))
        self.assertTrue(relaxed_limit_locked_low_volume(low_volume_signal))

    def test_locked_limit_up_low_volume_ratio_is_current_model_hit(self) -> None:
        locked = base_history({"volume": 1_000_000, "close": 110, "high": 110, "low": 110, "open": 110})
        signal = locked.iloc[70]

        self.assertTrue(current_model_hit(signal))
        self.assertFalse(relaxed_limit_locked_low_volume(signal))
        self.assertTrue(bool(signal["limit_up_like"]))

    def test_long_base_low_position_uses_current_model_hit(self) -> None:
        df = base_history()
        self.assertTrue(long_base_low_position(df.iloc[70]))

        relaxed = base_history({"volume": 3_000_000, "close": 110, "high": 110, "open": 110})
        self.assertFalse(long_base_low_position(relaxed.iloc[70]))

    def test_signal_low_stop_exits_before_take_profit_for_same_day_ambiguity(self) -> None:
        df = base_history()
        signal_idx = 70
        df.loc[71, "low"] = 98
        df.loc[71, "high"] = 112
        spec = next(s for s in PATTERN_SPECS if s.pattern_id == "next_open_tp5_signal_low_stop_10d")

        trade = simulate_trade(df, signal_idx, spec)

        self.assertIsNotNone(trade)
        assert trade is not None
        self.assertEqual(trade["exit_reason"], "stop_signal_low")
        self.assertLess(float(trade["return_pct"]), 0)

    def test_registry_never_auto_approves_daily(self) -> None:
        detail = pd.DataFrame(
            [
                {
                    "model_id": "volume_range_breakout",
                    "event_filter_id": "current_model_hit_all",
                    "model_hit_status": "current_model_hit",
                    "pattern_id": "next_open_hold_5d",
                    "event_date": "20260101",
                    "stock_id": "1234",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "market_regime": "mild_bull",
                    "entry_date": "20260102",
                    "entry_price": 100,
                    "exit_date": "20260106",
                    "exit_price": 104,
                    "exit_reason": "fixed_5d_close",
                    "holding_days": 5,
                    "return_pct": 4.0,
                    "mfe_pct": 5.0,
                    "mae_pct": -1.0,
                    "out_of_sample": False,
                    "volume_ratio": 2.5,
                    "signal_return_1d_pct": 4.0,
                    "signal_low": 95,
                    "signal_high": 105,
                    "previous_20d_high": 100,
                    "range_width_20_pct": 10,
                    "range_width_40_pct": 12,
                    "range_width_60_pct": 20,
                    "low_position_60_pct": 40,
                    "limit_up_like": False,
                }
            ]
        )

        registry = summarize_registry(detail)

        self.assertEqual(registry["approved_for_daily"].astype(str).str.lower().tolist(), ["false"])
        self.assertEqual(registry.iloc[0]["confidence_status"], "low")


if __name__ == "__main__":
    unittest.main()
