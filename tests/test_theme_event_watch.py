from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_theme_event_watch import event_window_phase  # noqa: E402


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
