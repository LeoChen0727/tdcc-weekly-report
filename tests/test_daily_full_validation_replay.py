from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import stat
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


def _source_revision_identity_fixture(
    tmp_path: Path,
) -> tuple[Path, Path, dict[str, object], str, Path]:
    repo = tmp_path / "identity-repo"
    bundle = tmp_path / "identity-bundle"
    repo.mkdir()
    bundle.mkdir()
    source_sha = "4" * 40
    structured_relative = (
        "output/history/historical_source_replay/test-authoritative-r1/"
        f"{REPLAY_DATE}/structured_source_manifest.json"
    )
    structured_path = repo / structured_relative
    structured_path.parent.mkdir(parents=True)
    structured_path.write_bytes(
        replay_runner.canonical_json_bytes(
            {
                "schema_version": 1,
                "report_date": REPLAY_DATE,
                "pipeline_commit_sha": source_sha,
            }
        )
    )
    structured_sha = hashlib.sha256(structured_path.read_bytes()).hexdigest()
    source_artifact_relative = "data/source.csv"
    source_artifact = repo / source_artifact_relative
    source_artifact.parent.mkdir(parents=True)
    source_artifact.write_text(
        f"date,value\n{REPLAY_DATE},official\n", encoding="utf-8"
    )
    source_artifact_sha = hashlib.sha256(
        source_artifact.read_bytes()
    ).hexdigest()
    source_payload = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "revision_kind": "authoritative_historical_revision",
        "source_sha": source_sha,
        "sources": [
            {
                "artifact_path": source_artifact_relative,
                "bytes": source_artifact.stat().st_size,
                "category": "official_test_source",
                "identity": f"official_test_source:{source_artifact_sha}",
                "sha256": source_artifact_sha,
                "source_url": "https://official.example.invalid/source",
            }
        ],
        "structured_source_manifest": {
            "bytes": structured_path.stat().st_size,
            "path": structured_relative,
            "sha256": structured_sha,
        },
    }
    source_path = bundle / replay_runner.SOURCE_REVISION_FILENAME
    source_path.write_bytes(replay_runner.canonical_json_bytes(source_payload))
    source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    checkpoint_manifest: dict[str, object] = {
        "source_revision_manifest": {
            "bytes": source_path.stat().st_size,
            "path": replay_runner.SOURCE_REVISION_FILENAME,
            "sha256": source_sha256,
        },
        "files": [
            {
                "bytes": structured_path.stat().st_size,
                "path": structured_relative,
                "sha256": structured_sha,
            }
        ],
    }
    return repo, bundle, checkpoint_manifest, source_sha, source_path


def test_checkpoint_source_revision_identity_uses_exact_canonical_object(
    tmp_path: Path,
) -> None:
    repo, bundle, manifest, source_sha, source_path = (
        _source_revision_identity_fixture(tmp_path)
    )
    structured_path = repo / manifest["files"][0]["path"]
    observed = replay_runner.require_checkpoint_source_revision_manifest_identity(
        bundle_dir=bundle,
        repo_root=repo,
        checkpoint_manifest=manifest,
        checkpoint_source_sha=source_sha,
        structured_source_manifest=structured_path,
    )
    assert observed == source_path
    assert source_path.read_bytes() == replay_runner.canonical_json_bytes(
        json.loads(source_path.read_text(encoding="utf-8"))
    )


@pytest.mark.parametrize(
    "mutation,match",
    [
        ("wrong_object", "path/object mismatch"),
        ("wrong_path", "path/object mismatch"),
        ("wrong_date", "date mismatch"),
        ("wrong_source_sha", "source SHA mismatch"),
        ("wrong_mode", "mode mismatch"),
        ("wrong_content", "raw bytes/SHA mismatch"),
        ("noncanonical", "raw/canonical SHA mismatch"),
    ],
)
def test_checkpoint_source_revision_identity_rejects_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
    match: str,
) -> None:
    repo, bundle, manifest, source_sha, source_path = (
        _source_revision_identity_fixture(tmp_path)
    )
    metadata = manifest["source_revision_manifest"]
    assert isinstance(metadata, dict)
    structured_path = repo / manifest["files"][0]["path"]
    if mutation == "wrong_object":
        other = bundle / "structured_source_manifest.json"
        other.write_bytes(source_path.read_bytes())
        metadata["path"] = other.name
    elif mutation == "wrong_path":
        metadata["path"] = "nested/source_revision_manifest.json"
    elif mutation == "wrong_date":
        payload = json.loads(source_path.read_text(encoding="utf-8"))
        payload["replay_date"] = "20260806"
        source_path.write_bytes(replay_runner.canonical_json_bytes(payload))
        metadata["bytes"] = source_path.stat().st_size
        metadata["sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
    elif mutation == "wrong_source_sha":
        payload = json.loads(source_path.read_text(encoding="utf-8"))
        payload["source_sha"] = "f" * 40
        source_path.write_bytes(replay_runner.canonical_json_bytes(payload))
        metadata["bytes"] = source_path.stat().st_size
        metadata["sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
    elif mutation == "wrong_mode":
        real_mode = replay_runner.checkpoint_manifest_file_mode
        monkeypatch.setattr(
            replay_runner,
            "checkpoint_manifest_file_mode",
            lambda path: (
                stat.S_IFREG | 0o755
                if path == source_path
                else real_mode(path)
            ),
        )
    elif mutation == "wrong_content":
        source_path.write_bytes(source_path.read_bytes() + b"drift")
    elif mutation == "noncanonical":
        payload = json.loads(source_path.read_text(encoding="utf-8"))
        source_path.write_text(
            json.dumps(payload, indent=2), encoding="utf-8", newline="\n"
        )
        metadata["bytes"] = source_path.stat().st_size
        metadata["sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
    with pytest.raises(replay_runner.ValidationReplayError, match=match):
        replay_runner.require_checkpoint_source_revision_manifest_identity(
            bundle_dir=bundle,
            repo_root=repo,
            checkpoint_manifest=manifest,
            checkpoint_source_sha=source_sha,
            structured_source_manifest=structured_path,
        )


def test_replay_checkpoint_capture_uses_revision_and_structured_identities(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _bundle, _manifest, checkpoint_sha, source_path = (
        _source_revision_identity_fixture(tmp_path)
    )
    structured_path = next(
        repo.glob(
            "output/history/historical_source_replay/*/"
            f"{REPLAY_DATE}/structured_source_manifest.json"
        )
    )
    replay_sha = "5" * 40
    replay_manifest = replay_runner.write_replay_source_revision_manifest(
        source_manifest_path=source_path,
        output_path=tmp_path / "replay-source.json",
        transition={
            "checkpoint_source_sha": checkpoint_sha,
            "replay_source_sha": replay_sha,
        },
    )
    observed: dict[str, object] = {}
    monkeypatch.setattr(
        replay_runner,
        "checkpoint_paths",
        lambda _repo, required: sorted(set(required)),
    )

    def fake_create_checkpoint(**kwargs: object) -> dict[str, object]:
        observed.update(kwargs)
        return {"files": []}

    monkeypatch.setattr(
        replay_runner.checkpoint,
        "create_checkpoint",
        fake_create_checkpoint,
    )
    replay_runner.capture_checkpoint(
        repo_root=repo,
        bundle_dir=tmp_path / "post-bundle",
        runner_temp=tmp_path / "runner-temp",
        source_sha=replay_sha,
        run_id="31291570842",
        structured_manifest_path=structured_path,
        revision_kind="authoritative_historical_revision",
        checkpoint_kind="post_validation",
        capture_context="validation_replay",
        producer_steps=["Validate catalyst layer"],
        source_revision_manifest_path=replay_manifest,
    )
    assert observed["source_identity_manifest"] == replay_manifest
    assert "data/source.csv" in observed["paths"]
    assert structured_path.relative_to(repo).as_posix() in observed["paths"]


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
    assert (
        'default: "4d715065f38389752aaeaa0c511280c47ccedc08"'
        in workflow
    )
    assert (
        "CHECKPOINT_SOURCE_SHA: ${{ inputs.checkpoint_source_sha }}"
        in workflow
    )
    assert '--checkpoint-source-sha "$CHECKPOINT_SOURCE_SHA"' in workflow
    assert '--checkpoint-artifact-id "$CHECKPOINT_ARTIFACT_ID"' in workflow
    assert '--checkpoint-artifact-digest "$CHECKPOINT_ARTIFACT_DIGEST"' in workflow
    assert "checkpoint replay source transition mismatch" in workflow


@pytest.mark.parametrize(
    "invalid_default",
    ["", "0" * 40],
)
def test_replay_workflow_rejects_omitted_or_wrong_checkpoint_source_default(
    invalid_default: str,
) -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github/workflows/daily_full_validation_replay_20260807.yml"
    ).read_text(encoding="utf-8")
    expected = replay_validator.AUTHORIZED_CHECKPOINT_SOURCE_SHA
    mutated = workflow.replace(
        f'default: "{expected}"',
        f'default: "{invalid_default}"',
        1,
    )
    assert mutated != workflow
    errors: list[str] = []
    replay_validator.validate_replay_workflow(mutated, errors)
    assert errors == [
        "validation replay checkpoint_source_sha must default to "
        "the exact immutable checkpoint source SHA"
    ]


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
        checkpoint_source_sha="2" * 40,
        structured_source_manifest=tmp_path / "structured.json",
        replay_source_manifest=None,
        failure_phase="verify checkpoint source revision manifest",
        steps=[{"step": "Guard", "status": "failure"}],
        error=replay_runner.ValidationReplayError("guard failed"),
    )
    assert observed["checkpoint_kind"] == "post_validation"
    assert observed["capture_context"] == "validation_replay"
    assert bundle.is_dir()
    payload = json.loads(
        (repo / replay_runner.STEP_RESULTS_PATH).read_text(encoding="utf-8")
    )
    assert payload["mode"] == "replay_failure"
    assert payload["error"] == "guard failed"
    assert payload["checkpoint_source_sha"] == "2" * 40
    assert payload["failure_phase"] == (
        "verify checkpoint source revision manifest"
    )
    assert observed["structured_manifest_path"] == (
        tmp_path / "structured.json"
    )
    assert observed["source_revision_manifest_path"] is None


def test_replay_source_manifest_failure_is_captured_before_rethrow(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    post_bundle = tmp_path / "post-bundle"
    source_sha = "3" * 40
    checkpoint_source_sha = "4" * 40
    observed: dict[str, object] = {}
    monkeypatch.setattr(replay_runner, "require_main_source", lambda *_: None)
    monkeypatch.setattr(
        replay_runner,
        "require_authorized_checkpoint_revision_transition",
        lambda **_: {
            "mode": "authorized_code_revision_transition",
            "checkpoint_source_sha": checkpoint_source_sha,
            "replay_source_sha": source_sha,
        },
    )
    monkeypatch.setattr(
        replay_runner,
        "require_authorized_checkpoint_bundle_identity",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay_runner.checkpoint,
        "restore_checkpoint",
        lambda **_: {"source_revision_manifest": {}, "files": []},
    )
    monkeypatch.setattr(
        replay_runner,
        "require_checkpoint_structured_source_manifest_identity",
        lambda **_: repo / "structured.json",
    )
    monkeypatch.setattr(
        replay_runner,
        "require_checkpoint_source_revision_manifest_identity",
        lambda **_: (_ for _ in ()).throw(
            replay_runner.ValidationReplayError("early identity failure")
        ),
    )

    def fake_capture(**kwargs: object) -> dict[str, object]:
        observed.update(kwargs)
        post_bundle.mkdir()
        (post_bundle / "failure.json").write_text(
            "{}\n", encoding="utf-8"
        )
        return {"files": []}

    monkeypatch.setattr(
        replay_runner, "capture_replay_failure_checkpoint", fake_capture
    )
    args = argparse.Namespace(
        repo_root=repo,
        runner_temp=tmp_path / "runner-temp",
        source_sha=source_sha,
        checkpoint_source_sha=checkpoint_source_sha,
        replay_date=REPLAY_DATE,
        checkpoint_run_id="31268964962",
        checkpoint_artifact_id="9025240156",
        checkpoint_artifact_digest=(
            replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
        ),
        bundle_dir=bundle,
        post_bundle_dir=post_bundle,
        run_id="31291570842",
    )
    with pytest.raises(
        replay_runner.ValidationReplayError, match="early identity failure"
    ):
        replay_runner.replay_from_checkpoint(args)
    assert observed["replay_source_manifest"] is None
    assert observed["failure_phase"] == (
        "verify checkpoint source revision manifest"
    )
    assert post_bundle.is_dir()


def test_minimal_replay_failure_receipt_preserves_original_error(
    tmp_path: Path,
) -> None:
    bundle = tmp_path / "failure-bundle"
    path = replay_runner.write_minimal_replay_failure_upload_receipt(
        bundle_dir=bundle,
        source_sha="3" * 40,
        checkpoint_source_sha="4" * 40,
        run_id="31291570842",
        failure_phase="verify checkpoint source revision manifest",
        error=replay_runner.ValidationReplayError("identity mismatch"),
        capture_error=replay_runner.ValidationReplayError(
            "full checkpoint unavailable"
        ),
    )
    payload = json.loads(path.read_text(encoding="utf-8"))
    sidecar = bundle / "replay_failure_evidence.json.sha256"
    assert payload["error"] == "identity mismatch"
    assert payload["full_checkpoint_capture_error"] == (
        "full checkpoint unavailable"
    )
    assert sidecar.read_text(encoding="ascii").strip() == hashlib.sha256(
        path.read_bytes()
    ).hexdigest()


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


@pytest.mark.parametrize("stream_name", ["stdout", "stderr"])
def test_renderer_output_is_utf8_safe_under_windows_cp1252(
    stream_name: str,
) -> None:
    raw = io.BytesIO()
    stream = io.TextIOWrapper(raw, encoding="cp1252", newline="")
    try:
        replay_runner.emit_utf8_safe_text(
            f"{stream_name}: 已產生六份隔離測試 PDF",
            stream=stream,
        )
        stream.flush()
        assert raw.getvalue().decode("utf-8") == (
            f"{stream_name}: 已產生六份隔離測試 PDF\n"
        )
    finally:
        stream.detach()


def test_replay_validator_rejects_locale_bound_renderer_output() -> None:
    runner = (
        Path(__file__).resolve().parents[1]
        / "scripts/run_daily_full_validation_replay.py"
    ).read_text(encoding="utf-8")
    mutated = runner.replace(
        "emit_utf8_safe_text(rendered_stdout, stream=sys.stdout)",
        "print(rendered_stdout.rstrip())",
        1,
    )
    assert mutated != runner
    errors: list[str] = []
    replay_validator.validate_runner(mutated, errors)
    assert (
        "validation replay renderer output must not use locale-bound print"
        in errors
    )


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
    calls: list[list[str]] = []

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
        calls.append(command[2:])

    monkeypatch.setattr(replay_runner, "run_command", fake_run_command)
    evidence = replay_runner.run_registered_parity_validators(
        tmp_path,
        {"VALIDATION_ONLY": "true"},
    )
    expected = [
        [
            path.as_posix(),
            *replay_runner.REGISTERED_PARITY_VALIDATOR_ARGUMENTS[path],
        ]
        for path in replay_runner.REGISTERED_PARITY_VALIDATOR_PATHS
    ]
    assert calls == expected
    assert [row["path"] for row in evidence["validators"]] == [
        path.as_posix()
        for path in replay_runner.REGISTERED_PARITY_VALIDATOR_PATHS
    ]
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
        calls.append(command[2])
        if command[2] == expected[1]:
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


def test_checkpoint_deletion_manifest_roundtrip_is_exact_and_fail_closed(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "replay@example.invalid")
    _git(repo, "config", "user.name", "Replay Test")
    _git(repo, "config", "core.autocrlf", "false")
    relative = "docs/latest/1216_統一_stale_daily_readme.txt"
    baseline = b"stale tracked source\n"
    target = repo / relative
    target.parent.mkdir(parents=True)
    (repo / ".gitattributes").write_text(
        "docs/latest/*.txt text eol=lf\n", encoding="ascii"
    )
    target.write_bytes(baseline)
    _git(repo, "add", ".gitattributes", relative)
    _git(repo, "commit", "-qm", "baseline")
    source_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    target.unlink()

    manifest_path = replay_runner.write_checkpoint_deletion_manifest(
        repo, source_sha, [relative]
    )
    manifest_raw = manifest_path.read_bytes()
    manifest = json.loads(manifest_raw.decode("utf-8"))
    assert manifest_raw == replay_runner.canonical_json_bytes(manifest)
    assert manifest["replay_date"] == "20260807"
    assert manifest["source_sha"] == source_sha
    assert manifest["deletions"][0]["path"] == relative
    assert manifest["deletions"][0]["mode"] == "100644"
    assert manifest["deletions"][0]["bytes"] == len(baseline)
    assert manifest["deletions"][0]["sha256"] == hashlib.sha256(
        baseline
    ).hexdigest()

    target.write_bytes(baseline)
    assert replay_runner.apply_checkpoint_deletions(repo, source_sha) == [
        relative
    ]
    assert not target.exists()

    target.write_bytes(baseline.replace(b"\n", b"\r\n"))
    assert replay_runner.apply_checkpoint_deletions(repo, source_sha) == [
        relative
    ]
    assert not target.exists()

    target.write_bytes(b"wrong current bytes\n")
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="baseline content drift",
    ):
        replay_runner.apply_checkpoint_deletions(repo, source_sha)
    target.write_bytes(baseline)

    changed = dict(manifest)
    changed["replay_date"] = "20260808"
    manifest_path.write_bytes(replay_runner.canonical_json_bytes(changed))
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="manifest identity mismatch",
    ):
        replay_runner.apply_checkpoint_deletions(repo, source_sha)

    changed = json.loads(json.dumps(manifest))
    changed["deletions"][0]["mode"] = "100755"
    manifest_path.write_bytes(replay_runner.canonical_json_bytes(changed))
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="source identity drift",
    ):
        replay_runner.apply_checkpoint_deletions(repo, source_sha)

    changed = json.loads(json.dumps(manifest))
    changed["deletions"][0]["path"] = "docs/latest/other.txt"
    manifest_path.write_bytes(replay_runner.canonical_json_bytes(changed))
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="source object is missing",
    ):
        replay_runner.apply_checkpoint_deletions(repo, source_sha)


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


def _validation_readme_fixture(
    tmp_path: Path,
) -> tuple[Path, str, str, dict[str, str]]:
    repo = tmp_path / "validation-readme-repo"
    freshness = repo / replay_runner.FRESHNESS_PATH
    freshness.parent.mkdir(parents=True)
    columns = [
        "expected_main_price_date",
        "main_price_date",
        "stock_monitor_price_date",
        "all_candidates_date",
        "official_price_fetch_date",
        "warrant_flow_date",
        "report_ready",
        "warrant_ready",
        "daily_pdf_ready",
        "warrant_source_status",
        "warrant_pdf_visibility",
    ]
    values = [
        REPLAY_DATE,
        REPLAY_DATE,
        REPLAY_DATE,
        REPLAY_DATE,
        REPLAY_DATE,
        REPLAY_DATE,
        "True",
        "True",
        "True",
        "ok",
        "visible",
    ]
    freshness.write_text(
        ",".join(columns) + "\n" + ",".join(values) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    market = repo / replay_runner.MARKET_SESSION_PATH
    market.parent.mkdir(parents=True, exist_ok=True)
    market.write_text(
        json.dumps(
            {
                "market_status": "open_confirmed",
                "market_session_date": REPLAY_DATE,
                "expected_main_price_date": REPLAY_DATE,
            }
        ),
        encoding="utf-8",
    )
    packet = repo / replay_runner.PACKET_PATH
    packet.parent.mkdir(parents=True, exist_ok=True)
    packet.write_text("validation packet\n", encoding="utf-8")
    replay_source_sha = "a" * 40
    checkpoint_source_sha = "b" * 40
    transition = {
        "mode": "authorized_code_revision_transition",
        "checkpoint_source_sha": checkpoint_source_sha,
        "replay_source_sha": replay_source_sha,
    }
    return repo, replay_source_sha, checkpoint_source_sha, transition


def test_validation_only_pdf_source_readme_is_date_and_revision_locked(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert replay_runner.PACKET_PATH.as_posix() == (
        "output/latest/chatgpt_daily_report_packet_latest.txt"
    )
    repo, replay_sha, checkpoint_sha, transition = (
        _validation_readme_fixture(tmp_path)
    )
    monkeypatch.setenv("DAILY_FULL_VALIDATION_ONLY", "1")
    path = replay_runner.write_validation_only_pdf_source_readme(
        repo_root=repo,
        replay_source_sha=replay_sha,
        transition=transition,
        validation_env={"DAILY_FULL_VALIDATION_ONLY": "1"},
    )
    fields = replay_runner.read_key_value_file(path)
    assert fields["main_price_date"] == REPLAY_DATE
    assert fields["validation_only"] == "true"
    assert fields["official_pdf_published"] == "false"
    assert fields["checkpoint_source_sha"] == checkpoint_sha
    assert fields["replay_source_sha"] == replay_sha
    payload = replay_runner.write_validation_source_state(
        repo, replay_sha, transition
    )
    assert payload["source_state"]["readme_fields"] == fields
    assert payload["files"][replay_runner.README_PATH.as_posix()][
        "sha256"
    ] == hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.mark.parametrize(
    ("mutation", "match"),
    [
        ("mode", "requires validation-only mode"),
        ("date", "freshness date mismatch"),
        ("market", "market date mismatch"),
        ("packet", "PDF source-gate artifact missing"),
    ],
)
def test_validation_only_pdf_source_readme_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
    match: str,
) -> None:
    repo, replay_sha, _checkpoint_sha, transition = (
        _validation_readme_fixture(tmp_path)
    )
    monkeypatch.setenv("DAILY_FULL_VALIDATION_ONLY", "1")
    if mutation == "mode":
        monkeypatch.delenv("DAILY_FULL_VALIDATION_ONLY")
    elif mutation == "date":
        path = repo / replay_runner.FRESHNESS_PATH
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                REPLAY_DATE, "20260806", 1
            ),
            encoding="utf-8",
        )
    elif mutation == "market":
        path = repo / replay_runner.MARKET_SESSION_PATH
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["expected_main_price_date"] = "20260806"
        path.write_text(json.dumps(payload), encoding="utf-8")
    elif mutation == "packet":
        (repo / replay_runner.PACKET_PATH).unlink()
    with pytest.raises(replay_runner.ValidationReplayError, match=match):
        replay_runner.write_validation_only_pdf_source_readme(
            repo_root=repo,
            replay_source_sha=replay_sha,
            transition=transition,
            validation_env=(
                {}
                if mutation == "mode"
                else {"DAILY_FULL_VALIDATION_ONLY": "1"}
            ),
        )


def test_validation_source_state_rejects_tampered_validation_readme(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, replay_sha, checkpoint_sha, transition = (
        _validation_readme_fixture(tmp_path)
    )
    monkeypatch.setenv("DAILY_FULL_VALIDATION_ONLY", "1")
    path = replay_runner.write_validation_only_pdf_source_readme(
        repo_root=repo,
        replay_source_sha=replay_sha,
        transition=transition,
        validation_env={"DAILY_FULL_VALIDATION_ONLY": "1"},
    )
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            f"replay_source_sha={replay_sha}",
            f"replay_source_sha={'c' * 40}",
        ),
        encoding="utf-8",
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="README identity mismatch",
    ):
        replay_runner.require_freshness_contract(
            repo, replay_sha, checkpoint_sha
        )


def test_post_step_source_gate_failure_is_captured_before_rethrow(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    market = repo / replay_runner.MARKET_SESSION_PATH
    market.parent.mkdir(parents=True)
    market.write_text(
        json.dumps(
            {
                "market_status": "open_confirmed",
                "market_session_date": REPLAY_DATE,
            }
        ),
        encoding="utf-8",
    )
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    post_bundle = tmp_path / "post-bundle"
    replay_sha = "d" * 40
    checkpoint_sha = "e" * 40
    transition = {
        "mode": "authorized_code_revision_transition",
        "checkpoint_source_sha": checkpoint_sha,
        "replay_source_sha": replay_sha,
    }
    observed: dict[str, object] = {}
    monkeypatch.setattr(replay_runner, "require_main_source", lambda *_: None)
    monkeypatch.setattr(
        replay_runner,
        "require_authorized_checkpoint_revision_transition",
        lambda **_: transition,
    )
    monkeypatch.setattr(
        replay_runner,
        "require_authorized_checkpoint_bundle_identity",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay_runner.checkpoint,
        "restore_checkpoint",
        lambda **_: {"source_revision_manifest": {}, "files": []},
    )
    monkeypatch.setattr(
        replay_runner,
        "require_checkpoint_structured_source_manifest_identity",
        lambda **_: repo / "structured.json",
    )
    monkeypatch.setattr(
        replay_runner,
        "require_checkpoint_source_revision_manifest_identity",
        lambda **_: repo / "source-revision.json",
    )
    monkeypatch.setattr(
        replay_runner,
        "write_replay_source_revision_manifest",
        lambda **_: repo / "replay-source.json",
    )
    monkeypatch.setattr(
        replay_runner,
        "materialize_publish_freshness_baseline",
        lambda **_: {},
    )
    monkeypatch.setattr(
        replay_runner,
        "base_environment",
        lambda **_: {"DAILY_FULL_VALIDATION_ONLY": "1"},
    )
    monkeypatch.setattr(replay_runner, "post_step_names", lambda *_: [])
    monkeypatch.setattr(replay_runner, "run_named_steps", lambda **_: None)
    monkeypatch.setattr(
        replay_runner,
        "run_registered_parity_validators",
        lambda *_: [],
    )
    monkeypatch.setattr(
        replay_runner,
        "write_validation_only_pdf_source_readme",
        lambda **_: (_ for _ in ()).throw(
            replay_runner.ValidationReplayError("source gate failed")
        ),
    )

    def fake_capture(**kwargs: object) -> dict[str, object]:
        observed.update(kwargs)
        post_bundle.mkdir()
        (post_bundle / "failure.json").write_text(
            "{}\n", encoding="utf-8"
        )
        return {"files": []}

    monkeypatch.setattr(
        replay_runner, "capture_replay_failure_checkpoint", fake_capture
    )
    args = argparse.Namespace(
        repo_root=repo,
        runner_temp=tmp_path / "runner-temp",
        source_sha=replay_sha,
        checkpoint_source_sha=checkpoint_sha,
        replay_date=REPLAY_DATE,
        checkpoint_run_id="31268964962",
        checkpoint_artifact_id="9025240156",
        checkpoint_artifact_digest=(
            replay_runner.AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
        ),
        bundle_dir=bundle,
        post_bundle_dir=post_bundle,
        run_id="31291570843",
    )
    with pytest.raises(
        replay_runner.ValidationReplayError, match="source gate failed"
    ):
        replay_runner.replay_from_checkpoint(args)
    assert observed["failure_phase"] == (
        "materialize validation-only PDF source README"
    )
    assert post_bundle.is_dir()


def test_20260810_profile_is_exact_and_default_profile_is_unchanged() -> None:
    old = replay_runner.replay_profile("20260807")
    current = replay_runner.replay_profile("20260810")

    assert old["checkpoint_run_id"] == "31268964962"
    assert old["checkpoint_capture_context"] == "validation_canary"
    assert old["market_session_validation_scope"] == (
        "authoritative_historical_revision"
    )
    assert current["checkpoint_source_sha"] == (
        "bf04304b0dafc480c690a8d5c9c53aa70634b7f2"
    )
    assert current["checkpoint_run_id"] == "31384317163"
    assert current["checkpoint_artifact_id"] == "9061570264"
    assert current["checkpoint_artifact_digest"] == (
        "sha256:"
        "87a586726d64300371a77fddf92f892357732cc754395aac3f3d872465ac49f4"
    )
    assert current["checkpoint_manifest_sha256"] == (
        "fd72454a5711225d93e85c22881c35b9f8a91f5d8ab3898f9d7f47c729a806d3"
    )
    assert current["checkpoint_capture_context"] == "production_pre_step41"
    assert current["checkpoint_revision_kind"] == "live_production_capture"
    assert current["market_session_validation_scope"] == (
        "live_production_capture"
    )
    assert current["original_failure_stock_id"] == "6152"
    with pytest.raises(RuntimeError, match="unsupported"):
        replay_runner.replay_profile("20260811")


def test_checkpoint_source_reconciliation_uses_payload_and_git_objects(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    def git(*arguments: str) -> str:
        result = replay_runner.subprocess.run(
            ["git", *arguments],
            cwd=repo,
            check=False,
            text=True,
            encoding="utf-8",
            stdout=replay_runner.subprocess.PIPE,
            stderr=replay_runner.subprocess.STDOUT,
        )
        assert result.returncode == 0, result.stdout
        return result.stdout.strip()

    git("init")
    git("config", "user.name", "Replay Test")
    git("config", "user.email", "replay@example.invalid")
    (repo / "output/latest").mkdir(parents=True)
    (repo / "scripts").mkdir()
    (repo / "output/latest/mutable.csv").write_text(
        "date,value\n20260810,checkpoint-source\n", encoding="utf-8"
    )
    (repo / "output/latest/checkpoint.csv").write_text(
        "date,value\n20260810,checkpoint-source\n", encoding="utf-8"
    )
    (repo / "scripts/model.py").write_text("VALUE = 'old'\n", encoding="utf-8")
    git("add", ".")
    git("commit", "-m", "checkpoint source")
    checkpoint_source_sha = git("rev-parse", "HEAD")

    (repo / "output/latest/mutable.csv").write_text(
        "date,value\n20260810,mutable-latest\n", encoding="utf-8"
    )
    (repo / "output/latest/checkpoint.csv").write_text(
        "date,value\n20260810,mutable-latest\n", encoding="utf-8"
    )
    (repo / "output/latest/added.csv").write_text(
        "date,value\n20260810,latest-only\n", encoding="utf-8"
    )
    (repo / "scripts/model.py").write_text(
        "VALUE = 'fixed'\n", encoding="utf-8"
    )
    git("add", ".")
    git("commit", "-m", "replay source")
    replay_source_sha = git("rev-parse", "HEAD")

    payload = b"date,value\n20260810,immutable-checkpoint\n"
    (repo / "output/latest/checkpoint.csv").write_bytes(payload)
    manifest = {
        "files": [
            {
                "path": "output/latest/checkpoint.csv",
                "bytes": len(payload),
                "sha256": replay_runner.hashlib.sha256(payload).hexdigest(),
            }
        ]
    }
    transition = {
        "checkpoint_source_sha": checkpoint_source_sha,
        "replay_source_sha": replay_source_sha,
        "changed_paths": [
            "output/latest/added.csv",
            "output/latest/checkpoint.csv",
            "output/latest/mutable.csv",
            "scripts/model.py",
        ],
        "authorized_live_paths": ["scripts/model.py"],
        "checkpoint_source_restore_paths": [
            "output/latest/added.csv",
            "output/latest/checkpoint.csv",
            "output/latest/mutable.csv",
        ],
    }

    evidence = replay_runner.reconcile_checkpoint_source_state(
        repo_root=repo,
        checkpoint_manifest=manifest,
        transition=transition,
    )

    assert (repo / "scripts/model.py").read_text(encoding="utf-8") == (
        "VALUE = 'fixed'\n"
    )
    assert (repo / "output/latest/checkpoint.csv").read_bytes() == payload
    assert (repo / "output/latest/mutable.csv").read_text(
        encoding="utf-8"
    ) == "date,value\n20260810,checkpoint-source\n"
    assert not (repo / "output/latest/added.csv").exists()
    assert evidence["mutable_latest_fallback_allowed"] is False
    assert {row["source"] for row in evidence["files"]} == {
        "checkpoint_source_git_object",
        "immutable_checkpoint_payload",
        "replay_source_git_object",
    }


def test_checkpoint_source_reconciliation_rejects_non_artifact_restore_path(
    tmp_path: Path,
) -> None:
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="outside immutable artifact roots",
    ):
        replay_runner.reconcile_checkpoint_source_state(
            repo_root=tmp_path,
            checkpoint_manifest={"files": []},
            transition={
                "checkpoint_source_sha": "a" * 40,
                "replay_source_sha": "b" * 40,
                "changed_paths": ["rules/contract.md"],
                "authorized_live_paths": [],
                "checkpoint_source_restore_paths": ["rules/contract.md"],
            },
        )


def test_20260810_revision_transition_requires_checkpoint_ancestry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    def git(*arguments: str) -> str:
        result = replay_runner.subprocess.run(
            ["git", *arguments],
            cwd=repo,
            check=False,
            text=True,
            encoding="utf-8",
            stdout=replay_runner.subprocess.PIPE,
            stderr=replay_runner.subprocess.STDOUT,
        )
        assert result.returncode == 0, result.stdout
        return result.stdout.strip()

    git("init")
    git("config", "user.name", "Replay Test")
    git("config", "user.email", "replay@example.invalid")
    (repo / "scripts").mkdir()
    (repo / "output/latest").mkdir(parents=True)
    (repo / "scripts/model.py").write_text("VALUE = 'old'\n", encoding="utf-8")
    (repo / "scripts/control.py").write_text("VALUE = 'old'\n", encoding="utf-8")
    (repo / "output/latest/state.csv").write_text("old\n", encoding="utf-8")
    git("add", ".")
    git("commit", "-m", "checkpoint source")
    checkpoint_source_sha = git("rev-parse", "HEAD")

    (repo / "scripts/model.py").write_text("VALUE = 'fixed'\n", encoding="utf-8")
    git("add", ".")
    git("commit", "-m", "model fix")
    model_fix_sha = git("rev-parse", "HEAD")

    (repo / "scripts/control.py").write_text(
        "VALUE = 'replay'\n", encoding="utf-8"
    )
    (repo / "output/latest/state.csv").write_text(
        "mutable latest\n", encoding="utf-8"
    )
    git("add", ".")
    git("commit", "-m", "replay control")
    replay_source_sha = git("rev-parse", "HEAD")

    monkeypatch.setattr(replay_runner, "REPLAY_DATE", "20260810")
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_SOURCE_SHA",
        checkpoint_source_sha,
    )
    monkeypatch.setattr(replay_runner, "AUTHORIZED_CHECKPOINT_RUN_ID", "1")
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_CHECKPOINT_ARTIFACT_ID", "2"
    )
    digest = "sha256:" + "a" * 64
    monkeypatch.setattr(
        replay_runner, "AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST", digest
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_20260810_MODEL_FIX_COMMIT",
        model_fix_sha,
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_20260810_MODEL_FIX_PATHS",
        ("scripts/model.py",),
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_20260810_REPLAY_CONTROL_PATHS",
        ("scripts/control.py",),
    )

    transition = replay_runner.require_authorized_checkpoint_revision_transition(
        repo_root=repo,
        checkpoint_source_sha=checkpoint_source_sha,
        replay_source_sha=replay_source_sha,
        checkpoint_run_id="1",
        checkpoint_artifact_id="2",
        checkpoint_artifact_digest=digest,
    )
    assert transition["authorized_live_paths"] == [
        "scripts/control.py",
        "scripts/model.py",
    ]
    assert transition["checkpoint_source_restore_paths"] == [
        "output/latest/state.csv"
    ]

    checkpoint_tree = git("rev-parse", f"{checkpoint_source_sha}^{{tree}}")
    unrelated_checkpoint = git(
        "commit-tree", checkpoint_tree, "-m", "unrelated checkpoint"
    )
    monkeypatch.setattr(
        replay_runner,
        "AUTHORIZED_CHECKPOINT_SOURCE_SHA",
        unrelated_checkpoint,
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="checkpoint source is not an ancestor",
    ):
        replay_runner.require_authorized_checkpoint_revision_transition(
            repo_root=repo,
            checkpoint_source_sha=unrelated_checkpoint,
            replay_source_sha=replay_source_sha,
            checkpoint_run_id="1",
            checkpoint_artifact_id="2",
            checkpoint_artifact_digest=digest,
        )


def test_20260810_workflow_is_exact_replay_only() -> None:
    workflow = (
        Path(__file__).resolve().parents[1]
        / ".github/workflows/daily_full_validation_replay_20260807.yml"
    ).read_text(encoding="utf-8")
    block = workflow.split("\n  replay-20260810:", 1)[1].split(
        "\n  isolated-six-pdf-validation:", 1
    )[0]

    assert 'REPLAY_DATE: "20260810"' in block
    assert (
        'CHECKPOINT_SOURCE_SHA: "bf04304b0dafc480c690a8d5c9c53aa70634b7f2"'
        in block
    )
    assert 'CHECKPOINT_RUN_ID: "31384317163"' in block
    assert 'CHECKPOINT_ARTIFACT_ID: "9061570264"' in block
    assert "daily-full-pre-step41-checkpoint-31384317163-1" in block
    assert "scripts/run_daily_full_validation_replay.py replay" in block
    assert "capture-canary" not in block
    assert "render-pdfs" not in block
    assert "git push" not in block
