from __future__ import annotations

import fnmatch
import subprocess


FORBIDDEN_STAGED_PATTERNS = {
    "output/latest/tdcc_*": "TDCC latest outputs are owned by tdcc_weekly/research workflows",
    "docs/latest/tdcc_*": "TDCC Pages outputs are owned by tdcc_weekly/research workflows",
    "output/history/tdcc_signals/*": "TDCC signal history is not a daily production output",
    "output/history/research/*": "research history is owned by research_backtest_pipeline",
    "output/history/surge_model/*": "surge model history is owned by research_backtest_pipeline",
    "output/history/msci_index_reviews/*": "MSCI review history is owned by research_backtest_pipeline",
    "output/history/volume_breakout/*": "volume-breakout backtest history is owned by research_backtest_pipeline",
    "output/latest/weekly_surge_*": "weekly surge research outputs are not daily production outputs",
    "docs/latest/weekly_surge_*": "weekly surge Pages outputs are not daily production outputs",
    "output/latest/explosive_volume_up_*": "explosive-volume research outputs are not daily production outputs",
    "docs/latest/explosive_volume_up_*": "explosive-volume Pages outputs are not daily production outputs",
    "output/latest/surge_model_*": "surge precondition research outputs are not daily production outputs",
    "docs/latest/surge_model_*": "surge precondition Pages outputs are not daily production outputs",
    "output/latest/msci_taiwan_rebalance_*": "MSCI rebalance research outputs are not daily production outputs",
    "docs/latest/msci_taiwan_rebalance_*": "MSCI rebalance Pages outputs are not daily production outputs",
    "output/latest/daily_signal_performance_*": "signal performance reports are not daily production outputs",
    "docs/latest/daily_signal_performance_*": "signal performance Pages outputs are not daily production outputs",
    "output/latest/daily_model_parameter_research_*": "model parameter research is not a daily production output",
    "docs/latest/daily_model_parameter_research_*": "model parameter research Pages output is not daily production output",
    "output/latest/daily_model_parameter_recommendations_*": "model parameter recommendations are not committed by daily production",
    "docs/latest/daily_model_parameter_recommendations_*": "model parameter recommendation Pages output is not daily production output",
}


def staged_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    for path in staged_files():
        for pattern, reason in FORBIDDEN_STAGED_PATTERNS.items():
            if fnmatch.fnmatch(path, pattern):
                errors.append(f"{path}: {reason}")

    if errors:
        print("ERROR: daily production attempted to stage non-daily paths")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("daily staged path validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
