from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TESTS = ROOT / "tests"
for path in (SCRIPTS, TESTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import revenue_unreacted_range_forward_holdout as v1  # noqa: E402
import revenue_unreacted_range_forward_holdout_v2 as v2  # noqa: E402
import validate_revenue_unreacted_range_forward_holdout_v2 as v2_validator  # noqa: E402
from test_revenue_unreacted_range_forward_holdout import (  # noqa: E402
    _price_frame,
    _source_manifest,
    _source_row,
)


GENERATED_AT = "2026-08-28 12:00:00 Asia/Taipei"


def _v2_manifest() -> pd.DataFrame:
    manifest = _source_manifest()
    manifest.loc[0, "artifact_version"] = v2.SOURCE_PROJECTION_ARTIFACT_VERSION
    manifest.loc[0, "projection_version"] = v2.SOURCE_PROJECTION_ARTIFACT_VERSION
    manifest.loc[0, "projected_episode_row_count"] = v2.PROJECTED_EPISODE_ROW_COUNT
    manifest.loc[0, "projected_episode_semantic_sha256"] = (
        v2.PROJECTED_EPISODE_SEMANTIC_SHA256
    )
    manifest.loc[0, "candidate_status"] = "generated_pending_supersede_approval"
    return manifest


def _pre_start_inputs() -> tuple[pd.DataFrame, dict[str, pd.DataFrame], pd.DataFrame]:
    source = pd.DataFrame([_source_row(stock_id="1111", position="mid")])
    price = _price_frame(
        trigger_dates=(),
        position="mid",
        end_date="20260828",
    )
    price["volume"] = 1_000_000.0
    price["analysis_price_adjustment_factor"] = 1.0
    daily = {
        "1111": price
    }
    return source, daily, _v2_manifest()


def _bind_fixture_manifest(monkeypatch: pytest.MonkeyPatch, manifest: pd.DataFrame) -> None:
    canonical_sha = v1._canonical_frame_sha256(manifest)
    monkeypatch.setattr(v2, "SELECTED_V2_MANIFEST_CANONICAL_SHA256", canonical_sha)
    monkeypatch.setattr(
        v2_validator,
        "SELECTED_V2_MANIFEST_CANONICAL_SHA256",
        canonical_sha,
    )


def test_pre_start_capture_is_empty_research_only_and_independently_validated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)

    v1_defaults = (
        v1.ARTIFACT_ID,
        v1.ARTIFACT_VERSION,
        v1.HOLDOUT_START_DATE,
        v1.DATA_CONTRACT_SHA256,
        v1.ALLOW_PRE_START_EMPTY_CAPTURE,
    )
    frames = v2.build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    manifest, detail, summary, comparison, anomaly = frames

    assert detail.empty
    assert manifest.iloc[0]["artifact_id"] == v2.ARTIFACT_ID
    assert manifest.iloc[0]["artifact_version"] == v2.ARTIFACT_VERSION
    assert manifest.iloc[0]["holdout_start_date"] == "20260831"
    assert manifest.iloc[0]["observed_through_date"] == "20260828"
    assert manifest.iloc[0]["holdout_status"] == "preregistered_waiting_for_start"
    assert manifest.iloc[0]["price_semantic_projection_version"] == (
        v2.PRICE_SEMANTIC_PROJECTION_VERSION
    )
    assert manifest.iloc[0]["price_semantic_projection_schema_sha256"] == (
        v2.PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
    )
    assert manifest.iloc[0]["price_semantic_projection_columns"] == "|".join(
        v2.PRICE_SEMANTIC_PROJECTION_COLUMNS
    )
    assert int(manifest.iloc[0]["price_semantic_projection_decimal_scale"]) == 8
    assert manifest.iloc[0]["price_semantic_projection_role"] == (
        "composite_promotion_input_lineage_component"
    )
    assert manifest.iloc[0]["price_input_legacy_lineage_role"] == (
        "provenance_diagnostic_only_not_promotion_gate"
    )
    assert set(summary["holdout_status"]) == {"preregistered_waiting_for_start"}
    assert set(comparison["comparison_conclusion"]) == {
        "no_promotion_conclusion_preregistered_waiting_for_start"
    }
    assert set(anomaly["research_only"].astype(str).str.lower()) == {"true"}
    for frame in frames:
        for column in v1.FALSE_FLAG_COLUMNS:
            assert set(frame[column].astype(str).str.lower()) <= {"false"}

    errors = v2_validator.validate_frames(
        *frames,
        source_detail=source,
        daily_by_stock=daily,
        source_manifest=source_manifest,
    )
    assert errors == []
    assert (
        v1.ARTIFACT_ID,
        v1.ARTIFACT_VERSION,
        v1.HOLDOUT_START_DATE,
        v1.DATA_CONTRACT_SHA256,
        v1.ALLOW_PRE_START_EMPTY_CAPTURE,
    ) == v1_defaults


def _v2_price_lineages(
    daily: dict[str, pd.DataFrame],
) -> tuple[tuple[str, str, int, int], tuple[str, str, int, int]]:
    cutoff = max(str(frame["date"].max()) for frame in daily.values())
    with v2.engine_v2_context():
        producer = v1._price_semantic_lineage(daily, cutoff_date=cutoff)
    with v2_validator.validator_v2_context():
        independent = v2_validator.validator._price_semantic_lineage(
            daily,
            cutoff_date=cutoff,
        )
    return producer, independent


def test_price_semantic_projection_is_fixed_scale_ordered_and_independent() -> None:
    _, daily, _ = _pre_start_inputs()
    baseline_producer, baseline_independent = _v2_price_lineages(daily)
    assert baseline_producer == baseline_independent

    noisy = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    noisy_frame = noisy["1111"]
    noisy_frame["ma60"] = noisy_frame["ma60"] + 1e-11
    noisy_frame["operation_ma20"] = 999999.123456789
    noisy_frame = noisy_frame.loc[
        :, list(reversed(noisy_frame.columns))
    ].iloc[::-1].reset_index(drop=True)
    noisy["1111"] = noisy_frame

    noisy_producer, noisy_independent = _v2_price_lineages(noisy)
    assert noisy_producer == baseline_producer
    assert noisy_independent == baseline_independent
    with v2.engine_v2_context():
        baseline_legacy = v1._price_lineage(v1._normalize_prices(daily))[0]
        noisy_legacy = v1._price_lineage(v1._normalize_prices(noisy))[0]
    assert noisy_legacy != baseline_legacy


def test_raw_price_projection_changes_for_canonical_source_drift() -> None:
    _, daily, _ = _pre_start_inputs()
    baseline, _ = _v2_price_lineages(daily)
    changed = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    changed["1111"].loc[0, "open"] += 0.0001
    changed["1111"].loc[0, "analysis_open"] += 0.0001
    observed, independent = _v2_price_lineages(changed)
    assert observed == independent
    assert observed[0] != baseline[0]
    assert observed[1] != baseline[1]


def test_raw_price_projection_leaves_derived_float_collision_to_exact_output_replay() -> None:
    frame = pd.DataFrame(
        {
            "date": ["20260827", "20260828"],
            "analysis_open": [10.0, 11.0],
            "analysis_high": [10.5, 11.5],
            "analysis_low": [9.5, 10.5],
            "analysis_close": [10.0, 11.0],
            "open": [10.0, 11.0],
            "high": [10.5, 11.5],
            "low": [9.5, 10.5],
            "close": [10.0, 11.0],
            "ma60": [10.000000004, 10.0],
            "ma120": [10.0, 10.0],
            "analysis_ema23": [10.0, 10.1],
            "cross_breakout_prev20": [True, False],
            "volume": [1_000_000.0, 1_000_000.0],
            "analysis_price_adjustment_factor": [1.0, 1.0],
            "price_resolution_ids_on_date": ["", ""],
        }
    )
    below = frame.copy()
    below.loc[0, "ma60"] = 9.999999996

    with v2.engine_v2_context():
        assert v1._base_trigger_hit(frame, 0) is True
        assert v1._base_trigger_hit(below, 0) is False
        producer_above = v1._price_semantic_lineage(
            {"1111": frame}, cutoff_date="20260828"
        )
        producer_below = v1._price_semantic_lineage(
            {"1111": below}, cutoff_date="20260828"
        )

    with v2_validator.validator_v2_context():
        independent_above = v2_validator.validator._price_semantic_lineage(
            {"1111": frame}, cutoff_date="20260828"
        )
        independent_below = v2_validator.validator._price_semantic_lineage(
            {"1111": below}, cutoff_date="20260828"
        )

    assert producer_above == independent_above
    assert producer_below == independent_below
    assert producer_above == producer_below
    assert v1._canonical_mapping_sha256(
        {"base_trigger_hit": v1._base_trigger_hit(frame, 0)}
    ) != v1._canonical_mapping_sha256(
        {"base_trigger_hit": v1._base_trigger_hit(below, 0)}
    )


def test_exact_five_frame_replay_rejects_derived_predicate_drift_with_same_raw_lineage(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = pd.DataFrame([_source_row(stock_id="1111", position="mid")])
    source_manifest = _v2_manifest()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    price = _price_frame(
        trigger_dates=("20260901",),
        position="mid",
        end_date="20261030",
    )
    price["volume"] = 1_000_000.0
    price["analysis_price_adjustment_factor"] = 1.0
    trigger_index = int(price.index[price["date"].eq("20260901")][0])
    price.loc[trigger_index, "ma60"] = 10.000000004
    price.loc[trigger_index, "ma120"] = 10.0
    above = {"1111": price}
    below = {"1111": price.copy()}
    below["1111"].loc[trigger_index, "ma60"] = 9.999999996

    above_lineage, _ = _v2_price_lineages(above)
    below_lineage, _ = _v2_price_lineages(below)
    assert above_lineage == below_lineage

    frames = v2.build_forward_holdout(
        source,
        above,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    assert not frames[1].empty
    errors = v2_validator.validate_frames(
        *frames,
        source_detail=source,
        daily_by_stock=below,
        source_manifest=source_manifest,
    )
    assert errors
    assert any(
        "replay drift" in error or "event completeness" in error
        for error in errors
    )


def test_v2_validator_treats_legacy_hashes_as_diagnostics_only(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    frames = list(
        v2.build_forward_holdout(
            source,
            daily,
            source_manifest=source_manifest,
            generated_at=GENERATED_AT,
        )
    )
    frames[0] = frames[0].copy()
    frames[0].loc[0, "price_input_canonical_sha256"] = "0" * 64
    frames[0].loc[0, "price_input_stock_canonical_sha256s"] = "1111:" + "1" * 64
    assert v2_validator.validate_frames(
        *frames,
        source_detail=source,
        daily_by_stock=daily,
        source_manifest=source_manifest,
    ) == []

    frames[0].loc[0, "price_semantic_projection_canonical_sha256"] = "2" * 64
    errors = v2_validator.validate_frames(
        *frames,
        source_detail=source,
        daily_by_stock=daily,
        source_manifest=source_manifest,
    )
    assert any("price_semantic_projection_canonical_sha256" in error for error in errors)


def test_v2_append_only_manifest_allows_only_exact_predecessor_schema_extension(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    manifest, *_ = v2.build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    predecessor = manifest.drop(columns=list(v2.PRICE_SEMANTIC_MANIFEST_COLUMNS))
    predecessor = predecessor.copy()
    predecessor.loc[0, "capture_id"] = "f" * 64
    with v2.engine_v2_context():
        v1.validate_append_only_history(
            predecessor,
            manifest,
            immutable_base=predecessor.copy(),
            allowed_schema_extension_columns=v2.PRICE_SEMANTIC_MANIFEST_COLUMNS,
        )
        malformed = predecessor.drop(columns=["financial_statement_scope"])
        with pytest.raises(RuntimeError, match="schema drift"):
            v1.validate_append_only_history(
                malformed,
                manifest,
                immutable_base=malformed.copy(),
                allowed_schema_extension_columns=v2.PRICE_SEMANTIC_MANIFEST_COLUMNS,
            )


def test_independent_history_validator_keeps_predecessor_diagnostics_immutable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    frames = v2.build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    current = dict(zip(names, frames, strict=True))
    immutable: dict[str, pd.DataFrame] = {}
    histories: dict[str, pd.DataFrame] = {}
    with v2_validator.validator_v2_context():
        for name, frame in current.items():
            predecessor = frame.copy()
            if not predecessor.empty:
                predecessor["capture_id"] = "f" * 64
            extension = (
                v2_validator.validator.APPEND_ONLY_SCHEMA_EXTENSION_COLUMNS_BY_ARTIFACT.get(
                    name, ()
                )
            )
            if extension:
                predecessor = predecessor.drop(columns=list(extension))
            immutable[name] = predecessor.copy()
            aligned = v2_validator.validator._align_exact_history_schema_extension(
                predecessor,
                list(frame.columns),
                allowed_extension_columns=extension,
            )
            assert aligned is not None
            histories[name] = (
                pd.concat([aligned, frame], ignore_index=True)
                if not frame.empty
                else aligned
            )
        assert v2_validator.validator.validate_history_surfaces(
            current,
            histories,
            immutable_base_frames=immutable,
        ) == []

        mutated = {name: frame.copy() for name, frame in immutable.items()}
        mutated["manifest"].loc[0, "price_input_canonical_sha256"] = "e" * 64
        errors = v2_validator.validator.validate_history_surfaces(
            current,
            histories,
            immutable_base_frames=mutated,
        )
    assert "manifest history immutable base prefix drift at row 2" in errors


def test_v1_family_does_not_emit_v2_price_projection_fields() -> None:
    source = pd.DataFrame([_source_row(stock_id="1111", position="mid")])
    daily = {
        "1111": _price_frame(
            trigger_dates=("20260810",),
            position="mid",
            end_date="20261030",
        )
    }
    manifest, detail, *_ = v1.build_forward_holdout(
        source,
        daily,
        source_manifest=_source_manifest(),
        generated_at=GENERATED_AT,
    )
    assert not any(
        column.startswith("price_semantic_projection_")
        for column in manifest.columns
    )
    assert not any(
        column.startswith("price_semantic_projection_")
        for column in detail.columns
    )
    assert not detail.empty
    for _, row in detail.iterrows():
        mapping = row.drop(labels=["event_row_canonical_sha256"]).to_dict()
        assert row["event_row_canonical_sha256"] == v1._canonical_mapping_sha256(
            mapping
        )


def test_v2_writer_uses_separate_exact17_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    frames = v2.build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )

    paths = v2.write_forward_holdout(
        *frames,
        replay_source_detail=source,
        output_root=tmp_path,
    )

    assert len(paths) == 17
    assert {path.relative_to(tmp_path).as_posix() for path in paths.values()} == set(
        v2.FORWARD_HOLDOUT_V2_ALLOWED_ARTIFACT_PATHS
    )
    assert all("forward_holdout_v2" in path.name for path in paths.values())
    assert not list(tmp_path.rglob("revenue_unreacted_range_forward_holdout_manifest*"))


def test_selected_v2_manifest_binding_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    source_manifest.loc[0, "projected_episode_semantic_sha256"] = "0" * 64

    with pytest.raises(RuntimeError, match="selected manifest drift"):
        v2.build_forward_holdout(
            source,
            daily,
            source_manifest=source_manifest,
            generated_at=GENERATED_AT,
        )


def test_v1_exact17_metadata_reproduces_authorized_bundle_digest() -> None:
    lines = [
        f"{path}|{size}|{digest}\n"
        for path, (size, digest) in sorted(v2.V1_EXACT17_PATH_EVIDENCE.items())
    ]
    assert len(lines) == 17
    assert hashlib.sha256("".join(lines).encode("utf-8")).hexdigest() == (
        v2.V1_EXACT17_BUNDLE_SHA256
    )


def test_v1_exact17_freeze_reports_the_drifting_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    relative = "output/latest/research_backtest/frozen.csv"
    payload = b"frozen\n"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    bundle = hashlib.sha256(
        f"{relative}|{len(payload)}|{digest}\n".encode("utf-8")
    ).hexdigest()
    monkeypatch.setattr(v2, "V1_EXACT17_PATH_EVIDENCE", {relative: (len(payload), digest)})
    monkeypatch.setattr(v2, "V1_EXACT17_BUNDLE_SHA256", bundle)
    assert v2.validate_v1_exact17_freeze(root=tmp_path) == bundle

    path.write_bytes(b"drift\n")
    with pytest.raises(RuntimeError, match="frozen.csv"):
        v2.validate_v1_exact17_freeze(root=tmp_path)


def test_v1_exact17_freeze_uses_git_blob_identity_for_clean_crlf_checkout(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.invalid"],
        cwd=repo,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Forward Holdout Test"],
        cwd=repo,
        check=True,
    )
    (repo / ".gitattributes").write_text("*.csv text eol=crlf\n", encoding="utf-8")
    relative = "output/latest/research_backtest/frozen.csv"
    path = repo / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(b"header\nvalue\n")
    subprocess.run(
        ["git", "add", ".gitattributes", relative],
        cwd=repo,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "freeze fixture"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    path.unlink()
    subprocess.run(["git", "checkout", "--", relative], cwd=repo, check=True)

    blob = subprocess.run(
        ["git", "cat-file", "blob", f"HEAD:{relative}"],
        cwd=repo,
        check=True,
        capture_output=True,
    ).stdout
    assert b"\r\n" in path.read_bytes()
    assert b"\r\n" not in blob
    digest = hashlib.sha256(blob).hexdigest()
    bundle = hashlib.sha256(
        f"{relative}|{len(blob)}|{digest}\n".encode("utf-8")
    ).hexdigest()
    monkeypatch.setattr(v2, "V1_EXACT17_PATH_EVIDENCE", {relative: (len(blob), digest)})
    monkeypatch.setattr(v2, "V1_EXACT17_BUNDLE_SHA256", bundle)

    assert v2.validate_v1_exact17_freeze(root=repo) == bundle
    path.write_text("header\nchanged\n", encoding="utf-8")
    with pytest.raises(RuntimeError, match="working-tree drift"):
        v2.validate_v1_exact17_freeze(root=repo)
