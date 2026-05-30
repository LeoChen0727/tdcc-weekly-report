# Daily Model Parameter Research

- generated_at: `2026-05-30 18:01:52 Asia/Taipei`
- price_history_files: `2126`
- max_price_rows: `137`
- data_range: `20251103` ~ `20260529`
- entry_basis: `signal_date_next_open`
- close_return_definition: `(D+n close / next trading day open - 1)`
- high_return_definition: `(max intraday high through D+n / next trading day open - 1)`

## Data Quality

- This is first-pass parameter research using the current repo price history.
- If sample_status is `small_sample_review_only` or `insufficient_sample`, do not treat the parameter as a final model weight.
- Revenue historical panel is not complete in price history, so `revenue_unreacted_range_proxy` only validates the price-range component.

## Top Parameter Sets By Avg Close Return

| model_id | parameter_set_id | selected_stock_days | selected_unique_stocks | best_close_horizon_d1_d10 | best_close_win_rate_pct | best_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 160 | 106 | D+10 | 76.71 | 15.56 | ok_first_pass | High thresholds up + 5d return 10-30% + 10d return 20-50% + KD bullish not overheated |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 876 | 291 | D+10 | 65.67 | 9.97 | ok_first_pass | All thresholds up + 5d return 10-30% + MACD hist > 0 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 967 | 585 | D+10 | 49.22 | 2.63 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.2 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 6277 | 1227 | D+10 | 44.77 | 2.36 | ok_first_pass | 5d return 10-30% + 5d average volume ratio >= 1.5 + MACD hist > 0 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 1408 | 735 | D+10 | 48.43 | 2.32 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 595 | 422 | D+10 | 44.7 | 2.22 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.5 |
| w_bottom_right_side | wproxy_vol1.5 | 13575 | 1755 | D+10 | 43.41 | 1.6 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.5 |
| w_bottom_right_side | wproxy_vol1.2 | 17994 | 1804 | D+10 | 43.57 | 1.56 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.2 |
| w_bottom_right_side | wproxy_vol1 | 22137 | 1834 | D+10 | 43.87 | 1.55 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1 |
| explosive_volume_red_candle | vol3_solid_red | 4660 | 1600 | D+10 | 42.33 | 1.35 | ok_first_pass | Volume ratio >= 3 + solid red candle + small upper shadow + close near high |
| near_high_neckline_challenge | near5_vol1.5 | 6761 | 1538 | D+10 | 41.28 | 1.24 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.5 | 4227 | 1341 | D+10 | 41.08 | 1.23 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 10837 | 928 | D+7 | 48.59 | 1.21 | ok_first_pass | TDCC consecutive up weeks >= 2 + price within 23d range +/-10% + 20d return <= 20% |
| near_high_neckline_challenge | near3_vol1.2 | 5786 | 1404 | D+10 | 41.64 | 1.21 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 19299 | 1535 | D+9 | 45.85 | 1.18 | ok_first_pass | TDCC consecutive up weeks >= 1 + price within 23d range +/-10% + 20d return <= 20% |
| price_pullback_23ema | ema-4_7_volmax1 | 33302 | 1913 | D+10 | 43.57 | 1.11 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 38700 | 1919 | D+10 | 43.61 | 1.1 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.2 |
| near_high_neckline_challenge | near5_vol1.2 | 9522 | 1597 | D+10 | 41.26 | 1.09 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| price_pullback_23ema | ema-4_7_volmax1.5 | 43858 | 1922 | D+10 | 43.45 | 1.08 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.5 |
| volume_range_breakout | w10_vol1.2_width25 | 8072 | 1855 | D+10 | 41.91 | 0.94 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width25 | 7143 | 1828 | D+10 | 41.75 | 0.91 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 25% |
| price_pullback_23ema | ema-2.5_5_volmax1 | 29245 | 1908 | D+10 | 42.82 | 0.89 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1 |
| volume_range_breakout | w10_vol2_width25 | 5721 | 1753 | D+10 | 41.45 | 0.88 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 25% |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 33802 | 1913 | D+10 | 42.83 | 0.87 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 38047 | 1918 | D+10 | 42.66 | 0.86 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.5 |
| volume_range_breakout | w10_vol3_width25 | 3695 | 1491 | D+10 | 40.72 | 0.77 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 25% |
| price_pullback_23ema | ema-1.5_3_volmax1 | 22337 | 1894 | D+10 | 42.44 | 0.71 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 25580 | 1902 | D+10 | 42.33 | 0.67 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.2 |
| volume_range_breakout | w10_vol1.5_width18 | 5901 | 1788 | D+10 | 40.78 | 0.64 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w10_vol1.2_width18 | 6704 | 1825 | D+10 | 40.79 | 0.63 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 18% |

## All Model Parameter Summary

| model_id | parameter_set_id | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | 4660 | 38.43 | 40.92 | 40.13 | 42.33 | -0.08 | 1.35 | ok_first_pass | Volume ratio >= 3 + solid red candle + small upper shadow + close near high |
| explosive_volume_red_candle | vol5_solid_red | 1931 | 38.68 | 40.21 | 38.46 | 40.64 | -0.42 | 0.62 | ok_first_pass | Volume ratio >= 5 + solid red candle + small upper shadow + close near high |
| explosive_volume_red_candle | vol10_solid_red | 458 | 36.24 | 37.22 | 32.59 | 34.1 | -1.46 | -0.83 | ok_first_pass | Volume ratio >= 10 + solid red candle + small upper shadow + close near high |
| near_high_neckline_challenge | near5_vol1.5 | 6761 | 38.8 | 41.02 | 41.95 | 41.28 | 0.27 | 1.24 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.5 | 4227 | 38.63 | 41.15 | 42.04 | 41.08 | 0.19 | 1.23 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.2 | 5786 | 39.54 | 41.3 | 42.22 | 41.64 | 0.32 | 1.21 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| near_high_neckline_challenge | near5_vol1.2 | 9522 | 39.4 | 41.26 | 42.02 | 41.26 | 0.3 | 1.09 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| platform_strengthening | w20_near5_vol1.5 | 3847 | 37.43 | 41.61 | 40.77 | 41.9 | 0.14 | 0.58 | ok_first_pass | 20d range width <= 18% + within 5% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w20_near3_vol1.5 | 2996 | 36.32 | 40.85 | 40.03 | 41.21 | 0.01 | 0.49 | ok_first_pass | 20d range width <= 18% + within 3% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w20_near5_vol1.2 | 5517 | 37.94 | 41.62 | 40.86 | 41.33 | 0.08 | 0.45 | ok_first_pass | 20d range width <= 18% + within 5% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w20_near3_vol1.2 | 4146 | 37.34 | 41.37 | 40.61 | 41.03 | 0.03 | 0.42 | ok_first_pass | 20d range width <= 18% + within 3% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w30_near5_vol1.5 | 2517 | 36.71 | 40.31 | 38.97 | 38.0 | -0.07 | -0.06 | ok_first_pass | 30d range width <= 18% + within 5% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w30_near3_vol1.5 | 1886 | 35.79 | 40.49 | 38.87 | 38.11 | -0.12 | -0.08 | ok_first_pass | 30d range width <= 18% + within 3% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w30_near3_vol1.2 | 2579 | 37.57 | 40.57 | 39.15 | 38.13 | -0.11 | -0.01 | ok_first_pass | 30d range width <= 18% + within 3% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w30_near5_vol1.2 | 3539 | 37.47 | 40.19 | 38.84 | 37.75 | -0.09 | -0.08 | ok_first_pass | 30d range width <= 18% + within 5% of range high + volume ratio >= 1.2 + solid red candle |
| price_pullback_23ema | ema-4_7_volmax1 | 33302 | 38.17 | 42.43 | 42.78 | 43.57 | 0.41 | 1.11 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 38700 | 38.33 | 42.45 | 42.86 | 43.61 | 0.41 | 1.1 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1.5 | 43858 | 38.47 | 42.21 | 42.72 | 43.45 | 0.4 | 1.08 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | 29245 | 38.02 | 41.95 | 42.22 | 42.82 | 0.29 | 0.89 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 33802 | 38.15 | 41.95 | 42.33 | 42.83 | 0.29 | 0.87 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 38047 | 38.3 | 41.78 | 42.21 | 42.66 | 0.28 | 0.86 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1 | 22337 | 37.88 | 41.61 | 41.95 | 42.44 | 0.19 | 0.71 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 25580 | 38.03 | 41.54 | 41.98 | 42.33 | 0.18 | 0.67 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | 28537 | 38.18 | 41.3 | 41.72 | 42.0 | 0.16 | 0.62 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 967 | 36.19 | 42.9 | 44.65 | 49.22 | 1.07 | 2.63 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 1408 | 37.43 | 43.1 | 44.38 | 48.43 | 1.06 | 2.32 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 595 | 36.64 | 42.61 | 42.2 | 44.7 | 0.81 | 2.22 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.5 |
| revenue_unreacted_range_proxy | range23_tol5 | 104102 | 38.23 | 41.88 | 42.37 | 41.31 | 0.09 | 0.2 | ok_first_pass | Price within 23d range +/- 5% proxy; actual revenue confirmation comes from daily candidate layer |
| revenue_unreacted_range_proxy | range23_tol10 | 104912 | 38.21 | 41.85 | 42.33 | 41.27 | 0.08 | 0.19 | ok_first_pass | Price within 23d range +/- 10% proxy; actual revenue confirmation comes from daily candidate layer |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 6277 | 37.12 | 39.68 | 42.19 | 44.77 | 0.21 | 2.36 | ok_first_pass | 5d return 10-30% + 5d average volume ratio >= 1.5 + MACD hist > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 160 | 36.88 | 47.59 | 57.26 | 76.71 | 4.48 | 15.56 | ok_first_pass | High thresholds up + 5d return 10-30% + 10d return 20-50% + KD bullish not overheated |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 876 | 39.16 | 43.79 | 51.91 | 65.67 | 3.48 | 9.97 | ok_first_pass | All thresholds up + 5d return 10-30% + MACD hist > 0 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 10837 | 40.37 | 45.05 | 47.69 | 45.82 | 1.0 | 0.55 | ok_first_pass | TDCC consecutive up weeks >= 2 + price within 23d range +/-10% + 20d return <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 19299 | 37.76 | 40.57 | 43.54 | 45.14 | 0.47 | 1.15 | ok_first_pass | TDCC consecutive up weeks >= 1 + price within 23d range +/-10% + 20d return <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | 5992 | 37.6 | 39.06 | 41.69 | 43.21 | -0.11 | -0.13 | ok_first_pass | TDCC consecutive up weeks >= 3 + price within 23d range +/-10% + 20d return <= 20% |
| volume_range_breakout | w10_vol1.2_width25 | 8072 | 38.26 | 40.75 | 40.7 | 41.91 | 0.0 | 0.94 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width25 | 7143 | 37.25 | 40.17 | 40.54 | 41.75 | -0.04 | 0.91 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w10_vol2_width25 | 5721 | 36.92 | 39.31 | 39.62 | 41.45 | -0.13 | 0.88 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 25% |
| volume_range_breakout | w10_vol3_width25 | 3695 | 36.7 | 39.1 | 39.46 | 40.72 | -0.19 | 0.77 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width18 | 5901 | 37.01 | 39.67 | 39.79 | 40.78 | -0.17 | 0.64 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w10_vol1.2_width18 | 6704 | 37.89 | 40.11 | 39.79 | 40.79 | -0.16 | 0.63 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 18% |
| volume_range_breakout | w10_vol2_width18 | 4705 | 36.71 | 38.87 | 38.66 | 40.38 | -0.27 | 0.56 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 18% |
| volume_range_breakout | w20_vol1.5_width25 | 3961 | 37.16 | 39.91 | 39.82 | 40.2 | -0.27 | 0.46 | ok_first_pass | 20d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w10_vol3_width18 | 3018 | 36.41 | 38.55 | 38.21 | 39.69 | -0.36 | 0.43 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 18% |
| volume_range_breakout | w20_vol1.2_width25 | 4318 | 38.03 | 40.38 | 40.02 | 40.22 | -0.22 | 0.42 | ok_first_pass | 20d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w20_vol2_width25 | 3382 | 36.49 | 39.09 | 38.99 | 39.79 | -0.35 | 0.39 | ok_first_pass | 20d range breakout + volume ratio >= 2 + range width <= 25% |
| volume_range_breakout | w20_vol3_width25 | 2362 | 36.54 | 38.97 | 38.7 | 39.39 | -0.41 | 0.32 | ok_first_pass | 20d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width12 | 4142 | 36.19 | 39.47 | 39.21 | 39.61 | -0.18 | 0.27 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 12% |
| volume_range_breakout | w10_vol1.2_width12 | 4744 | 37.35 | 39.96 | 39.22 | 39.53 | -0.2 | 0.21 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 12% |
| volume_range_breakout | w10_vol2_width12 | 3232 | 35.95 | 38.14 | 37.99 | 39.25 | -0.29 | 0.17 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 12% |
| volume_range_breakout | w10_vol3_width12 | 2031 | 34.71 | 36.83 | 36.7 | 38.86 | -0.55 | 0.09 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 12% |
| volume_range_breakout | w20_vol1.5_width18 | 2969 | 35.77 | 38.99 | 38.63 | 38.51 | -0.48 | 0.02 | ok_first_pass | 20d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w20_vol1.2_width18 | 3258 | 36.86 | 39.6 | 38.9 | 38.5 | -0.44 | -0.01 | ok_first_pass | 20d range breakout + volume ratio >= 1.2 + range width <= 18% |
| volume_range_breakout | w20_vol3_width18 | 1741 | 34.87 | 37.72 | 37.17 | 37.75 | -0.66 | -0.02 | ok_first_pass | 20d range breakout + volume ratio >= 3 + range width <= 18% |
| volume_range_breakout | w20_vol2_width18 | 2517 | 34.92 | 38.22 | 37.81 | 38.15 | -0.56 | -0.05 | ok_first_pass | 20d range breakout + volume ratio >= 2 + range width <= 18% |
| volume_range_breakout | w20_vol1.5_width12 | 1798 | 34.98 | 38.69 | 38.36 | 36.85 | -0.51 | -0.45 | ok_first_pass | 20d range breakout + volume ratio >= 1.5 + range width <= 12% |
| volume_range_breakout | w20_vol2_width12 | 1485 | 33.47 | 37.83 | 37.67 | 36.25 | -0.56 | -0.55 | ok_first_pass | 20d range breakout + volume ratio >= 2 + range width <= 12% |
| volume_range_breakout | w30_vol1.2_width25 | 2682 | 37.88 | 39.58 | 39.5 | 37.03 | -0.49 | -0.21 | ok_first_pass | 30d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w30_vol1.5_width25 | 2440 | 37.13 | 39.5 | 39.64 | 36.87 | -0.52 | -0.21 | ok_first_pass | 30d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w20_vol1.2_width12 | 2010 | 36.52 | 39.65 | 38.62 | 36.95 | -0.47 | -0.48 | ok_first_pass | 20d range breakout + volume ratio >= 1.2 + range width <= 12% |
| volume_range_breakout | w30_vol2_width25 | 2100 | 36.62 | 39.0 | 38.87 | 36.49 | -0.63 | -0.28 | ok_first_pass | 30d range breakout + volume ratio >= 2 + range width <= 25% |
| volume_range_breakout | w30_vol3_width25 | 1518 | 37.02 | 39.53 | 38.31 | 36.41 | -0.82 | -0.29 | ok_first_pass | 30d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w20_vol3_width12 | 978 | 33.33 | 36.56 | 36.51 | 36.28 | -0.78 | -0.72 | ok_first_pass | 20d range breakout + volume ratio >= 3 + range width <= 12% |
| volume_range_breakout | w30_vol1.2_width12 | 994 | 36.02 | 38.56 | 37.33 | 31.13 | -0.75 | -1.14 | ok_first_pass | 30d range breakout + volume ratio >= 1.2 + range width <= 12% |
| volume_range_breakout | w30_vol2_width12 | 730 | 33.15 | 37.83 | 37.47 | 29.54 | -0.86 | -1.4 | ok_first_pass | 30d range breakout + volume ratio >= 2 + range width <= 12% |
| volume_range_breakout | w30_vol1.5_width12 | 879 | 34.7 | 38.24 | 37.34 | 30.25 | -0.8 | -1.23 | ok_first_pass | 30d range breakout + volume ratio >= 1.5 + range width <= 12% |
| volume_range_breakout | w30_vol1.2_width18 | 1828 | 36.0 | 38.85 | 37.7 | 33.74 | -0.78 | -0.85 | ok_first_pass | 30d range breakout + volume ratio >= 1.2 + range width <= 18% |
| volume_range_breakout | w30_vol1.5_width18 | 1651 | 34.89 | 38.64 | 37.73 | 33.44 | -0.79 | -0.9 | ok_first_pass | 30d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w30_vol2_width18 | 1397 | 33.93 | 38.02 | 37.12 | 32.9 | -0.89 | -1.02 | ok_first_pass | 30d range breakout + volume ratio >= 2 + range width <= 18% |
| volume_range_breakout | w30_vol3_width12 | 500 | 33.0 | 37.15 | 36.18 | 29.05 | -1.22 | -1.76 | ok_first_pass | 30d range breakout + volume ratio >= 3 + range width <= 12% |
| volume_range_breakout | w30_vol3_width18 | 1007 | 33.96 | 37.54 | 35.74 | 32.15 | -1.2 | -1.12 | ok_first_pass | 30d range breakout + volume ratio >= 3 + range width <= 18% |
| w_bottom_right_side | wproxy_vol1.5 | 13575 | 37.59 | 39.93 | 40.47 | 43.41 | -0.01 | 1.6 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.5 |
| w_bottom_right_side | wproxy_vol1.2 | 17994 | 38.35 | 40.37 | 40.96 | 43.57 | 0.11 | 1.56 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.2 |
| w_bottom_right_side | wproxy_vol1 | 22137 | 38.8 | 40.94 | 41.45 | 43.87 | 0.2 | 1.55 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1 |
