from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from research_weekly_20pct_surge_volume import build_stock_day_frame


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")

THEME_HISTORY = Path("output/history/daily_signals/daily_theme_status_history.csv")
LATEST_THEME_STATUS = LATEST_DIR / "daily_theme_status_history_latest.csv"

OUT_CSV = LATEST_DIR / "weekly_surge_theme_segment_next_open_latest.csv"
OUT_MD = LATEST_DIR / "weekly_surge_theme_segment_next_open_latest.md"
HISTORY_CSV = HISTORY_DIR / "weekly_surge_theme_segment_next_open.csv"

WINDOWS = [5, 10, 20]
TARGET_PCT = 10.0
THRESHOLDS = [1.0, 1.2, 1.5, 2.0, 3.0]
METRICS = [
    ("start_day_volume_ratio_vs_prev20", "start_day_volume_ratio"),
    ("start_5d_avg_volume_ratio_vs_prev20", "start_5d_avg_volume_ratio"),
    ("prev_5d_avg_volume_ratio_vs_prev20", "prev_5d_avg_volume_ratio"),
]
STRICT_LABEL_TYPE = "strict_no_lookahead_history"
PROVISIONAL_LABEL_TYPE = "provisional_latest_stock_label"


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


def normalize_stock_id(value: object) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    if text.lower() in {"nan", "none", "null"}:
        return ""
    return text.strip()


def prepare_theme_tables() -> tuple[pd.DataFrame, pd.DataFrame]:
    history = read_csv(THEME_HISTORY)
    if not history.empty:
        history = history.copy()
        history["signal_date"] = history["signal_date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        history["stock_id"] = history["stock_id"].map(normalize_stock_id)
        history = history.drop_duplicates(subset=["signal_date", "stock_id"], keep="last")

    latest = read_csv(LATEST_THEME_STATUS)
    if not latest.empty:
        latest = latest.copy()
        latest["stock_id"] = latest["stock_id"].map(normalize_stock_id)
        latest = latest.drop_duplicates(subset=["stock_id"], keep="last")
    return history, latest


def attach_theme_labels(df: pd.DataFrame) -> pd.DataFrame:
    history, latest = prepare_theme_tables()
    out = df.copy()
    out["signal_date"] = out["date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
    out["stock_id"] = out["stock_id"].map(normalize_stock_id)

    if not history.empty:
        keep = [
            "signal_date",
            "stock_id",
            "theme_final_status",
            "theme_status_group",
            "theme_volume_attack_status",
            "candidate_source_type",
        ]
        strict = history[[c for c in keep if c in history.columns]].copy()
        strict = strict.rename(
            columns={
                "theme_final_status": "strict_theme_final_status",
                "theme_status_group": "strict_theme_status_group",
                "theme_volume_attack_status": "strict_theme_volume_attack_status",
                "candidate_source_type": "strict_candidate_source_type",
            }
        )
        out = out.merge(strict, how="left", on=["signal_date", "stock_id"])
    else:
        out["strict_theme_final_status"] = ""
        out["strict_theme_status_group"] = ""
        out["strict_theme_volume_attack_status"] = ""
        out["strict_candidate_source_type"] = ""

    if not latest.empty:
        keep = [
            "stock_id",
            "theme_final_status",
            "theme_status_group",
            "theme_volume_attack_status",
            "candidate_source_type",
        ]
        provisional = latest[[c for c in keep if c in latest.columns]].copy()
        provisional = provisional.rename(
            columns={
                "theme_final_status": "latest_theme_final_status",
                "theme_status_group": "latest_theme_status_group",
                "theme_volume_attack_status": "latest_theme_volume_attack_status",
                "candidate_source_type": "latest_candidate_source_type",
            }
        )
        out = out.merge(provisional, how="left", on="stock_id")
    else:
        out["latest_theme_final_status"] = ""
        out["latest_theme_status_group"] = ""
        out["latest_theme_volume_attack_status"] = ""
        out["latest_candidate_source_type"] = ""

    for col in [
        "strict_theme_status_group",
        "strict_theme_final_status",
        "strict_theme_volume_attack_status",
        "latest_theme_status_group",
        "latest_theme_final_status",
        "latest_theme_volume_attack_status",
    ]:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].fillna("").astype(str).str.strip().replace({"": "unlabeled"})
    return out


def summarize_group(
    df: pd.DataFrame,
    *,
    label_type: str,
    group_col: str,
    final_status_col: str,
    volume_attack_col: str,
    group_value: str,
    metric_col: str,
    metric_label: str,
    threshold: float,
    window: int,
) -> dict[str, object]:
    group_df = df[df[group_col] == group_value]
    picked = group_df[group_df[metric_col] >= threshold]
    hit_col = f"next_open_to_d{window}_high_10pct_hit"
    ret_col = f"next_open_to_d{window}_high_return_pct"
    hits = picked[picked[hit_col]]
    group_hits = group_df[group_df[hit_col]]
    return {
        "label_type": label_type,
        "target_window": f"D+{window}",
        "entry_basis": "D+1_open",
        "target_return_pct": TARGET_PCT,
        "theme_status_group": group_value,
        "filter_metric": metric_label,
        "filter_rule": f"{metric_label}>={threshold:g}",
        "threshold": threshold,
        "selected_stock_days": len(picked),
        "hit_stock_days": len(hits),
        "hit_rate_pct": round(len(hits) / len(picked) * 100, 2) if len(picked) else 0,
        "group_base_stock_days": len(group_df),
        "group_base_hit_days": len(group_hits),
        "group_base_hit_rate_pct": round(len(group_hits) / len(group_df) * 100, 2) if len(group_df) else 0,
        "selected_unique_stocks": picked["stock_id"].nunique(),
        "hit_unique_stocks": hits["stock_id"].nunique(),
        "median_next_open_to_high_return_pct": round(picked[ret_col].median(), 2) if len(picked) else 0,
        "avg_next_open_to_high_return_pct": round(picked[ret_col].mean(), 2) if len(picked) else 0,
        "avg_signal_close_to_next_open_gap_pct": round(picked["signal_close_to_next_open_gap_pct"].mean(), 2) if len(picked) else 0,
        "top_final_status_counts": top_counts(picked, final_status_col),
        "top_volume_attack_status_counts": top_counts(picked, volume_attack_col),
        "sample_status": sample_status(label_type, len(picked)),
    }


def sample_status(label_type: str, selected_count: int) -> str:
    if label_type == STRICT_LABEL_TYPE and selected_count < 30:
        return "insufficient_history"
    if selected_count < 30:
        return "insufficient_sample"
    if label_type == PROVISIONAL_LABEL_TYPE:
        return "provisional_latest_label_only"
    return "ok"


def top_counts(df: pd.DataFrame, col: str, limit: int = 5) -> str:
    if df.empty or col not in df.columns:
        return ""
    counts = df[col].fillna("").astype(str).replace({"": "blank"}).value_counts().head(limit)
    return "; ".join(f"{k}={v}" for k, v in counts.items())


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    label_specs = [
        (
            STRICT_LABEL_TYPE,
            "strict_theme_status_group",
            "strict_theme_final_status",
            "strict_theme_volume_attack_status",
        ),
        (
            PROVISIONAL_LABEL_TYPE,
            "latest_theme_status_group",
            "latest_theme_final_status",
            "latest_theme_volume_attack_status",
        ),
    ]
    for label_type, group_col, final_col, volume_col in label_specs:
        groups = sorted(g for g in df[group_col].dropna().astype(str).unique() if g)
        for group in groups:
            if group == "unlabeled" and label_type == STRICT_LABEL_TYPE:
                continue
            for metric_col, metric_label in METRICS:
                for threshold in THRESHOLDS:
                    for window in WINDOWS:
                        rows.append(
                            summarize_group(
                                df,
                                label_type=label_type,
                                group_col=group_col,
                                final_status_col=final_col,
                                volume_attack_col=volume_col,
                                group_value=group,
                                metric_col=metric_col,
                                metric_label=metric_label,
                                threshold=threshold,
                                window=window,
                            )
                        )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(
        ["label_type", "target_window", "hit_rate_pct", "selected_stock_days"],
        ascending=[True, True, False, False],
    ).reset_index(drop=True)


def build_markdown(summary: pd.DataFrame, df: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Weekly Surge Theme Segment Next-Open Research")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- entry_basis: D+1 open, because the signal is only known after D0 close.")
    lines.append("- target: max high from D+1 through D+5 / D+10 / D+20 reaches at least 10% above D+1 open.")
    lines.append("- strict_no_lookahead_history: joins `daily_theme_status_history.csv` on signal_date + stock_id.")
    lines.append("- provisional_latest_stock_label: exploratory only; joins the latest stock-level theme label backward and may contain look-ahead bias.")
    lines.append("- purpose: test whether mainstream/non-mainstream labels improve practical hit rate beyond volume filters.")
    lines.append("")

    total = len(df)
    lines.append("## Overall Base Hit Rates")
    lines.append("")
    lines.append("| Window | Hit Count | Base Hit Rate |")
    lines.append("|---|---:|---:|")
    for window in WINDOWS:
        hit_col = f"next_open_to_d{window}_high_10pct_hit"
        hits = int(df[hit_col].sum())
        lines.append(f"| D+{window} | {hits} | {hits / total * 100:.2f}% |")
    lines.append("")

    strict_rows = summary[summary["label_type"] == STRICT_LABEL_TYPE]
    provisional_rows = summary[summary["label_type"] == PROVISIONAL_LABEL_TYPE]
    lines.append("## Strict No-Lookahead Status")
    lines.append("")
    if strict_rows.empty or strict_rows["selected_stock_days"].max() < 30:
        lines.append("- current_status: insufficient_history")
        lines.append("- reason: daily theme status history has only started accumulating; strict historical labels are not mature enough for conclusions.")
    else:
        lines.extend(best_table(strict_rows, min_selected=30, limit=20))
    lines.append("")

    lines.append("## Provisional Exploration - Best D+10 Rows")
    lines.append("")
    d10 = provisional_rows[(provisional_rows["target_window"] == "D+10") & (provisional_rows["selected_stock_days"] >= 100)]
    lines.extend(best_table(d10, min_selected=100, limit=20))
    lines.append("")

    lines.append("## Provisional Exploration - Best D+5 Rows")
    lines.append("")
    d5 = provisional_rows[(provisional_rows["target_window"] == "D+5") & (provisional_rows["selected_stock_days"] >= 100)]
    lines.extend(best_table(d5, min_selected=100, limit=20))
    lines.append("")

    lines.append("## Provisional Group Baselines")
    lines.append("")
    baseline = (
        provisional_rows[
            (provisional_rows["filter_metric"] == "start_5d_avg_volume_ratio")
            & (provisional_rows["threshold"] == 1.0)
            & (provisional_rows["target_window"].isin(["D+5", "D+10", "D+20"]))
        ][
            [
                "target_window",
                "theme_status_group",
                "selected_stock_days",
                "hit_rate_pct",
                "group_base_hit_rate_pct",
                "sample_status",
            ]
        ]
        .sort_values(["target_window", "theme_status_group"])
    )
    lines.extend(df_to_md(baseline, limit=80))
    lines.append("")
    return "\n".join(lines) + "\n"


def best_table(df: pd.DataFrame, min_selected: int, limit: int) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    cols = [
        "target_window",
        "theme_status_group",
        "filter_metric",
        "threshold",
        "selected_stock_days",
        "hit_rate_pct",
        "median_next_open_to_high_return_pct",
        "avg_signal_close_to_next_open_gap_pct",
        "sample_status",
    ]
    best = df[df["selected_stock_days"] >= min_selected].sort_values(
        ["hit_rate_pct", "selected_stock_days"], ascending=[False, False]
    )
    return df_to_md(best[cols], limit=limit)


def df_to_md(df: pd.DataFrame, limit: int = 20) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    sub = df.head(limit)
    columns = list(sub.columns)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for _, row in sub.iterrows():
        lines.append("| " + " | ".join(clean(row.get(col, "")) for col in columns) + " |")
    return lines


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    df = build_stock_day_frame()
    if df.empty:
        raise RuntimeError("no stock day frame built")
    df = attach_theme_labels(df)
    summary = build_summary(df)
    write_csv(summary, OUT_CSV)
    write_csv(summary, HISTORY_CSV)
    OUT_MD.write_text(build_markdown(summary, df), encoding="utf-8", newline="\n")
    print(f"Saved: {OUT_CSV} rows={len(summary)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {HISTORY_CSV} rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
