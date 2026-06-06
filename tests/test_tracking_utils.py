from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from tracking_utils import recent_market_index_fetch_months  # noqa: E402


def test_recent_market_index_fetch_months_backfills_when_history_is_empty() -> None:
    assert recent_market_index_fetch_months("20260605", pd.DataFrame(), months=4) == [
        "20260301",
        "20260401",
        "20260501",
        "20260601",
    ]


def test_recent_market_index_fetch_months_refreshes_only_recent_months_when_current() -> None:
    old = pd.DataFrame(
        [
            {"date": "20260605", "index_code": "TWSE", "ohlc_available": True},
            {"date": "20260605", "index_code": "TPEX", "ohlc_available": True},
        ]
    )

    assert recent_market_index_fetch_months("20260605", old, months=4) == [
        "20260501",
        "20260601",
    ]


def test_recent_market_index_fetch_months_includes_missing_forward_months() -> None:
    old = pd.DataFrame(
        [
            {"date": "20260430", "index_code": "TWSE", "ohlc_available": True},
            {"date": "20260430", "index_code": "TPEX", "ohlc_available": True},
        ]
    )

    assert recent_market_index_fetch_months("20260605", old, months=4) == [
        "20260401",
        "20260501",
        "20260601",
    ]


def test_recent_market_index_fetch_months_backfills_if_required_index_missing() -> None:
    old = pd.DataFrame(
        [
            {"date": "20260605", "index_code": "TWSE", "ohlc_available": True},
        ]
    )

    assert recent_market_index_fetch_months("20260605", old, months=4) == [
        "20260301",
        "20260401",
        "20260501",
        "20260601",
    ]
