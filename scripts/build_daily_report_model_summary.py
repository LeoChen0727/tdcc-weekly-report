from __future__ import annotations

from pathlib import Path
import math
import re

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

PARAMETERS_CSV = LATEST_DIR / "daily_candidate_model_parameters_latest.csv"
REPORT_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"

REGISTRY_CSV = LATEST_DIR / "daily_report_model_registry_latest.csv"
REGISTRY_MD = LATEST_DIR / "daily_report_model_registry_latest.md"
SUMMARY_CSV = LATEST_DIR / "daily_candidate_model_summary_for_report_latest.csv"
SUMMARY_MD = LATEST_DIR / "daily_candidate_model_summary_for_report_latest.md"


REPORT_LINES = ("mainstream", "non_mainstream")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, encoding="utf-8-sig").fillna("")


def write_csv_md(df: pd.DataFrame, csv_path: Path, md_path: Path, title: str) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    lines = [f"# {title}", ""]
    if df.empty:
        lines.append("資料不足 / 僅能觀察。")
    else:
        try:
            lines.append(df.to_markdown(index=False))
        except Exception:
            lines.append(df.to_string(index=False))
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def safe_str(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and math.isnan(value):
        return ""
    text = str(value).strip()
    if text.lower() in {"nan", "none", "null"}:
        return ""
    return text


def to_number(value: object, default: float = math.inf) -> float:
    text = safe_str(value)
    if not text:
        return default
    text = re.sub(r"[^0-9.\-]", "", text)
    if not text:
        return default
    try:
        return float(text)
    except Exception:
        return default


def fmt_score(value: object) -> str:
    num = to_number(value, default=math.nan)
    if math.isnan(num):
        return "-"
    text = f"{num:.2f}".rstrip("0").rstrip(".")
    return text or "-"


def infer_group(model_id: str, model_name: str) -> str:
    text = f"{model_id} {model_name}".lower()
    if "tdcc" in text or "籌碼" in model_name:
        return "籌碼"
    if "short" in text or "短線" in model_name or "d+5" in text or "d+10" in text:
        return "短線"
    if "breakout" in text or "突破" in model_name:
        return "突破"
    if "pullback" in text or "回檔" in model_name:
        return "回檔"
    if "w_bottom" in text or "platform" in text or "neckline" in text or "w底" in model_name or "平台" in model_name or "頸線" in model_name:
        return "型態"
    if "theme" in text or "族群" in model_name:
        return "族群"
    if "revenue" in text or "營收" in model_name:
        return "基本面"
    return "綜合"


def build_registry(parameters: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    if parameters.empty:
        return pd.DataFrame(
            columns=[
                "model_id",
                "model_name_zh",
                "model_registry_order",
                "model_registry_active",
                "report_line_applicability",
                "model_group_zh",
                "model_description_zh",
            ]
        )

    work = parameters.copy()
    if "pdf_visibility" in work.columns:
        visibility = work["pdf_visibility"].astype(str).str.strip().str.lower()
        work = work[visibility.isin({"pdf_core_model", "pdf_specialty_section"})].copy()

    for idx, row in work.reset_index(drop=True).iterrows():
        model_id = safe_str(row.get("model_id"))
        model_name = safe_str(row.get("model_name_zh")) or model_id
        if not model_id:
            continue
        description = (
            safe_str(row.get("main_conditions"))
            or safe_str(row.get("operation_guidance"))
            or "依程式端模型條件選出。"
        )
        rows.append(
            {
                "model_id": model_id,
                "model_name_zh": model_name,
                "model_registry_order": idx + 1,
                "model_registry_active": True,
                "report_line_applicability": safe_str(row.get("report_line_applicability")) or "both",
                "model_group_zh": infer_group(model_id, model_name),
                "model_description_zh": description,
            }
        )
    return pd.DataFrame(rows)


def applicable(reg_row: pd.Series, report_line: str) -> bool:
    value = safe_str(reg_row.get("report_line_applicability")).lower()
    if not value or value == "both":
        return True
    parts = {part.strip() for part in re.split(r"[|,;/]", value) if part.strip()}
    return report_line in parts


def sort_candidates(df: pd.DataFrame, rank_col: str) -> pd.DataFrame:
    if df.empty:
        return df
    work = df.copy()
    work["_rank_key"] = work.get(rank_col, "").map(lambda x: to_number(x, default=math.inf))
    work["_overall_rank_key"] = work.get("model_rank_overall", work.get("model_rank", "")).map(lambda x: to_number(x, default=math.inf))
    work["_score_key"] = work.get("model_score", "").map(lambda x: to_number(x, default=-math.inf))
    return work.sort_values(["_rank_key", "_overall_rank_key", "_score_key"], ascending=[True, True, False])


def top_row(signals: pd.DataFrame, model_id: str, report_line: str, repeated: bool) -> pd.Series | None:
    if signals.empty:
        return None
    work = signals[
        signals.get("report_line", "").astype(str).str.strip().eq(report_line)
        & signals.get("model_id", "").astype(str).str.strip().eq(model_id)
    ].copy()
    if work.empty:
        return None

    status = work.get("same_model_repeat_status", pd.Series("", index=work.index)).astype(str).str.strip()
    if repeated:
        work = work[status.ne("new_model_signal") & status.ne("")]
        rank_col = "model_rank_repeated_signal"
    else:
        work = work[status.eq("new_model_signal")]
        rank_col = "model_rank_new_signal"
    if work.empty:
        return None
    return sort_candidates(work, rank_col).iloc[0]


def first_available(row: pd.Series | None, keys: list[str]) -> str:
    if row is None:
        return ""
    for key in keys:
        value = safe_str(row.get(key))
        if value:
            return value
    return ""


def stock_display(row: pd.Series | None) -> str:
    if row is None:
        return "今日無候選"
    sid = safe_str(row.get("stock_id"))
    name = safe_str(row.get("stock_name"))
    return f"{sid} {name}".strip() or "今日無候選"


def rank_number(row: pd.Series | None, keys: list[str]) -> str:
    value = first_available(row, keys)
    num = to_number(value, default=math.nan)
    if math.isnan(num):
        return ""
    return str(int(num)) if float(num).is_integer() else f"{num:.2f}".rstrip("0").rstrip(".")


def reminder(new_row: pd.Series | None, repeated_row: pd.Series | None) -> str:
    for row in (new_row, repeated_row):
        value = first_available(
            row,
            [
                "operation_reminder_zh",
                "next_confirmation_zh",
                "recommended_usage_zh",
                "risk_tags_zh",
                "why_selected_human_zh",
                "why_selected_zh",
            ],
        )
        if value:
            return value
    return "-"


def infer_signal_date(signals: pd.DataFrame) -> str:
    if signals.empty or "signal_date" not in signals.columns:
        return ""
    dates = sorted({safe_str(value) for value in signals["signal_date"].tolist() if safe_str(value)})
    return dates[0] if len(dates) == 1 else ""


def build_summary(registry: pd.DataFrame, signals: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    signal_date = infer_signal_date(signals)
    for report_line in REPORT_LINES:
        for _, reg in registry.sort_values("model_registry_order").iterrows():
            if not applicable(reg, report_line):
                continue
            model_id = safe_str(reg.get("model_id"))
            new = top_row(signals, model_id, report_line, repeated=False)
            repeated = top_row(signals, model_id, report_line, repeated=True)
            new_rank_num = rank_number(new, ["model_rank_new_signal", "display_rank_new_signal", "model_rank_overall", "model_rank"])
            repeated_rank_num = rank_number(repeated, ["model_rank_repeated_signal", "display_rank_repeated_signal", "model_rank_overall", "model_rank"])
            new_rank_label = f"新進榜 #{new_rank_num}" if new_rank_num else "-"
            repeated_rank_label = f"連續榜 #{repeated_rank_num}" if repeated_rank_num else "-"
            new_score = fmt_score(first_available(new, ["model_score"]))
            repeated_score = fmt_score(first_available(repeated, ["model_score"]))
            new_display = stock_display(new)
            repeated_display = stock_display(repeated)
            rows.append(
                {
                    "signal_date": signal_date,
                    "report_line": report_line,
                    "model_id": model_id,
                    "model_name_zh": safe_str(reg.get("model_name_zh")),
                    "model_registry_order": reg.get("model_registry_order"),
                    "model_group_zh": safe_str(reg.get("model_group_zh")),
                    "model_description_zh": safe_str(reg.get("model_description_zh")),
                    "new_signal_stock_display": new_display,
                    "new_stock_display": new_display,
                    "new_stock_id": first_available(new, ["stock_id"]),
                    "new_stock_name": first_available(new, ["stock_name"]),
                    "new_signal_model_score": new_score,
                    "new_model_score": new_score,
                    "new_signal_rank_label_zh": new_rank_label,
                    "new_rank_label": new_rank_label,
                    "display_rank_new_signal": new_rank_num or "-",
                    "model_rank_new_signal": new_rank_num or "-",
                    "new_model_rank_new_signal": new_rank_num or "-",
                    "repeated_signal_stock_display": repeated_display,
                    "repeated_stock_display": repeated_display,
                    "repeated_stock_id": first_available(repeated, ["stock_id"]),
                    "repeated_stock_name": first_available(repeated, ["stock_name"]),
                    "repeated_signal_model_score": repeated_score,
                    "repeated_model_score": repeated_score,
                    "repeated_signal_rank_label_zh": repeated_rank_label,
                    "repeated_rank_label": repeated_rank_label,
                    "display_rank_repeated_signal": repeated_rank_num or "-",
                    "model_rank_repeated_signal": repeated_rank_num or "-",
                    "repeated_model_rank_repeated_signal": repeated_rank_num or "-",
                    "operation_reminder_zh": reminder(new, repeated),
                }
            )
    return pd.DataFrame(rows)


def copy_to_docs(paths: list[Path]) -> None:
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    for path in paths:
        if path.exists():
            target = DOCS_LATEST_DIR / path.name
            target.write_bytes(path.read_bytes())


def main() -> None:
    parameters = read_csv(PARAMETERS_CSV)
    signals = read_csv(REPORT_SIGNALS_CSV)
    registry = build_registry(parameters)
    summary = build_summary(registry, signals)
    write_csv_md(registry, REGISTRY_CSV, REGISTRY_MD, "Daily Report Model Registry")
    write_csv_md(summary, SUMMARY_CSV, SUMMARY_MD, "Daily Candidate Model Summary For Report")
    copy_to_docs([REGISTRY_CSV, REGISTRY_MD, SUMMARY_CSV, SUMMARY_MD])
    print(f"Saved: {REGISTRY_CSV} rows={len(registry)}")
    print(f"Saved: {SUMMARY_CSV} rows={len(summary)}")


if __name__ == "__main__":
    main()
