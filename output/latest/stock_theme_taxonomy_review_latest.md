# Stock Theme Taxonomy Review

- generated_at: 2026-05-29 23:50:54 Asia/Taipei
- source_candidates: output/latest/all_candidates_latest.csv
- source_taxonomy: output/latest/stock_theme_taxonomy_latest.csv

## Usage

- `needs_market_theme_mapping`: today has a signal but no usable market-theme taxonomy. Do not route to the main attack list until reviewed.
- `industry_core_needs_market_theme`: official industry is electronic/semiconductor-like, but market theme is still missing. This is not enough for mainstream routing.
- `core_ai_related_theme`: explicitly mapped to AI/electronics/robotics/passive/PCB/LEO/optical/semiconductor theme buckets.
- `industry_non_mainstream_only`: official industry is non-mainstream and no market-theme override exists.
- `non_mainstream_theme`: explicitly mapped to a non-core/non-AI market theme.
- `mapped_needs_review`: mapped but low confidence or outside the core bucket list.

## Summary

| taxonomy_review_status           |   count |
|:---------------------------------|--------:|
| core_ai_related_theme            |     133 |
| industry_core_needs_market_theme |     259 |
| industry_non_mainstream_only     |     211 |
| mapped_needs_review              |       5 |
| non_mainstream_theme             |       1 |


## Needs Market Theme Mapping

_No rows._

## Industry Core But Market Theme Missing

|   stock_id | stock_name   | industry         | category         | decision_priority   | risk_handling_bucket        | effective_primary_theme   | effective_structural_theme_bucket   | effective_confidence   |
|-----------:|:-------------|:-----------------|:-----------------|:--------------------|:----------------------------|:--------------------------|:------------------------------------|:-----------------------|
|       3311 | 閎暉         | 通信網路業       | range_rebound    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       3050 | 鈺德         | 光電業           | range_rebound    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       6224 | 聚鼎         | 電子零組件業     | range_rebound    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       3027 | 盛達         | 通信網路業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8070 | 長華*        | 電子通路業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4545 | 銘鈺         | 電子零組件業     | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2425 | 承啟         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2419 | 仲琦         | 通信網路業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6438 | 迅得         | 其他電子業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6672 | 騰輝電子-KY  | 電子零組件業     | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2332 | 友訊         | 通信網路業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1582 | 信錦         | 電子零組件業     | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6206 | 飛捷         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3356 | 奇偶         | 光電業           | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3060 | 銘異         | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2425 | 承啟         | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3591 | 艾笛森       | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8213 | 志超         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2438 | 翔耀         | 光電業           | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3030 | 德律         | 其他電子業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5309 | 系統電       | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6104 | 創惟         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6226 | 光鼎         | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2342 | 茂矽         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6202 | 盛群         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6438 | 迅得         | 其他電子業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2347 | 聯強         | 電子通路業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3028 | 增你強       | 電子通路業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3406 | 玉晶光       | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6209 | 今國光       | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3356 | 奇偶         | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3031 | 佰鴻         | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6206 | 飛捷         | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6116 | 彩晶         | 光電業           | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3588 | 通嘉         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6438 | 迅得         | 其他電子業       | pullback_rebound | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2426 | 鼎元         | 光電業           | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3518 | 柏騰         | 其他電子業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       7769 | 鴻勁         | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8162 | 微矽電子-創  | 半導體業         | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4949 | 有成精密     | 光電業           | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6573 | 虹揚-KY      | 半導體業         | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2406 | 國碩         | 光電業           | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2467 | 志聖         | 電子零組件業     | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4934 | 太極         | 光電業           | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3702 | 大聯大       | 電子通路業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2363 | 矽統         | 半導體業         | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6426 | 統新         | 通信網路業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2465 | 麗臺         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3406 | 玉晶光       | 光電業           | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8021 | 尖點         | 其他電子業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3066 | 李洲         | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3550 | 聯穎         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4749 | 新應材       | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4931 | 新盛力       | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4976 | 佳凌         | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5452 | 佶優         | 其他電子業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5471 | 松翰         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6126 | 信音         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6411 | 晶焱         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6451 | 訊芯-KY      | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6462 | 神盾         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8249 | 菱光         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6830 | 汎銓         | 其他電子業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2363 | 矽統         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3217 | 優群         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2352 | 佳世達       | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2385 | 群光         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3390 | 旭軟         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3030 | 德律         | 其他電子業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3059 | 華晶科       | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5371 | 中光電       | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2476 | 鉅祥         | 電子零組件業     | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3003 | 健和興       | 電子零組件業     | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3550 | 聯穎         | 電子零組件業     | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2455 | 全新         | 通信網路業       | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6282 | 康舒         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2362 | 藍天         | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3045 | 台灣大       | 通信網路業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5471 | 松翰         | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2379 | 瑞昱         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3592 | 瑞鼎         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8109 | 博大         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2498 | 宏達電       | 通信網路業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2476 | 鉅祥         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2405 | 輔信         | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3003 | 健和興       | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8039 | 台虹         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2406 | 國碩         | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4952 | 凌通         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3022 | 威強電       | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2467 | 志聖         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4949 | 有成精密     | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3321 | 同泰         | 電子零組件業     | true_breakout    | D_risk_downgrade    | hard_exclusion              |                           |                                     |                        |
|       3702 | 大聯大       | 電子通路業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3312 | 弘憶股       | 電子通路業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6695 | 芯鼎         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3034 | 聯詠         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       7769 | 鴻勁         | 半導體業         | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8215 | 明基材       | 光電業           | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3028 | 增你強       | 電子通路業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6515 | 穎崴         | 半導體業         | revenue_pullback | D_risk_downgrade    | hard_exclusion              |                           |                                     |                        |
|       8163 | 達方         | 電腦及週邊設備業 | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2329 | 華泰         | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6531 | 愛普*        | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8112 | 至上         | 電子通路業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3257 | 虹冠電       | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6155 | 鈞寶         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2328 | 廣宇         | 電子零組件業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2303 | 聯電         | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3041 | 揚智         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3094 | 聯傑         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3545 | 敦泰         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6526 | 達發         | 半導體業         | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6698 | 旭暉應材     | 其他電子業       | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3016 | 嘉晶         | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6209 | 今國光       | 光電業           | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2465 | 麗臺         | 電腦及週邊設備業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       8021 | 尖點         | 其他電子業       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6799 | 來頡         | 半導體業         | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |

## Core AI-Related Theme

|   stock_id | stock_name   | industry         | category         | decision_priority   | risk_handling_bucket      | effective_primary_theme   | effective_structural_theme_bucket      | effective_confidence   |
|-----------:|:-------------|:-----------------|:-----------------|:--------------------|:--------------------------|:--------------------------|:---------------------------------------|:-----------------------|
|       2485 | 兆赫         | 通信網路業       | revenue_pullback | B_confirm_needed    | normal                    | 低軌衛星                  | low_earth_orbit_satellite_theme        | low                    |
|       2485 | 兆赫         | 通信網路業       | pattern          | C_watch_only        | normal                    | 低軌衛星                  | low_earth_orbit_satellite_theme        | low                    |
|       6284 | 佳邦         | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | 低軌衛星                  | low_earth_orbit_satellite_theme        | low                    |
|       6235 | 華孚         | 電腦及週邊設備業 | range_rebound    | A_priority_watch    | normal                    | AI伺服器/機構件           | ai_server_mechanical_theme             | medium                 |
|       2353 | 宏碁         | 電腦及週邊設備業 | range_rebound    | B_confirm_needed    | risk_watch                | AI PC/品牌通路            | ai_pc_consumer_theme                   | medium                 |
|       6862 | 三集瑞-KY    | 電子零組件業     | range_rebound    | B_confirm_needed    | risk_watch                | 被動元件                  | passive_component_theme                | high                   |
|       2420 | 新巨         | 電子零組件業     | range_rebound    | B_confirm_needed    | risk_watch                | 電源供應鏈                | power_supply_theme                     | high                   |
|       2317 | 鴻海         | 其他電子業       | pattern          | B_confirm_needed    | risk_watch                | 機器人/AI製造             | robotics_ai_manufacturing_theme        | medium                 |
|       2353 | 宏碁         | 電腦及週邊設備業 | pattern          | B_confirm_needed    | risk_watch                | AI PC/品牌通路            | ai_pc_consumer_theme                   | medium                 |
|       1597 | 直得         | 電機機械         | revenue_pullback | B_confirm_needed    | risk_watch                | 機器人/精密傳動           | robotics_precision_motion_theme        | medium                 |
|       3583 | 辛耘         | 半導體業         | pattern          | B_confirm_needed    | normal                    | 半導體設備/材料           | semiconductor_equipment_material_theme | high                   |
|       4576 | 大銀微系統   | 電機機械         | revenue_pullback | B_confirm_needed    | normal                    | 機器人/精密傳動           | robotics_precision_motion_theme        | high                   |
|       3019 | 亞光         | 光電業           | revenue_pullback | C_watch_only        | risk_watch                | 機器人/光學感測           | robotics_optics_sensor_theme           | medium                 |
|       2317 | 鴻海         | 其他電子業       | revenue_pullback | C_watch_only        | risk_watch                | 機器人/AI製造             | robotics_ai_manufacturing_theme        | medium                 |
|       8374 | 羅昇         | 電機機械         | revenue_pullback | C_watch_only        | risk_watch                | 機器人/自動化             | robotics_automation_theme              | medium                 |
|       2357 | 華碩         | 電腦及週邊設備業 | pattern          | C_watch_only        | risk_watch                | AI PC/電競                | ai_pc_consumer_theme                   | medium                 |
|       6412 | 群電         | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | 電源供應鏈                | power_supply_theme                     | medium                 |
|       2049 | 上銀         | 電機機械         | pattern          | C_watch_only        | normal                    | 機器人/精密傳動           | robotics_precision_motion_theme        | high                   |
|       2367 | 燿華         | 電子零組件業     | pattern          | C_watch_only        | normal                    | 低軌衛星                  | low_earth_orbit_satellite_theme        | high                   |
|       2375 | 凱美         | 電子零組件業     | true_breakout    | C_watch_only        | high_momentum_risk_follow | 被動元件                  | passive_component_theme                | high                   |
|       2345 | 智邦         | 通信網路業       | revenue_pullback | C_watch_only        | risk_watch                | 網通/光通訊               | network_optical_datacenter_theme       | high                   |
|       2451 | 創見         | 半導體業         | revenue_pullback | C_watch_only        | risk_watch                | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       3413 | 京鼎         | 半導體業         | pattern          | C_watch_only        | risk_watch                | 半導體設備/材料           | semiconductor_equipment_material_theme | medium                 |
|       6862 | 三集瑞-KY    | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | 被動元件                  | passive_component_theme                | high                   |
|       4906 | 正文         | 通信網路業       | true_breakout    | C_watch_only        | high_momentum_risk_follow | 低軌衛星                  | low_earth_orbit_satellite_theme        | medium                 |
|       2376 | 技嘉         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | risk_watch                | AI伺服器/AI PC            | ai_server_pc_theme                     | medium                 |
|       2357 | 華碩         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | risk_watch                | AI PC/電競                | ai_pc_consumer_theme                   | medium                 |
|       3680 | 家登         | 半導體業         | pattern          | C_watch_only        | risk_watch                | 半導體設備/材料           | semiconductor_equipment_material_theme | medium                 |
|       2368 | 金像電       | 電子零組件業     | revenue_pullback | C_watch_only        | risk_watch                | PCB/CCL                   | pcb_ccl_theme                          | high                   |
|       1590 | 亞德客-KY    | 電機機械         | revenue_pullback | C_watch_only        | risk_watch                | 機器人/氣動自動化         | robotics_automation_theme              | high                   |
|       6414 | 樺漢         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | risk_watch                | 機器人/工業電腦           | robotics_ipc_edge_ai_theme             | medium                 |
|       2382 | 廣達         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | risk_watch                | AI伺服器                  | ai_server_ipc_theme                    | high                   |
|       3044 | 健鼎         | 電子零組件業     | revenue_pullback | C_watch_only        | risk_watch                | PCB/CCL                   | pcb_ccl_theme                          | medium                 |
|       2383 | 台光電       | 電子零組件業     | revenue_pullback | C_watch_only        | risk_watch                | 高速CCL/低軌衛星          | high_speed_ccl_satellite_theme         | high                   |
|       2374 | 佳能         | 光電業           | revenue_pullback | C_watch_only        | risk_watch                | 機器人/光學感測           | robotics_optics_sensor_theme           | medium                 |
|       6215 | 和椿         | 其他電子業       | revenue_pullback | C_watch_only        | risk_watch                | 機器人/自動化             | robotics_precision_motion_theme        | medium                 |
|       2374 | 佳能         | 光電業           | pattern          | C_watch_only        | risk_watch                | 機器人/光學感測           | robotics_optics_sensor_theme           | medium                 |
|       3483 | 力致         | 電腦及週邊設備業 | pattern          | C_watch_only        | risk_watch                | 散熱                      | thermal_solution_theme                 | medium                 |
|       6485 | 點序         | 半導體業         | pattern          | C_watch_only        | risk_watch                | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       3035 | 智原         | 半導體業         | pattern          | C_watch_only        | risk_watch                | ASIC/先進製程             | asic_advanced_process_theme            | high                   |
|       3019 | 亞光         | 光電業           | pattern          | C_watch_only        | risk_watch                | 機器人/光學感測           | robotics_optics_sensor_theme           | medium                 |
|       2317 | 鴻海         | 其他電子業       | pattern          | C_watch_only        | risk_watch                | 機器人/AI製造             | robotics_ai_manufacturing_theme        | medium                 |
|       1597 | 直得         | 電機機械         | pattern          | C_watch_only        | risk_watch                | 機器人/精密傳動           | robotics_precision_motion_theme        | medium                 |
|       8028 | 昇陽半導體   | 半導體業         | range_rebound    | C_watch_only        | high_momentum_risk_follow | 半導體設備/材料           | semiconductor_equipment_material_theme | medium                 |
|       6223 | 旺矽         | 半導體業         | pattern          | C_watch_only        | risk_watch                | 半導體測試介面            | semiconductor_test_interface_theme     | high                   |
|       2395 | 研華         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | risk_watch                | 機器人/工業電腦           | robotics_ipc_edge_ai_theme             | medium                 |
|       3715 | 定穎投控     | 電子零組件業     | revenue_pullback | C_watch_only        | risk_watch                | PCB/車用高頻板            | pcb_ccl_theme                          | medium                 |
|       2376 | 技嘉         | 電腦及週邊設備業 | pattern          | C_watch_only        | risk_watch                | AI伺服器/AI PC            | ai_server_pc_theme                     | medium                 |
|       8210 | 勤誠         | 電腦及週邊設備業 | pattern          | C_watch_only        | normal                    | AI伺服器/機殼             | ai_server_mechanical_theme             | high                   |
|       3044 | 健鼎         | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | PCB/CCL                   | pcb_ccl_theme                          | medium                 |
|       2451 | 創見         | 半導體業         | pattern          | C_watch_only        | risk_watch                | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       2356 | 英業達       | 電腦及週邊設備業 | pattern          | C_watch_only        | high_momentum_risk_follow | AI伺服器                  | ai_server_ipc_theme                    | medium                 |
|       4906 | 正文         | 通信網路業       | pattern          | C_watch_only        | high_momentum_risk_follow | 低軌衛星                  | low_earth_orbit_satellite_theme        | medium                 |
|       2383 | 台光電       | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | 高速CCL/低軌衛星          | high_speed_ccl_satellite_theme         | high                   |
|       2395 | 研華         | 電腦及週邊設備業 | pattern          | C_watch_only        | risk_watch                | 機器人/工業電腦           | robotics_ipc_edge_ai_theme             | medium                 |
|       2359 | 所羅門       | 其他電子業       | pattern          | C_watch_only        | risk_watch                | 機器人/自動化             | robotics_automation_theme              | medium                 |
|       6414 | 樺漢         | 電腦及週邊設備業 | pattern          | C_watch_only        | risk_watch                | 機器人/工業電腦           | robotics_ipc_edge_ai_theme             | medium                 |
|       3661 | 世芯-KY      | 半導體業         | pattern          | C_watch_only        | normal                    | ASIC/先進製程             | asic_advanced_process_theme            | high                   |
|       3380 | 明泰         | 通信網路業       | range_rebound    | C_watch_only        | high_momentum_risk_follow | 網通/光通訊               | network_optical_datacenter_theme       | medium                 |
|       8271 | 宇瞻         | 半導體業         | range_rebound    | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       3596 | 智易         | 通信網路業       | pattern          | C_watch_only        | risk_watch                | 低軌衛星                  | low_earth_orbit_satellite_theme        | medium                 |
|       3704 | 合勤控       | 通信網路業       | pattern          | C_watch_only        | high_momentum_risk_follow | 網通/通訊                 | network_communication_theme            | medium                 |
|       8374 | 羅昇         | 電機機械         | pattern          | C_watch_only        | risk_watch                | 機器人/自動化             | robotics_automation_theme              | medium                 |
|       2365 | 昆盈         | 電腦及週邊設備業 | pattern          | C_watch_only        | risk_watch                | 機器人/周邊零組件         | robotics_component_theme               | medium                 |
|       3533 | 嘉澤         | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | 高速傳輸/連接器           | high_speed_interconnect_theme          | high                   |
|       4938 | 和碩         | 電腦及週邊設備業 | range_rebound    | C_watch_only        | high_momentum_risk_follow | AI PC/消費電子            | ai_pc_consumer_theme                   | medium                 |
|       2356 | 英業達       | 電腦及週邊設備業 | range_rebound    | C_watch_only        | high_momentum_risk_follow | AI伺服器                  | ai_server_ipc_theme                    | medium                 |
|       2481 | 強茂         | 半導體業         | range_rebound    | C_watch_only        | high_momentum_risk_follow | 半導體                    | semiconductor_theme                    | medium                 |
|       6215 | 和椿         | 其他電子業       | pattern          | C_watch_only        | risk_watch                | 機器人/自動化             | robotics_precision_motion_theme        | medium                 |
|       3338 | 泰碩         | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | 散熱                      | thermal_solution_theme                 | medium                 |
|       6108 | 競國         | 電子零組件業     | range_rebound    | D_risk_downgrade    | hard_exclusion            | PCB/CCL                   | pcb_ccl_theme                          | medium                 |
|       2408 | 南亞科       | 半導體業         | range_rebound    | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | high                   |
|       2368 | 金像電       | 電子零組件業     | pattern          | C_watch_only        | risk_watch                | PCB/CCL                   | pcb_ccl_theme                          | high                   |
|       8271 | 宇瞻         | 半導體業         | revenue_pullback | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       8271 | 宇瞻         | 半導體業         | pullback_rebound | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       3704 | 合勤控       | 通信網路業       | range_rebound    | C_watch_only        | high_momentum_risk_follow | 網通/通訊                 | network_communication_theme            | medium                 |
|       4967 | 十銓         | 半導體業         | revenue_pullback | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       6139 | 亞翔         | 其他電子業       | revenue_pullback | C_watch_only        | high_momentum_risk_follow | 半導體設備/材料           | semiconductor_equipment_material_theme | medium                 |
|       3231 | 緯創         | 電腦及週邊設備業 | revenue_pullback | C_watch_only        | high_momentum_risk_follow | AI伺服器                  | ai_server_ipc_theme                    | high                   |
|       5388 | 中磊         | 通信網路業       | revenue_pullback | C_watch_only        | high_momentum_risk_follow | 低軌衛星                  | low_earth_orbit_satellite_theme        | medium                 |
|       3380 | 明泰         | 通信網路業       | pattern          | C_watch_only        | high_momentum_risk_follow | 網通/光通訊               | network_optical_datacenter_theme       | medium                 |
|       4938 | 和碩         | 電腦及週邊設備業 | pattern          | C_watch_only        | high_momentum_risk_follow | AI PC/消費電子            | ai_pc_consumer_theme                   | medium                 |
|       3017 | 奇鋐         | 電腦及週邊設備業 | revenue_pullback | D_risk_downgrade    | hard_exclusion            | 散熱                      | thermal_solution_theme                 | high                   |
|       6213 | 聯茂         | 電子零組件業     | pattern          | C_watch_only        | high_momentum_risk_follow | PCB/CCL                   | pcb_ccl_theme                          | high                   |
|       2449 | 京元電子     | 半導體業         | revenue_pullback | C_watch_only        | high_momentum_risk_follow | AI晶片測試                | ai_chip_testing_theme                  | high                   |
|       8046 | 南電         | 電子零組件業     | revenue_pullback | D_risk_downgrade    | hard_exclusion            | ABF載板/IC載板            | abf_substrate_theme                    | high                   |
|       2449 | 京元電子     | 半導體業         | pullback_rebound | C_watch_only        | high_momentum_risk_follow | AI晶片測試                | ai_chip_testing_theme                  | high                   |
|       1815 | 富喬         | 電子零組件業     | pattern          | D_risk_downgrade    | hard_exclusion            | 玻纖布/CCL                | glass_fiber_ccl_theme                  | high                   |
|       2301 | 光寶科       | 電腦及週邊設備業 | pattern          | D_risk_downgrade    | hard_exclusion            | 電源/光電                 | power_supply_theme                     | medium                 |
|       2324 | 仁寶         | 電腦及週邊設備業 | pattern          | D_risk_downgrade    | hard_exclusion            | AI PC/消費電子            | ai_pc_consumer_theme                   | medium                 |
|       2377 | 微星         | 電腦及週邊設備業 | pattern          | D_risk_downgrade    | hard_exclusion            | AI PC/電競                | ai_pc_consumer_theme                   | medium                 |
|       2382 | 廣達         | 電腦及週邊設備業 | pattern          | D_risk_downgrade    | hard_exclusion            | AI伺服器                  | ai_server_ipc_theme                    | high                   |
|       2392 | 正崴         | 電子零組件業     | pattern          | D_risk_downgrade    | hard_exclusion            | 高速傳輸/連接器           | high_speed_interconnect_theme          | medium                 |
|       2449 | 京元電子     | 半導體業         | pattern          | D_risk_downgrade    | hard_exclusion            | AI晶片測試                | ai_chip_testing_theme                  | high                   |
|       3324 | 雙鴻         | 其他電子業       | pattern          | D_risk_downgrade    | hard_exclusion            | 散熱                      | thermal_solution_theme                 | high                   |
|       5351 | 鈺創         | 半導體業         | pattern          | D_risk_downgrade    | hard_exclusion            | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       5443 | 均豪         | 半導體業         | pattern          | D_risk_downgrade    | hard_exclusion            | 半導體設備/材料           | semiconductor_equipment_material_theme | medium                 |
|       6127 | 九豪         | 電子零組件業     | pattern          | D_risk_downgrade    | hard_exclusion            | 被動元件                  | passive_component_theme                | medium                 |
|       6269 | 台郡         | 電子零組件業     | pattern          | D_risk_downgrade    | hard_exclusion            | FPC/軟板                  | fpc_flexible_pcb_theme                 | medium                 |
|       8088 | 品安         | 半導體業         | pattern          | D_risk_downgrade    | hard_exclusion            | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       4540 | 全球傳動     | 電機機械         | revenue_pullback | D_risk_downgrade    | hard_exclusion            | 機器人/精密傳動           | robotics_precision_motion_theme        | medium                 |
|       2408 | 南亞科       | 半導體業         | revenue_pullback | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | high                   |
|       3006 | 晶豪科       | 半導體業         | revenue_pullback | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       3491 | 昇達科       | 通信網路業       | pattern          | D_risk_downgrade    | hard_exclusion            | 低軌衛星                  | low_earth_orbit_satellite_theme        | high                   |
|       2344 | 華邦電       | 半導體業         | pattern          | D_risk_downgrade    | hard_exclusion            | 記憶體/HBM                | memory_hbm_theme                       | high                   |
|       5469 | 瀚宇博       | 電子零組件業     | pattern          | C_watch_only        | high_momentum_risk_follow | PCB/CCL                   | pcb_ccl_theme                          | medium                 |
|       6125 | 廣運         | 光電業           | pattern          | D_risk_downgrade    | hard_exclusion            | 機器人/自動化設備         | robotics_automation_theme              | medium                 |
|       2408 | 南亞科       | 半導體業         | pullback_rebound | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | high                   |
|       6152 | 百一         | 通信網路業       | revenue_pullback | D_risk_downgrade    | hard_exclusion            | 低軌衛星                  | low_earth_orbit_satellite_theme        | medium                 |
|       6414 | 樺漢         | 電腦及週邊設備業 | pattern          | D_risk_downgrade    | hard_exclusion            | 機器人/工業電腦           | robotics_ipc_edge_ai_theme             | medium                 |
|       6239 | 力成         | 半導體業         | true_breakout    | C_watch_only        | high_momentum_risk_follow | 記憶體封測                | memory_packaging_testing_theme         | medium                 |
|       2451 | 創見         | 半導體業         | pattern          | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |
|       3443 | 創意         | 半導體業         | revenue_pullback | D_risk_downgrade    | hard_exclusion            | ASIC/先進製程             | asic_advanced_process_theme            | high                   |
|       6108 | 競國         | 電子零組件業     | revenue_pullback | D_risk_downgrade    | hard_exclusion            | PCB/CCL                   | pcb_ccl_theme                          | medium                 |
|       6669 | 緯穎         | 電腦及週邊設備業 | revenue_pullback | D_risk_downgrade    | hard_exclusion            | AI伺服器                  | ai_server_ipc_theme                    | high                   |
|       2449 | 京元電子     | 半導體業         | pattern          | C_watch_only        | high_momentum_risk_follow | AI晶片測試                | ai_chip_testing_theme                  | high                   |
|       1303 | 南亞         | 塑膠工業         | pattern          | C_watch_only        | high_momentum_risk_follow | 玻纖布/CCL                | glass_fiber_ccl_theme                  | high                   |
|       6139 | 亞翔         | 其他電子業       | pattern          | C_watch_only        | high_momentum_risk_follow | 半導體設備/材料           | semiconductor_equipment_material_theme | medium                 |
|       3231 | 緯創         | 電腦及週邊設備業 | pattern          | C_watch_only        | high_momentum_risk_follow | AI伺服器                  | ai_server_ipc_theme                    | high                   |
|       4967 | 十銓         | 半導體業         | pattern          | C_watch_only        | high_momentum_risk_follow | 記憶體/HBM                | memory_hbm_theme                       | medium                 |

## Industry Non-Mainstream Only

|   stock_id | stock_name   | industry   | category         | decision_priority   | risk_handling_bucket        | effective_primary_theme   | effective_structural_theme_bucket   | effective_confidence   |
|-----------:|:-------------|:-----------|:-----------------|:--------------------|:----------------------------|:--------------------------|:------------------------------------|:-----------------------|
|       1339 | 昭輝         | 汽車工業   | true_breakout    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       8454 | 富邦媒       | 數位雲端   | true_breakout    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       6005 | 群益證       | 金融保險業 | true_breakout    | C_watch_only        | hard_exclusion              |                           |                                     |                        |
|       1455 | 集盛         | 紡織纖維   | range_rebound    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       2618 | 長榮航       | 航運業     | range_rebound    | B_confirm_needed    | non_mainstream_observe_only |                           |                                     |                        |
|       1522 | 堤維西       | 汽車工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2610 | 華航         | 航運業     | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4551 | 智伸科       | 汽車工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2201 | 裕隆         | 汽車工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1710 | 東聯         | 化學工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       0050 | 元大台灣50   |            | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1524 | 耿鼎         | 汽車工業   | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5522 | 遠雄         | 建材營造   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2915 | 潤泰全       | 貿易百貨   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2637 | 慧洋-KY      | 航運業     | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6214 | 精誠         | 資訊服務業 | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1319 | 東陽         | 汽車工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1810 | 和成         | 玻璃陶瓷   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2929 | 淘帝-KY      | 貿易百貨   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1709 | 和益         | 化學工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2206 | 三陽工業     | 汽車工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2882 | 國泰金       | 金融保險業 | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2891 | 中信金       | 金融保險業 | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1533 | 車王電       | 汽車工業   | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1568 | 倉佑         | 汽車工業   | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3708 | 上緯投控     | 綠能環保   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2886 | 兆豐金       | 金融保險業 | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2017 | 官田鋼       | 鋼鐵工業   | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2645 | 長榮航太     | 航運業     | range_rebound    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5522 | 遠雄         | 建材營造   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2883 | 凱基金       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1304 | 台聚         | 塑膠工業   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2881 | 富邦金       | 金融保險業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6005 | 群益證       | 金融保險業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4755 | 三福化       | 化學工業   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2542 | 興富發       | 建材營造   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1409 | 新纖         | 紡織纖維   | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5522 | 遠雄         | 建材營造   | pullback_rebound | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3004 | 豐達科       | 鋼鐵工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1563 | 巧新         | 汽車工業   | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2867 | 三商壽       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1305 | 華夏         | 塑膠工業   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1313 | 聯成         | 塑膠工業   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2892 | 第一金       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1530 | 亞崴         | 電機機械   | true_breakout    | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4743 | 合一         | 生技醫療業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1522 | 堤維西       | 汽車工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2637 | 慧洋-KY      | 航運業     | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6214 | 精誠         | 資訊服務業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2891 | 中信金       | 金融保險業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6214 | 精誠         | 資訊服務業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1402 | 遠東新       | 紡織纖維   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6861 | 睿生光電     | 生技醫療業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1522 | 堤維西       | 汽車工業   | pullback_rebound | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2637 | 慧洋-KY      | 航運業     | pullback_rebound | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2882 | 國泰金       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2891 | 中信金       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2606 | 裕民         | 航運業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2101 | 南港         | 橡膠工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2027 | 大成鋼       | 鋼鐵工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2891 | 中信金       | 金融保險業 | pullback_rebound | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4764 | 雙鍵         | 化學工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       9958 | 世紀鋼       | 鋼鐵工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1808 | 潤隆         | 建材營造   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4142 | 國光生       | 生技醫療業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2022 | 聚亨         | 鋼鐵工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       4739 | 康普         | 化學工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2851 | 中再保       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1714 | 和桐         | 化學工業   | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       1810 | 和成         | 玻璃陶瓷   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2645 | 長榮航太     | 航運業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2882 | 國泰金       | 金融保險業 | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       3551 | 世禾         | 綠能環保   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5009 | 榮剛         | 鋼鐵工業   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       5213 | 亞昕         | 建材營造   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6015 | 宏遠證       | 金融業     | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       6179 | 亞通         | 其他       | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2206 | 三陽工業     | 汽車工業   | pattern          | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2886 | 兆豐金       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |
|       2885 | 元大金       | 金融保險業 | revenue_pullback | C_watch_only        | non_mainstream_observe_only |                           |                                     |                        |

## Non-Mainstream Theme

|   stock_id | stock_name   | industry   | category   | decision_priority   | risk_handling_bucket        | effective_primary_theme   | effective_structural_theme_bucket   | effective_confidence   |
|-----------:|:-------------|:-----------|:-----------|:--------------------|:----------------------------|:--------------------------|:------------------------------------|:-----------------------|
|       1536 | 和大         | 汽車工業   | pattern    | C_watch_only        | non_mainstream_observe_only | 車用電子/EV               | automotive_ev_theme                 | medium                 |

## Mapped But Needs Review

|   stock_id | stock_name   | industry   | category         | decision_priority   | risk_handling_bucket      | effective_primary_theme   | effective_structural_theme_bucket   | effective_confidence   |
|-----------:|:-------------|:-----------|:-----------------|:--------------------|:--------------------------|:--------------------------|:------------------------------------|:-----------------------|
|       3227 | 原相         | 半導體業   | pattern          | C_watch_only        | risk_watch                | 感測IC/機器人             | sensor_ic_robotics_theme            | medium                 |
|       4961 | 天鈺         | 半導體業   | pattern          | C_watch_only        | risk_watch                | 驅動IC/AI邊緣             | driver_power_ic_theme               | medium                 |
|       8996 | 高力         | 電機機械   | revenue_pullback | D_risk_downgrade    | hard_exclusion            | 散熱/能源設備             | thermal_energy_theme                | medium                 |
|       2354 | 鴻準         | 其他電子業 | pattern          | D_risk_downgrade    | hard_exclusion            | 機器人/機構件             | robotics_mechanical_theme           | medium                 |
|       3481 | 群創         | 光電業     | pattern          | C_watch_only        | high_momentum_risk_follow | 消費性電子/面板           | consumer_electronics_display_theme  | medium                 |
