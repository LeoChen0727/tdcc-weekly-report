from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from scripts import replay_historical_structured_sources as replay


def test_target_slice_hash_is_stable_when_later_rows_are_appended(tmp_path: Path) -> None:
    path = tmp_path / "history.csv"
    pd.DataFrame(
        [
            {"date": "20260720", "stock_id": "2330", "close": "100"},
            {"date": "20260721", "stock_id": "2330", "close": "101"},
        ]
    ).to_csv(path, index=False)

    before = replay.build_component_evidence(
        "stock",
        [(path, ["date", "stock_id"], {})],
        "20260720",
    )
    frame = pd.read_csv(path, dtype=str)
    frame.loc[len(frame)] = {"date": "20260724", "stock_id": "2330", "close": "104"}
    frame.to_csv(path, index=False)
    after = replay.build_component_evidence(
        "stock",
        [(path, ["date", "stock_id"], {})],
        "20260720",
    )

    assert before["slice_manifest_sha256"] == after["slice_manifest_sha256"]
    assert before["future_row_count"] == 1
    assert after["future_row_count"] == 2
    assert after["future_rows_excluded_from_slice"] is True


def test_immutable_manifest_rejects_nonidentical_collision(tmp_path: Path) -> None:
    path = tmp_path / "manifest.json"
    replay.write_json_immutable(path, {"replay_id": "run-1", "status": "pass"})
    replay.write_json_immutable(path, {"replay_id": "run-1", "status": "pass"})

    with pytest.raises(RuntimeError, match="immutable replay manifest collision"):
        replay.write_json_immutable(path, {"replay_id": "run-1", "status": "changed"})


def test_tpex_base_repair_routes_only_tpex(monkeypatch) -> None:
    commands: list[list[str]] = []
    monkeypatch.setattr(replay, "run_checked", lambda command, **kwargs: commands.append(command))
    monkeypatch.setattr(replay, "validate_exact_market_date", lambda date, codes: None)
    monkeypatch.setattr(
        replay,
        "read_json",
        lambda path: {
            "requested_date": "20260717",
            "requested_index_codes": ["TPEX"],
            "observed_dates": {"TPEX": "20260717"},
            "fallback_used": False,
            "future_rows_used": False,
        },
    )

    replay.run_market_date("20260717", {"TPEX"})

    assert len(commands) == 1
    assert commands[0][-2:] == ["--target-index-code", "TPEX"]
    assert "TWSE" not in commands[0]


def test_replay_id_is_path_safe() -> None:
    assert replay.parse_replay_id("github-run-123-1") == "github-run-123-1"
    with pytest.raises(RuntimeError, match="--replay-id"):
        replay.parse_replay_id("../escape")


def test_replay_window_excludes_weekend_dates_20260718_and_20260719() -> None:
    assert replay.expected_trading_dates("20260718", "20260724") == [
        "20260720",
        "20260721",
        "20260722",
        "20260723",
        "20260724",
    ]
