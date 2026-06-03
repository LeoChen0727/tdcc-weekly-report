# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-06-03 17:51:36 UTC`
- main_price_date: `20260603`
- purpose: Force daily reports to include short-term specialty sections that are not part of the fixed six candidate categories.
- market_abnormal_status_path: `output/latest/market_abnormal_status_latest.csv`

## Usage Contract
- This packet is mandatory for daily stock candidate analysis.
- `回檔後短線轉強` is one of the six fixed categories; it is not the whole short-term specialty layer.
- The daily PDF must include a standalone short-term specialty section if this packet exists.
- The section must include D+5 and D+10 tables separately.
- These are research/reporting signals only. Do not change core TDCC, ABM, or daily candidate model weights.
- If data is missing, write `資料不足 / 僅能觀察`; do not silently omit the section.

## TDCC Overheated Short-Term Edge

- section_required_in_daily_pdf: `True`
- section_type: `short_term_specialty_not_six_category`
- model_effect_allowed: `False`
- allowed_use: `reporting_priority_only`
- rule: `D+5` and `D+10` must be shown as separate tables.
- rule: close-to-close metrics and next-open metrics must not be mixed.

### D+5 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 25 | 76.0 | 3.884922722173117 | 76.0 | 3.6060465705459475 | insufficient_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 15 | 66.66666666666666 | -0.5549434999963627 | 66.66666666666666 | -0.5136114568738805 | insufficient_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 2 | 0.0 | -9.208780404858407 | 0.0 | -17.915295523445234 | insufficient_sample |

### D+10 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 15 | 73.33333333333333 | 0.9703147518259791 | 100.0 | 1.8238835862697804 | insufficient_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 25 | 84.0 | 11.747320890165929 | 100.0 | 15.249514532074715 | insufficient_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 2 | 0.0 |  |  |  | insufficient_sample |

### Current TDCC Edge Candidates
| stock_id | stock_name | theme | tdcc_price_phase |
| --- | --- | --- | --- |
| 2375 | 凱美 | passive components | overheated_after_tdcc |
| 2495 | 普安 | other | overheated_after_tdcc |
| 2484 | 希華 | other | overheated_after_tdcc |
| 6127 | 九豪 | other | overheated_after_tdcc |
| 6284 | 佳邦 | other | overheated_after_tdcc |
| 2312 | 金寶 | other | overheated_after_tdcc |
| 6175 | 立敦 | other | overheated_after_tdcc |
| 2369 | 菱生 | other | overheated_after_tdcc |
| 6706 | 惠特 | other | price_leading_tdcc |
| 4906 | 正文 | networking | overheated_after_tdcc |
| 6265 | 方土昶 | other | price_leading_tdcc |
| 2344 | 華邦電 | memory | overheated_after_tdcc |
| 8028 | 昇陽半導體 | semiconductor equipment/materials | overheated_after_tdcc |
| 2495 | 普安 | other | overheated_after_tdcc |
| 2484 | 希華 | other | overheated_after_tdcc |
| 6127 | 九豪 | other | overheated_after_tdcc |
| 2312 | 金寶 | other | overheated_after_tdcc |
| 2369 | 菱生 | other | overheated_after_tdcc |
| 4906 | 正文 | networking | overheated_after_tdcc |
| 2344 | 華邦電 | memory | overheated_after_tdcc |

## Next-Open +10pct Touch Strict Parameter Research

- legacy_file_prefix: `weekly_surge` is kept only for backward compatibility.
- display_name_zh: `隔日開盤買進後 D+1 至 D+10 / D+20 盤中觸及 +10% 研究`
- forbidden_label_zh: `周線急漲`
- not_weekly_candle: `True`
- section_required_in_daily_pdf: `True`
- section_type: `short_term_specialty_not_six_category`
- entry_basis: `D+1 open`; the signal is only knowable after the signal-day close.
- hit_definition: `D+1 open to D+N high reaches +10%`
- close_exit_definition: `D+1 open to D+N close`; close-exit win rate uses return > 0.
- intraperiod_low_definition: `D+1 open to D+N lowest low`; use this as adverse-move / pain-risk context.
- required_risk_columns: `avg_loss_next_open_to_close_return_pct`, `worst_loss_next_open_to_close_return_pct`, `median_next_open_to_low_return_pct`, `worst_next_open_to_low_return_pct`, `top_stock_concentration_pct`.
- win_rate_definition: keep +10% high touch-rate and close-exit win rate separate.
- model_effect_allowed: `False`
- allowed_use: `research_watchlist_and_reporting_priority_only`
- market_abnormal_status: read `market_abnormal_status_latest.csv/md`; disposition/attention stocks must be flagged as execution-risk. Historical disposition filtering remains `disposition_history_not_backfilled` until daily snapshots or verified history are available.
- rule: show a compact `D+1` to `D+10` summary, plus separate `D+5` and `D+10` tables with loss and intraperiod-low diagnostics.

### D+1 to D+10 Horizon Summary
| horizon | selected | close_mature | close_win_rate | avg_close_ret | median_close_ret | median_low_ret | +10pct_touch_rate | avg_gap | best_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D+1 | 107 | 107 | 48.6 | -0.06 | 0.0 | -1.22 | 1.87 | 0.68 | vol5_avg_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + near_60d_high_10pct |
| D+2 | 129 | 124 | 58.87 | 1.96 | 1.86 | -4.19 | 20.93 | 1.28 | vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+3 | 129 | 117 | 58.12 | 3.4 | 2.02 | -4.46 | 31.01 | 1.28 | vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+4 | 129 | 111 | 63.06 | 4.68 | 3.46 | -4.66 | 38.76 | 1.28 | vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+5 | 123 | 85 | 67.06 | 5.67 | 4.29 | -4.76 | 37.4 | 1.33 | vol5_avg_ge_1_5 + tdcc_high_streak2 + return_10d_20_50 |
| D+6 | 129 | 98 | 69.39 | 8.5 | 4.04 | -5.3 | 48.06 | 1.28 | vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+7 | 135 | 100 | 75.0 | 11.68 | 6.77 | -5.96 | 48.89 | 0.97 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 |
| D+8 | 112 | 77 | 83.12 | 17.01 | 10.85 | -5.39 | 53.57 | 0.98 | vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+9 | 135 | 100 | 86.0 | 19.61 | 13.8 | -5.96 | 60.0 | 0.97 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 |
| D+10 | 112 | 69 | 82.61 | 23.04 | 14.19 | -5.39 | 59.82 | 0.98 | vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 |

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 88 | 63.01 | 6.47 | 4.45 | -5.3 | -14.84 | 47.73 | 9.43 | -5.51 | -25.23 |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 88 | 63.01 | 6.47 | 4.45 | -5.3 | -14.84 | 47.73 | 9.43 | -5.51 | -25.23 |
| day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 74 | 54.84 | 3.06 | 1.35 | -7.46 | -19.31 | 47.3 | 9.29 | -6.21 | -22.19 |
| day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+5 | 92 | 54.55 | 2.64 | 1.54 | -7.46 | -19.31 | 46.74 | 9.01 | -6.41 | -22.19 |
| vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 110 | 62.77 | 5.55 | 4.35 | -5.68 | -14.84 | 46.36 | 9.1 | -5.73 | -25.23 |
| vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 110 | 62.77 | 5.55 | 4.35 | -5.68 | -14.84 | 46.36 | 9.1 | -5.73 | -25.23 |
| vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 129 | 63.81 | 6.14 | 3.08 | -6.3 | -17.33 | 44.96 | 9.44 | -5.3 | -19.33 |
| vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 69 | 63.33 | 5.0 | 2.5 | -6.06 | -14.67 | 44.93 | 8.54 | -5.83 | -14.83 |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 65 | 54.39 | 3.6 | 2.45 | -7.74 | -17.33 | 44.62 | 8.54 | -7.11 | -19.33 |
| vol5_avg_ge_1_5 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 72 | 61.4 | 5.64 | 3.08 | -5.44 | -14.84 | 44.44 | 8.59 | -5.51 | -25.23 |
| day_vol_ge_2 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+5 | 84 | 52.17 | 2.5 | 1.54 | -7.64 | -19.31 | 44.05 | 8.28 | -6.41 | -22.19 |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 66 | 53.45 | 3.38 | 2.0 | -7.81 | -17.33 | 43.94 | 8.36 | -7.22 | -19.33 |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 53 | 80.0 | 14.92 | 13.37 | -6.48 | -9.26 | 71.7 | 17.12 | -8.11 | -19.06 |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 53 | 80.0 | 14.92 | 13.37 | -6.48 | -9.26 | 71.7 | 17.12 | -8.11 | -19.06 |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 65 | 82.35 | 18.68 | 13.66 | -5.74 | -8.22 | 70.77 | 18.05 | -7.9 | -19.33 |
| vol5_avg_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 30 | 90.48 | 19.36 | 18.68 | -5.23 | -8.0 | 70.0 | 19.17 | -8.13 | -14.83 |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 66 | 82.35 | 18.68 | 13.66 | -5.74 | -8.22 | 69.7 | 17.77 | -7.94 | -19.33 |
| day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 57 | 80.0 | 14.92 | 13.37 | -6.48 | -9.26 | 68.42 | 16.99 | -8.3 | -19.06 |
| vol5_avg_ge_2 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 34 | 81.82 | 13.42 | 13.75 | -6.8 | -13.1 | 67.65 | 16.92 | -5.73 | -15.01 |
| vol5_avg_ge_2 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 37 | 81.82 | 13.42 | 13.75 | -6.8 | -13.1 | 67.57 | 16.96 | -5.41 | -15.01 |
| vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 72 | 82.35 | 18.68 | 13.66 | -5.74 | -8.22 | 65.28 | 17.3 | -8.04 | -19.33 |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 88 | 74.42 | 15.44 | 10.98 | -6.03 | -16.74 | 64.77 | 16.92 | -6.19 | -25.23 |
| vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 88 | 74.42 | 15.44 | 10.98 | -6.03 | -16.74 | 64.77 | 16.92 | -6.19 | -25.23 |
| vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 42 | 81.48 | 13.92 | 13.3 | -5.48 | -13.1 | 64.29 | 16.92 | -6.42 | -15.01 |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | market_abnormal_status | market_abnormal_risk_level | execution_risk_note | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_strict_research_watch | 8104 | 錸寶 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3257 | 虹冠電 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2324 | 仁寶 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3131 | 弘塑 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | attention;attention_accumulation | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3321 | 同泰 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3025 | 星通 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2353 | 宏碁 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 8454 | 富邦媒 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2338 | 光罩 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 46.36 | 63.64 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2312 | 金寶 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2484 | 希華 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 4906 | 正文 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 6282 | 康舒 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 1530 | 亞崴 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 1563 | 巧新 | vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 1409 | 新纖 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2369 | 菱生 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | attention_accumulation | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 8473 | 山林水 | vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2356 | 英業達 | vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2305 | 全友 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | attention_accumulation | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2332 | 友訊 | vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 6770 | 力積電 | vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2495 | 普安 | vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + return_10d_20_50 | 42.13 | 62.92 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3380 | 明泰 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 42.06 | 59.22 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3042 | 晶技 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 42.06 | 59.22 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |

## Explosive Volume Up Research

- section_required_in_daily_pdf: `True`
- section_type: `short_term_specialty_not_six_category`
- signal_definition: signal day volume divided by previous 20 trading day average volume, with signal day close-to-close return >= threshold.
- entry_basis: `D+1 open`
- close_win_rate: D+1 open to D+N close return > 0.
- high_hit_rate: after D+1 open entry, highest high during the holding window reaches +10% or +20%; this is performance labeling, not intraday signal entry.
- strict_candle_quality: red candle, real body >= 40% of intraday range, upper shadow <= 25%, close location >= 75%.
- relaxed_candle_quality: red candle, real body >= 25% of intraday range, upper shadow <= 35%, close location >= 65%.
- model_effect_allowed: `False`
- allowed_use: `research_watchlist_and_reporting_priority_only`
- rule: volume alone is not a core buy signal; combine with theme/mainstream status, TDCC phase, market regime, and technical position.
- position_rule: split bottom/low-zone volume reversal, low-to-mid reclaim, near-high attack, and high-zone extension before interpreting win rate.

### D+5 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+5 | 6607 | 6479 | 40.15 | -0.19 | -2.13 | 32.1 | 11.56 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+5 | 4688 | 4615 | 39.33 | -0.3 | -2.24 | 30.92 | 10.94 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+5 | 3404 | 3356 | 38.5 | -0.47 | -2.4 | 30.13 | 10.34 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+5 | 2539 | 2512 | 37.18 | -0.81 | -2.77 | 29.42 | 9.79 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+5 | 1181 | 1174 | 36.8 | -0.8 | -2.71 | 29.3 | 9.71 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+5 | 9650 | 9463 | 40.11 | -0.16 | -1.93 | 28.98 | 10.13 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+5 | 1940 | 1922 | 36.73 | -0.88 | -2.77 | 28.72 | 9.47 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+5 | 6588 | 6485 | 39.06 | -0.34 | -2.12 | 28.17 | 9.71 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+5 | 3337 | 3299 | 37.83 | -0.65 | -2.38 | 28.07 | 9.21 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+5 | 1481 | 1474 | 36.5 | -0.86 | -2.64 | 27.95 | 9.16 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+5 | 4622 | 4556 | 38.74 | -0.41 | -2.18 | 27.92 | 9.28 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+5 | 775 | 770 | 35.32 | -1.44 | -2.81 | 27.66 | 7.92 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+5 | 2525 | 2504 | 37.18 | -0.74 | -2.48 | 27.6 | 9.03 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+5 | 965 | 960 | 35.73 | -1.28 | -2.77 | 27.19 | 8.12 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+5 | 4331 | 4278 | 36.96 | -0.74 | -2.25 | 25.71 | 8.2 | ok |

### D+10 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 6607 | 6296 | 43.12 | 1.49 | -1.9 | 43.01 | 21.51 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 4688 | 4497 | 41.54 | 1.13 | -2.32 | 41.36 | 20.32 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 9650 | 9202 | 42.93 | 1.32 | -1.74 | 40.3 | 19.46 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 3404 | 3282 | 40.37 | 0.66 | -2.55 | 40.07 | 19.13 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 1181 | 1161 | 38.5 | -0.11 | -2.72 | 39.53 | 18.0 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 2539 | 2468 | 38.49 | -0.08 | -2.92 | 39.14 | 17.54 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 6588 | 6328 | 41.29 | 0.95 | -2.12 | 38.94 | 18.44 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 1940 | 1899 | 38.07 | -0.25 | -2.93 | 38.6 | 17.06 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 4622 | 4460 | 40.45 | 0.6 | -2.34 | 38.23 | 17.65 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 3337 | 3239 | 39.21 | 0.08 | -2.61 | 38.13 | 16.95 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 1481 | 1457 | 38.23 | -0.28 | -2.68 | 37.95 | 16.61 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 2525 | 2470 | 38.79 | -0.03 | -2.59 | 37.61 | 16.64 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+10 | 775 | 761 | 34.82 | -1.12 | -3.26 | 36.53 | 15.11 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+10 | 965 | 948 | 35.76 | -0.99 | -3.03 | 36.29 | 14.66 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 14699 | 14060 | 42.52 | 1.08 | -1.57 | 36.17 | 16.83 | ok |

### D+20 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 6607 | 5822 | 43.56 | 3.64 | -2.39 | 53.57 | 32.69 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 4688 | 4211 | 41.91 | 2.8 | -2.74 | 51.67 | 30.54 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 9650 | 8512 | 43.62 | 3.27 | -2.15 | 51.19 | 30.45 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 1181 | 1115 | 39.19 | 1.27 | -3.28 | 50.31 | 27.26 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 3404 | 3094 | 40.72 | 2.14 | -3.21 | 50.29 | 28.83 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 6588 | 5908 | 42.03 | 2.47 | -2.61 | 49.75 | 28.45 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 2539 | 2345 | 39.23 | 1.3 | -3.6 | 49.21 | 27.42 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 4622 | 4197 | 40.93 | 2.01 | -2.93 | 48.77 | 27.16 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 1940 | 1809 | 38.81 | 1.15 | -3.6 | 48.76 | 27.31 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 1481 | 1394 | 38.45 | 0.77 | -3.52 | 48.35 | 25.47 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 3337 | 3078 | 39.54 | 1.36 | -3.33 | 48.34 | 26.54 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 2525 | 2351 | 39.3 | 1.21 | -3.36 | 48.11 | 26.41 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+20 | 775 | 732 | 36.2 | -0.0 | -4.15 | 47.68 | 24.59 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 14699 | 13079 | 43.55 | 2.81 | -1.88 | 47.55 | 27.1 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 9195 | 8306 | 42.25 | 2.23 | -2.31 | 47.0 | 26.05 | ok |

### D+5 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 7 | 3 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 5 | 3 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 3 | 3 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 0 | 3 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 7 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 5 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 3 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 0 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 3 | 1 | 100.0 |
| invalid_intraday_range | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 7 | 1 | 100.0 |

### D+10 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 0 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 3 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 5 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 0 | 3 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 4 | 0 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 4 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 5 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 5 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 5 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 4 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 0 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 0 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 3 | 2 | 100.0 |

### D+20 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 10 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 8 | 3 | 4 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 8 | 0 | 4 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 3 | 7 | 3 | 100.0 |
| relaxed_red_small_upper_shadow | insufficient_position_history | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 6 | 7 | 4 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 4 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 5 | 7 | 1 | 100.0 |
| strict_red_close_near_high | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 7 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 7 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 5 | 7 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 6 | 7 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 6 | 5 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 6 | 3 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 6 | 0 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 8 | 7 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 8 | 5 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 8 | 3 | 1 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 7 | 3 | 100.0 |
| strict_red_close_near_high | low_to_mid_reclaim_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 4 | 100.0 |

### Latest Explosive Volume Events
| date | stock_id | stock_name | industry | market | close | volume_ratio_vs_prev20 | signal_return_1d_pct | signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | next_open_to_d10_max_high_return_pct | next_open_to_d20_max_high_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260528 | 1409 | 新纖 |  | TWSE | 20.75 | 7.6783752454324175 | 9.788359788359791 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 1339 | 昭輝 |  | TWSE | 44.85 | 7.3995980839772235 | 9.926470588235304 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 4545 | 銘鈺 |  | TWSE | 38.65 | 7.150971968971166 | 5.890410958904102 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 6573 | 虹揚-KY |  | TWSE | 14.85 | 6.899625167108819 | 9.999999999999986 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 8110 | 華東 |  | TWSE | 62.0 | 6.5202553836181885 | 2.310231023102305 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 2438 | 翔耀 |  | TWSE | 27.8 | 6.408196364053837 | 9.881422924901194 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 1521 | 大億 |  | TWSE | 26.95 | 6.390365885349802 | 9.999999999999986 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 2241 | 艾姆勒 |  | TWSE | 38.25 | 5.670536174054698 | 5.226960110041268 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 3257 | 虹冠電 |  | TWSE | 65.6 | 5.593307824797785 | 7.364975450081812 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 3652 | 精聯 |  | TWSE | 33.95 | 5.503016718251871 | 3.5060975609756184 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 1563 | 巧新 |  | TWSE | 61.1 | 5.289010947975152 | 9.892086330935257 | invalid_intraday_range | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 1524 | 耿鼎 |  | TWSE | 31.9 | 4.993118363409593 | 9.999999999999986 | invalid_intraday_range | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 8104 | 錸寶 |  | TWSE | 40.95 | 4.9500298696841405 | 9.932885906040267 | not_red_or_failed_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 5520 | 力泰 |  | TPEx | 82.4 | 4.895522388059701 | 0.24330900243310083 | not_red_or_failed_close | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 4728 | 雙美 |  | TPEx | 380.0 | 4.871794871794871 | 0.0 | strict_red_close_near_high | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 6792 | 詠業 |  | TWSE | 72.5 | 4.850226821407352 | 4.166666666666674 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 1810 | 和成 |  | TWSE | 20.0 | 4.687853317810788 | 0.5025125628140836 | not_red_or_failed_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 3027 | 盛達 |  | TWSE | 19.25 | 4.6763459814377795 | 3.7735849056603765 | red_candle_but_not_strong_close | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 8416 | 實威 |  | TPEx | 189.0 | 4.53781512605042 | 9.883720930232553 | invalid_intraday_range | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260528 | 2497 | 怡利電 |  | TWSE | 60.8 | 4.526520671847128 | 5.008635578583753 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |

## PDF Placement
- Place after the three-line candidate split and before or near category interpretation.
- Do not merge this packet into the six-category ranking table.
- If current candidates overlap with core candidate rows, show the overlap as a note, not as a model upgrade.

## Data Quality Notes
- Short-term samples are not full-cycle regime proof yet.
- Current use is suitable for tracking priority and discussion, not formal weight tuning.
- More bear-market and range-market samples are still required.

