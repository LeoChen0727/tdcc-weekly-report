from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DATA_DIR,
    LATEST_DIR,
    latest_price_date,
    load_price_history,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    pct_return,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


RAW_LATEST = LATEST_DIR / "warrant_daily_raw_latest.csv"
FLOW_LATEST = LATEST_DIR / "warrant_flow_latest.csv"
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"

DATA_WARRANT_DAILY = DATA_DIR / "warrant_daily"
DATA_WARRANT_FLOW = DATA_DIR / "warrant_flow_by_stock"
REPORT_MD = LATEST_DIR / "warrant_market_report_latest.md"
REPORT_PDF = LATEST_DIR / "warrant_market_report_latest.pdf"
FLOW_BY_STOCK_LATEST = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
SECTOR_HEAT_LATEST = LATEST_DIR / "warrant_sector_heat_latest.csv"
PERFORMANCE_MD = LATEST_DIR / "warrant_signal_performance_latest.md"


FLOW_COLUMNS = [
    "date",
    "stock_id",
    "stock_name",
    "call_warrant_count",
    "put_warrant_count",
    "call_turnover",
    "put_turnover",
    "total_warrant_turnover",
    "call_volume",
    "put_volume",
    "total_warrant_volume",
    "call_put_turnover_ratio",
    "candidate_category",
    "candidate_category_zh",
    "sector",
    "sub_theme",
    "tdcc_status",
    "tdcc_status_zh",
    "warrant_flow_signal",
    "warrant_flow_signal_zh",
    "data_quality_note",
]

SECTOR_COLUMNS = [
    "sector_or_theme",
    "stock_count",
    "call_turnover",
    "put_turnover",
    "total_warrant_turnover",
    "call_put_turnover_ratio",
    "representative_codes",
    "interpretation_zh",
]

PERFORMANCE_COLUMNS = [
    "date",
    "stock_id",
    "stock_name",
    "call_turnover",
    "put_turnover",
    "return_d1",
    "return_d3",
    "return_d5",
    "return_d10",
]

NUMERIC_COLUMNS = [
    "call_turnover",
    "put_turnover",
    "total_warrant_turnover",
    "call_volume",
    "put_volume",
    "total_warrant_volume",
    "call_put_turnover_ratio",
    "call_warrant_count",
    "put_warrant_count",
    "latest_warrant_count",
    "issuer_count",
    "top_issuer_call_turnover",
    "top_issuer_put_turnover",
    "issued_quantity_total",
    "cancelled_quantity_total",
    "call_turnover_change_1d",
    "call_turnover_change_5d",
    "put_turnover_change_1d",
    "put_turnover_change_5d",
    "call_volume_change_1d",
    "call_volume_change_5d",
    "put_volume_change_1d",
    "put_volume_change_5d",
    "low_float_call_spike_count",
    "low_float_put_spike_count",
    "warrant_flow_score",
]

CATEGORY_LABEL_ZH = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發但股價尚未反應",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
    "short_term_specialty": "短線專項",
    "tdcc_short_term_edge": "TDCC短線延續",
    "non_revenue_momentum": "營收未確認但題材先動",
    "volume_range_breakout": "底部放量攻擊",
    "bottom_volume_attack": "底部放量攻擊",
    "volume_breakout": "底部放量攻擊",
    "hot_theme_pullback": "熱門族群回檔",
}

TDCC_STATUS_ZH = {
    "strong_accumulation": "大戶強累積",
    "mild_accumulation": "大戶溫和增加",
    "neutral": "中性",
    "distribution_warning": "大戶轉弱警示",
    "insufficient_tdcc_history": "TDCC歷史不足",
}

WARRANT_SIGNAL_ZH = {
    "call_strong_inflow": "認購明確偏多",
    "call_inflow": "認購偏多",
    "call_put_bullish": "權證偏多",
    "put_strong_inflow": "認售明確偏空",
    "put_inflow": "認售偏空",
    "put_call_bearish": "權證偏空",
    "mixed_flow": "權證多空混合",
    "call_activity_observation": "認購活躍觀察",
    "put_activity_observation": "認售活躍觀察",
    "low_float_call_spike": "低流動性認購異常",
    "no_signal": "無明確訊號",
    "": "",
}

THEME_LABEL_ZH = {
    "core_mainstream": "主流族群",
    "mainstream": "主流族群",
    "non_mainstream": "非主流族群",
    "both": "主流 / 非主流皆可",
    "unclassified": "未分類",
    "unknown": "未分類",
}


def translate_tokens(value: Any, mapping: dict[str, str], fallback: str = "") -> str:
    text = safe_str(value).strip()
    if not text:
        return fallback
    parts = [
        part.strip()
        for part in text.replace(";", ",").replace("|", ",").split(",")
        if part.strip()
    ]
    if not parts:
        parts = [text]
    translated = [mapping.get(part, part) for part in parts]
    translated = [item for item in translated if safe_str(item)]
    return "、".join(dict.fromkeys(translated)) or fallback


def translate_theme(value: Any) -> str:
    text = safe_str(value)
    if not text:
        return ""
    return translate_tokens(text, THEME_LABEL_ZH, text)


def ensure_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def numeric_sum(df: pd.DataFrame, col: str) -> float:
    if col not in df.columns:
        return 0.0
    return float(pd.to_numeric(df[col], errors="coerce").fillna(0).sum())


def latest_date(df: pd.DataFrame) -> str:
    if df.empty or "date" not in df.columns:
        return ""
    dates = [normalize_date(value) for value in df["date"].astype(str).unique()]
    dates = [date for date in dates if date]
    return max(dates) if dates else ""


def empty_flow(date: str, note: str) -> pd.DataFrame:
    df = pd.DataFrame(columns=FLOW_COLUMNS)
    df.loc[0, "date"] = date
    df.loc[0, "data_quality_note"] = note
    return ensure_columns(df, FLOW_COLUMNS)


def prepare_flow(raw: pd.DataFrame, flow: pd.DataFrame, date: str) -> pd.DataFrame:
    if flow.empty and raw.empty:
        return empty_flow(date, "權證原始資料不足 / 僅能觀察")

    if not flow.empty:
        out = flow.copy()
    else:
        rows: list[dict[str, Any]] = []
        raw = raw.copy()
        raw["stock_id"] = raw["stock_id"].map(normalize_code)
        for stock_id, group in raw.groupby("stock_id", dropna=False):
            call = group[group["call_put"].astype(str).eq("call")] if "call_put" in group.columns else pd.DataFrame()
            put = group[group["call_put"].astype(str).eq("put")] if "call_put" in group.columns else pd.DataFrame()
            rows.append(
                {
                    "date": latest_date(group) or date,
                    "stock_id": stock_id,
                    "stock_name": (
                        safe_str(group["stock_name"].dropna().astype(str).iloc[0])
                        if "stock_name" in group.columns and not group["stock_name"].dropna().empty
                        else ""
                    ),
                    "call_warrant_count": call["warrant_id"].nunique() if "warrant_id" in call.columns else len(call),
                    "put_warrant_count": put["warrant_id"].nunique() if "warrant_id" in put.columns else len(put),
                    "call_turnover": pd.to_numeric(call.get("turnover", pd.Series(dtype=float)), errors="coerce").sum(),
                    "put_turnover": pd.to_numeric(put.get("turnover", pd.Series(dtype=float)), errors="coerce").sum(),
                    "call_volume": pd.to_numeric(call.get("volume", pd.Series(dtype=float)), errors="coerce").sum(),
                    "put_volume": pd.to_numeric(put.get("volume", pd.Series(dtype=float)), errors="coerce").sum(),
                }
            )
        out = pd.DataFrame(rows)

    out = out.copy()
    if "stock_id" in out.columns:
        out["stock_id"] = out["stock_id"].map(normalize_code)
    if "date" not in out.columns:
        out["date"] = date
    out["date"] = out["date"].map(normalize_date).replace("", date)

    for col in NUMERIC_COLUMNS:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")

    if "call_turnover" not in out.columns:
        out["call_turnover"] = 0.0
    if "put_turnover" not in out.columns:
        out["put_turnover"] = 0.0
    if "call_volume" not in out.columns:
        out["call_volume"] = 0.0
    if "put_volume" not in out.columns:
        out["put_volume"] = 0.0
    if "total_warrant_turnover" not in out.columns:
        out["total_warrant_turnover"] = out["call_turnover"].fillna(0) + out["put_turnover"].fillna(0)
    if "total_warrant_volume" not in out.columns:
        out["total_warrant_volume"] = out["call_volume"].fillna(0) + out["put_volume"].fillna(0)
    if "call_put_turnover_ratio" not in out.columns:
        out["call_put_turnover_ratio"] = out.apply(
            lambda row: (
                row["call_turnover"] / row["put_turnover"]
                if to_number(row.get("put_turnover")) > 0
                else math.nan
            ),
            axis=1,
        )
    return out


def add_candidate_context(flow: pd.DataFrame) -> pd.DataFrame:
    candidates = read_csv(ALL_CANDIDATES, dtype=str)
    if candidates.empty or flow.empty:
        out = flow.copy()
        out["candidate_category"] = ""
        out["candidate_category_zh"] = ""
        out["sector"] = ""
        out["sub_theme"] = ""
        out["tdcc_status"] = ""
        out["tdcc_status_zh"] = ""
        out["warrant_flow_signal_zh"] = out.get("warrant_flow_signal", "").map(
            lambda value: translate_tokens(value, WARRANT_SIGNAL_ZH, "")
        ) if "warrant_flow_signal" in out.columns else ""
        return ensure_columns(out, FLOW_COLUMNS)

    candidates = candidates.copy()
    candidates["stock_id"] = candidates["stock_id"].map(normalize_code)
    theme_col = "theme_group" if "theme_group" in candidates.columns else "industry"
    sub_theme_col = "hot_theme_tags" if "hot_theme_tags" in candidates.columns else theme_col
    tdcc_col = "tdcc_judgement" if "tdcc_judgement" in candidates.columns else "tdcc_status"
    context = (
        candidates.groupby("stock_id", as_index=False)
        .agg(
            candidate_category=("category", lambda s: ",".join(sorted(set(s.astype(str))))),
            sector=(theme_col, lambda s: next((safe_str(x) for x in s if safe_str(x)), "")),
            sub_theme=(sub_theme_col, lambda s: next((safe_str(x) for x in s if safe_str(x)), "")),
            tdcc_status=(tdcc_col, lambda s: next((safe_str(x) for x in s if safe_str(x)), "")),
        )
    )
    out = flow.merge(context, on="stock_id", how="left")
    for col in ["candidate_category", "sector", "sub_theme", "tdcc_status"]:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].fillna("")
    out["candidate_category_zh"] = out["candidate_category"].map(
        lambda value: translate_tokens(value, CATEGORY_LABEL_ZH, "")
    )
    out["tdcc_status_zh"] = out["tdcc_status"].map(
        lambda value: translate_tokens(value, TDCC_STATUS_ZH, "")
    )
    out["sector"] = out["sector"].map(translate_theme)
    out["sub_theme"] = out["sub_theme"].map(translate_theme)
    signal_col = "warrant_flow_signal" if "warrant_flow_signal" in out.columns else "flow_signal"
    if signal_col in out.columns:
        out["warrant_flow_signal"] = out[signal_col].fillna("")
        out["warrant_flow_signal_zh"] = out[signal_col].map(
            lambda value: translate_tokens(value, WARRANT_SIGNAL_ZH, "")
        )
    else:
        out["warrant_flow_signal"] = ""
        out["warrant_flow_signal_zh"] = ""
    if "data_quality_note" not in out.columns:
        out["data_quality_note"] = ""
    return ensure_columns(out, FLOW_COLUMNS)


def build_sector_heat(flow: pd.DataFrame) -> pd.DataFrame:
    usable = flow[flow["stock_id"].astype(str).str.len() > 0].copy() if not flow.empty else flow
    if usable.empty:
        return pd.DataFrame(columns=SECTOR_COLUMNS)

    group_col = "sub_theme" if "sub_theme" in usable.columns else "sector"
    usable[group_col] = usable[group_col].replace("", "未分類").fillna("未分類")
    heat = (
        usable.groupby(group_col, as_index=False)
        .agg(
            stock_count=("stock_id", "nunique"),
            call_turnover=("call_turnover", "sum"),
            put_turnover=("put_turnover", "sum"),
            total_warrant_turnover=("total_warrant_turnover", "sum"),
            representative_codes=("stock_id", lambda s: ",".join(s.astype(str).head(10))),
        )
        .rename(columns={group_col: "sector_or_theme"})
    )
    heat["call_put_turnover_ratio"] = heat.apply(
        lambda row: row["call_turnover"] / row["put_turnover"] if row["put_turnover"] else math.nan,
        axis=1,
    )
    heat["interpretation_zh"] = heat.apply(
        lambda row: (
            "認購相對偏多，仍需與價格、TDCC、族群同步確認。"
            if to_number(row.get("call_turnover")) > to_number(row.get("put_turnover"))
            else "權證資金未明顯偏多，僅作輔助觀察。"
        ),
        axis=1,
    )
    heat = heat.sort_values(["call_turnover", "stock_count"], ascending=[False, False])
    return ensure_columns(heat.reset_index(drop=True), SECTOR_COLUMNS)


def build_performance_table(flow: pd.DataFrame) -> pd.DataFrame:
    if flow.empty:
        return pd.DataFrame(columns=PERFORMANCE_COLUMNS)
    rows: list[dict[str, Any]] = []
    hot = flow[flow["stock_id"].astype(str).str.len() > 0].copy()
    if hot.empty:
        return pd.DataFrame(columns=PERFORMANCE_COLUMNS)
    hot = hot.sort_values(["call_turnover", "call_warrant_count"], ascending=[False, False]).head(50)
    for _, row in hot.iterrows():
        code = normalize_code(row.get("stock_id"))
        price = load_price_history(code)
        date = normalize_date(row.get("date"))
        if price.empty or not date:
            continue
        base = price[price["date"] <= date]
        if base.empty:
            continue
        pos = int(base.index[-1])
        close0 = to_number(price.loc[pos, "close"])
        item: dict[str, Any] = {
            "date": date,
            "stock_id": code,
            "stock_name": row.get("stock_name", ""),
            "call_turnover": row.get("call_turnover", ""),
            "put_turnover": row.get("put_turnover", ""),
        }
        for horizon in [1, 3, 5, 10]:
            item[f"return_d{horizon}"] = (
                pct_return(price.loc[pos + horizon, "close"], close0)
                if pos + horizon < len(price)
                else ""
            )
        rows.append(item)
    return ensure_columns(pd.DataFrame(rows), PERFORMANCE_COLUMNS)


def write_performance_md(perf: pd.DataFrame) -> None:
    lines = [
        "# 權證訊號後續績效追蹤",
        "",
        f"- generated_at: `{now_text()}`",
        "- 說明：權證只作輔助訊號，不可單獨作為買進理由。",
        "",
    ]
    if perf.empty:
        lines.append("目前資料不足 / 僅能觀察。")
    else:
        lines.append(markdown_table(perf, PERFORMANCE_COLUMNS, 50))
    PERFORMANCE_MD.write_text("\n".join(lines), encoding="utf-8")


def format_number(value: Any) -> str:
    num = to_number(value)
    if math.isnan(num):
        return "-"
    if abs(num) >= 1000:
        return f"{num:,.0f}"
    return f"{num:.2f}".rstrip("0").rstrip(".")


def write_pdf(md_path: Path, pdf_path: Path) -> None:
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.pdfgen import canvas
    except Exception as exc:
        print(f"WARNING: reportlab unavailable: {exc}")
        return

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4
    y = height - 42
    max_chars = 58
    for line in md_path.read_text(encoding="utf-8", errors="replace").splitlines():
        font_size = 16 if line.startswith("# ") else 12 if line.startswith("## ") else 9
        text = line.lstrip("# ").replace("`", "")
        c.setFont("STSong-Light", font_size)
        chunks = [text[i : i + max_chars] for i in range(0, len(text), max_chars)] or [""]
        for chunk in chunks:
            if y < 42:
                c.showPage()
                y = height - 42
                c.setFont("STSong-Light", font_size)
            c.drawString(42, y, chunk)
            y -= font_size + 4
    c.save()


def write_report(flow: pd.DataFrame, heat: pd.DataFrame, date: str, raw_rows: int, source_rows: int) -> None:
    real_flow = flow[flow["stock_id"].astype(str).str.len() > 0].copy()
    turnover_ready = numeric_sum(real_flow, "total_warrant_turnover") > 0
    call_top = (
        real_flow.sort_values(["call_turnover", "call_warrant_count"], ascending=[False, False]).head(20)
        if not real_flow.empty
        else pd.DataFrame(columns=FLOW_COLUMNS)
    )
    put_top = (
        real_flow.sort_values(["put_turnover", "put_warrant_count"], ascending=[False, False]).head(20)
        if not real_flow.empty
        else pd.DataFrame(columns=FLOW_COLUMNS)
    )
    ratio_top = (
        real_flow[pd.to_numeric(real_flow["call_put_turnover_ratio"], errors="coerce").notna()]
        .sort_values("call_put_turnover_ratio", ascending=False)
        .head(20)
        if not real_flow.empty
        else pd.DataFrame(columns=FLOW_COLUMNS)
    )
    overlap = real_flow[real_flow["candidate_category"].astype(str).str.len() > 0] if not real_flow.empty else real_flow
    quality_note = "資料可用" if not real_flow.empty else "資料不足 / 僅能觀察"
    if real_flow.empty:
        quality_note = "權證 raw/flow 檔未提供有效股票層級資料，今日權證分析只能作資料狀態提醒。"

    lines = [
        "# 權證市場輔助分析",
        "",
        f"- generated_at: `{now_text()}`",
        f"- data_date: `{date}`",
        f"- raw_rows: `{raw_rows}`",
        f"- stock_level_rows: `{source_rows}`",
        f"- turnover_ready: `{turnover_ready}`",
        "- 使用限制：權證只作輔助訊號，不可單獨作為買進理由。",
        "",
        "## 資料狀態",
        "",
        quality_note,
        "",
        "## 全市場認購 / 認售概況",
        "",
        f"- 認購成交金額合計：`{format_number(numeric_sum(real_flow, 'call_turnover'))}`",
        f"- 認售成交金額合計：`{format_number(numeric_sum(real_flow, 'put_turnover'))}`",
        f"- 認購權證檔數合計：`{format_number(numeric_sum(real_flow, 'call_warrant_count'))}`",
        f"- 認售權證檔數合計：`{format_number(numeric_sum(real_flow, 'put_warrant_count'))}`",
        "",
        "## 認購熱度前二十名",
        "",
        markdown_table(
            call_top,
            ["stock_id", "stock_name", "call_turnover", "call_warrant_count", "candidate_category_zh", "tdcc_status_zh", "sub_theme"],
            20,
        )
        if not call_top.empty
        else "今日無有效權證股票層級資料。",
        "",
        "## 認售熱度前二十名",
        "",
        markdown_table(
            put_top,
            ["stock_id", "stock_name", "put_turnover", "put_warrant_count", "candidate_category_zh", "tdcc_status_zh", "sub_theme"],
            20,
        )
        if not put_top.empty
        else "今日無有效權證股票層級資料。",
        "",
        "## Call / Put 比偏多觀察",
        "",
        markdown_table(
            ratio_top,
            ["stock_id", "stock_name", "call_put_turnover_ratio", "call_turnover", "put_turnover", "candidate_category_zh", "tdcc_status_zh", "sub_theme"],
            20,
        )
        if not ratio_top.empty
        else "今日無可計算 Call / Put 比的有效資料。",
        "",
        "## 族群熱度",
        "",
        markdown_table(heat, SECTOR_COLUMNS, 40) if not heat.empty else "今日無可用族群權證熱度資料。",
        "",
        "## 候選股交集",
        "",
        markdown_table(
            overlap,
            ["stock_id", "stock_name", "candidate_category_zh", "tdcc_status_zh", "call_turnover", "put_turnover", "sub_theme"],
            60,
        )
        if not overlap.empty
        else "今日權證資料與候選股交集不足 / 僅能觀察。",
        "",
        "## 風險提醒",
        "",
        "- 權證偏多只代表衍生性商品資金有參與，不代表股票本身一定可買。",
        "- 若價格、TDCC、族群擴散不配合，權證熱度不可升級為推薦理由。",
        "- 若 turnover_ready=False，成交金額不可作為資金熱度判斷，只能看檔數、覆蓋度與交集。",
        "",
    ]
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    write_pdf(REPORT_MD, REPORT_PDF)


def main() -> int:
    raw = read_csv(RAW_LATEST, dtype=str)
    flow_source = read_csv(FLOW_LATEST, dtype=str)
    date = latest_date(raw) or latest_date(flow_source) or latest_price_date()
    if not date:
        date = normalize_date(now_text()) or "unknown"

    DATA_WARRANT_DAILY.mkdir(parents=True, exist_ok=True)
    DATA_WARRANT_FLOW.mkdir(parents=True, exist_ok=True)
    if not raw.empty:
        write_csv(raw, DATA_WARRANT_DAILY / f"{date}.csv")

    flow = prepare_flow(raw, flow_source, date)
    if "date" in flow.columns:
        flow["date"] = flow["date"].map(normalize_date).replace("", date)
        flow = flow[flow["date"].eq(date) | flow["date"].eq("")].copy()
    flow = add_candidate_context(flow)
    flow = ensure_columns(flow, FLOW_COLUMNS)
    write_csv(flow, DATA_WARRANT_FLOW / f"{date}.csv")
    write_csv(flow, FLOW_BY_STOCK_LATEST)

    heat = build_sector_heat(flow)
    write_csv(heat, SECTOR_HEAT_LATEST)

    perf = build_performance_table(flow)
    write_performance_md(perf)
    write_report(flow, heat, date, len(raw), len(flow_source))

    print(f"Saved: {DATA_WARRANT_DAILY / f'{date}.csv'}")
    print(f"Saved: {DATA_WARRANT_FLOW / f'{date}.csv'}")
    print(f"Saved: {REPORT_MD}")
    print(f"Saved: {REPORT_PDF}")
    print(f"Saved: {FLOW_BY_STOCK_LATEST}")
    print(f"Saved: {SECTOR_HEAT_LATEST}")
    print(f"Saved: {PERFORMANCE_MD}")
    if raw.empty and flow_source.empty:
        print("WARNING: warrant raw/flow latest files are missing; emitted observe-only outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
