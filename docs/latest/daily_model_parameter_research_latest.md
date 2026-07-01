# Daily Model Parameter Research

- generated_at: `2026-07-01 13:13:02 Asia/Taipei`
- price_history_files: `2376`
- max_price_rows: `294`
- data_range: `20250407` ~ `20260630`
- entry_basis: `signal_date_next_open`
- close_return_definition: `(D+n close / next trading day open - 1)`
- high_return_definition: `(max intraday high through D+n / next trading day open - 1)`

## Data Quality

- This is first-pass parameter research using the current repo price history.
- If sample_status is `small_sample_review_only` or `insufficient_sample`, do not treat the parameter as a final model weight.
- Revenue historical panel is not complete in price history, so the revenue-unreacted research row only validates the price-range component.

## Top Parameter Sets By Avg Close Return

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | selected_unique_stocks | best_close_horizon_d1_d10 | best_close_win_rate_pct | best_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 333 | 221 | D+10 | 50.9 | 4.1 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1901 | 543 | D+10 | 47.57 | 2.99 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3311 | 794 | D+10 | 45.01 | 2.28 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3059 | 1038 | D+10 | 44.34 | 1.91 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 86122 | 1855 | D+10 | 45.99 | 1.87 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2114 | 959 | D+10 | 47.75 | 1.86 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1319 | 759 | D+10 | 46.33 | 1.84 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2281 | 936 | D+10 | 43.12 | 1.82 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 35662 | 1768 | D+10 | 51.59 | 1.81 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3033 | 1106 | D+10 | 47.7 | 1.76 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4765 | 1262 | D+10 | 44.22 | 1.75 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3782 | 1135 | D+10 | 44.16 | 1.75 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 25843 | 1487 | D+10 | 52.17 | 1.74 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12045 | 1460 | D+10 | 43.74 | 1.72 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3281 | 1116 | D+10 | 42.9 | 1.7 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 40677 | 1775 | D+10 | 50.59 | 1.68 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | production_current | production_baseline | production_parity | 4308 | 1215 | D+10 | 44.14 | 1.66 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2720 | 1015 | D+10 | 42.8 | 1.66 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3756 | 1071 | D+10 | 44.12 | 1.6 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2998 | 952 | D+10 | 43.82 | 1.57 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2531 | 934 | D+10 | 42.77 | 1.54 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2458 | 874 | D+10 | 43.6 | 1.52 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5881 | 1445 | D+10 | 43.38 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2111 | 841 | D+10 | 42.33 | 1.43 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1788 | 773 | D+10 | 42.22 | 1.43 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3716 | 1211 | D+10 | 43.14 | 1.42 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4642 | 1317 | D+10 | 43.43 | 1.41 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4123 | 1305 | D+10 | 42.07 | 1.32 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2813 | 1103 | D+10 | 41.97 | 1.31 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3402 | 1195 | D+10 | 42.2 | 1.3 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |

## All Model Parameter Summary

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | parameter_variant | variant_not_baseline | 8083 | 37.88 | 39.01 | 38.72 | 40.9 | -0.34 | 0.73 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | parameter_variant | variant_not_baseline | 3357 | 38.64 | 38.19 | 37.37 | 39.67 | -0.56 | 0.24 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | parameter_variant | variant_not_baseline | 834 | 38.13 | 37.83 | 37.79 | 37.75 | -0.67 | -0.28 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1173 | 45.78 | 53.04 | 53.22 | 50.4 | 1.27 | 0.95 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1409 | 45.92 | 52.13 | 51.98 | 48.53 | 1.16 | 0.56 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 3771 | 46.17 | 46.21 | 48.27 | 48.44 | 0.59 | 0.65 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 3771 | 46.17 | 46.21 | 48.27 | 48.44 | 0.59 | 0.65 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 4744 | 46.16 | 45.11 | 46.96 | 46.39 | 0.41 | 0.27 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 2598 | 46.34 | 42.52 | 45.31 | 46.84 | 0.18 | 0.4 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 3335 | 46.27 | 41.62 | 44.22 | 44.83 | -0.0 | 0.06 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near5_vol1.5 | parameter_variant | variant_not_baseline | 13313 | 39.0 | 40.9 | 41.56 | 43.07 | 0.09 | 0.97 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.5 | parameter_variant | variant_not_baseline | 8015 | 39.3 | 41.51 | 41.95 | 42.95 | 0.04 | 0.96 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | parameter_variant | variant_not_baseline | 11026 | 39.64 | 41.62 | 41.85 | 43.22 | 0.09 | 0.91 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | parameter_variant | variant_not_baseline | 18722 | 39.39 | 41.31 | 41.87 | 43.27 | 0.12 | 0.88 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | production_baseline | production_parity | 8289 | 36.66 | 39.22 | 40.0 | 42.3 | -0.14 | 1.01 | ok_first_pass | approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome |
| platform_strengthening | w20_near5_vol1.5 | parameter_variant | variant_not_baseline | 7857 | 38.79 | 41.24 | 41.26 | 42.71 | 0.02 | 0.44 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w20_near5_vol1.2 | parameter_variant | variant_not_baseline | 11428 | 39.53 | 41.46 | 41.46 | 42.52 | 0.02 | 0.38 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | parameter_variant | variant_not_baseline | 8657 | 39.12 | 41.53 | 41.42 | 42.46 | -0.02 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | parameter_variant | variant_not_baseline | 6149 | 37.97 | 40.82 | 40.72 | 42.19 | -0.07 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | parameter_variant | variant_not_baseline | 8113 | 39.59 | 41.19 | 40.8 | 41.76 | -0.06 | 0.22 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | parameter_variant | variant_not_baseline | 5850 | 39.42 | 40.93 | 40.37 | 41.59 | -0.08 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | parameter_variant | variant_not_baseline | 5706 | 38.87 | 40.74 | 40.79 | 41.8 | -0.07 | 0.2 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | parameter_variant | variant_not_baseline | 4205 | 38.34 | 40.49 | 40.22 | 41.76 | -0.09 | 0.18 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1 | parameter_variant | variant_not_baseline | 74419 | 39.11 | 42.71 | 43.38 | 44.77 | 0.26 | 1.07 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | parameter_variant | variant_not_baseline | 85860 | 39.28 | 42.87 | 43.57 | 44.88 | 0.28 | 1.07 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | parameter_variant | variant_not_baseline | 96805 | 39.35 | 42.85 | 43.55 | 44.89 | 0.28 | 1.06 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | parameter_variant | variant_not_baseline | 66252 | 39.02 | 42.46 | 43.2 | 44.48 | 0.22 | 0.96 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | parameter_variant | variant_not_baseline | 76073 | 39.17 | 42.6 | 43.37 | 44.54 | 0.23 | 0.94 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | parameter_variant | variant_not_baseline | 85250 | 39.25 | 42.59 | 43.36 | 44.54 | 0.24 | 0.94 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1 | parameter_variant | variant_not_baseline | 51709 | 38.93 | 42.31 | 43.05 | 44.35 | 0.19 | 0.84 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | parameter_variant | variant_not_baseline | 58834 | 39.11 | 42.47 | 43.2 | 44.37 | 0.19 | 0.82 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | parameter_variant | variant_not_baseline | 65289 | 39.28 | 42.47 | 43.17 | 44.29 | 0.19 | 0.81 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | production_current_proxy | production_baseline | production_proxy | 299969 | 39.08 | 42.72 | 43.57 | 44.46 | 0.21 | 0.68 | ok_first_pass | production baseline proxy replay: near 23EMA/support + MA/EMA trend proxy up |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 15962 | 40.15 | 41.7 | 42.16 | 42.73 | 0.07 | 0.39 | ok_first_pass | production proxy replay + 實體帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 30465 | 39.24 | 41.29 | 41.9 | 42.51 | 0.11 | 0.38 | ok_first_pass | production proxy replay + 帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | parameter_variant | variant_not_baseline | 10276 | 39.62 | 40.91 | 41.58 | 42.26 | -0.01 | 0.26 | ok_first_pass | production proxy replay + 實體強量紅K + 量比 >= 1.5 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 86122 | 39.1 | 43.01 | 44.28 | 45.99 | 0.57 | 1.87 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2114 | 37.65 | 43.21 | 45.45 | 47.75 | 0.98 | 1.86 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1319 | 38.51 | 42.82 | 44.63 | 46.33 | 0.95 | 1.84 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3033 | 38.21 | 43.21 | 44.96 | 47.7 | 0.88 | 1.76 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| revenue_unreacted_range | production_current_proxy | production_baseline | proxy_only | 335451 | 39.2 | 42.8 | 43.62 | 44.29 | 0.23 | 0.7 | ok_first_pass | production baseline proxy: price still in 23d range and attack not started; revenue panel missing |
| revenue_unreacted_range | range23_tol5 | parameter_variant | variant_not_baseline | 225528 | 39.01 | 42.63 | 43.24 | 44.01 | 0.1 | 0.4 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日模型層欄位提供 |
| revenue_unreacted_range | range23_tol10 | parameter_variant | variant_not_baseline | 227015 | 38.99 | 42.6 | 43.21 | 43.97 | 0.1 | 0.4 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日模型層欄位提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12045 | 37.35 | 39.42 | 41.49 | 43.74 | 0.13 | 1.72 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 333 | 38.14 | 40.31 | 42.62 | 50.9 | 0.53 | 4.1 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1901 | 39.61 | 40.22 | 41.93 | 47.57 | 0.21 | 2.99 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3311 | 39.23 | 40.0 | 41.82 | 45.01 | 0.02 | 2.28 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 35662 | 41.48 | 44.27 | 46.99 | 51.59 | 0.58 | 1.81 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 25843 | 42.41 | 45.72 | 48.41 | 52.17 | 0.71 | 1.74 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 40677 | 40.92 | 43.3 | 46.12 | 50.59 | 0.46 | 1.68 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | parameter_variant | variant_not_baseline | 16997 | 41.91 | 44.59 | 47.69 | 49.18 | 0.48 | 1.03 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3059 | 39.23 | 41.54 | 41.5 | 44.34 | 0.05 | 1.91 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2281 | 38.8 | 40.57 | 40.89 | 43.12 | 0.19 | 1.82 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4765 | 38.61 | 41.32 | 41.85 | 44.22 | 0.11 | 1.75 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3782 | 38.66 | 41.46 | 41.61 | 44.16 | 0.02 | 1.75 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3281 | 38.46 | 40.42 | 40.95 | 42.9 | 0.16 | 1.7 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4308 | 36.61 | 42.26 | 41.85 | 44.14 | 0.09 | 1.66 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2720 | 38.57 | 40.7 | 40.88 | 42.8 | 0.13 | 1.66 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3756 | 38.26 | 41.63 | 41.57 | 44.12 | 0.07 | 1.6 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2998 | 38.06 | 41.92 | 41.22 | 43.82 | -0.04 | 1.57 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2531 | 38.17 | 40.66 | 40.79 | 42.77 | 0.17 | 1.54 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2458 | 38.49 | 41.69 | 40.93 | 43.6 | -0.09 | 1.52 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5881 | 37.97 | 40.61 | 40.86 | 43.38 | -0.12 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2111 | 38.04 | 41.06 | 40.49 | 42.33 | 0.11 | 1.43 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1788 | 38.2 | 40.64 | 40.26 | 42.22 | 0.08 | 1.43 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3716 | 38.94 | 40.56 | 40.19 | 43.14 | -0.29 | 1.42 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4642 | 38.43 | 40.74 | 40.55 | 43.43 | -0.22 | 1.41 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4123 | 37.91 | 39.78 | 40.03 | 42.07 | -0.11 | 1.32 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2813 | 38.46 | 39.64 | 39.67 | 41.97 | -0.15 | 1.31 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3402 | 38.27 | 39.98 | 40.0 | 42.2 | -0.12 | 1.3 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 656 | 22.87 | 46.63 | 42.84 | 42.56 | 0.39 | 0.77 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1612 | 37.03 | 39.41 | 38.17 | 38.44 | -0.42 | 0.61 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1246 | 37.64 | 38.75 | 38.07 | 38.63 | -0.49 | 0.58 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1428 | 37.39 | 38.86 | 37.72 | 37.88 | -0.56 | 0.4 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | parameter_variant | variant_not_baseline | 2051 | 36.96 | 38.37 | 37.08 | 38.62 | -0.68 | 0.3 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1237 | 37.83 | 39.85 | 37.83 | 37.72 | -0.39 | 0.3 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | parameter_variant | variant_not_baseline | 977 | 38.18 | 39.09 | 37.54 | 37.37 | -0.48 | 0.17 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | parameter_variant | variant_not_baseline | 1813 | 37.51 | 37.81 | 36.79 | 37.99 | -0.81 | 0.12 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | parameter_variant | variant_not_baseline | 1564 | 37.72 | 37.54 | 36.59 | 38.23 | -0.86 | 0.1 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1107 | 37.94 | 39.47 | 37.32 | 36.8 | -0.51 | 0.07 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| w_bottom_right_side | wproxy_vol1 | parameter_variant | variant_not_baseline | 48494 | 38.86 | 41.49 | 42.42 | 44.42 | 0.23 | 1.25 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | parameter_variant | variant_not_baseline | 39091 | 38.53 | 40.97 | 41.83 | 44.07 | 0.17 | 1.25 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | production_baseline | production_parity | 91222 | 39.25 | 42.34 | 43.07 | 44.94 | 0.29 | 1.22 | ok_first_pass | approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit |
| w_bottom_right_side | wproxy_vol1.5 | parameter_variant | variant_not_baseline | 29237 | 38.13 | 40.42 | 41.34 | 43.51 | 0.08 | 1.21 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
