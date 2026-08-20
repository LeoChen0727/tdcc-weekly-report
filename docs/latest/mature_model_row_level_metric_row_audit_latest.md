# Mature Model Row-Level Metric Row Audit

- audit_id: `mature_model_row_level_metric_contract_audit_20260711`
- audit_version: `v2`
- generated_at: `2026-08-21 04:33:00 Asia/Taipei`
- stock operation rows audited: `252`

## Model Counts

| model_id | rows | ready metric | explicit unavailable | invalid | baseline misuse |
| --- | ---: | ---: | ---: | ---: | ---: |
| `price_pullback_23ema` | 228 | 144 | 84 | 0 | 0 |
| `volume_range_breakout_v2_low_position_volume_attack` | 2 | 0 | 2 | 0 | 0 |
| `w_bottom_right_side` | 22 | 0 | 22 | 0 | 0 |

## Row Evidence

| model_id | section | stock | row metric | scope | validation | baseline policy |
| --- | --- | --- | --- | --- | --- | --- |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6152 百一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `volume_range_breakout_v2_low_position_volume_attack` | active_operation | 6152 百一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 1216 統一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 1609 大亞 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 1904 正隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2101 南港 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2106 建大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2348 海悅 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2646 星宇航空 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2913 農林 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4114 健喬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4763 材料*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 1216 統一 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 1609 大亞 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 1904 正隆 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2101 南港 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2106 建大 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2348 海悅 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2646 星宇航空 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 2913 農林 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4114 健喬 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `w_bottom_right_side` | active_operation | 4763 材料*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1597 直得 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1605 華新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1608 華榮 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2323 中環 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2331 精英 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2353 宏碁 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2354 鴻準 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2365 昆盈 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2371 大同 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2436 偉詮電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2451 創見 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2467 志聖 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2474 可成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2484 希華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2489 瑞軒 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3005 神基 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3006 晶豪科 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3022 威強電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3221 台嘉碩 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3265 台星科 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3605 宏致 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3673 TPK-KY | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3714 富采 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4540 全球傳動 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4938 和碩 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4956 光鋐 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4967 十銓 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4976 佳凌 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 5289 宜鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5471 松翰 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5498 凱崴 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6265 方土昶 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6269 台郡 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6603 富強鑫 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6770 力積電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 7788 松川精密 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8021 尖點 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8110 華東 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8112 至上 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8222 寶一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8299 群聯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1216 統一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1316 上曜 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1795 美時 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2002 中鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2006 東和鋼鐵 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2010 春源 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2023 燁輝 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2034 允強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2104 國際中橡 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2201 裕隆 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2442 新美齊 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2501 國建 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2520 冠德 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2537 聯上發 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2601 益航 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2845 遠東銀 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2897 王道銀行 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2905 三商 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3056 富華新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4147 中裕 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4743 合一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4763 材料*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 5009 榮剛 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5521 工信 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5534 長虹 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5864 致和證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6753 龍德造船 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6919 康霈* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 9907 統一實 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1101 台泥 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1229 聯華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1517 利奇 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1519 華城 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1907 永豐餘 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2009 第一銅 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2014 中鴻 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2347 聯強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2356 英業達 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2362 藍天 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2379 瑞昱 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2527 宏璟 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2618 長榮航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2867 三商壽 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2882 國泰金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2883 凱基金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2884 玉山金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2885 元大金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2886 兆豐金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2891 中信金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2892 第一金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2929 淘帝-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3023 信邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3028 增你強 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3030 德律 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3036 文曄 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3094 聯傑 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3135 凌航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3227 原相 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3293 鈊象 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3665 貿聯-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3706 神達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4142 國光生 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5469 瀚宇博 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6605 帝寶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6830 汎銓 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8081 致新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8422 可寧衛* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9939 宏全 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 1597 直得 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1605 華新 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1608 華榮 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2323 中環 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2331 精英 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2353 宏碁 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2354 鴻準 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2365 昆盈 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2371 大同 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2436 偉詮電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2451 創見 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2467 志聖 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2474 可成 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2484 希華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2489 瑞軒 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3005 神基 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3006 晶豪科 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3022 威強電 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3221 台嘉碩 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3265 台星科 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3605 宏致 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3673 TPK-KY | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 3714 富采 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4540 全球傳動 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4938 和碩 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4956 光鋐 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4967 十銓 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4976 佳凌 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 5289 宜鼎 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5471 松翰 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5498 凱崴 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6265 方土昶 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6269 台郡 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6603 富強鑫 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 6770 力積電 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 7788 松川精密 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8021 尖點 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8110 華東 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8112 至上 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8222 寶一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 8299 群聯 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1216 統一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1316 上曜 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1717 長興 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1795 美時 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 1802 台玻 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2002 中鋼 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2006 東和鋼鐵 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2010 春源 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2023 燁輝 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2034 允強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2104 國際中橡 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2201 裕隆 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2442 新美齊 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2501 國建 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2520 冠德 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2537 聯上發 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2601 益航 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 2845 遠東銀 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2897 王道銀行 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 2905 三商 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 3056 富華新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 4147 中裕 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4743 合一 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 4763 材料*-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 5009 榮剛 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5521 工信 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5534 長虹 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 5864 致和證 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6753 龍德造船 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | confirmed_operation | 6919 康霈* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | confirmed_operation | 9907 統一實 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1101 台泥 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1229 聯華 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 1517 利奇 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1519 華城 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 1907 永豐餘 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2009 第一銅 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2014 中鴻 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2347 聯強 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2356 英業達 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2362 藍天 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2379 瑞昱 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2527 宏璟 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2618 長榮航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2867 三商壽 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2882 國泰金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2883 凱基金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2884 玉山金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2885 元大金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2886 兆豐金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2891 中信金 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 2892 第一金 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 2929 淘帝-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3023 信邦 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3028 增你強 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3029 零壹 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3030 德律 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3036 文曄 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3094 聯傑 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3135 凌航 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3227 原相 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3293 鈊象 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 3665 貿聯-KY | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 3706 神達 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 4142 國光生 | `price_pullback_23ema__technical_strength_rsi60_macd_positive` | exact_combo | pass | pass_formal_row_metric_selected |
| `price_pullback_23ema` | active_operation | 5469 瀚宇博 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6605 帝寶 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 6830 汎銓 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8081 致新 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 8422 可寧衛* | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
| `price_pullback_23ema` | active_operation | 9939 宏全 | `unavailable_no_approved_add_score_metric` |  | pass | pass_adapter_explicitly_blocks_baseline_fallback |
