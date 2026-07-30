from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, now_text, safe_str, write_csv  # noqa: E402


DATA_DIR = Path("data")
CONFIG_THEME_MAP = Path("config/stock_theme_map.csv")
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"

THEME_EVENTS_DIR = DATA_DIR / "theme_events"
FUNDAMENTAL_CATALYST_DIR = DATA_DIR / "fundamental_catalysts"
EVENT_CATALYST_DIR = DATA_DIR / "event_catalysts"

THEME_EVENT_CALENDAR = THEME_EVENTS_DIR / "theme_event_calendar.csv"
COMPANY_THEME_MAPPING = THEME_EVENTS_DIR / "company_theme_mapping.csv"
QUARTERLY_CATALYST = FUNDAMENTAL_CATALYST_DIR / "quarterly_catalyst.csv"
EVENT_CATALYST_LOG = EVENT_CATALYST_DIR / "event_catalyst_log.csv"

SOURCE_STATUS_MD = LATEST_DIR / "catalyst_data_source_status_latest.md"
SOURCE_STATUS_JSON = LATEST_DIR / "catalyst_data_source_status_latest.json"

TWSE_MONTHLY_REVENUE_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap05_L"
TPEX_MONTHLY_REVENUE_URL = "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O"
TWSE_MATERIAL_INFO_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap04_L"
TPEX_MATERIAL_INFO_URL = "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap04_O"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; tdcc-weekly-report catalyst fetcher)",
    "Accept": "application/json,text/html;q=0.8,*/*;q=0.5",
}

THEME_EVENT_COLUMNS = [
    "event_date",
    "event_end_date",
    "event_name",
    "event_type",
    "theme_tags",
    "related_industries",
    "related_stock_ids",
    "importance",
    "source_url",
    "last_updated",
]

COMPANY_THEME_COLUMNS = [
    "stock_id",
    "stock_name",
    "industry",
    "theme_tags",
    "theme_source",
    "theme_confidence",
    "theme_summary",
    "last_updated",
]

QUARTERLY_CATALYST_COLUMNS = [
    "stock_id",
    "stock_name",
    "quarter",
    "announcement_date",
    "eps",
    "eps_yoy",
    "eps_qoq",
    "gross_margin",
    "gross_margin_yoy_change",
    "gross_margin_qoq_change",
    "operating_margin",
    "operating_margin_yoy_change",
    "operating_margin_qoq_change",
    "net_income_yoy",
    "net_income_qoq",
    "profit_turnaround",
    "eps_surprise_flag",
    "margin_improvement_flag",
    "earnings_acceleration_flag",
    "revenue_good_eps_unconfirmed",
    "source_url",
    "last_updated",
]

EVENT_CATALYST_COLUMNS = [
    "event_date",
    "stock_id",
    "stock_name",
    "event_type",
    "theme_tags",
    "title",
    "summary",
    "source",
    "source_url",
    "catalyst_strength",
    "catalyst_confidence",
    "is_confirmed",
    "is_speculative",
    "related_to_revenue",
    "related_to_eps",
    "related_to_orders",
    "related_to_capacity",
    "related_to_customer",
    "last_updated",
]

THEME_TAG_MAP = {
    "ai server supply chain": "AI_server_theme",
    "ai server": "AI_server_theme",
    "pcb/ccl": "PCB_CCL_theme",
    "pcb": "PCB_CCL_theme",
    "passive components": "passive_component_theme",
    "semiconductor equipment/materials": "semiconductor_equipment_theme",
    "semiconductor equipment": "semiconductor_equipment_theme",
    "semiconductor": "semiconductor_theme",
    "memory": "memory_theme",
    "optical communication/cpo": "optical_communication_theme",
    "optical communication": "optical_communication_theme",
    "cpo": "optical_communication_theme",
    "robotics": "robotics_theme",
    "networking": "networking_theme",
    "green energy": "energy_storage_theme",
    "industrial computer": "IPC_theme",
    "ipc": "IPC_theme",
    "defense": "defense_theme",
    "power discrete/diodes": "power_discrete_theme",
}

MATERIAL_EVENT_KEYWORDS = [
    ("new_order", ["訂單", "接獲", "標案", "採購案", "合約"], "high"),
    ("customer_win", ["客戶", "導入", "採用", "供應", "合作"], "medium"),
    ("capacity_expansion", ["擴產", "產能", "新廠", "建廠", "投資設廠"], "medium"),
    ("mass_production", ["量產", "試產"], "medium"),
    ("product_certification", ["認證", "驗證", "通過"], "medium"),
    ("investor_conference", ["法人說明會", "法說會", "業績發表會"], "low"),
    ("shareholder_meeting", ["股東會", "股東常會", "股東臨時會"], "low"),
]

SHAREHOLDER_EVENT_KEYWORDS = ["股東會", "股東常會", "股東臨時會"]
INVESTOR_EVENT_KEYWORDS = ["法人說明會", "法說會", "業績發表會"]
PRODUCT_CERTIFICATION_KEYWORDS = ["認證", "驗證"]
PRODUCT_CERTIFICATION_CONTEXT = ["產品", "客戶", "規格", "測試", "審查", "資格", "認證", "驗證"]


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    for enc in ["utf-8-sig", "utf-8", "cp950"]:
        try:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc)
        except Exception:
            continue
    return pd.DataFrame()


def ensure_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def normalize_multiline_text(value: Any) -> str:
    text = safe_str(value)
    if not text:
        return ""
    return "\n".join(line.rstrip(" \t") for line in text.splitlines())


def normalize_source_csv_fields(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.columns:
        out[col] = out[col].map(normalize_multiline_text)
    return out


def write_source_csv(df: pd.DataFrame, path: Path) -> None:
    write_csv(normalize_source_csv_fields(df), path)


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Za-z]", "", text)
    if text.isdigit():
        return text.zfill(4)
    return text


def parse_roc_date(value: Any) -> str:
    text = safe_str(value)
    nums = re.findall(r"\d+", text)
    if len(nums) == 1 and len(nums[0]) in {6, 7}:
        raw = nums[0].zfill(7)
        year = int(raw[:-4])
        month = int(raw[-4:-2])
        day = int(raw[-2:])
        if year < 1911:
            year += 1911
        try:
            return date(year, month, day).strftime("%Y%m%d")
        except ValueError:
            return ""
    if len(nums) >= 3:
        year = int(nums[0])
        if year < 1911:
            year += 1911
        month = int(nums[1])
        day = int(nums[2])
        try:
            return date(year, month, day).strftime("%Y%m%d")
        except ValueError:
            return ""
    return ""


def parse_roc_year_month(value: Any) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) in {5, 6}:
        raw = digits.zfill(6)
        year = int(raw[:-2])
        month = int(raw[-2:])
        if year < 1911:
            year += 1911
        if 1 <= month <= 12:
            return f"{year:04d}{month:02d}"
    if len(digits) >= 6:
        return digits[:6]
    return ""


def to_float(value: Any) -> float | None:
    text = safe_str(value).replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except Exception:
        return None


def row_value(row: pd.Series | dict[str, Any], *names: str) -> str:
    if isinstance(row, pd.Series):
        items = row.to_dict()
    else:
        items = row
    stripped = {safe_str(k).strip(): v for k, v in items.items()}
    for name in names:
        if name in stripped:
            value = normalize_multiline_text(stripped[name])
            if value:
                return value
    return ""


def fetch_json_list(url: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    status: dict[str, Any] = {"url": url, "status": "not_run", "rows": 0, "error": ""}
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        status["http_status"] = response.status_code
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        status["status"] = "failed"
        status["error"] = str(exc)
        return [], status
    if not isinstance(data, list):
        status["status"] = "failed"
        status["error"] = "JSON root is not a list"
        return [], status
    rows = [item for item in data if isinstance(item, dict)]
    status["status"] = "ok"
    status["rows"] = len(rows)
    return rows, status


def stock_universe() -> dict[str, dict[str, str]]:
    frames: list[pd.DataFrame] = []
    candidates = read_csv(ALL_CANDIDATES)
    if not candidates.empty:
        frames.append(candidates)
    mapping = read_csv(COMPANY_THEME_MAPPING)
    if not mapping.empty:
        frames.append(mapping)
    if not frames:
        return {}
    combined = pd.concat(frames, ignore_index=True, sort=False)
    code_col = next((col for col in ["stock_id", "code", "ticker"] if col in combined.columns), "")
    if not code_col:
        return {}
    out: dict[str, dict[str, str]] = {}
    for _, row in combined.iterrows():
        code = normalize_code(row.get(code_col))
        if not code or code in out:
            continue
        out[code] = {
            "stock_name": row_value(row, "stock_name", "name"),
            "industry": row_value(row, "industry"),
            "theme_tags": row_value(row, "theme_tags", "theme_group", "細分族群"),
        }
    return out


def ensure_csv(path: Path, columns: list[str]) -> pd.DataFrame:
    df = read_csv(path)
    if df.empty:
        df = pd.DataFrame(columns=columns)
    df = ensure_columns(df, columns)
    write_source_csv(df, path)
    return df


def merge_rows(existing: pd.DataFrame, new_df: pd.DataFrame, columns: list[str], key_cols: list[str]) -> pd.DataFrame:
    if existing.empty:
        combined = new_df.copy()
    elif new_df.empty:
        combined = existing.copy()
    else:
        combined = pd.concat([existing, new_df], ignore_index=True, sort=False)
    combined = ensure_columns(combined, columns)
    for col in key_cols:
        if col not in combined.columns:
            combined[col] = ""
    combined = combined.drop_duplicates(key_cols, keep="last")
    return combined.sort_values(key_cols, kind="stable").reset_index(drop=True)


def split_tags(value: Any) -> list[str]:
    text = safe_str(value)
    if not text:
        return []
    parts = []
    for chunk in text.replace(",", ";").replace("、", ";").split(";"):
        item = chunk.strip()
        if item:
            parts.append(item)
    return parts


def normalize_theme_tags(*values: Any) -> str:
    tags: list[str] = []
    for value in values:
        for raw in split_tags(value):
            key = raw.lower()
            mapped = THEME_TAG_MAP.get(key)
            if mapped:
                tags.append(mapped)
            elif raw:
                tags.append(raw)
    return ";".join(dict.fromkeys(tags))


def build_company_theme_mapping(existing: pd.DataFrame) -> pd.DataFrame:
    stock_theme = read_csv(CONFIG_THEME_MAP)
    if stock_theme.empty:
        return ensure_columns(existing, COMPANY_THEME_COLUMNS)

    old_by_code = {}
    if not existing.empty and "stock_id" in existing.columns:
        for _, row in existing.iterrows():
            code = safe_str(row.get("stock_id"))
            if code:
                old_by_code[code] = row.to_dict()

    rows: list[dict[str, str]] = []
    for _, item in stock_theme.iterrows():
        code = safe_str(item.get("code")).zfill(4)
        if not code:
            continue
        old = old_by_code.get(code, {})
        tags = safe_str(old.get("theme_tags")) or normalize_theme_tags(
            item.get("primary_theme"),
            item.get("secondary_theme"),
            item.get("concept_tags"),
        )
        summary_parts = [
            safe_str(item.get("primary_theme")),
            safe_str(item.get("secondary_theme")),
            safe_str(item.get("concept_tags")),
        ]
        rows.append(
            {
                "stock_id": code,
                "stock_name": safe_str(old.get("stock_name")) or safe_str(item.get("name")),
                "industry": safe_str(old.get("industry")) or safe_str(item.get("industry")),
                "theme_tags": tags,
                "theme_source": safe_str(old.get("theme_source")) or CONFIG_THEME_MAP.as_posix(),
                "theme_confidence": safe_str(old.get("theme_confidence")) or "medium",
                "theme_summary": safe_str(old.get("theme_summary")) or " / ".join([x for x in summary_parts if x]),
                "last_updated": safe_str(old.get("last_updated")) or now_text(),
            }
        )

    generated = pd.DataFrame(rows)
    if existing.empty:
        combined = generated
    else:
        combined = pd.concat([existing, generated], ignore_index=True, sort=False)
        combined = combined.drop_duplicates("stock_id", keep="first")
    return ensure_columns(combined.sort_values("stock_id"), COMPANY_THEME_COLUMNS)


def build_monthly_revenue_fundamental_rows(universe: dict[str, dict[str, str]]) -> tuple[pd.DataFrame, dict[str, Any]]:
    source_defs = [
        ("TWSE monthly revenue OpenAPI", TWSE_MONTHLY_REVENUE_URL),
        ("TPEX monthly revenue OpenAPI", TPEX_MONTHLY_REVENUE_URL),
    ]
    rows: list[dict[str, str]] = []
    sources: dict[str, Any] = {}
    for label, url in source_defs:
        data, status = fetch_json_list(url)
        matched = 0
        for item in data:
            code = normalize_code(row_value(item, "公司代號", "SecuritiesCompanyCode"))
            if not code or code not in universe:
                continue
            revenue_yoy = to_float(row_value(item, "營業收入-去年同月增減(%)"))
            cumulative_yoy = to_float(row_value(item, "累計營業收入-前期比較增減(%)"))
            revenue_good = (revenue_yoy is not None and revenue_yoy >= 20) or (
                cumulative_yoy is not None and cumulative_yoy >= 10
            )
            stock_name = row_value(item, "公司名稱", "CompanyName") or universe[code].get("stock_name", "")
            rows.append(
                {
                    "stock_id": code,
                    "stock_name": stock_name,
                    "quarter": f"monthly_revenue_{parse_roc_year_month(row_value(item, '資料年月'))}",
                    "announcement_date": parse_roc_date(row_value(item, "出表日期", "Date")),
                    "eps": "",
                    "eps_yoy": "",
                    "eps_qoq": "",
                    "gross_margin": "",
                    "gross_margin_yoy_change": "",
                    "gross_margin_qoq_change": "",
                    "operating_margin": "",
                    "operating_margin_yoy_change": "",
                    "operating_margin_qoq_change": "",
                    "net_income_yoy": "",
                    "net_income_qoq": "",
                    "profit_turnaround": "False",
                    "eps_surprise_flag": "False",
                    "margin_improvement_flag": "False",
                    "earnings_acceleration_flag": "False",
                    "revenue_good_eps_unconfirmed": "True" if revenue_good else "False",
                    "source_url": url,
                    "last_updated": now_text(),
                }
            )
            matched += 1
        status["matched_tracked_rows"] = matched
        status["stored_rows"] = matched
        status["note"] = (
            "Official monthly revenue rows are stored as fundamental source rows with EPS/margin fields blank. "
            "They can flag revenue_good_eps_unconfirmed only; they are not EPS confirmation."
        )
        sources[label] = status
    return pd.DataFrame(rows, columns=QUARTERLY_CATALYST_COLUMNS), sources


def classify_material_event(title: Any, description: Any) -> tuple[str, str]:
    text = f"{safe_str(title)} {safe_str(description)}"
    if any(keyword in text for keyword in SHAREHOLDER_EVENT_KEYWORDS):
        return "shareholder_meeting", "low"
    if any(keyword in text for keyword in INVESTOR_EVENT_KEYWORDS):
        return "investor_conference", "low"

    for event_type, keywords, strength in MATERIAL_EVENT_KEYWORDS:
        if event_type in {"shareholder_meeting", "investor_conference"}:
            continue
        if event_type == "customer_win":
            matched = "客戶" in text and any(keyword in text for keyword in keywords[1:])
        elif event_type == "product_certification":
            matched = any(keyword in text for keyword in PRODUCT_CERTIFICATION_KEYWORDS) or (
                "通過" in text and any(keyword in text for keyword in PRODUCT_CERTIFICATION_CONTEXT)
            )
        else:
            matched = any(keyword in text for keyword in keywords)
        if matched:
            return event_type, strength
    return "material_information", "low"


def material_relation_flags(event_type: str) -> dict[str, str]:
    return {
        "related_to_revenue": "True" if event_type in {"new_order", "customer_win", "mass_production"} else "False",
        "related_to_eps": "False",
        "related_to_orders": "True" if event_type == "new_order" else "False",
        "related_to_capacity": "True" if event_type in {"capacity_expansion", "mass_production"} else "False",
        "related_to_customer": "True" if event_type == "customer_win" else "False",
    }


def build_material_event_rows(universe: dict[str, dict[str, str]]) -> tuple[pd.DataFrame, dict[str, Any]]:
    source_defs = [
        ("TWSE material information OpenAPI", TWSE_MATERIAL_INFO_URL),
        ("TPEX material information OpenAPI", TPEX_MATERIAL_INFO_URL),
    ]
    rows: list[dict[str, str]] = []
    sources: dict[str, Any] = {}
    for label, url in source_defs:
        data, status = fetch_json_list(url)
        matched = 0
        for item in data:
            code = normalize_code(row_value(item, "公司代號", "SecuritiesCompanyCode"))
            if not code or code not in universe:
                continue
            title = row_value(item, "主旨", "主旨 ")
            summary = row_value(item, "說明")
            event_type, strength = classify_material_event(title, summary)
            flags = material_relation_flags(event_type)
            stock_name = row_value(item, "公司名稱", "CompanyName") or universe[code].get("stock_name", "")
            theme_tags = universe[code].get("theme_tags", "")
            rows.append(
                {
                    "event_date": parse_roc_date(row_value(item, "事實發生日", "發言日期", "Date")),
                    "stock_id": code,
                    "stock_name": stock_name,
                    "event_type": event_type,
                    "theme_tags": normalize_theme_tags(theme_tags),
                    "title": title,
                    "summary": summary,
                    "source": label,
                    "source_url": url,
                    "catalyst_strength": strength,
                    "catalyst_confidence": "high",
                    "is_confirmed": "True",
                    "is_speculative": "False",
                    **flags,
                    "last_updated": now_text(),
                }
            )
            matched += 1
        status["matched_tracked_rows"] = matched
        status["stored_rows"] = matched
        status["note"] = (
            "Official material-information rows are filtered to tracked stocks. "
            "Only objective order/customer/capacity/production/certification keywords become evidence event types; other rows stay material_information context."
        )
        sources[label] = status
    return pd.DataFrame(rows, columns=EVENT_CATALYST_COLUMNS), sources


def build_status(sources: dict[str, Any]) -> dict[str, Any]:
    files = {
        "theme_event_calendar": THEME_EVENT_CALENDAR,
        "company_theme_mapping": COMPANY_THEME_MAPPING,
        "quarterly_catalyst": QUARTERLY_CATALYST,
        "event_catalyst_log": EVENT_CATALYST_LOG,
    }
    table_rows: dict[str, int] = {}
    for key, path in files.items():
        table_rows[key] = int(len(read_csv(path)))
    external_ok = any(int(info.get("stored_rows") or info.get("matched_tracked_rows") or 0) > 0 for info in sources.values())
    status: dict[str, Any] = {
        "generated_at": now_text(),
        "external_fetch_status": "partial_ok" if external_ok else "not_configured",
        "note": (
            "Official monthly revenue and material-information sources are used when reachable. "
            "No unverified news, MOPS pages, or social rumor data is fabricated."
        ),
        "files": {},
        "sources": sources,
    }
    for key, path in files.items():
        status["files"][key] = {
            "path": path.as_posix(),
            "exists": path.exists(),
            "rows": table_rows[key],
        }
    return status


def write_status(status: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    SOURCE_STATUS_JSON.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Catalyst Data Source Status",
        "",
        f"- generated_at: `{status['generated_at']}`",
        f"- external_fetch_status: `{status['external_fetch_status']}`",
        f"- note: {status['note']}",
        "",
        "| data_table | path | rows |",
        "|---|---|---:|",
    ]
    for name, info in status["files"].items():
        lines.append(f"| {name} | `{info['path']}` | {info['rows']} |")
    lines.extend(
        [
            "",
            "## External Source Status",
            "",
            "| source | status | rows | matched_tracked_rows | url | note |",
            "|---|---|---:|---:|---|---|",
        ]
    )
    for name, info in status.get("sources", {}).items():
        lines.append(
            f"| {name} | {info.get('status', '')} | {info.get('rows', 0)} | "
            f"{info.get('matched_tracked_rows', info.get('stored_rows', 0))} | {info.get('url', '')} | "
            f"{safe_str(info.get('note', info.get('error', '')))} |"
        )
    lines.extend(
        [
            "",
            "## Data Policy",
            "",
            "- Company announcements, MOPS, official financial statements, official exhibition pages, and company releases should be loaded into these tables before being treated as confirmed catalysts.",
            "- Empty rows mean the catalyst is not available yet. The daily model keeps fields blank instead of inventing a catalyst.",
        ]
    )
    SOURCE_STATUS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ensure_csv(THEME_EVENT_CALENDAR, THEME_EVENT_COLUMNS)
    existing_mapping = ensure_csv(COMPANY_THEME_MAPPING, COMPANY_THEME_COLUMNS)
    write_source_csv(build_company_theme_mapping(existing_mapping), COMPANY_THEME_MAPPING)
    universe = stock_universe()
    quarterly_existing = ensure_csv(QUARTERLY_CATALYST, QUARTERLY_CATALYST_COLUMNS)
    event_existing = ensure_csv(EVENT_CATALYST_LOG, EVENT_CATALYST_COLUMNS)
    quarterly_generated, revenue_sources = build_monthly_revenue_fundamental_rows(universe)
    event_generated, material_sources = build_material_event_rows(universe)
    write_source_csv(
        merge_rows(
            quarterly_existing,
            quarterly_generated,
            QUARTERLY_CATALYST_COLUMNS,
            ["stock_id", "quarter", "source_url"],
        ),
        QUARTERLY_CATALYST,
    )
    write_source_csv(
        merge_rows(
            event_existing,
            event_generated,
            EVENT_CATALYST_COLUMNS,
            ["event_date", "stock_id", "title", "source"],
        ),
        EVENT_CATALYST_LOG,
    )
    status = build_status({**revenue_sources, **material_sources})
    write_status(status)
    print(f"Saved: {THEME_EVENT_CALENDAR}")
    print(f"Saved: {COMPANY_THEME_MAPPING}")
    print(f"Saved: {QUARTERLY_CATALYST}")
    print(f"Saved: {EVENT_CATALYST_LOG}")
    print(f"Saved: {SOURCE_STATUS_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
