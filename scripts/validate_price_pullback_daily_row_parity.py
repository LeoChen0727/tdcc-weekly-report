from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_parameter_research import (  # noqa: E402
    DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV,
    DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD,
    PRICE_PULLBACK_DAILY_ROW_PARITY_CSV,
    PRICE_PULLBACK_DAILY_ROW_PARITY_MD,
)


REQUIRED_COLUMNS = {
    "generated_at",
    "model_id",
    "snapshot_report_date",
    "research_frame_has_date",
    "outcome_research_frame_has_date",
    "source_row_research_frame_has_date",
    "research_frame_date_basis",
    "published_row_count",
    "published_unique_stock_count",
    "published_duplicate_stock_count",
    "research_proxy_unique_stock_count",
    "overlap_stock_count",
    "published_not_in_proxy_rows",
    "proxy_not_published_rows",
    "published_proxy_coverage_pct",
    "proxy_publish_precision_pct",
    "published_not_in_proxy_sample",
    "proxy_not_published_sample",
    "parity_scope",
    "published_surface",
    "research_proxy_scope",
    "comparison_basis",
    "candidate_universe_snapshot_path",
    "candidate_universe_source_row_count",
    "candidate_universe_condition_stock_count",
    "candidate_universe_missing_required_columns",
    "published_selection_semantics_values",
    "published_source_category_counts",
    "published_report_bucket_counts",
    "candidate_universe_replay_status",
    "parity_gap_driver",
    "published_not_in_proxy_interpretation",
    "proxy_not_published_interpretation",
    "next_required_replay_artifact",
    "parity_status",
    "parity_blocker",
}

VALID_STATUSES = {
    "exact_daily_row_parity_pass",
    "blocked_missing_research_frame_date",
    "blocked_not_exact_daily_row_parity",
    "blocked_unreadable_snapshot",
    "blocked_invalid_snapshot_schema",
}


def _int_value(value: object) -> int:
    try:
        num = float(str(value).replace(",", "").strip())
    except Exception:
        return 0
    return int(num)


def validate_row_parity_frame(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if df.empty:
        return ["price pullback daily row parity artifact is empty"]

    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        return [f"price pullback daily row parity missing columns: {missing}"]

    if set(df["model_id"].astype(str)) != {"price_pullback_23ema"}:
        errors.append("price pullback daily row parity must contain only model_id=price_pullback_23ema")

    bad_status = sorted(set(df["parity_status"].astype(str)) - VALID_STATUSES)
    if bad_status:
        errors.append(f"price pullback daily row parity has invalid statuses: {bad_status}")

    for idx, row in df.iterrows():
        status = str(row.get("parity_status", ""))
        blocker = str(row.get("parity_blocker", "")).strip()
        published = _int_value(row.get("published_unique_stock_count"))
        proxy = _int_value(row.get("research_proxy_unique_stock_count"))
        overlap = _int_value(row.get("overlap_stock_count"))
        published_gap = _int_value(row.get("published_not_in_proxy_rows"))
        proxy_gap = _int_value(row.get("proxy_not_published_rows"))
        has_date = str(row.get("research_frame_has_date", "")).strip() == "True"
        has_outcome_date = str(row.get("outcome_research_frame_has_date", "")).strip() == "True"
        has_source_row_date = str(row.get("source_row_research_frame_has_date", "")).strip() == "True"
        date_basis = str(row.get("research_frame_date_basis", "")).strip()
        gap_driver = str(row.get("parity_gap_driver", "")).strip()
        candidate_replay_status = str(row.get("candidate_universe_replay_status", "")).strip()
        next_replay_artifact = str(row.get("next_required_replay_artifact", "")).strip()
        comparison_basis = str(row.get("comparison_basis", "")).strip()

        if status.startswith("blocked_") and not blocker:
            errors.append(f"row {idx} blocked parity status must include parity_blocker")
        if status == "exact_daily_row_parity_pass" and blocker:
            errors.append(f"row {idx} exact parity pass must not include parity_blocker")
        if status == "exact_daily_row_parity_pass":
            if not has_date or published_gap != 0 or proxy_gap != 0 or overlap != published or overlap != proxy:
                errors.append(f"row {idx} exact parity pass is inconsistent with row counts")
        if status == "blocked_not_exact_daily_row_parity" and published_gap == 0 and proxy_gap == 0:
            errors.append(f"row {idx} not-exact status must have a published/proxy row gap")
        if status == "blocked_missing_research_frame_date" and has_date:
            errors.append(f"row {idx} missing-date status is inconsistent with research_frame_has_date=True")
        if has_date != (has_outcome_date or has_source_row_date):
            errors.append(f"row {idx} research_frame_has_date must match outcome/source-row date flags")
        if not date_basis:
            errors.append(f"row {idx} research_frame_date_basis must be populated")
        if has_date and date_basis == "missing_research_frame_date":
            errors.append(f"row {idx} research_frame_date_basis cannot be missing when research_frame_has_date=True")
        if not has_date and date_basis != "missing_research_frame_date":
            errors.append(f"row {idx} missing research date must use research_frame_date_basis=missing_research_frame_date")
        if published_gap != max(published - overlap, 0):
            errors.append(f"row {idx} published_not_in_proxy_rows does not equal published-overlap")
        if proxy_gap != max(proxy - overlap, 0):
            errors.append(f"row {idx} proxy_not_published_rows does not equal proxy-overlap")
        if not gap_driver:
            errors.append(f"row {idx} parity_gap_driver must be populated")
        if status == "exact_daily_row_parity_pass" and gap_driver != "none_exact":
            errors.append(f"row {idx} exact parity pass must use parity_gap_driver=none_exact")
        if status.startswith("blocked_") and gap_driver == "none_exact":
            errors.append(f"row {idx} blocked parity status cannot use parity_gap_driver=none_exact")
        if not candidate_replay_status:
            errors.append(f"row {idx} candidate_universe_replay_status must be populated")
        if comparison_basis not in {
            "full_research_frame_proxy",
            "production_all_candidates_source_row_replay",
            "unavailable_published_snapshot",
        }:
            errors.append(f"row {idx} comparison_basis has invalid value: {comparison_basis}")
        if comparison_basis == "production_all_candidates_source_row_replay":
            if not str(row.get("candidate_universe_snapshot_path", "")).strip():
                errors.append(f"row {idx} production replay must include candidate_universe_snapshot_path")
            if candidate_replay_status == "candidate_universe_replay_exact_match" and (
                published_gap != 0 or proxy_gap != 0
            ):
                errors.append(f"row {idx} exact candidate-universe replay status is inconsistent with row gaps")
            if candidate_replay_status == "candidate_universe_replay_row_gap" and (
                published_gap == 0 and proxy_gap == 0
            ):
                errors.append(f"row {idx} row-gap candidate-universe replay status must have row gaps")
        if status == "blocked_not_exact_daily_row_parity" and not next_replay_artifact:
            errors.append(f"row {idx} not-exact status must name next_required_replay_artifact")
        if (
            comparison_basis == "full_research_frame_proxy"
            and proxy_gap > published
            and gap_driver != "research_full_universe_proxy_exceeds_daily_candidate_publication_scope"
        ):
            errors.append(f"row {idx} full-universe proxy gap must use the candidate-publication gap driver")

    return errors


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [
        PRICE_PULLBACK_DAILY_ROW_PARITY_CSV,
        PRICE_PULLBACK_DAILY_ROW_PARITY_MD,
        DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV,
        DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD,
    ]:
        if not path.exists():
            errors.append(f"missing price pullback daily row parity artifact: {path}")

    if PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.exists() and DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.exists():
        if PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.read_text(encoding="utf-8") != DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.read_text(encoding="utf-8"):
            errors.append("docs/latest row parity CSV copy does not match output/latest CSV")
    if PRICE_PULLBACK_DAILY_ROW_PARITY_MD.exists() and DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD.exists():
        if PRICE_PULLBACK_DAILY_ROW_PARITY_MD.read_text(encoding="utf-8") != DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD.read_text(encoding="utf-8"):
            errors.append("docs/latest row parity MD copy does not match output/latest MD")

    if PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.exists():
        errors.extend(
            validate_row_parity_frame(
                pd.read_csv(PRICE_PULLBACK_DAILY_ROW_PARITY_CSV, dtype=str, keep_default_na=False).fillna("")
            )
        )
    return errors


def main() -> int:
    errors = validate_files()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("price pullback daily row parity validation passed")
    print(f"validated_output={PRICE_PULLBACK_DAILY_ROW_PARITY_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
