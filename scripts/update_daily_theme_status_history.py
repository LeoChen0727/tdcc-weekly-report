from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
HISTORY_SIGNALS = ROOT / "output" / "history" / "daily_signals" / "daily_theme_status_history.csv"
HISTORY_CANDIDATES = ROOT / "output" / "history" / "daily_candidates" / "daily_theme_status_history.csv"
LATEST_CSV = LATEST_DIR / "daily_theme_status_history_latest.csv"
LATEST_MD = LATEST_DIR / "daily_theme_status_history_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / LATEST_CSV.name
DOCS_MD = DOCS_LATEST_DIR / LATEST_MD.name

TWO_LINE_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
VOLUME_ATTACK_STOCKS_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
VOLUME_ATTACK_THEME_CSV = LATEST_DIR / "volume_attack_theme_layer_latest.csv"
README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"

MAINSTREAM_SUPPORTED = {
    "mainstream_leader",
    "mainstream_follow_through",
    "emerging_theme",
}
NON_MAINSTREAM = {
    "single_name_signal",
    "non_mainstream_watch",
}
WEAK_OR_UNKNOWN = {
    "weak_theme",
    "neutral_or_unclear",
    "unknown",
    "",
}

OUTPUT_COLUMNS = [
    "signal_date",
    "stock_id",
    "stock_name",
    "theme_name",
    "theme_final_status",
    "theme_status_group",
    "candidate_source_type",
    "candidate_line_group",
    "candidate_line",
    "two_line_overlap_flag",
    "decision_priority",
    "decision_score",
    "tdcc_status",
    "warrant_flow_signal",
    "volume_ratio",
    "return_20d",
    "repeat_appear_label",
    "volume_breakout_type",
    "volume_breakout_priority",
    "selection_status",
    "volume_attack_bucket",
    "theme_volume_attack_status",
    "is_volume_attack_selected",
    "is_volume_attack_watch",
    "is_volume_attack_failed",
    "created_at",
    "source_files",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def read_main_price_date() -> str:
    if not README_TXT.exists():
        return ""
    for line in README_TXT.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("main_price_date="):
            return line.split("=", 1)[1].strip()
    return ""


def norm_stock_id(value: object) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    if text.lower() in {"nan", "none", "null"}:
        return ""
    return text.strip()


def choose(current: str, incoming: str) -> str:
    return current if clean(current) else clean(incoming)


def merge_source_files(current: str, incoming: str) -> str:
    items: list[str] = []
    for text in [current, incoming]:
        for item in clean(text).split(";"):
            item = item.strip()
            if item and item not in items:
                items.append(item)
    return ";".join(items)


def theme_status_group(status: str) -> str:
    value = clean(status)
    if value in MAINSTREAM_SUPPORTED:
        return "mainstream_supported"
    if value == "mainstream_overheated":
        return "mainstream_overheated"
    if value in NON_MAINSTREAM:
        return "non_mainstream"
    if value in WEAK_OR_UNKNOWN:
        return "weak_or_unknown"
    return "weak_or_unknown"


def normalize_bool(value: object) -> str:
    text = clean(value).lower()
    if text in {"true", "1", "yes", "y"}:
        return "True"
    if text in {"false", "0", "no", "n"}:
        return "False"
    return clean(value)


def row_value(row: pd.Series, column: str) -> str:
    return clean(row[column]) if column in row.index else ""


def build_rows() -> pd.DataFrame:
    main_date = read_main_price_date()
    rows: dict[tuple[str, str], dict[str, str]] = {}

    sources = [
        (TWO_LINE_CSV, "two_line"),
        (VOLUME_ATTACK_STOCKS_CSV, "volume_attack"),
    ]
    for path, source_name in sources:
        df = read_csv(path)
        if df.empty:
            continue
        for _, row in df.iterrows():
            stock_id = norm_stock_id(row_value(row, "stock_id"))
            if not stock_id:
                continue
            signal_date = row_value(row, "signal_date") or main_date
            if not signal_date:
                continue
            key = (signal_date, stock_id)
            if key not in rows:
                rows[key] = {column: "" for column in OUTPUT_COLUMNS}
                rows[key]["signal_date"] = signal_date
                rows[key]["stock_id"] = stock_id
                rows[key]["created_at"] = now_text()

            out = rows[key]
            out["stock_name"] = choose(out["stock_name"], row_value(row, "stock_name"))
            out["theme_name"] = choose(out["theme_name"], row_value(row, "theme_name") or row_value(row, "theme_group"))
            out["theme_final_status"] = choose(out["theme_final_status"], row_value(row, "theme_final_status"))
            out["candidate_source_type"] = choose(out["candidate_source_type"], row_value(row, "candidate_source_type"))
            out["candidate_line_group"] = choose(out["candidate_line_group"], row_value(row, "candidate_line_group"))
            out["candidate_line"] = choose(out["candidate_line"], row_value(row, "candidate_line"))
            out["two_line_overlap_flag"] = choose(out["two_line_overlap_flag"], normalize_bool(row_value(row, "two_line_overlap_flag")))
            out["decision_priority"] = choose(out["decision_priority"], row_value(row, "decision_priority"))
            out["decision_score"] = choose(out["decision_score"], row_value(row, "decision_score"))
            out["tdcc_status"] = choose(out["tdcc_status"], row_value(row, "tdcc_status"))
            out["warrant_flow_signal"] = choose(out["warrant_flow_signal"], row_value(row, "warrant_flow_signal"))
            out["volume_ratio"] = choose(out["volume_ratio"], row_value(row, "volume_ratio"))
            out["return_20d"] = choose(out["return_20d"], row_value(row, "return_20d"))
            out["repeat_appear_label"] = choose(out["repeat_appear_label"], row_value(row, "repeat_appear_label"))
            out["volume_breakout_type"] = choose(out["volume_breakout_type"], row_value(row, "volume_breakout_type"))
            out["volume_breakout_priority"] = choose(out["volume_breakout_priority"], row_value(row, "volume_breakout_priority"))
            out["selection_status"] = choose(out["selection_status"], row_value(row, "selection_status"))
            out["volume_attack_bucket"] = choose(out["volume_attack_bucket"], row_value(row, "volume_attack_bucket"))
            out["theme_volume_attack_status"] = choose(out["theme_volume_attack_status"], row_value(row, "theme_volume_attack_status"))
            out["is_volume_attack_selected"] = choose(out["is_volume_attack_selected"], normalize_bool(row_value(row, "is_volume_attack_selected")))
            out["is_volume_attack_watch"] = choose(out["is_volume_attack_watch"], normalize_bool(row_value(row, "is_volume_attack_watch")))
            out["is_volume_attack_failed"] = choose(out["is_volume_attack_failed"], normalize_bool(row_value(row, "is_volume_attack_failed")))
            out["source_files"] = merge_source_files(out["source_files"], f"{source_name}:{path.as_posix()}")

    out_df = pd.DataFrame(rows.values(), columns=OUTPUT_COLUMNS)
    if out_df.empty:
        return out_df
    out_df["theme_status_group"] = out_df["theme_final_status"].map(theme_status_group)
    return out_df.sort_values(["signal_date", "theme_status_group", "stock_id"]).reset_index(drop=True)


def append_history(latest: pd.DataFrame) -> pd.DataFrame:
    old = read_csv(HISTORY_SIGNALS)
    if old.empty:
        combined = latest.copy()
    else:
        for col in OUTPUT_COLUMNS:
            if col not in old.columns:
                old[col] = ""
        combined = pd.concat([old[OUTPUT_COLUMNS], latest[OUTPUT_COLUMNS]], ignore_index=True)
        combined = combined.drop_duplicates(subset=["signal_date", "stock_id"], keep="last")
    if not combined.empty:
        combined = combined.sort_values(["signal_date", "theme_status_group", "stock_id"]).reset_index(drop=True)
    return combined


def md_table(df: pd.DataFrame, columns: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    subset = df.head(limit)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for _, row in subset.iterrows():
        values = [clean(row.get(col, "")).replace("\n", " ") for col in columns]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def counts_table(df: pd.DataFrame, column: str) -> list[str]:
    if df.empty or column not in df.columns:
        return ["_No rows._"]
    counts = df[column].fillna("").astype(str).replace({"": "blank"}).value_counts().reset_index()
    counts.columns = [column, "count"]
    return md_table(counts, [column, "count"], limit=50)


def write_markdown(latest: pd.DataFrame, history: pd.DataFrame) -> None:
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    latest_date = latest["signal_date"].max() if not latest.empty else ""
    lines: list[str] = []
    lines.append("# Daily Theme Status History")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- latest_signal_date: `{latest_date}`")
    lines.append(f"- latest_rows: `{len(latest)}`")
    lines.append(f"- history_rows: `{len(history)}`")
    lines.append("- purpose: Persist stock-level mainstream/non-mainstream and volume-attack labels by signal date for no-lookahead backtests.")
    lines.append("- caveat: Historical rows begin when this tracker starts unless older snapshots are backfilled from archived artifacts.")
    lines.append("")
    lines.append("## Theme Status Group Counts")
    lines.extend(counts_table(latest, "theme_status_group"))
    lines.append("")
    lines.append("## Theme Final Status Counts")
    lines.extend(counts_table(latest, "theme_final_status"))
    lines.append("")
    lines.append("## Volume Attack Theme Status Counts")
    lines.extend(counts_table(latest, "theme_volume_attack_status"))
    lines.append("")
    lines.append("## Latest Stock-Level Rows")
    lines.extend(
        md_table(
            latest,
            [
                "signal_date",
                "stock_id",
                "stock_name",
                "theme_name",
                "theme_final_status",
                "theme_status_group",
                "theme_volume_attack_status",
                "candidate_source_type",
                "decision_priority",
                "volume_breakout_type",
                "selection_status",
            ],
            limit=40,
        )
    )
    lines.append("")
    text = "\n".join(lines) + "\n"
    LATEST_MD.write_text(text, encoding="utf-8", newline="\n")
    DOCS_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    latest = build_rows()
    if latest.empty:
        print("No daily theme status rows built; source files missing or empty.")
        latest = pd.DataFrame(columns=OUTPUT_COLUMNS)
    history = append_history(latest)
    write_csv(latest, LATEST_CSV)
    write_csv(history, HISTORY_SIGNALS)
    write_csv(history, HISTORY_CANDIDATES)
    DOCS_CSV.parent.mkdir(parents=True, exist_ok=True)
    write_csv(latest, DOCS_CSV)
    write_markdown(latest, history)
    print(f"Saved: {LATEST_CSV} rows={len(latest)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {HISTORY_SIGNALS} rows={len(history)}")
    print(f"Saved: {HISTORY_CANDIDATES} rows={len(history)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
