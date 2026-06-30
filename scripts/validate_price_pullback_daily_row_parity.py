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
        if published_gap != max(published - overlap, 0):
            errors.append(f"row {idx} published_not_in_proxy_rows does not equal published-overlap")
        if proxy_gap != max(proxy - overlap, 0):
            errors.append(f"row {idx} proxy_not_published_rows does not equal proxy-overlap")

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
