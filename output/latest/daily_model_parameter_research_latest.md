# Daily Model Parameter Research

- generated_at: `2026-06-30 11:18:33 Asia/Taipei`
- price_history_files: `2376`
- max_price_rows: `293`
- data_range: `20250407` ~ `20260629`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 332 | 221 | D+10 | 51.45 | 4.31 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1888 | 540 | D+10 | 47.69 | 3.08 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3288 | 791 | D+10 | 45.03 | 2.33 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2105 | 953 | D+10 | 47.79 | 1.91 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 34681 | 1765 | D+10 | 52.19 | 1.9 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3050 | 1035 | D+10 | 44.31 | 1.9 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 85716 | 1853 | D+10 | 46.06 | 1.89 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1311 | 754 | D+10 | 46.27 | 1.88 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 25125 | 1487 | D+10 | 52.85 | 1.83 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3021 | 1098 | D+10 | 47.8 | 1.81 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2272 | 933 | D+10 | 43.11 | 1.81 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 39655 | 1774 | D+10 | 51.12 | 1.75 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4752 | 1261 | D+10 | 44.18 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3773 | 1135 | D+10 | 44.1 | 1.74 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12018 | 1460 | D+10 | 43.72 | 1.72 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3269 | 1115 | D+10 | 42.85 | 1.68 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4297 | 1214 | D+10 | 44.12 | 1.65 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2711 | 1014 | D+10 | 42.74 | 1.64 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3747 | 1068 | D+10 | 44.08 | 1.59 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2991 | 950 | D+10 | 43.76 | 1.55 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2523 | 932 | D+10 | 42.73 | 1.52 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2451 | 871 | D+10 | 43.58 | 1.51 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5865 | 1443 | D+10 | 43.34 | 1.41 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3705 | 1209 | D+10 | 43.12 | 1.41 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1781 | 770 | D+10 | 42.23 | 1.41 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2104 | 839 | D+10 | 42.28 | 1.4 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4630 | 1316 | D+10 | 43.37 | 1.39 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1163 | 413 | D+10 | 53.01 | 1.34 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4110 | 1305 | D+10 | 42.02 | 1.3 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2804 | 1102 | D+10 | 41.94 | 1.29 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |

## All Model Parameter Summary

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | parameter_variant | variant_not_baseline | 8054 | 37.82 | 39.05 | 38.75 | 40.85 | -0.33 | 0.72 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | parameter_variant | variant_not_baseline | 3348 | 38.62 | 38.24 | 37.38 | 39.61 | -0.56 | 0.23 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | parameter_variant | variant_not_baseline | 833 | 38.18 | 37.83 | 37.81 | 37.64 | -0.65 | -0.33 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1163 | 45.57 | 53.04 | 53.38 | 53.01 | 1.27 | 1.34 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1398 | 45.78 | 52.13 | 52.1 | 50.48 | 1.17 | 0.85 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 3517 | 45.12 | 46.21 | 48.51 | 49.8 | 0.6 | 0.76 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 3517 | 45.12 | 46.21 | 48.51 | 49.8 | 0.6 | 0.76 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 2354 | 44.9 | 42.52 | 45.29 | 47.3 | 0.15 | 0.32 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 4446 | 45.16 | 45.11 | 47.23 | 47.36 | 0.41 | 0.35 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 3048 | 44.88 | 41.62 | 44.31 | 45.16 | -0.05 | -0.0 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near5_vol1.5 | parameter_variant | variant_not_baseline | 13276 | 38.99 | 40.93 | 41.58 | 43.07 | 0.08 | 0.97 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.5 | parameter_variant | variant_not_baseline | 7994 | 39.3 | 41.52 | 41.94 | 42.97 | 0.04 | 0.96 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | parameter_variant | variant_not_baseline | 11001 | 39.65 | 41.63 | 41.85 | 43.28 | 0.09 | 0.92 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | parameter_variant | variant_not_baseline | 18677 | 39.38 | 41.35 | 41.89 | 43.31 | 0.11 | 0.89 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | production_baseline | production_parity | 8268 | 36.6 | 39.27 | 40.04 | 42.32 | -0.14 | 1.0 | ok_first_pass | approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome |
| platform_strengthening | w20_near5_vol1.5 | parameter_variant | variant_not_baseline | 7835 | 38.76 | 41.28 | 41.22 | 42.77 | 0.02 | 0.45 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w20_near5_vol1.2 | parameter_variant | variant_not_baseline | 11402 | 39.51 | 41.49 | 41.46 | 42.59 | 0.02 | 0.39 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | parameter_variant | variant_not_baseline | 8639 | 39.09 | 41.57 | 41.43 | 42.53 | -0.02 | 0.35 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | parameter_variant | variant_not_baseline | 6134 | 37.92 | 40.88 | 40.69 | 42.26 | -0.07 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | parameter_variant | variant_not_baseline | 8100 | 39.58 | 41.24 | 40.79 | 41.89 | -0.06 | 0.23 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | parameter_variant | variant_not_baseline | 5838 | 39.4 | 40.96 | 40.35 | 41.7 | -0.08 | 0.22 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | parameter_variant | variant_not_baseline | 5696 | 38.85 | 40.81 | 40.75 | 41.95 | -0.07 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | parameter_variant | variant_not_baseline | 4196 | 38.3 | 40.54 | 40.14 | 41.88 | -0.09 | 0.19 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1 | parameter_variant | variant_not_baseline | 73932 | 39.0 | 42.69 | 43.38 | 44.84 | 0.27 | 1.08 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | parameter_variant | variant_not_baseline | 85325 | 39.18 | 42.86 | 43.56 | 44.95 | 0.28 | 1.08 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | parameter_variant | variant_not_baseline | 96237 | 39.25 | 42.84 | 43.55 | 44.98 | 0.29 | 1.07 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | parameter_variant | variant_not_baseline | 65836 | 38.92 | 42.43 | 43.19 | 44.56 | 0.22 | 0.97 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | parameter_variant | variant_not_baseline | 75617 | 39.07 | 42.57 | 43.37 | 44.62 | 0.23 | 0.95 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | parameter_variant | variant_not_baseline | 84767 | 39.17 | 42.57 | 43.35 | 44.63 | 0.24 | 0.95 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1 | parameter_variant | variant_not_baseline | 51382 | 38.83 | 42.26 | 43.05 | 44.44 | 0.19 | 0.85 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | parameter_variant | variant_not_baseline | 58478 | 39.03 | 42.44 | 43.19 | 44.46 | 0.19 | 0.83 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | parameter_variant | variant_not_baseline | 64913 | 39.2 | 42.44 | 43.15 | 44.39 | 0.19 | 0.82 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | production_current_proxy | production_baseline | production_proxy | 298431 | 39.0 | 42.72 | 43.57 | 44.52 | 0.21 | 0.69 | ok_first_pass | production baseline proxy replay: near 23EMA/support + MA/EMA trend proxy up |
| price_pullback_23ema | volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 30382 | 39.2 | 41.31 | 41.9 | 42.58 | 0.11 | 0.39 | ok_first_pass | production proxy replay + 帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | parameter_variant | variant_not_baseline | 15913 | 40.14 | 41.73 | 42.16 | 42.79 | 0.07 | 0.38 | ok_first_pass | production proxy replay + 實體帶量紅K + 量比 >= 1.2 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | parameter_variant | variant_not_baseline | 10239 | 39.61 | 40.94 | 41.56 | 42.29 | -0.01 | 0.26 | ok_first_pass | production proxy replay + 實體強量紅K + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2105 | 37.53 | 43.17 | 45.56 | 47.79 | 0.99 | 1.91 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 85716 | 39.03 | 43.02 | 44.3 | 46.06 | 0.57 | 1.89 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1311 | 38.37 | 42.78 | 44.82 | 46.27 | 0.97 | 1.88 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3021 | 38.13 | 43.19 | 45.04 | 47.8 | 0.89 | 1.81 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| revenue_unreacted_range | production_current_proxy | production_baseline | proxy_only | 333702 | 39.11 | 42.79 | 43.63 | 44.34 | 0.23 | 0.7 | ok_first_pass | production baseline proxy: price still in 23d range and attack not started; revenue panel missing |
| revenue_unreacted_range | range23_tol5 | parameter_variant | variant_not_baseline | 224727 | 38.98 | 42.62 | 43.23 | 44.06 | 0.1 | 0.41 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日模型層欄位提供 |
| revenue_unreacted_range | range23_tol10 | parameter_variant | variant_not_baseline | 226210 | 38.96 | 42.58 | 43.2 | 44.02 | 0.1 | 0.4 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日模型層欄位提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12018 | 37.34 | 39.43 | 41.49 | 43.72 | 0.12 | 1.72 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 332 | 38.25 | 40.63 | 43.43 | 51.45 | 0.73 | 4.31 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1888 | 39.46 | 40.23 | 41.98 | 47.69 | 0.21 | 3.08 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 3288 | 39.14 | 39.99 | 41.78 | 45.03 | -0.0 | 2.33 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 34681 | 41.08 | 44.26 | 47.07 | 52.19 | 0.59 | 1.9 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 25125 | 42.03 | 45.78 | 48.6 | 52.85 | 0.72 | 1.83 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 39655 | 40.55 | 43.27 | 46.22 | 51.12 | 0.46 | 1.75 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | parameter_variant | variant_not_baseline | 16504 | 41.55 | 44.6 | 47.83 | 49.8 | 0.48 | 1.08 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3050 | 39.11 | 41.56 | 41.53 | 44.31 | 0.06 | 1.9 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2272 | 38.64 | 40.67 | 40.95 | 43.11 | 0.21 | 1.81 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4752 | 38.49 | 41.34 | 41.87 | 44.18 | 0.12 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3773 | 38.56 | 41.48 | 41.63 | 44.1 | 0.03 | 1.74 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3269 | 38.3 | 40.5 | 41.01 | 42.85 | 0.17 | 1.68 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4297 | 36.54 | 42.28 | 41.89 | 44.12 | 0.1 | 1.65 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2711 | 38.44 | 40.77 | 40.93 | 42.74 | 0.15 | 1.64 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3747 | 38.16 | 41.68 | 41.55 | 44.08 | 0.07 | 1.59 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2991 | 37.98 | 41.96 | 41.21 | 43.76 | -0.03 | 1.55 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2523 | 38.05 | 40.76 | 40.8 | 42.73 | 0.18 | 1.52 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2451 | 38.39 | 41.74 | 40.91 | 43.58 | -0.09 | 1.51 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5865 | 37.89 | 40.64 | 40.88 | 43.34 | -0.11 | 1.41 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3705 | 38.87 | 40.59 | 40.24 | 43.12 | -0.27 | 1.41 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1781 | 38.07 | 40.75 | 40.26 | 42.23 | 0.1 | 1.41 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2104 | 37.93 | 41.15 | 40.49 | 42.28 | 0.12 | 1.4 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4630 | 38.38 | 40.76 | 40.57 | 43.37 | -0.21 | 1.39 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4110 | 37.79 | 39.85 | 40.06 | 42.02 | -0.1 | 1.3 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2804 | 38.34 | 39.73 | 39.74 | 41.94 | -0.13 | 1.29 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3392 | 38.18 | 40.05 | 40.02 | 42.12 | -0.11 | 1.28 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 654 | 22.94 | 46.53 | 42.86 | 42.6 | 0.41 | 0.77 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1606 | 36.92 | 39.5 | 38.2 | 38.41 | -0.41 | 0.61 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1241 | 37.55 | 38.8 | 38.08 | 38.65 | -0.48 | 0.57 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1423 | 37.32 | 38.9 | 37.72 | 37.85 | -0.56 | 0.4 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | parameter_variant | variant_not_baseline | 2044 | 36.89 | 38.44 | 37.11 | 38.58 | -0.68 | 0.29 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1232 | 37.74 | 40.02 | 37.77 | 37.68 | -0.39 | 0.29 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | parameter_variant | variant_not_baseline | 972 | 38.07 | 39.21 | 37.42 | 37.38 | -0.48 | 0.16 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | parameter_variant | variant_not_baseline | 1807 | 37.47 | 37.84 | 36.77 | 37.92 | -0.81 | 0.1 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | parameter_variant | variant_not_baseline | 1559 | 37.65 | 37.57 | 36.61 | 38.23 | -0.85 | 0.09 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1102 | 37.84 | 39.58 | 37.21 | 36.75 | -0.52 | 0.06 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| w_bottom_right_side | wproxy_vol1 | parameter_variant | variant_not_baseline | 48348 | 38.83 | 41.51 | 42.44 | 44.52 | 0.23 | 1.27 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | parameter_variant | variant_not_baseline | 38983 | 38.51 | 41.01 | 41.86 | 44.18 | 0.17 | 1.27 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | production_baseline | production_parity | 90806 | 39.22 | 42.35 | 43.08 | 45.06 | 0.29 | 1.24 | ok_first_pass | approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit |
| w_bottom_right_side | wproxy_vol1.5 | parameter_variant | variant_not_baseline | 29157 | 38.11 | 40.47 | 41.37 | 43.58 | 0.09 | 1.23 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
