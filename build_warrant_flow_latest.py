from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import math

import pandas as pd


LATEST_DIR = Path("output/latest")
RAW_LATEST = LATEST_DIR / "warrant_daily_raw_latest.csv"

OUTPUT_CSV = LATEST_DIR / "warrant_flow_latest.csv"
OUTPUT_MD = LATEST_DIR / "warrant_flow_latest.md"

HISTORY_DIR = Path("output/history/warrant_flow")

WARRANT_SIGNAL_ZH = {
    "call_put_bullish": "認購/認售結構偏多",
    "call_strong_inflow": "認購強流入",
    "call_inflow": "認購流入",
    "put_strong_inflow": "認售強流入",
    "put_inflow": "認售流入",
    "put_call_bearish": "認售/認購結構偏空",
    "mixed_flow": "多空混合",
    "call_activity_observation": "認購活躍觀察",
    "put_activity_observation": "認售活躍觀察",
    "low_float_call_spike": "低流通認購異常",
    "no_signal": "無明確權證訊號",
}


def warrant_signal_zh(value) -> str:
    text = "" if pd.isna(value) else str(value).strip()
    if not text:
        return "無明確權證訊號"
    return WARRANT_SIGNAL_ZH.get(text, "欄位尚未完成 / 暫用現有資料")


def clean_display(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).replace("|", "/").replace("\n", " ").strip()

OUTPUT_COLUMNS = [
    "date",
    "stock_id",
    "stock_name",
    "industry",

    "call_warrant_count",
    "put_warrant_count",

    "call_volume",
    "put_volume",
    "total_warrant_volume",

    "call_turnover",
    "put_turnover",
    "total_warrant_turnover",

    "call_put_turnover_ratio",

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

    "issuer_count",
    "top_issuer",
    "top_issuer_call_turnover",
    "top_issuer_put_turnover",

    "latest_warrant_count",
    "issued_quantity_total",
    "cancelled_quantity_total",

    "warrant_flow_signal",
    "warrant_flow_signal_zh",
    "warrant_flow_score",
    "warrant_flow_warning",
    "note",
]


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def to_number(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("--", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")

    if text in ["", "-", "nan", "None", "NaN"]:
        return pd.NA

    return pd.to_numeric(text, errors="coerce")


def safe_float(value, default=0.0) -> float:
    try:
        if pd.isna(value):
            return default

        return float(value)
    except Exception:
        return default


def is_missing_number(value) -> bool:
    try:
        return pd.isna(value) or math.isnan(float(value))
    except Exception:
        return True


def pct_change(current: float, previous: float):
    if previous is None or math.isnan(previous) or previous <= 0:
        return pd.NA

    return round((current / previous - 1) * 100, 2)


def read_raw_latest() -> pd.DataFrame:
    if not RAW_LATEST.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(RAW_LATEST, dtype={"stock_id": str, "date": str, "warrant_id": str})
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    for col in [
        "volume",
        "turnover",
        "issued_quantity",
        "cancelled_quantity",
        "latest_warrant_count",
        "float_quantity",
    ]:
        if col in df.columns:
            df[col] = df[col].map(to_number)
        else:
            df[col] = pd.NA

    if "call_put" not in df.columns:
        df["call_put"] = "unknown"

    if "issuer" not in df.columns:
        df["issuer"] = ""

    if "stock_name" not in df.columns:
        df["stock_name"] = ""

    if "stock_id" not in df.columns:
        df["stock_id"] = ""

    df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)

    return df


def build_stock_level_today(raw: pd.DataFrame) -> pd.DataFrame:
    if raw.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    latest_date = str(raw["date"].dropna().astype(str).max())
    raw = raw[raw["date"].astype(str) == latest_date].copy()

    rows = []

    for stock_id, group in raw.groupby("stock_id"):
        stock_name = ""

        if "stock_name" in group.columns:
            names = group["stock_name"].dropna().astype(str)
            names = names[names.str.len() > 0]

            if not names.empty:
                stock_name = names.iloc[0]

        call = group[group["call_put"] == "call"].copy()
        put = group[group["call_put"] == "put"].copy()

        call_turnover = safe_float(call["turnover"].sum())
        put_turnover = safe_float(put["turnover"].sum())
        total_turnover = call_turnover + put_turnover

        call_volume = safe_float(call["volume"].sum())
        put_volume = safe_float(put["volume"].sum())
        total_volume = call_volume + put_volume

        ratio = round(call_turnover / put_turnover, 2) if put_turnover > 0 else pd.NA

        low_float_call_spike_count = count_low_float_spikes(call)
        low_float_put_spike_count = count_low_float_spikes(put)

        issuer_turnover = (
            group.groupby("issuer", dropna=False)["turnover"]
            .sum()
            .sort_values(ascending=False)
        )

        top_issuer = ""

        if not issuer_turnover.empty:
            top_issuer = str(issuer_turnover.index[0])

        top_issuer_call_turnover = safe_float(call[call["issuer"] == top_issuer]["turnover"].sum()) if top_issuer else 0
        top_issuer_put_turnover = safe_float(put[put["issuer"] == top_issuer]["turnover"].sum()) if top_issuer else 0

        row = {
            "date": latest_date,
            "stock_id": stock_id,
            "stock_name": stock_name,
            "industry": "",

            "call_warrant_count": int(call["warrant_id"].nunique()) if "warrant_id" in call.columns else len(call),
            "put_warrant_count": int(put["warrant_id"].nunique()) if "warrant_id" in put.columns else len(put),

            "call_volume": round(call_volume, 0),
            "put_volume": round(put_volume, 0),
            "total_warrant_volume": round(total_volume, 0),

            "call_turnover": round(call_turnover, 0),
            "put_turnover": round(put_turnover, 0),
            "total_warrant_turnover": round(total_turnover, 0),

            "call_put_turnover_ratio": ratio,

            "call_turnover_change_1d": pd.NA,
            "call_turnover_change_5d": pd.NA,
            "put_turnover_change_1d": pd.NA,
            "put_turnover_change_5d": pd.NA,

            "call_volume_change_1d": pd.NA,
            "call_volume_change_5d": pd.NA,
            "put_volume_change_1d": pd.NA,
            "put_volume_change_5d": pd.NA,

            "low_float_call_spike_count": low_float_call_spike_count,
            "low_float_put_spike_count": low_float_put_spike_count,

            "issuer_count": int(group["issuer"].dropna().astype(str).replace("", pd.NA).dropna().nunique()),
            "top_issuer": top_issuer,
            "top_issuer_call_turnover": round(top_issuer_call_turnover, 0),
            "top_issuer_put_turnover": round(top_issuer_put_turnover, 0),

            "latest_warrant_count": safe_float(group["latest_warrant_count"].sum(), 0),
            "issued_quantity_total": safe_float(group["issued_quantity"].sum(), 0),
            "cancelled_quantity_total": safe_float(group["cancelled_quantity"].sum(), 0),

            "warrant_flow_signal": "no_signal",
            "warrant_flow_score": 0,
            "warrant_flow_warning": "",
            "note": "",
        }

        rows.append(row)

    return pd.DataFrame(rows)


def count_low_float_spikes(df: pd.DataFrame) -> int:
    if df.empty:
        return 0

    if "float_quantity" not in df.columns:
        return 0

    temp = df.copy()
    temp["float_quantity"] = pd.to_numeric(temp["float_quantity"], errors="coerce")
    temp["volume"] = pd.to_numeric(temp["volume"], errors="coerce")
    temp["turnover"] = pd.to_numeric(temp["turnover"], errors="coerce")

    low_float = temp[
        (
            (temp["float_quantity"].notna())
            & (temp["float_quantity"] > 0)
            & (temp["float_quantity"] <= 1000)
            & (
                (temp["volume"] >= temp["float_quantity"] * 0.25)
                | (temp["turnover"] >= 500000)
            )
        )
    ]

    return int(len(low_float))


def load_history_before(date_str: str) -> pd.DataFrame:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    frames = []

    for path in sorted(HISTORY_DIR.glob("warrant_flow_*.csv")):
        try:
            hist_date = path.stem.replace("warrant_flow_", "")

            if hist_date >= date_str:
                continue

            df = pd.read_csv(path, dtype={"stock_id": str, "date": str})
            frames.append(df)
        except Exception:
            continue

    if not frames:
        return pd.DataFrame()

    out = pd.concat(frames, ignore_index=True)
    out["stock_id"] = out["stock_id"].astype(str).str.zfill(4)
    out["date"] = out["date"].astype(str)

    return out


def add_history_changes(today: pd.DataFrame) -> pd.DataFrame:
    if today.empty:
        return today

    date_str = str(today["date"].iloc[0])
    hist = load_history_before(date_str)

    if hist.empty:
        return today

    metric_pairs = [
        ("call_turnover", "call_turnover_change_1d", "call_turnover_change_5d"),
        ("put_turnover", "put_turnover_change_1d", "put_turnover_change_5d"),
        ("call_volume", "call_volume_change_1d", "call_volume_change_5d"),
        ("put_volume", "put_volume_change_1d", "put_volume_change_5d"),
    ]

    today = today.copy()

    for stock_id, idxs in today.groupby("stock_id").groups.items():
        stock_hist = hist[hist["stock_id"] == stock_id].sort_values("date")

        if stock_hist.empty:
            continue

        prev = stock_hist.iloc[-1]
        prev5 = stock_hist.tail(5)

        for metric, change_1d_col, change_5d_col in metric_pairs:
            current = safe_float(today.loc[idxs, metric].iloc[0])
            previous = safe_float(prev.get(metric, pd.NA), math.nan)
            avg5 = pd.to_numeric(prev5[metric], errors="coerce").dropna().mean() if metric in prev5.columns else math.nan

            today.loc[idxs, change_1d_col] = pct_change(current, previous)
            today.loc[idxs, change_5d_col] = pct_change(current, avg5)

    return today


def has_history_comparison(row: pd.Series) -> bool:
    compare_cols = [
        "call_turnover_change_1d",
        "call_turnover_change_5d",
        "put_turnover_change_1d",
        "put_turnover_change_5d",
        "call_volume_change_1d",
        "call_volume_change_5d",
        "put_volume_change_1d",
        "put_volume_change_5d",
    ]

    for col in compare_cols:
        value = row.get(col, pd.NA)

        if not is_missing_number(value):
            return True

    return False


def classify_signal(row: pd.Series) -> tuple[str, int, str, str]:
    call_turnover = safe_float(row.get("call_turnover"))
    put_turnover = safe_float(row.get("put_turnover"))
    total_turnover = safe_float(row.get("total_warrant_turnover"))

    call_volume = safe_float(row.get("call_volume"))
    put_volume = safe_float(row.get("put_volume"))

    call_change_1d = safe_float(row.get("call_turnover_change_1d"), math.nan)
    call_change_5d = safe_float(row.get("call_turnover_change_5d"), math.nan)
    put_change_1d = safe_float(row.get("put_turnover_change_1d"), math.nan)
    put_change_5d = safe_float(row.get("put_turnover_change_5d"), math.nan)

    ratio = safe_float(row.get("call_put_turnover_ratio"), math.nan)

    low_float_call = int(safe_float(row.get("low_float_call_spike_count"), 0))
    low_float_put = int(safe_float(row.get("low_float_put_spike_count"), 0))

    signal = "no_signal"
    score = 0
    warning = []
    notes = []

    if total_turnover <= 0:
        return "no_signal", 0, "", "今日無可用權證成交金額"

    history_ready = has_history_comparison(row)

    # 第一階段：有歷史資料時，才用真正的流入 / 流出變化率
    if history_ready:
        call_inflow = (
            call_turnover >= 1_000_000
            and (
                (not math.isnan(call_change_1d) and call_change_1d >= 50)
                or (not math.isnan(call_change_5d) and call_change_5d >= 50)
            )
        )

        call_strong = (
            call_turnover >= 3_000_000
            and (
                (not math.isnan(call_change_1d) and call_change_1d >= 100)
                or (not math.isnan(call_change_5d) and call_change_5d >= 100)
            )
        )

        put_inflow = (
            put_turnover >= 1_000_000
            and (
                (not math.isnan(put_change_1d) and put_change_1d >= 50)
                or (not math.isnan(put_change_5d) and put_change_5d >= 50)
            )
        )

        bullish_ratio = not math.isnan(ratio) and ratio >= 2 and call_inflow
        mixed = call_inflow and put_inflow

        if mixed:
            signal = "mixed_flow"
            score = 0
            notes.append("認購與認售成交金額同步放大，方向不明")
        elif call_strong and bullish_ratio:
            signal = "call_put_bullish"
            score = 3
            notes.append("認購成交金額明顯大於認售，且認購資金明顯升溫")
        elif call_strong:
            signal = "call_strong_inflow"
            score = 2
            notes.append("認購權證成交金額明顯升溫")
        elif call_inflow:
            signal = "call_inflow"
            score = 1
            notes.append("認購權證資金升溫")
        elif put_inflow:
            signal = "put_inflow"
            score = -1
            warning.append("認售權證資金升溫，偏空或避險訊號")
            notes.append("認售成交金額增加")
        else:
            signal = "no_signal"
            score = 0
            notes.append("權證金流未見明顯高於近期平均的變化")

    # 第二階段：沒有歷史資料時，用絕對金額做首日觀察，不直接當真正流入
    else:
        if call_turnover >= 30_000_000 and (math.isnan(ratio) or ratio >= 3):
            signal = "call_activity_observation"
            score = 0
            notes.append("首日缺少歷史比較，認購權證成交金額偏高，先列觀察")
        elif call_turnover >= 10_000_000 and (math.isnan(ratio) or ratio >= 5):
            signal = "call_activity_observation"
            score = 0
            notes.append("首日缺少歷史比較，認購權證成交金額有一定水準，先列觀察")
        elif put_turnover >= 10_000_000 and (not math.isnan(ratio) and ratio <= 0.7):
            signal = "put_activity_observation"
            score = 0
            warning.append("首日缺少歷史比較，但認售權證成交金額偏高，先列避險觀察")
            notes.append("首日缺少歷史比較，認售權證成交金額偏高")
        elif call_turnover > 0 or put_turnover > 0:
            signal = "no_signal"
            score = 0
            notes.append("首日缺少歷史比較，權證成交金額未達觀察門檻")
        else:
            signal = "no_signal"
            score = 0
            notes.append("今日無可用權證成交金額")

    # 第三階段：低流通量權證異常成交，作為附加提醒
    if low_float_call > 0:
        if signal == "no_signal":
            signal = "low_float_call_spike"

        score += 1
        warning.append("低流通量認購權證異常成交，可能短線點火也可能過熱")
        notes.append(f"低流通量認購權證異常成交 {low_float_call} 檔")

    if low_float_put > 0:
        warning.append("低流通量認售權證異常成交")
        notes.append(f"低流通量認售權證異常成交 {low_float_put} 檔")

    # 第四階段：過熱提醒，先只給 warning，不直接改 signal，避免第一版太激進
    if call_turnover >= 100_000_000 and (not math.isnan(ratio) and ratio >= 10):
        warning.append("認購權證成交金額很大且認購/認售比偏高，需檢查標的是否高位追價或獲利結清")

    if call_volume >= 50_000_000 and call_turnover >= 50_000_000:
        warning.append("認購權證成交量與成交金額同步偏大，短線資金關注度高")

    if put_turnover >= 30_000_000:
        warning.append("認售權證成交金額偏大，需注意避險或偏空資金")

    return signal, int(score), "；".join(warning), "；".join(notes)


def apply_signals(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()

    signals = df.apply(classify_signal, axis=1, result_type="expand")
    signals.columns = ["warrant_flow_signal", "warrant_flow_score", "warrant_flow_warning", "note"]

    for col in signals.columns:
        df[col] = signals[col]

    df["warrant_flow_signal_zh"] = df["warrant_flow_signal"].map(warrant_signal_zh)

    return df


def write_markdown(df: pd.DataFrame) -> None:
    lines = []
    lines.append("# 標的股票層級權證金流判斷")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- CSV：`{OUTPUT_CSV}`")
    lines.append("")

    if df.empty:
        lines.append("目前沒有可用的官方權證資料。")
        OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
        return

    date_str = str(df["date"].iloc[0])
    lines.append(f"- 資料日期：`{date_str}`")
    lines.append(f"- 股票數：`{len(df)}`")
    lines.append("")

    summary = (
        df.groupby("warrant_flow_signal", dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    lines.append("## 訊號統計")
    lines.append("")
    lines.append("| warrant_flow_signal | count |")
    lines.append("|---|---:|")

    for _, row in summary.iterrows():
        lines.append(f"| {row['warrant_flow_signal']} | {row['count']} |")

    lines.append("")
    lines.append("## 權證金流較明顯標的")
    lines.append("")

    show = df[df["warrant_flow_signal"] != "no_signal"].copy()

    if show.empty:
        lines.append("今日無明顯權證金流訊號。")
    else:
        show = show.sort_values(
            ["warrant_flow_score", "total_warrant_turnover"],
            ascending=False,
        ).head(100)

        cols = [
            "stock_id",
            "stock_name",
            "warrant_flow_signal",
            "warrant_flow_score",
            "call_warrant_count",
            "put_warrant_count",
            "call_turnover",
            "put_turnover",
            "total_warrant_turnover",
            "call_put_turnover_ratio",
            "call_turnover_change_1d",
            "call_turnover_change_5d",
            "low_float_call_spike_count",
            "top_issuer",
            "warrant_flow_warning",
            "note",
        ]

        lines.append("| " + " | ".join(cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(cols)) + " |")

        for _, row in show.iterrows():
            values = []

            for col in cols:
                value = row.get(col, "")

                if pd.isna(value):
                    value = ""

                values.append(str(value).replace("|", "/").replace("\n", " "))

            lines.append("| " + " | ".join(values) + " |")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_markdown_v2(df: pd.DataFrame) -> None:
    lines = [
        "# 權證資金流向最新摘要",
        "",
        f"- 產出時間：`{now_taipei()} Asia/Taipei`",
        f"- CSV：`{OUTPUT_CSV}`",
        "",
    ]

    if df.empty:
        lines.append("目前沒有可用權證 raw data，僅能觀察。")
        OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
        return

    date_str = str(df["date"].iloc[0])
    lines.extend(
        [
            f"- 資料日期：`{date_str}`",
            f"- 股票筆數：`{len(df)}`",
            "",
        ]
    )

    summary = (
        df.groupby("warrant_flow_signal_zh", dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    lines.extend(["## 權證訊號分布", "", "| 權證訊號 | 數量 |", "|---|---:|"])
    for _, row in summary.iterrows():
        lines.append(f"| {clean_display(row['warrant_flow_signal_zh'])} | {row['count']} |")

    lines.extend(["", "## 權證偏多 / 偏空標的", ""])
    show = df[df["warrant_flow_signal"] != "no_signal"].copy()

    if show.empty:
        lines.append("目前沒有明確偏多或偏空權證訊號。")
    else:
        show = show.sort_values(
            ["warrant_flow_score", "total_warrant_turnover"],
            ascending=False,
        ).head(100)
        cols = [
            ("stock_id", "代號"),
            ("stock_name", "股票"),
            ("warrant_flow_signal_zh", "權證訊號"),
            ("warrant_flow_score", "權證分數"),
            ("call_warrant_count", "認購檔數"),
            ("put_warrant_count", "認售檔數"),
            ("call_turnover", "認購成交額"),
            ("put_turnover", "認售成交額"),
            ("total_warrant_turnover", "權證總成交額"),
            ("call_put_turnover_ratio", "認購/認售成交比"),
            ("call_turnover_change_1d", "認購成交額1日變化%"),
            ("call_turnover_change_5d", "認購成交額5日變化%"),
            ("low_float_call_spike_count", "低流通認購異常檔數"),
            ("top_issuer", "主要發行商"),
            ("warrant_flow_warning", "風險提醒"),
            ("note", "說明"),
        ]
        lines.append("| " + " | ".join(label for _, label in cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
        for _, row in show.iterrows():
            values = [clean_display(row.get(col, "")) for col, _ in cols]
            lines.append("| " + " | ".join(values) + " |")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    raw = read_raw_latest()

    if raw.empty:
        out = pd.DataFrame(columns=OUTPUT_COLUMNS)
        out.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
        write_markdown_v2(out)
        print("No raw warrant data. Empty warrant flow output created.")
        return 0

    out = build_stock_level_today(raw)
    out = add_history_changes(out)
    out = apply_signals(out)

    for col in OUTPUT_COLUMNS:
        if col not in out.columns:
            out[col] = pd.NA

    out = out[OUTPUT_COLUMNS].copy()

    out = out.sort_values(
        ["warrant_flow_score", "total_warrant_turnover"],
        ascending=False,
    ).reset_index(drop=True)

    date_str = str(out["date"].iloc[0]) if not out.empty else datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")

    out.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    out.to_csv(HISTORY_DIR / f"warrant_flow_{date_str}.csv", index=False, encoding="utf-8-sig")

    write_markdown_v2(out)

    print(f"Saved: {OUTPUT_CSV}, rows={len(out)}")
    print(f"Saved: {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
