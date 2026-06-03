# Daily Model Parameter Research

- generated_at: `2026-06-03 20:23:08 Asia/Taipei`
- price_history_files: `2368`
- max_price_rows: `275`
- data_range: `20250407` ~ `20260602`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 200 | 136 | D+10 | 75.28 | 14.28 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 1052 | 349 | D+10 | 65.86 | 10.88 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 1488 | 831 | D+10 | 48.96 | 2.7 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 2340 | 1041 | D+10 | 49.71 | 2.6 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 3305 | 1182 | D+10 | 49.37 | 2.28 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 12136 | 1486 | D+10 | 44.53 | 1.87 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 22504 | 1612 | D+10 | 48.79 | 1.78 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 13028 | 1127 | D+10 | 51.03 | 1.65 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| w_bottom_right_side | wproxy_vol1 | 48575 | 1960 | D+10 | 43.67 | 1.07 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | 39236 | 1959 | D+10 | 43.36 | 1.07 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | 29383 | 1952 | D+10 | 42.93 | 1.05 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
| price_pullback_23ema | ema-4_7_volmax1.5 | 95953 | 1965 | D+10 | 44.0 | 0.89 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 85371 | 1965 | D+10 | 43.94 | 0.88 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1 | 74311 | 1965 | D+10 | 43.84 | 0.88 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| near_high_neckline_challenge | near5_vol1.5 | 12920 | 1820 | D+10 | 42.32 | 0.82 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.5 | 7747 | 1659 | D+10 | 42.42 | 0.81 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| price_pullback_23ema | ema-2.5_5_volmax1 | 66268 | 1963 | D+10 | 43.56 | 0.78 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 84688 | 1964 | D+10 | 43.67 | 0.77 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 75791 | 1963 | D+10 | 43.62 | 0.77 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| near_high_neckline_challenge | near3_vol1.2 | 10635 | 1712 | D+10 | 42.63 | 0.76 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | 18150 | 1856 | D+10 | 42.33 | 0.71 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| volume_range_breakout | w10_vol1.2_width25 | 14041 | 1925 | D+10 | 41.52 | 0.71 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 25% |
| price_pullback_23ema | ema-1.5_3_volmax1 | 51829 | 1956 | D+10 | 43.41 | 0.68 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| volume_range_breakout | w10_vol2_width25 | 9746 | 1882 | D+10 | 40.9 | 0.68 | ok_first_pass | 10日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 25% |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 58784 | 1960 | D+10 | 43.44 | 0.67 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| volume_range_breakout | w10_vol1.5_width25 | 12332 | 1912 | D+10 | 41.1 | 0.67 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 25% |
| explosive_volume_red_candle | vol3_solid_red | 7473 | 1804 | D+10 | 40.57 | 0.67 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | 65073 | 1963 | D+10 | 43.4 | 0.66 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| volume_range_breakout | w10_vol3_width25 | 6306 | 1714 | D+10 | 39.83 | 0.52 | ok_first_pass | 10日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 25% |
| volume_range_breakout | w20_vol1.2_width25 | 8318 | 1816 | D+10 | 40.64 | 0.46 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 25% |

## All Model Parameter Summary

| model_id | parameter_set_id | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | 7473 | 38.16 | 39.52 | 38.75 | 40.57 | -0.34 | 0.67 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | 3144 | 39.06 | 38.77 | 37.33 | 39.37 | -0.59 | 0.08 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | 794 | 37.78 | 38.15 | 35.8 | 36.23 | -1.07 | -0.79 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| near_high_neckline_challenge | near5_vol1.5 | 12920 | 38.7 | 40.32 | 40.75 | 42.32 | 0.01 | 0.82 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.5 | 7747 | 38.48 | 40.53 | 41.15 | 42.42 | -0.03 | 0.81 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | 10635 | 38.98 | 40.77 | 41.09 | 42.63 | 0.03 | 0.76 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.2 | 18150 | 39.09 | 40.76 | 41.0 | 42.33 | 0.03 | 0.71 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| platform_strengthening | w20_near5_vol1.5 | 7655 | 38.39 | 40.78 | 40.6 | 41.45 | -0.03 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w20_near5_vol1.2 | 11155 | 39.21 | 41.08 | 41.07 | 41.37 | -0.02 | 0.28 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | 8424 | 38.82 | 41.12 | 40.98 | 41.3 | -0.07 | 0.23 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | 5985 | 37.48 | 40.34 | 39.99 | 40.89 | -0.14 | 0.22 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | 8113 | 39.46 | 41.18 | 40.72 | 41.03 | -0.04 | 0.17 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | 5707 | 38.41 | 40.65 | 40.41 | 40.97 | -0.06 | 0.17 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | 5809 | 39.04 | 40.96 | 40.22 | 40.99 | -0.07 | 0.16 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | 4178 | 37.51 | 40.47 | 39.79 | 41.01 | -0.1 | 0.13 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1.5 | 95953 | 38.48 | 42.57 | 43.04 | 44.0 | 0.25 | 0.89 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-4_7_volmax1 | 74311 | 38.25 | 42.56 | 42.97 | 43.84 | 0.25 | 0.88 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 85371 | 38.39 | 42.63 | 43.06 | 43.94 | 0.25 | 0.88 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1 | 66268 | 38.2 | 42.24 | 42.73 | 43.56 | 0.2 | 0.78 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 75791 | 38.33 | 42.32 | 42.83 | 43.62 | 0.2 | 0.77 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 84688 | 38.42 | 42.3 | 42.82 | 43.67 | 0.2 | 0.77 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1 | 51829 | 38.2 | 42.07 | 42.52 | 43.41 | 0.15 | 0.68 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 58784 | 38.35 | 42.16 | 42.6 | 43.44 | 0.15 | 0.67 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | 65073 | 38.48 | 42.14 | 42.55 | 43.4 | 0.15 | 0.66 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 1488 | 38.64 | 43.2 | 45.48 | 48.96 | 1.31 | 2.7 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 2340 | 37.82 | 43.23 | 46.4 | 49.71 | 1.23 | 2.6 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 3305 | 38.46 | 43.16 | 45.55 | 49.37 | 1.06 | 2.28 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| revenue_unreacted_range_proxy | range23_tol5 | 327127 | 39.66 | 42.21 | 42.54 | 42.95 | 0.06 | 0.2 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日候選決策層提供 |
| revenue_unreacted_range_proxy | range23_tol10 | 328692 | 39.64 | 42.18 | 42.51 | 42.92 | 0.06 | 0.19 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日候選決策層提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 12136 | 37.6 | 40.26 | 42.26 | 44.53 | 0.39 | 1.87 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 200 | 37.5 | 47.2 | 54.79 | 75.28 | 3.58 | 14.28 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 1052 | 39.45 | 44.08 | 49.68 | 65.86 | 2.93 | 10.88 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 22504 | 38.85 | 42.97 | 44.61 | 48.79 | 0.52 | 1.78 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 13028 | 41.17 | 47.27 | 48.49 | 51.03 | 0.98 | 1.65 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | 7477 | 39.44 | 43.74 | 44.99 | 44.47 | 0.23 | 0.08 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | w10_vol1.2_width25 | 14041 | 38.69 | 39.95 | 40.39 | 41.52 | -0.08 | 0.71 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol2_width25 | 9746 | 37.16 | 38.47 | 39.08 | 40.9 | -0.21 | 0.68 | ok_first_pass | 10日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol1.5_width25 | 12332 | 37.85 | 39.4 | 39.99 | 41.1 | -0.13 | 0.67 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol3_width25 | 6306 | 37.33 | 37.94 | 38.36 | 39.83 | -0.33 | 0.52 | ok_first_pass | 10日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 25% |
| volume_range_breakout | w20_vol1.2_width25 | 8318 | 38.37 | 39.62 | 40.4 | 40.64 | -0.17 | 0.46 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 25% |
| volume_range_breakout | w20_vol2_width25 | 6379 | 36.86 | 38.21 | 39.26 | 40.07 | -0.26 | 0.46 | ok_first_pass | 20日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol1.2_width18 | 12023 | 38.26 | 39.46 | 39.85 | 40.62 | -0.18 | 0.45 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 18% |
| volume_range_breakout | w20_vol1.5_width25 | 7575 | 37.62 | 38.95 | 39.89 | 40.19 | -0.22 | 0.45 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol1.5_width18 | 10488 | 37.46 | 39.0 | 39.51 | 40.23 | -0.21 | 0.44 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 18% |
| volume_range_breakout | w10_vol2_width18 | 8235 | 36.62 | 37.98 | 38.4 | 39.93 | -0.31 | 0.4 | ok_first_pass | 10日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 18% |
| volume_range_breakout | w20_vol3_width25 | 4515 | 37.32 | 37.74 | 38.64 | 39.63 | -0.33 | 0.39 | ok_first_pass | 20日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol3_width18 | 5267 | 36.74 | 37.3 | 37.45 | 38.75 | -0.46 | 0.22 | ok_first_pass | 10日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 18% |
| volume_range_breakout | w20_vol1.2_width18 | 6494 | 37.56 | 39.18 | 39.68 | 39.51 | -0.34 | 0.06 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 18% |
| volume_range_breakout | w10_vol1.2_width12 | 8738 | 37.51 | 38.88 | 39.28 | 39.44 | -0.28 | 0.04 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 12% |
| volume_range_breakout | w10_vol1.5_width12 | 7521 | 36.56 | 38.34 | 38.87 | 39.04 | -0.31 | 0.04 | ok_first_pass | 10日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 12% |
| volume_range_breakout | w20_vol1.5_width18 | 5860 | 36.64 | 38.41 | 39.01 | 38.96 | -0.39 | 0.04 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 18% |
| volume_range_breakout | w20_vol2_width18 | 4883 | 35.61 | 37.54 | 38.3 | 38.85 | -0.45 | 0.04 | ok_first_pass | 20日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 18% |
| volume_range_breakout | w30_vol3_width25 | 3220 | 36.77 | 37.79 | 38.09 | 38.76 | -0.54 | 0.04 | ok_first_pass | 30日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 25% |
| volume_range_breakout | w30_vol1.2_width25 | 5575 | 37.49 | 39.08 | 39.59 | 39.56 | -0.36 | 0.02 | ok_first_pass | 30日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 25% |
| volume_range_breakout | w30_vol2_width25 | 4390 | 35.99 | 38.02 | 38.71 | 38.88 | -0.44 | 0.01 | ok_first_pass | 30日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 25% |
| volume_range_breakout | w20_vol3_width18 | 3429 | 36.13 | 36.93 | 37.42 | 38.2 | -0.54 | 0.0 | ok_first_pass | 20日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 18% |
| volume_range_breakout | w30_vol1.5_width25 | 5106 | 36.6 | 38.31 | 39.12 | 38.96 | -0.4 | -0.01 | ok_first_pass | 30日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 25% |
| volume_range_breakout | w10_vol2_width12 | 5751 | 35.7 | 36.86 | 37.58 | 38.66 | -0.44 | -0.02 | ok_first_pass | 10日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 12% |
| volume_range_breakout | w10_vol3_width12 | 3593 | 35.54 | 35.76 | 36.04 | 37.54 | -0.67 | -0.18 | ok_first_pass | 10日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 12% |
| volume_range_breakout | w30_vol1.2_width18 | 3990 | 36.29 | 38.65 | 38.71 | 37.94 | -0.52 | -0.4 | ok_first_pass | 30日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 18% |
| volume_range_breakout | w30_vol1.5_width18 | 3622 | 35.2 | 37.72 | 38.14 | 37.23 | -0.54 | -0.44 | ok_first_pass | 30日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 18% |
| volume_range_breakout | w30_vol2_width18 | 3061 | 34.27 | 37.15 | 37.68 | 37.04 | -0.56 | -0.43 | ok_first_pass | 30日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 18% |
| volume_range_breakout | w20_vol1.2_width12 | 4036 | 37.44 | 38.64 | 39.2 | 37.87 | -0.52 | -0.45 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 12% |
| volume_range_breakout | w20_vol1.5_width12 | 3570 | 36.3 | 37.55 | 38.51 | 37.11 | -0.56 | -0.49 | ok_first_pass | 20日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 12% |
| volume_range_breakout | w20_vol2_width12 | 2889 | 34.72 | 36.36 | 37.79 | 36.96 | -0.62 | -0.49 | ok_first_pass | 20日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 12% |
| volume_range_breakout | w30_vol3_width18 | 2240 | 35.04 | 36.18 | 36.54 | 36.41 | -0.69 | -0.5 | ok_first_pass | 30日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 18% |
| volume_range_breakout | w30_vol1.2_width12 | 2199 | 35.61 | 37.63 | 38.26 | 35.88 | -0.73 | -0.89 | ok_first_pass | 30日盤整區間突破 + 量比 >= 1.2 + 區間寬度 <= 12% |
| volume_range_breakout | w30_vol1.5_width12 | 1954 | 34.44 | 36.39 | 37.54 | 34.76 | -0.8 | -0.99 | ok_first_pass | 30日盤整區間突破 + 量比 >= 1.5 + 區間寬度 <= 12% |
| volume_range_breakout | w20_vol3_width12 | 1949 | 35.61 | 35.42 | 36.54 | 36.56 | -0.79 | -0.64 | ok_first_pass | 20日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 12% |
| volume_range_breakout | w30_vol2_width12 | 1611 | 33.21 | 35.88 | 37.26 | 34.54 | -0.83 | -1.01 | ok_first_pass | 30日盤整區間突破 + 量比 >= 2 + 區間寬度 <= 12% |
| volume_range_breakout | w30_vol3_width12 | 1117 | 33.66 | 34.29 | 35.89 | 33.18 | -1.1 | -1.46 | ok_first_pass | 30日盤整區間突破 + 量比 >= 3 + 區間寬度 <= 12% |
| w_bottom_right_side | wproxy_vol1 | 48575 | 38.44 | 41.25 | 41.97 | 43.67 | 0.2 | 1.07 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | 39236 | 38.24 | 40.85 | 41.47 | 43.36 | 0.14 | 1.07 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | 29383 | 37.85 | 40.43 | 41.0 | 42.93 | 0.07 | 1.05 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
