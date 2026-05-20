import io
import pandas as pd
import requests

from datetime import datetime
from pathlib import Path


DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)
LATEST_DIR = OUTPUT_DIR / "latest"
LATEST_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = LATEST_DIR / "stock_monitor_latest.md"
BREAKOUT_CSV_PATH = LATEST_DIR / "breakout_latest.csv"
RANGE_REBOUND_CSV_PATH = LATEST_DIR / "range_rebound_watch_latest.csv"
REVENUE_PULLBACK_CSV_PATH = LATEST_DIR / "revenue_pullback_latest.csv"
PULLBACK_REBOUND_CSV_PATH = LATEST_DIR / "pullback_rebound_latest.csv"

TDCC_LATEST_PATH = LATEST_DIR / "tdcc_holder_ratio_latest.csv"
TDCC_HISTORY_DIR = OUTPUT_DIR / "history" / "tdcc"

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
    """
    嚴格向上盤整帶量突破 / 區間內轉強判斷。

    修正重點：
    1. 嚴格突破必須突破「前 60 個交易日最高價 high」。
    2. 今日 high 不納入 previous_60d_high，避免自己突破自己。
    3. 可用資料少於 90 日，不允許列入嚴格突破股。
    4. 尚未突破前高但站回 20MA/23EMA、放量、距前高不遠者，
       只分類為 range_rebound / near_resistance，不應放入嚴格突破股。
    """
    df = add_technical_metrics(df)

    if len(df) < 90:
        return None

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    open_price = latest["open"]
    high_today = latest["high"]
    low_today = latest["low"]
    close = latest["close"]
    prev_close = prev["close"]

    ma20 = latest["ma20"]
    ma60 = latest["ma60"]
    volume = latest["volume"]
    vol20 = latest["vol20"]

    volume_lots = volume / 1000

    if volume_lots < MIN_VOLUME_LOTS:
        return None

    if pd.isna(open_price) or pd.isna(high_today) or pd.isna(low_today):
        return None

    if pd.isna(ma20) or pd.isna(ma60) or pd.isna(vol20):
        return None

    previous_60 = df.iloc[-61:-1].copy()

    if previous_60.empty or len(previous_60) < 60:
        return None

    previous_60d_high = previous_60["high"].max()
    previous_60d_low = previous_60["low"].min()

    previous_40 = df.iloc[-41:-1].copy()
    previous_40d_high = previous_40["high"].max() if len(previous_40) >= 40 else previous_60d_high
    previous_40d_low = previous_40["low"].min() if len(previous_40) >= 40 else previous_60d_low

    if previous_60d_low <= 0 or previous_60d_high <= 0:
        return None

    consolidation_range_pct = (previous_40d_high - previous_40d_low) / previous_40d_low * 100
    breakout_pct = (close - previous_60d_high) / previous_60d_high * 100
    distance_to_previous_40d_high_pct = (close / previous_40d_high - 1) * 100
    distance_to_previous_60d_high_pct = (close / previous_60d_high - 1) * 100

    volume_ratio = volume / vol20 if vol20 and vol20 > 0 else 0
    return_5d = (close / df.iloc[-6]["close"] - 1) * 100 if len(df) >= 6 else 0

    gap_ma20 = (close / ma20 - 1) * 100 if ma20 and ma20 > 0 else 0
    gap_ma60 = (close / ma60 - 1) * 100 if ma60 and ma60 > 0 else 0

    ema23 = df["close"].ewm(span=23, adjust=False).mean().iloc[-1]
    gap_ema23 = (close / ema23 - 1) * 100 if ema23 and ema23 > 0 else 0

    close_above_ma20 = close > ma20
    close_above_ema23 = close > ema23
    close_above_ma60 = close > ma60

        true_breakout = (
        close > previous_60d_high
        and volume_ratio >= 1.5
    )

    range_rebound = (
        not true_breakout
        and volume_ratio >= 1.5
        and (close_above_ma20 or close_above_ema23)
        and close < previous_60d_high
        and distance_to_previous_60d_high_pct >= -10
        and close > prev_close
        and close >= open_price
    )

    near_resistance = (
        not true_breakout
        and close < previous_60d_high
        and distance_to_previous_60d_high_pct >= -5
        and volume_ratio >= 1.5
        and (close_above_ma20 or close_above_ema23)
    )

    if true_breakout:
        breakout_type = "true_breakout"
    elif range_rebound:
        breakout_type = "range_rebound"
    elif near_resistance:
        breakout_type = "near_resistance"
    else:
        breakout_type = "false_or_unconfirmed_breakout"

    if breakout_type == "false_or_unconfirmed_breakout":
        return None

    score = 0

    if consolidation_range_pct <= 18:
        score += 25
    elif consolidation_range_pct <= 25:
        score += 15

    if true_breakout:
        if breakout_pct >= 5:
            score += 35
        elif breakout_pct >= 2:
            score += 32
        else:
            score += 30
    else:
        score += 12

    if volume_ratio >= 2:
        score += 25
    elif volume_ratio >= 1.5:
        score += 18
    elif volume_ratio >= 1.2:
        score += 8

    if close_above_ma20:
        score += 10

    if close_above_ema23:
        score += 8

    if close_above_ma60:
        score += 10

    if close > open_price:
        score += 5

    if close > prev_close:
        score += 5

    if true_breakout:
        if return_5d > 20:
            score -= 20
        elif return_5d > 12:
            score -= 10
    else:
        if distance_to_previous_60d_high_pct >= -3:
            score += 8
        elif distance_to_previous_60d_high_pct >= -10:
            score += 5

    if not true_breakout:
        score = min(score, 69)

    return {
        "date": latest["date"],
        "close": round(close, 2),
        "volume_lots": round(volume_lots, 0),
        "ma20": round(ma20, 2),
        "ma60": round(ma60, 2),
        "ema23": round(ema23, 2),
        "gap_ma20_pct": round(gap_ma20, 2),
        "gap_ma60_pct": round(gap_ma60, 2),
        "gap_ema23_pct": round(gap_ema23, 2),

        "high_40": round(previous_40d_high, 2),
        "low_40": round(previous_40d_low, 2),

        "previous_40d_high": round(previous_40d_high, 2),
        "previous_60d_high": round(previous_60d_high, 2),
        "distance_to_previous_40d_high_pct": round(distance_to_previous_40d_high_pct, 2),
        "distance_to_previous_60d_high_pct": round(distance_to_previous_60d_high_pct, 2),

        "consolidation_range_pct": round(consolidation_range_pct, 2),
        "breakout_pct": round(breakout_pct, 2),
        "volume_ratio": round(volume_ratio, 2),
        "return_5d_pct": round(return_5d, 2),
        "breakout_type": breakout_type,
        "score": round(score, 1),
    }


def judge_breakout(row):
    if row["score"] >= 85:
        return "強突破候選"
    if row["score"] >= 70:
        return "可觀察"
    if row["score"] >= 55:
        return "初步觀察"
    return "不列入"


def calculate_revenue_pullback_score(df, revenue_row):
    """
    營收成長但股價回檔。
    維持寬版條件，避免太早漏掉潛在標的。
    """
    df = add_technical_metrics(df)

    if len(df) < 61:
        return None

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    open_price = latest["open"]
    close = latest["close"]
    prev_close = prev["close"]
    ma20 = latest["ma20"]
    ma60 = latest["ma60"]
    volume = latest["volume"]
    vol20 = latest["vol20"]
    volume_lots = volume / 1000
    volume_ratio = volume / vol20 if vol20 and vol20 > 0 else 0

    if volume_lots < MIN_VOLUME_LOTS:
        return None

    if pd.isna(open_price) or pd.isna(ma20) or pd.isna(ma60) or pd.isna(vol20):
        return None

    gap_ma20 = (close / ma20 - 1) * 100 if ma20 and ma20 > 0 else 0
    gap_ma60 = (close / ma60 - 1) * 100 if ma60 and ma60 > 0 else 0

    return_10d = (close / df.iloc[-11]["close"] - 1) * 100 if len(df) >= 11 else 0
    return_20d = (close / df.iloc[-21]["close"] - 1) * 100 if len(df) >= 21 else 0

    close_vs_prev_pct = (close / prev_close - 1) * 100 if prev_close and prev_close > 0 else 0
    intraday_pct = (close / open_price - 1) * 100 if open_price and open_price > 0 else 0

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
        "volume_ratio": round(volume_ratio, 2),
        "ma20": round(ma20, 2),
        "ma60": round(ma60, 2),
        "gap_ma20_pct": round(gap_ma20, 2),
        "gap_ma60_pct": round(gap_ma60, 2),
        "return_10d_pct": round(return_10d, 2),
        "return_20d_pct": round(return_20d, 2),
        "close_vs_prev_pct": round(close_vs_prev_pct, 2),
        "intraday_pct": round(intraday_pct, 2),
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


def judge_rebound(row):
    if row["volume_ratio"] >= 1.8 and row["close_vs_prev_pct"] >= 3:
        return "強轉強"
    if row["volume_ratio"] >= 1.2 and row["close_vs_prev_pct"] > 0:
        return "初步轉強"
    return "觀察"


def find_breakout_candidates(stock_map, industry_map):
    rows = []

    for ticker, df in stock_map.items():
        try:
            metrics = calculate_breakout_score(df)

            if metrics is None:
                continue

            if metrics["score"] >= 55:
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


def find_pullback_rebound_candidates(revenue_pullback_df):
    """
    從營收回檔觀察池中，找短線開始轉強的股票。

    條件：
    1. 已經在營收回檔候選股中
    2. 今日收盤 > 昨日收盤
    3. 今日收盤 >= 今日開盤
    4. 量比 >= 1.2
    5. 接近或站回 20MA
    """
    if revenue_pullback_df.empty:
        return pd.DataFrame()

    df = revenue_pullback_df.copy()

    condition = (
        (df["close_vs_prev_pct"] > 0) &
        (df["intraday_pct"] >= 0) &
        (df["volume_ratio"] >= 1.2) &
        (
            (df["gap_ma20_pct"] >= 0) |
            (df["gap_ma20_pct"].abs() <= 5)
        )
    )

    result = df[condition].copy()

    if result.empty:
        return result

    result["rebound_judge"] = result.apply(judge_rebound, axis=1)

    result = result.sort_values(
        ["volume_ratio", "close_vs_prev_pct", "score"],
        ascending=False
    )

    return result.reset_index(drop=True)



def load_tdcc_latest():
    """
    讀取最新 TDCC 週資料，並與前一期比較。

    目前 TDCC 欄位：
    - date
    - code
    - name
    - over_400_pct
    - over_600_pct
    - over_800_pct
    - over_1000_pct

    目前沒有 100 張以上資料，所以先用：
    over_400_pct = 中大戶以上 proxy
    over_1000_pct = 超大戶 proxy
    """
    tdcc_cols = [
        "ticker",
        "tdcc_date",
        "tdcc_over_400_pct",
        "tdcc_over_400_change",
        "tdcc_over_1000_pct",
        "tdcc_over_1000_change",
        "tdcc_judge",
    ]

    if not TDCC_LATEST_PATH.exists():
        return pd.DataFrame(columns=tdcc_cols)

    try:
        latest_df = pd.read_csv(TDCC_LATEST_PATH, dtype={"code": str})
    except Exception as e:
        print(f"TDCC latest read failed: {e}")
        return pd.DataFrame(columns=tdcc_cols)

    if latest_df.empty:
        return pd.DataFrame(columns=tdcc_cols)

    if "code" not in latest_df.columns:
        if "ticker" in latest_df.columns:
            latest_df["code"] = latest_df["ticker"]
        else:
            return pd.DataFrame(columns=tdcc_cols)

    latest_df = latest_df.copy()
    latest_df["ticker"] = latest_df["code"].astype(str).str.zfill(4)
    latest_df["date"] = latest_df["date"].astype(str)

    for col in ["over_400_pct", "over_1000_pct"]:
        if col in latest_df.columns:
            latest_df[col] = pd.to_numeric(latest_df[col], errors="coerce")

    latest_date = latest_df["date"].max()
    previous_df = pd.DataFrame()

    try:
        history_files = sorted(TDCC_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv"))
        history_frames = []

        for file in history_files:
            temp = pd.read_csv(file, dtype={"code": str})

            if "code" not in temp.columns and "ticker" in temp.columns:
                temp["code"] = temp["ticker"]

            if "date" in temp.columns and "code" in temp.columns:
                history_frames.append(temp)

        if history_frames:
            history_all = pd.concat(history_frames, ignore_index=True)
            history_all["date"] = history_all["date"].astype(str)
            history_all["ticker"] = history_all["code"].astype(str).str.zfill(4)

            previous_dates = sorted([
                d for d in history_all["date"].dropna().unique()
                if str(d) < str(latest_date)
            ])

            if previous_dates:
                previous_date = previous_dates[-1]
                previous_df = history_all[history_all["date"] == previous_date].copy()

                for col in ["over_400_pct", "over_1000_pct"]:
                    if col in previous_df.columns:
                        previous_df[col] = pd.to_numeric(previous_df[col], errors="coerce")

    except Exception as e:
        print(f"TDCC history read failed: {e}")
        previous_df = pd.DataFrame()

    base_cols = ["ticker", "date", "over_400_pct", "over_1000_pct"]
    latest_use = latest_df[[c for c in base_cols if c in latest_df.columns]].copy()

    latest_use = latest_use.rename(columns={
        "date": "tdcc_date",
        "over_400_pct": "tdcc_over_400_pct",
        "over_1000_pct": "tdcc_over_1000_pct",
    })

    if not previous_df.empty:
        prev_use = previous_df[[c for c in base_cols if c in previous_df.columns]].copy()

        prev_use = prev_use.rename(columns={
            "over_400_pct": "prev_over_400_pct",
            "over_1000_pct": "prev_over_1000_pct",
        })

        latest_use = latest_use.merge(
            prev_use[["ticker", "prev_over_400_pct", "prev_over_1000_pct"]],
            on="ticker",
            how="left"
        )

        latest_use["tdcc_over_400_change"] = (
            latest_use["tdcc_over_400_pct"] - latest_use["prev_over_400_pct"]
        )
        latest_use["tdcc_over_1000_change"] = (
            latest_use["tdcc_over_1000_pct"] - latest_use["prev_over_1000_pct"]
        )
    else:
        latest_use["tdcc_over_400_change"] = pd.NA
        latest_use["tdcc_over_1000_change"] = pd.NA

    def judge_tdcc(row):
        c400 = row.get("tdcc_over_400_change", pd.NA)
        c1000 = row.get("tdcc_over_1000_change", pd.NA)

        if pd.isna(c400) or pd.isna(c1000):
            return "僅最新TDCC"

        if c400 > 0 and c1000 > 0:
            return "中大戶/超大戶同步增加"

        if c400 > 0 and c1000 <= 0:
            return "中大戶增加"

        if c400 <= 0 and c1000 > 0:
            return "超大戶增加"

        if c400 < 0 and c1000 < 0:
            return "大戶籌碼減少"

        return "變化不明顯"

    latest_use["tdcc_judge"] = latest_use.apply(judge_tdcc, axis=1)

    for col in [
        "tdcc_over_400_pct",
        "tdcc_over_400_change",
        "tdcc_over_1000_pct",
        "tdcc_over_1000_change",
    ]:
        latest_use[col] = pd.to_numeric(latest_use[col], errors="coerce").round(2)

    return latest_use[tdcc_cols].copy()


def enrich_with_tdcc(df, tdcc_df):
    """
    把 TDCC 最新週資料併入候選股清單。
    """
    tdcc_cols = [
        "tdcc_date",
        "tdcc_over_400_pct",
        "tdcc_over_400_change",
        "tdcc_over_1000_pct",
        "tdcc_over_1000_change",
        "tdcc_judge",
    ]

    if df.empty:
        return df

    result = df.copy()

    if tdcc_df.empty:
        for col in tdcc_cols:
            if col not in result.columns:
                result[col] = ""
        result["tdcc_judge"] = "無TDCC資料"
        return result

    result["ticker"] = result["ticker"].astype(str).str.zfill(4)

    tdcc_df = tdcc_df.copy()
    tdcc_df["ticker"] = tdcc_df["ticker"].astype(str).str.zfill(4)

    result = result.drop(columns=[c for c in tdcc_cols if c in result.columns], errors="ignore")

    result = result.merge(
        tdcc_df,
        on="ticker",
        how="left"
    )

    for col in tdcc_cols:
        if col not in result.columns:
            result[col] = ""

    result["tdcc_judge"] = result["tdcc_judge"].fillna("無TDCC資料")

    return result



def generate_markdown_table(df, columns, rename_map, max_rows=30):
    if df.empty:
        return "沒有符合條件的股票。"

    show_df = df.head(max_rows).copy()
    show_df.insert(0, "rank", range(1, len(show_df) + 1))

    cols = ["rank"] + columns
    table_df = show_df[cols].rename(columns={"rank": "排名", **rename_map})

    return table_df.to_markdown(index=False)


def generate_report(price_data, breakout_df, revenue_pullback_df, pullback_rebound_df):
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
    rebound_mainstream_df, rebound_non_mainstream_df = split_mainstream(pullback_rebound_df)

    breakout_columns = [
        "ticker", "name", "industry", "date", "close", "volume_lots", "ma20", "ma60",
        "gap_ma20_pct", "gap_ma60_pct", "volume_ratio", "consolidation_range_pct",
        "breakout_pct", "return_5d_pct",
        "tdcc_date", "tdcc_over_400_pct", "tdcc_over_400_change",
        "tdcc_over_1000_pct", "tdcc_over_1000_change", "tdcc_judge",
        "score", "judge"
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
        "tdcc_date": "TDCC日",
        "tdcc_over_400_pct": "400張以上%",
        "tdcc_over_400_change": "400張變化",
        "tdcc_over_1000_pct": "1000張以上%",
        "tdcc_over_1000_change": "1000張變化",
        "tdcc_judge": "TDCC判斷",
        "score": "分數",
        "judge": "判斷",
    }

    pullback_columns = [
        "ticker", "name", "industry", "date", "revenue_period",
        "revenue_yoy_pct", "cumulative_yoy_pct",
        "close", "volume_lots", "volume_ratio", "ma20", "ma60",
        "gap_ma20_pct", "gap_ma60_pct",
        "return_10d_pct", "return_20d_pct",
        "close_vs_prev_pct", "intraday_pct",
        "tdcc_date", "tdcc_over_400_pct", "tdcc_over_400_change",
        "tdcc_over_1000_pct", "tdcc_over_1000_change", "tdcc_judge",
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
        "volume_ratio": "量比",
        "ma20": "20MA",
        "ma60": "60MA",
        "gap_ma20_pct": "距月線%",
        "gap_ma60_pct": "距季線%",
        "return_10d_pct": "近10日漲幅%",
        "return_20d_pct": "近20日漲幅%",
        "close_vs_prev_pct": "對前收%",
        "intraday_pct": "日內漲跌%",
        "tdcc_date": "TDCC日",
        "tdcc_over_400_pct": "400張以上%",
        "tdcc_over_400_change": "400張變化",
        "tdcc_over_1000_pct": "1000張以上%",
        "tdcc_over_1000_change": "1000張變化",
        "tdcc_judge": "TDCC判斷",
        "score": "分數",
        "judge": "判斷",
    }

    rebound_columns = [
        "ticker", "name", "industry", "date", "revenue_yoy_pct", "cumulative_yoy_pct",
        "close", "volume_lots", "volume_ratio", "gap_ma20_pct", "gap_ma60_pct",
        "return_10d_pct", "return_20d_pct", "close_vs_prev_pct", "intraday_pct",
        "tdcc_date", "tdcc_over_400_pct", "tdcc_over_400_change",
        "tdcc_over_1000_pct", "tdcc_over_1000_change", "tdcc_judge",
        "score", "rebound_judge"
    ]

    rebound_rename = {
        "ticker": "代號",
        "name": "名稱",
        "industry": "產業",
        "date": "資料日",
        "revenue_yoy_pct": "月營收YoY%",
        "cumulative_yoy_pct": "累計YoY%",
        "close": "收盤價",
        "volume_lots": "成交量張",
        "volume_ratio": "量比",
        "gap_ma20_pct": "距月線%",
        "gap_ma60_pct": "距季線%",
        "return_10d_pct": "近10日漲幅%",
        "return_20d_pct": "近20日漲幅%",
        "close_vs_prev_pct": "對前收%",
        "intraday_pct": "日內漲跌%",
        "tdcc_date": "TDCC日",
        "tdcc_over_400_pct": "400張以上%",
        "tdcc_over_400_change": "400張變化",
        "tdcc_over_1000_pct": "1000張以上%",
        "tdcc_over_1000_change": "1000張變化",
        "tdcc_judge": "TDCC判斷",
        "score": "原始分數",
        "rebound_judge": "轉強判斷",
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
    lines.append("> 盤整帶量突破：嚴格向上突破，必須突破近 40 日高點、量比 >= 1.5、站上 20MA / 60MA、收盤高於前收，且不是放量黑 K。")
    lines.append("")
    lines.append("> 營收回檔股中的短線轉強：從營收回檔觀察池中，找出今日收盤轉強、量能回升、接近或站回 20MA 的股票。")
    lines.append("")
    lines.append("> TDCC：引用 output/latest/tdcc_holder_ratio_latest.csv 的最新週資料；400張以上作為中大戶 proxy，1000張以上作為超大戶 proxy。")
    lines.append("")
    lines.append("> 主流題材版目前保留：半導體、電子零組件、電腦及週邊、通信網路、光電、其他電子、資訊服務、電子通路、電機機械、綠能環保、生技醫療、數位雲端。")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 1. 全市場：嚴格向上盤整帶量突破候選股")
    lines.append("")
    lines.append(generate_markdown_table(breakout_df, breakout_columns, breakout_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 2. 主流題材：嚴格向上盤整帶量突破候選股")
    lines.append("")
    lines.append(generate_markdown_table(breakout_mainstream_df, breakout_columns, breakout_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 3. 非主流 / 防禦傳產：嚴格向上盤整帶量突破候選股")
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

    lines.append("## 7. 全市場：營收回檔股中的短線轉強候選股")
    lines.append("")
    lines.append(generate_markdown_table(pullback_rebound_df, rebound_columns, rebound_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 8. 主流題材：營收回檔股中的短線轉強候選股")
    lines.append("")
    lines.append(generate_markdown_table(rebound_mainstream_df, rebound_columns, rebound_rename))

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 9. 非主流 / 防禦傳產：營收回檔股中的短線轉強候選股")
    lines.append("")
    lines.append(generate_markdown_table(rebound_non_mainstream_df, rebound_columns, rebound_rename))

    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main():
    price_data = load_official_price_history()

    if price_data.empty:
        generate_report(
            price_data=price_data,
            breakout_df=pd.DataFrame(),
            revenue_pullback_df=pd.DataFrame(),
            pullback_rebound_df=pd.DataFrame()
        )
        print("No official price data. Empty report generated.")
        return

    revenue_df = fetch_monthly_revenue()
    industry_map = build_industry_map(revenue_df)
    stock_map = build_stock_history_map(price_data)
    tdcc_df = load_tdcc_latest()

    breakout_all_df = find_breakout_candidates(stock_map, industry_map)
    breakout_all_df = enrich_with_tdcc(breakout_all_df, tdcc_df)

    if not breakout_all_df.empty and "breakout_type" in breakout_all_df.columns:
        range_rebound_df = breakout_all_df[
            breakout_all_df["breakout_type"].isin(["range_rebound", "near_resistance"])
        ].copy()

        breakout_df = breakout_all_df[
            breakout_all_df["breakout_type"] == "true_breakout"
        ].copy()
    else:
        range_rebound_df = pd.DataFrame()
        breakout_df = breakout_all_df.copy()

    revenue_pullback_df = find_revenue_pullback_candidates(stock_map, revenue_df)
    revenue_pullback_df = enrich_with_tdcc(revenue_pullback_df, tdcc_df)

    pullback_rebound_df = find_pullback_rebound_candidates(revenue_pullback_df)
    pullback_rebound_df = enrich_with_tdcc(pullback_rebound_df, tdcc_df)

    breakout_df.to_csv(BREAKOUT_CSV_PATH, index=False, encoding="utf-8-sig")
    range_rebound_df.to_csv(RANGE_REBOUND_CSV_PATH, index=False, encoding="utf-8-sig")
    revenue_pullback_df.to_csv(REVENUE_PULLBACK_CSV_PATH, index=False, encoding="utf-8-sig")
    pullback_rebound_df.to_csv(PULLBACK_REBOUND_CSV_PATH, index=False, encoding="utf-8-sig")

    generate_report(price_data, breakout_df, revenue_pullback_df, pullback_rebound_df)

    print("Official-data stock monitor report generated.")
    print(f"Trading days loaded: {price_data['date'].nunique()}")
    print(f"Stocks loaded: {price_data['ticker'].nunique()}")
    print(f"Volume threshold: {MIN_VOLUME_LOTS} lots")
    print(f"Strict true breakout candidates: {len(breakout_df)}")
    print(f"Range rebound / near resistance watch candidates: {len(range_rebound_df)}")
    print(f"Revenue pullback candidates: {len(revenue_pullback_df)}")
    print(f"Pullback rebound candidates: {len(pullback_rebound_df)}")
    print(f"TDCC rows loaded: {len(tdcc_df)}")


if __name__ == "__main__":
    main()
