from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path

import pytest

from scripts.daily_full_validation_replay_checkpoint import (
    CHECKPOINT_MANIFEST,
    CHECKPOINT_MANIFEST_SHA,
    PAYLOAD_DIR,
    REPLAY_DATE,
    ReplayCheckpointError,
    assert_isolated_output_path,
    assert_validation_only_command,
    create_checkpoint,
    restore_checkpoint,
    verify_checkpoint,
)
import scripts.run_daily_full_validation_replay as replay_runner
import scripts.validate_daily_full_validation_replay as replay_validator
import scripts.validate_repo_file_lifecycle_inventory as lifecycle_validator


RUN_ID = "31190000000"


def _git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True
    )


def _fixture(
    tmp_path: Path,
) -> tuple[Path, Path, list[str], str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "replay@example.invalid")
    _git(repo, "config", "user.name", "Replay Test")
    paths: list[str] = []
    categories = (
        "market_session",
        "daily_price_raw",
        "daily_price_normalized",
        "candidate_inputs",
        "warrant_raw",
        "warrant_normalized",
        "trading_calendar",
    )
    for index, category in enumerate(categories):
        relative = f"checkpoint_inputs/{category}.csv"
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"date,value\n{REPLAY_DATE},{index}\n",
            encoding="utf-8",
        )
        paths.append(relative)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "baseline")
    source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    for relative in paths:
        with (repo / relative).open("a", encoding="utf-8") as handle:
            handle.write("revision,authoritative\n")
    identities = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "revision_kind": "authoritative_historical_revision",
        "source_sha": source_sha,
        "byte_parity_with_run_31174813266": False,
        "sources": [
            {
                "category": Path(relative).stem,
                "identity": (
                    f"official-{Path(relative).stem}-{REPLAY_DATE}"
                ),
                "source_url": (
                    "https://official.example.invalid/"
                    f"{Path(relative).name}?date={REPLAY_DATE}"
                ),
                "artifact_path": relative,
                "bytes": (repo / relative).stat().st_size,
                "sha256": hashlib.sha256(
                    (repo / relative).read_bytes()
                ).hexdigest(),
            }
            for relative in paths
        ],
    }
    identity_path = repo / "source_revision_manifest.json"
    identity_path.write_text(
        json.dumps(identities), encoding="utf-8"
    )
    paths.append("source_revision_manifest.json")
    return repo, identity_path, paths, source_sha


def _build(
    tmp_path: Path,
) -> tuple[Path, Path, list[str], str]:
    repo, identity_path, paths, source_sha = _fixture(tmp_path)
    bundle = tmp_path / "bundle"
    create_checkpoint(
        repo_root=repo,
        bundle_dir=bundle,
        paths=paths,
        replay_date=REPLAY_DATE,
        source_sha=source_sha,
        producer_run_id=RUN_ID,
        producer_head_sha=source_sha,
        source_identity_manifest=identity_path,
        checkpoint_kind="pre_step41",
        producer_steps=["Build volume breakout watch"],
    )
    return repo, bundle, paths, source_sha


def test_checkpoint_roundtrip_exact_manifest_bytes_sha_date_source_and_path_set(
    tmp_path: Path,
) -> None:
    repo, bundle, paths, source_sha = _build(tmp_path)
    manifest = verify_checkpoint(
        bundle_dir=bundle,
        expected_source_sha=source_sha,
        expected_run_id=RUN_ID,
        expected_kind="pre_step41",
    )
    assert manifest["replay_date"] == "20260807"
    assert manifest["authoritative_historical_revision"] is True
    assert manifest["byte_parity_with_run_31174813266"] is False
    assert manifest["path_allowlist"] == sorted(paths)
    assert (
        manifest["safety"]["mutable_source_fallback_allowed"] is False
    )
    assert (
        bundle / CHECKPOINT_MANIFEST_SHA
    ).read_text().strip() == hashlib.sha256(
        (bundle / CHECKPOINT_MANIFEST).read_bytes()
    ).hexdigest()

    restore_root = tmp_path / "restore"
    subprocess.run(
        ["git", "clone", "-q", str(repo), str(restore_root)],
        check=True,
    )
    _git(restore_root, "checkout", "-q", source_sha)
    restored = restore_checkpoint(
        bundle_dir=bundle,
        destination_root=restore_root,
        expected_source_sha=source_sha,
        expected_run_id=RUN_ID,
        expected_kind="pre_step41",
    )
    assert len(restored["files"]) == len(paths)
    for relative in paths:
        assert (restore_root / relative).read_bytes() == (
            bundle / PAYLOAD_DIR / relative
        ).read_bytes()


def test_checkpoint_restore_accepts_clean_new_replay_source_and_keeps_old_identity(
    tmp_path: Path,
) -> None:
    repo, bundle, paths, checkpoint_source_sha = _build(tmp_path)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "track checkpoint revision")
    (repo / paths[0]).write_text("current replay baseline\n", encoding="utf-8")
    _git(repo, "add", paths[0])
    _git(repo, "commit", "-qm", "new replay source")
    replay_source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    restore_root = tmp_path / "cross-revision-restore"
    subprocess.run(
        ["git", "clone", "-q", str(repo), str(restore_root)], check=True
    )
    restored = restore_checkpoint(
        bundle_dir=bundle,
        destination_root=restore_root,
        expected_source_sha=checkpoint_source_sha,
        expected_destination_source_sha=replay_source_sha,
        expected_run_id=RUN_ID,
        expected_kind="pre_step41",
    )
    assert restored["source_sha"] == checkpoint_source_sha
    assert (restore_root / paths[0]).read_bytes() == (
        bundle / PAYLOAD_DIR / paths[0]
    ).read_bytes()


def test_checkpoint_restore_rejects_dirty_new_replay_source(
    tmp_path: Path,
) -> None:
    repo, bundle, paths, checkpoint_source_sha = _build(tmp_path)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "new replay source")
    replay_source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    (repo / paths[0]).write_text("dirty\n", encoding="utf-8")
    with pytest.raises(ReplayCheckpointError, match="restore collision"):
        restore_checkpoint(
            bundle_dir=bundle,
            destination_root=repo,
            expected_source_sha=checkpoint_source_sha,
            expected_destination_source_sha=replay_source_sha,
            expected_run_id=RUN_ID,
            expected_kind="pre_step41",
        )


def test_cross_revision_manifest_preserves_checkpoint_and_replay_sources(
    tmp_path: Path,
) -> None:
    repo, identity_path, paths, checkpoint_source_sha = _fixture(tmp_path)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "replay source")
    replay_source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    transition = {
        "mode": "authorized_code_revision_transition",
        "checkpoint_source_sha": checkpoint_source_sha,
        "replay_source_sha": replay_source_sha,
        "checkpoint_run_id": "31268964962",
        "checkpoint_artifact_id": "9025240156",
        "checkpoint_artifact_digest": replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST,
    }
    output = replay_runner.write_replay_source_revision_manifest(
        source_manifest_path=identity_path,
        output_path=tmp_path / "replay-source-revision.json",
        transition=transition,
    )
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["checkpoint_source_sha"] == checkpoint_source_sha
    assert payload["replay_source_sha"] == replay_source_sha
    assert payload["source_sha"] == replay_source_sha
    assert payload["revision_transition"]["checkpoint_source_manifest_sha256"]
    post_bundle = tmp_path / "post-bundle"
    post_manifest = create_checkpoint(
        repo_root=repo,
        bundle_dir=post_bundle,
        paths=paths,
        replay_date=REPLAY_DATE,
        source_sha=replay_source_sha,
        producer_run_id="31270000001",
        producer_head_sha=replay_source_sha,
        source_identity_manifest=output,
        checkpoint_kind="post_validation",
        producer_steps=["Validate catalyst layer"],
        capture_context="validation_replay",
    )
    assert post_manifest["checkpoint_source_sha"] == checkpoint_source_sha
    assert post_manifest["replay_source_sha"] == replay_source_sha
    assert post_manifest["revision_transition"] == payload[
        "revision_transition"
    ]
    verified = verify_checkpoint(
        bundle_dir=post_bundle,
        expected_source_sha=replay_source_sha,
        expected_run_id="31270000001",
        expected_kind="post_validation",
        expected_capture_context="validation_replay",
    )
    assert verified["checkpoint_source_sha"] == checkpoint_source_sha
    manifest_path = post_bundle / CHECKPOINT_MANIFEST
    mutated = json.loads(manifest_path.read_text(encoding="utf-8"))
    mutated["checkpoint_source_sha"] = "b" * 40
    mutated["revision_transition"]["checkpoint_source_sha"] = "b" * 40
    manifest_path.write_text(
        json.dumps(mutated, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    (post_bundle / CHECKPOINT_MANIFEST_SHA).write_text(
        hashlib.sha256(manifest_path.read_bytes()).hexdigest() + "\n",
        encoding="ascii",
    )
    with pytest.raises(
        ReplayCheckpointError,
        match="checkpoint source revision metadata mismatch",
    ):
        verify_checkpoint(
            bundle_dir=post_bundle,
            expected_source_sha=replay_source_sha,
            expected_run_id="31270000001",
            expected_kind="post_validation",
            expected_capture_context="validation_replay",
        )


def test_authorized_revision_transition_pins_identity_and_producer_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, paths, checkpoint_source_sha = _build(tmp_path)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "authorized producer fix")
    producer_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    with (repo / paths[1]).open("a", encoding="utf-8") as handle:
        handle.write("validator-fix,true\n")
    _git(repo, "add", paths[1])
    _git(repo, "commit", "-qm", "authorized validator fix")
    validator_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    formal_only_path = "formal_lineage_fix.py"
    (repo / formal_only_path).write_text(
        "formal-lineage-fix\n", encoding="utf-8"
    )
    with (repo / paths[2]).open("a", encoding="utf-8") as handle:
        handle.write("formal-lineage-fix,true\n")
    _git(repo, "add", paths[2], formal_only_path)
    _git(repo, "commit", "-qm", "authorized formal lineage fix")
    formal_lineage_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    operation_only_path = "operation_completeness_fix.py"
    (repo / operation_only_path).write_text(
        "operation-completeness-fix\n", encoding="utf-8"
    )
    with (repo / paths[2]).open("a", encoding="utf-8") as handle:
        handle.write("operation-completeness-fix,true\n")
    _git(repo, "add", paths[2], operation_only_path)
    _git(repo, "commit", "-qm", "authorized operation completeness fix")
    operation_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_SOURCE_SHA",
        checkpoint_source_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_COMMIT",
        producer_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_PATHS",
        (paths[0], paths[1]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_VALIDATOR_FIX_COMMIT",
        validator_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_VALIDATOR_FIX_PATHS", (paths[1],)
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT",
        formal_lineage_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS",
        (formal_only_path, paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT",
        operation_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS",
        (operation_only_path, paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_OPERATION_SHARED_PATH",
        paths[2],
    )
    transition = replay_runner.require_authorized_checkpoint_revision_transition(
        repo_root=repo,
        checkpoint_source_sha=checkpoint_source_sha,
        replay_source_sha=operation_fix_sha,
        checkpoint_run_id=replay_runner.AUTHORIZED_CHECKPOINT_RUN_ID,
        checkpoint_artifact_id=replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_ID,
        checkpoint_artifact_digest=(
            replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
        ),
    )
    assert transition["mode"] == "authorized_code_revision_transition"
    assert transition["producer_fix_commit"] == producer_fix_sha
    assert transition["validator_fix_commit"] == validator_fix_sha
    assert transition["formal_lineage_fix_commit"] == formal_lineage_fix_sha
    assert transition["operation_completeness_fix_commit"] == operation_fix_sha
    with pytest.raises(
        replay_runner.ValidationReplayError, match="not preauthorized"
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=checkpoint_source_sha,
            replay_source_sha=operation_fix_sha,
            checkpoint_run_id="999",
            checkpoint_artifact_id=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_ID
            ),
            checkpoint_artifact_digest=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
            ),
        )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="identity inputs are malformed",
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=producer_fix_sha,
            replay_source_sha=producer_fix_sha,
            checkpoint_run_id="bad",
            checkpoint_artifact_id="bad",
            checkpoint_artifact_digest="bad",
        )
    (repo / paths[0]).write_text("producer drift\n", encoding="utf-8")
    _git(repo, "add", paths[0])
    _git(repo, "commit", "-qm", "unauthorized producer drift")
    drift_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    with pytest.raises(
        replay_runner.ValidationReplayError, match="producer fix paths drifted"
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=checkpoint_source_sha,
            replay_source_sha=drift_sha,
            checkpoint_run_id=replay_runner.AUTHORIZED_CHECKPOINT_RUN_ID,
            checkpoint_artifact_id=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_ID
            ),
            checkpoint_artifact_digest=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
            ),
        )


def test_authorized_revision_transition_rejects_validator_fix_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, paths, checkpoint_source_sha = _build(tmp_path)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "authorized producer fix")
    producer_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    with (repo / paths[1]).open("a", encoding="utf-8") as handle:
        handle.write("validator-fix,true\n")
    _git(repo, "add", paths[1])
    _git(repo, "commit", "-qm", "authorized validator fix")
    validator_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_SOURCE_SHA",
        checkpoint_source_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_COMMIT",
        producer_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_PATHS",
        (paths[0], paths[1]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_VALIDATOR_FIX_COMMIT",
        validator_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_VALIDATOR_FIX_PATHS", (paths[1],)
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT",
        validator_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS",
        ("formal_lineage_fix.py", paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT",
        validator_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS",
        ("operation_completeness_fix.py", paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_OPERATION_SHARED_PATH",
        paths[2],
    )
    with (repo / paths[1]).open("a", encoding="utf-8") as handle:
        handle.write("unauthorized-drift,true\n")
    _git(repo, "add", paths[1])
    _git(repo, "commit", "-qm", "unauthorized validator drift")
    drift_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="validator fix paths drifted",
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=checkpoint_source_sha,
            replay_source_sha=drift_sha,
            checkpoint_run_id=replay_runner.AUTHORIZED_CHECKPOINT_RUN_ID,
            checkpoint_artifact_id=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_ID
            ),
            checkpoint_artifact_digest=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
            ),
        )


def test_authorized_revision_transition_rejects_formal_lineage_fix_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, paths, checkpoint_source_sha = _build(tmp_path)
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "authorized producer fix")
    producer_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    with (repo / paths[1]).open("a", encoding="utf-8") as handle:
        handle.write("validator-fix,true\n")
    _git(repo, "add", paths[1])
    _git(repo, "commit", "-qm", "authorized validator fix")
    validator_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    formal_only_path = "formal_lineage_fix.py"
    (repo / formal_only_path).write_text(
        "formal-lineage-fix\n", encoding="utf-8"
    )
    with (repo / paths[2]).open("a", encoding="utf-8") as handle:
        handle.write("formal-lineage-fix,true\n")
    _git(repo, "add", paths[2], formal_only_path)
    _git(repo, "commit", "-qm", "authorized formal lineage fix")
    formal_lineage_fix_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_SOURCE_SHA",
        checkpoint_source_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_COMMIT",
        producer_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_PATHS",
        (paths[0], paths[1]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_VALIDATOR_FIX_COMMIT",
        validator_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_VALIDATOR_FIX_PATHS", (paths[1],)
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT",
        formal_lineage_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS",
        (formal_only_path, paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT",
        formal_lineage_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS",
        ("operation_completeness_fix.py", paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_OPERATION_SHARED_PATH",
        paths[2],
    )
    with (repo / formal_only_path).open("a", encoding="utf-8") as handle:
        handle.write("unauthorized-drift,true\n")
    _git(repo, "add", formal_only_path)
    _git(repo, "commit", "-qm", "unauthorized formal lineage drift")
    drift_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="formal lineage fix paths drifted",
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=checkpoint_source_sha,
            replay_source_sha=drift_sha,
            checkpoint_run_id=replay_runner.AUTHORIZED_CHECKPOINT_RUN_ID,
            checkpoint_artifact_id=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_ID
            ),
            checkpoint_artifact_digest=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
            ),
        )


def test_authorized_revision_transition_rejects_operation_completeness_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, paths, checkpoint_source_sha = _build(tmp_path)
    def current_head() -> str:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "authorized producer fix")
    producer_fix_sha = current_head()
    with (repo / paths[1]).open("a", encoding="utf-8") as handle:
        handle.write("validator-fix,true\n")
    _git(repo, "add", paths[1])
    _git(repo, "commit", "-qm", "authorized validator fix")
    validator_fix_sha = current_head()
    formal_only_path = "formal_lineage_fix.py"
    (repo / formal_only_path).write_text(
        "formal-lineage-fix\n", encoding="utf-8"
    )
    with (repo / paths[2]).open("a", encoding="utf-8") as handle:
        handle.write("formal-lineage-fix,true\n")
    _git(repo, "add", paths[2], formal_only_path)
    _git(repo, "commit", "-qm", "authorized formal lineage fix")
    formal_lineage_fix_sha = current_head()
    operation_only_path = "operation_completeness_fix.py"
    (repo / operation_only_path).write_text(
        "operation-completeness-fix\n", encoding="utf-8"
    )
    with (repo / paths[2]).open("a", encoding="utf-8") as handle:
        handle.write("operation-completeness-fix,true\n")
    _git(repo, "add", paths[2], operation_only_path)
    _git(repo, "commit", "-qm", "authorized operation completeness fix")
    operation_fix_sha = current_head()
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_SOURCE_SHA",
        checkpoint_source_sha,
    )
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_PRODUCER_FIX_COMMIT", producer_fix_sha
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_PRODUCER_FIX_PATHS",
        (paths[0], paths[1]),
    )
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_VALIDATOR_FIX_COMMIT", validator_fix_sha
    )
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_VALIDATOR_FIX_PATHS", (paths[1],)
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT",
        formal_lineage_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS",
        (formal_only_path, paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT",
        operation_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS",
        (operation_only_path, paths[2]),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_FORMAL_OPERATION_SHARED_PATH",
        paths[2],
    )
    with (repo / operation_only_path).open("a", encoding="utf-8") as handle:
        handle.write("unauthorized-drift\n")
    _git(repo, "add", operation_only_path)
    _git(repo, "commit", "-qm", "unauthorized operation completeness drift")
    drift_sha = current_head()
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="operation completeness fix paths drifted",
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=checkpoint_source_sha,
            replay_source_sha=drift_sha,
            checkpoint_run_id=replay_runner.AUTHORIZED_CHECKPOINT_RUN_ID,
            checkpoint_artifact_id=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_ID
            ),
            checkpoint_artifact_digest=(
                replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
            ),
        )


def test_authorized_checkpoint_manifest_and_sidecar_sha_are_pinned(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, bundle, _, _ = _build(tmp_path)
    manifest_sha = hashlib.sha256(
        (bundle / CHECKPOINT_MANIFEST).read_bytes()
    ).hexdigest()
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_MANIFEST_SHA256",
        manifest_sha,
    )
    replay_runner.require_authorized_checkpoint_bundle_identity(bundle)
    (bundle / CHECKPOINT_MANIFEST_SHA).write_text(
        "0" * 64 + "\n", encoding="ascii"
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="manifest/sidecar SHA mismatch",
    ):
        replay_runner.require_authorized_checkpoint_bundle_identity(bundle)


def test_cross_revision_workflow_requires_explicit_checkpoint_identity() -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github/workflows/daily_full_validation_replay_20260807.yml"
    ).read_text(encoding="utf-8")
    assert "checkpoint_source_sha:" in workflow
    assert '--checkpoint-source-sha "$CHECKPOINT_SOURCE_SHA"' in workflow
    assert '--checkpoint-artifact-id "$CHECKPOINT_ARTIFACT_ID"' in workflow
    assert '--checkpoint-artifact-digest "$CHECKPOINT_ARTIFACT_DIGEST"' in workflow
    assert "checkpoint replay source transition mismatch" in workflow


def _freshness_csv_bytes(date: str, *, ready: bool) -> bytes:
    return (
        "market_session_date,expected_main_price_date,main_price_date,"
        "report_ready,daily_pdf_ready\n"
        f"{date},{date},{date},{ready},{ready}\n"
    ).encode("utf-8")


def _publish_baseline_fixture(
    tmp_path: Path,
    *,
    baseline_date: str = "20260805",
    current_matches_baseline: bool = False,
) -> tuple[Path, Path, str, dict[str, object], bytes]:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "codex@example.invalid")
    _git(repo, "config", "user.name", "Codex Test")
    path = repo / replay_runner.FRESHNESS_PATH
    path.parent.mkdir(parents=True)
    baseline_bytes = _freshness_csv_bytes(baseline_date, ready=False)
    path.write_bytes(baseline_bytes)
    _git(repo, "add", replay_runner.FRESHNESS_PATH.as_posix())
    _git(repo, "commit", "-qm", "baseline")
    source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if not current_matches_baseline:
        path.write_bytes(_freshness_csv_bytes("20260807", ready=True))
    manifest: dict[str, object] = {
        "files": [
            {
                "path": replay_runner.FRESHNESS_PATH.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "baseline": {
                    "exists": True,
                    "bytes": len(baseline_bytes),
                    "sha256": hashlib.sha256(baseline_bytes).hexdigest(),
                },
            }
        ]
    }
    return repo, tmp_path / "runner-temp", source_sha, manifest, baseline_bytes


def test_publish_freshness_baseline_materializes_exact_checkpoint_git_object(
    tmp_path: Path,
) -> None:
    repo, runner_temp, source_sha, manifest, baseline_bytes = (
        _publish_baseline_fixture(tmp_path)
    )
    evidence = replay_runner.materialize_publish_freshness_baseline(
        repo_root=repo,
        runner_temp=runner_temp,
        checkpoint_source_sha=source_sha,
        checkpoint_manifest=manifest,
    )
    materialized = (
        runner_temp
        / replay_runner.PUBLISH_BASELINE_DIRNAME
        / replay_runner.FRESHNESS_PATH.name
    )
    assert materialized.read_bytes() == baseline_bytes
    assert evidence["baseline_date"] == "20260805"
    assert evidence["baseline_sha256"] == hashlib.sha256(
        baseline_bytes
    ).hexdigest()
    assert evidence["current_substitution_forbidden"] is True


@pytest.mark.parametrize(
    "mutation,match",
    [
        ("missing", "no unique"),
        ("wrong_path", "no unique"),
        ("bytes", "bytes/SHA mismatch"),
        ("sha", "bytes/SHA mismatch"),
        ("date", "date mismatch"),
        ("current_as_baseline", "cannot substitute"),
    ],
)
def test_publish_freshness_baseline_rejects_untrusted_materialization(
    tmp_path: Path,
    mutation: str,
    match: str,
) -> None:
    repo, runner_temp, source_sha, manifest, _baseline_bytes = (
        _publish_baseline_fixture(
            tmp_path,
            baseline_date=("20260804" if mutation == "date" else "20260805"),
            current_matches_baseline=(mutation == "current_as_baseline"),
        )
    )
    entry = manifest["files"][0]
    if mutation == "missing":
        manifest["files"] = []
    elif mutation == "wrong_path":
        entry["path"] = "output/latest/not_freshness.csv"
    elif mutation == "bytes":
        entry["baseline"]["bytes"] += 1
    elif mutation == "sha":
        entry["baseline"]["sha256"] = "0" * 64
    with pytest.raises(replay_runner.ValidationReplayError, match=match):
        replay_runner.materialize_publish_freshness_baseline(
            repo_root=repo,
            runner_temp=runner_temp,
            checkpoint_source_sha=source_sha,
            checkpoint_manifest=manifest,
        )


def test_replay_failure_checkpoint_is_created_before_error_is_rethrown(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    bundle = tmp_path / "post-bundle"
    observed: dict[str, object] = {}

    def fake_capture_checkpoint(**kwargs: object) -> dict[str, object]:
        observed.update(kwargs)
        bundle.mkdir()
        (bundle / "checkpoint_manifest.json").write_text(
            "{}\n", encoding="utf-8"
        )
        return {"files": []}

    monkeypatch.setattr(
        replay_runner, "capture_checkpoint", fake_capture_checkpoint
    )
    replay_runner.capture_replay_failure_checkpoint(
        repo_root=repo,
        runner_temp=tmp_path / "runner-temp",
        bundle_dir=bundle,
        source_sha="1" * 40,
        run_id="31290000000",
        replay_source_manifest=tmp_path / "source.json",
        steps=[{"step": "Guard", "status": "failure"}],
        error=replay_runner.ValidationReplayError("guard failed"),
    )
    assert observed["checkpoint_kind"] == "post_step_failure"
    assert observed["capture_context"] == "validation_replay_failure"
    assert bundle.is_dir()
    payload = json.loads(
        (repo / replay_runner.STEP_RESULTS_PATH).read_text(encoding="utf-8")
    )
    assert payload["mode"] == "replay_failure"
    assert payload["error"] == "guard failed"


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "bytes",
        "sha",
        "date",
        "source_sha",
        "run_id",
    ],
)
def test_checkpoint_verification_rejects_contract_drift(
    tmp_path: Path, mutation: str
) -> None:
    _, bundle, _, source_sha = _build(tmp_path)
    manifest_path = bundle / CHECKPOINT_MANIFEST
    manifest = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )
    if mutation == "missing":
        (
            bundle
            / PAYLOAD_DIR
            / manifest["path_allowlist"][0]
        ).unlink()
    elif mutation == "extra":
        (bundle / PAYLOAD_DIR / "unexpected.txt").write_text(
            "x", encoding="utf-8"
        )
    elif mutation == "bytes":
        path = (
            bundle
            / PAYLOAD_DIR
            / manifest["path_allowlist"][0]
        )
        path.write_bytes(path.read_bytes() + b"x")
    else:
        if mutation == "sha":
            manifest["files"][0]["sha256"] = "0" * 64
        elif mutation == "date":
            manifest["replay_date"] = "20260808"
        elif mutation == "source_sha":
            manifest["source_sha"] = "2" * 40
        elif mutation == "run_id":
            manifest["producer_run_id"] = "999"
        manifest_path.write_text(
            json.dumps(
                manifest, sort_keys=True, separators=(",", ":")
            )
            + "\n",
            encoding="utf-8",
        )
        (bundle / CHECKPOINT_MANIFEST_SHA).write_text(
            hashlib.sha256(manifest_path.read_bytes()).hexdigest()
            + "\n",
            encoding="ascii",
        )
    with pytest.raises(ReplayCheckpointError):
        verify_checkpoint(
            bundle_dir=bundle,
            expected_source_sha=source_sha,
            expected_run_id=RUN_ID,
            expected_kind="pre_step41",
        )


def test_checkpoint_rejects_date_fallback_and_source_identity_sha_drift(
    tmp_path: Path,
) -> None:
    repo, identity_path, paths, source_sha = _fixture(tmp_path)
    with pytest.raises(ReplayCheckpointError, match="20260807"):
        create_checkpoint(
            repo_root=repo,
            bundle_dir=tmp_path / "wrong-date",
            paths=paths,
            replay_date="20260808",
            source_sha=source_sha,
            producer_run_id=RUN_ID,
            producer_head_sha=source_sha,
            source_identity_manifest=identity_path,
            checkpoint_kind="pre_step41",
            producer_steps=["Build volume breakout watch"],
        )
    identity = json.loads(
        identity_path.read_text(encoding="utf-8")
    )
    identity["sources"][0]["sha256"] = "0" * 64
    identity_path.write_text(
        json.dumps(identity), encoding="utf-8"
    )
    with pytest.raises(ReplayCheckpointError, match="SHA mismatch"):
        create_checkpoint(
            repo_root=repo,
            bundle_dir=tmp_path / "wrong-source",
            paths=paths,
            replay_date=REPLAY_DATE,
            source_sha=source_sha,
            producer_run_id=RUN_ID,
            producer_head_sha=source_sha,
            source_identity_manifest=identity_path,
            checkpoint_kind="pre_step41",
            producer_steps=["Build volume breakout watch"],
        )


def test_checkpoint_verification_rejects_source_revision_manifest_drift(
    tmp_path: Path,
) -> None:
    _, bundle, _, source_sha = _build(tmp_path)
    revision_path = bundle / "source_revision_manifest.json"
    revision = json.loads(revision_path.read_text(encoding="utf-8"))
    revision["source_sha"] = "f" * 40
    revision_path.write_text(
        json.dumps(revision, sort_keys=True), encoding="utf-8"
    )
    with pytest.raises(
        ReplayCheckpointError,
        match="source revision manifest mismatch",
    ):
        verify_checkpoint(
            bundle_dir=bundle,
            expected_source_sha=source_sha,
            expected_run_id=RUN_ID,
            expected_kind="pre_step41",
        )


def test_restore_rejects_baseline_collision(
    tmp_path: Path,
) -> None:
    repo, bundle, paths, source_sha = _build(tmp_path)
    restore_root = tmp_path / "restore"
    subprocess.run(
        ["git", "clone", "-q", str(repo), str(restore_root)],
        check=True,
    )
    _git(restore_root, "checkout", "-q", source_sha)
    (restore_root / paths[0]).write_text(
        "collision\n", encoding="utf-8"
    )
    with pytest.raises(ReplayCheckpointError, match="collision"):
        restore_checkpoint(
            bundle_dir=bundle,
            destination_root=restore_root,
            expected_source_sha=source_sha,
            expected_run_id=RUN_ID,
            expected_kind="pre_step41",
        )


@pytest.mark.parametrize(
    "command",
    [
        "git commit -m forbidden",
        "git push origin HEAD:main",
        "git rebase origin/main",
        "gh workflow run daily_full_pipeline.yml",
        "python scripts/run_chatgpt_daily_report_entrypoint.py",
        "python scripts/move_daily_reports_after_verified_copy.py",
    ],
)
def test_validation_only_command_guard_rejects_production_mutations(
    command: str,
) -> None:
    with pytest.raises(ReplayCheckpointError):
        assert_validation_only_command(command)


def test_isolated_output_guard_rejects_outside_and_official_roots(
    tmp_path: Path,
) -> None:
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    assert_isolated_output_path(
        sandbox / "validation_outputs" / "report.pdf",
        sandbox,
    )
    with pytest.raises(ReplayCheckpointError):
        assert_isolated_output_path(
            tmp_path / "outside.pdf", sandbox
        )
    with pytest.raises(ReplayCheckpointError):
        assert_isolated_output_path(
            sandbox / "published_reports" / "report.pdf",
            sandbox,
        )


def _write_csv(
    path: Path, fieldnames: list[str], rows: list[dict[str, str]]
) -> None:
    import csv

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def test_production_workflow_checkpoint_precedes_original_step41() -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github/workflows/daily_full_pipeline.yml"
    ).read_text(encoding="utf-8")
    step40 = workflow.index("- name: Build volume breakout watch")
    capture = workflow.index(
        "- name: Create failure-safe immutable pre-step41 checkpoint"
    )
    upload = workflow.index(
        "- name: Upload failure-safe immutable pre-step41 checkpoint"
    )
    step41 = workflow.index(
        "- name: Build volume attack theme layer"
    )
    assert step40 < capture < upload < step41
    assert (
        "daily-full-pre-step41-checkpoint-"
        "${{ github.run_id }}-${{ github.run_attempt }}"
    ) in workflow
    assert "if-no-files-found: error" in workflow[capture:step41]
    assert "retention-days: 30" in workflow[capture:step41]


def test_validation_workflow_has_exact_two_mode_canary_replay_contract() -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github/workflows/"
        "daily_full_validation_replay_20260807.yml"
    ).read_text(encoding="utf-8")
    assert "default: capture_canary" in workflow
    assert workflow.count("- capture_canary") == 1
    assert workflow.count("- replay") == 1
    assert (
        workflow.index(
            "Upload immutable pre-step41 checkpoint "
            "before controlled failure"
        )
        < workflow.index(
            "Controlled canary failure after immutable checkpoint upload"
        )
    )
    assert "exit 86" in workflow
    assert "checkpoint_artifact_id" in workflow
    assert "checkpoint_artifact_digest" in workflow
    assert '[[ "$ARTIFACT_DIGEST" =~ ^[0-9a-f]{64}$ ]]' in workflow
    assert (
        "checkpoint_artifact_digest=sha256:$ARTIFACT_DIGEST"
        in workflow
    )
    assert "workflow_run.id mismatch" in workflow
    assert "artifact digest mismatch" in workflow
    assert "canary run must be completed failure" in workflow
    assert "canary run head SHA mismatch" in workflow
    assert "canary workflow path mismatch" in workflow
    assert "runs-on: windows-2025" in workflow
    assert "render-pdfs" in workflow
    assert "PyMuPDF" in workflow
    assert "pillow" in workflow
    post_upload = workflow.index(
        "- name: Upload post-step41 validation checkpoint and gates"
    )
    isolated_pdf_job = workflow.index("  isolated-six-pdf-validation:")
    post_upload_block = workflow[post_upload:isolated_pdf_job]
    assert "if: always()" in post_upload_block
    assert "post-validation-checkpoint" in post_upload_block
    assert "if-no-files-found: error" in post_upload_block
    assert "contents: write" not in workflow
    assert "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY" not in workflow


def test_workflow_step_parser_uses_original_step41_through_catalyst_gate() -> None:
    root = Path(__file__).resolve().parents[1]
    commands = replay_runner.step_map(root)
    names = replay_runner.post_step_names(root)
    assert "Build volume attack theme layer" in commands
    assert names[0] == "Build volume attack theme layer"
    assert names[-1] == "Validate catalyst layer"
    assert "Build daily candidate model layer" in names
    assert "Guard daily freshness before publishing" in names
    assert "Validate official daily PDF contract" in names
    assert all("commit" not in name.lower() for name in names)


def test_post_replay_removes_only_mutable_futures_refetch() -> None:
    source = (
        "python scripts/fetch_futures_options_indicators.py\n"
        "python scripts/build_market_regime_dashboard.py\n"
        "python scripts/validate_market_regime_dashboard.py\n"
    )
    result = replay_runner.remove_mutable_post_commands(source)
    assert "fetch_futures_options_indicators.py" not in result
    assert "build_market_regime_dashboard.py" in result
    assert "validate_market_regime_dashboard.py" in result


def test_historical_market_session_is_date_locked_not_wall_clock() -> None:
    source = (
        Path(__file__).resolve().parents[1]
        / "scripts/run_daily_full_validation_replay.py"
    ).read_text(encoding="utf-8")
    assert '"2026-08-07T23:00:00+08:00"' in source
    assert '"--assessment-date"' in source
    assert '"confirm"' in source


@pytest.mark.parametrize(
    ("market_status", "market_session_date"),
    [
        ("closed_scheduled", "20260807"),
        ("open_confirmed", "20260808"),
    ],
)
def test_historical_market_session_requires_exact_open_day(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    market_status: str,
    market_session_date: str,
) -> None:
    path = tmp_path / replay_runner.MARKET_SESSION_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "expected_main_price_date": "20260807",
                "market_status": market_status,
                "market_session_date": market_session_date,
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        replay_runner, "run_command", lambda *_args, **_kwargs: ""
    )
    with pytest.raises(replay_runner.ValidationReplayError):
        replay_runner.run_market_session_preflight(tmp_path, {})


def test_github_environment_propagates_simple_and_multiline_values(
    tmp_path: Path,
) -> None:
    github_env = tmp_path / "github_env"
    github_env.write_text(
        "SIMPLE=value\nMULTI<<END\nline1\nline2\nEND\n",
        encoding="utf-8",
    )
    env = {"GITHUB_ENV": str(github_env)}
    replay_runner.apply_github_environment(env)
    assert env["SIMPLE"] == "value"
    assert env["MULTI"] == "line1\nline2"


def test_exact_date_csv_guard_rejects_current_data_substitution(
    tmp_path: Path,
) -> None:
    path = tmp_path / "source.csv"
    _write_csv(
        path,
        ["date", "stock_id"],
        [{"date": "20260807", "stock_id": "2059"}],
    )
    replay_runner.require_csv_exact_date(
        path, "20260807", ("date",), "source"
    )
    _write_csv(
        path,
        ["date", "stock_id"],
        [{"date": "20260808", "stock_id": "2059"}],
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="not exact date",
    ):
        replay_runner.require_csv_exact_date(
            path, "20260807", ("date",), "source"
        )


def _write_registered_parity_evidence(root: Path) -> None:
    for relative_path in replay_runner.PARITY_EVIDENCE_PATHS:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"registered-validator-evidence\n")


def test_registered_parity_validators_run_in_fail_closed_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_registered_parity_evidence(tmp_path)
    calls: list[str] = []

    def fake_run_command(
        command: list[str],
        *,
        cwd: Path,
        env: dict[str, str],
        label: str,
    ) -> None:
        assert cwd == tmp_path
        assert env == {"VALIDATION_ONLY": "true"}
        assert label.startswith("registered replay parity validator:")
        calls.append(command[-1])

    monkeypatch.setattr(replay_runner, "run_command", fake_run_command)
    evidence = replay_runner.run_registered_parity_validators(
        tmp_path,
        {"VALIDATION_ONLY": "true"},
    )
    expected = [
        path.as_posix()
        for path in replay_runner.REGISTERED_PARITY_VALIDATOR_PATHS
    ]
    assert calls == expected
    assert [row["path"] for row in evidence["validators"]] == expected
    assert evidence["validation_mode"] == (
        "registered_fail_closed_validators"
    )
    assert set(evidence["artifacts"]) == {
        path.as_posix()
        for path in replay_runner.PARITY_EVIDENCE_PATHS
    }


def test_registered_parity_validator_nonzero_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[str] = []
    expected = [
        path.as_posix()
        for path in replay_runner.REGISTERED_PARITY_VALIDATOR_PATHS
    ]

    def fake_run_command(
        command: list[str],
        *,
        cwd: Path,
        env: dict[str, str],
        label: str,
    ) -> None:
        calls.append(command[-1])
        if command[-1] == expected[1]:
            raise replay_runner.ValidationReplayError(
                "registered validator exited nonzero"
            )

    monkeypatch.setattr(replay_runner, "run_command", fake_run_command)
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="exited nonzero",
    ):
        replay_runner.run_registered_parity_validators(tmp_path, {})
    assert calls == expected[:2]


def test_replay_runner_does_not_consume_governed_fields_directly() -> None:
    import ast

    source = Path(replay_runner.__file__).read_text(encoding="utf-8")
    literals = {
        node.value
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    }
    assert "final_rank_score" not in literals
    assert "warrant_flow_signal" not in literals


def test_source_state_hash_drift_fails_closed(tmp_path: Path) -> None:
    source_sha = "a" * 40
    files = {}
    for relative in (
        replay_runner.FRESHNESS_PATH,
        replay_runner.README_PATH,
        replay_runner.PACKET_PATH,
        replay_runner.MARKET_SESSION_PATH,
    ):
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{relative.as_posix()}\n", encoding="utf-8")
        files[relative.as_posix()] = {
            "bytes": path.stat().st_size,
            "sha256": replay_runner.sha256_file(path),
        }
    state_path = tmp_path / replay_runner.VALIDATION_SOURCE_STATE_PATH
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "replay_date": "20260807",
                "source_sha": source_sha,
                "source_state": {"source_commit_sha": source_sha},
                "files": files,
                "safety": {
                    "validation_only": True,
                    "official_pdf_published": False,
                    "repo_artifacts_pushed": False,
                },
            }
        ),
        encoding="utf-8",
    )
    assert replay_runner.verify_local_source_state(
        tmp_path, source_sha
    )["source_commit_sha"] == source_sha
    (tmp_path / replay_runner.README_PATH).write_text(
        "drift\n", encoding="utf-8"
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="file drift",
    ):
        replay_runner.verify_local_source_state(
            tmp_path, source_sha
        )


def test_static_validation_replay_contract_passes_current_repo() -> None:
    assert replay_validator.validate() == []


def test_lifecycle_workflow_scanner_recognizes_python_dash_b_invocations() -> None:
    invocations = lifecycle_validator.workflow_invocations()
    workflow = (
        ".github/workflows/"
        "daily_full_validation_replay_20260807.yml"
    )
    assert workflow in invocations[
        "scripts/run_daily_full_validation_replay.py"
    ]
    assert workflow in invocations[
        "scripts/validate_daily_full_validation_replay.py"
    ]


def test_authoritative_revision_extends_20260806_price_history_then_replans_exact_date(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    runner_temp = tmp_path / "runner-temp"
    repo.mkdir()
    runner_temp.mkdir()
    changed = sorted(
        set(replay_runner.PRICE_HISTORY_EXTENSION_REQUIRED_FILES)
        | {"data/stock_price_history/2330.csv"}
    )
    for relative in changed:
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("date,stock_id\n20260807,2330\n", encoding="utf-8")
    source_sha = "a" * 40
    calls: list[str] = []
    cleanup_calls: list[str] = []
    planner_calls = 0

    def fake_replay_price_date(target_date: str) -> dict:
        calls.append(f"extend:{target_date}")
        return {
            "target_date": target_date,
            "saved_price_date": target_date,
            "is_target_date": True,
            "future_rows_used": False,
            "source_responses": [
                {
                    "source_name": "TWSE_T187AP03_L",
                    "exact_date_match": True,
                    "observed_response_dates": [target_date],
                }
            ],
            "stock_history_coverage": {"missing_history_rows": 0},
        }

    monkeypatch.setattr(
        replay_runner.historical_replay,
        "previous_trading_date",
        lambda _date: "20260806",
    )
    monkeypatch.setattr(
        replay_runner.historical_replay,
        "replay_price_date",
        fake_replay_price_date,
    )
    monkeypatch.setattr(
        replay_runner.historical_replay,
        "source_tail_matrix",
        lambda: {
            "daily_price": "20260807",
            "stock_price_history": {"max_date": "20260807"},
        },
    )
    monkeypatch.setattr(
        replay_runner,
        "real_index_identity",
        lambda _repo: (tmp_path / "real-index", "c" * 64),
    )
    monkeypatch.setattr(
        replay_runner,
        "assert_real_index_unchanged",
        lambda *_args, **_kwargs: None,
    )
    monkeypatch.setattr(
        replay_runner,
        "price_extension_status_entries",
        lambda _repo: [
            {"path": path, "status": "??", "mode": "100644"}
            for path in changed
        ],
    )
    monkeypatch.setattr(
        replay_runner,
        "prepare_validation_only_git_index",
        lambda **kwargs: (
            {**kwargs["env"], "GIT_INDEX_FILE": "verified-index"},
            tmp_path / "temporary-index",
            tmp_path / "pathspec",
            tmp_path / "temporary-git-dir",
        ),
    )
    monkeypatch.setattr(
        replay_runner,
        "remove_validation_only_git_index",
        lambda **_kwargs: cleanup_calls.append("removed"),
    )

    def fake_run_command(command, *, cwd, env, label):
        nonlocal planner_calls
        calls.append(label)
        if "planner" in label:
            planner_calls += 1
            output = Path(command[command.index("--output") + 1])
            payload = (
                {
                    "should_replay": True,
                    "start_date": "20260806",
                    "end_date": "20260806",
                    "price_history_high_water_date": "20260806",
                    "required_base_date": "20260805",
                    "trading_dates": ["20260806"],
                }
                if planner_calls == 1
                else {
                    "should_replay": True,
                    "start_date": "20260806",
                    "end_date": "20260807",
                    "price_history_high_water_date": "20260807",
                    "required_base_date": "20260805",
                    "trading_dates": ["20260806", "20260807"],
                }
            )
            output.write_text(json.dumps(payload), encoding="utf-8")
        elif label == "authoritative historical source replay":
            assert env["GIT_INDEX_FILE"] == "verified-index"
            replay_id = command[command.index("--replay-id") + 1]
            manifest = (
                repo
                / "output/history/historical_source_replay"
                / replay_id
                / "20260807/structured_source_manifest.json"
            )
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(
                json.dumps(
                    {
                        "report_date": "20260807",
                        "pipeline_commit_sha": source_sha,
                        "as_published": False,
                    }
                ),
                encoding="utf-8",
            )
        return ""

    monkeypatch.setattr(replay_runner, "run_command", fake_run_command)

    plan, manifest = replay_runner.run_authoritative_historical_revision(
        repo_root=repo,
        runner_temp=runner_temp,
        env={"DAILY_FULL_VALIDATION_ONLY": "1"},
        run_id="31270000000",
        source_sha=source_sha,
    )

    assert plan["end_date"] == "20260807"
    assert plan["trading_dates"][-1] == "20260807"
    assert plan["validation_only_price_history_extension"]["initial_plan"][
        "price_history_high_water_date"
    ] == "20260806"
    assert manifest.is_file()
    assert calls.index("extend:20260807") < calls.index(
        "historical source replay planner after price extension"
    )
    assert calls.count("authoritative historical source replay") == 1
    assert cleanup_calls == ["removed"]


def test_validation_only_git_index_is_a_real_clean_synthetic_main_and_rejects_extra_drift(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    runner_temp = tmp_path / "runner-temp"
    repo.mkdir()
    runner_temp.mkdir()
    _git(repo, "init", "-q", "--initial-branch=main")
    _git(repo, "config", "user.email", "replay@example.invalid")
    _git(repo, "config", "user.name", "Replay Test")
    tracked_paths = sorted(
        (
            set(replay_runner.PRICE_HISTORY_EXTENSION_REQUIRED_FILES)
            - {
                "data/daily_price/20260807.csv",
                "data/daily_price/daily_price_20260807.csv",
            }
        )
        | {"data/stock_price_history/2330.csv", "unrelated.txt"}
    )
    for relative in tracked_paths:
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("baseline\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-qm", "baseline")
    source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    for relative in replay_runner.PRICE_HISTORY_EXTENSION_REQUIRED_FILES:
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("date,stock_id\n20260807,2330\n", encoding="utf-8")
    stock_history = repo / "data/stock_price_history/2330.csv"
    stock_history.write_text(
        "date,stock_id\n20260806,2330\n20260807,2330\n",
        encoding="utf-8",
    )
    entries = replay_runner.price_extension_status_entries(repo)
    real_index_path, real_index_sha256 = replay_runner.real_index_identity(repo)
    manifest = {
        "source_sha": source_sha,
        "real_index_path": str(real_index_path),
        "real_index_sha256": real_index_sha256,
        "files": [
            {
                **entry,
                "bytes": (repo / entry["path"]).stat().st_size,
                "sha256": replay_runner.sha256_file(repo / entry["path"]),
            }
            for entry in entries
        ],
    }
    env = os.environ.copy()
    producer_env, index_path, pathspec_path, git_dir_path = (
        replay_runner.prepare_validation_only_git_index(
            repo_root=repo,
            runner_temp=runner_temp,
            env=env,
            manifest=manifest,
        )
    )
    for args in (
        ("diff", "--cached", "--quiet"),
        ("diff", "--quiet"),
    ):
        assert subprocess.run(
            ["git", *args], cwd=repo, env=producer_env, check=False
        ).returncode == 0
    assert subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=repo,
        env=producer_env,
        check=True,
        capture_output=True,
        text=True,
    ).stdout == ""
    assert subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=repo,
        env=producer_env,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip() == "main"
    assert subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        env=producer_env,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip() == source_sha
    replay_runner.assert_real_index_unchanged(
        repo, real_index_path, real_index_sha256
    )
    replay_runner.remove_validation_only_git_index(
        repo_root=repo,
        index_path=index_path,
        pathspec_path=pathspec_path,
        git_dir_path=git_dir_path,
        real_index_path=real_index_path,
        real_index_sha256=real_index_sha256,
        source_sha=source_sha,
    )
    assert not index_path.exists()
    assert not pathspec_path.exists()
    assert not git_dir_path.exists()

    for mutation in ("head_ref", "head_tree", "index"):
        producer_env, index_path, pathspec_path, git_dir_path = (
            replay_runner.prepare_validation_only_git_index(
                repo_root=repo,
                runner_temp=runner_temp,
                env=env,
                manifest=manifest,
            )
        )
        if mutation == "head_ref":
            _git_env = producer_env
            subprocess.run(
                ["git", "update-ref", "refs/heads/not-main", "HEAD"],
                cwd=repo,
                env=_git_env,
                check=True,
            )
            subprocess.run(
                ["git", "symbolic-ref", "HEAD", "refs/heads/not-main"],
                cwd=repo,
                env=_git_env,
                check=True,
            )
            expected_error = "synthetic branch drifted"
        elif mutation == "head_tree":
            subprocess.run(
                ["git", "update-ref", "-d", f"refs/replace/{source_sha}"],
                cwd=repo,
                env=producer_env,
                check=True,
            )
            expected_error = "synthetic replace ref drifted"
        else:
            index_drift_env = producer_env.copy()
            index_drift_env["GIT_NO_REPLACE_OBJECTS"] = "1"
            subprocess.run(
                ["git", "read-tree", source_sha],
                cwd=repo,
                env=index_drift_env,
                check=True,
            )
            expected_error = "synthetic index tree drifted"
        with pytest.raises(
            replay_runner.ValidationReplayError,
            match=expected_error,
        ):
            replay_runner.assert_validation_only_git_baseline(
                repo_root=repo,
                producer_env=producer_env,
                source_sha=source_sha,
                expected_paths=[row["path"] for row in manifest["files"]],
            )
        replay_runner.remove_validation_only_git_index(
            repo_root=repo,
            index_path=index_path,
            pathspec_path=pathspec_path,
            git_dir_path=git_dir_path,
            real_index_path=real_index_path,
            real_index_sha256=real_index_sha256,
            source_sha=source_sha,
        )

    (repo / "unrelated.txt").write_text("unexpected drift\n", encoding="utf-8")
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="verify validation-only working tree baseline failed",
    ):
        replay_runner.prepare_validation_only_git_index(
            repo_root=repo,
            runner_temp=runner_temp,
            env=env,
            manifest=manifest,
        )
    replay_runner.assert_real_index_unchanged(
        repo, real_index_path, real_index_sha256
    )
    assert not (runner_temp / "price-history-extension.git-index").exists()
    assert not (runner_temp / "price-history-extension-paths.bin").exists()
    assert not (runner_temp / "price-history-extension.git-dir").exists()

    (repo / "unrelated.txt").write_text("baseline\n", encoding="utf-8")
    (repo / "unexpected-untracked.txt").write_text(
        "unexpected untracked drift\n", encoding="utf-8"
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="did not preserve an exact clean baseline",
    ):
        replay_runner.prepare_validation_only_git_index(
            repo_root=repo,
            runner_temp=runner_temp,
            env=env,
            manifest=manifest,
        )
    replay_runner.assert_real_index_unchanged(
        repo, real_index_path, real_index_sha256
    )
    assert not (runner_temp / "price-history-extension.git-index").exists()
    assert not (runner_temp / "price-history-extension-paths.bin").exists()
    assert not (runner_temp / "price-history-extension.git-dir").exists()


def test_price_history_extension_manifest_fails_closed_on_source_or_hash_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    runner_temp = tmp_path / "runner-temp"
    repo.mkdir()
    runner_temp.mkdir()
    relative = "data/daily_price/daily_price_20260807.csv"
    changed = sorted(
        set(replay_runner.PRICE_HISTORY_EXTENSION_REQUIRED_FILES)
        | {"data/stock_price_history/2330.csv"}
    )
    for changed_path in changed:
        file_path = repo / changed_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(
            "date,stock_id\n20260807,2330\n", encoding="utf-8"
        )
    path = repo / relative
    source_sha = "b" * 40
    status = {
        "target_date": "20260807",
        "saved_price_date": "20260807",
        "is_target_date": True,
        "future_rows_used": False,
        "source_responses": [
            {
                "exact_date_match": True,
                "observed_response_dates": ["20260807"],
            }
        ],
        "stock_history_coverage": {"missing_history_rows": 0},
    }
    payload = {
        "schema_version": 1,
        "mode": "validation_only_authoritative_price_history_extension",
        "replay_date": "20260807",
        "source_sha": source_sha,
        "real_index_path": str(tmp_path / "real-index"),
        "real_index_sha256": "c" * 64,
        "source_status": status,
        "files": [
            {
                "path": changed_path,
                "status": "??",
                "mode": "100644",
                "bytes": (repo / changed_path).stat().st_size,
                "sha256": replay_runner.sha256_file(repo / changed_path),
            }
            for changed_path in changed
        ],
    }
    manifest = runner_temp / replay_runner.PRICE_HISTORY_EXTENSION_MANIFEST
    manifest.write_bytes(replay_runner.canonical_json_bytes(payload))
    digest = replay_runner.sha256_file(manifest)
    monkeypatch.setattr(
        replay_runner,
        "price_extension_status_entries",
        lambda _repo: [
            {"path": changed_path, "status": "??", "mode": "100644"}
            for changed_path in changed
        ],
    )

    assert replay_runner.verify_price_history_extension_manifest(
        repo_root=repo,
        manifest_path=manifest,
        expected_manifest_sha256=digest,
        source_sha=source_sha,
    )["replay_date"] == "20260807"

    monkeypatch.setattr(
        replay_runner,
        "price_extension_status_entries",
        lambda _repo: [
            *[
                {"path": changed_path, "status": "??", "mode": "100644"}
                for changed_path in changed
            ],
            {
                "path": "output/latest/unapproved.csv",
                "status": "??",
                "mode": "100644",
            },
        ],
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="path set drift",
    ):
        replay_runner.verify_price_history_extension_manifest(
            repo_root=repo,
            manifest_path=manifest,
            expected_manifest_sha256=digest,
            source_sha=source_sha,
        )

    monkeypatch.setattr(
        replay_runner,
        "price_extension_status_entries",
        lambda _repo: [
            {
                "path": changed_path,
                "status": "??",
                "mode": "100755" if changed_path == relative else "100644",
            }
            for changed_path in changed
        ],
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="status/mode mismatch",
    ):
        replay_runner.verify_price_history_extension_manifest(
            repo_root=repo,
            manifest_path=manifest,
            expected_manifest_sha256=digest,
            source_sha=source_sha,
        )

    monkeypatch.setattr(
        replay_runner,
        "price_extension_status_entries",
        lambda _repo: [
            {"path": changed_path, "status": "??", "mode": "100644"}
            for changed_path in changed
        ],
    )

    path.write_text("date,stock_id\n20260806,2330\n", encoding="utf-8")
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="byte mismatch|hash mismatch",
    ):
        replay_runner.verify_price_history_extension_manifest(
            repo_root=repo,
            manifest_path=manifest,
            expected_manifest_sha256=digest,
            source_sha=source_sha,
        )

    bad_status = {**status, "source_responses": []}
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="lacks exact-date source evidence",
    ):
        replay_runner._validate_price_history_extension_status(bad_status)

    wrong_date_status = {
        **status,
        "target_date": "20260806",
        "saved_price_date": "20260806",
    }
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="wrong-date",
    ):
        replay_runner._validate_price_history_extension_status(wrong_date_status)

    monkeypatch.setattr(
        replay_runner,
        "real_index_identity",
        lambda _repo: (tmp_path / "real-index", "d" * 64),
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="real Git index drifted",
    ):
        replay_runner.assert_real_index_unchanged(
            repo,
            tmp_path / "real-index",
            "c" * 64,
        )
