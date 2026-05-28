from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


LATEST_DIR = Path("output/latest")
THEME_LAYER_CSV = LATEST_DIR / "volume_attack_theme_layer_latest.csv"
THEME_LAYER_MD = LATEST_DIR / "volume_attack_theme_layer_latest.md"
STOCK_LAYER_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
STOCK_LAYER_MD = LATEST_DIR / "volume_attack_theme_stocks_latest.md"
VALIDATION_JSON = LATEST_DIR / "volume_attack_theme_layer_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "volume_attack_theme_layer_validation_latest.md"

VALID_THEME_STATUSES = {
    "confirmed_volume_theme",
    "early_mainstream_candidate",
    "watch_volume_theme",
    "single_stock_volume_attack",
    "overheated_volume_theme",
    "failed_volume_theme",
    "weak_or_non_mainstream_volume_watch",
    "non_mainstream_volume_watch",
    "theme_status_missing",
    "insufficient_data",
}

REQUIRED_THEME_COLUMNS = [
    "theme_name",
    "theme_final_status",
    "theme_structural_status",
    "theme_mainstream_label",
    "theme_volume_attack_status",
    "volume_attack_count",
    "leader_stock_id",
    "leader_stock_name",
    "interpretation",
]

REQUIRED_STOCK_COLUMNS = [
    "stock_id",
    "stock_name",
    "theme_name",
    "theme_final_status",
    "theme_structural_status",
    "theme_mainstream_label",
    "theme_volume_attack_status",
    "volume_breakout_type",
    "volume_breakout_priority",
    "selection_status",
    "candidate_source_type",
]


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def missing_columns(df: pd.DataFrame, required: list[str]) -> list[str]:
    return [col for col in required if col not in df.columns]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    theme = read_csv(THEME_LAYER_CSV)
    stocks = read_csv(STOCK_LAYER_CSV)

    for path in [THEME_LAYER_CSV, THEME_LAYER_MD, STOCK_LAYER_CSV, STOCK_LAYER_MD]:
        if not path.exists():
            errors.append(f"missing_file: {path.as_posix()}")

    if not theme.empty:
        miss = missing_columns(theme, REQUIRED_THEME_COLUMNS)
        if miss:
            errors.append(f"theme_layer missing columns: {miss}")
        if "theme_volume_attack_status" in theme.columns:
            invalid = sorted(set(theme["theme_volume_attack_status"].astype(str)) - VALID_THEME_STATUSES)
            if invalid:
                errors.append(f"theme_layer invalid theme_volume_attack_status: {invalid}")
    else:
        warnings.append("theme_layer_empty")

    if not stocks.empty:
        miss = missing_columns(stocks, REQUIRED_STOCK_COLUMNS)
        if miss:
            errors.append(f"stock_layer missing columns: {miss}")
        for col in ["theme_final_status", "theme_volume_attack_status"]:
            if col in stocks.columns and (stocks[col].astype(str).str.strip() == "").any():
                errors.append(f"stock_layer has blank {col}")
    else:
        warnings.append("stock_layer_empty")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "theme_rows": int(len(theme)),
        "stock_rows": int(len(stocks)),
    }

    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    VALIDATION_MD.write_text(
        "\n".join(
            [
                "# Volume Attack Theme Layer Validation",
                "",
                f"- status: `{result['status']}`",
                f"- theme_rows: `{result['theme_rows']}`",
                f"- stock_rows: `{result['stock_rows']}`",
                f"- errors: `{'; '.join(errors) if errors else 'none'}`",
                f"- warnings: `{'; '.join(warnings) if warnings else 'none'}`",
                "",
            ]
        ),
        encoding="utf-8",
    )

    if errors:
        raise SystemExit(1)
    print(f"volume_attack_theme_layer validation pass: theme_rows={len(theme)} stock_rows={len(stocks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
