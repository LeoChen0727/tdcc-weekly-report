from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import math
import re
import warnings

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image, ImageDraw, ImageFont


REPO_RAW_BASE = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"

DATA_PRICE_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")
LATEST_DIR = OUTPUT_DIR / "latest"

CHART_ROOT_DIR = LATEST_DIR / "charts"
CONTACT_SHEET_DIR = LATEST_DIR / "contact_sheets"

CHART_MANIFEST_PATH = LATEST_DIR / "chart_manifest.csv"
CONTACT_SHEET_MANIFEST_PATH = LATEST_DIR / "contact_sheet_manifest.csv"

LOOKBACK_DAYS = 180
PRICE_DATA_PATH = DATA_PRICE_DIR.as_posix()
CONTACT_SHEET_LIMIT = 20

MAX_CHARTS_PER_CATEGORY = {
    "true_breakout": 30,
    "range_rebound": 30,
    "revenue_breakout_low_response": 30,
    "revenue_pullback": 30,
    "pullback_rebound": 30,
    "pattern": 30,
}

CATEGORY_CONFIG = [
    {
        "category": "true_breakout",
        "csv_path": LATEST_DIR / "breakout_latest.csv",
        "note": "嚴格突破",
    },
    {
        "category": "range_rebound",
        "csv_path": LATEST_DIR / "range_rebound_watch_latest.csv",
        "note": "區間內轉強 / 挑戰前高觀察",
    },
    {
        "category": "revenue_breakout_low_response",
        "csv_path": LATEST_DIR / "revenue_breakout_low_response_latest.csv",
        "note": "營收爆發但股價尚未反應",
    },
    {
        "category": "revenue_pullback",
        "csv_path": LATEST_DIR / "revenue_pullback_latest.csv",
        "note": "營收成長股價回檔",
    },
    {
        "category": "pullback_rebound",
        "csv_path": LATEST_DIR / "pullback_rebound_latest.csv",
        "note": "回檔後短線轉強",
    },
    {
        "category": "pattern",
        "csv_path": LATEST_DIR / "daily_pattern_watch_latest.csv",
        "note": "型態觀察",
    },
]

warnings.filterwarnings("ignore", message="Glyph .* missing from font.*")


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_code(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    text = re.sub(r"[^0-9]", "", text)

    if not text:
        return ""

    return text.zfill(4)


def normalize_name(value) -> str:
    if pd.isna(value):
        return ""

    return str(value).strip().replace("/", "-").replace("\\", "-").replace(" ", "")


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default

        text = str(value).strip().replace(",", "").replace("%", "")

        if text == "":
            return default

        return float(text)
    except Exception:
        return default


def fmt_price(value) -> str:
    if pd.isna(value):
        return "-"

    try:
        return f"{float(value):.2f}"
    except Exception:
        return "-"


def fmt_pct(value) -> str:
    if pd.isna(value):
        return "-"

    try:
        return f"{float(value):.2f}%"
    except Exception:
        return "-"


def safe_filename(text: str) -> str:
    text = str(text).strip()
    text = text.replace("/", "-").replace("\\", "-").replace(":", "-")
    text = re.sub(r"[^\w\u4e00-\u9fff\-_]+", "_", text)
    return text[:80]


def pick_column(df: pd.DataFrame, candidates: list[str], default=""):
    for col in candidates:
        if col in df.columns:
            return df[col]

    return default


def read_csv_safe(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"Missing candidate file: {path}")
        return pd.DataFrame()

    try:
        return pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str})
    except Exception as exc:
        print(f"Failed to read {path}: {exc}")
        return pd.DataFrame()


def standardize_candidate_columns(df: pd.DataFrame, category: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    result = pd.DataFrame()
    result["_source_order"] = range(len(df))

    result["category"] = category

    if "breakout_type" in df.columns:
        result["breakout_type"] = df["breakout_type"].astype(str)
    else:
        if category == "true_breakout":
            result["breakout_type"] = "true_breakout"
        elif category == "range_rebound":
            result["breakout_type"] = "range_rebound"
        elif category == "revenue_breakout_low_response":
            result["breakout_type"] = "revenue_breakout_low_response"
        elif category == "revenue_pullback":
            result["breakout_type"] = "revenue_pullback"
        elif category == "pullback_rebound":
            result["breakout_type"] = "pullback_rebound"
        elif category == "pattern":
            result["breakout_type"] = "pattern"
        else:
            result["breakout_type"] = category

    result["stock_id"] = pick_column(df, ["stock_id", "ticker", "code", "股票代號"], "").map(normalize_code)
    result["stock_name"] = pick_column(df, ["stock_name", "name", "company_name", "股票名稱"], "").map(normalize_name)

    result["date"] = pick_column(df, ["date", "資料日期"], "")
    result["industry"] = pick_column(df, ["industry", "產業別"], "")
    result["score"] = pick_column(df, ["score", "分數"], pd.NA)
    result["rank"] = pick_column(df, ["rank", "排行"], pd.NA)

    result["close"] = pick_column(df, ["close", "收盤價"], pd.NA)
    result["volume"] = pick_column(df, ["volume", "volume_lots", "成交量"], pd.NA)
    result["volume_ratio"] = pick_column(df, ["volume_ratio", "volume_ratio_20", "量比"], pd.NA)

    result["latest_revenue_yoy"] = pick_column(df, ["latest_revenue_yoy", "revenue_yoy_pct"], pd.NA)
    result["cumulative_revenue_yoy"] = pick_column(df, ["cumulative_revenue_yoy", "cumulative_yoy_pct"], pd.NA)
    result["return_5d"] = pick_column(df, ["return_5d", "return_5d_pct"], pd.NA)
    result["distance_to_ma20_pct"] = pick_column(df, ["distance_to_ma20_pct", "gap_ma20_pct"], pd.NA)
    result["distance_to_ma60_pct"] = pick_column(df, ["distance_to_ma60_pct", "gap_ma60_pct"], pd.NA)

    result["note"] = pick_column(df, ["note", "備註", "revenue_acceleration_note"], "")

    result = result[result["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()

    return result


def load_all_candidates() -> pd.DataFrame:
    frames = []

    for config in CATEGORY_CONFIG:
        category = config["category"]
        csv_path = config["csv_path"]

        df = read_csv_safe(csv_path)

        if df.empty:
            continue

        standardized = standardize_candidate_columns(df, category)

        if standardized.empty:
            continue

        if category == "true_breakout":
            standardized = standardized[standardized["breakout_type"] == "true_breakout"].copy()

        if category == "range_rebound":
            standardized = standardized[
                standardized["breakout_type"].isin(
                    ["range_rebound", "near_resistance", "abnormal_volume_up"]
                )
            ].copy()

        frames.append(standardized)

    if not frames:
        return pd.DataFrame()

    candidates = pd.concat(frames, ignore_index=True)

    return candidates


def limit_candidates_for_charts(candidates: pd.DataFrame) -> pd.DataFrame:
    """
    限制每日實際產圖數量。

    all_candidates_latest.csv / xlsx 保留完整名單；
    chart_manifest.csv / charts / contact_sheets 只保留每類前 N 檔，
    避免 GitHub Actions 因為畫太多圖而跑太久。
    """
    if candidates.empty:
        return candidates

    df = candidates.copy()
    df["_source_order"] = range(len(df))

    if "score" not in df.columns:
        df["score"] = pd.NA

    if "rank" not in df.columns:
        df["rank"] = pd.NA

    df["_score_sort"] = pd.to_numeric(df["score"], errors="coerce")
    df["_rank_sort"] = pd.to_numeric(df["rank"], errors="coerce")

    limited_frames = []

    for category, part in df.groupby("category", sort=False):
        limit = MAX_CHARTS_PER_CATEGORY.get(category, 30)

        part = part.sort_values(
            ["_score_sort", "_rank_sort", "_source_order"],
            ascending=[False, True, True],
            na_position="last",
        ).head(limit)

        limited_frames.append(part)

    if not limited_frames:
        return pd.DataFrame()

    result = pd.concat(limited_frames, ignore_index=True)
    result = result.drop(columns=["_source_order", "_score_sort", "_rank_sort"], errors="ignore")

    print("Chart generation limited by category:")

    if not result.empty:
        print(result.groupby("category").size())

    return result


def load_price_history() -> pd.DataFrame:
    frames = []

    for path in sorted(DATA_PRICE_DIR.glob("*.csv")):
        try:
            df = pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str, "date": str})
        except Exception as exc:
            print(f"Skip price file {path}: {exc}")
            continue

        if df.empty:
            continue

        if "stock_id" not in df.columns:
            if "ticker" in df.columns:
                df = df.rename(columns={"ticker": "stock_id"})
            elif "code" in df.columns:
                df = df.rename(columns={"code": "stock_id"})

        if "stock_id" not in df.columns:
            continue

        if "date" not in df.columns:
            match = re.search(r"([0-9]{8})", path.name)

            if match:
                df["date"] = match.group(1)

        if "name" not in df.columns:
            df["name"] = ""

        required = {"date", "stock_id", "open", "high", "low", "close", "volume"}

        if not required.issubset(set(df.columns)):
            continue

        df = df.copy()
        df["date"] = df["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
        df["stock_id"] = df["stock_id"].map(normalize_code)
        df["name"] = df["name"].map(normalize_name)

        for col in ["open", "high", "low", "close", "volume"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna(subset=["date", "stock_id", "open", "high", "low", "close", "volume"])
        df = df[df["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

        frames.append(df[["date", "stock_id", "name", "open", "high", "low", "close", "volume"]])

    if not frames:
        return pd.DataFrame()

    price_df = pd.concat(frames, ignore_index=True)
    price_df = price_df.drop_duplicates(subset=["date", "stock_id"], keep="last")
    price_df = price_df.sort_values(["stock_id", "date"]).reset_index(drop=True)

    return price_df


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["ema23"] = df["close"].ewm(span=23, adjust=False).mean()

    return df


def calc_reference_levels(df: pd.DataFrame) -> dict:
    latest = df.iloc[-1]
    close = float(latest["close"])

    previous_40 = df.iloc[-41:-1].copy()
    previous_60 = df.iloc[-61:-1].copy()

    previous_40d_high = previous_40["high"].max() if len(previous_40) >= 20 else pd.NA
    previous_40d_low = previous_40["low"].min() if len(previous_40) >= 20 else pd.NA
    previous_60d_high = previous_60["high"].max() if len(previous_60) >= 20 else pd.NA
    previous_60d_low = previous_60["low"].min() if len(previous_60) >= 20 else pd.NA

    distance_40 = (close / previous_40d_high - 1) * 100 if not pd.isna(previous_40d_high) and previous_40d_high > 0 else pd.NA
    distance_60 = (close / previous_60d_high - 1) * 100 if not pd.isna(previous_60d_high) and previous_60d_high > 0 else pd.NA

    return {
        "previous_40d_high": previous_40d_high,
        "previous_40d_low": previous_40d_low,
        "previous_60d_high": previous_60d_high,
        "previous_60d_low": previous_60d_low,
        "distance_to_previous_40d_high_pct": distance_40,
        "distance_to_previous_60d_high_pct": distance_60,
        "is_true_breakout_60": close > previous_60d_high if not pd.isna(previous_60d_high) else False,
    }


def check_price_data_warning(df: pd.DataFrame) -> str:
    warning_flags = []
    available_days = len(df)

    if available_days < 120:
        warning_flags.append("available_days_too_few")

    ohlc_cols = ["open", "high", "low", "close"]
    flat_ohlc_count = 0

    for i in range(1, len(df)):
        prev_row = df.iloc[i - 1]
        curr_row = df.iloc[i]

        same_ohlc = True

        for col in ohlc_cols:
            prev_value = safe_float(prev_row[col])
            curr_value = safe_float(curr_row[col])

            if pd.isna(prev_value) or pd.isna(curr_value):
                same_ohlc = False
                break

            if abs(prev_value - curr_value) > 0.001:
                same_ohlc = False
                break

        if same_ohlc:
            flat_ohlc_count += 1

    if flat_ohlc_count >= 5:
        warning_flags.append("suspected_flat_price")

    temp = df.copy()
    temp["prev_close"] = temp["close"].shift(1)
    temp["gap_pct"] = (temp["close"] / temp["prev_close"] - 1) * 100
    max_abs_gap = temp["gap_pct"].abs().max()

    if not pd.isna(max_abs_gap) and max_abs_gap >= 25:
        warning_flags.append("large_price_gap_warning")

    unique_dates = df["date"].dropna().astype(str).nunique()

    if unique_dates < available_days * 0.95:
        warning_flags.append("duplicate_or_missing_date_warning")

    return "ok" if not warning_flags else ";".join(sorted(set(warning_flags)))


def draw_candles(ax, df: pd.DataFrame) -> None:
    width = 0.6

    for idx, row in df.iterrows():
        open_price = float(row["open"])
        high_price = float(row["high"])
        low_price = float(row["low"])
        close_price = float(row["close"])

        color = "#d62728" if close_price >= open_price else "#2ca02c"

        ax.vlines(idx, low_price, high_price, color=color, linewidth=0.8)

        body_low = min(open_price, close_price)
        body_height = abs(close_price - open_price)

        if body_height == 0:
            body_height = 0.01

        rect = Rectangle(
            (idx - width / 2, body_low),
            width,
            body_height,
            facecolor=color,
            edgecolor=color,
            linewidth=0.5,
            alpha=0.75,
        )
        ax.add_patch(rect)


def make_note(category: str, breakout_type: str, ref: dict) -> str:
    previous_60d_high = ref.get("previous_60d_high", pd.NA)
    distance_60 = ref.get("distance_to_previous_60d_high_pct", pd.NA)

    if category == "true_breakout":
        return f"真正突破前60日高點 {fmt_price(previous_60d_high)}，突破幅度 {fmt_pct(distance_60)}"

    if category == "range_rebound":
        if breakout_type == "abnormal_volume_up":
            return f"異常大量上漲但尚未突破前高；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

        return f"尚未突破前高 / 挑戰前高觀察；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "revenue_breakout_low_response":
        return f"營收爆發低反應；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "revenue_pullback":
        return f"營收成長但股價回檔；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "pullback_rebound":
        return f"回檔後短線轉強；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "pattern":
        return f"型態觀察；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    return ""


def create_chart(
    price_df: pd.DataFrame,
    candidate: pd.Series,
    category: str,
    chart_path: Path,
) -> dict:
    stock_id = normalize_code(candidate.get("stock_id", ""))
    stock_name = normalize_name(candidate.get("stock_name", ""))

    df = price_df[price_df["stock_id"] == stock_id].copy()
    df = df.sort_values("date").tail(LOOKBACK_DAYS).reset_index(drop=True)

    available_days = len(df)

    if df.empty or available_days < 20:
        raise ValueError(f"{stock_id} {stock_name} available price days too few: {available_days}")

    if not stock_name:
        names = df["name"].dropna().astype(str)

        if not names.empty:
            stock_name = normalize_name(names.iloc[-1])

    df = add_indicators(df)
    ref = calc_reference_levels(df)

    latest = df.iloc[-1]
    chart_date = str(latest["date"])

    price_data_warning = check_price_data_warning(df)

    previous_40d_high = ref.get("previous_40d_high", pd.NA)
    previous_60d_high = ref.get("previous_60d_high", pd.NA)
    previous_60d_low = ref.get("previous_60d_low", pd.NA)

    distance_40 = ref.get("distance_to_previous_40d_high_pct", pd.NA)
    distance_60 = ref.get("distance_to_previous_60d_high_pct", pd.NA)

    breakout_type = str(candidate.get("breakout_type", category))
    note = make_note(category, breakout_type, ref)

    candidate_note = str(candidate.get("note", "")).strip()

    if candidate_note and candidate_note != "nan":
        note = f"{note} | {candidate_note}" if note else candidate_note

    if price_data_warning != "ok":
        note = f"{note} | price_data_warning: {price_data_warning}" if note else f"price_data_warning: {price_data_warning}"

    fig = plt.figure(figsize=(14, 8))
    grid = fig.add_gridspec(5, 1, hspace=0.08)

    ax_price = fig.add_subplot(grid[:4, 0])
    ax_volume = fig.add_subplot(grid[4, 0], sharex=ax_price)

    draw_candles(ax_price, df)

    x = range(len(df))

    ax_price.plot(x, df["ema23"], linewidth=1.2, label="23EMA")
    ax_price.plot(x, df["ma20"], linewidth=1.0, label="20MA")
    ax_price.plot(x, df["ma60"], linewidth=1.0, label="60MA")

    if not pd.isna(previous_40d_high):
        ax_price.axhline(float(previous_40d_high), linestyle="--", linewidth=1.0, label=f"Prev40 High {fmt_price(previous_40d_high)}")

    if not pd.isna(previous_60d_high):
        ax_price.axhline(float(previous_60d_high), linestyle=":", linewidth=1.2, label=f"Prev60 High {fmt_price(previous_60d_high)}")

    if not pd.isna(previous_60d_low):
        ax_price.axhline(float(previous_60d_low), linestyle=":", linewidth=0.8, label=f"Prev60 Low {fmt_price(previous_60d_low)}")

    latest_x = len(df) - 1
    latest_close = float(latest["close"])

    ax_price.scatter([latest_x], [latest_close], s=50, zorder=5)
    ax_price.annotate(
        f"Close {fmt_price(latest_close)}",
        xy=(latest_x, latest_close),
        xytext=(-80, 20),
        textcoords="offset points",
        arrowprops=dict(arrowstyle="->", linewidth=0.8),
        fontsize=9,
    )

    title = (
        f"{stock_id} {stock_name} | {category} | {chart_date}\n"
        f"{breakout_type} | Days: {available_days} | Data: {price_data_warning} | "
        f"Dist60: {fmt_pct(distance_60)} | Dist40: {fmt_pct(distance_40)}"
    )

    ax_price.set_title(title, fontsize=12)
    ax_price.legend(loc="upper left", fontsize=8)
    ax_price.grid(True, alpha=0.25)

    volume_colors = ["#d62728" if close >= open_ else "#2ca02c" for open_, close in zip(df["open"], df["close"])]
    ax_volume.bar(x, df["volume"], color=volume_colors, alpha=0.65)
    ax_volume.plot(x, df["volume"].rolling(20).mean(), linewidth=1.0, label="Volume MA20")
    ax_volume.legend(loc="upper left", fontsize=8)
    ax_volume.grid(True, alpha=0.2)

    tick_count = min(10, len(df))

    if tick_count > 0:
        tick_positions = [int(i * (len(df) - 1) / max(tick_count - 1, 1)) for i in range(tick_count)]
        tick_labels = [str(df.iloc[i]["date"])[4:] for i in tick_positions]
        ax_volume.set_xticks(tick_positions)
        ax_volume.set_xticklabels(tick_labels, rotation=45, ha="right", fontsize=8)

    plt.setp(ax_price.get_xticklabels(), visible=False)

    chart_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chart_path, dpi=120, bbox_inches="tight")
    plt.close(fig)

    return {
        "date": chart_date,
        "stock_id": stock_id,
        "stock_name": stock_name,
        "category": category,
        "available_days": available_days,
        "price_data_warning": price_data_warning,
        "chart_path": chart_path.as_posix(),
        "chart_url": f"{REPO_RAW_BASE}/{chart_path.as_posix()}",
        "price_data_path": PRICE_DATA_PATH,
        "chart_days": LOOKBACK_DAYS,
        "close": round(float(latest["close"]), 2),
        "previous_40d_high": round(float(previous_40d_high), 2) if not pd.isna(previous_40d_high) else pd.NA,
        "previous_60d_high": round(float(previous_60d_high), 2) if not pd.isna(previous_60d_high) else pd.NA,
        "distance_to_previous_40d_high_pct": round(float(distance_40), 2) if not pd.isna(distance_40) else pd.NA,
        "distance_to_previous_60d_high_pct": round(float(distance_60), 2) if not pd.isna(distance_60) else pd.NA,
        "breakout_type": breakout_type,
        "score": candidate.get("score", pd.NA),
        "rank": candidate.get("rank", pd.NA),
        "note": note,
    }


def clean_old_outputs() -> None:
    CHART_ROOT_DIR.mkdir(parents=True, exist_ok=True)
    CONTACT_SHEET_DIR.mkdir(parents=True, exist_ok=True)

    for category_dir in CHART_ROOT_DIR.iterdir() if CHART_ROOT_DIR.exists() else []:
        if category_dir.is_dir():
            for file in category_dir.glob("*.png"):
                file.unlink()

    for file in CONTACT_SHEET_DIR.glob("*.png"):
        file.unlink()


def make_contact_sheet(category: str, chart_paths: list[Path]) -> dict | None:
    if not chart_paths:
        return None

    selected_paths = chart_paths[:CONTACT_SHEET_LIMIT]

    images = []

    for path in selected_paths:
        try:
            img = Image.open(path).convert("RGB")
            img.thumbnail((700, 420))
            images.append((path, img.copy()))
        except Exception as exc:
            print(f"Skip contact sheet image {path}: {exc}")

    if not images:
        return None

    cols = 2
    rows = math.ceil(len(images) / cols)

    cell_w = 760
    cell_h = 500

    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 24)
    except Exception:
        font = ImageFont.load_default()

    for idx, (path, img) in enumerate(images):
        row = idx // cols
        col = idx % cols

        x0 = col * cell_w
        y0 = row * cell_h

        title = path.name
        draw.text((x0 + 20, y0 + 15), title, fill="black", font=font)

        img_x = x0 + 20
        img_y = y0 + 60

        sheet.paste(img, (img_x, img_y))

    contact_path = CONTACT_SHEET_DIR / f"{category}_contact_sheet.png"
    sheet.save(contact_path)

    return {
        "category": category,
        "contact_sheet_path": contact_path.as_posix(),
        "contact_sheet_url": f"{REPO_RAW_BASE}/{contact_path.as_posix()}",
        "chart_count": len(chart_paths),
        "created_at": now_taipei(),
    }


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    clean_old_outputs()

    candidates = load_all_candidates()

    if candidates.empty:
        print("No candidates found. Empty chart manifest generated.")
        pd.DataFrame().to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        pd.DataFrame().to_csv(CONTACT_SHEET_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        return 0

    candidates = limit_candidates_for_charts(candidates)

    if candidates.empty:
        print("No candidates after chart limit. Empty chart manifest generated.")
        pd.DataFrame().to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        pd.DataFrame().to_csv(CONTACT_SHEET_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        return 0

    price_df = load_price_history()

    if price_df.empty:
        print("No price history found. Empty chart manifest generated.")
        pd.DataFrame().to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        pd.DataFrame().to_csv(CONTACT_SHEET_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        return 0

    manifest_rows = []
    chart_paths_by_category: dict[str, list[Path]] = {}

    for _, candidate in candidates.iterrows():
        category = str(candidate.get("category", "")).strip()
        stock_id = normalize_code(candidate.get("stock_id", ""))
        stock_name = normalize_name(candidate.get("stock_name", ""))

        if not category or not stock_id:
            continue

        category_dir = CHART_ROOT_DIR / category
        chart_filename = f"{stock_id}_{safe_filename(stock_name)}_{category}_{candidate.get('date', '')}.png"
        chart_path = category_dir / chart_filename

        try:
            row = create_chart(price_df, candidate, category, chart_path)
            manifest_rows.append(row)
            chart_paths_by_category.setdefault(category, []).append(chart_path)
        except Exception as exc:
            print(f"Chart failed: {stock_id} {stock_name} {category}: {exc}")

            manifest_rows.append(
                {
                    "date": candidate.get("date", ""),
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "category": category,
                    "available_days": pd.NA,
                    "price_data_warning": "chart_failed",
                    "chart_path": "",
                    "chart_url": "",
                    "price_data_path": PRICE_DATA_PATH,
                    "chart_days": LOOKBACK_DAYS,
                    "close": candidate.get("close", pd.NA),
                    "previous_40d_high": pd.NA,
                    "previous_60d_high": pd.NA,
                    "distance_to_previous_40d_high_pct": pd.NA,
                    "distance_to_previous_60d_high_pct": pd.NA,
                    "breakout_type": candidate.get("breakout_type", category),
                    "score": candidate.get("score", pd.NA),
                    "rank": candidate.get("rank", pd.NA),
                    "note": f"chart_failed: {exc}",
                }
            )

    manifest_df = pd.DataFrame(manifest_rows)

    if not manifest_df.empty:
        manifest_df = manifest_df.sort_values(
            ["category", "score", "rank"],
            ascending=[True, False, True],
            na_position="last",
        )

    manifest_df.to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")

    contact_rows = []

    for category, chart_paths in chart_paths_by_category.items():
        contact_row = make_contact_sheet(category, chart_paths)

        if contact_row:
            contact_rows.append(contact_row)

    contact_df = pd.DataFrame(contact_rows)
    contact_df.to_csv(CONTACT_SHEET_MANIFEST_PATH, index=False, encoding="utf-8-sig")

    print(f"Saved chart manifest: {CHART_MANIFEST_PATH}")
    print(f"Rows: {len(manifest_df)}")
    print(f"Saved contact sheet manifest: {CONTACT_SHEET_MANIFEST_PATH}")
    print(f"Contact sheets: {len(contact_df)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
