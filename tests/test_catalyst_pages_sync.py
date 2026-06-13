from __future__ import annotations

from pathlib import Path

import pytest

from scripts.sync_catalyst_pages_artifacts import CATALYST_PAGES_ARTIFACTS, sync_artifacts


ROOT = Path(__file__).resolve().parents[1]


def test_sync_catalyst_pages_artifacts_copies_required_files(tmp_path: Path) -> None:
    latest = tmp_path / "output" / "latest"
    docs_latest = tmp_path / "docs" / "latest"
    latest.mkdir(parents=True)

    for name in CATALYST_PAGES_ARTIFACTS:
        (latest / name).write_text(f"{name}\n", encoding="utf-8")

    copied = sync_artifacts(latest, docs_latest)

    assert len(copied) == len(CATALYST_PAGES_ARTIFACTS)
    for name in CATALYST_PAGES_ARTIFACTS:
        assert (docs_latest / name).read_text(encoding="utf-8") == f"{name}\n"


def test_sync_catalyst_pages_artifacts_fails_on_missing_source(tmp_path: Path) -> None:
    latest = tmp_path / "output" / "latest"
    docs_latest = tmp_path / "docs" / "latest"
    latest.mkdir(parents=True)

    with pytest.raises(FileNotFoundError, match="missing catalyst Pages artifact"):
        sync_artifacts(latest, docs_latest, ["catalyst_summary_latest.md"])


def test_event_and_weekly_workflows_publish_pages_and_use_full_validation() -> None:
    for workflow in [
        ROOT / ".github" / "workflows" / "event_catalyst_update.yml",
        ROOT / ".github" / "workflows" / "weekly_theme_review.yml",
    ]:
        text = workflow.read_text(encoding="utf-8")
        assert "actions: write" in text
        assert "tabulate lxml html5lib beautifulsoup4" in text
        assert "python scripts/build_theme_event_watch.py" in text
        assert "python scripts/sync_catalyst_pages_artifacts.py" in text
        assert "git add docs/latest/" in text
        assert "gh workflow run pages.yml --ref main" in text
        assert "Timed out waiting for GitHub Pages deploy workflow" in text
        assert "validate_event_calendar_data.py --schema-only" not in text
        assert "validate_catalyst_layer.py --schema-only" not in text


def test_daily_workflow_syncs_catalyst_pages_artifacts() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    assert "python scripts/sync_catalyst_pages_artifacts.py" in text
