# Stock Theme Taxonomy

- generated_at: `2026-05-29 23:50:53 Asia/Taipei`
- rows: `180`
- purpose: program-side market theme taxonomy. This overrides legacy industry for theme grouping.
- priority: manual `data/theme_events/stock_theme_taxonomy.csv` > `company_theme_mapping.csv` > `config/stock_theme_map.csv`.
- rule: `primary_theme` / `structural_theme_bucket` / `theme_structural_status` are the authoritative fields for mainstream/non-mainstream split.
- rule: industry is secondary context only.

## Primary Theme Counts

- 被動元件: `16`
- 低軌衛星: `16`
- 半導體設備/材料: `16`
- 光通訊/CPO: `11`
- 記憶體/HBM: `11`
- PCB/CCL: `9`
- 機器人/精密傳動: `7`
- 半導體: `6`
- 散熱: `5`
- 高速傳輸/連接器: `5`
- 機器人/自動化: `5`
- 玻纖布/CCL: `5`
- ABF載板/IC載板: `4`
- AI伺服器: `4`
- 車用電子/EV: `3`
- 電源供應鏈: `3`
- 機器人/工業電腦: `3`
- ASIC/先進製程: `3`
- 網通/光通訊: `2`
- 網通/通訊: `2`
- 機器人/光學感測: `2`
- AI PC/消費電子: `2`
- AI伺服器/機殼: `2`
- 半導體測試介面: `2`
- AI PC/電競: `2`
- FPC/軟板: `2`
- 封測/驅動IC: `1`
- 防衛/無人機: `1`
- AI伺服器/機構件: `1`
- AI伺服器/工業電腦: `1`

## Required Examples

- 三集瑞-KY、國巨、凱美、華新科、信昌電、臺慶科、光頡、蜜望實：被動元件。
- 大銀微系統、上銀、直得、全球傳動：機器人/精密傳動。
- 華通、啟碁、正文：低軌衛星。
- 富喬、建榮、南亞、台玻、德宏：玻纖布/CCL。

## Rows

| stock_id | stock_name | official_industry | primary_theme | structural_theme_bucket | theme_structural_status | confidence | taxonomy_source | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3037 | 欣興 | 電子零組件 | ABF載板/IC載板 | abf_substrate_theme | core_mainstream_theme | high | manual_theme_taxonomy | ABF載板主流題材，不與一般PCB混同 |
| 3189 | 景碩 | 電子零組件 | ABF載板/IC載板 | abf_substrate_theme | core_mainstream_theme | high | manual_theme_taxonomy | ABF載板主流題材，不與一般PCB混同 |
| 4958 | 臻鼎-KY | 電子零組件 | ABF載板/IC載板 | abf_substrate_theme | core_mainstream_theme | high | manual_theme_taxonomy | 高階PCB與ABF題材交集，ABF需獨立觀察 |
| 8046 | 南電 | 電子零組件 | ABF載板/IC載板 | abf_substrate_theme | core_mainstream_theme | high | manual_theme_taxonomy | ABF載板主流題材，不與一般PCB混同 |
| 2353 | 宏碁 | 電腦週邊 | AI PC/品牌通路 | ai_pc_consumer_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2324 | 仁寶 | 電腦週邊 | AI PC/消費電子 | ai_pc_consumer_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 4938 | 和碩 | 電腦週邊 | AI PC/消費電子 | ai_pc_consumer_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2357 | 華碩 | 電腦週邊 | AI PC/電競 | ai_pc_consumer_theme | core_mainstream_theme | medium | manual_theme_taxonomy | AI PC與電競觀察 |
| 2377 | 微星 | 電腦週邊 | AI PC/電競 | ai_pc_consumer_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2356 | 英業達 | 電腦週邊 | AI伺服器 | ai_server_ipc_theme | core_mainstream_theme | medium | manual_theme_taxonomy | AI伺服器供應鏈觀察 |
| 2382 | 廣達 | 電腦週邊 | AI伺服器 | ai_server_ipc_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI伺服器主流供應鏈 |
| 3231 | 緯創 | 電腦週邊 | AI伺服器 | ai_server_ipc_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI伺服器主流供應鏈 |
| 6669 | 緯穎 | 電腦週邊 | AI伺服器 | ai_server_ipc_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI伺服器主流供應鏈 |
| 2376 | 技嘉 | 電腦週邊 | AI伺服器/AI PC | ai_server_pc_theme | core_mainstream_theme | medium | manual_theme_taxonomy | AI伺服器/AI PC交集 |
| 4916 | 事欣科 | computer peripherals | AI伺服器/工業電腦 | ai_server_ipc_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=AI_server_theme;IPC_theme;gaming;server |
| 6235 | 華孚 | 電腦週邊 | AI伺服器/機構件 | ai_server_mechanical_theme | core_mainstream_theme | medium | manual_theme_taxonomy | AI機構件觀察 |
| 3013 | 晟銘電 | 電子零組件 | AI伺服器/機殼 | ai_server_mechanical_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8210 | 勤誠 | 電腦週邊 | AI伺服器/機殼 | ai_server_mechanical_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI伺服器機殼供應鏈 |
| 2449 | 京元電子 | 半導體 | AI晶片測試 | ai_chip_testing_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3035 | 智原 | 半導體 | ASIC/先進製程 | asic_advanced_process_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3443 | 創意 | 半導體 | ASIC/先進製程 | asic_advanced_process_theme | core_mainstream_theme | high | manual_theme_taxonomy | ASIC/先進製程觀察 |
| 3661 | 世芯-KY | 半導體 | ASIC/先進製程 | asic_advanced_process_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6153 | 嘉聯益 | 電子零組件 | FPC/軟板 | fpc_flexible_pcb_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6269 | 台郡 | 電子零組件 | FPC/軟板 | fpc_flexible_pcb_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2355 | 敬鵬 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | medium | manual_theme_taxonomy | PCB族群觀察 |
| 2368 | 金像電 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 高階PCB/AI伺服器板 |
| 3044 | 健鼎 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 5439 | 高技 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | medium | manual_theme_taxonomy | PCB族群觀察 |
| 5464 | 霖宏 | PCB | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=PCB_CCL_theme |
| 5469 | 瀚宇博 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6108 | 競國 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6213 | 聯茂 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | CCL材料 |
| 6274 | 台燿 | 電子零組件 | PCB/CCL | pcb_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 高階CCL材料 |
| 3715 | 定穎投控 | 電子零組件 | PCB/車用高頻板 | pcb_ccl_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2313 | 華通 | PCB | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；華通可同時屬PCB與低軌衛星 |
| 2314 | 台揚 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | 低軌衛星通訊設備觀察 |
| 2367 | 燿華 | PCB | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | 低軌衛星PCB觀察 |
| 2462 | 良得電 | 電子零組件 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | low | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2485 | 兆赫 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | low | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3105 | 穩懋 | 半導體 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3138 | 耀登 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3491 | 昇達科 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | 低軌衛星射頻供應鏈 |
| 3596 | 智易 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 4906 | 正文 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 低軌衛星/網通觀察 |
| 5388 | 中磊 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6152 | 百一 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6271 | 同欣電 | 半導體 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6284 | 佳邦 | 電子零組件 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | low | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6285 | 啟碁 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | 低軌衛星/網通供應鏈 |
| 8011 | 台通 | 通信網路 | 低軌衛星 | low_earth_orbit_satellite_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3711 | 日月光投控 | 半導體 | 先進封裝/CoWoS | advanced_packaging_cowos_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3081 | 聯亞 | 半導體 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光通訊上游觀察 |
| 3163 | 波若威 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光通訊族群 |
| 3234 | 光環 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 光通訊觀察 |
| 3363 | 上詮 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光通訊/CPO供應鏈 |
| 3450 | 聯鈞 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光通訊/CPO主流題材 |
| 3454 | 晶睿 | 光電 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | low | manual_theme_taxonomy | 低信心光通訊/網通交集觀察 |
| 4908 | 前鼎 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 光通訊觀察 |
| 4977 | 眾達-KY | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光收發模組觀察 |
| 4979 | 華星光 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光通訊族群 |
| 6442 | 光聖 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | high | manual_theme_taxonomy | 光通訊族群 |
| 6530 | 創威 | 通信網路 | 光通訊/CPO | optical_communication_cpo_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2481 | 強茂 | semiconductor | 半導體 | semiconductor_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=power_discrete_theme;diodes;diode;power discrete |
| 3033 | 威健 | electronic distributors | 半導體 | semiconductor_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=semiconductor_theme;IC distribution |
| 3048 | 益登 | electronic distributors | 半導體 | semiconductor_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=semiconductor_theme;IC distribution |
| 3707 | 漢磊 | semiconductor | 半導體 | semiconductor_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=semiconductor_theme;foundry;compound semiconductor |
| 5425 | 台半 | semiconductor | 半導體 | semiconductor_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=power_discrete_theme;diodes;diode;power discrete |
| 8261 | 富鼎 | semiconductor | 半導體 | semiconductor_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=power_discrete_theme;MOSFET;power discrete |
| 3264 | 欣銓 | 半導體 | 半導體測試 | semiconductor_testing_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6223 | 旺矽 | 半導體 | 半導體測試介面 | semiconductor_test_interface_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6510 | 精測 | 半導體 | 半導體測試介面 | semiconductor_test_interface_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3131 | 弘塑 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | high | manual_theme_taxonomy | 半導體設備材料主流供應鏈 |
| 3167 | 大量 | 電機機械 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3413 | 京鼎 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 半導體設備觀察 |
| 3498 | 陽程 | semiconductor equipment | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=semiconductor_equipment_theme;automation equipment;automation;equipment |
| 3563 | 牧德 | 光電 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3583 | 辛耘 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | high | manual_theme_taxonomy | 半導體設備材料主流供應鏈 |
| 3680 | 家登 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 半導體設備材料觀察 |
| 4770 | 上品 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 半導體材料觀察 |
| 5443 | 均豪 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 半導體設備觀察 |
| 5536 | 聖暉 | 其他電子 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6139 | 亞翔 | 其他電子 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6187 | 萬潤 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | high | manual_theme_taxonomy | 半導體設備材料主流供應鏈 |
| 6196 | 帆宣 | 其他電子 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6640 | 均華 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 半導體設備觀察 |
| 6667 | 信紘科 | 其他電子 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8028 | 昇陽半導體 | 半導體 | 半導體設備/材料 | semiconductor_equipment_material_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 半導體服務/材料觀察 |
| 8150 | 南茂 | 半導體 | 封測/驅動IC | packaging_testing_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8114 | 振樺電 | 電腦週邊 | 工業電腦/特殊應用 | ipc_special_application_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6789 | 采鈺 | 半導體 | 影像感測/先進封裝 | cis_advanced_packaging_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3227 | 原相 | 半導體 | 感測IC/機器人 | sensor_ic_robotics_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3017 | 奇鋐 | 其他電子 | 散熱 | thermal_solution_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI散熱主流供應鏈 |
| 3324 | 雙鴻 | 其他電子 | 散熱 | thermal_solution_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI散熱主流供應鏈 |
| 3338 | 泰碩 | 電子零組件 | 散熱 | thermal_solution_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3483 | 力致 | 電腦週邊 | 散熱 | thermal_solution_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6230 | 尼得科超眾 | 電腦週邊 | 散熱 | thermal_solution_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3653 | 健策 | 電子零組件 | 散熱/機構件 | thermal_mechanical_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI散熱/機構件供應鏈 |
| 8996 | 高力 | 電機機械 | 散熱/能源設備 | thermal_energy_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2317 | 鴻海 | 其他電子 | 機器人/AI製造 | robotics_ai_manufacturing_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2374 | 佳能 | 光電 | 機器人/光學感測 | robotics_optics_sensor_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 族群優先於官方產業；佳能屬機器人光學感測/機器視覺供應鏈 |
| 3019 | 亞光 | 光電 | 機器人/光學感測 | robotics_optics_sensor_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人光學感測觀察 |
| 4585 | 達明 | 電機機械 | 機器人/協作機器人 | robotics_collaborative_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2365 | 昆盈 | 電腦週邊 | 機器人/周邊零組件 | robotics_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2395 | 研華 | 電腦週邊 | 機器人/工業電腦 | robotics_ipc_edge_ai_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6166 | 凌華 | 電腦週邊 | 機器人/工業電腦 | robotics_ipc_edge_ai_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6414 | 樺漢 | 電腦週邊 | 機器人/工業電腦 | robotics_ipc_edge_ai_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2354 | 鴻準 | 其他電子 | 機器人/機構件 | robotics_mechanical_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 1590 | 亞德客-KY | 電機機械 | 機器人/氣動自動化 | robotics_automation_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；亞德客-KY屬機器人與工業自動化供應鏈 |
| 1597 | 直得 | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人精密傳動觀察 |
| 2049 | 上銀 | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；機器人與精密傳動代表股 |
| 3813 | 大銀微系統 | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | high | manual_theme_taxonomy | 同名歷史代號/資料相容列 |
| 4540 | 全球傳動 | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人精密傳動觀察 |
| 4571 | 鈞興-KY | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人精密傳動觀察 |
| 4576 | 大銀微系統 | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；與上銀同屬精密傳動/機器人供應鏈 |
| 4583 | 台灣精銳 | 電機機械 | 機器人/精密傳動 | robotics_precision_motion_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人精密傳動觀察 |
| 2250 | IKKA-KY | 汽車零組件 | 機器人/精密零組件 | robotics_precision_motion_theme | core_mainstream_theme | low | manual_theme_taxonomy | 低信心機器人零組件觀察 |
| 2359 | 所羅門 | 其他電子 | 機器人/自動化 | robotics_automation_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人系統整合觀察 |
| 2464 | 盟立 | 其他電子 | 機器人/自動化 | robotics_automation_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人自動化設備觀察 |
| 6188 | 廣明 | 電腦週邊 | 機器人/自動化 | robotics_automation_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6215 | 和椿 | 其他電子 | 機器人/自動化 | robotics_precision_motion_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人自動化觀察 |
| 8374 | 羅昇 | 電機機械 | 機器人/自動化 | robotics_automation_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 機器人自動化元件觀察 |
| 6125 | 廣運 | 電機機械 | 機器人/自動化設備 | robotics_automation_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3481 | 群創 | optoelectronics | 消費性電子/面板 | consumer_electronics_display_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=consumer electronics;panel;display |
| 1303 | 南亞 | 塑膠工業 | 玻纖布/CCL | glass_fiber_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；南亞可歸玻纖布/CCL題材 |
| 1802 | 台玻 | 玻璃陶瓷 | 玻纖布/CCL | glass_fiber_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；台玻可歸玻纖布/CCL題材 |
| 1815 | 富喬 | 電子零組件 | 玻纖布/CCL | glass_fiber_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 玻纖布主流題材 |
| 5340 | 建榮 | 電子零組件 | 玻纖布/CCL | glass_fiber_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 玻纖布主流題材 |
| 5475 | 德宏 | 電子零組件 | 玻纖布/CCL | glass_fiber_ccl_theme | core_mainstream_theme | high | manual_theme_taxonomy | 玻纖布主流題材 |
| 2345 | 智邦 | 通信網路 | 網通/光通訊 | network_optical_datacenter_theme | core_mainstream_theme | high | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3380 | 明泰 | 通信網路 | 網通/光通訊 | network_optical_datacenter_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3704 | 合勤控 | 通信網路 | 網通/通訊 | network_communication_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6546 | 正基 | 通信網路 | 網通/通訊 | network_communication_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2327 | 國巨 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 被動元件族群 |
| 2375 | 凱美 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 被動元件族群 |
| 2456 | 奇力新 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 被動元件/電感歷史觀察 |
| 2472 | 立隆電 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2492 | 華新科 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 被動元件族群 |
| 3026 | 禾伸堂 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3090 | 日電貿 | 電子通路 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3357 | 臺慶科 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 被動元件/電感 |
| 3624 | 光頡 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 被動元件/電阻 |
| 6127 | 九豪 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6173 | 信昌電 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 被動元件上游 |
| 6175 | 立敦 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6207 | 雷科 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6862 | 三集瑞-KY | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | high | manual_theme_taxonomy | 族群優先於官方產業；被動元件/電感 |
| 8042 | 金山電 | electronic components | 被動元件 | passive_component_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=passive_component_theme;capacitors;capacitor |
| 8043 | 蜜望實 | 電子零組件 | 被動元件 | passive_component_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 被動元件通路觀察 |
| 2344 | 華邦電 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | high | manual_theme_taxonomy | 記憶體族群 |
| 2408 | 南亞科 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | high | manual_theme_taxonomy | 記憶體族群 |
| 2451 | 創見 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 記憶體模組觀察 |
| 3006 | 晶豪科 | semiconductor | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=memory_theme;DRAM IC;DRAM |
| 3260 | 威剛 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 記憶體模組觀察 |
| 4967 | 十銓 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 記憶體模組觀察 |
| 5351 | 鈺創 | semiconductor | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=memory_theme;DRAM IC;IC design |
| 6485 | 點序 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8088 | 品安 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8271 | 宇瞻 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8299 | 群聯 | 半導體 | 記憶體/HBM | memory_hbm_theme | core_mainstream_theme | high | manual_theme_taxonomy | 記憶體/儲存控制IC |
| 6239 | 力成 | 半導體 | 記憶體封測 | memory_packaging_testing_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 1536 | 和大 | 電機機械 | 車用電子/EV | automotive_ev_theme | non_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3552 | 同致 | 電子零組件 | 車用電子/EV | automotive_ev_theme | non_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6279 | 胡連 | 電子零組件 | 車用電子/EV | automotive_ev_theme | non_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 8033 | 雷虎 | 其他電子 | 防衛/無人機 | defense_drone_theme | non_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2634 | 漢翔 | 航運業 | 防衛/航太 | defense_aerospace_theme | non_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 6753 | 龍德造船 | 航運業 | 防衛/造船 | defense_shipbuilding_theme | non_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3305 | 昇貿 | electronic materials | 電子材料 | electronic_material_theme | core_mainstream_theme | medium | company_theme_mapping_auto | auto mapped from theme_tags=other electronics;solder materials;solder;materials |
| 2301 | 光寶科 | 電子零組件 | 電源/光電 | power_supply_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 電源供應鏈觀察 |
| 2308 | 台達電 | 電子零組件 | 電源/散熱 | power_supply_theme | core_mainstream_theme | high | manual_theme_taxonomy | AI電源與散熱主流供應鏈 |
| 2420 | 新巨 | 電子零組件 | 電源供應鏈 | power_supply_theme | core_mainstream_theme | high | manual_theme_taxonomy | 電源供應鏈 |
| 3015 | 全漢 | 電子零組件 | 電源供應鏈 | power_supply_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 電源供應鏈觀察 |
| 6412 | 群電 | 電子零組件 | 電源供應鏈 | power_supply_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 電源供應鏈觀察 |
| 4961 | 天鈺 | 半導體 | 驅動IC/AI邊緣 | driver_power_ic_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 2383 | 台光電 | 電子零組件 | 高速CCL/低軌衛星 | high_speed_ccl_satellite_theme | core_mainstream_theme | high | manual_theme_taxonomy | 可同時屬高階CCL與低軌衛星材料供應鏈 |
| 2392 | 正崴 | 電子零組件 | 高速傳輸/連接器 | high_speed_interconnect_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3023 | 信邦 | 電子零組件 | 高速傳輸/連接器 | high_speed_interconnect_theme | core_mainstream_theme | medium | manual_theme_taxonomy | 連接器觀察 |
| 3533 | 嘉澤 | 電子零組件 | 高速傳輸/連接器 | high_speed_interconnect_theme | core_mainstream_theme | high | manual_theme_taxonomy | 高速連接器主流供應鏈 |
| 3605 | 宏致 | 電子零組件 | 高速傳輸/連接器 | high_speed_interconnect_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
| 3665 | 貿聯-KY | 電子零組件 | 高速傳輸/連接器 | high_speed_interconnect_theme | core_mainstream_theme | high | manual_theme_taxonomy | 高速傳輸/連接器主流供應鏈 |
| 4966 | 譜瑞-KY | 半導體 | 高速傳輸IC | high_speed_ic_theme | core_mainstream_theme | medium | manual_theme_taxonomy | market theme taxonomy expansion; market theme overrides exchange industry |
