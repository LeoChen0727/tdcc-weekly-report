from __future__ import annotations

import hashlib
import json
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


def test_seven_model_signal_columns_are_required(tmp_path: Path) -> None:
    path = tmp_path / replay_runner.MODEL_SIGNAL_PATH
    required = list(replay_runner.REQUIRED_MODEL_SIGNAL_COLUMNS)
    _write_csv(
        path,
        ["stock_id", *required],
        [
            {
                "stock_id": "2059",
                **{field: "evidence" for field in required},
            }
        ],
    )
    evidence = replay_runner.validate_model_signal_schema(tmp_path)
    assert evidence["rows"] == 1
    assert evidence["required_columns"] == required
    _write_csv(
        path,
        ["stock_id", *required[:-1]],
        [
            {
                "stock_id": "2059",
                **{
                    field: "evidence"
                    for field in required[:-1]
                },
            }
        ],
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="rank_reason_zh",
    ):
        replay_runner.validate_model_signal_schema(tmp_path)


def test_candidate_scoped_warrant_projection_covers_2059_and_7711(
    tmp_path: Path,
) -> None:
    _write_csv(
        tmp_path / replay_runner.ALL_CANDIDATES_PATH,
        ["stock_id"],
        [{"stock_id": "2059"}],
    )
    _write_csv(
        tmp_path / replay_runner.WARRANT_FLOW_PATH,
        ["stock_id", "warrant_flow_signal"],
        [
            {"stock_id": "2059", "warrant_flow_signal": "positive"},
            {"stock_id": "7711", "warrant_flow_signal": "positive"},
        ],
    )
    _write_csv(
        tmp_path / replay_runner.THEME_STOCK_PATH,
        ["stock_id"],
        [{"stock_id": "2059"}],
    )
    evidence = (
        replay_runner.validate_candidate_scoped_warrant_projection(
            tmp_path
        )
    )
    assert evidence["leaked_ids"] == []
    assert evidence["regressions"]["2059"][
        "projection_contract_pass"
    ]
    assert evidence["regressions"]["7711"][
        "projection_contract_pass"
    ]

    _write_csv(
        tmp_path / replay_runner.THEME_STOCK_PATH,
        ["stock_id"],
        [{"stock_id": "2059"}, {"stock_id": "7711"}],
    )
    with pytest.raises(
        replay_runner.ValidationReplayError,
        match="7711",
    ):
        replay_runner.validate_candidate_scoped_warrant_projection(
            tmp_path
        )


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
