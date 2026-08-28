from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_WORKFLOW = ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml"
DAILY_MODEL_RECOMMENDER = ROOT / "scripts" / "build_daily_model_parameter_recommendations.py"
DAILY_MODEL_LAYER = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
TDCC_WEEKLY_REPORT = ROOT / "scripts" / "build_tdcc_weekly_candidate_reports.py"


FORBIDDEN_RESEARCH_STAGE_PATTERNS = {
    "config files": r"git add\s+config/",
    "script files": r"git add\s+scripts/",
    "workflow files": r"git add\s+\.github/workflows/",
    "daily price source data": r"git add\s+data/daily_price/",
    "daily production report history": r"git add\s+output/history/reports/",
    "daily market PDF artifacts": r"git add\s+output/latest/daily_market_.*\.pdf",
    "daily recommendation PDF artifacts": r"git add\s+output/latest/(mainstream|non_mainstream)_.*\.pdf",
    "warrant market PDF artifacts": r"git add\s+output/latest/warrant_market_report_.*\.pdf",
    "TDCC weekly PDF artifacts": r"git add\s+output/latest/tdcc_weekly_.*\.pdf",
    "broad research history root": r"git add\s+output/history/research/\s",
    "formal daily model snapshots": r"git add\s+output/history/daily_model_snapshots/",
    "formal model readiness": r"git add\s+output/latest/model_operation_readiness_latest",
    "formal approved operation evidence": r"git add\s+output/latest/approved_operation_patterns_latest",
    "formal daily operation adapters": r"git add\s+output/latest/daily_(w_bottom|neckline|price_pullback_23ema|volume_breakout)_",
}

FORBIDDEN_RESEARCH_RUN_PATTERNS = {
    "daily candidate model layer": r"python\s+scripts/build_daily_candidate_model_layer\.py",
    "daily market PDF generator": r"python\s+scripts/generate_daily_market_pdf\.py",
    "ChatGPT-side daily PDF generator": r"python\s+scripts/generate_chatgpt_side_daily_reports\.py",
    "TDCC weekly PDF report builder": r"python\s+scripts/build_tdcc_weekly_candidate_reports\.py",
    "TDCC history backfill": r"python\s+scripts/backfill_tdcc_history\.py",
    "legacy cross-model parameter producer": r"python\s+scripts/build_daily_model_parameter_research\.py",
    "formal approved operation producer": r"python\s+scripts/build_approved_operation_patterns\.py",
    "formal W-bottom operation adapter": r"python\s+scripts/build_daily_w_bottom_operation_sections\.py",
    "formal 23EMA operation adapter": r"python\s+scripts/build_daily_price_pullback_23ema_operation_section\.py",
    "formal model readiness producer": r"python\s+scripts/build_model_operation_readiness\.py",
    "model-owned formal revenue readiness producer": (
        r"python\s+scripts/sync_revenue_unreacted_range_operation_readiness\.py"
    ),
    "formal daily snapshot publisher": r"python\s+scripts/update_daily_published_model_snapshots\.py",
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    errors: list[str] = []
    workflow_text = read_text(RESEARCH_WORKFLOW)

    for label, pattern in FORBIDDEN_RESEARCH_STAGE_PATTERNS.items():
        if re.search(pattern, workflow_text):
            errors.append(f"research_backtest_pipeline must not auto-stage {label}: {pattern}")

    for label, pattern in FORBIDDEN_RESEARCH_RUN_PATTERNS.items():
        if re.search(pattern, workflow_text):
            errors.append(f"research_backtest_pipeline must not run {label}: {pattern}")

    recommender_text = read_text(DAILY_MODEL_RECOMMENDER)
    if 'Path("config/' in recommender_text or "CONFIG_CSV" in recommender_text:
        errors.append(
            "daily model parameter recommendations are research outputs; "
            "they must not be written into config/"
        )

    daily_model_text = read_text(DAILY_MODEL_LAYER)
    if "build_daily_model_parameter_recommendations" in daily_model_text:
        errors.append("daily candidate model layer must not import or execute research recommendation builder")
    if 'MODEL_PARAMETER_RECOMMENDATIONS = LATEST_DIR / "daily_model_parameter_recommendations_latest.csv"' not in daily_model_text:
        errors.append("daily candidate model layer should read research recommendations only from output/latest")

    tdcc_weekly_text = read_text(TDCC_WEEKLY_REPORT)
    if "daily_model_parameter_recommendations_latest.csv" in tdcc_weekly_text:
        errors.append("TDCC weekly report must not read raw model-parameter research recommendations directly")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("research production boundary validation passed")
    print(f"validated_workflow={RESEARCH_WORKFLOW.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
