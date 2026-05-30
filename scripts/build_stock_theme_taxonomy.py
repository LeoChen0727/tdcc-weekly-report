from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (
    DOCS_LATEST_DIR,
    LATEST_DIR,
    STOCK_PRICE_HISTORY_DIR,
    normalize_code,
    now_text,
    read_csv,
    safe_str,
    write_csv,
)


CONFIG_THEME_MAP = Path("config/stock_theme_map.csv")
AUTHORIZED_SEED = Path("config/stock_theme_authorized_seed.csv")
MANUAL_OVERRIDE = Path("config/stock_theme_taxonomy_manual.csv")
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"

TAXONOMY_CSV = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
TAXONOMY_MD = LATEST_DIR / "stock_theme_taxonomy_latest.md"
AUTHORIZED_PREVIEW_CSV = LATEST_DIR / "stock_theme_authorized_seed_preview_latest.csv"
AUTHORIZED_PREVIEW_MD = LATEST_DIR / "stock_theme_authorized_seed_preview_latest.md"
TEMPLATE_XLSX = LATEST_DIR / "stock_theme_manual_fill_template_latest.xlsx"
TEMPLATE_CSV = LATEST_DIR / "stock_theme_manual_fill_template_latest.csv"
VALIDATION_JSON = LATEST_DIR / "stock_theme_taxonomy_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "stock_theme_taxonomy_validation_latest.md"

DOCS_TAXONOMY_CSV = DOCS_LATEST_DIR / "stock_theme_taxonomy_latest.csv"
DOCS_TAXONOMY_MD = DOCS_LATEST_DIR / "stock_theme_taxonomy_latest.md"
DOCS_AUTHORIZED_PREVIEW_CSV = DOCS_LATEST_DIR / "stock_theme_authorized_seed_preview_latest.csv"
DOCS_AUTHORIZED_PREVIEW_MD = DOCS_LATEST_DIR / "stock_theme_authorized_seed_preview_latest.md"
DOCS_TEMPLATE_XLSX = DOCS_LATEST_DIR / "stock_theme_manual_fill_template_latest.xlsx"
DOCS_TEMPLATE_CSV = DOCS_LATEST_DIR / "stock_theme_manual_fill_template_latest.csv"
DOCS_VALIDATION_JSON = DOCS_LATEST_DIR / "stock_theme_taxonomy_validation_latest.json"
DOCS_VALIDATION_MD = DOCS_LATEST_DIR / "stock_theme_taxonomy_validation_latest.md"


MAINSTREAM_VALUES = {
    "主流": "core_mainstream",
    "核心主流": "core_mainstream",
    "mainstream": "core_mainstream",
    "core_mainstream": "core_mainstream",
    "非主流": "non_mainstream",
    "non_mainstream": "non_mainstream",
    "非ai": "non_mainstream",
    "非AI": "non_mainstream",
    "觀察": "theme_unknown",
    "未分類": "theme_unknown",
    "": "",
}


STRUCTURAL_BUCKET_BY_THEME_KEYWORD = {
    "機器人": "robotics_precision_motion_theme",
    "robot": "robotics_precision_motion_theme",
    "robotics": "robotics_precision_motion_theme",
    "自動化": "robotics_automation_theme",
    "automation": "robotics_automation_theme",
    "低軌": "low_earth_orbit_satellite_theme",
    "衛星": "low_earth_orbit_satellite_theme",
    "satellite": "low_earth_orbit_satellite_theme",
    "光通訊": "network_optical_datacenter_theme",
    "cpo": "network_optical_datacenter_theme",
    "CPO": "network_optical_datacenter_theme",
    "optical": "network_optical_datacenter_theme",
    "datacenter": "network_optical_datacenter_theme",
    "網通交換器": "network_switch_theme",
    "網通": "network_optical_datacenter_theme",
    "玻纖": "glass_fiber_ccl_theme",
    "glass fiber": "glass_fiber_ccl_theme",
    "ccL": "pcb_ccl_theme",
    "CCL": "pcb_ccl_theme",
    "pcb": "pcb_ccl_theme",
    "PCB": "pcb_ccl_theme",
    "abf": "pcb_ccl_theme",
    "ABF": "pcb_ccl_theme",
    "被動": "passive_component_theme",
    "passive": "passive_component_theme",
    "MLCC": "passive_component_theme",
    "capacitor": "passive_component_theme",
    "resistor": "passive_component_theme",
    "inductor": "passive_component_theme",
    "電容": "passive_component_theme",
    "電感": "passive_component_theme",
    "電阻": "passive_component_theme",
    "散熱": "thermal_solution_theme",
    "thermal": "thermal_solution_theme",
    "電源": "power_supply_theme",
    "power supply": "power_supply_theme",
    "BBU": "power_supply_theme",
    "重電": "power_grid_theme",
    "電網": "power_grid_theme",
    "記憶體": "memory_hbm_theme",
    "memory": "memory_hbm_theme",
    "hbm": "memory_hbm_theme",
    "HBM": "memory_hbm_theme",
    "半導體設備": "semiconductor_equipment_material_theme",
    "semiconductor equipment": "semiconductor_equipment_material_theme",
    "materials": "semiconductor_equipment_material_theme",
    "先進封裝": "advanced_packaging_theme",
    "advanced packaging": "advanced_packaging_theme",
    "矽智財": "asic_advanced_process_theme",
    "ASIC": "asic_advanced_process_theme",
    "asic": "asic_advanced_process_theme",
    "ai伺服器": "ai_server_ipc_theme",
    "AI伺服器": "ai_server_ipc_theme",
    "伺服器": "ai_server_ipc_theme",
    "AI server": "ai_server_ipc_theme",
    "server": "ai_server_ipc_theme",
    "industrial computer": "ai_server_ipc_theme",
    "IPC": "ai_server_ipc_theme",
    "AI PC": "ai_pc_consumer_theme",
    "aipc": "ai_pc_consumer_theme",
    "AI PC": "ai_pc_consumer_theme",
    "high-speed": "high_speed_interconnect_theme",
    "interface": "high_speed_interconnect_theme",
    "MOSFET": "power_supply_theme",
    "diode": "power_supply_theme",
    "軍工": "defense_drone_theme",
    "無人機": "defense_drone_theme",
    "drone": "defense_drone_theme",
    "交換器": "network_switch_theme",
    "switch": "network_switch_theme",
    "車用": "automotive_electronics_theme",
    "automotive": "automotive_electronics_theme",
}


CORE_BUCKETS = {
    "ai_server_ipc_theme",
    "ai_pc_consumer_theme",
    "ai_server_mechanical_theme",
    "ai_chip_testing_theme",
    "asic_advanced_process_theme",
    "semiconductor_equipment_material_theme",
    "advanced_packaging_theme",
    "memory_hbm_theme",
    "network_optical_datacenter_theme",
    "low_earth_orbit_satellite_theme",
    "high_speed_interconnect_theme",
    "thermal_solution_theme",
    "power_supply_theme",
    "power_grid_theme",
    "pcb_ccl_theme",
    "glass_fiber_ccl_theme",
    "fpc_flexible_pcb_theme",
    "passive_component_theme",
    "robotics_precision_motion_theme",
    "robotics_automation_theme",
    "robotics_ipc_edge_ai_theme",
    "robotics_optics_sensor_theme",
    "defense_drone_theme",
    "network_switch_theme",
    "automotive_electronics_theme",
    "specialty_material_theme",
}


NON_MAINSTREAM_INDUSTRY_KEYWORDS = [
    "紡織",
    "成衣",
    "金融",
    "保險",
    "鋼鐵",
    "水泥",
    "營建",
    "建材",
    "航運",
    "觀光",
    "食品",
    "化學",
    "塑膠",
    "橡膠",
    "玻璃陶瓷",
    "貿易百貨",
]

NON_MAINSTREAM_INDUSTRY_KEYWORDS.extend(
    [
        "塑膠",
        "化學",
        "紡織",
        "航運",
        "金融",
        "鋼鐵",
        "食品",
        "觀光",
        "營建",
    ]
)

PROVISIONAL_INDUSTRY_RULES = [
    ("半導體", "半導體_設備材料待細分", "semiconductor_general_theme", "core_mainstream"),
    ("電子零組件", "電子零組件_待細分", "electronic_component_general_theme", "core_mainstream"),
    ("電子通路", "電子通路_IC通路待細分", "electronics_channel_general_theme", "core_mainstream"),
    ("通信網路", "網通_低軌衛星待細分", "networking_general_theme", "core_mainstream"),
    ("光電", "光電_CPO光通訊待細分", "optoelectronics_general_theme", "core_mainstream"),
    ("電機機械", "機器人自動化_電機機械待細分", "robotics_precision_motion_theme", "core_mainstream"),
    ("電器電纜", "重電電網_電器電纜待細分", "power_grid_theme", "core_mainstream"),
    ("電腦及週邊", "AI_PC_電腦週邊待細分", "computer_peripheral_general_theme", "core_mainstream"),
    ("其他電子", "AI伺服器_其他電子待細分", "other_electronics_general_theme", "core_mainstream"),
    ("資訊服務", "資訊服務_AI應用待細分", "information_service_general_theme", "core_mainstream"),
    ("數位雲端", "數位雲端_AI應用待細分", "digital_cloud_general_theme", "core_mainstream"),
    ("塑膠", "塑膠工業", "non_mainstream_theme", "non_mainstream"),
    ("化學", "化學工業", "non_mainstream_theme", "non_mainstream"),
    ("紡織", "紡織纖維", "non_mainstream_theme", "non_mainstream"),
    ("航運", "航運業", "non_mainstream_theme", "non_mainstream"),
    ("金融", "金融保險", "non_mainstream_theme", "non_mainstream"),
    ("鋼鐵", "鋼鐵工業", "non_mainstream_theme", "non_mainstream"),
    ("食品", "食品工業", "non_mainstream_theme", "non_mainstream"),
    ("觀光", "觀光餐旅", "non_mainstream_theme", "non_mainstream"),
    ("營建", "建材營造", "non_mainstream_theme", "non_mainstream"),
    ("半導體", "半導體業_待細分", "semiconductor_general_theme", "core_mainstream"),
    ("電子零組件", "電子零組件_待細分", "electronic_component_general_theme", "core_mainstream"),
    ("電腦及週邊", "AI_PC_電腦週邊待細分", "computer_peripheral_general_theme", "core_mainstream"),
    ("其他電子", "AI供應鏈_其他電子待細分", "other_electronics_general_theme", "core_mainstream"),
    ("通信網路", "網通_低軌衛星待細分", "networking_general_theme", "core_mainstream"),
    ("光電", "光電_CPO光通訊待細分", "optoelectronics_general_theme", "core_mainstream"),
    ("電子通路", "電子通路_IC通路待細分", "electronics_channel_general_theme", "core_mainstream"),
    ("資訊服務", "資訊服務_AI軟體待細分", "information_service_general_theme", "core_mainstream"),
    ("數位雲端", "數位雲端_AI服務待細分", "digital_cloud_general_theme", "core_mainstream"),
    ("電機機械", "機器人自動化_電機機械待細分", "robotics_precision_motion_theme", "core_mainstream"),
    ("電器電纜", "重電電網_電器電纜待細分", "power_grid_theme", "core_mainstream"),
    ("金融", "金融保險", "non_mainstream_theme", "non_mainstream"),
    ("紡織", "紡織纖維", "non_mainstream_theme", "non_mainstream"),
    ("鋼鐵", "鋼鐵工業", "non_mainstream_theme", "non_mainstream"),
    ("建材營造", "建材營造", "non_mainstream_theme", "non_mainstream"),
    ("航運", "航運業", "non_mainstream_theme", "non_mainstream"),
    ("化學", "化學工業", "non_mainstream_theme", "non_mainstream"),
    ("塑膠", "塑膠工業", "non_mainstream_theme", "non_mainstream"),
    ("水泥", "水泥工業", "non_mainstream_theme", "non_mainstream"),
    ("玻璃陶瓷", "玻璃陶瓷", "non_mainstream_theme", "non_mainstream"),
    ("橡膠", "橡膠工業", "non_mainstream_theme", "non_mainstream"),
    ("食品", "食品工業", "non_mainstream_theme", "non_mainstream"),
    ("觀光", "觀光餐旅", "non_mainstream_theme", "non_mainstream"),
    ("造紙", "造紙工業", "non_mainstream_theme", "non_mainstream"),
    ("貿易百貨", "貿易百貨", "non_mainstream_theme", "non_mainstream"),
    ("生技醫療", "生技醫療業", "non_mainstream_theme", "non_mainstream"),
    ("油電燃氣", "油電燃氣業", "non_mainstream_theme", "non_mainstream"),
    ("存託憑證", "存託憑證", "non_mainstream_theme", "non_mainstream"),
    ("運動休閒", "運動休閒", "non_mainstream_theme", "non_mainstream"),
    ("綠能環保", "綠能環保", "non_mainstream_theme", "non_mainstream"),
]

CORE_BUCKETS.update({bucket for _, _, bucket, label in PROVISIONAL_INDUSTRY_RULES if label == "core_mainstream"})


def compact_text(value: Any) -> str:
    return safe_str(value).replace("\ufeff", "").strip()


def split_themes(*values: Any) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        text = compact_text(value)
        for token in text.replace("；", ";").replace("、", ";").replace(",", ";").split(";"):
            item = token.strip()
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return result


def normalize_mainstream(value: Any) -> str:
    text = compact_text(value)
    return MAINSTREAM_VALUES.get(text, text if text in {"core_mainstream", "non_mainstream", "theme_unknown"} else "")


def provisional_industry_rule(industry: str) -> tuple[str, str, str] | None:
    text = compact_text(industry)
    for keyword, primary_theme, bucket, mainstream_label in PROVISIONAL_INDUSTRY_RULES:
        if keyword in text:
            return primary_theme, bucket, mainstream_label
    return None


def infer_bucket(primary_theme: str, secondary_themes: str, industry: str, fallback: str = "") -> str:
    if compact_text(fallback):
        return compact_text(fallback)
    haystack = f"{primary_theme};{secondary_themes};{industry}"
    for keyword, bucket in STRUCTURAL_BUCKET_BY_THEME_KEYWORD.items():
        if keyword in haystack:
            return bucket
    provisional = provisional_industry_rule(industry)
    if provisional:
        return provisional[1]
    if any(keyword in industry for keyword in NON_MAINSTREAM_INDUSTRY_KEYWORDS):
        return "non_mainstream_theme"
    return ""


def infer_mainstream_label(bucket: str, industry: str, manual_value: str = "") -> str:
    manual = normalize_mainstream(manual_value)
    if manual:
        return manual
    if bucket in CORE_BUCKETS:
        return "core_mainstream"
    if bucket == "non_mainstream_theme" or any(keyword in industry for keyword in NON_MAINSTREAM_INDUSTRY_KEYWORDS):
        return "non_mainstream"
    return "theme_unknown"


def infer_industry_mainstream_label(industry: str) -> str:
    """Classify the official industry only, without theme overrides."""
    text = compact_text(industry)
    provisional = provisional_industry_rule(text)
    if provisional:
        return provisional[2]
    if any(keyword in text for keyword in NON_MAINSTREAM_INDUSTRY_KEYWORDS):
        return "non_mainstream"
    return "theme_unknown"


def effective_mainstream_label(theme_label: str, industry_label: str) -> str:
    """Report routing uses theme first, then industry only as fallback."""
    theme = normalize_mainstream(theme_label)
    industry = normalize_mainstream(industry_label)
    if theme in {"core_mainstream", "non_mainstream"}:
        return theme
    if industry in {"core_mainstream", "non_mainstream"}:
        return industry
    return "theme_unknown"


def mainstream_conflict_note(industry_label: str, theme_label: str, effective_label: str) -> tuple[str, str]:
    industry = normalize_mainstream(industry_label)
    theme = normalize_mainstream(theme_label)
    if industry in {"core_mainstream", "non_mainstream"} and theme in {"core_mainstream", "non_mainstream"} and industry != theme:
        return "True", f"industry={industry};theme={theme};report_routing={effective_label}"
    return "False", ""


def report_membership_fields(industry_label: str, theme_label: str, effective_label: str) -> dict[str, str]:
    """Return report routing memberships without changing model scores.

    A stock can have a mainstream theme and a non-mainstream official industry
    at the same time.  For example, 南亞 is both glass-fiber/CCL related and
    plastics by official industry.  It must be eligible for both report views.
    """
    labels = {
        "industry": normalize_mainstream(industry_label),
        "theme": normalize_mainstream(theme_label),
        "effective": normalize_mainstream(effective_label),
    }
    memberships: list[str] = []
    if "core_mainstream" in labels.values():
        memberships.append("mainstream")
    if "non_mainstream" in labels.values():
        memberships.append("non_mainstream")
    if not memberships:
        memberships.append("theme_unknown")
    memberships = list(dict.fromkeys(memberships))
    mainstream = "mainstream" in memberships
    non_mainstream = "non_mainstream" in memberships
    if mainstream and non_mainstream:
        note = "theme_mainstream_section+industry_non_mainstream_section"
    elif mainstream:
        note = "mainstream_section"
    elif non_mainstream:
        note = "non_mainstream_section"
    else:
        note = "theme_unknown_section"
    return {
        "report_line_memberships": "|".join(memberships),
        "mainstream_report_eligible": "True" if mainstream else "False",
        "non_mainstream_report_eligible": "True" if non_mainstream else "False",
        "dual_report_membership_flag": "True" if mainstream and non_mainstream else "False",
        "report_line_membership_note": note,
    }


def load_universe() -> pd.DataFrame:
    rows: dict[str, dict[str, str]] = {}

    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if not candidates.empty:
        for _, row in candidates.iterrows():
            code = normalize_code(row.get("stock_id", ""))
            if not code:
                continue
            rows.setdefault(code, {"stock_id": code})
            rows[code]["stock_name"] = compact_text(row.get("stock_name", "")) or rows[code].get("stock_name", "")
            rows[code]["industry"] = compact_text(row.get("industry", "")) or rows[code].get("industry", "")

    for path in STOCK_PRICE_HISTORY_DIR.glob("*.csv"):
        code = normalize_code(path.stem)
        if not code:
            continue
        rows.setdefault(code, {"stock_id": code})
        if not rows[code].get("stock_name") or not rows[code].get("industry"):
            df = read_csv(path, dtype=str, keep_default_na=False, nrows=5)
            if not df.empty:
                rows[code]["stock_name"] = rows[code].get("stock_name", "") or compact_text(df.iloc[-1].get("stock_name", ""))
                rows[code]["industry"] = rows[code].get("industry", "") or compact_text(df.iloc[-1].get("industry", ""))
                rows[code]["market"] = rows[code].get("market", "") or compact_text(df.iloc[-1].get("market", ""))

    universe = pd.DataFrame(rows.values())
    if universe.empty:
        return pd.DataFrame(columns=["stock_id", "stock_name", "industry", "market"])
    for col in ["stock_name", "industry", "market"]:
        if col not in universe.columns:
            universe[col] = ""
    return universe.sort_values("stock_id").reset_index(drop=True)


def load_default_map() -> pd.DataFrame:
    df = read_csv(CONFIG_THEME_MAP, dtype=str, keep_default_na=False)
    if df.empty:
        return pd.DataFrame(columns=["stock_id"])
    df = df.rename(
        columns={
            "code": "stock_id",
            "name": "stock_name",
            "secondary_theme": "secondary_themes",
            "concept_tags": "concept_tags",
        }
    )
    df["stock_id"] = df["stock_id"].map(normalize_code)
    return df


def load_authorized_seed() -> pd.DataFrame:
    df = read_csv(AUTHORIZED_SEED, dtype=str, keep_default_na=False)
    if df.empty:
        return pd.DataFrame(columns=["stock_id"])
    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_code)
    return df


def load_manual() -> pd.DataFrame:
    df = read_csv(MANUAL_OVERRIDE, dtype=str, keep_default_na=False)
    if df.empty:
        return pd.DataFrame(columns=["stock_id"])
    rename = {
        "股票代號": "stock_id",
        "股票名稱": "stock_name",
        "目前產業": "industry",
        "主流非主流": "theme_mainstream_label",
        "主流/非主流": "theme_mainstream_label",
        "主要族群1": "primary_theme",
        "主要族群": "primary_theme",
        "族群1": "primary_theme",
        "族群2": "theme_2",
        "族群3": "theme_3",
        "備註": "notes",
    }
    df = df.rename(columns={k: v for k, v in rename.items() if k in df.columns})
    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_code)
    return df


def build_taxonomy() -> pd.DataFrame:
    universe = load_universe()
    default_map = load_default_map()
    authorized = load_authorized_seed()
    manual = load_manual()

    seed_sources = []
    for source_df in [default_map, authorized, manual]:
        if not source_df.empty and "stock_id" in source_df.columns:
            cols = [col for col in ["stock_id", "stock_name", "industry"] if col in source_df.columns]
            seed_sources.append(source_df[cols].copy())
    if seed_sources:
        seeded_universe = pd.concat([universe, *seed_sources], ignore_index=True)
        seeded_universe["stock_id"] = seeded_universe["stock_id"].map(normalize_code)
        for col in ["stock_name", "industry", "market"]:
            if col not in seeded_universe.columns:
                seeded_universe[col] = ""
        universe = (
            seeded_universe.sort_values(["stock_id", "stock_name", "industry"])
            .groupby("stock_id", as_index=False)
            .agg(
                {
                    "stock_name": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
                    "industry": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
                    "market": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
                }
            )
        )

    out = universe.copy()
    if not default_map.empty:
        default_cols = [
            col
            for col in ["stock_id", "primary_theme", "secondary_themes", "industry", "concept_tags"]
            if col in default_map.columns
        ]
        out = out.merge(default_map[default_cols].add_prefix("default_"), left_on="stock_id", right_on="default_stock_id", how="left")
    if not authorized.empty:
        authorized_cols = [
            col
            for col in [
                "stock_id",
                "stock_name",
                "industry",
                "theme_mainstream_label",
                "primary_theme",
                "secondary_themes",
                "structural_theme_bucket",
                "theme_structural_status",
                "concept_tags",
                "notes",
            ]
            if col in authorized.columns
        ]
        out = out.merge(
            authorized[authorized_cols].add_prefix("authorized_"),
            left_on="stock_id",
            right_on="authorized_stock_id",
            how="left",
        )
    if not manual.empty:
        manual_cols = [
            col
            for col in [
                "stock_id",
                "stock_name",
                "industry",
                "theme_mainstream_label",
                "primary_theme",
                "theme_2",
                "theme_3",
                "secondary_themes",
                "structural_theme_bucket",
                "notes",
            ]
            if col in manual.columns
        ]
        out = out.merge(manual[manual_cols].add_prefix("manual_"), left_on="stock_id", right_on="manual_stock_id", how="left")

    rows: list[dict[str, str]] = []
    for _, row in out.iterrows():
        stock_id = normalize_code(row.get("stock_id", ""))
        stock_name = (
            compact_text(row.get("manual_stock_name", ""))
            or compact_text(row.get("authorized_stock_name", ""))
            or compact_text(row.get("stock_name", ""))
            or compact_text(row.get("default_stock_name", ""))
        )
        industry = compact_text(row.get("manual_industry", "")) or compact_text(row.get("industry", "")) or compact_text(row.get("default_industry", ""))
        manual_primary = compact_text(row.get("manual_primary_theme", ""))
        authorized_primary = compact_text(row.get("authorized_primary_theme", ""))
        default_primary = compact_text(row.get("default_primary_theme", ""))
        provisional = provisional_industry_rule(industry)
        provisional_primary = provisional[0] if provisional else ""
        primary = manual_primary or authorized_primary or default_primary or provisional_primary or industry
        secondary_list = split_themes(
            row.get("manual_theme_2", ""),
            row.get("manual_theme_3", ""),
            row.get("manual_secondary_themes", ""),
            row.get("authorized_secondary_themes", ""),
            row.get("default_secondary_themes", ""),
        )
        secondary = ";".join([item for item in secondary_list if item != primary])
        bucket = infer_bucket(
            primary,
            secondary,
            industry,
            row.get("manual_structural_theme_bucket", "") or row.get("authorized_structural_theme_bucket", ""),
        )
        mainstream = infer_mainstream_label(
            bucket,
            industry,
            row.get("manual_theme_mainstream_label", "") or row.get("authorized_theme_mainstream_label", ""),
        )
        industry_mainstream = infer_industry_mainstream_label(industry)
        effective_mainstream = effective_mainstream_label(mainstream, industry_mainstream)
        conflict_flag, conflict_note = mainstream_conflict_note(industry_mainstream, mainstream, effective_mainstream)
        membership = report_membership_fields(industry_mainstream, mainstream, effective_mainstream)
        if any(compact_text(row.get(col, "")) for col in ["manual_primary_theme", "manual_theme_mainstream_label", "manual_theme_2", "manual_theme_3"]):
            source = "manual_override"
        elif any(compact_text(row.get(col, "")) for col in ["authorized_primary_theme", "authorized_theme_mainstream_label", "authorized_structural_theme_bucket"]):
            source = "authorized_seed"
        elif provisional:
            source = "provisional_industry_theme"
        else:
            source = "default_theme_map" if default_primary else "industry_default"
        confidence = "high" if source in {"manual_override", "authorized_seed"} else ("medium" if source == "default_theme_map" else "low")
        notes = ";".join(
            split_themes(
                row.get("authorized_notes", ""),
                row.get("manual_notes", ""),
                "provisional_industry_mapping" if source == "provisional_industry_theme" else "",
                "dual_industry_theme_identity" if conflict_flag == "True" else "",
            )
        )
        status = (
            compact_text(row.get("manual_theme_structural_status", ""))
            or compact_text(row.get("authorized_theme_structural_status", ""))
            or ("market_theme" if bucket in CORE_BUCKETS else ("non_mainstream_theme" if mainstream == "non_mainstream" else "needs_manual_review"))
        )
        concept_tags = ";".join(split_themes(row.get("authorized_concept_tags", ""), row.get("default_concept_tags", "")))
        rows.append(
            {
                "stock_id": stock_id,
                "stock_name": stock_name,
                "industry": industry,
                "primary_theme": primary,
                "secondary_themes": secondary,
                "structural_theme_bucket": bucket,
                "theme_structural_status": status,
                "theme_mainstream_label": mainstream,
                "industry_mainstream_label": industry_mainstream,
                "effective_mainstream_label": effective_mainstream,
                "mainstream_conflict_flag": conflict_flag,
                "mainstream_conflict_note": conflict_note,
                **membership,
                "taxonomy_source": source,
                "confidence": confidence,
                "concept_tags": concept_tags,
                "notes": notes,
                "updated_at": now_text(),
            }
        )
    return pd.DataFrame(rows).sort_values("stock_id").reset_index(drop=True)


def build_template(taxonomy: pd.DataFrame, rows_per_sheet: int = 500) -> pd.DataFrame:
    label_map = {"core_mainstream": "??", "non_mainstream": "???", "theme_unknown": ""}
    template = pd.DataFrame(
        {
            "????": taxonomy["stock_id"],
            "????": taxonomy["stock_name"],
            "????": taxonomy["industry"],
            "??/???": taxonomy["effective_mainstream_label"].map(label_map).fillna(""),
            "????1": taxonomy["primary_theme"],
            "??2": taxonomy["secondary_themes"].map(lambda x: split_themes(x)[0] if split_themes(x) else ""),
            "??3": taxonomy["secondary_themes"].map(lambda x: split_themes(x)[1] if len(split_themes(x)) > 1 else ""),
            "?????": taxonomy["industry_mainstream_label"].map(label_map).fillna(""),
            "????": taxonomy["theme_mainstream_label"].map(label_map).fillna(""),
            "??????": taxonomy["effective_mainstream_label"].map(label_map).fillna(""),
            "????": taxonomy["mainstream_conflict_flag"].map({"True": "?", "False": ""}).fillna(""),
            "report_line_memberships": taxonomy["report_line_memberships"],
            "mainstream_report_eligible": taxonomy["mainstream_report_eligible"],
            "non_mainstream_report_eligible": taxonomy["non_mainstream_report_eligible"],
            "??": taxonomy["notes"],
        }
    )
    write_csv(template, TEMPLATE_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(template, DOCS_TEMPLATE_CSV)

    with pd.ExcelWriter(TEMPLATE_XLSX, engine="openpyxl") as writer:
        instructions = pd.DataFrame(
            [
                {"??": "??/???", "??": "?????????????????????????????"},
                {"??": "????1", "??": "????????????????????????????????"},
                {"??": "??2/??3", "??": "???????????????????"},
                {"??": "?????/????/??????/????", "??": "??????????????????????????????"},
                {"??": "??", "??": "??????????????"},
            ]
        )
        instructions.to_excel(writer, index=False, sheet_name="instructions")
        for start in range(0, len(template), rows_per_sheet):
            sheet = f"stocks_{start + 1:04d}_{min(start + rows_per_sheet, len(template)):04d}"
            template.iloc[start : start + rows_per_sheet].to_excel(writer, index=False, sheet_name=sheet)
        workbook = writer.book
        for ws in workbook.worksheets:
            ws.freeze_panes = "A2"
            for col in ws.columns:
                letter = col[0].column_letter
                ws.column_dimensions[letter].width = 18 if letter not in {"E", "F", "G", "H", "I", "J", "K", "L"} else 24
    DOCS_TEMPLATE_XLSX.write_bytes(TEMPLATE_XLSX.read_bytes())
    return template

def markdown_table(df: pd.DataFrame, cols: list[str], limit: int = 40) -> str:
    show = df.loc[:, [col for col in cols if col in df.columns]].head(limit).fillna("")
    if show.empty:
        return "_No rows._"
    return show.to_markdown(index=False)


def validate(taxonomy: pd.DataFrame) -> dict[str, Any]:
    total = len(taxonomy)
    return {
        "generated_at": now_text(),
        "total_rows": total,
        "mainstream_count": int((taxonomy["theme_mainstream_label"] == "core_mainstream").sum()) if total else 0,
        "non_mainstream_count": int((taxonomy["theme_mainstream_label"] == "non_mainstream").sum()) if total else 0,
        "effective_mainstream_count": int((taxonomy["effective_mainstream_label"] == "core_mainstream").sum()) if total else 0,
        "effective_non_mainstream_count": int((taxonomy["effective_mainstream_label"] == "non_mainstream").sum()) if total else 0,
        "mainstream_conflict_count": int((taxonomy["mainstream_conflict_flag"] == "True").sum()) if total else 0,
        "dual_report_membership_count": int((taxonomy["dual_report_membership_flag"] == "True").sum()) if total else 0,
        "mainstream_report_eligible_count": int((taxonomy["mainstream_report_eligible"] == "True").sum()) if total else 0,
        "non_mainstream_report_eligible_count": int((taxonomy["non_mainstream_report_eligible"] == "True").sum()) if total else 0,
        "unknown_count": int((taxonomy["theme_mainstream_label"] == "theme_unknown").sum()) if total else 0,
        "manual_override_count": int((taxonomy["taxonomy_source"] == "manual_override").sum()) if total else 0,
        "authorized_seed_count": int((taxonomy["taxonomy_source"] == "authorized_seed").sum()) if total else 0,
        "provisional_industry_theme_count": int((taxonomy["taxonomy_source"] == "provisional_industry_theme").sum()) if total else 0,
        "default_theme_map_count": int((taxonomy["taxonomy_source"] == "default_theme_map").sum()) if total else 0,
        "industry_default_count": int((taxonomy["taxonomy_source"] == "industry_default").sum()) if total else 0,
        "duplicate_stock_ids": int(taxonomy["stock_id"].duplicated().sum()) if total else 0,
        "missing_stock_name_count": int((taxonomy["stock_name"].astype(str).str.strip() == "").sum()) if total else 0,
        "missing_primary_theme_count": int((taxonomy["primary_theme"].astype(str).str.strip() == "").sum()) if total else 0,
    }


def write_outputs(taxonomy: pd.DataFrame, template: pd.DataFrame) -> None:
    write_csv(taxonomy, TAXONOMY_CSV)
    write_csv(taxonomy, DOCS_TAXONOMY_CSV)

    counts = validate(taxonomy)
    VALIDATION_JSON.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")
    DOCS_VALIDATION_JSON.parent.mkdir(parents=True, exist_ok=True)
    DOCS_VALIDATION_JSON.write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")

    review = taxonomy[taxonomy["theme_mainstream_label"].eq("theme_unknown") | taxonomy["primary_theme"].eq("")]
    lines = [
        "# Stock Theme Taxonomy",
        "",
        f"- generated_at: {now_text()}",
        f"- total_rows: {counts['total_rows']}",
        f"- mainstream_count: {counts['mainstream_count']}",
        f"- non_mainstream_count: {counts['non_mainstream_count']}",
        f"- effective_mainstream_count: {counts['effective_mainstream_count']}",
        f"- effective_non_mainstream_count: {counts['effective_non_mainstream_count']}",
        f"- mainstream_conflict_count: {counts['mainstream_conflict_count']}",
        f"- dual_report_membership_count: {counts['dual_report_membership_count']}",
        f"- mainstream_report_eligible_count: {counts['mainstream_report_eligible_count']}",
        f"- non_mainstream_report_eligible_count: {counts['non_mainstream_report_eligible_count']}",
        f"- unknown_count: {counts['unknown_count']}",
        f"- manual_override_count: {counts['manual_override_count']}",
        f"- authorized_seed_count: {counts['authorized_seed_count']}",
        "",
        "## Authorized Seed Preview",
        markdown_table(taxonomy[taxonomy["taxonomy_source"].isin(["manual_override", "authorized_seed"])], ["stock_id", "stock_name", "industry", "primary_theme", "secondary_themes", "structural_theme_bucket", "taxonomy_source"], 120),
        "",
        "## Mainstream Sample",
        markdown_table(taxonomy[taxonomy["effective_mainstream_label"].eq("core_mainstream")], ["stock_id", "stock_name", "industry", "primary_theme", "secondary_themes", "industry_mainstream_label", "theme_mainstream_label", "effective_mainstream_label"], 30),
        "",
        "## Non-Mainstream Sample",
        markdown_table(taxonomy[taxonomy["effective_mainstream_label"].eq("non_mainstream")], ["stock_id", "stock_name", "industry", "primary_theme", "secondary_themes", "industry_mainstream_label", "theme_mainstream_label", "effective_mainstream_label"], 30),
        "",
        "## Dual Industry / Theme Identity",
        markdown_table(taxonomy[taxonomy["dual_report_membership_flag"].eq("True")], ["stock_id", "stock_name", "industry", "primary_theme", "industry_mainstream_label", "theme_mainstream_label", "effective_mainstream_label", "report_line_memberships", "mainstream_report_eligible", "non_mainstream_report_eligible", "mainstream_conflict_note"], 80),
        "",
        "## Needs Review",
        markdown_table(review, ["stock_id", "stock_name", "industry", "primary_theme", "theme_mainstream_label", "taxonomy_source"], 60),
        "",
        "## Manual Fill Template",
        "- output/latest/stock_theme_manual_fill_template_latest.xlsx",
        "- Fill only 主流/非主流 and 主要族群1/族群2/族群3 when corrections are needed.",
        "- Blank theme fields keep the default taxonomy.",
        "",
    ]
    text = "\n".join(lines)
    TAXONOMY_MD.write_text(text, encoding="utf-8", newline="\n")
    DOCS_TAXONOMY_MD.write_text(text, encoding="utf-8", newline="\n")

    validation_md = [
        "# Stock Theme Taxonomy Validation",
        "",
        f"- generated_at: {counts['generated_at']}",
        f"- total_rows: {counts['total_rows']}",
        f"- mainstream_count: {counts['mainstream_count']}",
        f"- non_mainstream_count: {counts['non_mainstream_count']}",
        f"- effective_mainstream_count: {counts['effective_mainstream_count']}",
        f"- effective_non_mainstream_count: {counts['effective_non_mainstream_count']}",
        f"- mainstream_conflict_count: {counts['mainstream_conflict_count']}",
        f"- dual_report_membership_count: {counts['dual_report_membership_count']}",
        f"- mainstream_report_eligible_count: {counts['mainstream_report_eligible_count']}",
        f"- non_mainstream_report_eligible_count: {counts['non_mainstream_report_eligible_count']}",
        f"- unknown_count: {counts['unknown_count']}",
        f"- duplicate_stock_ids: {counts['duplicate_stock_ids']}",
        f"- missing_stock_name_count: {counts['missing_stock_name_count']}",
        f"- missing_primary_theme_count: {counts['missing_primary_theme_count']}",
        "",
        "Validation passes unless duplicate stock ids exist. Unknown theme is allowed but routed to theme_unknown.",
        "",
    ]
    validation_text = "\n".join(validation_md)
    VALIDATION_MD.write_text(validation_text, encoding="utf-8", newline="\n")
    DOCS_VALIDATION_MD.write_text(validation_text, encoding="utf-8", newline="\n")

    preview = taxonomy[taxonomy["taxonomy_source"].isin(["manual_override", "authorized_seed"])].copy()
    preview_cols = [
        "stock_id",
        "stock_name",
        "industry",
        "primary_theme",
        "secondary_themes",
        "structural_theme_bucket",
        "theme_mainstream_label",
        "industry_mainstream_label",
        "effective_mainstream_label",
        "mainstream_conflict_flag",
        "mainstream_conflict_note",
        "report_line_memberships",
        "mainstream_report_eligible",
        "non_mainstream_report_eligible",
        "dual_report_membership_flag",
        "report_line_membership_note",
        "taxonomy_source",
        "concept_tags",
        "notes",
    ]
    preview = preview.loc[:, [col for col in preview_cols if col in preview.columns]].sort_values(["primary_theme", "stock_id"])
    write_csv(preview, AUTHORIZED_PREVIEW_CSV)
    write_csv(preview, DOCS_AUTHORIZED_PREVIEW_CSV)
    preview_lines = [
        "# Stock Theme Authorized Seed Preview",
        "",
        f"- generated_at: {now_text()}",
        f"- rows: {len(preview)}",
        "- purpose: user-authorized market theme seed integrated with existing manual/default taxonomy.",
        "",
        markdown_table(preview, ["stock_id", "stock_name", "primary_theme", "secondary_themes", "structural_theme_bucket", "industry_mainstream_label", "theme_mainstream_label", "effective_mainstream_label", "report_line_memberships", "mainstream_report_eligible", "non_mainstream_report_eligible", "dual_report_membership_flag", "taxonomy_source"], 140),
        "",
    ]
    preview_text = "\n".join(preview_lines)
    AUTHORIZED_PREVIEW_MD.write_text(preview_text, encoding="utf-8", newline="\n")
    DOCS_AUTHORIZED_PREVIEW_MD.write_text(preview_text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows-per-sheet", type=int, default=500)
    args = parser.parse_args()
    taxonomy = build_taxonomy()
    template = build_template(taxonomy, rows_per_sheet=args.rows_per_sheet)
    write_outputs(taxonomy, template)
    counts = validate(taxonomy)
    if counts["duplicate_stock_ids"]:
        raise RuntimeError(f"duplicate stock ids: {counts['duplicate_stock_ids']}")
    print(f"Saved: {TAXONOMY_CSV} rows={len(taxonomy)}")
    print(f"Saved: {TEMPLATE_XLSX} rows={len(template)}")
    print(f"Saved: {VALIDATION_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
