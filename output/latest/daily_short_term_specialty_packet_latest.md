# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-05-30 09:59:04 UTC`
- main_price_date: `20260529`
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
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 25 | 76.0 | 5.120141638005707 | 76.0 | 3.6060465705459475 | insufficient_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 15 | 66.66666666666666 | -0.021036025881650745 | 66.66666666666666 | -0.5136114568738805 | insufficient_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 2 | 0.0 | -9.208780404858407 | 0.0 | -17.915295523445234 | insufficient_sample |

### D+10 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 4 | 75.0 | -12.632049918268184 | 100.0 | 1.8238835862697804 | insufficient_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 11 | 81.81818181818183 | 6.825929445216938 | 100.0 | 15.249514532074715 | insufficient_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 0 |  |  |  |  | pending_only |

### Current TDCC Edge Candidates
| stock_id | stock_name | theme | tdcc_price_phase |
| --- | --- | --- | --- |
| 2375 | 凱美 | passive components | overheated_after_tdcc |
| 8358 | 金居 | other | overheated_after_tdcc |
| 3189 | 景碩 | other | overheated_after_tdcc |
| 3042 | 晶技 | other | overheated_after_tdcc |
| 2495 | 普安 | other | overheated_after_tdcc |
| 2484 | 希華 | other | overheated_after_tdcc |
| 2305 | 全友 | other | overheated_after_tdcc |
| 6127 | 九豪 | other | overheated_after_tdcc |
| 8473 | 山林水 | other | overheated_after_tdcc |
| 3532 | 台勝科 | other | overheated_after_tdcc |
| 5864 | 致和證 | other | overheated_after_tdcc |
| 2428 | 興勤 | other | overheated_after_tdcc |
| 6870 | 騰雲 | other | overheated_after_tdcc |
| 6284 | 佳邦 | other | overheated_after_tdcc |
| 2312 | 金寶 | other | overheated_after_tdcc |
| 6175 | 立敦 | other | overheated_after_tdcc |
| 8289 | 泰藝 | other | overheated_after_tdcc |
| 2369 | 菱生 | other | overheated_after_tdcc |
| 8261 | 富鼎 | power discrete/diodes | overheated_after_tdcc |
| 2356 | 英業達 | other | overheated_after_tdcc |

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
| D+1 | 159 | 159 | 47.8 | 0.14 | 0.0 | -1.52 | 0.63 | 0.55 | vol5_avg_ge_1_5 + tdcc_all_up + bb_width_not_extreme + near_60d_high_5pct |
| D+2 | 129 | 124 | 58.87 | 1.96 | 1.86 | -4.19 | 20.93 | 1.28 | vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+3 | 109 | 103 | 58.25 | 3.14 | 1.83 | -4.59 | 34.86 | 1.18 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 |
| D+4 | 129 | 111 | 63.06 | 4.68 | 3.46 | -4.66 | 38.76 | 1.28 | vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+5 | 121 | 83 | 68.67 | 5.83 | 4.98 | -4.76 | 38.02 | 1.35 | vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50 |
| D+6 | 121 | 72 | 69.44 | 6.71 | 6.65 | -4.76 | 45.45 | 1.35 | vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50 |
| D+7 | 121 | 66 | 75.76 | 7.27 | 6.99 | -4.76 | 47.11 | 1.35 | vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50 |
| D+8 | 112 | 77 | 83.12 | 17.01 | 10.85 | -5.39 | 53.57 | 0.98 | vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 |
| D+9 | 135 | 100 | 86.0 | 19.61 | 13.8 | -5.96 | 60.0 | 0.97 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 |
| D+10 | 112 | 69 | 82.61 | 23.04 | 14.19 | -5.39 | 59.82 | 0.98 | vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 |

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 87 | 63.01 | 6.47 | 4.45 | -5.3 | -14.84 | 48.28 | 9.57 | -5.41 | -15.79 |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 87 | 63.01 | 6.47 | 4.45 | -5.3 | -14.84 | 48.28 | 9.57 | -5.41 | -15.79 |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 48 | 63.16 | 5.09 | 3.33 | -6.88 | -17.33 | 47.92 | 9.1 | -5.67 | -19.33 |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 48 | 63.16 | 5.09 | 3.33 | -6.88 | -17.33 | 47.92 | 9.1 | -5.67 | -19.33 |
| day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 74 | 54.84 | 3.06 | 1.35 | -7.46 | -19.31 | 47.3 | 9.29 | -6.21 | -22.19 |
| vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 109 | 62.77 | 5.55 | 4.35 | -5.68 | -14.84 | 46.79 | 9.18 | -5.61 | -16.26 |
| vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 109 | 62.77 | 5.55 | 4.35 | -5.68 | -14.84 | 46.79 | 9.18 | -5.61 | -16.26 |
| day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+5 | 92 | 54.55 | 2.64 | 1.54 | -7.46 | -19.31 | 46.74 | 9.01 | -6.41 | -22.19 |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 43 | 56.25 | 2.74 | 1.53 | -7.58 | -16.35 | 46.51 | 9.0 | -6.21 | -19.88 |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 43 | 56.25 | 2.74 | 1.53 | -7.58 | -16.35 | 46.51 | 9.0 | -6.21 | -19.88 |
| vol5_avg_ge_3 + bb_width_not_extreme + return_10d_20_50 | D+5 | 35 | 48.57 | 1.22 | 0.0 | -8.5 | -23.73 | 45.71 | 7.52 | -8.03 | -33.44 |
| vol5_avg_ge_3 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | D+5 | 35 | 48.57 | 1.22 | 0.0 | -8.5 | -23.73 | 45.71 | 7.52 | -8.03 | -33.44 |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 43 | 86.21 | 19.41 | 16.26 | -8.21 | -12.61 | 74.42 | 17.33 | -7.34 | -19.88 |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 43 | 86.21 | 19.41 | 16.26 | -8.21 | -12.61 | 74.42 | 17.33 | -7.34 | -19.88 |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 48 | 91.43 | 22.34 | 18.68 | -6.4 | -8.22 | 72.92 | 18.58 | -6.99 | -19.33 |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 48 | 91.43 | 22.34 | 18.68 | -6.4 | -8.22 | 72.92 | 18.58 | -6.99 | -19.33 |
| day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 46 | 86.21 | 19.41 | 16.26 | -8.21 | -12.61 | 71.74 | 15.73 | -7.48 | -19.88 |
| day_vol_ge_2 + market_strong_bull + tdcc_all_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 31 | 89.47 | 21.52 | 16.26 | -10.26 | -12.61 | 67.74 | 15.43 | -7.34 | -19.88 |
| day_vol_ge_2 + market_bull + tdcc_all_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 31 | 89.47 | 21.52 | 16.26 | -10.26 | -12.61 | 67.74 | 15.43 | -7.34 | -19.88 |
| vol5_avg_ge_2 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 34 | 81.82 | 13.42 | 13.75 | -6.8 | -13.1 | 67.65 | 16.92 | -5.73 | -15.01 |
| vol5_avg_ge_2 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 37 | 81.82 | 13.42 | 13.75 | -6.8 | -13.1 | 67.57 | 16.96 | -5.41 | -15.01 |
| vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 52 | 91.43 | 22.34 | 18.68 | -6.4 | -8.22 | 67.31 | 16.73 | -6.99 | -19.33 |
| day_vol_ge_2 + tdcc_all_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 33 | 89.47 | 21.52 | 16.26 | -10.26 | -12.61 | 66.67 | 14.91 | -7.34 | -19.88 |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 87 | 74.42 | 15.44 | 10.98 | -6.03 | -16.74 | 65.52 | 16.96 | -6.19 | -21.89 |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | market_abnormal_status | market_abnormal_risk_level | execution_risk_note | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_strict_research_watch | 8104 | 錸寶 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3257 | 虹冠電 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2324 | 仁寶 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3131 | 弘塑 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | attention;attention_accumulation | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3321 | 同泰 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3025 | 星通 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2353 | 宏碁 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 8454 | 富邦媒 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2338 | 光罩 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 46.79 | 64.22 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2312 | 金寶 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 44.96 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 1530 | 亞崴 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 1563 | 巧新 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 1409 | 新纖 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2369 | 菱生 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | attention_accumulation | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 8473 | 山林水 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2356 | 英業達 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2305 | 全友 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | attention_accumulation | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2332 | 友訊 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 6770 | 力積電 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2495 | 普安 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.56 | 63.28 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 2484 | 希華 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 4906 | 正文 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 6282 | 康舒 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 44.96 | 63.12 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3380 | 明泰 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.68 | 60.1 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| A_strict_research_watch | 3042 | 晶技 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 42.56 | 60.1 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |

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
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+5 | 4663 | 4539 | 41.37 | 0.06 | -2.0 | 34.35 | 12.69 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+5 | 3215 | 3144 | 40.43 | -0.08 | -2.18 | 32.92 | 12.05 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+5 | 2298 | 2250 | 39.82 | -0.23 | -2.32 | 32.18 | 11.38 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+5 | 6617 | 6434 | 41.58 | 0.08 | -1.76 | 31.6 | 11.42 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+5 | 1690 | 1663 | 38.54 | -0.6 | -2.69 | 31.57 | 10.82 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+5 | 4424 | 4323 | 40.71 | -0.04 | -1.92 | 30.56 | 10.92 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+5 | 1269 | 1251 | 37.49 | -0.76 | -2.72 | 30.22 | 10.15 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+5 | 2181 | 2143 | 39.24 | -0.43 | -2.25 | 30.19 | 10.13 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+5 | 3060 | 2994 | 40.28 | -0.14 | -2.07 | 30.09 | 10.29 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+5 | 740 | 733 | 35.2 | -1.09 | -2.9 | 29.74 | 9.82 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+5 | 1633 | 1612 | 38.09 | -0.62 | -2.38 | 29.09 | 9.62 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+5 | 9842 | 9565 | 41.19 | 0.13 | -1.51 | 27.97 | 9.85 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+5 | 4030 | 3942 | 39.62 | -0.22 | -1.96 | 27.93 | 9.28 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+5 | 931 | 924 | 35.17 | -1.15 | -2.84 | 27.92 | 9.09 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+5 | 6086 | 5946 | 40.13 | -0.06 | -1.74 | 27.87 | 9.67 | ok |

### D+10 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 4663 | 4359 | 45.38 | 2.38 | -1.28 | 46.32 | 24.04 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 3215 | 3028 | 43.49 | 2.03 | -1.82 | 44.39 | 23.08 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 6617 | 6177 | 44.91 | 2.11 | -1.27 | 43.84 | 22.15 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 2298 | 2178 | 42.79 | 1.64 | -2.0 | 43.39 | 21.81 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 4424 | 4169 | 43.39 | 1.88 | -1.71 | 42.43 | 21.3 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 1690 | 1621 | 40.84 | 0.77 | -2.36 | 42.32 | 20.17 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 3060 | 2901 | 42.71 | 1.52 | -1.84 | 41.64 | 20.2 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 2181 | 2086 | 41.28 | 0.94 | -2.27 | 41.37 | 19.37 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 1269 | 1230 | 39.92 | 0.54 | -2.49 | 41.3 | 19.35 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 740 | 722 | 38.78 | 0.2 | -2.83 | 41.14 | 20.08 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 1633 | 1580 | 40.44 | 0.74 | -2.31 | 40.44 | 18.67 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 9842 | 9211 | 44.35 | 1.84 | -1.23 | 39.93 | 19.62 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+10 | 6086 | 5751 | 42.97 | 1.66 | -1.64 | 39.52 | 19.3 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+10 | 4030 | 3833 | 42.53 | 1.39 | -1.79 | 39.5 | 18.73 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 931 | 909 | 38.39 | 0.03 | -2.83 | 39.38 | 18.15 | ok |

### D+20 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 4663 | 3888 | 45.99 | 5.29 | -1.61 | 57.38 | 36.5 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 6617 | 5490 | 45.92 | 4.82 | -1.46 | 55.46 | 34.59 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 3215 | 2744 | 43.62 | 4.16 | -2.43 | 54.96 | 34.07 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 4424 | 3751 | 43.99 | 3.82 | -2.21 | 53.64 | 32.28 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 2298 | 1992 | 42.27 | 3.31 | -3.02 | 53.31 | 32.03 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 3060 | 2640 | 42.61 | 3.09 | -2.74 | 52.16 | 30.38 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 1690 | 1499 | 40.76 | 2.4 | -3.28 | 52.1 | 30.62 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 9842 | 8234 | 45.96 | 4.24 | -1.25 | 52.08 | 31.22 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 6086 | 5204 | 44.52 | 3.51 | -1.71 | 51.44 | 29.78 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 2181 | 1926 | 40.97 | 2.35 | -3.12 | 51.25 | 29.49 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 740 | 677 | 39.14 | 2.0 | -3.72 | 51.11 | 29.39 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 1269 | 1141 | 39.53 | 2.05 | -3.54 | 50.92 | 29.8 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 1633 | 1462 | 40.15 | 1.99 | -3.3 | 50.55 | 28.73 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+20 | 4030 | 3498 | 42.71 | 2.85 | -2.39 | 50.34 | 28.53 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 931 | 847 | 38.25 | 1.26 | -3.76 | 49.23 | 26.8 | ok |

### D+5 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| red_candle_but_not_strong_close | mid_range_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 5 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 5 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 5 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 1 | 100.0 |

### D+10 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 6 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 6 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 6 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 6 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 7 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 7 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 5 | 2 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 3 | 2 | 100.0 |

### D+20 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 4 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 3 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 5 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 5 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 5 | 5 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 5 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |

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

