from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_operation_lag_bucket_audit import (  # noqa: E402
    V1_ARTIFACT_VERSION,
    V2_ARTIFACT_VERSION,
    artifact_version_for_projection,
    source_operation_version_for_projection,
    ADOPTED_GRID_ID,
    DETAIL_CSV,
    LATEST_CSV,
    PRIMARY_ANALYSIS_BASIS,
    SENSITIVITY_ANALYSIS_BASIS,
    SOURCE_OPERATION_DETAIL_CSV,
)
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)
from validate_revenue_unreacted_range_operation_lag_bucket_audit import (  # noqa: E402
    validate,
)
import validate_revenue_unreacted_range_operation_lag_bucket_audit as validator  # noqa: E402


def test_operation_lag_versions_are_projection_bound() -> None:
    assert artifact_version_for_projection(V1_PROJECTION_VERSION) == V1_ARTIFACT_VERSION
    assert artifact_version_for_projection(V2_PROJECTION_VERSION) == V2_ARTIFACT_VERSION
    assert source_operation_version_for_projection(V1_PROJECTION_VERSION) == (
        validator.SOURCE_OPERATION_ARTIFACT_VERSION
    )
    assert source_operation_version_for_projection(V2_PROJECTION_VERSION) == (
        validator.V2_SOURCE_OPERATION_ARTIFACT_VERSION
    )
    assert validator._expected_versions(V2_PROJECTION_VERSION) == (
        V2_ARTIFACT_VERSION,
        validator.V2_SOURCE_OPERATION_ARTIFACT_VERSION,
    )
    with pytest.raises(RuntimeError, match="unsupported canonical source projection"):
        validator._expected_versions("unknown")


def test_operation_lag_trusted_v1_replay_requires_explicit_opt_in(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = pd.DataFrame({"projection_version": [V1_PROJECTION_VERSION]})
    replay = (
        manifest,
        pd.DataFrame({"stock_id": ["1111"]}),
        pd.DataFrame({"stock_id": ["1111"]}),
    )
    trusted_calls = 0

    def trusted_source_frames():
        nonlocal trusted_calls
        trusted_calls += 1
        return replay

    monkeypatch.setattr(
        validator,
        "load_source_snapshot_projection_manifest",
        lambda _path: manifest,
    )
    monkeypatch.setattr(validator, "_trusted_source_frames", trusted_source_frames)

    with pytest.raises(RuntimeError, match="requires explicit --historical-v1-source-audit"):
        validator._canonical_source_frames()
    assert trusted_calls == 0
    assert validator._canonical_source_frames(
        historical_v1_source_audit=True
    ) is replay
    assert trusted_calls == 1
    monkeypatch.setattr(
        sys,
        "argv",
        ["validator", "--historical-v1-source-audit"],
    )
    assert validator.parse_args().historical_v1_source_audit is True


def test_operation_lag_canonical_v2_uses_current_sources_without_trusted_replay(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = pd.DataFrame(
        {
            "projection_version": [V2_PROJECTION_VERSION],
            "cutoff_price_input_stock_count": [1],
            "cutoff_price_input_row_count": [0],
            "cutoff_price_input_file_semantic_sha256s": [f"1111:0:{'a' * 64}"],
        }
    )
    episodes = pd.DataFrame({"stock_id": ["1111"]})
    operation_path = tmp_path / "operation_detail.csv"
    pd.DataFrame({"stock_id": ["1111"]}).to_csv(operation_path, index=False)

    monkeypatch.setattr(
        validator,
        "load_source_snapshot_projection_manifest",
        lambda _path: manifest,
    )
    monkeypatch.setattr(
        validator, "load_projected_source_detail", lambda _path: episodes
    )
    monkeypatch.setattr(
        validator, "validate_projection_binding_frames", lambda *_args: []
    )
    monkeypatch.setattr(validator, "SOURCE_OPERATION_DETAIL_CSV", operation_path)
    monkeypatch.setattr(
        validator,
        "_trusted_source_frames",
        lambda: pytest.fail("canonical v2 must not replay trusted v1 sources"),
    )
    monkeypatch.setattr(
        validator,
        "_trusted_price_frames",
        lambda *_args: pytest.fail("canonical v2 must not replay trusted v1 prices"),
    )

    observed_manifest, operations, observed_episodes = (
        validator._canonical_source_frames()
    )
    assert observed_manifest is manifest
    assert operations["stock_id"].tolist() == ["1111"]
    assert observed_episodes is episodes
    assert validator._current_price_frames(set(), manifest) == {}
    with pytest.raises(RuntimeError, match="requires the default ROOT canonical v1"):
        validator._canonical_source_frames(historical_v1_source_audit=True)


def test_operation_lag_bucket_audit_passes() -> None:
    assert validate() == []


def test_operation_lag_trusted_v1_source_and_price_descriptor_probe() -> None:
    manifest, operations, episodes = validator._trusted_source_frames()
    prices = validator._trusted_price_frames({"2380"}, manifest)

    assert len(manifest) == 1
    assert not operations.empty
    assert not episodes.empty
    assert prices["2380"]["date"].max() == validator.PRICE_HISTORY_CUTOFF_DATE


def test_operation_lag_trusted_v1_contract_fails_closed(monkeypatch) -> None:
    with pytest.raises(RuntimeError, match="unsafe Git path"):
        validator._safe_repo_path("../data/stock_price_history/2380.csv")
    with pytest.raises(RuntimeError, match="unsafe stock id"):
        validator._trusted_stock_path("2380/evil")

    manifest, _, _ = validator._trusted_source_frames()
    mutated = manifest.copy()
    mutated.loc[0, "cutoff_date"] = "20260714"
    with pytest.raises(RuntimeError, match="descriptor drift"):
        validator._validate_v1_manifest_descriptor(mutated)

    monkeypatch.setattr(validator, "TRUSTED_SOURCE_REVISION", "f" * 40)
    with pytest.raises(RuntimeError, match="commit is unavailable"):
        validator._trusted_revision_preflight()


def test_operation_lag_git_calls_disable_replace_objects(monkeypatch) -> None:
    real_run = subprocess.run
    calls: list[list[str]] = []

    def recording_run(args, *positional, **kwargs):
        calls.append(list(args))
        return real_run(args, *positional, **kwargs)

    monkeypatch.setattr(validator.subprocess, "run", recording_run)
    validator._trusted_revision_preflight()

    assert calls
    assert all(call[1] == "--no-replace-objects" for call in calls)


def test_operation_lag_bucket_uses_asof_latest_revenue_without_future_backfill() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={
            "stock_id": str,
            "trigger_date": str,
            "asof_latest_qualifying_trade_date": str,
            "final_episode_latest_qualifying_trade_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    assert detail["final_episode_latest_after_trigger_flag"].astype(str).eq("True").any()
    assert detail["asof_latest_qualifying_trade_date"].le(detail["trigger_date"]).all()
    future = detail.loc[
        pd.to_numeric(detail["future_qualifying_update_ignored_count"], errors="coerce").gt(0)
    ]
    assert not future.empty
    assert future["asof_latest_qualifying_trade_date"].lt(
        future["final_episode_latest_qualifying_trade_date"]
    ).all()
    assert detail["latest_source_lag_bucket"].astype(str).ne("").all()
    assert detail["first_source_lag_bucket"].astype(str).ne("").all()


def test_operation_lag_bucket_exactly_covers_the_adopted_mature_grid() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    source = pd.read_csv(
        SOURCE_OPERATION_DETAIL_CSV,
        dtype={"stock_id": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    source = source.loc[
        source["grid_id"].eq(ADOPTED_GRID_ID)
        & source["return_valid"].astype(str).eq("True")
    ]
    detail_keys = set(zip(detail["episode_key"], detail["stock_id"], detail["entry_date"]))
    source_keys = set(zip(source["episode_key"], source["stock_id"], source["entry_date"]))
    assert detail_keys == source_keys
    for _stock_id, stock in detail.groupby("stock_id", sort=False):
        ordered = stock.sort_values("entry_date", kind="mergesort")
        entries = ordered["entry_date"].iloc[1:].reset_index(drop=True)
        prior_exits = ordered["exit_date"].iloc[:-1].reset_index(drop=True)
        assert not entries.le(prior_exits).any()


def test_operation_lag_bucket_partitions_conserve_primary_and_sensitivity_rows() -> None:
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    for analysis_basis in (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS):
        for lag_basis in (
            "latest_qualifying_source_asof_trigger",
            "episode_first_qualifying_source",
            "latest_qualifying_source_watch_horizon_comparison",
        ):
            rows = summary.loc[
                summary["analysis_basis"].eq(analysis_basis)
                & summary["lag_basis_id"].eq(lag_basis)
            ]
            overall = int(rows.loc[rows["lag_bucket_id"].eq("all"), "operation_count"].iloc[0])
            bucket_total = int(
                pd.to_numeric(
                    rows.loc[~rows["lag_bucket_id"].eq("all"), "operation_count"],
                    errors="raise",
                ).sum()
            )
            assert bucket_total == overall
