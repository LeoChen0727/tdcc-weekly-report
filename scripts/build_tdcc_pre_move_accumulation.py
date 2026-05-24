from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    TDCC_SIGNALS_DIR,
    append_update_csv,
    markdown_table,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


SNAPSHOT_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_snapshot.csv"
ABM_LATEST_CSV = LATEST_DIR / "tdcc_pre_move_accumulation_latest.csv"
ABM_LATEST_MD = LATEST_DIR / "tdcc_pre_move_accumulation_latest.md"
ABM_HISTORY = TDCC_SIGNALS_DIR / "tdcc_pre_move_accumulation_history.csv"


OUTPUT_COLUMNS = [
    "signal_date",
    "code",
    "name",
    "primary_theme",
    "secondary_theme",
    "abm_rank",
    "abm_score",
    "setup_type",
    "tdcc_price_phase",
    "priority_group",
    "all_threshold_streak_weeks",
    "tdcc_400_streak_weeks",
    "tdcc_600_streak_weeks",
    "tdcc_800_streak_weeks",
    "tdcc_1000_streak_weeks",
    "tdcc_800_ratio_20w_high",
    "tdcc_1000_ratio_20w_high",
    "price_return_5d",
    "price_return_10d",
    "price_return_20d",
    "price_return_60d",
    "distance_ma20_pct",
    "distance_ma60_pct",
    "distance_20d_high_pct",
    "distance_60d_high_pct",
    "price_range_20d_pct",
    "price_range_60d_pct",
    "bollinger_bandwidth_20d",
    "atr_pct_14d",
    "volume_ratio_5d",
    "volume_ratio_20d",
    "relative_ret_2w",
    "turnover_ratio",
    "is_price_not_reacted",
    "is_compression",
    "is_volume_healthy",
    "is_volume_explosive",
    "theme_breadth_score",
    "abm_reason",
    "created_at",
    "updated_at",
]


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes"}


def score_row(row: pd.Series) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    all_streak = int(to_number(row.get("all_threshold_streak_weeks"), 0) or 0)
    s800 = int(to_number(row.get("tdcc_800_streak_weeks"), 0) or 0)
    s1000 = int(to_number(row.get("tdcc_1000_streak_weeks"), 0) or 0)
    price20 = to_number(row.get("price_return_20d"))
    price5 = to_number(row.get("price_return_5d"))
    dist20 = to_number(row.get("distance_ma20_pct"))
    range20 = to_number(row.get("price_range_20d_pct"))
    vol20 = to_number(row.get("volume_ratio_20d"))
    vol5 = to_number(row.get("volume_ratio_5d"))
    breadth = to_number(row.get("theme_breadth_score"), 0)

    if all_streak >= 3:
        score += 30
        reasons.append("四級距連續三週增加")
    elif all_streak == 2:
        score += 22
        reasons.append("四級距連續兩週增加")
    elif s800 >= 2 and s1000 >= 2:
        score += 20
        reasons.append(">800/>1000 連續改善")
    elif boolish(row.get("has_400")) or boolish(row.get("has_600")):
        score += 10
        reasons.append("低級距先改善")

    if boolish(row.get("has_800")) and boolish(row.get("has_1000")):
        score += 20
        reasons.append("高級距同步改善")
    elif boolish(row.get("has_800")) or boolish(row.get("has_1000")):
        score += 12
        reasons.append("高級距單邊改善")
    elif boolish(row.get("has_400")) or boolish(row.get("has_600")):
        score += 5

    if math.isnan(price20) or price20 <= 5:
        score += 25
        reasons.append("20日股價尚未明顯反應")
    elif price20 <= 10:
        score += 20
    elif price20 <= 15:
        score += 12
    elif price20 <= 25:
        score += 5
    else:
        score -= 20
        reasons.append("20日漲幅偏大")

    above_ma20 = boolish(row.get("above_ma20"))
    if above_ma20 and (math.isnan(dist20) or dist20 <= 8):
        score += 10
    elif not math.isnan(dist20) and -3 < dist20 <= 12:
        score += 6
    elif not math.isnan(dist20) and dist20 > 20:
        score -= 10
        reasons.append("距月線過遠")

    ma60_slope = to_number(row.get("ma60_slope"))
    if not boolish(row.get("above_ma60")) and not math.isnan(ma60_slope) and ma60_slope < 0:
        score -= 10

    if not math.isnan(range20) and range20 <= 15:
        score += 10
        reasons.append("20日平台壓縮")
    elif not math.isnan(range20) and range20 <= 20:
        score += 6
    elif not math.isnan(range20) and range20 > 35:
        score -= 8

    if not math.isnan(vol20) and 1.0 <= vol20 <= 2.0:
        score += 5
    elif not math.isnan(vol20) and 0.8 <= vol20 <= 2.5:
        score += 3
    if not math.isnan(vol5) and vol5 > 3 and not math.isnan(price5) and price5 > 15:
        score -= 10
        reasons.append("短線爆量漲幅偏大")

    if breadth >= 5:
        score += 5
        reasons.append("同族群多檔同步")
    elif breadth >= 3:
        score += 3

    if not math.isnan(price5) and price5 > 25:
        score -= 25
    if not math.isnan(price20) and price20 > 30:
        score -= 30
    if not math.isnan(dist20) and dist20 > 20:
        score -= 20
    if not math.isnan(vol5) and vol5 > 4 and not math.isnan(price5) and price5 > 15:
        score -= 15

    return max(0, min(100, int(round(score)))), reasons


def setup_type(row: pd.Series, score: int) -> str:
    price5 = to_number(row.get("price_return_5d"))
    price20 = to_number(row.get("price_return_20d"))
    dist20 = to_number(row.get("distance_ma20_pct"))
    vol5 = to_number(row.get("volume_ratio_5d"))
    high_threshold = boolish(row.get("has_800")) or boolish(row.get("has_1000"))
    tdcc_cont = int(to_number(row.get("all_threshold_streak_weeks"), 0) or 0) >= 2 or (
        int(to_number(row.get("tdcc_800_streak_weeks"), 0) or 0) >= 2
        and int(to_number(row.get("tdcc_1000_streak_weeks"), 0) or 0) >= 2
    )

    if (not math.isnan(price5) and price5 > 25) or (not math.isnan(price20) and price20 > 30) or (not math.isnan(dist20) and dist20 > 20) or (not math.isnan(vol5) and vol5 > 4 and not math.isnan(price5) and price5 > 15):
        return "overheated"
    if tdcc_cont and high_threshold and (math.isnan(price20) or price20 <= 10) and (math.isnan(dist20) or dist20 <= 10) and not boolish(row.get("is_volume_explosive")):
        return "quiet_accumulation"
    if tdcc_cont and boolish(row.get("breakout_20d")) and (math.isnan(price20) or price20 <= 15) and not boolish(row.get("is_volume_explosive")):
        return "early_breakout"
    if high_threshold and not math.isnan(price20) and price20 > 15:
        return "strong_momentum"
    if score < 45:
        return "watch_only"
    return "watch_only"


def priority_group(score: int, setup: str, row: pd.Series) -> str:
    price20 = to_number(row.get("price_return_20d"))
    dist20 = to_number(row.get("distance_ma20_pct"))
    if setup == "overheated" or (not math.isnan(price20) and price20 > 30) or (not math.isnan(dist20) and dist20 > 20):
        return "Avoid/low priority"
    if score >= 75 and setup in {"quiet_accumulation", "early_breakout"} and (math.isnan(price20) or price20 <= 15):
        return "A"
    if score >= 60:
        return "B"
    if score >= 45:
        return "C"
    return "C"


def build_abm(snapshot: pd.DataFrame) -> pd.DataFrame:
    if snapshot.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    latest_date = safe_str(snapshot["signal_date"].max())
    current = snapshot[snapshot["signal_date"].astype(str) == latest_date].copy()
    rows: list[dict[str, Any]] = []
    for _, row in current.iterrows():
        score, reasons = score_row(row)
        setup = setup_type(row, score)
        out = row.to_dict()
        out["abm_score"] = score
        out["setup_type"] = setup
        out["priority_group"] = priority_group(score, setup, row)
        out["abm_reason"] = "；".join(reasons) if reasons else "條件不完整，列為觀察"
        out["updated_at"] = now_text()
        out["created_at"] = safe_str(out.get("created_at")) or now_text()
        rows.append(out)
    out_df = pd.DataFrame(rows)
    out_df = out_df.sort_values(["abm_score", "code"], ascending=[False, True]).reset_index(drop=True)
    out_df["abm_rank"] = range(1, len(out_df) + 1)
    for col in OUTPUT_COLUMNS:
        if col not in out_df.columns:
            out_df[col] = ""
    return out_df[OUTPUT_COLUMNS]


def write_markdown(df: pd.DataFrame) -> None:
    if df.empty:
        ABM_LATEST_MD.write_text("# TDCC Pre-Move Accumulation\n\nNo data.\n", encoding="utf-8")
        return
    top = df[df["setup_type"].isin(["quiet_accumulation", "early_breakout", "watch_only"])].sort_values("abm_score", ascending=False).head(20)
    active = df[df["setup_type"].isin(["strong_momentum", "overheated"])].sort_values("abm_score", ascending=False).head(30)
    theme = (
        df.groupby("primary_theme", dropna=False)
        .agg(
            quiet_accumulation_count=("setup_type", lambda s: (s == "quiet_accumulation").sum()),
            early_breakout_count=("setup_type", lambda s: (s == "early_breakout").sum()),
            overheated_count=("setup_type", lambda s: (s == "overheated").sum()),
            average_abm_score=("abm_score", "mean"),
            representative_codes=("code", lambda s: ",".join(s.astype(str).head(8))),
        )
        .reset_index()
        .sort_values(["quiet_accumulation_count", "early_breakout_count", "average_abm_score"], ascending=[False, False, False])
    )
    lines = [
        "# TDCC 潛伏吸籌候選股",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{safe_str(df['signal_date'].max())}`",
        f"- rows: `{len(df)}`",
        "",
        "## 本週潛伏吸籌候選股 Top 20",
        "",
        markdown_table(top, ["abm_rank", "code", "name", "primary_theme", "abm_score", "setup_type", "tdcc_price_phase", "all_threshold_streak_weeks", "tdcc_800_streak_weeks", "tdcc_1000_streak_weeks", "price_return_5d", "price_return_20d", "relative_ret_2w", "distance_ma20_pct", "price_range_20d_pct", "volume_ratio_20d", "abm_reason"], 20),
        "",
        "## A/B/C 分級",
        "",
        markdown_table(df.sort_values(["priority_group", "abm_score"], ascending=[True, False]), ["priority_group", "abm_rank", "code", "name", "abm_score", "setup_type", "tdcc_price_phase", "price_return_20d", "relative_ret_2w", "distance_ma20_pct", "abm_reason"], 80),
        "",
        "## 已發動 / 過熱名單",
        "",
        markdown_table(active, ["abm_rank", "code", "name", "primary_theme", "abm_score", "setup_type", "tdcc_price_phase", "price_return_5d", "price_return_20d", "relative_ret_2w", "distance_ma20_pct", "volume_ratio_5d", "abm_reason"], 30),
        "",
        "## 族群潛伏廣度",
        "",
        markdown_table(theme, ["primary_theme", "quiet_accumulation_count", "early_breakout_count", "overheated_count", "average_abm_score", "representative_codes"], 50),
        "",
        "## 解讀",
        "",
        "- TDCC Strength Ranking 找籌碼最強股，可能已經漲多。",
        "- ABM Ranking 找大戶持續增加但股價尚未充分反應的股票。",
        "- 已大漲、距月線太遠或爆量過熱者會降為 strong_momentum / overheated，不排在潛伏吸籌前段。",
    ]
    ABM_LATEST_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    snapshot = read_csv(SNAPSHOT_CSV, dtype=str)
    if snapshot.empty:
        raise FileNotFoundError(f"Missing or empty {SNAPSHOT_CSV}. Run build_tdcc_signal_structures.py first.")
    abm = build_abm(snapshot)
    write_csv(abm, ABM_LATEST_CSV)
    append_update_csv(abm, ABM_HISTORY, ["signal_date", "code"], ["signal_date", "abm_rank"])

    # Update ABM columns back to the snapshot for downstream analysis.
    update = snapshot.merge(
        abm[["signal_date", "code", "abm_rank", "abm_score", "setup_type", "priority_group", "abm_reason"]],
        on=["signal_date", "code"],
        how="left",
        suffixes=("", "_new"),
    )
    for col in ["abm_rank", "abm_score", "setup_type", "priority_group", "abm_reason"]:
        new_col = f"{col}_new"
        if new_col in update.columns:
            base = update[col] if col in update.columns else pd.Series("", index=update.index)
            new_values = update[new_col]
            update[col] = new_values.where(new_values.astype(str).str.len() > 0, base)
            update = update.drop(columns=[new_col])
    write_csv(update, SNAPSHOT_CSV)

    write_markdown(abm)
    print(f"Saved: {ABM_LATEST_CSV}")
    print(f"Saved: {ABM_LATEST_MD}")
    print(f"Saved: {ABM_HISTORY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
