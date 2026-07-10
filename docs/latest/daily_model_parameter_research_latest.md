# Daily Model Parameter Research

- generated_at: `2026-07-10 17:43:21 Asia/Taipei`
- price_history_files: `2376`
- max_price_rows: `301`
- data_range: `20250407` ~ `20260709`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 371 | 245 | D+10 | 47.38 | 2.84 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 2163 | 614 | D+10 | 45.02 | 2.36 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| volume_range_breakout_v2_low_position_volume_attack | volume_range_breakout_v2_low_position_operation_v1 | production_baseline | production_parity | 523 | 262 | D+10 | 45.02 | 2.25 | ok_first_pass | formal v2 baseline: 120d low-position bucket with all shape buckets, 60d breakout and close-only next-day continuation handled by operation adapter |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3160 | 1054 | D+10 | 44.33 | 1.92 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2185 | 981 | D+10 | 47.99 | 1.84 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 89287 | 1863 | D+10 | 45.73 | 1.78 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3906 | 1154 | D+10 | 44.13 | 1.76 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1364 | 782 | D+10 | 46.35 | 1.76 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4927 | 1282 | D+10 | 44.16 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2352 | 950 | D+10 | 43.05 | 1.74 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3121 | 1127 | D+10 | 47.78 | 1.73 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| price_pullback_23ema | price_pullback_23ema_prev20_breakout_stop_v1 | production_baseline | production_parity | 9612 | 1186 | D+10 | 50.38 | 1.72 | ok_first_pass | approved operation baseline: 23EMA/support pullback, return20_0_25, TDCC high thresholds up, OBV above MA20 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3804 | 869 | D+10 | 43.12 | 1.66 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12521 | 1484 | D+10 | 43.56 | 1.65 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3389 | 1137 | D+10 | 42.82 | 1.64 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3880 | 1095 | D+10 | 44.06 | 1.62 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 41834 | 1790 | D+10 | 50.84 | 1.61 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2804 | 1029 | D+10 | 42.77 | 1.61 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3093 | 970 | D+10 | 43.78 | 1.59 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2536 | 888 | D+10 | 43.62 | 1.56 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 30805 | 1528 | D+10 | 51.23 | 1.54 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2615 | 956 | D+10 | 42.74 | 1.52 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 47726 | 1796 | D+10 | 49.76 | 1.47 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 6080 | 1465 | D+10 | 43.35 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4794 | 1340 | D+10 | 43.42 | 1.43 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3842 | 1233 | D+10 | 43.1 | 1.43 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2177 | 857 | D+10 | 42.35 | 1.4 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1844 | 787 | D+10 | 42.22 | 1.39 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4262 | 1330 | D+10 | 42.04 | 1.29 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3510 | 1216 | D+10 | 42.18 | 1.28 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |

## All Model Parameter Summary

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | parameter_variant | variant_not_baseline | 8365 | 37.75 | 39.06 | 38.68 | 40.78 | -0.32 | 0.74 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | parameter_variant | variant_not_baseline | 3459 | 38.59 | 38.03 | 37.31 | 39.38 | -0.56 | 0.18 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | parameter_variant | variant_not_baseline | 858 | 38.34 | 37.73 | 37.51 | 37.44 | -0.71 | -0.36 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1278 | 46.24 | 53.21 | 53.74 | 49.48 | 1.26 | 0.88 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1525 | 46.16 | 52.18 | 52.44 | 47.58 | 1.17 | 0.5 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 5590 | 43.43 | 45.51 | 49.11 | 47.16 | 0.59 | 0.54 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 5590 | 43.43 | 45.51 | 49.11 | 47.16 | 0.59 | 0.54 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 4312 | 42.6 | 43.0 | 47.41 | 45.91 | 0.34 | 0.35 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 6961 | 43.08 | 44.25 | 47.59 | 45.45 | 0.4 | 0.18 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 5436 | 42.22 | 41.8 | 45.89 | 44.39 | 0.14 | 0.02 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near5_vol1.5 | parameter_variant | variant_not_baseline | 13756 | 38.83 | 40.69 | 41.57 | 42.94 | 0.07 | 0.94 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.5 | parameter_variant | variant_not_baseline | 8289 | 39.15 | 41.24 | 41.99 | 42.77 | 0.03 | 0.91 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | parameter_variant | variant_not_baseline | 11391 | 39.5 | 41.38 | 41.84 | 43.0 | 0.07 | 0.86 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | parameter_variant | variant_not_baseline | 19330 | 39.21 | 41.12 | 41.87 | 43.12 | 0.1 | 0.85 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | production_baseline | production_parity | 8590 | 36.5 | 39.13 | 40.11 | 42.19 | -0.09 | 0.99 | ok_first_pass | approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome |
| platform_strengthening | w20_near5_vol1.5 | parameter_variant | variant_not_baseline | 8090 | 38.91 | 41.23 | 41.46 | 42.7 | 0.03 | 0.44 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w20_near5_vol1.2 | parameter_variant | variant_not_baseline | 11746 | 39.67 | 41.51 | 41.64 | 42.53 | 0.03 | 0.38 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | parameter_variant | variant_not_baseline | 8902 | 39.27 | 41.66 | 41.56 | 42.51 | -0.01 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | parameter_variant | variant_not_baseline | 6331 | 38.11 | 40.93 | 40.9 | 42.26 | -0.07 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | parameter_variant | variant_not_baseline | 6033 | 39.57 | 40.96 | 40.47 | 41.64 | -0.09 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | parameter_variant | variant_not_baseline | 8365 | 39.74 | 41.2 | 40.97 | 41.78 | -0.06 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | parameter_variant | variant_not_baseline | 4336 | 38.49 | 40.45 | 40.3 | 41.82 | -0.1 | 0.19 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | parameter_variant | variant_not_baseline | 5887 | 38.97 | 40.63 | 40.93 | 41.82 | -0.07 | 0.19 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | price_pullback_23ema_prev20_breakout_stop_v1 | production_baseline | production_parity | 9612 | 41.92 | 45.28 | 48.35 | 50.38 | 0.71 | 1.72 | ok_first_pass | approved operation baseline: 23EMA/support pullback, return20_0_25, TDCC high thresholds up, OBV above MA20 |
| price_pullback_23ema | ema-4_7_volmax1 | parameter_variant | variant_not_baseline | 77683 | 39.04 | 42.94 | 43.82 | 44.77 | 0.3 | 1.03 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | parameter_variant | variant_not_baseline | 89480 | 39.19 | 43.09 | 43.99 | 44.86 | 0.31 | 1.03 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | parameter_variant | variant_not_baseline | 100803 | 39.24 | 43.04 | 43.95 | 44.86 | 0.31 | 1.02 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | parameter_variant | variant_not_baseline | 69135 | 38.98 | 42.71 | 43.66 | 44.53 | 0.25 | 0.93 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | parameter_variant | variant_not_baseline | 79244 | 39.1 | 42.83 | 43.81 | 44.57 | 0.26 | 0.92 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | parameter_variant | variant_not_baseline | 88731 | 39.17 | 42.8 | 43.77 | 44.55 | 0.26 | 0.91 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1 | parameter_variant | variant_not_baseline | 53892 | 38.92 | 42.6 | 43.57 | 44.43 | 0.22 | 0.82 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | parameter_variant | variant_not_baseline | 61229 | 39.08 | 42.75 | 43.68 | 44.43 | 0.22 | 0.8 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | parameter_variant | variant_not_baseline | 67874 | 39.22 | 42.74 | 43.63 | 44.34 | 0.22 | 0.78 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 31433 | 39.27 | 41.25 | 42.01 | 42.42 | 0.11 | 0.38 | ok_first_pass | production proxy replay + 帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 16502 | 40.27 | 41.7 | 42.19 | 42.62 | 0.07 | 0.38 | ok_first_pass | production proxy replay + 實體帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | parameter_variant | variant_not_baseline | 10622 | 39.7 | 40.92 | 41.62 | 42.07 | -0.02 | 0.24 | ok_first_pass | production proxy replay + 實體強量紅K + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2185 | 37.76 | 43.56 | 45.86 | 47.99 | 0.99 | 1.84 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 89287 | 38.98 | 43.0 | 44.43 | 45.73 | 0.57 | 1.78 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1364 | 38.71 | 43.45 | 45.22 | 46.35 | 0.96 | 1.76 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3121 | 38.19 | 43.47 | 45.48 | 47.78 | 0.92 | 1.73 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| revenue_unreacted_range | production_current_proxy | production_baseline | proxy_only | 348224 | 39.32 | 43.11 | 44.03 | 44.29 | 0.26 | 0.68 | ok_first_pass | production baseline proxy: price still in 23d range and attack not started; revenue gate tested separately |
| revenue_unreacted_range | range23_tol5 | parameter_variant | variant_not_baseline | 231788 | 39.08 | 42.88 | 43.62 | 44.12 | 0.13 | 0.4 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日模型層欄位提供 |
| revenue_unreacted_range | range23_tol10 | parameter_variant | variant_not_baseline | 233315 | 39.06 | 42.84 | 43.59 | 44.08 | 0.12 | 0.4 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日模型層欄位提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12521 | 37.02 | 39.1 | 41.4 | 43.56 | 0.14 | 1.65 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 371 | 37.2 | 40.5 | 41.67 | 47.38 | 0.34 | 2.84 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 2163 | 38.28 | 39.04 | 41.68 | 45.02 | 0.31 | 2.36 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3804 | 37.62 | 38.74 | 42.0 | 43.12 | 0.16 | 1.66 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 41834 | 41.56 | 45.7 | 48.61 | 50.84 | 0.68 | 1.61 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 30805 | 42.13 | 46.62 | 49.68 | 51.23 | 0.8 | 1.54 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 47726 | 40.81 | 44.45 | 47.6 | 49.76 | 0.56 | 1.47 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | parameter_variant | variant_not_baseline | 20578 | 41.66 | 45.71 | 49.37 | 49.3 | 0.63 | 1.08 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3160 | 38.89 | 41.65 | 41.7 | 44.33 | 0.13 | 1.92 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3906 | 38.35 | 41.5 | 41.73 | 44.13 | 0.07 | 1.76 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4927 | 38.24 | 41.29 | 41.92 | 44.16 | 0.15 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2352 | 38.48 | 40.78 | 41.06 | 43.05 | 0.23 | 1.74 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3389 | 38.06 | 40.53 | 41.04 | 42.82 | 0.19 | 1.64 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3880 | 37.91 | 41.47 | 41.62 | 44.06 | 0.1 | 1.62 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2804 | 38.27 | 40.86 | 40.99 | 42.77 | 0.17 | 1.61 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3093 | 37.8 | 41.8 | 41.32 | 43.78 | 0.02 | 1.59 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2536 | 38.17 | 41.63 | 41.13 | 43.62 | 0.0 | 1.56 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2615 | 37.74 | 40.57 | 40.82 | 42.74 | 0.18 | 1.52 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 6080 | 37.66 | 40.56 | 40.99 | 43.35 | -0.06 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4794 | 38.17 | 40.72 | 40.72 | 43.42 | -0.14 | 1.43 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3842 | 38.68 | 40.61 | 40.41 | 43.1 | -0.19 | 1.43 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2177 | 37.71 | 40.99 | 40.52 | 42.35 | 0.12 | 1.4 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1844 | 37.85 | 40.61 | 40.38 | 42.22 | 0.12 | 1.39 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4262 | 37.56 | 39.8 | 40.13 | 42.04 | -0.07 | 1.29 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3510 | 38.01 | 40.03 | 40.1 | 42.18 | -0.08 | 1.28 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2906 | 38.2 | 39.76 | 39.81 | 41.86 | -0.11 | 1.26 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 683 | 22.69 | 46.4 | 43.07 | 43.1 | 0.52 | 0.97 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1661 | 36.97 | 39.84 | 38.44 | 38.54 | -0.34 | 0.62 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1281 | 37.55 | 39.18 | 38.36 | 38.67 | -0.4 | 0.55 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1469 | 37.44 | 39.34 | 37.95 | 37.94 | -0.48 | 0.39 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1275 | 37.65 | 40.14 | 38.0 | 37.98 | -0.32 | 0.37 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | parameter_variant | variant_not_baseline | 2119 | 36.86 | 38.48 | 37.39 | 38.68 | -0.6 | 0.32 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1004 | 38.05 | 39.44 | 37.77 | 37.54 | -0.38 | 0.17 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | parameter_variant | variant_not_baseline | 1869 | 37.51 | 38.02 | 37.06 | 38.0 | -0.72 | 0.12 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1138 | 37.96 | 39.89 | 37.48 | 37.01 | -0.43 | 0.1 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | parameter_variant | variant_not_baseline | 1614 | 37.61 | 37.71 | 36.9 | 38.18 | -0.76 | 0.1 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout_v2_low_position_volume_attack | volume_range_breakout_v2_low_position_operation_v1 | production_baseline | production_parity | 523 | 38.24 | 42.34 | 39.85 | 45.02 | 0.46 | 2.25 | ok_first_pass | formal v2 baseline: 120d low-position bucket with all shape buckets, 60d breakout and close-only next-day continuation handled by operation adapter |
| volume_range_breakout_v2_mid_position_momentum_attack | volume_range_breakout_v2_mid_position_operation_v1 | production_baseline | production_parity | 79 | 31.65 | 36.71 | 41.03 | 46.15 | -1.86 | -0.83 | small_sample_review_only | formal v2 baseline: 120d mid-position bucket with non-consolidation or wide-range shape, 60d breakout and close-only next-day continuation handled by operation adapter |
| w_bottom_right_side | wproxy_vol1 | parameter_variant | variant_not_baseline | 50271 | 38.65 | 41.32 | 42.44 | 44.18 | 0.23 | 1.2 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | parameter_variant | variant_not_baseline | 40561 | 38.32 | 40.76 | 41.82 | 43.83 | 0.18 | 1.2 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | parameter_variant | variant_not_baseline | 30348 | 37.94 | 40.22 | 41.32 | 43.29 | 0.1 | 1.17 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | production_baseline | production_parity | 94984 | 39.16 | 42.35 | 43.31 | 44.81 | 0.3 | 1.15 | ok_first_pass | approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit |
