from __future__ import annotations

import hashlib
import io
import sys
import subprocess
from decimal import Decimal
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_volume_v2_warrant_lineage_history_audit as builder  # noqa: E402
import validate_volume_v2_warrant_lineage_history_audit as validator  # noqa: E402


def test_canonical_text_sha_is_bom_and_line_ending_independent() -> None:
    lf = "欄位,值\n股票,2330\n".encode("utf-8")
    crlf_with_bom = b"\xef\xbb\xbf" + lf.replace(b"\n", b"\r\n")

    assert builder.sha256_bytes(lf) == builder.sha256_bytes(crlf_with_bom)
    assert validator.sha256_bytes(lf) == validator.sha256_bytes(crlf_with_bom)
    assert builder.sha256_bytes(lf) == validator.sha256_bytes(lf)
    assert not builder.manifest_v1_sha256_candidates(
        lf
    ) & builder.manifest_v1_sha256_candidates(crlf_with_bom)
    assert not validator.manifest_v1_sha256_candidates(
        lf
    ) & validator.manifest_v1_sha256_candidates(crlf_with_bom)


@pytest.mark.parametrize(
    "present_revision_columns",
    [
        ("snapshot_revision",),
        ("supersedes_snapshot_sha256",),
        ("revision_reason",),
        ("snapshot_revision", "supersedes_snapshot_sha256"),
        ("snapshot_revision", "revision_reason"),
        ("supersedes_snapshot_sha256", "revision_reason"),
    ],
)
def test_volume_builder_and_independent_validator_reject_partial_revision_schema(
    tmp_path: Path,
    present_revision_columns: tuple[str, ...],
) -> None:
    revision_values = {
        "snapshot_revision": "r1",
        "supersedes_snapshot_sha256": "",
        "revision_reason": "legacy_v1_manifest",
    }
    row = {
        "snapshot_report_date": "20260717",
        "artifact_id": "model_signals_for_report",
        "snapshot_sha256": "1" * 64,
    }
    row.update(
        {column: revision_values[column] for column in present_revision_columns}
    )
    manifest = pd.DataFrame([row])
    payload = manifest.to_csv(index=False, lineterminator="\n").encode("utf-8")

    with pytest.raises(RuntimeError, match="partial revision schema"):
        builder.validated_revision_manifest_rows(manifest)
    with pytest.raises(RuntimeError, match="partial revision schema"):
        builder.normalized_manifest_identity_frame(payload, "builder-history.csv")
    with pytest.raises(RuntimeError, match="partial revision schema"):
        validator.expected_audit_sources(tmp_path, manifest)
    with pytest.raises(RuntimeError, match="partial revision schema"):
        validator.independent_normalized_manifest_identity_frame(
            payload,
            "validator-history.csv",
        )


def test_volume_builder_and_independent_validator_reject_blank_modern_revision(
    tmp_path: Path,
) -> None:
    manifest = pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260717",
                "artifact_id": "model_signals_for_report",
                "snapshot_revision": "",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "modern_schema_must_not_default_to_r1",
                "snapshot_sha256": "1" * 64,
            }
        ]
    )
    payload = manifest.to_csv(index=False, lineterminator="\n").encode("utf-8")

    with pytest.raises(RuntimeError, match="snapshot_revision must not be blank"):
        builder.validated_revision_manifest_rows(manifest)
    with pytest.raises(RuntimeError, match="snapshot_revision must not be blank"):
        builder.normalized_manifest_identity_frame(payload, "builder-history.csv")
    with pytest.raises(RuntimeError, match="snapshot_revision must not be blank"):
        validator.expected_audit_sources(tmp_path, manifest)
    with pytest.raises(RuntimeError, match="snapshot_revision must not be blank"):
        validator.independent_normalized_manifest_identity_frame(
            payload,
            "validator-history.csv",
        )


def _git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout.strip()


def _manifest_v1_sha256(payload: bytes) -> str:
    normalized = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _formal_frame(report_date: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "signal_date": report_date,
                "report_line": "mainstream",
                "model_id": "volume_range_breakout_v2_high_position_volume_attack",
                "stock_id": "2330",
                "source_row_index": "volume_breakout:0",
                "warrant_flow_signal": "",
                "base_model_score": "50.0",
                "operation_score": "0.0",
                "tdcc_score": "0.0",
                "pattern_score": "0.0",
                "risk_penalty": "0.0",
                "final_rank_score": "50.0",
                "model_rank": "1",
            }
        ]
    )


def _non_volume_formal_frame(report_date: str) -> pd.DataFrame:
    row = _formal_frame(report_date).iloc[0].copy()
    row["model_id"] = "non_volume_test_model"
    row["source_row_index"] = "non_volume:0"
    return pd.DataFrame([row])


def _write_current_sources(
    root: Path,
    report_date: str,
    *,
    watch_score: str = "1",
    candidate_score: str = "1",
    watch_rank: str = "1",
    candidate_rank: str = "1",
) -> None:
    latest = root / "output" / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    _formal_frame(report_date).to_csv(
        latest / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
        lineterminator="\n",
    )
    pd.DataFrame(
        [
            {
                "signal_date": report_date,
                "stock_id": "2330",
                "warrant_flow_signal": "",
                "score": watch_score,
                "rank": watch_rank,
                "tdcc_status": "",
                "false_breakout_risk": "False",
            }
        ]
    ).to_csv(
        latest / "volume_breakout_watch_latest.csv",
        index=False,
        lineterminator="\n",
    )
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "warrant_flow_signal": "",
                "score": candidate_score,
                "rank": candidate_rank,
            }
        ]
    ).to_csv(latest / "all_candidates_latest.csv", index=False, lineterminator="\n")
    pd.DataFrame([{"stock_id": "2330", "warrant_flow_signal": ""}]).to_csv(
        latest / "warrant_flow_latest.csv",
        index=False,
        lineterminator="\n",
    )


def _write_non_volume_current_sources(root: Path, report_date: str) -> None:
    _write_current_sources(root, report_date)
    _non_volume_formal_frame(report_date).to_csv(
        root / builder.FORMAL_SOURCE_PATH,
        index=False,
        lineterminator="\n",
    )


def _manifest_row(
    root: Path,
    report_date: str,
    *,
    snapshot_path: str = "",
    snapshot_revision: str | None = None,
    supersedes_snapshot_sha256: str = "",
    revision_reason: str = "",
) -> dict[str, str]:
    snapshot_path = snapshot_path or (
        "output/history/daily_model_snapshots/"
        f"daily_candidate_model_signals_for_report_{report_date}.csv"
    )
    payload = (root / snapshot_path).read_bytes()
    row = {
        "snapshot_report_date": report_date,
        "pipeline_commit_sha": "0" * 40,
        "artifact_id": "model_signals_for_report",
        "source_path": builder.FORMAL_SOURCE_PATH,
        "snapshot_path": snapshot_path,
        "snapshot_sha256": _manifest_v1_sha256(payload),
        "row_count": "1",
    }
    if snapshot_revision is not None:
        row.update(
            {
                "snapshot_revision": snapshot_revision,
                "supersedes_snapshot_sha256": supersedes_snapshot_sha256,
                "revision_reason": revision_reason,
            }
        )
    return row


def _setup_dynamic_repo(
    root: Path,
    *,
    current_watch_score: str = "1",
    current_candidate_score: str = "1",
    current_watch_rank: str = "1",
    current_candidate_rank: str = "1",
    explicit_candidate_allowlist: bool = False,
) -> None:
    (root / "scripts").mkdir(parents=True)
    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    production_source = (
        "def append_volume_breakout_signals():\n"
        "    score_source = {field: candidate_values[field] for field in candidate_fields}\n"
        "    score_source.update({field: watch_values[field] for field in watch_fields})\n"
        "    score_source['warrant_flow_signal'] = authoritative_warrant_signal\n"
        if explicit_candidate_allowlist
        else "def append_volume_breakout_signals():\n"
        "    score_source = {}\n"
        "    score_source.update(row.to_dict())\n"
        "    score_source['warrant_flow_signal'] = authoritative_warrant_signal\n"
    )
    (root / builder.PRODUCTION_CODE_PATH).write_text(
        production_source,
        encoding="utf-8",
        newline="\n",
    )
    _write_current_sources(root, "20260717")
    _formal_frame("20260717").to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260717.csv",
        index=False,
        lineterminator="\n",
    )
    pd.DataFrame([_manifest_row(root, "20260717")]).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv",
        index=False,
        lineterminator="\n",
    )
    _git(root, "init")
    _git(root, "config", "user.name", "test")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "core.autocrlf", "false")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "historical snapshot")
    _write_current_sources(
        root,
        "20260718",
        watch_score=current_watch_score,
        candidate_score=current_candidate_score,
        watch_rank=current_watch_rank,
        candidate_rank=current_candidate_rank,
    )


def _setup_zero_volume_manifest_repo(root: Path) -> None:
    (root / "scripts").mkdir(parents=True)
    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    (root / builder.PRODUCTION_CODE_PATH).write_text(
        "def append_volume_breakout_signals():\n"
        "    score_source = {}\n"
        "    score_source.update(row.to_dict())\n"
        "    score_source['warrant_flow_signal'] = authoritative_warrant_signal\n",
        encoding="utf-8",
        newline="\n",
    )
    _write_non_volume_current_sources(root, "20260717")
    snapshot_path = (
        snapshot_dir / "daily_candidate_model_signals_for_report_20260717.csv"
    )
    snapshot_path.write_bytes((root / builder.FORMAL_SOURCE_PATH).read_bytes())
    pd.DataFrame([_manifest_row(root, "20260717")]).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv",
        index=False,
        lineterminator="\n",
    )
    _git(root, "init")
    _git(root, "config", "user.name", "test")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "core.autocrlf", "false")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "zero-volume historical snapshot")


def _validate_generated_audit(root: Path, audit: pd.DataFrame, target: Path) -> None:
    csv_path = target / "audit.csv"
    md_path = target / "audit.md"
    docs_csv_path = target / "audit-docs.csv"
    docs_md_path = target / "audit-docs.md"
    builder.write_audit_artifacts(
        audit,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )
    assert validator.validate(
        root,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    ) == []


def _formal_audit_rows(audit: pd.DataFrame) -> pd.DataFrame:
    return audit[audit["audit_row_type"].eq("formal_row")]


def _coverage_audit_rows(audit: pd.DataFrame) -> pd.DataFrame:
    return audit[audit["audit_row_type"].eq("revision_coverage")]


def test_same_date_line_ending_only_reuses_max_manifest_revision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    snapshot_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_candidate_model_signals_for_report_20260717.csv"
    )
    payload = snapshot_path.read_bytes().replace(b"\r\n", b"\n")
    (root / builder.FORMAL_SOURCE_PATH).write_bytes(
        payload.replace(b"\n", b"\r\n")
    )

    sources = builder.build_audit_sources(root, builder.manifest_rows(root))
    same_day = [source for source in sources if source["report_date"] == "20260717"]
    assert [source["snapshot_revision"] for source in same_day] == ["r1"]


def test_zero_to_has_volume_rows_creates_pending_r2_with_full_coverage(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_zero_volume_manifest_repo(root)
    _write_current_sources(root, "20260717")

    audit = builder.build_audit_dataframe(root)
    coverage = _coverage_audit_rows(audit)
    formal = _formal_audit_rows(audit)

    assert list(coverage["snapshot_revision"]) == ["r1", "r2"]
    assert list(coverage["revision_formal_row_count"]) == ["0", "1"]
    assert list(formal["snapshot_revision"]) == ["r2"]
    assert (
        coverage.loc[
            coverage["snapshot_revision"].eq("r2"), "expected_session_status"
        ].iloc[0]
        == "current_formal_latest_pending_snapshot_revision"
    )
    assert coverage["historical_promotion_evidence_eligible"].eq("False").all()
    assert formal["historical_promotion_evidence_eligible"].eq("False").all()
    _validate_generated_audit(root, audit, tmp_path / "zero-to-has")


def test_has_to_zero_volume_rows_creates_pending_r2_coverage_only(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    _write_non_volume_current_sources(root, "20260717")

    audit = builder.build_audit_dataframe(root)
    coverage = _coverage_audit_rows(audit)
    formal = _formal_audit_rows(audit)

    assert list(coverage["snapshot_revision"]) == ["r1", "r2"]
    assert list(coverage["revision_formal_row_count"]) == ["1", "0"]
    assert list(formal["snapshot_revision"]) == ["r1"]
    pending = coverage[coverage["snapshot_revision"].eq("r2")].iloc[0]
    assert pending["formal_row_disposition"] == "not_applicable_revision_coverage"
    assert pending["historical_promotion_evidence_eligible"] == "False"
    _validate_generated_audit(root, audit, tmp_path / "has-to-zero")


def test_historical_zero_volume_revision_remains_in_revision_coverage(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_zero_volume_manifest_repo(root)
    _write_current_sources(root, "20260717")
    current_path = root / builder.FORMAL_SOURCE_PATH
    r2_sha = _manifest_v1_sha256(current_path.read_bytes())
    r2_relative = (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717_"
        f"r2_{r2_sha[:12]}.csv"
    )
    (root / r2_relative).write_bytes(current_path.read_bytes())
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    r1_sha = str(manifest.iloc[0]["snapshot_sha256"])
    for column, default in (
        ("snapshot_revision", "r1"),
        ("supersedes_snapshot_sha256", ""),
        ("revision_reason", "legacy_v1_manifest"),
    ):
        if column not in manifest.columns:
            manifest[column] = default
    r2_row = _manifest_row(
        root,
        "20260717",
        snapshot_path=r2_relative,
        snapshot_revision="r2",
        supersedes_snapshot_sha256=r1_sha,
        revision_reason="zero_to_has_volume_rows",
    )
    manifest = pd.concat([manifest, pd.DataFrame([r2_row])], ignore_index=True)
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "publish historical zero-to-has r2")

    audit = builder.build_audit_dataframe(root)
    coverage = _coverage_audit_rows(audit)
    formal = _formal_audit_rows(audit)

    assert list(coverage["snapshot_revision"]) == ["r1", "r2"]
    assert list(coverage["revision_formal_row_count"]) == ["0", "1"]
    assert list(formal["snapshot_revision"]) == ["r2"]
    assert coverage.loc[
        coverage["snapshot_revision"].eq("r1"),
        "historical_promotion_evidence_eligible",
    ].iloc[0] == "False"
    _validate_generated_audit(root, audit, tmp_path / "historical-zero")


def test_validator_rejects_missing_zero_revision_coverage_row(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_zero_volume_manifest_repo(root)
    _write_current_sources(root, "20260717")
    audit = builder.build_audit_dataframe(root)
    missing_zero_coverage = audit[
        ~(
            audit["audit_row_type"].eq("revision_coverage")
            & audit["snapshot_revision"].eq("r1")
        )
    ].copy()
    output = tmp_path / "missing-zero-coverage"
    csv_path = output / "audit.csv"
    md_path = output / "audit.md"
    docs_csv_path = output / "audit-docs.csv"
    docs_md_path = output / "audit-docs.md"
    builder.write_audit_artifacts(
        missing_zero_coverage,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )

    errors = validator.validate(
        root, csv_path, md_path, docs_csv_path, docs_md_path
    )
    assert any("revision coverage row count mismatch" in error for error in errors)


def test_new_day_current_audit_transitions_to_immutable_history_with_parity(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)

    current = builder.build_audit_dataframe(root)
    current_formal = _formal_audit_rows(current)
    current_row = current_formal[
        current_formal["snapshot_report_date"].eq("20260718")
    ].iloc[0]
    assert set(current["snapshot_revision"]) == {"r1"}
    historical_r1 = current_formal[
        current_formal["snapshot_report_date"].eq("20260717")
    ].iloc[0]
    assert historical_r1["revision_reason"] == "legacy_v1_manifest"
    assert historical_r1["legacy_revision_history_status"] == "complete"
    assert (
        historical_r1["legacy_precontract_revision_history_status"] == "complete"
    )
    assert current_row["paired_source_resolution"] == builder.CURRENT_SOURCE_RESOLUTION
    assert current_row["legacy_revision_history_status"] == "current_pending_snapshot"
    assert current_row["historical_promotion_evidence_eligible"] == "False"
    assert current_row["formal_row_disposition"] == "verified_clean"
    assert current_row["evidence_status"] == "complete"
    _validate_generated_audit(root, current, tmp_path / "current")

    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    current_formal = root / builder.FORMAL_SOURCE_PATH
    published_snapshot = (
        snapshot_dir / "daily_candidate_model_signals_for_report_20260718.csv"
    )
    published_snapshot.write_bytes(current_formal.read_bytes())
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest = pd.concat(
        [manifest, pd.DataFrame([_manifest_row(root, "20260718")])],
        ignore_index=True,
    )
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    pending = builder.build_audit_dataframe(root)
    pending_formal = _formal_audit_rows(pending)
    pending_row = pending_formal[
        pending_formal["snapshot_report_date"].eq("20260718")
    ].iloc[0]
    assert (
        pending_row["paired_source_resolution"]
        == builder.PUBLISHED_PENDING_SOURCE_RESOLUTION
    )
    _validate_generated_audit(root, pending, tmp_path / "pending")

    _git(root, "add", ".")
    _git(root, "commit", "-m", "publish new snapshot")
    historical = builder.build_audit_dataframe(root)
    historical_formal = _formal_audit_rows(historical)
    historical_row = historical_formal[
        historical_formal["snapshot_report_date"].eq("20260718")
    ].iloc[0]
    assert (
        historical_row["paired_source_resolution"]
        == "manifest_history_first_exact_row_same_commit_sources"
    )
    _validate_generated_audit(root, historical, tmp_path / "historical")

    parity_fields = (
        "formal_row_sha256",
        "watch_row_sha256",
        "candidate_row_sha256",
        "official_warrant_row_sha256",
        "production_code_sha256",
        "formal_snapshot_sha256",
        "watch_artifact_sha256",
        "candidate_artifact_sha256",
        "official_warrant_artifact_sha256",
        "formal_row_disposition",
        "evidence_status",
    )
    for field in parity_fields:
        assert current_row[field] == pending_row[field] == historical_row[field]


def _setup_same_day_revision_repo(root: Path) -> tuple[str, str]:
    _setup_dynamic_repo(root)
    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    r1_sha = str(manifest.iloc[0]["snapshot_sha256"])

    _write_current_sources(root, "20260717")
    current_formal_path = root / builder.FORMAL_SOURCE_PATH
    revised = pd.read_csv(current_formal_path, dtype=str, keep_default_na=False)
    revised.loc[0, "pattern_score"] = "1.0"
    revised.loc[0, "final_rank_score"] = "51.0"
    revised.to_csv(current_formal_path, index=False, lineterminator="\n")

    r2_manifest_sha = _manifest_v1_sha256(current_formal_path.read_bytes())
    r2_relative = (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717_"
        f"r2_{r2_manifest_sha[:12]}.csv"
    )
    (root / r2_relative).write_bytes(current_formal_path.read_bytes())
    r2_row = _manifest_row(
        root,
        "20260717",
        snapshot_path=r2_relative,
        snapshot_revision="r2",
        supersedes_snapshot_sha256=r1_sha,
        revision_reason="same_date_formal_lineage_correction",
    )
    for column, default in (
        ("snapshot_revision", "r1"),
        ("supersedes_snapshot_sha256", ""),
        ("revision_reason", "legacy_v1_manifest"),
    ):
        if column not in manifest.columns:
            manifest[column] = default
    manifest.loc[:, "snapshot_revision"] = "r1"
    manifest.loc[:, "revision_reason"] = "legacy_v1_manifest"
    manifest = pd.concat([manifest, pd.DataFrame([r2_row])], ignore_index=True)
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    return r1_sha, str(r2_row["snapshot_sha256"])


def test_same_day_revisions_are_preserved_and_current_matches_max_revision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_same_day_revision_repo(root)

    sources = builder.build_audit_sources(root, builder.manifest_rows(root))
    same_day = [source for source in sources if source["report_date"] == "20260717"]
    assert [source["snapshot_revision"] for source in same_day] == ["r1", "r2"]

    audit = builder.build_audit_dataframe(root)
    same_day_audit = _formal_audit_rows(audit)
    same_day_audit = same_day_audit[
        same_day_audit["snapshot_report_date"].eq("20260717")
    ]
    same_day_coverage = _coverage_audit_rows(audit)
    same_day_coverage = same_day_coverage[
        same_day_coverage["snapshot_report_date"].eq("20260717")
    ]
    assert list(same_day_audit["snapshot_revision"]) == ["r1", "r2"]
    assert len(same_day_audit) == 2
    assert list(same_day_coverage["snapshot_revision"]) == ["r1", "r2"]
    assert set(same_day_coverage["revision_formal_row_count"]) == {"1"}
    assert set(same_day_audit["formal_row_disposition"]) == {"verified_clean"}
    assert set(same_day_audit["legacy_precontract_revision_history_status"]) == {
        "complete"
    }
    assert (
        same_day_audit.loc[
            same_day_audit["snapshot_revision"].eq("r2"),
            "legacy_revision_history_status",
        ].iloc[0]
        == "versioned_revision_exact"
    )
    _validate_generated_audit(root, audit, tmp_path / "same-day-revisions")


def test_same_day_current_drift_becomes_pending_next_revision(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_same_day_revision_repo(root)
    _git(root, "add", ".")
    _git(root, "commit", "-m", "publish immutable r2")

    r1_path = (
        root
        / "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717.csv"
    )
    (root / builder.FORMAL_SOURCE_PATH).write_bytes(r1_path.read_bytes())

    audit = builder.build_audit_dataframe(root)
    same_day = _formal_audit_rows(audit)
    same_day = same_day[same_day["snapshot_report_date"].eq("20260717")]
    assert list(same_day["snapshot_revision"]) == ["r1", "r2", "r3"]
    pending = same_day[same_day["snapshot_revision"].eq("r3")].iloc[0]
    assert (
        pending["expected_session_status"]
        == "current_formal_latest_pending_snapshot_revision"
    )
    assert pending["revision_reason"] == "pending_warrant_formal_sync"
    assert pending["supersedes_snapshot_sha256"] == same_day.loc[
        same_day["snapshot_revision"].eq("r2"),
        "formal_snapshot_manifest_v1_sha256",
    ].iloc[0]
    assert pending["legacy_revision_history_status"] == "current_pending_snapshot"
    assert pending["historical_promotion_evidence_eligible"] == "False"
    _validate_generated_audit(root, audit, tmp_path / "pending-r3")


def test_pre_publisher_same_date_row_count_drop_is_pending_revision(
    tmp_path: Path,
) -> None:
    """Two-to-one is the bounded regression analogue of run 29698237679's 321-to-303 drift."""

    root = tmp_path / "repo"
    root.mkdir()
    _setup_same_day_revision_repo(root)
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    r2_index = manifest.index[manifest["snapshot_revision"].eq("r2")][0]
    r2_path = root / str(manifest.at[r2_index, "snapshot_path"])
    r2 = pd.read_csv(r2_path, dtype=str, keep_default_na=False)
    second = r2.iloc[0].copy()
    second["stock_id"] = "2317"
    second["source_row_index"] = "volume_breakout:1"
    second["model_rank"] = "2"
    r2 = pd.concat([r2, pd.DataFrame([second])], ignore_index=True)
    r2.to_csv(r2_path, index=False, lineterminator="\n")
    (root / builder.FORMAL_SOURCE_PATH).write_bytes(r2_path.read_bytes())
    manifest.at[r2_index, "snapshot_sha256"] = _manifest_v1_sha256(
        r2_path.read_bytes()
    )
    manifest.at[r2_index, "row_count"] = "2"
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "publish two-row immutable r2")

    r1_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_candidate_model_signals_for_report_20260717.csv"
    )
    (root / builder.FORMAL_SOURCE_PATH).write_bytes(r1_path.read_bytes())

    sources = builder.build_audit_sources(root, builder.manifest_rows(root))
    same_day = [source for source in sources if source["report_date"] == "20260717"]
    assert [source["snapshot_revision"] for source in same_day] == ["r1", "r2", "r3"]
    assert len(
        builder.volume_v2_formal_rows(same_day[1]["formal_payload"], "immutable-r2")
    ) == 2
    assert len(
        builder.volume_v2_formal_rows(same_day[2]["formal_payload"], "pending-r3")
    ) == 1
    assert (
        same_day[2]["expected_session_status"]
        == "current_formal_latest_pending_snapshot_revision"
    )


def test_same_day_revision_chain_rejects_wrong_supersedes_sha(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_same_day_revision_repo(root)
    manifest_path = (
        root
        / "output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[manifest["snapshot_revision"].eq("r2"), "supersedes_snapshot_sha256"] = (
        "f" * 64
    )
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    with pytest.raises(RuntimeError, match="supersedes_snapshot_sha256"):
        builder.build_audit_dataframe(root)


def test_validator_rejects_noncanonical_paired_artifact_paths(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    audit = builder.build_audit_dataframe(root)

    historical = audit["snapshot_report_date"].eq("20260717")
    historical_formal = historical & audit["audit_row_type"].eq("formal_row")
    audit.loc[historical, "watch_artifact_path"] = (
        "C:/stale/output/latest/daily_volume_breakout_watch_latest.csv"
    )
    audit.loc[historical_formal, "watch_artifact_path"] = "../path-escape.csv"
    audit.loc[:, "candidate_artifact_path"] = "../path-escape-candidate.csv"
    audit.loc[:, "official_warrant_artifact_path"] = (
        "output/latest/stale_warrant_market_analysis.csv"
    )

    output = tmp_path / "tampered-paths"
    csv_path = output / "audit.csv"
    md_path = output / "audit.md"
    docs_csv_path = output / "audit-docs.csv"
    docs_md_path = output / "audit-docs.md"
    builder.write_audit_artifacts(
        audit, csv_path, md_path, docs_csv_path, docs_md_path
    )
    errors = validator.validate(
        root, csv_path, md_path, docs_csv_path, docs_md_path
    )

    assert any(
        "multiple values for revision-level field watch_artifact_path" in error
        for error in errors
    )
    for field in (
        "watch_artifact_path",
        "candidate_artifact_path",
        "official_warrant_artifact_path",
    ):
        assert any(f"{field} mismatch" in error for error in errors)


def test_builder_and_validator_reject_same_canonical_payload_fake_revision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_same_day_revision_repo(root)
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    r1 = manifest[manifest["snapshot_revision"].eq("r1")].iloc[0]
    r2_index = manifest.index[manifest["snapshot_revision"].eq("r2")][0]
    r1_payload = (root / str(r1["snapshot_path"])).read_bytes()
    crlf_payload = r1_payload.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    (root / str(manifest.at[r2_index, "snapshot_path"])).write_bytes(crlf_payload)
    (root / builder.FORMAL_SOURCE_PATH).write_bytes(crlf_payload)
    manifest.at[r2_index, "snapshot_sha256"] = _manifest_v1_sha256(crlf_payload)
    manifest.at[r2_index, "row_count"] = str(
        len(pd.read_csv(io.BytesIO(crlf_payload), dtype=str, keep_default_na=False))
    )
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    with pytest.raises(RuntimeError, match="must change the canonical snapshot payload"):
        builder.build_audit_dataframe(root)
    with pytest.raises(RuntimeError, match="must change the canonical snapshot payload"):
        validator.expected_audit_sources(root, manifest)


def test_legacy_lf_manifest_hash_accepts_crlf_raw_snapshot(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    manifest = builder.manifest_rows(root)
    snapshot_path = root / str(manifest.iloc[0]["snapshot_path"])
    lf_payload = snapshot_path.read_bytes().replace(b"\r\n", b"\n")
    snapshot_path.write_bytes(lf_payload.replace(b"\n", b"\r\n"))

    audit = builder.build_audit_dataframe(root)
    _validate_generated_audit(root, audit, tmp_path / "legacy-crlf-compatible")


def test_manifest_row_count_parsers_require_nonnegative_integer() -> None:
    for value in ("", "-1", "+1", "1.0", "one"):
        with pytest.raises(RuntimeError, match="nonnegative integer"):
            builder.manifest_data_row_count(
                value, report_date="20260717", snapshot_revision="r1"
            )
        with pytest.raises(RuntimeError, match="nonnegative integer"):
            validator.expected_manifest_data_row_count(
                value, report_date="20260717", snapshot_revision="r1"
            )
    assert (
        builder.manifest_data_row_count(
            "0", report_date="20260717", snapshot_revision="r1"
        )
        == 0
    )
    assert (
        validator.expected_manifest_data_row_count(
            "12", report_date="20260717", snapshot_revision="r1"
        )
        == 12
    )


def test_builder_and_validator_reject_manifest_row_count_mismatch(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    good_audit = builder.build_audit_dataframe(root)
    output = tmp_path / "row-count-mismatch"
    csv_path = output / "audit.csv"
    md_path = output / "audit.md"
    docs_csv_path = output / "audit-docs.csv"
    docs_md_path = output / "audit-docs.md"
    builder.write_audit_artifacts(
        good_audit, csv_path, md_path, docs_csv_path, docs_md_path
    )

    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[:, "row_count"] = "999"
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    with pytest.raises(RuntimeError, match="row_count differs from raw snapshot"):
        builder.build_audit_dataframe(root)
    errors = validator.validate(
        root, csv_path, md_path, docs_csv_path, docs_md_path
    )
    assert any("row_count differs from raw snapshot" in error for error in errors)


def _setup_same_canonical_manifest_republication_repo(
    root: Path,
) -> tuple[str, str]:
    _setup_dynamic_repo(root)
    first_commit = _git(root, "rev-parse", "HEAD")
    _write_current_sources(root, "20260717")

    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    snapshot_path = root / str(manifest.iloc[0]["snapshot_path"])
    lf_payload = snapshot_path.read_bytes().replace(b"\r\n", b"\n")
    snapshot_path.write_bytes(lf_payload.replace(b"\n", b"\r\n"))
    manifest.loc[:, "generated_at"] = "2026-07-17 18:00:00 Asia/Taipei"
    manifest.loc[:, "pipeline_commit_sha"] = "2" * 40
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "republish same canonical formal payload")
    second_commit = _git(root, "rev-parse", "HEAD")
    return first_commit, second_commit


def test_exact_manifest_republication_selects_bound_commit_and_fails_promotion(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    first_commit, second_commit = _setup_same_canonical_manifest_republication_repo(
        root
    )

    audit = builder.build_audit_dataframe(root)
    row = _formal_audit_rows(audit)
    row = row[row["snapshot_report_date"].eq("20260717")].iloc[0]
    assert first_commit != second_commit
    assert row["snapshot_commit_sha"] == second_commit
    assert row["paired_source_commit_sha"] == second_commit
    assert (
        row["paired_source_resolution"]
        == "manifest_history_first_exact_row_same_commit_sources"
    )
    assert row["legacy_precontract_revision_history_status"] == (
        "incomplete_fail_closed"
    )
    assert row["legacy_revision_history_status"] == "complete"
    assert row["formal_row_disposition"] == "verified_clean"
    assert row["evidence_status"] == "complete"
    assert row["historical_promotion_evidence_eligible"] == "False"
    _validate_generated_audit(root, audit, tmp_path / "exact-republication")


def test_exact_row_missing_uses_oldest_same_canonical_fail_closed_fallback(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    first_commit, _ = _setup_same_canonical_manifest_republication_repo(root)
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[:, "generated_at"] = "2026-07-17 19:00:00 Asia/Taipei"
    manifest.loc[:, "pipeline_commit_sha"] = "3" * 40
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    audit = builder.build_audit_dataframe(root)
    row = _formal_audit_rows(audit)
    row = row[row["snapshot_report_date"].eq("20260717")].iloc[0]
    assert row["snapshot_commit_sha"] == first_commit
    assert row["paired_source_commit_sha"] == first_commit
    assert row["paired_source_resolution"] == (
        "legacy_same_canonical_publication_fallback_incomplete"
    )
    assert row["legacy_revision_history_status"] == "incomplete_fail_closed"
    assert row["legacy_precontract_revision_history_status"] == (
        "incomplete_fail_closed"
    )
    assert row["formal_row_disposition"] == "quarantined"
    assert row["evidence_status"] == "incomplete"
    assert row["historical_promotion_evidence_eligible"] == "False"
    _validate_generated_audit(root, audit, tmp_path / "missing-exact-fallback")


def test_validator_rejects_tampered_same_canonical_fallback_disposition(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_same_canonical_manifest_republication_repo(root)
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[:, "generated_at"] = "2026-07-17 19:00:00 Asia/Taipei"
    manifest.loc[:, "pipeline_commit_sha"] = "3" * 40
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    audit = builder.build_audit_dataframe(root)
    revision = audit["snapshot_report_date"].eq("20260717")
    formal = revision & audit["audit_row_type"].eq("formal_row")
    audit.loc[revision, "paired_source_resolution"] = (
        "manifest_history_first_exact_row_same_commit_sources"
    )
    audit.loc[revision, "legacy_revision_history_status"] = "complete"
    audit.loc[revision, "legacy_precontract_revision_history_status"] = "complete"
    audit.loc[formal, "formal_row_disposition"] = "verified_clean"
    audit.loc[formal, "evidence_status"] = "complete"
    audit.loc[formal, "historical_promotion_evidence_eligible"] = "True"

    output = tmp_path / "tampered-fallback"
    csv_path = output / "audit.csv"
    md_path = output / "audit.md"
    docs_csv_path = output / "audit-docs.csv"
    docs_md_path = output / "audit-docs.md"
    builder.write_audit_artifacts(
        audit, csv_path, md_path, docs_csv_path, docs_md_path
    )
    errors = validator.validate(
        root, csv_path, md_path, docs_csv_path, docs_md_path
    )
    for field in (
        "paired_source_resolution",
        "legacy_revision_history_status",
        "legacy_precontract_revision_history_status",
        "formal_row_disposition",
        "evidence_status",
        "historical_promotion_evidence_eligible",
    ):
        assert any(f"{field} mismatch" in error for error in errors)


def test_same_canonical_fallback_requires_valid_paired_publication(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    snapshot_path = root / str(manifest.iloc[0]["snapshot_path"])
    invalid_publication = _formal_frame("20260717")
    invalid_publication.loc[0, "pattern_score"] = "9.0"
    invalid_publication.loc[0, "final_rank_score"] = "59.0"
    invalid_publication.to_csv(snapshot_path, index=False, lineterminator="\n")
    manifest.loc[:, "snapshot_sha256"] = _manifest_v1_sha256(
        snapshot_path.read_bytes()
    )
    manifest.loc[:, "source_sha256"] = manifest.loc[:, "snapshot_sha256"]
    manifest.loc[:, "generated_at"] = "2026-07-17 20:00:00 Asia/Taipei"
    manifest.loc[:, "pipeline_commit_sha"] = "4" * 40
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    # Deliberately retain the 20260718 current formal source, so the commit is
    # an observed manifest+snapshot pair but not a valid same-commit formal publication.
    _git(root, "add", ".")
    _git(root, "commit", "-m", "invalid formal publication pairing")

    with pytest.raises(RuntimeError, match="no valid same-canonical publication"):
        builder.build_audit_dataframe(root)
    with pytest.raises(RuntimeError, match="no valid same-canonical publication"):
        validator.expected_audit_sources(root, manifest)


def _write_formal_variant(root: Path, report_date: str, pattern_score: str) -> None:
    _write_current_sources(root, report_date)
    formal_path = root / builder.FORMAL_SOURCE_PATH
    formal = pd.read_csv(formal_path, dtype=str, keep_default_na=False)
    formal.loc[0, "pattern_score"] = pattern_score
    formal.loc[0, "final_rank_score"] = str(Decimal("50") + Decimal(pattern_score))
    formal.to_csv(formal_path, index=False, lineterminator="\n")


def _commit_current_legacy_manifest_revision(
    root: Path, report_date: str, pattern_score: str, message: str
) -> None:
    _write_formal_variant(root, report_date, pattern_score)
    snapshot_path = (
        root
        / "output/history/daily_model_snapshots"
        / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    )
    snapshot_path.write_bytes((root / builder.FORMAL_SOURCE_PATH).read_bytes())
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    pd.DataFrame([_manifest_row(root, report_date)]).to_csv(
        manifest_path, index=False, lineterminator="\n"
    )
    _git(root, "add", ".")
    _git(root, "commit", "-m", message)


def test_legacy_git_manifest_recovery_adds_exact_precontract_revision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    _commit_current_legacy_manifest_revision(
        root, "20260717", "1.0", "second legacy publication"
    )
    _write_current_sources(root, "20260718")

    audit = builder.build_audit_dataframe(root)
    historical = _formal_audit_rows(audit)
    historical = historical[historical["snapshot_report_date"].eq("20260717")]

    assert list(historical["snapshot_revision"]) == ["legacy_r1", "r1"]
    recovered = historical[historical["snapshot_revision"].eq("legacy_r1")].iloc[0]
    assert recovered["revision_reason"] == "legacy_git_manifest_recovered"
    assert (
        recovered["legacy_revision_history_status"]
        == "legacy_git_manifest_recovered"
    )
    assert set(historical["legacy_precontract_revision_history_status"]) == {
        "complete"
    }
    assert set(historical["formal_row_disposition"]) == {"verified_clean"}
    assert set(historical["historical_promotion_evidence_eligible"]) == {"True"}
    _validate_generated_audit(root, audit, tmp_path / "legacy-recovered")


def test_legacy_git_manifest_recovery_requires_joint_manifest_snapshot_change(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    report_date = "20260717"
    snapshot_relative = (
        "output/history/daily_model_snapshots/"
        f"daily_candidate_model_signals_for_report_{report_date}.csv"
    )
    snapshot_path = root / snapshot_relative
    future = pd.read_csv(snapshot_path, dtype=str, keep_default_na=False)
    future.loc[0, "pattern_score"] = "9.0"
    future.loc[0, "final_rank_score"] = "59.0"
    future_payload = future.to_csv(index=False, lineterminator="\n").encode("utf-8")
    future_sha = _manifest_v1_sha256(future_payload)

    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    target = manifest["snapshot_report_date"].eq(report_date) & manifest[
        "artifact_id"
    ].eq("model_signals_for_report")
    assert int(target.sum()) == 1
    manifest.loc[target, ["snapshot_sha256", "source_sha256"]] = future_sha
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    _git(root, "add", manifest_path.relative_to(root).as_posix())
    _git(root, "commit", "-m", "prewrite future snapshot sha")

    snapshot_path.write_bytes(future_payload)
    (root / builder.FORMAL_SOURCE_PATH).write_bytes(future_payload)
    _git(
        root,
        "add",
        snapshot_relative,
        builder.FORMAL_SOURCE_PATH,
    )
    _git(root, "commit", "-m", "snapshot without manifest change")
    snapshot_only_commit = _git(root, "rev-parse", "HEAD")

    history = builder.distinct_git_path_history(root, snapshot_relative)
    assert history
    snapshot_only_history = [
        entry for entry in history if entry["commit_sha"] == snapshot_only_commit
    ]
    assert len(snapshot_only_history) == 1
    history_entry = snapshot_only_history[0]
    commit_sha = history_entry["commit_sha"]
    changed = builder.commit_changed_paths(root, commit_sha)
    manifest_relative = builder.MANIFEST_PATH.relative_to(builder.ROOT).as_posix()
    assert snapshot_relative in changed
    assert manifest_relative not in changed
    assert (
        builder.recover_legacy_git_manifest_source(
            root,
            report_date,
            "legacy_r1",
            snapshot_relative,
            history_entry,
        )
        is None
    )

    independent_history = validator.independent_distinct_git_path_history(
        root, snapshot_relative
    )
    assert independent_history
    independent_snapshot_only_history = [
        entry
        for entry in independent_history
        if entry["commit_sha"] == snapshot_only_commit
    ]
    assert len(independent_snapshot_only_history) == 1
    assert (
        validator.independently_recover_legacy_source(
            root,
            report_date,
            "legacy_r1",
            snapshot_relative,
            independent_snapshot_only_history[0],
        )
        is None
    )


def test_incomplete_precontract_history_quarantines_only_date_only_revision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)

    _write_formal_variant(root, "20260717", "1.0")
    legacy_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_candidate_model_signals_for_report_20260717.csv"
    )
    legacy_path.write_bytes((root / builder.FORMAL_SOURCE_PATH).read_bytes())
    _git(root, "add", ".")
    _git(root, "commit", "-m", "unmanifested legacy overwrite")

    _commit_current_legacy_manifest_revision(
        root, "20260717", "2.0", "final legacy publication"
    )
    manifest_path = (
        root
        / "output/history/daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    r1_sha = str(manifest.iloc[0]["snapshot_sha256"])
    for column, default in (
        ("snapshot_revision", "r1"),
        ("supersedes_snapshot_sha256", ""),
        ("revision_reason", "legacy_v1_manifest"),
    ):
        if column not in manifest.columns:
            manifest[column] = default

    _write_formal_variant(root, "20260717", "3.0")
    r2_sha = _manifest_v1_sha256(
        (root / builder.FORMAL_SOURCE_PATH).read_bytes()
    )
    r2_relative = (
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_20260717_"
        f"r2_{r2_sha[:12]}.csv"
    )
    (root / r2_relative).write_bytes((root / builder.FORMAL_SOURCE_PATH).read_bytes())
    r2_row = _manifest_row(
        root,
        "20260717",
        snapshot_path=r2_relative,
        snapshot_revision="r2",
        supersedes_snapshot_sha256=r1_sha,
        revision_reason="same_date_formal_lineage_correction",
    )
    manifest = pd.concat([manifest, pd.DataFrame([r2_row])], ignore_index=True)
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "versioned r2 publication")

    audit = builder.build_audit_dataframe(root)
    historical = _formal_audit_rows(audit)
    historical = historical[historical["snapshot_report_date"].eq("20260717")]
    assert set(historical["legacy_precontract_revision_history_status"]) == {
        "incomplete_fail_closed"
    }
    date_only = historical[historical["snapshot_revision"].eq("r1")].iloc[0]
    versioned = historical[historical["snapshot_revision"].eq("r2")].iloc[0]
    assert date_only["legacy_revision_history_status"] == "incomplete_fail_closed"
    assert date_only["formal_row_disposition"] == "quarantined"
    assert date_only["evidence_status"] == "incomplete"
    assert versioned["legacy_revision_history_status"] == "versioned_revision_exact"
    assert versioned["formal_row_disposition"] == "verified_clean"
    assert versioned["evidence_status"] == "complete"
    assert set(historical["historical_promotion_evidence_eligible"]) == {"False"}
    _validate_generated_audit(root, audit, tmp_path / "legacy-incomplete")


def test_validator_rejects_tampered_history_status_and_promotion_eligibility(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    audit = builder.build_audit_dataframe(root)
    target = audit["snapshot_report_date"].eq("20260717") & audit[
        "audit_row_type"
    ].eq("formal_row")
    assert int(target.sum()) == 1
    audit.loc[target, "legacy_revision_history_status"] = "incomplete_fail_closed"
    audit.loc[target, "historical_promotion_evidence_eligible"] = "False"

    output = tmp_path / "tampered-history"
    csv_path = output / "audit.csv"
    md_path = output / "audit.md"
    docs_csv_path = output / "audit-docs.csv"
    docs_md_path = output / "audit-docs.md"
    builder.write_audit_artifacts(
        audit, csv_path, md_path, docs_csv_path, docs_md_path
    )
    errors = validator.validate(
        root, csv_path, md_path, docs_csv_path, docs_md_path
    )

    assert any("legacy_revision_history_status" in error for error in errors)
    assert any(
        "historical_promotion_evidence_eligible mismatch" in error
        for error in errors
    )


def test_quarantined_dynamic_audit_is_valid_evidence_artifact(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(
        root,
        current_watch_score="9",
        current_candidate_score="1",
    )

    audit = builder.build_audit_dataframe(root)
    formal_audit = _formal_audit_rows(audit)
    row = formal_audit[formal_audit["snapshot_report_date"].eq("20260718")].iloc[0]
    assert row["formal_row_disposition"] == "quarantined"
    assert row["evidence_status"] == "complete"
    _validate_generated_audit(root, audit, tmp_path / "quarantined")


def test_unreplayable_dynamic_audit_is_valid_fail_closed_artifact(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    formal_path = root / builder.FORMAL_SOURCE_PATH
    formal = pd.read_csv(formal_path, dtype=str, keep_default_na=False)
    formal.loc[0, "final_rank_score"] = "not-a-number"
    formal.to_csv(formal_path, index=False, lineterminator="\n")

    audit = builder.build_audit_dataframe(root)
    formal_audit = _formal_audit_rows(audit)
    row = formal_audit[formal_audit["snapshot_report_date"].eq("20260718")].iloc[0]
    assert row["formal_row_disposition"] == "unreplayable"
    assert row["evidence_status"] == "incomplete"
    _validate_generated_audit(root, audit, tmp_path / "unreplayable")


def test_builder_reconstructs_all_dynamic_volume_v2_sources(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    sources = builder.build_audit_sources(ROOT, builder.manifest_rows(ROOT))
    expected_dates = tuple(dict.fromkeys(source["report_date"] for source in sources))
    expected_rows = sum(
        len(builder.volume_v2_formal_rows(source["formal_payload"], builder.FORMAL_SOURCE_PATH))
        for source in sources
    )
    formal_audit = _formal_audit_rows(audit)
    coverage_audit = _coverage_audit_rows(audit)

    assert len(formal_audit) == expected_rows
    assert len(coverage_audit) == len(sources)
    assert tuple(audit["snapshot_report_date"].drop_duplicates()) == expected_dates
    assert int(formal_audit["watch_disposition"].eq("superseded_advisory_snapshot").sum()) >= 1
    assert formal_audit.loc[
        formal_audit["candidate_row_present"].eq("False"), "counterfactual_score_context"
    ].eq("{}").all()
    assert formal_audit.loc[
        formal_audit["official_warrant_row_present"].eq("True"),
        "official_warrant_row_sha256",
    ].str.fullmatch(r"[0-9a-f]{64}").all()
    collision = formal_audit[
        formal_audit["watch_candidate_score_collision"].eq("True")
        | formal_audit["watch_candidate_rank_collision"].eq("True")
    ]
    legacy_collision = collision[
        ~collision["dispatcher_warrant_source_mode"].eq(
            "canonical_candidate_explicit_allowlist"
        )
    ]
    assert legacy_collision["formal_row_disposition"].eq("quarantined").all()
    assert legacy_collision["historical_promotion_evidence_eligible"].eq("False").all()
    assert (
        legacy_collision["impact_scope"]
        == "legacy_watch_source_score_rank_effect_unresolved"
    ).all()
    explicit_collision = collision[
        collision["dispatcher_warrant_source_mode"].eq(
            "canonical_candidate_explicit_allowlist"
        )
    ]
    assert explicit_collision["formal_row_disposition"].eq("verified_clean").all()
    assert explicit_collision["impact_scope"].eq(
        "watch_only_no_formal_score_or_rank_effect"
    ).all()
    assert set(formal_audit["replay_status"]) == {"resolved"}
    assert set(formal_audit["rank_replay_status"]) == {"resolved"}
    incomplete_revisions = formal_audit[
        formal_audit["legacy_revision_history_status"].eq("incomplete_fail_closed")
    ]
    assert incomplete_revisions["formal_row_disposition"].eq("quarantined").all()
    assert incomplete_revisions["evidence_status"].eq("incomplete").all()
    assert incomplete_revisions[
        "historical_promotion_evidence_eligible"
    ].eq("False").all()
    incomplete_dates = formal_audit[
        formal_audit["legacy_precontract_revision_history_status"].eq(
            "incomplete_fail_closed"
        )
    ]
    assert incomplete_dates["historical_promotion_evidence_eligible"].eq("False").all()
    eligible = formal_audit[
        formal_audit["historical_promotion_evidence_eligible"].eq("True")
    ]
    assert eligible["formal_row_disposition"].eq("verified_clean").all()
    assert eligible["legacy_precontract_revision_history_status"].eq("complete").all()
    assert eligible["snapshot_commit_sha"].str.fullmatch(r"[0-9a-f]{40}").all()
    assert eligible["paired_source_commit_sha"].str.fullmatch(r"[0-9a-f]{40}").all()
    absent = formal_audit[formal_audit["candidate_row_present"].eq("False")]
    assert set(absent["counterfactual_score_context"]) == {"{}"}
    rounding_gap = pd.to_numeric(
        formal_audit["published_component_replay_rounding_gap"], errors="raise"
    ).abs()
    assert float(rounding_gap.max()) <= 0.3

    collision = formal_audit[
        formal_audit["watch_disposition"].eq("superseded_advisory_snapshot")
        & formal_audit["snapshot_revision"].eq("r1")
    ].iloc[0]
    assert collision["snapshot_report_date"] == "20260716"
    assert collision["stock_id"] == "6505"
    assert collision["model_id"] == "volume_range_breakout_v2_high_position_volume_attack"
    assert collision["watch_warrant_signal"] == "call_put_bullish"
    assert collision["candidate_warrant_signal"] == "call_strong_inflow"
    assert collision["official_warrant_signal"] == "call_strong_inflow"
    assert collision["formal_warrant_signal"] == "call_strong_inflow"
    assert collision["watch_source_score"] == "99.0"
    assert collision["candidate_source_score"] == "99.0"
    assert collision["watch_source_rank"] == ""
    assert collision["candidate_source_rank"] == ""
    assert collision["collision_fields"] == "warrant_flow_signal"
    assert collision["published_counterfactual_collision_fields"] == ""
    assert collision["published_warrant_basis_signal"] == "call_strong_inflow"
    assert collision["warrant_bonus_points"] == "0"
    assert collision["base_model_score_delta"] == "0"
    assert collision["tdcc_score_delta"] == "0"
    assert collision["risk_penalty_delta"] == "0"
    assert collision["score_delta"] == "0"
    assert collision["rank_delta"] == "0"
    assert collision["published_final_rank_score"] == "73.0"
    assert collision["published_model_rank"] == "1"
    if collision["legacy_revision_history_status"] == "incomplete_fail_closed":
        assert collision["formal_row_disposition"] == "quarantined"
        assert (
            collision["impact_scope"]
            == "legacy_revision_history_incomplete_fail_closed"
        )
    else:
        assert collision["formal_row_disposition"] == "verified_clean"
        assert collision["impact_scope"] == "watch_only_no_formal_score_or_rank_effect"

    output_csv = tmp_path / "output.csv"
    output_md = tmp_path / "output.md"
    docs_csv = tmp_path / "docs.csv"
    docs_md = tmp_path / "docs.md"
    builder.write_audit_artifacts(audit, output_csv, output_md, docs_csv, docs_md)

    assert output_csv.read_bytes() == docs_csv.read_bytes()
    assert output_md.read_bytes() == docs_md.read_bytes()


def test_dispatcher_source_mode_distinguishes_legacy_and_canonical_order() -> None:
    legacy = b"""
def append_volume_breakout_signals():
    score_source = {}
    score_source.update(row.to_dict())
"""
    canonical = b"""
def append_volume_breakout_signals():
    score_source = {}
    score_source.update(row.to_dict())
    score_source[\"warrant_flow_signal\"] = authoritative_warrant_signal
"""
    explicit_allowlist = b"""
def append_volume_breakout_signals():
    score_source = {field: candidate_values[field] for field in candidate_fields}
    score_source.update({field: watch_values[field] for field in watch_fields})
    score_source[\"warrant_flow_signal\"] = authoritative_warrant_signal
"""

    assert builder.dispatcher_warrant_source_mode(legacy) == "legacy_watch_overrides_candidate"
    assert (
        builder.dispatcher_warrant_source_mode(canonical)
        == "canonical_candidate_after_watch_merge"
    )
    assert (
        builder.dispatcher_warrant_source_mode(explicit_allowlist)
        == "canonical_candidate_explicit_allowlist"
    )


def test_explicit_allowlist_audit_and_independent_validator_use_canonical_source(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root, explicit_candidate_allowlist=True)

    audit = builder.build_audit_dataframe(root)
    current = _formal_audit_rows(audit)
    current = current[current["snapshot_report_date"].eq("20260718")]

    assert len(current) == 1
    assert set(current["dispatcher_warrant_source_mode"]) == {
        "canonical_candidate_explicit_allowlist"
    }
    assert set(current["published_warrant_score_source"]) == {
        "canonical_candidate"
    }
    _validate_generated_audit(root, audit, tmp_path / "explicit-allowlist")


def test_20260810_6426_explicit_allowlist_ignores_advisory_watch_score_collision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(
        root,
        explicit_candidate_allowlist=True,
        current_watch_score="",
        current_candidate_score="69",
    )
    latest = root / "output" / "latest"
    formal = pd.read_csv(
        latest / "daily_candidate_model_signals_for_report_latest.csv",
        dtype=str,
        keep_default_na=False,
    )
    formal.loc[:, "signal_date"] = "20260810"
    formal.loc[:, "stock_id"] = "6426"
    formal.loc[:, "model_id"] = (
        "volume_range_breakout_v2_mid_position_momentum_attack"
    )
    formal.to_csv(
        latest / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
        lineterminator="\n",
    )
    watch = pd.read_csv(
        latest / "volume_breakout_watch_latest.csv",
        dtype=str,
        keep_default_na=False,
    )
    watch.loc[:, "signal_date"] = "20260810"
    watch.loc[:, "stock_id"] = "6426"
    watch.to_csv(
        latest / "volume_breakout_watch_latest.csv",
        index=False,
        lineterminator="\n",
    )
    for filename in ("all_candidates_latest.csv", "warrant_flow_latest.csv"):
        frame = pd.read_csv(latest / filename, dtype=str, keep_default_na=False)
        frame.loc[:, "stock_id"] = "6426"
        frame.to_csv(latest / filename, index=False, lineterminator="\n")

    audit = builder.build_audit_dataframe(root)
    current = _formal_audit_rows(audit)
    current = current[
        current["snapshot_report_date"].eq("20260810")
        & current["stock_id"].eq("6426")
    ]

    assert len(current) == 1
    row = current.iloc[0]
    assert row["dispatcher_warrant_source_mode"] == (
        "canonical_candidate_explicit_allowlist"
    )
    assert row["model_id"] == (
        "volume_range_breakout_v2_mid_position_momentum_attack"
    )
    assert row["watch_source_score"] == ""
    assert row["candidate_source_score"] == "69"
    assert row["watch_candidate_score_collision"] == "True"
    assert row["score_delta"] == "0"
    assert row["rank_delta"] == "0"
    assert row["formal_row_disposition"] == "verified_clean"
    assert row["evidence_status"] == "complete"
    assert row["impact_scope"] == "watch_only_no_formal_score_or_rank_effect"
    _validate_generated_audit(root, audit, tmp_path / "explicit-score-collision")


def test_explicit_allowlist_ignores_advisory_watch_rank_collision(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(
        root,
        explicit_candidate_allowlist=True,
        current_watch_rank="7",
        current_candidate_rank="1",
    )

    audit = builder.build_audit_dataframe(root)
    current = _formal_audit_rows(audit)
    row = current[current["snapshot_report_date"].eq("20260718")].iloc[0]

    assert row["watch_candidate_rank_collision"] == "True"
    assert row["score_delta"] == "0"
    assert row["rank_delta"] == "0"
    assert row["formal_row_disposition"] == "verified_clean"
    assert row["impact_scope"] == "watch_only_no_formal_score_or_rank_effect"
    _validate_generated_audit(root, audit, tmp_path / "explicit-rank-collision")


@pytest.mark.parametrize(
    ("watch_score", "candidate_score", "watch_rank", "candidate_rank"),
    [
        ("99", "69", "1", "1"),
        ("1", "1", "7", "1"),
    ],
)
def test_generic_watch_merge_score_or_rank_collision_remains_quarantined(
    tmp_path: Path,
    watch_score: str,
    candidate_score: str,
    watch_rank: str,
    candidate_rank: str,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(
        root,
        current_watch_score=watch_score,
        current_candidate_score=candidate_score,
        current_watch_rank=watch_rank,
        current_candidate_rank=candidate_rank,
    )

    audit = builder.build_audit_dataframe(root)
    current = _formal_audit_rows(audit)
    row = current[current["snapshot_report_date"].eq("20260718")].iloc[0]

    assert row["dispatcher_warrant_source_mode"] == (
        "canonical_candidate_after_watch_merge"
    )
    assert row["formal_row_disposition"] == "quarantined"
    assert row["impact_scope"] == "legacy_watch_source_score_rank_effect_unresolved"
    assert row["historical_promotion_evidence_eligible"] == "False"
    _validate_generated_audit(root, audit, tmp_path / "generic-source-collision")


def test_published_warrant_score_source_covers_every_dispatcher_mode() -> None:
    assert (
        builder.published_warrant_score_source(
            "canonical_candidate_after_watch_merge"
        )
        == "canonical_candidate"
    )
    assert (
        builder.published_warrant_score_source(
            "canonical_candidate_explicit_allowlist"
        )
        == "canonical_candidate"
    )
    assert (
        builder.published_warrant_score_source("legacy_watch_overrides_candidate")
        == "legacy_watch"
    )
    with pytest.raises(RuntimeError, match="unknown dispatcher warrant source mode"):
        builder.published_warrant_score_source("unknown_mode")
    with pytest.raises(RuntimeError, match="unknown dispatcher warrant source mode"):
        builder.published_warrant_score_source("canonical_candidate_unknown")


def test_three_collision_fields_replay_complete_component_delta() -> None:
    candidate = pd.Series(
        {
            "warrant_flow_signal": "no_signal",
            "tdcc_judgement": "mild_accumulation",
            "false_breakout_risk": "False",
        }
    )
    watch = pd.Series(
        {
            "warrant_flow_signal": "call_inflow",
            "tdcc_status": "distribution_warning",
            "false_breakout_risk": "True",
        }
    )
    published, canonical = builder.build_collision_contexts(
        candidate,
        watch,
        "legacy_watch_overrides_candidate",
    )
    formal = pd.Series(
        {
            "base_model_score": "62.0",
            "operation_score": "5.0",
            "tdcc_score": "3.0",
            "pattern_score": "4.0",
            "risk_penalty": "12.0",
            "final_rank_score": "62.0",
        }
    )

    replay = builder.replay_collision_components(
        formal,
        "volume_range_breakout_v2_low_position_volume_attack",
        published,
        canonical,
    )
    independent = validator.independent_component_replay(
        formal,
        "volume_range_breakout_v2_low_position_volume_attack",
        published,
        canonical,
    )

    assert builder.collision_field_names(published, canonical) == builder.COLLISION_FIELDS
    assert replay["counterfactual_base"] == Decimal("74")
    assert replay["counterfactual_tdcc"] == Decimal("7")
    assert replay["counterfactual_risk"] == Decimal("2")
    assert replay["counterfactual_final"] == Decimal("88")
    assert replay["final_delta"] == Decimal("26")
    assert independent["canonical_base"] == replay["counterfactual_base"]
    assert independent["canonical_tdcc"] == replay["counterfactual_tdcc"]
    assert independent["canonical_risk"] == replay["counterfactual_risk"]
    assert independent["canonical_final"] == replay["counterfactual_final"]


def test_component_replay_clamps_counterfactual_base_and_final() -> None:
    candidate = pd.Series({"tdcc_judgement": "mild_accumulation"})
    watch = pd.Series({"tdcc_status": "distribution_warning"})
    published, canonical = builder.build_collision_contexts(
        candidate,
        watch,
        "legacy_watch_overrides_candidate",
    )
    formal = pd.Series(
        {
            "base_model_score": "92.0",
            "operation_score": "0.0",
            "tdcc_score": "0.0",
            "pattern_score": "0.0",
            "risk_penalty": "6.0",
            "final_rank_score": "86.0",
        }
    )

    replay = builder.replay_collision_components(
        formal,
        "volume_range_breakout_v2_low_position_volume_attack",
        published,
        canonical,
    )

    assert replay["counterfactual_base"] == Decimal("100")
    assert replay["counterfactual_final"] == Decimal("100")


def test_counterfactual_rank_tie_break_ignores_published_rank() -> None:
    frame = pd.DataFrame(
        [
            {
                "counterfactual_final_rank_score": "80.0",
                "published_model_rank": "1",
                "stock_id": "6505",
                "source_row_index": "volume_breakout:9",
                "replay_status": "resolved",
            },
            {
                "counterfactual_final_rank_score": "80.0",
                "published_model_rank": "3",
                "stock_id": "2332",
                "source_row_index": "volume_breakout:8",
                "replay_status": "resolved",
            },
            {
                "counterfactual_final_rank_score": "80.0",
                "published_model_rank": "2",
                "stock_id": "2332",
                "source_row_index": "volume_breakout:2",
                "replay_status": "resolved",
            },
        ]
    )

    assert builder.counterfactual_rank_order(frame, frame.index) == [2, 1, 0]


def test_validator_accepts_fresh_deterministic_artifacts(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    _validate_generated_audit(ROOT, audit, tmp_path / "fresh")


def test_daily_model_pr_workflow_rebuilds_and_pins_history_audit() -> None:
    workflow = (
        ROOT / ".github/workflows/daily_model_maintenance_pr_validation.yml"
    ).read_text(encoding="utf-8")

    assert "python scripts/build_volume_v2_warrant_lineage_history_audit.py" in workflow
    assert "python scripts/validate_volume_v2_warrant_lineage_history_audit.py" in workflow
    assert "tests/test_volume_v2_warrant_lineage_history_audit.py" in workflow
    for governed_path in (
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "scripts/validate_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_volume_v2_warrant_lineage_history_audit.py",
        "docs/latest/volume_v2_warrant_lineage_history_audit_latest.csv",
        "docs/latest/volume_v2_warrant_lineage_history_audit_latest.md",
        "output/latest/volume_v2_warrant_lineage_history_audit_latest.csv",
        "output/latest/volume_v2_warrant_lineage_history_audit_latest.md",
    ):
        assert governed_path in workflow


def test_production_workflows_build_audit_from_their_published_snapshot_state() -> None:
    build_command = "python scripts/build_volume_v2_warrant_lineage_history_audit.py"
    validate_command = "python scripts/validate_volume_v2_warrant_lineage_history_audit.py"
    publish_command = "python scripts/update_daily_published_model_snapshots.py"
    snapshot_validate_command = (
        "python scripts/validate_daily_published_model_snapshots.py"
    )

    daily = (ROOT / ".github/workflows/daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    candidate_index = daily.index("python scripts/build_daily_candidate_model_layer.py")
    audit_source_publish = daily.index(publish_command, candidate_index)
    scoped_snapshot_validate = daily.index(
        snapshot_validate_command,
        audit_source_publish,
    )
    first_build = daily.index(build_command, scoped_snapshot_validate)
    first_validate = daily.index(validate_command, first_build)
    operation_index = daily.index(
        "python scripts/build_daily_volume_breakout_operation_section.py",
        first_validate,
    )
    post_audit_publish = daily.index(publish_command, operation_index)
    full_snapshot_validate = daily.index(
        snapshot_validate_command,
        post_audit_publish,
    )
    final_audit_validate = daily.index(validate_command, post_audit_publish)
    assert (
        candidate_index
        < audit_source_publish
        < scoped_snapshot_validate
        < first_build
        < first_validate
        < operation_index
        < post_audit_publish
        < full_snapshot_validate
        < final_audit_validate
    )
    assert daily.count(publish_command) == 2
    assert daily.count(build_command) == 1

    warrant = (ROOT / ".github/workflows/warrant_flow.yml").read_text(
        encoding="utf-8"
    )
    candidate_index = warrant.index("python scripts/build_daily_candidate_model_layer.py")
    first_build = warrant.index(build_command, candidate_index)
    first_validate = warrant.index(validate_command, first_build)
    publish_index = warrant.index(publish_command, first_validate)
    second_build = warrant.index(build_command, publish_index)
    second_validate = warrant.index(validate_command, second_build)
    assert candidate_index < first_build < first_validate < publish_index
    assert publish_index < second_build < second_validate
    assert "git add output/latest/volume_v2_warrant_lineage_history_audit_latest.*" in warrant
    assert "git add docs/latest/volume_v2_warrant_lineage_history_audit_latest.*" in warrant


def test_validator_rejects_tampered_formal_disposition(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    target = audit[
        audit["audit_row_type"].eq("formal_row")
        & audit["snapshot_report_date"].eq("20260716")
        & audit["snapshot_revision"].eq("r1")
        & audit["stock_id"].eq("6505")
    ].index
    assert len(target) == 1
    audit.loc[target[0], "formal_row_disposition"] = "superseded"

    csv_path = tmp_path / "audit.csv"
    docs_csv_path = tmp_path / "audit_docs.csv"
    payload = audit.to_csv(index=False, lineterminator="\n").encode("utf-8")
    csv_path.write_bytes(payload)
    docs_csv_path.write_bytes(payload)
    md_path = tmp_path / "audit.md"
    docs_md_path = tmp_path / "audit_docs.md"
    md_payload = builder.render_markdown(builder.build_audit_dataframe(ROOT)).encode("utf-8")
    md_path.write_bytes(md_payload)
    docs_md_path.write_bytes(md_payload)

    errors = validator.validate(
        ROOT,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )
    assert any("formal_row_disposition mismatch" in error for error in errors)


def test_validator_rejects_tampered_component_replay(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    target = audit[
        audit["audit_row_type"].eq("formal_row")
        & audit["snapshot_report_date"].eq("20260716")
        & audit["snapshot_revision"].eq("r1")
        & audit["stock_id"].eq("6505")
    ].index
    assert len(target) == 1
    audit.loc[target[0], "counterfactual_base_model_score"] = "999.0"

    csv_path = tmp_path / "audit.csv"
    docs_csv_path = tmp_path / "audit_docs.csv"
    payload = audit.to_csv(index=False, lineterminator="\n").encode("utf-8")
    csv_path.write_bytes(payload)
    docs_csv_path.write_bytes(payload)
    md_path = tmp_path / "audit.md"
    docs_md_path = tmp_path / "audit_docs.md"
    md_payload = builder.render_markdown(builder.build_audit_dataframe(ROOT)).encode("utf-8")
    md_path.write_bytes(md_payload)
    docs_md_path.write_bytes(md_payload)

    errors = validator.validate(
        ROOT,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )
    assert any("counterfactual_base_model_score mismatch" in error for error in errors)
