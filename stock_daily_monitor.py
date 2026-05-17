import io
import time
import requests
import pandas as pd

from datetime import datetime
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

REPORT_PATH = OUTPUT_DIR / "stock_monitor_latest.md"
BREAKOUT_CSV_PATH = OUTPUT_DIR / "breakout_latest.csv"
REVENUE_PULLBACK_CSV_PATH = OUTPUT_DIR / "revenue_pullback_latest.csv"


def fetch_twse_listed_symbols():
    """
    抓上市股票基本資料。
    """
    url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers, timeout=20)
    r.encoding = "big5"

    tables = pd.read_html(io.StringIO(r.text))
    df = tables[0]

    df.columns = df.iloc[0]
    df = df.iloc[1:].copy()

    df = df[df["有價證券代號及名稱"].astype(str).str.match(r"^\d{4}")]
    df[["ticker", "name"]] = df["有價證券代號及名稱"].str.extract(r"^(\d{4})\s+(.+)$")
    df["market"] = "listed"

    return df[["ticker", "name", "market"]].dropna().reset_index(drop=True)


def fetch_yahoo_price(ticker, market="listed"):
    """
    Yahoo Finance:
    上市股票：xxxx.TW
    上櫃股票：xxxx.TWO

    目前 v1 先掃上市股票，所以 market 預設 listed。
    """
    suffix = "TW" if market == "listed" else "TWO"
    symbol = f"{ticker}.{suffix}"

    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=6mo&interval=1d"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers, timeout=15)
    data = r.json()

    result = data.get("chart", {}).get("result")
    if not result:
        return None

    result = result[0]
    timestamps = result.get("timestamp", [])
    quote = result.get("indicators", {}).get("quote", [{}])[0]

    if not timestamps or not quote:
        return None

    df = pd.DataFrame({
        "date": pd.to_datetime(timestamps, unit="s").tz_localize("UTC").tz_convert("Asia/Taipei").date,
        "open": quote.get("open"),
        "high": quote.get("high"),
        "low": quote.get("low"),
        "close": quote.get("close"),
        "volume": quote.get("volume"),
    })

    df = df.dropna(subset=["close", "volume"]).copy()

    if len(df) < 60:
        return None

    return df


def add_technical_metrics(df):
    df = df.copy()
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["vol20"] = df["volume"].rolling(20).mean()
    return df


def calculate_breakout_score(df):
    """
    盤整帶量突破 v1 分數。
    """
    df = add_technical_metrics(df)
    latest = df.iloc[-1]

    close = latest["close"]
    ma20 = latest["ma20"]
    ma60 = latest["ma60"]
    volume = latest["volume"]
    vol20 = latest["vol20"]

    recent_40 = df.iloc[-41:-1]
    high_40 = recent_40["high"].max()
    low_40 = recent_40["low"].min()

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
        "close": round(close, 2),
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


def fetch_monthly_revenue():
    """
    抓上市 + 上櫃最新月營收資料。

    L = listed 上市
    O = OTC 上櫃
    """
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


def calculate_revenue_pullback_score(price_df, revenue_row):
    """
    營收成長但股價回檔 v1。
    """
    df = add_technical_metrics(price_df)
    latest = df.iloc[-1]

    close = latest["close"]
    ma20 = latest["ma20"]
    ma60 = latest["ma60"]

    gap_ma20 = (close / ma20 - 1) * 100 if ma20 and ma20 > 0 else 0
    gap_ma60 = (close / ma60 - 1) * 100 if ma60 and ma60 > 0 else 0

    return_10d = (close / df.iloc[-11]["close"] - 1) * 100 if len(df) >= 11 else 0
    return_20d = (close / df.iloc[-21]["close"] - 1) * 100 if len(df) >= 21 else 0

    revenue_yoy = revenue_row["revenue_yoy_pct"]
    cumulative_yoy = revenue_row["cumulative_yoy_pct"]

    score = 0

    # 營收成長
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

    # 回檔幅度
    if return_10d <= -8:
        score += 20
    elif return_10d <= -5:
        score += 14
    elif return_20d <= -8:
        score += 12

    # 接近均線
    if abs(gap_ma20) <= 5:
        score += 15
    elif abs(gap_ma60) <= 7:
        score += 15
    elif abs(gap_ma20) <= 8:
        score += 8

    # 沒有跌破季線太深
    if gap_ma60 < -10:
        score -= 20

    # 短線還在月線上方太遠，不算回檔低接
    if gap_ma20 > 12:
        score -= 15

    return {
        "revenue_period": revenue_row.get("revenue_period", ""),
        "industry": revenue_row.get("industry", ""),
        "revenue_yoy_pct": round(revenue_yoy, 2),
        "cumulative_yoy_pct": round(cumulative_yoy, 2),
        "close": round(close, 2),
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


def find_breakout_candidates(symbols):
    rows = []

    for _, item in symbols.iterrows():
        ticker = item["ticker"]
        name = item["name"]
        market = item.get("market", "listed")

        try:
            price_df = fetch_yahoo_price(ticker, market=market)
            if price_df is None:
                continue

            metrics = calculate_breakout_score(price_df)

            if metrics["score"] >= 50:
                rows.append({
                    "ticker": ticker,
                    "name": name,
                    "market": market,
                    **metrics,
                })

            time.sleep(0.15)

        except Exception as e:
            print(f"Breakout skip {ticker} {name}: {e}")
            continue

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_breakout, axis=1)
    result = result.sort_values(["score", "volume_ratio"], ascending=False)

    return result.reset_index(drop=True)


def find_revenue_pullback_candidates(revenue_df, limit=300):
    """
    v1 先從營收符合條件者裡面掃前 limit 檔，避免第一次執行過久。
    """
    if revenue_df.empty:
        return pd.DataFrame()

    base = revenue_df[
        (revenue_df["revenue_yoy_pct"] >= 20) &
        (revenue_df["cumulative_yoy_pct"] >= 10)
    ].copy()

    base = base.head(limit)

    rows = []

    for _, item in base.iterrows():
        ticker = item["ticker"]
        name = item["name"]
        market = item.get("market", "listed")

        try:
            price_df = fetch_yahoo_price(ticker, market=market)
            if price_df is None:
                continue

            metrics = calculate_revenue_pullback_score(price_df, item)

            # 先用寬鬆門檻，之後再調嚴
            if metrics["score"] >= 50:
                rows.append({
                    "ticker": ticker,
                    "name": name,
                    "market": market,
                    **metrics,
                })

            time.sleep(0.15)

        except Exception as e:
            print(f"Revenue pullback skip {ticker} {name}: {e}")
            continue

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_revenue_pullback, axis=1)
    result = result.sort_values(["score", "revenue_yoy_pct"], ascending=False)

    return result.reset_index(drop=True)


def generate_markdown_table(df, columns, rename_map, max_rows=30):
    if df.empty:
        return "沒有符合條件的股票。"

    show_df = df.head(max_rows).copy()
    show_df.insert(0, "rank", range(1, len(show_df) + 1))

    cols = ["rank"] + columns
    table_df = show_df[cols].rename(columns={"rank": "排名", **rename_map})

    return table_df.to_markdown(index=False)


def generate_report(breakout_df, revenue_pullback_df):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append("# 台股每日監測報告")
    lines.append("")
    lines.append(f"產生時間：{now}")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 1. 盤整帶量突破候選股")
    lines.append("")
    lines.append(generate_markdown_table(
        breakout_df,
        columns=[
            "ticker", "name", "close", "ma20", "ma60",
            "gap_ma20_pct", "gap_ma60_pct",
            "volume_ratio", "consolidation_range_pct",
            "breakout_pct", "return_5d_pct", "score", "judge"
        ],
        rename_map={
            "ticker": "代號",
            "name": "名稱",
            "close": "收盤價",
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
    ))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 2. 營收成長但股價回檔候選股")
    lines.append("")
    lines.append(generate_markdown_table(
        revenue_pullback_df,
        columns=[
            "ticker", "name", "industry", "revenue_period",
            "revenue_yoy_pct", "cumulative_yoy_pct",
            "close", "ma20", "ma60",
            "gap_ma20_pct", "gap_ma60_pct",
            "return_10d_pct", "return_20d_pct",
            "score", "judge"
        ],
        rename_map={
            "ticker": "代號",
            "name": "名稱",
            "industry": "產業",
            "revenue_period": "營收年月",
            "revenue_yoy_pct": "月營收YoY%",
            "cumulative_yoy_pct": "累計YoY%",
            "close": "收盤價",
            "ma20": "20MA",
            "ma60": "60MA",
            "gap_ma20_pct": "距月線%",
            "gap_ma60_pct": "距季線%",
            "return_10d_pct": "近10日漲幅%",
            "return_20d_pct": "近20日漲幅%",
            "score": "分數",
            "judge": "判斷",
        }
    ))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 3. 兩策略交集股")
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
                    "ticker", "name", "industry",
                    "revenue_yoy_pct", "cumulative_yoy_pct",
                    "gap_ma20_pct", "gap_ma60_pct",
                    "return_10d_pct", "score", "judge"
                ],
                rename_map={
                    "ticker": "代號",
                    "name": "名稱",
                    "industry": "產業",
                    "revenue_yoy_pct": "月營收YoY%",
                    "cumulative_yoy_pct": "累計YoY%",
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
    # v1 先掃上市前 300 檔做突破監測，避免 GitHub Actions 跑太久
    symbols = fetch_twse_listed_symbols().head(300)

    revenue_df = fetch_monthly_revenue()

    breakout_df = find_breakout_candidates(symbols)
    revenue_pullback_df = find_revenue_pullback_candidates(revenue_df, limit=300)

    if not breakout_df.empty:
        breakout_df.to_csv(BREAKOUT_CSV_PATH, index=False, encoding="utf-8-sig")

    if not revenue_pullback_df.empty:
        revenue_pullback_df.to_csv(REVENUE_PULLBACK_CSV_PATH, index=False, encoding="utf-8-sig")

    generate_report(breakout_df, revenue_pullback_df)

    print("Daily stock monitor report generated.")
    print(f"Breakout candidates: {len(breakout_df)}")
    print(f"Revenue pullback candidates: {len(revenue_pullback_df)}")


if __name__ == "__main__":
    main()
