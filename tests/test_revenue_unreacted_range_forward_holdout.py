from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_daily_model_parameter_research as parameter_research  # noqa: E402
import revenue_unreacted_range_forward_holdout as holdout_module  # noqa: E402
import revenue_unreacted_range_research_frame as research_frame_module  # noqa: E402
import validate_revenue_unreacted_range_forward_holdout as holdout_validator  # noqa: E402
from revenue_unreacted_range_forward_holdout import (  # noqa: E402
    BRIDGE_END_DATE,
    BRIDGE_START_DATE,
    CHALLENGER_VARIANT_IDS,
    CONFIRMATION_VARIANT_ID,
    HOLDING_DAYS,
    HOLDING_SESSION_INDEX_OFFSET,
    HOLDOUT_START_DATE,
    PR462_PROJECTED_EPISODE_ROW_COUNT,
    PR462_PROJECTED_EPISODE_SEMANTIC_SHA256,
    PREREGISTRATION_MERGE_COMMIT,
    PRIMARY_VARIANT_ID,
    RULE_CANONICAL_SHA256,
    STOP_POLICY_ID,
    TRAINING_CUTOFF_DATE,
    build_forward_holdout,
    validate_append_only_history,
    write_forward_holdout as _write_forward_holdout,
)


GENERATED_AT = "2026-08-11 12:00:00 Asia/Taipei"
ANCHOR_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
EXPECTED_VARIANTS = {
    "source_mid_falling",
    "source_low_falling",
    "source_low_or_mid_falling_union",
}


@pytest.fixture(autouse=True)
def _accept_synthetic_training_projection_pair(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        holdout_validator,
        "validate_projection_binding_frames",
        lambda *_args, **_kwargs: [],
    )


def _flag(value: object) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes"}


def _price_frame(
    *,
    trigger_dates: tuple[str, ...],
    position: str,
    return_pct: float = 10.0,
    end_date: str = "20261030",
    source_date: str = "20260617",
) -> pd.DataFrame:
    dates = pd.bdate_range("2025-11-03", pd.Timestamp(end_date)).strftime("%Y%m%d")
    frame = pd.DataFrame(
        {
            "date": dates,
            "analysis_open": 100.0,
            "analysis_high": 101.0,
            "analysis_low": 99.0,
            "analysis_close": 100.0,
            "open": 100.0,
            "high": 101.0,
            "low": 99.0,
            "close": 100.0,
            "price_resolution_ids_on_date": "",
        }
    )
    source_index = int(frame.index[frame["date"].eq(source_date)][0])
    target = 90.0 if position == "low" else 100.0
    falling = np.linspace(112.0, target, 26)
    frame.loc[source_index - 25 : source_index, "analysis_close"] = falling
    frame.loc[source_index - 25 : source_index, "close"] = falling
    frame.loc[source_index - 25 : source_index, "analysis_open"] = falling
    frame.loc[source_index - 25 : source_index, "open"] = falling
    frame.loc[source_index - 25 : source_index, "analysis_high"] = falling + 1.0
    frame.loc[source_index - 25 : source_index, "high"] = falling + 1.0
    frame.loc[source_index - 25 : source_index, "analysis_low"] = falling - 1.0
    frame.loc[source_index - 25 : source_index, "low"] = falling - 1.0
    frame.at[source_index - 100, "analysis_high"] = 120.0
    frame.at[source_index - 100, "high"] = 120.0
    frame.at[source_index - 99, "analysis_low"] = 80.0
    frame.at[source_index - 99, "low"] = 80.0

    trigger_indices = [
        int(frame.index[frame["date"].eq(trigger_date)][0])
        for trigger_date in trigger_dates
        if len(frame.index[frame["date"].eq(trigger_date)])
    ]
    level = 100.0
    cursor = source_index + 1
    for trigger_index in trigger_indices:
        if cursor < trigger_index:
            frame.loc[cursor : trigger_index - 1, ["analysis_close", "close"]] = level
        frame.loc[trigger_index, ["analysis_close", "close"]] = level + 1.0
        if trigger_index + 1 < len(frame):
            frame.loc[trigger_index + 1, ["analysis_close", "close"]] = level + 3.0
        level += 3.0
        cursor = trigger_index + 2
    if cursor < len(frame):
        frame.loc[cursor:, ["analysis_close", "close"]] = level

    for trigger_index in trigger_indices:
        entry_index = trigger_index + 2
        exit_index = entry_index + HOLDING_SESSION_INDEX_OFFSET
        if entry_index < len(frame):
            frame.at[entry_index, "analysis_open"] = 100.0
            frame.at[entry_index, "open"] = 100.0
        if exit_index < len(frame):
            exit_close = 100.0 * (1.0 + return_pct / 100.0)
            frame.at[exit_index, "analysis_close"] = exit_close
            frame.at[exit_index, "close"] = exit_close

    # Every declared trigger is a genuine close crossover under the frozen
    # previous-20-close formula, even when an earlier D+30 exit is inside the
    # later trigger's lookback window.
    for trigger_index in trigger_indices:
        previous_high = float(
            frame["analysis_close"].iloc[trigger_index - 20 : trigger_index].max()
        )
        frame.loc[trigger_index, ["analysis_close", "close"]] = previous_high + 1.0
        if trigger_index + 1 < len(frame):
            frame.loc[trigger_index + 1, ["analysis_close", "close"]] = (
                previous_high + 3.0
            )

    close = frame["analysis_close"]
    frame["analysis_high"] = np.maximum(frame["analysis_high"], close + 1.0)
    frame["high"] = np.maximum(frame["high"], frame["close"] + 1.0)
    frame["analysis_low"] = np.minimum(frame["analysis_low"], close - 1.0)
    frame["low"] = np.minimum(frame["low"], frame["close"] - 1.0)
    frame["ma60"] = close.rolling(60, min_periods=60).mean()
    frame["ma120"] = close.rolling(120, min_periods=120).mean()
    frame["analysis_ema23"] = close.ewm(span=23, adjust=False).mean()
    previous_high = close.shift(1).rolling(20, min_periods=20).max()
    breakout = close.gt(previous_high)
    frame["cross_breakout_prev20"] = breakout & ~breakout.shift(
        1, fill_value=False
    ).astype(bool)
    return frame.reset_index(drop=True)


def _source_row(
    *,
    stock_id: str,
    position: str,
    anomaly_candidate: bool = False,
    source_date: str = "20260617",
) -> dict[str, object]:
    source_sequence_index = len(
        pd.bdate_range("2025-11-03", pd.Timestamp(source_date))
    ) - 1
    return {
        "generated_at": "2026-07-31 19:12:03 Asia/Taipei",
        "model_id": "revenue_unreacted_range",
        "artifact_id": "revenue_unreacted_range_source_first_condition_audit",
        "artifact_version": "source_first_condition_v3_20260720",
        "monthly_revenue_history_blob_sha256": "1" * 64,
        "monthly_revenue_canonical_table_sha256": "2" * 64,
        "cross_market_resolution_registry_canonical_sha256": "3" * 64,
        "condition_variant_id": "absolute_or_two_month_yoy_ge15",
        "episode_key": f"episode-{stock_id}",
        "stock_id": stock_id,
        "stock_name": f"測試{stock_id}",
        "episode_start_revenue_period": "202605",
        "episode_start_source_date": source_date,
        "episode_start_cross_market_resolution_id": "none",
        "episode_start_source_row_canonical_sha256": "4" * 64,
        "episode_start_canonical_source_table_date": source_date,
        "episode_start_trade_date": source_date,
        "episode_start_sequence_index": source_sequence_index,
        "latest_qualifying_revenue_period": "202605",
        "latest_qualifying_source_date": source_date,
        "latest_qualifying_cross_market_resolution_id": "none",
        "latest_qualifying_source_row_canonical_sha256": "4" * 64,
        "latest_qualifying_canonical_source_table_date": source_date,
        "latest_qualifying_trade_date": source_date,
        "latest_qualifying_sequence_index": source_sequence_index,
        "qualifying_update_count": 1,
        "qualifying_revenue_periods": "202605",
        "qualifying_source_dates": source_date,
        "qualifying_cross_market_resolution_ids": "none",
        "qualifying_source_row_canonical_sha256s": "4" * 64,
        "qualifying_canonical_source_table_dates": source_date,
        "qualifying_trade_dates": source_date,
        "qualifying_sequence_indices": str(source_sequence_index),
        "start_source_revenue_anomaly_candidate_flag": anomaly_candidate,
        "qualifying_source_revenue_anomaly_candidate_flags": str(anomaly_candidate),
        "qualifying_source_revenue_anomaly_candidate_flag": anomaly_candidate,
        "unresolved_price_path_candidate_flag": False,
        "episode_end_date": TRAINING_CUTOFF_DATE,
        "episode_status": "right_censored_before_active_horizon",
        "first_breakout_date": "",
        "first_breakout_outcome": "no_breakout_observed_by_training_cutoff",
        "launch_date": "",
        "same_stock_non_overlap_applied": True,
        # These are evidence-only fixture hints.  The producer must still derive
        # the classification from the point-in-time price anchor.
        "expected_source_position_bucket": position,
        "expected_source_shape_bucket": "falling",
        "approved_for_daily": False,
        "production_change": False,
    }


def _append_qualifying_update(
    source_row: dict[str, object],
    price: pd.DataFrame,
    *,
    source_date: str,
    revenue_period: str = "202607",
    row_sha: str = "7" * 64,
) -> None:
    sequence_index = int(price.index[price["date"].astype(str).eq(source_date)][0])
    source_row.update(
        {
            "latest_qualifying_revenue_period": revenue_period,
            "latest_qualifying_source_date": source_date,
            "latest_qualifying_source_row_canonical_sha256": row_sha,
            "latest_qualifying_canonical_source_table_date": source_date,
            "latest_qualifying_trade_date": source_date,
            "latest_qualifying_sequence_index": sequence_index,
            "qualifying_update_count": 2,
            "qualifying_revenue_periods": (
                f"{source_row['episode_start_revenue_period']}|{revenue_period}"
            ),
            "qualifying_source_dates": (
                f"{source_row['episode_start_source_date']}|{source_date}"
            ),
            "qualifying_cross_market_resolution_ids": "none|none",
            "qualifying_source_row_canonical_sha256s": (
                f"{source_row['episode_start_source_row_canonical_sha256']}|{row_sha}"
            ),
            "qualifying_canonical_source_table_dates": (
                f"{source_row['episode_start_canonical_source_table_date']}|{source_date}"
            ),
            "qualifying_trade_dates": (
                f"{source_row['episode_start_trade_date']}|{source_date}"
            ),
            "qualifying_sequence_indices": (
                f"{source_row['episode_start_sequence_index']}|{sequence_index}"
            ),
            "qualifying_source_revenue_anomaly_candidate_flags": "False|False",
            "qualifying_source_revenue_anomaly_candidate_flag": False,
        }
    )


def _source_manifest(_fixture_episode_count: int = 0) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "generated_at": "2026-07-31 19:12:03 Asia/Taipei",
                "model_id": "revenue_unreacted_range",
                "artifact_id": "revenue_unreacted_range_source_snapshot_projection",
                "artifact_version": "source_snapshot_projection_v1_20260731",
                "projection_id": "revenue_unreacted_range_source_snapshot_asof_20260713",
                "projection_version": "source_snapshot_projection_v1_20260731",
                "projection_policy_id": "raw_source_and_price_truncated_before_source_first_episode_assembly_v1",
                "cutoff_date": TRAINING_CUTOFF_DATE,
                "projected_episode_row_count": PR462_PROJECTED_EPISODE_ROW_COUNT,
                "projected_episode_semantic_sha256": (
                    PR462_PROJECTED_EPISODE_SEMANTIC_SHA256
                ),
                "monthly_revenue_history_blob_sha256": "1" * 64,
                "monthly_revenue_canonical_table_sha256": "2" * 64,
                "cross_market_resolution_registry_canonical_sha256": "3" * 64,
                "cutoff_price_input_semantic_sha256": "6" * 64,
                "research_only": True,
                "formal_model_use_allowed": False,
                "approved_for_daily": False,
                "production_change": False,
                "promotion_evidence_allowed": False,
                "ranking_consumption_allowed": False,
                "pdf_consumption_allowed": False,
            }
        ]
    )


def holdout_inputs() -> tuple[pd.DataFrame, dict[str, pd.DataFrame], pd.DataFrame]:
    specs = (
        ("1111", "mid", ("20260804",), 10.0, "20261030", True),
        ("2222", "low", ("20260805",), -5.0, "20261030", False),
        # The price history ends before entry + 29, so this event is censored.
        ("3333", "mid", ("20260806",), 20.0, "20260828", False),
        # Bridge-period signal: counted as excluded evidence, never a holdout row.
        ("4444", "mid", ("20260803",), 5.0, "20261030", False),
    )
    rows: list[dict[str, object]] = []
    daily: dict[str, pd.DataFrame] = {}
    for stock_id, position, triggers, return_pct, end_date, anomaly in specs:
        rows.append(
            _source_row(
                stock_id=stock_id,
                position=position,
                anomaly_candidate=anomaly,
            )
        )
        daily[stock_id] = _price_frame(
            trigger_dates=triggers,
            position=position,
            return_pct=return_pct,
            end_date=end_date,
        )
    source = pd.DataFrame(rows)
    return source, daily, _source_manifest(len(source))


def write_forward_holdout(
    *frames: pd.DataFrame,
    replay_source_detail: pd.DataFrame | None = None,
    **kwargs: object,
) -> dict[str, Path]:
    """Exercise the production 17-path writer with an exact raw source input."""

    if replay_source_detail is None:
        replay_source_detail = holdout_inputs()[0]
    return _write_forward_holdout(
        *frames,
        replay_source_detail=replay_source_detail,
        **kwargs,
    )


def _build():
    source, daily, source_manifest = holdout_inputs()
    outputs = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    assert len(outputs) == 5
    return (*outputs, source, daily, source_manifest)


def test_preregistered_contract_and_bridge_period_are_frozen() -> None:
    manifest, detail, summary, comparison, anomaly, *_ = _build()

    assert PREREGISTRATION_MERGE_COMMIT == ANCHOR_COMMIT
    assert TRAINING_CUTOFF_DATE == "20260713"
    assert BRIDGE_START_DATE == "20260714"
    assert BRIDGE_END_DATE == "20260803"
    assert HOLDOUT_START_DATE == "20260804"
    assert PRIMARY_VARIANT_ID == "source_mid_falling"
    assert set(CHALLENGER_VARIANT_IDS) == {
        "source_low_falling",
        "source_low_or_mid_falling_union",
    }
    assert CONFIRMATION_VARIANT_ID == "delayed_next_close_continuation_bonus"
    assert STOP_POLICY_ID == "none_no_stop_reference"
    assert HOLDING_DAYS == 30
    assert HOLDING_SESSION_INDEX_OFFSET == 29
    assert len(RULE_CANONICAL_SHA256) == 64

    row = manifest.iloc[0]
    assert row["preregistration_merge_commit"] == ANCHOR_COMMIT
    assert row["rule_canonical_sha256"] == RULE_CANONICAL_SHA256
    assert str(row["training_cutoff_date"]) == TRAINING_CUTOFF_DATE
    assert str(row["holdout_start_date"]) == HOLDOUT_START_DATE
    assert int(row["bridge_excluded_signal_count"]) >= 1
    assert detail["trigger_date"].astype(str).min() >= HOLDOUT_START_DATE
    assert not detail["trigger_date"].astype(str).between(
        BRIDGE_START_DATE, BRIDGE_END_DATE
    ).any()
    assert set(summary["variant_id"].astype(str)) == EXPECTED_VARIANTS
    assert set(comparison["variant_id"].astype(str)) == EXPECTED_VARIANTS
    assert not anomaly.empty


def test_pr462_projection_is_exactly_pinned_and_drift_fails_closed() -> None:
    source, daily, source_manifest = holdout_inputs()
    assert int(source_manifest.iloc[0]["projected_episode_row_count"]) == 19569
    assert (
        source_manifest.iloc[0]["projected_episode_semantic_sha256"]
        == "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
    )
    manifest, *_ = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    assert int(manifest.iloc[0]["training_source_projected_episode_row_count"]) == 19569
    assert (
        manifest.iloc[0]["training_source_projection_semantic_sha256"]
        == PR462_PROJECTED_EPISODE_SEMANTIC_SHA256
    )

    for column, corrupt_value in (
        ("projected_episode_row_count", PR462_PROJECTED_EPISODE_ROW_COUNT + 1),
        ("projected_episode_row_count", PR462_PROJECTED_EPISODE_ROW_COUNT + 0.9),
        ("projected_episode_semantic_sha256", "f" * 64),
    ):
        corrupted = source_manifest.copy()
        corrupted[column] = corrupted[column].astype(object)
        corrupted.at[0, column] = corrupt_value
        with pytest.raises(
            RuntimeError,
            match="PR462 projected episode|exact integer",
        ):
            build_forward_holdout(
                source,
                daily,
                source_manifest=corrupted,
                generated_at=GENERATED_AT,
            )

    for column in ("research_only", "formal_model_use_allowed"):
        corrupted = source_manifest.copy()
        corrupted[column] = corrupted[column].astype(object)
        corrupted.at[0, column] = "not-a-boolean"
        with pytest.raises(RuntimeError, match="canonical boolean"):
            build_forward_holdout(
                source,
                daily,
                source_manifest=corrupted,
                generated_at=GENERATED_AT,
            )

    for column in (
        "unresolved_price_path_candidate_flag",
        "qualifying_source_revenue_anomaly_candidate_flag",
        "qualifying_source_revenue_anomaly_candidate_flags",
    ):
        corrupted_source = source.copy()
        corrupted_source[column] = corrupted_source[column].astype(object)
        corrupted_source.at[corrupted_source.index[0], column] = "not-a-boolean"
        with pytest.raises(RuntimeError, match="source anomaly.*canonical boolean"):
            build_forward_holdout(
                corrupted_source,
                daily,
                source_manifest=source_manifest,
                generated_at=GENERATED_AT,
            )

    for column, value in (
        ("qualifying_update_count", 1.9),
        ("episode_start_sequence_index", 100.5),
        ("latest_qualifying_sequence_index", 100.5),
        ("qualifying_sequence_indices", "100.5"),
    ):
        corrupted_source = source.copy()
        corrupted_source[column] = corrupted_source[column].astype(object)
        corrupted_source.at[corrupted_source.index[0], column] = value
        with pytest.raises(RuntimeError, match="exact integer|sequence.*contract"):
            build_forward_holdout(
                corrupted_source,
                daily,
                source_manifest=source_manifest,
                generated_at=GENERATED_AT,
            )


def test_point_in_time_source_and_d2_entry_d30_close_contract() -> None:
    _manifest, detail, *_ = _build()
    row = detail.loc[
        detail["variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["stock_id"].astype(str).eq("1111")
    ].iloc[0]

    price = _price_frame(trigger_dates=("20260804",), position="mid")
    dates = price["date"].astype(str).tolist()
    trigger_index = dates.index("20260804")
    entry_index = trigger_index + 2
    exit_index = entry_index + HOLDING_SESSION_INDEX_OFFSET
    assert str(row["source_asof_date"]) == "20260617"
    for column in (
        "source_asof_date",
        "source_asof_trade_date",
        "source_asof_canonical_source_table_date",
    ):
        assert str(row[column]) <= str(row["trigger_date"])
    assert int(row["source_asof_sequence_index"]) <= int(row["trigger_index"])
    assert str(row["confirmation_date"]) == dates[trigger_index + 1]
    assert str(row["entry_date"]) == dates[entry_index]
    assert str(row["planned_exit_date"]) == dates[exit_index]
    assert str(row["exit_date"]) == dates[exit_index]
    assert row["entry_price_basis"] == "analysis_open"
    assert row["exit_price_basis"] == "analysis_close"
    assert int(row["holding_session_index_offset"]) == 29
    assert _flag(row["return_valid"])
    assert not _flag(row["right_censored"])


def test_future_qualifying_anomaly_update_does_not_pollute_asof_flag() -> None:
    source_date = "20260617"
    future_date = "20260805"
    source_row = _source_row(
        stock_id="7777",
        position="mid",
        anomaly_candidate=False,
        source_date=source_date,
    )
    price = _price_frame(
        trigger_dates=("20260804",),
        position="mid",
        source_date=source_date,
    )
    future_index = int(price.index[price["date"].astype(str).eq(future_date)][0])
    source_row.update(
        {
            "latest_qualifying_revenue_period": "202607",
            "latest_qualifying_source_date": future_date,
            "latest_qualifying_source_row_canonical_sha256": "7" * 64,
            "latest_qualifying_canonical_source_table_date": future_date,
            "latest_qualifying_trade_date": future_date,
            "latest_qualifying_sequence_index": future_index,
            "qualifying_update_count": 2,
            "qualifying_revenue_periods": "202605|202607",
            "qualifying_source_dates": f"{source_date}|{future_date}",
            "qualifying_cross_market_resolution_ids": "none|none",
            "qualifying_source_row_canonical_sha256s": f"{'4' * 64}|{'7' * 64}",
            "qualifying_canonical_source_table_dates": f"{source_date}|{future_date}",
            "qualifying_trade_dates": f"{source_date}|{future_date}",
            "qualifying_sequence_indices": (
                f"{source_row['episode_start_sequence_index']}|{future_index}"
            ),
            "qualifying_source_revenue_anomaly_candidate_flags": "False|True",
            "qualifying_source_revenue_anomaly_candidate_flag": True,
        }
    )
    _manifest, detail, *_ = build_forward_holdout(
        pd.DataFrame([source_row]),
        {"7777": price},
        source_manifest=_source_manifest(),
        generated_at=GENERATED_AT,
    )
    row = detail.iloc[0]
    assert str(row["trigger_date"]) == "20260804"
    assert str(row["source_asof_date"]) == source_date
    assert int(row["future_qualifying_update_ignored_count"]) == 1
    assert not _flag(row["source_anomaly_candidate_flag"])
    assert not _flag(row["anomaly_candidate_flag"])


def test_expired_watch_trigger_does_not_block_later_qualifying_update() -> None:
    first_source_date = "20260323"
    later_source_date = "20260817"
    price = _price_frame(
        trigger_dates=("20260804", "20260818"),
        position="mid",
        source_date=later_source_date,
    )
    source_row = _source_row(
        stock_id="7780",
        position="mid",
        source_date=first_source_date,
    )
    _append_qualifying_update(
        source_row,
        price,
        source_date=later_source_date,
    )

    outputs = build_forward_holdout(
        pd.DataFrame([source_row]),
        {"7780": price},
        source_manifest=_source_manifest(),
        generated_at=GENERATED_AT,
    )
    _manifest, detail, *_ = outputs

    # 20260804 is 96 sessions after the only then-available revenue source, so
    # it is outside the frozen watch universe and cannot consume the lifecycle.
    # The 20260817 revenue update opens a new watch window for 20260818.
    assert detail["trigger_date"].astype(str).tolist() == ["20260818"]
    assert detail["source_asof_date"].astype(str).tolist() == [later_source_date]
    assert detail["source_to_trigger_trading_days"].astype(int).tolist() == [1]
    assert holdout_validator.validate_frames(
        *outputs,
        source_detail=pd.DataFrame([source_row]),
        daily_by_stock={"7780": price},
        source_manifest=_source_manifest(),
        training_source_projection_detail=pd.DataFrame(
            [{"synthetic_training_projection": "v1"}]
        ),
    ) == []


def test_in_horizon_nonmember_trigger_still_consumes_full_universe_lifecycle() -> None:
    first_source_date = "20260731"
    later_source_date = "20260817"
    source_row = _source_row(
        stock_id="7781",
        position="mid",
        source_date=first_source_date,
    )
    price = _price_frame(
        trigger_dates=("20260804", "20260820"),
        position="mid",
        source_date=later_source_date,
    )
    _append_qualifying_update(
        source_row,
        price,
        source_date=later_source_date,
    )
    source = pd.DataFrame([source_row])
    outputs = build_forward_holdout(
        source,
        {"7781": price},
        source_manifest=_source_manifest(),
        generated_at=GENERATED_AT,
    )

    # The in-horizon 20260804 operation is part of PR #462's full source
    # universe even though its then-current source anchor is not low/mid
    # falling.  It therefore blocks the later low/mid event until D+30 exit.
    assert outputs[1].empty
    assert holdout_validator.validate_frames(
        *outputs,
        source_detail=source,
        daily_by_stock={"7781": price},
        source_manifest=_source_manifest(),
        training_source_projection_detail=pd.DataFrame(
            [{"synthetic_training_projection": "v1"}]
        ),
    ) == []

    # Without that earlier source-valid operation, the later qualifier/trigger
    # is independently eligible.  This pins lifecycle-before-stratification,
    # not a fixture that simply lacks a low/mid candidate.
    later_only_price = _price_frame(
        trigger_dates=("20260820",),
        position="mid",
        source_date=later_source_date,
    )
    later_only = build_forward_holdout(
        source,
        {"7781": later_only_price},
        source_manifest=_source_manifest(),
        generated_at=GENERATED_AT,
    )
    assert later_only[1]["trigger_date"].astype(str).tolist() == ["20260820"]


def test_source_canonical_table_date_after_trigger_fails_closed() -> None:
    source = pd.DataFrame([_source_row(stock_id="7788", position="mid")])
    source.at[0, "qualifying_canonical_source_table_dates"] = "20260805"
    source.at[0, "episode_start_canonical_source_table_date"] = "20260805"
    source.at[0, "latest_qualifying_canonical_source_table_date"] = "20260805"
    price = _price_frame(trigger_dates=("20260804",), position="mid")
    with pytest.raises(RuntimeError, match="as-of date exceeds trigger"):
        build_forward_holdout(
            source,
            {"7788": price},
            source_manifest=_source_manifest(),
            generated_at=GENERATED_AT,
        )


def test_right_censored_event_is_not_in_mature_metrics() -> None:
    _manifest, detail, summary, comparison, anomaly, *_ = _build()
    censored = detail.loc[
        detail["variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["stock_id"].astype(str).eq("3333")
    ].iloc[0]
    primary = summary.loc[summary["variant_id"].eq(PRIMARY_VARIANT_ID)].iloc[0]

    assert censored["operation_status"] == "right_censored_before_d30"
    assert _flag(censored["right_censored"])
    assert not _flag(censored["return_valid"])
    assert pd.isna(pd.to_numeric(pd.Series([censored["realized_return_pct"]]), errors="coerce").iloc[0])
    assert int(primary["right_censored_count"]) >= 1
    assert int(primary["mature_count"]) == int(
        detail.loc[
            detail["variant_id"].eq(PRIMARY_VARIANT_ID)
            & detail["return_valid"].map(_flag)
        ].shape[0]
    )
    assert int(
        comparison.loc[
            comparison["variant_id"].eq(PRIMARY_VARIANT_ID), "mature_count"
        ].iloc[0]
    ) == int(primary["mature_count"])
    assert "right_censored_count" in anomaly.columns


def test_same_stock_rearm_starts_only_after_prior_realized_exit() -> None:
    price = _price_frame(
        trigger_dates=("20260804", "20260820", "20260918"),
        position="mid",
        return_pct=8.0,
        end_date="20261130",
        source_date="20260713",
    )
    source = pd.DataFrame(
        [_source_row(stock_id="5555", position="mid", source_date="20260713")]
    )
    outputs = build_forward_holdout(
        source,
        {"5555": price},
        source_manifest=_source_manifest(1),
        generated_at=GENERATED_AT,
    )
    _manifest, detail, summary, _comparison, _anomaly = outputs
    primary = detail.loc[detail["variant_id"].eq(PRIMARY_VARIANT_ID)].sort_values(
        "entry_date", kind="mergesort"
    )

    assert primary["trigger_date"].astype(str).tolist() == ["20260804", "20260918"]
    assert (
        primary["entry_date"].astype(str).iloc[1]
        > primary["exit_date"].astype(str).iloc[0]
    )
    assert int(
        summary.loc[
            summary["variant_id"].eq(PRIMARY_VARIANT_ID),
            "same_stock_overlap_pair_count",
        ].iloc[0]
    ) == 0


def test_primary_challengers_share_operation_contract_and_union_is_not_duplicated() -> None:
    _manifest, detail, summary, comparison, *_ = _build()
    # Detail stores each event once under its disjoint source cell.  The union
    # challenger is derived by membership in the comparison artifact.
    assert set(detail["variant_id"].astype(str)) == {
        "source_mid_falling",
        "source_low_falling",
    }
    contract_columns = (
        "confirmation_variant_id",
        "entry_price_basis",
        "holding_days",
        "holding_session_index_offset",
        "exit_price_basis",
        "stop_policy_id",
    )
    for column in contract_columns:
        assert detail.groupby("variant_id")[column].nunique(dropna=False).max() == 1
        assert detail[column].nunique(dropna=False) == 1
    assert (summary["same_stock_overlap_pair_count"].astype(int) == 0).all()
    assert (comparison["same_stock_overlap_pair_count"].astype(int) == 0).all()

    assert not detail.duplicated(["stock_id", "episode_key", "trigger_date"]).any()
    union_count = int(
        comparison.loc[
            comparison["variant_id"].eq("source_low_or_mid_falling_union"),
            "event_count",
        ].iloc[0]
    )
    assert union_count == len(
        detail[["stock_id", "episode_key", "trigger_date"]].drop_duplicates()
    )


def test_anomaly_candidates_remain_primary_and_only_sensitivity_excludes() -> None:
    _manifest, detail, summary, _comparison, anomaly, *_ = _build()
    row = detail.loc[
        detail["variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["stock_id"].astype(str).eq("1111")
    ].iloc[0]
    primary_summary = summary.loc[
        summary["variant_id"].eq(PRIMARY_VARIANT_ID)
    ].iloc[0]
    primary_anomaly = anomaly.loc[
        anomaly["variant_id"].eq(PRIMARY_VARIANT_ID)
        & anomaly["analysis_basis"].eq("primary_candidate_retaining")
    ].iloc[0]
    sensitivity = anomaly.loc[
        anomaly["variant_id"].eq(PRIMARY_VARIANT_ID)
        & anomaly["analysis_basis"].eq(
            "excluding_unresolved_anomaly_candidates_sensitivity"
        )
    ].iloc[0]

    assert _flag(row["anomaly_candidate_flag"])
    assert _flag(row["primary_metric_included"])
    assert not _flag(row["sensitivity_metric_included"])
    assert int(primary_summary["anomaly_candidate_count"]) >= 1
    assert int(primary_anomaly["mature_count"]) == int(primary_summary["mature_count"])
    assert int(sensitivity["mature_count"]) < int(primary_anomaly["mature_count"])


def test_only_censored_events_report_holdout_accumulating() -> None:
    source = pd.DataFrame([_source_row(stock_id="6666", position="mid")])
    price = _price_frame(
        trigger_dates=("20260806",),
        position="mid",
        end_date="20260828",
    )
    manifest, detail, summary, comparison, _anomaly = build_forward_holdout(
        source,
        {"6666": price},
        source_manifest=_source_manifest(1),
        generated_at=GENERATED_AT,
    )

    assert manifest.iloc[0]["holdout_status"] == "holdout_accumulating"
    assert int(manifest.iloc[0]["primary_mature_count"]) == 0
    assert detail["right_censored"].map(_flag).all()
    assert (summary["mature_count"].astype(int) == 0).all()
    assert (comparison["mature_count"].astype(int) == 0).all()
    for column in ("win_rate_pct", "average_return_pct", "median_return_pct"):
        assert pd.to_numeric(summary[column], errors="coerce").isna().all()


@pytest.mark.parametrize(
    "column",
    ("analysis_ema23", "cross_breakout_prev20"),
)
def test_frozen_price_features_reject_precomputed_input_drift(column: str) -> None:
    source, daily, source_manifest = holdout_inputs()
    corrupted = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    target = corrupted["1111"]
    row = target.index[-1]
    if column == "cross_breakout_prev20":
        target.at[row, column] = not bool(target.at[row, column])
    else:
        target.at[row, column] = float(target.at[row, column]) + 0.5

    with pytest.raises(RuntimeError, match="derived price field.*frozen"):
        build_forward_holdout(
            source,
            corrupted,
            source_manifest=source_manifest,
            generated_at=GENERATED_AT,
        )


def test_pr462_authoritative_prepared_ma_rounding_remains_accepted() -> None:
    source, daily, source_manifest = holdout_inputs()
    rounded = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    for frame in rounded.values():
        frame["ma60"] = pd.to_numeric(frame["ma60"], errors="coerce").round(4)
        frame["ma120"] = pd.to_numeric(frame["ma120"], errors="coerce").round(4)

    _manifest, detail, *_ = build_forward_holdout(
        source,
        rounded,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    assert set(detail["stock_id"].astype(str)) == {"1111", "2222", "3333"}


def test_append_only_history_rejects_prior_row_mutation() -> None:
    manifest, *_ = _build()
    validate_append_only_history(manifest.copy(), manifest.copy())

    mutated = deepcopy(manifest)
    mutated.loc[mutated.index[0], "rule_canonical_sha256"] = "f" * 64
    with pytest.raises(RuntimeError, match="append-only"):
        validate_append_only_history(manifest, mutated)


def test_empty_history_accepts_one_capture_and_rejects_two_capture_batch() -> None:
    manifest, *_ = _build()
    empty = manifest.iloc[0:0].copy()
    second_capture = manifest.copy()
    second_capture["capture_id"] = "f" * 64
    batched = pd.concat([manifest, second_capture], ignore_index=True)

    validate_append_only_history(empty, manifest)
    validate_append_only_history(empty, manifest, immutable_base=empty.copy())
    with pytest.raises(RuntimeError, match="multiple captures"):
        validate_append_only_history(empty, batched)
    with pytest.raises(RuntimeError, match="multiple captures"):
        validate_append_only_history(empty, batched, immutable_base=empty.copy())


def test_append_only_history_rejects_clean_uncommitted_capture_before_third_append() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )[0]
    daily_second = {key: value.copy() for key, value in daily.items()}
    last = daily_second["1111"].index[-1]
    daily_second["1111"].at[last, "price_resolution_ids_on_date"] = "revision-1"
    second = build_forward_holdout(
        source,
        daily_second,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )[0]
    daily_third = {key: value.copy() for key, value in daily_second.items()}
    daily_third["1111"].at[last, "price_resolution_ids_on_date"] = "revision-2"
    third = build_forward_holdout(
        source,
        daily_third,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:20:00 Asia/Taipei",
    )[0]
    existing = pd.concat([first, second], ignore_index=True)

    with pytest.raises(RuntimeError, match="uncommitted history tail"):
        validate_append_only_history(
            existing,
            third,
            immutable_base=first,
        )


def test_append_only_history_rejects_rewritten_uncommitted_current_capture() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )[0]
    daily["1111"].at[
        daily["1111"].index[-1], "price_resolution_ids_on_date"
    ] = "revision-1"
    second = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )[0]
    existing = pd.concat([first, second], ignore_index=True)
    existing.at[len(first), "rule_canonical_sha256"] = "f" * 64

    with pytest.raises(RuntimeError, match="uncommitted history tail rewrite"):
        validate_append_only_history(
            existing,
            second,
            immutable_base=first,
        )


def test_append_only_history_allows_idempotent_uncommitted_current_capture() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )[0]
    daily["1111"].at[
        daily["1111"].index[-1], "price_resolution_ids_on_date"
    ] = "revision-1"
    second = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )[0]

    validate_append_only_history(
        pd.concat([first, second], ignore_index=True),
        second.assign(generated_at="2026-08-11 12:11:00 Asia/Taipei"),
        immutable_base=first,
    )


def test_append_only_history_rejects_stale_existing_capture_as_current() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )[0]
    daily["1111"].at[
        daily["1111"].index[-1], "price_resolution_ids_on_date"
    ] = "revision-1"
    second = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )[0]
    committed = pd.concat([first, second], ignore_index=True)

    validate_append_only_history(committed, second, immutable_base=committed)
    with pytest.raises(RuntimeError, match="current capture is stale"):
        validate_append_only_history(committed, first, immutable_base=committed)


def test_append_only_history_rejects_current_capture_row_reordering() -> None:
    _manifest, detail, *_ = _build()
    reordered = detail.iloc[::-1].reset_index(drop=True)

    with pytest.raises(RuntimeError, match="row order drift"):
        validate_append_only_history(detail, reordered, immutable_base=detail)


def test_append_only_history_rejects_truncated_nonempty_immutable_base() -> None:
    manifest, *_ = _build()

    with pytest.raises(RuntimeError, match="immutable base prefix drift"):
        validate_append_only_history(
            manifest.iloc[0:0].copy(),
            manifest,
            immutable_base=manifest,
        )


def test_new_capture_requires_immutable_history_base() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )[0]
    daily["1111"].at[
        daily["1111"].index[-1], "price_resolution_ids_on_date"
    ] = "revision-1"
    second = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )[0]

    with pytest.raises(RuntimeError, match="immutable base is required"):
        validate_append_only_history(first, second)


def test_immutable_git_base_prefix_includes_generated_at() -> None:
    manifest, *_ = _build()
    tampered_base = manifest.copy()
    tampered_base.at[0, "generated_at"] = "2099-01-01 00:00:00 Asia/Taipei"

    with pytest.raises(RuntimeError, match="immutable base prefix drift"):
        validate_append_only_history(
            manifest,
            manifest,
            immutable_base=tampered_base,
        )


def test_empty_immutable_base_cannot_authorize_prior_multi_capture_history() -> None:
    manifest, *_ = _build()
    second = manifest.copy()
    second["capture_id"] = "f" * 64
    existing = pd.concat([manifest, second], ignore_index=True)

    with pytest.raises(RuntimeError, match="immutable base is absent"):
        validate_append_only_history(
            existing,
            second,
            immutable_base=manifest.iloc[0:0].copy(),
        )


def test_rule_contract_binds_every_numeric_feature_and_anomaly_boundary() -> None:
    expected_keys = {
        "source_variant_contract",
        "position_feature_contract",
        "shape_feature_contract",
        "base_trigger_contract",
        "source_eligibility_before_lifecycle",
        "operation_return_review_threshold_pct",
        "lifecycle_then_stratification_order",
    }
    assert expected_keys.issubset(holdout_module.RULE_CONTRACT)
    assert holdout_module.RULE_CONTRACT["operation_return_review_threshold_pct"] == 80.0
    mutations = (
        ("source_variant_contract", "absolute_latest_yoy_min_pct_inclusive", 29.0),
        ("source_variant_contract", "absolute_cumulative_yoy_min_pct_inclusive", 19.0),
        ("source_variant_contract", "two_month_latest_yoy_min_pct_inclusive", 14.0),
        ("position_feature_contract", "lookback_prior_sessions", 119),
        ("position_feature_contract", "low_max_pct_inclusive", 39.0),
        ("position_feature_contract", "mid_max_pct_inclusive", 74.0),
        ("shape_feature_contract", "return_lookback_sessions", 19),
        ("shape_feature_contract", "falling_return_max_pct_exclusive", -4.0),
        ("shape_feature_contract", "ema_slope_lookback_sessions", 4),
        ("shape_feature_contract", "falling_ema_slope_max_pct_exclusive", -0.1),
        ("shape_feature_contract", "range_window_sessions", 22),
        ("base_trigger_contract", "previous_close_high_window_sessions", 19),
    )
    for section, key, value in mutations:
        changed = deepcopy(holdout_module.RULE_CONTRACT)
        changed[section][key] = value
        assert holdout_module._canonical_json_sha256(changed) != RULE_CANONICAL_SHA256
    changed = deepcopy(holdout_module.RULE_CONTRACT)
    changed["operation_return_review_threshold_pct"] = 79.0
    assert holdout_module._canonical_json_sha256(changed) != RULE_CANONICAL_SHA256
    changed = deepcopy(holdout_module.RULE_CONTRACT)
    changed["source_eligibility_before_lifecycle"] = (
        "operation_block_before_point_in_time_watch_eligibility"
    )
    assert holdout_module._canonical_json_sha256(changed) != RULE_CANONICAL_SHA256


def test_append_only_history_is_idempotent_across_generated_at_only() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )
    second = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:05:00 Asia/Taipei",
    )
    for existing, regenerated in zip(first, second, strict=True):
        assert existing["capture_id"].astype(str).tolist() == regenerated[
            "capture_id"
        ].astype(str).tolist()
        validate_append_only_history(existing, regenerated)


def test_writer_preserves_all_17_bytes_for_idempotent_semantic_capture(
    tmp_path: Path,
) -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )
    regenerated = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:05:00 Asia/Taipei",
    )
    assert first[0].at[0, "capture_id"] == regenerated[0].at[0, "capture_id"]
    assert first[0].at[0, "generated_at"] != regenerated[0].at[0, "generated_at"]

    paths = write_forward_holdout(*first, output_root=tmp_path)
    before = {name: path.read_bytes() for name, path in paths.items()}
    write_forward_holdout(*regenerated, output_root=tmp_path)
    assert {name: path.read_bytes() for name, path in paths.items()} == before
    for artifact in ("manifest", "detail", "summary", "comparison", "anomaly"):
        assert paths[f"{artifact}_latest"].read_bytes() == paths[
            f"{artifact}_docs"
        ].read_bytes()
        assert paths[f"{artifact}_latest"].read_bytes() == paths[
            f"{artifact}_history"
        ].read_bytes()

    # Reproduce the exact pre-fix partial refresh: histories retain the first
    # capture timestamp while all ten latest/docs mirrors receive the rerun time.
    for artifact, frame in zip(
        ("manifest", "detail", "summary", "comparison", "anomaly"),
        regenerated,
        strict=True,
    ):
        drifted_payload = holdout_module._csv_payload(frame)
        paths[f"{artifact}_latest"].write_bytes(drifted_payload)
        paths[f"{artifact}_docs"].write_bytes(drifted_payload)
    assert {name: path.read_bytes() for name, path in paths.items()} != before
    write_forward_holdout(*regenerated, output_root=tmp_path)
    assert {name: path.read_bytes() for name, path in paths.items()} == before

    # Semantically equal CRLF mirrors are still byte-different from the
    # canonical LF history payload and must not survive an idempotent rerun.
    for artifact in ("manifest", "detail", "summary", "comparison", "anomaly"):
        for surface in ("latest", "docs"):
            path = paths[f"{artifact}_{surface}"]
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
    assert {name: path.read_bytes() for name, path in paths.items()} != before
    write_forward_holdout(*regenerated, output_root=tmp_path)
    assert {name: path.read_bytes() for name, path in paths.items()} == before

    semantic_mutation = [frame.copy() for frame in regenerated]
    semantic_mutation[2].at[0, "event_count"] = int(
        semantic_mutation[2].at[0, "event_count"]
    ) + 1
    with pytest.raises(RuntimeError, match="append-only.*rewrite"):
        write_forward_holdout(*semantic_mutation, output_root=tmp_path)
    assert {name: path.read_bytes() for name, path in paths.items()} == before

    # If all three mirrors already share a semantically valid raw encoding,
    # idempotency preserves those exact bytes instead of normalizing only the
    # latest/docs pair and splitting it from append-only history.
    for name, path in paths.items():
        if name.startswith("replay_source_"):
            continue
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
    all_crlf = {name: path.read_bytes() for name, path in paths.items()}
    write_forward_holdout(*regenerated, output_root=tmp_path)
    assert {name: path.read_bytes() for name, path in paths.items()} == all_crlf
    for artifact in ("manifest", "detail", "summary", "comparison", "anomaly"):
        assert paths[f"{artifact}_latest"].read_bytes() == paths[
            f"{artifact}_docs"
        ].read_bytes()
        assert paths[f"{artifact}_latest"].read_bytes() == paths[
            f"{artifact}_history"
        ].read_bytes()


def test_writer_keeps_byte_equal_mirrors_inside_research_only_scope(
    tmp_path: Path,
) -> None:
    manifest, detail, summary, comparison, anomaly, *_ = _build()
    paths = write_forward_holdout(
        manifest,
        detail,
        summary,
        comparison,
        anomaly,
        output_root=tmp_path,
    )
    assert len(paths) == 17
    forbidden = (
        "daily_candidate",
        "model_operation",
        "readiness",
        "approval",
        "pdf",
        "packet",
    )
    for path in paths.values():
        relative = path.relative_to(tmp_path).as_posix()
        assert relative.startswith(
            ("output/latest/research_backtest/", "output/history/research/", "docs/latest/")
        )
        assert not any(token in relative.lower() for token in forbidden)
        assert path.is_file()
    for artifact in ("manifest", "detail", "summary", "comparison", "anomaly"):
        latest = paths[f"{artifact}_latest"].read_bytes()
        docs = paths[f"{artifact}_docs"].read_bytes()
        history = paths[f"{artifact}_history"].read_bytes()
        assert latest == docs == history

    # A second identical materialization remains one append-only capture.
    write_forward_holdout(
        manifest,
        detail,
        summary,
        comparison,
        anomaly,
        output_root=tmp_path,
    )
    for artifact, frame in zip(
        ("manifest", "detail", "summary", "comparison", "anomaly"),
        (manifest, detail, summary, comparison, anomaly),
        strict=True,
    ):
        persisted = pd.read_csv(
            paths[f"{artifact}_history"], keep_default_na=False, low_memory=False
        )
        assert len(persisted) == len(frame)

    # A genuinely new immutable input capture appends instead of rewriting the
    # first capture.  The tiny last-session change is after every measured exit.
    source, daily, source_manifest = holdout_inputs()
    last = daily["1111"].index[-1]
    daily["1111"].at[last, "price_resolution_ids_on_date"] = "revision-1"
    next_frames = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )
    assert next_frames[0].iloc[0]["capture_id"] != manifest.iloc[0]["capture_id"]
    immutable_bases = dict(
        zip(
            ("manifest", "detail", "summary", "comparison", "anomaly"),
            (manifest, detail, summary, comparison, anomaly),
            strict=True,
        )
    )
    write_forward_holdout(
        *next_frames,
        output_root=tmp_path,
        immutable_history_bases=immutable_bases,
    )
    for artifact, first_frame, next_frame in zip(
        ("manifest", "detail", "summary", "comparison", "anomaly"),
        (manifest, detail, summary, comparison, anomaly),
        next_frames,
        strict=True,
    ):
        persisted = pd.read_csv(
            paths[f"{artifact}_history"], keep_default_na=False, low_memory=False
        )
        assert len(persisted) == len(first_frame) + len(next_frame)


def test_writer_fails_closed_without_replay_source_detail(tmp_path: Path) -> None:
    frames = _build()[:5]

    with pytest.raises(RuntimeError, match="replay source detail is required"):
        holdout_module.write_forward_holdout(*frames, output_root=tmp_path)

    assert not list(tmp_path.rglob("revenue_unreacted_range_forward_holdout_*"))

    empty_source = holdout_inputs()[0].iloc[0:0].copy()
    with pytest.raises(RuntimeError, match="replay source detail is empty"):
        holdout_module.write_forward_holdout(
            *frames,
            replay_source_detail=empty_source,
            output_root=tmp_path,
        )

    assert not list(tmp_path.rglob("revenue_unreacted_range_forward_holdout_*"))


def test_writer_publishes_exact_seventeen_paths_with_bound_replay_source(
    tmp_path: Path,
) -> None:
    source, daily, source_manifest = holdout_inputs()
    replay_source = source.copy().reset_index(drop=True)
    frames = build_forward_holdout(
        replay_source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )

    paths = write_forward_holdout(
        *frames,
        replay_source_detail=replay_source,
        output_root=tmp_path,
    )

    assert len(paths) == 17
    assert len(set(paths.values())) == 17
    assert paths["replay_source_latest"].relative_to(tmp_path).as_posix() == (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv"
    )
    assert paths["replay_source_docs"].relative_to(tmp_path).as_posix() == (
        "docs/latest/"
        "revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv"
    )
    assert paths["replay_source_latest"].read_bytes() == paths[
        "replay_source_docs"
    ].read_bytes()

    persisted_source = pd.read_csv(
        paths["replay_source_latest"],
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    canonical_persisted_source = holdout_module._normalize_source(
        persisted_source
    ).reset_index(drop=True)
    assert holdout_module._canonical_frame_sha256(canonical_persisted_source) == str(
        frames[0].iloc[0]["source_detail_canonical_sha256"]
    )


def _read_forward_holdout_publish(
    paths: dict[str, Path],
) -> tuple[list[pd.DataFrame], dict[str, pd.DataFrame], pd.DataFrame]:
    dtype = {
        "stock_id": str,
        "trigger_date": str,
        "entry_date": str,
        "exit_date": str,
        "capture_id": str,
        "artifact_row_key": str,
    }

    def read(path: Path) -> pd.DataFrame:
        return pd.read_csv(
            path,
            dtype=dtype,
            keep_default_na=False,
            low_memory=False,
        )

    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    return (
        [read(paths[f"{name}_latest"]) for name in names],
        {name: read(paths[f"{name}_history"]) for name in names},
        read(paths["replay_source_latest"]),
    )


def test_writer_rejects_partial_four_of_five_git_base_before_publish(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    frames = _build()[:5]
    observed = {"count": 0}

    def partial_base(*_args, **_kwargs):
        offset = observed["count"]
        observed["count"] += 1
        return frames[offset] if offset < 4 else None

    monkeypatch.setattr(holdout_module, "_git_history_base_frame", partial_base)
    with pytest.raises(RuntimeError, match="zero or all five surfaces"):
        write_forward_holdout(
            *frames,
            output_root=tmp_path,
            history_base_ref="synthetic-base",
        )

    assert observed["count"] == 5
    assert not list(tmp_path.rglob("*.csv"))
    assert not list(tmp_path.rglob("*.lock"))


def test_late_history_rewrite_failure_leaves_every_prior_surface_unchanged(
    tmp_path: Path,
) -> None:
    manifest, detail, summary, comparison, anomaly, *_ = _build()
    paths = write_forward_holdout(
        manifest,
        detail,
        summary,
        comparison,
        anomaly,
        output_root=tmp_path,
    )
    before = {name: path.read_bytes() for name, path in paths.items()}

    source, daily, source_manifest = holdout_inputs()
    last = daily["1111"].index[-1]
    daily["1111"].at[last, "price_resolution_ids_on_date"] = "revision-2"
    next_manifest, next_detail, next_summary, next_comparison, _next_anomaly = (
        build_forward_holdout(
            source,
            daily,
            source_manifest=source_manifest,
            generated_at="2026-08-11 12:20:00 Asia/Taipei",
        )
    )
    conflicting_anomaly = anomaly.copy()
    conflicting_anomaly.at[
        conflicting_anomaly.index[-1], "excluded_anomaly_candidate_count"
    ] = 999

    with pytest.raises(RuntimeError, match="append-only"):
        write_forward_holdout(
            next_manifest,
            next_detail,
            next_summary,
            next_comparison,
            conflicting_anomaly,
            output_root=tmp_path,
            immutable_history_bases=dict(
                zip(
                    ("manifest", "detail", "summary", "comparison", "anomaly"),
                    (manifest, detail, summary, comparison, anomaly),
                    strict=True,
                )
            ),
        )

    after = {name: path.read_bytes() for name, path in paths.items()}
    assert after == before


def test_injected_publish_io_failure_after_eighth_target_rolls_back_all_17_paths_byte_exact(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    first = _build()[:5]
    paths = write_forward_holdout(*first, output_root=tmp_path)
    before = {name: path.read_bytes() for name, path in paths.items()}

    source, daily, source_manifest = holdout_inputs()
    last = daily["1111"].index[-1]
    daily["1111"].at[last, "price_resolution_ids_on_date"] = "revision-3"
    next_frames = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:30:00 Asia/Taipei",
    )
    real_replace = holdout_module._replace_file
    calls = {"count": 0, "failed": False}

    def fail_once_during_commit(source_path: Path, target_path: Path) -> None:
        calls["count"] += 1
        if calls["count"] == 8 and not calls["failed"]:
            calls["failed"] = True
            raise OSError("injected publish failure")
        real_replace(source_path, target_path)

    monkeypatch.setattr(holdout_module, "_replace_file", fail_once_during_commit)
    with pytest.raises(RuntimeError, match="every target was rolled back"):
        write_forward_holdout(
            *next_frames,
            output_root=tmp_path,
            immutable_history_bases=dict(
                zip(
                    ("manifest", "detail", "summary", "comparison", "anomaly"),
                    first,
                    strict=True,
                )
            ),
        )

    assert calls["failed"]
    assert {name: path.read_bytes() for name, path in paths.items()} == before
    assert not list(tmp_path.rglob("*.tmp"))


def test_post_publish_replay_failure_rolls_back_all_17_paths_byte_exact(
    tmp_path: Path,
) -> None:
    first = _build()[:5]
    paths = write_forward_holdout(*first, output_root=tmp_path)
    before = {name: path.read_bytes() for name, path in paths.items()}
    source, daily, source_manifest = holdout_inputs()
    last = daily["1111"].index[-1]
    daily["1111"].at[last, "price_resolution_ids_on_date"] = "revision-4"
    next_frames = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:40:00 Asia/Taipei",
    )

    def reject_persisted(_paths: object) -> None:
        raise RuntimeError("synthetic persisted history parity failure")

    with pytest.raises(
        RuntimeError,
        match="rolled back.*synthetic persisted history parity failure",
    ):
        write_forward_holdout(
            *next_frames,
            output_root=tmp_path,
            immutable_history_bases=dict(
                zip(
                    ("manifest", "detail", "summary", "comparison", "anomaly"),
                    first,
                    strict=True,
                )
            ),
            post_publish_check=reject_persisted,
        )
    assert {name: path.read_bytes() for name, path in paths.items()} == before
    assert not list(tmp_path.rglob("*.tmp"))


def test_replay_source_drift_fails_before_mutating_all_17_paths(
    tmp_path: Path,
) -> None:
    source, daily, source_manifest = holdout_inputs()
    replay_source = source.copy().reset_index(drop=True)
    frames = build_forward_holdout(
        replay_source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    paths = write_forward_holdout(
        *frames,
        replay_source_detail=replay_source,
        output_root=tmp_path,
    )
    before = {name: path.read_bytes() for name, path in paths.items()}
    corrupted_source = replay_source.copy()
    corrupted_source.at[corrupted_source.index[0], "stock_name"] = "corrupted-name"

    with pytest.raises(
        RuntimeError,
        match="replay source detail SHA-256 disagrees with the manifest",
    ):
        write_forward_holdout(
            *frames,
            replay_source_detail=corrupted_source,
            output_root=tmp_path,
        )

    assert {name: path.read_bytes() for name, path in paths.items()} == before
    assert not list(tmp_path.rglob("*.tmp"))


def test_missing_replay_source_mirror_rolls_back_all_17_paths_byte_exact(
    tmp_path: Path,
) -> None:
    source, daily, source_manifest = holdout_inputs()
    replay_source = source.copy().reset_index(drop=True)
    frames = build_forward_holdout(
        replay_source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    paths = write_forward_holdout(
        *frames,
        replay_source_detail=replay_source,
        output_root=tmp_path,
    )
    before = {name: path.read_bytes() for name, path in paths.items()}

    def delete_docs_mirror(candidate_paths: dict[str, Path]) -> None:
        candidate_paths["replay_source_docs"].unlink()
        raise RuntimeError("missing replay source docs mirror")

    with pytest.raises(
        RuntimeError,
        match="rolled back.*missing replay source docs mirror",
    ):
        write_forward_holdout(
            *frames,
            replay_source_detail=replay_source,
            output_root=tmp_path,
            post_publish_check=delete_docs_mirror,
        )

    assert {name: path.read_bytes() for name, path in paths.items()} == before
    assert not list(tmp_path.rglob("*.tmp"))


def test_injected_publish_io_failure_rolls_back_all_17_paths_byte_exact(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source, daily, source_manifest = holdout_inputs()
    replay_source = source.copy().reset_index(drop=True)
    frames = build_forward_holdout(
        replay_source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    paths = write_forward_holdout(
        *frames,
        replay_source_detail=replay_source,
        output_root=tmp_path,
    )
    before = {name: path.read_bytes() for name, path in paths.items()}
    real_replace = holdout_module._replace_file
    calls = {"count": 0, "failed": False}

    def fail_once_after_fifteen_targets(source_path: Path, target_path: Path) -> None:
        calls["count"] += 1
        if calls["count"] == 16 and not calls["failed"]:
            calls["failed"] = True
            raise OSError("injected replay-source publish failure")
        real_replace(source_path, target_path)

    monkeypatch.setattr(
        holdout_module,
        "_replace_file",
        fail_once_after_fifteen_targets,
    )
    with pytest.raises(RuntimeError, match="every target was rolled back"):
        write_forward_holdout(
            *frames,
            replay_source_detail=replay_source,
            output_root=tmp_path,
        )

    assert calls["failed"]
    assert {name: path.read_bytes() for name, path in paths.items()} == before
    assert not list(tmp_path.rglob("*.tmp"))


def test_publish_lock_rejects_concurrent_writer_without_target_drift(
    tmp_path: Path,
) -> None:
    frames = _build()[:5]
    paths = write_forward_holdout(*frames, output_root=tmp_path)
    before = {name: path.read_bytes() for name, path in paths.items()}
    lock_path = (
        tmp_path
        / "output/history/research"
        / ".revenue_unreacted_range_forward_holdout.publish.lock"
    )
    lock_path.write_text("held-by-another-writer\n", encoding="utf-8")
    with pytest.raises(RuntimeError, match="publish lock is already held"):
        write_forward_holdout(*frames, output_root=tmp_path)
    assert {name: path.read_bytes() for name, path in paths.items()} == before
    assert lock_path.read_text(encoding="utf-8") == "held-by-another-writer\n"


def test_publish_lock_is_held_through_transaction_temporary_cleanup(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    frames = _build()[:5]
    lock_path = (
        tmp_path
        / "output/history/research"
        / ".revenue_unreacted_range_forward_holdout.publish.lock"
    )
    real_publish = holdout_module._publish_payloads_transactionally
    observed = {"returned_with_lock": False}

    def observe_publish(
        payloads,
        *,
        expected_path_count=17,
        post_publish_check=None,
    ):
        assert lock_path.is_file()
        result = real_publish(
            payloads,
            expected_path_count=expected_path_count,
            post_publish_check=post_publish_check,
        )
        assert lock_path.is_file()
        assert not list(tmp_path.rglob("*.tmp"))
        observed["returned_with_lock"] = True
        return result

    monkeypatch.setattr(
        holdout_module,
        "_publish_payloads_transactionally",
        observe_publish,
    )
    write_forward_holdout(*frames, output_root=tmp_path)
    assert observed["returned_with_lock"]
    assert not lock_path.exists()


def test_all_outputs_remain_research_only_and_formal_consumers_are_forbidden() -> None:
    manifest, detail, summary, comparison, anomaly, *_ = _build()
    for frame in (manifest, detail, summary, comparison, anomaly):
        assert not frame.empty
        assert frame["research_only"].map(_flag).all()
        for column in (
            "formal_model_use_allowed",
            "approved_for_daily",
            "presentation_allowed",
            "promotion_evidence_allowed",
            "production_change",
        ):
            assert column in frame.columns
            assert not frame[column].map(_flag).any()
    assert not _flag(manifest.iloc[0]["ranking_consumption_allowed"])
    assert not _flag(manifest.iloc[0]["pdf_consumption_allowed"])


def test_build_is_deterministic_except_for_explicit_generated_at() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    second = build_forward_holdout(
        source.sample(frac=1.0, random_state=7).reset_index(drop=True),
        {key: value.sample(frac=1.0, random_state=9).reset_index(drop=True) for key, value in reversed(list(daily.items()))},
        source_manifest=source_manifest.copy(),
        generated_at=GENERATED_AT,
    )
    for left, right in zip(first, second, strict=True):
        pd.testing.assert_frame_equal(left, right)


def test_current_wrapper_caps_source_materialization_at_observed_price_date(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    research_frame = pd.DataFrame(
        {
            "stock_id": ["1111", "1111", "1111"],
            "date": ["20260810", "20260807", "20260806"],
        }
    )
    prepared = research_frame.copy()
    observed: dict[str, object] = {}

    monkeypatch.setattr(
        research_frame_module,
        "build_revenue_unreacted_range_research_frame",
        lambda: research_frame.copy(),
    )
    monkeypatch.setattr(
        parameter_research,
        "_revenue_unreacted_timing_prepared_frame",
        lambda frame: prepared.copy(),
    )
    monkeypatch.setattr(
        parameter_research,
        "_attach_revenue_signal_market_regime",
        lambda frame: frame.copy(),
    )

    def fake_source_builder(*, observation_cutoff_date: str | None = None):
        # 20260811 represents a monthly-revenue update unavailable at the
        # observed 20260810 price boundary.  An unbounded call would leak it.
        observed["source_cutoff"] = observation_cutoff_date
        available = pd.DataFrame(
            {"latest_qualifying_source_date": ["20260810", "20260811"]}
        )
        selected = available.loc[
            available["latest_qualifying_source_date"].le(
                str(observation_cutoff_date or "99999999")
            )
        ].reset_index(drop=True)
        return pd.DataFrame([{"row_count": len(selected)}]), selected

    def fake_prepare_daily(prepared_frame, source_detail):
        observed["source_dates"] = source_detail[
            "latest_qualifying_source_date"
        ].astype(str).tolist()
        return {"1111": prepared_frame.copy()}

    source_manifest = pd.DataFrame([{"sentinel": "source-manifest"}])
    training_projection_detail = pd.DataFrame(
        [{"sentinel": "training-projection-detail"}]
    )
    sentinel_outputs = tuple(pd.DataFrame([{"sentinel": index}]) for index in range(5))

    def fake_build(source_detail, daily_by_stock, *, source_manifest, generated_at=None):
        observed["build_source_dates"] = source_detail[
            "latest_qualifying_source_date"
        ].astype(str).tolist()
        observed["daily_keys"] = sorted(daily_by_stock)
        observed["source_manifest"] = source_manifest.iloc[0]["sentinel"]
        return sentinel_outputs

    monkeypatch.setattr(
        holdout_module, "build_source_first_condition_audit", fake_source_builder
    )
    monkeypatch.setattr(
        holdout_module,
        "_attach_qualifying_anomaly_flags",
        lambda source_detail, _prepared: source_detail.copy(),
    )
    monkeypatch.setattr(holdout_module, "prepare_daily_by_stock", fake_prepare_daily)
    monkeypatch.setattr(
        holdout_module,
        "load_source_snapshot_projection_manifest",
        lambda path: (
            observed.setdefault("training_manifest_path", Path(path))
            and source_manifest.copy()
        ),
    )
    monkeypatch.setattr(
        holdout_module,
        "load_projected_source_detail",
        lambda path: (
            observed.setdefault("training_detail_path", Path(path))
            and training_projection_detail.copy()
        ),
    )
    monkeypatch.setattr(
        holdout_module,
        "validate_projection_binding",
        lambda manifest, detail, **kwargs: observed.update(
            {
                "training_pair_manifest": manifest.iloc[0]["sentinel"],
                "training_pair_detail": detail.iloc[0]["sentinel"],
                "training_pair_expected_version": kwargs[
                    "expected_artifact_version"
                ],
            }
        ),
    )
    monkeypatch.setattr(holdout_module, "build_forward_holdout", fake_build)

    result = holdout_module.build_current_forward_holdout()

    assert result == sentinel_outputs
    assert observed["source_cutoff"] == "20260810"
    assert observed["source_dates"] == ["20260810"]
    assert observed["build_source_dates"] == ["20260810"]
    assert observed["daily_keys"] == ["1111"]
    assert observed["source_manifest"] == "source-manifest"
    assert observed["training_manifest_path"] == (
        holdout_module.TRAINING_SOURCE_PROJECTION_MANIFEST_CSV
    )
    assert observed["training_detail_path"] == (
        holdout_module.TRAINING_SOURCE_PROJECTION_DETAIL_CSV
    )
    assert observed["training_pair_manifest"] == "source-manifest"
    assert observed["training_pair_detail"] == "training-projection-detail"
    assert observed["training_pair_expected_version"] == (
        holdout_module.SOURCE_PROJECTION_ARTIFACT_VERSION
    )


def _install_stage_validation_harness(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    *,
    validation_errors: list[str],
) -> tuple[dict[str, object], dict[str, Path]]:
    source_detail = pd.DataFrame([{"source": "bounded"}])
    persisted_source = source_detail.copy()
    daily_by_stock = {"1111": pd.DataFrame([{"date": "20260810"}])}
    source_manifest = pd.DataFrame([{"manifest": "pinned"}])
    training_projection_detail = pd.DataFrame([{"projection": "v1-pinned"}])
    frames = tuple(
        pd.DataFrame([{"surface": name}])
        for name in ("manifest", "detail", "summary", "comparison", "anomaly")
    )
    paths = {
        f"{name}_{surface}": tmp_path / f"{name}_{surface}.csv"
        for name in ("manifest", "detail", "summary", "comparison", "anomaly")
        for surface in ("latest", "history")
    }
    paths.update(
        {
            "replay_source_latest": tmp_path / "replay_source_detail_latest.csv",
            "replay_source_docs": tmp_path / "replay_source_detail_docs.csv",
        }
    )
    name_to_frame = {
        name: frame
        for name, frame in zip(
            ("manifest", "detail", "summary", "comparison", "anomaly"),
            frames,
            strict=True,
        )
    }
    observed: dict[str, object] = {"events": [], "validate_calls": 0}

    monkeypatch.setattr(
        holdout_module,
        "_materialize_current_forward_holdout_inputs",
        lambda: (
            source_detail,
            daily_by_stock,
            source_manifest,
            training_projection_detail,
        ),
    )
    def fake_build(source, daily, *, source_manifest):
        observed["events"].append("build")
        assert source is source_detail
        observed["in_memory_source"] = source
        assert daily is daily_by_stock
        assert source_manifest is source_manifest_fixture
        return frames

    source_manifest_fixture = source_manifest

    def fake_write(
        *written_frames,
        replay_source_detail=None,
        output_root=None,
        post_publish_check=None,
    ):
        write_kind = "staged" if output_root is not None else "real"
        observed["events"].append(f"write:{write_kind}")
        for actual, expected in zip(written_frames, frames, strict=True):
            pd.testing.assert_frame_equal(actual, expected)
        assert replay_source_detail is source_detail
        if output_root is None:
            result = paths
        else:
            root = Path(output_root)
            result = {
                f"{name}_{surface}": root / f"{name}_{surface}.csv"
                for name in ("manifest", "detail", "summary", "comparison", "anomaly")
                for surface in ("latest", "history")
            }
            result.update(
                {
                    "replay_source_latest": root / "replay_source_detail_latest.csv",
                    "replay_source_docs": root / "replay_source_detail_docs.csv",
                }
            )
        replay_payload = persisted_source.to_csv(index=False).encode("utf-8")
        for key in ("replay_source_latest", "replay_source_docs"):
            result[key].parent.mkdir(parents=True, exist_ok=True)
            result[key].write_bytes(replay_payload)
        if post_publish_check is not None:
            post_publish_check(result)
        return result

    def fake_read_csv(path, **_kwargs):
        observed["events"].append(f"read:{Path(path).stem}")
        if "replay_source_detail" in Path(path).stem:
            return persisted_source.copy()
        name = Path(path).stem.removesuffix("_latest").removesuffix("_history")
        return name_to_frame[name].copy()

    def fake_validate(
        *persisted,
        source_detail,
        daily_by_stock,
        source_manifest,
        training_source_projection_detail,
        history_frames=None,
        immutable_history_base_frames=None,
    ):
        observed["events"].append("validate")
        observed["validate_calls"] = int(observed["validate_calls"]) + 1
        observed.setdefault("validated_sources", []).append(source_detail)
        for actual, expected in zip(persisted, frames, strict=True):
            pd.testing.assert_frame_equal(actual, expected)
        if int(observed["validate_calls"]) == 1:
            assert source_detail is observed["in_memory_source"]
        else:
            pd.testing.assert_frame_equal(source_detail, persisted_source)
            assert source_detail is not observed["in_memory_source"]
        assert daily_by_stock is daily_fixture
        assert source_manifest is source_manifest_fixture
        assert training_source_projection_detail is training_projection_detail
        if int(observed["validate_calls"]) > 1:
            assert history_frames is not None
            assert set(history_frames) == set(name_to_frame)
            for name, frame in history_frames.items():
                pd.testing.assert_frame_equal(frame, name_to_frame[name])
        else:
            assert history_frames is None
        assert immutable_history_base_frames is None
        # The first call validates in-memory frames.  Injected errors apply to
        # the first persisted replay so the failure proves write/read gating.
        return list(validation_errors) if int(observed["validate_calls"]) > 1 else []

    daily_fixture = daily_by_stock
    monkeypatch.setattr(holdout_module, "build_forward_holdout", fake_build)
    monkeypatch.setattr(holdout_module, "write_forward_holdout", fake_write)
    monkeypatch.setattr(holdout_module.pd, "read_csv", fake_read_csv)
    monkeypatch.setattr(holdout_validator, "validate_frames", fake_validate)
    return observed, paths


def test_forward_holdout_stage_validates_persisted_surfaces_after_write(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    observed, paths = _install_stage_validation_harness(
        monkeypatch,
        tmp_path,
        validation_errors=[],
    )

    result = holdout_module.build_and_write_current_forward_holdout()

    assert result == paths
    assert observed["validate_calls"] == 3
    events = list(observed["events"])
    assert events[0:3] == ["build", "validate", "write:staged"]
    assert events[-1] == "validate"
    assert events.count("write:staged") == 1
    assert events.count("write:real") == 1
    assert len([event for event in events if str(event).startswith("read:")]) == 22
    validated_sources = observed["validated_sources"]
    assert validated_sources[0] is observed["in_memory_source"]
    assert validated_sources[1] is not observed["in_memory_source"]
    assert validated_sources[2] is not observed["in_memory_source"]
    pd.testing.assert_frame_equal(validated_sources[1], validated_sources[2])


def test_forward_holdout_stage_fails_closed_on_independent_validation_error(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    observed, _paths = _install_stage_validation_harness(
        monkeypatch,
        tmp_path,
        validation_errors=["synthetic persisted lineage drift"],
    )

    with pytest.raises(
        RuntimeError,
        match="independent replay failed.*synthetic persisted lineage drift",
    ):
        holdout_module.build_and_write_current_forward_holdout()

    assert observed["validate_calls"] == 2
    assert "write:staged" in list(observed["events"])
    assert "write:real" not in list(observed["events"])
    assert list(observed["events"])[-1] == "validate"
