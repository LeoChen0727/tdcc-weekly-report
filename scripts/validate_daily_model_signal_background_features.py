from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_signal_background_features import (  # noqa: E402
    CATALOG_CSV,
    DOCS_CATALOG_CSV,
    DOCS_CATALOG_MD,
    DOCS_PANEL_CSV,
    DOCS_PANEL_MD,
    FORBIDDEN_MODEL_SEMANTIC_COLUMN_PATTERNS,
    PANEL_CSV,
    PANEL_ID,
    PANEL_MD,
)
from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract  # noqa: E402


REQUIRED_PANEL_COLUMNS = {
    "generated_at",
    "feature_panel_id",
    "feature_scope",
    "stock_id",
    "signal_date",
    "source_model_ids",
    "source_tdcc_dataset_id",
    "feature_as_of_date",
    "point_in_time_status",
    "price_history_rows_as_of",
    "future_price_rows_ignored",
    "close",
    "distance_to_ema23_pct",
    "pre45_return_pct",
    "pre45_range_width_pct",
    "pre45_drawdown_pct",
    "pre90_return_pct",
    "pre90_range_width_pct",
    "macd_hist",
    "rsi14",
    "kd_k_value",
    "kd_d_value",
    "obv",
    "tdcc_as_of_date",
    "tdcc_data_status",
    "tdcc_over_400_change_1w",
    "tdcc_over_1000_change_1w",
    "monthly_revenue_context_as_of_date",
    "monthly_revenue_data_status",
    "monthly_revenue_latest_yoy_pct",
    "monthly_revenue_cumulative_yoy_pct",
    "monthly_revenue_strong_flag",
    "monthly_revenue_formal_model_use_allowed",
    "theme_context_as_of_date",
    "theme_context_data_status",
    "theme_context_status_group",
    "theme_context_source_artifact",
    "market_index_as_of_date",
    "twse_return_20d_pct",
    "tpex_return_20d_pct",
}

REQUIRED_CATALOG_COLUMNS = {
    "generated_at",
    "feature_column",
    "feature_family",
    "feature_scope",
    "allowed_use",
    "model_specific_owner",
    "point_in_time_rule",
}

ALLOWED_PANEL_SCOPES = {"shared_objective_point_in_time"}
ALLOWED_POINT_IN_TIME_STATUS = {
    "exact_signal_date",
    "used_previous_trading_day",
    "missing_price_history",
    "no_price_on_or_before_signal",
}
ALLOWED_THEME_CONTEXT_STATUS = {
    "ready_exact_signal_date",
    "ready_previous_signal_date",
    "missing_theme_status_history",
    "no_theme_on_or_before_signal",
}
ALLOWED_MONTHLY_REVENUE_STATUS = {
    "ready_exact_signal_date",
    "ready_previous_snapshot_date",
    "missing_monthly_revenue_pit_panel",
    "no_revenue_on_or_before_signal",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_docs_mirror(errors: list[str]) -> None:
    for output_path, docs_path in [
        (PANEL_CSV, DOCS_PANEL_CSV),
        (PANEL_MD, DOCS_PANEL_MD),
        (CATALOG_CSV, DOCS_CATALOG_CSV),
        (CATALOG_CSV.with_suffix(".md"), DOCS_CATALOG_MD),
    ]:
        if not output_path.exists():
            errors.append(f"missing output artifact: {output_path.as_posix()}")
            continue
        if not docs_path.exists():
            errors.append(f"missing docs/latest mirror: {docs_path.as_posix()}")
            continue
        if output_path.read_bytes() != docs_path.read_bytes():
            errors.append(f"docs/latest mirror differs: {docs_path.as_posix()}")


def validate_panel(panel: pd.DataFrame, expected_tdcc_dataset_id: str | None = None) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_PANEL_COLUMNS - set(panel.columns)
    if missing:
        errors.append(f"background feature panel missing columns: {sorted(missing)}")
        return errors
    if panel.empty:
        errors.append("background feature panel is empty")
        return errors

    if expected_tdcc_dataset_id:
        dataset_ids = sorted(
            {value for value in panel["source_tdcc_dataset_id"].astype(str) if value}
        )
        if dataset_ids != [expected_tdcc_dataset_id]:
            errors.append(
                "background feature panel source_tdcc_dataset_id mismatch: "
                f"expected {expected_tdcc_dataset_id}, got {dataset_ids}"
            )

    semantic_columns = [
        col
        for col in panel.columns
        for pattern in FORBIDDEN_MODEL_SEMANTIC_COLUMN_PATTERNS
        if pattern in col.lower()
    ]
    if semantic_columns:
        errors.append(f"shared background feature panel contains model-semantic columns: {sorted(set(semantic_columns))}")

    duplicated = panel.duplicated(["stock_id", "signal_date"], keep=False)
    if duplicated.any():
        errors.append("background feature panel must be unique by stock_id + signal_date")

    scopes = set(panel["feature_scope"].astype(str))
    if scopes - ALLOWED_PANEL_SCOPES:
        errors.append(f"unexpected panel feature_scope values: {sorted(scopes - ALLOWED_PANEL_SCOPES)}")

    ids = set(panel["feature_panel_id"].astype(str))
    if ids != {PANEL_ID}:
        errors.append(f"unexpected feature_panel_id values: {sorted(ids)}")

    statuses = set(panel["point_in_time_status"].astype(str))
    if statuses - ALLOWED_POINT_IN_TIME_STATUS:
        errors.append(f"unexpected point_in_time_status values: {sorted(statuses - ALLOWED_POINT_IN_TIME_STATUS)}")

    dated = panel[panel["feature_as_of_date"].astype(str).ne("")]
    future_price = dated[dated["feature_as_of_date"].astype(str) > dated["signal_date"].astype(str)]
    if not future_price.empty:
        errors.append("feature_as_of_date must not be after signal_date")

    dated_tdcc = panel[panel["tdcc_as_of_date"].astype(str).ne("")]
    future_tdcc = dated_tdcc[dated_tdcc["tdcc_as_of_date"].astype(str) > dated_tdcc["signal_date"].astype(str)]
    if not future_tdcc.empty:
        errors.append("tdcc_as_of_date must not be after signal_date")

    revenue_statuses = set(panel["monthly_revenue_data_status"].astype(str))
    if revenue_statuses - ALLOWED_MONTHLY_REVENUE_STATUS:
        errors.append(f"unexpected monthly_revenue_data_status values: {sorted(revenue_statuses - ALLOWED_MONTHLY_REVENUE_STATUS)}")

    dated_revenue = panel[panel["monthly_revenue_context_as_of_date"].astype(str).ne("")]
    future_revenue = dated_revenue[
        dated_revenue["monthly_revenue_context_as_of_date"].astype(str) > dated_revenue["signal_date"].astype(str)
    ]
    if not future_revenue.empty:
        errors.append("monthly_revenue_context_as_of_date must not be after signal_date")

    formal_revenue_allowed = panel[
        panel["monthly_revenue_formal_model_use_allowed"].astype(str).str.lower().isin(["true", "1", "yes"])
    ]
    if not formal_revenue_allowed.empty:
        errors.append("coverage-limited monthly revenue context must not be marked formal model-use allowed")

    theme_statuses = set(panel["theme_context_data_status"].astype(str))
    if theme_statuses - ALLOWED_THEME_CONTEXT_STATUS:
        errors.append(f"unexpected theme_context_data_status values: {sorted(theme_statuses - ALLOWED_THEME_CONTEXT_STATUS)}")

    dated_theme = panel[panel["theme_context_as_of_date"].astype(str).ne("")]
    future_theme = dated_theme[
        dated_theme["theme_context_as_of_date"].astype(str) > dated_theme["signal_date"].astype(str)
    ]
    if not future_theme.empty:
        errors.append("theme_context_as_of_date must not be after signal_date")

    ready_theme = panel[panel["theme_context_data_status"].isin(["ready_exact_signal_date", "ready_previous_signal_date"])]
    ready_without_artifact = ready_theme[ready_theme["theme_context_source_artifact"].astype(str).eq("")]
    if not ready_without_artifact.empty:
        errors.append("theme_context_source_artifact is required when theme context is ready")

    dated_market = panel[panel["market_index_as_of_date"].astype(str).ne("")]
    future_market = dated_market[dated_market["market_index_as_of_date"].astype(str) > dated_market["signal_date"].astype(str)]
    if not future_market.empty:
        errors.append("market_index_as_of_date must not be after signal_date")

    ready = panel[panel["point_in_time_status"].isin(["exact_signal_date", "used_previous_trading_day"])]
    if ready.empty:
        errors.append("background feature panel has no point-in-time ready price rows")

    return errors


def validate_catalog(panel: pd.DataFrame, catalog: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_CATALOG_COLUMNS - set(catalog.columns)
    if missing:
        errors.append(f"background feature catalog missing columns: {sorted(missing)}")
        return errors
    if catalog.empty:
        errors.append("background feature catalog is empty")
        return errors

    catalog_columns = set(catalog["feature_column"].astype(str))
    missing_from_catalog = set(panel.columns) - catalog_columns
    if missing_from_catalog:
        errors.append(f"panel columns missing from catalog: {sorted(missing_from_catalog)}")

    model_specific = catalog[catalog["feature_scope"].eq("model_specific_not_in_shared_panel")]
    required_boundaries = {
        "price_pullback_23ema_operation_filter",
        "neckline_45d_non_bearish_filter",
    }
    missing_boundaries = required_boundaries - set(model_specific["feature_column"].astype(str))
    if missing_boundaries:
        errors.append(f"catalog missing model-specific boundary rows: {sorted(missing_boundaries)}")

    revenue = catalog[catalog["feature_column"].eq("monthly_revenue_point_in_time_panel")]
    if revenue.empty:
        errors.append("catalog must document monthly revenue point-in-time panel")
    elif set(revenue["feature_scope"].astype(str)) != {"shared_objective_point_in_time"}:
        errors.append("monthly revenue point-in-time panel must be marked shared_objective_point_in_time")
    elif not revenue["allowed_use"].astype(str).str.contains("coverage_limited", regex=False).all():
        errors.append("monthly revenue point-in-time panel catalog row must disclose coverage_limited use")

    shared_catalog = catalog[catalog["feature_column"].isin(panel.columns)]
    forbidden_shared = shared_catalog[shared_catalog["feature_scope"].eq("model_specific_not_in_shared_panel")]
    if not forbidden_shared.empty:
        errors.append("panel columns must not be cataloged as model_specific_not_in_shared_panel")

    return errors


def main() -> int:
    errors: list[str] = []
    validate_docs_mirror(errors)
    try:
        panel = read_csv(PANEL_CSV)
        catalog = read_csv(CATALOG_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing background feature artifact: {exc}")
        panel = pd.DataFrame()
        catalog = pd.DataFrame()

    if not panel.empty:
        try:
            expected_tdcc_dataset_id = load_research_tdcc_dataset_contract().dataset_id
        except Exception as exc:
            errors.append(f"cannot load canonical TDCC dataset contract: {exc}")
            expected_tdcc_dataset_id = None
        errors.extend(validate_panel(panel, expected_tdcc_dataset_id))
    if not catalog.empty:
        errors.extend(validate_catalog(panel, catalog))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"validated_background_feature_panel_rows={len(panel)}")
    print(f"validated_background_feature_catalog_rows={len(catalog)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
