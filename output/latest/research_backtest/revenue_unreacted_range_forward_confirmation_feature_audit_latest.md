# 營收改善尚未反應模型：前向確認與特徵稽核

- generated_at: `2026-07-14 14:45:55 Asia/Taipei`
- model_id: `revenue_unreacted_range`
- artifact_version: `forward_confirmation_v1_20260713`
- 狀態：`research_only`，不可直接升格或進入 PDF 操作列。
- 來源母體：`absolute_or_two_month_yoy_ge15` 的 source-first、同股不重疊 episodes。
- 突破事件：收盤由未高於前高，首次跨到高於前 N 日最高收盤價。
- 前向選取：每條確認規則只採第一次符合事件；後來成功不得回頭取代較早已確認的失敗。
- 特徵對照：成功組使用 source 標記的真正發動日，失敗組使用 source 第一個成熟失敗突破；僅供找差異，不是可交易勝率。
- 嚴格成功：觸發收盤後 D+15 內達 +20%，且至 D+20 每日收盤均未跌回 +20% 以下。
- 操作報酬：確認日收盤成立，下一交易日開盤進場，確認日起算 D+20 收盤固定出場；本稽核尚未定義停損。
- 和局口徑：本次尚未核准和局定義；資料不足者獨立列為 right-censored，不得算失敗。
- 盤中高低：僅可用於 K 棒與收盤位置等 advisory 特徵，不得單獨支撐 promotion。
- 高報酬查核：D+20 絕對報酬達 80% 只會觸發 review candidate；primary 保留，未完成底層根因前不得判定為異常。
- 基準第一個突破嚴格成功率：`5.6369%`。
- 財報範圍：本次只使用月營收；EPS、毛利率、營益率、營業利益、業外與淨利均未納入。

## 確認規則矩陣

| rule_id | rule_information_cutoff | confirmed_episode_count | confirmation_coverage_pct | strict_success_rate_pct | mature_failure_rate_pct | avg_confirmation_next_open_to_d20_close_return_pct | median_confirmation_next_open_to_d20_close_return_pct | known_4916_selected_date | known_4916_selected_outcome | known_1303_selected_date | known_1303_selected_outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prev20_next_close_ma60_gt_ma120 | next_trading_day_close | 756 | 48.5237 | 9.4901 | 90.5099 | 5.3604 | 1.1897 | 20251209 | mature_failure |  |  |
| prev20_ma60_gt_ma120 | trigger_date_close | 993 | 63.7356 | 8.0698 | 91.9302 | 5.7075 | 0.7921 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_kdj_bullish_not_extreme | trigger_date_close | 1346 | 86.3928 | 6.7675 | 93.2325 | 3.3676 | -0.9252 | 20251209 | mature_failure |  |  |
| prev20_next_close_kdj_bullish | next_trading_day_close | 1085 | 69.6406 | 6.7269 | 93.2731 | 2.5148 | -0.9641 | 20251209 | mature_failure |  |  |
| prev20_next_close_obv_above_ma20 | next_trading_day_close | 1197 | 76.8293 | 6.6368 | 93.3632 | 2.2608 | -0.9592 | 20251209 | mature_failure |  |  |
| prev20_next_close_continuation | next_trading_day_close | 1249 | 80.1669 | 6.4157 | 93.5843 | 2.1233 | -1.1322 | 20251209 | mature_failure |  |  |
| prev20_next_close_volume_ge1_5 | next_trading_day_close | 1039 | 66.6881 | 6.3808 | 93.6192 | 2.0344 | -1.293 | 20251209 | mature_failure |  |  |
| prev20_next_close_market_bull | next_trading_day_close | 1202 | 77.1502 | 6.2555 | 93.7445 | 2.0518 | -1.12 | 20251209 | mature_failure |  |  |
| prev20_revenue_lag_0_14 | trigger_date_close | 1187 | 76.1874 | 6.1818 | 93.8182 | 3.1593 | -0.779 | 20251223 | mature_failure | 20260527 | strict_success |
| prev20_solid_red_candle | trigger_date_close | 1358 | 87.163 | 6.166 | 93.834 | 2.763 | -1.462 | 20251212 | mature_failure | 20260527 | strict_success |
| prev20_next_close_holds_breakout | next_trading_day_close | 1384 | 88.8318 | 6.091 | 93.909 | 2.4385 | -0.9667 | 20251209 | mature_failure |  |  |
| source_first_close_above_prev20_reference | trigger_date_close | 1460 | 93.7099 | 5.7622 | 94.2378 | 2.645 | -1.4599 | 20251209 | mature_failure | 20260527 | strict_success |
| first_close_cross_prev60 | trigger_date_close | 1062 | 68.1643 | 5.6818 | 94.3182 | 2.3065 | -2.0821 | 20260112 | mature_failure | 20260527 | strict_success |
| prev20_obv_above_ma20 | trigger_date_close | 1422 | 91.2709 | 5.6604 | 94.3396 | 2.6696 | -1.0676 | 20251209 | mature_failure | 20260527 | strict_success |
| first_close_cross_prev20 | trigger_date_close | 1456 | 93.4531 | 5.6369 | 94.3631 | 2.6068 | -1.4493 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_close_above_ma20_ema23 | trigger_date_close | 1453 | 93.2606 | 5.5026 | 94.4974 | 2.6957 | -1.462 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_return20_0_25 | trigger_date_close | 1435 | 92.1053 | 5.4978 | 94.5022 | 2.4362 | -1.492 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_market_bull | trigger_date_close | 1421 | 91.2067 | 5.3144 | 94.6856 | 2.4151 | -1.4934 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_volume_ge1_5 | trigger_date_close | 1327 | 85.1733 | 5.1178 | 94.8822 | 2.1722 | -1.7241 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_next_close_tdcc_high | next_trading_day_close | 366 | 23.4917 | 5.0388 | 94.9612 | 1.8844 | -0.7235 | 20260518 | strict_success |  |  |
| prev20_volume_ge2 | trigger_date_close | 1222 | 78.4339 | 5.0265 | 94.9735 | 1.9882 | -1.7361 | 20251212 | mature_failure |  |  |
| first_close_cross_prev40 | trigger_date_close | 1244 | 79.846 | 4.8458 | 95.1542 | 1.4481 | -1.6018 | 20251212 | mature_failure | 20260527 | strict_success |
| prev20_tdcc_high_thresholds_up | trigger_date_close | 567 | 36.3928 | 4.8309 | 95.1691 | 2.2439 | 0.0 | 20260518 | strict_success | 20260527 | strict_success |
| prev20_tdcc_consecutive_up_ge1 | trigger_date_close | 698 | 44.801 | 4.6555 | 95.3445 | 2.3883 | 0.0 | 20260518 | strict_success | 20260527 | strict_success |
| prev20_revenue_lag_61_90 | trigger_date_close | 342 | 21.9512 | 4.5775 | 95.4225 | 0.2181 | -2.367 |  |  |  |  |
| prev20_revenue_lag_31_60 | trigger_date_close | 601 | 38.5751 | 3.8938 | 96.1062 | 1.8507 | -1.2924 |  |  |  |  |
| prev20_range23_le15 | trigger_date_close | 1216 | 78.0488 | 3.8394 | 96.1606 | 1.6876 | -1.4745 |  |  |  |  |
| prev20_revenue_lag_15_30 | trigger_date_close | 806 | 51.733 | 3.6048 | 96.3952 | 1.9099 | -1.3 | 20251209 | mature_failure |  |  |
| prev20_revenue_lag_91_126 | trigger_date_close | 171 | 10.9756 | 3.1496 | 96.8504 | -0.0659 | -2.2059 |  |  |  |  |

## 成功與失敗事件的特徵差異

| feature_id | feature_family | success_observed_count | failure_observed_count | success_hit_rate_pct | failure_hit_rate_pct | success_minus_failure_hit_rate_pct_points | strict_success_share_when_feature_hit_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breakout_prev60 | breakout | 343 | 1292 | 53.3528 | 16.3313 | 37.0215 | 46.4467 |
| breakout_prev40 | breakout | 343 | 1292 | 65.8892 | 28.87 | 37.0192 | 37.7295 |
| ma60_gt_ma120 | technical | 343 | 1292 | 69.3878 | 36.9969 | 32.3909 | 33.2402 |
| position120_high_gt75 | price_position | 333 | 1108 | 66.3664 | 37.6354 | 28.731 | 34.6395 |
| next_close_continuation | close_confirmation | 343 | 1292 | 59.7668 | 42.8793 | 16.8875 | 27.0092 |
| next_close_holds_breakout | close_confirmation | 343 | 1292 | 84.5481 | 73.452 | 11.0961 | 23.406 |
| rsi14_ge60 | technical | 342 | 1191 | 77.7778 | 67.0865 | 10.6913 | 24.9765 |
| revenue_cumulative_ge30 | monthly_revenue | 343 | 1292 | 39.3586 | 33.3591 | 5.9995 | 23.8516 |
| solid_red_candle | candle | 343 | 1292 | 68.5131 | 62.6935 | 5.8196 | 22.488 |
| obv_above_ma20 | technical | 343 | 1291 | 95.3353 | 89.8528 | 5.4825 | 21.9906 |
| revenue_latest_ge50 | monthly_revenue | 343 | 1292 | 27.6968 | 23.6068 | 4.09 | 23.75 |
| revenue_lag_31_60 | revenue_freshness | 343 | 1292 | 13.9942 | 10.5263 | 3.4679 | 26.087 |
| revenue_lag_61_90 | revenue_freshness | 343 | 1292 | 4.6647 | 1.548 | 3.1167 | 44.4444 |
| revenue_two_month_yoy_ge15 | monthly_revenue | 343 | 1285 | 49.2711 | 46.3813 | 2.8898 | 22.0915 |
| market_correction_or_high_risk | market_regime_risk | 343 | 1292 | 9.621 | 6.8885 | 2.7325 | 27.0492 |
| kdj_bullish_not_extreme | technical | 343 | 1211 | 69.0962 | 66.3914 | 2.7048 | 22.7666 |
| volume_ge1_5 | volume | 343 | 1292 | 67.3469 | 65.0155 | 2.3314 | 21.5686 |
| revenue_lag_91_126 | revenue_freshness | 343 | 1292 | 2.0408 | 0.2322 | 1.8086 | 70.0 |
| revenue_lag_15_30 | revenue_freshness | 343 | 1292 | 20.4082 | 19.4272 | 0.981 | 21.8069 |
| macd_hist_gt0 | technical | 326 | 979 | 95.092 | 95.097 | -0.005 | 24.9799 |
| close_above_ma20_ema23 | technical | 343 | 1292 | 99.1254 | 99.226 | -0.1006 | 20.9618 |
| volume_ge2 | volume | 343 | 1292 | 50.1458 | 51.4706 | -1.3248 | 20.5496 |
| kdj_j_ge100 | technical_risk | 343 | 1211 | 28.2799 | 30.4707 | -2.1908 | 20.8155 |
| market_bull | market_regime | 343 | 1292 | 90.379 | 93.1115 | -2.7325 | 20.4891 |
| revenue_lag_0_14 | revenue_freshness | 343 | 1292 | 58.8921 | 68.2663 | -9.3742 | 18.6347 |
| rsi14_40_70 | technical | 342 | 1191 | 67.5439 | 79.2611 | -11.7172 | 19.6596 |
| return20_0_25 | price_momentum | 343 | 1292 | 85.1312 | 97.0588 | -11.9276 | 18.8875 |
| position120_mid_40_75 | price_position | 333 | 1108 | 24.024 | 36.3718 | -12.3478 | 16.5631 |
| tdcc_high_thresholds_up | tdcc | 95 | 193 | 29.4737 | 45.0777 | -15.604 | 24.3478 |
| position120_low_le40 | price_position | 333 | 1108 | 9.6096 | 25.9928 | -16.3832 | 10.0 |
| tdcc_consecutive_up_ge1 | tdcc | 95 | 193 | 38.9474 | 55.4404 | -16.493 | 25.6944 |
| range23_le15 | price_shape | 343 | 1292 | 45.7726 | 75.4644 | -29.6918 | 13.8693 |

## 指定案例

| stock_id | stock_name | contrast_group | trigger_date | outcome_status | next_day_close_gt_trigger_close | volume_ratio_prev20 | ma60_gt_ma120 | obv_above_ma20 | kdj_bullish_not_extreme | tdcc_high_thresholds_up | market_regime | revenue_lag_trading_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1303 | 南亞 | strict_success_launch_event | 20260527 | strict_success | False | 1.677 | True | True | False | True | strong_bull | 7.0 |
| 4916 | 事欣科 | first_mature_failure_event | 20251209 | mature_failure | True | 1.9351 | True | True | True | False | mild_bull | 16.0 |
| 4916 | 事欣科 | strict_success_launch_event | 20260518 | strict_success | True | 0.9934 | True | True | True | True | strong_bull | 0.0 |

## 高報酬底層路徑查核候選

| stock_id | stock_name | entry_date | fixed_exit_date | fixed_d20_return_pct | path_trading_row_count | max_abs_raw_close_return_1d_pct | max_abs_analysis_open_gap_pct | price_resolution_ids_in_path | bottom_level_price_path_result | review_disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| 6515 | 穎崴 | 20250828 | 20251001 | 85.3061 | 20 | 10.0 | 4.0 |  | no_single_day_scale_break_observed | unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly |
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
