from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd

from tracking_utils import LATEST_DIR, normalize_code, normalize_date, read_csv, safe_str, write_csv


THEME_EVENT_CALENDAR = Path("data/theme_events/theme_event_calendar.csv")
STOCK_THEME_TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
MODEL_SIGNALS_FOR_REPORT = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"

THEME_EVENT_WATCH_CSV = LATEST_DIR / "theme_event_watch_latest.csv"
THEME_EVENT_WATCH_MD = LATEST_DIR / "theme_event_watch_latest.md"

EMPTY_WATCH_STATUS = "no_current_theme_event_watch"

WATCH_COLUMNS = [
    "signal_date",
    "event_date",
    "event_end_date",
    "days_to_event",
    "event_phase",
    "event_name",
    "event_type",
    "theme_tag",
    "importance",
    "matched_stock_count",
    "matched_stock_ids",
    "matched_stock_names",
    "candidate_intersection_count",
    "candidate_intersection_stock_ids",
    "candidate_intersection_stock_names",
    "candidate_intersection_models",
    "top_candidate_summary_zh",
    "theme_event_watch_status",
    "pdf_section_zh",
    "interpretation_zh",
    "source_url",
]


def empty_watch_row(signal_date: str, event_count: int) -> dict[str, Any]:
    return {
        "signal_date": signal_date,
        "event_date": "",
        "event_end_date": "",
        "days_to_event": "",
        "event_phase": "empty_state",
        "event_name": "目前無可顯示主題事件",
        "event_type": "",
        "theme_tag": "",
        "importance": "",
        "matched_stock_count": 0,
        "matched_stock_ids": "",
        "matched_stock_names": "",
        "candidate_intersection_count": 0,
        "candidate_intersection_stock_ids": "",
        "candidate_intersection_stock_names": "",
        "candidate_intersection_models": "",
        "top_candidate_summary_zh": "目前無符合顯示條件的主題事件觀察列",
        "theme_event_watch_status": EMPTY_WATCH_STATUS,
        "pdf_section_zh": "主題事件觀察",
        "interpretation_zh": (
            f"theme_event_calendar 已有 {event_count} 筆資料，但目前沒有落在可顯示觀察窗或候選股交集的主題事件；"
            "PDF 僅顯示空狀態，不補造事件判斷。"
        ),
        "source_url": "",
    }


def ensure_nonempty_watch(out: pd.DataFrame, signal_date: str, event_count: int) -> pd.DataFrame:
    if out.empty and event_count > 0:
        return pd.DataFrame([empty_watch_row(signal_date, event_count)], columns=WATCH_COLUMNS)
    return out


def split_tags(value: Any) -> list[str]:
    text = safe_str(value)
    if not text:
        return []
    for sep in ["|", ",", "、", "，"]:
        text = text.replace(sep, ";")
    seen: dict[str, bool] = {}
    out: list[str] = []
    for part in text.split(";"):
        tag = safe_str(part)
        if tag and tag not in seen:
            seen[tag] = True
            out.append(tag)
    return out


def parse_day(value: Any) -> datetime | None:
    text = normalize_date(value)
    if not text:
        return None
    try:
        return datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return None


def latest_signal_date() -> str:
    for path in [MODEL_SIGNALS_FOR_REPORT, ALL_CANDIDATES]:
        df = read_csv(path, dtype=str)
        if not df.empty and "signal_date" in df.columns:
            dates = sorted({normalize_date(v) for v in df["signal_date"].dropna() if normalize_date(v)})
            if dates:
                return dates[-1]
        if not df.empty and "date" in df.columns:
            dates = sorted({normalize_date(v) for v in df["date"].dropna() if normalize_date(v)})
            if dates:
                return dates[-1]
    return datetime.now().strftime("%Y%m%d")


def event_phase(days_to_event: int) -> str:
    if days_to_event < -7:
        return "past"
    if days_to_event < 0:
        return "recent_ended"
    if days_to_event <= 7:
        return "upcoming_0_7d"
    if days_to_event <= 21:
        return "upcoming_8_21d"
    if days_to_event <= 45:
        return "upcoming_22_45d"
    return "future_logged"


def event_window_phase(base_day: datetime, event_day: datetime, event_end_day: datetime | None = None) -> tuple[int, str]:
    end_day = event_end_day or event_day
    if end_day < event_day:
        end_day = event_day
    if base_day > end_day:
        days = (end_day - base_day).days
    elif base_day < event_day:
        days = (event_day - base_day).days
    else:
        days = 0
    return days, event_phase(days)


def watch_status(phase: str, importance: str, candidate_count: int) -> str:
    if phase == "upcoming_0_7d":
        return "near_term_event_watch"
    if phase == "upcoming_8_21d":
        return "early_event_watch"
    if phase == "recent_ended":
        return "recent_event_followup"
    if phase == "upcoming_22_45d" and (importance == "high" or candidate_count > 0):
        return "early_event_watch"
    if phase == "past":
        return "past_event_archived"
    return "future_event_logged"


def row_text(row: pd.Series, columns: list[str]) -> str:
    return ";".join(safe_str(row.get(col)) for col in columns)


def taxonomy_matches(taxonomy: pd.DataFrame, tag: str) -> pd.DataFrame:
    if taxonomy.empty:
        return taxonomy
    search_cols = [
        "hot_primary_theme",
        "hot_secondary_themes",
        "primary_theme",
        "secondary_themes",
        "basic_theme",
        "concept_tags",
        "structural_theme_bucket",
        "theme_structural_status",
    ]
    existing = [col for col in search_cols if col in taxonomy.columns]
    if not existing:
        return taxonomy.iloc[0:0]
    mask = taxonomy.apply(lambda row: tag in row_text(row, existing), axis=1)
    return taxonomy[mask].copy()


def candidate_lookup() -> pd.DataFrame:
    model = read_csv(MODEL_SIGNALS_FOR_REPORT, dtype=str)
    if not model.empty:
        for col in ["stock_id", "stock_name", "model_name_zh", "model_score", "display_rank", "report_line"]:
            if col not in model.columns:
                model[col] = ""
        model["stock_id"] = model["stock_id"].map(normalize_code)
        return model
    cand = read_csv(ALL_CANDIDATES, dtype=str)
    if cand.empty:
        return pd.DataFrame(columns=["stock_id", "stock_name", "model_name_zh", "model_score", "display_rank", "report_line"])
    cand["stock_id"] = cand["stock_id"].map(normalize_code)
    cand["model_name_zh"] = cand.get("category_cn", cand.get("category", ""))
    cand["model_score"] = cand.get("model_score", cand.get("score", ""))
    cand["display_rank"] = cand.get("model_rank", cand.get("rank", ""))
    cand["report_line"] = cand.get("report_line_memberships", "")
    return cand


def summarize_candidates(rows: pd.DataFrame, limit: int = 5) -> tuple[str, str, str]:
    if rows.empty:
        return "", "", ""
    rows = rows.copy()
    if "display_rank" in rows.columns:
        rows["_rank_num"] = pd.to_numeric(rows["display_rank"], errors="coerce").fillna(999999)
    else:
        rows["_rank_num"] = 999999
    rows = rows.sort_values(["_rank_num", "stock_id"], kind="stable")
    unique = rows.drop_duplicates("stock_id", keep="first").head(limit)
    ids = ";".join(unique["stock_id"].map(safe_str))
    names = ";".join((unique["stock_id"].map(safe_str) + " " + unique["stock_name"].map(safe_str)).tolist())
    models = []
    for _, row in unique.iterrows():
        model = safe_str(row.get("model_name_zh")) or "模型欄位尚未完成"
        rank = safe_str(row.get("display_rank"))
        label = f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}:{model}"
        if rank:
            label += f"#{rank}"
        models.append(label)
    return ids, names, ";".join(models)


def write_markdown(df: pd.DataFrame) -> None:
    lines = [
        "# Theme Event Watch",
        "",
        "用途：近期事件預警 / 主題催化觀察。這是事件與族群提醒層，不是獨立買進模型；需要與價格、量能、TDCC、營收、權證與模型訊號交叉判斷。",
        "",
    ]
    if df.empty:
        lines.append("目前沒有符合視窗的主題事件。")
    else:
        display_cols = [
            "event_name",
            "event_date",
            "days_to_event",
            "theme_tag",
            "theme_event_watch_status",
            "matched_stock_count",
            "candidate_intersection_count",
            "top_candidate_summary_zh",
            "interpretation_zh",
        ]
        lines.append(df[display_cols].to_markdown(index=False))
    lines.append("")
    THEME_EVENT_WATCH_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    signal_date = latest_signal_date()
    base_day = parse_day(signal_date) or datetime.now()

    events = read_csv(THEME_EVENT_CALENDAR, dtype=str)
    taxonomy = read_csv(STOCK_THEME_TAXONOMY, dtype=str)
    candidates = candidate_lookup()

    if not taxonomy.empty:
        taxonomy["stock_id"] = taxonomy["stock_id"].map(normalize_code)
        if "stock_name" not in taxonomy.columns:
            taxonomy["stock_name"] = ""

    rows: list[dict[str, Any]] = []
    if not events.empty:
        for _, event in events.iterrows():
            event_day = parse_day(event.get("event_date"))
            if event_day is None:
                continue
            event_end_day = parse_day(event.get("event_end_date"))
            days, phase = event_window_phase(base_day, event_day, event_end_day)
            if phase in {"past", "future_logged"}:
                continue
            theme_tags = split_tags(event.get("theme_tags"))
            explicit_ids = {normalize_code(v) for v in split_tags(event.get("related_stock_ids")) if normalize_code(v)}
            for tag in theme_tags:
                matched = taxonomy_matches(taxonomy, tag)
                if explicit_ids:
                    explicit = taxonomy[taxonomy["stock_id"].isin(explicit_ids)].copy() if not taxonomy.empty else pd.DataFrame()
                    matched = pd.concat([matched, explicit], ignore_index=True, sort=False).drop_duplicates("stock_id", keep="first")
                matched_ids = set(matched["stock_id"].map(normalize_code)) if not matched.empty else set(explicit_ids)
                cand_rows = candidates[candidates["stock_id"].isin(matched_ids)].copy() if not candidates.empty and matched_ids else candidates.iloc[0:0]
                cand_ids, cand_names, cand_models = summarize_candidates(cand_rows)
                matched_names = ""
                if not matched.empty:
                    top_match = matched.drop_duplicates("stock_id", keep="first").head(20)
                    matched_names = ";".join((top_match["stock_id"].map(safe_str) + " " + top_match["stock_name"].map(safe_str)).tolist())
                status = watch_status(phase, safe_str(event.get("importance")), len(cand_rows.drop_duplicates("stock_id")) if not cand_rows.empty else 0)
                if len(matched_ids) == 0 and cand_rows.empty:
                    interpretation = "事件已建檔，但目前 taxonomy 尚未找到對應股票；需補族群標籤。"
                elif cand_rows.empty:
                    interpretation = "事件相關族群已建檔，但今日候選模型尚未出現交集；列為提前觀察。"
                else:
                    interpretation = "事件相關族群與今日候選股有交集；PDF 應列入近期事件預警 / 主題催化觀察。"
                rows.append(
                    {
                        "signal_date": signal_date,
                        "event_date": normalize_date(event.get("event_date")),
                        "event_end_date": normalize_date(event.get("event_end_date")),
                        "days_to_event": days,
                        "event_phase": phase,
                        "event_name": safe_str(event.get("event_name")),
                        "event_type": safe_str(event.get("event_type")),
                        "theme_tag": tag,
                        "importance": safe_str(event.get("importance")),
                        "matched_stock_count": len(matched_ids),
                        "matched_stock_ids": ";".join(sorted(matched_ids)),
                        "matched_stock_names": matched_names,
                        "candidate_intersection_count": len(cand_rows.drop_duplicates("stock_id")) if not cand_rows.empty else 0,
                        "candidate_intersection_stock_ids": cand_ids,
                        "candidate_intersection_stock_names": cand_names,
                        "candidate_intersection_models": cand_models,
                        "top_candidate_summary_zh": cand_models or "今日候選暫無交集",
                        "theme_event_watch_status": status,
                        "pdf_section_zh": "近期事件預警 / 主題催化觀察",
                        "interpretation_zh": interpretation,
                        "source_url": safe_str(event.get("source_url")),
                    }
                )

    out = pd.DataFrame(rows)
    for col in WATCH_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    out = out[WATCH_COLUMNS]
    out = ensure_nonempty_watch(out, signal_date, len(events))
    if not out.empty:
        out = out.sort_values(["days_to_event", "event_name", "theme_tag"], kind="stable").reset_index(drop=True)
    write_csv(out, THEME_EVENT_WATCH_CSV)
    write_markdown(out)
    print(f"Saved: {THEME_EVENT_WATCH_CSV} rows={len(out)}")
    print(f"Saved: {THEME_EVENT_WATCH_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
