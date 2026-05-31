from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_code, safe_str, write_csv


OUTPUT = Path("config/stock_theme_taxonomy_manual.csv")


def u(value: str) -> str:
    """Keep source ASCII-stable while still accepting Chinese workbook headers."""
    return value.encode("ascii").decode("unicode_escape")


COLUMN_ALIASES = {
    u(r"\u80a1\u7968\u4ee3\u865f"): "stock_id",
    u(r"\u4ee3\u865f"): "stock_id",
    "stock_id": "stock_id",
    u(r"\u80a1\u7968\u540d\u7a31"): "stock_name",
    u(r"\u80a1\u540d"): "stock_name",
    u(r"\u540d\u7a31"): "stock_name",
    "stock_name": "stock_name",
    u(r"\u4e0a\u5e02\u6ac3\u7522\u696d"): "industry",
    u(r"\u7522\u696d"): "industry",
    "industry": "industry",
    u(r"\u4e3b\u6d41/\u975e\u4e3b\u6d41"): "theme_mainstream_label",
    u(r"\u4e3b\u6d41\u975e\u4e3b\u6d41"): "theme_mainstream_label",
    u(r"\u5206\u6d41"): "theme_mainstream_label",
    "theme_mainstream_label": "theme_mainstream_label",
    u(r"\u65cf\u7fa4"): "primary_theme",
    u(r"\u65cf\u7fa41"): "primary_theme",
    "primary_theme": "primary_theme",
    u(r"\u65cf\u7fa42"): "theme_2",
    "theme_2": "theme_2",
    u(r"\u65cf\u7fa43"): "theme_3",
    "theme_3": "theme_3",
    u(r"\u65cf\u7fa44"): "theme_4",
    "theme_4": "theme_4",
    u(r"\u65cf\u7fa45"): "theme_5",
    "theme_5": "theme_5",
    u(r"\u5099\u8a3b"): "notes",
    "notes": "notes",
}


MAINSTREAM_MAP = {
    u(r"\u4e3b\u6d41"): "core_mainstream",
    u(r"\u6838\u5fc3\u4e3b\u6d41"): "core_mainstream",
    u(r"AI\u4e3b\u6d41"): "core_mainstream",
    "core_mainstream": "core_mainstream",
    "mainstream": "core_mainstream",
    u(r"\u975e\u4e3b\u6d41"): "non_mainstream",
    u(r"\u50b3\u7522"): "non_mainstream",
    "non_mainstream": "non_mainstream",
    u(r"\u90fd\u6709"): "both",
    u(r"\u96d9\u91cd"): "both",
    u(r"\u4e3b\u6d41+\u975e\u4e3b\u6d41"): "both",
    u(r"\u4e3b\u6d41|\u975e\u4e3b\u6d41"): "both",
    "mainstream|non_mainstream": "both",
    "both": "both",
    u(r"\u5f85\u5206\u985e"): "theme_unknown",
    u(r"\u672a\u5206\u985e"): "theme_unknown",
    "theme_unknown": "theme_unknown",
    "": "",
}


def read_input(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
        frames = []
        sheets = pd.read_excel(path, sheet_name=None, dtype=str, keep_default_na=False)
        for name, df in sheets.items():
            if str(name).strip().lower() in {"instructions", u(r"\u8aaa\u660e")}:
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

    for col in [
        "stock_name",
        "industry",
        "theme_mainstream_label",
        "primary_theme",
        "theme_2",
        "theme_3",
        "theme_4",
        "theme_5",
        "notes",
    ]:
        if col not in renamed.columns:
            renamed[col] = ""

    out = renamed[
        [
            "stock_id",
            "stock_name",
            "industry",
            "theme_mainstream_label",
            "primary_theme",
            "theme_2",
            "theme_3",
            "theme_4",
            "theme_5",
            "notes",
        ]
    ].copy()
    out["stock_id"] = out["stock_id"].map(normalize_code)
    out = out[out["stock_id"].ne("")]

    for col in ["stock_name", "industry", "primary_theme", "theme_2", "theme_3", "theme_4", "theme_5", "notes"]:
        out[col] = out[col].map(safe_str)

    out["theme_3"] = out[["theme_3", "theme_4", "theme_5"]].apply(
        lambda row: ";".join([safe_str(v) for v in row if safe_str(v)]),
        axis=1,
    )
    out = out.drop(columns=["theme_4", "theme_5"])
    out["theme_mainstream_label"] = out["theme_mainstream_label"].map(lambda x: MAINSTREAM_MAP.get(safe_str(x), safe_str(x)))

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
