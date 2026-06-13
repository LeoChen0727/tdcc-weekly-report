from __future__ import annotations

from pathlib import Path
import subprocess

from scripts import validate_daily_production_boundaries as boundaries
from scripts import validate_apps_script_workflow_triggers
from scripts import validate_daily_staged_paths


ROOT = Path(__file__).resolve().parents[1]
DAILY_DECISION_LAYER_FIELDS = [
    "decision_priority",
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
]
DAILY_OPERATION_CONCLUSION_PHRASES = [
    "推薦可買",
    "可買候選",
    "買進條件",
    "不買條件",
    "目前不買",
    "條件式買進",
    "買進後",
    "先不買",
    "排除買進",
]


def test_daily_production_boundary_validator_passes_current_repo() -> None:
    assert boundaries.main() == 0


def test_apps_script_workflow_trigger_validator_passes_current_repo() -> None:
    assert validate_apps_script_workflow_triggers.main() == 0


def test_apps_script_daily_trigger_skips_weekends_and_disables_raw_health_check() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerDailyStockMonitor"
    )

    assert "dayOfWeek === 0 || dayOfWeek === 6" in body
    assert 'dispatchWorkflow_("daily_full_pipeline.yml", {' in body
    assert 'run_raw_health_check: "false"' in body


def test_canonical_chatgpt_side_generator_is_tracked_and_not_legacy_six_category() -> None:
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")

    assert path.exists()
    assert "CATEGORY_SPECS" not in text
    assert 'REPO = ROOT / "tdcc-weekly-report-git"' not in text
    assert "daily_report_model_registry_latest.csv" in text
    assert "daily_candidate_model_signals_for_report_latest.csv" in text
    assert "model_score" in text
    assert "risk_tags" in text
    for field in DAILY_DECISION_LAYER_FIELDS:
        assert field not in text
    assert "model_recommendation_rows_for_line" in text
    assert "資金進入族群觀察" in text
    assert "daily_candidate_group_rotation_latest.csv" in text
    assert "CHATGPT_SIDE_KLINE_DAYS = 126" in text
    assert ".tail(CHATGPT_SIDE_KLINE_DAYS)" in text
    assert "kline_180" not in text
    assert "tail(180)" not in text
    assert "180日K線" not in text
    raw_readme = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT"
    pages_readme = "https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT"
    assert text.index(raw_readme) < text.index(pages_readme)


def test_observation_list_is_row_per_stock_not_joined_cell() -> None:
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")
    start = text.index("def model_front_observation_rows_for_line(")
    end = text.index("\ndef append_group_rotation_end_section(", start)
    function_text = text[start:end]

    assert 'rows = [["榜別", "模型", "股票", "模型狀態", "分數 / 風險"]]' in function_text
    assert "listing_status_label(row, stage)" in function_text
    assert "listing_status_sort_key(listing_label)" in function_text
    assert '"新上榜": 0' in text
    assert '"重複上榜": 1' in text
    assert "model_rows += 1" in function_text
    assert '".join(lines)' not in function_text
    assert "[24 * mm, 36 * mm, 34 * mm, 112 * mm, 62 * mm]" in text


def test_daily_pdf_packet_and_rules_do_not_depend_on_decision_layer() -> None:
    paths = [
        ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py",
        ROOT / "scripts" / "generate_daily_market_pdf.py",
        ROOT / "scripts" / "validate_daily_market_report.py",
        ROOT / "build_chatgpt_daily_report_packet.py",
        ROOT / "build_daily_market_report_artifacts.py",
        ROOT / "build_chatgpt_daily_report_rules.py",
        ROOT / "scripts" / "build_chatgpt_indicator_usage_guide.py",
        ROOT / "scripts" / "build_volume_breakout_watch.py",
        ROOT / "rules" / "daily_stock_candidate_rules.md",
        ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for field in DAILY_DECISION_LAYER_FIELDS:
            assert field not in text, f"{path.name} still references {field}"
        for phrase in DAILY_OPERATION_CONCLUSION_PHRASES:
            assert phrase not in text, f"{path.name} still emits {phrase}"

    packet_text = (ROOT / "build_chatgpt_daily_report_packet.py").read_text(
        encoding="utf-8"
    )
    assert "daily_candidate_model_signals_for_report_latest.csv" in packet_text
    assert "model_score" in packet_text
    assert "risk_penalty_tags" in packet_text


def test_daily_production_sources_do_not_build_or_depend_on_decision_layer() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8",
        errors="replace",
    )
    assert "build_daily_candidate_decision_layer.py" not in workflow
    assert "validate_daily_candidate_decision_layer.py" not in workflow

    assert not (ROOT / "scripts" / "build_daily_candidate_decision_layer.py").exists()
    assert not (ROOT / "scripts" / "validate_daily_candidate_decision_layer.py").exists()

    paths = [
        ROOT / "scripts" / "build_daily_candidate_model_layer.py",
        ROOT / "scripts" / "build_daily_theme_leadership_layer.py",
        ROOT / "scripts" / "validate_daily_theme_leadership_layer.py",
        ROOT / "scripts" / "build_non_revenue_momentum_watch.py",
        ROOT / "scripts" / "build_theme_event_watch.py",
        ROOT / "scripts" / "update_daily_theme_status_history.py",
        ROOT / "scripts" / "check_raw_data_health.py",
        ROOT / "publish_chatgpt_report_readme_and_check.py",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name == "build_daily_theme_leadership_layer.py":
            start = text.index("DEPRECATED_DECISION_COLUMNS = [")
            end = text.index("\n\nBULLISH_WARRANT_SIGNALS", start)
            cleanup_block = text[start:end]
            for field in DAILY_DECISION_LAYER_FIELDS:
                if field != "daily_candidate_decision":
                    assert field in cleanup_block
            text = text[:start] + text[end:]
        for field in DAILY_DECISION_LAYER_FIELDS:
            assert field not in text, f"{path.as_posix()} still references {field}"


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
    assert "approximately 126 trading days" in published
    assert "180-day windows" not in published


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
