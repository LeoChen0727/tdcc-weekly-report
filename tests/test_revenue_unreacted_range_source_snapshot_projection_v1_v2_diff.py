from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_source_snapshot_projection_v1_v2_diff import (  # noqa: E402
    DETAIL_COLUMNS,
    SUMMARY_COLUMNS,
    build_diff_from_paths,
    write_diff_artifacts,
)
import revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as producer  # noqa: E402
import validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as validator  # noqa: E402


EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION = (
    "corrected_official_cutoff_price_gated_episode_membership"
)
EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS = {
    "qualifying_canonical_source_table_dates",
    "qualifying_revenue_periods",
    "qualifying_source_dates",
    "qualifying_source_row_canonical_sha256s",
    "qualifying_cross_market_resolution_ids",
    "qualifying_update_count",
    "latest_qualifying_canonical_source_table_date",
    "latest_qualifying_revenue_period",
    "latest_qualifying_source_date",
    "latest_qualifying_source_row_canonical_sha256",
    "qualifying_source_revenue_anomaly_candidate_flag",
}
EXPECTED_CUTOFF_REVENUE_CAUSAL_INVARIANT_FIELDS = {
    "cutoff_revenue_subset_row_count",
    "cutoff_revenue_subset_semantic_sha256",
}
EXPECTED_MONTHLY_RESOLUTION_CAUSAL_INVARIANT_FIELDS = {
    "cross_market_resolution_registry_canonical_sha256",
    "applied_monthly_resolution_count",
    "applied_monthly_resolution_ids",
    "applied_monthly_resolution_semantic_sha256",
}


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _manifest_row(*, version: int, v1_manifest_sha: str = "", v1_detail_sha: str = "") -> dict[str, object]:
    is_v2 = version == 2
    row: dict[str, object] = {
        "generated_at": f"2026-08-22 0{version}:00:00 Asia/Taipei",
        "model_id": "revenue_unreacted_range",
        "artifact_id": "revenue_unreacted_range_source_snapshot_projection",
        "artifact_version": (
            "source_snapshot_projection_v2_20260822"
            if is_v2
            else "source_snapshot_projection_v1_20260731"
        ),
        "projection_id": "revenue_unreacted_range_source_snapshot_asof_20260713",
        "projection_version": (
            "source_snapshot_projection_v2_20260822"
            if is_v2
            else "source_snapshot_projection_v1_20260731"
        ),
        "projection_policy_id": (
            "raw_source_and_corrected_official_price_truncated_before_source_first_episode_assembly_v2"
            if is_v2
            else "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
        ),
        "cutoff_date": "20260713",
        "full_source_artifact_id": "revenue_unreacted_range_source_first_condition_audit",
        "full_source_artifact_version": "source_first_condition_v3_20260720",
        "full_source_episode_row_count": 4 if is_v2 else 3,
        "full_source_episode_semantic_sha256": ("2" if is_v2 else "1") * 64,
        "monthly_revenue_history_blob_sha256": ("4" if is_v2 else "3") * 64,
        "monthly_revenue_canonical_table_sha256": ("6" if is_v2 else "5") * 64,
        "cross_market_resolution_registry_canonical_sha256": "7" * 64,
        "cutoff_revenue_subset_row_count": 2,
        "cutoff_revenue_subset_semantic_sha256": "8" * 64,
        "cutoff_price_input_stock_count": 2,
        "cutoff_price_input_row_count": 5 if is_v2 else 4,
        "cutoff_price_input_file_semantic_sha256s": (
            (
                f"1111:3:{'b' * 64}|3333:2:{'d' * 64}"
                if is_v2
                else f"1111:2:{'a' * 64}|2222:2:{'c' * 64}"
            )
        ),
        "cutoff_price_input_semantic_sha256": ("d" if is_v2 else "c") * 64,
        "applied_monthly_resolution_count": 0,
        "applied_monthly_resolution_ids": "none",
        "applied_monthly_resolution_semantic_sha256": "e" * 64,
        "applied_price_resolution_count": 0,
        "applied_price_resolution_ids": "none",
        "applied_price_resolution_semantic_sha256": "f" * 64,
        "projected_episode_row_count": 2,
        "projected_episode_semantic_sha256": ("1" if is_v2 else "0") * 64,
        "projected_max_source_date": "20260617",
        "projected_max_trade_date": "20260629",
        "projected_max_episode_end_date": "20260713",
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
    }
    if is_v2:
        row.update(
            {
                "predecessor_projection_version": "source_snapshot_projection_v1_20260731",
                "predecessor_manifest_bytes_sha256": v1_manifest_sha,
                "predecessor_detail_bytes_sha256": v1_detail_sha,
                "lineage_change_reason": (
                    "corrected_official_pre_cutoff_price_history_lineage_rebaseline_20260822"
                ),
                "candidate_status": "generated_pending_supersede_approval",
            }
        )
    return row


def _write_projection_pair(tmp_path: Path) -> dict[str, Path]:
    tmp_path.mkdir(parents=True, exist_ok=True)
    paths = {
        "v1_manifest": tmp_path / "v1_manifest.csv",
        "v1_detail": tmp_path / "v1_detail.csv",
        "v2_manifest": tmp_path / "v2_manifest.csv",
        "v2_detail": tmp_path / "v2_detail.csv",
        "summary": tmp_path / "diff_summary.csv",
        "detail": tmp_path / "diff_detail.csv",
    }
    v1_detail = pd.DataFrame(
        [
            {
                "generated_at": "old",
                "monthly_revenue_history_blob_sha256": "3" * 64,
                "episode_key": "e1",
                "stock_id": "1111",
                "source_close": "10",
            },
            {
                "generated_at": "old",
                "monthly_revenue_history_blob_sha256": "3" * 64,
                "episode_key": "e2",
                "stock_id": "2222",
                "source_close": "20",
            },
        ]
    )
    v1_manifest = pd.DataFrame([_manifest_row(version=1)])
    v1_manifest.to_csv(paths["v1_manifest"], index=False)
    v1_detail.to_csv(paths["v1_detail"], index=False)
    v2_detail = pd.DataFrame(
        [
            {
                "generated_at": "new",
                "monthly_revenue_history_blob_sha256": "4" * 64,
                "episode_key": "e1",
                "stock_id": "1111",
                "source_close": "11",
            },
            {
                "generated_at": "new",
                "monthly_revenue_history_blob_sha256": "4" * 64,
                "episode_key": "e3",
                "stock_id": "3333",
                "source_close": "30",
            },
        ]
    )
    v2_manifest = pd.DataFrame(
        [
            _manifest_row(
                version=2,
                v1_manifest_sha=_sha(paths["v1_manifest"].read_bytes()),
                v1_detail_sha=_sha(paths["v1_detail"].read_bytes()),
            )
        ]
    )
    v2_manifest.to_csv(paths["v2_manifest"], index=False)
    v2_detail.to_csv(paths["v2_detail"], index=False)
    return paths


def _build_and_write(paths: dict[str, Path]) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary, detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
        generated_at="2026-08-22 03:00:00 Asia/Taipei",
    )
    write_diff_artifacts(
        summary,
        detail,
        summary_path=paths["summary"],
        detail_path=paths["detail"],
    )
    return summary, detail


def _validate(paths: dict[str, Path]) -> list[str]:
    return validator.validate(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
        summary_path=paths["summary"],
        detail_path=paths["detail"],
        expected_v1_manifest_bytes=paths["v1_manifest"].stat().st_size,
        expected_v1_manifest_sha256=_sha(paths["v1_manifest"].read_bytes()),
        expected_v1_detail_bytes=paths["v1_detail"].stat().st_size,
        expected_v1_detail_sha256=_sha(paths["v1_detail"].read_bytes()),
        expected_v1_detail_row_count=len(
            pd.read_csv(paths["v1_detail"], dtype=str, keep_default_na=False)
        ),
    )


def _write_price_gated_membership_pair(tmp_path: Path) -> dict[str, Path]:
    paths = _write_projection_pair(tmp_path)
    v1_detail = pd.read_csv(paths["v1_detail"], dtype=str, keep_default_na=False)
    v2_detail = pd.read_csv(paths["v2_detail"], dtype=str, keep_default_na=False)
    v2_detail.loc[v2_detail["episode_key"].eq("e1"), "source_close"] = "10"
    for index, column in enumerate(
        sorted(EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS),
        start=1,
    ):
        v1_detail[column] = "unchanged_removed_episode"
        v2_detail[column] = "unchanged_added_episode"
        if column == "qualifying_update_count":
            old_value, new_value = "1", "2"
        elif column == "qualifying_source_revenue_anomaly_candidate_flag":
            old_value, new_value = "false", "true"
        else:
            old_value, new_value = f"old_membership_{index}", f"new_membership_{index}"
        v1_detail.loc[v1_detail["episode_key"].eq("e1"), column] = old_value
        v2_detail.loc[v2_detail["episode_key"].eq("e1"), column] = new_value
    v1_detail.to_csv(paths["v1_detail"], index=False)
    v2_detail.to_csv(paths["v2_detail"], index=False)
    v2_manifest = pd.read_csv(
        paths["v2_manifest"], dtype=str, keep_default_na=False
    )
    v2_manifest.loc[0, "predecessor_detail_bytes_sha256"] = _sha(
        paths["v1_detail"].read_bytes()
    )
    v2_manifest.to_csv(paths["v2_manifest"], index=False)
    return paths


def _unclassified_diagnostic_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    summary_row = {column: "" for column in SUMMARY_COLUMNS}
    summary_row["unclassified_semantic_drift_count"] = 2
    summary = pd.DataFrame([summary_row], columns=list(SUMMARY_COLUMNS))
    detail = pd.DataFrame(
        [
            {
                "drift_id": "d2",
                "drift_scope": "manifest",
                "identity_key": "projection",
                "column_name": "cutoff_revenue_subset_semantic_sha256",
                "v1_value": "a",
                "v2_value": "b",
                "change_type": "changed",
                "classification": "unclassified_semantic_drift",
                "source_evidence": (
                    "immutable cutoff/revenue/resolution/formal-use contract changed"
                ),
            },
            {
                "drift_id": "d1",
                "drift_scope": "episode",
                "identity_key": 'e1"\nforged=1',
                "column_name": "stock_id",
                "v1_value": "1111",
                "v2_value": "9999",
                "change_type": "changed",
                "classification": "unclassified_semantic_drift",
                "source_evidence": "non-price episode field changed",
            },
        ],
        columns=list(DETAIL_COLUMNS),
    )
    return summary, detail


def test_v1_v2_diff_is_deterministic_classified_and_independently_validated(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    paths = _write_projection_pair(tmp_path)
    summary, detail = _build_and_write(paths)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
    row = summary.iloc[0]
    assert list(summary.columns) == list(SUMMARY_COLUMNS)
    assert list(detail.columns) == list(DETAIL_COLUMNS)
    assert row["added_episode_count"] == 1
    assert row["removed_episode_count"] == 1
    assert row["changed_episode_count"] == 1
    assert row["changed_columns"] == "source_close"
    assert row["cutoff_price_input_changed_stock_count"] == 3
    assert row["unclassified_semantic_drift_count"] == 0
    assert set(detail["classification"]) <= {
        "authorized_v2_candidate_metadata",
        "current_full_source_capture_refresh",
        "corrected_official_cutoff_price_lineage",
    }
    assert _validate(paths) == []

    repeated_summary, repeated_detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
        generated_at="2026-08-22 03:00:00 Asia/Taipei",
    )
    pd.testing.assert_frame_equal(repeated_summary, summary)
    pd.testing.assert_frame_equal(repeated_detail, detail)


def test_unclassified_drift_reports_every_row_before_zero_write_side_effects(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    summary, detail = _unclassified_diagnostic_frames()
    summary_path = tmp_path / "missing-summary-parent" / "diff_summary.csv"
    detail_path = tmp_path / "missing-detail-parent" / "diff_detail.csv"
    mkdir_calls: list[Path] = []
    to_csv_calls: list[object] = []

    def record_mkdir(path: Path, *args: object, **kwargs: object) -> None:
        mkdir_calls.append(path)

    def record_to_csv(
        frame: pd.DataFrame,
        *args: object,
        **kwargs: object,
    ) -> None:
        to_csv_calls.append(frame)

    monkeypatch.setattr(Path, "mkdir", record_mkdir)
    monkeypatch.setattr(pd.DataFrame, "to_csv", record_to_csv)

    with pytest.raises(RuntimeError, match="unclassified semantic drift"):
        write_diff_artifacts(
            summary,
            detail,
            summary_path=summary_path,
            detail_path=detail_path,
        )

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == (
        "v1_v2_diff_unclassified_semantic_drift_count=2\n"
        "v1_v2_diff_unclassified_semantic_drift_row="
        '{"change_type":"changed","classification":"unclassified_semantic_drift",'
        '"column_name":"stock_id","drift_scope":"episode",'
        '"identity_key":"e1\\\"\\nforged=1",'
        '"source_evidence":"non-price episode field changed"}\n'
        "v1_v2_diff_unclassified_semantic_drift_row="
        '{"change_type":"changed","classification":"unclassified_semantic_drift",'
        '"column_name":"cutoff_revenue_subset_semantic_sha256",'
        '"drift_scope":"manifest","identity_key":"projection",'
        '"source_evidence":"immutable cutoff/revenue/resolution/formal-use contract changed"}\n'
    )
    assert len(captured.err.splitlines()) == 3
    assert mkdir_calls == []
    assert to_csv_calls == []
    assert not summary_path.parent.exists()
    assert not detail_path.parent.exists()
    assert not summary_path.exists()
    assert not detail_path.exists()


def test_diff_writer_rejects_unclassified_episode_or_manifest_drift(
    tmp_path: Path,
) -> None:
    paths = _write_projection_pair(tmp_path)
    v2_detail = pd.read_csv(paths["v2_detail"], dtype=str, keep_default_na=False)
    v2_detail.loc[v2_detail["episode_key"].eq("e1"), "stock_id"] = "9999"
    v2_detail.to_csv(paths["v2_detail"], index=False)
    summary, detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
    )
    assert summary.iloc[0]["unclassified_semantic_drift_count"] >= 1
    assert "unclassified_semantic_drift" in set(detail["classification"])
    with pytest.raises(RuntimeError, match="unclassified semantic drift"):
        write_diff_artifacts(summary, detail)

    paths = _write_projection_pair(tmp_path / "manifest")
    v2_manifest = pd.read_csv(paths["v2_manifest"], dtype=str, keep_default_na=False)
    v2_manifest.loc[0, "cutoff_revenue_subset_semantic_sha256"] = "9" * 64
    v2_manifest.to_csv(paths["v2_manifest"], index=False)
    summary, detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
    )
    assert summary.iloc[0]["unclassified_semantic_drift_count"] == 1
    with pytest.raises(RuntimeError, match="unclassified semantic drift"):
        write_diff_artifacts(summary, detail)


def test_price_derived_episode_change_requires_that_stock_lineage_to_change(
    tmp_path: Path,
) -> None:
    paths = _write_projection_pair(tmp_path)
    v1_manifest = pd.read_csv(paths["v1_manifest"], dtype=str, keep_default_na=False)
    v2_manifest = pd.read_csv(paths["v2_manifest"], dtype=str, keep_default_na=False)
    v1_tokens = v1_manifest.loc[0, "cutoff_price_input_file_semantic_sha256s"].split("|")
    v2_tokens = v2_manifest.loc[0, "cutoff_price_input_file_semantic_sha256s"].split("|")
    v2_tokens[0] = v1_tokens[0]
    v2_manifest.loc[0, "cutoff_price_input_file_semantic_sha256s"] = "|".join(v2_tokens)
    v2_manifest.to_csv(paths["v2_manifest"], index=False)

    summary, detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
    )

    source_close = detail.loc[
        detail["identity_key"].eq("e1") & detail["column_name"].eq("source_close")
    ].iloc[0]
    assert source_close["classification"] == "unclassified_semantic_drift"
    assert summary.iloc[0]["unclassified_semantic_drift_count"] == 1
    with pytest.raises(RuntimeError, match="unclassified semantic drift"):
        write_diff_artifacts(summary, detail)


def test_price_gated_membership_allowlist_and_invariants_are_exact_and_independent() -> None:
    assert producer.CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION == (
        EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION
    )
    assert validator.CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION == (
        EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION
    )
    assert producer.CAUSAL_EPISODE_MEMBERSHIP_FIELDS == (
        EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS
    )
    assert validator.CAUSAL_EPISODE_MEMBERSHIP_FIELDS == (
        EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS
    )
    assert set(producer.CUTOFF_REVENUE_CAUSAL_INVARIANT_FIELDS) == (
        EXPECTED_CUTOFF_REVENUE_CAUSAL_INVARIANT_FIELDS
    )
    assert set(validator.CUTOFF_REVENUE_CAUSAL_INVARIANT_FIELDS) == (
        EXPECTED_CUTOFF_REVENUE_CAUSAL_INVARIANT_FIELDS
    )
    assert set(producer.MONTHLY_RESOLUTION_CAUSAL_INVARIANT_FIELDS) == (
        EXPECTED_MONTHLY_RESOLUTION_CAUSAL_INVARIANT_FIELDS
    )
    assert set(validator.MONTHLY_RESOLUTION_CAUSAL_INVARIANT_FIELDS) == (
        EXPECTED_MONTHLY_RESOLUTION_CAUSAL_INVARIANT_FIELDS
    )


@pytest.mark.parametrize(
    "mutation",
    (
        "manifest_scope",
        "other_column",
        "added_change_type",
        "missing_v1_descriptor",
        "missing_v2_descriptor",
        "missing_cutoff_invariant",
        "empty_cutoff_invariant",
        "missing_monthly_invariant",
        "empty_monthly_invariant",
    ),
)
def test_price_gated_membership_predicate_rejects_every_incomplete_condition(
    mutation: str,
) -> None:
    manifest_values = {
        "cutoff_revenue_subset_row_count": "2",
        "cutoff_revenue_subset_semantic_sha256": "8" * 64,
        "cross_market_resolution_registry_canonical_sha256": "7" * 64,
        "applied_monthly_resolution_count": "0",
        "applied_monthly_resolution_ids": "none",
        "applied_monthly_resolution_semantic_sha256": "e" * 64,
    }
    v1_manifest = pd.Series(manifest_values)
    v2_manifest = pd.Series(manifest_values)
    v1_price = {"1111": (2, "a" * 64)}
    v2_price = {"1111": (3, "b" * 64)}
    column = "qualifying_source_dates"
    change_type = "changed"
    drift_scope = "episode"
    if mutation == "manifest_scope":
        drift_scope = "manifest"
    elif mutation == "other_column":
        column = "stock_name"
    elif mutation == "added_change_type":
        change_type = "added"
    elif mutation == "missing_v1_descriptor":
        v1_price = {}
    elif mutation == "missing_v2_descriptor":
        v2_price = {}
    elif mutation == "missing_cutoff_invariant":
        v2_manifest = v2_manifest.drop("cutoff_revenue_subset_row_count")
    elif mutation == "empty_cutoff_invariant":
        v2_manifest.loc["cutoff_revenue_subset_row_count"] = ""
    elif mutation == "missing_monthly_invariant":
        v2_manifest = v2_manifest.drop(
            "applied_monthly_resolution_semantic_sha256"
        )
    else:
        v2_manifest.loc["applied_monthly_resolution_semantic_sha256"] = ""

    for module in (producer, validator):
        classification, _evidence = module._episode_membership_classification(
            drift_scope=drift_scope,
            column=column,
            change_type=change_type,
            stock_id="1111",
            v1_price=v1_price,
            v2_price=v2_price,
            v1_manifest_row=v1_manifest,
            v2_manifest_row=v2_manifest,
        )
        assert classification == "unclassified_semantic_drift"
    assert producer._manifest_classification(column, False)[0] == (
        "unclassified_semantic_drift"
    )
    assert validator._classification(column)[0] == "unclassified_semantic_drift"


def test_price_gated_membership_exact11_is_causally_classified_and_validated(
    tmp_path: Path,
) -> None:
    paths = _write_price_gated_membership_pair(tmp_path)
    summary, detail = _build_and_write(paths)
    membership = detail.loc[
        detail["identity_key"].eq("e1")
        & detail["column_name"].isin(EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS)
    ].copy()

    assert set(membership["column_name"]) == EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS
    assert len(membership) == 11
    assert set(membership["drift_scope"]) == {"episode"}
    assert set(membership["change_type"]) == {"changed"}
    assert set(membership["classification"]) == {
        EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION
    }
    assert membership["source_evidence"].str.contains(
        "drift_scope=episode", regex=False
    ).all()
    assert membership["source_evidence"].str.contains(
        "cutoff_price_descriptor_changed=true", regex=False
    ).all()
    assert membership["source_evidence"].str.contains(
        "cutoff_revenue_invariants_equal=true", regex=False
    ).all()
    assert membership["source_evidence"].str.contains(
        "monthly_resolution_invariants_equal=true", regex=False
    ).all()
    assert summary.iloc[0]["unclassified_semantic_drift_count"] == 0
    assert _validate(paths) == []

    tampered = pd.read_csv(paths["detail"], dtype=str, keep_default_na=False)
    target = tampered["classification"].eq(
        EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_CLASSIFICATION
    )
    tampered.loc[target, "classification"] = "corrected_official_cutoff_price_lineage"
    tampered.to_csv(paths["detail"], index=False)
    assert any("independent reconstruction" in error for error in _validate(paths))


@pytest.mark.parametrize(
    ("mutation", "evidence_token"),
    (
        ("unchanged_descriptor", "cutoff_price_lineage:"),
        ("cutoff_revenue_drift", "cutoff_revenue_invariants_equal=false"),
        ("monthly_resolution_drift", "monthly_resolution_invariants_equal=false"),
    ),
)
def test_price_gated_membership_fails_closed_without_complete_causal_evidence(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    mutation: str,
    evidence_token: str,
) -> None:
    paths = _write_price_gated_membership_pair(tmp_path / mutation)
    v1_manifest = pd.read_csv(paths["v1_manifest"], dtype=str, keep_default_na=False)
    v2_manifest = pd.read_csv(paths["v2_manifest"], dtype=str, keep_default_na=False)
    if mutation == "unchanged_descriptor":
        v1_token = str(
            v1_manifest.loc[0, "cutoff_price_input_file_semantic_sha256s"]
        ).split("|")[0]
        v2_tokens = str(
            v2_manifest.loc[0, "cutoff_price_input_file_semantic_sha256s"]
        ).split("|")
        v2_tokens[0] = v1_token
        v2_manifest.loc[0, "cutoff_price_input_file_semantic_sha256s"] = "|".join(
            v2_tokens
        )
    elif mutation == "cutoff_revenue_drift":
        v2_manifest.loc[0, "cutoff_revenue_subset_semantic_sha256"] = "9" * 64
    else:
        v2_manifest.loc[0, "applied_monthly_resolution_semantic_sha256"] = "9" * 64
    v2_manifest.to_csv(paths["v2_manifest"], index=False)

    summary, detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
    )
    membership = detail.loc[
        detail["identity_key"].eq("e1")
        & detail["column_name"].isin(EXPECTED_CAUSAL_EPISODE_MEMBERSHIP_FIELDS)
    ]
    assert len(membership) == 11
    assert set(membership["classification"]) == {"unclassified_semantic_drift"}
    assert membership["source_evidence"].str.contains(
        evidence_token, regex=False
    ).all()
    assert int(summary.iloc[0]["unclassified_semantic_drift_count"]) >= 11

    blocked_summary = tmp_path / mutation / "blocked" / "summary.csv"
    blocked_detail = tmp_path / mutation / "blocked" / "detail.csv"
    with pytest.raises(RuntimeError, match="unclassified semantic drift"):
        write_diff_artifacts(
            summary,
            detail,
            summary_path=blocked_summary,
            detail_path=blocked_detail,
        )
    assert "v1_v2_diff_unclassified_semantic_drift_count=" in capsys.readouterr().err
    assert not blocked_summary.parent.exists()
    assert not blocked_summary.exists()
    assert not blocked_detail.exists()


def test_nonallowlisted_nonprice_field_stays_unclassified_with_price_change(
    tmp_path: Path,
) -> None:
    paths = _write_price_gated_membership_pair(tmp_path)
    v1_detail = pd.read_csv(paths["v1_detail"], dtype=str, keep_default_na=False)
    v2_detail = pd.read_csv(paths["v2_detail"], dtype=str, keep_default_na=False)
    v1_detail["stock_name"] = "unchanged"
    v2_detail["stock_name"] = "unchanged"
    v1_detail.loc[v1_detail["episode_key"].eq("e1"), "stock_name"] = "old name"
    v2_detail.loc[v2_detail["episode_key"].eq("e1"), "stock_name"] = "new name"
    v1_detail.to_csv(paths["v1_detail"], index=False)
    v2_detail.to_csv(paths["v2_detail"], index=False)
    v2_manifest = pd.read_csv(paths["v2_manifest"], dtype=str, keep_default_na=False)
    v2_manifest.loc[0, "predecessor_detail_bytes_sha256"] = _sha(
        paths["v1_detail"].read_bytes()
    )
    v2_manifest.to_csv(paths["v2_manifest"], index=False)

    summary, detail = build_diff_from_paths(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
    )
    row = detail.loc[
        detail["identity_key"].eq("e1") & detail["column_name"].eq("stock_name")
    ].iloc[0]
    assert row["classification"] == "unclassified_semantic_drift"
    assert row["source_evidence"] == "non-price episode field changed"
    assert int(summary.iloc[0]["unclassified_semantic_drift_count"]) == 1

def test_independent_validator_rejects_tampered_diff_and_predecessor(
    tmp_path: Path,
) -> None:
    paths = _write_projection_pair(tmp_path)
    _build_and_write(paths)
    detail = pd.read_csv(paths["detail"], dtype=str, keep_default_na=False)
    detail.loc[0, "classification"] = "tampered_classification"
    detail.to_csv(paths["detail"], index=False)
    assert any("independent reconstruction" in error for error in _validate(paths))

    paths = _write_projection_pair(tmp_path / "predecessor")
    v2_manifest = pd.read_csv(paths["v2_manifest"], dtype=str, keep_default_na=False)
    v2_manifest.loc[0, "predecessor_detail_bytes_sha256"] = "0" * 64
    v2_manifest.to_csv(paths["v2_manifest"], index=False)
    with pytest.raises(RuntimeError, match="predecessor detail"):
        build_diff_from_paths(
            v1_manifest_path=paths["v1_manifest"],
            v1_detail_path=paths["v1_detail"],
            v2_manifest_path=paths["v2_manifest"],
            v2_detail_path=paths["v2_detail"],
        )


def test_independent_validator_rejects_summary_byte_and_formal_flag_tamper(
    tmp_path: Path,
) -> None:
    paths = _write_projection_pair(tmp_path)
    _build_and_write(paths)
    summary = pd.read_csv(paths["summary"], dtype=str, keep_default_na=False)
    summary.loc[0, "v2_detail_sha256"] = "0" * 64
    summary.loc[0, "formal_model_use_allowed"] = "true"
    summary.to_csv(paths["summary"], index=False)
    errors = _validate(paths)
    assert "diff summary v2_detail SHA-256 mismatch" in errors
    assert "v1/v2 diff formal_model_use_allowed must be false" in errors


def test_validator_defaults_pin_the_approved_immutable_v1_bytes(
    tmp_path: Path,
) -> None:
    paths = _write_projection_pair(tmp_path)
    _build_and_write(paths)

    errors = validator.validate(
        v1_manifest_path=paths["v1_manifest"],
        v1_detail_path=paths["v1_detail"],
        v2_manifest_path=paths["v2_manifest"],
        v2_detail_path=paths["v2_detail"],
        summary_path=paths["summary"],
        detail_path=paths["detail"],
    )

    assert any("immutable v1 manifest bytes mismatch" in error for error in errors)
    assert any("immutable v1 manifest SHA-256 mismatch" in error for error in errors)
    assert any("immutable v1 detail bytes mismatch" in error for error in errors)
    assert any("immutable v1 detail SHA-256 mismatch" in error for error in errors)
    assert any("immutable v1 detail row count mismatch" in error for error in errors)
