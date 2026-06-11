from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_production_boundaries as boundaries


ROOT = Path(__file__).resolve().parents[1]


def test_daily_production_boundary_validator_passes_current_repo() -> None:
    assert boundaries.main() == 0


def test_canonical_chatgpt_side_generator_is_tracked_and_not_legacy_six_category() -> None:
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")

    assert path.exists()
    assert "CATEGORY_SPECS" not in text
    assert 'REPO = ROOT / "tdcc-weekly-report-git"' not in text
    assert "daily_report_model_registry_latest.csv" in text
    assert "daily_candidate_model_signals_for_report_latest.csv" in text
    assert "model_recommendation_rows_for_line" in text
    assert "資金進入族群觀察" in text
    assert "daily_candidate_group_rotation_latest.csv" in text


def test_daily_workflow_uses_latest_only_volume_breakout_watch() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_volume_breakout_watch.py --latest-only" in text
    assert "python scripts/build_volume_breakout_watch.py\n" not in text


def test_docs_daily_rules_match_authoritative_rules() -> None:
    authoritative = (ROOT / "rules" / "daily_stock_candidate_rules.md").read_text(
        encoding="utf-8"
    )
    published = (ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md").read_text(
        encoding="utf-8"
    )

    assert published == authoritative
    assert "six ChatGPT-side PDF deliverables" in published
    assert "four ChatGPT-side PDF deliverables" not in published
