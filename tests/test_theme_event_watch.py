from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import pandas as pd

from build_theme_event_watch import EMPTY_WATCH_STATUS, WATCH_COLUMNS, ensure_nonempty_watch, event_window_phase  # noqa: E402


def day(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def test_recently_ended_multi_day_event_uses_event_end_date() -> None:
    days, phase = event_window_phase(day("20260611"), day("20260602"), day("20260605"))

    assert days == -6
    assert phase == "recent_ended"


def test_in_progress_multi_day_event_is_near_term_watch() -> None:
    days, phase = event_window_phase(day("20260603"), day("20260602"), day("20260605"))

    assert days == 0
    assert phase == "upcoming_0_7d"


def test_theme_event_watch_emits_empty_state_when_calendar_has_rows_but_no_watch_rows() -> None:
    out = ensure_nonempty_watch(pd.DataFrame(columns=WATCH_COLUMNS), "20260612", 1)

    assert len(out) == 1
    row = out.iloc[0]
    assert row["theme_event_watch_status"] == EMPTY_WATCH_STATUS
    assert row["event_phase"] == "empty_state"
    assert row["candidate_intersection_count"] == 0
    assert set(WATCH_COLUMNS).issubset(out.columns)
