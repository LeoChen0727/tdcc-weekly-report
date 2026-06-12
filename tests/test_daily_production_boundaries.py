from __future__ import annotations

from pathlib import Path
import subprocess

from scripts import validate_daily_production_boundaries as boundaries
from scripts import validate_daily_staged_paths


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


def test_observation_list_is_row_per_stock_not_joined_cell() -> None:
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")
    start = text.index("def model_front_observation_rows_for_line(")
    end = text.index("\ndef append_group_rotation_end_section(", start)
    function_text = text[start:end]

    assert 'rows = [["模型", "股票", "狀態", "操作提醒"]]' in function_text
    assert "model_rows += 1" in function_text
    assert '".join(lines)' not in function_text
    assert "[42 * mm, 36 * mm, 122 * mm, 68 * mm]" in text


def test_daily_workflow_uses_latest_only_volume_breakout_watch() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_volume_breakout_watch.py --latest-only" in text
    assert "python scripts/build_volume_breakout_watch.py\n" not in text
    assert text.count("python scripts/validate_daily_staged_paths.py") == 2


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


def test_docs_master_rules_match_authoritative_rules() -> None:
    authoritative = (ROOT / "rules" / "master_priority_rules.md").read_text(
        encoding="utf-8"
    )
    published = (ROOT / "docs" / "rules" / "master_priority_rules.md").read_text(
        encoding="utf-8"
    )

    assert published == authoritative


def test_thread_workflow_points_to_canonical_pdf_generator() -> None:
    text = (ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md").read_text(encoding="utf-8")

    assert "scripts/generate_chatgpt_side_daily_reports.py" in text
    assert "generate_repo_chatgpt_side_reports.py" not in text


def test_daily_staged_path_validator_accepts_current_staged_set() -> None:
    result = subprocess.run(
        ["python", "scripts/validate_daily_staged_paths.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_daily_staged_path_forbidden_patterns_cover_tdcc_and_research_outputs() -> None:
    examples = [
        "output/latest/tdcc_weekly_candidate_full_latest.pdf",
        "docs/latest/tdcc_signal_effectiveness_latest.md",
        "output/history/research/daily_model_parameter_research.csv",
        "output/latest/weekly_surge_strict_parameter_search_latest.csv",
        "output/latest/daily_model_parameter_recommendations_latest.md",
    ]

    for example in examples:
        assert any(
            validate_daily_staged_paths.fnmatch.fnmatch(example, pattern)
            for pattern in validate_daily_staged_paths.FORBIDDEN_STAGED_PATTERNS
        ), example
