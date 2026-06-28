# Daily Model Parameter Research

- generated_at: `2026-06-29 05:03:41 Asia/Taipei`
- price_history_files: `2373`
- max_price_rows: `289`
- data_range: `20250407` ~ `20260623`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 297 | 202 | D+10 | 50.76 | 4.17 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1722 | 525 | D+10 | 47.85 | 3.24 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1109 | 412 | D+9 | 63.75 | 3.11 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1336 | 459 | D+9 | 60.24 | 2.57 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 2995 | 777 | D+10 | 44.83 | 2.29 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 31187 | 1728 | D+10 | 53.78 | 2.1 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2049 | 941 | D+10 | 48.51 | 2.05 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 22466 | 1417 | D+10 | 54.85 | 2.04 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1275 | 743 | D+10 | 46.81 | 2.01 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 35719 | 1748 | D+10 | 52.57 | 1.94 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1676 | 605 | D+4 | 57.78 | 1.94 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 2933 | 1083 | D+10 | 48.47 | 1.91 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 83552 | 1847 | D+10 | 46.18 | 1.89 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3003 | 1025 | D+10 | 44.36 | 1.87 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 2785 | 710 | D+4 | 57.57 | 1.79 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 2785 | 710 | D+4 | 57.57 | 1.79 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2232 | 921 | D+10 | 43.14 | 1.79 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4691 | 1249 | D+10 | 44.21 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3721 | 1126 | D+10 | 44.17 | 1.74 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 11687 | 1450 | D+10 | 43.68 | 1.67 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3219 | 1103 | D+10 | 42.82 | 1.66 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4240 | 1204 | D+10 | 44.17 | 1.65 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2668 | 1003 | D+10 | 42.76 | 1.63 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 2233 | 695 | D+4 | 55.86 | 1.61 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3699 | 1056 | D+10 | 44.09 | 1.59 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 3569 | 791 | D+4 | 56.04 | 1.56 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2951 | 942 | D+10 | 43.81 | 1.56 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2415 | 863 | D+10 | 43.63 | 1.5 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2485 | 922 | D+10 | 42.68 | 1.49 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5780 | 1429 | D+10 | 43.43 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |

## All Model Parameter Summary

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | parameter_variant | variant_not_baseline | 7912 | 37.89 | 39.46 | 39.05 | 40.99 | -0.28 | 0.74 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | parameter_variant | variant_not_baseline | 3277 | 38.63 | 38.65 | 37.64 | 39.79 | -0.52 | 0.24 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | parameter_variant | variant_not_baseline | 812 | 37.56 | 38.4 | 37.53 | 37.88 | -0.68 | -0.31 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1109 | 44.91 | 55.03 | 58.17 | 63.93 | 1.95 | 2.89 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1336 | 45.21 | 54.05 | 56.3 | 60.24 | 1.8 | 2.31 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1676 | 44.57 | 57.81 | 54.65 | 47.73 | 1.54 | 0.33 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 2785 | 44.7 | 56.53 | 56.23 | 54.25 | 1.72 | 1.36 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 2785 | 44.7 | 56.53 | 56.23 | 54.25 | 1.72 | 1.36 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 2233 | 45.23 | 55.33 | 52.76 | 45.05 | 1.31 | -0.1 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 3569 | 45.22 | 54.78 | 54.25 | 50.88 | 1.52 | 0.82 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near3_vol1.5 | parameter_variant | variant_not_baseline | 7877 | 39.27 | 41.84 | 42.44 | 43.26 | 0.1 | 1.01 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.5 | parameter_variant | variant_not_baseline | 13049 | 38.92 | 41.28 | 42.09 | 43.27 | 0.15 | 1.0 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | parameter_variant | variant_not_baseline | 10855 | 39.64 | 41.94 | 42.25 | 43.56 | 0.14 | 0.97 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | production_current_proxy | production_baseline | production_proxy | 17561 | 39.37 | 41.78 | 42.42 | 43.7 | 0.18 | 0.95 | ok_first_pass | production baseline proxy: within 5% below 60d high + volume >= 1.2 + EMA23 up |
| near_high_neckline_challenge | near5_vol1.2 | parameter_variant | variant_not_baseline | 18368 | 39.37 | 41.67 | 42.28 | 43.48 | 0.17 | 0.93 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| neckline_volume_breakout_confirmation | production_current_proxy | production_baseline | production_proxy | 8164 | 36.62 | 39.49 | 40.22 | 42.5 | -0.1 | 1.04 | ok_first_pass | production baseline proxy: W-bottom proxy + volume/locked-limit neckline breakout proxy |
| platform_strengthening | w20_near5_vol1.5 | parameter_variant | variant_not_baseline | 7780 | 38.8 | 41.5 | 41.41 | 42.83 | 0.04 | 0.47 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | production_current_proxy | production_baseline | production_proxy | 11316 | 39.54 | 41.68 | 41.61 | 42.7 | 0.03 | 0.41 | ok_first_pass | production baseline proxy: 20d range width <= 18%, near upper edge, volume >= 1.2, solid red candle |
| platform_strengthening | w20_near5_vol1.2 | parameter_variant | variant_not_baseline | 11316 | 39.54 | 41.68 | 41.61 | 42.7 | 0.03 | 0.41 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | parameter_variant | variant_not_baseline | 8577 | 39.16 | 41.79 | 41.54 | 42.68 | -0.01 | 0.38 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | parameter_variant | variant_not_baseline | 6090 | 37.98 | 41.11 | 40.84 | 42.31 | -0.07 | 0.36 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | parameter_variant | variant_not_baseline | 5794 | 39.47 | 41.12 | 40.43 | 41.84 | -0.08 | 0.25 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | parameter_variant | variant_not_baseline | 8036 | 39.66 | 41.44 | 40.96 | 42.05 | -0.05 | 0.25 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | parameter_variant | variant_not_baseline | 5657 | 38.96 | 41.05 | 40.97 | 42.07 | -0.05 | 0.23 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | parameter_variant | variant_not_baseline | 4168 | 38.39 | 40.7 | 40.32 | 41.96 | -0.09 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1 | parameter_variant | variant_not_baseline | 71850 | 39.09 | 43.21 | 43.75 | 44.89 | 0.31 | 1.08 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | parameter_variant | variant_not_baseline | 82972 | 39.26 | 43.37 | 43.94 | 45.01 | 0.32 | 1.08 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | parameter_variant | variant_not_baseline | 93625 | 39.34 | 43.34 | 43.92 | 45.05 | 0.33 | 1.08 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | parameter_variant | variant_not_baseline | 63953 | 39.01 | 42.92 | 43.55 | 44.6 | 0.26 | 0.97 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | parameter_variant | variant_not_baseline | 73501 | 39.16 | 43.06 | 43.73 | 44.66 | 0.27 | 0.96 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | parameter_variant | variant_not_baseline | 82439 | 39.25 | 43.06 | 43.72 | 44.69 | 0.27 | 0.95 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | production_current_proxy | production_baseline | production_proxy | 100110 | 39.2 | 42.95 | 43.56 | 44.56 | 0.27 | 0.94 | ok_first_pass | production baseline proxy: near 23EMA/support + EMA23 slope proxy up |
| price_pullback_23ema | ema-1.5_3_volmax1 | parameter_variant | variant_not_baseline | 49895 | 38.91 | 42.76 | 43.42 | 44.49 | 0.22 | 0.86 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | parameter_variant | variant_not_baseline | 56817 | 39.1 | 42.92 | 43.57 | 44.51 | 0.23 | 0.84 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | parameter_variant | variant_not_baseline | 63096 | 39.25 | 42.92 | 43.53 | 44.45 | 0.23 | 0.82 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2049 | 37.48 | 43.86 | 45.85 | 48.51 | 1.05 | 2.05 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1275 | 38.27 | 43.49 | 45.11 | 46.81 | 1.06 | 2.01 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 2933 | 38.19 | 43.85 | 45.43 | 48.47 | 0.95 | 1.91 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 83552 | 39.11 | 43.56 | 44.76 | 46.18 | 0.65 | 1.89 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| revenue_unreacted_range | production_current_proxy | production_baseline | proxy_only | 327357 | 39.15 | 43.15 | 43.87 | 44.39 | 0.26 | 0.7 | ok_first_pass | production baseline proxy: price still in 23d range and attack not started; revenue panel missing |
| revenue_unreacted_range | range23_tol5 | parameter_variant | variant_not_baseline | 221140 | 38.97 | 42.87 | 43.46 | 44.13 | 0.12 | 0.42 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日模型層欄位提供 |
| revenue_unreacted_range | range23_tol10 | parameter_variant | variant_not_baseline | 222614 | 38.96 | 42.84 | 43.43 | 44.09 | 0.12 | 0.42 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日模型層欄位提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 11687 | 37.4 | 39.85 | 41.81 | 43.68 | 0.22 | 1.67 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 297 | 40.07 | 42.91 | 44.09 | 50.76 | 0.96 | 4.17 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1722 | 40.19 | 42.68 | 44.36 | 47.85 | 0.87 | 3.24 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 2995 | 39.47 | 42.02 | 43.94 | 44.83 | 0.59 | 2.29 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 31187 | 41.41 | 46.42 | 48.98 | 53.78 | 0.78 | 2.1 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 22466 | 42.41 | 48.35 | 51.09 | 54.85 | 1.01 | 2.04 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 35719 | 40.87 | 45.54 | 48.23 | 52.57 | 0.71 | 1.94 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | parameter_variant | variant_not_baseline | 14565 | 42.0 | 47.31 | 50.4 | 51.74 | 0.73 | 1.18 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3003 | 39.19 | 41.89 | 41.65 | 44.36 | 0.11 | 1.87 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2232 | 38.71 | 41.0 | 41.02 | 43.14 | 0.24 | 1.79 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4691 | 38.61 | 41.68 | 42.09 | 44.21 | 0.18 | 1.74 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3721 | 38.65 | 41.77 | 41.8 | 44.17 | 0.08 | 1.74 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3219 | 38.4 | 40.88 | 41.22 | 42.82 | 0.23 | 1.66 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4240 | 36.58 | 42.58 | 42.07 | 44.17 | 0.17 | 1.65 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2668 | 38.49 | 41.07 | 41.05 | 42.76 | 0.19 | 1.63 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3699 | 38.28 | 42.01 | 41.75 | 44.09 | 0.12 | 1.59 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2951 | 38.05 | 42.25 | 41.36 | 43.81 | 0.02 | 1.56 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2415 | 38.43 | 42.04 | 41.02 | 43.63 | -0.04 | 1.5 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2485 | 38.11 | 41.13 | 41.01 | 42.68 | 0.23 | 1.49 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5780 | 37.96 | 40.95 | 41.11 | 43.43 | -0.05 | 1.43 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4555 | 38.44 | 41.06 | 40.76 | 43.5 | -0.15 | 1.41 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3638 | 38.95 | 40.97 | 40.4 | 43.19 | -0.21 | 1.39 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2072 | 37.93 | 41.46 | 40.61 | 42.27 | 0.15 | 1.38 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1751 | 38.04 | 41.05 | 40.36 | 42.2 | 0.13 | 1.36 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4041 | 37.86 | 40.17 | 40.26 | 42.03 | -0.05 | 1.29 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3331 | 38.25 | 40.34 | 40.15 | 42.17 | -0.08 | 1.28 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2748 | 38.43 | 40.1 | 39.84 | 41.96 | -0.09 | 1.27 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 644 | 22.67 | 46.9 | 43.04 | 42.45 | 0.56 | 0.6 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1576 | 36.8 | 39.77 | 38.31 | 38.31 | -0.4 | 0.56 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1216 | 37.34 | 38.93 | 37.97 | 38.71 | -0.5 | 0.53 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1397 | 37.15 | 39.05 | 37.74 | 37.81 | -0.56 | 0.36 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1210 | 37.52 | 40.22 | 37.8 | 37.59 | -0.4 | 0.25 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | parameter_variant | variant_not_baseline | 2005 | 36.71 | 38.66 | 37.23 | 38.49 | -0.67 | 0.24 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | parameter_variant | variant_not_baseline | 954 | 37.74 | 39.3 | 37.26 | 37.41 | -0.51 | 0.11 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | parameter_variant | variant_not_baseline | 1773 | 37.28 | 38.01 | 36.83 | 37.87 | -0.82 | 0.06 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | parameter_variant | variant_not_baseline | 1527 | 37.46 | 37.77 | 36.57 | 38.22 | -0.86 | 0.03 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1083 | 37.58 | 39.72 | 37.17 | 36.71 | -0.53 | 0.02 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| w_bottom_right_side | wproxy_vol1 | parameter_variant | variant_not_baseline | 47386 | 38.85 | 41.95 | 42.81 | 44.74 | 0.29 | 1.3 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | parameter_variant | variant_not_baseline | 38227 | 38.53 | 41.43 | 42.23 | 44.42 | 0.23 | 1.3 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | production_current_proxy | production_baseline | production_proxy | 88619 | 39.25 | 42.82 | 43.47 | 45.24 | 0.35 | 1.28 | ok_first_pass | production baseline proxy: W-bottom geometry proxy and not already a breakout |
| w_bottom_right_side | wproxy_vol1.5 | parameter_variant | variant_not_baseline | 28589 | 38.1 | 40.9 | 41.75 | 43.82 | 0.15 | 1.26 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
