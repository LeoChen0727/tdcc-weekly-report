from __future__ import annotations

import ast
import sys
from pathlib import Path
import subprocess

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_low_mid_falling_candidate_audit as producer  # noqa: E402
import revenue_unreacted_range_source_snapshot_projection as projection  # noqa: E402
import validate_revenue_unreacted_range_low_mid_falling_candidate_audit as validator  # noqa: E402


GENERATED_AT = "2026-07-20 12:00:00 Asia/Taipei"
TRIGGER_INDEX = 220


def test_low_mid_versions_follow_rearmed_generation() -> None:
    assert producer.versions_for_rearmed_artifact(producer.REARMED_ARTIFACT_VERSION) == (
        producer.V1_ARTIFACT_VERSION,
        producer.POSITION_SHAPE_ARTIFACT_VERSION,
        producer.SOURCE_PROJECTION_ARTIFACT_VERSION,
    )
    assert producer.versions_for_rearmed_artifact(
        producer.V2_REARMED_ARTIFACT_VERSION
    ) == (
        producer.V2_ARTIFACT_VERSION,
        producer.V2_POSITION_SHAPE_ARTIFACT_VERSION,
        producer.V2_SOURCE_PROJECTION_ARTIFACT_VERSION,
    )
    assert validator._version_contract(projection.V2_PROJECTION_VERSION) == (
        validator.V2_ARTIFACT_VERSION,
        validator.V2_REARMED_ARTIFACT_VERSION,
        validator.V2_POSITION_SHAPE_ARTIFACT_VERSION,
    )
    with pytest.raises(RuntimeError, match="unsupported rearmed artifact version"):
        producer.versions_for_rearmed_artifact("unknown")
    with pytest.raises(
        RuntimeError,
        match="unsupported canonical source projection version",
    ):
        validator._version_contract("unknown")


def _v1_manifest_frame() -> pd.DataFrame:
    return pd.DataFrame([validator.EXPECTED_V1_MANIFEST_DESCRIPTOR])


def _completed(
    returncode: int = 0,
    *,
    stdout: bytes = b"",
    stderr: bytes = b"",
) -> subprocess.CompletedProcess[bytes]:
    return subprocess.CompletedProcess([], returncode, stdout=stdout, stderr=stderr)


def test_strict_integral_accepts_csv_integer_float_text_only() -> None:
    assert validator._strict_integral("215", label="sequence index") == 215
    assert validator._strict_integral("215.0", label="sequence index") == 215
    assert validator._strict_integral(215.0, label="sequence index") == 215

    for invalid in ("215.5", "nan", "inf", "not-a-number", ""):
        with pytest.raises(ValueError):
            validator._strict_integral(invalid, label="sequence index")


def test_canonical_hash_is_stable_across_csv_numeric_and_boolean_text() -> None:
    in_memory = pd.DataFrame(
        [
            {
                "stock_id": "0050",
                "sequence_index": 215.0,
                "candidate_flag": True,
                "ratio": 0.1,
                "zero": -0.0,
            }
        ]
    )
    csv_round_trip = pd.DataFrame(
        [
            {
                "stock_id": "0050",
                "sequence_index": "215.0",
                "candidate_flag": "True",
                "ratio": "0.1000",
                "zero": "-0.0",
            }
        ]
    )

    assert producer._canonical_table_sha256(in_memory) == producer._canonical_table_sha256(
        csv_round_trip
    )
    assert validator._canonical_table_sha256(
        in_memory
    ) == validator._canonical_table_sha256(csv_round_trip)
    assert producer._canonical_table_sha256(in_memory) == validator._canonical_table_sha256(
        csv_round_trip
    )
    assert producer._canonical_value("0050") == "0050"
    assert validator._canonical_value("0050") == "0050"
    assert producer._canonical_value(50) == "50"
    assert validator._canonical_value(50) == "50"


def _price_frame(source_index: int, position: str, return_pct: float) -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-02", periods=290).strftime("%Y%m%d")
    target = 90.0 if position == "low" else 100.0
    close = np.full(290, 110.0)
    close[source_index - 25 : source_index + 1] = np.linspace(112.0, target, 26)
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
            "open": analysis_open,
            "high": high,
            "low": low,
            "close": close,
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
    *,
    with_future_update: bool = False,
) -> dict[str, object]:
    indices = [source_index, 230] if with_future_update else [source_index]
    source_dates = [str(price.at[index, "date"]) for index in indices]
    periods = ["202601", "202602"] if with_future_update else ["202601"]
    resolution_ids = ["none"] * len(indices)
    source_hashes = [str(offset + 4) * 64 for offset in range(len(indices))]
    return {
        "model_id": validator.MODEL_ID,
        "artifact_id": validator.SOURCE_FIRST_ARTIFACT_ID,
        "artifact_version": validator.SOURCE_FIRST_ARTIFACT_VERSION,
        "monthly_revenue_history_blob_sha256": "1" * 64,
        "monthly_revenue_canonical_table_sha256": "2" * 64,
        "cross_market_resolution_registry_canonical_sha256": "3" * 64,
        "condition_variant_id": validator.SOURCE_VARIANT_ID,
        "episode_key": f"episode-{stock_id}",
        "stock_id": stock_id,
        "stock_name": stock_name,
        "episode_start_revenue_period": periods[0],
        "episode_start_source_date": source_dates[0],
        "episode_start_cross_market_resolution_id": resolution_ids[0],
        "episode_start_source_row_canonical_sha256": source_hashes[0],
        "episode_start_canonical_source_table_date": source_dates[0],
        "episode_start_trade_date": source_dates[0],
        "episode_start_sequence_index": indices[0],
        "episode_end_date": str(price.at[250, "date"]),
        "latest_qualifying_revenue_period": periods[-1],
        "latest_qualifying_source_date": source_dates[-1],
        "latest_qualifying_cross_market_resolution_id": resolution_ids[-1],
        "latest_qualifying_source_row_canonical_sha256": source_hashes[-1],
        "latest_qualifying_canonical_source_table_date": source_dates[-1],
        "latest_qualifying_trade_date": source_dates[-1],
        "latest_qualifying_sequence_index": indices[-1],
        "qualifying_update_count": len(indices),
        "qualifying_revenue_periods": "|".join(periods),
        "qualifying_source_dates": "|".join(source_dates),
        "qualifying_cross_market_resolution_ids": "|".join(resolution_ids),
        "qualifying_source_row_canonical_sha256s": "|".join(source_hashes),
        "qualifying_canonical_source_table_dates": "|".join(source_dates),
        "qualifying_trade_dates": "|".join(source_dates),
        "qualifying_sequence_indices": "|".join(str(index) for index in indices),
    }


def _operation_rows(
    stock_id: str,
    stock_name: str,
    price: pd.DataFrame,
    *,
    source_candidate: bool,
    artifact_version: str = validator.REARMED_ARTIFACT_VERSION,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    dates = price["date"].astype(str).tolist()
    for lifecycle_id in validator.LIFECYCLE_POLICY_IDS:
        for confirmation_id in validator.CONFIRMATION_VARIANT_IDS:
            delayed = confirmation_id == "delayed_next_close_continuation_bonus"
            confirmation_index = TRIGGER_INDEX + (1 if delayed else 0)
            entry_index = confirmation_index + 1
            exit_index = entry_index + validator.HOLDING_DAYS - 1
            entry = float(price.at[entry_index, "analysis_open"])
            exit_close = float(price.at[exit_index, "analysis_close"])
            realized = (exit_close / entry - 1.0) * 100.0
            rows.append(
                {
                    "model_id": validator.MODEL_ID,
                    "artifact_id": validator.REARMED_ARTIFACT_ID,
                    "artifact_version": artifact_version,
                    "source_artifact_id": validator.SOURCE_FIRST_ARTIFACT_ID,
                    "source_variant_id": validator.SOURCE_VARIANT_ID,
                    "grid_id": (
                        f"{lifecycle_id}|{confirmation_id}|d"
                        f"{validator.HOLDING_DAYS}|{validator.NO_STOP_POLICY_ID}"
                    ),
                    "lifecycle_policy_id": lifecycle_id,
                    "confirmation_variant_id": confirmation_id,
                    "holding_days": validator.HOLDING_DAYS,
                    "stop_policy_id": validator.NO_STOP_POLICY_ID,
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
                    "entry_price_basis": "analysis_open",
                    "fixed_exit_price_basis": "analysis_close",
                    "exit_price_basis": "fixed_future_close",
                    "exit_reason": "fixed_d30_close",
                    "intraday_operation_basis_used": False,
                    "realized_return_pct": round(realized, 4),
                    "return_outcome": (
                        "win"
                        if realized > 0
                        else "failure"
                        if realized < 0
                        else "neutral"
                    ),
                    "source_anomaly_candidate_flag": source_candidate,
                    "unresolved_price_path_candidate_flag": False,
                    "operation_return_review_candidate_flag": False,
                }
            )
    return rows


def _build_fixture(
    root: Path,
    *,
    projection_version: str = validator.V1_PROJECTION_VERSION,
) -> dict[str, Path]:
    (
        _expected_artifact_version,
        rearmed_artifact_version,
        _expected_position_shape_artifact_version,
    ) = validator._version_contract(projection_version)
    specs = (
        ("1111", "low-60", 160, "low", 25.0, True, True),
        ("2222", "mid-50", 170, "mid", -10.0, False, False),
        ("3333", "mid-61", 159, "mid", 5.0, False, False),
    )
    source_rows: list[dict[str, object]] = []
    operation_rows: list[dict[str, object]] = []
    daily: dict[str, pd.DataFrame] = {}
    price_dir = root / validator.SOURCE_RELATIVE_PATHS["price_dir"]
    price_dir.mkdir(parents=True, exist_ok=True)
    producer_copy = root / validator.PRODUCER_RELATIVE_PATH
    producer_copy.parent.mkdir(parents=True, exist_ok=True)
    producer_copy.write_bytes(Path(producer.__file__).read_bytes())
    for relative_path in (
        validator.SOURCE_FIRST_PRODUCER_RELATIVE_PATH,
        validator.REARMED_PRODUCER_RELATIVE_PATH,
        validator.POSITION_SHAPE_PRODUCER_RELATIVE_PATH,
        validator.DATA_SHARING_REGISTRY_RELATIVE_PATH,
        validator.BACKGROUND_REGISTRY_RELATIVE_PATH,
    ):
        destination = root / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((ROOT / relative_path).read_bytes())
    for (
        stock_id,
        stock_name,
        source_index,
        position,
        return_pct,
        source_candidate,
        with_future_update,
    ) in specs:
        price = _price_frame(source_index, position, return_pct)
        daily[stock_id] = price.loc[
            :,
            [
                "date",
                "analysis_open",
                "analysis_high",
                "analysis_low",
                "analysis_close",
            ],
        ].copy()
        raw_price_path = price_dir / f"{stock_id}.csv"
        price.loc[:, ["date", "open", "high", "low", "close"]].to_csv(
            raw_price_path, index=False
        )
        roundtripped = pd.read_csv(raw_price_path, low_memory=False)
        daily[stock_id] = roundtripped.rename(
            columns={
                "open": "analysis_open",
                "high": "analysis_high",
                "low": "analysis_low",
                "close": "analysis_close",
            }
        ).loc[
            :,
            [
                "date",
                "analysis_open",
                "analysis_high",
                "analysis_low",
                "analysis_close",
            ],
        ]
        source_rows.append(
            _source_row(
                stock_id,
                stock_name,
                price,
                source_index,
                with_future_update=with_future_update,
            )
        )
        operation_rows.extend(
            _operation_rows(
                stock_id,
                stock_name,
                price,
                source_candidate=source_candidate,
                artifact_version=rearmed_artifact_version,
            )
        )
    source = pd.DataFrame(source_rows)
    operations = pd.DataFrame(operation_rows)
    summary, detail, paired, contrast = producer.build_low_mid_falling_candidate_audit(
        source,
        operations,
        daily,
        generated_at=GENERATED_AT,
    )
    paths = producer.write_low_mid_falling_candidate_audit(
        summary,
        detail,
        paired,
        contrast,
        output_root=root,
    )
    source_path = root / validator.SOURCE_RELATIVE_PATHS["source_first"]
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source.to_csv(source_path, index=False, encoding="utf-8-sig")
    projected_source = pd.read_csv(
        source_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    manifest_columns = (
        validator.V2_PROJECTION_MANIFEST_COLUMNS
        if projection_version == validator.V2_PROJECTION_VERSION
        else validator.V1_PROJECTION_MANIFEST_COLUMNS
    )
    manifest_row = {column: "" for column in manifest_columns}
    source_dates = (
        projected_source["qualifying_source_dates"]
        .astype(str)
        .str.split("|")
        .explode()
        .tolist()
    )
    trade_dates = (
        projected_source["qualifying_trade_dates"]
        .astype(str)
        .str.split("|")
        .explode()
        .tolist()
    )
    manifest_row.update(
        {
            "generated_at": GENERATED_AT,
            "model_id": projection.MODEL_ID,
            "artifact_id": projection.ARTIFACT_ID,
            "artifact_version": projection_version,
            "projection_id": projection.PROJECTION_ID,
            "projection_version": projection_version,
            "projection_policy_id": (
                validator.V2_PROJECTION_POLICY_ID
                if projection_version == validator.V2_PROJECTION_VERSION
                else validator.V1_PROJECTION_POLICY_ID
            ),
            "cutoff_date": projection.CUTOFF_DATE,
            "full_source_artifact_id": validator.SOURCE_FIRST_ARTIFACT_ID,
            "full_source_artifact_version": validator.SOURCE_FIRST_ARTIFACT_VERSION,
            "full_source_episode_row_count": len(projected_source),
            "full_source_episode_semantic_sha256": "4" * 64,
            "monthly_revenue_history_blob_sha256": "1" * 64,
            "monthly_revenue_canonical_table_sha256": "5" * 64,
            "cross_market_resolution_registry_canonical_sha256": "3" * 64,
            "cutoff_revenue_subset_row_count": len(projected_source),
            "cutoff_revenue_subset_semantic_sha256": "2" * 64,
            "cutoff_price_input_stock_count": projected_source["stock_id"].nunique(),
            "cutoff_price_input_row_count": 1,
            "cutoff_price_input_file_semantic_sha256s": "synthetic",
            "cutoff_price_input_semantic_sha256": "6" * 64,
            "applied_monthly_resolution_count": 0,
            "applied_monthly_resolution_ids": "none",
            "applied_monthly_resolution_semantic_sha256": "7" * 64,
            "applied_price_resolution_count": 0,
            "applied_price_resolution_ids": "none",
            "applied_price_resolution_semantic_sha256": "8" * 64,
            "projected_episode_row_count": len(projected_source),
            "projected_episode_semantic_sha256": (
                projection.canonical_projected_source_detail_semantic_sha256(
                    projected_source
                )
            ),
            "projected_max_source_date": max(source_dates),
            "projected_max_trade_date": max(trade_dates),
            "projected_max_episode_end_date": max(
                projected_source["episode_end_date"].astype(str)
            ),
            "research_only": True,
            "formal_model_use_allowed": False,
            "approved_for_daily": False,
            "production_change": False,
            "promotion_evidence_allowed": False,
            "ranking_consumption_allowed": False,
            "pdf_consumption_allowed": False,
        }
    )
    if projection_version == validator.V2_PROJECTION_VERSION:
        manifest_row.update(
            {
                "predecessor_projection_version": validator.V1_PROJECTION_VERSION,
                "predecessor_manifest_bytes_sha256": (
                    validator.V1_PREDECESSOR_MANIFEST_SHA256
                ),
                "predecessor_detail_bytes_sha256": (
                    validator.V1_PREDECESSOR_DETAIL_SHA256
                ),
                "lineage_change_reason": validator.V2_LINEAGE_CHANGE_REASON,
                "candidate_status": validator.V2_CANDIDATE_STATUS,
            }
        )
    projection_manifest_path = root / validator.SOURCE_RELATIVE_PATHS[
        "projection_manifest"
    ]
    projection_manifest_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([manifest_row], columns=manifest_columns).to_csv(
        projection_manifest_path,
        index=False,
    )
    rearmed_path = root / validator.SOURCE_RELATIVE_PATHS["rearmed"]
    serialized_operations = operations.copy()
    serialized_operations["planned_exit_index"] = serialized_operations[
        "planned_exit_index"
    ].map(lambda value: f"{float(value):.1f}")
    serialized_operations.to_csv(rearmed_path, index=False, encoding="utf-8-sig")
    return paths


def _rewrite_family(paths: dict[str, Path], family: str, frame: pd.DataFrame) -> None:
    frame.to_csv(
        paths[f"{family}_latest"],
        index=False,
        encoding="utf-8-sig",
        lineterminator="\n",
    )
    paths[f"{family}_history"].write_bytes(paths[f"{family}_latest"].read_bytes())
    paths[f"{family}_docs"].write_bytes(paths[f"{family}_latest"].read_bytes())


def test_validator_is_independent_and_accepts_synthetic_replay(tmp_path: Path) -> None:
    paths = _build_fixture(tmp_path)

    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    imported_modules = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    imported_modules.update(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    )
    assert (
        "revenue_unreacted_range_low_mid_falling_candidate_audit"
        not in imported_modules
    )
    assert imported_modules.isdisjoint(
        {
            "revenue_unreacted_range_source_snapshot_projection",
            "validate_revenue_unreacted_range_source_snapshot_projection",
        }
    )
    assert validator.validate(artifact_root=tmp_path, source_root=tmp_path) == []
    detail = pd.read_csv(
        paths["detail_latest"],
        dtype={
            "stock_id": str,
            "asof_latest_qualifying_source_row_canonical_sha256": str,
        },
        keep_default_na=False,
    )
    row = detail.loc[detail["stock_id"].eq("1111")].iloc[0]
    assert row["asof_latest_qualifying_cross_market_resolution_id"] == "none"
    assert row["asof_latest_qualifying_source_row_canonical_sha256"] == "4" * 64
    assert (
        str(row["asof_latest_qualifying_canonical_source_table_date"])
        == str(row["asof_latest_qualifying_source_date"])
    )


def test_validator_accepts_synthetic_v2_governance(tmp_path: Path) -> None:
    paths = _build_fixture(
        tmp_path,
        projection_version=validator.V2_PROJECTION_VERSION,
    )

    assert validator.validate(artifact_root=tmp_path, source_root=tmp_path) == []
    for path_key in (
        "summary_latest",
        "detail_latest",
        "paired_latest",
        "contrast_latest",
    ):
        frame = pd.read_csv(paths[path_key], keep_default_na=False)
        assert set(frame["artifact_version"].astype(str)) == {
            validator.V2_ARTIFACT_VERSION
        }


@pytest.mark.parametrize(
    ("family", "label"),
    (
        ("summary", "summary"),
        ("detail", "detail"),
        ("paired", "paired"),
        ("contrast", "feature_contrast"),
    ),
)
def test_validator_rejects_v2_artifact_version_drift(
    tmp_path: Path,
    family: str,
    label: str,
) -> None:
    paths = _build_fixture(
        tmp_path,
        projection_version=validator.V2_PROJECTION_VERSION,
    )
    frame = pd.read_csv(paths[f"{family}_latest"], keep_default_na=False)
    frame.loc[:, "artifact_version"] = validator.ARTIFACT_VERSION
    _rewrite_family(paths, family, frame)

    errors = validator.validate(artifact_root=tmp_path, source_root=tmp_path)

    assert f"{label} governance drift: artifact_version" in errors


def test_validator_rejects_v2_projection_with_v1_rearmed_input(
    tmp_path: Path,
) -> None:
    _build_fixture(
        tmp_path,
        projection_version=validator.V2_PROJECTION_VERSION,
    )
    rearmed_path = tmp_path / validator.SOURCE_RELATIVE_PATHS["rearmed"]
    rearmed = pd.read_csv(rearmed_path, keep_default_na=False)
    rearmed.loc[:, "artifact_version"] = validator.REARMED_ARTIFACT_VERSION
    rearmed.to_csv(rearmed_path, index=False, encoding="utf-8-sig")

    errors = validator.validate(artifact_root=tmp_path, source_root=tmp_path)

    assert "rearmed governance or price-basis drift: artifact_version" in errors


def test_validator_rejects_latest_known_source_and_watch_horizon_drift(
    tmp_path: Path,
) -> None:
    paths = _build_fixture(tmp_path)
    detail = pd.read_csv(paths["detail_latest"], dtype={"stock_id": str})
    row = detail.index[detail["stock_id"].eq("1111")][0]
    assert int(detail.at[row, "future_qualifying_update_ignored_count"]) == 1
    detail.at[row, "latest_source_to_trigger_trading_days"] = 61
    _rewrite_family(paths, "detail", detail)

    errors = validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    assert any("latest_source_to_trigger_trading_days drift" in error for error in errors)


def test_validator_rejects_d30_price_replay_and_timing_drift(tmp_path: Path) -> None:
    _build_fixture(tmp_path)
    rearmed_path = tmp_path / validator.SOURCE_RELATIVE_PATHS["rearmed"]
    rearmed = pd.read_csv(rearmed_path, dtype={"stock_id": str})
    rearmed.loc[0, "realized_return_pct"] = 999.0
    rearmed.to_csv(rearmed_path, index=False, encoding="utf-8-sig")

    errors = validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    assert any("D30 open-to-close replay drift" in error for error in errors)


def test_validator_rejects_union_summary_paired_and_contrast_drift(
    tmp_path: Path,
) -> None:
    paths = _build_fixture(tmp_path)
    detail = pd.read_csv(paths["detail_latest"], dtype={"stock_id": str})
    detail.loc[0, "low_or_mid_falling_union_member"] = False
    _rewrite_family(paths, "detail", detail)
    assert any(
        "low_or_mid_falling_union_member drift" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    paths = _build_fixture(tmp_path)
    summary = pd.read_csv(paths["summary_latest"])
    summary.loc[0, "operation_count"] = 999
    _rewrite_family(paths, "summary", summary)
    assert any(
        "metric drift: operation_count" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    paths = _build_fixture(tmp_path)
    paired = pd.read_csv(paths["paired_latest"], dtype={"stock_id": str})
    paired.loc[0, "delayed_minus_base_return_pct_points"] = 999.0
    _rewrite_family(paths, "paired", paired)
    assert any(
        "delayed_minus_base_return_pct_points drift" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    paths = _build_fixture(tmp_path)
    contrast = pd.read_csv(paths["contrast_latest"])
    contrast.loc[0, "high_mean"] = 999.0
    _rewrite_family(paths, "contrast", contrast)
    assert any(
        "metric drift: high_mean" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )


def test_validator_rejects_formal_flag_and_byte_mirror_drift(tmp_path: Path) -> None:
    paths = _build_fixture(tmp_path)
    summary = pd.read_csv(paths["summary_latest"])
    summary.loc[0, "formal_model_use_allowed"] = True
    _rewrite_family(paths, "summary", summary)
    assert any(
        "formal_model_use_allowed=False" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    paths = _build_fixture(tmp_path)
    paths["detail_docs"].write_bytes(paths["detail_docs"].read_bytes() + b"\n")
    assert any(
        "detail latest/history/docs byte mirrors drift" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )


def test_validator_rejects_lineage_and_registered_contract_drift(
    tmp_path: Path,
) -> None:
    paths = _build_fixture(tmp_path)
    detail = pd.read_csv(paths["detail_latest"], dtype={"stock_id": str})
    original = detail.copy()
    detail.loc[:, "price_history_manifest_canonical_sha256"] = "0" * 64
    _rewrite_family(paths, "detail", detail)
    assert any(
        "price_history_manifest_canonical_sha256" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    _rewrite_family(paths, "detail", original)
    registry_path = tmp_path / validator.DATA_SHARING_REGISTRY_RELATIVE_PATH
    registry = pd.read_csv(registry_path, keep_default_na=False)
    original_registry = registry.copy()
    row = registry["data_family_id"].astype(str).eq(validator.ARTIFACT_ID)
    registry.loc[row, "data_contract_sha256"] = "f" * 64
    registry.to_csv(registry_path, index=False, encoding="utf-8")
    assert any(
        "data contract SHA-256 drift" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    original_registry.to_csv(registry_path, index=False, encoding="utf-8")
    background_path = tmp_path / validator.BACKGROUND_REGISTRY_RELATIVE_PATH
    background = pd.read_csv(background_path, keep_default_na=False)
    row = background["data_family_id"].astype(str).eq(validator.ARTIFACT_ID)
    background.loc[row, "allowed_use"] += " mutated"
    background.to_csv(background_path, index=False, encoding="utf-8")
    assert any(
        "background data contract SHA-256 drift" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )


def test_validator_rejects_position_shape_producer_lineage_mutation(
    tmp_path: Path,
) -> None:
    paths = _build_fixture(tmp_path)
    detail = pd.read_csv(paths["detail_latest"], dtype={"stock_id": str})
    detail.loc[:, "position_shape_producer_semantic_sha256"] = "0" * 64
    _rewrite_family(paths, "detail", detail)
    assert any(
        "position_shape_producer_semantic_sha256" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )

    paths = _build_fixture(tmp_path)
    position_shape_path = tmp_path / validator.POSITION_SHAPE_PRODUCER_RELATIVE_PATH
    position_shape_path.write_bytes(position_shape_path.read_bytes() + b"\n# mutation\n")
    assert any(
        "position_shape_producer_semantic_sha256" in error
        for error in validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    )


def test_validator_rejects_asof_payload_lineage_misalignment(tmp_path: Path) -> None:
    _build_fixture(tmp_path)
    source_path = tmp_path / validator.SOURCE_RELATIVE_PATHS["source_first"]
    source = pd.read_csv(source_path, dtype={"stock_id": str}, keep_default_na=False)
    row = source.index[source["stock_id"].eq("1111")][0]
    assert int(source.at[row, "qualifying_update_count"]) == 2
    source.at[row, "qualifying_source_row_canonical_sha256s"] = "4" * 64
    source.to_csv(source_path, index=False, encoding="utf-8-sig")

    errors = validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    assert any(
        "projected detail semantic SHA-256 binding mismatch" in error
        or "qualifying lineage is not aligned" in error
        for error in errors
    )


def test_validator_rejects_source_first_run_lineage_mutation(tmp_path: Path) -> None:
    _build_fixture(tmp_path)
    source_path = tmp_path / validator.SOURCE_RELATIVE_PATHS["source_first"]
    source = pd.read_csv(source_path, dtype={"stock_id": str}, keep_default_na=False)
    source["monthly_revenue_history_blob_sha256"] = "a" * 64
    source.to_csv(source_path, index=False, encoding="utf-8-sig")

    errors = validator.validate(artifact_root=tmp_path, source_root=tmp_path)
    assert any(
        "source_first_canonical_row_sha256" in error
        or "monthly_revenue_history_blob_sha256" in error
        for error in errors
    )


def test_trusted_git_commands_disable_replace_objects(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[list[str]] = []

    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(args)
        return _completed()

    monkeypatch.setattr(validator.subprocess, "run", fake_run)
    validator._git("cat-file", "-t", "a" * 40)

    assert calls == [
        [
            "git",
            "--no-replace-objects",
            "-C",
            str(validator.ROOT),
            "cat-file",
            "-t",
            "a" * 40,
        ]
    ]


def test_trusted_revision_rejects_wrong_sha_and_nonancestor(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with pytest.raises(RuntimeError, match="lowercase 40-character SHA"):
        validator._trusted_revision_preflight("A" * 40)

    revision = "a" * 40

    def fake_git(*args: str, **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if args[0] == "rev-parse":
            return _completed(stdout=f"{revision}\n".encode("ascii"))
        if args[:2] == ("cat-file", "-t"):
            return _completed(stdout=b"commit\n")
        if args[0] == "merge-base":
            return _completed(1, stderr=b"not ancestor")
        raise AssertionError(args)

    monkeypatch.setattr(validator, "_git", fake_git)
    with pytest.raises(RuntimeError, match="not an ancestor"):
        validator._trusted_revision_preflight(revision)


def test_trusted_path_blob_and_revision_keyed_cache_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with pytest.raises(RuntimeError, match="unsafe Git path"):
        validator._safe_repo_path("../data/stock_price_history/1111.csv")
    with pytest.raises(RuntimeError, match="unsafe stock id"):
        validator._trusted_stock_path("1111/../2222")

    revision = "b" * 40
    validator._TRUSTED_TREE_CACHE.clear()
    validator._TRUSTED_BLOB_CACHE.clear()
    monkeypatch.setattr(validator, "_trusted_tree", lambda _revision: {})
    with pytest.raises(RuntimeError, match="Git blob is missing"):
        validator._trusted_blobs({"safe.csv"}, revision=revision)

    path = "safe.csv"
    other_revision = "c" * 40
    validator._TRUSTED_BLOB_CACHE[(revision, path)] = b"first"
    validator._TRUSTED_BLOB_CACHE[(other_revision, path)] = b"second"
    assert validator._trusted_blobs({path}, revision=revision)[path] == b"first"
    assert (
        validator._trusted_blobs({path}, revision=other_revision)[path]
        == b"second"
    )
    validator._TRUSTED_BLOB_CACHE.clear()


def test_trusted_v1_manifest_descriptor_rejects_drift() -> None:
    manifest = _v1_manifest_frame()
    validator._validate_v1_manifest_descriptor(manifest)
    manifest.loc[0, "projection_policy_id"] = "v2_policy"
    with pytest.raises(RuntimeError, match="descriptor drift"):
        validator._validate_v1_manifest_descriptor(manifest)


def test_trusted_pipe_dates_reject_empty_token() -> None:
    frame = pd.DataFrame({"qualifying_source_dates": ["20260601||20260603"]})
    with pytest.raises(RuntimeError, match="invalid date"):
        validator._validate_trusted_date_values(
            frame,
            ("qualifying_source_dates",),
            label="source-first detail",
            pipe_delimited=True,
        )


def test_historical_v1_source_replay_uses_only_trusted_raw_blobs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = pd.DataFrame(
        {
            "stock_id": ["1111"],
            "episode_start_source_date": ["20260601"],
            "episode_start_canonical_source_table_date": ["20260601"],
            "episode_start_trade_date": ["20260602"],
            "latest_qualifying_source_date": ["20260603"],
            "latest_qualifying_canonical_source_table_date": ["20260603"],
            "latest_qualifying_trade_date": ["20260604"],
            "episode_end_date": ["20260713"],
            "qualifying_source_dates": ["20260601|20260603"],
            "qualifying_canonical_source_table_dates": ["20260601|20260603"],
            "qualifying_trade_dates": ["20260602|20260604"],
        }
    )
    rearmed = pd.DataFrame(
        {
            "stock_id": ["1111", "2222"],
            "lifecycle_policy_id": [validator.LIFECYCLE_POLICY_IDS[0], "other"],
            "confirmation_variant_id": [
                validator.CONFIRMATION_VARIANT_IDS[0],
                "other",
            ],
            "holding_days": [validator.HOLDING_DAYS, 10],
            "stop_policy_id": [validator.NO_STOP_POLICY_ID, "other"],
            "return_valid": [True, False],
            "trigger_date": ["20260701", "20260701"],
            "confirmation_date": ["20260702", "20260702"],
            "entry_date": ["20260703", ""],
            "planned_exit_date": ["20260713", ""],
            "exit_date": ["20260713", ""],
        }
    )
    relative_paths = {
        name: validator.SOURCE_RELATIVE_PATHS[name]
        for name in ("projection_manifest", "source_first", "rearmed")
    }
    payloads = {
        relative_paths["source_first"]: source.to_csv(
            index=False, lineterminator="\n"
        ).encode("utf-8"),
        relative_paths["rearmed"]: rearmed.to_csv(
            index=False, lineterminator="\n"
        ).encode("utf-8"),
        relative_paths["projection_manifest"]: _v1_manifest_frame()
        .to_csv(index=False, lineterminator="\n")
        .encode("utf-8"),
    }
    monkeypatch.setattr(validator, "_trusted_revision_preflight", lambda _revision: None)
    monkeypatch.setattr(
        validator,
        "_trusted_blobs",
        lambda paths, revision: {path: payloads[path] for path in paths},
    )

    _manifest, observed_source, observed_rearmed = validator._read_sources(
        validator.ROOT,
        historical_v1_source_audit=True,
    )

    assert observed_source["stock_id"].tolist() == ["1111"]
    assert observed_rearmed["stock_id"].tolist() == ["1111", "2222"]
    monkeypatch.setattr(
        sys,
        "argv",
        ["validator", "--historical-v1-source-audit"],
    )
    assert validator.parse_args().historical_v1_source_audit is True


def test_default_v1_source_replay_fails_before_any_trusted_git_call(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("ordinary canonical v1 validation must not read Git history")

    monkeypatch.setattr(validator, "_trusted_revision_preflight", fail)
    monkeypatch.setattr(validator, "_trusted_blobs", fail)

    with pytest.raises(
        RuntimeError,
        match="requires explicit --historical-v1-source-audit",
    ):
        validator._read_sources(
            validator.ROOT,
            projection_version=validator.V1_PROJECTION_VERSION,
        )


def test_default_v2_source_replay_never_calls_trusted_git_helpers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in ("projection_manifest", "source_first", "rearmed"):
        path = tmp_path / validator.SOURCE_RELATIVE_PATHS[name]
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame({"stock_id": ["1111"]}).to_csv(path, index=False)
        monkeypatch.setitem(validator.SOURCE_RELATIVE_PATHS, name, str(path))

    def fail(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("ordinary canonical v2 validation must not read Git history")

    monkeypatch.setattr(validator, "_trusted_revision_preflight", fail)
    monkeypatch.setattr(validator, "_trusted_blobs", fail)

    _manifest, observed_source, observed_rearmed = validator._read_sources(
        validator.ROOT,
        projection_version=validator.V2_PROJECTION_VERSION,
    )

    assert observed_source["stock_id"].tolist() == ["1111"]
    assert observed_rearmed["stock_id"].tolist() == ["1111"]


def test_historical_v1_source_audit_rejects_nondefault_or_v2_sources(
    tmp_path: Path,
) -> None:
    with pytest.raises(RuntimeError, match="default ROOT canonical v1"):
        validator._read_sources(
            tmp_path,
            projection_version=validator.V1_PROJECTION_VERSION,
            historical_v1_source_audit=True,
        )
    with pytest.raises(RuntimeError, match="default ROOT canonical v1"):
        validator._read_sources(
            validator.ROOT,
            projection_version=validator.V2_PROJECTION_VERSION,
            historical_v1_source_audit=True,
        )

    assert validator.validate(
        artifact_root=tmp_path,
        source_root=tmp_path,
        historical_v1_source_audit=True,
    ) == [
        "--historical-v1-source-audit requires the default ROOT artifact and "
        "source roots"
    ]


def test_trusted_price_replay_ignores_current_calendar_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    current_dir = tmp_path / "data" / "stock_price_history"
    current_dir.mkdir(parents=True)
    (current_dir / "1111.csv").write_text("date,close\n20990101,999\n", encoding="utf-8")
    trusted = pd.DataFrame(
        {
            "date": ["20260710", "20260713", "20260714"],
            "open": [10.0, 11.0, 999.0],
            "high": [10.5, 11.5, 999.0],
            "low": [9.5, 10.5, 999.0],
            "close": [10.0, 11.0, 999.0],
        }
    ).to_csv(index=False, lineterminator="\n").encode("utf-8")
    relative = validator._trusted_stock_path("1111")
    monkeypatch.setattr(
        validator,
        "_trusted_blobs",
        lambda paths, revision: {path: trusted for path in paths},
    )

    replay = validator._load_adjusted_price(
        "1111",
        current_dir,
        pd.DataFrame(
            columns=["stock_id", "resume_date", "exchange_ratio", "resolution_id"]
        ),
        trusted_revision="e" * 40,
    )

    assert relative == "data/stock_price_history/1111.csv"
    assert replay["date"].tolist() == ["20260710", "20260713"]
    assert replay["analysis_close"].tolist() == [10.0, 11.0]
