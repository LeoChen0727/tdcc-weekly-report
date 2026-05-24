from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, now_text, safe_str, write_csv  # noqa: E402


DATA_DIR = Path("data")
CONFIG_THEME_MAP = Path("config/stock_theme_map.csv")

THEME_EVENTS_DIR = DATA_DIR / "theme_events"
FUNDAMENTAL_CATALYST_DIR = DATA_DIR / "fundamental_catalysts"
EVENT_CATALYST_DIR = DATA_DIR / "event_catalysts"

THEME_EVENT_CALENDAR = THEME_EVENTS_DIR / "theme_event_calendar.csv"
COMPANY_THEME_MAPPING = THEME_EVENTS_DIR / "company_theme_mapping.csv"
QUARTERLY_CATALYST = FUNDAMENTAL_CATALYST_DIR / "quarterly_catalyst.csv"
EVENT_CATALYST_LOG = EVENT_CATALYST_DIR / "event_catalyst_log.csv"

SOURCE_STATUS_MD = LATEST_DIR / "catalyst_data_source_status_latest.md"
SOURCE_STATUS_JSON = LATEST_DIR / "catalyst_data_source_status_latest.json"

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


def ensure_csv(path: Path, columns: list[str]) -> pd.DataFrame:
    df = read_csv(path)
    if df.empty:
        df = pd.DataFrame(columns=columns)
    df = ensure_columns(df, columns)
    write_csv(df, path)
    return df


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


def build_status() -> dict[str, Any]:
    files = {
        "theme_event_calendar": THEME_EVENT_CALENDAR,
        "company_theme_mapping": COMPANY_THEME_MAPPING,
        "quarterly_catalyst": QUARTERLY_CATALYST,
        "event_catalyst_log": EVENT_CATALYST_LOG,
    }
    status: dict[str, Any] = {
        "generated_at": now_text(),
        "external_fetch_status": "not_configured",
        "note": "Schema and local/manual data tables are prepared. No unverified news, MOPS, or social rumor data is fabricated.",
        "files": {},
    }
    for key, path in files.items():
        df = read_csv(path)
        status["files"][key] = {
            "path": path.as_posix(),
            "exists": path.exists(),
            "rows": int(len(df)),
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
    write_csv(build_company_theme_mapping(existing_mapping), COMPANY_THEME_MAPPING)
    ensure_csv(QUARTERLY_CATALYST, QUARTERLY_CATALYST_COLUMNS)
    ensure_csv(EVENT_CATALYST_LOG, EVENT_CATALYST_COLUMNS)
    status = build_status()
    write_status(status)
    print(f"Saved: {THEME_EVENT_CALENDAR}")
    print(f"Saved: {COMPANY_THEME_MAPPING}")
    print(f"Saved: {QUARTERLY_CATALYST}")
    print(f"Saved: {EVENT_CATALYST_LOG}")
    print(f"Saved: {SOURCE_STATUS_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
