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
import validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as validator  # noqa: E402


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


def test_v1_v2_diff_is_deterministic_classified_and_independently_validated(
    tmp_path: Path,
) -> None:
    paths = _write_projection_pair(tmp_path)
    summary, detail = _build_and_write(paths)
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
