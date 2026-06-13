from __future__ import annotations

from pathlib import Path

from scripts import validate_no_conflict_markers


ROOT = Path(__file__).resolve().parents[1]


def test_conflict_marker_regex_matches_real_markers() -> None:
    assert validate_no_conflict_markers.CONFLICT_MARKER_RE.match("<<<<<<< Updated upstream")
    assert validate_no_conflict_markers.CONFLICT_MARKER_RE.match("=======")
    assert validate_no_conflict_markers.CONFLICT_MARKER_RE.match(">>>>>>> Stashed changes")
    assert not validate_no_conflict_markers.CONFLICT_MARKER_RE.match("=" * 80)


def test_workflows_validate_no_conflict_markers_before_commits() -> None:
    for workflow in [
        ROOT / ".github" / "workflows" / "daily_full_pipeline.yml",
        ROOT / ".github" / "workflows" / "event_catalyst_update.yml",
        ROOT / ".github" / "workflows" / "weekly_theme_review.yml",
    ]:
        text = workflow.read_text(encoding="utf-8")
        assert "python scripts/validate_no_conflict_markers.py" in text
