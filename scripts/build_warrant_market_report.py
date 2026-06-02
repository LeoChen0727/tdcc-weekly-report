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
    fmt_pct,
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
TDCC_LATEST = LATEST_DIR / "tdcc_holder_ratio_latest.csv"

DATA_WARRANT_DAILY = DATA_DIR / "warrant_daily"
DATA_WARRANT_FLOW = DATA_DIR / "warrant_flow_by_stock"
REPORT_MD = LATEST_DIR / "warrant_market_report_latest.md"
REPORT_PDF = LATEST_DIR / "warrant_market_report_latest.pdf"
FLOW_BY_STOCK_LATEST = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
SECTOR_HEAT_LATEST = LATEST_DIR / "warrant_sector_heat_latest.csv"
PERFORMANCE_MD = LATEST_DIR / "warrant_signal_performance_latest.md"


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
    "non_revenue_momentum": "題材先動 / 非營收動能",
    "volume_range_breakout": "帶量突破",
    "volume_breakout": "帶量突破",
    "hot_theme_pullback": "熱門族群回檔",
}

TDCC_STATUS_ZH = {
    "strong_accumulation": "大戶強正向",
    "mild_accumulation": "大戶正向",
    "neutral": "中性",
    "distribution_warning": "大戶轉弱",
    "insufficient_tdcc_history": "TDCC資料不足",
}

WARRANT_SIGNAL_ZH = {
    "call_strong_inflow": "認購明確偏多",
    "call_inflow": "認購偏多",
    "call_put_bullish": "認購/認售結構偏多",
    "put_strong_inflow": "認售明確偏空",
    "put_inflow": "認售偏空",
    "put_call_bearish": "認售/認購結構偏空",
    "mixed_flow": "權證多空混合",
    "call_activity_observation": "認購活躍觀察",
    "put_activity_observation": "認售活躍觀察",
    "low_float_call_spike": "低流通認購異常",
    "no_signal": "權證無明確訊號",
    "": "",
}


def translate_tokens(value: Any, mapping: dict[str, str], fallback: str = "") -> str:
    text = safe_str(value).strip()
    if not text or text.lower() == "nan":
        return fallback
    parts = [p.strip() for p in text.replace(";", ",").replace("|", ",").split(",") if p.strip()]
    if not parts:
        parts = [text]
    translated = [mapping.get(part, part) for part in parts]
    translated = [x for x in translated if x and x.lower() != "nan"]
    return "、".join(dict.fromkeys(translated)) or fallback


def numeric_sum(df: pd.DataFrame, col: str) -> float:
    if col not in df.columns:
        return 0.0
    return float(pd.to_numeric(df[col], errors="coerce").fillna(0).sum())


def latest_date(df: pd.DataFrame) -> str:
    if df.empty or "date" not in df.columns:
        return ""
    dates = [normalize_date(x) for x in df["date"].astype(str).unique()]
    dates = [d for d in dates if d]
    return max(dates) if dates else ""


def prepare_flow(raw: pd.DataFrame, flow: pd.DataFrame) -> pd.DataFrame:
    if flow.empty and raw.empty:
        return pd.DataFrame()
    if not flow.empty:
        out = flow.copy()
    else:
        rows: list[dict[str, Any]] = []
        raw["stock_id"] = raw["stock_id"].map(normalize_code)
        for stock_id, group in raw.groupby("stock_id", dropna=False):
            call = group[group["call_put"].astype(str).eq("call")]
            put = group[group["call_put"].astype(str).eq("put")]
            rows.append(
                {
                    "date": latest_date(group),
                    "stock_id": stock_id,
                    "stock_name": safe_str(group["stock_name"].dropna().astype(str).iloc[0]) if "stock_name" in group.columns and not group["stock_name"].dropna().empty else "",
                    "call_warrant_count": call["warrant_id"].nunique() if "warrant_id" in call.columns else len(call),
                    "put_warrant_count": put["warrant_id"].nunique() if "warrant_id" in put.columns else len(put),
                    "call_turnover": pd.to_numeric(call.get("turnover", pd.Series(dtype=float)), errors="coerce").sum(),
                    "put_turnover": pd.to_numeric(put.get("turnover", pd.Series(dtype=float)), errors="coerce").sum(),
                    "call_volume": pd.to_numeric(call.get("volume", pd.Series(dtype=float)), errors="coerce").sum(),
                    "put_volume": pd.to_numeric(put.get("volume", pd.Series(dtype=float)), errors="coerce").sum(),
                }
            )
        out = pd.DataFrame(rows)
    out["stock_id"] = out["stock_id"].map(normalize_code)
    for col in NUMERIC_COLUMNS:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    if "total_warrant_turnover" not in out.columns:
        out["total_warrant_turnover"] = out.get("call_turnover", 0).fillna(0) + out.get("put_turnover", 0).fillna(0)
    if "call_put_turnover_ratio" not in out.columns:
        out["call_put_turnover_ratio"] = out.apply(lambda r: r["call_turnover"] / r["put_turnover"] if to_number(r.get("put_turnover")) > 0 else math.nan, axis=1)
    return out


def add_candidate_context(flow: pd.DataFrame) -> pd.DataFrame:
    candidates = read_csv(ALL_CANDIDATES, dtype=str)
    if candidates.empty:
        flow["candidate_category"] = ""
        flow["sector"] = ""
        flow["sub_theme"] = ""
        flow["tdcc_status"] = ""
        return flow
    candidates["stock_id"] = candidates["stock_id"].map(normalize_code)
    context = (
        candidates.groupby("stock_id", as_index=False)
        .agg(
            candidate_category=("category", lambda s: ",".join(sorted(set(s.astype(str))))),
            sector=("theme_group", lambda s: next((x for x in s.astype(str) if x and x != "nan"), "")),
            sub_theme=("細分族群", lambda s: next((x for x in s.astype(str) if x and x != "nan"), "")),
            tdcc_status=("tdcc_judgement", lambda s: next((x for x in s.astype(str) if x and x != "nan"), "")),
        )
    )
    out = flow.merge(context, on="stock_id", how="left")
    for col in ["candidate_category", "sector", "sub_theme", "tdcc_status"]:
        if col not in out.columns:
            out[col] = ""
    out["candidate_category_zh"] = out["candidate_category"].map(lambda x: translate_tokens(x, CATEGORY_LABEL_ZH, ""))
    out["tdcc_status_zh"] = out["tdcc_status"].map(lambda x: translate_tokens(x, TDCC_STATUS_ZH, ""))
    if "warrant_flow_signal" in out.columns:
        out["warrant_flow_signal_zh"] = out["warrant_flow_signal"].map(lambda x: translate_tokens(x, WARRANT_SIGNAL_ZH, ""))
    if "flow_signal" in out.columns and "warrant_flow_signal_zh" not in out.columns:
        out["warrant_flow_signal_zh"] = out["flow_signal"].map(lambda x: translate_tokens(x, WARRANT_SIGNAL_ZH, ""))
    return out


def build_sector_heat(flow: pd.DataFrame) -> pd.DataFrame:
    if flow.empty:
        return pd.DataFrame()
    group_col = "sub_theme" if "sub_theme" in flow.columns else "sector"
    df = flow.copy()
    df[group_col] = df[group_col].replace("", "unknown").fillna("unknown")
    heat = (
        df.groupby(group_col, as_index=False)
        .agg(
            stock_count=("stock_id", "nunique"),
            call_turnover=("call_turnover", "sum"),
            put_turnover=("put_turnover", "sum"),
            total_warrant_turnover=("total_warrant_turnover", "sum"),
            call_warrant_count=("call_warrant_count", "sum"),
            put_warrant_count=("put_warrant_count", "sum"),
            representative_codes=("stock_id", lambda s: ",".join(s.astype(str).head(10))),
        )
        .rename(columns={group_col: "sector_or_theme"})
    )
    heat["call_put_turnover_ratio"] = heat.apply(lambda r: r["call_turnover"] / r["put_turnover"] if r["put_turnover"] else math.nan, axis=1)
    return heat.sort_values(["call_turnover", "stock_count"], ascending=[False, False]).reset_index(drop=True)


def performance_line(flow: pd.DataFrame) -> str:
    if flow.empty:
        return "目前沒有權證 stock-level flow 可追蹤。"
    rows: list[dict[str, Any]] = []
    hot = flow.sort_values(["call_turnover", "call_warrant_count"], ascending=[False, False]).head(50)
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
        item = {"date": date, "stock_id": code, "stock_name": row.get("stock_name", ""), "call_turnover": row.get("call_turnover", ""), "put_turnover": row.get("put_turnover", "")}
        for h in [1, 3, 5, 10]:
            if pos + h < len(price):
                item[f"return_d{h}"] = pct_return(price.loc[pos + h, "close"], close0)
            else:
                item[f"return_d{h}"] = ""
        rows.append(item)
    perf = pd.DataFrame(rows)
    if perf.empty:
        return "權證熱度後續績效尚未成熟，等待後續交易日累積。"
    lines = [
        "# Warrant Signal Performance",
        "",
        f"- generated_at: `{now_text()}`",
        "- 權證只作輔助訊號，不可單獨作為買進理由。",
        "",
        markdown_table(perf, ["date", "stock_id", "stock_name", "call_turnover", "put_turnover", "return_d1", "return_d3", "return_d5", "return_d10"], 50),
    ]
    return "\n".join(lines)


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
    for line in md_path.read_text(encoding="utf-8", errors="replace").splitlines():
        font_size = 16 if line.startswith("# ") else 12 if line.startswith("## ") else 9
        text = line.lstrip("# ").replace("`", "")
        c.setFont("STSong-Light", font_size)
        for chunk in [text[i : i + 90] for i in range(0, len(text), 90)] or [""]:
            if y < 42:
                c.showPage()
                y = height - 42
                c.setFont("STSong-Light", font_size)
            c.drawString(42, y, chunk)
            y -= font_size + 4
    c.save()


def main() -> int:
    raw = read_csv(RAW_LATEST, dtype=str)
    flow_source = read_csv(FLOW_LATEST, dtype=str)
    if raw.empty and flow_source.empty:
        raise FileNotFoundError("Missing warrant raw/flow latest files")
    date = latest_date(raw) or latest_date(flow_source)
    if not date:
        raise RuntimeError("Unable to determine warrant data date")

    DATA_WARRANT_DAILY.mkdir(parents=True, exist_ok=True)
    DATA_WARRANT_FLOW.mkdir(parents=True, exist_ok=True)
    if not raw.empty:
        write_csv(raw, DATA_WARRANT_DAILY / f"{date}.csv")

    flow = prepare_flow(raw, flow_source)
    flow["date"] = flow["date"].map(normalize_date)
    flow = flow[flow["date"] == date].copy()
    flow = add_candidate_context(flow)
    write_csv(flow, DATA_WARRANT_FLOW / f"{date}.csv")
    write_csv(flow, FLOW_BY_STOCK_LATEST)

    heat = build_sector_heat(flow)
    write_csv(heat, SECTOR_HEAT_LATEST)

    turnover_ready = to_number(flow.get("total_warrant_turnover", pd.Series([0])).sum(), 0) > 0
    call_top = flow.sort_values(["call_turnover", "call_warrant_count"], ascending=[False, False]).head(20)
    put_top = flow.sort_values(["put_turnover", "put_warrant_count"], ascending=[False, False]).head(20)
    ratio_top = flow[pd.to_numeric(flow.get("call_put_turnover_ratio", pd.Series(dtype=float)), errors="coerce").notna()].sort_values("call_put_turnover_ratio", ascending=False).head(20)

    perf_text = performance_line(flow)
    PERFORMANCE_MD.write_text(perf_text, encoding="utf-8")

    lines = [
        "# 全市場權證資料分析與追蹤",
        "",
        f"- generated_at: `{now_text()}`",
        f"- data_date: `{date}`",
        f"- raw_rows: `{len(raw)}`",
        f"- stock_level_rows: `{len(flow)}`",
        f"- turnover_ready: `{turnover_ready}`",
        "- 權證只作輔助訊號，不可單獨作為買進理由。",
        "",
        "## 一、資料狀態",
        "",
        "今日權證資料日期已跟主流程同步。" if date else "無法判斷權證資料日期。",
        "" if turnover_ready else "注意：今日 stock-level 權證成交金額為 0 或缺值，代表官方權證清單已更新，但成交金額/報價資料尚未成功解析；本報告只做清單與可得欄位追蹤，不假裝有資金熱度。",
        "",
        "## 二、全市場認購/認售成交金額總覽",
        "",
        f"- call_turnover_total: `{numeric_sum(flow, 'call_turnover')}`",
        f"- put_turnover_total: `{numeric_sum(flow, 'put_turnover')}`",
        f"- call_warrant_count_total: `{numeric_sum(flow, 'call_warrant_count')}`",
        f"- put_warrant_count_total: `{numeric_sum(flow, 'put_warrant_count')}`",
        "",
        "## 三、認購成交金額前20名標的",
        "",
        markdown_table(call_top, ["stock_id", "stock_name", "call_turnover", "call_warrant_count", "candidate_category_zh", "tdcc_status_zh", "sub_theme"], 20),
        "",
        "## 四、認售成交金額前20名標的",
        "",
        markdown_table(put_top, ["stock_id", "stock_name", "put_turnover", "put_warrant_count", "candidate_category_zh", "tdcc_status_zh", "sub_theme"], 20),
        "",
        "## 五、Call/Put 比異常標的",
        "",
        markdown_table(ratio_top, ["stock_id", "stock_name", "call_put_turnover_ratio", "call_turnover", "put_turnover", "candidate_category_zh", "tdcc_status_zh", "sub_theme"], 20),
        "",
        "## 六、族群權證熱度",
        "",
        markdown_table(heat, ["sector_or_theme", "stock_count", "call_turnover", "put_turnover", "call_put_turnover_ratio", "representative_codes"], 40),
        "",
        "## 七、與每日候選分類、股價型態、TDCC、法人/主力資料交叉比對",
        "",
        markdown_table(flow[flow.get("candidate_category", "").astype(str).str.len() > 0] if "candidate_category" in flow.columns else pd.DataFrame(), ["stock_id", "stock_name", "candidate_category_zh", "tdcc_status_zh", "call_turnover", "put_turnover", "sub_theme"], 60),
        "",
        "## 八、過熱與反指標風險",
        "",
        "- 認購熱度高只是短線資金參考，不可單獨作為買進理由。",
        "- 若股價已過熱、TDCC 轉弱或權證熱度過度集中，應視為追價風險。",
        "- 若成交金額資料缺失，本日不做權證熱度強弱結論。",
        "",
        "## 九、後續追蹤名單",
        "",
        markdown_table(call_top, ["stock_id", "stock_name", "call_turnover", "call_warrant_count", "candidate_category_zh", "tdcc_status_zh", "sub_theme"], 30),
        "",
    ]
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    write_pdf(REPORT_MD, REPORT_PDF)

    print(f"Saved: {DATA_WARRANT_DAILY / f'{date}.csv'}")
    print(f"Saved: {DATA_WARRANT_FLOW / f'{date}.csv'}")
    print(f"Saved: {REPORT_MD}")
    print(f"Saved: {REPORT_PDF}")
    print(f"Saved: {FLOW_BY_STOCK_LATEST}")
    print(f"Saved: {SECTOR_HEAT_LATEST}")
    print(f"Saved: {PERFORMANCE_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
