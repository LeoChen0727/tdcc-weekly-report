from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from scripts import plan_historical_structured_source_replay as planner


TAIFEX_SOURCES = tuple(planner.replay.TAIFEX_HISTORY_SPECS)
TAIFEX_DATED_SOURCES = tuple(planner.replay.TAIFEX_DATED_RAW_SOURCE_IDS)


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


def operational_tail_matrix(
    *,
    high_water: str = "20260729",
    taifex_dated_tail: str = "20260728",
    warrant_tail: str | None = None,
) -> dict:
    matrix = tail_matrix(high_water=high_water, base=high_water)
    for source_id in TAIFEX_DATED_SOURCES:
        matrix["taifex"][source_id] = taifex_dated_tail
    if warrant_tail is not None:
        matrix["warrant_daily"] = warrant_tail
        matrix["warrant_flow"] = warrant_tail
    return matrix


def cross_day_operational_tail_matrix(
    *,
    high_water: str = "20260729",
    operational_date: str = "20260724",
    taifex_dated_tail: str = "20260723",
) -> dict:
    matrix = tail_matrix(high_water=high_water, base=operational_date)
    for source_id in TAIFEX_DATED_SOURCES:
        matrix["taifex"][source_id] = taifex_dated_tail
    return matrix


def test_plan_returns_exact_bounded_replay_window() -> None:
    result = planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=3)

    assert result == {
        "should_replay": True,
        "start_date": "20260727",
        "end_date": "20260728",
        "price_history_high_water_date": "20260729",
        "required_base_date": "20260724",
        "taifex_dated_tail_date": "20260724",
        "repair_taifex_base_date": "",
        "trading_dates": ["20260727", "20260728"],
        "reason": "structured_sources_require_pre_resume_catch_up",
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
        "taifex_dated_tail_date": "20260729",
        "repair_taifex_base_date": "",
        "trading_dates": [],
        "reason": "structured_sources_already_at_price_history_high_water",
    }


def test_plan_accepts_source_specific_operational_tails_without_replay() -> None:
    result = planner.plan_from_tail_matrix(
        operational_tail_matrix(),
        max_replay_dates=3,
    )

    assert result == {
        "should_replay": False,
        "start_date": "",
        "end_date": "",
        "price_history_high_water_date": "20260729",
        "required_base_date": "20260729",
        "taifex_dated_tail_date": "20260728",
        "repair_taifex_base_date": "",
        "trading_dates": [],
        "reason": "structured_sources_satisfy_source_specific_operational_tails",
    }


def test_plan_accepts_natural_current_recovery_with_d1_warrant_and_taifex(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        planner.replay,
        "expected_trading_dates",
        lambda start_date, end_date: ["20260827"],
    )
    monkeypatch.setattr(
        planner.replay,
        "previous_trading_date",
        lambda date: {"20260827": "20260826"}[date],
    )

    result = planner.plan_from_tail_matrix(
        operational_tail_matrix(
            high_water="20260827",
            taifex_dated_tail="20260826",
            warrant_tail="20260826",
        ),
        max_replay_dates=10,
    )

    assert result == {
        "should_replay": False,
        "start_date": "",
        "end_date": "",
        "price_history_high_water_date": "20260827",
        "required_base_date": "20260827",
        "taifex_dated_tail_date": "20260826",
        "repair_taifex_base_date": "",
        "trading_dates": [],
        "reason": "structured_sources_satisfy_source_specific_operational_tails",
    }


def test_no_replay_current_plan_accepts_taifex_history_superset(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    target_date = "20260819"
    history_path = Path("data/futures_options/taifex_futures_contracts_history.csv")
    raw_path = Path(f"data/futures_options/raw/futures_contracts_{target_date}.csv")
    vix_path = Path("data/futures_options/taiwan_vix_history.csv")
    history_path.parent.mkdir(parents=True)
    raw_path.parent.mkdir(parents=True)
    shared = pd.DataFrame(
        [
            {
                "日期": target_date,
                "商品名稱": f"臺股期貨{i:02d}",
                "身份別": "自營商",
                "未平倉餘額_多方_口數": str(1000 + i),
            }
            for i in range(66)
        ]
    )
    history_only = pd.DataFrame(
        [
            {
                "日期": target_date,
                "商品名稱": "臺灣中型100期貨",
                "身份別": identity,
                "未平倉餘額_多方_口數": str(2000 + i),
            }
            for i, identity in enumerate(("自營商", "投信", "外資"))
        ]
    )
    shared.to_csv(raw_path, index=False)
    pd.concat([shared, history_only], ignore_index=True).to_csv(history_path, index=False)
    pd.DataFrame([{"date": target_date, "value": "18.5"}]).to_csv(
        vix_path,
        index=False,
    )

    history_specs = {
        "futures_contracts": (
            history_path,
            ["日期", "商品名稱", "身份別"],
        ),
        "taiwan_vix": (vix_path, ["date"]),
    }
    matrix = {
        "daily_price": target_date,
        "stock_price_history": {
            "max_date": target_date,
            "files": 100,
            "files_at_max": 100,
        },
        "market_index": {"TWSE": target_date, "TPEX": target_date},
        "market_index_ohlc": {"TWSE": target_date, "TPEX": target_date},
        "taifex": {source_id: target_date for source_id in history_specs},
        "warrant_daily": target_date,
        "warrant_flow": target_date,
    }
    monkeypatch.setattr(planner.replay, "TAIFEX_HISTORY_SPECS", history_specs)
    monkeypatch.setattr(
        planner.replay,
        "TAIFEX_DATED_RAW_SOURCE_IDS",
        ("futures_contracts",),
    )
    monkeypatch.setattr(planner, "TAIFEX_DATED_SOURCE_IDS", ("futures_contracts",))
    monkeypatch.setattr(planner.replay, "source_tail_matrix", lambda: matrix)
    monkeypatch.setattr(
        planner.replay,
        "expected_trading_dates",
        lambda start_date, end_date: [target_date],
    )
    monkeypatch.setattr(
        planner.replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda date: {},
    )
    monkeypatch.setattr(
        planner.replay,
        "validate_stock_history_date_coverage",
        lambda date, manifest_end_date: {},
    )
    build_evidence = planner.replay.build_source_output_evidence
    observed_taifex_evidence: list[dict] = []

    def capture_evidence(source_id: str, date: str) -> dict:
        if source_id != "taifex_futures_options_vix":
            return {"pk_unique": True}
        evidence = build_evidence(source_id, date)
        observed_taifex_evidence.append(evidence)
        return evidence

    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        capture_evidence,
    )

    result = planner.build_plan(max_replay_dates=1)

    assert result["should_replay"] is False
    assert result["reason"] == "structured_sources_already_at_price_history_high_water"
    parity = observed_taifex_evidence[0]["taifex_raw_history_parity"]
    assert parity["futures_contracts"]["raw_row_count"] == 66
    assert parity["futures_contracts"]["history_row_count"] == 69
    assert parity["futures_contracts"]["history_only_row_count"] == 3


def test_plan_leaves_single_operational_advance_to_daily_full() -> None:
    result = planner.plan_from_tail_matrix(
        cross_day_operational_tail_matrix(high_water="20260727"),
        max_replay_dates=1,
    )

    assert result == {
        "should_replay": False,
        "start_date": "",
        "end_date": "",
        "price_history_high_water_date": "20260727",
        "required_base_date": "20260724",
        "taifex_dated_tail_date": "20260723",
        "repair_taifex_base_date": "",
        "trading_dates": [],
        "reason": "structured_sources_ready_for_single_daily_full_advance",
    }


def test_plan_leaves_single_aligned_advance_to_daily_full() -> None:
    result = planner.plan_from_tail_matrix(
        tail_matrix(high_water="20260727", base="20260724"),
        max_replay_dates=1,
    )

    assert result["should_replay"] is False
    assert result["required_base_date"] == "20260724"
    assert result["taifex_dated_tail_date"] == "20260724"
    assert result["repair_taifex_base_date"] == ""
    assert result["reason"] == "structured_sources_ready_for_single_daily_full_advance"


def test_plan_repairs_taifex_base_then_replays_only_pre_resume_dates() -> None:
    result = planner.plan_from_tail_matrix(
        cross_day_operational_tail_matrix(),
        max_replay_dates=3,
    )

    assert result == {
        "should_replay": True,
        "start_date": "20260727",
        "end_date": "20260728",
        "price_history_high_water_date": "20260729",
        "required_base_date": "20260724",
        "taifex_dated_tail_date": "20260723",
        "repair_taifex_base_date": "20260724",
        "trading_dates": ["20260727", "20260728"],
        "reason": "structured_sources_require_pre_resume_catch_up",
    }


def test_plan_counts_taifex_base_repair_against_replay_limit() -> None:
    with pytest.raises(
        RuntimeError,
        match="taifex_base_repair_count=1 max_replay_dates=2",
    ):
        planner.plan_from_tail_matrix(
            cross_day_operational_tail_matrix(),
            max_replay_dates=2,
        )


def test_plan_reads_source_tail_matrix_once(monkeypatch) -> None:
    calls = 0
    price_validated: list[str] = []
    stock_validated: list[tuple[str, str]] = []
    coverage: list[tuple[str, str, int, bool]] = []

    def source_tail_matrix() -> dict:
        nonlocal calls
        calls += 1
        return operational_tail_matrix(warrant_tail="20260728")

    monkeypatch.setattr(planner.replay, "source_tail_matrix", source_tail_matrix)
    monkeypatch.setattr(
        planner.replay,
        "validate_exact_baseline",
        lambda *args, **kwargs: pytest.fail(
            "operational no-replay must not use the aligned replay baseline"
        ),
    )
    monkeypatch.setattr(
        planner.replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda end_date: price_validated.append(end_date),
    )
    monkeypatch.setattr(
        planner.replay,
        "validate_stock_history_date_coverage",
        lambda end_date, manifest_end_date: stock_validated.append(
            (end_date, manifest_end_date)
        ),
    )
    monkeypatch.setattr(
        planner,
        "validate_operational_structured_source_coverage",
        lambda high_water, taifex_dated_tail_date, warrant_tail_date, count,
        allow_historical_structured_absence: coverage.append(
            (
                high_water,
                taifex_dated_tail_date,
                warrant_tail_date,
                count,
                allow_historical_structured_absence,
            )
        ),
    )

    result = planner.build_plan(max_replay_dates=1)

    assert result["should_replay"] is False
    assert calls == 1
    assert price_validated == ["20260729"]
    assert stock_validated == [("20260729", "20260729")]
    assert coverage == [("20260729", "20260728", "20260728", 1, True)]


def test_build_plan_fails_when_exact_baseline_validation_fails(monkeypatch) -> None:
    monkeypatch.setattr(
        planner.replay,
        "source_tail_matrix",
        lambda: tail_matrix(high_water="20260728", base="20260724"),
    )

    def fail_exact_baseline(*args, **kwargs) -> None:
        raise RuntimeError("canonical legacy parity failed")

    monkeypatch.setattr(planner.replay, "validate_exact_baseline", fail_exact_baseline)

    with pytest.raises(RuntimeError, match="canonical legacy parity failed"):
        planner.build_plan(max_replay_dates=1)


def test_build_plan_routes_mixed_replay_baseline_and_coverage(monkeypatch) -> None:
    matrix = cross_day_operational_tail_matrix()
    baseline_calls: list[tuple[dict, str, str, str]] = []
    coverage_calls: list[tuple[str, str, str, int]] = []
    monkeypatch.setattr(planner.replay, "source_tail_matrix", lambda: matrix)
    monkeypatch.setattr(
        planner.replay,
        "validate_exact_baseline",
        lambda observed, required_base, high_water, repair_taifex_base_date: (
            baseline_calls.append(
                (observed, required_base, high_water, repair_taifex_base_date)
            )
        ),
    )
    monkeypatch.setattr(
        planner,
        "validate_operational_structured_source_coverage",
        lambda high_water, taifex_dated_tail_date, warrant_tail_date,
        count: coverage_calls.append(
            (high_water, taifex_dated_tail_date, warrant_tail_date, count)
        ),
    )
    monkeypatch.setattr(
        planner,
        "validate_recent_structured_source_coverage",
        lambda *args, **kwargs: pytest.fail(
            "mixed replay baseline must use source-specific coverage"
        ),
    )

    result = planner.build_plan(max_replay_dates=3)

    assert result["repair_taifex_base_date"] == "20260724"
    assert baseline_calls == [(matrix, "20260724", "20260729", "20260724")]
    assert coverage_calls == [("20260724", "20260723", "20260724", 3)]


def test_no_replay_recent_coverage_relaxes_only_older_taifex_dates(monkeypatch) -> None:
    previous = {
        "20260729": "20260728",
        "20260728": "20260727",
    }
    calls: list[tuple[str, str]] = []
    vix_calls: list[str] = []
    historical_parity_calls: list[tuple[str, bool]] = []
    monkeypatch.setattr(planner.replay, "previous_trading_date", previous.__getitem__)
    def capture_output(source_id: str, target_date: str) -> dict[str, bool]:
        calls.append((source_id, target_date))
        return {"pk_unique": True}

    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        capture_output,
    )
    monkeypatch.setattr(
        planner.replay,
        "canonical_target_slice",
        lambda path, target_date, pk_columns: (
            vix_calls.append(target_date),
            {"pk_unique": True},
        )[1],
    )
    monkeypatch.setattr(
        planner.replay,
        "validate_taifex_raw_history_parity",
        lambda target_date, allow_historical_unilateral_gaps: (
            historical_parity_calls.append(
                (target_date, allow_historical_unilateral_gaps)
            )
        ),
    )

    planner.validate_recent_structured_source_coverage(
        "20260729",
        count=3,
        allow_historical_structured_absence=True,
    )

    assert calls == [
        ("market_index", "20260727"),
        ("market_index", "20260728"),
        ("market_index", "20260729"),
        ("official_warrant_daily", "20260729"),
        ("taifex_futures_options_vix", "20260729"),
    ]
    assert vix_calls == ["20260727", "20260728"]
    assert historical_parity_calls == [
        ("20260727", True),
        ("20260728", True),
    ]


def test_replay_precondition_keeps_every_taifex_date_strict(monkeypatch) -> None:
    calls: list[tuple[str, str]] = []
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: ["20260728", "20260729"],
    )
    def capture_output(source_id: str, target_date: str) -> dict[str, bool]:
        calls.append((source_id, target_date))
        return {"pk_unique": True}

    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        capture_output,
    )

    planner.validate_recent_structured_source_coverage("20260729", count=2)

    assert calls == [
        ("market_index", "20260728"),
        ("market_index", "20260729"),
        ("official_warrant_daily", "20260728"),
        ("official_warrant_daily", "20260729"),
        ("taifex_futures_options_vix", "20260728"),
        ("taifex_futures_options_vix", "20260729"),
    ]


def test_recent_coverage_rejects_market_duplicate_pk(monkeypatch) -> None:
    target_date = "20260825"
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [target_date],
    )
    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        lambda source_id, date: {
            "pk_unique": source_id != "market_index",
            "components": [
                {"pk_unique": source_id != "market_index"},
            ],
        },
    )

    with pytest.raises(RuntimeError, match="source=market_index.*reason=duplicate_pk"):
        planner.validate_recent_structured_source_coverage(target_date, count=1)


def test_no_replay_older_vix_duplicate_pk_fails_closed(monkeypatch) -> None:
    historical_date = "20260824"
    current_date = "20260825"
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [historical_date, current_date],
    )
    monkeypatch.setattr(
        planner.replay,
        "canonical_target_slice",
        lambda path, target_date, pk_columns: {"pk_unique": False},
    )

    with pytest.raises(RuntimeError, match="source=taiwan_vix.*reason=duplicate_pk"):
        planner.validate_taifex_structured_source_coverage(
            current_date,
            count=2,
            allow_historical_absence=True,
        )


def test_no_replay_current_taifex_duplicate_pk_remains_strict(monkeypatch) -> None:
    current_date = "20260825"
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [current_date],
    )
    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        lambda source_id, target_date: {
            "pk_unique": False,
            "components": [{"pk_unique": False}],
        },
    )

    with pytest.raises(
        RuntimeError,
        match="source=taifex_futures_options_vix.*reason=duplicate_pk",
    ):
        planner.validate_taifex_structured_source_coverage(
            current_date,
            count=1,
            allow_historical_absence=True,
        )


def test_recent_taifex_coverage_allows_20260821_unilateral_history_gap(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    historical_date = "20260821"
    current_date = "20260824"
    history_path = Path("data/futures_options/taifex_institutional_fo_history.csv")
    raw_root = Path("data/futures_options/raw")
    vix_path = Path("data/futures_options/taiwan_vix_history.csv")
    history_path.parent.mkdir(parents=True)
    raw_root.mkdir(parents=True)
    pd.DataFrame(
        [{"date": current_date, "kind": "dealer", "value": "11"}]
    ).to_csv(history_path, index=False)
    pd.DataFrame(
        [{"date": current_date, "kind": "dealer", "value": "11"}]
    ).to_csv(raw_root / f"institutional_fo_{current_date}.csv", index=False)
    pd.DataFrame(
        [
            {"date": historical_date, "value": "17.5"},
            {"date": current_date, "value": "18.0"},
        ]
    ).to_csv(vix_path, index=False)
    monkeypatch.setattr(
        planner.replay,
        "TAIFEX_HISTORY_SPECS",
        {
            "institutional_fo": (history_path, ["date", "kind"]),
            planner.TAIFEX_VIX_SOURCE_ID: (vix_path, ["date"]),
        },
    )
    monkeypatch.setattr(
        planner.replay,
        "TAIFEX_DATED_RAW_SOURCE_IDS",
        ("institutional_fo",),
    )
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [historical_date, current_date],
    )
    build_evidence = planner.replay.build_source_output_evidence
    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        lambda source_id, target_date: (
            build_evidence(source_id, target_date)
            if source_id == "taifex_futures_options_vix"
            else {"pk_unique": True}
        ),
    )

    planner.validate_recent_structured_source_coverage(
        current_date,
        count=2,
        allow_historical_structured_absence=True,
    )


def test_no_replay_warrant_older_both_absent_is_non_blocking(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    historical_date = "20260824"
    current_date = "20260825"
    daily_path = Path(
        f"output/history/warrant_daily/warrant_daily_{current_date}.csv"
    )
    flow_path = Path(
        f"output/history/warrant_flow/warrant_flow_{current_date}.csv"
    )
    daily_path.parent.mkdir(parents=True)
    flow_path.parent.mkdir(parents=True)
    pd.DataFrame(
        [
            {
                "date": current_date,
                "market": "TWSE",
                "warrant_id": "03001P",
            }
        ]
    ).to_csv(daily_path, index=False)
    pd.DataFrame(
        [{"date": current_date, "stock_id": "2330"}]
    ).to_csv(flow_path, index=False)
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [historical_date, current_date],
    )

    evidence = planner.validate_warrant_structured_source_coverage(
        current_date,
        count=2,
        allow_historical_absence=True,
    )

    assert evidence[historical_date] == {
        "historical_absence_status": "paired_artifacts_absent_non_blocking",
        "warrant_daily_path": (
            f"output/history/warrant_daily/warrant_daily_{historical_date}.csv"
        ),
        "warrant_daily_exists": False,
        "warrant_flow_path": (
            f"output/history/warrant_flow/warrant_flow_{historical_date}.csv"
        ),
        "warrant_flow_exists": False,
    }
    assert evidence[current_date]["historical_absence_status"] == "not_applicable"
    assert evidence[current_date]["output_evidence"]["pk_unique"] is True


@pytest.mark.parametrize("present_member", ["warrant_daily", "warrant_flow"])
def test_no_replay_warrant_older_partial_pair_fails_closed(
    tmp_path: Path,
    monkeypatch,
    present_member: str,
) -> None:
    monkeypatch.chdir(tmp_path)
    historical_date = "20260824"
    current_date = "20260825"
    if present_member == "warrant_daily":
        path = Path(
            f"output/history/warrant_daily/warrant_daily_{historical_date}.csv"
        )
        rows = [
            {
                "date": historical_date,
                "market": "TWSE",
                "warrant_id": "03001P",
            }
        ]
    else:
        path = Path(
            f"output/history/warrant_flow/warrant_flow_{historical_date}.csv"
        )
        rows = [{"date": historical_date, "stock_id": "2330"}]
    path.parent.mkdir(parents=True)
    pd.DataFrame(rows).to_csv(path, index=False)
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [historical_date, current_date],
    )

    with pytest.raises(RuntimeError, match="reason=warrant_pair_lineage_mismatch"):
        planner.validate_warrant_structured_source_coverage(
            current_date,
            count=2,
            allow_historical_absence=True,
        )


def test_no_replay_warrant_current_missing_pair_remains_strict(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    current_date = "20260825"
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [current_date],
    )

    with pytest.raises(RuntimeError, match="replay output slice path missing"):
        planner.validate_warrant_structured_source_coverage(
            current_date,
            count=1,
            allow_historical_absence=True,
        )


def test_replay_precondition_warrant_older_missing_pair_remains_strict(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    historical_date = "20260824"
    current_date = "20260825"
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [historical_date, current_date],
    )

    with pytest.raises(RuntimeError, match="replay output slice path missing"):
        planner.validate_warrant_structured_source_coverage(
            current_date,
            count=2,
        )


def test_warrant_strict_builder_rejects_duplicate_component_pk(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    current_date = "20260825"
    daily_path = Path(
        f"output/history/warrant_daily/warrant_daily_{current_date}.csv"
    )
    flow_path = Path(
        f"output/history/warrant_flow/warrant_flow_{current_date}.csv"
    )
    daily_path.parent.mkdir(parents=True)
    flow_path.parent.mkdir(parents=True)
    duplicate = {
        "date": current_date,
        "market": "TWSE",
        "warrant_id": "03001P",
    }
    pd.DataFrame([duplicate, duplicate]).to_csv(daily_path, index=False)
    pd.DataFrame(
        [{"date": current_date, "stock_id": "2330"}]
    ).to_csv(flow_path, index=False)
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [current_date],
    )

    with pytest.raises(RuntimeError, match="reason=duplicate_pk"):
        planner.validate_warrant_structured_source_coverage(
            current_date,
            count=1,
        )


def test_recent_structured_coverage_propagates_internal_gap(monkeypatch) -> None:
    def fail(source_id: str, target_date: str) -> None:
        raise RuntimeError(f"missing structured row {source_id} {target_date}")

    monkeypatch.setattr(planner.replay, "build_source_output_evidence", fail)

    with pytest.raises(RuntimeError, match="missing structured row"):
        planner.validate_recent_structured_source_coverage("20260729", count=1)


def test_operational_coverage_uses_distinct_d0_and_taifex_d1_windows(
    monkeypatch,
) -> None:
    evidence_calls: list[tuple[str, str]] = []
    vix_calls: list[tuple[Path, str, tuple[str, ...]]] = []
    monkeypatch.setattr(
        planner,
        "recent_trading_dates_ending_at",
        lambda end_date, count: [end_date],
    )
    def capture_output(source_id: str, target_date: str) -> dict[str, bool]:
        evidence_calls.append((source_id, target_date))
        return {"pk_unique": True}

    monkeypatch.setattr(
        planner.replay,
        "build_source_output_evidence",
        capture_output,
    )
    monkeypatch.setattr(
        planner.replay,
        "canonical_target_slice",
        lambda path, target_date, pk_columns: (
            vix_calls.append((path, target_date, tuple(pk_columns))),
            {"pk_unique": True},
        )[1],
    )

    planner.validate_operational_structured_source_coverage(
        "20260729",
        taifex_dated_tail_date="20260728",
        warrant_tail_date="20260728",
        count=3,
    )

    assert evidence_calls == [
        ("market_index", "20260729"),
        ("official_warrant_daily", "20260728"),
        ("taifex_futures_options_vix", "20260728"),
    ]
    assert vix_calls == [
        (
            planner.replay.TAIFEX_HISTORY_SPECS["taiwan_vix"][0],
            "20260729",
            tuple(planner.replay.TAIFEX_HISTORY_SPECS["taiwan_vix"][1]),
        )
    ]


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

    with pytest.raises(RuntimeError, match="source-specific operational tail mismatch"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_taifex_dated_tail_older_than_d1() -> None:
    matrix = operational_tail_matrix(taifex_dated_tail="20260727")

    with pytest.raises(RuntimeError, match="must be one common D0 or D-1"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_mixed_taifex_dated_release_dates() -> None:
    matrix = operational_tail_matrix()
    matrix["taifex"][TAIFEX_DATED_SOURCES[0]] = "20260729"

    with pytest.raises(RuntimeError, match="must be one common D0 or D-1"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_lagged_vix_when_other_d0_sources_are_current() -> None:
    matrix = operational_tail_matrix()
    matrix["taifex"]["taiwan_vix"] = "20260728"

    with pytest.raises(RuntimeError, match="D0 structured source tails must share one date"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_mixed_warrant_release_dates() -> None:
    matrix = operational_tail_matrix()
    matrix["warrant_flow"] = "20260728"

    with pytest.raises(RuntimeError, match="warrant source tails must be one common"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_warrant_pair_older_than_d1() -> None:
    matrix = operational_tail_matrix(warrant_tail="20260727")

    with pytest.raises(RuntimeError, match="warrant source tails must be one common"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_lagged_warrant_pair_for_replay_base() -> None:
    matrix = tail_matrix()
    matrix["warrant_daily"] = "20260723"
    matrix["warrant_flow"] = "20260723"

    with pytest.raises(RuntimeError, match="warrant source tails must be one common"):
        planner.plan_from_tail_matrix(matrix, max_replay_dates=3)


def test_plan_rejects_future_taifex_dated_tail() -> None:
    matrix = operational_tail_matrix(taifex_dated_tail="20260730")

    with pytest.raises(RuntimeError, match="must be one common D0 or D-1"):
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
        planner.plan_from_tail_matrix(tail_matrix(), max_replay_dates=1)


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
