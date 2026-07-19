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

from daily_snapshot_revision_utils import (  # noqa: E402
    select_latest_snapshot_revisions,
    snapshot_file_sha256,
)


ARTIFACT_ID = "model_signals_for_report"
REPORT_DATE = "20260717"


def write_manifest(snapshot_dir: Path, rows: list[dict[str, str]]) -> Path:
    path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    pd.DataFrame(rows).to_csv(path, index=False, lineterminator="\n")
    return path


def repository_snapshot_dir(repository_root: Path) -> Path:
    path = repository_root / "output" / "history" / "daily_model_snapshots"
    path.mkdir(parents=True, exist_ok=True)
    return path


def revision_row(
    path: Path,
    sha256: str,
    revision: str,
    *,
    supersedes: str = "",
    reason: str = "",
) -> dict[str, str]:
    return {
        "snapshot_report_date": REPORT_DATE,
        "snapshot_revision": revision,
        "supersedes_snapshot_sha256": supersedes,
        "revision_reason": reason,
        "artifact_id": ARTIFACT_ID,
        "snapshot_path": path.as_posix(),
        "snapshot_sha256": sha256,
    }


def test_legacy_r1_accepts_raw_crlf_manifest_hash(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    snapshot = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    payload = b"signal_date,stock_id\r\n20260717,1111\r\n"
    snapshot.write_bytes(payload)
    raw_sha = hashlib.sha256(payload).hexdigest()
    write_manifest(
        snapshot_dir,
        [
            {
                "snapshot_report_date": REPORT_DATE,
                "artifact_id": ARTIFACT_ID,
                "snapshot_path": snapshot.as_posix(),
                "snapshot_sha256": raw_sha,
            }
        ],
    )

    selected = select_latest_snapshot_revisions(
        snapshot_dir,
        ARTIFACT_ID,
        repository_root=tmp_path,
    )

    assert len(selected) == 1
    assert selected[0].revision == "r1"
    assert selected[0].snapshot_sha256 == raw_sha


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
def test_partial_revision_manifest_schema_fails_closed(
    tmp_path: Path,
    present_revision_columns: tuple[str, ...],
) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    snapshot = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    revision_values = {
        "snapshot_revision": "r1",
        "supersedes_snapshot_sha256": "",
        "revision_reason": "legacy_v1_manifest",
    }
    row = {
        "snapshot_report_date": REPORT_DATE,
        "artifact_id": ARTIFACT_ID,
        "snapshot_path": snapshot.as_posix(),
        "snapshot_sha256": "1" * 64,
    }
    row.update(
        {column: revision_values[column] for column in present_revision_columns}
    )
    write_manifest(snapshot_dir, [row])

    with pytest.raises(RuntimeError, match="partial revision schema"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )


def test_modern_revision_schema_blank_snapshot_revision_fails_closed(
    tmp_path: Path,
) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    snapshot = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    write_manifest(
        snapshot_dir,
        [
            revision_row(
                snapshot,
                "1" * 64,
                "",
                reason="modern_schema_must_not_default_to_r1",
            )
        ],
    )

    with pytest.raises(RuntimeError, match="snapshot_revision must not be blank"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )


def test_same_date_selection_uses_manifest_max_r2_and_exact_path(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    r1.write_text("signal_date,stock_id\n20260717,1111\n", encoding="utf-8")
    r1_sha = snapshot_file_sha256(r1)
    staging = snapshot_dir / "r2-staging.csv"
    staging.write_text("signal_date,stock_id\n20260717,2222\n", encoding="utf-8")
    r2_sha = snapshot_file_sha256(staging)
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r2_{r2_sha[:12]}.csv"
    )
    staging.rename(r2)
    write_manifest(
        snapshot_dir,
        [
            revision_row(r1, r1_sha, "r1", reason="legacy_v1_manifest"),
            revision_row(
                r2,
                r2_sha,
                "r2",
                supersedes=r1_sha,
                reason="same_day_correction",
            ),
        ],
    )

    selected = select_latest_snapshot_revisions(
        snapshot_dir,
        ARTIFACT_ID,
        repository_root=tmp_path,
    )

    assert len(selected) == 1
    assert selected[0].revision == "r2"
    assert selected[0].path == r2.resolve()
    assert selected[0].snapshot_sha256 == r2_sha


def test_broken_revision_chain_fails_closed(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    r1_sha = "1" * 64
    r3_sha = "3" * 64
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    r3 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r3_{r3_sha[:12]}.csv"
    )
    write_manifest(
        snapshot_dir,
        [
            revision_row(r1, r1_sha, "r1", reason="legacy_v1_manifest"),
            revision_row(r3, r3_sha, "r3", supersedes=r1_sha, reason="bad_gap"),
        ],
    )

    with pytest.raises(RuntimeError, match="revision sequence is not continuous"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )


def test_wrong_versioned_filename_sha12_fails_closed(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    r1_sha = "1" * 64
    r2_sha = "2" * 64
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r2_deadbeef0000.csv"
    )
    write_manifest(
        snapshot_dir,
        [
            revision_row(r1, r1_sha, "r1", reason="legacy_v1_manifest"),
            revision_row(
                r2,
                r2_sha,
                "r2",
                supersedes=r1_sha,
                reason="same_day_correction",
            ),
        ],
    )

    with pytest.raises(RuntimeError, match="path identity mismatch"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )

def test_r2_without_revision_reason_fails_closed(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    r1_sha = "1" * 64
    r2_sha = "2" * 64
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r2_{r2_sha[:12]}.csv"
    )
    write_manifest(
        snapshot_dir,
        [
            revision_row(r1, r1_sha, "r1", reason="legacy_v1_manifest"),
            revision_row(r2, r2_sha, "r2", supersedes=r1_sha),
        ],
    )

    with pytest.raises(RuntimeError, match="revision_reason is required"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )


def test_missing_intermediate_revision_file_fails_closed(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    r1_sha = "1" * 64
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    staging = snapshot_dir / "r2-staging.csv"
    staging.write_text("signal_date,stock_id\n20260717,2222\n", encoding="utf-8")
    r2_sha = snapshot_file_sha256(staging)
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r2_{r2_sha[:12]}.csv"
    )
    staging.rename(r2)
    write_manifest(
        snapshot_dir,
        [
            revision_row(r1, r1_sha, "r1", reason="legacy_v1_manifest"),
            revision_row(
                r2,
                r2_sha,
                "r2",
                supersedes=r1_sha,
                reason="same_day_correction",
            ),
        ],
    )

    with pytest.raises(RuntimeError, match=r"file is missing: .*revision=r1"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
        )


def test_tampered_intermediate_revision_file_fails_closed(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    r1.write_text("signal_date,stock_id\n20260717,1111\n", encoding="utf-8")
    r1_sha = snapshot_file_sha256(r1)
    staging = snapshot_dir / "r2-staging.csv"
    staging.write_text("signal_date,stock_id\n20260717,2222\n", encoding="utf-8")
    r2_sha = snapshot_file_sha256(staging)
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r2_{r2_sha[:12]}.csv"
    )
    staging.rename(r2)
    write_manifest(
        snapshot_dir,
        [
            revision_row(r1, r1_sha, "r1", reason="legacy_v1_manifest"),
            revision_row(
                r2,
                r2_sha,
                "r2",
                supersedes=r1_sha,
                reason="same_day_correction",
            ),
        ],
    )
    r1.write_text("signal_date,stock_id\n20260717,9999\n", encoding="utf-8")

    with pytest.raises(RuntimeError, match=r"SHA-256 mismatch: .*revision=r1"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
        )


def test_manifest_path_escape_fails_closed(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    outside = tmp_path / "outside" / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    write_manifest(
        snapshot_dir,
        [revision_row(outside, "1" * 64, "r1", reason="legacy_v1_manifest")],
    )

    with pytest.raises(RuntimeError, match="does not end in the approved path"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )


def test_repo_relative_posix_snapshot_path_resolves_after_repository_move(
    tmp_path: Path,
) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    staging = snapshot_dir / "staging.csv"
    staging.write_text("signal_date,stock_id\n20260717,1111\n", encoding="utf-8")
    sha256 = snapshot_file_sha256(staging)
    snapshot = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r1_{sha256[:12]}.csv"
    )
    staging.rename(snapshot)
    relative_path = snapshot.relative_to(tmp_path).as_posix()
    row = revision_row(snapshot, sha256, "r1", reason="initial_publish")
    row["snapshot_path"] = relative_path
    write_manifest(snapshot_dir, [row])

    selected = select_latest_snapshot_revisions(
        snapshot_dir,
        ARTIFACT_ID,
        repository_root=tmp_path,
    )

    assert selected[0].path_text == relative_path
    assert selected[0].path == snapshot.resolve()


def test_legacy_absolute_c_snapshot_path_relocates_only_by_complete_tail(
    tmp_path: Path,
) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    snapshot = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    snapshot.write_text("signal_date,stock_id\n20260717,1111\n", encoding="utf-8")
    sha256 = snapshot_file_sha256(snapshot)
    row = revision_row(
        snapshot,
        sha256,
        "r1",
        reason="legacy_v1_manifest",
    )
    row["snapshot_path"] = (
        "C:/retired-runner/repository/output/history/daily_model_snapshots/"
        + snapshot.name
    )
    write_manifest(snapshot_dir, [row])

    selected = select_latest_snapshot_revisions(
        snapshot_dir,
        ARTIFACT_ID,
        repository_root=tmp_path,
    )

    assert selected[0].path == snapshot.resolve()
    assert selected[0].path_text.startswith("C:/retired-runner/")


def test_helper_rejects_canonical_duplicate_revision_with_raw_legacy_r1_hash(
    tmp_path: Path,
) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    lf_payload = b"signal_date,stock_id\n20260717,1111\n"
    crlf_payload = lf_payload.replace(b"\n", b"\r\n")
    r1 = snapshot_dir / f"daily_candidate_model_signals_for_report_{REPORT_DATE}.csv"
    r1.write_bytes(crlf_payload)
    r1_raw_sha = hashlib.sha256(crlf_payload).hexdigest()
    canonical_sha = hashlib.sha256(lf_payload).hexdigest()
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r2_{canonical_sha[:12]}.csv"
    )
    r2.write_bytes(lf_payload)
    write_manifest(
        snapshot_dir,
        [
            revision_row(
                r1,
                r1_raw_sha,
                "r1",
                reason="legacy_v1_manifest",
            ),
            revision_row(
                r2,
                canonical_sha,
                "r2",
                supersedes=r1_raw_sha,
                reason="fake_line_ending_revision",
            ),
        ],
    )

    with pytest.raises(RuntimeError, match="canonical duplicate payload revision"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
        )


def test_helper_rejects_lookalike_filename_and_parent_escape(tmp_path: Path) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    sha256 = "1" * 64
    lookalike = snapshot_dir / (
        f"unregistered_{REPORT_DATE}_r1_{sha256[:12]}.csv"
    )
    row = revision_row(lookalike, sha256, "r1", reason="initial_publish")
    write_manifest(snapshot_dir, [row])
    with pytest.raises(RuntimeError, match="path identity mismatch"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )

    approved_name = (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r1_{sha256[:12]}.csv"
    )
    row["snapshot_path"] = (
        "output/history/daily_model_snapshots/../daily_model_snapshots/"
        + approved_name
    )
    write_manifest(snapshot_dir, [row])
    with pytest.raises(RuntimeError, match="path escape"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
            require_files=False,
        )


def test_helper_rejects_contained_nested_absolute_snapshot_path(
    tmp_path: Path,
) -> None:
    snapshot_dir = repository_snapshot_dir(tmp_path)
    nested_dir = snapshot_dir / "nested"
    nested_dir.mkdir(parents=True, exist_ok=True)
    staging = nested_dir / "staging.csv"
    staging.write_text("signal_date,stock_id\n20260717,1111\n", encoding="utf-8")
    sha256 = snapshot_file_sha256(staging)
    nested_snapshot = nested_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_r1_"
        f"{sha256[:12]}.csv"
    )
    staging.rename(nested_snapshot)
    row = revision_row(
        nested_snapshot,
        sha256,
        "r1",
        reason="initial_publish",
    )
    row["snapshot_path"] = nested_snapshot.resolve().as_posix()
    write_manifest(snapshot_dir, [row])

    with pytest.raises(RuntimeError, match="does not end in the approved path"):
        select_latest_snapshot_revisions(
            snapshot_dir,
            ARTIFACT_ID,
            repository_root=tmp_path,
        )
