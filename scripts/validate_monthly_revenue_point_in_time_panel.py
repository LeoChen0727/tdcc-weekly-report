from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_monthly_revenue_point_in_time_panel import (  # noqa: E402
    DOCS_PANEL_CSV,
    DOCS_PANEL_MD,
    OUTPUT_COLUMNS,
    PANEL_CSV,
    PANEL_ID,
    PANEL_MD,
    PANEL_VERSION,
)


ALLOWED_POINT_IN_TIME_STATUS = {
    "ready_snapshot_observed_missing_release_date",
    "ready_reported_release_date_confirmed",
    "blocked_future_reported_release_date",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_docs_mirror(errors: list[str]) -> None:
    for output_path, docs_path in [(PANEL_CSV, DOCS_PANEL_CSV), (PANEL_MD, DOCS_PANEL_MD)]:
        if not output_path.exists():
            errors.append(f"missing output artifact: {output_path.as_posix()}")
            continue
        if not docs_path.exists():
            errors.append(f"missing docs/latest mirror: {docs_path.as_posix()}")
            continue
        if output_path.read_bytes() != docs_path.read_bytes():
            errors.append(f"docs/latest mirror differs: {docs_path.as_posix()}")


def validate_panel(panel: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = set(OUTPUT_COLUMNS) - set(panel.columns)
    if missing:
        errors.append(f"monthly revenue PIT panel missing columns: {sorted(missing)}")
        return errors
    if panel.empty:
        errors.append("monthly revenue PIT panel is empty")
        return errors

    panel_ids = set(panel["panel_id"].astype(str))
    if panel_ids != {PANEL_ID}:
        errors.append(f"unexpected panel_id values: {sorted(panel_ids)}")

    versions = set(panel["panel_version"].astype(str))
    if versions != {PANEL_VERSION}:
        errors.append(f"unexpected panel_version values: {sorted(versions)}")

    statuses = set(panel["point_in_time_status"].astype(str))
    if statuses - ALLOWED_POINT_IN_TIME_STATUS:
        errors.append(f"unexpected point_in_time_status values: {sorted(statuses - ALLOWED_POINT_IN_TIME_STATUS)}")

    duplicated = panel.duplicated(["stock_id", "observed_as_of_date", "revenue_period"], keep=False)
    if duplicated.any():
        errors.append("monthly revenue PIT panel must be unique by stock_id + observed_as_of_date + revenue_period")

    missing_key = panel[
        panel["stock_id"].astype(str).eq("")
        | panel["observed_as_of_date"].astype(str).eq("")
        | panel["revenue_period"].astype(str).eq("")
    ]
    if not missing_key.empty:
        errors.append("monthly revenue PIT panel has blank stock_id, observed_as_of_date, or revenue_period")

    future_snapshot = panel[
        panel["observed_as_of_date"].astype(str) > panel["source_snapshot_date"].astype(str)
    ]
    if not future_snapshot.empty:
        errors.append("observed_as_of_date must not be after source_snapshot_date")

    dated_release = panel[panel["reported_release_date"].astype(str).ne("")]
    future_release = dated_release[
        dated_release["reported_release_date"].astype(str) > dated_release["observed_as_of_date"].astype(str)
    ]
    if not future_release.empty:
        errors.append("reported_release_date must not be after observed_as_of_date for usable rows")

    ready = panel[panel["research_join_allowed"].astype(str).eq("True")]
    if ready.empty:
        errors.append("monthly revenue PIT panel has no research_join_allowed rows")

    formal_allowed = panel[panel["allowed_for_formal_historical_model_use"].astype(str).eq("True")]
    if not formal_allowed.empty:
        errors.append("coverage-limited monthly revenue panel must not allow formal historical model use")

    bad_release_claim = panel[
        panel["reported_release_date_status"].astype(str).str.contains("not_actual_release_date_year_month", regex=False)
        & panel["reported_release_date"].astype(str).ne("")
    ]
    if not bad_release_claim.empty:
        errors.append("year-month revenue period values must not be treated as actual release dates")

    numeric_cols = ["latest_revenue_yoy_pct", "cumulative_revenue_yoy_pct"]
    no_numeric = panel[
        panel[numeric_cols].fillna("").astype(str).apply(lambda col: col.str.strip().eq("")).all(axis=1)
    ]
    if not no_numeric.empty:
        errors.append("monthly revenue PIT panel rows must include latest or cumulative YoY value")

    return errors


def main() -> int:
    errors: list[str] = []
    validate_docs_mirror(errors)
    try:
        panel = read_csv(PANEL_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing monthly revenue PIT panel artifact: {exc}")
        panel = pd.DataFrame()

    if not panel.empty:
        errors.extend(validate_panel(panel))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"validated_monthly_revenue_point_in_time_panel_rows={len(panel)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
