from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import plan_historical_structured_source_replay as planner


TAIFEX_SOURCES = tuple(planner.replay.TAIFEX_HISTORY_SPECS)


def tail_matrix(*, high_water: str = "20260729", base: str = "20260724") -> dict:
    return {
        "daily_price": high_water,
        "stock_price_history": {
            "max_date": high_water,
            "files": 100,
            "files_at_max": 100,
        },
        "market_index": {"TWSE": base, "TPEX": base},
        "market_index_ohlc": {"TWSE": base, "TPEX": base},
        "taifex": {source_id: base for source_id in TAIFEX_SOURCES},
        "warrant_daily": base,
        "warrant_flow": base,
    }


def test_plan_returns_exact_bounded_replay_window() -> None:
    result = planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=3)

    assert result == {
        "should_replay": True,
        "start_date": "20260727",
        "end_date": "20260729",
        "price_history_high_water_date": "20260729",
        "required_base_date": "20260724",
        "trading_dates": ["20260727", "20260728", "20260729"],
        "reason": "structured_sources_behind_price_history_high_water",
    }


def test_plan_returns_no_replay_when_structured_tails_match_high_water() -> None:
    result = planner.plan_from_tail_matrix(
        tail_matrix(high_water="20260729", base="20260729"),
        max_replay_dates=1,
    )

    assert result == {
        "should_replay": False,
        "start_date": "",
        "end_date": "",
        "price_history_high_water_date": "20260729",
        "required_base_date": "20260729",
        "trading_dates": [],
        "reason": "structured_sources_already_at_price_history_high_water",
    }


def test_plan_reads_source_tail_matrix_once(monkeypatch) -> None:
    calls = 0
    validated: list[tuple[dict, str, str]] = []
    coverage: list[tuple[str, int]] = []

    def source_tail_matrix() -> dict:
        nonlocal calls
        calls += 1
        return tail_matrix(high_water="20260729", base="20260729")

    monkeypatch.setattr(planner.replay, "source_tail_matrix", source_tail_matrix)
    monkeypatch.setattr(
        planner.replay,
        "validate_exact_baseline",
        lambda matrix, required_base, high_water: validated.append(
            (matrix, required_base, high_water)
        ),
    )
    monkeypatch.setattr(
        planner,
        "validate_recent_structured_source_coverage",
        lambda end_date, count: coverage.append((end_date, count)),
    )

    result = planner.build_plan(max_replay_dates=1)

    assert result["should_replay"] is False
    assert calls == 1
    assert validated == [
        (
            tail_matrix(high_water="20260729", base="20260729"),
            "20260729",
            "20260729",
        )
    ]
    assert coverage == [("20260729", 1)]


def test_build_plan_fails_when_exact_baseline_validation_fails(monkeypatch) -> None:
    monkeypatch.setattr(
        planner.replay,
        "source_tail_matrix",
        lambda: tail_matrix(high_water="20260729", base="20260729"),
    )

    def fail_exact_baseline(*args, **kwargs) -> None:
        raise RuntimeError("canonical legacy parity failed")

    monkeypatch.setattr(planner.replay, "validate_exact_baseline", fail_exact_baseline)

    with pytest.raises(RuntimeError, match="canonical legacy parity failed"):
        planner.build_plan(max_replay_dates=1)


def test_recent_structured_coverage_checks_each_family_for_each_date(monkeypatch) -> None:
    previous = {
        "20260729": "20260728",
        "20260728": "20260727",
    }
    calls: list[tuple[str, str]] = []
    monkeypatch.setattr(planner.replay, "previous_trading_date", previous.__getitem__)
    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        lambda source_id, target_date: calls.append((source_id, target_date)),
    )

    planner.validate_recent_structured_source_coverage("20260729", count=3)

    assert calls == [
        (source_id, target_date)
        for target_date in ("20260727", "20260728", "20260729")
        for source_id in (
            "market_index",
            "taifex_futures_options_vix",
            "official_warrant_daily",
        )
    ]


def test_recent_structured_coverage_propagates_internal_gap(monkeypatch) -> None:
    def fail(source_id: str, target_date: str) -> None:
        raise RuntimeError(f"missing structured row {source_id} {target_date}")

    monkeypatch.setattr(planner.replay, "build_source_output_evidence", fail)

    with pytest.raises(RuntimeError, match="missing structured row"):
        planner.validate_recent_structured_source_coverage("20260729", count=1)


def test_plan_rejects_price_and_history_tail_mismatch() -> None:
    matrix = tail_matrix()
    matrix["stock_price_history"]["max_date"] = "20260728"

    with pytest.raises(RuntimeError, match="price/history tails are not aligned"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("daily_price",), ""),
        (("stock_price_history", "max_date"), ""),
        (("market_index", "TWSE"), ""),
        (("market_index_ohlc", "TPEX"), ""),
        (("taifex", TAIFEX_SOURCES[0]), ""),
        (("warrant_daily",), ""),
        (("warrant_flow",), ""),
    ],
)
def test_plan_rejects_empty_required_tail(path: tuple[str, ...], value: str) -> None:
    matrix = tail_matrix()
    target = matrix
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

    with pytest.raises(RuntimeError, match="tail is empty"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


@pytest.mark.parametrize(
    ("family", "key"),
    [
        ("market_index", "TPEX"),
        ("market_index_ohlc", "TWSE"),
        ("taifex", TAIFEX_SOURCES[-1]),
    ],
)
def test_plan_rejects_misaligned_structured_tail(family: str, key: str) -> None:
    matrix = tail_matrix()
    matrix[family][key] = "20260723"

    with pytest.raises(RuntimeError, match="structured tails are not aligned"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_missing_taifex_tail() -> None:
    matrix = tail_matrix()
    del matrix["taifex"][TAIFEX_SOURCES[-1]]

    with pytest.raises(RuntimeError, match="TAIFEX tail set mismatch"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_structured_base_later_than_high_water() -> None:
    with pytest.raises(RuntimeError, match="structured base is later"):
        planner.plan_from_tail_matrix(
            tail_matrix(high_water="20260724", base="20260727"),
            max_replay_dates=3,
        )


def test_plan_rejects_window_over_max_replay_dates() -> None:
    with pytest.raises(RuntimeError, match="exceeds --max-replay-dates"):
        planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=2)


def test_plan_rejects_nonpositive_max_replay_dates() -> None:
    with pytest.raises(RuntimeError, match="must be a positive integer"):
        planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=0)


def test_plan_rejects_window_without_a_trading_date() -> None:
    with pytest.raises(RuntimeError, match="high-water is not a trading date"):
        planner.plan_from_tail_matrix(
            tail_matrix(high_water="20260726", base="20260724"),
            max_replay_dates=3,
        )


def test_plan_rejects_weekend_high_water_even_when_window_contains_a_trading_date() -> None:
    with pytest.raises(RuntimeError, match="high-water is not a trading date"):
        planner.plan_from_tail_matrix(
            tail_matrix(high_water="20260725", base="20260723"),
            max_replay_dates=3,
        )


def test_plan_rejects_noncontiguous_first_trading_date(monkeypatch) -> None:
    monkeypatch.setattr(planner.replay, "previous_trading_date", lambda date: "20260723")

    with pytest.raises(RuntimeError, match="not immediately before"):
        planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=3)


def test_main_writes_json_only_after_plan_succeeds(tmp_path: Path, monkeypatch) -> None:
    output = tmp_path / "plan.json"
    expected = planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=3)
    monkeypatch.setattr(planner, "build_plan", lambda **kwargs: expected)

    assert planner.main(["--max-replay-dates", "3", "--output", str(output)]) == 0
    assert json.loads(output.read_text(encoding="utf-8")) == expected


def test_main_does_not_write_output_when_plan_fails(tmp_path: Path, monkeypatch) -> None:
    output = tmp_path / "plan.json"

    def fail(**kwargs):
        raise RuntimeError("fail closed")

    monkeypatch.setattr(planner, "build_plan", fail)

    with pytest.raises(RuntimeError, match="fail closed"):
        planner.main(["--max-replay-dates", "3", "--output", str(output)])
    assert not output.exists()
