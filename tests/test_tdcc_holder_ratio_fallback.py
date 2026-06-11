from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tdcc_holder_ratio_top10 import find_latest_snapshot_path  # noqa: E402


def test_find_latest_snapshot_path_uses_newest_date(tmp_path: Path) -> None:
    older = tmp_path / "tdcc_holder_ratio_20260605.csv"
    newer = tmp_path / "tdcc_holder_ratio_20260612.csv"
    ignored = tmp_path / "tdcc_holder_ratio_latest.csv"

    older.write_text("date,code\n20260605,1101\n", encoding="utf-8")
    newer.write_text("date,code\n20260612,1101\n", encoding="utf-8")
    ignored.write_text("date,code\n20260699,1101\n", encoding="utf-8")

    assert find_latest_snapshot_path(tmp_path) == newer


def test_find_latest_snapshot_path_returns_none_when_missing(tmp_path: Path) -> None:
    assert find_latest_snapshot_path(tmp_path) is None
