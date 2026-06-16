from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


TAXONOMY_CSV = Path("output/latest/stock_theme_taxonomy_latest.csv")
COMPANY_INDUSTRY_SNAPSHOT = Path("output/latest/company_industry_snapshot_latest.csv")
VALIDATION_JSON = Path("output/latest/stock_theme_taxonomy_validation_latest.json")


REQUIRED_COLUMNS = {
    "stock_id",
    "stock_name",
    "industry",
    "basic_theme",
    "mainstream_membership",
    "hot_theme_1",
    "hot_theme_2",
    "hot_theme_3",
    "hot_theme_4",
    "hot_theme_5",
    "primary_theme",
    "secondary_themes",
    "structural_theme_bucket",
    "theme_structural_status",
    "theme_mainstream_label",
    "report_line_memberships",
    "mainstream_report_eligible",
    "non_mainstream_report_eligible",
    "dual_report_membership_flag",
    "taxonomy_source",
    "confidence",
}


VALID_MAINSTREAM = {"core_mainstream", "non_mainstream", "theme_unknown", ""}
VALID_MAINSTREAM_MEMBERSHIP = {"主流", "非主流", "都有"}
UNRESOLVED_THEME_VALUES = {"", "未分類", "普通股_待補官方產業"}


def normalize_code(value: object) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) <= 4 else text


def is_special_non_common_security(stock_id: object, stock_name: object = "") -> bool:
    code = normalize_code(stock_id)
    name = str(stock_name).strip()
    return (
        code.startswith("00")
        or code.startswith("02")
        or code.startswith("7")
        or code.startswith("91")
        or any(token in name for token in ["購", "售", "牛", "熊", "ETF", "ETN"])
    )


def active_company_stock_ids() -> set[str]:
    if not COMPANY_INDUSTRY_SNAPSHOT.exists():
        return set()
    df = pd.read_csv(COMPANY_INDUSTRY_SNAPSHOT, dtype=str, keep_default_na=False)
    if df.empty or "stock_id" not in df.columns:
        return set()
    return {normalize_code(value) for value in df["stock_id"] if normalize_code(value)}


def main() -> int:
    if not TAXONOMY_CSV.exists():
        raise FileNotFoundError(TAXONOMY_CSV)
    df = pd.read_csv(TAXONOMY_CSV, dtype=str, keep_default_na=False)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise RuntimeError(f"Missing taxonomy columns: {sorted(missing)}")
    duplicate_count = int(df["stock_id"].duplicated().sum())
    invalid_mainstream = sorted(set(df["theme_mainstream_label"]) - VALID_MAINSTREAM)
    basic_theme = df["basic_theme"].astype(str).str.strip()
    primary_theme = df["primary_theme"].astype(str).str.strip()
    unresolved_basic_theme = int(basic_theme.isin(UNRESOLVED_THEME_VALUES).sum())
    unresolved_primary_theme = int(primary_theme.isin(UNRESOLVED_THEME_VALUES).sum())
    active_ids = active_company_stock_ids()
    inactive_common_stock_rows = 0
    if active_ids:
        inactive_common_stock_rows = int(
            df.apply(
                lambda row: normalize_code(row.get("stock_id", "")) not in active_ids
                and not is_special_non_common_security(row.get("stock_id", ""), row.get("stock_name", "")),
                axis=1,
            ).sum()
        )
    invalid_mainstream_membership = sorted(
        value
        for value in set(df["mainstream_membership"].astype(str).str.strip())
        if value not in VALID_MAINSTREAM_MEMBERSHIP
    )
    result = {
        "rows": len(df),
        "duplicate_stock_ids": duplicate_count,
        "invalid_mainstream_labels": invalid_mainstream,
        "unresolved_basic_theme": unresolved_basic_theme,
        "unresolved_primary_theme": unresolved_primary_theme,
        "inactive_common_stock_rows": inactive_common_stock_rows,
        "invalid_mainstream_membership": invalid_mainstream_membership,
        "validation_passed": (
            duplicate_count == 0
            and not invalid_mainstream
            and unresolved_basic_theme == 0
            and unresolved_primary_theme == 0
            and inactive_common_stock_rows == 0
            and not invalid_mainstream_membership
        ),
    }
    if VALIDATION_JSON.exists():
        try:
            previous = json.loads(VALIDATION_JSON.read_text(encoding="utf-8"))
            previous.update(result)
            result = previous
        except Exception:
            pass
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if not result["validation_passed"]:
        raise RuntimeError(json.dumps(result, ensure_ascii=False))
    print(f"Validation passed: {TAXONOMY_CSV} rows={len(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
