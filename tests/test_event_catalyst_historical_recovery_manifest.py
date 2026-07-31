from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_event_catalyst_historical_recovery_manifest import (  # noqa: E402
    BLOCKED_STATUS,
    TARGET_DATES,
    build_manifests,
)
from validate_event_catalyst_historical_recovery_manifest import (  # noqa: E402
    validate_index,
)


def run_git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )


def build_fixture(root: Path) -> Path:
    evidence = root / "config" / "event_catalyst_historical_recovery_failures.csv"
    evidence.parent.mkdir(parents=True)
    shutil.copy2(
        ROOT / "config" / "event_catalyst_historical_recovery_failures.csv",
        evidence,
    )
    (root / "config" / "event_catalyst_overlay_contract.csv").write_text(
        "overlay_id,score_allowed,ranking_allowed\nfixture,false,false\n",
        encoding="utf-8",
    )

    latest = root / "output" / "latest"
    latest.mkdir(parents=True)
    (latest / "catalyst_data_source_status_latest.json").write_text(
        json.dumps(
            {
                "generated_at": "2026-07-31 08:00:00 Asia/Taipei",
                "external_fetch_status": "ok",
            }
        ),
        encoding="utf-8",
    )
    (latest / "calendar_data_source_status_latest.json").write_text(
        json.dumps(
            {
                "generated_at": "2026-07-31 08:01:00 Asia/Taipei",
                "status": "ok",
            }
        ),
        encoding="utf-8",
    )

    replay_root = (
        root
        / "output"
        / "history"
        / "historical_source_replay"
        / "github-run-30510020253-1"
    )
    for target_date in TARGET_DATES:
        replay_path = replay_root / target_date / "structured_source_manifest.json"
        replay_path.parent.mkdir(parents=True)
        replay_path.write_text(
            json.dumps(
                {
                    "report_date": target_date,
                    "replay_id": "github-run-30510020253-1",
                    "pipeline_commit_sha": "f2ac085b0ac9b4a7b6c9f2c423dbf606615f6bd0",
                    "publication_status": "reconstructed_not_as_published",
                    "as_published": False,
                    "forbidden_reconstruction": [
                        "event_as_published",
                        "catalyst_as_published",
                    ],
                }
            ),
            encoding="utf-8",
        )

    run_git(root, "init", "--initial-branch=main")
    run_git(root, "config", "user.email", "test@example.invalid")
    run_git(root, "config", "user.name", "Test")
    run_git(root, "add", ".")
    run_git(root, "commit", "-m", "fixture")
    return evidence


def test_historical_recovery_is_blocked_without_reconstructing_content(
    tmp_path: Path,
) -> None:
    evidence = build_fixture(tmp_path)
    output_root = tmp_path / "output" / "history" / "event_catalyst_recovery"
    latest_json = (
        tmp_path / "output" / "latest" / "event_catalyst_historical_recovery_latest.json"
    )
    latest_md = (
        tmp_path / "output" / "latest" / "event_catalyst_historical_recovery_latest.md"
    )
    index = build_manifests(
        tmp_path,
        evidence_csv=evidence,
        recovery_id="github-run-999-1",
        workflow_run_id="999",
        workflow_run_url="https://example.invalid/actions/runs/999",
        output_root=output_root,
        latest_json=latest_json,
        latest_md=latest_md,
    )

    docs_latest = tmp_path / "docs" / "latest"
    docs_latest.mkdir(parents=True)
    docs_json = docs_latest / latest_json.name
    docs_md = docs_latest / latest_md.name
    shutil.copy2(latest_json, docs_json)
    shutil.copy2(latest_md, docs_md)

    assert index["completion_state"] == BLOCKED_STATUS
    assert tuple(index["target_dates"]) == TARGET_DATES
    for line in latest_md.read_text(encoding="utf-8").splitlines():
        assert line == line.rstrip(" \t")
    assert validate_index(
        tmp_path,
        index_path=latest_json,
        evidence_csv=evidence,
        docs_json=docs_json,
        latest_md=latest_md,
        docs_md=docs_md,
    ) == []

    for entry in index["manifests"]:
        manifest = json.loads((tmp_path / entry["manifest_path"]).read_text(encoding="utf-8"))
        assert manifest["status"] == BLOCKED_STATUS
        assert manifest["current_value_backfill_allowed"] is False
        assert manifest["historical_content_reconstructed"] is False
        assert manifest["runner_uncommitted_sources_irrecoverable"] is True
        assert "dataset_coverage" not in manifest
