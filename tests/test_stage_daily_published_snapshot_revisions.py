from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import stage_daily_published_snapshot_revisions as staging  # noqa: E402
import update_daily_published_model_snapshots as publisher  # noqa: E402


def _git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def _write_fixture(root: Path) -> tuple[Path, Path, Path]:
    _git(root, "init")
    report_date = "20260720"
    snapshot_dir = root / "output/history/daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    payload = b"main_price_date,report_ready\n20260720,True\n"
    digest = hashlib.sha256(payload).hexdigest()
    snapshot_path = snapshot_dir / f"data_freshness_{report_date}_r1_{digest[:12]}.csv"
    snapshot_path.write_bytes(payload)
    backup_path = snapshot_dir / f"data_freshness_{report_date}_backup.csv"
    backup_path.write_bytes(b"unregistered backup\n")
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    row = {column: "" for column in publisher.MANIFEST_COLUMNS}
    row.update(
        {
            "snapshot_report_date": report_date,
            "snapshot_revision": "r1",
            "supersedes_snapshot_sha256": "",
            "revision_reason": "initial_publish",
            "generated_at": "2026-07-20 12:00:00 Asia/Taipei",
            "pipeline_commit_sha": "a" * 40,
            "main_price_date": report_date,
            "report_ready": "True",
            "artifact_id": "data_freshness",
            "source_path": "output/latest/data_freshness_latest.csv",
            "snapshot_path": snapshot_path.relative_to(root).as_posix(),
            "source_sha256": digest,
            "snapshot_sha256": digest,
            "row_count": "1",
            "column_count": "2",
            "purpose": "as_published_daily_model_snapshot",
        }
    )
    pd.DataFrame([row], columns=publisher.MANIFEST_COLUMNS).to_csv(
        manifest_path,
        index=False,
        lineterminator="\n",
    )
    return manifest_path, snapshot_path, backup_path


def _append_manifest_artifact(
    root: Path,
    manifest_path: Path,
    *,
    artifact_id: str,
) -> Path:
    artifact = publisher.ARTIFACTS_BY_ID[artifact_id]
    payload = b"signal_date,stock_id\n20260720,2330\n"
    digest = hashlib.sha256(payload).hexdigest()
    snapshot_path = (
        manifest_path.parent
        / f"{artifact.snapshot_stem}_20260720_r1_{digest[:12]}.csv"
    )
    snapshot_path.write_bytes(payload)
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False).fillna("")
    row = manifest.iloc[0].to_dict()
    row.update(
        {
            "artifact_id": artifact_id,
            "source_path": f"output/latest/{artifact.source_name}",
            "snapshot_path": snapshot_path.relative_to(root).as_posix(),
            "source_sha256": digest,
            "snapshot_sha256": digest,
            "row_count": "1",
            "column_count": "2",
        }
    )
    pd.concat(
        [manifest, pd.DataFrame([row], columns=publisher.MANIFEST_COLUMNS)],
        ignore_index=True,
    ).to_csv(manifest_path, index=False, lineterminator="\n")
    return snapshot_path


def _commit_fixture_baseline(
    root: Path,
    manifest_path: Path,
    snapshot_path: Path,
) -> None:
    _git(
        root,
        "add",
        "--",
        manifest_path.relative_to(root).as_posix(),
        snapshot_path.relative_to(root).as_posix(),
    )
    _git(
        root,
        "-c",
        "user.name=Snapshot Test",
        "-c",
        "user.email=snapshot-test@example.invalid",
        "commit",
        "-m",
        "baseline snapshot manifest",
    )


def _index_bytes(root: Path) -> bytes | None:
    raw_path = _git(root, "rev-parse", "--git-path", "index")
    index_path = Path(raw_path)
    if not index_path.is_absolute():
        index_path = root / index_path
    return index_path.read_bytes() if index_path.is_file() else None


def test_exact_manifest_staging_excludes_unregistered_same_prefix_backup(
    tmp_path: Path,
) -> None:
    manifest_path, snapshot_path, backup_path = _write_fixture(tmp_path)

    staged = staging.stage_registered_snapshot_revisions(
        report_date="20260720",
        artifact_ids={"data_freshness"},
        manifest_path=manifest_path,
        snapshot_dir=manifest_path.parent,
        repository_root=tmp_path,
    )

    expected = {
        manifest_path.relative_to(tmp_path).as_posix(),
        snapshot_path.relative_to(tmp_path).as_posix(),
    }
    assert set(staged) == expected
    assert set(_git(tmp_path, "diff", "--cached", "--name-only").splitlines()) == expected
    assert backup_path.relative_to(tmp_path).as_posix() not in expected
    assert f"?? {backup_path.relative_to(tmp_path).as_posix()}" in _git(
        tmp_path, "status", "--porcelain"
    )


def test_exact_manifest_staging_requires_every_selected_artifact(
    tmp_path: Path,
) -> None:
    manifest_path, _, _ = _write_fixture(tmp_path)

    with pytest.raises(RuntimeError, match="missing a registered artifact"):
        staging.stage_registered_snapshot_revisions(
            report_date="20260720",
            artifact_ids={"data_freshness", "all_candidates_source_rows"},
            manifest_path=manifest_path,
            snapshot_dir=manifest_path.parent,
            repository_root=tmp_path,
        )


def test_exact_manifest_staging_rejects_unselected_new_manifest_row_and_restores_index(
    tmp_path: Path,
) -> None:
    manifest_path, selected_snapshot, _ = _write_fixture(tmp_path)
    _commit_fixture_baseline(tmp_path, manifest_path, selected_snapshot)
    unselected_snapshot = _append_manifest_artifact(
        tmp_path,
        manifest_path,
        artifact_id="model_signals_for_report",
    )
    unrelated = tmp_path / "notes.txt"
    unrelated.write_text("preserve this pre-staged path\n", encoding="utf-8")
    _git(tmp_path, "add", "--", unrelated.relative_to(tmp_path).as_posix())
    index_before = _index_bytes(tmp_path)

    with pytest.raises(RuntimeError, match="unselected new snapshot rows"):
        staging.stage_registered_snapshot_revisions(
            report_date="20260720",
            artifact_ids={"data_freshness"},
            manifest_path=manifest_path,
            snapshot_dir=manifest_path.parent,
            repository_root=tmp_path,
        )

    assert _index_bytes(tmp_path) == index_before
    assert _git(tmp_path, "diff", "--cached", "--name-only").splitlines() == [
        unrelated.relative_to(tmp_path).as_posix()
    ]
    assert f"?? {unselected_snapshot.relative_to(tmp_path).as_posix()}" in _git(
        tmp_path, "status", "--porcelain", "--untracked-files=all"
    )


def test_exact_manifest_staging_rejects_pre_staged_unregistered_snapshot_and_restores_index(
    tmp_path: Path,
) -> None:
    manifest_path, selected_snapshot, backup_path = _write_fixture(tmp_path)
    _commit_fixture_baseline(tmp_path, manifest_path, selected_snapshot)
    backup_relative = backup_path.relative_to(tmp_path).as_posix()
    _git(tmp_path, "add", "--", backup_relative)
    index_before = _index_bytes(tmp_path)

    with pytest.raises(RuntimeError, match="already staged"):
        staging.stage_registered_snapshot_revisions(
            report_date="20260720",
            artifact_ids={"data_freshness"},
            manifest_path=manifest_path,
            snapshot_dir=manifest_path.parent,
            repository_root=tmp_path,
        )

    assert _index_bytes(tmp_path) == index_before
    assert _git(tmp_path, "diff", "--cached", "--name-only").splitlines() == [
        backup_relative
    ]
