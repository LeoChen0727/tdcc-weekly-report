# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-07-01 04:12:41 UTC`
- main_price_date: `20260630`
- purpose: Force daily reports to include short-term research-stat support sections without removing active D+5/D+10 core model rows.
- market_abnormal_status_path: `output/latest/market_abnormal_status_latest.csv`

## Usage Contract
- This packet is mandatory for daily stock candidate analysis.
- `回檔後短線轉強` and `TDCC短線延續模型 D+5/D+10` are separate model concepts.
- The daily PDF must include a standalone short-term research-stat support section if this packet exists.
- The section must include D+5 and D+10 tables separately.
- These research-stat tables are supporting evidence only. Do not override core TDCC, ABM, or daily candidate model weights.
- If data is missing, write `資料不足 / 僅能觀察`; do not silently omit the section.

## TDCC Overheated Short-Term Edge

- section_required_in_daily_pdf: `True`
- section_type: `short_term_research_stat_support`
- model_effect_allowed: `False`
- allowed_use: `reporting_priority_only`
- rule: `D+5` and `D+10` must be shown as separate tables.
- rule: close-to-close metrics and next-open metrics must not be mixed.

### D+5 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 179 | 50.83798882681564 | 1.64444559509577 | 49.162011173184354 | 0.42985627834722473 | ok_initial_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 188 | 50.53191489361703 | 2.796591004789769 | 47.87234042553192 | 1.4409719396981235 | ok_initial_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 49 | 42.857142857142854 | 0.5628671885797184 | 36.734693877551024 | -0.8131236488068305 | ok_initial_sample |

### D+10 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 44 | 59.09090909090909 | 4.99418229629367 | 61.36363636363637 | 3.9440897092054956 | ok_initial_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 166 | 66.86746987951807 | 4.8005692948852134 | 60.24096385542169 | 3.608596094049532 | ok_initial_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 160 | 63.74999999999999 | 3.41868354289977 | 57.49999999999999 | 2.334441017452047 | ok_initial_sample |

### Current TDCC Edge Candidates
| stock_id | stock_name | theme | tdcc_price_phase |
| --- | --- | --- | --- |
| 5328 | 華容 | other | overheated_after_tdcc |
| 8261 | 富鼎 | power discrete/diodes | overheated_after_tdcc |
| 2316 | 楠梓電 | other | overheated_after_tdcc |
| 5011 | 久陽 | other | overheated_after_tdcc |
| 6213 | 聯茂 | other | overheated_after_tdcc |
| 8046 | 南電 | other | overheated_after_tdcc |
| 6672 | 騰輝電子-KY | other | overheated_after_tdcc |
| 1718 | 中纖 | other | overheated_after_tdcc |
| 6270 | 倍微 | other | overheated_after_tdcc |
| 2316 | 楠梓電 | other | overheated_after_tdcc |
| 4716 | 大立 | other | overheated_after_tdcc |
| 5011 | 久陽 | other | overheated_after_tdcc |
| 6243 | 迅杰 | other | overheated_after_tdcc |
| 6213 | 聯茂 | other | overheated_after_tdcc |
| 8046 | 南電 | other | overheated_after_tdcc |
| 4707 | 磐亞 | other | overheated_after_tdcc |
| 6672 | 騰輝電子-KY | other | overheated_after_tdcc |
| 1515 | 力山 | other | overheated_after_tdcc |
| 7795 | 長廣 | other | overheated_after_tdcc |
| 1718 | 中纖 | other | overheated_after_tdcc |

## Next-Open +10pct Touch Strict Parameter Research

- legacy_file_prefix: `weekly_surge` is kept only for backward compatibility.
- display_name_zh: `短線急漲 D+1 到 D+10 / D+20 次日開盤進場 +10% 觸及研究`
- forbidden_label_zh: `週線急漲`
- not_weekly_candle: `True`
- section_required_in_daily_pdf: `True`
- section_type: `short_term_research_stat_support`
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
| D+1 | 118 | 118 | 47.46 | 0.43 | 0.0 | -1.95 | 5.08 | -0.26 | vol5_avg_ge_3 + market_strong_bull + tdcc_high_streak2 |
| D+2 | 127 | 125 | 52.0 | 0.94 | 0.22 | -1.88 | 8.66 | 0.64 | vol5_avg_ge_1_5 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+3 | 140 | 135 | 52.59 | 0.78 | 0.43 | -3.43 | 13.57 | 0.56 | vol5_avg_ge_2 + tdcc_high_streak2 + macd_hist_pos + kd_bullish_not_overheated + near_60d_high_5pct |
| D+4 | 229 | 213 | 56.34 | 1.92 | 0.88 | -4.33 | 31.88 | 1.55 | vol5_avg_ge_2 + tdcc_high_streak2 + rsi_50_75 + return_20d_10_60 |
| D+5 | 127 | 118 | 52.54 | 1.67 | 0.28 | -3.03 | 20.47 | 0.64 | vol5_avg_ge_1_5 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+6 | 210 | 178 | 51.69 | 3.33 | 0.85 | -6.98 | 40.48 | 0.89 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 |
| D+7 | 141 | 122 | 56.56 | 1.78 | 0.59 | -3.98 | 25.53 | 0.91 | day_vol_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+8 | 141 | 120 | 55.83 | 1.54 | 0.89 | -4.23 | 28.37 | 0.91 | day_vol_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+9 | 269 | 209 | 58.85 | 8.67 | 2.86 | -9.74 | 51.3 | 0.63 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 |
| D+10 | 210 | 171 | 57.89 | 5.95 | 3.07 | -7.76 | 50.95 | 0.89 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 |

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 44 | 48.72 | -0.1 | -0.98 | -7.72 | -23.85 | 50.0 | 9.55 | -6.86 | -24.97 |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 36 | 45.45 | -1.71 | -3.04 | -8.0 | -23.85 | 50.0 | 9.55 | -7.38 | -24.97 |
| vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct | D+5 | 31 | 53.33 | 2.59 | 1.12 | -4.79 | -11.55 | 48.39 | 8.54 | -4.78 | -12.55 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_5d_10_30 | D+5 | 31 | 48.28 | 0.85 | -0.98 | -7.0 | -15.96 | 48.39 | 8.54 | -6.74 | -17.34 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+5 | 53 | 48.89 | 1.46 | -0.33 | -6.48 | -23.85 | 47.17 | 9.24 | -6.58 | -24.97 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_10_40 | D+5 | 30 | 51.85 | 2.35 | 1.54 | -5.28 | -15.96 | 46.67 | 9.27 | -6.07 | -17.34 |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+5 | 39 | 37.14 | -1.03 | -1.75 | -6.51 | -23.85 | 46.15 | 7.86 | -7.42 | -24.97 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_5d_10_30 | D+5 | 50 | 42.0 | -0.02 | -1.87 | -5.76 | -15.96 | 46.0 | 7.54 | -5.43 | -17.34 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_5d_5_20 | D+5 | 37 | 45.45 | 1.23 | -1.62 | -6.06 | -15.96 | 45.95 | 9.0 | -6.1 | -17.34 |
| vol5_avg_ge_3 + market_bull + tdcc_high_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 46 | 47.62 | -0.67 | -2.01 | -7.86 | -23.85 | 45.65 | 7.03 | -7.11 | -24.97 |
| vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + return_20d_10_60 | D+5 | 33 | 54.55 | 2.63 | 1.54 | -6.62 | -14.15 | 45.45 | 8.54 | -5.74 | -14.87 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 31 | 45.16 | -0.82 | -3.04 | -7.92 | -23.85 | 45.16 | 6.98 | -7.08 | -24.97 |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+10 | 39 | 55.56 | 4.46 | 1.39 | -8.38 | -18.6 | 58.97 | 11.16 | -8.4 | -25.98 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+10 | 53 | 53.57 | 4.57 | 0.32 | -6.7 | -18.6 | 58.49 | 11.16 | -7.98 | -25.98 |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+10 | 36 | 47.37 | 0.61 | -0.35 | -9.2 | -18.6 | 58.33 | 11.17 | -8.23 | -24.97 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_5d_10_30 | D+10 | 31 | 50.0 | 0.33 | 0.74 | -7.09 | -18.6 | 58.06 | 11.15 | -7.98 | -24.97 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_5d_10_30 | D+10 | 50 | 55.88 | 4.74 | 1.36 | -6.67 | -18.6 | 58.0 | 13.29 | -7.75 | -20.43 |
| vol5_avg_ge_2 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 59 | 53.7 | 5.0 | 2.09 | -8.67 | -18.6 | 57.63 | 14.55 | -8.07 | -24.16 |
| vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + return_20d_10_60 | D+10 | 33 | 43.48 | -1.33 | -2.76 | -9.41 | -18.6 | 57.58 | 10.98 | -7.63 | -20.43 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_20d_10_60 | D+10 | 33 | 50.0 | 1.32 | 0.73 | -8.16 | -18.6 | 57.58 | 11.19 | -7.88 | -25.98 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+10 | 44 | 48.0 | 1.34 | -0.35 | -9.42 | -19.28 | 56.82 | 11.17 | -8.14 | -24.97 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_10_40 | D+10 | 30 | 50.0 | 2.99 | -0.29 | -8.1 | -18.6 | 56.67 | 10.81 | -7.93 | -20.43 |
| vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 76 | 55.07 | 4.48 | 2.51 | -9.48 | -20.55 | 56.58 | 14.15 | -8.65 | -25.79 |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 108 | 52.04 | 5.28 | 1.89 | -9.41 | -20.73 | 56.48 | 12.95 | -9.06 | -25.79 |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | market_abnormal_status | market_abnormal_risk_level | execution_risk_note | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B_strict_research_confirm | 1444 | 力麗 | day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 37.5 | 52.07 | day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2458 | 義隆 | day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 37.5 | 52.07 | day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1710 | 東聯 | day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 37.5 | 52.07 | day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 7402 | 邑錡 | day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 37.5 | 51.97 | day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1617 | 榮星 | vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 38.5 | 51.52 | vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 2634 | 漢翔 | vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + return_5d_5_20; vol5_avg_ge_3 + tdcc_high_streak2 + close_above_ema23 + near_60d_high_5pct; vol5_avg_ge_3 + tdcc_high_streak2 + close_above_ema23 + return_20d_10_60; vol5_avg_ge_3 + tdcc_high_streak2 + macd_hist_pos + return_20d_10_60; vol5_avg_ge_3 + tdcc_high_streak2 + return_20d_10_60; vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + near_60d_high_5pct | 38.76 |  | vol5_avg_ge_3 + tdcc_high_streak2 + close_above_ema23 + return_20d_10_60 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 5347 | 世界 | vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 38.5 |  | vol5_avg_ge_2 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 1815 | 富喬 | day_vol_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_5d_10_30 | 37.7 |  | day_vol_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_5d_10_30 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 1718 | 中纖 | day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_streak2 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 37.04 |  | day_vol_ge_2 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 7795 | 長廣 | day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_streak2 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | 37.04 |  | day_vol_ge_2 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 3189 | 景碩 | vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50 | 36.75 |  | vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 5464 | 霖宏 | vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 36.75 |  | vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | disposition | D_disposition_or_periodic | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 8261 | 富鼎 | vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 36.75 |  | vol5_avg_ge_1_5 + tdcc_high_streak2 + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 4128 | 中天 | vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_20d_10_60; vol5_avg_ge_2 + tdcc_high_up + bb_width_not_extreme + return_20d_10_60; vol5_avg_ge_2 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + return_20d_10_60 | 36.64 |  | vol5_avg_ge_2 + tdcc_high_up + bb_width_not_extreme + return_20d_10_60 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 4532 | 瑞智 | vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + return_5d_5_20; vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + near_60d_high_5pct | 36.63 |  | vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + return_5d_5_20 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 5011 | 久陽 | day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 36.49 |  | day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 6658 | 聯策 | day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50 | 36.39 |  | day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 4716 | 大立 | day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 36.05 |  | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 5371 | 中光電 | day_vol_ge_2 + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50 | 35.98 |  | day_vol_ge_2 + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 6156 | 松上 | day_vol_ge_2 + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + return_10d_20_50 | 35.98 |  | day_vol_ge_2 + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 3257 | 虹冠電 | vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 35.34 |  | vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 6226 | 光鼎 | vol5_avg_ge_3 + tdcc_high_streak2 + close_above_ema23 + near_60d_high_5pct | 35.29 |  | vol5_avg_ge_3 + tdcc_high_streak2 + close_above_ema23 + near_60d_high_5pct | disposition | D_disposition_or_periodic | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 4924 | 欣厚-KY | vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_20d_10_60 | 35.21 |  | vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_20d_10_60 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 8054 | 安國 | vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_20d_10_60 | 35.21 |  | vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_20d_10_60 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| C_strict_short_term_watch | 1515 | 力山 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 35.19 |  | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |

## Explosive Volume Up Research

- section_required_in_daily_pdf: `True`
- section_type: `short_term_research_stat_support`
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
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+5 | 7322 | 7194 | 40.13 | -0.17 | -2.2 | 32.9 | 12.08 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+5 | 5174 | 5082 | 39.33 | -0.22 | -2.28 | 31.66 | 11.47 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+5 | 3734 | 3667 | 38.45 | -0.34 | -2.5 | 30.87 | 10.99 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+5 | 1271 | 1249 | 37.31 | -0.49 | -2.7 | 30.66 | 10.65 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+5 | 2768 | 2716 | 37.3 | -0.65 | -2.82 | 30.27 | 10.46 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+5 | 833 | 820 | 36.34 | -0.89 | -2.72 | 29.88 | 9.39 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+5 | 10673 | 10499 | 40.09 | -0.16 | -2.0 | 29.63 | 10.54 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+5 | 2107 | 2070 | 36.81 | -0.72 | -2.83 | 29.52 | 9.95 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+5 | 1603 | 1574 | 37.04 | -0.6 | -2.6 | 29.29 | 9.85 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+5 | 3649 | 3585 | 37.91 | -0.53 | -2.47 | 28.79 | 9.76 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+5 | 7256 | 7135 | 38.99 | -0.29 | -2.18 | 28.73 | 10.11 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+5 | 1039 | 1022 | 36.5 | -0.86 | -2.66 | 28.67 | 9.2 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+5 | 5071 | 4985 | 38.58 | -0.33 | -2.26 | 28.49 | 9.85 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+5 | 2755 | 2709 | 37.5 | -0.57 | -2.49 | 28.46 | 9.41 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_3pct | D+5 | 2016 | 1983 | 36.26 | -0.76 | -2.6 | 26.68 | 8.88 | ok |

### D+10 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 7322 | 6916 | 43.36 | 1.64 | -1.84 | 44.19 | 22.34 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 5174 | 4899 | 41.89 | 1.31 | -2.22 | 42.34 | 21.19 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 10673 | 10123 | 43.15 | 1.38 | -1.72 | 41.21 | 20.07 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 3734 | 3540 | 40.73 | 0.92 | -2.46 | 40.9 | 20.03 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 1271 | 1208 | 38.91 | 0.19 | -2.7 | 39.98 | 18.87 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 2768 | 2629 | 38.99 | 0.24 | -2.78 | 39.86 | 18.49 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 7256 | 6891 | 41.65 | 1.07 | -2.06 | 39.7 | 19.16 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 2107 | 2001 | 38.18 | -0.01 | -2.85 | 38.93 | 17.54 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 5071 | 4813 | 40.83 | 0.78 | -2.27 | 38.89 | 18.45 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 3649 | 3461 | 39.76 | 0.37 | -2.5 | 38.75 | 17.83 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 1603 | 1518 | 38.67 | 0.0 | -2.64 | 38.34 | 17.39 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 2755 | 2612 | 39.17 | 0.23 | -2.52 | 38.06 | 17.15 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+10 | 833 | 788 | 35.66 | -0.67 | -2.96 | 37.69 | 16.24 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 16187 | 15443 | 42.86 | 1.15 | -1.53 | 37.14 | 17.51 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+10 | 1039 | 980 | 36.53 | -0.6 | -2.9 | 37.04 | 15.61 | ok |

### D+20 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 7322 | 6510 | 44.96 | 4.52 | -1.82 | 55.81 | 34.35 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 5174 | 4615 | 43.23 | 3.72 | -2.36 | 53.56 | 32.24 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 10673 | 9550 | 45.17 | 4.07 | -1.58 | 53.31 | 32.12 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 3734 | 3333 | 41.94 | 3.09 | -2.75 | 51.88 | 30.24 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 7256 | 6510 | 43.5 | 3.28 | -2.15 | 51.61 | 30.14 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 1271 | 1136 | 40.05 | 1.76 | -2.96 | 50.97 | 28.17 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 2768 | 2474 | 40.3 | 2.27 | -3.12 | 50.53 | 28.78 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 5071 | 4544 | 42.3 | 2.79 | -2.55 | 50.33 | 28.57 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 2107 | 1882 | 39.8 | 2.06 | -3.12 | 49.84 | 28.32 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 16187 | 14587 | 45.13 | 3.6 | -1.39 | 49.76 | 28.89 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 3649 | 3267 | 40.71 | 2.21 | -2.93 | 49.59 | 28.04 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 2755 | 2466 | 40.39 | 2.03 | -2.95 | 49.19 | 27.58 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 1603 | 1438 | 39.36 | 1.24 | -3.17 | 49.03 | 26.43 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 10119 | 9100 | 43.73 | 3.03 | -1.86 | 48.93 | 27.82 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+20 | 833 | 733 | 36.97 | 0.52 | -3.8 | 48.7 | 25.51 | ok |

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
| invalid_intraday_range | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 7 | 1 | 100.0 |
| invalid_intraday_range | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 5 | 1 | 100.0 |
| invalid_intraday_range | high_zone_extension_or_chase | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 8 | 3 | 1 | 100.0 |

### D+10 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 0 | 1 | 100.0 |
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

### D+20 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 5 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 3 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 4 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 5 | 2 | 100.0 |

### Latest Explosive Volume Events
| date | stock_id | stock_name | industry | market | close | volume_ratio_vs_prev20 | signal_return_1d_pct | signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | next_open_to_d10_max_high_return_pct | next_open_to_d20_max_high_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260629 | 1435 | 中福 |  | TWSE | 24.9 | 9.765470372900355 | 9.933774834437092 | strict_red_close_near_high | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 9960 | 邁達康 |  | TPEx | 33.9 | 9.486723394708587 | 5.937499999999996 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 6712 | 長聖 |  | TPEx | 158.0 | 7.44521863928121 | 7.118644067796609 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 8183 | 精星 |  | TPEx | 34.1 | 7.4306816134798455 | 5.572755417956676 | red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 8107 | 大億金茂 |  | TPEx | 12.75 | 6.823469204683487 | 3.238866396761142 | not_red_or_failed_close | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 4707 | 磐亞 |  | TPEx | 30.3 | 6.526712846259616 | 9.981851179673317 | strict_red_close_near_high | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 1445 | 大宇 |  | TWSE | 11.8 | 6.451189430454217 | 9.259259259259256 | strict_red_close_near_high | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 2012 | 春雨 |  | TWSE | 16.65 | 6.115520457000449 | 8.823529411764696 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 6226 | 光鼎 |  | TWSE | 20.05 | 6.0518357056636845 | 9.86301369863014 | strict_red_close_near_high | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 6928 | 攸泰科技 |  | TWSE | 51.7 | 5.600605779621571 | 7.708333333333339 | strict_red_close_near_high | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 2506 | 太設 |  | TWSE | 8.79 | 5.46784213581402 | 0.1138952164009055 | not_red_or_failed_close | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 4716 | 大立 |  | TPEx | 23.9 | 5.43250834462022 | 1.2711864406779627 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 3717 | 聯嘉投控 |  | TWSE | 25.95 | 5.271459011387702 | 9.957627118644051 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 2415 | 錩新 |  | TWSE | 37.45 | 5.181005731766646 | 8.393632416787277 | strict_red_close_near_high | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 4532 | 瑞智 |  | TWSE | 26.15 | 5.00527659829278 | 9.873949579831919 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 2634 | 漢翔 |  | TWSE | 52.0 | 4.773746466465258 | 5.691056910569103 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 3349 | 寶德 |  | TPEx | 18.05 | 4.582823976178214 | 0.0 | not_red_or_failed_close | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 2630 | 亞航 |  | TWSE | 44.45 | 4.533519806564371 | 6.4670658682634885 | strict_red_close_near_high | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 4924 | 欣厚-KY |  | TPEx | 13.9 | 4.493247348782272 | 7.3359073359073435 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260629 | 3227 | 原相 |  | TPEx | 233.5 | 4.338109891389843 | 9.882352941176475 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |

## PDF Placement
- Place after the three-line candidate split and before or near category interpretation.
- Do not use this packet to replace the active core model ranking table.
- If current candidates overlap with core candidate rows, show the overlap as supporting evidence, not as a second buy/sell gate.

## Data Quality Notes
- Short-term samples are not full-cycle regime proof yet.
- Current use is suitable for tracking priority and discussion, not formal weight tuning.
- More bear-market and range-market samples are still required.

