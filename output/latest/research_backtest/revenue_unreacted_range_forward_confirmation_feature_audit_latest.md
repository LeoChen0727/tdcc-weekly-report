# 營收改善尚未反應模型：前向確認與特徵稽核

- generated_at: `2026-07-13 19:20:48 Asia/Taipei`
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
- 基準第一個突破嚴格成功率：`5.6493%`。
- 財報範圍：本次只使用月營收；EPS、毛利率、營益率、營業利益、業外與淨利均未納入。

## 確認規則矩陣

| rule_id | rule_information_cutoff | confirmed_episode_count | confirmation_coverage_pct | strict_success_rate_pct | mature_failure_rate_pct | avg_confirmation_next_open_to_d20_close_return_pct | median_confirmation_next_open_to_d20_close_return_pct | known_4916_selected_date | known_4916_selected_outcome | known_1303_selected_date | known_1303_selected_outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prev20_next_close_ma60_gt_ma120 | next_trading_day_close | 753 | 48.3312 | 9.4901 | 90.5099 | 5.3718 | 1.2259 | 20251209 | mature_failure |  |  |
| prev20_ma60_gt_ma120 | trigger_date_close | 990 | 63.543 | 8.0698 | 91.9302 | 5.7075 | 0.7921 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_kdj_bullish_not_extreme | trigger_date_close | 1344 | 86.2644 | 6.7837 | 93.2163 | 3.3652 | -0.9434 | 20251209 | mature_failure |  |  |
| prev20_next_close_kdj_bullish | next_trading_day_close | 1081 | 69.3838 | 6.754 | 93.246 | 2.5508 | -0.9331 | 20251209 | mature_failure |  |  |
| prev20_next_close_obv_above_ma20 | next_trading_day_close | 1193 | 76.5725 | 6.6667 | 93.3333 | 2.285 | -0.9489 | 20251209 | mature_failure |  |  |
| prev20_next_close_continuation | next_trading_day_close | 1244 | 79.846 | 6.4433 | 93.5567 | 2.134 | -1.1227 | 20251209 | mature_failure |  |  |
| prev20_next_close_volume_ge1_5 | next_trading_day_close | 1037 | 66.5597 | 6.3941 | 93.6059 | 2.0665 | -1.2903 | 20251209 | mature_failure |  |  |
| prev20_next_close_market_bull | next_trading_day_close | 1202 | 77.1502 | 6.2555 | 93.7445 | 2.0518 | -1.12 | 20251209 | mature_failure |  |  |
| prev20_revenue_lag_0_14 | trigger_date_close | 1187 | 76.1874 | 6.1818 | 93.8182 | 3.1593 | -0.779 | 20251223 | mature_failure | 20260527 | strict_success |
| prev20_solid_red_candle | trigger_date_close | 1358 | 87.163 | 6.1807 | 93.8193 | 2.7706 | -1.4504 | 20251212 | mature_failure | 20260527 | strict_success |
| prev20_next_close_holds_breakout | next_trading_day_close | 1382 | 88.7035 | 6.1146 | 93.8854 | 2.4462 | -0.9646 | 20251209 | mature_failure |  |  |
| source_first_close_above_prev20_reference | trigger_date_close | 1457 | 93.5173 | 5.7749 | 94.2251 | 2.6544 | -1.4609 | 20251209 | mature_failure | 20260527 | strict_success |
| first_close_cross_prev60 | trigger_date_close | 1060 | 68.0359 | 5.6995 | 94.3005 | 2.3213 | -2.0833 | 20260112 | mature_failure | 20260527 | strict_success |
| prev20_obv_above_ma20 | trigger_date_close | 1421 | 91.2067 | 5.6775 | 94.3225 | 2.6844 | -1.0676 | 20251209 | mature_failure | 20260527 | strict_success |
| first_close_cross_prev20 | trigger_date_close | 1453 | 93.2606 | 5.6493 | 94.3507 | 2.6162 | -1.4599 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_close_above_ma20_ema23 | trigger_date_close | 1450 | 93.068 | 5.5147 | 94.4853 | 2.7053 | -1.4675 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_return20_0_25 | trigger_date_close | 1432 | 91.9127 | 5.5101 | 94.4899 | 2.4454 | -1.4943 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_market_bull | trigger_date_close | 1421 | 91.2067 | 5.3144 | 94.6856 | 2.4151 | -1.4934 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_volume_ge1_5 | trigger_date_close | 1325 | 85.0449 | 5.1303 | 94.8697 | 2.1627 | -1.7361 | 20251209 | mature_failure | 20260527 | strict_success |
| prev20_next_close_tdcc_high | next_trading_day_close | 361 | 23.1707 | 5.1181 | 94.8819 | 1.9027 | -0.7557 | 20260518 | strict_success |  |  |
| prev20_volume_ge2 | trigger_date_close | 1220 | 78.3055 | 5.0398 | 94.9602 | 1.9926 | -1.7422 | 20251212 | mature_failure |  |  |
| prev20_tdcc_high_thresholds_up | trigger_date_close | 564 | 36.2003 | 4.89 | 95.11 | 2.2652 | 0.0 | 20260518 | strict_success | 20260527 | strict_success |
| first_close_cross_prev40 | trigger_date_close | 1239 | 79.525 | 4.863 | 95.137 | 1.4591 | -1.6043 | 20251212 | mature_failure | 20260527 | strict_success |
| prev20_tdcc_consecutive_up_ge1 | trigger_date_close | 691 | 44.3517 | 4.6992 | 95.3008 | 2.4061 | -0.0705 | 20260518 | strict_success | 20260527 | strict_success |
| prev20_revenue_lag_61_90 | trigger_date_close | 342 | 21.9512 | 4.5936 | 95.4064 | 0.2283 | -2.3656 |  |  |  |  |
| prev20_revenue_lag_31_60 | trigger_date_close | 599 | 38.4467 | 3.9076 | 96.0924 | 1.8824 | -1.2712 |  |  |  |  |
| prev20_range23_le15 | trigger_date_close | 1213 | 77.8562 | 3.8529 | 96.1471 | 1.6902 | -1.4827 |  |  |  |  |
| prev20_revenue_lag_15_30 | trigger_date_close | 799 | 51.2837 | 3.629 | 96.371 | 1.9304 | -1.3257 | 20251209 | mature_failure |  |  |
| prev20_revenue_lag_91_126 | trigger_date_close | 170 | 10.9114 | 3.2258 | 96.7742 | -0.0734 | -2.3746 |  |  |  |  |

## 成功與失敗事件的特徵差異

| feature_id | feature_family | success_observed_count | failure_observed_count | success_hit_rate_pct | failure_hit_rate_pct | success_minus_failure_hit_rate_pct_points | strict_success_share_when_feature_hit_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| breakout_prev60 | breakout | 343 | 1289 | 53.3528 | 16.3693 | 36.9835 | 46.4467 |
| breakout_prev40 | breakout | 343 | 1289 | 65.8892 | 28.9372 | 36.952 | 37.7295 |
| ma60_gt_ma120 | technical | 343 | 1289 | 69.3878 | 37.083 | 32.3048 | 33.2402 |
| position120_high_gt75 | price_position | 333 | 1105 | 66.3664 | 37.7376 | 28.6288 | 34.6395 |
| next_close_continuation | close_confirmation | 343 | 1289 | 59.7668 | 42.7463 | 17.0205 | 27.1164 |
| next_close_holds_breakout | close_confirmation | 343 | 1289 | 84.5481 | 73.3902 | 11.1579 | 23.4628 |
| rsi14_ge60 | technical | 342 | 1188 | 77.7778 | 67.0875 | 10.6903 | 25.0235 |
| revenue_cumulative_ge30 | monthly_revenue | 343 | 1289 | 39.3586 | 33.2816 | 6.077 | 23.9362 |
| solid_red_candle | candle | 343 | 1289 | 68.5131 | 62.8394 | 5.6737 | 22.488 |
| obv_above_ma20 | technical | 343 | 1288 | 95.3353 | 89.8292 | 5.5061 | 22.035 |
| revenue_latest_ge50 | monthly_revenue | 343 | 1289 | 27.6968 | 23.5842 | 4.1126 | 23.8095 |
| revenue_lag_31_60 | revenue_freshness | 343 | 1289 | 13.9942 | 10.4732 | 3.521 | 26.2295 |
| revenue_lag_61_90 | revenue_freshness | 343 | 1289 | 4.6647 | 1.5516 | 3.1131 | 44.4444 |
| market_correction_or_high_risk | market_regime_risk | 343 | 1289 | 9.621 | 6.6718 | 2.9492 | 27.7311 |
| revenue_two_month_yoy_ge15 | monthly_revenue | 343 | 1282 | 49.2711 | 46.4119 | 2.8592 | 22.1204 |
| kdj_bullish_not_extreme | technical | 343 | 1208 | 69.0962 | 66.3907 | 2.7055 | 22.8104 |
| volume_ge1_5 | volume | 343 | 1289 | 67.3469 | 65.0892 | 2.2577 | 21.5888 |
| revenue_lag_91_126 | revenue_freshness | 343 | 1289 | 2.0408 | 0.2327 | 1.8081 | 70.0 |
| revenue_lag_15_30 | revenue_freshness | 343 | 1289 | 20.4082 | 19.3173 | 1.0909 | 21.9436 |
| macd_hist_gt0 | technical | 326 | 976 | 95.092 | 95.082 | 0.01 | 25.0404 |
| close_above_ma20_ema23 | technical | 343 | 1289 | 99.1254 | 99.2242 | -0.0988 | 21.0006 |
| volume_ge2 | volume | 343 | 1289 | 50.1458 | 51.5128 | -1.367 | 20.5742 |
| kdj_j_ge100 | technical_risk | 343 | 1208 | 28.2799 | 30.5464 | -2.2665 | 20.8155 |
| market_bull | market_regime | 343 | 1289 | 90.379 | 93.3282 | -2.9492 | 20.4891 |
| revenue_lag_0_14 | revenue_freshness | 343 | 1289 | 58.8921 | 68.4251 | -9.533 | 18.6347 |
| rsi14_40_70 | technical | 342 | 1188 | 67.5439 | 79.2929 | -11.749 | 19.6931 |
| return20_0_25 | price_momentum | 343 | 1289 | 85.1312 | 97.052 | -11.9208 | 18.9242 |
| position120_mid_40_75 | price_position | 333 | 1105 | 24.024 | 36.3801 | -12.3561 | 16.5975 |
| tdcc_high_thresholds_up | tdcc | 95 | 190 | 29.4737 | 44.7368 | -15.2631 | 24.7788 |
| position120_low_le40 | price_position | 333 | 1105 | 9.6096 | 25.8824 | -16.2728 | 10.0629 |
| tdcc_consecutive_up_ge1 | tdcc | 95 | 190 | 38.9474 | 55.2632 | -16.3158 | 26.0563 |
| range23_le15 | price_shape | 343 | 1289 | 45.7726 | 75.4073 | -29.6347 | 13.9061 |

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
