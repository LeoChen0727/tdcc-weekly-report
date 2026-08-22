# 營收改善尚未反應模型：前向確認與特徵稽核

- generated_at: `2026-08-23 07:25:19 Asia/Taipei`
- model_id: `revenue_unreacted_range`
- artifact_version: `forward_confirmation_v3_20260822`
- 狀態：`research_only`，不可直接升格或進入 PDF 操作列。
- 來源母體：固定綁定 `20260713` source snapshot projection 中 `absolute_or_two_month_yoy_ge15` 的同股不重疊 episodes。
- 截止防線：cutoff 後新增的 current source-first episodes 不得改變本 artifact。
- 突破事件：收盤由未高於前高，首次跨到高於前 N 日最高收盤價。
- 前向選取：每條確認規則只採第一次符合事件；後來成功不得回頭取代較早已確認的失敗。
- 特徵對照：成功組使用 source 標記的真正發動日，失敗組使用 source 第一個成熟失敗突破；僅供找差異，不是可交易勝率。
- 嚴格成功：觸發收盤後 D+15 內達 +20%，且至 D+20 每日收盤均未跌回 +20% 以下。
- 操作報酬：確認日收盤成立，下一交易日開盤進場，確認日起算 D+20 收盤固定出場；本稽核尚未定義停損。
- 和局口徑：本次尚未核准和局定義；資料不足者獨立列為 right-censored，不得算失敗。
- 盤中高低：僅可用於 K 棒與收盤位置等 advisory 特徵，不得單獨支撐 promotion。
- 高報酬查核：D+20 絕對報酬達 80% 只會觸發 review candidate；primary 保留，未完成底層根因前不得判定為異常。
- 基準第一個突破嚴格成功率：`5.641%`。
- 財報範圍：本次只使用月營收；EPS、毛利率、營益率、營業利益、業外與淨利均未納入。

## 確認規則矩陣

| rule_id | rule_information_cutoff | confirmed_episode_count | confirmation_coverage_pct | strict_success_rate_pct | mature_failure_rate_pct | avg_confirmation_next_open_to_d20_close_return_pct | median_confirmation_next_open_to_d20_close_return_pct | known_4916_selected_date | known_4916_selected_outcome | known_1303_selected_date | known_1303_selected_outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prev20_next_close_ma60_gt_ma120 | next_trading_day_close | 771 | 49.5183 | 8.6111 | 91.3889 | 4.9119 | 0.9195 | 20251209 | mature_failure |  |  |
| prev20_ma60_gt_ma120 | trigger_date_close | 1001 | 64.2903 | 7.2589 | 92.7411 | 5.2088 | 0.0 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_next_close_kdj_bullish | next_trading_day_close | 1090 | 70.0064 | 6.9069 | 93.0931 | 2.3095 | -1.2903 | 20251209 | mature_failure |  |  |
| prev20_kdj_bullish_not_extreme | trigger_date_close | 1349 | 86.641 | 6.5287 | 93.4713 | 3.1392 | -0.9741 | 20251209 | mature_failure |  |  |
| prev20_next_close_obv_above_ma20 | next_trading_day_close | 1203 | 77.264 | 6.512 | 93.488 | 2.6909 | -1.1295 | 20251209 | mature_failure |  |  |
| prev20_next_close_volume_ge1_5 | next_trading_day_close | 1047 | 67.2447 | 6.4315 | 93.5685 | 2.4257 | -1.3444 | 20251209 | mature_failure |  |  |
| prev20_next_close_continuation | next_trading_day_close | 1251 | 80.3468 | 6.4048 | 93.5952 | 2.5375 | -1.2402 | 20251209 | mature_failure |  |  |
| prev20_next_close_market_bull | next_trading_day_close | 1204 | 77.3282 | 6.2445 | 93.7555 | 2.4247 | -1.2407 | 20251209 | mature_failure |  |  |
| prev20_revenue_lag_0_14 | trigger_date_close | 1182 | 75.9152 | 6.21 | 93.79 | 3.7069 | -0.7194 | 20251223 | mature_failure | 20260527 | strict_success |
| prev20_solid_red_candle | trigger_date_close | 1358 | 87.219 | 6.1709 | 93.8291 | 2.6005 | -1.4642 | 20251212 | mature_failure | 20260527 | strict_success |
| prev20_next_close_holds_breakout | next_trading_day_close | 1383 | 88.8247 | 6.0185 | 93.9815 | 2.7406 | -1.0101 | 20251209 | mature_failure |  |  |
| source_first_close_above_prev20_reference | trigger_date_close | 1459 | 93.7058 | 5.7664 | 94.2336 | 2.9828 | -1.3342 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_obv_above_ma20 | trigger_date_close | 1424 | 91.4579 | 5.6647 | 94.3353 | 2.992 | -1.0257 | 20251209 | mature_failure | 20260527 | strict_success |
| first_close_cross_prev20 | trigger_date_close | 1455 | 93.4489 | 5.641 | 94.359 | 2.9203 | -1.3225 | 20251209 | mature_failure | 20260527 | strict_success |
| first_close_cross_prev60 | trigger_date_close | 1071 | 68.7861 | 5.5102 | 94.4898 | 2.1192 | -2.0016 | 20260112 | mature_failure | 20260527 | strict_success |
| prev20_close_above_ma20_ema23 | trigger_date_close | 1453 | 93.3205 | 5.5026 | 94.4974 | 2.4966 | -1.4035 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_return20_0_25 | trigger_date_close | 1434 | 92.1002 | 5.5019 | 94.4981 | 2.7657 | -1.473 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_market_bull | trigger_date_close | 1419 | 91.1368 | 5.3223 | 94.6777 | 2.748 | -1.4108 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_volume_ge2 | trigger_date_close | 1222 | 78.4843 | 5.1146 | 94.8854 | 2.4279 | -1.6303 | 20251212 | mature_failure |  |  |
| prev20_volume_ge1_5 | trigger_date_close | 1325 | 85.0996 | 5.0448 | 94.9552 | 2.4468 | -1.6092 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_next_close_tdcc_high | next_trading_day_close | 367 | 23.571 | 5.0193 | 94.9807 | 1.8673 | -0.7557 | 20260518 | strict_success |  |  |
| first_close_cross_prev40 | trigger_date_close | 1247 | 80.0899 | 4.9123 | 95.0877 | 1.6194 | -1.4061 | 20251212 | mature_failure | 20260527 | strict_success |
| prev20_tdcc_high_thresholds_up | trigger_date_close | 572 | 36.7373 | 4.8193 | 95.1807 | 2.2087 | 0.0 | 20260518 | strict_success | 20260527 | strict_success |
| prev20_tdcc_consecutive_up_ge1 | trigger_date_close | 701 | 45.0225 | 4.6468 | 95.3532 | 2.361 | -0.0705 | 20260518 | strict_success | 20260527 | strict_success |
| prev20_revenue_lag_61_90 | trigger_date_close | 347 | 22.2864 | 4.5139 | 95.4861 | 0.1074 | -2.3933 |  |  |  |  |
| prev20_revenue_lag_15_30 | trigger_date_close | 814 | 52.28 | 3.836 | 96.164 | 1.8912 | -1.2744 | 20251209 | mature_failure |  |  |
| prev20_range23_le15 | trigger_date_close | 1213 | 77.9062 | 3.762 | 96.238 | 1.591 | -1.473 |  |  |  |  |
| prev20_revenue_lag_31_60 | trigger_date_close | 597 | 38.343 | 3.7433 | 96.2567 | 1.652 | -1.4628 |  |  |  |  |
| prev20_revenue_lag_91_126 | trigger_date_close | 175 | 11.2396 | 3.0534 | 96.9466 | 0.7449 | -1.8722 |  |  |  |  |

## 成功與失敗事件的特徵差異

| feature_id | feature_family | success_observed_count | failure_observed_count | success_hit_rate_pct | failure_hit_rate_pct | success_minus_failure_hit_rate_pct_points | strict_success_share_when_feature_hit_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breakout_prev60 | breakout | 339 | 1291 | 54.2773 | 17.1185 | 37.1588 | 45.4321 |
| breakout_prev40 | breakout | 339 | 1291 | 66.9617 | 30.2866 | 36.6751 | 36.7314 |
| ma60_gt_ma120 | technical | 339 | 1291 | 69.0265 | 39.1944 | 29.8321 | 31.6216 |
| position120_high_gt75 | price_position | 337 | 1168 | 67.9525 | 40.411 | 27.5415 | 32.6676 |
| next_close_continuation | close_confirmation | 339 | 1291 | 60.177 | 43.7645 | 16.4125 | 26.528 |
| next_close_holds_breakout | close_confirmation | 339 | 1291 | 84.6608 | 72.9667 | 11.6941 | 23.3523 |
| rsi14_ge60 | technical | 338 | 1204 | 77.5148 | 68.1894 | 9.3254 | 24.1921 |
| revenue_cumulative_ge30 | monthly_revenue | 339 | 1291 | 39.823 | 33.3075 | 6.5155 | 23.8938 |
| solid_red_candle | candle | 339 | 1291 | 69.6165 | 63.5167 | 6.0998 | 22.3485 |
| revenue_latest_ge50 | monthly_revenue | 339 | 1291 | 28.6136 | 23.8575 | 4.7561 | 23.9506 |
| obv_above_ma20 | technical | 339 | 1290 | 95.2802 | 91.3953 | 3.8849 | 21.5047 |
| revenue_lag_31_60 | revenue_freshness | 339 | 1291 | 13.8643 | 10.3796 | 3.4847 | 25.9669 |
| revenue_two_month_yoy_ge15 | monthly_revenue | 339 | 1284 | 49.8525 | 46.6511 | 3.2014 | 22.0052 |
| market_correction_or_high_risk | market_regime_risk | 339 | 1291 | 9.7345 | 6.6615 | 3.073 | 27.7311 |
| revenue_lag_61_90 | revenue_freshness | 339 | 1291 | 4.4248 | 1.6266 | 2.7982 | 41.6667 |
| volume_ge1_5 | volume | 339 | 1291 | 67.5516 | 65.4531 | 2.0985 | 21.3222 |
| kdj_bullish_not_extreme | technical | 338 | 1223 | 68.9349 | 67.4571 | 1.4778 | 22.0227 |
| revenue_lag_91_126 | revenue_freshness | 339 | 1291 | 1.7699 | 0.3098 | 1.4601 | 60.0 |
| revenue_lag_15_30 | revenue_freshness | 339 | 1291 | 20.944 | 19.907 | 1.037 | 21.6463 |
| macd_hist_gt0 | technical | 323 | 1030 | 94.4272 | 94.2718 | 0.1554 | 23.9028 |
| close_above_ma20_ema23 | technical | 339 | 1291 | 99.41 | 99.6127 | -0.2027 | 20.764 |
| kdj_j_ge100 | technical_risk | 338 | 1223 | 28.6982 | 29.5176 | -0.8194 | 21.179 |
| volume_ge2 | volume | 339 | 1291 | 50.1475 | 51.433 | -1.2855 | 20.3837 |
| market_bull | market_regime | 339 | 1291 | 90.2655 | 93.3385 | -3.073 | 20.2515 |
| revenue_lag_0_14 | revenue_freshness | 339 | 1291 | 58.9971 | 67.7769 | -8.7798 | 18.6047 |
| return20_0_25 | price_momentum | 339 | 1291 | 84.6608 | 97.0565 | -12.3957 | 18.6364 |
| position120_mid_40_75 | price_position | 337 | 1168 | 22.2552 | 34.6747 | -12.4195 | 15.625 |
| rsi14_40_70 | technical | 338 | 1204 | 66.568 | 79.7342 | -13.1662 | 18.9873 |
| position120_low_le40 | price_position | 337 | 1168 | 9.7923 | 24.9144 | -15.1221 | 10.1852 |
| tdcc_high_thresholds_up | tdcc | 95 | 193 | 29.4737 | 45.0777 | -15.604 | 24.3478 |
| tdcc_consecutive_up_ge1 | tdcc | 95 | 193 | 38.9474 | 55.4404 | -16.493 | 25.6944 |
| range23_le15 | price_shape | 339 | 1291 | 45.1327 | 75.0581 | -29.9254 | 13.6364 |

## 指定案例

| stock_id | stock_name | contrast_group | trigger_date | outcome_status | next_day_close_gt_trigger_close | volume_ratio_prev20 | ma60_gt_ma120 | obv_above_ma20 | kdj_bullish_not_extreme | tdcc_high_thresholds_up | market_regime | revenue_lag_trading_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | strict_success_launch_event | 20260527 | strict_success | False | 1.677 | True | True | False | True | strong_bull | 7.0 |
| 4916 | 事欣科 | first_mature_failure_event | 20251209 | mature_failure | True | 1.9351 | True | True | True | False | mild_bull | 16.0 |
| 4916 | 事欣科 | strict_success_launch_event | 20260518 | strict_success | True | 0.9934 | True | True | True | True | strong_bull | 0.0 |

## 高報酬底層路徑查核候選

| stock_id | stock_name | entry_date | fixed_exit_date | fixed_d20_return_pct | path_trading_row_count | max_abs_raw_close_return_1d_pct | max_abs_analysis_open_gap_pct | price_resolution_ids_in_path | bottom_level_price_path_result | review_disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8291 | 尚茂 | 20260429 | 20260527 | 503.4913 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 8291 | 尚茂 | 20260428 | 20260526 | 502.7397 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 5386 | 青雲 | 20260202 | 20260311 | 220.603 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 5386 | 青雲 | 20260203 | 20260312 | 167.4419 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6949 | 沛爾生醫-創 | 20250728 | 20250822 | 134.8348 | 20 | 10.0 | 9.9609 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6265 | 方土昶 | 20251219 | 20260119 | 132.7434 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6949 | 沛爾生醫-創 | 20250725 | 20250821 | 111.6071 | 20 | 10.0 | 9.9609 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6861 | 睿生光電 | 20260206 | 20260317 | 107.5099 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 5464 | 霖宏 | 20260422 | 20260520 | 107.3733 | 20 | 9.9685 | 9.9685 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 8438 | 昶昕 | 20251222 | 20260120 | 107.3579 | 20 | 10.0 | 9.3176 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3481 | 群創 | 20260507 | 20260603 | 106.25 | 20 | 10.0 | 9.9664 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 5426 | 振發 | 20260525 | 20260622 | 104.9096 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6735 | 美達科技 | 20260407 | 20260505 | 104.4753 | 20 | 10.0 | 9.9548 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3229 | 晟鈦 | 20260414 | 20260512 | 102.0619 | 20 | 9.9387 | 9.9875 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 2061 | 風青 | 20260505 | 20260601 | 102.0253 | 20 | 10.0 | 9.8655 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6658 | 聯策 | 20260422 | 20260520 | 100.2356 | 20 | 9.988 | 9.9548 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3093 | 港建* | 20260210 | 20260319 | 99.6296 | 20 | 9.9877 | 9.9877 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6658 | 聯策 | 20260401 | 20260430 | 96.7105 | 20 | 9.988 | 9.9548 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 5464 | 霖宏 | 20260421 | 20260519 | 95.3125 | 20 | 9.9685 | 9.9685 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 2243 | 宏旭-KY | 20260601 | 20260629 | 94.8718 | 20 | 10.0 | 9.9822 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 2243 | 宏旭-KY | 20260602 | 20260630 | 94.2078 | 20 | 10.0 | 9.9822 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 2061 | 風青 | 20260506 | 20260602 | 93.25 | 20 | 10.0 | 9.8655 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6949 | 沛爾生醫-創 | 20250711 | 20250807 | 92.8349 | 20 | 9.9609 | 9.9609 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 8043 | 蜜望實 | 20260514 | 20260610 | 88.6256 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 1714 | 和桐 | 20260605 | 20260703 | 88.0165 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 4973 | 廣穎電通 | 20260508 | 20260604 | 86.8365 | 20 | 9.9398 | 9.9042 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 2337 | 旺宏 | 20251223 | 20260121 | 86.0406 | 20 | 10.0 | 9.9193 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3339 | 泰谷 | 20260324 | 20260422 | 85.5034 | 20 | 10.0 | 9.882 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3114 | 好德 | 20260525 | 20260622 | 84.5343 | 20 | 9.9754 | 9.9476 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 8033 | 雷虎 | 20250725 | 20250821 | 83.5714 | 20 | 9.9281 | 5.9569 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3229 | 晟鈦 | 20260415 | 20260513 | 82.4847 | 20 | 9.9387 | 9.9875 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 3583 | 辛耘 | 20260312 | 20260410 | 82.3848 | 20 | 9.9783 | 8.0868 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6949 | 沛爾生醫-創 | 20260120 | 20260225 | 81.5789 | 20 | 10.0 | 5.3571 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 6654 | 天正國際 | 20260526 | 20260623 | 80.9091 | 20 | 10.0 | 10.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 8455 | 大拓-KY | 20260428 | 20260526 | 80.5869 | 20 | 9.9723 | 9.9723 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 4763 | 材料*-KY | 20250523 | 20250701 | -89.9779 | 20 | 89.774 | 89.8079 |  | scale_break_or_incomplete_path_requires_root_cause_review | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 4763 | 材料*-KY | 20250605 | 20250711 | -91.281 | 20 | 89.774 | 89.8079 |  | scale_break_or_incomplete_path_requires_root_cause_review | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
| 4763 | 材料*-KY | 20250606 | 20250714 | -91.4712 | 20 | 89.774 | 89.8079 |  | scale_break_or_incomplete_path_requires_root_cause_review | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
