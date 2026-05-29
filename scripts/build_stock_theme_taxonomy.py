from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DATA_DIR, LATEST_DIR, normalize_code, now_text, read_csv, safe_str, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

THEME_EVENTS_DIR = DATA_DIR / "theme_events"
MANUAL_TAXONOMY = THEME_EVENTS_DIR / "stock_theme_taxonomy.csv"
COMPANY_THEME_MAPPING = THEME_EVENTS_DIR / "company_theme_mapping.csv"
CONFIG_THEME_MAP = ROOT / "config" / "stock_theme_map.csv"

LATEST_CSV = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
LATEST_MD = LATEST_DIR / "stock_theme_taxonomy_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / "stock_theme_taxonomy_latest.csv"
DOCS_MD = DOCS_LATEST_DIR / "stock_theme_taxonomy_latest.md"

OUTPUT_COLUMNS = [
    "stock_id",
    "stock_name",
    "official_industry",
    "primary_theme",
    "secondary_themes",
    "structural_theme_bucket",
    "theme_structural_status",
    "theme_mainstream_label",
    "concept_tags",
    "taxonomy_source",
    "confidence",
    "last_reviewed",
    "notes",
]


TAG_RULES: list[dict[str, Any]] = [
    {
        "tokens": ["passive_component_theme", "passive components", "capacitor", "mlcc", "resistor", "inductor"],
        "primary_theme": "被動元件",
        "bucket": "passive_component_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "MLCC;電容;電阻;電感",
        "concept": "passive components;MLCC;capacitor;resistor;inductor",
    },
    {
        "tokens": ["memory_theme", "memory", "dram", "flash", "hbm"],
        "primary_theme": "記憶體/HBM",
        "bucket": "memory_hbm_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "DRAM;Flash;HBM;記憶體控制",
        "concept": "memory;DRAM;Flash;HBM",
    },
    {
        "tokens": ["semiconductor_equipment_theme", "semiconductor equipment", "wet process", "wafer reclaim", "automation equipment"],
        "primary_theme": "半導體設備/材料",
        "bucket": "semiconductor_equipment_material_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "半導體設備;材料;自動化;製程設備",
        "concept": "semiconductor equipment;semiconductor materials;automation",
    },
    {
        "tokens": ["semiconductor_theme", "semiconductor", "ic design", "foundry", "compound semiconductor", "ic distribution"],
        "primary_theme": "半導體",
        "bucket": "semiconductor_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "IC設計;晶圓代工;化合物半導體;通路",
        "concept": "semiconductor;IC design;foundry;compound semiconductor;IC distribution",
    },
    {
        "tokens": ["pcb_ccl_theme", "pcb/ccl", "pcb", "ccl"],
        "primary_theme": "PCB/CCL",
        "bucket": "pcb_ccl_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "PCB;CCL;載板",
        "concept": "PCB;CCL;substrate",
    },
    {
        "tokens": ["optical_communication_theme", "optical communication", "optical components", "cpo"],
        "primary_theme": "光通訊/CPO",
        "bucket": "optical_communication_cpo_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "光通訊;CPO;光元件",
        "concept": "optical communication;CPO;optical components",
    },
    {
        "tokens": ["networking_theme", "networking", "network equipment", "communications", "wireless"],
        "primary_theme": "網通/通訊",
        "bucket": "network_communication_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "網通設備;通訊;無線",
        "concept": "networking;communications;wireless",
    },
    {
        "tokens": ["ai_server_theme", "ai server", "server", "ipc_theme", "industrial computer"],
        "primary_theme": "AI伺服器/工業電腦",
        "bucket": "ai_server_ipc_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "AI伺服器;工業電腦;伺服器供應鏈",
        "concept": "AI server;IPC;server",
    },
    {
        "tokens": ["power_discrete_theme", "power discrete", "mosfet", "diode", "diodes"],
        "primary_theme": "功率元件",
        "bucket": "power_discrete_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "MOSFET;二極體;功率半導體",
        "concept": "power discrete;MOSFET;diode",
    },
    {
        "tokens": ["consumer electronics", "panel", "display"],
        "primary_theme": "消費性電子/面板",
        "bucket": "consumer_electronics_display_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "面板;顯示器;消費性電子",
        "concept": "consumer electronics;panel;display",
    },
    {
        "tokens": ["other electronics", "solder", "materials"],
        "primary_theme": "電子材料",
        "bucket": "electronic_material_theme",
        "status": "core_mainstream_theme",
        "label": "mainstream_growth_theme",
        "secondary": "電子材料;焊料",
        "concept": "electronic materials;solder materials",
    },
]


NON_MAINSTREAM_INDUSTRY_RULES = [
    ("航運", "航運業", "shipping_theme"),
    ("金融", "金融保險", "financial_theme"),
    ("鋼鐵", "鋼鐵工業", "steel_theme"),
    ("紡織", "紡織纖維", "textile_theme"),
    ("營建", "建材營造", "construction_theme"),
    ("化學", "化學工業", "chemical_theme"),
    ("塑膠", "塑膠工業", "plastic_theme"),
    ("食品", "食品工業", "food_theme"),
    ("觀光", "觀光餐旅", "tourism_theme"),
]


def clean_stock_id(value: Any) -> str:
    return normalize_code(value)


def match_tag_rule(*texts: str) -> dict[str, Any] | None:
    haystack = " ".join(safe_str(text).lower() for text in texts)
    for rule in TAG_RULES:
        if any(token.lower() in haystack for token in rule["tokens"]):
            return rule
    return None


def industry_rule(industry: str) -> tuple[str, str, str] | None:
    text = safe_str(industry)
    for token, primary, bucket in NON_MAINSTREAM_INDUSTRY_RULES:
        if token in text:
            return primary, bucket, "non_mainstream_theme"
    return None


def normalize_manual(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    out = df.copy()
    for col in OUTPUT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    out["stock_id"] = out["stock_id"].map(clean_stock_id)
    out["taxonomy_source"] = out["taxonomy_source"].where(out["taxonomy_source"].astype(str).str.strip().ne(""), "manual_stock_theme_taxonomy")
    out["confidence"] = out["confidence"].where(out["confidence"].astype(str).str.strip().ne(""), "high")
    out["last_reviewed"] = out["last_reviewed"].where(out["last_reviewed"].astype(str).str.strip().ne(""), now_text())
    return out[OUTPUT_COLUMNS]


def row_from_rule(
    stock_id: str,
    stock_name: str,
    official_industry: str,
    rule: dict[str, Any],
    source: str,
    confidence: str,
    notes: str,
) -> dict[str, str]:
    return {
        "stock_id": clean_stock_id(stock_id),
        "stock_name": safe_str(stock_name),
        "official_industry": safe_str(official_industry),
        "primary_theme": rule["primary_theme"],
        "secondary_themes": rule["secondary"],
        "structural_theme_bucket": rule["bucket"],
        "theme_structural_status": rule["status"],
        "theme_mainstream_label": rule["label"],
        "concept_tags": rule["concept"],
        "taxonomy_source": source,
        "confidence": confidence,
        "last_reviewed": now_text(),
        "notes": notes,
    }


def build_from_company_mapping(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    if df.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    for _, row in df.iterrows():
        stock_id = clean_stock_id(row.get("stock_id", ""))
        if not stock_id:
            continue
        tags = safe_str(row.get("theme_tags", ""))
        summary = safe_str(row.get("theme_summary", ""))
        industry = safe_str(row.get("industry", ""))
        rule = match_tag_rule(tags, summary, industry)
        if rule:
            rows.append(
                row_from_rule(
                    stock_id=stock_id,
                    stock_name=safe_str(row.get("stock_name", "")),
                    official_industry=industry,
                    rule=rule,
                    source="company_theme_mapping_auto",
                    confidence=safe_str(row.get("theme_confidence", "")) or "medium",
                    notes=f"auto mapped from theme_tags={tags}",
                )
            )
            continue
        fallback = industry_rule(industry)
        if fallback:
            primary, bucket, status = fallback
            rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": safe_str(row.get("stock_name", "")),
                    "official_industry": industry,
                    "primary_theme": primary,
                    "secondary_themes": "",
                    "structural_theme_bucket": bucket,
                    "theme_structural_status": status,
                    "theme_mainstream_label": "non_mainstream_theme",
                    "concept_tags": safe_str(row.get("theme_tags", "")),
                    "taxonomy_source": "company_theme_mapping_industry_fallback",
                    "confidence": "low",
                    "last_reviewed": now_text(),
                    "notes": "industry fallback; manual review recommended",
                }
            )
    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)


def build_from_config(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    if df.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    for _, row in df.iterrows():
        stock_id = clean_stock_id(row.get("code", ""))
        if not stock_id:
            continue
        primary = safe_str(row.get("primary_theme", ""))
        secondary = safe_str(row.get("secondary_theme", ""))
        concept = safe_str(row.get("concept_tags", ""))
        industry = safe_str(row.get("industry", ""))
        rule = match_tag_rule(primary, secondary, concept, industry)
        if not rule:
            fallback = industry_rule(industry)
            if not fallback:
                continue
            primary_name, bucket, status = fallback
            rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": safe_str(row.get("name", "")),
                    "official_industry": industry,
                    "primary_theme": primary_name,
                    "secondary_themes": secondary,
                    "structural_theme_bucket": bucket,
                    "theme_structural_status": status,
                    "theme_mainstream_label": "non_mainstream_theme",
                    "concept_tags": concept,
                    "taxonomy_source": "config_stock_theme_map_industry_fallback",
                    "confidence": "low",
                    "last_reviewed": now_text(),
                    "notes": "config fallback; manual review recommended",
                }
            )
            continue
        rows.append(
            row_from_rule(
                stock_id=stock_id,
                stock_name=safe_str(row.get("name", "")),
                official_industry=industry,
                rule=rule,
                source="config_stock_theme_map_auto",
                confidence="medium",
                notes=f"auto mapped from primary_theme={primary}; secondary_theme={secondary}",
            )
        )
    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)


def merge_taxonomy(*frames: pd.DataFrame) -> pd.DataFrame:
    priority_source = {
        "manual": 1,
        "company": 2,
        "config": 3,
    }
    parts: list[pd.DataFrame] = []
    for label, frame in zip(priority_source, frames):
        if frame.empty:
            continue
        part = frame.copy()
        part["_priority"] = priority_source[label]
        parts.append(part)
    if not parts:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    merged = pd.concat(parts, ignore_index=True)
    merged["stock_id"] = merged["stock_id"].map(clean_stock_id)
    merged = merged[merged["stock_id"].ne("")]
    merged = merged.sort_values(["stock_id", "_priority"]).drop_duplicates("stock_id", keep="first")
    merged = merged.drop(columns=["_priority"])
    return merged[OUTPUT_COLUMNS].sort_values(["primary_theme", "stock_id"]).reset_index(drop=True)


def build_taxonomy() -> pd.DataFrame:
    manual = normalize_manual(read_csv(MANUAL_TAXONOMY, dtype=str, keep_default_na=False))
    company = build_from_company_mapping(read_csv(COMPANY_THEME_MAPPING, dtype=str, keep_default_na=False))
    config = build_from_config(read_csv(CONFIG_THEME_MAP, dtype=str, keep_default_na=False))
    return merge_taxonomy(manual, company, config)


def build_markdown(df: pd.DataFrame) -> str:
    lines = [
        "# Stock Theme Taxonomy",
        "",
        f"- generated_at: `{now_text()}`",
        f"- rows: `{len(df)}`",
        "- purpose: program-side market theme taxonomy. This overrides legacy industry for theme grouping.",
        "- priority: manual `data/theme_events/stock_theme_taxonomy.csv` > `company_theme_mapping.csv` > `config/stock_theme_map.csv`.",
        "- rule: `primary_theme` / `structural_theme_bucket` / `theme_structural_status` are the authoritative fields for mainstream/non-mainstream split.",
        "- rule: industry is secondary context only.",
        "",
    ]
    if not df.empty:
        counts = df["primary_theme"].value_counts().head(30)
        lines.append("## Primary Theme Counts")
        lines.append("")
        for theme, count in counts.items():
            lines.append(f"- {theme}: `{count}`")
        lines.append("")

    lines.extend(
        [
            "## Required Examples",
            "",
            "- 三集瑞-KY、國巨、凱美、華新科、信昌電、臺慶科、光頡、蜜望實：被動元件。",
            "- 大銀微系統、上銀、直得、全球傳動：機器人/精密傳動。",
            "- 華通、啟碁、正文：低軌衛星。",
            "- 富喬、建榮、南亞、台玻、德宏：玻纖布/CCL。",
            "",
        ]
    )

    show_cols = [
        "stock_id",
        "stock_name",
        "official_industry",
        "primary_theme",
        "structural_theme_bucket",
        "theme_structural_status",
        "confidence",
        "taxonomy_source",
        "notes",
    ]
    lines.append("## Rows")
    lines.append("")
    lines.append("| " + " | ".join(show_cols) + " |")
    lines.append("| " + " | ".join(["---"] * len(show_cols)) + " |")
    for _, row in df.iterrows():
        values = [safe_str(row.get(col, "")).replace("|", "/").replace("\n", " ") for col in show_cols]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    df = build_taxonomy()
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(df, LATEST_CSV)
    LATEST_MD.write_text(build_markdown(df), encoding="utf-8")
    write_csv(df, DOCS_CSV)
    DOCS_MD.write_text(build_markdown(df), encoding="utf-8")
    print(f"Saved: {LATEST_CSV} rows={len(df)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {DOCS_CSV}")
    print(f"Saved: {DOCS_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
