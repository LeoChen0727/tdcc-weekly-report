# Mature Model Row-Level Metric Row Audit

- audit_id: `mature_model_row_level_metric_contract_audit_20260711`
- audit_version: `v2`
- generated_at: `2026-11-11 19:47:19 Asia/Taipei`
- stock operation rows audited: `132`

## Model Counts

| model_id | rows | ready metric | explicit unavailable | invalid | baseline misuse |
| --- | ---: | ---: | ---: | ---: | ---: |
| `price_pullback_23ema` | 86 | 42 | 44 | 0 | 0 |
| `revenue_unreacted_range` | 20 | 0 | 20 | 0 | 0 |
| `volume_range_breakout_v2_high_position_volume_attack` | 14 | 14 | 0 | 0 | 0 |
| `volume_range_breakout_v2_low_position_volume_attack` | 10 | 0 | 10 | 0 | 0 |
| `w_bottom_right_side` | 2 | 0 | 2 | 0 | 0 |

## Row Evidence

| model_id | section | stock | row metric | scope | validation | baseline policy |
| --- | --- | --- | --- | --- | --- | --- |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 3321 同泰 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 4960 誠美材 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 8291 尚茂 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 3379 彬台 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 8455 大拓-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 3321 同泰 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 4960 誠美材 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 8291 尚茂 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 3379 彬台 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 8455 大拓-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_high_position_volume_attack` | confirmed_operation | 2465 麗臺 | `high_pos_base_plus_volume_lt2` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | confirmed_operation | 6708 天擎 | `high_pos_base_plus_volume_lt2` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 2033 佳大 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 2321 東訊 | `high_pos_base_plus_breakout_2_5` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 5013 強新 | `high_pos_base_plus_breakout_2_5` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 6221 晉泰 | `high_pos_base_plus_ma20_gt_ma60` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 8099 大世科 | `high_pos_base_plus_volume_lt2` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | confirmed_operation | 2465 麗臺 | `high_pos_base_plus_volume_lt2` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | confirmed_operation | 6708 天擎 | `high_pos_base_plus_volume_lt2` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 2033 佳大 | `high_pos_base_plus_kdj_overheated` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 2321 東訊 | `high_pos_base_plus_breakout_2_5` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 5013 強新 | `high_pos_base_plus_breakout_2_5` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 6221 晉泰 | `high_pos_base_plus_ma20_gt_ma60` | single_add_score | pass | pass_formal_row_metric_selected |
| `volume_range_breakout_v2_high_position_volume_attack` | active_operation | 8099 大世科 | `high_pos_base_plus_volume_lt2` | single_add_score | pass | pass_formal_row_metric_selected |
| `w_bottom_right_side` | active_operation | 3293 鈊象 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 3293 鈊象 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4155 訊映 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4720 德淵 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1215 卜蜂 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1402 遠東新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1440 南紡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1789 神隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2002 中鋼 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2010 春源 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2023 燁輝 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2027 大成鋼 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2034 允強 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2105 正新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2106 建大 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2352 佳世達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2355 敬鵬 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2379 瑞昱 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2412 中華電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2542 興富發 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2607 榮運 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2637 慧洋-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2892 第一金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3005 神基 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3029 零壹 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3031 佰鴻 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3045 台灣大 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3293 鈊象 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4105 東洋 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4306 炎洲 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4770 上品 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4960 誠美材 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4967 十銓 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5210 寶碩 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5521 工信 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5876 上海商銀 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6108 競國 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6152 百一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6214 精誠 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6245 立端 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6672 騰輝電子-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8042 金山電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8213 志超 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9910 豐泰 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9933 中鼎 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4155 訊映 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4720 德淵 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1215 卜蜂 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1402 遠東新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1440 南紡 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1789 神隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2002 中鋼 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2010 春源 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2023 燁輝 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2027 大成鋼 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2034 允強 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2105 正新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2106 建大 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2352 佳世達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2355 敬鵬 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2379 瑞昱 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2412 中華電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2542 興富發 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2607 榮運 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2637 慧洋-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2892 第一金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3005 神基 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3029 零壹 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3031 佰鴻 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3045 台灣大 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3293 鈊象 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4105 東洋 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4306 炎洲 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 4770 上品 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4960 誠美材 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4967 十銓 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5210 寶碩 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 5521 工信 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5876 上海商銀 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6108 競國 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6152 百一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6214 精誠 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 6245 立端 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6672 騰輝電子-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8042 金山電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 8213 志超 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9910 豐泰 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 9933 中鼎 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 3042 晶技 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 8046 南電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 6274 台燿 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 3037 欣興 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 2397 友通 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 6259 百徽 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 2027 大成鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 2465 麗臺 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 4967 十銓 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | confirmed_operation | 3141 晶宏 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 3042 晶技 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 8046 南電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 6274 台燿 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 3037 欣興 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 2397 友通 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 6259 百徽 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 2027 大成鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 2465 麗臺 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | active_operation | 4967 十銓 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `revenue_unreacted_range` | confirmed_operation | 3141 晶宏 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
