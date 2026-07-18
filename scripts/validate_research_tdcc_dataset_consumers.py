from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import pandas as pd

from research_tdcc_dataset_consumer import (
    ResearchTdccDatasetContract,
    load_research_tdcc_dataset_contract,
    require_dataset_id,
)


ROOT = Path(__file__).resolve().parents[1]
CONSUMER_PATHS = (
    "scripts/build_daily_model_parameter_research.py",
    "scripts/build_daily_model_signal_background_features.py",
    "scripts/build_surge_precondition_model.py",
    "scripts/build_tdcc_overheated_short_term_edge.py",
    "scripts/build_tdcc_signal_structures.py",
    "scripts/build_tdcc_weekly_ranking_backtest.py",
    "scripts/build_volume_breakout_tdcc_buy_signal_grid.py",
    "scripts/build_volume_breakout_tdcc_confluence_backtest.py",
    "scripts/build_w_bottom_tdcc_abc_backtest.py",
    "scripts/build_weekly_surge_multifactor_candidates.py",
    "scripts/build_weekly_surge_strict_parameter_candidates.py",
    "scripts/research_weekly_surge_multifactor_grid.py",
    "scripts/research_weekly_surge_strict_parameter_search.py",
    "scripts/update_tdcc_normalized_signal_performance.py",
)
FORBIDDEN_SOURCE_LITERALS = (
    "data/tdcc_stock_history",
    "output/history/tdcc",
    "tdcc_holder_ratio_latest.csv",
    ".glob(\"tdcc_holder_ratio_",
    ".glob('tdcc_holder_ratio_",
)


def validate_consumer_sources(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in CONSUMER_PATHS:
        path = root / relative
        if not path.exists():
            errors.append(f"missing registered research TDCC consumer: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if "research_tdcc_dataset_consumer" not in text:
            errors.append(f"research TDCC consumer does not import canonical adapter: {relative}")
        for literal in FORBIDDEN_SOURCE_LITERALS:
            if literal in text:
                errors.append(f"research TDCC consumer uses forbidden source {literal}: {relative}")
    return errors


def validate_csv_artifacts(
    paths: Iterable[Path],
    contract: ResearchTdccDatasetContract,
) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.exists() or path.stat().st_size <= 0:
            errors.append(f"missing or empty TDCC research artifact: {path.as_posix()}")
            continue
        try:
            frame = pd.read_csv(path, dtype=str, keep_default_na=False)
            require_dataset_id(frame, contract, label=path.as_posix())
        except Exception as exc:
            errors.append(str(exc))
    return errors


def validate_markdown_artifacts(
    paths: Iterable[Path],
    contract: ResearchTdccDatasetContract,
) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.exists() or path.stat().st_size <= 0:
            errors.append(f"missing or empty TDCC research artifact: {path.as_posix()}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if contract.dataset_id not in text or "source_tdcc_dataset_id" not in text:
            errors.append(f"TDCC research markdown lacks canonical dataset lineage: {path.as_posix()}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate research/backtest canonical TDCC consumers and artifact lineage."
    )
    parser.add_argument("--csv", action="append", default=[], help="CSV artifact requiring canonical dataset id")
    parser.add_argument("--markdown", action="append", default=[], help="Markdown artifact requiring canonical dataset id")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_consumer_sources()
    try:
        contract = load_research_tdcc_dataset_contract()
    except Exception as exc:
        errors.append(str(exc))
        contract = None
    if contract is not None:
        errors.extend(validate_csv_artifacts((Path(value) for value in args.csv), contract))
        errors.extend(validate_markdown_artifacts((Path(value) for value in args.markdown), contract))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "research TDCC canonical consumer validation passed: "
        f"dataset_id={contract.dataset_id} history_snapshot_count={len(contract.history_dates)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
