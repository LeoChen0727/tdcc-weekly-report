# Mature Model Row-Level Metric Row Audit

- audit_id: `mature_model_row_level_metric_contract_audit_20260711`
- audit_version: `v2`
- generated_at: `2026-08-31 19:46:24 Asia/Taipei`
- stock operation rows audited: `568`

## Model Counts

| model_id | rows | ready metric | explicit unavailable | invalid | baseline misuse |
| --- | ---: | ---: | ---: | ---: | ---: |
| `price_pullback_23ema` | 500 | 202 | 298 | 0 | 0 |
| `volume_range_breakout_v2_high_position_volume_attack` | 14 | 12 | 2 | 0 | 0 |
| `volume_range_breakout_v2_low_position_volume_attack` | 16 | 0 | 16 | 0 | 0 |
| `volume_range_breakout_v2_mid_position_momentum_attack` | 18 | 0 | 18 | 0 | 0 |
| `w_bottom_right_side` | 20 | 0 | 20 | 0 | 0 |

## Row Evidence

| model_id | section | stock | row metric | scope | validation | baseline policy |
| --- | --- | --- | --- | --- | --- | --- |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 3629 地心引力 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 4927 泰鼎-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 4977 眾達-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6152 百一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6290 良維 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 8103 瀚荃 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 5493 三聯 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6983 華洋精機 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 3629 地心引力 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 4927 泰鼎-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 4977 眾達-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6152 百一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6290 良維 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 8103 瀚荃 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 5493 三聯 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6983 華洋精機 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | confirmed_operation | 3555 博士旺 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 4304 勝昱 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6103 合邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 2489 瑞軒 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 4908 前鼎 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6278 台表科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6269 台郡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6168 宏齊 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6727 亞泰金屬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | confirmed_operation | 3555 博士旺 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 4304 勝昱 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6103 合邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 2489 瑞軒 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 4908 前鼎 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6278 台表科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6269 台郡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6168 宏齊 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_mid_position_momentum_attack` | active_operation | 6727 亞泰金屬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_high_position_volume_attack` | confirmed_operation | 2033 佳大 | `high_pos_base_plus_ma20_gt_ma60` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 6226 光鼎 | `high_pos_base_plus_ma20_gt_ma60` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 2491 吉祥全 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 4939 亞電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 3406 玉晶光 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 6141 柏承 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 7788 松川精密 | `pdf_combo__not_limit_up_like` | exact_combo | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | confirmed_operation | 2033 佳大 | `high_pos_base_plus_ma20_gt_ma60` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 6226 光鼎 | `high_pos_base_plus_ma20_gt_ma60` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 2491 吉祥全 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 4939 亞電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 3406 玉晶光 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 6141 柏承 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 7788 松川精密 | `pdf_combo__not_limit_up_like` | exact_combo | pass | pass_formal_row_metric_selected |
| `w_bottom_right_side` | confirmed_operation | 3293 鈊象 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2101 南港 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2106 建大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2204 中華 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2348 海悅 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2646 星宇航空 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2913 農林 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4114 健喬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4763 材料*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | confirmed_operation | 3293 鈊象 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2101 南港 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2106 建大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2204 中華 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2348 海悅 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2646 星宇航空 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2913 農林 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4114 健喬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4763 材料*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1519 華城 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2312 金寶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2355 敬鵬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2360 致茂 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2371 大同 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2375 凱美 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2393 億光 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2395 研華 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2449 京元電子 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2451 創見 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2476 鉅祥 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3016 嘉晶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3042 晶技 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3550 聯穎 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4576 大銀微系統 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6153 嘉聯益 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6165 浪凡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6190 萬泰科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 8043 蜜望實 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1316 上曜 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1409 新纖 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1708 東鹼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1714 和桐 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1904 正隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2543 皇昌 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2607 榮運 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3176 基亞 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4108 懷特 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4416 三圓 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4541 晟田 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4714 永捷 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4739 康普 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 5871 中租-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6015 宏遠證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 7777 能率亞洲 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 9921 巨大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 9941 裕融 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1101 台泥 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1102 亞泥 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1216 統一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1229 聯華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1304 台聚 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1305 華夏 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1308 亞聚 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1309 台達化 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1310 台苯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1313 聯成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1314 中石化 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1319 東陽 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1402 遠東新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1434 福懋 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1440 南紡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1504 東元 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1517 利奇 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1536 和大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1536 和大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1563 巧新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1582 信錦 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1597 直得 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1605 華新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1608 華榮 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1710 東聯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1712 興農 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1722 台肥 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1723 中碳 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1795 美時 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1808 潤隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1809 中釉 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1905 華紙 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1907 永豐餘 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1909 榮成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2002 中鋼 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2006 東和鋼鐵 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2009 第一銅 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2010 春源 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2014 中鴻 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2017 官田鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2023 燁輝 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2027 大成鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2034 允強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2101 南港 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2104 國際中橡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2105 正新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2201 裕隆 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2316 楠梓電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2323 中環 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2330 台積電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2331 精英 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2344 華邦電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2347 聯強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2353 宏碁 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2354 鴻準 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2356 英業達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2359 所羅門 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2362 藍天 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2365 昆盈 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2367 燿華 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2369 菱生 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2374 佳能 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2379 瑞昱 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2382 廣達 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2385 群光 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2402 毅嘉 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2428 興勤 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2436 偉詮電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2442 新美齊 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2461 光群雷 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2467 志聖 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2474 可成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2484 希華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2485 兆赫 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2495 普安 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2501 國建 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2511 太子 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2520 冠德 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2527 宏璟 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2536 宏普 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2537 聯上發 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2542 興富發 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2603 長榮 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2606 裕民 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2609 陽明 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2611 志信 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2612 中航 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2613 中櫃 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2617 台航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2618 長榮航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2633 台灣高鐵 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2634 漢翔 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2634 漢翔 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2636 台驊控股 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2641 正德 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2845 遠東銀 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2852 第一保 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2855 統一證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2867 三商壽 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2884 玉山金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2885 元大金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2886 兆豐金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2887 台新新光金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2891 中信金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2892 第一金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2897 王道銀行 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2903 遠百 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2905 三商 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2913 農林 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2915 潤泰全 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2929 淘帝-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3005 神基 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3006 晶豪科 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3013 晟銘電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3019 亞光 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3022 威強電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3023 信邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3028 增你強 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3030 德律 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3034 聯詠 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3035 智原 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3044 健鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3045 台灣大 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3048 益登 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3056 富華新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3062 建漢 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3094 聯傑 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3135 凌航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3189 景碩 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3221 台嘉碩 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3227 原相 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3236 千如 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3260 威剛 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3265 台星科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3305 昇貿 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3437 榮創 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3591 艾笛森 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3605 宏致 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3661 世芯-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3665 貿聯-KY | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3706 神達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3711 日月光投控 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4142 國光生 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4147 中裕 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4540 全球傳動 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4916 事欣科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4938 和碩 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4952 凌通 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4960 誠美材 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4967 十銓 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4976 佳凌 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4989 榮科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5009 榮剛 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5285 界霖 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5289 宜鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5309 系統電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5328 華容 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5469 瀚宇博 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5521 工信 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5534 長虹 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5607 遠雄港 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6016 康和證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6026 福邦證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6116 彩晶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6125 廣運 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6127 九豪 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6133 金橋 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6139 亞翔 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6197 佳必琪 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6205 詮欣 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6207 雷科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6244 茂迪 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6265 方土昶 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6284 佳邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6415 矽力*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6449 鈺邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6472 保瑞 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6477 安集 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6488 環球晶 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6505 台塑化 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6525 捷敏-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6548 長科* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6603 富強鑫 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6672 騰輝電子-KY | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6693 廣閎科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6706 惠特 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6742 澤米 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6753 龍德造船 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6770 力積電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6789 采鈺 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8027 鈦昇 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8064 東捷 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8074 鉅橡 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8081 致新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8110 華東 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8111 立碁 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8112 至上 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8222 寶一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8299 群聯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8422 可寧衛* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8436 大江 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8932 智通* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9105 泰金寶-DR | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9904 寶成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9907 統一實 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9933 中鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9939 宏全 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9945 潤泰新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1519 華城 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2312 金寶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2355 敬鵬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2360 致茂 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2371 大同 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2375 凱美 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2393 億光 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2395 研華 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2449 京元電子 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2451 創見 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2476 鉅祥 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3016 嘉晶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3042 晶技 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3550 聯穎 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4576 大銀微系統 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6153 嘉聯益 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6165 浪凡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6190 萬泰科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 8043 蜜望實 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1316 上曜 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1409 新纖 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1708 東鹼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1714 和桐 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1904 正隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2543 皇昌 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2607 榮運 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3176 基亞 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4108 懷特 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4416 三圓 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4541 晟田 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4714 永捷 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4739 康普 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 5871 中租-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6015 宏遠證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 7777 能率亞洲 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 9921 巨大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 9941 裕融 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1101 台泥 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1102 亞泥 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1216 統一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1229 聯華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1304 台聚 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1305 華夏 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1308 亞聚 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1309 台達化 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1310 台苯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1313 聯成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1314 中石化 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1319 東陽 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1402 遠東新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1434 福懋 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1440 南紡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1504 東元 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1517 利奇 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1536 和大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1536 和大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1563 巧新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1582 信錦 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1597 直得 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1605 華新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1608 華榮 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1710 東聯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1712 興農 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1722 台肥 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1723 中碳 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1795 美時 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1808 潤隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1809 中釉 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1905 華紙 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1907 永豐餘 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1909 榮成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2002 中鋼 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2006 東和鋼鐵 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2009 第一銅 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2010 春源 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2014 中鴻 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2017 官田鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2023 燁輝 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2027 大成鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2034 允強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2101 南港 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2104 國際中橡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2105 正新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2201 裕隆 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2316 楠梓電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2323 中環 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2330 台積電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2331 精英 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2344 華邦電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2347 聯強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2353 宏碁 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2354 鴻準 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2356 英業達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2359 所羅門 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2362 藍天 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2365 昆盈 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2367 燿華 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2369 菱生 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2374 佳能 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2379 瑞昱 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2382 廣達 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2385 群光 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2402 毅嘉 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2428 興勤 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2436 偉詮電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2442 新美齊 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2461 光群雷 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2467 志聖 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2474 可成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2484 希華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2485 兆赫 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2495 普安 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2501 國建 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2511 太子 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2520 冠德 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2527 宏璟 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2536 宏普 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2537 聯上發 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2542 興富發 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2603 長榮 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2606 裕民 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2609 陽明 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2611 志信 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2612 中航 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2613 中櫃 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2617 台航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2618 長榮航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2633 台灣高鐵 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2634 漢翔 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2634 漢翔 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2636 台驊控股 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2641 正德 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2845 遠東銀 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2852 第一保 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2855 統一證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2867 三商壽 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2884 玉山金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2885 元大金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2886 兆豐金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2887 台新新光金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2891 中信金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2892 第一金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2897 王道銀行 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2903 遠百 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2905 三商 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2913 農林 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2915 潤泰全 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2929 淘帝-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3005 神基 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3006 晶豪科 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3013 晟銘電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3019 亞光 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3022 威強電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3023 信邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3028 增你強 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3030 德律 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3034 聯詠 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3035 智原 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3044 健鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3045 台灣大 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3048 益登 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3056 富華新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3062 建漢 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3094 聯傑 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3135 凌航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3189 景碩 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3221 台嘉碩 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3227 原相 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3236 千如 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3260 威剛 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3265 台星科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3305 昇貿 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3437 榮創 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3591 艾笛森 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3605 宏致 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3661 世芯-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3665 貿聯-KY | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3706 神達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3711 日月光投控 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4142 國光生 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4147 中裕 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4540 全球傳動 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4916 事欣科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4938 和碩 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4952 凌通 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4960 誠美材 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4967 十銓 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4976 佳凌 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4989 榮科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5009 榮剛 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5285 界霖 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5289 宜鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5309 系統電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5328 華容 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5469 瀚宇博 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5521 工信 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5534 長虹 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5607 遠雄港 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6016 康和證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6026 福邦證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6116 彩晶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6125 廣運 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6127 九豪 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6133 金橋 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6139 亞翔 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6197 佳必琪 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6205 詮欣 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6207 雷科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6244 茂迪 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6265 方土昶 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6284 佳邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6415 矽力*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6449 鈺邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6472 保瑞 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6477 安集 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6488 環球晶 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6505 台塑化 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6525 捷敏-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6548 長科* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6603 富強鑫 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6672 騰輝電子-KY | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6693 廣閎科 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6706 惠特 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6742 澤米 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6753 龍德造船 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6770 力積電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6789 采鈺 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8027 鈦昇 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8064 東捷 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8074 鉅橡 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8081 致新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8110 華東 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8111 立碁 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8112 至上 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8222 寶一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8299 群聯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8422 可寧衛* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8436 大江 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8932 智通* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9105 泰金寶-DR | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9904 寶成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9907 統一實 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9933 中鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9939 宏全 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9945 潤泰新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
