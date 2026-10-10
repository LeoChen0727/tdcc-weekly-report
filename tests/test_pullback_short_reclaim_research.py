from __future__ import annotations

import ast
import base64
import copy
import hashlib
import json
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_pullback_short_reclaim_research as producer  # noqa: E402
import validate_pullback_short_reclaim_research as validator  # noqa: E402
import build_pullback_short_reclaim_share_unit_reconciliation as unit_producer  # noqa: E402
import validate_pullback_short_reclaim_share_unit_reconciliation as unit_validator  # noqa: E402
import validate_pullback_short_reclaim_matched_feature_research as matched_feature_validator  # noqa: E402

# Keep the model-owned comparison suite on the existing shared-research CI entrypoint.
from test_pullback_short_reclaim_23ema_condition_comparison import (  # noqa: E402,F401
    comparison_sources,
    comparison_bundle,
    comparison_references,
    test_comparison_independent_bundle_success,
    test_comparison_frozen_columns_dates_and_partial_basis_unchanged,
    test_comparison_original_cell_tamper_rejected,
    test_comparison_joined_feature_tamper_rejected,
    test_comparison_source_and_snapshot_tamper_rejected,
    test_comparison_legacy_crlf_identity_is_not_guessed,
    test_comparison_summary_metrics_tamper_rejected,
    test_comparison_full_and_same_schema_denominators_are_separate,
    test_comparison_exhaustive_table_rows_and_order,
    test_comparison_feature_table_tamper_rejected,
    test_comparison_unknown_and_recorded_false_are_not_equivalent,
    test_comparison_feature_numeric_boundaries,
    test_comparison_return_thresholds_censoring_and_sensitivity_are_descriptive,
    test_comparison_manifest_boundary_tamper_rejected,
    test_comparison_validator_has_no_business_import,
    test_comparison_unsafe_source_paths_fail_closed,
    test_comparison_actual_artifact_bytes_validate,
    test_comparison_new_anomaly_candidates_stay_primary,
    test_comparison_feature_denominators_include_same_schema_populations,
    test_comparison_immutable_output_lf_rules,
)

# Keep the model-owned matched-feature suite on the existing shared-research CI entrypoint.
from test_pullback_short_reclaim_matched_feature_research import (  # noqa: E402,F401
    independent_references,
    matched_bundle,
    source_payloads,
    test_actual_published_artifacts_validate_when_present,
    test_audit_identity_overlap_and_union_contract,
    test_audit_tamper_rejected,
    test_boundary_flags_fail_closed,
    test_exact_eight_event_union_and_dispositions,
    test_exact_schema_and_column_order,
    test_feature_tamper_rejected,
    test_frozen_source_hash_and_manifest_tamper_rejected,
    test_manifest_tamper_rejected,
    test_matched_bundle_independently_validates,
    test_metric_tamper_rejected,
    test_missing_paired_side_keeps_difference_blank,
    test_model_owned_guard_rejects_foreign_model_write,
    test_model_owned_guard_rejects_protected_index_or_head_drift,
    test_model_owned_guard_rejects_unregistered_outputs,
    test_row_order_and_exhaustiveness_are_contractual,
    test_shallow_checkout_filesystem_fallback_is_content_sha_only,
    test_source_candidate_disposition_change_rejected,
    test_validator_has_no_producer_or_business_semantic_import,
    test_write_bundle_different_existing_bytes_fails_without_overwrite,
    test_write_bundle_same_existing_bytes_are_not_rewritten,
)


def test_matched_feature_published_bundle_ci_bridge() -> None:
    result = matched_feature_validator.validate(ROOT)
    assert result["source_rows"] == 3020
    assert result["unique_signal_events"] == 2992
    assert result["source_duplicate_groups"] == 28
    assert result["union_review_candidate_events"] == 8
    assert result["first_publication_pit_proven"] is False
    assert result["formal_use_allowed"] is False


REPORT_DATE = "20260803"


def _signal_row(
    stock_id: str,
    *,
    report_line: str = "mainstream",
    model_id: str = producer.MODEL_ID,
    score: str = "60",
) -> dict[str, str]:
    return {
        "signal_date": REPORT_DATE,
        "source_row_index": stock_id,
        "stock_id": stock_id,
        "stock_name": f"Stock {stock_id}",
        "model_id": model_id,
        "model_name_zh": "回檔後短線轉強模型",
        "main_condition_met": "True",
        "entry_basis": "signal_date_next_open",
        "model_score": score,
        "score_components": "base=50",
        "risk_penalty_tags": "",
        "next_confirmation": "close_confirmed",
        "model_main_conditions": "published_exact_signal",
        "model_add_score_items": "",
        "model_forbidden_veto": "",
        "model_operation_guidance": "research_only",
        "selection_semantics": "published_signal_truth",
        "model_rank": "1",
        "report_line": report_line,
        "report_bucket": report_line,
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def _snapshot_path(
    snapshot_dir: Path,
    rows: list[dict[str, str]],
    revision: str,
) -> tuple[Path, str]:
    staging = snapshot_dir / f"staging_{revision}.csv"
    _write_csv(staging, rows)
    sha = producer.canonical_file_sha256(staging)
    path = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_{revision}_{sha[:12]}.csv"
    )
    staging.rename(path)
    return path, sha


def _manifest_row(
    path: Path,
    sha: str,
    revision: str,
    *,
    supersedes: str = "",
    reason: str = "fixture",
) -> dict[str, str]:
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    return {
        "snapshot_report_date": REPORT_DATE,
        "snapshot_revision": revision,
        "supersedes_snapshot_sha256": supersedes,
        "revision_reason": reason,
        "generated_at": "2026-08-03 18:00:00 Asia/Taipei",
        "pipeline_commit_sha": "a" * 40,
        "main_price_date": REPORT_DATE,
        "report_ready": "True",
        "artifact_id": producer.ARTIFACT_ID,
        "source_path": "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "snapshot_path": path.resolve().as_posix(),
        "source_sha256": sha,
        "snapshot_sha256": sha,
        "row_count": str(len(frame)),
        "column_count": str(len(frame.columns)),
        "purpose": "as_published_daily_model_snapshot",
    }


def _write_price(
    price_dir: Path,
    stock_id: str,
    closes: list[float],
    *,
    entry_open: float = 100.0,
) -> None:
    dates = pd.bdate_range("2026-08-03", periods=len(closes) + 1)
    rows: list[dict[str, object]] = [
        {
            "date": dates[0].strftime("%Y%m%d"),
            "stock_id": stock_id,
            "open": entry_open,
            "close": entry_open,
        }
    ]
    for position, close in enumerate(closes, start=1):
        rows.append(
            {
                "date": dates[position].strftime("%Y%m%d"),
                "stock_id": stock_id,
                "open": entry_open if position == 1 else closes[position - 2],
                "close": close,
            }
        )
    _write_csv(price_dir / f"{stock_id}.csv", rows)


def _fixture(
    tmp_path: Path,
    *,
    target_rows: list[dict[str, str]] | None = None,
    include_r1: bool = True,
    price_rows: dict[str, list[float]] | None = None,
) -> tuple[Path, Path, Path]:
    snapshot_dir = tmp_path / "output/history/daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    latest_rows = target_rows or [
        _signal_row("1111", report_line="mainstream"),
        _signal_row("1111", report_line="non_mainstream"),
        _signal_row("2222"),
        _signal_row("3333", model_id="another_model"),
    ]
    manifest_rows: list[dict[str, str]] = []
    supersedes = ""
    if include_r1:
        r1_path, r1_sha = _snapshot_path(
            snapshot_dir,
            [_signal_row("9999")],
            "r1",
        )
        manifest_rows.append(_manifest_row(r1_path, r1_sha, "r1", reason="initial"))
        supersedes = r1_sha
        revision = "r2"
    else:
        revision = "r1"
    latest_path, latest_sha = _snapshot_path(snapshot_dir, latest_rows, revision)
    manifest_rows.append(
        _manifest_row(
            latest_path,
            latest_sha,
            revision,
            supersedes=supersedes,
            reason="corrected_latest" if include_r1 else "initial",
        )
    )
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    _write_csv(manifest_path, manifest_rows)
    price_dir = tmp_path / "data/stock_price_history"
    for stock_id, closes in (
        price_rows
        or {
            "1111": [100, 101, 102, 103, 110, 105, 104, 103, 102, 100]
            + [99] * 9
            + [80],
            "2222": [100, 120, 140, 160, 200] + [200] * 15,
        }
    ).items():
        _write_price(price_dir, stock_id, closes)
    return snapshot_dir, manifest_path, price_dir


def _build(
    snapshot_dir: Path,
    manifest_path: Path,
    price_dir: Path,
) -> producer.ReplayBundle:
    return producer.build_replay(
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
        generated_at="2026-09-01 12:00:00 Asia/Taipei",
    )


def _mutate_artifact_header(frame: pd.DataFrame, mutation: str) -> pd.DataFrame:
    columns = list(frame.columns)
    if mutation == "missing":
        return frame.drop(columns=[columns[-1]])
    if mutation == "extra":
        mutated = frame.copy()
        mutated["unexpected_header_field"] = ""
        return mutated
    if mutation == "reordered":
        return frame.loc[:, [columns[1], columns[0], *columns[2:]]]
    if mutation == "duplicate":
        mutated = frame.copy()
        mutated.insert(1, columns[0], mutated.iloc[:, 0], allow_duplicates=True)
        return mutated
    raise AssertionError(f"unsupported header mutation: {mutation}")


def test_latest_revision_exact_signal_replay_and_identity_dedup(tmp_path: Path) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)

    bundle = _build(snapshot_dir, manifest_path, price_dir)

    assert set(bundle.events["snapshot_revision"]) == {"r2"}
    assert set(bundle.events["stock_id"]) == {"1111", "2222"}
    assert len(bundle.events) == 3
    duplicate = bundle.events[bundle.events["stock_id"].eq("1111")]
    assert len(duplicate) == 2
    assert duplicate["primary_metric_included"].tolist() == ["True", "False"]
    assert duplicate["source_row_sha256"].nunique() == 2
    canonical = duplicate[duplicate["primary_metric_included"].eq("True")].iloc[0]
    assert canonical["entry_date"] == "20260804"
    assert float(canonical["entry_open_price"]) == 100.0
    assert float(canonical["d5_return_pct"]) == 10.0
    assert canonical["d5_outcome"] == "win"
    assert float(canonical["d10_return_pct"]) == 0.0
    assert canonical["d10_outcome"] == "neutral"
    assert float(canonical["d20_return_pct"]) == -20.0
    assert canonical["d20_outcome"] == "failure"
    d5 = bundle.summary[bundle.summary["horizon"].eq("D+5")].iloc[0]
    assert int(d5["published_source_row_count"]) == 3
    assert int(d5["unique_signal_event_count"]) == 2
    assert int(d5["duplicate_presentation_row_count"]) == 1
    assert int(d5["mature_count"]) == 2
    assert set(bundle.summary["formal_use_allowed"]) == {"False"}
    assert set(bundle.summary["operation_contract_status"]) == {"decision_required"}
    assert validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    ) == []


@pytest.mark.parametrize("surface", ["events", "summary", "anomalies"])
def test_validate_files_rejects_non_exact_artifact_headers(
    tmp_path: Path,
    surface: str,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    paths = producer.write_replay(bundle, tmp_path / "research")
    artifact_paths = {
        "events": paths[0],
        "summary": paths[1],
        "anomalies": paths[2],
    }
    original_payloads = {path: path.read_bytes() for path in artifact_paths.values()}

    for mutation, expected_error in (
        ("missing", "missing columns"),
        ("extra", "has unexpected columns"),
        ("reordered", "column order mismatch"),
        ("duplicate", "has unexpected columns"),
    ):
        for path, payload in original_payloads.items():
            path.write_bytes(payload)
        artifact_path = artifact_paths[surface]
        frame = pd.read_csv(artifact_path, dtype=str, keep_default_na=False)
        tampered = _mutate_artifact_header(frame, mutation)
        tampered.to_csv(artifact_path, index=False, encoding="utf-8")

        errors = validator.validate_files(
            events_path=paths[0],
            summary_path=paths[1],
            anomalies_path=paths[2],
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            price_dir=price_dir,
        )

        assert any(
            f"{surface} artifact header {expected_error}" in error
            for error in errors
        )


def test_anomaly_candidate_is_unresolved_and_retained_in_primary_metrics(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)

    bundle = _build(snapshot_dir, manifest_path, price_dir)

    anomaly = bundle.anomalies[
        bundle.anomalies["stock_id"].eq("2222")
        & bundle.anomalies["horizon"].eq("D+5")
    ].iloc[0]
    assert float(anomaly["realized_return_pct"]) == 100.0
    assert anomaly["statistical_trigger_status"] == "anomaly_candidate"
    assert anomaly["final_disposition"] == "unresolved_anomaly_candidate"
    assert anomaly["retained_in_primary_metrics"] == "True"
    d5 = bundle.summary[bundle.summary["horizon"].eq("D+5")].iloc[0]
    assert int(d5["mature_count"]) == 2
    assert int(d5["unresolved_anomaly_candidate_count"]) == 1
    assert int(d5["excluded_anomaly_candidate_count"]) == 0
    assert float(d5["average_return_pct"]) == 55.0
    assert int(d5["sensitivity_sample_count"]) == 1
    assert int(d5["sensitivity_excluded_anomaly_candidate_count"]) == 1
    assert float(d5["sensitivity_average_return_pct"]) == 10.0
    assert d5["sensitivity_is_corrected_primary"] == "False"
    assert d5["price_source_formal_lineage_status"] == (
        "mutable_current_files_unpinned_block_formal_use"
    )


def test_maturity_is_explicit_for_partial_and_missing_price_history(
    tmp_path: Path,
) -> None:
    rows = [_signal_row("1111"), _signal_row("4444")]
    snapshot_dir, manifest_path, price_dir = _fixture(
        tmp_path,
        target_rows=rows,
        include_r1=False,
        price_rows={"1111": [101, 102, 103, 104, 105, 106, 107]},
    )

    bundle = _build(snapshot_dir, manifest_path, price_dir)

    partial = bundle.events[bundle.events["stock_id"].eq("1111")].iloc[0]
    missing = bundle.events[bundle.events["stock_id"].eq("4444")].iloc[0]
    assert partial["d5_maturity_status"] == "mature"
    assert partial["d10_maturity_status"] == "not_mature"
    assert partial["d20_maturity_status"] == "not_mature"
    assert missing["d5_maturity_status"] == "missing_price_history"
    assert missing["price_source_sha256"] == ""
    assert int(bundle.summary.loc[bundle.summary["horizon"].eq("D+5"), "mature_count"].iloc[0]) == 1
    assert int(bundle.summary.loc[bundle.summary["horizon"].eq("D+10"), "mature_count"].iloc[0]) == 0
    assert int(
        bundle.summary.loc[
            bundle.summary["horizon"].eq("D+5"), "right_censored_count"
        ].iloc[0]
    ) == 1
    assert int(
        bundle.summary.loc[
            bundle.summary["horizon"].eq("D+10"), "right_censored_count"
        ].iloc[0]
    ) == 2


def test_snapshot_row_count_mismatch_fails_closed(tmp_path: Path) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[manifest.index[-1], "row_count"] = "999"
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    with pytest.raises(RuntimeError, match="row/column count mismatch"):
        _build(snapshot_dir, manifest_path, price_dir)


def test_duplicate_report_rows_with_semantic_drift_fail_closed(tmp_path: Path) -> None:
    rows = [
        _signal_row("1111", report_line="mainstream", score="60"),
        _signal_row("1111", report_line="non_mainstream", score="61"),
    ]
    snapshot_dir, manifest_path, price_dir = _fixture(
        tmp_path,
        target_rows=rows,
        include_r1=False,
        price_rows={"1111": [100] * 20},
    )

    with pytest.raises(RuntimeError, match="disagree on signal semantics"):
        _build(snapshot_dir, manifest_path, price_dir)


def test_independent_validator_detects_return_formal_and_summary_tampering(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    events = bundle.events.astype(object).copy()
    summary = bundle.summary.astype(object).copy()
    events.loc[events.index[0], "d5_return_pct"] = "999"
    events.loc[events.index[0], "formal_use_allowed"] = "True"
    summary.loc[summary["horizon"].eq("D+5"), "mature_count"] = "999"

    errors = validator.validate_replay_bundle(
        events,
        summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )

    assert any("formal_use_allowed" in error for error in errors)
    assert any("d5_return_pct mismatch" in error for error in errors)
    assert any("mature_count mismatch" in error for error in errors)


def test_independent_validator_detects_removed_or_promoted_anomaly(tmp_path: Path) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    anomalies = bundle.anomalies.copy()
    anomalies.loc[anomalies.index[0], "final_disposition"] = "verified_real_extreme"

    errors = validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )

    assert any("final_disposition mismatch" in error for error in errors)

    removed_errors = validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        bundle.anomalies.iloc[0:0].copy(),
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("does not exactly match numerical trigger candidates" in error for error in removed_errors)


def test_validator_rejects_revision_source_row_and_price_lineage_tampering(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)

    wrong_revision = bundle.events.astype(object).copy()
    wrong_revision.loc[wrong_revision.index[0], "snapshot_revision"] = "r1"
    revision_errors = validator.validate_replay_bundle(
        wrong_revision,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("latest-revision pullback source rows" in error for error in revision_errors)

    wrong_hashes = bundle.events.astype(object).copy()
    wrong_hashes.loc[wrong_hashes.index[0], "source_row_sha256"] = "0" * 64
    wrong_hashes.loc[wrong_hashes.index[1], "price_source_sha256"] = "1" * 64
    hash_errors = validator.validate_replay_bundle(
        wrong_hashes,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("source_row_sha256 mismatch" in error for error in hash_errors)
    assert any("price_source_sha256 mismatch" in error for error in hash_errors)

    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[manifest["snapshot_revision"].eq("r2"), "supersedes_snapshot_sha256"] = (
        "f" * 64
    )
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")
    chain_errors = validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("supersedes_snapshot_sha256" in error for error in chain_errors)


def test_validator_recomputes_anomaly_trigger_and_rejects_gate_promotion(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    anomaly_event_index = bundle.events.index[
        bundle.events["stock_id"].eq("2222")
        & bundle.events["primary_metric_included"].eq("True")
    ][0]
    cleared = bundle.events.astype(object).copy()
    cleared.loc[anomaly_event_index, "d5_anomaly_candidate"] = "False"
    cleared.loc[anomaly_event_index, "statistical_trigger_status"] = "not_triggered"
    cleared.loc[anomaly_event_index, "anomaly_candidate_horizons"] = ""
    cleared.loc[anomaly_event_index, "anomaly_disposition"] = "not_applicable"
    trigger_errors = validator.validate_replay_bundle(
        cleared,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("d5_anomaly_candidate mismatch" in error for error in trigger_errors)

    events = bundle.events.astype(object).copy()
    summary = bundle.summary.astype(object).copy()
    anomalies = bundle.anomalies.astype(object).copy()
    events.loc[events.index[0], "formal_use_allowed"] = "True"
    events.loc[events.index[0], "trade_eligible"] = "True"
    events.loc[events.index[0], "promotion_evidence_allowed"] = "True"
    events.loc[events.index[0], "operation_contract_status"] = "approved"
    summary.loc[summary.index[0], "promotion_evidence_allowed"] = "True"
    summary.loc[summary.index[0], "sensitivity_is_corrected_primary"] = "True"
    anomalies.loc[anomalies.index[0], "promotion_evidence_allowed"] = "True"
    gate_errors = validator.validate_replay_bundle(
        events,
        summary,
        anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("formal_use_allowed" in error for error in gate_errors)
    assert any("trade_eligible" in error for error in gate_errors)
    assert any("promotion_evidence_allowed" in error for error in gate_errors)
    assert any("operation_contract_status" in error for error in gate_errors)
    assert any("corrected primary" in error for error in gate_errors)


@pytest.mark.parametrize("identity_surface", ["report", "signal", "price"])
def test_producer_and_independent_validator_reject_impossible_identity_dates(
    tmp_path: Path,
    identity_surface: str,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path, include_r1=False)
    valid_bundle = _build(snapshot_dir, manifest_path, price_dir)
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    latest = manifest.index[-1]
    snapshot_path = Path(manifest.at[latest, "snapshot_path"])

    if identity_surface == "report":
        manifest.at[latest, "snapshot_report_date"] = "20261340"
    elif identity_surface == "signal":
        snapshot = pd.read_csv(snapshot_path, dtype=str, keep_default_na=False)
        target_index = snapshot[snapshot["model_id"].eq(producer.MODEL_ID)].index[0]
        snapshot.at[target_index, "signal_date"] = "20261340"
        snapshot.to_csv(snapshot_path, index=False, encoding="utf-8", lineterminator="\n")
        sha = producer.canonical_file_sha256(snapshot_path)
        manifest.at[latest, "snapshot_sha256"] = sha
    else:
        price_path = price_dir / "1111.csv"
        price = pd.read_csv(price_path, dtype=str, keep_default_na=False)
        price.at[0, "date"] = "20261340"
        price.to_csv(price_path, index=False, encoding="utf-8", lineterminator="\n")
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    with pytest.raises(RuntimeError, match="invalid|date contract|signal_date|identity"):
        _build(snapshot_dir, manifest_path, price_dir)

    errors = validator.validate_replay_bundle(
        valid_bundle.events,
        valid_bundle.summary,
        valid_bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("independent source replay failed" in error for error in errors)


@pytest.mark.parametrize(
    "invalid_date",
    ["20261340", " 20260101 ", "\t20260228\n"],
)
def test_producer_and_validator_date_parsers_reject_nonexact_or_impossible_dates(
    invalid_date: str,
) -> None:
    assert producer._date(invalid_date) == ""
    assert validator._date(invalid_date) == ""


def test_empty_anomaly_artifact_keeps_schema_and_validates_from_files(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(
        tmp_path,
        target_rows=[_signal_row("1111")],
        include_r1=False,
        price_rows={"1111": [101] * 20},
    )
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    output_dir = tmp_path / "research"
    events_path, summary_path, anomalies_path = producer.write_replay(bundle, output_dir)

    assert bundle.anomalies.empty
    assert set(validator.ANOMALY_REQUIRED_COLUMNS).issubset(bundle.anomalies.columns)
    assert validator.validate_files(
        events_path=events_path,
        summary_path=summary_path,
        anomalies_path=anomalies_path,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    ) == []


def test_validator_imports_are_limited_to_stdlib_pandas_and_low_level_utils() -> None:
    source_path = SCRIPTS / "validate_pullback_short_reclaim_research.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    imported_modules: set[str] = set()
    project_imports: list[ast.ImportFrom] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module)
            if node.module.split(".", 1)[0] not in sys.stdlib_module_names and (
                node.module.split(".", 1)[0] != "pandas"
            ):
                project_imports.append(node)

    allowed_roots = set(sys.stdlib_module_names) | {"pandas"}
    unexpected = {
        module
        for module in imported_modules
        if module.split(".", 1)[0] not in allowed_roots
        and not module.endswith("_utils")
    }
    assert unexpected == set()
    assert len(project_imports) == 2
    assert all(
        node.module is not None
        and "." not in node.module
        and node.module.endswith("_utils")
        and all(
            alias.name.startswith(("normalize_", "safe_", "select_", "snapshot_"))
            for alias in node.names
        )
        for node in project_imports
    )


def test_cli_write_is_wrapped_by_model_owned_artifact_guard() -> None:
    source_path = SCRIPTS / "build_pullback_short_reclaim_research.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    main = next(
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "main"
    )
    guards = [
        node
        for node in ast.walk(main)
        if isinstance(node, ast.With)
        and any(
            isinstance(item.context_expr, ast.Call)
            and isinstance(item.context_expr.func, ast.Name)
            and item.context_expr.func.id == "model_owned_artifact_guard"
            for item in node.items
        )
    ]

    assert len(guards) == 1
    preflight_statement = next(
        node
        for node in main.body
        if isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id == "_preflight_model_owned_outputs"
    )
    guard_statement = next(node for node in main.body if node is guards[0])
    assert main.body.index(preflight_statement) < main.body.index(guard_statement)


def test_cli_without_registered_ownership_leaves_no_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry_path = tmp_path / "config/model_research_artifact_ownership.csv"
    _write_csv(
        registry_path,
        [
            {
                "owner_model_id": "unrelated_model",
                "producer": "unrelated_producer",
                "artifact_glob": "output/latest/research_backtest/unrelated_*",
                "artifact_class": "model_research_output",
                "change_policy": "model_owned_write",
                "formal_evidence_status": "research_only",
            }
        ],
    )
    monkeypatch.setattr(producer, "ROOT", tmp_path)
    output_dir = tmp_path / "output/latest/research_backtest"

    with pytest.raises(RuntimeError, match="unregistered artifact change"):
        producer.main([])

    assert not output_dir.exists()
    assert all(
        not path.exists() for path in producer._replay_output_paths(output_dir)
    )


@pytest.fixture(scope="module")
def frozen_share_unit_bundle() -> tuple:
    """Read five pinned blobs once; never rerun the old market replay producer."""
    config = json.loads((ROOT / unit_producer.CONFIG_REL).read_text(encoding="utf-8"))
    bundle = unit_producer.build_bundle(ROOT)
    sources = unit_validator.load_sources(ROOT)
    return bundle, config, sources


def _unit_manifest_rebound(detail: pd.DataFrame, summary: pd.DataFrame, manifest: dict) -> dict:
    result = copy.deepcopy(manifest)
    result["output_sha256"] = {
        unit_validator.OUTPUTS[key]: hashlib.sha256(
            frame.to_csv(index=False, lineterminator="\n").encode("utf-8")
        ).hexdigest()
        for key, frame in (("detail", detail), ("summary", summary))
    }
    return result


def test_share_unit_frozen_population_dates_and_unresolved_primary_preserved(frozen_share_unit_bundle: tuple) -> None:
    (detail, summary, manifest), config, sources = frozen_share_unit_bundle
    result = unit_validator.validate_bundle(ROOT, detail, summary, manifest, config=config, sources=sources)
    assert result == {
        "source_rows": 3020, "unique_signal_events": 2992, "known_action_affected_rows": 1,
        "unresolved_anomalies_retained": 1, "formal_use_allowed": False, "total_return_complete": False,
    }
    target = detail[detail.stock_id.eq("5904")].iloc[0]
    assert target.entry_date == "20260714"
    assert target.d20_exit_date == "20260819"  # Individual stock row 20, not market day 20.
    assert target.d5_share_factor == target.d10_share_factor == "1"
    assert target.d5_share_unit_return_pct == target.d5_return_pct
    assert target.d10_share_unit_return_pct == target.d10_return_pct
    assert target.d20_share_factor == "10"
    assert target.d20_return_pct == "-88.270677"
    assert target.d20_share_unit_return_pct == "17.293233"
    assert target.primary_metric_included == "True"
    assert target.anomaly_disposition == "unresolved_anomaly_candidate"
    assert target.cash_flow_status == "not_modelled_not_total_return"
    assert set(detail.formal_use_allowed) == {"False"}
    assert set(detail.promotion_evidence_allowed) == {"False"}
    assert set(detail.total_return_complete) == {"False"}
    assert summary.partial_known_share_unit_affected_count.tolist() == ["0", "0", "1"]


@pytest.mark.parametrize("column,value", [
    ("d20_share_factor", "100"),
    ("d20_share_unit_return_pct", "1072.932331"),
    ("d5_share_factor", "10"),
    ("d10_share_unit_return_pct", "904.51128"),
    ("entry_date", "20260810"),
    ("d20_exit_date", "20260810"),
    ("d20_return_pct", "17.293233"),
    ("primary_metric_included", "False"),
    ("anomaly_disposition", "verified_non_comparable"),
    ("formal_use_allowed", "True"),
    ("promotion_evidence_allowed", "True"),
    ("total_return_complete", "True"),
    ("first_publication_pit_proven", "True"),
    ("cash_flow_status", "complete_total_return"),
])
def test_share_unit_validator_rejects_detail_tampering_even_with_rebound_hash(
    frozen_share_unit_bundle: tuple, column: str, value: str,
) -> None:
    (original, summary, manifest), config, sources = frozen_share_unit_bundle
    detail = original.copy(deep=True)
    detail.loc[detail.stock_id.eq("5904"), column] = value
    rebound = _unit_manifest_rebound(detail, summary, manifest)
    with pytest.raises(ValueError):
        unit_validator.validate_bundle(ROOT, detail, summary, rebound, config=config, sources=sources)


@pytest.mark.parametrize("column,value", [
    ("average_return_pct", "99"),
    ("unresolved_anomaly_candidate_count", "0"),
    ("partial_known_share_unit_mature_count", "1965"),
    ("partial_known_share_unit_affected_count", "0"),
    ("partial_known_share_unit_win_rate_pct", "99"),
    ("partial_known_share_unit_average_return_pct", "99"),
    ("partial_known_share_unit_median_return_pct", "99"),
    ("partial_known_share_unit_result_status", "corrected_primary"),
])
def test_share_unit_validator_rejects_summary_tampering_even_with_rebound_hash(
    frozen_share_unit_bundle: tuple, column: str, value: str,
) -> None:
    (detail, original, manifest), config, sources = frozen_share_unit_bundle
    summary = original.copy(deep=True)
    summary.loc[summary.horizon.eq("D+20"), column] = value
    rebound = _unit_manifest_rebound(detail, summary, manifest)
    with pytest.raises(ValueError):
        unit_validator.validate_bundle(ROOT, detail, summary, rebound, config=config, sources=sources)


@pytest.mark.parametrize("mutation", ["factor", "effective_date", "receipt", "source_commit", "price_hash", "formal"])
def test_share_unit_config_is_anchored_not_self_authenticating(frozen_share_unit_bundle: tuple, mutation: str) -> None:
    (detail, summary, original_manifest), original_config, sources = frozen_share_unit_bundle
    config = copy.deepcopy(original_config)
    if mutation == "factor":
        config["action"]["share_factor"] = 100
    elif mutation == "effective_date":
        config["action"]["effective_date"] = "20260720"
    elif mutation == "receipt":
        fake_receipt = base64.b64decode(config["action"]["receipt_body_base64"]).replace(b"5904", b"5905")
        config["action"]["receipt_body_base64"] = base64.b64encode(fake_receipt).decode("ascii")
        config["action"]["receipt_sha256"] = hashlib.sha256(fake_receipt).hexdigest()
    elif mutation == "source_commit":
        config["source_commit"] = "0" * 40
    elif mutation == "price_hash":
        config["price_source"]["raw_sha256"] = "0" * 64
    else:
        config["limitations"]["formal_model_use_allowed"] = True
    manifest = copy.deepcopy(original_manifest)
    manifest["config_canonical_sha256"] = hashlib.sha256(
        json.dumps(config, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    manifest["action"] = config["action"]
    with pytest.raises(RuntimeError):
        unit_producer.validate_config(config)
    with pytest.raises(ValueError):
        unit_validator.validate_bundle(ROOT, detail, summary, manifest, config=config, sources=sources)


def test_share_unit_validator_rejects_raw_source_and_manifest_hash_drift(frozen_share_unit_bundle: tuple) -> None:
    (detail, summary, original_manifest), config, original_sources = frozen_share_unit_bundle
    sources = dict(original_sources)
    sources["price"] += b"\n"
    with pytest.raises(ValueError, match="immutable input raw SHA"):
        unit_validator.validate_bundle(ROOT, detail, summary, original_manifest, config=config, sources=sources)
    manifest = copy.deepcopy(original_manifest)
    manifest["output_sha256"][unit_validator.OUTPUTS["detail"]] = "0" * 64
    with pytest.raises(ValueError, match="manifest"):
        unit_validator.validate_bundle(ROOT, detail, summary, manifest, config=config, sources=original_sources)


def test_share_unit_independent_validator_does_not_import_project_business_code() -> None:
    tree = ast.parse((SCRIPTS / "validate_pullback_short_reclaim_share_unit_reconciliation.py").read_text(encoding="utf-8"))
    imports = {
        name.split(".", 1)[0]
        for node in ast.walk(tree)
        for name in ([alias.name for alias in node.names] if isinstance(node, ast.Import)
                     else [node.module or ""] if isinstance(node, ast.ImportFrom) else [])
    }
    assert imports <= set(sys.stdlib_module_names) | {"pandas"}


def test_share_unit_producer_rejects_double_adjustment(frozen_share_unit_bundle: tuple) -> None:
    (detail, summary, _manifest), config, sources = frozen_share_unit_bundle
    with pytest.raises(RuntimeError, match="already reconciled"):
        unit_producer.build_reconciliation(detail, summary, unit_validator._csv(sources["anomalies"]),
                                          unit_validator._csv(sources["price"]), config)


def test_share_unit_committed_artifacts_pass_independent_byte_validation() -> None:
    result = unit_validator.validate(ROOT)
    assert result["source_rows"] == 3020
    assert result["known_action_affected_rows"] == 1
    assert result["formal_use_allowed"] is False


def test_share_unit_artifact_exact_lf_checkout_contract() -> None:
    prefix = "output/research/pullback_short_reclaim/pullback_short_reclaim_share_unit_reconciliation_v1_"
    observed = [line.strip() for line in (ROOT / ".gitattributes").read_text(encoding="utf-8").splitlines()
                if line.startswith(prefix)]
    expected = [prefix + suffix + " text eol=lf" for suffix in ("detail.csv", "summary.csv", "manifest.json")]
    assert len(observed) == 3
    assert set(observed) == set(expected)
