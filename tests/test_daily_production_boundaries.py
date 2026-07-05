from __future__ import annotations

from pathlib import Path
import subprocess

from scripts import validate_daily_production_boundaries as boundaries
from scripts import validate_apps_script_workflow_triggers
from scripts import validate_daily_staged_paths
from scripts import validate_research_production_boundaries


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


def test_research_production_boundary_validator_passes_current_repo() -> None:
    assert validate_research_production_boundaries.main() == 0


def test_apps_script_workflow_trigger_validator_passes_current_repo() -> None:
    assert validate_apps_script_workflow_triggers.main() == 0


def test_apps_script_daily_trigger_skips_weekends_and_disables_raw_health_check() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerDailyStockMonitor"
    )

    assert "dayOfWeek === 0 || dayOfWeek === 6" in body
    assert 'dispatchWorkflow_("daily_full_pipeline.yml", {' in body
    assert 'run_raw_health_check: "false"' in body


def test_apps_script_recent_daily_price_gap_repair_trigger_is_weekday_only() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerDailyPriceGapRepair"
    )

    assert "dayOfWeek === 0 || dayOfWeek === 6" in body
    assert 'dispatchWorkflow_("repair_recent_daily_price_gaps.yml", {' in body
    assert 'lookback_days: "7"' in body
    assert 'max_repair_dates: "5"' in body


def test_apps_script_tdcc_history_gap_repair_trigger_is_tuesday_monthly_guard() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerTdccHistoryGapRepair"
    )
    install_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "installTdccHistoryGapRepairTrigger_"
    )

    assert 'dispatchWorkflow_("repair_tdcc_monthly_history_gaps.yml", {' in body
    assert 'universe: "chatgpt-top"' in body
    assert 'max_stocks: "80"' in body
    assert 'max_requests: "500"' in body
    assert 'rebuild_max_dates: "4"' in body
    assert "ScriptApp.WeekDay.TUESDAY" in install_body
    assert ".atHour(9)" in install_body


def test_canonical_chatgpt_side_generator_is_tracked_and_not_legacy_six_category() -> None:
    entrypoint = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
    entrypoint_text = entrypoint.read_text(encoding="utf-8", errors="replace")
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")

    assert entrypoint.exists()
    assert "resolve_daily_report_source_state" in entrypoint_text
    assert '"worktree", "add", "--detach"' in entrypoint_text
    assert "CHATGPT_DAILY_REPORT_ENTRYPOINT" in entrypoint_text
    assert "CHATGPT_DAILY_SOURCE_REF" in entrypoint_text
    assert "PYTHONIOENCODING" in entrypoint_text
    assert "reconfigure(encoding=\"utf-8\", errors=\"replace\")" in entrypoint_text
    assert "source-gate-only" in entrypoint_text
    assert path.exists()
    assert "CATEGORY_SPECS" not in text
    assert 'REPO = ROOT / "tdcc-weekly-report-git"' not in text
    assert "daily_report_model_registry_latest.csv" in text
    assert "CHATGPT_DAILY_SOURCE_REF" in text
    assert "daily_candidate_model_signals_for_report_latest.csv" in text
    assert "model_score" in text
    assert "risk_tags" in text
    for field in DAILY_DECISION_LAYER_FIELDS:
        assert field not in text
    assert "mainstream_curated_recommendation_rows" in text
    assert "non_mainstream_curated_recommendation_rows" in text
    assert "資金進入族群觀察" in text
    assert "daily_candidate_group_rotation_latest.csv" in text
    assert "CHATGPT_SIDE_KLINE_DAYS = 126" in text
    assert ".tail(CHATGPT_SIDE_KLINE_DAYS)" in text
    assert "kline_180" not in text
    assert "tail(180)" not in text
    assert "180日K線" not in text
    assert "resolve_daily_report_source_state" in text
    assert "require_entrypoint_invocation" in text
    assert "run_chatgpt_daily_report_entrypoint.py" in text
    assert "--request-date" not in text
    assert "args.request_date" not in text
    assert "fetch_remote_readme_values" not in text
    assert "REMOTE_README_URLS" not in text
    assert 'REQUEST_DATE = datetime.now().strftime("%Y%m%d")' not in text

    resolver = ROOT / "scripts" / "resolve_daily_report_source_state.py"
    resolver_text = resolver.read_text(encoding="utf-8", errors="replace")
    assert resolver.exists()
    assert "origin/main" in resolver_text
    assert "git show" in resolver_text
    assert "data_freshness_latest.csv" in resolver_text
    assert "READ_ME_FIRST_DAILY_REPORT.txt" in resolver_text
    assert "chatgpt_daily_report_packet_latest.txt" in resolver_text
    assert "OneDrive" in resolver_text

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8", errors="replace")
    assert "chatgpt_side_outputs*/" in gitignore


def test_observation_list_is_row_per_stock_not_joined_cell() -> None:
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")
    start = text.index("def mainstream_curated_front_observation_rows(")
    end = text.index("\ndef non_mainstream_curated_front_observation_rows(", start)
    function_text = text[start:end]

    assert 'rows = [["榜別", "模型", "股票", "模型狀態", "分數 / 風險"]]' in function_text
    assert "listing_status_label(row, stage)" in function_text
    assert "listing_status_sort_key(listing_label)" in function_text
    assert '"新上榜": 0' in text
    assert '"重複上榜": 1' in text
    assert "model_rows += 1" in function_text
    assert '".join(lines)' not in function_text

    non_mainstream_pdf = text[
        text.index("def build_non_mainstream_curated_pdf(") : text.index(
            "\ndef build_mainstream_full_candidate_pdf(",
            text.index("def build_non_mainstream_curated_pdf("),
        )
    ]
    assert "non_mainstream_curated_front_observation_rows(" not in non_mainstream_pdf
    assert "non_mainstream_curated_recommendation_rows(" not in non_mainstream_pdf


def test_daily_pdf_packet_and_rules_do_not_depend_on_decision_layer() -> None:
    paths = [
        ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py",
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


def test_formal_daily_report_dates_use_freshness_hard_gate_without_fallbacks() -> None:
    tracking_text = (ROOT / "scripts" / "tracking_utils.py").read_text(encoding="utf-8")
    start = tracking_text.index("def require_daily_report_ready_main_price_date(")
    end = tracking_text.index("\n\ndef load_price_history(", start)
    hard_gate_body = tracking_text[start:end]

    for field in ["main_price_date", "report_ready", "warrant_ready", "daily_pdf_ready"]:
        assert field in hard_gate_body
    assert "latest_stock_price_history_date" not in hard_gate_body
    assert "latest_price_date" not in hard_gate_body

    files = {
        ROOT / "build_daily_market_report_artifacts.py": [
            "require_daily_report_ready_main_price_date",
        ],
        ROOT / "scripts" / "build_theme_event_watch.py": [
            "main_price_date_from_freshness",
        ],
    }
    for path, required in files.items():
        text = path.read_text(encoding="utf-8")
        for literal in required:
            assert literal in text, f"{path.as_posix()} missing {literal}"

    forbidden = {
        ROOT / "build_daily_market_report_artifacts.py": [
            'dates = candidates["date"].map(normalize_date)',
            "all_candidates_latest.csv date 最大值",
            'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")',
        ],
        ROOT / "scripts" / "build_theme_event_watch.py": [
            'return datetime.now().strftime("%Y%m%d")',
            "or datetime.now()",
        ],
        ROOT / "build_warrant_flow_latest.py": [
            'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")',
        ],
    }
    for path, literals in forbidden.items():
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            assert literal not in text, f"{path.as_posix()} still has date fallback {literal}"


def test_daily_workflow_uses_latest_only_volume_breakout_watch() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_volume_breakout_watch.py --latest-only" in text
    assert "python scripts/build_volume_breakout_watch.py\n" not in text
    assert text.count("python scripts/validate_daily_staged_paths.py") == 2
    assert "git add docs/latest/ || true" not in text
    assert "git add output/latest/ docs/latest/ || true" not in text


def test_daily_workflow_requires_current_usable_warrant_fetch_with_evidence() -> None:
    daily_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    warrant_text = (ROOT / ".github" / "workflows" / "warrant_flow.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/fetch_official_warrant_daily.py --require-current-usable" in daily_text
    assert "timeout-minutes: 18" in daily_text
    assert 'OFFICIAL_WARRANT_FETCH_MAX_SECONDS: "180"' in daily_text
    assert 'OFFICIAL_WARRANT_FETCH_ATTEMPTS: "3"' in daily_text
    assert 'OFFICIAL_WARRANT_FETCH_RETRY_SLEEP_SECONDS: "180"' in daily_text
    assert "python scripts/validate_warrant_source_status.py --allow-noncritical-grace" in daily_text
    assert "- name: Upload warrant fetch evidence" in daily_text
    assert "output/latest/warrant_daily_fetch_latest.md" in daily_text
    assert "output/latest/warrant_source_status_latest.md" in daily_text
    assert "output/latest/warrant_source_status_latest.json" in daily_text
    assert "output/debug/warrant_fetch_debug_latest.md" in daily_text
    assert "output/debug/warrant_fetch_debug_latest.csv" in daily_text
    assert "--require-current-usable" not in warrant_text


def test_daily_workflow_publishes_as_published_model_snapshots() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/update_daily_published_model_snapshots.py" in text
    assert "python scripts/validate_daily_published_model_snapshots.py" in text
    assert "git add output/history/daily_candidate_models/ || true" in text
    assert "git add output/history/daily_model_snapshots/ || true" in text
    assert (
        text.index("- name: Guard daily freshness before publishing")
        < text.index("- name: Build daily market report artifacts")
        < text.index("- name: Publish daily model snapshots")
        < text.index("- name: Commit report artifacts, packets, and rules first")
    )
    commit_block = text[
        text.index("- name: Commit report artifacts, packets, and rules first") :
        text.index("- name: Wait briefly for GitHub Pages and raw propagation")
    ]
    assert "python scripts/validate_daily_published_model_snapshots.py" in commit_block


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

    assert "scripts/run_chatgpt_daily_report_entrypoint.py" in text
    assert "scripts/generate_chatgpt_side_daily_reports.py" in text
    assert "renderer, not the official entrypoint" in text
    assert "generate_repo_chatgpt_side_reports.py" not in text


def test_chatgpt_daily_usage_prompt_uses_official_entrypoint_not_pages_first() -> None:
    text = (ROOT / "docs" / "CHATGPT_DAILY_REPORT_USAGE_PROMPT.md").read_text(
        encoding="utf-8"
    )

    assert "scripts/run_chatgpt_daily_report_entrypoint.py --source-gate-only" in text
    assert "git show origin/main" in text
    assert "chatgpt_daily_report_packet_latest.txt" in text
    assert "六份" in text
    assert "chatgpt_daily_report_runtime_manifest.json" in text
    assert "優先讀 GitHub Pages" not in text
    assert "如果 Pages 讀不到，再讀 raw" not in text
    assert "請同時提供四份成品" not in text
    assert "daily_market_curated_pdf_pages_url" not in text


def test_repo_agent_rules_default_to_independent_business_surfaces() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    workflow_text = (ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md").read_text(
        encoding="utf-8"
    )

    assert "All business-facing code in this repository defaults to independent ownership." in text
    assert "Changing A must not silently change B." in text
    assert "Stock model parameters, thresholds, scoring weights, ranking rules, and gates" in text
    assert "Business-facing code defaults to independent ownership." in workflow_text


def test_repo_agent_rules_require_completion_claim_evidence() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "Completion Claim Evidence Gate" in text
    assert "completion_state=complete" in text
    assert "PR number and URL" in text
    assert "Merge commit on `main`" in text
    assert "Post-merge official `main` workflow run id and conclusion" in text
    assert "Local post-merge validators or tests" in text
    assert "Runtime behavior or user-facing artifact inspection result" in text
    assert "Final `git status --short --branch` state" in text
    assert "`remaining blocker`" in text
    assert "main_workflow_passed_pending_artifact_inspection" in text
    assert "renderer consumed the dedicated adapter" in text
    assert "PDF contract/replay validation passed after merge" in text


def test_formal_model_change_rules_include_pdf_operation_adapter_gate() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    model_contract = (ROOT / "docs" / "stock_model_contract_governance.md").read_text(
        encoding="utf-8"
    )
    pdf_contract = (ROOT / "docs" / "daily_pdf_contract_consumer_governance.md").read_text(
        encoding="utf-8"
    )

    for text in (agents, model_contract):
        assert "operation-row adapter" in text
        assert "model_operation_readiness_latest.csv" in text
        assert "pdf_integration_status=pdf_integrated_daily_adapter" in text

    assert "presentation_allowed=False" in agents
    assert "PDF renderer must not convert candidate signal rows" in agents
    assert "daily PDF renderer must not infer buyable, active, pending, exit, or stop-loss lifecycle rows" in model_contract
    assert "Registry approval alone does not authorize the PDF renderer to infer lifecycle" in pdf_contract


def test_formal_model_change_rules_require_close_confirmed_operation_prices() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    model_contract = (ROOT / "docs" / "stock_model_contract_governance.md").read_text(
        encoding="utf-8"
    )
    price_pullback_spec = (
        ROOT / "docs" / "specs" / "price_pullback_23ema_operation_candidate_spec.md"
    ).read_text(encoding="utf-8")

    for text in (agents, model_contract):
        assert "Formal operation buy/sell/stop/profit-taking rules" in text
        assert "close-confirmed by" in text
        assert "next trading day open" in text
        assert "after a qualifying close confirmation" in text
        assert "same-day close" in text
        assert "intraday high/low as formal entry" in text
        assert "profit-taking, win, failure, or realized-return prices" in text
        assert "research-only observation" in text
        assert "price_pullback_23ema" in text
        assert "research_only_intraday_trigger" in text
        assert "close_prev20_high_break_same_day_close" in text

    assert "Formal Price Confirmation Boundary" in price_pullback_spec
    assert "Intraday high/low observations must not be used as" in price_pullback_spec
    assert "realized execution prices" in price_pullback_spec
    assert "intraday high touches the signal-day previous 20-day high" in price_pullback_spec
    assert "research_only_intraday_trigger" in price_pullback_spec
    assert "close breaks the signal-day previous 20-day high, then sell at the next" in price_pullback_spec
    assert "close_prev20_high_break_same_day_close" in price_pullback_spec
    assert "known only after that close" in price_pullback_spec
    assert boundaries.validate_model_operation_price_confirmation_rules() == []


def test_operation_price_confirmation_validator_fails_closed_when_rule_missing(
    tmp_path,
    monkeypatch,
) -> None:
    rule_file = tmp_path / "rule.md"
    rule_file.write_text(
        "Formal operation buy/sell/stop/profit-taking rules must be close-confirmed by default.",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        boundaries,
        "MODEL_OPERATION_PRICE_CONFIRMATION_RULE_LITERALS",
        {
            rule_file: {
                "must not use intraday high/low as formal entry, exit, stop, profit-taking, win, failure, or realized-return prices": (
                    "test operation price rule"
                ),
            },
        },
    )

    errors = boundaries.validate_model_operation_price_confirmation_rules()

    assert errors
    assert "test operation price rule" in errors[0]


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


def test_research_workflow_does_not_stage_generated_recommendations_as_config() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )
    recommender = (ROOT / "scripts" / "build_daily_model_parameter_recommendations.py").read_text(
        encoding="utf-8"
    )

    assert "git add config/daily_model_parameter_recommendations.csv" not in workflow
    assert "CONFIG_CSV" not in recommender
    assert 'Path("config/daily_model_parameter_recommendations.csv")' not in recommender
