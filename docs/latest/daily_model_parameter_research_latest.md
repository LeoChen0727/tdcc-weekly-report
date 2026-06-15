# Daily Model Parameter Research

- generated_at: `2026-06-15 16:25:21 Asia/Taipei`
- price_history_files: `2370`
- max_price_rows: `280`
- data_range: `20250407` ~ `20260612`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 265 | 175 | D+10 | 69.18 | 9.26 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1397 | 452 | D+10 | 57.65 | 6.98 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 618 | 321 | D+7 | 75.0 | 5.28 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 2313 | 681 | D+10 | 52.59 | 5.03 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 757 | 371 | D+7 | 72.88 | 5.01 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 657 | 390 | D+10 | 44.76 | 3.85 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1519 | 845 | D+10 | 48.97 | 2.69 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2383 | 1056 | D+10 | 49.72 | 2.62 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3090 | 1085 | D+10 | 44.72 | 2.41 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3363 | 1195 | D+10 | 49.44 | 2.32 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 16636 | 1269 | D+10 | 55.3 | 2.29 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | production_current | production_baseline | production_parity | 4349 | 1274 | D+10 | 44.82 | 2.24 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 24273 | 1662 | D+10 | 53.17 | 2.23 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2324 | 983 | D+10 | 43.19 | 2.23 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 27457 | 1686 | D+10 | 52.54 | 2.2 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3819 | 1180 | D+10 | 44.67 | 2.19 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2504 | 920 | D+10 | 44.04 | 2.16 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3055 | 997 | D+10 | 44.43 | 2.13 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4808 | 1302 | D+10 | 44.5 | 2.11 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3823 | 1109 | D+10 | 44.36 | 2.05 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2772 | 1067 | D+10 | 43.03 | 2.03 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3342 | 1162 | D+10 | 42.98 | 1.98 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1842 | 820 | D+10 | 42.21 | 1.93 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12550 | 1507 | D+10 | 44.75 | 1.91 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2175 | 890 | D+10 | 42.51 | 1.9 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3716 | 1260 | D+10 | 43.66 | 1.88 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2607 | 978 | D+10 | 42.62 | 1.88 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4643 | 1360 | D+10 | 43.95 | 1.79 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 1502 | 578 | D+6 | 57.86 | 1.75 | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1502 | 578 | D+6 | 57.86 | 1.75 | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |

## All Model Parameter Summary

| model_id | parameter_set_id | parameter_role | production_parity_status | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | parameter_variant | variant_not_baseline | 7646 | 38.41 | 39.77 | 38.89 | 40.87 | -0.35 | 0.72 | ok_first_pass | 量比 >= 3 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol5_solid_red | parameter_variant | variant_not_baseline | 3190 | 39.25 | 38.91 | 37.37 | 39.59 | -0.62 | 0.14 | ok_first_pass | 量比 >= 5 + 實體紅K + 上影線小 + 收盤接近日高 |
| explosive_volume_red_candle | vol10_solid_red | parameter_variant | variant_not_baseline | 799 | 38.05 | 38.44 | 36.06 | 36.4 | -1.09 | -0.76 | ok_first_pass | 量比 >= 10 + 實體紅K + 上影線小 + 收盤接近日高 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 618 | 45.63 | 65.37 | 67.52 |  | 2.68 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | parameter_variant | variant_not_baseline | 757 | 43.99 | 61.68 | 62.98 |  | 2.15 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_supported + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | production_current_proxy | production_baseline | production_proxy | 1502 | 43.61 | 56.14 | 57.13 |  | 1.22 |  | ok_first_pass | production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 1502 | 43.61 | 56.14 | 57.13 |  | 1.22 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | parameter_variant | variant_not_baseline | 884 | 42.19 | 49.48 | 49.49 |  | 0.14 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -2.5% 至 5% 或接近20日支撐 8% 內 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1944 | 42.8 | 52.96 | 52.91 |  | 0.65 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_any + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | parameter_variant | variant_not_baseline | 1187 | 42.04 | 47.25 | 46.01 |  | -0.38 |  | ok_first_pass | 歷史熱門/主流族群狀態 strict_mainstream_overheated + 距 23EMA -4% 至 7% 或接近20日支撐 10% 內 |
| near_high_neckline_challenge | near3_vol1.5 | parameter_variant | variant_not_baseline | 7981 | 38.94 | 40.8 | 41.38 | 42.61 | -0.04 | 0.85 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near5_vol1.5 | parameter_variant | variant_not_baseline | 13304 | 39.02 | 40.5 | 41.01 | 42.58 | 0.0 | 0.85 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.5 + 23EMA 向上 |
| near_high_neckline_challenge | near3_vol1.2 | parameter_variant | variant_not_baseline | 10973 | 39.36 | 40.95 | 41.36 | 42.84 | 0.02 | 0.81 | ok_first_pass | 距 60 日高點下方 3% 內 + 量比 >= 1.2 + 23EMA 向上 |
| near_high_neckline_challenge | production_current_proxy | production_baseline | production_proxy | 17861 | 39.26 | 40.89 | 41.36 | 42.77 | 0.03 | 0.76 | ok_first_pass | production baseline proxy: within 5% below 60d high + volume >= 1.2 + EMA23 up |
| near_high_neckline_challenge | near5_vol1.2 | parameter_variant | variant_not_baseline | 18696 | 39.35 | 40.9 | 41.29 | 42.64 | 0.03 | 0.75 | ok_first_pass | 距 60 日高點下方 5% 內 + 量比 >= 1.2 + 23EMA 向上 |
| platform_strengthening | w20_near5_vol1.5 | parameter_variant | variant_not_baseline | 7944 | 39.12 | 41.75 | 41.36 | 41.78 | 0.04 | 0.39 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | production_current_proxy | production_baseline | production_proxy | 11572 | 39.85 | 42.0 | 41.84 | 41.75 | 0.05 | 0.34 | ok_first_pass | production baseline proxy: 20d range width <= 18%, near upper edge, volume >= 1.2, solid red candle |
| platform_strengthening | w20_near5_vol1.2 | parameter_variant | variant_not_baseline | 11572 | 39.85 | 42.0 | 41.84 | 41.75 | 0.05 | 0.34 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.2 | parameter_variant | variant_not_baseline | 8754 | 39.54 | 42.1 | 41.7 | 41.64 | -0.0 | 0.3 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w20_near3_vol1.5 | parameter_variant | variant_not_baseline | 6214 | 38.3 | 41.36 | 40.7 | 41.2 | -0.07 | 0.29 | ok_first_pass | 20日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.2 | parameter_variant | variant_not_baseline | 6053 | 39.9 | 41.96 | 40.81 | 41.4 | -0.02 | 0.24 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.2 | parameter_variant | variant_not_baseline | 8441 | 40.18 | 42.23 | 41.44 | 41.43 | 0.01 | 0.24 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.2 + 實體紅K |
| platform_strengthening | w30_near5_vol1.5 | parameter_variant | variant_not_baseline | 5947 | 39.28 | 41.8 | 41.11 | 41.31 | -0.0 | 0.22 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 5% 內 + 量比 >= 1.5 + 實體紅K |
| platform_strengthening | w30_near3_vol1.5 | parameter_variant | variant_not_baseline | 4359 | 38.5 | 41.53 | 40.38 | 41.4 | -0.05 | 0.2 | ok_first_pass | 30日區間寬度 <= 18% + 距區間上緣 3% 內 + 量比 >= 1.5 + 實體紅K |
| price_pullback_23ema | ema-4_7_volmax1 | parameter_variant | variant_not_baseline | 77036 | 38.31 | 42.43 | 43.08 | 44.2 | 0.23 | 0.96 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | parameter_variant | variant_not_baseline | 88457 | 38.44 | 42.52 | 43.21 | 44.3 | 0.24 | 0.96 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | parameter_variant | variant_not_baseline | 99377 | 38.54 | 42.49 | 43.21 | 44.36 | 0.24 | 0.96 | ok_first_pass | 距 23EMA -4% 至 7% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | parameter_variant | variant_not_baseline | 68456 | 38.27 | 42.2 | 42.89 | 43.94 | 0.19 | 0.86 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | parameter_variant | variant_not_baseline | 78275 | 38.4 | 42.28 | 43.02 | 44.0 | 0.2 | 0.85 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | parameter_variant | variant_not_baseline | 87449 | 38.5 | 42.28 | 43.04 | 44.04 | 0.2 | 0.85 | ok_first_pass | 距 23EMA -2.5% 至 5% + 23EMA 向上 + 量比 <= 1.5 |
| price_pullback_23ema | production_current_proxy | production_baseline | production_proxy | 105679 | 38.53 | 42.16 | 42.82 | 43.91 | 0.19 | 0.84 | ok_first_pass | production baseline proxy: near 23EMA/support + EMA23 slope proxy up |
| price_pullback_23ema | ema-1.5_3_volmax1 | parameter_variant | variant_not_baseline | 53341 | 38.26 | 42.09 | 42.75 | 43.79 | 0.16 | 0.75 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | parameter_variant | variant_not_baseline | 60503 | 38.41 | 42.2 | 42.87 | 43.82 | 0.17 | 0.74 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | parameter_variant | variant_not_baseline | 66975 | 38.54 | 42.18 | 42.84 | 43.78 | 0.16 | 0.73 | ok_first_pass | 距 23EMA -1.5% 至 3% + 23EMA 向上 + 量比 <= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | parameter_variant | variant_not_baseline | 1519 | 38.71 | 43.0 | 45.51 | 48.97 | 1.31 | 2.69 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | parameter_variant | variant_not_baseline | 2383 | 37.85 | 43.04 | 46.48 | 49.72 | 1.23 | 2.62 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | parameter_variant | variant_not_baseline | 3363 | 38.42 | 43.12 | 45.77 | 49.44 | 1.07 | 2.32 | ok_first_pass | 前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= 1 |
| pullback_short_reclaim | production_current_proxy | production_baseline | production_proxy | 88658 | 38.59 | 42.68 | 43.99 | 45.56 | 0.49 | 1.7 | ok_first_pass | production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up |
| revenue_unreacted_range | production_current_proxy | production_baseline | proxy_only | 453519 | 39.89 | 42.79 | 43.42 | 43.82 | 0.24 | 0.53 | ok_first_pass | production baseline proxy: price still in 23d range and attack not started; revenue panel missing |
| revenue_unreacted_range | range23_tol5 | parameter_variant | variant_not_baseline | 331637 | 39.78 | 42.44 | 42.92 | 43.36 | 0.1 | 0.25 | ok_first_pass | 股價位於 23 日區間上下 5% 內；營收確認由每日模型層欄位提供 |
| revenue_unreacted_range | range23_tol10 | parameter_variant | variant_not_baseline | 333285 | 39.76 | 42.42 | 42.89 | 43.33 | 0.09 | 0.25 | ok_first_pass | 股價位於 23 日區間上下 10% 內；營收確認由每日模型層欄位提供 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | parameter_variant | variant_not_baseline | 12550 | 37.83 | 40.04 | 42.05 | 44.75 | 0.32 | 1.91 | ok_first_pass | 5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | parameter_variant | variant_not_baseline | 265 | 38.11 | 42.86 | 45.05 | 69.18 | 1.49 | 9.26 | ok_first_pass | 高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | parameter_variant | variant_not_baseline | 1397 | 40.59 | 41.84 | 45.2 | 57.65 | 1.54 | 6.98 | ok_first_pass | 四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | production_baseline | production_proxy | 2313 | 39.21 | 40.5 | 44.16 | 52.59 | 0.86 | 5.03 | ok_first_pass | production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD |
| tdcc_stealth_accumulation | tdcc_up2_range10 | parameter_variant | variant_not_baseline | 16636 | 41.79 | 47.92 | 51.29 | 55.3 | 1.09 | 2.29 | ok_first_pass | TDCC 連續增加週數 >= 2 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | production_current_proxy | production_baseline | production_proxy | 24273 | 40.04 | 44.98 | 48.35 | 53.17 | 0.73 | 2.23 | ok_first_pass | production baseline proxy: TDCC positive, attack not started, low volume/return, still in range |
| tdcc_stealth_accumulation | tdcc_up1_range10 | parameter_variant | variant_not_baseline | 27457 | 39.75 | 44.07 | 47.61 | 52.54 | 0.67 | 2.2 | ok_first_pass | TDCC 連續增加週數 >= 1 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | parameter_variant | variant_not_baseline | 10144 | 40.61 | 45.83 | 50.04 | 49.33 | 0.65 | 0.81 | ok_first_pass | TDCC 連續增加週數 >= 3 + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20% |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | parameter_variant | variant_not_baseline | 657 | 23.14 | 46.33 | 42.81 | 44.76 | 0.95 | 3.85 | ok_first_pass | 鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3090 | 39.77 | 42.37 | 41.23 | 44.72 | 0.14 | 2.41 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | production_current | production_baseline | production_parity | 4349 | 37.34 | 43.07 | 41.82 | 44.82 | 0.23 | 2.24 | ok_first_pass | production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2324 | 39.11 | 41.16 | 40.25 | 43.19 | 0.13 | 2.23 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | parameter_variant | variant_not_baseline | 3819 | 39.38 | 42.4 | 41.59 | 44.67 | 0.14 | 2.19 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | parameter_variant | variant_not_baseline | 2504 | 39.06 | 42.49 | 40.71 | 44.04 | 0.06 | 2.16 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3055 | 38.85 | 42.81 | 41.28 | 44.43 | 0.16 | 2.13 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | parameter_variant | variant_not_baseline | 4808 | 39.33 | 42.04 | 41.71 | 44.5 | 0.2 | 2.11 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | parameter_variant | variant_not_baseline | 3823 | 39.05 | 42.27 | 41.45 | 44.36 | 0.2 | 2.05 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | parameter_variant | variant_not_baseline | 2772 | 39.07 | 41.35 | 40.52 | 43.03 | 0.12 | 2.03 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | parameter_variant | variant_not_baseline | 3342 | 39.08 | 41.03 | 40.61 | 42.98 | 0.16 | 1.98 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | parameter_variant | variant_not_baseline | 1842 | 38.49 | 41.03 | 39.68 | 42.21 | 0.07 | 1.93 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2175 | 38.62 | 41.67 | 40.23 | 42.51 | 0.16 | 1.9 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | parameter_variant | variant_not_baseline | 2607 | 38.82 | 41.19 | 40.45 | 42.62 | 0.2 | 1.88 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | parameter_variant | variant_not_baseline | 3716 | 39.64 | 41.59 | 40.25 | 43.66 | -0.19 | 1.88 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol2_minvol500 | parameter_variant | variant_not_baseline | 4643 | 39.18 | 41.76 | 40.73 | 43.95 | -0.12 | 1.79 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | parameter_variant | variant_not_baseline | 5887 | 38.63 | 41.43 | 40.9 | 43.69 | -0.04 | 1.73 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 2 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol3_minvol500 | parameter_variant | variant_not_baseline | 2827 | 39.05 | 40.4 | 39.41 | 42.24 | -0.18 | 1.7 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol3_minvol500 | parameter_variant | variant_not_baseline | 3422 | 38.87 | 40.68 | 39.84 | 42.46 | -0.14 | 1.61 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol3_minvol500 | parameter_variant | variant_not_baseline | 4149 | 38.47 | 40.43 | 39.89 | 42.23 | -0.1 | 1.56 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 3 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1293 | 37.82 | 39.13 | 36.83 | 38.09 | -0.64 | 0.78 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1667 | 37.43 | 39.43 | 37.1 | 37.9 | -0.56 | 0.69 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol1000 | parameter_variant | variant_not_baseline | 1474 | 37.65 | 39.0 | 36.56 | 37.46 | -0.69 | 0.57 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 1000張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1033 | 38.14 | 39.47 | 36.35 | 36.97 | -0.61 | 0.49 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1304 | 37.96 | 39.81 | 36.71 | 37.25 | -0.53 | 0.48 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.01_vol5_minvol500 | parameter_variant | variant_not_baseline | 2094 | 37.2 | 38.54 | 36.47 | 38.46 | -0.79 | 0.46 | ok_first_pass | 收盤突破前20日高點 1% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.03_vol5_minvol500 | parameter_variant | variant_not_baseline | 1597 | 37.88 | 38.11 | 35.95 | 38.22 | -0.97 | 0.39 | ok_first_pass | 收盤突破前20日高點 3% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol2000 | parameter_variant | variant_not_baseline | 1162 | 37.95 | 39.65 | 36.16 | 36.66 | -0.62 | 0.38 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 2000張 + 實體紅K |
| volume_range_breakout | prior20x1.02_vol5_minvol500 | parameter_variant | variant_not_baseline | 1846 | 37.65 | 38.11 | 36.09 | 37.94 | -0.93 | 0.35 | ok_first_pass | 收盤突破前20日高點 2% + 量比 >= 5 + 20日均量 >= 500張 + 實體紅K |
| w_bottom_right_side | wproxy_vol1 | parameter_variant | variant_not_baseline | 50207 | 38.63 | 41.3 | 42.18 | 43.95 | 0.2 | 1.12 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | parameter_variant | variant_not_baseline | 40571 | 38.47 | 40.93 | 41.67 | 43.61 | 0.14 | 1.12 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | parameter_variant | variant_not_baseline | 30407 | 38.11 | 40.5 | 41.16 | 43.15 | 0.06 | 1.09 | ok_first_pass | W底近似條件 + 右側結構墊高 + 量比 >= 1.5 |
| w_bottom_right_side | production_current_proxy | production_baseline | production_proxy | 95910 | 38.82 | 42.13 | 42.87 | 44.28 | 0.27 | 1.07 | ok_first_pass | production baseline proxy: W-bottom geometry proxy and not already a breakout |
