from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import json
import re
import shutil

import pandas as pd
from pypdf import PdfReader


LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
REPEAT_APPEARANCE_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
REPEAT_APPEARANCE_MD = LATEST_DIR / "candidate_repeat_appearance_latest.md"
NON_REVENUE_MOMENTUM_CSV = LATEST_DIR / "non_revenue_momentum_watch_latest.csv"
PDF_MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"

CURATED_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"
MODEL_SUMMARY_CSV = LATEST_DIR / "daily_candidate_model_summary_for_report_latest.csv"
MODEL_REPORT_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
TECHNICAL_SNAPSHOT_CSV = LATEST_DIR / "individual_stock_technical_snapshot_latest.csv"
MODEL_LINE_PDFS = {
    "mainstream_highlight": LATEST_DIR / "mainstream_daily_recommendation_highlight_latest.pdf",
    "mainstream_full": LATEST_DIR / "mainstream_full_candidate_list_latest.pdf",
    "non_mainstream_highlight": LATEST_DIR / "non_mainstream_daily_recommendation_highlight_latest.pdf",
    "non_mainstream_full": LATEST_DIR / "non_mainstream_full_candidate_list_latest.pdf",
}
VALIDATION_JSON = LATEST_DIR / "daily_market_report_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_market_report_validation_latest.md"
DOCS_VALIDATION_MD = DOCS_LATEST_DIR / "daily_market_report_validation_latest.md"

MIN_PDF_SIZE_BYTES_BY_LABEL = {
    "curated": 10_000,
    "full_table": 25_000,
}
MAX_REASONABLE_PAGES = 120

CURATED_REQUIRED_SECTIONS = [
    "今日市場結論",
    "Market Background and Warrant Summary",
    "財報 / 事件催化觀察",
    "今日優先追蹤",
    "分類解讀",
    "風險提醒",
    "明日觀察",
]

FULL_REQUIRED_SECTIONS = [
    "Market Background and Warrant Summary",
    "族群性分析 / 今日族群輪動",
    "族群矩陣",
    "各分類清單",
]

CATEGORY_ORDER = [
    "嚴格突破",
    "區間內轉強 / 挑戰前高觀察",
    "營收爆發低反應股",
    "營收成長股價回檔",
    "回檔後短線轉強",
    "型態觀察",
]

FORBIDDEN_TERMS = [
    "持股",
    "成本",
    "損益",
    "融資",
    "張",
    "個人部位",
    "我的持股",
]

DEBUG_TERMS = [
    "READ_ME_FIRST",
    "preferred_chatgpt_url",
    "fallback url",
    "packet 解析",
    "規則檔讀取",
    "cache miss",
    "Cache miss",
    "GitHub API",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat"}:
        return ""
    return text


def normalize_date_value(value: Any) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) >= 8:
        return digits[:8]
    return ""


def read_freshness() -> dict[str, str]:
    if not DATA_FRESHNESS_CSV.exists():
        return {}
    try:
        df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str).fillna("")
        if not df.empty:
            return {str(k): safe_str(v) for k, v in df.iloc[0].to_dict().items()}
    except Exception:
        return {}
    return {}


def read_manifest() -> dict[str, Any]:
    if not PDF_MANIFEST_JSON.exists():
        return {}
    try:
        data = json.loads(PDF_MANIFEST_JSON.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    return {}


def pdf_info(path: Path) -> dict[str, Any]:
    info = {
        "path": path.as_posix(),
        "exists": path.exists(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
        "pages": 0,
        "text": "",
        "read_error": "",
    }
    if not path.exists():
        return info
    try:
        reader = PdfReader(str(path))
        info["pages"] = len(reader.pages)
        texts: list[str] = []
        for page in reader.pages:
            try:
                texts.append(page.extract_text() or "")
            except Exception:
                texts.append("")
        info["text"] = "\n".join(texts)
    except Exception as exc:
        info["read_error"] = str(exc)
    return info


def normalize_for_search(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def check_pdf_basic(label: str, info: dict[str, Any], errors: list[str], warnings: list[str]) -> None:
    if not info["exists"]:
        errors.append(f"{label}: PDF does not exist: {info['path']}")
        return
    min_size = MIN_PDF_SIZE_BYTES_BY_LABEL.get(label, 10_000)
    if info["size_bytes"] < min_size:
        errors.append(f"{label}: PDF size too small: {info['size_bytes']}")
    if info["pages"] < 1:
        errors.append(f"{label}: PDF page count is zero")
    if info["pages"] > MAX_REASONABLE_PAGES:
        warnings.append(f"{label}: PDF page count is high: {info['pages']}")
    if info["read_error"]:
        errors.append(f"{label}: PDF read error: {info['read_error']}")
    if len(normalize_for_search(info["text"])) < 100:
        errors.append(f"{label}: extracted PDF text is too short for validation")


def check_required_sections(label: str, text: str, sections: list[str], errors: list[str]) -> None:
    compact = normalize_for_search(text)
    for section in sections:
        if normalize_for_search(section) not in compact:
            errors.append(f"{label}: missing required section: {section}")


def check_forbidden_terms(label: str, text: str, errors: list[str]) -> None:
    compact = normalize_for_search(text)
    for term in FORBIDDEN_TERMS:
        if normalize_for_search(term) in compact:
            errors.append(f"{label}: forbidden term appears in formal PDF text: {term}")
    for term in DEBUG_TERMS:
        if normalize_for_search(term) in compact:
            errors.append(f"{label}: debug/read-flow term appears in formal PDF text: {term}")


def check_duplicate_rank_labels(label: str, text: str, errors: list[str]) -> None:
    compact = normalize_for_search(text)
    duplicated_patterns = [
        "新進榜#新進榜",
        "新進榜新進榜",
        "連續榜#連續榜",
        "連續榜連續榜",
        "累計榜#累計榜",
        "累計榜累計榜",
        "重複進榜#重複進榜",
        "重複進榜重複進榜",
    ]
    for pattern in duplicated_patterns:
        if normalize_for_search(pattern) in compact:
            errors.append(f"{label}: duplicate rank label appears in PDF text: {pattern}")


def check_raw_slug_terms(label: str, text: str, errors: list[str]) -> None:
    raw_terms = [
        "call_strong_inflow",
        "call_put_bullish",
        "call_inflow",
        "mixed_flow",
        "no_signal",
        "range_rebound",
        "revenue_pullback",
        "revenue_breakout_low_response",
        "pullback_rebound",
        "short_term_specialty",
        "mild_accumulation",
        "strong_accumulation",
        "tdcc_short_term_edge",
        "hot_theme_pullback",
        "non_mainstream",
        "mainstream",
        "insufficient_data",
        "neckline",
    ]
    compact = normalize_for_search(text)
    for term in raw_terms:
        if normalize_for_search(term) in compact:
            errors.append(f"{label}: raw slug appears in formal PDF text: {term}")


def check_category_order(label: str, text: str, errors: list[str]) -> None:
    order_line_match = re.search(r"分類順序[:：]\s*(.+)", text)
    if order_line_match:
        order_line = order_line_match.group(1)
        positions = [(category, order_line.find(category)) for category in CATEGORY_ORDER]
        missing = [category for category, pos in positions if pos < 0]
        if missing:
            for category in missing:
                errors.append(f"{label}: missing category in order line: {category}")
            return
        actual = [category for category, _ in sorted(positions, key=lambda item: item[1])]
        if actual != CATEGORY_ORDER:
            errors.append(f"{label}: category order is wrong: {actual}")
        return

    start_marker = "各分類清單" if label == "full_table" else "分類解讀"
    start_pos = normalize_for_search(text).find(normalize_for_search(start_marker))
    if start_pos >= 0:
        # Map the marker back approximately by searching the raw marker too.  The
        # order check must use line boundaries; compact text also contains
        # category names inside table cells and reason text.
        raw_start = text.find(start_marker)
        if raw_start >= 0:
            text = text[raw_start:]

    positions: list[tuple[str, int]] = []
    for category in CATEGORY_ORDER:
        pattern = re.compile(rf"(?m)^\s*{re.escape(category)}\s*$")
        match = pattern.search(text)
        pos = match.start() if match else -1
        if pos < 0:
            errors.append(f"{label}: missing category heading: {category}")
        else:
            positions.append((category, pos))
    if len(positions) == len(CATEGORY_ORDER):
        sorted_positions = sorted(positions, key=lambda item: item[1])
        actual = [item[0] for item in sorted_positions]
        if actual != CATEGORY_ORDER:
            errors.append(f"{label}: category order is wrong: {actual}")


def check_no_total_ranking(label: str, text: str, errors: list[str]) -> None:
    compact = normalize_for_search(text)
    bad_phrases = [
        "total ranking",
        "overall ranking",
        "overall rank",
        "single total ranking",
        "總排名",
        "綜合總排名",
        "全部候選股總排名",
    ]
    for phrase in bad_phrases:
        if normalize_for_search(phrase) in compact:
            errors.append(f"{label}: appears to mix categories into a total ranking: {phrase}")


def check_score_rank_priority(label: str, text: str, errors: list[str]) -> None:
    compact = normalize_for_search(text)
    required_any = ["分數/排名/priority", "分數/排名", "score"]
    if not any(normalize_for_search(item) in compact for item in required_any):
        errors.append(f"{label}: missing score/rank/priority wording")


def check_report_date(label: str, text: str, main_date: str, errors: list[str]) -> None:
    if main_date and main_date not in text:
        errors.append(f"{label}: main_price_date {main_date} not found in PDF text")


def check_candidate_date(errors: list[str], main_date: str) -> None:
    if not ALL_CANDIDATES_CSV.exists():
        errors.append(f"missing {ALL_CANDIDATES_CSV}")
        return
    try:
        df = pd.read_csv(ALL_CANDIDATES_CSV, dtype=str, keep_default_na=False).fillna("")
        authoritative_cols = [
            col
            for col in ["main_price_date", "signal_date", "date", "price_date", "trade_date"]
            if col in df.columns
        ]
        if not authoritative_cols:
            errors.append("all_candidates missing authoritative date columns: main_price_date/signal_date/date")
            return
        date_sets: dict[str, list[str]] = {}
        for col in authoritative_cols:
            values = sorted({normalize_date_value(value) for value in df[col].tolist()} - {""})
            date_sets[col] = values
        if main_date and not any(main_date in values for values in date_sets.values()):
            errors.append(
                f"all_candidates authoritative dates do not contain main_price_date {main_date}; "
                f"date_sets={date_sets}"
            )
        if main_date:
            for col, values in date_sets.items():
                bad_values = [value for value in values if value != main_date]
                if bad_values:
                    errors.append(f"all_candidates {col} contains non-current dates: {bad_values[:10]}")
            if "source_date" in df.columns:
                source_values = sorted({normalize_date_value(value) for value in df["source_date"].tolist()} - {""})
                bad_source_values = [value for value in source_values if value != main_date]
                if bad_source_values:
                    examples = (
                        df[df["source_date"].map(normalize_date_value).isin(bad_source_values)]
                        [["stock_id", "stock_name", "category", "source_date"]]
                        .head(10)
                        .to_dict("records")
                    )
                    errors.append(
                        f"all_candidates source_date contains stale dates: {bad_source_values[:10]} examples={examples}"
                    )
    except Exception as exc:
        errors.append(f"failed to inspect all_candidates date: {exc}")


def check_technical_snapshot_date(errors: list[str], main_date: str) -> None:
    if not TECHNICAL_SNAPSHOT_CSV.exists():
        errors.append(f"missing {TECHNICAL_SNAPSHOT_CSV}")
        return
    if not main_date:
        return
    try:
        df = pd.read_csv(TECHNICAL_SNAPSHOT_CSV, dtype=str, keep_default_na=False).fillna("")
    except Exception as exc:
        errors.append(f"failed to inspect technical snapshot date: {exc}")
        return
    if "signal_date" not in df.columns:
        errors.append("technical snapshot missing signal_date")
        return
    values = sorted({normalize_date_value(value) for value in df["signal_date"].tolist()} - {""})
    bad_values = [value for value in values if value != main_date]
    if bad_values:
        examples = (
            df[df["signal_date"].map(normalize_date_value).isin(bad_values)]
            [["stock_id", "stock_name", "signal_date"]]
            .head(10)
            .to_dict("records")
        )
        errors.append(f"technical snapshot contains non-current signal_date: {bad_values[:10]} examples={examples}")


def check_catalyst_columns(errors: list[str]) -> None:
    if not ALL_CANDIDATES_CSV.exists():
        return
    required = {
        "theme_strength_score",
        "catalyst_strength_score",
        "catalyst_tags",
        "fundamental_catalyst_score",
        "fundamental_catalyst_tags",
        "event_catalyst_tags",
        "price_reaction_level",
        "similar_to_shihsinko_flag",
        "revenue_good_eps_unconfirmed_flag",
        "catalyst_summary",
        "already_reacted_to_catalyst",
        "low_reaction_after_catalyst",
        "catalyst_quality",
        "catalyst_confidence",
    }
    try:
        df = pd.read_csv(ALL_CANDIDATES_CSV, dtype=str, keep_default_na=False)
    except Exception as exc:
        errors.append(f"failed to inspect catalyst columns: {exc}")
        return
    missing = required - set(df.columns)
    if missing:
        errors.append(f"all_candidates missing catalyst columns: {sorted(missing)}")
        return
    similar = df[df["similar_to_shihsinko_flag"].astype(str).str.lower().isin(["true", "1", "yes"])]
    if similar.empty:
        return
    if "already_reacted_to_catalyst" in similar.columns:
        bad = similar[similar["already_reacted_to_catalyst"].astype(str).str.lower().isin(["true", "1", "yes"])]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes already_reacted_to_catalyst rows")
    if "is_construction_recognition" in similar.columns:
        bad = similar[similar["is_construction_recognition"].astype(str).str.lower().isin(["true", "1", "yes"])]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes construction recognition rows")
    tdcc_cols = [col for col in ["tdcc_accumulation_signal", "tdcc_judgement"] if col in similar.columns]
    for col in tdcc_cols:
        bad = similar[similar[col].astype(str).str.contains("distribution_warning", case=False, na=False)]
        if not bad.empty:
            errors.append("similar_to_shihsinko_flag includes distribution_warning rows")


def check_repeat_appearance_columns(errors: list[str]) -> None:
    required = {
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
    }
    if not REPEAT_APPEARANCE_CSV.exists():
        errors.append(f"missing {REPEAT_APPEARANCE_CSV}")
    if not REPEAT_APPEARANCE_MD.exists():
        errors.append(f"missing {REPEAT_APPEARANCE_MD}")
    if not ALL_CANDIDATES_CSV.exists():
        return
    try:
        df = pd.read_csv(ALL_CANDIDATES_CSV, dtype=str, keep_default_na=False)
    except Exception as exc:
        errors.append(f"failed to inspect repeat appearance columns: {exc}")
        return
    missing = required - set(df.columns)
    if missing:
        errors.append(f"all_candidates missing repeat appearance columns: {sorted(missing)}")


def check_repeat_appearance_in_pdf(label: str, text: str, errors: list[str]) -> None:
    compact = normalize_for_search(text)
    required = ["連續上榜"]
    if label == "full_table":
        required.extend(["近5日上榜", "近10日上榜", "多分類共振"])
    for phrase in required:
        if normalize_for_search(phrase) not in compact:
            errors.append(f"{label}: missing repeat appearance wording: {phrase}")


def check_non_revenue_momentum_section(curated_text: str, full_text: str, errors: list[str]) -> None:
    if not NON_REVENUE_MOMENTUM_CSV.exists():
        return
    try:
        df = pd.read_csv(NON_REVENUE_MOMENTUM_CSV, dtype=str, keep_default_na=False)
    except Exception as exc:
        errors.append(f"failed to inspect non-revenue momentum CSV: {exc}")
        return
    required = {
        "non_revenue_momentum_type",
        "revenue_confirmation_status",
        "theme_final_status",
        "theme_volume_attack_status",
        "volume_breakout_type",
        "next_confirmation",
    }
    missing = required - set(df.columns)
    if missing:
        errors.append(f"non-revenue momentum missing columns: {sorted(missing)}")
        return
    if df.empty:
        return
    combined = normalize_for_search(curated_text + "\n" + full_text)
    required_any = [
        "非營收驅動強勢股",
        "Non-Revenue Momentum",
        "non_revenue_momentum",
    ]
    if not any(normalize_for_search(term) in combined for term in required_any):
        errors.append("PDF missing non-revenue momentum specialty section")


def check_decision_layer_watchlist(errors: list[str]) -> None:
    try:
        import importlib.util

        module_path = Path("scripts/generate_daily_market_pdf.py")
        spec = importlib.util.spec_from_file_location("generate_daily_market_pdf_validation", module_path)
        if spec is None or spec.loader is None:
            errors.append("failed to load daily PDF generator for decision-layer validation")
            return
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        df = module.load_candidates()
        selected = module.selected_by_category(df)
        watch = module.top_watchlist(selected)
    except Exception as exc:
        errors.append(f"failed decision-layer watchlist validation: {exc}")
        return

    if watch.empty:
        return
    if "decision_priority" in watch.columns:
        bad_priority = watch[watch["decision_priority"].astype(str).ne("A_priority_watch")]
        if not bad_priority.empty:
            ids = bad_priority["stock_id"].astype(str).head(10).tolist()
            errors.append(f"front watchlist contains non-A decision_priority rows: {ids}")
    bad_warning_rows = []
    for _, row in watch.iterrows():
        if module.has_decision_warning(row):
            bad_warning_rows.append(str(row.get("stock_id", "")))
    if bad_warning_rows:
        errors.append(f"front watchlist contains decision-warning rows: {bad_warning_rows[:10]}")
    if "stock_id" in watch.columns and watch["stock_id"].astype(str).eq("2347").any():
        errors.append("2347 appears in front watchlist despite stale/no-confirmation warning")


def check_model_line_pdfs(errors: list[str], warnings: list[str]) -> dict[str, dict[str, Any]]:
    infos: dict[str, dict[str, Any]] = {}
    for label, path in MODEL_LINE_PDFS.items():
        info = pdf_info(path)
        infos[label] = {
            "path": path.as_posix(),
            "exists": info["exists"],
            "size_bytes": info["size_bytes"],
            "pages": info["pages"],
        }
        check_pdf_basic(label, info, errors, warnings)
        check_duplicate_rank_labels(label, info["text"], errors)
        check_raw_slug_terms(label, info["text"], errors)
    return infos


def check_model_summary_for_report(errors: list[str]) -> dict[str, Any]:
    summary = {
        "path": MODEL_SUMMARY_CSV.as_posix(),
        "exists": MODEL_SUMMARY_CSV.exists(),
        "rows": 0,
        "models_by_report_line": {},
    }
    if not MODEL_SUMMARY_CSV.exists():
        errors.append(f"missing {MODEL_SUMMARY_CSV}")
        return summary
    required = {
        "report_line",
        "model_id",
        "model_name_zh",
        "model_registry_order",
        "new_signal_stock_display",
        "new_signal_rank_label_zh",
        "display_rank_new_signal",
        "model_rank_new_signal",
        "repeated_signal_stock_display",
        "repeated_signal_rank_label_zh",
        "display_rank_repeated_signal",
        "model_rank_repeated_signal",
        "operation_reminder_zh",
    }
    try:
        df = pd.read_csv(MODEL_SUMMARY_CSV, dtype=str).fillna("")
    except Exception as exc:
        errors.append(f"failed to read {MODEL_SUMMARY_CSV}: {exc}")
        return summary
    summary["rows"] = int(len(df))
    missing = required - set(df.columns)
    if missing:
        errors.append(f"model summary missing columns: {sorted(missing)}")
        return summary
    report_lines = set(df["report_line"].astype(str))
    if report_lines != {"mainstream", "non_mainstream"}:
        errors.append(f"model summary invalid report_line values: {sorted(report_lines)}")
    dupes = df.duplicated(["report_line", "model_id"])
    if dupes.any():
        rows = df.loc[dupes, ["report_line", "model_id"]].head(10).to_dict("records")
        errors.append(f"model summary duplicate report_line/model_id rows: {rows}")
    for report_line in ["mainstream", "non_mainstream"]:
        part = df[df["report_line"].eq(report_line)].copy()
        summary["models_by_report_line"][report_line] = int(len(part))
        if len(part) != 10:
            errors.append(f"{report_line}: expected 10 fixed model summary rows, got {len(part)}")
        no_candidate = "今日無候選"
        new_prefix = "新進榜 #"
        repeated_prefixes = (
            "連續榜 #",
            "累計榜 #",
            "重複進榜 #",
        )
        valid_new_labels = part["new_signal_rank_label_zh"].astype(str).str.strip().apply(
            lambda value: value in {"", "-", no_candidate} or value.startswith(new_prefix)
        )
        if not valid_new_labels.all():
            bad = part.loc[~valid_new_labels, ["report_line", "model_id", "new_signal_rank_label_zh"]].head(10).to_dict("records")
            errors.append(f"{report_line}: new_signal_rank_label_zh has invalid labels: {bad}")
        valid_repeated_labels = part["repeated_signal_rank_label_zh"].astype(str).str.strip().apply(
            lambda value: value in {"", "-", no_candidate} or value.startswith(repeated_prefixes)
        )
        if not valid_repeated_labels.all():
            bad = part.loc[~valid_repeated_labels, ["report_line", "model_id", "repeated_signal_rank_label_zh"]].head(10).to_dict("records")
            errors.append(f"{report_line}: repeated_signal_rank_label_zh has invalid labels: {bad}")
    return summary


def check_model_report_signals_for_report(errors: list[str]) -> dict[str, Any]:
    summary = {
        "path": MODEL_REPORT_SIGNALS_CSV.as_posix(),
        "exists": MODEL_REPORT_SIGNALS_CSV.exists(),
        "rows": 0,
        "duplicate_report_model_stock_rows": 0,
    }
    main_date = safe_str(read_freshness().get("main_price_date", ""))
    if not MODEL_REPORT_SIGNALS_CSV.exists():
        errors.append(f"missing {MODEL_REPORT_SIGNALS_CSV}")
        return summary
    required = {
        "report_line",
        "model_id",
        "stock_id",
        "model_name_zh",
        "display_rank",
        "model_rank",
        "same_model_repeat_status",
        "same_model_repeat_status_zh",
        "display_rank_new_signal",
        "display_rank_repeated_signal",
        "model_rank_new_signal",
        "model_rank_repeated_signal",
        "why_selected_human_zh",
        "operation_reminder_zh",
    }
    try:
        df = pd.read_csv(MODEL_REPORT_SIGNALS_CSV, dtype=str).fillna("")
    except Exception as exc:
        errors.append(f"failed to read {MODEL_REPORT_SIGNALS_CSV}: {exc}")
        return summary
    summary["rows"] = int(len(df))
    missing = required - set(df.columns)
    if missing:
        errors.append(f"model report signals missing columns: {sorted(missing)}")
        return summary
    report_lines = set(df["report_line"].astype(str))
    if report_lines - {"mainstream", "non_mainstream"}:
        errors.append(f"model report signals invalid report_line values: {sorted(report_lines)}")
    duplicate_count = int(df.duplicated(["report_line", "model_id", "stock_id"]).sum())
    summary["duplicate_report_model_stock_rows"] = duplicate_count
    if duplicate_count:
        dupes = df[df.duplicated(["report_line", "model_id", "stock_id"], keep=False)]
        rows = dupes[["report_line", "model_id", "stock_id"]].head(10).to_dict("records")
        errors.append(f"model report signals duplicate report_line/model_id/stock_id rows: {rows}")
    if main_date:
        for col in ["signal_date", "date", "main_price_date"]:
            if col in df.columns:
                values = sorted({normalize_date_value(value) for value in df[col].tolist()} - {""})
                bad_values = [value for value in values if value != main_date]
                if bad_values:
                    examples = (
                        df[df[col].map(normalize_date_value).isin(bad_values)]
                        [["report_line", "model_id", "stock_id", col]]
                        .head(10)
                        .to_dict("records")
                    )
                    errors.append(
                        f"model report signals {col} contains non-current dates: {bad_values[:10]} examples={examples}"
                    )
        if "source_date" in df.columns:
            source_values = sorted({normalize_date_value(value) for value in df["source_date"].tolist()} - {""})
            bad_source_values = [value for value in source_values if value != main_date]
            if bad_source_values:
                examples = (
                    df[df["source_date"].map(normalize_date_value).isin(bad_source_values)]
                    [["report_line", "model_id", "stock_id", "source_date"]]
                    .head(10)
                    .to_dict("records")
                )
                errors.append(
                    f"model report signals source_date contains stale dates: {bad_source_values[:10]} examples={examples}"
                )
    if df["why_selected_human_zh"].astype(str).str.strip().eq("").any():
        errors.append("model report signals has blank why_selected_human_zh rows")
    if df["operation_reminder_zh"].astype(str).str.strip().eq("").any():
        errors.append("model report signals has blank operation_reminder_zh rows")
    return summary


def validate() -> tuple[dict[str, Any], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    freshness = read_freshness()
    manifest = read_manifest()
    main_date = safe_str(freshness.get("main_price_date") or manifest.get("main_price_date", ""))

    curated = pdf_info(CURATED_PDF)
    full = pdf_info(FULL_TABLE_PDF)
    model_line_pdf_infos = check_model_line_pdfs(errors, warnings)
    model_summary_info = check_model_summary_for_report(errors)
    model_report_signal_info = check_model_report_signals_for_report(errors)

    check_pdf_basic("curated", curated, errors, warnings)
    check_pdf_basic("full_table", full, errors, warnings)
    check_required_sections("curated", curated["text"], CURATED_REQUIRED_SECTIONS, errors)
    check_required_sections("full_table", full["text"], FULL_REQUIRED_SECTIONS, errors)
    check_category_order("curated", curated["text"], errors)
    check_category_order("full_table", full["text"], errors)
    check_forbidden_terms("curated", curated["text"], errors)
    check_forbidden_terms("full_table", full["text"], errors)
    check_duplicate_rank_labels("curated", curated["text"], errors)
    check_duplicate_rank_labels("full_table", full["text"], errors)
    check_raw_slug_terms("curated", curated["text"], errors)
    check_raw_slug_terms("full_table", full["text"], errors)
    check_no_total_ranking("curated", curated["text"], errors)
    check_no_total_ranking("full_table", full["text"], errors)
    check_score_rank_priority("curated", curated["text"], errors)
    check_score_rank_priority("full_table", full["text"], errors)
    check_report_date("curated", curated["text"], main_date, errors)
    check_report_date("full_table", full["text"], main_date, errors)
    check_candidate_date(errors, main_date)
    check_technical_snapshot_date(errors, main_date)
    check_catalyst_columns(errors)
    check_repeat_appearance_columns(errors)
    check_repeat_appearance_in_pdf("curated", curated["text"], errors)
    check_repeat_appearance_in_pdf("full_table", full["text"], errors)
    check_non_revenue_momentum_section(curated["text"], full["text"], errors)
    check_decision_layer_watchlist(errors)

    result = {
        "generated_at": now_text(),
        "status": "pass" if not errors else "fail",
        "main_price_date": main_date,
        "curated_pdf": {
            "path": CURATED_PDF.as_posix(),
            "exists": curated["exists"],
            "size_bytes": curated["size_bytes"],
            "pages": curated["pages"],
        },
        "full_table_pdf": {
            "path": FULL_TABLE_PDF.as_posix(),
            "exists": full["exists"],
            "size_bytes": full["size_bytes"],
            "pages": full["pages"],
        },
        "model_line_pdfs": model_line_pdf_infos,
        "model_summary_for_report": model_summary_info,
        "model_report_signals_for_report": model_report_signal_info,
        "checks": {
            "pdf_exists": curated["exists"] and full["exists"],
            "pdf_size_reasonable": (
                curated["size_bytes"] >= MIN_PDF_SIZE_BYTES_BY_LABEL["curated"]
                and full["size_bytes"] >= MIN_PDF_SIZE_BYTES_BY_LABEL["full_table"]
            ),
            "pdf_pages_reasonable": 1 <= curated["pages"] <= MAX_REASONABLE_PAGES and 1 <= full["pages"] <= MAX_REASONABLE_PAGES,
            "curated_required_sections": all(normalize_for_search(s) in normalize_for_search(curated["text"]) for s in CURATED_REQUIRED_SECTIONS),
            "full_required_sections": all(normalize_for_search(s) in normalize_for_search(full["text"]) for s in FULL_REQUIRED_SECTIONS),
            "no_forbidden_terms": not any(normalize_for_search(term) in normalize_for_search(curated["text"] + full["text"]) for term in FORBIDDEN_TERMS),
            "category_order": not any("category order" in err or "missing category" in err for err in errors),
            "no_total_ranking": not any("total ranking" in err for err in errors),
            "score_rank_priority_present": not any("score/rank/priority" in err for err in errors),
            "report_date_matches": not any("main_price_date" in err or "all_candidates date" in err for err in errors),
            "catalyst_layer_columns_present": not any("catalyst" in err or "similar_to_shihsinko" in err for err in errors),
            "repeat_appearance_columns_present": not any("repeat appearance" in err or "連續上榜" in err or "近5日上榜" in err for err in errors),
            "model_line_pdfs_exist": all(item["exists"] for item in model_line_pdf_infos.values()),
            "model_summary_fixed_rows": not any("model summary" in err for err in errors),
            "model_report_signals_deduped": model_report_signal_info.get("duplicate_report_model_stock_rows", 0) == 0,
            "model_report_signals_pdf_facing_fields_present": not any("model report signals missing columns" in err for err in errors),
        },
        "errors": errors,
        "warnings": warnings,
    }
    return result, errors, warnings


def write_outputs(result: dict[str, Any]) -> None:
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Daily Market PDF Validation",
        "",
        f"- generated_at: `{result.get('generated_at', '')}`",
        f"- status: `{result.get('status', '')}`",
        f"- main_price_date: `{result.get('main_price_date', '')}`",
        "",
        "## PDF Files",
        f"- curated: `{result['curated_pdf']['path']}` / pages `{result['curated_pdf']['pages']}` / bytes `{result['curated_pdf']['size_bytes']}`",
        f"- full_table: `{result['full_table_pdf']['path']}` / pages `{result['full_table_pdf']['pages']}` / bytes `{result['full_table_pdf']['size_bytes']}`",
        "",
        "## Checks",
    ]
    for key, value in result.get("checks", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Errors")
    if result.get("errors"):
        for err in result["errors"]:
            lines.append(f"- {err}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Warnings")
    if result.get("warnings"):
        for warning in result["warnings"]:
            lines.append(f"- {warning}")
    else:
        lines.append("- none")
    lines.append("")
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(VALIDATION_MD, DOCS_VALIDATION_MD)

    main_date = safe_str(result.get("main_price_date", ""))
    if main_date:
        HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(VALIDATION_JSON, HISTORY_REPORT_DIR / f"{main_date}_daily_market_report_validation.json")
        shutil.copyfile(VALIDATION_MD, HISTORY_REPORT_DIR / f"{main_date}_daily_market_report_validation.md")


def main() -> int:
    result, errors, _warnings = validate()
    write_outputs(result)
    print(f"Saved: {VALIDATION_JSON}")
    print(f"Saved: {VALIDATION_MD}")
    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
