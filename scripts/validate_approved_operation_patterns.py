from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_approved_operation_patterns import (  # noqa: E402
    BUY_FILTER_ID,
    DOCS_CSV,
    DOCS_MD,
    ENTRY_RULE_ID,
    EXIT_RULE_ID,
    MIN_MEDIAN_RETURN,
    MIN_RESEARCH_SCORE,
    MIN_SAMPLE_SIZE,
    MIN_WIN_RATE,
    MODEL_ID,
    OPERATION_MODULE_ID,
    OUT_CSV,
    OUT_MD,
    STOP_LOSS_RULE_ID,
    positive_rank_rows,
)
from tracking_utils import read_csv, to_number  # noqa: E402


REQUIRED_COLUMNS = {
    "model_id",
    "operation_module_id",
    "approval_version",
    "approved_for_daily",
    "approval_status",
    "operation_directive_level",
    "entry_rule_id",
    "stop_loss_rule_id",
    "exit_rule_id",
    "buy_filter_id",
    "min_sample_size",
    "min_win_rate",
    "min_median_return",
    "require_out_of_sample_pass",
    "min_research_score",
    "evidence_rank_source",
    "evidence_total_rank_rows",
    "evidence_positive_rank_rows",
    "risk_notes_zh",
}


def bool_text(value: object) -> str:
    return str(value).strip().lower()


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [OUT_CSV, OUT_MD, DOCS_CSV, DOCS_MD]:
        if not path.exists():
            errors.append(f"missing approved operation artifact: {path}")
    if OUT_CSV.exists() and DOCS_CSV.exists() and OUT_CSV.read_text(encoding="utf-8") != DOCS_CSV.read_text(encoding="utf-8"):
        errors.append("docs/latest CSV copy does not match output/latest approved operation CSV")
    if OUT_MD.exists() and DOCS_MD.exists() and OUT_MD.read_text(encoding="utf-8") != DOCS_MD.read_text(encoding="utf-8"):
        errors.append("docs/latest MD copy does not match output/latest approved operation MD")
    return errors


def validate_approval() -> list[str]:
    errors: list[str] = []
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    if df.empty:
        return [f"empty approved operation artifact: {OUT_CSV}"]
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        return [f"approved operation artifact missing columns: {missing}"]
    if len(df) != 1:
        errors.append(f"approved operation artifact must contain exactly one current approval row, got {len(df)}")

    row = df.iloc[0]
    expected = {
        "model_id": MODEL_ID,
        "operation_module_id": OPERATION_MODULE_ID,
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_directive_level": "approved_daily_operation_guidance",
        "entry_rule_id": ENTRY_RULE_ID,
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "buy_filter_id": BUY_FILTER_ID,
        "require_out_of_sample_pass": "True",
    }
    for col, value in expected.items():
        if str(row.get(col, "")) != value:
            errors.append(f"{col} must be {value!r}, got {row.get(col, '')!r}")

    if to_number(row.get("min_sample_size")) < MIN_SAMPLE_SIZE:
        errors.append("approval min_sample_size is weaker than the v1 gate")
    if to_number(row.get("min_win_rate")) < MIN_WIN_RATE:
        errors.append("approval min_win_rate is weaker than the v1 gate")
    if to_number(row.get("min_median_return")) < MIN_MEDIAN_RETURN:
        errors.append("approval min_median_return is weaker than the v1 gate")
    if to_number(row.get("min_research_score")) < MIN_RESEARCH_SCORE:
        errors.append("approval min_research_score is weaker than the v1 gate")
    if int(to_number(row.get("evidence_positive_rank_rows"), 0)) <= 0:
        errors.append("approval must have at least one positive confirmed rank row")

    return errors


def validate_positive_rank_source() -> list[str]:
    errors: list[str] = []
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    if df.empty:
        return errors
    row = df.iloc[0]
    source = Path("output/latest") / str(row.get("evidence_rank_source", ""))
    rank = read_csv(source, dtype=str).fillna("")
    if rank.empty:
        return [f"missing approval evidence rank source: {source}"]
    positive = positive_rank_rows(rank)
    expected_count = int(to_number(row.get("evidence_positive_rank_rows"), 0))
    if len(positive) != expected_count:
        errors.append(f"positive rank row count mismatch: artifact={expected_count}, recomputed={len(positive)}")
    if not positive.empty and "approved_for_daily" in positive.columns:
        raw_approved = set(positive["approved_for_daily"].astype(str).str.lower())
        if raw_approved != {"false"}:
            errors.append(f"raw rank rows should remain research evidence rows, got approved_for_daily={sorted(raw_approved)}")
    return errors


def main() -> int:
    errors = validate_files() + validate_approval() + validate_positive_rank_source()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    df = read_csv(OUT_CSV, dtype=str).fillna("")
    print("approved operation pattern validation passed")
    print(f"validated_output={OUT_CSV}")
    print(f"approved_models={df['model_id'].tolist()}")
    print(f"operation_module_id={df.iloc[0]['operation_module_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
