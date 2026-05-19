from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import math
import re
import shutil

import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


DAILY_PRICE_DIR = Path("data/daily_price")
LATEST_DIR = Path("output/latest")

CHART_ROOT = LATEST_DIR / "charts"
CONTACT_SHEET_DIR = LATEST_DIR / "contact_sheets"
CHART_MANIFEST_PATH = LATEST_DIR / "chart_manifest.csv"

REPO_RAW_BASE = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"

LOOKBACK_DAYS = 180
CONTACT_SHEET_LIMIT = 20

CATEGORY_CONFIG = [
    {
        "category": "true_breakout",
        "csv_path": LATEST_DIR / "breakout_latest.csv",
        "note": "真正突破前高",
    },
    {
        "category": "range_rebound",
        "csv_path": LATEST_DIR / "range_rebound_watch_latest.csv",
        "note": "區間內轉強 / 挑戰前高觀察",
    },
    {
        "category": "revenue_pullback",
        "csv_path": LATEST_DIR / "revenue_pullback_latest.csv",
        "note": "營收成長但股價回檔",
    },
    {
        "category": "pullback_rebound",
        "csv_path": LATEST_DIR / "pullback_rebound_latest.csv",
        "note": "營收回檔後短線轉強",
    },
]


def ensure_dirs() -> None:
    CHART_ROOT.mkdir(parents=True, exist_ok=True)
    CONTACT_SHEET_DIR.mkdir(parents=True, exist_ok=True)

    for item in CATEGORY_CONFIG:
        (CHART_ROOT / item["category"]).mkdir(parents=True, exist_ok=True)

    (CHART_ROOT / "pattern").mkdir(parents=True, exist_ok=True)


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_code(value) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    text = re.sub(r"[^0-9]", "", text)
    return text.zfill(4)


def normalize_name(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip().replace("/", "_").replace("\\", "_").replace(" ", "")


def clean_number(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("--", "")
    text = text.replace("X", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")

    if text == "":
        return pd.NA

    return pd.to_numeric(text, errors="coerce")


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def fmt_price(value) -> str:
    if value is None or pd.isna(value):
        return "-"
    return f"{float(value):.2f}"


def fmt_pct(value) -> str:
    if value is None or pd.isna(value):
        return "-"
    value = float(value)
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def extract_date_from_path(path: Path) -> str | None:
    match = re.search(r"([0-9]{8})", path.name)
    if match:
        return match.group(1)
    return None


def load_daily_price_history() -> pd.DataFrame:
    files = sorted(DAILY_PRICE_DIR.glob("*.csv"))

    frames = []

    for path in files:
        try:
            df = pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str, "date": str})
        except Exception as exc:
            print(f"Skip daily price file {path}: {exc}")
            continue

        if df.empty:
            continue

        if "ticker" in df.columns and "stock_id" not in df.columns:
            df = df.rename(columns={"ticker": "stock_id"})

        if "code" in df.columns and "stock_id" not in df.columns:
            df = df.rename(columns={"code": "stock_id"})

        if "stock_id" not in df.columns:
            print(f"Skip daily price file {path}: missing stock_id/ticker/code")
            continue

        if "date" not in df.columns:
            date = extract_date_from_path(path)
            if date:
                df["date"] = date

        if "name" not in df.columns:
            df["name"] = ""

        if "trading_value" not in df.columns:
            if "amount" in df.columns:
                df["trading_value"] = df["amount"]
            elif "turnover" in df.columns:
                df["trading_value"] = df["turnover"]
            else:
                df["trading_value"] = pd.NA

        required = {"date", "stock_id", "open", "high", "low", "close", "volume"}

        missing = required - set(df.columns)

        if missing:
            print(f"Skip daily price file {path}: missing columns {sorted(missing)}")
            continue

        df = df.copy()
        df["date"] = df["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
        df["stock_id"] = df["stock_id"].map(normalize_code)
        df["name"] = df["name"].map(normalize_name)

        for col in ["open", "high", "low", "close", "volume", "trading_value"]:
            df[col] = df[col].map(clean_number)

        df = df.dropna(subset=["date", "stock_id", "open", "high", "low", "close"])
        df = df[df["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

        frames.append(
            df[
                [
                    "date",
                    "stock_id",
                    "name",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "trading_value",
                ]
            ]
        )

    if not frames:
        return pd.DataFrame()

    price = pd.concat(frames, ignore_index=True)
    price = price.drop_duplicates(subset=["date", "stock_id"], keep="last")
    price = price.sort_values(["stock_id", "date"]).reset_index(drop=True)

    return price


def standardize_candidate_columns(df: pd.DataFrame, category: str) -> pd.DataFrame:
    df = df.copy()

    if "stock_id" not in df.columns:
        if "ticker" in df.columns:
            df = df.rename(columns={"ticker": "stock_id"})
        elif "code" in df.columns:
            df = df.rename(columns={"code": "stock_id"})

    if "stock_name" not in df.columns:
        if "name" in df.columns:
            df = df.rename(columns={"name": "stock_name"})
        elif "company_name" in df.columns:
            df = df.rename(columns={"company_name": "stock_name"})
        else:
            df["stock_name"] = ""

    if "stock_id" not in df.columns:
        return pd.DataFrame()

    df["stock_id"] = df["stock_id"].map(normalize_code)
    df["stock_name"] = df["stock_name"].map(normalize_name)
    df["category"] = category

    if "breakout_type" not in df.columns:
        if category == "true_breakout":
            df["breakout_type"] = "true_breakout"
        elif category == "range_rebound":
            df["breakout_type"] = "range_rebound"
        elif category == "revenue_pullback":
            df["breakout_type"] = "revenue_pullback"
        elif category == "pullback_rebound":
            df["breakout_type"] = "pullback_rebound"
        else:
            df["breakout_type"] = category

    if "score" not in df.columns:
        df["score"] = pd.NA

    df = df[df["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

    return df


def load_candidates_from_csv(path: Path, category: str) -> pd.DataFrame:
    if not path.exists():
        print(f"Candidate file missing, skip: {path}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str})
    except Exception as exc:
        print(f"Failed to read candidate file {path}: {exc}")
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    return standardize_candidate_columns(df, category)


def load_pattern_candidates() -> pd.DataFrame:
    pattern_files = []

    for path in sorted(LATEST_DIR.glob("*pattern*.csv")):
        name = path.name.lower()

        if "chart_manifest" in name:
            continue

        if "current_holdings" in name:
            continue

        if "repair" in name:
            continue

        pattern_files.append(path)

    frames = []

    for path in pattern_files:
        try:
            df = pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str})
        except Exception as exc:
            print(f"Failed to read pattern candidate file {path}: {exc}")
            continue

        if df.empty:
            continue

        df = standardize_candidate_columns(df, "pattern")

        if df.empty:
            continue

        df["pattern_source_file"] = str(path)
        df["breakout_type"] = "pattern"

        frames.append(df)

    if not frames:
        return pd.DataFrame()

    combined = pd.concat(frames, ignore_index=True)
    combined = combined.drop_duplicates(subset=["stock_id", "category"], keep="first")

    return combined


def load_all_candidates() -> pd.DataFrame:
    frames = []

    for item in CATEGORY_CONFIG:
        df = load_candidates_from_csv(item["csv_path"], item["category"])
        if not df.empty:
            frames.append(df)

    pattern_df = load_pattern_candidates()

    if not pattern_df.empty:
        frames.append(pattern_df)

    if not frames:
        return pd.DataFrame()

    candidates = pd.concat(frames, ignore_index=True)

    candidates = candidates.drop_duplicates(
        subset=["stock_id", "category", "breakout_type"],
        keep="first",
    )

    return candidates


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["open", "high", "low", "close", "volume", "trading_value"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["ema23"] = df["close"].ewm(span=23, adjust=False).mean()
    df["volume_ma20"] = df["volume"].rolling(20).mean()
    df["volume_ratio_20"] = df["volume"] / df["volume_ma20"]

    return df


def calc_reference_levels(df: pd.DataFrame) -> dict:
    if df.empty:
        return {}

    latest = df.iloc[-1]
    previous = df.iloc[:-1].copy()

    previous_40 = previous.tail(40)
    previous_60 = previous.tail(60)

    previous_40d_high = previous_40["high"].max() if not previous_40.empty else pd.NA
    previous_60d_high = previous_60["high"].max() if not previous_60.empty else pd.NA

    previous_40d_low = previous_40["low"].min() if not previous_40.empty else pd.NA
    previous_60d_low = previous_60["low"].min() if not previous_60.empty else pd.NA

    close = latest["close"]

    distance_40 = (close / previous_40d_high - 1) * 100 if previous_40d_high and not pd.isna(previous_40d_high) else pd.NA
    distance_60 = (close / previous_60d_high - 1) * 100 if previous_60d_high and not pd.isna(previous_60d_high) else pd.NA

    is_true_breakout_40 = close > previous_40d_high if previous_40d_high and not pd.isna(previous_40d_high) else False
    is_true_breakout_60 = close > previous_60d_high if previous_60d_high and not pd.isna(previous_60d_high) else False

    return {
        "date": latest["date"],
        "close": close,
        "previous_40d_high": previous_40d_high,
        "previous_60d_high": previous_60d_high,
        "previous_40d_low": previous_40d_low,
        "previous_60d_low": previous_60d_low,
        "distance_to_previous_40d_high_pct": distance_40,
        "distance_to_previous_60d_high_pct": distance_60,
        "is_true_breakout_40": is_true_breakout_40,
        "is_true_breakout_60": is_true_breakout_60,
        "ma20": latest.get("ma20", pd.NA),
        "ma60": latest.get("ma60", pd.NA),
        "ema23": latest.get("ema23", pd.NA),
        "volume_ratio_20": latest.get("volume_ratio_20", pd.NA),
    }


def make_note(category: str, breakout_type: str, ref: dict) -> str:
    close = ref.get("close", pd.NA)
    previous_60d_high = ref.get("previous_60d_high", pd.NA)
    distance_60 = ref.get("distance_to_previous_60d_high_pct", pd.NA)
    is_true_breakout_60 = bool(ref.get("is_true_breakout_60", False))

    if category == "true_breakout":
        if is_true_breakout_60:
            return f"真正突破前60日高點；收盤 {fmt_price(close)}，前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"
        return f"分類檢查警示：尚未突破前60日高點；收盤 {fmt_price(close)}，前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "range_rebound":
        return f"尚未突破前高 / 挑戰前高觀察；收盤 {fmt_price(close)}，前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "revenue_pullback":
        return f"營收成長但股價回檔；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "pullback_rebound":
        return f"營收回檔後短線轉強；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    if category == "pattern":
        return f"Pattern Scanner 候選；前60日高點 {fmt_price(previous_60d_high)}，距離 {fmt_pct(distance_60)}"

    return str(breakout_type)


def draw_candles(ax, df: pd.DataFrame) -> None:
    x_values = range(len(df))

    for x, row in zip(x_values, df.itertuples(index=False)):
        open_price = float(row.open)
        high_price = float(row.high)
        low_price = float(row.low)
        close_price = float(row.close)

        is_up = close_price >= open_price
        color = "#d62728" if is_up else "#2ca02c"

        ax.vlines(x, low_price, high_price, color=color, linewidth=0.8)

        body_low = min(open_price, close_price)
        body_height = abs(close_price - open_price)

        if body_height == 0:
            body_height = max(close_price * 0.001, 0.01)

        rect = plt.Rectangle(
            (x - 0.3, body_low),
            0.6,
            body_height,
            facecolor=color,
            edgecolor=color,
            alpha=0.75,
        )

        ax.add_patch(rect)


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

    if df.empty or len(df) < 20:
        raise ValueError(f"{stock_id} {stock_name} available price days too few: {len(df)}")

    if not stock_name:
        names = df["name"].dropna().astype(str)
        if not names.empty:
            stock_name = normalize_name(names.iloc[-1])

    df = add_indicators(df)
    ref = calc_reference_levels(df)

    latest = df.iloc[-1]
    chart_date = str(latest["date"])

    previous_40d_high = ref.get("previous_40d_high", pd.NA)
    previous_60d_high = ref.get("previous_60d_high", pd.NA)
    previous_40d_low = ref.get("previous_40d_low", pd.NA)
    previous_60d_low = ref.get("previous_60d_low", pd.NA)

    distance_40 = ref.get("distance_to_previous_40d_high_pct", pd.NA)
    distance_60 = ref.get("distance_to_previous_60d_high_pct", pd.NA)

    breakout_type = str(candidate.get("breakout_type", category))
    note = make_note(category, breakout_type, ref)

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

    if category == "true_breakout" and bool(ref.get("is_true_breakout_60", False)):
        label = "True breakout over previous 60D high"
    elif category == "range_rebound":
        label = "Not yet breakout / near resistance watch"
    else:
        label = note

    title = (
        f"{stock_id} {stock_name} | {category} | {chart_date}\n"
        f"{label} | Dist60: {fmt_pct(distance_60)} | Dist40: {fmt_pct(distance_40)}"
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
    fig.savefig(chart_path, dpi=130, bbox_inches="tight")
    plt.close(fig)

    return {
        "date": chart_date,
        "stock_id": stock_id,
        "stock_name": stock_name,
        "category": category,
        "chart_path": str(chart_path).replace("\\", "/"),
        "chart_url": f"{REPO_RAW_BASE}/{str(chart_path).replace('\\', '/')}",
        "close": round(float(latest["close"]), 2),
        "previous_40d_high": round(float(previous_40d_high), 2) if not pd.isna(previous_40d_high) else pd.NA,
        "previous_60d_high": round(float(previous_60d_high), 2) if not pd.isna(previous_60d_high) else pd.NA,
        "distance_to_previous_40d_high_pct": round(float(distance_40), 2) if not pd.isna(distance_40) else pd.NA,
        "distance_to_previous_60d_high_pct": round(float(distance_60), 2) if not pd.isna(distance_60) else pd.NA,
        "breakout_type": breakout_type,
        "note": note,
    }


def clean_old_outputs() -> None:
    for category_dir in [
        CHART_ROOT / "true_breakout",
        CHART_ROOT / "range_rebound",
        CHART_ROOT / "revenue_pullback",
        CHART_ROOT / "pullback_rebound",
        CHART_ROOT / "pattern",
    ]:
        if category_dir.exists():
            for path in category_dir.glob("*.png"):
                path.unlink()

    if CONTACT_SHEET_DIR.exists():
        for path in CONTACT_SHEET_DIR.glob("*.png"):
            path.unlink()


def create_contact_sheet(category: str, chart_paths: list[Path]) -> Path | None:
    chart_paths = [path for path in chart_paths if path.exists()]
    chart_paths = chart_paths[:CONTACT_SHEET_LIMIT]

    if not chart_paths:
        return None

    columns = 2
    rows = math.ceil(len(chart_paths) / columns)

    fig, axes = plt.subplots(rows, columns, figsize=(18, 5 * rows))

    if rows == 1:
        axes = [axes] if columns == 1 else axes

    flat_axes = []
    if rows == 1:
        flat_axes = list(axes)
    else:
        for row_axes in axes:
            flat_axes.extend(list(row_axes))

    for ax, path in zip(flat_axes, chart_paths):
        img = mpimg.imread(path)
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(path.name, fontsize=10)

    for ax in flat_axes[len(chart_paths):]:
        ax.axis("off")

    output_path = CONTACT_SHEET_DIR / f"{category}_contact_sheet.png"
    fig.suptitle(f"{category} contact sheet", fontsize=16)
    fig.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)

    return output_path


def main() -> int:
    ensure_dirs()
    clean_old_outputs()

    price_df = load_daily_price_history()

    if price_df.empty:
        print("No daily price history found. Empty chart manifest generated.")
        pd.DataFrame().to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        return 0

    candidates = load_all_candidates()

    if candidates.empty:
        print("No candidates found. Empty chart manifest generated.")
        pd.DataFrame().to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")
        return 0

    manifest_rows = []
    category_chart_paths: dict[str, list[Path]] = {}

    for _, candidate in candidates.iterrows():
        stock_id = normalize_code(candidate.get("stock_id", ""))
        stock_name = normalize_name(candidate.get("stock_name", ""))
        category = str(candidate.get("category", "")).strip()

        if not stock_id or not category:
            continue

        chart_date = str(candidate.get("date", "")).replace("-", "").replace("/", "").strip()

        if not chart_date or chart_date.lower() == "nan":
            stock_price = price_df[price_df["stock_id"] == stock_id].copy()
            if stock_price.empty:
                chart_date = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")
            else:
                chart_date = str(stock_price["date"].max())

        if not stock_name:
            stock_price = price_df[price_df["stock_id"] == stock_id].copy()
            if not stock_price.empty:
                stock_name = normalize_name(stock_price.iloc[-1].get("name", ""))

        filename = f"{stock_id}_{stock_name}_{category}_{chart_date}.png"
        filename = filename.replace("/", "_").replace("\\", "_").replace(" ", "")

        chart_path = CHART_ROOT / category / filename

        try:
            row = create_chart(
                price_df=price_df,
                candidate=candidate,
                category=category,
                chart_path=chart_path,
            )
            manifest_rows.append(row)
            category_chart_paths.setdefault(category, []).append(chart_path)
            print(f"Chart generated: {chart_path}")
        except Exception as exc:
            warning_row = {
                "date": chart_date,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "category": category,
                "chart_path": "",
                "chart_url": "",
                "close": pd.NA,
                "previous_40d_high": pd.NA,
                "previous_60d_high": pd.NA,
                "distance_to_previous_40d_high_pct": pd.NA,
                "distance_to_previous_60d_high_pct": pd.NA,
                "breakout_type": str(candidate.get("breakout_type", category)),
                "note": f"chart_failed: {exc}",
            }
            manifest_rows.append(warning_row)
            print(f"Chart failed for {stock_id} {stock_name} {category}: {exc}")

    manifest = pd.DataFrame(manifest_rows)

    if not manifest.empty:
        manifest = manifest.sort_values(["category", "stock_id"]).reset_index(drop=True)

    manifest.to_csv(CHART_MANIFEST_PATH, index=False, encoding="utf-8-sig")

    contact_rows = []

    for category, paths in category_chart_paths.items():
        contact_path = create_contact_sheet(category, paths)

        if contact_path:
            contact_rows.append(
                {
                    "category": category,
                    "contact_sheet_path": str(contact_path).replace("\\", "/"),
                    "contact_sheet_url": f"{REPO_RAW_BASE}/{str(contact_path).replace('\\', '/')}",
                    "chart_count": len(paths),
                    "created_at": now_taipei(),
                }
            )
            print(f"Contact sheet generated: {contact_path}")

    contact_df = pd.DataFrame(contact_rows)
    contact_df.to_csv(LATEST_DIR / "contact_sheet_manifest.csv", index=False, encoding="utf-8-sig")

    print(f"Chart manifest saved: {CHART_MANIFEST_PATH}")
    print(f"Contact sheet manifest saved: {LATEST_DIR / 'contact_sheet_manifest.csv'}")
    print(f"Charts generated: {len(manifest_rows)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
