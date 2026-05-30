from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_code, safe_str, write_csv


OUTPUT = Path("config/stock_theme_taxonomy_manual.csv")


COLUMN_ALIASES = {
    "股票代號": "stock_id",
    "代號": "stock_id",
    "stock_id": "stock_id",
    "股票名稱": "stock_name",
    "股名": "stock_name",
    "stock_name": "stock_name",
    "目前產業": "industry",
    "產業": "industry",
    "industry": "industry",
    "主流/非主流": "theme_mainstream_label",
    "主流非主流": "theme_mainstream_label",
    "主流": "theme_mainstream_label",
    "theme_mainstream_label": "theme_mainstream_label",
    "主要族群1": "primary_theme",
    "主要族群": "primary_theme",
    "族群1": "primary_theme",
    "primary_theme": "primary_theme",
    "族群2": "theme_2",
    "theme_2": "theme_2",
    "族群3": "theme_3",
    "theme_3": "theme_3",
    "備註": "notes",
    "notes": "notes",
}


MAINSTREAM_MAP = {
    "主流": "core_mainstream",
    "核心主流": "core_mainstream",
    "core_mainstream": "core_mainstream",
    "mainstream": "core_mainstream",
    "非主流": "non_mainstream",
    "non_mainstream": "non_mainstream",
    "非AI": "non_mainstream",
    "非ai": "non_mainstream",
    "未分類": "theme_unknown",
    "觀察": "theme_unknown",
    "theme_unknown": "theme_unknown",
    "": "",
}


def read_input(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
        frames = []
        sheets = pd.read_excel(path, sheet_name=None, dtype=str, keep_default_na=False)
        for name, df in sheets.items():
            if str(name).strip() == "填寫說明":
                continue
            frames.append(df)
        return pd.concat(frames, ignore_index=True, sort=False) if frames else pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def normalize_input(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["stock_id"])
    renamed = df.rename(columns={col: COLUMN_ALIASES.get(str(col).strip(), str(col).strip()) for col in df.columns})
    if "stock_id" not in renamed.columns:
        raise RuntimeError("Missing required column: 股票代號 / stock_id")
    for col in ["stock_name", "industry", "theme_mainstream_label", "primary_theme", "theme_2", "theme_3", "notes"]:
        if col not in renamed.columns:
            renamed[col] = ""
    out = renamed[["stock_id", "stock_name", "industry", "theme_mainstream_label", "primary_theme", "theme_2", "theme_3", "notes"]].copy()
    out["stock_id"] = out["stock_id"].map(normalize_code)
    out = out[out["stock_id"].ne("")]
    for col in ["stock_name", "industry", "primary_theme", "theme_2", "theme_3", "notes"]:
        out[col] = out[col].map(safe_str)
    out["theme_mainstream_label"] = out["theme_mainstream_label"].map(lambda x: MAINSTREAM_MAP.get(safe_str(x), safe_str(x)))
    # Keep rows where the user actually supplied a useful override.
    useful_cols = ["theme_mainstream_label", "primary_theme", "theme_2", "theme_3", "notes"]
    mask = out[useful_cols].apply(lambda row: any(safe_str(v) for v in row), axis=1)
    out = out[mask].drop_duplicates("stock_id", keep="last").sort_values("stock_id").reset_index(drop=True)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Import a user-filled stock theme taxonomy Excel/CSV file.")
    parser.add_argument("input_path", help="Path to the filled Excel/CSV file.")
    parser.add_argument("--output", default=str(OUTPUT), help="Output manual override CSV path.")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise FileNotFoundError(input_path)
    out = normalize_input(read_input(input_path))
    write_csv(out, args.output)
    print(f"Saved: {args.output} rows={len(out)}")
    print("Next: python scripts/build_stock_theme_taxonomy.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
