from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


TAXONOMY_CSV = Path("output/latest/stock_theme_taxonomy_latest.csv")
VALIDATION_JSON = Path("output/latest/stock_theme_taxonomy_validation_latest.json")


REQUIRED_COLUMNS = {
    "stock_id",
    "stock_name",
    "industry",
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


def main() -> int:
    if not TAXONOMY_CSV.exists():
        raise FileNotFoundError(TAXONOMY_CSV)
    df = pd.read_csv(TAXONOMY_CSV, dtype=str, keep_default_na=False)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise RuntimeError(f"Missing taxonomy columns: {sorted(missing)}")
    duplicate_count = int(df["stock_id"].duplicated().sum())
    invalid_mainstream = sorted(set(df["theme_mainstream_label"]) - VALID_MAINSTREAM)
    result = {
        "rows": len(df),
        "duplicate_stock_ids": duplicate_count,
        "invalid_mainstream_labels": invalid_mainstream,
        "validation_passed": duplicate_count == 0 and not invalid_mainstream,
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
