import io
import pandas as pd
import requests

from datetime import datetime
from pathlib import Path


DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)

REPORT_PATH = OUTPUT_DIR / "stock_monitor_latest.md"
BREAKOUT_CSV_PATH = OUTPUT_DIR / "breakout_latest.csv"
REVENUE_PULLBACK_CSV_PATH = OUTPUT_DIR / "revenue_pullback_latest.csv"

MIN_VOLUME_LOTS = 1000


MAINSTREAM_INDUSTRY_KEYWORDS = [
    "半導體",
    "電子零組件",
    "電腦及週邊",
    "通信網路",
    "光電",
    "其他電子",
    "資訊服務",
    "電子通路",
    "電機機械",
    "綠能環保",
    "生技醫療",
    "數位雲端",
]


def is_mainstream_industry(industry):
    if pd.isna(industry):
        return False

    text = str(industry).strip()

    return any(keyword in text for keyword in MAINSTREAM_INDUSTRY_KEYWORDS)


def split_mainstream(df):
    if df.empty or "industry" not in df.columns:
        return pd.DataFrame(), pd.DataFrame()

    mainstream_df = df[df["industry"].apply(is_mainstream_industry)].copy()
    non_mainstream_df = df[~df["industry"].apply(is_mainstream_industry)].copy()

    return mainstream_df, non_mainstream_df


def load_official_price_history():
    files = sorted(DATA_DIR.glob("*.csv"))

    if not files:
        print("No official daily price files found.")
        return pd.DataFrame()

    frames = []

    for file in files:
        try:
            df = pd.read_csv(file, dtype={"ticker": str})
            frames.append(df)
        except Exception as e:
            print(f"Skip file {file}: {e}")

    if not frames:
        return pd.DataFrame()

    data = pd.concat(frames, ignore_index=True)

    data["ticker"] = data["ticker"].astype(str).str.zfill(4)
    data["date"] = data["date"].astype(str)

    numeric_cols = ["open", "high", "low", "close", "volume", "turnover"]

    for col in numeric_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    data = data.dropna(subset=["ticker", "date", "close", "volume"])
    data = data.sort_values(["ticker", "date"]).reset_index(drop=True)

    return data


def fetch_monthly_revenue():
    urls = [
        ("listed", "https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv"),
        ("otc", "https://mopsfin.twse.com.tw/opendata/t187ap05_O.csv"),
    ]

    frames = []

    for market, url in urls:
        try:
            r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            r.encoding = "utf-8-sig"

            df = pd.read_csv(io.StringIO(r.text))
            df["market"] = market
            frames.append(df)

        except Exception as e:
            print(f"Revenue fetch failed: {market} {e}")

    if not frames:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)

    rename_map = {
        "公司代號": "ticker",
        "公司名稱": "name",
        "產業別": "industry",
        "資料年月": "revenue_period",
        "營業收入-當月營收": "monthly_revenue",
        "營業收入-去年同月增減(%)": "revenue_yoy_pct",
        "累計營業收入-前期比較增減(%)": "cumulative_yoy_pct",
    }

    keep_cols = [c for c in rename_map.keys() if c in df.columns]
    df = df[keep_cols + ["market"]].rename(columns=rename_map)

    df["ticker"] = df["ticker"].astype(str).str.extract(r"(\d{4})")[0]

    for col in ["monthly_revenue", "revenue_yoy_pct", "cumulative_yoy_pct"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("--", "", regex=False)
                .str.strip()
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["ticker", "revenue_yoy_pct", "cumulative_yoy_pct"])

    return df.reset_index(drop=True)


def build_industry_map(revenue_df):
    if revenue_df.empty:
        return {}

    temp = revenue_df.dropna(subset=["ticker"]).copy()
    temp["ticker"] = temp["ticker"].astype(str).str.zfill(4)

    industry_map = {}

    for _, row in temp.iterrows():
        ticker = row["ticker"]
        industry_map[ticker] = {
            "industry": row.get("industry", ""),
            "revenue_period": row.get("revenue_period", ""),
            "revenue_yoy_pct": row.get("revenue_yoy_pct", None),
            "cumulative_yoy_pct": row.get("cumulative_yoy_pct", None),
        }

    return industry_map


def build_stock_history_map(price_data):
    stock_map = {}

    for ticker, group in price_data.groupby("ticker"):
        group = group.sort_values("date").copy()

        if len(group) < 60:
            continue

        stock_map[ticker] = group.reset_index(drop=True)

    return stock_map


def add_technical_metrics(df):
    df = df.copy()
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["vol20"] = df["volume"].rolling(20).mean()
    return df


def calculate_breakout_score(df):
    df = add_technical_metrics(df)

    if len(df) < 61:
        return None

    latest = df.iloc[-1]

    close = latest["close"]
    ma20 = latest["ma20"]
    ma60 = latest["ma60"]
    volume = latest["volume"]
    vol20 = latest["vol20"]
    volume_lots = volume / 1000

    if volume_lots < MIN_VOLUME_LOTS:
        return None

    if pd.isna(ma20) or pd.isna(ma60) or pd.isna(vol20):
        return None

    recent_40 = df.iloc[-41:-1]
    high_40 = recent_40["high"].max()
    low_40 = recent_40["low"].min()

    if low_40 <= 0 or high_40 <= 0:
        return None

    consolidation_range_pct = (high_40 - low_40) / low_40 * 100
    breakout_pct = (close - high_40) / high_40 * 100
    volume_ratio = volume / vol20 if vol20 and vol20 > 0 else 0

    return_5d = (close / df.iloc[-6]["close"] - 1) * 100 if len(df) >= 6 else 0
    gap_ma20 = (close / ma20 - 1) * 100 if ma20 and ma20 > 0 else 0
    gap_ma60 = (close / ma60 - 1) * 100 if ma60 and ma60 > 0 else 0

    score = 0

    if consolidation_range_pct <= 18:
        score += 25
    elif consolidation_range_pct <= 25:
        score += 15

    if breakout_pct >= 0:
        score += 30
    elif breakout_pct >= -2:
        score += 20
    elif breakout_pct >= -5:
        score += 10

    if volume_ratio >= 2:
        score += 25
    elif volume_ratio >= 1.5:
        score += 18
    elif volume_ratio >= 1.2:
        score += 10

    if close > ma20:
        score += 10
    if close > ma60:
        score += 10

    if return_5d > 20:
        score -= 20
    elif return_5d > 12:
        score -= 10

    return {
        "date": latest["date"],
        "close": round(close, 2),
        "volume_lots": round(volume_lots, 0),
        "ma20": round(ma20, 2),
        "ma60": round(ma60, 2),
        "gap_ma20_pct": round(gap_ma20, 2),
        "gap_ma60_pct": round(gap_ma60, 2),
        "high_40": round(high_40, 2),
        "low_40": round(low_40, 2),
        "consolidation_range_pct": round(consolidation_range_pct, 2),
        "breakout_pct": round(breakout_pct, 2),
        "volume_ratio": round(volume_ratio, 2),
        "return_5d_pct": round(return_5d, 2),
        "score": round(score, 1),
    }


def judge_breakout(row):
    if row["score"] >= 80:
        return "強突破候選"
    if row["score"] >= 65:
        return "可觀察"
    if row["score"] >= 50:
        return "初步觀察"
    return "不列入"


def calculate_revenue_pullback_score(df, revenue_row):
    df = add_technical_metrics(df)

    if len(df) < 61:
        return None

    latest = df.iloc[-1]

    close = latest["close"]
    ma20 = latest["ma20"]
    ma60 = latest["ma60"]
    volume = latest["volume"]
    volume_lots = volume / 1000

    if volume_lots < MIN_VOLUME_LOTS:
        return None

    if pd.isna(ma20) or pd.isna(ma60):
        return None

    gap_ma20 = (close / ma20 - 1) * 100 if ma20 and ma20 > 0 else 0
    gap_ma60 = (close / ma60 - 1) * 100 if ma60 and ma60 > 0 else 0

    return_10d = (close / df.iloc[-11]["close"] - 1) * 100 if len(df) >= 11 else 0
    return_20d = (close / df.iloc[-21]["close"] - 1) * 100 if len(df) >= 21 else 0

    revenue_yoy = revenue_row["revenue_yoy_pct"]
    cumulative_yoy = revenue_row["cumulative_yoy_pct"]

    score = 0

    if revenue_yoy >= 50:
        score += 30
    elif revenue_yoy >= 20:
        score += 22
    elif revenue_yoy >= 10:
        score += 12

    if cumulative_yoy >= 30:
        score += 25
    elif cumulative_yoy >= 10:
        score += 18
    elif cumulative_yoy >= 5:
        score += 8

    if return_10d <= -8:
        score += 20
    elif return_10d <= -5:
        score += 14
    elif return_20d <= -8:
        score += 12

    if abs(gap_ma20) <= 5:
        score += 15
    elif abs(gap_ma60) <= 7:
        score += 15
    elif abs(gap_ma20) <= 8:
        score += 8

    if gap_ma60 < -10:
        score -= 20

    if gap_ma20 > 12:
        score -= 15

    return {
        "date": latest["date"],
        "revenue_period": revenue_row.get("revenue_period", ""),
        "industry": revenue_row.get("industry", ""),
        "revenue_yoy_pct": round(revenue_yoy, 2),
        "cumulative_yoy_pct": round(cumulative_yoy, 2),
        "close": round(close, 2),
        "volume_lots": round(volume_lots, 0),
        "ma20": round(ma20, 2),
        "ma60": round(ma60, 2),
        "gap_ma20_pct": round(gap_ma20, 2),
        "gap_ma60_pct": round(gap_ma60, 2),
        "return_10d_pct": round(return_10d, 2),
        "return_20d_pct": round(return_20d, 2),
        "score": round(score, 1),
    }


def judge_revenue_pullback(row):
    if row["score"] >= 80:
        return "高優先觀察"
    if row["score"] >= 65:
        return "可觀察"
    if row["score"] >= 50:
        return "初步觀察"
    return "不列入"


def find_breakout_candidates(stock_map, industry_map):
    rows = []

    for ticker, df in stock_map.items():
        try:
            metrics = calculate_breakout_score(df)

            if metrics is None:
                continue

            if metrics["score"] >= 50:
                latest = df.iloc[-1]
                industry_info = industry_map.get(ticker, {})

                rows.append({
                    "ticker": ticker,
                    "name": latest.get("name", ""),
                    "market": latest.get("market", ""),
                    "industry": industry_info.get("industry", ""),
                    **metrics,
                })

        except Exception as e:
            print(f"Breakout skip {ticker}: {e}")
            continue

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_breakout, axis=1)
    result = result.sort_values(["score", "volume_lots", "volume_ratio"], ascending=False)

    return result.reset_index(drop=True)


def find_revenue_pullback_candidates(stock_map, revenue_df):
    if revenue_df.empty:
        return pd.DataFrame()

    base = revenue_df[
        (revenue_df["revenue_yoy_pct"] >= 20) &
        (revenue_df["cumulative_yoy_pct"] >= 10)
    ].copy()

    rows = []

    for _, item in base.iterrows():
        ticker = str(item["ticker"]).zfill(4)

        if ticker not in stock_map:
            continue

        try:
            price_df = stock_map[ticker]
            metrics = calculate_revenue_pullback_score(price_df, item)

            if metrics is None:
                continue

            if metrics["score"] >= 50:
                latest = price_df.iloc[-1]

                rows.append({
                    "ticker": ticker,
                    "name": item.get("name", latest.get("name", "")),
                    "market": item.get("market", latest.get("market", "")),
                    **metrics,
                })

        except Exception as e:
            print(f"Revenue pullback skip {ticker}: {e}")
            continue

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_revenue_pullback, axis=1)
    result = result.sort_values(["score", "volume_lots", "revenue_yoy_pct"], ascending=False)

    return result.reset_index(drop=True)


def generate_markdown_table(df, columns, rename_map, max_rows=30):
    if df.empty:
        return "沒有符合條件的股票。"

    show_df = df.head(max_rows).copy()
    show_df.insert(0, "rank", range(1, len(show_df) + 1))

    cols = ["rank"] + columns
    table_df = show_df[cols].rename(columns={"rank": "排名", **rename_map})

    return table_df.to_markdown(index=False)


def generate_report(price_data, breakout_df, revenue_pullback_df):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if price_data.empty:
        latest_price_date = "無"
        total_stocks = 0
        trading_days = 0
    else:
        latest_price_date = price_data["date"].max()
        total_stocks = price_data["ticker"].nunique()
        trading_days = price_data["date"].nunique()

    breakout_mainstream_df, breakout_non_mainstream_df = split_mainstream(breakout_df)
    pullback_mainstream_df, pullback_non_mainstream_df = split_mainstream(revenue_pullback_df)

    breakout_columns = [
        "ticker", "name", "industry", "date", "close", "volume_lots", "ma20", "ma60",
        "gap_ma20_pct", "gap_ma60_pct", "volume_ratio", "consolidation_range_pct",
        "breakout_pct", "return_5d_pct", "score", "judge"
    ]

    breakout_rename = {
        "ticker": "代號",
        "name": "名稱",
        "industry": "產業",
        "date": "資料日",
        "close": "收盤價",
        "volume_lots": "成交量張",
        "ma20": "20MA",
        "ma60": "60MA",
        "gap_ma20_pct": "距月線%",
        "gap_ma60_pct": "距季線%",
        "volume_ratio": "量比",
        "consolidation_range_pct": "40日區間%",
        "breakout_pct": "突破40日高點%",
        "return_5d_pct": "近5日漲幅%",
        "score": "分數",
        "judge": "判斷",
    }

    pullback_columns = [
        "ticker", "name", "industry", "date", "revenue_period",
        "revenue_yoy_pct", "cumulative_yoy_pct",
        "close", "volume_lots", "ma20", "ma60",
        "gap_ma20_pct", "gap_ma60_pct",
        "return_10d_pct", "return_20d_pct",
        "score", "judge"
    ]

    pullback_rename = {
        "ticker": "代號",
        "name": "名稱",
        "industry": "產業",
        "date": "價格資料日",
        "revenue_period": "營收年月",
        "revenue_yoy_pct": "月營收YoY%",
        "cumulative_yoy_pct": "累計YoY%",
        "close": "收盤價",
        "volume_lots": "成交量張",
        "ma20": "20MA",
        "ma60": "60MA",
        "gap_ma20_pct": "距月線%",
        "gap_ma60_pct": "距季線%",
        "return_10d_pct": "近10日漲幅%",
        "return_20d_pct": "近20日漲幅%",
        "score": "分數",
        "judge": "判斷",
    }

    lines = []
    lines.append("# 台股每日監測報告")
    lines.append("")
    lines.append(f"產生時間：{now}")
    lines.append(f"最新官方價格資料日：{latest_price_date}")
    lines.append(f"已累積交易日數：{trading_days}")
    lines.append(f"股票檔數：{total_stocks}")
    lines.append(f"成交量門檻：最新交易日成交量 >= {MIN_VOLUME_LOTS} 張")
    lines.append("")
    lines.append("> 價格與成交量資料來源：GitHub 內累積的官方 TWSE / TPEx 每日收盤資料。")
    lines.append("")
    lines.append("> 主流題材版目前保留：半導體、電子零組件、電腦及週邊、通信網路、光電、其他電子、資訊服務、電子通路、電機機械、綠能環保、生技醫療、數位雲端。")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 1. 全市場：盤整帶量突破候選股")
    lines.append("")
    lines.append(generate_markdown_table(breakout_df, breakout_columns, breakout_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 2. 主流題材：盤整帶量突破候選股")
    lines.append("")
    lines.append(generate_markdown_table(breakout_mainstream_df, breakout_columns, breakout_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 3. 非主流 / 防禦傳產：盤整帶量突破候選股")
    lines.append("")
    lines.append(generate_markdown_table(breakout_non_mainstream_df, breakout_columns, breakout_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 4. 全市場：營收成長但股價回檔候選股")
    lines.append("")
    lines.append(generate_markdown_table(revenue_pullback_df, pullback_columns, pullback_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 5. 主流題材：營收成長但股價回檔候選股")
    lines.append("")
    lines.append(generate_markdown_table(pullback_mainstream_df, pullback_columns, pullback_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 6. 非主流 / 防禦傳產：營收成長但股價回檔候選股")
    lines.append("")
    lines.append(generate_markdown_table(pullback_non_mainstream_df, pullback_columns, pullback_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 7. 兩策略交集股")
    lines.append("")

    if breakout_df.empty or revenue_pullback_df.empty:
        lines.append("沒有交集。")
    else:
        breakout_codes = set(breakout_df["ticker"])
        pullback_codes = set(revenue_pullback_df["ticker"])
        overlap_codes = breakout_codes & pullback_codes

        if not overlap_codes:
            lines.append("沒有交集。")
        else:
            overlap = revenue_pullback_df[revenue_pullback_df["ticker"].isin(overlap_codes)].copy()
            overlap = overlap.sort_values("score", ascending=False)

            lines.append(generate_markdown_table(
                overlap,
                columns=[
                    "ticker", "name", "industry", "date",
                    "revenue_yoy_pct", "cumulative_yoy_pct",
                    "close", "volume_lots",
                    "gap_ma20_pct", "gap_ma60_pct",
                    "return_10d_pct", "score", "judge"
                ],
                rename_map={
                    "ticker": "代號",
                    "name": "名稱",
                    "industry": "產業",
                    "date": "資料日",
                    "revenue_yoy_pct": "月營收YoY%",
                    "cumulative_yoy_pct": "累計YoY%",
                    "close": "收盤價",
                    "volume_lots": "成交量張",
                    "gap_ma20_pct": "距月線%",
                    "gap_ma60_pct": "距季線%",
                    "return_10d_pct": "近10日漲幅%",
                    "score": "分數",
                    "judge": "判斷",
                }
            ))

    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main():
    price_data = load_official_price_history()

    if price_data.empty:
        generate_report(
            price_data=price_data,
            breakout_df=pd.DataFrame(),
            revenue_pullback_df=pd.DataFrame()
        )
        print("No official price data. Empty report generated.")
        return

    revenue_df = fetch_monthly_revenue()
    industry_map = build_industry_map(revenue_df)
    stock_map = build_stock_history_map(price_data)

    breakout_df = find_breakout_candidates(stock_map, industry_map)
    revenue_pullback_df = find_revenue_pullback_candidates(stock_map, revenue_df)

    if not breakout_df.empty:
        breakout_df.to_csv(BREAKOUT_CSV_PATH, index=False, encoding="utf-8-sig")

    if not revenue_pullback_df.empty:
        revenue_pullback_df.to_csv(REVENUE_PULLBACK_CSV_PATH, index=False, encoding="utf-8-sig")

    generate_report(price_data, breakout_df, revenue_pullback_df)

    print("Official-data stock monitor report generated.")
    print(f"Trading days loaded: {price_data['date'].nunique()}")
    print(f"Stocks loaded: {price_data['ticker'].nunique()}")
    print(f"Volume threshold: {MIN_VOLUME_LOTS} lots")
    print(f"Breakout candidates: {len(breakout_df)}")
    print(f"Revenue pullback candidates: {len(revenue_pullback_df)}")


if __name__ == "__main__":
    main()
