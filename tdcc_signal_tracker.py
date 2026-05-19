from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re

import pandas as pd


OUTPUT_DIR = Path("output")
LATEST_DIR = OUTPUT_DIR / "latest"
HISTORY_DIR = OUTPUT_DIR / "history"
TDCC_HISTORY_DIR = HISTORY_DIR / "tdcc"
SIGNAL_DIR = HISTORY_DIR / "tdcc_signals"
DAILY_PRICE_DIR = Path("data") / "daily_price"

LATEST_SNAPSHOT_CANDIDATES = [
    LATEST_DIR / "tdcc_holder_ratio_latest.csv",
    OUTPUT_DIR / "tdcc_holder_ratio_latest.csv",
]

SIGNAL_LOG_PATH = SIGNAL_DIR / "tdcc_signal_log.csv"
PERFORMANCE_CSV_PATH = SIGNAL_DIR / "tdcc_signal_performance.csv"
LATEST_REPORT_PATH = OUTPUT_DIR / "tdcc_signal_performance_latest.md"
LATEST_REPORT_COMPAT_PATH = LATEST_DIR / "tdcc_signal_performance_latest.md"

THRESHOLDS = [400, 600, 800, 1000]
TOP_N = 20
HORIZONS = [1, 2, 5, 10, 20]

SIGNAL_KEY_COLUMNS = [
    "signal_date",
    "code",
    "signal_type",
    "threshold_group",
]

PERFORMANCE_COLUMNS = [
    "signal_trade_date",
    "signal_close",
    "pre_signal_5d_return_pct",
    "d1_close",
    "d2_close",
    "d5_close",
    "d10_close",
    "d20_close",
    "d1_return_pct",
    "d2_return_pct",
    "d5_return_pct",
    "d10_return_pct",
    "d20_return_pct",
    "max_high_after_signal_5d",
    "max_high_after_signal_10d",
    "max_high_after_signal_20d",
    "max_return_5d",
    "max_return_10d",
    "max_return_20d",
    "min_low_after_signal_5d",
    "min_low_after_signal_10d",
    "min_low_after_signal_20d",
    "max_drawdown_5d",
    "max_drawdown_10d",
    "max_drawdown_20d",
    "status",
]


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    SIGNAL_DIR.mkdir(parents=True, exist_ok=True)


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).replace("\ufeff", "").strip()


def normalize_code(value) -> str:
    text = normalize_text(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4)


def is_common_stock_code(code: str) -> bool:
    code = normalize_code(code)

    if not re.match(r"^[0-9]{4}$", code):
        return False

    if code.startswith("00"):
        return False

    try:
        return int(code) >= 1000
    except ValueError:
        return False


def to_number(value):
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


def signed_pct(value) -> str:
    if pd.isna(value):
        return "-"
    value = float(value)
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def extract_date_from_path(path: Path) -> str | None:
    match = re.search(r"([0-9]{8})", path.name)
    if match:
        return match.group(1)
    return None


def get_latest_snapshot_path() -> Path:
    for path in LATEST_SNAPSHOT_CANDIDATES:
        if path.exists():
            return path

    raise FileNotFoundError(
        "找不到 TDCC 最新快照。請確認以下任一檔案存在："
        + " / ".join(str(path) for path in LATEST_SNAPSHOT_CANDIDATES)
    )


def load_snapshot(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"code": str})

    required = {"date", "code", "name"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"{path} 缺少必要欄位：{sorted(missing)}")

    for threshold in THRESHOLDS:
        col = f"over_{threshold}_pct"
        if col not in df.columns:
            raise ValueError(f"{path} 缺少欄位：{col}")

    df = df.copy()
    df["date"] = df["date"].map(normalize_text)
    df["code"] = df["code"].map(normalize_code)
    df["name"] = df["name"].map(normalize_text)
    df = df[df["code"].map(is_common_stock_code)].copy()

    for threshold in THRESHOLDS:
        col = f"over_{threshold}_pct"
        df[col] = df[col].map(to_number)

    return df.reset_index(drop=True)


def get_snapshot_date(snapshot: pd.DataFrame) -> str:
    dates = snapshot["date"].dropna().astype(str).unique()
    if len(dates) == 0:
        raise ValueError("snapshot 沒有 date。")
    return max(dates)


def find_history_snapshot_paths() -> list[Path]:
    paths = []

    if TDCC_HISTORY_DIR.exists():
        paths.extend(sorted(TDCC_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv")))

    if HISTORY_DIR.exists():
        paths.extend(sorted(HISTORY_DIR.glob("tdcc_holder_ratio_*.csv")))

    unique = {}

    for path in paths:
        date = extract_date_from_path(path)
        if date:
            unique[date] = path

    return [unique[date] for date in sorted(unique.keys())]


def find_previous_snapshot_path(current_date: str) -> Path | None:
    candidates = []

    for path in find_history_snapshot_paths():
        date = extract_date_from_path(path)
        if date and date < current_date:
            candidates.append((date, path))

    if not candidates:
        return None

    return sorted(candidates, key=lambda item: item[0])[-1][1]


def get_recent_snapshot_paths(required_count: int) -> list[Path]:
    paths = []

    for path in find_history_snapshot_paths():
        date = extract_date_from_path(path)
        if date:
            paths.append((date, path))

    paths = sorted(paths, key=lambda item: item[0])
    return [path for _, path in paths[-required_count:]]


def build_weekly_top20_signals(
    current_snapshot: pd.DataFrame,
    previous_snapshot: pd.DataFrame | None,
    source_tdcc_date: str,
    source_compare_date: str | None,
) -> pd.DataFrame:
    signals = []

    if previous_snapshot is None:
        for threshold in THRESHOLDS:
            current_col = f"over_{threshold}_pct"

            table = current_snapshot[["code", "name", current_col]].copy()
            table = table.rename(columns={current_col: "current_pct"})
            table["previous_pct"] = pd.NA
            table["weekly_change_pct"] = pd.NA

            table = table.sort_values(
                ["current_pct", "code"],
                ascending=[False, True],
            ).head(TOP_N)

            for rank, row in enumerate(table.itertuples(index=False), start=1):
                signals.append(
                    {
                        "signal_date": source_tdcc_date,
                        "code": row.code,
                        "name": row.name,
                        "signal_type": "weekly_top20_current_pct",
                        "threshold_group": f"over_{threshold}",
                        "rank": rank,
                        "current_pct": row.current_pct,
                        "previous_pct": pd.NA,
                        "weekly_change_pct": pd.NA,
                        "is_consecutive_2w": False,
                        "consecutive_score": 0.0,
                        "source_tdcc_date": source_tdcc_date,
                        "source_compare_date": source_compare_date or "",
                        "created_at": now_taipei(),
                    }
                )

        return pd.DataFrame(signals)

    current_cols = ["code", "name"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]
    previous_cols = ["code"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]

    current = current_snapshot[current_cols].copy()
    previous = previous_snapshot[previous_cols].copy()

    merged = current.merge(
        previous,
        on="code",
        how="inner",
        suffixes=("_current", "_previous"),
    )

    for threshold in THRESHOLDS:
        current_col = f"over_{threshold}_pct_current"
        previous_col = f"over_{threshold}_pct_previous"

        table = merged[["code", "name", current_col, previous_col]].copy()
        table = table.rename(
            columns={
                current_col: "current_pct",
                previous_col: "previous_pct",
            }
        )

        table["current_pct"] = pd.to_numeric(table["current_pct"], errors="coerce")
        table["previous_pct"] = pd.to_numeric(table["previous_pct"], errors="coerce")
        table = table.dropna(subset=["current_pct", "previous_pct"])
        table["weekly_change_pct"] = table["current_pct"] - table["previous_pct"]

        table = table.sort_values(
            ["weekly_change_pct", "current_pct", "code"],
            ascending=[False, False, True],
        ).head(TOP_N)

        for rank, row in enumerate(table.itertuples(index=False), start=1):
            signals.append(
                {
                    "signal_date": source_tdcc_date,
                    "code": row.code,
                    "name": row.name,
                    "signal_type": "weekly_change_top20",
                    "threshold_group": f"over_{threshold}",
                    "rank": rank,
                    "current_pct": row.current_pct,
                    "previous_pct": row.previous_pct,
                    "weekly_change_pct": row.weekly_change_pct,
                    "is_consecutive_2w": False,
                    "consecutive_score": 0.0,
                    "source_tdcc_date": source_tdcc_date,
                    "source_compare_date": source_compare_date or "",
                    "created_at": now_taipei(),
                }
            )

    return pd.DataFrame(signals)


def build_consecutive_2w_signals() -> pd.DataFrame:
    recent_paths = get_recent_snapshot_paths(3)

    if len(recent_paths) < 3:
        return pd.DataFrame()

    snapshots = [load_snapshot(path) for path in recent_paths]
    dates = [get_snapshot_date(snapshot) for snapshot in snapshots]

    base = snapshots[-1][["code", "name"]].copy()

    for i, snapshot in enumerate(snapshots):
        cols = ["code"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]
        temp = snapshot[cols].copy()
        temp = temp.rename(
            columns={
                f"over_{threshold}_pct": f"over_{threshold}_pct_w{i}"
                for threshold in THRESHOLDS
            }
        )
        base = base.merge(temp, on="code", how="inner")

    for threshold in THRESHOLDS:
        for i in range(1, len(snapshots)):
            prev_col = f"over_{threshold}_pct_w{i - 1}"
            curr_col = f"over_{threshold}_pct_w{i}"
            delta_col = f"delta_{threshold}_w{i}"

            base[prev_col] = pd.to_numeric(base[prev_col], errors="coerce")
            base[curr_col] = pd.to_numeric(base[curr_col], errors="coerce")
            base[delta_col] = base[curr_col] - base[prev_col]

    delta_cols = [
        f"delta_{threshold}_w{i}"
        for threshold in THRESHOLDS
        for i in range(1, len(snapshots))
    ]

    table = base.dropna(subset=delta_cols).copy()

    for col in delta_cols:
        table = table[table[col] > 0].copy()

    if table.empty:
        return pd.DataFrame()

    for threshold in THRESHOLDS:
        threshold_delta_cols = [
            f"delta_{threshold}_w{i}" for i in range(1, len(snapshots))
        ]
        table[f"over_{threshold}_total_change"] = table[threshold_delta_cols].sum(axis=1)

    score_cols = [f"over_{threshold}_total_change" for threshold in THRESHOLDS]
    table["consecutive_score"] = table[score_cols].sum(axis=1)

    table = table.sort_values(
        ["consecutive_score", "code"],
        ascending=[False, True],
    ).head(TOP_N)

    latest_date = dates[-1]
    compare_date = dates[-2]

    signals = []

    for rank, row in enumerate(table.itertuples(index=False), start=1):
        current_values = []
        previous_values = []
        latest_week_changes = []

        for threshold in THRESHOLDS:
            current_values.append(getattr(row, f"over_{threshold}_pct_w2"))
            previous_values.append(getattr(row, f"over_{threshold}_pct_w1"))
            latest_week_changes.append(getattr(row, f"delta_{threshold}_w2"))

        current_pct = sum(current_values) / len(current_values)
        previous_pct = sum(previous_values) / len(previous_values)
        weekly_change_pct = sum(latest_week_changes)

        signals.append(
            {
                "signal_date": latest_date,
                "code": row.code,
                "name": row.name,
                "signal_type": "consecutive_2w_all_thresholds",
                "threshold_group": "all_400_600_800_1000",
                "rank": rank,
                "current_pct": current_pct,
                "previous_pct": previous_pct,
                "weekly_change_pct": weekly_change_pct,
                "is_consecutive_2w": True,
                "consecutive_score": row.consecutive_score,
                "source_tdcc_date": latest_date,
                "source_compare_date": compare_date,
                "created_at": now_taipei(),
            }
        )

    return pd.DataFrame(signals)


def build_current_signals() -> pd.DataFrame:
    latest_snapshot_path = get_latest_snapshot_path()

    current_snapshot = load_snapshot(latest_snapshot_path)
    current_date = get_snapshot_date(current_snapshot)

    previous_path = find_previous_snapshot_path(current_date)
    previous_snapshot = load_snapshot(previous_path) if previous_path else None
    previous_date = get_snapshot_date(previous_snapshot) if previous_snapshot is not None else None

    weekly_signals = build_weekly_top20_signals(
        current_snapshot=current_snapshot,
        previous_snapshot=previous_snapshot,
        source_tdcc_date=current_date,
        source_compare_date=previous_date,
    )

    consecutive_signals = build_consecutive_2w_signals()

    signals = pd.concat(
        [weekly_signals, consecutive_signals],
        ignore_index=True,
    )

    if signals.empty:
        return signals

    signals["code"] = signals["code"].map(normalize_code)

    for col in ["rank", "current_pct", "previous_pct", "weekly_change_pct", "consecutive_score"]:
        if col in signals.columns:
            signals[col] = pd.to_numeric(signals[col], errors="coerce")

    return signals


def load_existing_signal_log() -> pd.DataFrame:
    if not SIGNAL_LOG_PATH.exists():
        return pd.DataFrame()

    df = pd.read_csv(SIGNAL_LOG_PATH, dtype={"code": str})

    if "code" in df.columns:
        df["code"] = df["code"].map(normalize_code)

    return df


def save_signal_log(new_signals: pd.DataFrame) -> pd.DataFrame:
    existing = load_existing_signal_log()

    if existing.empty:
        combined = new_signals.copy()
    else:
        combined = pd.concat([existing, new_signals], ignore_index=True)

    if combined.empty:
        combined.to_csv(SIGNAL_LOG_PATH, index=False, encoding="utf-8-sig")
        return combined

    combined["code"] = combined["code"].map(normalize_code)

    combined = combined.drop_duplicates(
        subset=SIGNAL_KEY_COLUMNS,
        keep="last",
    )

    combined = combined.sort_values(
        ["signal_date", "signal_type", "threshold_group", "rank", "code"],
        ascending=[True, True, True, True, True],
    ).reset_index(drop=True)

    combined.to_csv(SIGNAL_LOG_PATH, index=False, encoding="utf-8-sig")

    return combined


def load_daily_price_data() -> pd.DataFrame:
    files = sorted(DAILY_PRICE_DIR.glob("*.csv"))

    if not files:
        return pd.DataFrame()

    frames = []

    for path in files:
        try:
            df = pd.read_csv(path, dtype={"ticker": str, "code": str})
        except Exception as exc:
            print(f"Skip daily price file {path}: {exc}")
            continue

        if df.empty:
            continue

        if "ticker" in df.columns and "code" not in df.columns:
            df = df.rename(columns={"ticker": "code"})

        if "date" not in df.columns:
            date = extract_date_from_path(path)
            if date:
                df["date"] = date

        required = {"date", "code", "open", "high", "low", "close"}
        missing = required - set(df.columns)

        if missing:
            print(f"Skip daily price file {path}, missing columns: {missing}")
            continue

        if "name" not in df.columns:
            df["name"] = ""

        df["code"] = df["code"].map(normalize_code)
        df["date"] = df["date"].map(normalize_text)

        for col in ["open", "high", "low", "close"]:
            df[col] = df[col].map(to_number)

        df = df.dropna(subset=["date", "code", "close"])
        df = df[df["code"].map(is_common_stock_code)].copy()

        frames.append(df[["date", "code", "name", "open", "high", "low", "close"]])

    if not frames:
        return pd.DataFrame()

    price = pd.concat(frames, ignore_index=True)
    price = price.drop_duplicates(subset=["date", "code"], keep="last")
    price = price.sort_values(["code", "date"]).reset_index(drop=True)

    return price


def latest_trading_date_on_or_before(dates: list[str], target_date: str) -> str | None:
    candidates = [date for date in dates if date <= target_date]

    if not candidates:
        return None

    return candidates[-1]


def ensure_performance_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in PERFORMANCE_COLUMNS:
        if col not in df.columns:
            df[col] = pd.NA

    return df


def calculate_signal_performance(signal_log: pd.DataFrame, price: pd.DataFrame) -> pd.DataFrame:
    if signal_log.empty:
        return ensure_performance_columns(pd.DataFrame())

    if price.empty:
        perf = signal_log.copy()
        perf["status"] = "no_price_data"
        return ensure_performance_columns(perf)

    rows = []

    for _, signal in signal_log.iterrows():
        signal_dict = signal.to_dict()

        code = normalize_code(signal_dict["code"])
        signal_date = normalize_text(signal_dict["signal_date"])

        price_by_code = price[price["code"] == code].copy()
        price_by_code = price_by_code.sort_values("date").reset_index(drop=True)

        row = dict(signal_dict)
        row["code"] = code

        if price_by_code.empty:
            row["signal_trade_date"] = ""
            row["signal_close"] = pd.NA
            row["pre_signal_5d_return_pct"] = pd.NA

            for horizon in HORIZONS:
                row[f"d{horizon}_close"] = pd.NA
                row[f"d{horizon}_return_pct"] = pd.NA
                row[f"max_high_after_signal_{horizon}d"] = pd.NA
                row[f"max_return_{horizon}d"] = pd.NA
                row[f"min_low_after_signal_{horizon}d"] = pd.NA
                row[f"max_drawdown_{horizon}d"] = pd.NA

            row["status"] = "missing_price_for_code"
            rows.append(row)
            continue

        date_list = price_by_code["date"].tolist()
        base_trade_date = latest_trading_date_on_or_before(date_list, signal_date)

        row["signal_trade_date"] = base_trade_date or ""

        if not base_trade_date:
            row["signal_close"] = pd.NA
            row["pre_signal_5d_return_pct"] = pd.NA

            for horizon in HORIZONS:
                row[f"d{horizon}_close"] = pd.NA
                row[f"d{horizon}_return_pct"] = pd.NA
                row[f"max_high_after_signal_{horizon}d"] = pd.NA
                row[f"max_return_{horizon}d"] = pd.NA
                row[f"min_low_after_signal_{horizon}d"] = pd.NA
                row[f"max_drawdown_{horizon}d"] = pd.NA

            row["status"] = "missing_signal_close"
            rows.append(row)
            continue

        base_index = price_by_code.index[price_by_code["date"] == base_trade_date].tolist()[0]
        base_row = price_by_code.loc[base_index]
        signal_close = float(base_row["close"])

        row["signal_close"] = signal_close

        pre_index = base_index - 5
        if pre_index >= 0:
            pre_close = float(price_by_code.loc[pre_index, "close"])
            row["pre_signal_5d_return_pct"] = (signal_close / pre_close - 1) * 100
        else:
            row["pre_signal_5d_return_pct"] = pd.NA

        available_after = len(price_by_code) - base_index - 1

        for horizon in HORIZONS:
            target_index = base_index + horizon

            if target_index < len(price_by_code):
                close_value = float(price_by_code.loc[target_index, "close"])
                row[f"d{horizon}_close"] = close_value
                row[f"d{horizon}_return_pct"] = (close_value / signal_close - 1) * 100
            else:
                row[f"d{horizon}_close"] = pd.NA
                row[f"d{horizon}_return_pct"] = pd.NA

            window = price_by_code.iloc[base_index + 1 : base_index + horizon + 1].copy()

            if window.empty:
                row[f"max_high_after_signal_{horizon}d"] = pd.NA
                row[f"max_return_{horizon}d"] = pd.NA
                row[f"min_low_after_signal_{horizon}d"] = pd.NA
                row[f"max_drawdown_{horizon}d"] = pd.NA
            else:
                max_high = float(window["high"].max())
                min_low = float(window["low"].min())

                row[f"max_high_after_signal_{horizon}d"] = max_high
                row[f"max_return_{horizon}d"] = (max_high / signal_close - 1) * 100
                row[f"min_low_after_signal_{horizon}d"] = min_low
                row[f"max_drawdown_{horizon}d"] = (min_low / signal_close - 1) * 100

        if available_after >= 20:
            row["status"] = "complete_20d"
        elif available_after >= 10:
            row["status"] = "partial_10d"
        elif available_after >= 5:
            row["status"] = "partial_5d"
        elif available_after >= 2:
            row["status"] = "partial_2d"
        elif available_after >= 1:
            row["status"] = "partial_1d"
        else:
            row["status"] = "pending"

        rows.append(row)

    perf = pd.DataFrame(rows)
    perf = ensure_performance_columns(perf)

    sort_cols = ["signal_date", "signal_type", "threshold_group", "rank", "code"]
    existing_sort_cols = [col for col in sort_cols if col in perf.columns]

    if existing_sort_cols:
        perf = perf.sort_values(existing_sort_cols).reset_index(drop=True)

    return perf


def make_simple_table(df: pd.DataFrame, columns: list[str]) -> str:
    if df.empty:
        return "目前沒有可用資料。"

    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")

    for _, row in df.iterrows():
        values = []

        for col in columns:
            value = row.get(col, "")

            if pd.isna(value):
                values.append("-")
            elif isinstance(value, float):
                if "return" in col or "drawdown" in col or "pct" in col or "rate" in col:
                    values.append(signed_pct(value))
                else:
                    values.append(f"{value:.2f}")
            else:
                values.append(str(value))

        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


def top_return_table(perf: pd.DataFrame, return_col: str, limit: int = 20) -> pd.DataFrame:
    if perf.empty or return_col not in perf.columns:
        return pd.DataFrame()

    table = perf.dropna(subset=[return_col]).copy()

    if table.empty:
        return pd.DataFrame()

    table[return_col] = pd.to_numeric(table[return_col], errors="coerce")
    table = table.dropna(subset=[return_col])

    if table.empty:
        return pd.DataFrame()

    return table.sort_values(return_col, ascending=False).head(limit)


def make_latest_batch_summary(signals: pd.DataFrame) -> str:
    if signals.empty:
        return "目前沒有 TDCC signal。"

    latest_date = signals["signal_date"].max()
    latest = signals[signals["signal_date"] == latest_date].copy()

    table = latest[
        [
            "signal_date",
            "code",
            "name",
            "signal_type",
            "threshold_group",
            "rank",
            "current_pct",
            "previous_pct",
            "weekly_change_pct",
            "is_consecutive_2w",
            "consecutive_score",
        ]
    ].sort_values(["signal_type", "threshold_group", "rank", "code"])

    return make_simple_table(
        table.head(120),
        [
            "signal_date",
            "code",
            "name",
            "signal_type",
            "threshold_group",
            "rank",
            "current_pct",
            "previous_pct",
            "weekly_change_pct",
            "is_consecutive_2w",
            "consecutive_score",
        ],
    )


def make_return_ranking(perf: pd.DataFrame, horizon: int) -> str:
    col = f"d{horizon}_return_pct"
    table = top_return_table(perf, col, limit=20)

    if table.empty:
        return "目前沒有可用資料。"

    output_cols = [
        "signal_date",
        "code",
        "name",
        "signal_type",
        "threshold_group",
        "signal_close",
        f"d{horizon}_close",
        col,
        "status",
    ]

    return make_simple_table(table[output_cols], output_cols)


def make_four_threshold_sync_table(perf: pd.DataFrame) -> str:
    if perf.empty:
        return "目前沒有可用資料。"

    weekly = perf[
        perf["signal_type"].isin(["weekly_change_top20", "weekly_top20_current_pct"])
    ].copy()

    if weekly.empty:
        return "目前沒有四級距同步資料。"

    counts = (
        weekly.groupby(["signal_date", "code", "name"])
        .agg(
            threshold_count=("threshold_group", "nunique"),
            avg_d5_return_pct=("d5_return_pct", "mean"),
            avg_d10_return_pct=("d10_return_pct", "mean"),
            avg_d20_return_pct=("d20_return_pct", "mean"),
            max_return_20d=("max_return_20d", "max"),
            max_drawdown_20d=("max_drawdown_20d", "min"),
        )
        .reset_index()
    )

    table = counts[counts["threshold_count"] >= 4].copy()

    if table.empty:
        return "目前沒有同週四級距同步入榜股票。"

    table = table.sort_values(["signal_date", "avg_d10_return_pct"], ascending=[False, False])

    return make_simple_table(
        table.head(50),
        [
            "signal_date",
            "code",
            "name",
            "threshold_count",
            "avg_d5_return_pct",
            "avg_d10_return_pct",
            "avg_d20_return_pct",
            "max_return_20d",
            "max_drawdown_20d",
        ],
    )


def make_consecutive_performance_table(perf: pd.DataFrame) -> str:
    if perf.empty:
        return "目前沒有可用資料。"

    table = perf[perf["signal_type"] == "consecutive_2w_all_thresholds"].copy()

    if table.empty:
        return "目前沒有連續兩週四級距同步增加 signal。"

    table = table.sort_values(["signal_date", "d10_return_pct"], ascending=[False, False])

    return make_simple_table(
        table.head(50),
        [
            "signal_date",
            "code",
            "name",
            "rank",
            "consecutive_score",
            "signal_close",
            "d5_return_pct",
            "d10_return_pct",
            "d20_return_pct",
            "max_return_20d",
            "max_drawdown_20d",
            "status",
        ],
    )


def make_overheat_warnings(perf: pd.DataFrame) -> str:
    if perf.empty:
        return "目前沒有可用資料。"

    warnings = []

    if "pre_signal_5d_return_pct" in perf.columns:
        pre_hot = perf[
            pd.to_numeric(perf["pre_signal_5d_return_pct"], errors="coerce") >= 10
        ].copy()

        if not pre_hot.empty:
            pre_hot = pre_hot.sort_values("pre_signal_5d_return_pct", ascending=False).head(30)
            warnings.append("### 訊號日前 5 日漲幅過大")
            warnings.append(
                make_simple_table(
                    pre_hot,
                    [
                        "signal_date",
                        "code",
                        "name",
                        "signal_type",
                        "threshold_group",
                        "pre_signal_5d_return_pct",
                        "d5_return_pct",
                        "d10_return_pct",
                        "max_drawdown_10d",
                    ],
                )
            )

    if "d1_return_pct" in perf.columns:
        d1_black = perf[
            pd.to_numeric(perf["d1_return_pct"], errors="coerce") <= -3
        ].copy()

        if not d1_black.empty:
            d1_black = d1_black.sort_values("d1_return_pct", ascending=True).head(30)
            warnings.append("### 訊號日後隔日明顯轉弱")
            warnings.append(
                make_simple_table(
                    d1_black,
                    [
                        "signal_date",
                        "code",
                        "name",
                        "signal_type",
                        "threshold_group",
                        "d1_return_pct",
                        "d5_return_pct",
                        "max_drawdown_10d",
                        "status",
                    ],
                )
            )

    if "max_drawdown_20d" in perf.columns:
        drawdown = perf[
            pd.to_numeric(perf["max_drawdown_20d"], errors="coerce") <= -10
        ].copy()

        if not drawdown.empty:
            drawdown = drawdown.sort_values("max_drawdown_20d", ascending=True).head(30)
            warnings.append("### 訊號後最大回撤過大")
            warnings.append(
                make_simple_table(
                    drawdown,
                    [
                        "signal_date",
                        "code",
                        "name",
                        "signal_type",
                        "threshold_group",
                        "max_drawdown_5d",
                        "max_drawdown_10d",
                        "max_drawdown_20d",
                        "d20_return_pct",
                        "status",
                    ],
                )
            )

    if not warnings:
        return "目前沒有觸發過熱警示。"

    return "\n\n".join(warnings)


def summarize_group_stats(perf: pd.DataFrame, group_col: str) -> pd.DataFrame:
    if perf.empty or group_col not in perf.columns:
        return pd.DataFrame()

    df = perf.copy()

    for col in ["d5_return_pct", "d10_return_pct", "d20_return_pct"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    grouped = (
        df.groupby(group_col)
        .agg(
            signal_count=("code", "count"),
            avg_d5_return_pct=("d5_return_pct", "mean"),
            avg_d10_return_pct=("d10_return_pct", "mean"),
            avg_d20_return_pct=("d20_return_pct", "mean"),
            win_rate_d5=("d5_return_pct", lambda s: (pd.to_numeric(s, errors="coerce") > 0).mean() * 100),
            win_rate_d10=("d10_return_pct", lambda s: (pd.to_numeric(s, errors="coerce") > 0).mean() * 100),
            win_rate_d20=("d20_return_pct", lambda s: (pd.to_numeric(s, errors="coerce") > 0).mean() * 100),
        )
        .reset_index()
        .sort_values("avg_d10_return_pct", ascending=False)
    )

    return grouped


def make_statistics_summary(perf: pd.DataFrame) -> str:
    if perf.empty:
        return "目前沒有可用統計。"

    lines = []

    threshold_stats = summarize_group_stats(perf, "threshold_group")
    lines.append("### 各 threshold_group 統計")
    lines.append(
        make_simple_table(
            threshold_stats,
            [
                "threshold_group",
                "signal_count",
                "avg_d5_return_pct",
                "avg_d10_return_pct",
                "avg_d20_return_pct",
                "win_rate_d5",
                "win_rate_d10",
                "win_rate_d20",
            ],
        )
    )

    signal_type_stats = summarize_group_stats(perf, "signal_type")
    lines.append("")
    lines.append("### 各 signal_type 統計")
    lines.append(
        make_simple_table(
            signal_type_stats,
            [
                "signal_type",
                "signal_count",
                "avg_d5_return_pct",
                "avg_d10_return_pct",
                "avg_d20_return_pct",
                "win_rate_d5",
                "win_rate_d10",
                "win_rate_d20",
            ],
        )
    )

    weekly = perf[
        perf["signal_type"].isin(["weekly_change_top20", "weekly_top20_current_pct"])
    ].copy()

    if not weekly.empty:
        counts = (
            weekly.groupby(["signal_date", "code"])
            .agg(
                threshold_count=("threshold_group", "nunique"),
                avg_d5_return_pct=("d5_return_pct", "mean"),
                avg_d10_return_pct=("d10_return_pct", "mean"),
                avg_d20_return_pct=("d20_return_pct", "mean"),
            )
            .reset_index()
        )

        counts["sync_type"] = counts["threshold_count"].apply(
            lambda x: "four_threshold_sync" if x >= 4 else "single_or_partial"
        )

        sync_stats = (
            counts.groupby("sync_type")
            .agg(
                signal_count=("code", "count"),
                avg_d5_return_pct=("avg_d5_return_pct", "mean"),
                avg_d10_return_pct=("avg_d10_return_pct", "mean"),
                avg_d20_return_pct=("avg_d20_return_pct", "mean"),
            )
            .reset_index()
        )

        lines.append("")
        lines.append("### 四級距同步入榜 vs 單一/部分級距")
        lines.append(
            make_simple_table(
                sync_stats,
                [
                    "sync_type",
                    "signal_count",
                    "avg_d5_return_pct",
                    "avg_d10_return_pct",
                    "avg_d20_return_pct",
                ],
            )
        )

    consecutive = perf[perf["signal_type"] == "consecutive_2w_all_thresholds"].copy()
    non_consecutive = perf[perf["signal_type"] != "consecutive_2w_all_thresholds"].copy()

    compare_rows = []

    for label, df in [
        ("consecutive_2w_all_thresholds", consecutive),
        ("other_signals", non_consecutive),
    ]:
        if df.empty:
            continue

        compare_rows.append(
            {
                "group": label,
                "signal_count": len(df),
                "avg_d5_return_pct": pd.to_numeric(df["d5_return_pct"], errors="coerce").mean(),
                "avg_d10_return_pct": pd.to_numeric(df["d10_return_pct"], errors="coerce").mean(),
                "avg_d20_return_pct": pd.to_numeric(df["d20_return_pct"], errors="coerce").mean(),
            }
        )

    if compare_rows:
        compare_df = pd.DataFrame(compare_rows)

        lines.append("")
        lines.append("### 連續兩週同步增加 vs 其他 signal")
        lines.append(
            make_simple_table(
                compare_df,
                [
                    "group",
                    "signal_count",
                    "avg_d5_return_pct",
                    "avg_d10_return_pct",
                    "avg_d20_return_pct",
                ],
            )
        )

    return "\n\n".join(lines)


def build_markdown_report(signals: pd.DataFrame, perf: pd.DataFrame) -> str:
    latest_signal_date = signals["signal_date"].max() if not signals.empty else "無"

    lines = []
    lines.append("# TDCC 訊號績效追蹤報告")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 最新 TDCC signal 批次日期：`{latest_signal_date}`")
    lines.append(f"- signal log：`{SIGNAL_LOG_PATH}`")
    lines.append(f"- performance csv：`{PERFORMANCE_CSV_PATH}`")
    lines.append("")
    lines.append("## 1. 本週 TDCC 入榜股票清單摘要")
    lines.append("")
    lines.append(make_latest_batch_summary(signals))
    lines.append("")

    for horizon in HORIZONS:
        lines.append(f"## 2.{horizon} D+{horizon} 表現排行")
        lines.append("")
        lines.append(make_return_ranking(perf, horizon))
        lines.append("")

    lines.append("## 3. 四級距同步入榜股票的表現")
    lines.append("")
    lines.append(make_four_threshold_sync_table(perf))
    lines.append("")

    lines.append("## 4. 連續兩週四級距同步增加股票的表現")
    lines.append("")
    lines.append(make_consecutive_performance_table(perf))
    lines.append("")

    lines.append("## 5. 過熱警示")
    lines.append("")
    lines.append(make_overheat_warnings(perf))
    lines.append("")

    lines.append("## 6. 統計摘要")
    lines.append("")
    lines.append(make_statistics_summary(perf))
    lines.append("")

    lines.append("## 7. 使用說明")
    lines.append("")
    lines.append("- 這份報告只用來驗證 TDCC 週增訊號是否有後續報酬，不是直接買賣建議。")
    lines.append("- `signal_close` 使用 signal 日期當天或之前最近一個可用交易日收盤價。")
    lines.append("- D+1 / D+2 / D+5 / D+10 / D+20 使用後續第 N 個交易日收盤價。")
    lines.append("- `max_return_*d` 使用 signal 後 N 個交易日內最高價計算。")
    lines.append("- `max_drawdown_*d` 使用 signal 後 N 個交易日內最低價計算。")
    lines.append("- 若每日股價資料不足，status 會顯示 partial 或 pending。")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    ensure_dirs()

    print("Building current TDCC signals...")
    new_signals = build_current_signals()
    print(f"New signals: {len(new_signals)}")

    print("Saving signal log...")
    signal_log = save_signal_log(new_signals)
    print(f"Signal log rows: {len(signal_log)}")

    print("Loading daily price data...")
    price = load_daily_price_data()
    print(f"Daily price rows: {len(price)}")

    print("Calculating TDCC signal performance...")
    perf = calculate_signal_performance(signal_log, price)
    print(f"Performance rows: {len(perf)}")

    perf.to_csv(PERFORMANCE_CSV_PATH, index=False, encoding="utf-8-sig")

    print("Writing markdown report...")
    report = build_markdown_report(signal_log, perf)

    LATEST_REPORT_PATH.write_text(report, encoding="utf-8")
    LATEST_REPORT_COMPAT_PATH.write_text(report, encoding="utf-8")

    print(f"Signal log saved: {SIGNAL_LOG_PATH}")
    print(f"Performance CSV saved: {PERFORMANCE_CSV_PATH}")
    print(f"Markdown report saved: {LATEST_REPORT_PATH}")
    print(f"Markdown report compatibility copy saved: {LATEST_REPORT_COMPAT_PATH}")
    print("Done.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
