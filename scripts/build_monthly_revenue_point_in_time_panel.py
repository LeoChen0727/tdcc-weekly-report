from __future__ import annotations

import math
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, normalize_code, now_text, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
HISTORY_DIR = ROOT / "output" / "history" / "research"

PANEL_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_point_in_time_panel_latest.csv"
PANEL_MD = RESEARCH_LATEST_DIR / "monthly_revenue_point_in_time_panel_latest.md"
HISTORY_CSV = HISTORY_DIR / "monthly_revenue_point_in_time_panel.csv"
DOCS_PANEL_CSV = DOCS_LATEST_DIR / PANEL_CSV.name
DOCS_PANEL_MD = DOCS_LATEST_DIR / PANEL_MD.name

PANEL_ID = "monthly_revenue_point_in_time_panel"
PANEL_VERSION = "daily_snapshot_observed_revenue_v1"
SOURCE_KIND = "daily_all_candidates_snapshot_observed_asof"

REVENUE_SOURCE_COLUMNS = [
    "stock_id",
    "stock_name",
    "latest_revenue_yoy",
    "cumulative_revenue_yoy",
    "revenue_release_date",
    "revenue_period",
    "revenue_yoy_pct",
    "cumulative_yoy_pct",
    "revenue_signal_type",
    "revenue_applicability_note",
    "revenue_good_eps_unconfirmed_flag",
]

OUTPUT_COLUMNS = [
    "generated_at",
    "panel_id",
    "panel_version",
    "source_kind",
    "stock_id",
    "stock_name",
    "revenue_period",
    "revenue_period_roc",
    "observed_as_of_date",
    "source_snapshot_date",
    "source_snapshot_files",
    "source_row_count",
    "reported_release_date_raw",
    "reported_release_date",
    "reported_release_date_status",
    "latest_revenue_yoy_pct",
    "cumulative_revenue_yoy_pct",
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_good_eps_unconfirmed_flag",
    "revenue_signal_type",
    "revenue_applicability_note",
    "revenue_numerical_anomaly_flag",
    "revenue_numerical_anomaly_reason",
    "value_conflict_flag",
    "point_in_time_status",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
    "coverage_note",
]


def rel_to_root(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    return str(value).strip()


def clean_numeric_text(value: Any) -> str:
    text = safe_str(value).replace(",", "")
    if re.fullmatch(r"-?\d+\.0", text):
        text = text[:-2]
    return text


def to_float(value: Any) -> float:
    text = clean_numeric_text(value)
    if not text:
        return math.nan
    try:
        out = float(text)
    except ValueError:
        return math.nan
    return out if math.isfinite(out) else math.nan


def first_non_empty(values: pd.Series) -> str:
    for value in values:
        text = safe_str(value)
        if text:
            return text
    return ""


def first_numeric_text(values: pd.Series) -> str:
    for value in values:
        text = clean_numeric_text(value)
        if text:
            return text
    return ""


def bool_text(value: Any) -> str:
    text = safe_str(value).lower()
    return "True" if text in {"true", "1", "yes"} else "False"


def parse_revenue_period(value: Any) -> tuple[str, str]:
    raw = clean_numeric_text(value)
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "", ""
    if len(digits) in {5, 6}:
        padded = digits.zfill(6)
        year = int(padded[:-2])
        month = int(padded[-2:])
        if year < 1911:
            year += 1911
        if 1 <= month <= 12:
            return f"{year:04d}{month:02d}", digits
    if len(digits) >= 6:
        year = int(digits[:4])
        month = int(digits[4:6])
        if year >= 1911 and 1 <= month <= 12:
            return digits[:6], digits
    return "", digits


def parse_reported_release_date(value: Any) -> tuple[str, str]:
    raw = clean_numeric_text(value)
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "", "missing"
    if len(digits) in {5, 6}:
        period, _ = parse_revenue_period(digits)
        if period:
            return "", "not_actual_release_date_year_month"
    if len(digits) == 7:
        year = int(digits[:-4])
        month = int(digits[-4:-2])
        day = int(digits[-2:])
        if year < 1911:
            year += 1911
    elif len(digits) == 8:
        year = int(digits[:4])
        month = int(digits[4:6])
        day = int(digits[6:])
    else:
        return "", "unparseable"
    try:
        return f"{year:04d}{month:02d}{day:02d}", "parsed_release_date"
    except ValueError:
        return "", "unparseable"


def revenue_flags(latest_yoy: Any, cumulative_yoy: Any) -> tuple[str, str]:
    latest = to_float(latest_yoy)
    cumulative = to_float(cumulative_yoy)
    positive = (
        (not math.isnan(latest) and latest > 0)
        or (not math.isnan(cumulative) and cumulative > 0)
    )
    strong = (
        (not math.isnan(latest) and latest >= 20)
        or (not math.isnan(cumulative) and cumulative >= 10)
    )
    return ("True" if positive else "False", "True" if strong else "False")


def anomaly_flag(latest_yoy: Any, cumulative_yoy: Any) -> tuple[str, str]:
    latest = to_float(latest_yoy)
    cumulative = to_float(cumulative_yoy)
    reasons: list[str] = []
    if not math.isnan(latest) and abs(latest) >= 300:
        reasons.append("latest_revenue_yoy_abs_ge_300pct")
    if not math.isnan(cumulative) and abs(cumulative) >= 500:
        reasons.append("cumulative_revenue_yoy_abs_ge_500pct")
    return ("True" if reasons else "False", ";".join(reasons))


def snapshot_date(path: Path) -> str:
    match = re.search(r"_(\d{8})\.csv$", path.name)
    return match.group(1) if match else ""


def read_snapshot(path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(
            path,
            dtype=str,
            keep_default_na=False,
            usecols=lambda col: col in REVENUE_SOURCE_COLUMNS,
        )
    except (OSError, ValueError, pd.errors.ParserError):
        return pd.DataFrame()
    if df.empty:
        return df
    for col in REVENUE_SOURCE_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    out = df[REVENUE_SOURCE_COLUMNS].copy()
    out["stock_id"] = out["stock_id"].map(normalize_code)
    out["source_snapshot_date"] = snapshot_date(path)
    out["source_snapshot_file"] = rel_to_root(path)
    out["latest_revenue_yoy_pct"] = out.apply(
        lambda row: first_numeric_text(pd.Series([row.get("latest_revenue_yoy"), row.get("revenue_yoy_pct")])),
        axis=1,
    )
    out["cumulative_revenue_yoy_pct"] = out.apply(
        lambda row: first_numeric_text(
            pd.Series([row.get("cumulative_revenue_yoy"), row.get("cumulative_yoy_pct")])
        ),
        axis=1,
    )
    period_pairs = out["revenue_period"].map(parse_revenue_period)
    out["revenue_period"] = period_pairs.map(lambda item: item[0])
    out["revenue_period_roc"] = period_pairs.map(lambda item: item[1])
    release_pairs = out["revenue_release_date"].map(parse_reported_release_date)
    out["reported_release_date"] = release_pairs.map(lambda item: item[0])
    out["reported_release_date_status"] = release_pairs.map(lambda item: item[1])
    out["reported_release_date_raw"] = out["revenue_release_date"].map(safe_str)
    has_revenue_value = out["latest_revenue_yoy_pct"].ne("") | out["cumulative_revenue_yoy_pct"].ne("")
    return out[out["stock_id"].ne("") & out["revenue_period"].ne("") & has_revenue_value].copy()


def conflict_flag(values: pd.Series) -> str:
    normalized = {clean_numeric_text(value) for value in values if clean_numeric_text(value)}
    return "True" if len(normalized) > 1 else "False"


def build_panel(snapshot_dir: Path = SNAPSHOT_DIR) -> pd.DataFrame:
    frames = [read_snapshot(path) for path in sorted(snapshot_dir.glob("all_candidates_*.csv"))]
    frames = [frame for frame in frames if not frame.empty]
    if not frames:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    raw = pd.concat(frames, ignore_index=True).fillna("")
    grouped = raw.groupby(["stock_id", "source_snapshot_date", "revenue_period"], dropna=False)
    rows: list[dict[str, Any]] = []
    generated_at = now_text()
    for (stock_id, source_date, revenue_period), part in grouped:
        latest = first_numeric_text(part["latest_revenue_yoy_pct"])
        cumulative = first_numeric_text(part["cumulative_revenue_yoy_pct"])
        positive, strong = revenue_flags(latest, cumulative)
        anomaly, anomaly_reason = anomaly_flag(latest, cumulative)
        release_date = first_non_empty(part["reported_release_date"])
        release_statuses = sorted({safe_str(value) for value in part["reported_release_date_status"] if safe_str(value)})
        release_status = ";".join(release_statuses)
        if release_date and release_date > source_date:
            point_status = "blocked_future_reported_release_date"
            research_allowed = "False"
        elif release_date:
            point_status = "ready_reported_release_date_confirmed"
            research_allowed = "True"
        else:
            point_status = "ready_snapshot_observed_missing_release_date"
            research_allowed = "True"
        rows.append(
            {
                "generated_at": generated_at,
                "panel_id": PANEL_ID,
                "panel_version": PANEL_VERSION,
                "source_kind": SOURCE_KIND,
                "stock_id": stock_id,
                "stock_name": first_non_empty(part["stock_name"]),
                "revenue_period": revenue_period,
                "revenue_period_roc": first_non_empty(part["revenue_period_roc"]),
                "observed_as_of_date": source_date,
                "source_snapshot_date": source_date,
                "source_snapshot_files": ";".join(sorted(set(part["source_snapshot_file"].map(safe_str)))),
                "source_row_count": int(len(part)),
                "reported_release_date_raw": ";".join(sorted({safe_str(v) for v in part["reported_release_date_raw"] if safe_str(v)})),
                "reported_release_date": release_date,
                "reported_release_date_status": release_status,
                "latest_revenue_yoy_pct": latest,
                "cumulative_revenue_yoy_pct": cumulative,
                "revenue_positive_flag": positive,
                "revenue_strong_flag": strong,
                "revenue_good_eps_unconfirmed_flag": bool_text(first_non_empty(part["revenue_good_eps_unconfirmed_flag"])),
                "revenue_signal_type": first_non_empty(part["revenue_signal_type"]),
                "revenue_applicability_note": first_non_empty(part["revenue_applicability_note"]),
                "revenue_numerical_anomaly_flag": anomaly,
                "revenue_numerical_anomaly_reason": anomaly_reason,
                "value_conflict_flag": "True"
                if conflict_flag(part["latest_revenue_yoy_pct"]) == "True"
                or conflict_flag(part["cumulative_revenue_yoy_pct"]) == "True"
                else "False",
                "point_in_time_status": point_status,
                "research_join_allowed": research_allowed,
                "allowed_for_formal_historical_model_use": "False",
                "coverage_note": (
                    "coverage_limited_to_daily_all_candidates_snapshots; observed_as_of_date is the snapshot date; "
                    "reported_release_date is not available when the source column contains only revenue year-month"
                ),
            }
        )
    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    return out.sort_values(["observed_as_of_date", "stock_id", "revenue_period"]).reset_index(drop=True)


def write_markdown(panel: pd.DataFrame) -> None:
    status_counts = (
        panel.groupby("point_in_time_status", dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values("point_in_time_status")
        if not panel.empty
        else pd.DataFrame(columns=["point_in_time_status", "rows"])
    )
    coverage = (
        panel.groupby("observed_as_of_date", dropna=False)
        .agg(rows=("stock_id", "size"), unique_stocks=("stock_id", "nunique"))
        .reset_index()
        .sort_values("observed_as_of_date")
        if not panel.empty
        else pd.DataFrame(columns=["observed_as_of_date", "rows", "unique_stocks"])
    )
    anomaly = (
        panel[panel["revenue_numerical_anomaly_flag"].astype(str).eq("True")]
        .groupby("revenue_numerical_anomaly_reason", dropna=False)
        .size()
        .reset_index(name="rows")
        if not panel.empty
        else pd.DataFrame(columns=["revenue_numerical_anomaly_reason", "rows"])
    )
    lines = [
        "# Monthly Revenue Point-In-Time Panel",
        "",
        f"- generated_at: `{now_text()}`",
        f"- panel_id: `{PANEL_ID}`",
        f"- panel_version: `{PANEL_VERSION}`",
        "- source_kind: `daily_all_candidates_snapshot_observed_asof`",
        "- status: `coverage_limited_research_only`",
        "- allowed_use: research-only as-of join when `research_join_allowed=True`.",
        "- forbidden_use: do not make revenue a formal historical model gate from this panel; `allowed_for_formal_historical_model_use` must remain `False` until a full release-date source is validated.",
        "- release_date_boundary: when the source column contains a revenue year-month such as `11505`, it is treated as period metadata, not as an actual release date.",
        "",
        "## Status Counts",
        "",
        markdown_table(status_counts, ["point_in_time_status", "rows"]) if not status_counts.empty else "No status rows.",
        "",
        "## Snapshot Coverage",
        "",
        markdown_table(coverage, ["observed_as_of_date", "rows", "unique_stocks"], limit=40)
        if not coverage.empty
        else "No coverage rows.",
        "",
        "## Numerical Anomaly Labels",
        "",
        markdown_table(anomaly, ["revenue_numerical_anomaly_reason", "rows"], limit=20)
        if not anomaly.empty
        else "No revenue numerical anomaly labels.",
        "",
        "## Sample",
        "",
        markdown_table(
            panel,
            [
                "observed_as_of_date",
                "stock_id",
                "stock_name",
                "revenue_period",
                "latest_revenue_yoy_pct",
                "cumulative_revenue_yoy_pct",
                "revenue_positive_flag",
                "revenue_strong_flag",
                "point_in_time_status",
                "allowed_for_formal_historical_model_use",
            ],
            limit=30,
        )
        if not panel.empty
        else "No panel rows.",
    ]
    PANEL_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PANEL_MD.write_text(PANEL_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    panel = build_panel()
    if panel.empty:
        raise RuntimeError("No monthly revenue rows found in daily all-candidates snapshots")
    write_csv(panel, PANEL_CSV)
    write_csv(panel, HISTORY_CSV)
    write_csv(panel, DOCS_PANEL_CSV)
    write_markdown(panel)
    print(f"Saved {PANEL_CSV} rows={len(panel)}")
    print(f"Saved {DOCS_PANEL_CSV} rows={len(panel)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
