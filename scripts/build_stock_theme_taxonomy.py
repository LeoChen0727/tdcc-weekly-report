from __future__ import annotations

import argparse
import json
import sys
from urllib.request import urlopen
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
COMPANY_INDUSTRY_SNAPSHOT = LATEST_DIR / "company_industry_snapshot_latest.csv"
DOCS_COMPANY_INDUSTRY_SNAPSHOT = DOCS_LATEST_DIR / "company_industry_snapshot_latest.csv"

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

TWSE_COMPANY_INFO_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap03_L"
TPEX_COMPANY_INFO_URL = "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O"

INDUSTRY_CODE_MAP = {
    "01": "水泥工業",
    "02": "食品工業",
    "03": "塑膠工業",
    "04": "紡織纖維",
    "05": "電機機械",
    "06": "電器電纜",
    "08": "玻璃陶瓷",
    "09": "造紙工業",
    "10": "鋼鐵工業",
    "11": "橡膠工業",
    "12": "汽車工業",
    "14": "建材營造",
    "15": "航運業",
    "16": "觀光餐旅",
    "17": "金融保險業",
    "18": "貿易百貨",
    "20": "其他業",
    "21": "化學工業",
    "22": "生技醫療業",
    "23": "油電燃氣業",
    "24": "半導體業",
    "25": "電腦及週邊設備業",
    "26": "光電業",
    "27": "通信網路業",
    "28": "電子零組件業",
    "29": "電子通路業",
    "30": "資訊服務業",
    "31": "其他電子業",
    "32": "文化創意業",
    "33": "農業科技",
    "34": "電子商務",
    "35": "綠能環保",
    "36": "數位雲端",
    "37": "運動休閒",
    "38": "居家生活",
}


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

# Clean UTF-8 taxonomy overrides.  The historical block above is kept for
# compatibility, but current pipeline decisions must be driven by readable
# Chinese labels and official listed-company industry fallback rules.
MAINSTREAM_VALUES = {
    "主流": "core_mainstream",
    "核心主流": "core_mainstream",
    "核心題材": "core_mainstream",
    "AI主流": "core_mainstream",
    "mainstream": "core_mainstream",
    "core_mainstream": "core_mainstream",
    "非主流": "non_mainstream",
    "傳產": "non_mainstream",
    "non_mainstream": "non_mainstream",
    "待分類": "theme_unknown",
    "未分類": "theme_unknown",
    "theme_unknown": "theme_unknown",
    "": "",
}

STRUCTURAL_BUCKET_BY_THEME_KEYWORD = {
    "AI伺服器": "ai_server_ipc_theme",
    "伺服器": "ai_server_ipc_theme",
    "AI server": "ai_server_ipc_theme",
    "IPC": "ai_server_ipc_theme",
    "工業電腦": "ai_server_ipc_theme",
    "AI PC": "ai_pc_consumer_theme",
    "AIPC": "ai_pc_consumer_theme",
    "PCB": "pcb_ccl_theme",
    "CCL": "pcb_ccl_theme",
    "ABF": "pcb_ccl_theme",
    "玻纖布": "glass_fiber_ccl_theme",
    "被動元件": "passive_component_theme",
    "MLCC": "passive_component_theme",
    "電感": "passive_component_theme",
    "電容": "passive_component_theme",
    "電阻": "passive_component_theme",
    "散熱": "thermal_solution_theme",
    "液冷": "thermal_solution_theme",
    "電源": "power_supply_theme",
    "BBU": "power_supply_theme",
    "重電": "power_grid_theme",
    "電網": "power_grid_theme",
    "低軌衛星": "low_earth_orbit_satellite_theme",
    "衛星": "low_earth_orbit_satellite_theme",
    "CPO": "network_optical_datacenter_theme",
    "光通訊": "network_optical_datacenter_theme",
    "網通": "network_optical_datacenter_theme",
    "交換器": "network_switch_theme",
    "記憶體": "memory_hbm_theme",
    "儲存": "memory_hbm_theme",
    "HBM": "memory_hbm_theme",
    "半導體設備": "semiconductor_equipment_material_theme",
    "半導體材料": "semiconductor_equipment_material_theme",
    "CoWoS": "advanced_packaging_theme",
    "先進封裝": "advanced_packaging_theme",
    "矽智財": "asic_advanced_process_theme",
    "ASIC": "asic_advanced_process_theme",
    "機器人": "robotics_precision_motion_theme",
    "自動化": "robotics_automation_theme",
    "精密傳動": "robotics_precision_motion_theme",
    "機器視覺": "robotics_optics_sensor_theme",
    "軍工": "defense_drone_theme",
    "無人機": "defense_drone_theme",
    "車用": "automotive_electronics_theme",
    "特化": "specialty_material_theme",
    "特殊材料": "specialty_material_theme",
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
    "semiconductor_general_theme",
    "electronic_component_general_theme",
    "electronics_channel_general_theme",
    "networking_general_theme",
    "optoelectronics_general_theme",
    "computer_peripheral_general_theme",
    "other_electronics_general_theme",
    "information_service_general_theme",
    "digital_cloud_general_theme",
}

NON_MAINSTREAM_INDUSTRY_KEYWORDS = [
    "金融保險",
    "航運",
    "紡織",
    "成衣",
    "營建",
    "建材營造",
    "鋼鐵",
    "化學",
    "塑膠",
    "橡膠",
    "玻璃陶瓷",
    "食品",
    "觀光",
    "貿易百貨",
    "水泥",
    "造紙",
    "油電燃氣",
    "生技醫療",
    "農業",
    "運動休閒",
    "居家生活",
    "文化創意",
    "綠能環保",
    "其他",
]

PROVISIONAL_INDUSTRY_RULES = [
    ("半導體業", "半導體業_待細分", "semiconductor_general_theme", "core_mainstream"),
    ("電子零組件業", "電子零組件業_待細分", "electronic_component_general_theme", "core_mainstream"),
    ("電子通路業", "電子通路業_待細分", "electronics_channel_general_theme", "core_mainstream"),
    ("通信網路業", "通信網路業_待細分", "networking_general_theme", "core_mainstream"),
    ("光電業", "光電業_待細分", "optoelectronics_general_theme", "core_mainstream"),
    ("電腦及週邊設備業", "電腦及週邊設備業_待細分", "computer_peripheral_general_theme", "core_mainstream"),
    ("其他電子業", "其他電子業_待細分", "other_electronics_general_theme", "core_mainstream"),
    ("資訊服務業", "資訊服務業_待細分", "information_service_general_theme", "core_mainstream"),
    ("數位雲端", "數位雲端_待細分", "digital_cloud_general_theme", "core_mainstream"),
    ("電機機械", "機器人自動化_電機機械待細分", "robotics_precision_motion_theme", "core_mainstream"),
    ("電器電纜", "重電電網_電器電纜待細分", "power_grid_theme", "core_mainstream"),
    ("金融保險", "金融保險業", "non_mainstream_theme", "non_mainstream"),
    ("航運", "航運業", "non_mainstream_theme", "non_mainstream"),
    ("紡織", "紡織纖維", "non_mainstream_theme", "non_mainstream"),
    ("成衣", "成衣服飾", "non_mainstream_theme", "non_mainstream"),
    ("建材營造", "建材營造", "non_mainstream_theme", "non_mainstream"),
    ("營建", "建材營造", "non_mainstream_theme", "non_mainstream"),
    ("鋼鐵", "鋼鐵工業", "non_mainstream_theme", "non_mainstream"),
    ("化學", "化學工業", "non_mainstream_theme", "non_mainstream"),
    ("塑膠", "塑膠工業", "non_mainstream_theme", "non_mainstream"),
    ("橡膠", "橡膠工業", "non_mainstream_theme", "non_mainstream"),
    ("食品", "食品工業", "non_mainstream_theme", "non_mainstream"),
    ("觀光", "觀光餐旅", "non_mainstream_theme", "non_mainstream"),
    ("貿易百貨", "貿易百貨", "non_mainstream_theme", "non_mainstream"),
    ("玻璃陶瓷", "玻璃陶瓷", "non_mainstream_theme", "non_mainstream"),
    ("水泥", "水泥工業", "non_mainstream_theme", "non_mainstream"),
    ("造紙", "造紙工業", "non_mainstream_theme", "non_mainstream"),
    ("油電燃氣", "油電燃氣業", "non_mainstream_theme", "non_mainstream"),
    ("生技醫療", "生技醫療業", "non_mainstream_theme", "non_mainstream"),
]

CORE_BUCKETS.update({bucket for _, _, bucket, label in PROVISIONAL_INDUSTRY_RULES if label == "core_mainstream"})

# Final ASCII-safe UTF-8 rule overrides.  These use unicode escapes so this file
# remains stable even when edited from tools with a non-UTF-8 console codepage.
MAINSTREAM_VALUES = {
    "\u4e3b\u6d41": "core_mainstream",
    "\u6838\u5fc3\u4e3b\u6d41": "core_mainstream",
    "\u6838\u5fc3\u984c\u6750": "core_mainstream",
    "AI\u4e3b\u6d41": "core_mainstream",
    "mainstream": "core_mainstream",
    "core_mainstream": "core_mainstream",
    "\u975e\u4e3b\u6d41": "non_mainstream",
    "\u50b3\u7522": "non_mainstream",
    "non_mainstream": "non_mainstream",
    "\u90fd\u6709": "both",
    "\u96d9\u91cd": "both",
    "\u4e3b\u6d41+\u975e\u4e3b\u6d41": "both",
    "\u4e3b\u6d41|\u975e\u4e3b\u6d41": "both",
    "mainstream|non_mainstream": "both",
    "both": "both",
    "\u5f85\u5206\u985e": "theme_unknown",
    "\u672a\u5206\u985e": "theme_unknown",
    "theme_unknown": "theme_unknown",
    "": "",
}

STRUCTURAL_BUCKET_BY_THEME_KEYWORD = {
    "AI\u4f3a\u670d\u5668": "ai_server_ipc_theme",
    "\u4f3a\u670d\u5668": "ai_server_ipc_theme",
    "AI server": "ai_server_ipc_theme",
    "IPC": "ai_server_ipc_theme",
    "\u5de5\u696d\u96fb\u8166": "ai_server_ipc_theme",
    "AI PC": "ai_pc_consumer_theme",
    "AIPC": "ai_pc_consumer_theme",
    "PCB": "pcb_ccl_theme",
    "CCL": "pcb_ccl_theme",
    "ABF": "pcb_ccl_theme",
    "\u73bb\u7e96\u5e03": "glass_fiber_ccl_theme",
    "\u88ab\u52d5\u5143\u4ef6": "passive_component_theme",
    "MLCC": "passive_component_theme",
    "\u96fb\u611f": "passive_component_theme",
    "\u96fb\u5bb9": "passive_component_theme",
    "\u96fb\u963b": "passive_component_theme",
    "\u6563\u71b1": "thermal_solution_theme",
    "\u6db2\u51b7": "thermal_solution_theme",
    "\u96fb\u6e90": "power_supply_theme",
    "BBU": "power_supply_theme",
    "\u91cd\u96fb": "power_grid_theme",
    "\u96fb\u7db2": "power_grid_theme",
    "\u4f4e\u8ecc\u885b\u661f": "low_earth_orbit_satellite_theme",
    "\u885b\u661f": "low_earth_orbit_satellite_theme",
    "CPO": "network_optical_datacenter_theme",
    "\u5149\u901a\u8a0a": "network_optical_datacenter_theme",
    "\u7db2\u901a": "network_optical_datacenter_theme",
    "\u4ea4\u63db\u5668": "network_switch_theme",
    "\u8a18\u61b6\u9ad4": "memory_hbm_theme",
    "\u5132\u5b58": "memory_hbm_theme",
    "HBM": "memory_hbm_theme",
    "\u534a\u5c0e\u9ad4\u8a2d\u5099": "semiconductor_equipment_material_theme",
    "\u534a\u5c0e\u9ad4\u6750\u6599": "semiconductor_equipment_material_theme",
    "CoWoS": "advanced_packaging_theme",
    "\u5148\u9032\u5c01\u88dd": "advanced_packaging_theme",
    "\u77fd\u667a\u8ca1": "asic_advanced_process_theme",
    "ASIC": "asic_advanced_process_theme",
    "\u6a5f\u5668\u4eba": "robotics_precision_motion_theme",
    "\u81ea\u52d5\u5316": "robotics_automation_theme",
    "\u7cbe\u5bc6\u50b3\u52d5": "robotics_precision_motion_theme",
    "\u6a5f\u5668\u8996\u89ba": "robotics_optics_sensor_theme",
    "\u8ecd\u5de5": "defense_drone_theme",
    "\u7121\u4eba\u6a5f": "defense_drone_theme",
    "\u8eca\u7528": "automotive_electronics_theme",
    "\u7279\u5316": "specialty_material_theme",
    "\u7279\u6b8a\u6750\u6599": "specialty_material_theme",
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
    "semiconductor_general_theme",
    "electronic_component_general_theme",
    "electronics_channel_general_theme",
    "networking_general_theme",
    "optoelectronics_general_theme",
    "computer_peripheral_general_theme",
    "other_electronics_general_theme",
    "information_service_general_theme",
    "digital_cloud_general_theme",
}

NON_MAINSTREAM_INDUSTRY_KEYWORDS = [
    "\u91d1\u878d\u4fdd\u96aa",
    "\u822a\u904b",
    "\u7d21\u7e54",
    "\u6210\u8863",
    "\u71df\u5efa",
    "\u5efa\u6750\u71df\u9020",
    "\u92fc\u9435",
    "\u5316\u5b78",
    "\u5851\u81a0",
    "\u6a61\u81a0",
    "\u73bb\u7483\u9676\u74f7",
    "\u98df\u54c1",
    "\u89c0\u5149",
    "\u8cbf\u6613\u767e\u8ca8",
    "\u6c34\u6ce5",
    "\u9020\u7d19",
    "\u6cb9\u96fb\u71c3\u6c23",
    "\u751f\u6280\u91ab\u7642",
    "\u8fb2\u696d",
    "\u904b\u52d5\u4f11\u9592",
    "\u5c45\u5bb6\u751f\u6d3b",
    "\u6587\u5316\u5275\u610f",
    "\u7da0\u80fd\u74b0\u4fdd",
    "\u5176\u4ed6",
]

PROVISIONAL_INDUSTRY_RULES = [
    ("semiconductor", "\u534a\u5c0e\u9ad4\u696d_\u5f85\u7d30\u5206", "semiconductor_general_theme", "core_mainstream"),
    ("power discrete", "\u534a\u5c0e\u9ad4\u696d_\u529f\u7387\u5143\u4ef6\u5f85\u7d30\u5206", "semiconductor_general_theme", "core_mainstream"),
    ("diodes", "\u534a\u5c0e\u9ad4\u696d_\u529f\u7387\u5143\u4ef6\u5f85\u7d30\u5206", "semiconductor_general_theme", "core_mainstream"),
    ("\u534a\u5c0e\u9ad4\u696d", "\u534a\u5c0e\u9ad4\u696d_\u5f85\u7d30\u5206", "semiconductor_general_theme", "core_mainstream"),
    ("\u96fb\u5b50\u96f6\u7d44\u4ef6\u696d", "\u96fb\u5b50\u96f6\u7d44\u4ef6\u696d_\u5f85\u7d30\u5206", "electronic_component_general_theme", "core_mainstream"),
    ("\u96fb\u5b50\u901a\u8def\u696d", "\u96fb\u5b50\u901a\u8def\u696d_\u5f85\u7d30\u5206", "electronics_channel_general_theme", "core_mainstream"),
    ("\u901a\u4fe1\u7db2\u8def\u696d", "\u901a\u4fe1\u7db2\u8def\u696d_\u5f85\u7d30\u5206", "networking_general_theme", "core_mainstream"),
    ("\u5149\u96fb\u696d", "\u5149\u96fb\u696d_\u5f85\u7d30\u5206", "optoelectronics_general_theme", "core_mainstream"),
    ("\u96fb\u8166\u53ca\u9031\u908a\u8a2d\u5099\u696d", "\u96fb\u8166\u53ca\u9031\u908a\u8a2d\u5099\u696d_\u5f85\u7d30\u5206", "computer_peripheral_general_theme", "core_mainstream"),
    ("\u5176\u4ed6\u96fb\u5b50\u696d", "\u5176\u4ed6\u96fb\u5b50\u696d_\u5f85\u7d30\u5206", "other_electronics_general_theme", "core_mainstream"),
    ("\u8cc7\u8a0a\u670d\u52d9\u696d", "\u8cc7\u8a0a\u670d\u52d9\u696d_\u5f85\u7d30\u5206", "information_service_general_theme", "core_mainstream"),
    ("\u6578\u4f4d\u96f2\u7aef", "\u6578\u4f4d\u96f2\u7aef_\u5f85\u7d30\u5206", "digital_cloud_general_theme", "core_mainstream"),
    ("\u96fb\u6a5f\u6a5f\u68b0", "\u6a5f\u5668\u4eba\u81ea\u52d5\u5316_\u96fb\u6a5f\u6a5f\u68b0\u5f85\u7d30\u5206", "robotics_precision_motion_theme", "core_mainstream"),
    ("\u96fb\u5668\u96fb\u7e9c", "\u91cd\u96fb\u96fb\u7db2_\u96fb\u5668\u96fb\u7e9c\u5f85\u7d30\u5206", "power_grid_theme", "core_mainstream"),
    ("\u91d1\u878d\u696d", "\u91d1\u878d\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u91d1\u878d\u4fdd\u96aa", "\u91d1\u878d\u4fdd\u96aa\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u6c7d\u8eca\u5de5\u696d", "\u6c7d\u8eca\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u822a\u904b", "\u822a\u904b\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u7d21\u7e54", "\u7d21\u7e54\u7e96\u7dad", "non_mainstream_theme", "non_mainstream"),
    ("\u6210\u8863", "\u6210\u8863\u670d\u98fe", "non_mainstream_theme", "non_mainstream"),
    ("\u5efa\u6750\u71df\u9020", "\u5efa\u6750\u71df\u9020", "non_mainstream_theme", "non_mainstream"),
    ("\u71df\u5efa", "\u5efa\u6750\u71df\u9020", "non_mainstream_theme", "non_mainstream"),
    ("\u92fc\u9435", "\u92fc\u9435\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u5316\u5b78", "\u5316\u5b78\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u5851\u81a0", "\u5851\u81a0\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u6a61\u81a0", "\u6a61\u81a0\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u98df\u54c1", "\u98df\u54c1\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u89c0\u5149", "\u89c0\u5149\u9910\u65c5", "non_mainstream_theme", "non_mainstream"),
    ("\u8cbf\u6613\u767e\u8ca8", "\u8cbf\u6613\u767e\u8ca8", "non_mainstream_theme", "non_mainstream"),
    ("\u73bb\u7483\u9676\u74f7", "\u73bb\u7483\u9676\u74f7", "non_mainstream_theme", "non_mainstream"),
    ("\u6c34\u6ce5", "\u6c34\u6ce5\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u9020\u7d19", "\u9020\u7d19\u5de5\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u6cb9\u96fb\u71c3\u6c23", "\u6cb9\u96fb\u71c3\u6c23\u696d", "non_mainstream_theme", "non_mainstream"),
    ("\u751f\u6280\u91ab\u7642", "\u751f\u6280\u91ab\u7642\u696d", "non_mainstream_theme", "non_mainstream"),
    ("91", "DR / 外國上市", "non_mainstream_theme", "non_mainstream"),
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
    return MAINSTREAM_VALUES.get(text, text if text in {"core_mainstream", "non_mainstream", "theme_unknown", "both"} else "")


THEME_DISPLAY_MAP = {
    "91": "DR / 外國上市",
    "DR_or_foreign_listing": "DR / 外國上市",
    "ETF_or_index_product": "指數 / ETF / ETN商品",
    "etf_or_index_product": "指數 / ETF / ETN商品",
    "指數/ETF/ETN商品": "指數 / ETF / ETN商品",
    "AI server supply chain": "AI伺服器",
    "industrial computer": "工業電腦",
    "computer peripherals": "電腦及週邊設備業",
    "electronic components": "電子零組件業",
    "passive components": "被動元件",
    "capacitors": "電容",
    "capacitor": "電容",
    "resistors": "電阻",
    "resistor": "電阻",
    "inductors": "電感",
    "inductor": "電感",
    "ceramic powder": "陶瓷粉末",
    "MLCC": "MLCC",
    "power discrete/diodes": "功率元件/二極體",
    "diodes": "二極體",
    "diode": "二極體",
    "MOSFET": "MOSFET",
    "semiconductor": "半導體業",
    "semiconductor equipment": "半導體設備",
    "semiconductor equipment/materials": "半導體設備材料",
    "semiconductor materials": "半導體材料",
    "IC distribution": "IC通路",
    "electronic distributors": "電子通路業",
    "foundry": "晶圓代工",
    "memory": "記憶體",
    "DRAM IC": "DRAM IC",
    "DRAM and flash": "DRAM/Flash",
    "IC design": "IC設計",
    "PCB/CCL": "PCB_CCL_ABF材料",
    "PCB": "PCB",
    "optical communication/CPO": "CPO光通訊",
    "optical components": "光通訊元件",
    "optical communication": "光通訊",
    "networking": "網通",
    "network equipment": "網通設備",
    "communications": "通信網路業",
    "wafer reclaim": "晶圓再生",
    "wet process": "濕製程設備",
    "automation equipment": "自動化設備",
    "consumer electronics": "消費性電子",
    "panel": "面板",
    "other electronics": "其他電子業",
    "solder materials": "焊錫材料",
    "electronic materials": "電子材料",
    "AI伺服器": "AI伺服器",
    "被動元件": "被動元件",
    "矽智財_ASIC": "矽智財_ASIC",
}


def display_theme(value: Any) -> str:
    text = compact_text(value)
    if not text:
        return ""
    return THEME_DISPLAY_MAP.get(text, text)


def display_theme_list(value: Any) -> str:
    return ";".join(display_theme(item) for item in split_themes(value))


def provisional_industry_rule(industry: str) -> tuple[str, str, str] | None:
    text = compact_text(industry)
    for keyword, primary_theme, bucket, mainstream_label in PROVISIONAL_INDUSTRY_RULES:
        if keyword in text:
            return primary_theme, bucket, mainstream_label
    return None


MISSING_INDUSTRY_FALLBACKS: dict[str, tuple[str, str, str, str]] = {
    # A few valid listed/TPEX names can miss the upstream industry snapshot.
    # Keep them explicit so the daily reports do not leak an unclassified bucket.
    "0200": ("\u6307\u6578/ETF/ETN\u5546\u54c1", "\u6307\u6578/ETF/ETN\u5546\u54c1", "non_mainstream_theme", "non_mainstream"),
    "1342": ("TPU材料 / 工業複合材料", "TPU材料 / 工業複合材料", "non_mainstream_theme", "non_mainstream"),
    "1438": ("建材營造", "建材營造", "non_mainstream_theme", "non_mainstream"),
    "2348": ("房地產代銷 / 建設服務", "房地產代銷 / 建設服務", "non_mainstream_theme", "non_mainstream"),
    "2809": ("\u91d1\u878d\u4fdd\u96aa\u696d", "\u91d1\u878d\u4fdd\u96aa\u696d", "non_mainstream_theme", "non_mainstream"),
    "2888": ("\u91d1\u878d\u4fdd\u96aa\u696d", "\u91d1\u878d\u4fdd\u96aa\u696d", "non_mainstream_theme", "non_mainstream"),
    "3454": ("\u5149\u96fb\u696d", "\u5b89\u63a7/\u667a\u6167\u5f71\u50cf", "non_mainstream_theme", "non_mainstream"),
    "3426": ("電機機械", "電機機械", "robotics_precision_motion_theme", "core_mainstream"),
    "4987": ("\u96fb\u8166\u53ca\u9031\u908a\u8a2d\u5099\u696d", "\u96fb\u8166\u53ca\u9031\u908a\u8a2d\u5099\u696d", "non_mainstream_theme", "non_mainstream"),
    "5871": ("租賃金融 / 企業融資", "租賃金融 / 企業融資", "non_mainstream_theme", "non_mainstream"),
    "6288": ("\u6c7d\u8eca\u5de5\u696d", "\u6c7d\u8eca\u96f6\u7d44\u4ef6", "non_mainstream_theme", "non_mainstream"),
    "6585": ("TPU材料 / 工業複合材料", "TPU材料 / 工業複合材料", "non_mainstream_theme", "non_mainstream"),
    "6747": ("\u751f\u6280\u91ab\u7642\u696d", "\u751f\u6280\u91ab\u7642\u696d", "non_mainstream_theme", "non_mainstream"),
    "6901": ("投資控股 / 創投", "投資控股 / 創投", "non_mainstream_theme", "non_mainstream"),
    "9907": ("包材 / 容器製造", "包材 / 容器製造", "non_mainstream_theme", "non_mainstream"),
    "9917": ("保全 / 智慧安防服務", "保全 / 智慧安防服務", "non_mainstream_theme", "non_mainstream"),
    "9933": ("工程承攬 / EPC服務", "工程承攬 / EPC服務", "non_mainstream_theme", "non_mainstream"),
    "9941": ("汽車金融 / 分期租賃", "汽車金融 / 分期租賃", "non_mainstream_theme", "non_mainstream"),
    "9945": ("建設營造 / 商用不動產", "建設營造 / 商用不動產", "non_mainstream_theme", "non_mainstream"),
}


GENERIC_INDUSTRY_VALUES = {
    "普通股",
    "普通股_待補官方產業",
    "其他",
    "其他業",
    "other",
    "unknown",
    "unclassified",
}


def is_generic_industry(value: Any) -> bool:
    return compact_text(value) in GENERIC_INDUSTRY_VALUES


def is_special_non_common_security(stock_id: Any, stock_name: Any = "") -> bool:
    code = normalize_code(stock_id)
    name = compact_text(stock_name)
    if not code:
        return False
    return (
        code.startswith("00")
        or code.startswith("02")
        or code.startswith("7")
        or code.startswith("91")
        or any(token in name for token in ["購", "售", "牛", "熊", "ETF", "ETN"])
    )


def active_company_stock_ids() -> set[str]:
    snapshot = read_csv(COMPANY_INDUSTRY_SNAPSHOT, dtype=str, keep_default_na=False)
    if snapshot.empty or "stock_id" not in snapshot.columns:
        return set()
    return {normalize_code(value) for value in snapshot["stock_id"] if normalize_code(value)}


def filter_inactive_common_stock_rows(df: pd.DataFrame, active_ids: set[str]) -> pd.DataFrame:
    if df.empty or "stock_id" not in df.columns or not active_ids:
        return df.copy()
    out = df.copy()
    names = out["stock_name"] if "stock_name" in out.columns else pd.Series([""] * len(out), index=out.index)
    stock_ids = out["stock_id"].map(normalize_code)
    keep = [
        bool(code)
        and (
            code in active_ids
            or is_special_non_common_security(code, names.iloc[pos] if pos < len(names) else "")
        )
        for pos, code in enumerate(stock_ids)
    ]
    return out.loc[keep].copy()


def missing_industry_fallback(stock_id: str, stock_name: str) -> tuple[str, str, str, str] | None:
    code = normalize_code(stock_id)
    name = compact_text(stock_name)
    if code in MISSING_INDUSTRY_FALLBACKS:
        return MISSING_INDUSTRY_FALLBACKS[code]
    if code.startswith("00"):
        theme = "指數 / ETF / ETN商品"
        return theme, theme, "non_mainstream_theme", "non_mainstream"
    if code.startswith("7") or any(token in name for token in ["\u8cfc", "\u552e", "\u725b", "\u718a"]):
        theme = "\u6b0a\u8b49/\u884d\u751f\u5546\u54c1"
        return theme, theme, "non_mainstream_theme", "non_mainstream"
    return None


def infer_bucket(primary_theme: str, secondary_themes: str, industry: str, fallback: str = "") -> str:
    if compact_text(fallback):
        return compact_text(fallback)
    theme_text = f"{primary_theme};{secondary_themes}"
    # Specific market themes must win over broad industry/generic tags.  For
    # example, 富喬/台玻/南亞 may also carry PCB/CCL or plastics context, but
    # the actionable theme here is glass fiber; passive components likewise
    # must not be diluted into generic electronic components.
    priority_rules = [
        (["ETF_or_index_product", "etf_or_index_product"], "non_mainstream_theme"),
        (["玻纖布", "glass fiber"], "glass_fiber_ccl_theme"),
        (["被動元件", "passive components", "capacitors", "capacitor", "MLCC", "電感", "電容", "電阻"], "passive_component_theme"),
    ]
    theme_lower = theme_text.lower()
    for keywords, bucket in priority_rules:
        if any(keyword.lower() in theme_lower for keyword in keywords):
            return bucket
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
    """Report routing uses theme first, then industry only as fallback.

    Anything still unresolved is routed to non-mainstream instead of a third
    "unknown" report bucket. Manual review can still improve the theme labels,
    but the daily reports must not drop these stocks from both mainstream and
    non-mainstream views.
    """
    theme = normalize_mainstream(theme_label)
    industry = normalize_mainstream(industry_label)
    if theme == "both":
        return "both"
    if theme in {"core_mainstream", "non_mainstream"}:
        return theme
    if industry in {"core_mainstream", "non_mainstream"}:
        return industry
    return "non_mainstream"


def mainstream_conflict_note(industry_label: str, theme_label: str, effective_label: str) -> tuple[str, str]:
    industry = normalize_mainstream(industry_label)
    theme = normalize_mainstream(theme_label)
    if theme == "both":
        return "True", f"manual_both;industry={industry or 'unknown'};theme=both;report_routing=both"
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
    if "both" in labels.values():
        memberships.extend(["mainstream", "non_mainstream"])
    if "core_mainstream" in labels.values():
        memberships.append("mainstream")
    if "non_mainstream" in labels.values():
        memberships.append("non_mainstream")
    if not memberships:
        memberships.append("non_mainstream")
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
        note = "non_mainstream_section"
    return {
        "report_line_memberships": "|".join(memberships),
        "mainstream_report_eligible": "True" if mainstream else "False",
        "non_mainstream_report_eligible": "True" if non_mainstream else "False",
        "dual_report_membership_flag": "True" if mainstream and non_mainstream else "False",
        "report_line_membership_note": note,
    }


MAINSTREAM_MEMBERSHIP_ZH = {
    "core_mainstream": "\u4e3b\u6d41",
    "non_mainstream": "\u975e\u4e3b\u6d41",
    "both": "\u90fd\u6709",
    "theme_unknown": "\u975e\u4e3b\u6d41",
    "": "\u975e\u4e3b\u6d41",
}


def mainstream_membership_zh(effective_label: str, membership: dict[str, str] | None = None) -> str:
    """User-facing report membership: 主流 / 非主流 / 都有.

    This is a display contract for reports and the manual Excel template.  It
    must be available in the taxonomy itself so later stages do not recreate
    routing logic or drop unclassified rows.
    """
    membership = membership or {}
    mainstream = compact_text(membership.get("mainstream_report_eligible", "")).lower() == "true"
    non_mainstream = compact_text(membership.get("non_mainstream_report_eligible", "")).lower() == "true"
    dual = compact_text(membership.get("dual_report_membership_flag", "")).lower() == "true"
    if dual or (mainstream and non_mainstream):
        return "\u90fd\u6709"
    if mainstream:
        return "\u4e3b\u6d41"
    if non_mainstream:
        return "\u975e\u4e3b\u6d41"
    return MAINSTREAM_MEMBERSHIP_ZH.get(normalize_mainstream(effective_label), "\u975e\u4e3b\u6d41")


def hot_theme_slots(primary_theme: Any, secondary_themes: Any, slot_count: int = 5) -> list[str]:
    """Return up to five user-facing hot theme labels for taxonomy outputs."""
    themes = [display_theme(item) for item in split_themes(primary_theme, secondary_themes)]
    themes = [theme for theme in themes if theme]
    themes = list(dict.fromkeys(themes))
    return (themes + [""] * slot_count)[:slot_count]


def decode_industry_code(value: str) -> str:
    code = compact_text(value)
    if not code:
        return ""
    code = code.zfill(2) if code.isdigit() and len(code) <= 2 else code
    return INDUSTRY_CODE_MAP.get(code, code)


def fetch_json_records(url: str) -> list[dict[str, Any]]:
    with urlopen(url, timeout=20) as response:
        data = response.read().decode("utf-8")
    records = json.loads(data)
    return records if isinstance(records, list) else []


def preserve_snapshot_industries(out: pd.DataFrame, snapshot_path: Path = COMPANY_INDUSTRY_SNAPSHOT) -> pd.DataFrame:
    if not snapshot_path.exists():
        return out
    snapshot = read_csv(snapshot_path, dtype=str, keep_default_na=False)
    if snapshot.empty or not {"stock_id", "industry"}.issubset(snapshot.columns):
        return out
    snapshot_by_id: dict[str, dict[str, str]] = {}
    for _, snapshot_row in snapshot.iterrows():
        code = normalize_code(snapshot_row.get("stock_id", ""))
        industry = compact_text(snapshot_row.get("industry", ""))
        if code and industry and not is_generic_industry(industry):
            snapshot_by_id[code] = {
                "stock_name": compact_text(snapshot_row.get("stock_name", "")),
                "industry": industry,
                "market": compact_text(snapshot_row.get("market", "")),
            }
    for idx, row in out.iterrows():
        code = normalize_code(row.get("stock_id", ""))
        industry = compact_text(row.get("industry", ""))
        snapshot_row = snapshot_by_id.get(code)
        if snapshot_row and (not industry or is_generic_industry(industry)):
            out.at[idx, "industry"] = snapshot_row["industry"]
            out.at[idx, "stock_name"] = compact_text(row.get("stock_name", "")) or snapshot_row["stock_name"]
            out.at[idx, "market"] = compact_text(row.get("market", "")) or snapshot_row["market"]
            out.at[idx, "industry_source"] = "snapshot_preserved_after_generic_official"
    return out


def merge_snapshot_rows_for_failed_official_sources(
    out: pd.DataFrame,
    failed_markets: set[str],
    snapshot_path: Path = COMPANY_INDUSTRY_SNAPSHOT,
) -> pd.DataFrame:
    """Preserve cached official rows when only part of the live source fails.

    TWSE and TPEx are fetched from separate endpoints.  A partial live fetch
    must not overwrite the company-industry snapshot with only the successful
    market, because that would make ordinary active stocks lose their basic
    industry classification for the rest of the daily pipeline.
    """

    failed = {compact_text(market).upper() for market in failed_markets if compact_text(market)}
    if out.empty or not failed or not snapshot_path.exists():
        return out

    snapshot = read_csv(snapshot_path, dtype=str, keep_default_na=False)
    required = {"stock_id", "industry", "market"}
    if snapshot.empty or not required.issubset(snapshot.columns):
        return out

    merged = out.copy()
    for col in ["stock_id", "stock_name", "industry", "market", "industry_source"]:
        if col not in merged.columns:
            merged[col] = ""
        if col not in snapshot.columns:
            snapshot[col] = ""

    fresh_ids = {normalize_code(value) for value in merged["stock_id"] if normalize_code(value)}
    snapshot_codes = snapshot["stock_id"].map(normalize_code)
    snapshot_markets = snapshot["market"].map(lambda value: compact_text(value).upper())
    missing_failed_market = snapshot_codes.ne("") & ~snapshot_codes.isin(fresh_ids) & snapshot_markets.isin(failed)
    fallback = snapshot.loc[missing_failed_market, ["stock_id", "stock_name", "industry", "market", "industry_source"]].copy()
    if fallback.empty:
        return merged

    fallback["industry_source"] = fallback["industry_source"].map(
        lambda value: (
            f"snapshot_fallback_after_partial_official_fetch:{compact_text(value)}"
            if compact_text(value)
            else "snapshot_fallback_after_partial_official_fetch"
        )
    )
    combined = pd.concat([merged, fallback], ignore_index=True)
    combined["stock_id"] = combined["stock_id"].map(normalize_code)
    return combined.drop_duplicates("stock_id", keep="first").sort_values("stock_id").reset_index(drop=True)


def load_official_company_industry() -> pd.DataFrame:
    """Load official TWSE/TPEx industry metadata.

    This is a best-effort enrichment layer.  If the network is unavailable,
    fall back to the last generated snapshot so taxonomy does not collapse
    into unclassified buckets.
    """
    rows: list[dict[str, str]] = []
    failed_markets: set[str] = set()
    sources = [
        (
            "TWSE",
            TWSE_COMPANY_INFO_URL,
            {
                "code": "公司代號",
                "name": "公司簡稱",
                "industry_code": "產業別",
            },
        ),
        (
            "TPEX",
            TPEX_COMPANY_INFO_URL,
            {
                "code": "SecuritiesCompanyCode",
                "name": "CompanyAbbreviation",
                "industry_code": "SecuritiesIndustryCode",
            },
        ),
    ]
    for market, url, fields in sources:
        try:
            records = fetch_json_records(url)
        except Exception as exc:
            print(f"WARNING: failed to fetch official company industry {market}: {exc}")
            failed_markets.add(market)
            continue
        for item in records:
            code = normalize_code(item.get(fields["code"], ""))
            if not code:
                continue
            industry = decode_industry_code(item.get(fields["industry_code"], ""))
            rows.append(
                {
                    "stock_id": code,
                    "stock_name": compact_text(item.get(fields["name"], "")),
                    "industry": industry,
                    "market": market,
                    "industry_source": f"official_{market.lower()}",
                }
            )

    if not rows and COMPANY_INDUSTRY_SNAPSHOT.exists():
        return read_csv(COMPANY_INDUSTRY_SNAPSHOT, dtype=str, keep_default_na=False)

    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=["stock_id", "stock_name", "industry", "market", "industry_source"])
    out = out.drop_duplicates("stock_id", keep="first").sort_values("stock_id").reset_index(drop=True)
    out = preserve_snapshot_industries(out)
    out = merge_snapshot_rows_for_failed_official_sources(out, failed_markets)
    write_csv(out, COMPANY_INDUSTRY_SNAPSHOT)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(out, DOCS_COMPANY_INDUSTRY_SNAPSHOT)
    return out


def load_universe() -> pd.DataFrame:
    rows: dict[str, dict[str, str]] = {}

    official = load_official_company_industry()
    if not official.empty:
        for _, row in official.iterrows():
            code = normalize_code(row.get("stock_id", ""))
            if not code:
                continue
            rows.setdefault(code, {"stock_id": code})
            rows[code]["stock_name"] = compact_text(row.get("stock_name", "")) or rows[code].get("stock_name", "")
            rows[code]["industry"] = compact_text(row.get("industry", "")) or rows[code].get("industry", "")
            rows[code]["market"] = compact_text(row.get("market", "")) or rows[code].get("market", "")
            rows[code]["industry_source"] = compact_text(row.get("industry_source", "")) or rows[code].get("industry_source", "")

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
    if "industry_source" not in universe.columns:
        universe["industry_source"] = ""
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
    rename.update(
        {
            "\u80a1\u7968\u4ee3\u865f": "stock_id",
            "\u80a1\u7968\u540d\u7a31": "stock_name",
            "\u4e0a\u5e02\u6ac3\u7522\u696d": "industry",
            "\u57fa\u672c\u65cf\u7fa4": "basic_theme",
            "\u57fa\u790e\u65cf\u7fa4": "basic_theme",
            "\u4e3b\u6d41/\u975e\u4e3b\u6d41": "theme_mainstream_label",
            "\u71b1\u9580\u65cf\u7fa41": "primary_theme",
            "\u71b1\u9580\u65cf\u7fa42": "theme_2",
            "\u71b1\u9580\u65cf\u7fa43": "theme_3",
            "\u71b1\u9580\u65cf\u7fa44": "theme_4",
            "\u71b1\u9580\u65cf\u7fa45": "theme_5",
            "\u65cf\u7fa41": "primary_theme",
            "\u65cf\u7fa42": "theme_2",
            "\u65cf\u7fa43": "theme_3",
            "\u5099\u8a3b": "notes",
        }
    )
    df = df.rename(columns={k: v for k, v in rename.items() if k in df.columns})
    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_code)
    return df


def build_taxonomy() -> pd.DataFrame:
    universe = load_universe()
    active_ids = active_company_stock_ids()
    universe = filter_inactive_common_stock_rows(universe, active_ids)
    default_map = load_default_map()
    authorized = filter_inactive_common_stock_rows(load_authorized_seed(), active_ids)
    manual = filter_inactive_common_stock_rows(load_manual(), active_ids)
    default_map = filter_inactive_common_stock_rows(default_map, active_ids)

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
        if "industry_source" not in seeded_universe.columns:
            seeded_universe["industry_source"] = ""
        universe = (
            seeded_universe.sort_values(["stock_id", "stock_name", "industry"])
            .groupby("stock_id", as_index=False)
            .agg(
                {
                    "stock_name": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
                    "industry": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
                    "market": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
                    "industry_source": lambda s: next((compact_text(x) for x in s if compact_text(x)), ""),
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
                "basic_theme",
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
                "basic_theme",
                "theme_mainstream_label",
                "primary_theme",
                "theme_2",
                "theme_3",
                "theme_4",
                "theme_5",
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
        manual_basic = compact_text(row.get("manual_basic_theme", ""))
        manual_primary = compact_text(row.get("manual_primary_theme", ""))
        authorized_primary = compact_text(row.get("authorized_primary_theme", ""))
        default_primary = compact_text(row.get("default_primary_theme", ""))
        provisional = provisional_industry_rule(industry)
        provisional_primary = provisional[0] if provisional else ""
        missing_fallback = missing_industry_fallback(stock_id, stock_name) if not industry or is_generic_industry(industry) else None
        if missing_fallback and not provisional:
            fallback_basic, fallback_primary, fallback_bucket, fallback_mainstream = missing_fallback
            industry = fallback_basic if is_generic_industry(industry) else (industry or fallback_basic)
            provisional = (fallback_primary, fallback_bucket, fallback_mainstream)
            provisional_primary = provisional[0]
        basic_theme = (
            manual_basic
            or industry
            or provisional_primary
            or manual_primary
            or authorized_primary
            or default_primary
            or "\u666e\u901a\u80a1_\u5f85\u88dc\u5b98\u65b9\u7522\u696d"
        )
        primary = manual_primary or authorized_primary or default_primary or provisional_primary or basic_theme
        secondary_list = split_themes(
            row.get("manual_theme_2", ""),
            row.get("manual_theme_3", ""),
            row.get("manual_theme_4", ""),
            row.get("manual_theme_5", ""),
            row.get("manual_secondary_themes", ""),
            row.get("authorized_secondary_themes", ""),
            row.get("default_secondary_themes", ""),
        )
        secondary = ";".join([item for item in secondary_list if item != primary])
        hot_theme_list = split_themes(manual_primary or authorized_primary or default_primary, secondary)
        hot_primary = hot_theme_list[0] if hot_theme_list else ""
        hot_secondary = ";".join(hot_theme_list[1:]) if len(hot_theme_list) > 1 else ""
        has_hot_theme = "True" if hot_theme_list else "False"
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
        if any(compact_text(row.get(col, "")) for col in ["manual_basic_theme", "manual_primary_theme", "manual_theme_mainstream_label", "manual_theme_2", "manual_theme_3", "manual_theme_4", "manual_theme_5"]):
            source = "manual_override"
        elif any(compact_text(row.get(col, "")) for col in ["authorized_primary_theme", "authorized_theme_mainstream_label", "authorized_structural_theme_bucket"]):
            source = "authorized_seed"
        elif provisional:
            source = "missing_industry_fallback" if missing_fallback else "provisional_industry_theme"
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
        industry = display_theme(industry)
        basic_theme = display_theme(basic_theme)
        primary = display_theme(primary)
        secondary = display_theme_list(secondary)
        hot_primary = display_theme(hot_primary)
        hot_secondary = display_theme_list(hot_secondary)
        hot_slots = hot_theme_slots(hot_primary, hot_secondary)
        concept_tags = display_theme_list(concept_tags)
        rows.append(
            {
                "stock_id": stock_id,
                "stock_name": stock_name,
                "industry": industry,
                "industry_source": compact_text(row.get("industry_source", "")),
                "basic_theme": basic_theme,
                "hot_primary_theme": hot_primary,
                "hot_secondary_themes": hot_secondary,
                "mainstream_membership": mainstream_membership_zh(effective_mainstream, membership),
                "hot_theme_1": hot_slots[0],
                "hot_theme_2": hot_slots[1],
                "hot_theme_3": hot_slots[2],
                "hot_theme_4": hot_slots[3],
                "hot_theme_5": hot_slots[4],
                "has_hot_theme": has_hot_theme,
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


def build_template(taxonomy: pd.DataFrame, rows_per_sheet: int = 500, write_files: bool = True) -> pd.DataFrame:
    """Build the user-fillable taxonomy workbook with simple readable columns."""
    basic_theme = taxonomy["basic_theme"] if "basic_theme" in taxonomy.columns else taxonomy.get("industry", pd.Series([""] * len(taxonomy)))
    if "mainstream_membership" in taxonomy.columns:
        mainstream_display = taxonomy["mainstream_membership"]
    else:
        mainstream_display = taxonomy.apply(
            lambda row: mainstream_membership_zh(
                row.get("effective_mainstream_label", ""),
                {
                    "mainstream_report_eligible": row.get("mainstream_report_eligible", ""),
                    "non_mainstream_report_eligible": row.get("non_mainstream_report_eligible", ""),
                    "dual_report_membership_flag": row.get("dual_report_membership_flag", ""),
                },
            ),
            axis=1,
        )
    hot_theme_columns = {
        f"hot_theme_{idx}": taxonomy[f"hot_theme_{idx}"] if f"hot_theme_{idx}" in taxonomy.columns else pd.Series([""] * len(taxonomy))
        for idx in range(1, 6)
    }
    if "dual_report_membership_flag" in taxonomy.columns:
        mainstream_display = mainstream_display.mask(taxonomy["dual_report_membership_flag"].astype(str).eq("True"), "都有")
    if "mainstream_membership" in taxonomy.columns:
        mainstream_display = taxonomy["mainstream_membership"]
    template = pd.DataFrame(
        {
            "\u80a1\u7968\u4ee3\u865f": taxonomy["stock_id"],
            "\u80a1\u7968\u540d\u7a31": taxonomy["stock_name"],
            "\u4e0a\u5e02\u6ac3\u7522\u696d": taxonomy["industry"],
            "\u57fa\u672c\u65cf\u7fa4": basic_theme,
            "\u4e3b\u6d41/\u975e\u4e3b\u6d41": mainstream_display,
            "\u71b1\u9580\u65cf\u7fa41": hot_theme_columns["hot_theme_1"],
            "\u71b1\u9580\u65cf\u7fa42": hot_theme_columns["hot_theme_2"],
            "\u71b1\u9580\u65cf\u7fa43": hot_theme_columns["hot_theme_3"],
            "\u71b1\u9580\u65cf\u7fa44": hot_theme_columns["hot_theme_4"],
            "\u71b1\u9580\u65cf\u7fa45": hot_theme_columns["hot_theme_5"],
            "\u5099\u8a3b": taxonomy["notes"],
        }
    )
    if not write_files:
        return template

    write_csv(template, TEMPLATE_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(template, DOCS_TEMPLATE_CSV)

    with pd.ExcelWriter(TEMPLATE_XLSX, engine="openpyxl") as writer:
        instructions = pd.DataFrame(
            [
                {
                    "\u6b04\u4f4d": "\u4e3b\u6d41/\u975e\u4e3b\u6d41",
                    "\u586b\u5beb\u65b9\u5f0f": "\u586b\u4e3b\u6d41\u3001\u975e\u4e3b\u6d41\u3001\u90fd\u6709\u6216\u7559\u7a7a\u3002\u7559\u7a7a\u6642\u7a0b\u5f0f\u4f7f\u7528\u65e2\u6709\u984c\u6750\u8207\u7522\u696d\u9810\u8a2d\u3002",
                },
                {
                    "\u6b04\u4f4d": "\u57fa\u672c\u65cf\u7fa4",
                    "\u586b\u5beb\u65b9\u5f0f": "\u6bcf\u6a94\u80a1\u7968\u90fd\u61c9\u6709\u4e00\u500b\u5e38\u614b\u5206\u985e\uff0c\u4f8b\u5982\u96fb\u6a5f\u6a5f\u68b0\u3001\u901a\u4fe1\u7db2\u8def\u3001\u5851\u81a0\u3001\u91d1\u878d\u4fdd\u96aa\u3002",
                },
                {
                    "\u6b04\u4f4d": "\u71b1\u9580\u65cf\u7fa41\uff5e\u71b1\u9580\u65cf\u7fa45",
                    "\u586b\u5beb\u65b9\u5f0f": "\u53ea\u586b\u8cc7\u91d1\u984c\u6750\u6216\u4f60\u8981\u7d0d\u5165\u71b1\u9580\u65cf\u7fa4\u6a21\u578b\u7684\u6a19\u7c64\uff0c\u4f8b\u5982\u6a5f\u5668\u4eba\u81ea\u52d5\u5316\u3001\u73bb\u7e96\u5e03\u3001\u4f4e\u8ecc\u885b\u661f\u3001\u88ab\u52d5\u5143\u4ef6\u3002\u7559\u7a7a\u6642\u4e0d\u9032\u5165\u71b1\u9580\u65cf\u7fa4\u56de\u6a94\u6a21\u578b\u3002",
                },
                {
                    "\u6b04\u4f4d": "\u5099\u8a3b",
                    "\u586b\u5beb\u65b9\u5f0f": "\u9700\u8981\u8aaa\u660e\u4f86\u6e90\u6216\u4f8b\u5916\u6642\u586b\u3002",
                },
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
                ws.column_dimensions[letter].width = 16 if letter in {"A", "B", "C", "D", "E"} else 22
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
