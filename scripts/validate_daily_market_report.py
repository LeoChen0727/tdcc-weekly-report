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
PDF_MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"

CURATED_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"
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


def check_category_order(label: str, text: str, errors: list[str]) -> None:
    compact = normalize_for_search(text)
    start_marker = "各分類清單" if label == "full_table" else "分類解讀"
    start_pos = compact.find(normalize_for_search(start_marker))
    if start_pos >= 0:
        compact = compact[start_pos:]

    positions: list[tuple[str, int]] = []
    for category in CATEGORY_ORDER:
        pos = compact.find(normalize_for_search(category))
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
        df = pd.read_csv(ALL_CANDIDATES_CSV, dtype=str, usecols=["date"]).fillna("")
        dates = sorted(set(df["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)))
        if main_date and main_date not in dates:
            errors.append(f"all_candidates date does not contain main_price_date {main_date}; dates={dates[:5]}")
    except Exception as exc:
        errors.append(f"failed to inspect all_candidates date: {exc}")


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


def validate() -> tuple[dict[str, Any], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    freshness = read_freshness()
    manifest = read_manifest()
    main_date = safe_str(freshness.get("main_price_date") or manifest.get("main_price_date", ""))

    curated = pdf_info(CURATED_PDF)
    full = pdf_info(FULL_TABLE_PDF)

    check_pdf_basic("curated", curated, errors, warnings)
    check_pdf_basic("full_table", full, errors, warnings)
    check_required_sections("curated", curated["text"], CURATED_REQUIRED_SECTIONS, errors)
    check_required_sections("full_table", full["text"], FULL_REQUIRED_SECTIONS, errors)
    check_category_order("curated", curated["text"], errors)
    check_category_order("full_table", full["text"], errors)
    check_forbidden_terms("curated", curated["text"], errors)
    check_forbidden_terms("full_table", full["text"], errors)
    check_no_total_ranking("curated", curated["text"], errors)
    check_no_total_ranking("full_table", full["text"], errors)
    check_score_rank_priority("curated", curated["text"], errors)
    check_score_rank_priority("full_table", full["text"], errors)
    check_report_date("curated", curated["text"], main_date, errors)
    check_report_date("full_table", full["text"], main_date, errors)
    check_candidate_date(errors, main_date)
    check_catalyst_columns(errors)
    check_repeat_appearance_columns(errors)
    check_repeat_appearance_in_pdf("curated", curated["text"], errors)
    check_repeat_appearance_in_pdf("full_table", full["text"], errors)

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
