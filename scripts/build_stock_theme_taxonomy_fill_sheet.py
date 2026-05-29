from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

REVIEW_CSV = LATEST_DIR / "stock_theme_taxonomy_review_latest.csv"
OUT_XLSX = LATEST_DIR / "stock_theme_taxonomy_fill_blank_latest.xlsx"
DOCS_XLSX = DOCS_LATEST_DIR / "stock_theme_taxonomy_fill_blank_latest.xlsx"


def read_review() -> pd.DataFrame:
    if not REVIEW_CSV.exists():
        raise FileNotFoundError(REVIEW_CSV)
    return pd.read_csv(REVIEW_CSV, dtype=str, keep_default_na=False)


def make_sheet(df: pd.DataFrame, statuses: list[str], limit: int | None = None) -> pd.DataFrame:
    part = df[df["taxonomy_review_status"].isin(statuses)].copy()
    if "decision_score" in part.columns:
        part["_score"] = pd.to_numeric(part["decision_score"], errors="coerce").fillna(0)
    else:
        part["_score"] = 0
    if "volume_ratio" in part.columns:
        part["_vol"] = pd.to_numeric(part["volume_ratio"], errors="coerce").fillna(0)
    else:
        part["_vol"] = 0
    part = part.sort_values(["_score", "_vol", "stock_id"], ascending=[False, False, True])
    if limit:
        part = part.head(limit)

    out = pd.DataFrame(
        {
            "股票代號": part.get("stock_id", ""),
            "股票名稱": part.get("stock_name", ""),
            "官方產業": part.get("industry", ""),
            "今日候選類型": part.get("category", ""),
            "今日評級": part.get("decision_priority", ""),
            "目前族群": part.get("effective_primary_theme", ""),
            "你填族群": "",
            "備註": "",
        }
    )
    return out.drop_duplicates(["股票代號", "今日候選類型", "今日評級"]).reset_index(drop=True)


def build_workbook(df: pd.DataFrame, path: Path) -> None:
    instructions = pd.DataFrame(
        [
            ["你只需要填哪一欄？", "只填「你填族群」。備註可填可不填。"],
            ["怎麼填？", "用市場常用族群名稱，例如：被動元件、低軌衛星、光通訊、機器人、玻纖布/CCL、ABF載板。"],
            ["不確定怎麼辦？", "空白即可，或在備註寫不確定。"],
            ["目前族群已有值怎麼辦？", "如果你覺得錯，在「你填族群」填正確版本；如果正確就不用填。"],
            ["不要填什麼？", "不用填英文 bucket、不用填主流狀態、不用填信心。那些我後續會轉換。"],
        ],
        columns=["問題", "答案"],
    )

    examples = pd.DataFrame(
        [
            ["2049", "上銀", "電機機械", "機器人/精密傳動"],
            ["1590", "亞德客-KY", "電機機械", "機器人/氣動自動化"],
            ["2374", "佳能", "光電業", "機器人/光學感測"],
            ["2313", "華通", "電子零組件業", "低軌衛星"],
            ["1303", "南亞", "塑膠工業", "玻纖布/CCL"],
            ["6862", "三集瑞-KY", "電子零組件業", "被動元件"],
        ],
        columns=["股票代號", "股票名稱", "官方產業", "你填族群範例"],
    )

    sheets = {
        "先填這張_核心產業待補": make_sheet(df, ["industry_core_needs_market_theme"]),
        "無族群待補": make_sheet(df, ["needs_market_theme_mapping"]),
        "已分類可檢查": make_sheet(df, ["core_ai_related_theme", "mapped_needs_review"]),
        "非主流暫列": make_sheet(df, ["industry_non_mainstream_only", "non_mainstream_theme"]),
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        instructions.to_excel(writer, sheet_name="填寫說明", index=False)
        examples.to_excel(writer, sheet_name="填寫範例", index=False)
        for name, sheet in sheets.items():
            sheet.to_excel(writer, sheet_name=name[:31], index=False)
        for worksheet in writer.sheets.values():
            worksheet.freeze_panes = "A2"
            widths = {
                "A": 12,
                "B": 16,
                "C": 18,
                "D": 18,
                "E": 14,
                "F": 22,
                "G": 24,
                "H": 32,
            }
            for col, width in widths.items():
                worksheet.column_dimensions[col].width = width


def main() -> int:
    df = read_review()
    build_workbook(df, OUT_XLSX)
    build_workbook(df, DOCS_XLSX)
    print(f"Saved: {OUT_XLSX}")
    print(f"Saved: {DOCS_XLSX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
