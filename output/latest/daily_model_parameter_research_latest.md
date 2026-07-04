# Daily Model Parameter Research

- generated_at: `2026-07-05 04:40:31 Asia/Taipei`
- price_history_files: `2376`
- max_price_rows: `297`
- data_range: `20250407` ~ `20260703`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 348 | 231 | D+10 | 51.03 | 3.92 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1960 | 553 | D+10 | 47.5 | 2.9 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3417 | 808 | D+10 | 45.17 | 2.15 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3101 | 1045 | D+10 | 44.46 | 1.93 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 87366 | 1859 | D+10 | 45.87 | 1.84 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2309 | 940 | D+10 | 43.33 | 1.84 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2139 | 970 | D+10 | 47.76 | 1.84 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1340 | 773 | D+10 | 46.25 | 1.8 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3832 | 1143 | D+10 | 44.23 | 1.77 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4824 | 1269 | D+10 | 44.22 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 38487 | 1769 | D+10 | 50.94 | 1.73 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3061 | 1115 | D+10 | 47.58 | 1.73 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12186 | 1467 | D+10 | 43.83 | 1.71 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | production_current | production_baseline | production_parity | 4370 | 1225 | D+10 | 44.23 | 1.69 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3321 | 1122 | D+10 | 42.99 | 1.69 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2754 | 1018 | D+10 | 42.99 | 1.68 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 27995 | 1491 | D+10 | 51.38 | 1.66 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 43725 | 1775 | D+10 | 50.02 | 1.61 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3799 | 1081 | D+10 | 44.14 | 1.61 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3035 | 960 | D+10 | 43.89 | 1.6 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2560 | 940 | D+10 | 42.92 | 1.56 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2487 | 879 | D+10 | 43.72 | 1.55 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2137 | 845 | D+10 | 42.55 | 1.46 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1808 | 776 | D+10 | 42.45 | 1.45 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3766 | 1218 | D+10 | 43.22 | 1.44 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5950 | 1451 | D+10 | 43.35 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4700 | 1326 | D+10 | 43.46 | 1.43 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2846 | 1109 | D+10 | 42.09 | 1.33 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4169 | 1311 | D+10 | 42.11 | 1.32 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3441 | 1201 | D+10 | 42.29 | 1.32 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |

## All Model Parameter Summary

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | parameter_variant | variant_not_baseline | 8203 | 38.01 | 39.28 | 38.63 | 40.95 | -0.33 | 0.74 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | parameter_variant | variant_not_baseline | 3396 | 38.81 | 38.44 | 37.19 | 39.65 | -0.59 | 0.25 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | parameter_variant | variant_not_baseline | 845 | 38.22 | 37.92 | 37.58 | 37.64 | -0.71 | -0.26 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1217 | 46.75 | 53.34 | 53.4 | 48.23 | 1.27 | 0.65 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1455 | 46.74 | 52.39 | 52.15 | 46.56 | 1.18 | 0.29 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 3301 | 48.35 | 45.79 | 47.15 | 47.91 | 0.47 | 0.91 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 4518 | 47.92 | 48.01 | 49.22 | 48.05 | 0.74 | 0.8 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 4518 | 47.92 | 48.01 | 49.22 | 48.05 | 0.74 | 0.8 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 5632 | 47.6 | 46.91 | 47.84 | 46.35 | 0.55 | 0.42 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 4177 | 47.91 | 44.77 | 45.87 | 46.21 | 0.27 | 0.51 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near5_vol1.5 | parameter_variant | variant_not_baseline | 13472 | 39.16 | 40.93 | 41.51 | 43.04 | 0.07 | 0.96 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.5 | parameter_variant | variant_not_baseline | 8113 | 39.44 | 41.56 | 41.91 | 42.94 | 0.03 | 0.95 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | parameter_variant | variant_not_baseline | 11166 | 39.78 | 41.65 | 41.8 | 43.15 | 0.08 | 0.9 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | parameter_variant | variant_not_baseline | 18946 | 39.54 | 41.35 | 41.86 | 43.22 | 0.1 | 0.88 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | production_baseline | production_parity | 8401 | 36.77 | 39.44 | 39.98 | 42.21 | -0.13 | 0.99 | ok_first_pass | approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome |
| platform_strengthening | w20_near5_vol1.5 | parameter_variant | variant_not_baseline | 7944 | 39.06 | 41.32 | 41.26 | 42.69 | 0.02 | 0.43 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w20_near5_vol1.2 | parameter_variant | variant_not_baseline | 11548 | 39.77 | 41.57 | 41.48 | 42.48 | 0.02 | 0.37 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | parameter_variant | variant_not_baseline | 8757 | 39.43 | 41.7 | 41.41 | 42.48 | -0.02 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | parameter_variant | variant_not_baseline | 6220 | 38.28 | 40.97 | 40.7 | 42.23 | -0.07 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | parameter_variant | variant_not_baseline | 5914 | 39.75 | 41.07 | 40.33 | 41.56 | -0.09 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | parameter_variant | variant_not_baseline | 8198 | 39.86 | 41.25 | 40.79 | 41.65 | -0.07 | 0.2 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | parameter_variant | variant_not_baseline | 5763 | 39.16 | 40.72 | 40.75 | 41.71 | -0.08 | 0.19 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | parameter_variant | variant_not_baseline | 4245 | 38.66 | 40.6 | 40.14 | 41.74 | -0.1 | 0.18 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1 | parameter_variant | variant_not_baseline | 75599 | 39.35 | 43.0 | 43.55 | 44.72 | 0.28 | 1.06 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | parameter_variant | variant_not_baseline | 87135 | 39.5 | 43.16 | 43.74 | 44.82 | 0.3 | 1.06 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | parameter_variant | variant_not_baseline | 98184 | 39.56 | 43.12 | 43.72 | 44.82 | 0.3 | 1.05 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | parameter_variant | variant_not_baseline | 67318 | 39.27 | 42.74 | 43.38 | 44.45 | 0.24 | 0.96 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | parameter_variant | variant_not_baseline | 77217 | 39.39 | 42.87 | 43.55 | 44.5 | 0.25 | 0.94 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | parameter_variant | variant_not_baseline | 86476 | 39.47 | 42.86 | 43.54 | 44.48 | 0.26 | 0.93 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1 | parameter_variant | variant_not_baseline | 52526 | 39.19 | 42.59 | 43.25 | 44.31 | 0.21 | 0.85 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | parameter_variant | variant_not_baseline | 59707 | 39.34 | 42.75 | 43.39 | 44.32 | 0.21 | 0.82 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | parameter_variant | variant_not_baseline | 66210 | 39.49 | 42.74 | 43.36 | 44.23 | 0.21 | 0.81 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | production_current_proxy | production_baseline | production_proxy | 304517 | 39.36 | 43.01 | 43.71 | 44.44 | 0.22 | 0.68 | ok_first_pass | production baseline proxy replay: near 23EMA/support + MA/EMA trend proxy up |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 16206 | 40.34 | 41.85 | 42.12 | 42.68 | 0.06 | 0.4 | ok_first_pass | production proxy replay + 實體帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 30879 | 39.41 | 41.42 | 41.88 | 42.46 | 0.1 | 0.39 | ok_first_pass | production proxy replay + 帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | parameter_variant | variant_not_baseline | 10435 | 39.81 | 41.02 | 41.53 | 42.2 | -0.02 | 0.25 | ok_first_pass | production proxy replay + 實體強量紅K + 量比 >= 1.5 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 87366 | 39.27 | 43.19 | 44.34 | 45.87 | 0.57 | 1.84 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2139 | 37.96 | 43.42 | 45.65 | 47.76 | 1.0 | 1.84 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1340 | 38.81 | 43.14 | 44.85 | 46.25 | 0.97 | 1.8 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3061 | 38.45 | 43.39 | 45.28 | 47.58 | 0.93 | 1.73 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| revenue_unreacted_range | production_current_proxy | production_baseline | proxy_only | 341516 | 39.53 | 43.12 | 43.81 | 44.26 | 0.25 | 0.7 | ok_first_pass | production baseline proxy: price still in 23d range and attack not started; revenue gate tested separately |
| revenue_unreacted_range | range23_tol5 | parameter_variant | variant_not_baseline | 228227 | 39.2 | 42.84 | 43.35 | 43.97 | 0.11 | 0.4 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日模型層欄位提供 |
| revenue_unreacted_range | range23_tol10 | parameter_variant | variant_not_baseline | 229725 | 39.19 | 42.8 | 43.32 | 43.93 | 0.11 | 0.39 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日模型層欄位提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12186 | 37.48 | 39.55 | 41.4 | 43.83 | 0.14 | 1.71 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 348 | 37.93 | 41.42 | 41.57 | 51.03 | 0.44 | 3.92 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1960 | 39.9 | 40.75 | 41.58 | 47.5 | 0.34 | 2.9 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3417 | 39.57 | 40.57 | 41.7 | 45.17 | 0.13 | 2.15 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 38487 | 42.72 | 45.86 | 47.76 | 50.94 | 0.66 | 1.73 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 27995 | 43.59 | 47.25 | 48.95 | 51.38 | 0.79 | 1.66 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 43725 | 42.07 | 44.8 | 46.79 | 50.02 | 0.54 | 1.61 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | parameter_variant | variant_not_baseline | 18483 | 43.2 | 46.21 | 48.34 | 48.75 | 0.59 | 1.06 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3101 | 39.28 | 41.87 | 41.51 | 44.46 | 0.1 | 1.93 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2309 | 38.85 | 41.05 | 40.85 | 43.33 | 0.19 | 1.84 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3832 | 38.67 | 41.73 | 41.64 | 44.23 | 0.07 | 1.77 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4824 | 38.6 | 41.56 | 41.84 | 44.22 | 0.15 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4370 | 36.59 | 42.5 | 41.87 | 44.23 | 0.13 | 1.69 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3321 | 38.48 | 40.78 | 40.9 | 42.99 | 0.17 | 1.69 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2754 | 38.6 | 41.1 | 40.87 | 42.99 | 0.15 | 1.68 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3799 | 38.25 | 41.85 | 41.58 | 44.14 | 0.11 | 1.61 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3035 | 38.09 | 42.13 | 41.29 | 43.89 | 0.02 | 1.6 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2560 | 38.12 | 40.98 | 40.78 | 42.92 | 0.19 | 1.56 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2487 | 38.56 | 41.98 | 41.0 | 43.72 | -0.01 | 1.55 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2137 | 38.0 | 41.38 | 40.54 | 42.55 | 0.13 | 1.46 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1808 | 38.16 | 41.05 | 40.31 | 42.45 | 0.11 | 1.45 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3766 | 39.06 | 40.88 | 40.16 | 43.22 | -0.24 | 1.44 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5950 | 38.02 | 40.84 | 40.84 | 43.35 | -0.09 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4700 | 38.51 | 40.98 | 40.56 | 43.46 | -0.18 | 1.43 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2846 | 38.58 | 40.06 | 39.59 | 42.09 | -0.16 | 1.33 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4169 | 37.97 | 40.09 | 39.95 | 42.11 | -0.1 | 1.32 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3441 | 38.36 | 40.32 | 39.95 | 42.29 | -0.11 | 1.32 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 671 | 22.95 | 46.76 | 42.97 | 42.79 | 0.57 | 0.83 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1631 | 37.16 | 40.0 | 38.11 | 38.51 | -0.39 | 0.63 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1259 | 37.73 | 39.43 | 38.03 | 38.83 | -0.46 | 0.61 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1444 | 37.53 | 39.44 | 37.67 | 38.05 | -0.54 | 0.45 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1250 | 37.84 | 40.42 | 37.82 | 37.93 | -0.34 | 0.36 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | parameter_variant | variant_not_baseline | 2073 | 37.14 | 38.83 | 37.04 | 38.66 | -0.66 | 0.33 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | parameter_variant | variant_not_baseline | 985 | 38.17 | 39.76 | 37.55 | 37.64 | -0.42 | 0.22 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | parameter_variant | variant_not_baseline | 1832 | 37.72 | 38.28 | 36.75 | 38.11 | -0.79 | 0.17 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | parameter_variant | variant_not_baseline | 1580 | 37.91 | 38.1 | 36.56 | 38.37 | -0.83 | 0.15 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1118 | 38.01 | 40.05 | 37.3 | 37.07 | -0.47 | 0.14 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| w_bottom_right_side | wproxy_vol1 | parameter_variant | variant_not_baseline | 49093 | 39.0 | 41.59 | 42.41 | 44.29 | 0.23 | 1.23 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | parameter_variant | variant_not_baseline | 39587 | 38.67 | 41.06 | 41.81 | 43.95 | 0.18 | 1.22 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | parameter_variant | variant_not_baseline | 29613 | 38.29 | 40.5 | 41.27 | 43.42 | 0.1 | 1.2 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | production_baseline | production_parity | 92642 | 39.47 | 42.52 | 43.15 | 44.85 | 0.3 | 1.19 | ok_first_pass | approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit |
