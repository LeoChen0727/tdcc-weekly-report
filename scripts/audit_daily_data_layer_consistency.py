from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd

from tracking_utils import LATEST_DIR, main_price_date_from_freshness, read_csv, safe_str


AUDIT_JSON = LATEST_DIR / "daily_data_layer_consistency_audit_latest.json"
AUDIT_MD = LATEST_DIR / "daily_data_layer_consistency_audit_latest.md"
README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
README_INDEX_JSON = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT_INDEX.json"
CHATGPT_DAILY_RULES = LATEST_DIR / "CHATGPT_DAILY_REPORT_RULES.txt"

MODEL_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
RAW_MODEL_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_latest.csv"
VOLUME_WATCH = LATEST_DIR / "volume_breakout_watch_latest.csv"
VOLUME_ATTACK_STOCKS = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
GROUP_ROTATION = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"
TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
TAXONOMY_TEMPLATE_CSV = LATEST_DIR / "stock_theme_manual_fill_template_latest.csv"
TAXONOMY_TEMPLATE_XLSX = LATEST_DIR / "stock_theme_manual_fill_template_latest.xlsx"
DOCS_LATEST_DIR = Path("docs/latest")
DOCS_TAXONOMY_TEMPLATE_CSV = DOCS_LATEST_DIR / "stock_theme_manual_fill_template_latest.csv"
DOCS_TAXONOMY_TEMPLATE_XLSX = DOCS_LATEST_DIR / "stock_theme_manual_fill_template_latest.xlsx"
MARKET_TIMING_PACKET = LATEST_DIR / "market_timing_chatgpt_packet_latest.md"

REQUIRED_VOLUME_COLUMNS = {
    "volume_breakout_priority",
    "selection_status",
    "risk_flags",
    "next_volume_breakout_confirmation",
    "range_high",
    "range_low",
    "range_breakout_pct",
    "volume_ma20",
}

UNREADABLE_PATTERN = re.compile(r"\ufffd|\?\?\?")
MOJIBAKE_PATTERN = re.compile(r"[\ue000-\uf8ff]|\ufffd|ï¿½|銝|甇|撌|脫||||")
RAW_SLUG_PATTERN = re.compile(r"(^|[\s|/、,;])([a-z]+(?:_[a-z0-9]+){1,})(?=$|[\s|/、,;])")
REQUIRED_MODEL_DISPLAY_COLUMNS = {
    "report_bucket_zh",
    "source_category_zh",
    "effective_primary_theme_zh",
    "effective_structural_theme_bucket_zh",
    "tdcc_status_zh",
    "warrant_flow_signal_zh",
    "risk_tags_zh",
    "score_components_zh",
}

NO_THIRD_BUCKET_COLUMNS = {
    "report_bucket",
    "report_line",
    "effective_mainstream_label",
    "report_line_memberships",
}

VALID_REPORT_LINES = {"mainstream", "non_mainstream"}

REQUIRED_MODEL_COLUMNS = {
    "signal_date",
    "report_line",
    "report_bucket",
    "model_id",
    "model_name_zh",
    "stock_id",
    "stock_name",
    "display_rank",
    "model_score",
    "main_condition_met",
    "why_selected_zh",
    "next_confirmation_zh",
}

REQUIRED_TAXONOMY_COLUMNS = {
    "stock_id",
    "stock_name",
    "basic_theme",
    "effective_mainstream_label",
    "report_line_memberships",
    "mainstream_report_eligible",
    "non_mainstream_report_eligible",
}

THIRD_BUCKET_VALUES = {"", "theme_unknown", "unclassified", "unknown", "other"}

# Representative semantic checks. These are not exhaustive taxonomy assertions;
# they are cheap tripwires for the categories that previously broke reports.
TAXONOMY_SANITY_CASES = {
    "2049": {"name": "上銀", "theme_contains": ["機器人"], "membership_any": ["mainstream"]},
    "1590": {"name": "亞德客-KY", "theme_contains": ["機器人"], "membership_any": ["mainstream"]},
    "1815": {"name": "富喬", "theme_contains": ["玻纖", "PCB", "CCL"], "membership_any": ["mainstream"]},
    "2313": {"name": "華通", "theme_contains": ["PCB", "低軌"], "membership_any": ["mainstream"]},
    "2317": {"name": "鴻海", "theme_contains": ["AI"], "membership_any": ["mainstream"]},
    "1303": {"name": "南亞", "membership_any": ["mainstream", "non_mainstream"]},
    "1617": {"name": "Rongxing", "theme_contains": ["\u96fb\u5668\u96fb\u7e9c"]},
    "1618": {"name": "Heji", "theme_contains": ["\u91cd\u96fb", "\u96fb\u5668\u96fb\u7e9c"]},
}


def _safe_read(path: Path) -> pd.DataFrame:
    return read_csv(path, dtype=str, keep_default_na=False)


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8-sig", errors="replace")


def _market_timing_packet_main_date() -> str:
    text = _read_text(MARKET_TIMING_PACKET)
    match = re.search(r"(?m)^-\s*main_price_date:\s*(\d{8})\s*$", text)
    return match.group(1) if match else ""


def _market_timing_packet_mojibake_lines(limit: int = 10) -> list[str]:
    text = _read_text(MARKET_TIMING_PACKET)
    hits: list[str] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if MOJIBAKE_PATTERN.search(line):
            hits.append(f"{line_no}: {line[:160]}")
            if len(hits) >= limit:
                break
    return hits


def _bad_text_rows(df: pd.DataFrame, cols: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for col in cols:
        if col in df.columns:
            count = int(df[col].astype(str).str.contains(UNREADABLE_PATTERN, na=False).sum())
            if count:
                result[col] = count
    return result


def _raw_slug_rows(df: pd.DataFrame, cols: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for col in cols:
        if col in df.columns:
            count = int(df[col].astype(str).map(lambda value: bool(RAW_SLUG_PATTERN.search(value))).sum())
            if count:
                result[col] = count
    return result


def _blank_rows(df: pd.DataFrame, cols: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for col in cols:
        if col in df.columns:
            count = int(df[col].astype(str).str.strip().eq("").sum())
            if count:
                result[col] = count
    return result


def _third_bucket_rows(df: pd.DataFrame, cols: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for col in cols:
        if col in df.columns:
            count = int(df[col].astype(str).str.strip().str.lower().isin(THIRD_BUCKET_VALUES).sum())
            if count:
                result[col] = count
    return result


def _split_memberships(value: object) -> set[str]:
    text = safe_str(value)
    if not text:
        return set()
    return {part.strip() for part in re.split(r"[|,;/、]+", text) if part.strip()}


def _template_xlsx_rows(path: Path) -> int:
    if not path.exists():
        return 0
    workbook = pd.ExcelFile(path)
    return sum(
        len(pd.read_excel(path, sheet_name=sheet, dtype=str))
        for sheet in workbook.sheet_names
        if sheet.startswith("stocks_")
    )


def _read_key_value_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line or line.lstrip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        result[key.strip()] = value.strip()
    return result


def _read_json_file(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return {"__decode_error__": True}
    return data if isinstance(data, dict) else {"__non_object__": True}


def _split_order(value: object) -> list[str]:
    if isinstance(value, list):
        raw_items = [safe_str(item) for item in value]
    else:
        raw_items = safe_str(value).split(",")
    result: list[str] = []
    for item in raw_items:
        item = item.strip()
        if not item:
            continue
        # Index text may include notes such as "only for astrology tasks".
        result.append(item.split()[0].strip())
    return result


def _validate_raw_api_before_pages(label: str, order: list[str], errors: list[str]) -> None:
    relevant = [
        item
        for item in order
        if "readme" in item.lower() and "astrology" not in item.lower()
    ]
    if not relevant:
        errors.append(f"{label} missing README read order entries")
        return
    first = relevant[0].lower()
    if "pages_url" in first:
        errors.append(f"{label} puts Pages before raw/API: first={relevant[0]}")

    for family in ("date_stamped", "history", "latest"):
        family_items = [item for item in relevant if family in item.lower()]
        if not family_items:
            continue
        first_family = family_items[0].lower()
        if "pages_url" in first_family:
            errors.append(f"{label} puts {family} Pages before raw/API: first={family_items[0]}")


def _validate_chatgpt_daily_rules_read_order(errors: list[str], details: dict[str, object]) -> None:
    text = _read_text(CHATGPT_DAILY_RULES)
    details["chatgpt_daily_rules_present"] = bool(text)
    if not text:
        errors.append("CHATGPT_DAILY_REPORT_RULES.txt is missing or unreadable")
        return
    bad_snippets = [
        "https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT.txt\n- If Pages entry fails",
        "If Pages entry fails, use raw entry",
        "packet_pages_url\n  packet_commit_raw_url",
    ]
    hits = [snippet for snippet in bad_snippets if snippet in text]
    details["chatgpt_daily_rules_pages_first_snippet_count"] = len(hits)
    if hits:
        errors.append("CHATGPT_DAILY_REPORT_RULES.txt still contains Pages-first daily read order")


def audit(include_readme: bool = False) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, object] = {}

    freshness_main_date = main_price_date_from_freshness()
    main_date = freshness_main_date
    details["main_price_date"] = freshness_main_date

    if include_readme:
        readme_kv = _read_key_value_file(README_TXT)
        readme_index = _read_json_file(README_INDEX_JSON)
        readme_main_date = safe_str(readme_kv.get("main_price_date", ""))
        readme_report_ready = safe_str(readme_kv.get("report_ready", ""))
        readme_index_main_date = safe_str(readme_index.get("main_price_date", ""))
        readme_index_report_ready = safe_str(readme_index.get("report_ready", ""))
        preferred_chatgpt_url = safe_str(readme_kv.get("preferred_chatgpt_url", ""))
        details["readme_main_price_date"] = readme_main_date
        details["readme_report_ready"] = readme_report_ready
        details["readme_index_main_price_date"] = readme_index_main_date
        details["readme_index_report_ready"] = readme_index_report_ready
        details["preferred_chatgpt_url"] = preferred_chatgpt_url
        if "github.io" in preferred_chatgpt_url.lower():
            errors.append("preferred_chatgpt_url points to GitHub Pages; daily packet preference must be raw/API")
        readme_order = _split_order(readme_kv.get("readme_cache_bypass_order", ""))
        readme_index_order = _split_order(readme_index.get("recommended_read_order", []))
        details["readme_cache_bypass_order"] = readme_order
        details["readme_index_recommended_read_order"] = readme_index_order
        if readme_order:
            _validate_raw_api_before_pages("README readme_cache_bypass_order", readme_order, errors)
        else:
            errors.append("README readme_cache_bypass_order is missing")
        if readme_index_order:
            _validate_raw_api_before_pages("README index recommended_read_order", readme_index_order, errors)
        else:
            errors.append("README index recommended_read_order is missing")
        if not readme_kv:
            errors.append("READ_ME_FIRST_DAILY_REPORT.txt is missing or unreadable")
        elif readme_main_date != main_date:
            errors.append(f"README main_price_date mismatch: expected {main_date}, got {readme_main_date}")
        if readme_index.get("__decode_error__"):
            errors.append("READ_ME_FIRST_DAILY_REPORT_INDEX.json is not valid JSON")
        elif not readme_index:
            errors.append("READ_ME_FIRST_DAILY_REPORT_INDEX.json is missing or unreadable")
        elif readme_index_main_date != main_date:
            errors.append(f"README index main_price_date mismatch: expected {main_date}, got {readme_index_main_date}")
        _validate_chatgpt_daily_rules_read_order(errors, details)

    signals = _safe_read(MODEL_SIGNALS)
    raw_signals = _safe_read(RAW_MODEL_SIGNALS)
    volume = _safe_read(VOLUME_WATCH)
    volume_theme_stocks = _safe_read(VOLUME_ATTACK_STOCKS)
    group_rotation = _safe_read(GROUP_ROTATION)
    taxonomy = _safe_read(TAXONOMY)
    taxonomy_template_csv = _safe_read(TAXONOMY_TEMPLATE_CSV)
    docs_taxonomy_template_csv = _safe_read(DOCS_TAXONOMY_TEMPLATE_CSV)

    model_signal_dates_for_expected = sorted(
        {
            safe_str(value)
            for value in signals.get("signal_date", pd.Series(dtype=str)).astype(str).tolist()
            if safe_str(value)
        }
    )
    if len(model_signal_dates_for_expected) == 1:
        main_date = model_signal_dates_for_expected[0]
    details["effective_model_signal_date"] = main_date
    if freshness_main_date and main_date and freshness_main_date != main_date:
        warnings.append(
            f"freshness main_price_date={freshness_main_date} differs from model signal_date={main_date}; "
            "auditing report data layer consistency against model signal_date"
        )

    details["model_signal_rows"] = len(signals)
    details["raw_model_signal_rows"] = len(raw_signals)
    details["volume_watch_rows"] = len(volume)
    details["volume_theme_stock_rows"] = len(volume_theme_stocks)
    details["group_rotation_rows"] = len(group_rotation)
    details["taxonomy_rows"] = len(taxonomy)
    details["taxonomy_template_csv_rows"] = len(taxonomy_template_csv)
    details["taxonomy_template_xlsx_rows"] = _template_xlsx_rows(TAXONOMY_TEMPLATE_XLSX)
    details["docs_taxonomy_template_csv_rows"] = len(docs_taxonomy_template_csv)
    details["docs_taxonomy_template_xlsx_rows"] = _template_xlsx_rows(DOCS_TAXONOMY_TEMPLATE_XLSX)

    market_timing_packet_date = _market_timing_packet_main_date()
    details["market_timing_packet_main_price_date"] = market_timing_packet_date
    if not MARKET_TIMING_PACKET.exists():
        errors.append(f"{MARKET_TIMING_PACKET} is missing")
    elif market_timing_packet_date != main_date:
        errors.append(
            f"market timing packet main_price_date mismatch: expected {main_date}, "
            f"got {market_timing_packet_date or 'missing'}"
        )
    elif bad_packet_lines := _market_timing_packet_mojibake_lines():
        details["market_timing_packet_mojibake_lines"] = bad_packet_lines
        errors.append(f"market timing packet contains mojibake/private-use text: {bad_packet_lines[:3]}")

    if signals.empty:
        errors.append("daily_candidate_model_signals_for_report_latest.csv is empty")
    else:
        missing_model_cols = sorted(REQUIRED_MODEL_COLUMNS - set(signals.columns))
        details["missing_required_model_columns"] = missing_model_cols
        if missing_model_cols:
            errors.append(f"model signal missing required columns: {missing_model_cols}")
        blank_model_cols = _blank_rows(signals, sorted(REQUIRED_MODEL_COLUMNS & set(signals.columns)))
        details["blank_required_model_columns"] = blank_model_cols
        if blank_model_cols:
            errors.append(f"model signal required columns contain blanks: {blank_model_cols}")
        signal_dates = sorted(set(signals.get("signal_date", pd.Series(dtype=str)).astype(str)))
        details["model_signal_dates"] = signal_dates
        if signal_dates != [main_date]:
            errors.append(f"model signal_date mismatch: expected {main_date}, got {signal_dates}")
        dup = int(signals.duplicated(["report_bucket", "model_id", "stock_id"]).sum())
        details["same_model_report_duplicates"] = dup
        if dup:
            errors.append(f"report table has duplicate report_bucket/model_id/stock_id rows: {dup}")
        if {"report_line", "report_line_memberships"}.issubset(signals.columns):
            membership_mismatch = int(
                signals.apply(
                    lambda row: safe_str(row.get("report_line")) not in _split_memberships(row.get("report_line_memberships")),
                    axis=1,
                ).sum()
            )
            details["model_report_line_membership_mismatch_rows"] = membership_mismatch
            if membership_mismatch:
                errors.append(f"model signal rows have report_line not present in report_line_memberships: {membership_mismatch}")
        bad_text = _bad_text_rows(
            signals,
            ["model_name_zh", "model_main_conditions", "model_add_score_items", "model_operation_guidance"],
        )
        details["model_signal_unreadable_text"] = bad_text
        if bad_text:
            errors.append(f"unreadable text found in model signal columns: {bad_text}")
        missing_display = sorted(REQUIRED_MODEL_DISPLAY_COLUMNS - set(signals.columns))
        details["missing_model_display_columns"] = missing_display
        if missing_display:
            errors.append(f"model signal missing Chinese display columns: {missing_display}")
        display_cols = sorted(REQUIRED_MODEL_DISPLAY_COLUMNS & set(signals.columns))
        bad_display_text = _bad_text_rows(signals, display_cols)
        raw_slug_display = _raw_slug_rows(signals, display_cols)
        details["model_signal_display_unreadable_text"] = bad_display_text
        details["model_signal_display_raw_slug_rows"] = raw_slug_display
        if bad_display_text:
            errors.append(f"unreadable text found in model display columns: {bad_display_text}")
        if raw_slug_display:
            errors.append(f"raw slug leaked in model display columns: {raw_slug_display}")
        third_bucket_model = _third_bucket_rows(signals, sorted(NO_THIRD_BUCKET_COLUMNS & set(signals.columns)))
        details["model_signal_third_bucket_rows"] = third_bucket_model
        if third_bucket_model:
            errors.append(f"third report bucket leaked into model signal rows: {third_bucket_model}")
        if "main_condition_met" in signals.columns:
            main_condition_ok = signals["main_condition_met"].astype(str).str.lower().isin(["true", "1", "yes", "y"])
            bad_main_condition = int((~main_condition_ok).sum())
        else:
            bad_main_condition = 0
        details["model_signal_main_condition_not_true_rows"] = bad_main_condition
        if bad_main_condition:
            errors.append(f"model signal rows not marked main_condition_met=true: {bad_main_condition}")

    if not raw_signals.empty:
        raw_dates = sorted(set(raw_signals.get("signal_date", pd.Series(dtype=str)).astype(str)))
        details["raw_model_signal_dates"] = raw_dates
        if raw_dates != [main_date]:
            errors.append(f"raw model signal_date mismatch: expected {main_date}, got {raw_dates}")

    if volume.empty:
        warnings.append("volume_breakout_watch_latest.csv is empty")
    else:
        missing_volume_cols = sorted(REQUIRED_VOLUME_COLUMNS - set(volume.columns))
        details["missing_volume_columns"] = missing_volume_cols
        if missing_volume_cols:
            errors.append(f"volume breakout watch missing columns: {missing_volume_cols}")
        vol_dates = sorted(set(volume.get("signal_date", pd.Series(dtype=str)).astype(str)))
        details["volume_signal_dates"] = vol_dates
        if vol_dates != [main_date]:
            warnings.append(
                f"volume watch signal_date mismatch: expected {main_date}, got {vol_dates}; "
                "stale auxiliary table ignored for date gating"
            )

    if not volume_theme_stocks.empty:
        other_rows = volume_theme_stocks[
            volume_theme_stocks.get("theme_name", pd.Series(dtype=str)).astype(str).str.lower().isin(["", "other", "unknown"])
        ]
        details["volume_theme_other_rows"] = int(len(other_rows))
        if len(other_rows):
            warnings.append(f"volume attack theme stocks still has generic theme rows: {len(other_rows)}")

    if not group_rotation.empty:
        valid_models = {"group_fund_rotation_launch", "group_slow_inflow_rotation"}
        bad_models = sorted(set(group_rotation.get("rotation_model_id", pd.Series(dtype=str)).astype(str)) - valid_models)
        details["group_rotation_invalid_models"] = bad_models
        if bad_models:
            errors.append(f"invalid group rotation model ids: {bad_models}")
        slow_rows = int(group_rotation.get("rotation_model_id", pd.Series(dtype=str)).astype(str).eq("group_slow_inflow_rotation").sum())
        launch_rows = int(group_rotation.get("rotation_model_id", pd.Series(dtype=str)).astype(str).eq("group_fund_rotation_launch").sum())
        details["group_rotation_slow_rows"] = slow_rows
        details["group_rotation_launch_rows"] = launch_rows
        if not slow_rows and not launch_rows:
            warnings.append("group rotation has no launch or slow-inflow rows")

    if taxonomy.empty:
        errors.append("stock_theme_taxonomy_latest.csv is empty")
    else:
        missing_taxonomy_cols = sorted(REQUIRED_TAXONOMY_COLUMNS - set(taxonomy.columns))
        details["missing_required_taxonomy_columns"] = missing_taxonomy_cols
        if missing_taxonomy_cols:
            errors.append(f"taxonomy missing required columns: {missing_taxonomy_cols}")
        if "stock_id" in taxonomy.columns:
            duplicate_stock_ids = int(taxonomy["stock_id"].astype(str).str.zfill(4).duplicated().sum())
            details["taxonomy_duplicate_stock_id_rows"] = duplicate_stock_ids
            if duplicate_stock_ids:
                errors.append(f"taxonomy contains duplicate stock_id rows: {duplicate_stock_ids}")
        basic_series = taxonomy.get("basic_theme", pd.Series(dtype=str)).astype(str).str.strip()
        primary_series = taxonomy.get("primary_theme", pd.Series(dtype=str)).astype(str).str.strip()
        unresolved_basic = int(basic_series.isin(["", "未分類"]).sum())
        unresolved_primary = int(primary_series.isin(["", "未分類"]).sum())
        details["taxonomy_unresolved_basic_theme_rows"] = unresolved_basic
        details["taxonomy_unresolved_primary_theme_rows"] = unresolved_primary
        if unresolved_basic:
            errors.append(f"taxonomy rows unresolved basic_theme: {unresolved_basic}")
        if unresolved_primary:
            errors.append(f"taxonomy rows unresolved primary_theme: {unresolved_primary}")
        taxonomy_third_bucket = _third_bucket_rows(taxonomy, ["effective_mainstream_label", "report_line_memberships"])
        details["taxonomy_third_bucket_rows"] = taxonomy_third_bucket
        if taxonomy_third_bucket:
            errors.append(f"third report bucket leaked into taxonomy effective fields: {taxonomy_third_bucket}")
        taxonomy_blank_required = _blank_rows(taxonomy, sorted(REQUIRED_TAXONOMY_COLUMNS & set(taxonomy.columns)))
        details["taxonomy_blank_required_columns"] = taxonomy_blank_required
        if taxonomy_blank_required:
            errors.append(f"taxonomy required columns contain blanks: {taxonomy_blank_required}")
        if "report_line_memberships" in taxonomy.columns:
            invalid_membership_rows = int(
                taxonomy["report_line_memberships"]
                .map(lambda value: not _split_memberships(value) or bool(_split_memberships(value) - VALID_REPORT_LINES))
                .sum()
            )
            details["taxonomy_invalid_report_line_membership_rows"] = invalid_membership_rows
            if invalid_membership_rows:
                errors.append(f"taxonomy rows have invalid report_line_memberships: {invalid_membership_rows}")
        if {"report_line_memberships", "mainstream_report_eligible", "non_mainstream_report_eligible"}.issubset(taxonomy.columns):
            eligibility_mismatch_rows = int(
                taxonomy.apply(
                    lambda row: (
                        ("mainstream" in _split_memberships(row.get("report_line_memberships")))
                        != (safe_str(row.get("mainstream_report_eligible")).lower() in {"true", "1", "yes", "y"})
                    )
                    or (
                        ("non_mainstream" in _split_memberships(row.get("report_line_memberships")))
                        != (safe_str(row.get("non_mainstream_report_eligible")).lower() in {"true", "1", "yes", "y"})
                    ),
                    axis=1,
                ).sum()
            )
            details["taxonomy_report_line_eligibility_mismatch_rows"] = eligibility_mismatch_rows
            if eligibility_mismatch_rows:
                errors.append(f"taxonomy report line memberships and eligibility flags mismatch: {eligibility_mismatch_rows}")
        sanity_errors: list[str] = []
        taxonomy_by_id = {str(row["stock_id"]).zfill(4): row for _, row in taxonomy.iterrows() if "stock_id" in taxonomy.columns}
        for stock_id, rule in TAXONOMY_SANITY_CASES.items():
            row = taxonomy_by_id.get(stock_id)
            if row is None:
                sanity_errors.append(f"{stock_id} missing from taxonomy")
                continue
            theme_text = " ".join(
                safe_str(row.get(col, ""))
                for col in ["basic_theme", "hot_primary_theme", "hot_secondary_themes", "primary_theme", "secondary_themes", "structural_theme_bucket"]
            )
            membership = safe_str(row.get("report_line_memberships", ""))
            if "theme_contains" in rule and not any(token in theme_text for token in rule["theme_contains"]):
                sanity_errors.append(f"{stock_id} {rule['name']} theme sanity failed: {theme_text}")
            if "membership_any" in rule and not any(token in membership for token in rule["membership_any"]):
                sanity_errors.append(f"{stock_id} {rule['name']} membership sanity failed: {membership}")
        details["taxonomy_sanity_errors"] = sanity_errors
        if sanity_errors:
            errors.extend(sanity_errors)
        expected_template_columns = {
            "股票代號",
            "股票名稱",
            "上市櫃產業",
            "基本族群",
            "主流/非主流",
            "熱門族群1",
            "熱門族群2",
            "熱門族群3",
            "熱門族群4",
            "熱門族群5",
            "備註",
        }
        missing_template_cols = sorted(expected_template_columns - set(taxonomy_template_csv.columns))
        details["taxonomy_template_missing_columns"] = missing_template_cols
        if missing_template_cols:
            errors.append(f"taxonomy fill template missing columns: {missing_template_cols}")
        docs_missing_template_cols = sorted(expected_template_columns - set(docs_taxonomy_template_csv.columns))
        details["docs_taxonomy_template_missing_columns"] = docs_missing_template_cols
        if docs_missing_template_cols:
            errors.append(f"docs taxonomy fill template missing columns: {docs_missing_template_cols}")
        if len(taxonomy_template_csv) != len(taxonomy):
            errors.append(f"taxonomy fill template csv row mismatch: expected {len(taxonomy)}, got {len(taxonomy_template_csv)}")
        if details["taxonomy_template_xlsx_rows"] != len(taxonomy):
            errors.append(
                f"taxonomy fill template xlsx row mismatch: expected {len(taxonomy)}, got {details['taxonomy_template_xlsx_rows']}"
            )
        if len(docs_taxonomy_template_csv) != len(taxonomy):
            errors.append(
                f"docs taxonomy fill template csv row mismatch: expected {len(taxonomy)}, got {len(docs_taxonomy_template_csv)}"
            )
        if details["docs_taxonomy_template_xlsx_rows"] != len(taxonomy):
            errors.append(
                f"docs taxonomy fill template xlsx row mismatch: expected {len(taxonomy)}, got {details['docs_taxonomy_template_xlsx_rows']}"
            )

    status = "pass" if not errors else "fail"
    return {"status": status, "errors": errors, "warnings": warnings, "details": details}


def write_report(result: dict[str, object]) -> None:
    AUDIT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    details = result.get("details", {})
    lines = [
        "# Daily Data Layer Consistency Audit",
        "",
        f"- status: `{result['status']}`",
        f"- main_price_date: `{details.get('main_price_date', '')}`",
        f"- readme_main_price_date: `{details.get('readme_main_price_date', '')}`",
        f"- readme_index_main_price_date: `{details.get('readme_index_main_price_date', '')}`",
        f"- model_signal_rows: `{details.get('model_signal_rows', 0)}`",
        f"- volume_watch_rows: `{details.get('volume_watch_rows', 0)}`",
        f"- volume_theme_other_rows: `{details.get('volume_theme_other_rows', 0)}`",
        f"- group_rotation_rows: `{details.get('group_rotation_rows', 0)}`",
        f"- taxonomy_rows: `{details.get('taxonomy_rows', 0)}`",
        f"- taxonomy_template_csv_rows: `{details.get('taxonomy_template_csv_rows', 0)}`",
        f"- taxonomy_template_xlsx_rows: `{details.get('taxonomy_template_xlsx_rows', 0)}`",
        f"- docs_taxonomy_template_csv_rows: `{details.get('docs_taxonomy_template_csv_rows', 0)}`",
        f"- docs_taxonomy_template_xlsx_rows: `{details.get('docs_taxonomy_template_xlsx_rows', 0)}`",
        "",
        "## Errors",
        "",
    ]
    errors = result.get("errors") or []
    lines.extend([f"- {x}" for x in errors] if errors else ["- none"])
    lines.extend(["", "## Warnings", ""])
    warnings = result.get("warnings") or []
    lines.extend([f"- {x}" for x in warnings] if warnings else ["- none"])
    lines.extend(["", "## Details", "", "```json", json.dumps(details, ensure_ascii=False, indent=2), "```", ""])
    AUDIT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit daily model/report data consistency.")
    parser.add_argument(
        "--include-readme",
        action="store_true",
        help="Also verify READ_ME_FIRST and its index after the publish step has regenerated them.",
    )
    args = parser.parse_args()
    result = audit(include_readme=args.include_readme)
    write_report(result)
    print(f"Saved: {AUDIT_JSON}")
    print(f"Saved: {AUDIT_MD}")
    if result["status"] != "pass":
        for error in result.get("errors", []):
            print(f"ERROR: {error}")
        return 1
    print("Daily data layer consistency audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

