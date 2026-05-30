# Daily Model Parameter Research

- generated_at: `2026-05-30 20:32:44 Asia/Taipei`
- price_history_files: `2368`
- max_price_rows: `273`
- data_range: `20250407` ~ `20260529`
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 161 | 107 | D+10 | 76.71 | 15.56 | ok_first_pass | High thresholds up + 5d return 10-30% + 10d return 20-50% + KD bullish not overheated |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 903 | 300 | D+10 | 63.23 | 9.18 | ok_first_pass | All thresholds up + 5d return 10-30% + MACD hist > 0 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 1480 | 827 | D+10 | 48.96 | 2.69 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 2326 | 1038 | D+10 | 49.67 | 2.59 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 3282 | 1179 | D+10 | 49.29 | 2.26 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 12006 | 1484 | D+10 | 44.18 | 1.76 | ok_first_pass | 5d return 10-30% + 5d average volume ratio >= 1.5 + MACD hist > 0 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 11599 | 928 | D+7 | 48.17 | 1.09 | ok_first_pass | TDCC consecutive up weeks >= 2 + price within 23d range +/-10% + 20d return <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 20547 | 1537 | D+9 | 45.46 | 1.07 | ok_first_pass | TDCC consecutive up weeks >= 1 + price within 23d range +/-10% + 20d return <= 20% |
| w_bottom_right_side | wproxy_vol1 | 48061 | 1960 | D+10 | 43.44 | 1.0 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | 38800 | 1959 | D+10 | 43.13 | 1.0 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | 29059 | 1952 | D+10 | 42.69 | 0.97 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.5 |
| price_pullback_23ema | ema-4_7_volmax1.5 | 94922 | 1965 | D+10 | 43.65 | 0.81 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 84445 | 1965 | D+10 | 43.56 | 0.79 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-4_7_volmax1 | 73468 | 1965 | D+10 | 43.42 | 0.79 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1 |
| near_high_neckline_challenge | near5_vol1.5 | 12793 | 1820 | D+10 | 42.03 | 0.74 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.5 | 7657 | 1655 | D+10 | 42.16 | 0.73 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.2 | 10503 | 1708 | D+10 | 42.39 | 0.7 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 83867 | 1964 | D+10 | 43.32 | 0.69 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 75056 | 1963 | D+10 | 43.25 | 0.68 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1 | 65600 | 1963 | D+10 | 43.16 | 0.68 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1 |
| volume_range_breakout | w10_vol1.2_width25 | 13789 | 1924 | D+10 | 41.42 | 0.68 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width25 | 12129 | 1911 | D+10 | 40.98 | 0.65 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w10_vol2_width25 | 9607 | 1879 | D+10 | 40.76 | 0.65 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 25% |
| near_high_neckline_challenge | near5_vol1.2 | 17960 | 1856 | D+10 | 42.07 | 0.64 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| price_pullback_23ema | ema-1.5_3_volmax1 | 51372 | 1955 | D+10 | 43.04 | 0.6 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1 |
| explosive_volume_red_candle | vol3_solid_red | 7382 | 1800 | D+10 | 40.35 | 0.6 | ok_first_pass | Volume ratio >= 3 + solid red candle + small upper shadow + close near high |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | 64521 | 1962 | D+10 | 43.08 | 0.59 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 58278 | 1959 | D+10 | 43.09 | 0.59 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.2 |
| volume_range_breakout | w10_vol3_width25 | 6242 | 1709 | D+10 | 39.68 | 0.49 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w10_vol1.2_width18 | 11799 | 1912 | D+10 | 40.54 | 0.44 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 18% |

## All Model Parameter Summary

| model_id | parameter_set_id | selected_stock_days | d1_close_win_rate_pct | d3_close_win_rate_pct | d5_close_win_rate_pct | d10_close_win_rate_pct | d5_avg_close_return_pct | d10_avg_close_return_pct | sample_status | parameter_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | 7382 | 38.05 | 39.45 | 38.73 | 40.35 | -0.36 | 0.6 | ok_first_pass | Volume ratio >= 3 + solid red candle + small upper shadow + close near high |
| explosive_volume_red_candle | vol5_solid_red | 3113 | 39.16 | 38.81 | 37.39 | 39.07 | -0.62 | -0.0 | ok_first_pass | Volume ratio >= 5 + solid red candle + small upper shadow + close near high |
| explosive_volume_red_candle | vol10_solid_red | 789 | 37.9 | 38.22 | 35.69 | 36.03 | -1.14 | -0.8 | ok_first_pass | Volume ratio >= 10 + solid red candle + small upper shadow + close near high |
| near_high_neckline_challenge | near5_vol1.5 | 12793 | 38.54 | 40.15 | 40.57 | 42.03 | -0.02 | 0.74 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.5 | 7657 | 38.34 | 40.36 | 41.0 | 42.16 | -0.06 | 0.73 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.5 + rising 23EMA |
| near_high_neckline_challenge | near3_vol1.2 | 10503 | 38.84 | 40.6 | 40.98 | 42.39 | 0.01 | 0.7 | ok_first_pass | Within 3% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| near_high_neckline_challenge | near5_vol1.2 | 17960 | 38.91 | 40.57 | 40.85 | 42.07 | 0.01 | 0.64 | ok_first_pass | Within 5% below 60d high + volume ratio >= 1.2 + rising 23EMA |
| platform_strengthening | w20_near5_vol1.5 | 7509 | 37.98 | 40.57 | 40.59 | 41.31 | -0.04 | 0.32 | ok_first_pass | 20d range width <= 18% + within 5% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w20_near5_vol1.2 | 10946 | 38.83 | 40.89 | 40.99 | 41.27 | -0.03 | 0.26 | ok_first_pass | 20d range width <= 18% + within 5% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w20_near3_vol1.2 | 8275 | 38.43 | 40.95 | 40.92 | 41.27 | -0.08 | 0.23 | ok_first_pass | 20d range width <= 18% + within 3% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w20_near3_vol1.5 | 5877 | 37.06 | 40.14 | 39.94 | 40.82 | -0.15 | 0.22 | ok_first_pass | 20d range width <= 18% + within 3% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w30_near5_vol1.2 | 7969 | 39.09 | 41.06 | 40.68 | 40.94 | -0.05 | 0.16 | ok_first_pass | 30d range width <= 18% + within 5% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w30_near3_vol1.2 | 5714 | 38.66 | 40.88 | 40.15 | 40.94 | -0.08 | 0.15 | ok_first_pass | 30d range width <= 18% + within 3% of range high + volume ratio >= 1.2 + solid red candle |
| platform_strengthening | w30_near5_vol1.5 | 5606 | 38.0 | 40.53 | 40.44 | 40.81 | -0.07 | 0.15 | ok_first_pass | 30d range width <= 18% + within 5% of range high + volume ratio >= 1.5 + solid red candle |
| platform_strengthening | w30_near3_vol1.5 | 4104 | 37.09 | 40.35 | 39.77 | 40.89 | -0.11 | 0.12 | ok_first_pass | 30d range width <= 18% + within 3% of range high + volume ratio >= 1.5 + solid red candle |
| price_pullback_23ema | ema-4_7_volmax1.5 | 94922 | 38.4 | 42.35 | 42.94 | 43.65 | 0.24 | 0.81 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-4_7_volmax1 | 73468 | 38.2 | 42.34 | 42.9 | 43.42 | 0.24 | 0.79 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-4_7_volmax1.2 | 84445 | 38.33 | 42.41 | 42.98 | 43.56 | 0.25 | 0.79 | ok_first_pass | Distance to 23EMA -4% to 7% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | 83867 | 38.34 | 42.07 | 42.7 | 43.32 | 0.19 | 0.69 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.5 |
| price_pullback_23ema | ema-2.5_5_volmax1 | 65600 | 38.13 | 42.03 | 42.65 | 43.16 | 0.19 | 0.68 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | 75056 | 38.26 | 42.1 | 42.73 | 43.25 | 0.19 | 0.68 | ok_first_pass | Distance to 23EMA -2.5% to 5% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1 | 51372 | 38.13 | 41.83 | 42.43 | 43.04 | 0.15 | 0.6 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | 58278 | 38.27 | 41.92 | 42.5 | 43.09 | 0.15 | 0.59 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.2 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | 64521 | 38.4 | 41.89 | 42.44 | 43.08 | 0.14 | 0.59 | ok_first_pass | Distance to 23EMA -1.5% to 3% + rising 23EMA + volume ratio <= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | 1480 | 38.72 | 43.22 | 45.55 | 48.96 | 1.32 | 2.69 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.5 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | 2326 | 37.88 | 43.08 | 46.38 | 49.67 | 1.24 | 2.59 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1.2 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | 3282 | 38.39 | 43.02 | 45.48 | 49.29 | 1.05 | 2.26 | ok_first_pass | Prior 20d return >= 10% + distance to 23EMA -1% to 6% + MACD hist > 0 + volume ratio >= 1 |
| revenue_unreacted_range_proxy | range23_tol5 | 325154 | 39.55 | 42.04 | 42.41 | 42.78 | 0.05 | 0.17 | ok_first_pass | Price within 23d range +/- 5% proxy; actual revenue confirmation comes from daily candidate layer |
| revenue_unreacted_range_proxy | range23_tol10 | 326700 | 39.53 | 42.01 | 42.39 | 42.76 | 0.05 | 0.17 | ok_first_pass | Price within 23d range +/- 10% proxy; actual revenue confirmation comes from daily candidate layer |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | 12006 | 37.6 | 40.15 | 42.24 | 44.18 | 0.36 | 1.76 | ok_first_pass | 5d return 10-30% + 5d average volume ratio >= 1.5 + MACD hist > 0 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | 161 | 36.65 | 47.26 | 57.26 | 76.71 | 4.48 | 15.56 | ok_first_pass | High thresholds up + 5d return 10-30% + 10d return 20-50% + KD bullish not overheated |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | 903 | 38.76 | 43.24 | 50.8 | 63.23 | 3.2 | 9.18 | ok_first_pass | All thresholds up + 5d return 10-30% + MACD hist > 0 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | 11599 | 40.08 | 44.81 | 47.18 | 46.0 | 0.91 | 0.54 | ok_first_pass | TDCC consecutive up weeks >= 2 + price within 23d range +/-10% + 20d return <= 20% |
| tdcc_stealth_accumulation | tdcc_up1_range10 | 20547 | 37.71 | 40.56 | 43.2 | 45.02 | 0.41 | 1.05 | ok_first_pass | TDCC consecutive up weeks >= 1 + price within 23d range +/-10% + 20d return <= 20% |
| tdcc_stealth_accumulation | tdcc_up3_range10 | 6423 | 37.61 | 39.5 | 42.07 | 43.95 | -0.08 | -0.02 | ok_first_pass | TDCC consecutive up weeks >= 3 + price within 23d range +/-10% + 20d return <= 20% |
| volume_range_breakout | w10_vol1.2_width25 | 13789 | 38.42 | 39.83 | 40.34 | 41.42 | -0.09 | 0.68 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width25 | 12129 | 37.6 | 39.28 | 39.93 | 40.98 | -0.14 | 0.65 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w10_vol2_width25 | 9607 | 36.98 | 38.38 | 39.02 | 40.76 | -0.22 | 0.65 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 25% |
| volume_range_breakout | w10_vol3_width25 | 6242 | 37.26 | 37.86 | 38.34 | 39.68 | -0.35 | 0.49 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w10_vol1.2_width18 | 11799 | 37.98 | 39.32 | 39.74 | 40.54 | -0.2 | 0.44 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 18% |
| volume_range_breakout | w20_vol2_width25 | 6300 | 36.73 | 38.09 | 39.14 | 39.93 | -0.28 | 0.44 | ok_first_pass | 20d range breakout + volume ratio >= 2 + range width <= 25% |
| volume_range_breakout | w20_vol1.5_width25 | 7469 | 37.43 | 38.83 | 39.78 | 40.06 | -0.24 | 0.43 | ok_first_pass | 20d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w10_vol1.5_width18 | 10310 | 37.21 | 38.87 | 39.41 | 40.13 | -0.23 | 0.42 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w20_vol1.2_width25 | 8204 | 38.19 | 39.5 | 40.28 | 40.52 | -0.2 | 0.42 | ok_first_pass | 20d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w10_vol2_width18 | 8109 | 36.43 | 37.88 | 38.3 | 39.81 | -0.34 | 0.39 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 18% |
| volume_range_breakout | w20_vol3_width25 | 4473 | 37.27 | 37.63 | 38.56 | 39.52 | -0.36 | 0.38 | ok_first_pass | 20d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w10_vol3_width18 | 5207 | 36.66 | 37.22 | 37.41 | 38.64 | -0.48 | 0.21 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 18% |
| volume_range_breakout | w10_vol1.2_width12 | 8569 | 37.23 | 38.72 | 39.11 | 39.37 | -0.31 | 0.03 | ok_first_pass | 10d range breakout + volume ratio >= 1.2 + range width <= 12% |
| volume_range_breakout | w10_vol1.5_width12 | 7391 | 36.3 | 38.18 | 38.71 | 38.95 | -0.34 | 0.03 | ok_first_pass | 10d range breakout + volume ratio >= 1.5 + range width <= 12% |
| volume_range_breakout | w20_vol1.2_width18 | 6404 | 37.34 | 39.07 | 39.52 | 39.36 | -0.38 | 0.03 | ok_first_pass | 20d range breakout + volume ratio >= 1.2 + range width <= 18% |
| volume_range_breakout | w20_vol2_width18 | 4822 | 35.44 | 37.43 | 38.18 | 38.69 | -0.48 | 0.02 | ok_first_pass | 20d range breakout + volume ratio >= 2 + range width <= 18% |
| volume_range_breakout | w30_vol3_width25 | 3197 | 36.66 | 37.68 | 38.02 | 38.58 | -0.56 | 0.02 | ok_first_pass | 30d range breakout + volume ratio >= 3 + range width <= 25% |
| volume_range_breakout | w20_vol1.5_width18 | 5776 | 36.41 | 38.28 | 38.86 | 38.8 | -0.43 | 0.01 | ok_first_pass | 20d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w30_vol1.2_width25 | 5506 | 37.18 | 38.99 | 39.48 | 39.45 | -0.4 | 0.01 | ok_first_pass | 30d range breakout + volume ratio >= 1.2 + range width <= 25% |
| volume_range_breakout | w20_vol3_width18 | 3398 | 36.05 | 36.86 | 37.32 | 38.06 | -0.58 | -0.01 | ok_first_pass | 20d range breakout + volume ratio >= 3 + range width <= 18% |
| volume_range_breakout | w30_vol2_width25 | 4346 | 35.8 | 37.94 | 38.62 | 38.74 | -0.47 | -0.01 | ok_first_pass | 30d range breakout + volume ratio >= 2 + range width <= 25% |
| volume_range_breakout | w30_vol1.5_width25 | 5041 | 36.32 | 38.23 | 39.03 | 38.85 | -0.44 | -0.02 | ok_first_pass | 30d range breakout + volume ratio >= 1.5 + range width <= 25% |
| volume_range_breakout | w10_vol2_width12 | 5659 | 35.48 | 36.71 | 37.45 | 38.57 | -0.46 | -0.03 | ok_first_pass | 10d range breakout + volume ratio >= 2 + range width <= 12% |
| volume_range_breakout | w10_vol3_width12 | 3551 | 35.48 | 35.65 | 35.96 | 37.5 | -0.69 | -0.18 | ok_first_pass | 10d range breakout + volume ratio >= 3 + range width <= 12% |
| volume_range_breakout | w30_vol1.2_width18 | 3943 | 35.96 | 38.61 | 38.56 | 37.8 | -0.55 | -0.42 | ok_first_pass | 30d range breakout + volume ratio >= 1.2 + range width <= 18% |
| volume_range_breakout | w30_vol1.5_width18 | 3578 | 34.88 | 37.68 | 37.99 | 37.07 | -0.57 | -0.45 | ok_first_pass | 30d range breakout + volume ratio >= 1.5 + range width <= 18% |
| volume_range_breakout | w30_vol2_width18 | 3032 | 34.04 | 37.11 | 37.53 | 36.85 | -0.59 | -0.45 | ok_first_pass | 30d range breakout + volume ratio >= 2 + range width <= 18% |
| volume_range_breakout | w20_vol1.2_width12 | 3981 | 37.23 | 38.51 | 38.99 | 37.72 | -0.54 | -0.47 | ok_first_pass | 20d range breakout + volume ratio >= 1.2 + range width <= 12% |
| volume_range_breakout | w20_vol2_width12 | 2852 | 34.57 | 36.21 | 37.64 | 36.82 | -0.64 | -0.52 | ok_first_pass | 20d range breakout + volume ratio >= 2 + range width <= 12% |
| volume_range_breakout | w20_vol1.5_width12 | 3519 | 36.09 | 37.39 | 38.31 | 36.95 | -0.59 | -0.51 | ok_first_pass | 20d range breakout + volume ratio >= 1.5 + range width <= 12% |
| volume_range_breakout | w30_vol3_width18 | 2226 | 34.91 | 36.16 | 36.39 | 36.21 | -0.74 | -0.52 | ok_first_pass | 30d range breakout + volume ratio >= 3 + range width <= 18% |
| volume_range_breakout | w30_vol1.2_width12 | 2172 | 35.27 | 37.55 | 38.03 | 35.71 | -0.75 | -0.91 | ok_first_pass | 30d range breakout + volume ratio >= 1.2 + range width <= 12% |
| volume_range_breakout | w30_vol1.5_width12 | 1930 | 34.15 | 36.29 | 37.28 | 34.57 | -0.82 | -1.02 | ok_first_pass | 30d range breakout + volume ratio >= 1.5 + range width <= 12% |
| volume_range_breakout | w20_vol3_width12 | 1931 | 35.63 | 35.29 | 36.41 | 36.52 | -0.82 | -0.65 | ok_first_pass | 20d range breakout + volume ratio >= 3 + range width <= 12% |
| volume_range_breakout | w30_vol2_width12 | 1596 | 33.02 | 35.78 | 37.06 | 34.36 | -0.85 | -1.04 | ok_first_pass | 30d range breakout + volume ratio >= 2 + range width <= 12% |
| volume_range_breakout | w30_vol3_width12 | 1111 | 33.66 | 34.27 | 35.72 | 33.03 | -1.12 | -1.49 | ok_first_pass | 30d range breakout + volume ratio >= 3 + range width <= 12% |
| w_bottom_right_side | wproxy_vol1 | 48061 | 38.27 | 41.02 | 41.82 | 43.44 | 0.17 | 1.0 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1 |
| w_bottom_right_side | wproxy_vol1.2 | 38800 | 38.07 | 40.64 | 41.33 | 43.13 | 0.11 | 1.0 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.2 |
| w_bottom_right_side | wproxy_vol1.5 | 29059 | 37.69 | 40.21 | 40.85 | 42.69 | 0.04 | 0.97 | ok_first_pass | W-bottom proxy + higher right-side structure + volume ratio >= 1.5 |
