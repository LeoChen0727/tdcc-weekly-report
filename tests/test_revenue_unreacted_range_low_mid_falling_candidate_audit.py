from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_low_mid_falling_candidate_audit as low_mid_producer  # noqa: E402
from revenue_unreacted_range_low_mid_falling_candidate_audit import (  # noqa: E402
    ANALYSIS_BASES,
    ARTIFACT_ID,
    CONFIRMATION_VARIANT_IDS,
    DATA_CONTRACT_SHA256,
    FINANCIAL_STATEMENT_SCOPE,
    LIFECYCLE_POLICY_IDS,
    NO_STOP_POLICY_ID,
    REARMED_ARTIFACT_ID,
    REARMED_ARTIFACT_VERSION,
    REARMED_ENTRY_PRICE_BASIS,
    REARMED_EXIT_PRICE_BASIS,
    REARMED_EXIT_REASON,
    REARMED_FIXED_EXIT_PRICE_BASIS,
    REARMED_PERSISTED_DETAIL_DROP_COLUMNS,
    REARMED_SOURCE_ARTIFACT_ID,
    PRIMARY_ANALYSIS_BASIS,
    SENSITIVITY_ANALYSIS_BASIS,
    SOURCE_VARIANT_ID,
    SOURCE_FIRST_ARTIFACT_ID,
    SOURCE_FIRST_ARTIFACT_VERSION,
    VARIANT_SPECS,
    build_low_mid_falling_candidate_audit,
    write_low_mid_falling_candidate_audit,
)


GENERATED_AT = "2026-07-20 12:00:00 Asia/Taipei"
TRIGGER_INDEX = 220


def _price_frame(source_index: int, position: str, return_pct: float) -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-02", periods=290).strftime("%Y%m%d")
    target = 90.0 if position == "low" else 100.0
    close = np.full(290, 110.0)
    close[source_index - 25 : source_index + 1] = np.linspace(
        112.0, target, 26
    )
    close[source_index + 1 :] = 100.0
    close[TRIGGER_INDEX] = 100.0
    close[TRIGGER_INDEX + 1] = 102.0
    analysis_open = close.copy()
    analysis_open[TRIGGER_INDEX + 1] = 100.0
    analysis_open[TRIGGER_INDEX + 2] = 100.0
    exit_value = 100.0 * (1.0 + return_pct / 100.0)
    close[TRIGGER_INDEX + 30] = exit_value
    close[TRIGGER_INDEX + 31] = exit_value
    high = close + 1.0
    low = close - 1.0
    high[source_index - 100] = 120.0
    low[source_index - 99] = 80.0
    return pd.DataFrame(
        {
            "date": dates,
            "analysis_open": analysis_open,
            "analysis_high": high,
            "analysis_low": low,
            "analysis_close": close,
        }
    )


def _source_row(
    stock_id: str,
    stock_name: str,
    price: pd.DataFrame,
    source_index: int,
) -> dict[str, object]:
    source_date = str(price.at[source_index, "date"])
    return {
        "model_id": "revenue_unreacted_range",
        "artifact_id": SOURCE_FIRST_ARTIFACT_ID,
        "artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
        "monthly_revenue_history_blob_sha256": "1" * 64,
        "monthly_revenue_canonical_table_sha256": "2" * 64,
        "cross_market_resolution_registry_canonical_sha256": "3" * 64,
        "condition_variant_id": SOURCE_VARIANT_ID,
        "episode_key": f"episode-{stock_id}",
        "stock_id": stock_id,
        "stock_name": stock_name,
        "episode_start_revenue_period": "202601",
        "episode_start_source_date": source_date,
        "episode_start_cross_market_resolution_id": "none",
        "episode_start_source_row_canonical_sha256": "4" * 64,
        "episode_start_canonical_source_table_date": source_date,
        "episode_start_trade_date": source_date,
        "episode_start_sequence_index": source_index,
        "latest_qualifying_revenue_period": "202601",
        "latest_qualifying_source_date": source_date,
        "latest_qualifying_cross_market_resolution_id": "none",
        "latest_qualifying_source_row_canonical_sha256": "4" * 64,
        "latest_qualifying_canonical_source_table_date": source_date,
        "latest_qualifying_trade_date": source_date,
        "latest_qualifying_sequence_index": source_index,
        "qualifying_update_count": 1,
        "qualifying_revenue_periods": "202601",
        "qualifying_source_dates": source_date,
        "qualifying_cross_market_resolution_ids": "none",
        "qualifying_source_row_canonical_sha256s": "4" * 64,
        "qualifying_canonical_source_table_dates": source_date,
        "qualifying_trade_dates": source_date,
        "qualifying_sequence_indices": str(source_index),
    }


def _operation_rows(
    stock_id: str,
    stock_name: str,
    price: pd.DataFrame,
    *,
    source_candidate: bool,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    dates = price["date"].astype(str).tolist()
    for lifecycle_id in LIFECYCLE_POLICY_IDS:
        for confirmation_id in CONFIRMATION_VARIANT_IDS:
            delayed = confirmation_id == "delayed_next_close_continuation_bonus"
            confirmation_index = TRIGGER_INDEX + (1 if delayed else 0)
            entry_index = confirmation_index + 1
            exit_index = entry_index + 29
            entry = float(price.at[entry_index, "analysis_open"])
            exit_close = float(price.at[exit_index, "analysis_close"])
            realized = (exit_close / entry - 1.0) * 100.0
            rows.append(
                {
                    "model_id": "revenue_unreacted_range",
                    "artifact_id": REARMED_ARTIFACT_ID,
                    "artifact_version": REARMED_ARTIFACT_VERSION,
                    "source_artifact_id": REARMED_SOURCE_ARTIFACT_ID,
                    "source_variant_id": SOURCE_VARIANT_ID,
                    "grid_id": "|".join(
                        (
                            lifecycle_id,
                            confirmation_id,
                            "d30",
                            NO_STOP_POLICY_ID,
                        )
                    ),
                    "lifecycle_policy_id": lifecycle_id,
                    "confirmation_variant_id": confirmation_id,
                    "holding_days": 30,
                    "stop_policy_id": NO_STOP_POLICY_ID,
                    "return_valid": True,
                    "episode_key": f"episode-{stock_id}",
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "trigger_date": dates[TRIGGER_INDEX],
                    "confirmation_date": dates[confirmation_index],
                    "entry_index": entry_index,
                    "entry_date": dates[entry_index],
                    "entry_price": entry,
                    "planned_exit_index": exit_index,
                    "planned_exit_date": dates[exit_index],
                    "exit_index": exit_index,
                    "exit_date": dates[exit_index],
                    "exit_price": exit_close,
                    "entry_price_basis": REARMED_ENTRY_PRICE_BASIS,
                    "fixed_exit_price_basis": REARMED_FIXED_EXIT_PRICE_BASIS,
                    "exit_price_basis": REARMED_EXIT_PRICE_BASIS,
                    "exit_reason": REARMED_EXIT_REASON,
                    "realized_return_pct": round(realized, 4),
                    "return_outcome": (
                        "win" if realized > 0 else "failure" if realized < 0 else "neutral"
                    ),
                    "source_anomaly_candidate_flag": source_candidate,
                    "unresolved_price_path_candidate_flag": False,
                    "operation_return_review_candidate_flag": False,
                    "intraday_operation_basis_used": False,
                }
            )
    return rows


def _inputs() -> tuple[pd.DataFrame, pd.DataFrame, dict[str, pd.DataFrame]]:
    specs = (
        # Exactly 60 sessions: included low+falling and retained anomaly candidate.
        ("1111", "low-60", 160, "low", 25.0, True),
        # 50 sessions: included mid+falling.
        ("2222", "mid-50", 170, "mid", -10.0, False),
        # 61 sessions: excluded even though its source anchor is mid+falling.
        ("3333", "mid-61", 159, "mid", 5.0, False),
    )
    source_rows: list[dict[str, object]] = []
    operation_rows: list[dict[str, object]] = []
    daily: dict[str, pd.DataFrame] = {}
    for stock_id, name, source_index, position, return_pct, source_candidate in specs:
        price = _price_frame(source_index, position, return_pct)
        daily[stock_id] = price
        source_rows.append(_source_row(stock_id, name, price, source_index))
        operation_rows.extend(
            _operation_rows(
                stock_id,
                name,
                price,
                source_candidate=source_candidate,
            )
        )
    return pd.DataFrame(source_rows), pd.DataFrame(operation_rows), daily


def _build() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    source, operations, daily = _inputs()
    return build_low_mid_falling_candidate_audit(
        source,
        operations,
        daily,
        generated_at=GENERATED_AT,
    )


def _summary_row(
    summary: pd.DataFrame,
    *,
    basis: str,
    lifecycle: str,
    confirmation: str,
    variant: str,
) -> pd.Series:
    return summary.loc[
        summary["analysis_basis"].eq(basis)
        & summary["lifecycle_policy_id"].eq(lifecycle)
        & summary["confirmation_variant_id"].eq(confirmation)
        & summary["candidate_variant_id"].eq(variant)
    ].iloc[0]


def test_watch_horizon_union_and_primary_candidate_retention() -> None:
    summary, detail, _paired, _contrast = _build()

    assert set(detail["stock_id"]) == {"1111", "2222"}
    assert set(detail["latest_source_to_trigger_trading_days"].astype(int)) == {50, 60}
    assert len(detail) == 2 * len(LIFECYCLE_POLICY_IDS) * len(CONFIRMATION_VARIANT_IDS)
    assert detail["operation_key"].is_unique
    assert detail["low_or_mid_falling_union_member"].astype(bool).all()
    assert not (
        detail["low_falling_member"].astype(bool)
        & detail["mid_falling_member"].astype(bool)
    ).any()

    primary_union = _summary_row(
        summary,
        basis=PRIMARY_ANALYSIS_BASIS,
        lifecycle="rearm_after_realized_exit_next_trade_day",
        confirmation="base_close_confirmed",
        variant="source_low_or_mid_falling_union",
    )
    primary_low = _summary_row(
        summary,
        basis=PRIMARY_ANALYSIS_BASIS,
        lifecycle="rearm_after_realized_exit_next_trade_day",
        confirmation="base_close_confirmed",
        variant="source_low_falling",
    )
    primary_mid = _summary_row(
        summary,
        basis=PRIMARY_ANALYSIS_BASIS,
        lifecycle="rearm_after_realized_exit_next_trade_day",
        confirmation="base_close_confirmed",
        variant="source_mid_falling",
    )
    sensitivity_union = _summary_row(
        summary,
        basis=SENSITIVITY_ANALYSIS_BASIS,
        lifecycle="rearm_after_realized_exit_next_trade_day",
        confirmation="base_close_confirmed",
        variant="source_low_or_mid_falling_union",
    )
    assert int(primary_union["operation_count"]) == 2
    assert int(primary_union["combined_exclusion_candidate_count"]) == 1
    assert int(primary_low["operation_count"]) == 1
    assert int(primary_mid["operation_count"]) == 1
    assert int(sensitivity_union["operation_count"]) == 1


def test_d1_d2_pairing_and_high_low_feature_contrast() -> None:
    _summary, detail, paired, contrast = _build()
    dates = _inputs()[2]["1111"]["date"].astype(str).tolist()

    pair = paired.loc[
        paired["lifecycle_policy_id"].eq(
            "rearm_after_realized_exit_next_trade_day"
        )
        & paired["stock_id"].eq("1111")
    ].iloc[0]
    assert pair["base_confirmation_date"] == dates[TRIGGER_INDEX]
    assert pair["base_entry_date"] == dates[TRIGGER_INDEX + 1]
    assert pair["delayed_confirmation_date"] == dates[TRIGGER_INDEX + 1]
    assert pair["delayed_entry_date"] == dates[TRIGGER_INDEX + 2]
    assert (
        pair["paired_comparison_role"]
        == "same_trigger_distinct_information_cutoff_not_independent_operations"
    )
    assert len(paired) == 2 * len(LIFECYCLE_POLICY_IDS)

    primary_union_base = contrast.loc[
        contrast["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & contrast["lifecycle_policy_id"].eq(
            "rearm_after_realized_exit_next_trade_day"
        )
        & contrast["confirmation_variant_id"].eq("base_close_confirmed")
        & contrast["candidate_variant_id"].eq(
            "source_low_or_mid_falling_union"
        )
        & contrast["feature_id"].eq("source_position_120d_pct")
    ].iloc[0]
    assert int(primary_union_base["high_return_operation_count"]) == 1
    assert int(primary_union_base["low_return_operation_count"]) == 1
    assert float(primary_union_base["high_mean"]) < float(
        primary_union_base["low_mean"]
    )
    assert set(detail["confirmation_variant_id"]) == set(CONFIRMATION_VARIANT_IDS)


def test_immutable_lineage_hashes_are_emitted_and_stable_per_source() -> None:
    summary, detail, paired, contrast = _build()
    digest_pattern = r"[0-9a-f]{64}"

    assert set(detail["data_contract_sha256"]) == {DATA_CONTRACT_SHA256}
    assert detail["producer_semantic_sha256"].str.fullmatch(digest_pattern).all()
    assert detail["source_first_producer_semantic_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert detail["rearmed_producer_semantic_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert detail["position_shape_producer_semantic_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert detail["source_first_canonical_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert detail["rearmed_operation_canonical_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert detail["price_history_canonical_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert detail.groupby("episode_key")[
        "source_first_canonical_row_sha256"
    ].nunique().eq(1).all()
    assert detail.groupby("stock_id")["price_history_canonical_sha256"].nunique().eq(
        1
    ).all()
    assert detail["rearmed_operation_canonical_row_sha256"].is_unique
    assert set(detail["entry_price_basis"]) == {REARMED_ENTRY_PRICE_BASIS}
    assert set(detail["fixed_exit_price_basis"]) == {
        REARMED_FIXED_EXIT_PRICE_BASIS
    }
    assert set(detail["exit_price_basis"]) == {REARMED_EXIT_PRICE_BASIS}
    assert set(detail["exit_reason"]) == {REARMED_EXIT_REASON}
    assert not detail["intraday_operation_basis_used"].astype(bool).any()
    assert (detail["exit_index"].astype(int) - detail["entry_index"].astype(int)).eq(
        29
    ).all()
    assert detail["planned_exit_index"].astype(int).eq(
        detail["exit_index"].astype(int)
    ).all()
    assert detail["planned_exit_date"].astype(str).eq(
        detail["exit_date"].astype(str)
    ).all()
    assert detail["candidate_detail_row_sha256"].str.fullmatch(digest_pattern).all()
    for frame in (summary, paired, contrast):
        assert set(frame["data_contract_sha256"]) == {DATA_CONTRACT_SHA256}
        assert frame["producer_semantic_sha256"].str.fullmatch(digest_pattern).all()
        assert frame["position_shape_producer_semantic_sha256"].str.fullmatch(
            digest_pattern
        ).all()
    for frame in (summary, detail, paired, contrast):
        assert set(frame["monthly_revenue_history_blob_sha256"]) == {"1" * 64}
        assert set(frame["monthly_revenue_canonical_table_sha256"]) == {"2" * 64}
        assert set(frame["cross_market_resolution_registry_canonical_sha256"]) == {
            "3" * 64
        }
        for column in (
            "source_first_selected_slice_canonical_sha256",
            "rearmed_d30_no_stop_slice_canonical_sha256",
            "price_history_manifest_canonical_sha256",
            "detail_artifact_canonical_sha256",
            "source_first_canonical_row_set_sha256",
            "rearmed_operation_canonical_row_set_sha256",
            "price_history_canonical_set_sha256",
            "candidate_detail_row_set_sha256",
        ):
            assert frame[column].str.fullmatch(digest_pattern).all()
            assert frame[column].nunique() == 1
    assert paired["source_first_canonical_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert paired["base_rearmed_operation_canonical_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert paired["delayed_rearmed_operation_canonical_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert paired["base_candidate_detail_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()
    assert paired["delayed_candidate_detail_row_sha256"].str.fullmatch(
        digest_pattern
    ).all()


def test_rearmed_lineage_hashes_use_exact_persisted_artifact_schema() -> None:
    source, operations, daily = _inputs()
    transient_values = {
        "base_confirmation_rule": "close confirmation description",
        "bonus_timing_role": "advisory bonus role",
        "stop_rule": "no stop; fixed future close exit",
        "episode_status": "mature",
        "source_launch_date": "20260115",
        "same_stock_non_overlap_policy": "entry after prior exit",
        "outcome_definition": "win above zero",
        "operation_return_review_policy": "review candidate only",
        "financial_statement_scope": "monthly_revenue_only",
        "promotion_readiness": "research_only",
        "lifecycle_role": "research lifecycle",
    }
    assert set(transient_values) == set(REARMED_PERSISTED_DETAIL_DROP_COLUMNS)
    full_memory_operations = operations.assign(**transient_values)
    persisted_operations = full_memory_operations.drop(
        columns=list(REARMED_PERSISTED_DETAIL_DROP_COLUMNS)
    )

    full_detail = build_low_mid_falling_candidate_audit(
        source,
        full_memory_operations,
        daily,
        generated_at=GENERATED_AT,
    )[1].sort_values("operation_key", kind="mergesort").reset_index(drop=True)
    persisted_detail = build_low_mid_falling_candidate_audit(
        source,
        persisted_operations,
        daily,
        generated_at=GENERATED_AT,
    )[1].sort_values("operation_key", kind="mergesort").reset_index(drop=True)

    for column in (
        "rearmed_operation_canonical_row_sha256",
        "rearmed_d30_no_stop_slice_canonical_sha256",
        "candidate_detail_row_sha256",
        "detail_artifact_canonical_sha256",
    ):
        assert full_detail[column].tolist() == persisted_detail[column].tolist()

    changed_operations = persisted_operations.copy()
    changed_stock_id = str(changed_operations.loc[0, "stock_id"])
    changed_operations.loc[
        changed_operations["stock_id"].astype(str).eq(changed_stock_id), "stock_name"
    ] = "persisted-lineage-change"
    changed_detail = build_low_mid_falling_candidate_audit(
        source,
        changed_operations,
        daily,
        generated_at=GENERATED_AT,
    )[1]
    baseline_hashes = set(
        persisted_detail["rearmed_operation_canonical_row_sha256"].astype(str)
    )
    changed_hashes = set(
        changed_detail["rearmed_operation_canonical_row_sha256"].astype(str)
    )
    assert baseline_hashes != changed_hashes


def test_rearmed_persisted_schema_projection_fails_on_partial_drop_columns() -> None:
    source, operations, daily = _inputs()
    operations[REARMED_PERSISTED_DETAIL_DROP_COLUMNS[0]] = "partial"

    with pytest.raises(RuntimeError, match="persisted-schema projection is partial"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )


def test_price_history_hash_uses_only_fixed_normalized_analysis_ohlc_subset() -> None:
    source, operations, daily = _inputs()
    daily["1111"] = daily["1111"].assign(incidental_vendor_note="before")
    baseline = build_low_mid_falling_candidate_audit(
        source,
        operations,
        daily,
        generated_at=GENERATED_AT,
    )[1]
    baseline_sha = baseline.loc[
        baseline["stock_id"].eq("1111"), "price_history_canonical_sha256"
    ].iloc[0]

    incidental = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    incidental["1111"]["incidental_vendor_note"] = "after"
    incidental_detail = build_low_mid_falling_candidate_audit(
        source,
        operations,
        incidental,
        generated_at=GENERATED_AT,
    )[1]
    assert (
        incidental_detail.loc[
            incidental_detail["stock_id"].eq("1111"),
            "price_history_canonical_sha256",
        ].iloc[0]
        == baseline_sha
    )

    canonical = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    canonical["1111"].loc[0, "analysis_high"] += 0.125
    canonical_detail = build_low_mid_falling_candidate_audit(
        source,
        operations,
        canonical,
        generated_at=GENERATED_AT,
    )[1]
    assert (
        canonical_detail.loc[
            canonical_detail["stock_id"].eq("1111"),
            "price_history_canonical_sha256",
        ].iloc[0]
        != baseline_sha
    )


@pytest.mark.parametrize(
    ("column", "mutated", "message"),
    (
        ("artifact_id", "wrong-source", "source-first artifact id drift"),
        ("artifact_version", "wrong-version", "source-first artifact version drift"),
    ),
)
def test_source_first_contract_mutation_fails_closed(
    column: str,
    mutated: object,
    message: str,
) -> None:
    source, operations, daily = _inputs()
    source.loc[source.index[0], column] = mutated
    with pytest.raises(RuntimeError, match=message):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )


def test_source_first_run_lineage_mutation_changes_row_hash_and_propagates() -> None:
    source, operations, daily = _inputs()
    baseline = build_low_mid_falling_candidate_audit(
        source,
        operations,
        daily,
        generated_at=GENERATED_AT,
    )
    baseline_rows = baseline[1].set_index("episode_key")

    mutated = source.copy()
    mutated["monthly_revenue_canonical_table_sha256"] = "a" * 64
    outputs = build_low_mid_falling_candidate_audit(
        mutated,
        operations,
        daily,
        generated_at=GENERATED_AT,
    )
    mutated_rows = outputs[1].set_index("episode_key")
    assert not mutated_rows["source_first_canonical_row_sha256"].eq(
        baseline_rows["source_first_canonical_row_sha256"]
    ).all()
    for frame in outputs:
        assert set(frame["monthly_revenue_canonical_table_sha256"]) == {"a" * 64}


def test_source_first_run_lineage_invalid_sha_fails_closed() -> None:
    source, operations, daily = _inputs()
    source["cross_market_resolution_registry_canonical_sha256"] = "invalid"
    with pytest.raises(RuntimeError, match="source-first cross_market_resolution"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )


def test_asof_source_payload_lineage_is_selected_from_aligned_lists() -> None:
    _summary, detail, _paired, _contrast = _build()
    assert set(detail["asof_latest_qualifying_cross_market_resolution_id"]) == {
        "none"
    }
    assert set(detail["asof_latest_qualifying_source_row_canonical_sha256"]) == {
        "4" * 64
    }
    assert detail["asof_latest_qualifying_canonical_source_table_date"].astype(
        str
    ).eq(detail["asof_latest_qualifying_source_date"].astype(str)).all()


@pytest.mark.parametrize(
    ("module_name", "constant_name"),
    (
        ("source_first_producer", "ARTIFACT_ID"),
        ("source_first_producer", "ARTIFACT_VERSION"),
        ("source_first_producer", "PRIMARY_VARIANT_ID"),
        ("rearmed_producer", "ARTIFACT_ID"),
        ("rearmed_producer", "ARTIFACT_VERSION"),
        ("rearmed_producer", "SOURCE_ARTIFACT_ID"),
        ("rearmed_producer", "SOURCE_VARIANT_ID"),
        ("rearmed_producer", "NO_STOP_POLICY_ID"),
        ("position_shape_producer", "ARTIFACT_ID"),
        ("position_shape_producer", "ARTIFACT_VERSION"),
        ("position_shape_producer", "SOURCE_VARIANT_ID"),
        ("position_shape_producer", "POSITION_POLICY"),
        ("position_shape_producer", "SHAPE_POLICY"),
        ("position_shape_producer", "PRICE_HISTORY_CUTOFF_DATE"),
    ),
)
def test_upstream_business_contract_constants_are_literal_pins(
    monkeypatch: pytest.MonkeyPatch,
    module_name: str,
    constant_name: str,
) -> None:
    upstream = getattr(low_mid_producer, module_name)
    monkeypatch.setattr(upstream, constant_name, "mutated-upstream-contract")
    source, operations, daily = _inputs()
    with pytest.raises(RuntimeError, match="pinned upstream contract drift"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )


def test_source_variant_and_sequence_index_mutations_fail_closed() -> None:
    source, operations, daily = _inputs()
    source["condition_variant_id"] = "wrong-source-variant"
    with pytest.raises(RuntimeError, match="source variant is empty or drifted"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )

    source, operations, daily = _inputs()
    source.loc[source.index[0], "latest_qualifying_trade_date"] = "19990101"
    with pytest.raises(RuntimeError, match="qualifying scalar/list lineage drift"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )

    source, operations, daily = _inputs()
    original_index = int(source.loc[source.index[0], "qualifying_sequence_indices"])
    next_date = str(daily["1111"].at[original_index + 1, "date"])
    source.loc[source.index[0], "qualifying_trade_dates"] = next_date
    source.loc[source.index[0], "qualifying_sequence_indices"] = str(original_index + 1)
    source.loc[source.index[0], "episode_start_trade_date"] = next_date
    source.loc[source.index[0], "episode_start_sequence_index"] = original_index + 1
    source.loc[source.index[0], "latest_qualifying_trade_date"] = next_date
    source.loc[source.index[0], "latest_qualifying_sequence_index"] = original_index + 1
    with pytest.raises(RuntimeError, match="not the first normalized session"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )

    source, operations, daily = _inputs()
    source.loc[source.index[0], "qualifying_sequence_indices"] = str(
        int(source.loc[source.index[0], "qualifying_sequence_indices"]) + 1
    )
    source.loc[source.index[0], "episode_start_sequence_index"] = int(
        source.loc[source.index[0], "episode_start_sequence_index"]
    ) + 1
    source.loc[source.index[0], "latest_qualifying_sequence_index"] = int(
        source.loc[source.index[0], "latest_qualifying_sequence_index"]
    ) + 1
    with pytest.raises(RuntimeError, match="qualifying sequence index drift"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )

    source, operations, daily = _inputs()
    latest_index = int(source.loc[source.index[0], "qualifying_sequence_indices"])
    first_index = latest_index - 1
    first_date = str(daily["1111"].at[first_index, "date"])
    latest_date = str(daily["1111"].at[latest_index, "date"])
    source.loc[source.index[0], "qualifying_update_count"] = 2
    source.loc[source.index[0], "qualifying_revenue_periods"] = "202512|202601"
    source.loc[source.index[0], "qualifying_source_dates"] = (
        f"{first_date}|{latest_date}"
    )
    source.loc[source.index[0], "qualifying_cross_market_resolution_ids"] = (
        "none|none"
    )
    source.loc[source.index[0], "qualifying_source_row_canonical_sha256s"] = (
        f"{'6' * 64}|{'4' * 64}"
    )
    source.loc[source.index[0], "qualifying_canonical_source_table_dates"] = (
        f"{first_date}|{latest_date}"
    )
    source.loc[source.index[0], "qualifying_trade_dates"] = (
        f"{first_date}|{latest_date}"
    )
    source.loc[source.index[0], "qualifying_sequence_indices"] = (
        f"{first_index}|{first_index}"
    )
    source.loc[source.index[0], "episode_start_revenue_period"] = "202512"
    source.loc[source.index[0], "episode_start_source_date"] = first_date
    source.loc[source.index[0], "episode_start_cross_market_resolution_id"] = "none"
    source.loc[source.index[0], "episode_start_source_row_canonical_sha256"] = (
        "6" * 64
    )
    source.loc[source.index[0], "episode_start_canonical_source_table_date"] = (
        first_date
    )
    source.loc[source.index[0], "episode_start_trade_date"] = first_date
    source.loc[source.index[0], "episode_start_sequence_index"] = first_index
    source.loc[source.index[0], "latest_qualifying_revenue_period"] = "202601"
    source.loc[source.index[0], "latest_qualifying_source_date"] = latest_date
    source.loc[source.index[0], "latest_qualifying_trade_date"] = latest_date
    source.loc[source.index[0], "latest_qualifying_sequence_index"] = first_index
    with pytest.raises(RuntimeError, match="sequence is not strictly increasing"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )


@pytest.mark.parametrize(
    ("column", "mutated", "message"),
    (
        ("artifact_id", "wrong-rearmed", "rearmed artifact id drift"),
        (
            "artifact_version",
            "wrong-version",
            "low/mid falling rearmed artifact version is not constant",
        ),
        ("source_artifact_id", "wrong-source", "rearmed source artifact id drift"),
        ("source_variant_id", "wrong-variant", "rearmed source variant drift"),
        ("lifecycle_policy_id", "wrong-lifecycle", "rearmed lifecycle drift"),
        ("confirmation_variant_id", "wrong-confirmation", "rearmed confirmation drift"),
        ("holding_days", 29, "rearmed grid contract drift"),
        ("stop_policy_id", "wrong-stop", "rearmed grid contract drift"),
        ("entry_price_basis", "analysis_close", "entry price basis drift"),
        (
            "fixed_exit_price_basis",
            "analysis_open",
            "fixed exit price basis drift",
        ),
        ("exit_price_basis", "analysis_open", "selected exit price basis drift"),
        ("exit_reason", "wrong-exit", "selected exit reason drift"),
        ("intraday_operation_basis_used", True, "must be explicitly false"),
        ("entry_index", 999, "recorded entry index drift"),
        ("planned_exit_index", 999, "recorded planned exit index drift"),
        ("exit_index", 999, "recorded exit index drift"),
        ("planned_exit_date", "19990101", "recorded planned exit date drift"),
        ("entry_price", 999.0, "recorded entry price drift"),
        ("exit_price", 999.0, "recorded exit price drift"),
    ),
)
def test_rearmed_contract_mutation_fails_closed(
    column: str,
    mutated: object,
    message: str,
) -> None:
    source, operations, daily = _inputs()
    operations.loc[operations.index[0], column] = mutated
    with pytest.raises(RuntimeError, match=message):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
        )


def test_injected_data_contract_sha_must_match_registered_contract() -> None:
    source, operations, daily = _inputs()
    with pytest.raises(RuntimeError, match="data contract SHA-256 drift"):
        build_low_mid_falling_candidate_audit(
            source,
            operations,
            daily,
            generated_at=GENERATED_AT,
            data_contract_sha256="0" * 64,
        )


def test_episode_first_match_and_same_grid_overlap_fail_closed() -> None:
    source, operations, daily = _inputs()
    duplicate = operations.loc[
        operations["lifecycle_policy_id"].eq("episode_first_match_once")
        & operations["confirmation_variant_id"].eq("base_close_confirmed")
        & operations["stock_id"].eq("2222")
    ].iloc[[0]]
    with pytest.raises(RuntimeError, match="multiple operations per episode"):
        build_low_mid_falling_candidate_audit(
            source,
            pd.concat([operations, duplicate], ignore_index=True),
            daily,
            generated_at=GENERATED_AT,
        )

    overlapping = operations.loc[
        operations["lifecycle_policy_id"].eq(
            "rearm_after_realized_exit_next_trade_day"
        )
        & operations["confirmation_variant_id"].eq("base_close_confirmed")
        & operations["stock_id"].eq("2222")
    ].iloc[0].copy()
    dates = daily["2222"]["date"].astype(str).tolist()
    second_trigger = 230
    second_entry = second_trigger + 1
    second_exit = second_entry + 29
    daily["2222"] = daily["2222"].copy()
    daily["2222"].loc[second_entry, "analysis_open"] = 100.0
    daily["2222"].loc[second_exit, "analysis_close"] = 110.0
    overlapping["trigger_date"] = dates[second_trigger]
    overlapping["confirmation_date"] = dates[second_trigger]
    overlapping["entry_index"] = second_entry
    overlapping["entry_date"] = dates[second_entry]
    overlapping["entry_price"] = 100.0
    overlapping["planned_exit_index"] = second_exit
    overlapping["planned_exit_date"] = dates[second_exit]
    overlapping["exit_index"] = second_exit
    overlapping["exit_date"] = dates[second_exit]
    overlapping["exit_price"] = 110.0
    overlapping["realized_return_pct"] = 10.0
    overlapping["return_outcome"] = "win"
    with pytest.raises(RuntimeError, match="same-stock overlap"):
        build_low_mid_falling_candidate_audit(
            source,
            pd.concat([operations, overlapping.to_frame().T], ignore_index=True),
            daily,
            generated_at=GENERATED_AT,
        )


def test_governance_flags_and_writer_mirrors(tmp_path: Path) -> None:
    summary, detail, paired, contrast = _build()
    for frame in (summary, detail, paired, contrast):
        assert not frame["approved_for_daily"].astype(bool).any()
        assert not frame["presentation_allowed"].astype(bool).any()
        assert not frame["formal_model_use_allowed"].astype(bool).any()
        assert not frame["production_change"].astype(bool).any()
        assert set(frame["financial_statement_scope"]) == {
            FINANCIAL_STATEMENT_SCOPE
        }
    assert set(summary["analysis_basis"]) == set(ANALYSIS_BASES)
    assert len(summary) == (
        len(ANALYSIS_BASES)
        * len(LIFECYCLE_POLICY_IDS)
        * len(CONFIRMATION_VARIANT_IDS)
        * len(VARIANT_SPECS)
    )

    paths = write_low_mid_falling_candidate_audit(
        summary,
        detail,
        paired,
        contrast,
        output_root=tmp_path,
    )
    for family in ("summary", "detail", "paired", "contrast"):
        assert paths[f"{family}_latest"].is_file()
        assert (
            paths[f"{family}_latest"].read_bytes()
            == paths[f"{family}_history"].read_bytes()
            == paths[f"{family}_docs"].read_bytes()
        )
    markdown = paths["markdown_latest"].read_text(encoding="utf-8")
    assert ARTIFACT_ID in str(paths["summary_latest"])
    assert "0～60" in markdown
    assert "research_only" in markdown
    assert paths["markdown_docs"].read_bytes() == paths[
        "markdown_latest"
    ].read_bytes()
