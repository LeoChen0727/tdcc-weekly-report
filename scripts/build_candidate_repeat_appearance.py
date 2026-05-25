from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DAILY_SIGNALS_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    main_price_date_from_freshness,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    resolve_candidate_signal_date,
    safe_str,
    to_number,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
ALL_CANDIDATES_MD = LATEST_DIR / "all_candidates_latest.md"

SIGNAL_LOG = DAILY_SIGNALS_DIR / "daily_candidate_signal_log.csv"
SIGNAL_LOG_ALIAS = HISTORY_DIR / "daily_candidates" / "daily_candidate_signal_log.csv"

REPEAT_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
REPEAT_MD = LATEST_DIR / "candidate_repeat_appearance_latest.md"

REPEAT_COLUMNS = [
    "signal_date",
    "stock_id",
    "stock_name",
    "consecutive_appear_days_any_category",
    "consecutive_appear_days_same_category",
    "appear_count_5d",
    "appear_count_10d",
    "appear_count_20d",
    "first_seen_date",
    "last_seen_date",
    "multi_category_flags",
    "repeat_appear_label",
    "repeat_appear_note",
]


def truthy(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def pct_value(row: pd.Series, names: list[str]) -> float:
    for name in names:
        if name in row.index:
            num = to_number(row.get(name, ""))
            if not math.isnan(num):
                return num
    return math.nan


def read_signal_log() -> pd.DataFrame:
    log = read_csv(SIGNAL_LOG, dtype=str, keep_default_na=False)
    if log.empty:
        log = read_csv(SIGNAL_LOG_ALIAS, dtype=str, keep_default_na=False)
    if log.empty:
        return log
    for col in ["signal_date", "stock_id", "category", "stock_name"]:
        if col not in log.columns:
            log[col] = ""
    log["signal_date"] = log["signal_date"].map(normalize_date)
    log["stock_id"] = log["stock_id"].map(normalize_code)
    log["category"] = log["category"].map(safe_str)
    log["stock_name"] = log["stock_name"].map(safe_str)
    log = log[(log["signal_date"] != "") & (log["stock_id"] != "")]
    return log


def consecutive_any(stock_dates: set[str], trading_dates: list[str], main_date: str) -> int:
    if main_date not in trading_dates:
        return 0
    count = 0
    for date in reversed(trading_dates[: trading_dates.index(main_date) + 1]):
        if date in stock_dates:
            count += 1
        else:
            break
    return count


def consecutive_same_category(log: pd.DataFrame, stock_id: str, category: str, trading_dates: list[str], main_date: str) -> int:
    if main_date not in trading_dates:
        return 0
    subset = log[(log["stock_id"] == stock_id) & (log["category"] == category)]
    dates = set(subset["signal_date"].tolist())
    count = 0
    for date in reversed(trading_dates[: trading_dates.index(main_date) + 1]):
        if date in dates:
            count += 1
        else:
            break
    return count


def count_appear(stock_dates: set[str], trading_dates: list[str], main_date: str, window: int) -> int:
    if main_date not in trading_dates:
        return 0
    end = trading_dates.index(main_date) + 1
    dates = trading_dates[max(0, end - window) : end]
    return sum(1 for date in dates if date in stock_dates)


def current_rows_by_stock(candidates: pd.DataFrame) -> dict[str, pd.DataFrame]:
    out: dict[str, pd.DataFrame] = {}
    for stock_id, part in candidates.groupby("stock_id", dropna=False):
        key = normalize_code(stock_id)
        if key:
            out[key] = part.copy()
    return out


def is_breakout(rows: pd.DataFrame) -> bool:
    for _, row in rows.iterrows():
        category = safe_str(row.get("category", "")).lower()
        breakout_type = safe_str(row.get("breakout_type", "")).lower()
        if category == "true_breakout" or breakout_type == "true_breakout":
            return True
        if truthy(row.get("break_prior_high", "")) or truthy(row.get("limit_up_breakout", "")):
            return True
        if pct_value(row, ["breakout_pct"]) > 0:
            return True
    return False


def is_overheated(rows: pd.DataFrame) -> bool:
    for _, row in rows.iterrows():
        ret5 = pct_value(row, ["return_5d", "return_5d_pct"])
        ret20 = pct_value(row, ["return_20d", "return_20d_pct"])
        dist_ma20 = pct_value(row, ["distance_to_ma20_pct", "gap_ma20_pct"])
        volume_ratio = pct_value(row, ["volume_ratio"])
        if truthy(row.get("already_priced_in", "")) or truthy(row.get("catalyst_overheated", "")):
            return True
        if truthy(row.get("overheat_flag", "")):
            return True
        if (not math.isnan(ret20) and ret20 > 30) or (not math.isnan(dist_ma20) and dist_ma20 > 20):
            return True
        if not math.isnan(ret5) and not math.isnan(volume_ratio) and ret5 > 15 and volume_ratio > 3:
            return True
    return False


def is_stale(rows: pd.DataFrame, appear_count_10d: int, appear_count_20d: int, broke_out: bool) -> bool:
    if broke_out:
        return False
    if appear_count_10d < 3 and appear_count_20d < 5:
        return False
    weak_markers = 0
    for _, row in rows.iterrows():
        tdcc = " ".join(
            safe_str(row.get(col, ""))
            for col in ["tdcc_judgement", "tdcc_accumulation_signal", "tdcc_judge", "tdcc_status"]
        ).lower()
        if "distribution" in tdcc:
            weak_markers += 1
        volume_ratio = pct_value(row, ["volume_ratio"])
        if not math.isnan(volume_ratio) and volume_ratio < 0.8:
            weak_markers += 1
        ret20 = pct_value(row, ["return_20d", "return_20d_pct"])
        if not math.isnan(ret20) and ret20 < -3:
            weak_markers += 1
    return weak_markers > 0


def label_and_note(
    *,
    consecutive_any_days: int,
    appear_10d: int,
    appear_20d: int,
    first_seen: str,
    main_date: str,
    broke_out: bool,
    overheated: bool,
    stale: bool,
) -> tuple[str, str]:
    if overheated and consecutive_any_days >= 2:
        return "continued_overheated", "連續上榜但短期漲幅或乖離過熱，精華追蹤應降級。"
    if first_seen == main_date or appear_20d <= 1:
        return "first_seen", "首次上榜，屬於新訊號，需等量價、TDCC 與 benchmark 確認。"
    if stale:
        return "stale_signal", "反覆上榜但量價、TDCC 或相對強弱未改善，視為訊號鈍化。"
    if 2 <= consecutive_any_days <= 3:
        return "continued_2_3d", f"連續 {consecutive_any_days} 個交易日上榜，訊號延續但仍需確認。"
    if (appear_10d >= 3 or appear_20d >= 5) and not broke_out:
        return "repeated_but_no_breakout", f"近 10 日上榜 {appear_10d} 日、近 20 日上榜 {appear_20d} 日，尚未突破，需分辨醞釀或鈍化。"
    if consecutive_any_days >= 4:
        return "continued_many_days", f"連續 {consecutive_any_days} 個交易日上榜，需判斷是持續醞釀或訊號鈍化。"
    return "first_seen", "歷史上榜資料仍少，先當新訊號觀察。"


def build_repeat_table(log: pd.DataFrame, candidates: pd.DataFrame, main_date: str) -> pd.DataFrame:
    trading_dates = sorted(log["signal_date"].dropna().astype(str).unique().tolist())
    current = log[log["signal_date"] == main_date].copy()
    if current.empty:
        raise RuntimeError(f"daily candidate signal log does not contain main_price_date={main_date}")

    if "stock_id" not in candidates.columns:
        raise RuntimeError("all_candidates_latest.csv missing stock_id")
    candidates = candidates.copy()
    candidates["stock_id"] = candidates["stock_id"].map(normalize_code)
    current_candidates = current_rows_by_stock(candidates)

    records: list[dict[str, Any]] = []
    for stock_id, part in current.groupby("stock_id"):
        stock_dates = set(log.loc[log["stock_id"] == stock_id, "signal_date"].tolist())
        categories = sorted(set(safe_str(x) for x in part["category"].tolist() if safe_str(x)))
        same_streak = 0
        for category in categories:
            same_streak = max(same_streak, consecutive_same_category(log, stock_id, category, trading_dates, main_date))
        appear_5d = count_appear(stock_dates, trading_dates, main_date, 5)
        appear_10d = count_appear(stock_dates, trading_dates, main_date, 10)
        appear_20d = count_appear(stock_dates, trading_dates, main_date, 20)
        first_seen = min(stock_dates) if stock_dates else ""
        last_seen = max(stock_dates) if stock_dates else ""
        rows = current_candidates.get(stock_id, pd.DataFrame())
        broke_out = is_breakout(rows) if not rows.empty else False
        overheated = is_overheated(rows) if not rows.empty else False
        stale = is_stale(rows, appear_10d, appear_20d, broke_out) if not rows.empty else False
        any_streak = consecutive_any(stock_dates, trading_dates, main_date)
        label, note = label_and_note(
            consecutive_any_days=any_streak,
            appear_10d=appear_10d,
            appear_20d=appear_20d,
            first_seen=first_seen,
            main_date=main_date,
            broke_out=broke_out,
            overheated=overheated,
            stale=stale,
        )
        stock_name = safe_str(part["stock_name"].replace("", pd.NA).dropna().iloc[0]) if "stock_name" in part.columns and not part["stock_name"].replace("", pd.NA).dropna().empty else ""
        records.append(
            {
                "signal_date": main_date,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "consecutive_appear_days_any_category": any_streak,
                "consecutive_appear_days_same_category": same_streak,
                "appear_count_5d": appear_5d,
                "appear_count_10d": appear_10d,
                "appear_count_20d": appear_20d,
                "first_seen_date": first_seen,
                "last_seen_date": last_seen,
                "multi_category_flags": "|".join(categories),
                "repeat_appear_label": label,
                "repeat_appear_note": note,
            }
        )

    out = pd.DataFrame(records)
    if out.empty:
        return pd.DataFrame(columns=REPEAT_COLUMNS)
    out = out.sort_values(
        ["consecutive_appear_days_any_category", "appear_count_10d", "appear_count_20d", "stock_id"],
        ascending=[False, False, False, True],
    )
    for col in REPEAT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    return out[REPEAT_COLUMNS].reset_index(drop=True)


def write_markdown(repeat: pd.DataFrame, main_date: str, history_days: int) -> None:
    lines = [
        "# Candidate Repeat Appearance Latest",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{main_date}`",
        f"- history_available_days: `{history_days}`",
        f"- source_signal_log: `{SIGNAL_LOG.as_posix()}`",
        f"- alias_signal_log: `{SIGNAL_LOG_ALIAS.as_posix()}`",
        "",
        "## Label Rules",
        "- first_seen: 首次上榜，新訊號需確認。",
        "- continued_2_3d: 連續 2-3 個交易日上榜，訊號延續。",
        "- continued_many_days: 連續多日上榜，需判斷醞釀或鈍化。",
        "- repeated_but_no_breakout: 近 10/20 日反覆上榜但尚未突破。",
        "- continued_overheated: 連續上榜但股價已過熱，應降級。",
        "- stale_signal: 反覆上榜但量價、TDCC 或 benchmark 未改善。",
        "",
        "## Current Repeat Appearance",
        "",
    ]
    if repeat.empty:
        lines.append("_No current repeat appearance rows._")
    else:
        cols = [
            "stock_id",
            "stock_name",
            "consecutive_appear_days_any_category",
            "consecutive_appear_days_same_category",
            "appear_count_5d",
            "appear_count_10d",
            "appear_count_20d",
            "multi_category_flags",
            "repeat_appear_label",
            "repeat_appear_note",
        ]
        try:
            lines.append(repeat[cols].to_markdown(index=False))
        except Exception:
            lines.append(repeat[cols].to_csv(index=False))
    lines.append("")
    REPEAT_MD.write_text("\n".join(lines), encoding="utf-8")


def rewrite_all_candidates(candidates: pd.DataFrame, repeat: pd.DataFrame) -> pd.DataFrame:
    out = candidates.copy()
    out["stock_id"] = out["stock_id"].map(normalize_code)
    merge_cols = [col for col in REPEAT_COLUMNS if col != "stock_name"]
    for col in merge_cols:
        if col != "stock_id" and col in out.columns:
            out = out.drop(columns=[col])
    out = out.merge(repeat[merge_cols], on="stock_id", how="left")
    for col in merge_cols:
        if col not in out.columns:
            out[col] = ""
    out[merge_cols] = out[merge_cols].fillna("")
    write_csv(out, ALL_CANDIDATES)
    try:
        with pd.ExcelWriter(ALL_CANDIDATES_XLSX, engine="openpyxl") as writer:
            out.to_excel(writer, sheet_name="all_candidates", index=False)
    except Exception as exc:
        print(f"WARNING: failed to write {ALL_CANDIDATES_XLSX}: {exc}")
    try:
        ALL_CANDIDATES_MD.write_text(out.head(300).to_markdown(index=False), encoding="utf-8")
    except Exception:
        ALL_CANDIDATES_MD.write_text(out.head(300).to_csv(index=False), encoding="utf-8")
    return out


def main() -> int:
    preferred_date = main_price_date_from_freshness()
    log = read_signal_log()
    if log.empty:
        raise RuntimeError(f"missing daily candidate signal log: {SIGNAL_LOG} or {SIGNAL_LOG_ALIAS}")
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if candidates.empty:
        raise RuntimeError(f"missing or empty {ALL_CANDIDATES}")
    main_date, date_notes = resolve_candidate_signal_date(candidates, preferred_date)
    if main_date not in set(log["signal_date"].astype(str)):
        latest_log_date = max(set(log["signal_date"].astype(str))) if not log.empty else ""
        if latest_log_date:
            date_notes.append(
                f"resolved signal_date={main_date} not found in signal log; using latest signal log date={latest_log_date}"
            )
            main_date = latest_log_date
    for note in date_notes:
        print(f"WARNING: {note}")

    repeat = build_repeat_table(log, candidates, main_date)
    history_days = len(sorted(log["signal_date"].dropna().astype(str).unique().tolist()))
    write_csv(repeat, REPEAT_CSV)
    write_markdown(repeat, main_date, history_days)
    write_csv(log, SIGNAL_LOG_ALIAS)
    enriched = rewrite_all_candidates(candidates, repeat)
    print(f"Saved: {REPEAT_CSV}, rows={len(repeat)}")
    print(f"Saved: {REPEAT_MD}")
    print(f"Saved: {SIGNAL_LOG_ALIAS}, rows={len(log)}")
    print(f"Updated: {ALL_CANDIDATES}, rows={len(enriched)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
