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

from revenue_unreacted_range_position_shape_transition_matrix import (  # noqa: E402
    ADOPTED_GRID_ID,
    ANALYSIS_BASES,
    ANCHOR_IDS,
    ARTIFACT_ID,
    MODEL_ID,
    PRIMARY_ANALYSIS_BASIS,
    SENSITIVITY_ANALYSIS_BASIS,
    SOURCE_OPERATION_LAG_ARTIFACT_ID,
    SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
    SOURCE_REARMED_ARTIFACT_ID,
    SOURCE_REARMED_ARTIFACT_VERSION,
    SOURCE_VARIANT_ID,
    _sha256 as producer_source_file_sha256,
    build_position_shape_transition_matrix,
    canonical_operation_lag_semantic_sha256,
    canonical_rearmed_semantic_sha256,
    write_position_shape_transition_matrix,
)
from validate_revenue_unreacted_range_position_shape_transition_matrix import (  # noqa: E402
    _governance_errors,
    _sha256 as validator_source_file_sha256,
)


def _price_frame() -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-02", periods=200).strftime("%Y%m%d")
    close = np.full(200, 100.0)
    close[97:125] = 90.0
    close[125:152] = np.linspace(90.0, 115.0, 27)
    close[152:] = 115.0
    high = close + 1.0
    low = close - 1.0
    high[80] = 120.0
    low[81] = 80.0
    return pd.DataFrame(
        {
            "date": dates,
            "analysis_open": close,
            "analysis_high": high,
            "analysis_low": low,
            "analysis_close": close,
            # Raw columns deliberately disagree. The matrix must use analysis_* only.
            "open": 999.0,
            "high": 1000.0,
            "low": 998.0,
            "close": 999.0,
        }
    )


def _operation_source(price: pd.DataFrame) -> pd.DataFrame:
    dates = price["date"].astype(str).tolist()
    rows = []
    for stock_id, source_index, return_pct, source_candidate in (
        ("1111", 120, 25.0, False),
        ("2222", 149, -10.0, True),
    ):
        rows.append(
            {
                "model_id": MODEL_ID,
                "artifact_id": SOURCE_OPERATION_LAG_ARTIFACT_ID,
                "artifact_version": SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
                "source_variant_id": SOURCE_VARIANT_ID,
                "grid_id": ADOPTED_GRID_ID,
                "episode_key": f"episode-{stock_id}",
                "stock_id": stock_id,
                "stock_name": f"stock-{stock_id}",
                "asof_latest_qualifying_source_date": dates[source_index],
                "asof_latest_qualifying_trade_date": dates[source_index],
                "trigger_date": dates[150],
                "confirmation_date": dates[151],
                "entry_date": dates[152],
                "exit_date": dates[181],
                "latest_source_to_trigger_trading_days": 150 - source_index,
                "first_source_to_trigger_trading_days": 150 - source_index,
                "realized_return_pct": return_pct,
                "return_outcome": "win" if return_pct > 0 else "failure",
                "realized_return_ge20": return_pct >= 20.0,
                "source_anomaly_candidate_flag": source_candidate,
                "operation_return_review_candidate_flag": False,
                "time_travel_guard_passed": True,
                "same_stock_non_overlap_applied": True,
            }
        )
    return pd.DataFrame(rows)


def _rearmed_lineage(source: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "grid_id",
        "episode_key",
        "stock_id",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
        "realized_return_pct",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "operation_return_review_candidate_flag",
    ]
    enriched = source.copy()
    enriched["unresolved_price_path_candidate_flag"] = enriched["stock_id"].eq("2222")
    lineage = enriched.loc[:, columns].copy()
    lineage["artifact_id"] = SOURCE_REARMED_ARTIFACT_ID
    lineage["artifact_version"] = SOURCE_REARMED_ARTIFACT_VERSION
    lineage["return_valid"] = True
    return lineage


def _build() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    price = _price_frame()
    source = _operation_source(price)
    summary, detail, transition = build_position_shape_transition_matrix(
        source,
        rearmed_detail=_rearmed_lineage(source),
        daily_by_stock={"1111": price, "2222": price},
        generated_at="2026-07-17 12:00:00 Asia/Taipei",
        enforce_pinned_baseline=False,
    )
    return summary, detail, transition, price


def test_three_anchor_detail_uses_adjusted_prices_and_exact_anchor_offsets() -> None:
    _summary, detail, _transition, price = _build()
    assert len(detail) == 6
    first = detail.loc[
        detail["stock_id"].eq("1111") & detail["anchor_id"].eq("revenue_available")
    ].iloc[0]
    preweek = detail.loc[
        detail["stock_id"].eq("1111")
        & detail["anchor_id"].eq("pre_breakout_week_close")
    ].iloc[0]
    confirmation = detail.loc[
        detail["stock_id"].eq("1111")
        & detail["anchor_id"].eq("formal_confirmation_close")
    ].iloc[0]

    assert first["anchor_date"] == price.at[120, "date"]
    assert preweek["anchor_date"] == price.at[145, "date"]
    assert confirmation["anchor_date"] == price.at[151, "date"]
    assert first["position_window_start_date"] == price.at[0, "date"]
    assert first["position_window_end_date"] == price.at[119, "date"]
    assert first["position_prior_session_count"] == 120
    assert first["anchor_adjusted_close"] == 90.0
    assert first["position_120d_pct"] == 25.0
    assert first["position_bucket"] == "low_pos_le40"
    assert first["shape_bucket"] == "consolidation"
    assert preweek["position_bucket"] == "mid_pos_40_75"
    assert preweek["shape_bucket"] == "rising"
    assert confirmation["position_bucket"] == "high_pos_gt75"
    assert confirmation["shape_bucket"] == "rising"
    assert detail["price_basis"].eq("adjusted_analysis_ohlc_only").all()


def test_latest_source_after_preweek_is_labeled_without_fake_chronology() -> None:
    _summary, detail, transition, _price = _build()
    early = detail.loc[detail["stock_id"].eq("1111")]
    late = detail.loc[detail["stock_id"].eq("2222")]
    assert early["source_before_or_on_preweek_flag"].astype(bool).all()
    assert early["anchor_chronology_id"].eq("source_before_or_on_preweek").all()
    assert not late["source_before_or_on_preweek_flag"].astype(bool).any()
    assert late["anchor_chronology_id"].eq(
        "latest_source_arrived_after_preweek_before_or_on_trigger"
    ).all()
    primary_paths = transition.loc[
        transition["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & ~transition["row_type"].eq("overall_state_comparison")
    ]
    assert set(primary_paths["anchor_chronology_id"]) == {
        "source_before_or_on_preweek",
        "latest_source_arrived_after_preweek_before_or_on_trigger",
    }
    late_path = primary_paths.loc[
        primary_paths["row_type"].eq("nonchronological_anchor_state_sequence")
        & primary_paths["anchor_chronology_id"].eq(
            "latest_source_arrived_after_preweek_before_or_on_trigger"
        )
    ].iloc[0]
    assert (
        late_path["comparison_sequence_semantics"]
        == "labeled_anchor_comparison_not_chronological_latest_source_after_preweek"
    )
    assert late_path["row_type"] == "nonchronological_anchor_state_sequence"
    early_path = primary_paths.loc[
        primary_paths["row_type"].eq("chronological_transition")
    ].iloc[0]
    assert early_path["anchor_chronology_id"] == "source_before_or_on_preweek"


def test_cell_summary_has_twelve_cells_plus_insufficient_and_conserves_bases() -> None:
    summary, _detail, transition, _price = _build()
    assert len(summary) == 2 * 3 * 13
    assert set(summary["analysis_basis"]) == set(ANALYSIS_BASES)
    for analysis_basis, expected in (
        (PRIMARY_ANALYSIS_BASIS, 2),
        (SENSITIVITY_ANALYSIS_BASIS, 1),
    ):
        for anchor_id in ANCHOR_IDS:
            cells = summary.loc[
                summary["analysis_basis"].eq(analysis_basis)
                & summary["anchor_id"].eq(anchor_id)
            ]
            assert len(cells) == 13
            assert int(cells["operation_count"].sum()) == expected
            assert int(cells["analysis_basis_operation_count"].iloc[0]) == expected
        overall = transition.loc[
            transition["analysis_basis"].eq(analysis_basis)
            & transition["row_type"].eq("overall_state_comparison")
        ].iloc[0]
        assert int(overall["operation_count"]) == expected
        if analysis_basis == PRIMARY_ANALYSIS_BASIS:
            assert int(overall["unresolved_price_path_candidate_count"]) == 1
    sensitivity = summary.loc[
        summary["analysis_basis"].eq(SENSITIVITY_ANALYSIS_BASIS)
    ]
    assert int(sensitivity["combined_exclusion_candidate_count"].sum()) == 0


def test_incomplete_120_session_history_is_kept_in_insufficient_cell() -> None:
    price = _price_frame().iloc[20:].reset_index(drop=True)
    source = _operation_source(_price_frame()).iloc[[0]].copy()
    # Remap the same logical operation to the shortened frame.
    dates = price["date"].astype(str).tolist()
    source["asof_latest_qualifying_source_date"] = dates[100]
    source["asof_latest_qualifying_trade_date"] = dates[100]
    source["trigger_date"] = dates[130]
    source["confirmation_date"] = dates[131]
    source["entry_date"] = dates[132]
    source["exit_date"] = dates[161]
    source["latest_source_to_trigger_trading_days"] = 30
    source["first_source_to_trigger_trading_days"] = 30
    summary, detail, _transition = build_position_shape_transition_matrix(
        source,
        rearmed_detail=_rearmed_lineage(source),
        daily_by_stock={"1111": price},
        enforce_pinned_baseline=False,
    )
    revenue = detail.loc[detail["anchor_id"].eq("revenue_available")].iloc[0]
    assert revenue["position_prior_session_count"] == 100
    assert not bool(revenue["classification_observed"])
    assert revenue["position_shape_cell_id"] == "insufficient_history"
    revenue_summary = summary.loc[
        summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & summary["anchor_id"].eq("revenue_available")
        & summary["position_shape_cell_id"].eq("insufficient_history")
    ].iloc[0]
    assert int(revenue_summary["operation_count"]) == 1
    primary_paths = _transition.loc[
        _transition["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & ~_transition["row_type"].eq("overall_state_comparison")
    ]
    assert primary_paths.empty


def test_rearmed_lineage_drift_fails_closed() -> None:
    price = _price_frame()
    source = _operation_source(price)
    rearmed = _rearmed_lineage(source)
    rearmed.loc[0, "realized_return_pct"] = 99.0
    with pytest.raises(RuntimeError, match="return drift"):
        build_position_shape_transition_matrix(
            source,
            rearmed_detail=rearmed,
            daily_by_stock={"1111": price, "2222": price},
            enforce_pinned_baseline=False,
        )


def test_canonical_semantic_hash_ignores_generated_at_and_input_order() -> None:
    price = _price_frame()
    source = _operation_source(price)
    source["generated_at"] = "first"
    left = canonical_operation_lag_semantic_sha256(source)
    source["generated_at"] = "second"
    right = canonical_operation_lag_semantic_sha256(
        source.iloc[::-1].reset_index(drop=True)
    )
    assert left == right

    rearmed = _rearmed_lineage(source)
    rearmed["generated_at"] = "first"
    lineage_left = canonical_rearmed_semantic_sha256(rearmed)
    rearmed["generated_at"] = "second"
    lineage_right = canonical_rearmed_semantic_sha256(
        rearmed.iloc[::-1].reset_index(drop=True)
    )
    assert lineage_left == lineage_right


def test_source_file_sha_is_stable_across_windows_and_linux_line_endings(
    tmp_path: Path,
) -> None:
    lf_path = tmp_path / "source_lf.csv"
    crlf_path = tmp_path / "source_crlf.csv"
    lf_path.write_bytes(b"column_a,column_b\n1,2\n3,4\n")
    crlf_path.write_bytes(b"column_a,column_b\r\n1,2\r\n3,4\r\n")

    expected = producer_source_file_sha256(lf_path)
    assert producer_source_file_sha256(crlf_path) == expected
    assert validator_source_file_sha256(lf_path) == expected
    assert validator_source_file_sha256(crlf_path) == expected


def test_raw_only_price_frame_is_rejected() -> None:
    price = _price_frame().drop(
        columns=["analysis_open", "analysis_high", "analysis_low", "analysis_close"]
    )
    source = _operation_source(_price_frame()).iloc[[0]].copy()
    with pytest.raises(RuntimeError, match="adjusted price frame is missing"):
        build_position_shape_transition_matrix(
            source,
            rearmed_detail=_rearmed_lineage(source),
            daily_by_stock={"1111": price},
            enforce_pinned_baseline=False,
        )


def test_writer_accepts_explicit_output_root_and_path_override(tmp_path: Path) -> None:
    summary, detail, transition, _price = _build()
    custom_summary = tmp_path / "custom" / "summary.csv"
    paths = write_position_shape_transition_matrix(
        summary,
        detail,
        transition,
        output_root=tmp_path,
        output_paths={"summary_latest": custom_summary},
    )
    assert paths["summary_latest"] == custom_summary
    assert custom_summary.is_file()
    assert paths["detail_latest"].is_file()
    assert paths["transition_latest"].is_file()
    assert paths["markdown_latest"].is_file()
    assert paths["summary_history"].read_bytes() == custom_summary.read_bytes()
    markdown = paths["markdown_latest"].read_text(encoding="utf-8")
    assert "asof_latest_qualifying_trade_date" in markdown
    assert "chronological transition" in markdown


def test_independent_validator_does_not_import_the_producer_business_module() -> None:
    validator = (
        ROOT / "scripts" / "validate_revenue_unreacted_range_position_shape_transition_matrix.py"
    ).read_text(encoding="utf-8")
    assert "from revenue_unreacted_range_position_shape_transition_matrix import" not in validator
    assert "import revenue_unreacted_range_position_shape_transition_matrix" not in validator
    assert "from build_revenue_unreacted_range_research import" not in validator


@pytest.mark.parametrize("frame_name", ["summary", "detail", "transition"])
def test_validator_rejects_presentation_allowed_drift(frame_name: str) -> None:
    summary, detail, transition, _price = _build()
    frames = {"summary": summary, "detail": detail, "transition": transition}
    mutated = frames[frame_name].copy()
    mutated["presentation_allowed"] = True

    errors = _governance_errors(mutated, frame_name, {})

    assert f"{frame_name} must keep presentation_allowed=False" in errors


def test_model_owned_builder_and_workflows_route_the_new_stage_and_validator() -> None:
    builder = (ROOT / "scripts" / "build_revenue_unreacted_range_research.py").read_text(
        encoding="utf-8"
    )
    assert "position_shape_transition_matrix" in builder
    assert "build_position_shape_transition_matrix()" in builder
    assert "write_position_shape_transition_matrix(" in builder
    validator_command = (
        "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py"
    )
    for workflow_path in (
        ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml",
        ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml",
    ):
        assert validator_command in workflow_path.read_text(encoding="utf-8")
