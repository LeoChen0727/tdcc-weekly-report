# Daily Model Parameter Research

- generated_at: `2026-06-12 11:42:00 Asia/Taipei`
- price_history_files: `2370`
- max_price_rows: `279`
- data_range: `20250407` ~ `20260611`
- entry_basis: `signal_date_next_open`
- close_return_definition: `(D+n close / next trading day open - 1)`
- high_return_definition: `(max intraday high through D+n / next trading day open - 1)`

## Data Quality

- This is first-pass parameter research using the current repo price history.
- If sample_status is `small_sample_review_only` or `insufficient_sample`, do not treat the parameter as a final model weight.
- Revenue historical panel is not complete in price history, so the revenue-unreacted research row only validates the price-range component.

## Top Parameter Sets By Avg Close Return

| model_id | parameter_set_id | selected_stock_days | selected_unique_stocks | best_close_horizon_d1_d10 | best_close_win_rate_pct | best_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 255 | 167 | D+10 | 72.18 | 10.92 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 1361 | 442 | D+10 | 60.37 | 8.44 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | 550 | 296 | D+7 | 75.0 | 5.28 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | 677 | 343 | D+6 | 80.93 | 5.21 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 1514 | 843 | D+10 | 49.04 | 2.71 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 2375 | 1054 | D+10 | 49.78 | 2.64 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | 1354 | 544 | D+6 | 62.16 | 2.61 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | 3076 | 1079 | D+10 | 44.8 | 2.45 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 3355 | 1193 | D+10 | 49.42 | 2.33 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 15906 | 1256 | D+10 | 55.08 | 2.31 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | 2313 | 977 | D+10 | 43.3 | 2.26 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | 3805 | 1175 | D+10 | 44.81 | 2.24 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 26468 | 1676 | D+10 | 52.25 | 2.23 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | 2496 | 918 | D+10 | 44.12 | 2.19 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | 3047 | 995 | D+10 | 44.56 | 2.18 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | 1763 | 633 | D+6 | 59.07 | 2.18 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | 4792 | 1299 | D+10 | 44.64 | 2.15 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | 3813 | 1107 | D+10 | 44.5 | 2.09 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | 2761 | 1061 | D+10 | 43.17 | 2.06 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | 3329 | 1157 | D+10 | 43.1 | 2.01 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | 1836 | 818 | D+10 | 42.34 | 1.96 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | 3701 | 1256 | D+10 | 43.81 | 1.95 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 12515 | 1501 | D+10 | 44.81 | 1.93 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | 2169 | 888 | D+10 | 42.66 | 1.93 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | 2599 | 976 | D+10 | 42.76 | 1.91 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | 4628 | 1358 | D+10 | 44.14 | 1.87 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | 5870 | 1487 | D+10 | 43.86 | 1.79 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | 2816 | 1142 | D+10 | 42.4 | 1.76 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | 3411 | 1236 | D+10 | 42.64 | 1.67 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | 4136 | 1344 | D+10 | 42.39 | 1.61 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |

## All Model Parameter Summary

| model_id | parameter_set_id | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | 7635 | 38.4 | 39.8 | 38.91 | 40.92 | -0.33 | 0.73 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | 3187 | 39.25 | 38.9 | 37.44 | 39.69 | -0.59 | 0.17 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | 799 | 38.05 | 38.44 | 35.89 | 36.45 | -1.1 | -0.74 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | 550 | 46.55 | 65.37 | 71.47 |  | 3.37 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | 677 | 45.05 | 61.68 | 66.58 |  | 2.82 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | 1354 | 44.61 | 56.14 | 61.08 |  | 2.01 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | 1763 | 43.73 | 52.96 | 57.04 |  | 1.45 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | 804 | 43.28 | 49.48 | 53.56 |  | 1.02 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | 1086 | 42.91 | 47.25 | 50.6 |  | 0.52 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near3_vol1.5 | 7955 | 38.97 | 40.83 | 41.4 | 42.64 | -0.03 | 0.86 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.5 | 13259 | 39.03 | 40.56 | 41.03 | 42.58 | 0.02 | 0.86 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | 10932 | 39.37 | 41.01 | 41.39 | 42.88 | 0.04 | 0.82 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | 18625 | 39.34 | 40.98 | 41.32 | 42.64 | 0.04 | 0.76 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| platform_strengthening | w20_near5_vol1.5 | 7920 | 39.13 | 41.72 | 41.18 | 41.7 | 0.02 | 0.39 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w20_near5_vol1.2 | 11530 | 39.84 | 41.96 | 41.68 | 41.67 | 0.03 | 0.33 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | 8722 | 39.53 | 42.08 | 41.5 | 41.6 | -0.03 | 0.3 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | 6195 | 38.31 | 41.35 | 40.49 | 41.15 | -0.1 | 0.28 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | 6026 | 39.89 | 41.93 | 40.69 | 41.43 | -0.04 | 0.24 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | 8410 | 40.18 | 42.2 | 41.29 | 41.45 | -0.01 | 0.24 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | 5927 | 39.31 | 41.77 | 40.93 | 41.31 | -0.02 | 0.23 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | 4341 | 38.52 | 41.53 | 40.27 | 41.43 | -0.07 | 0.21 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1 | 76435 | 38.28 | 42.52 | 43.15 | 44.19 | 0.25 | 0.96 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 87783 | 38.42 | 42.61 | 43.27 | 44.28 | 0.26 | 0.96 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | 98649 | 38.51 | 42.59 | 43.27 | 44.34 | 0.26 | 0.96 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | 67974 | 38.23 | 42.27 | 42.94 | 43.91 | 0.21 | 0.86 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 86859 | 38.46 | 42.36 | 43.08 | 44.01 | 0.22 | 0.85 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 77730 | 38.36 | 42.36 | 43.07 | 43.97 | 0.21 | 0.84 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1 | 53006 | 38.23 | 42.14 | 42.78 | 43.75 | 0.17 | 0.74 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 60120 | 38.37 | 42.25 | 42.89 | 43.77 | 0.18 | 0.73 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | 66562 | 38.5 | 42.24 | 42.87 | 43.73 | 0.17 | 0.72 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 1514 | 38.77 | 42.97 | 45.53 | 49.04 | 1.33 | 2.71 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 2375 | 37.94 | 43.04 | 46.52 | 49.78 | 1.24 | 2.64 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 3355 | 38.48 | 43.14 | 45.79 | 49.42 | 1.08 | 2.33 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| revenue_unreacted_range | range23_tol5 | 330819 | 39.75 | 42.46 | 42.89 | 43.28 | 0.1 | 0.24 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日候選決策層提供 |
| revenue_unreacted_range | range23_tol10 | 332438 | 39.74 | 42.44 | 42.86 | 43.26 | 0.09 | 0.24 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日候選決策層提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 12515 | 37.83 | 40.2 | 42.21 | 44.81 | 0.37 | 1.93 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 255 | 38.04 | 43.88 | 48.5 | 72.18 | 2.29 | 10.92 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 1361 | 40.85 | 42.79 | 46.67 | 60.37 | 2.02 | 8.44 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 15906 | 41.63 | 48.61 | 51.64 | 55.08 | 1.19 | 2.31 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 26468 | 39.59 | 44.58 | 47.84 | 52.25 | 0.75 | 2.23 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | 9596 | 40.3 | 46.46 | 50.29 | 48.21 | 0.74 | 0.66 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | 3076 | 39.76 | 42.37 | 41.49 | 44.8 | 0.22 | 2.45 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | 2313 | 39.04 | 41.16 | 40.48 | 43.3 | 0.21 | 2.26 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | 3805 | 39.37 | 42.4 | 41.83 | 44.81 | 0.21 | 2.24 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | 2496 | 39.1 | 42.49 | 40.97 | 44.12 | 0.16 | 2.19 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | 3047 | 38.89 | 42.81 | 41.53 | 44.56 | 0.24 | 2.18 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | 4792 | 39.32 | 42.04 | 41.86 | 44.64 | 0.25 | 2.15 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | 3813 | 39.08 | 42.27 | 41.58 | 44.5 | 0.26 | 2.09 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | 2761 | 39.01 | 41.35 | 40.75 | 43.17 | 0.19 | 2.06 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | 3329 | 39.02 | 41.03 | 40.72 | 43.1 | 0.21 | 2.01 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | 1836 | 38.51 | 41.03 | 39.91 | 42.34 | 0.16 | 1.96 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | 3701 | 39.64 | 41.59 | 40.48 | 43.81 | -0.11 | 1.95 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | 2169 | 38.64 | 41.67 | 40.46 | 42.66 | 0.25 | 1.93 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | 2599 | 38.82 | 41.19 | 40.53 | 42.76 | 0.26 | 1.91 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | 4628 | 39.17 | 41.76 | 40.93 | 44.14 | -0.06 | 1.87 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | 5870 | 38.62 | 41.43 | 41.01 | 43.86 | 0.01 | 1.79 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | 2816 | 38.99 | 40.4 | 39.61 | 42.4 | -0.11 | 1.76 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | 3411 | 38.82 | 40.68 | 40.03 | 42.64 | -0.08 | 1.67 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | 4136 | 38.42 | 40.43 | 39.99 | 42.39 | -0.06 | 1.61 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | 1290 | 37.75 | 39.13 | 37.04 | 38.15 | -0.55 | 0.8 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | 1663 | 37.34 | 39.43 | 37.25 | 37.97 | -0.49 | 0.72 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | 1471 | 37.59 | 39.0 | 36.74 | 37.54 | -0.62 | 0.59 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | 2090 | 37.13 | 38.54 | 36.58 | 38.61 | -0.73 | 0.52 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | 1031 | 38.12 | 39.47 | 36.54 | 37.05 | -0.53 | 0.5 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | 1301 | 37.89 | 39.81 | 36.81 | 37.31 | -0.46 | 0.49 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | 1594 | 37.83 | 38.11 | 36.15 | 38.39 | -0.88 | 0.46 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | 1843 | 37.6 | 38.11 | 36.23 | 38.11 | -0.86 | 0.41 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | 1160 | 37.93 | 39.65 | 36.33 | 36.73 | -0.54 | 0.39 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| w_bottom_right_side | wproxy_vol1 | 49973 | 38.62 | 41.41 | 42.25 | 43.94 | 0.22 | 1.13 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | 40396 | 38.47 | 41.04 | 41.74 | 43.62 | 0.16 | 1.12 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | 30272 | 38.12 | 40.6 | 41.23 | 43.17 | 0.09 | 1.09 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
