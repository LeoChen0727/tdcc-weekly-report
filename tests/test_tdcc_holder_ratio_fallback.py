from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import pandas as pd

from tdcc_holder_ratio_top10 import build_holder_ratio_snapshot, find_latest_snapshot_path  # noqa: E402


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


def test_holder_ratio_snapshot_excludes_invalid_single_holder_distribution() -> None:
    raw = pd.DataFrame(
        [
            {"date": "20260626", "code": "2380", "name": "虹光", "level": str(level), "holders": 0, "shares": 0, "ratio_pct": 0.0}
            for level in range(1, 15)
        ]
        + [
            {"date": "20260626", "code": "2380", "name": "虹光", "level": "15", "holders": 1, "shares": 60_000_000, "ratio_pct": 100.0},
            {"date": "20260626", "code": "2380", "name": "虹光", "level": "16", "holders": 0, "shares": 0, "ratio_pct": 0.0},
            {"date": "20260626", "code": "2380", "name": "虹光", "level": "17", "holders": 1, "shares": 60_000_000, "ratio_pct": 100.0},
            {"date": "20260626", "code": "3374", "name": "精材", "level": "12", "holders": 20, "shares": 4_000_000, "ratio_pct": 4.0},
            {"date": "20260626", "code": "3374", "name": "精材", "level": "13", "holders": 10, "shares": 3_000_000, "ratio_pct": 3.0},
            {"date": "20260626", "code": "3374", "name": "精材", "level": "14", "holders": 5, "shares": 2_000_000, "ratio_pct": 2.0},
            {"date": "20260626", "code": "3374", "name": "精材", "level": "15", "holders": 3, "shares": 1_000_000, "ratio_pct": 1.0},
            {"date": "20260626", "code": "3374", "name": "精材", "level": "17", "holders": 1000, "shares": 100_000_000, "ratio_pct": 100.0},
        ]
    )

    snapshot = build_holder_ratio_snapshot(raw, {})

    assert "2380" not in set(snapshot["code"].astype(str))
    assert snapshot.loc[snapshot["code"].eq("3374"), "over_400_pct"].iloc[0] == 10.0
    assert snapshot.loc[snapshot["code"].eq("3374"), "over_1000_pct"].iloc[0] == 1.0
