import io
import time
import requests
import pandas as pd

from datetime import datetime
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

REPORT_PATH = OUTPUT_DIR / "stock_monitor_latest.md"
CSV_PATH = OUTPUT_DIR / "breakout_latest.csv"


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

    return df[["ticker", "name"]].dropna().reset_index(drop=True)


def fetch_yahoo_price(ticker):
    """
    用 Yahoo Finance 抓台股日線。
    上市：xxxx.TW
    """
    symbol = f"{ticker}.TW"
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


def calculate_breakout_score(df):
    """
    盤整帶量突破 v1 分數。
    """
    latest = df.iloc[-1].copy()

    df = df.copy()
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["vol20"] = df["volume"].rolling(20).mean()

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

    # 盤整區越窄越好
    if consolidation_range_pct <= 18:
        score += 25
    elif consolidation_range_pct <= 25:
        score += 15

    # 接近或突破40日高點
    if breakout_pct >= 0:
        score += 30
    elif breakout_pct >= -2:
        score += 20
    elif breakout_pct >= -5:
        score += 10

    # 量放大
    if volume_ratio >= 2:
        score += 25
    elif volume_ratio >= 1.5:
        score += 18
    elif volume_ratio >= 1.2:
        score += 10

    # 均線位置
    if close > ma20:
        score += 10
    if close > ma60:
        score += 10

    # 避免短線已經噴太遠
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


def find_breakout_candidates(limit=300):
    """
    先掃上市股票前 limit 檔，避免第一次執行太久。
    成功後再放大到全部上市櫃。
    """
    symbols = fetch_twse_listed_symbols()
    symbols = symbols.head(limit)

    rows = []

    for i, item in symbols.iterrows():
        ticker = item["ticker"]
        name = item["name"]

        try:
            price_df = fetch_yahoo_price(ticker)
            if price_df is None:
                continue

            metrics = calculate_breakout_score(price_df)

            if metrics["score"] >= 50:
                rows.append({
                    "ticker": ticker,
                    "name": name,
                    **metrics,
                })

            time.sleep(0.15)

        except Exception as e:
            print(f"Skip {ticker} {name}: {e}")
            continue

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_breakout, axis=1)
    result = result.sort_values(["score", "volume_ratio"], ascending=False)

    return result.reset_index(drop=True)


def generate_report(breakout_df):
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

    if breakout_df.empty:
        lines.append("今日沒有符合條件的盤整帶量突破候選股。")
    else:
        show_df = breakout_df.head(30).copy()
        show_df.insert(0, "rank", range(1, len(show_df) + 1))

        columns = [
            "rank", "ticker", "name", "close", "ma20", "ma60",
            "gap_ma20_pct", "gap_ma60_pct",
            "volume_ratio", "consolidation_range_pct",
            "breakout_pct", "return_5d_pct", "score", "judge"
        ]

        table_df = show_df[columns].rename(columns={
            "rank": "排名",
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
        })

        lines.append(table_df.to_markdown(index=False))

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. 營收成長但股價回檔候選股")
    lines.append("")
    lines.append("尚未啟用。下一階段新增。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. 兩策略交集股")
    lines.append("")
    lines.append("尚未啟用。下一階段新增。")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main():
    breakout_df = find_breakout_candidates(limit=300)

    if not breakout_df.empty:
        breakout_df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")

    generate_report(breakout_df)

    print("Daily stock monitor report generated.")
    print(f"Breakout candidates: {len(breakout_df)}")


if __name__ == "__main__":
    main()
