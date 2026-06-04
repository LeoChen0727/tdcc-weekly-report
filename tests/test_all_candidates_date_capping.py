from __future__ import annotations

import pandas as pd

import build_all_candidates_latest as candidates


def test_future_source_date_is_capped_to_effective_market_date(monkeypatch):
    monkeypatch.setattr(candidates, "main_price_date_from_freshness", lambda: "20260603")
    monkeypatch.setattr(candidates, "latest_stock_price_history_date", lambda: "20260603")

    source = pd.DataFrame(
        {
            "date": ["20260604"],
            "stock_id": ["3046"],
            "stock_name": ["建碁"],
            "category": ["range_rebound"],
        }
    )

    result, signal_date, notes = candidates.canonicalize_candidate_dates(source)

    assert signal_date == "20260603"
    assert len(result) == 1
    assert result.loc[result.index[0], "date"] == "20260603"
    assert result.loc[result.index[0], "signal_date"] == "20260603"
    assert result.loc[result.index[0], "main_price_date"] == "20260603"
    assert result.loc[result.index[0], "source_date"] == "20260603"
    assert result.loc[result.index[0], "raw_source_date"] == "20260604"
    assert "capped_future_source_rows=1 effective_source_date=20260603" in notes


def test_older_source_date_is_dropped_against_effective_market_date(monkeypatch):
    monkeypatch.setattr(candidates, "main_price_date_from_freshness", lambda: "20260603")
    monkeypatch.setattr(candidates, "latest_stock_price_history_date", lambda: "20260603")

    source = pd.DataFrame(
        {
            "date": ["20260602"],
            "stock_id": ["3046"],
            "stock_name": ["建碁"],
            "category": ["range_rebound"],
        }
    )

    result, signal_date, notes = candidates.canonicalize_candidate_dates(source)

    assert signal_date == "20260603"
    assert result.empty
    assert "dropped_stale_source_rows=1 expected_source_date=20260603" in notes
