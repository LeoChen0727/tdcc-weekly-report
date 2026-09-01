from __future__ import annotations

import ast
import hashlib
import shutil
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_hot_theme_pullback_research as producer  # noqa: E402
import validate_hot_theme_pullback_research as validator  # noqa: E402


def _write_price(path: Path, closes: list[float]) -> None:
    dates = pd.bdate_range("2026-01-05", periods=len(closes))
    frame = pd.DataFrame(
        {
            "date": [value.strftime("%Y%m%d") for value in dates],
            "open": [100.0] * len(closes),
            "high": [max(101.0, value) for value in closes],
            "low": [min(99.0, value) for value in closes],
            "close": closes,
        }
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding="utf-8")


def _fixture(tmp_path: Path) -> tuple[Path, Path, Path, Path]:
    root = tmp_path / "repo"
    snapshot_root = (
        root / "output" / "history" / "daily_model_snapshots"
    )
    price_root = root / "data" / "stock_price_history"
    snapshot_root.mkdir(parents=True)
    producer_copy = root / producer.PRODUCER
    producer_copy.parent.mkdir(parents=True)
    shutil.copyfile(Path(producer.__file__), producer_copy)
    snapshot_path = snapshot_root / "signals_20260102.csv"
    signals = pd.DataFrame(
        [
            {
                "signal_date": "20260102",
                "stock_id": "1111",
                "stock_name": "上漲股",
                "model_id": producer.MODEL_ID,
                "model_score": "80",
                "model_rank": "1",
                "report_bucket": "mainstream",
            },
            {
                "signal_date": "20260102",
                "stock_id": "1111",
                "stock_name": "上漲股",
                "model_id": producer.MODEL_ID,
                "model_score": "80",
                "model_rank": "1",
                "report_bucket": "non_mainstream",
            },
            {
                "signal_date": "20260102",
                "stock_id": "2222",
                "stock_name": "下跌股",
                "model_id": producer.MODEL_ID,
                "model_score": "70",
                "model_rank": "2",
                "report_bucket": "mainstream",
            },
            {
                "signal_date": "20260102",
                "stock_id": "3333",
                "stock_name": "持平股",
                "model_id": producer.MODEL_ID,
                "model_score": "60",
                "model_rank": "3",
                "report_bucket": "mainstream",
            },
            {
                "signal_date": "20260102",
                "stock_id": "9999",
                "stock_name": "其他模型",
                "model_id": "another_model",
                "model_score": "99",
                "model_rank": "1",
                "report_bucket": "mainstream",
            },
        ]
    )
    signals.to_csv(snapshot_path, index=False, encoding="utf-8")
    raw_sha = hashlib.sha256(snapshot_path.read_bytes()).hexdigest()
    manifest_path = snapshot_root / "daily_published_model_snapshot_manifest.csv"
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260102",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "test",
                "generated_at": "2026-01-02",
                "pipeline_commit_sha": "a" * 40,
                "artifact_id": "model_signals_for_report",
                "snapshot_path": snapshot_path.as_posix(),
                "snapshot_sha256": raw_sha,
                "row_count": len(signals),
                "column_count": len(signals.columns),
                "purpose": "as_published_daily_model_snapshot",
            }
        ]
    ).to_csv(manifest_path, index=False, encoding="utf-8")

    rising = [100.0 + index * 2.0 for index in range(22)]
    falling = [100.0 - index * 2.0 for index in range(22)]
    flat = [100.0] * 22
    _write_price(price_root / "1111.csv", rising)
    _write_price(price_root / "2222.csv", falling)
    _write_price(price_root / "3333.csv", flat)
    return root, manifest_path, snapshot_root, price_root


def _write_bound_artifacts(
    root: Path,
    events: pd.DataFrame,
    summary: pd.DataFrame,
    anomalies: pd.DataFrame,
    manifest: pd.DataFrame,
) -> tuple[Path, Path, Path, Path]:
    artifact_root = root / "output" / "latest" / "research_backtest"
    artifact_root.mkdir(parents=True, exist_ok=True)
    paths = {
        "events": artifact_root
        / "hot_theme_pullback_published_signal_events_latest.csv",
        "summary": artifact_root
        / "hot_theme_pullback_published_signal_summary_latest.csv",
        "anomalies": artifact_root
        / "hot_theme_pullback_published_signal_anomaly_candidates_latest.csv",
    }
    frames = {"events": events, "summary": summary, "anomalies": anomalies}
    bound_manifest = manifest.copy()
    payload_hashes: list[str] = []
    for key, frame in frames.items():
        frame.to_csv(paths[key], index=False, encoding="utf-8-sig")
        payload_sha = producer.canonical_file_sha256(paths[key])
        payload_hashes.append(payload_sha)
        bound_manifest[f"{key}_path"] = paths[key].relative_to(root).as_posix()
        bound_manifest[f"{key}_file_sha256"] = payload_sha
        bound_manifest[f"{key}_row_count"] = len(frame)
    bound_manifest["evidence_payload_bundle_sha256"] = producer.row_set_sha256(
        payload_hashes
    )
    manifest_path = (
        artifact_root / "hot_theme_pullback_published_signal_manifest_latest.csv"
    )
    bound_manifest.to_csv(manifest_path, index=False, encoding="utf-8-sig")
    return (
        paths["events"],
        paths["summary"],
        paths["anomalies"],
        manifest_path,
    )


def test_published_signal_replay_is_row_level_and_fail_closed(tmp_path: Path) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )

    assert events["signal_event_key"].nunique() == 3
    assert len(events) == 9
    assert set(events["scenario_id"]) == set(producer.SCENARIOS)
    duplicated_surface = events[
        events["signal_event_key"].astype(str).str.contains(r"\|1111$")
    ]
    assert set(duplicated_surface["source_signal_row_count"]) == {2}
    assert not events["formal_use_allowed"].astype(bool).any()
    assert not summary["formal_use_allowed"].astype(bool).any()
    assert not manifest["promotion_evidence_allowed"].astype(bool).any()
    assert not anomalies.empty
    assert anomalies["primary_metric_included"].astype(bool).all()
    assert anomalies["anomaly_disposition"].eq(
        "unresolved_anomaly_candidate"
    ).all()
    assert validator.validate_frames(
        events,
        summary,
        anomalies,
        manifest,
        root=root,
    ) == []


def test_cli_without_ownership_registration_creates_no_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    registry_path = tmp_path / "model_research_artifact_ownership.csv"
    pd.DataFrame(
        [
            {
                "owner_model_id": "unrelated_model",
                "producer": "scripts/build_unrelated_research.py",
                "artifact_glob": "output/latest/research_backtest/unrelated_model_*",
                "artifact_class": "model_research_output",
                "change_policy": "model_owned_write",
                "formal_evidence_status": "research_only",
                "notes": "fixture",
            }
        ]
    ).to_csv(registry_path, index=False, encoding="utf-8")
    output_root = tmp_path / "should_not_exist"
    monkeypatch.setattr(producer, "OWNERSHIP_REGISTRY_PATH", registry_path)
    monkeypatch.setattr(producer, "LATEST_ROOT", output_root / "latest")
    monkeypatch.setattr(producer, "HISTORY_ROOT", output_root / "history")
    monkeypatch.setattr(producer, "DOCS_ROOT", output_root / "docs")

    with pytest.raises(RuntimeError, match="ownership preflight failed"):
        producer.main()
    assert not output_root.exists()


def test_independent_validator_rejects_return_tamper(tmp_path: Path) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    tampered = events.copy()
    mature_index = tampered[tampered["return_valid"].astype(bool)].index[0]
    tampered.at[mature_index, "gross_return_pct"] = 999.0
    errors = validator.validate_frames(
        tampered,
        summary,
        anomalies,
        manifest,
        root=root,
    )
    assert any(
        "return formula mismatch" in error or "canonical row hash mismatch" in error
        for error in errors
    )


def test_snapshot_manifest_hash_is_fail_closed(tmp_path: Path) -> None:
    _, manifest_path, snapshot_root, _ = _fixture(tmp_path)
    signal_path = snapshot_root / "signals_20260102.csv"
    signal_path.write_text(
        signal_path.read_text(encoding="utf-8") + "\n",
        encoding="utf-8",
    )
    with pytest.raises(RuntimeError, match="snapshot SHA mismatch"):
        producer.load_latest_signal_manifest(manifest_path, snapshot_root)


def test_validator_rejects_same_named_manifest_outside_registered_root(
    tmp_path: Path,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    outside_manifest = (
        tmp_path / "outside" / "daily_published_model_snapshot_manifest.csv"
    )
    outside_manifest.parent.mkdir()
    shutil.copyfile(manifest_path, outside_manifest)
    tampered_manifest = manifest.copy()
    tampered_manifest.at[0, "source_manifest_path"] = outside_manifest.as_posix()
    tampered_manifest.at[0, "source_manifest_sha256"] = (
        producer.canonical_file_sha256(outside_manifest)
    )

    errors = validator.validate_frames(
        events,
        summary,
        anomalies,
        tampered_manifest,
        root=root,
    )
    assert any("outside registered snapshot root" in error for error in errors)


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    [
        ("duplicate_same", "duplicate date"),
        ("duplicate_conflict", "duplicate date"),
        ("invalid_date", "invalid date"),
        ("nonnumeric_close", "invalid required price"),
        ("missing_close_column", "missing required columns"),
    ],
)
def test_price_loaders_fail_closed_on_invalid_rows(
    tmp_path: Path,
    mutation: str,
    expected_error: str,
) -> None:
    _, _, _, price_root = _fixture(tmp_path)
    price_path = price_root / "1111.csv"
    frame = pd.read_csv(price_path, dtype=str, keep_default_na=False)
    if mutation in {"duplicate_same", "duplicate_conflict"}:
        duplicate = frame.iloc[[0]].copy()
        if mutation == "duplicate_conflict":
            duplicate.loc[:, "close"] = "777"
        frame = pd.concat([frame, duplicate], ignore_index=True)
    elif mutation == "invalid_date":
        frame.at[0, "date"] = "20261340"
    elif mutation == "nonnumeric_close":
        frame.at[0, "close"] = "not-a-price"
    elif mutation == "missing_close_column":
        frame = frame.drop(columns=["close"])
    frame.to_csv(price_path, index=False, encoding="utf-8")

    with pytest.raises(RuntimeError, match=expected_error):
        producer._price_frame("1111", price_root)
    with pytest.raises(RuntimeError, match=expected_error):
        validator._load_price(price_path)


def test_right_censoring_is_explicit_and_independently_validated(
    tmp_path: Path,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    price_path = price_root / "1111.csv"
    short_history = pd.read_csv(
        price_path, dtype=str, keep_default_na=False
    ).iloc[:8]
    short_history.to_csv(price_path, index=False, encoding="utf-8")
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    selected = events[
        events["stock_id"].astype(str).eq("1111")
        & events["scenario_id"].isin(["fixed_d10_close", "fixed_d20_close"])
    ]
    assert selected["right_censored"].astype(bool).all()
    assert not selected["return_valid"].astype(bool).any()
    assert set(selected["invalid_reason"]) == {
        "right_censored_before_d10",
        "right_censored_before_d20",
    }
    assert validator.validate_frames(
        events, summary, anomalies, manifest, root=root
    ) == []


def test_sensitivity_is_separate_and_never_corrected_primary(
    tmp_path: Path,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    assert not summary["sensitivity_is_corrected_primary"].astype(bool).any()
    for _, row in summary.iterrows():
        assert int(row["candidate_exclusion_sensitivity_count"]) == (
            int(row["mature_count"]) - int(row["anomaly_candidate_count"])
        )
    tampered_summary = summary.copy()
    tampered_summary.at[0, "sensitivity_is_corrected_primary"] = True
    errors = validator.validate_frames(
        events,
        tampered_summary,
        anomalies,
        manifest,
        root=root,
    )
    assert any("mislabels sensitivity as primary" in error for error in errors)


def _refresh_event_and_manifest_hashes(
    events: pd.DataFrame,
    manifest: pd.DataFrame,
    event_index: int,
) -> None:
    events.at[event_index, "event_row_canonical_sha256"] = (
        producer.canonical_row_sha256(events.loc[event_index])
    )
    manifest.at[0, "events_row_set_sha256"] = producer.row_set_sha256(
        events["event_row_canonical_sha256"].astype(str).tolist()
    )


def test_independent_validator_rejects_lineage_tamper(tmp_path: Path) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    tampered_events = events.copy()
    tampered_manifest = manifest.copy()
    event_index = int(tampered_events.index[0])
    tampered_events.at[event_index, "snapshot_sha256"] = "f" * 64
    _refresh_event_and_manifest_hashes(
        tampered_events, tampered_manifest, event_index
    )

    errors = validator.validate_frames(
        tampered_events,
        summary,
        anomalies,
        tampered_manifest,
        root=root,
    )
    assert any("source field snapshot_sha256 mismatch" in error for error in errors)


def test_independent_validator_rejects_anomaly_flag_tamper(tmp_path: Path) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    tampered_events = events.copy()
    tampered_anomalies = anomalies.copy()
    tampered_manifest = manifest.copy()
    event_index = int(
        tampered_events[tampered_events["anomaly_candidate_flag"].astype(bool)].index[0]
    )
    original_hash = tampered_events.at[event_index, "event_row_canonical_sha256"]
    tampered_events.at[event_index, "anomaly_candidate_flag"] = False
    tampered_events.at[event_index, "anomaly_candidate_kinds"] = ""
    tampered_events.at[event_index, "anomaly_disposition"] = "not_triggered"
    tampered_anomalies = tampered_anomalies[
        ~tampered_anomalies["event_row_canonical_sha256"].astype(str).eq(original_hash)
    ].copy()
    _refresh_event_and_manifest_hashes(
        tampered_events, tampered_manifest, event_index
    )
    tampered_manifest.at[0, "anomaly_candidate_count"] = len(tampered_anomalies)
    tampered_manifest.at[0, "effective_anomaly_blocker_count"] = len(
        tampered_anomalies
    )

    errors = validator.validate_frames(
        tampered_events,
        summary,
        tampered_anomalies,
        tampered_manifest,
        root=root,
    )
    assert any("anomaly candidate flag mismatch" in error for error in errors)


@pytest.mark.parametrize(
    "field",
    ["stock_id", "gross_return_pct", "snapshot_sha256"],
)
def test_validator_rejects_anomaly_payload_tamper(
    tmp_path: Path,
    field: str,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    tampered_anomalies = anomalies.copy()
    tampered_value = {
        "stock_id": "9999",
        "gross_return_pct": 999.0,
        "snapshot_sha256": "f" * 64,
    }[field]
    tampered_anomalies.at[tampered_anomalies.index[0], field] = tampered_value
    errors = validator.validate_frames(
        events,
        summary,
        tampered_anomalies,
        manifest,
        root=root,
    )
    assert any(f"field {field} differs" in error for error in errors)


def test_validate_files_binds_anomaly_sha_row_count_and_payload_bundle(
    tmp_path: Path,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    paths = _write_bound_artifacts(root, events, summary, anomalies, manifest)
    assert validator.validate_files(*paths, root=root) == []

    anomaly_path = paths[2]
    tampered = pd.read_csv(anomaly_path, dtype=str, keep_default_na=False)
    tampered.at[0, "stock_id"] = "9999"
    tampered.to_csv(anomaly_path, index=False, encoding="utf-8-sig")
    errors = validator.validate_files(*paths, root=root)
    assert any("anomalies artifact file SHA mismatch" in error for error in errors)
    assert any("evidence payload bundle SHA mismatch" in error for error in errors)
    assert any("field stock_id differs" in error for error in errors)

    restored_paths = _write_bound_artifacts(root, events, summary, anomalies, manifest)
    duplicated = pd.read_csv(
        restored_paths[2], dtype=str, keep_default_na=False
    )
    duplicated = pd.concat([duplicated, duplicated.iloc[[0]]], ignore_index=True)
    duplicated.to_csv(restored_paths[2], index=False, encoding="utf-8-sig")
    errors = validator.validate_files(*restored_paths, root=root)
    assert any("anomalies artifact row count mismatch" in error for error in errors)


@pytest.mark.parametrize(
    ("surface", "field", "tampered_value", "expected_error"),
    [
        ("events", "formal_use_allowed", True, "improperly allows formal use"),
        ("events", "approved_for_daily", True, "improperly allows daily approval"),
        ("events", "presentation_allowed", True, "improperly allows presentation"),
        (
            "events",
            "operation_contract_status",
            "approved",
            "operation contract is not fail closed",
        ),
        (
            "events",
            "full_historical_condition_replay_status",
            "complete",
            "full replay blocker mismatch",
        ),
        ("summary", "formal_use_allowed", True, "improperly allows formal use"),
        (
            "summary",
            "operation_contract_status",
            "approved",
            "operation contract mismatch",
        ),
        (
            "summary",
            "full_historical_condition_replay_status",
            "complete",
            "full replay blocker mismatch",
        ),
        (
            "manifest",
            "formal_use_allowed",
            True,
            "improperly enables formal_use_allowed",
        ),
        (
            "manifest",
            "approved_for_daily",
            True,
            "improperly enables approved_for_daily",
        ),
        (
            "manifest",
            "presentation_allowed",
            True,
            "improperly enables presentation_allowed",
        ),
        (
            "manifest",
            "promotion_evidence_allowed",
            True,
            "improperly enables promotion_evidence_allowed",
        ),
        (
            "manifest",
            "production_change",
            True,
            "improperly enables production_change",
        ),
        (
            "manifest",
            "operation_contract_status",
            "approved",
            "operation contract mismatch",
        ),
        (
            "manifest",
            "full_historical_condition_replay_status",
            "complete",
            "full replay blocker mismatch",
        ),
    ],
)
def test_all_formal_presentation_promotion_and_historical_flags_fail_closed(
    tmp_path: Path,
    surface: str,
    field: str,
    tampered_value: object,
    expected_error: str,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    frames = {
        "events": events.copy(),
        "summary": summary.copy(),
        "manifest": manifest.copy(),
    }
    frames[surface].at[0, field] = tampered_value
    if surface == "events":
        _refresh_event_and_manifest_hashes(
            frames["events"], frames["manifest"], 0
        )
    errors = validator.validate_frames(
        frames["events"],
        frames["summary"],
        anomalies,
        frames["manifest"],
        root=root,
    )
    assert any(expected_error in error for error in errors)


def test_independent_validator_rejects_promotion_flag_tamper(tmp_path: Path) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    tampered_events = events.copy()
    tampered_manifest = manifest.copy()
    event_index = int(tampered_events.index[0])
    tampered_events.at[event_index, "approved_for_daily"] = True
    tampered_events.at[event_index, "presentation_allowed"] = True
    tampered_events.at[event_index, "operation_contract_status"] = "approved"
    tampered_events.at[
        event_index, "full_historical_condition_replay_status"
    ] = "complete"
    _refresh_event_and_manifest_hashes(
        tampered_events, tampered_manifest, event_index
    )
    tampered_manifest.at[0, "approved_for_daily"] = True
    tampered_manifest.at[0, "presentation_allowed"] = True
    tampered_manifest.at[0, "promotion_evidence_allowed"] = True
    tampered_manifest.at[0, "operation_contract_status"] = "approved"
    tampered_manifest.at[
        0, "full_historical_condition_replay_status"
    ] = "complete"

    errors = validator.validate_frames(
        tampered_events,
        summary,
        anomalies,
        tampered_manifest,
        root=root,
    )
    assert any("improperly allows daily approval" in error for error in errors)
    assert any("manifest improperly enables approved_for_daily" in error for error in errors)
    assert any("manifest operation contract mismatch" in error for error in errors)


@pytest.mark.parametrize(
    "invalid_token",
    ["false", "0", "unexpected", "", " True ", "\tFalse\n"],
)
def test_validator_rejects_unknown_formal_and_promotion_bool_tokens(
    tmp_path: Path,
    invalid_token: str,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    events = events.astype(object)
    manifest = manifest.astype(object)
    events.at[events.index[0], "formal_use_allowed"] = invalid_token
    manifest.at[0, "promotion_evidence_allowed"] = invalid_token

    errors = validator.validate_frames(
        events,
        summary,
        anomalies,
        manifest,
        root=root,
    )

    assert any(
        "events formal_use_allowed must use exact True/False tokens" in error
        for error in errors
    )
    assert any(
        "manifest promotion_evidence_allowed must use exact True/False tokens" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("surface", "field", "invalid_token"),
    [
        ("events", "approved_for_daily", "unexpected"),
        ("events", "presentation_allowed", "0"),
        ("manifest", "production_change", "false"),
        ("manifest", "production_condition_recalculated", "\tFalse\n"),
    ],
)
def test_reviewer_boolean_mutations_fail_before_semantic_interpretation(
    tmp_path: Path,
    surface: str,
    field: str,
    invalid_token: str,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    frames = {
        "events": events.astype(object),
        "summary": summary.astype(object),
        "manifest": manifest.astype(object),
    }
    frames[surface].at[frames[surface].index[0], field] = invalid_token

    errors = validator.validate_frames(
        frames["events"],
        frames["summary"],
        anomalies,
        frames["manifest"],
        root=root,
    )

    assert errors == [
        f"{surface} {field} must use exact True/False tokens: "
        f"observed={[invalid_token]}"
    ]


BOOLEAN_CONTRACT_CASES = [
    (surface, field)
    for surface, fields in validator.BOOLEAN_CONTRACT_FIELDS.items()
    for field in fields
]


@pytest.mark.parametrize(("surface", "field"), BOOLEAN_CONTRACT_CASES)
def test_every_boolean_contract_field_rejects_nonexact_tokens(
    tmp_path: Path,
    surface: str,
    field: str,
) -> None:
    assert validator.BOOLEAN_CONTRACT_FIELDS == {
        "events": (
            "return_valid",
            "right_censored",
            "primary_metric_included",
            "anomaly_candidate_flag",
            "formal_use_allowed",
            "approved_for_daily",
            "presentation_allowed",
            "research_only",
        ),
        "summary": (
            "primary_metrics_retain_unresolved_candidates",
            "sensitivity_is_corrected_primary",
            "formal_use_allowed",
        ),
        "manifest": (
            "production_condition_recalculated",
            "formal_use_allowed",
            "approved_for_daily",
            "presentation_allowed",
            "promotion_evidence_allowed",
            "production_change",
        ),
    }
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    events, summary, anomalies, manifest = producer.build_research(
        manifest_path=manifest_path,
        snapshot_root=snapshot_root,
        price_root=price_root,
    )
    frames = {
        "events": events.astype(object),
        "summary": summary.astype(object),
        "manifest": manifest.astype(object),
    }
    frames[surface].at[frames[surface].index[0], field] = " False "

    errors = validator.validate_frames(
        frames["events"],
        frames["summary"],
        anomalies,
        frames["manifest"],
        root=root,
    )

    assert errors == [
        f"{surface} {field} must use exact True/False tokens: "
        "observed=[' False ']"
    ]


def test_producer_and_independent_validator_reject_impossible_identity_dates(
    tmp_path: Path,
) -> None:
    root, manifest_path, snapshot_root, price_root = _fixture(tmp_path)
    source_manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    source_manifest.at[0, "snapshot_report_date"] = "20261340"
    source_manifest.to_csv(manifest_path, index=False, encoding="utf-8")

    with pytest.raises(RuntimeError, match="invalid report dates"):
        producer.build_research(
            manifest_path=manifest_path,
            snapshot_root=snapshot_root,
            price_root=price_root,
        )

    with pytest.raises(RuntimeError, match="invalid report dates"):
        validator._rebuild_source_bases(manifest_path, root)


@pytest.mark.parametrize(
    "invalid_date",
    ["20261340", " 20260101 ", "\t20260228\n"],
)
def test_producer_and_validator_date_parsers_reject_nonexact_or_impossible_dates(
    invalid_date: str,
) -> None:
    assert producer._date(invalid_date) == ""
    assert validator._date(invalid_date) == ""


def test_validator_imports_only_stdlib_and_pandas() -> None:
    validator_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "validate_hot_theme_pullback_research.py"
    )
    tree = ast.parse(validator_path.read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    allowed_import_roots = {
        "__future__",
        "hashlib",
        "datetime",
        "json",
        "math",
        "pathlib",
        "typing",
        "pandas",
    }
    assert {name.split(".", 1)[0] for name in imported} <= allowed_import_roots
    assert "pandas" in imported
