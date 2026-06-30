# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-06-30 04:06:25 UTC`
- main_price_date: `20260629`
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
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 55 | 61.81818181818181 | 2.007138920383993 | 52.72727272727272 | 0.981665075610172 | ok_initial_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 29 | 68.96551724137932 | 0.6167228677293995 | 51.724137931034484 | -0.5799540456505534 | insufficient_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 3 | 33.33333333333333 | -8.735295810155648 | 0.0 | -15.000941483141283 | insufficient_sample |

### D+10 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 44 | 65.9090909090909 | 4.035247570490869 | 75.0 | 6.421625534305545 | ok_initial_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 25 | 64.0 | 0.5853341495359701 | 68.0 | 2.9247386554659225 | insufficient_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 2 | 0.0 | -12.54181939956227 | 0.0 | -20.139627605676154 | insufficient_sample |

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
| 5011 | 久陽 | other | overheated_after_tdcc |
| 6213 | 聯茂 | other | overheated_after_tdcc |
| 8046 | 南電 | other | overheated_after_tdcc |
| 6672 | 騰輝電子-KY | other | overheated_after_tdcc |
| 1515 | 力山 | other | overheated_after_tdcc |
| 7795 | 長廣 | other | overheated_after_tdcc |
| 1718 | 中纖 | other | overheated_after_tdcc |
| 6270 | 倍微 | other | overheated_after_tdcc |

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
| D+1 | 127 | 127 | 49.61 | 0.46 | 0.0 | -1.47 | 0.79 | 0.5 | vol5_avg_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + near_60d_high_10pct |
| D+2 | 120 | 114 | 57.02 | 0.73 | 0.43 | -1.71 | 7.5 | 0.36 | vol5_avg_ge_2 + tdcc_high_streak2 + rsi_50_75 + near_60d_high_5pct |
| D+3 | 120 | 109 | 57.8 | 1.23 | 0.76 | -2.15 | 13.33 | 0.36 | vol5_avg_ge_2 + tdcc_high_streak2 + rsi_50_75 + near_60d_high_5pct |
| D+4 | 177 | 145 | 60.69 | 2.27 | 1.74 | -3.5 | 29.38 | 0.37 | vol5_avg_ge_2 + tdcc_high_streak2 + rsi_50_75 + return_20d_10_60 |
| D+5 | 122 | 81 | 58.02 | 3.32 | 1.54 | -4.5 | 31.97 | 0.7 | vol5_avg_ge_3 + tdcc_high_up + rsi_50_75 + return_20d_10_60 |
| D+6 | 174 | 157 | 54.78 | 4.03 | 2.56 | -6.71 | 47.13 | 1.02 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 |
| D+7 | 120 | 104 | 55.77 | 1.6 | 0.57 | -3.34 | 25.83 | 0.66 | day_vol_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+8 | 234 | 194 | 59.28 | 7.62 | 3.3 | -7.76 | 49.15 | 0.56 | vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 |
| D+9 | 217 | 185 | 60.0 | 10.01 | 3.83 | -8.29 | 54.38 | 0.6 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 |
| D+10 | 160 | 102 | 60.78 | 9.64 | 5.63 | -7.14 | 50.62 | 0.8 | vol5_avg_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 |

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+5 | 34 | 63.64 | 6.49 | 4.67 | -5.01 | -12.99 | 55.88 | 11.06 | -4.67 | -17.16 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_20d_10_60 | D+5 | 35 | 65.22 | 5.58 | 4.8 | -6.98 | -21.61 | 51.43 | 10.98 | -4.78 | -24.5 |
| vol5_avg_ge_3 + tdcc_high_up + bb_width_not_extreme + return_10d_10_40 | D+5 | 38 | 61.54 | 5.28 | 3.61 | -5.17 | -12.99 | 50.0 | 10.32 | -5.19 | -17.16 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_10pct | D+5 | 30 | 63.64 | 4.68 | 3.61 | -2.83 | -5.21 | 50.0 | 9.47 | -3.85 | -11.98 |
| vol5_avg_ge_3 + tdcc_high_up + bb_width_not_extreme + return_20d_10_60 | D+5 | 44 | 66.67 | 5.12 | 4.8 | -6.92 | -21.61 | 45.45 | 9.4 | -4.76 | -24.5 |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 139 | 53.85 | 3.73 | 1.84 | -6.93 | -15.09 | 43.88 | 8.1 | -6.19 | -19.68 |
| vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 139 | 53.85 | 3.73 | 1.84 | -6.93 | -15.09 | 43.88 | 8.1 | -6.19 | -19.68 |
| day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 128 | 50.89 | 2.21 | 0.56 | -8.16 | -19.31 | 43.75 | 7.96 | -6.68 | -22.19 |
| day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | D+5 | 39 | 46.15 | 0.04 | -0.98 | -8.64 | -16.35 | 43.59 | 7.74 | -9.18 | -21.61 |
| day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 104 | 52.0 | 2.67 | 1.26 | -7.59 | -18.9 | 43.27 | 7.99 | -7.01 | -21.65 |
| day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 104 | 52.0 | 2.67 | 1.26 | -7.59 | -18.9 | 43.27 | 7.99 | -7.01 | -21.65 |
| vol5_avg_ge_3 + tdcc_high_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 37 | 54.55 | 2.9 | 1.12 | -4.94 | -12.99 | 43.24 | 6.98 | -4.78 | -17.16 |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+10 | 34 | 57.14 | 3.9 | 2.77 | -8.94 | -18.6 | 64.71 | 12.23 | -6.31 | -20.43 |
| day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | D+10 | 39 | 40.54 | 3.14 | -1.88 | -8.87 | -20.55 | 64.1 | 14.55 | -10.61 | -25.79 |
| day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | D+10 | 30 | 37.93 | 2.41 | -4.31 | -8.92 | -18.6 | 63.33 | 15.12 | -12.75 | -21.61 |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 66 | 46.43 | 4.47 | -1.23 | -10.18 | -24.59 | 62.12 | 12.67 | -10.47 | -28.74 |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 69 | 46.43 | 4.47 | -1.23 | -10.18 | -24.59 | 60.87 | 11.9 | -10.0 | -28.74 |
| vol5_avg_ge_3 + tdcc_high_up + bb_width_not_extreme + return_10d_10_40 | D+10 | 38 | 52.94 | 2.85 | 2.47 | -7.92 | -18.6 | 60.53 | 11.17 | -6.31 | -20.43 |
| day_vol_ge_2 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 81 | 54.55 | 6.72 | 3.07 | -9.25 | -18.6 | 60.49 | 15.88 | -8.39 | -21.89 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_20d_10_60 | D+10 | 35 | 53.33 | 1.86 | 1.83 | -10.05 | -18.6 | 60.0 | 11.89 | -6.67 | -24.5 |
| day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 104 | 53.33 | 6.3 | 2.73 | -8.59 | -18.6 | 59.62 | 15.89 | -7.93 | -21.89 |
| day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 104 | 53.33 | 6.3 | 2.73 | -8.59 | -18.6 | 59.62 | 15.89 | -7.93 | -21.89 |
| day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 74 | 44.83 | 3.97 | -1.74 | -10.18 | -24.59 | 59.46 | 11.62 | -9.88 | -28.74 |
| day_vol_ge_2 + market_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+10 | 86 | 55.0 | 7.03 | 3.12 | -9.14 | -18.6 | 59.3 | 15.79 | -8.35 | -21.89 |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | market_abnormal_status | market_abnormal_risk_level | execution_risk_note | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B_strict_research_confirm | 6175 | 立敦 | day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | 43.88 | 59.62 | day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3532 | 台勝科 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 41.38 | 59.09 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6182 | 合晶 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 43.75 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6488 | 環球晶 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 43.75 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | disposition;attention | D_disposition_or_periodic | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2492 | 華新科 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 43.75 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2342 | 茂矽 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 43.75 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 8358 | 金居 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 43.75 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | disposition;attention | D_disposition_or_periodic | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2302 | 麗正 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 43.75 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4958 | 臻鼎-KY | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 40.34 | 57.14 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3484 | 崧騰 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3362 | 先進光 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4976 | 佳凌 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 5481 | 新華 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 9946 | 三發地產 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1905 | 華紙 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2890 | 永豐金 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 39.75 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6156 | 松上 | day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 38.72 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3290 | 東浦 | day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 38.72 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 7610 | 聯友金屬-創 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 38.72 | 53.83 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6613 | 朋億* | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 37.97 | 52.91 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | disposition;attention | D_disposition_or_periodic | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4923 | 力士 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + rsi_50_75 + return_10d_20_50 | 38.1 | 52.61 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3236 | 千如 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + rsi_50_75 + return_10d_20_50 | 38.1 | 52.61 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 7712 | 博盛半導體 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 38.1 | 52.61 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6432 | 今展科 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + rsi_50_75 + return_10d_20_50 | 38.1 | 52.61 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6949 | 沛爾生醫-創 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_bull + macd_hist_pos + return_10d_20_50 | 38.1 | 52.61 | day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |

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
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+5 | 6998 | 6834 | 40.36 | -0.12 | -2.14 | 32.67 | 11.93 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+5 | 4956 | 4853 | 39.56 | -0.18 | -2.24 | 31.53 | 11.31 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+5 | 3580 | 3511 | 38.65 | -0.34 | -2.41 | 30.59 | 10.74 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+5 | 1220 | 1202 | 37.19 | -0.61 | -2.71 | 30.03 | 10.23 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+5 | 2656 | 2611 | 37.5 | -0.66 | -2.77 | 29.95 | 10.23 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+5 | 10243 | 9997 | 40.2 | -0.12 | -1.94 | 29.37 | 10.38 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+5 | 2021 | 1989 | 36.9 | -0.76 | -2.77 | 29.16 | 9.7 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+5 | 799 | 783 | 35.89 | -1.09 | -2.77 | 28.86 | 8.81 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+5 | 1537 | 1510 | 36.95 | -0.67 | -2.6 | 28.74 | 9.6 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+5 | 6972 | 6825 | 39.18 | -0.26 | -2.13 | 28.6 | 9.96 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+5 | 3507 | 3434 | 38.03 | -0.53 | -2.38 | 28.54 | 9.58 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+5 | 4875 | 4772 | 38.7 | -0.33 | -2.23 | 28.23 | 9.62 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+5 | 2648 | 2594 | 37.51 | -0.61 | -2.42 | 28.14 | 9.21 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+5 | 996 | 973 | 36.18 | -0.99 | -2.68 | 28.06 | 8.84 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+5 | 4556 | 4466 | 37.46 | -0.58 | -2.2 | 26.18 | 8.55 | ok |

### D+10 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 6998 | 6647 | 43.09 | 1.57 | -1.94 | 43.66 | 21.96 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 4956 | 4712 | 41.6 | 1.25 | -2.32 | 41.81 | 20.8 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 10243 | 9747 | 43.0 | 1.33 | -1.77 | 40.81 | 19.78 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 3580 | 3407 | 40.5 | 0.85 | -2.51 | 40.42 | 19.61 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 1220 | 1155 | 38.53 | 0.02 | -2.74 | 39.48 | 18.27 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 2656 | 2524 | 38.83 | 0.17 | -2.83 | 39.42 | 18.07 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 6972 | 6648 | 41.5 | 1.02 | -2.11 | 39.31 | 18.83 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 2021 | 1920 | 38.02 | -0.08 | -2.9 | 38.65 | 17.29 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 4875 | 4641 | 40.68 | 0.73 | -2.31 | 38.53 | 18.08 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 3507 | 3330 | 39.67 | 0.3 | -2.51 | 38.41 | 17.45 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 1537 | 1460 | 38.36 | -0.16 | -2.7 | 37.95 | 16.85 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 2648 | 2511 | 39.03 | 0.15 | -2.52 | 37.83 | 16.89 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+10 | 799 | 745 | 35.17 | -0.92 | -3.15 | 37.05 | 15.57 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 15608 | 14872 | 42.81 | 1.12 | -1.55 | 36.81 | 17.26 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+10 | 996 | 934 | 36.3 | -0.78 | -2.94 | 36.62 | 15.1 | ok |

### D+20 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 6998 | 6256 | 45.33 | 4.65 | -1.69 | 55.88 | 34.51 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 4956 | 4473 | 43.57 | 3.83 | -2.23 | 53.48 | 32.37 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 10243 | 9177 | 45.45 | 4.19 | -1.47 | 53.29 | 32.23 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 3580 | 3248 | 42.3 | 3.19 | -2.66 | 52.03 | 30.48 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 6972 | 6306 | 43.8 | 3.38 | -2.07 | 51.51 | 30.24 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 1220 | 1122 | 40.29 | 1.88 | -2.91 | 51.16 | 28.34 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 2656 | 2421 | 40.6 | 2.37 | -2.99 | 50.56 | 28.87 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 4875 | 4426 | 42.63 | 2.9 | -2.43 | 50.36 | 28.74 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 2021 | 1847 | 40.01 | 2.13 | -3.04 | 49.92 | 28.37 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 15608 | 14025 | 45.33 | 3.71 | -1.3 | 49.62 | 28.92 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 3507 | 3193 | 40.96 | 2.29 | -2.87 | 49.55 | 28.12 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 2648 | 2420 | 40.66 | 2.12 | -2.88 | 49.21 | 27.69 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 1537 | 1418 | 39.63 | 1.36 | -3.04 | 49.08 | 26.59 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 9745 | 8819 | 43.92 | 3.12 | -1.79 | 48.78 | 27.85 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+20 | 799 | 725 | 36.97 | 0.57 | -3.76 | 48.69 | 25.52 | ok |

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
| strict_red_close_near_high | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 10 | 0 | 1 | 100.0 |

### D+10 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 3 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 0 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 3 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 5 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 0 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 7 | 1 | 100.0 |
| red_candle_but_not_strong_close | long_base_low_zone_volume_reversal | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | insufficient_position_history | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | insufficient_position_history | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | insufficient_position_history | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | insufficient_position_history | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 8 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | insufficient_position_history | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | insufficient_position_history | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 0 | 1 | 100.0 |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 7 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 10 | 5 | 1 | 100.0 |
| not_red_or_failed_close | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 5 | 1 | 100.0 |
| not_red_or_failed_close | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 3 | 1 | 100.0 |

### D+20 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 10 | 3 | 1 | 100.0 |
| strict_red_close_near_high | near_high_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 10 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 5 | 0 | 7 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 5 | 3 | 5 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 6 | 0 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 5 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 3 | 7 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 5 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+20 | 4 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | insufficient_position_history | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | low_to_mid_reclaim_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 3 | 1 | 100.0 |

### Latest Explosive Volume Events
| date | stock_id | stock_name | industry | market | close | volume_ratio_vs_prev20 | signal_return_1d_pct | signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | next_open_to_d10_max_high_return_pct | next_open_to_d20_max_high_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 7777 | 能率亞洲 |  | TPEx | 43.95 | 9.418214187832621 | 1.6184971098266 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 6517 | 保勝光學 |  | TPEx | 78.6 | 9.272681350357145 | 2.610966057441244 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 3268 | 海德威 |  | TPEx | 21.65 | 9.071741555094759 | 0.23148148148146586 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 8091 | 翔名 |  | TPEx | 260.5 | 8.041658105765789 | 5.040322580645151 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 5489 | 彩富 |  | TPEx | 42.4 | 7.877717196986305 | 6.265664160400997 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 6859 | 伯特光 |  | TPEx | 139.0 | 7.749250041467917 | 9.881422924901194 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 2061 | 風青 |  | TPEx | 48.05 | 7.703609293164285 | 9.954233409610968 | strict_red_close_near_high | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 4513 | 福裕 |  | TPEx | 17.4 | 7.6911785226920575 | 0.5780346820809079 | red_candle_but_not_strong_close | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 4541 | 晟田 |  | TPEx | 51.0 | 7.506509027184496 | 6.25 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 3717 | 聯嘉投控 |  | TWSE | 22.45 | 7.449803887121156 | 3.6951501154734556 | red_candle_but_not_strong_close | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 6488 | 環球晶 |  | TPEx | 1100.0 | 7.085838531795927 | 5.263157894736836 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 8042 | 金山電 | electronic components | TPEx | 195.5 | 6.980623247616644 | 1.558441558441559 | relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme |  |  |
| 20260617 | 5455 | 昇益 |  | TPEx | 27.4 | 6.893265024764693 | 1.8587360594795488 | relaxed_red_small_upper_shadow | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 4707 | 磐亞 |  | TPEx | 22.6 | 6.616680631883005 | 9.97566909975669 | strict_red_close_near_high | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 1225 | 福懋油 |  | TWSE | 33.0 | 6.607447175120999 | 3.125 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 5460 | 同協 |  | TPEx | 16.4 | 6.499062031506322 | 6.148867313915862 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 2425 | 承啟 |  | TWSE | 41.25 | 6.430649449770658 | 4.430379746835444 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 6180 | 橘子 |  | TPEx | 50.4 | 6.351376566915604 | 4.347826086956519 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 1907 | 永豐餘 |  | TWSE | 27.5 | 6.330861069929016 | 2.0408163265306145 | not_red_or_failed_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260617 | 3484 | 崧騰 |  | TPEx | 51.8 | 6.317292261741243 | 8.937960042061 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |

## PDF Placement
- Place after the three-line candidate split and before or near category interpretation.
- Do not use this packet to replace the active core model ranking table.
- If current candidates overlap with core candidate rows, show the overlap as supporting evidence, not as a second buy/sell gate.

## Data Quality Notes
- Short-term samples are not full-cycle regime proof yet.
- Current use is suitable for tracking priority and discussion, not formal weight tuning.
- More bear-market and range-market samples are still required.

