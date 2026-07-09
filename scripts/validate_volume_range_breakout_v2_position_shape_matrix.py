from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_position_shape_matrix import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    BASE_CONFIRMATION_RULE_ID,
    BASE_ENTRY_RULE_ID,
    BASE_HOLDING_DAYS,
    BASE_SCOPE_ID,
    BASE_STOP_POLICY_ID,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_MATRIX_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MATRIX_CSV,
    LATEST_MD,
    MATRIX_COLUMNS,
    POSITION_AXES,
    POSITION_BUCKETS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SHAPE_BUCKETS,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    WIN_RATE_THRESHOLD_PCT,
)


FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def int_value(value: object) -> int:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(parsed):
        fail(f"expected numeric integer value, got {value!r}")
    return int(parsed)


def numeric_value(value: object) -> float:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(parsed):
        return float("nan")
    return float(parsed)


def validate_common(frame: pd.DataFrame, columns: list[str], name: str) -> None:
    if frame.empty:
        fail(f"{name} must not be empty")
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(frame.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} contains forbidden production fields: {forbidden}")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if set(frame["analysis_scope_id"].astype(str)) != {BASE_SCOPE_ID}:
        fail(f"{name} analysis_scope_id must be {BASE_SCOPE_ID}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def source_scope() -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source promotion readiness detail must not be empty")
    if set(source.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("source detail must come from promotion readiness audit")
    source = source[
        source["holding_days"].astype(str).eq(str(BASE_HOLDING_DAYS))
        & source["stop_policy_id"].astype(str).eq(BASE_STOP_POLICY_ID)
        & source["confirmation_rule_id"].astype(str).eq(BASE_CONFIRMATION_RULE_ID)
        & source["entry_rule_id"].astype(str).eq(BASE_ENTRY_RULE_ID)
    ].copy()
    if source.empty:
        fail("source filter produced no rows")
    if source["source_event_key"].duplicated().any():
        fail("source scope must be unique by source_event_key")
    if not false_only(source.get("approved_for_daily", pd.Series(dtype=str))):
        fail("source approved_for_daily must remain false")
    return source


def validate_detail(detail: pd.DataFrame, source: pd.DataFrame) -> None:
    validate_common(detail, DETAIL_COLUMNS, "detail")
    if len(detail) != len(source):
        fail(f"detail row count mismatch: got {len(detail)} expected {len(source)}")
    if detail["source_event_key"].duplicated().any():
        fail("detail source_event_key must be unique")
    if set(detail["source_event_key"]) != set(source["source_event_key"]):
        fail("detail source_event_key set must equal source scope")
    if set(detail["holding_days"].astype(str)) != {str(BASE_HOLDING_DAYS)}:
        fail("detail holding_days must be the D+15 baseline")
    if set(detail["stop_policy_id"].astype(str)) != {BASE_STOP_POLICY_ID}:
        fail("detail stop_policy_id must be the MA20/EMA23 close stop baseline")
    if set(detail["confirmation_rule_id"].astype(str)) != {BASE_CONFIRMATION_RULE_ID}:
        fail("detail confirmation_rule_id mismatch")
    if set(detail["entry_rule_id"].astype(str)) != {BASE_ENTRY_RULE_ID}:
        fail("detail entry_rule_id mismatch")
    if set(detail["bucket_assignment_status"].astype(str)) != {"assigned"}:
        fail("detail bucket_assignment_status must be assigned")
    if set(detail["shape_bucket"].astype(str)) != set(SHAPE_BUCKETS):
        fail("detail must contain exactly the configured shape buckets")
    for axis in POSITION_AXES:
        suffix = axis.split("_")[1]
        bucket_col = f"position_bucket_{suffix}"
        shape_col = f"position_shape_bucket_{suffix}"
        if set(detail[bucket_col].astype(str)) != set(POSITION_BUCKETS):
            fail(f"detail {bucket_col} must contain exactly the configured position buckets")
        expected = axis + "__" + detail[bucket_col].astype(str) + "__" + detail["shape_bucket"].astype(str)
        if not detail[shape_col].astype(str).equals(expected):
            fail(f"detail {shape_col} must match axis + position bucket + shape bucket")


def validate_metric_formula(row: pd.Series) -> None:
    valid = int_value(row["valid_return_count"])
    expected = False
    if valid > 0:
        expected = (
            numeric_value(row["win_rate_pct"]) >= WIN_RATE_THRESHOLD_PCT
            and numeric_value(row["avg_return_pct"]) > 0
            and numeric_value(row["median_return_pct"]) > 0
        )
    observed = str(row["meets_win_return_metric"]).lower() == "true"
    if observed != expected:
        fail("meets_win_return_metric must depend only on win rate and positive average/median return")


def validate_summary_counts(matrix: pd.DataFrame, detail: pd.DataFrame) -> None:
    for _, row in matrix.iterrows():
        sample = int_value(row["sample_size"])
        valid = int_value(row["valid_return_count"])
        invalid = int_value(row["invalid_return_count"])
        if sample != valid + invalid:
            fail("sample_size must equal valid_return_count + invalid_return_count")
        if int_value(row["source_sample_size"]) != len(detail):
            fail("source_sample_size must equal detail row count")
        if sample > len(detail):
            fail("bucket sample_size cannot exceed source sample size")
        if str(row["sample_count_context"]) != "reported_not_a_disqualifier":
            fail("sample_count_context must report count without disqualifying the bucket")
        if "thin_sample" in str(row["decision_hint"]).lower() or "sample" in str(row["decision_hint"]).lower():
            fail("decision_hint must not reject buckets because of sample size")
        validate_metric_formula(row)
        for col in ["coverage_pct", "win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "stop_exit_rate_pct"]:
            value = numeric_value(row[col])
            if not pd.isna(value) and (value < 0 or value > 100):
                fail(f"{col} out of range")


def validate_matrix(matrix: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_common(matrix, MATRIX_COLUMNS, "matrix")
    if set(matrix["condition_role"].astype(str)) != {"matrix_bucket_not_hidden_gate"}:
        fail("matrix condition_role must remain matrix_bucket_not_hidden_gate")
    expected_row_counts = {
        "overall_baseline": 1,
        "shape_bucket": len(SHAPE_BUCKETS),
        "position_bucket": len(POSITION_AXES) * len(POSITION_BUCKETS),
        "position_shape_bucket": len(POSITION_AXES) * len(POSITION_BUCKETS) * len(SHAPE_BUCKETS),
    }
    actual_counts = matrix["row_type"].value_counts().to_dict()
    if actual_counts != expected_row_counts:
        fail(f"matrix row_type counts mismatch: {actual_counts}")
    validate_summary_counts(matrix, detail)

    overall = matrix[matrix["row_type"].eq("overall_baseline")].iloc[0]
    if int_value(overall["sample_size"]) != len(detail):
        fail("overall baseline sample_size must equal detail row count")

    shape_rows = matrix[matrix["row_type"].eq("shape_bucket")]
    if set(shape_rows["shape_bucket"].astype(str)) != set(SHAPE_BUCKETS):
        fail("shape_bucket rows must cover every shape bucket")
    if int(shape_rows["sample_size"].map(int_value).sum()) != len(detail):
        fail("shape_bucket sample sizes must sum to source sample size")

    for axis in POSITION_AXES:
        suffix = axis.split("_")[1]
        position_col = f"position_bucket_{suffix}"
        axis_position = matrix[
            matrix["row_type"].eq("position_bucket") & matrix["position_axis"].eq(axis)
        ]
        if set(axis_position["position_bucket"].astype(str)) != set(POSITION_BUCKETS):
            fail(f"position_bucket rows must cover every bucket for {axis}")
        if int(axis_position["sample_size"].map(int_value).sum()) != len(detail):
            fail(f"position_bucket sample sizes must sum to source size for {axis}")

        axis_matrix = matrix[
            matrix["row_type"].eq("position_shape_bucket") & matrix["position_axis"].eq(axis)
        ]
        expected_pairs = {(pos, shape) for pos in POSITION_BUCKETS for shape in SHAPE_BUCKETS}
        observed_pairs = set(zip(axis_matrix["position_bucket"], axis_matrix["shape_bucket"]))
        if observed_pairs != expected_pairs:
            fail(f"position_shape matrix must cover every position/shape pair for {axis}")
        if int(axis_matrix["sample_size"].map(int_value).sum()) != len(detail):
            fail(f"position_shape sample sizes must sum to source size for {axis}")

        for _, row in axis_matrix.iterrows():
            expected_count = len(
                detail[
                    detail[position_col].astype(str).eq(row["position_bucket"])
                    & detail["shape_bucket"].astype(str).eq(row["shape_bucket"])
                ]
            )
            if int_value(row["sample_size"]) != expected_count:
                fail(f"matrix sample_size mismatch for {axis} {row['position_bucket']} {row['shape_bucket']}")


def validate_history(latest: pd.DataFrame, history: pd.DataFrame, name: str) -> None:
    if len(latest) != len(history):
        fail(f"{name} latest/history row counts differ")
    if list(latest.columns) != list(history.columns):
        fail(f"{name} latest/history columns differ")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only artifact",
        "Bucket assignment is exhaustive and non-overlapping per position axis.",
        "Sample count is reported as context only and is not a disqualifier.",
        "120d Position x Shape Matrix",
        "240d Position x Shape Matrix",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> None:
    source = source_scope()
    matrix = read_csv(LATEST_MATRIX_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    history_matrix = read_csv(HISTORY_MATRIX_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    validate_detail(detail, source)
    validate_matrix(matrix, detail)
    validate_history(matrix, history_matrix, "matrix")
    validate_history(detail, history_detail, "detail")
    validate_markdown()
    print(
        "volume range breakout v2 position-shape matrix validation passed "
        f"matrix_rows={len(matrix)} detail_rows={len(detail)}"
    )


if __name__ == "__main__":
    main()
