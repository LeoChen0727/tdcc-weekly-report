# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-07-05 15:08:37 UTC`
- main_price_date: `20260703`
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
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 191 | 51.30890052356021 | 1.8236701833473918 | 49.73821989528796 | 0.6172974538881897 | ok_initial_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 197 | 51.26903553299492 | 2.8429792368234725 | 48.73096446700508 | 1.4409851333669708 | ok_initial_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 49 | 42.857142857142854 | 0.5628671885797184 | 36.734693877551024 | -0.8131236488068305 | ok_initial_sample |

### D+10 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 49 | 59.183673469387756 | 4.537976000443233 | 59.183673469387756 | 3.2944164365352337 | ok_initial_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 188 | 63.829787234042556 | 4.207929161229109 | 56.38297872340425 | 2.9792439014781276 | ok_initial_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 179 | 60.893854748603346 | 2.920240367642197 | 54.7486033519553 | 1.833248890323482 | ok_initial_sample |

### Current TDCC Edge Candidates
| stock_id | stock_name | theme | tdcc_price_phase |
| --- | --- | --- | --- |
| 2483 | 百容 | other | overheated_after_tdcc |
| 4707 | 磐亞 | other | overheated_after_tdcc |
| 6409 | 旭隼 | other | overheated_after_tdcc |
| 2484 | 希華 | other | overheated_after_tdcc |
| 5371 | 中光電 | other | overheated_after_tdcc |
| 2481 | 強茂 | power discrete/diodes | overheated_after_tdcc |
| 6525 | 捷敏-KY | other | overheated_after_tdcc |
| 2645 | 長榮航太 | other | overheated_after_tdcc |
| 2634 | 漢翔 | other | overheated_after_tdcc |
| 1314 | 中石化 | other | overheated_after_tdcc |
| 6753 | 龍德造船 | other | overheated_after_tdcc |
| 1313 | 聯成 | other | overheated_after_tdcc |
| 1310 | 台苯 | other | overheated_after_tdcc |
| 1301 | 台塑 | other | overheated_after_tdcc |
| 2059 | 川湖 | other | price_leading_tdcc |
| 5483 | 中美晶 | other | overheated_after_tdcc |
| 2305 | 全友 | other | overheated_after_tdcc |
| 1714 | 和桐 | other | overheated_after_tdcc |
| 2302 | 麗正 | other | overheated_after_tdcc |
| 2342 | 茂矽 | other | price_leading_tdcc |

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
| D+1 | 106 | 106 | 49.06 | 0.41 | -0.09 | -1.91 | 1.89 | 0.78 | vol5_avg_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_10pct |
| D+2 | 132 | 130 | 52.31 | 1.03 | 0.24 | -1.88 | 8.33 | 0.62 | vol5_avg_ge_1_5 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+3 | 106 | 99 | 53.54 | 1.76 | 0.88 | -2.72 | 19.81 | 0.78 | vol5_avg_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_10pct |
| D+4 | 101 | 96 | 56.25 | 1.55 | 0.93 | -5.21 | 38.61 | 3.22 | vol5_avg_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_20d_10_60 |
| D+5 | 101 | 95 | 54.74 | 2.35 | 0.97 | -5.52 | 43.56 | 3.22 | vol5_avg_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_20d_10_60 |
| D+6 | 101 | 90 | 54.44 | 3.07 | 1.52 | -6.0 | 47.52 | 3.22 | vol5_avg_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_20d_10_60 |
| D+7 | 153 | 132 | 53.79 | 1.34 | 0.47 | -3.73 | 26.8 | 0.89 | day_vol_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct |
| D+8 | 226 | 185 | 54.59 | 4.31 | 2.03 | -7.23 | 47.79 | 0.92 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 |
| D+9 | 107 | 100 | 58.0 | 5.43 | 1.4 | -11.7 | 53.27 | 0.81 | vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 |
| D+10 | 226 | 176 | 58.52 | 5.92 | 3.07 | -7.66 | 52.65 | 0.92 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 |

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 47 | 52.27 | 1.07 | 0.72 | -7.83 | -23.85 | 51.06 | 10.64 | -6.55 | -24.97 |
| vol5_avg_ge_3 + tdcc_high_streak2 + bb_width_not_extreme + return_5d_5_20 | D+5 | 33 | 53.12 | 2.88 | 2.88 | -5.98 | -15.96 | 48.48 | 8.77 | -5.47 | -17.34 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+5 | 56 | 50.94 | 2.26 | 0.41 | -6.63 | -23.85 | 48.21 | 9.62 | -6.33 | -24.97 |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 38 | 47.22 | -1.0 | -2.01 | -8.11 | -23.85 | 47.37 | 7.73 | -7.05 | -24.97 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_5d_5_20 | D+5 | 53 | 48.0 | 3.06 | -1.3 | -6.22 | -15.96 | 47.17 | 9.0 | -5.97 | -17.34 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_5d_10_30 | D+5 | 34 | 48.39 | 0.85 | -0.98 | -7.2 | -15.96 | 47.06 | 7.73 | -6.06 | -17.34 |
| day_vol_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_10d_20_50 | D+5 | 39 | 42.11 | -1.76 | -1.64 | -8.8 | -18.35 | 46.15 | 8.54 | -8.71 | -20.0 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_5d_10_30 | D+5 | 50 | 42.0 | -0.02 | -1.87 | -5.76 | -15.96 | 46.0 | 7.54 | -5.43 | -17.34 |
| vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + return_20d_10_60 | D+5 | 35 | 54.55 | 2.63 | 1.54 | -6.62 | -14.15 | 45.71 | 8.54 | -5.52 | -14.87 |
| vol5_avg_ge_3 + tdcc_all_up + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_10_40 | D+5 | 33 | 50.0 | 2.05 | 0.28 | -5.51 | -15.96 | 45.45 | 8.54 | -5.97 | -17.34 |
| vol5_avg_ge_3 + tdcc_high_up + kd_bullish_not_overheated + bb_width_not_extreme + near_60d_high_5pct | D+5 | 33 | 54.84 | 2.9 | 1.54 | -4.79 | -11.55 | 45.45 | 6.71 | -4.73 | -12.55 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_5d_10_30 | D+5 | 31 | 45.16 | -0.82 | -3.04 | -7.92 | -23.85 | 45.16 | 6.98 | -7.08 | -24.97 |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | median_next_open_to_close_return_pct | avg_loss_next_open_to_close_return_pct | worst_loss_next_open_to_close_return_pct | hit_rate_pct | median_next_open_to_high_return_pct | median_next_open_to_low_return_pct | worst_next_open_to_low_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_5d_10_30 | D+10 | 50 | 55.81 | 3.87 | 1.83 | -7.2 | -18.6 | 64.0 | 14.39 | -7.75 | -20.43 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_20d_10_60 | D+10 | 33 | 55.17 | 2.5 | 1.83 | -7.96 | -18.6 | 63.64 | 14.11 | -7.88 | -25.98 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+10 | 56 | 62.16 | 6.18 | 3.07 | -7.03 | -18.6 | 62.5 | 14.39 | -7.93 | -25.98 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+10 | 47 | 51.72 | 1.97 | 1.83 | -9.7 | -19.28 | 61.7 | 13.99 | -8.05 | -24.97 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_5d_10_30 | D+10 | 31 | 54.17 | 1.64 | 2.15 | -8.74 | -18.6 | 61.29 | 11.19 | -7.98 | -24.97 |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_10d_10_40 | D+10 | 41 | 66.67 | 6.72 | 3.74 | -8.71 | -18.6 | 60.98 | 14.68 | -8.52 | -25.98 |
| vol5_avg_ge_3 + market_bull + tdcc_all_up + bb_width_not_extreme + return_5d_10_30 | D+10 | 38 | 52.17 | 1.53 | 1.83 | -9.57 | -18.6 | 60.53 | 13.29 | -8.23 | -24.97 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_10d_10_40 | D+10 | 48 | 54.55 | 4.05 | 1.68 | -6.67 | -18.6 | 60.42 | 14.93 | -7.75 | -20.43 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_20d_10_60 | D+10 | 54 | 51.28 | 2.28 | 0.32 | -8.7 | -18.6 | 59.26 | 13.39 | -8.28 | -25.98 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_5d_10_30 | D+10 | 51 | 57.14 | 5.61 | 2.8 | -6.42 | -18.6 | 58.82 | 11.19 | -7.88 | -24.97 |
| vol5_avg_ge_3 + tdcc_all_up + bb_width_not_extreme + return_5d_5_20 | D+10 | 53 | 50.0 | 2.46 | -0.29 | -9.66 | -19.28 | 58.49 | 13.99 | -7.54 | -20.8 |
| vol5_avg_ge_3 + market_strong_bull + tdcc_all_up + kd_bullish_not_overheated + return_20d_10_60 | D+10 | 48 | 54.55 | 3.2 | 1.14 | -7.07 | -18.6 | 58.33 | 13.78 | -7.26 | -20.43 |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | market_abnormal_status | market_abnormal_risk_level | execution_risk_note | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B_strict_research_confirm | 4989 | 榮科 | day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | 43.56 | 55.14 | day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2231 | 為升 | day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | 41.13 | 55.14 | day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3349 | 寶德 | day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + bb_width_not_extreme + return_20d_10_60; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 41.13 | 55.14 | day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6435 | 大中 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 39.92 | 54.0 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4924 | 欣厚-KY | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_streak2 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50 | 39.35 | 54.0 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3360 | 尚立 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50 | 38.01 | 54.0 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2634 | 漢翔 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 39.35 | 52.65 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6753 | 龍德造船 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 39.35 | 52.65 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 5371 | 中光電 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 37.97 | 52.65 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6164 | 華興 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | 37.97 | 52.65 | vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1301 | 台塑 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | 40.0 | 52.26 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2484 | 希華 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_bull + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_bull + rsi_50_75 + return_10d_20_50 | 40.0 | 52.26 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1409 | 新纖 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + market_bull + rsi_50_75 + return_10d_20_50 | 40.0 | 52.26 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6525 | 捷敏-KY | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | 40.0 | 52.26 | day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4743 | 合一 | vol5_avg_ge_2 + tdcc_high_up + bb_width_not_extreme + return_20d_10_60; vol5_avg_ge_2 + tdcc_all_up + bb_width_not_extreme + return_20d_10_60; vol5_avg_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_20d_10_60; vol5_avg_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_20d_10_60; day_vol_ge_2 + market_bull + tdcc_high_streak2 + bb_width_not_extreme + return_5d_10_30; day_vol_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_20d_10_60; day_vol_ge_2 + tdcc_high_streak2 + bb_width_not_extreme + return_5d_10_30; day_vol_ge_2 + tdcc_high_streak2 + kd_bullish_not_overheated + bb_width_not_extreme + return_20d_10_60 | 43.56 | 51.25 | vol5_avg_ge_2 + tdcc_high_up + bb_width_not_extreme + return_20d_10_60 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4532 | 瑞智 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 39.35 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1314 | 中石化 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 39.35 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2645 | 長榮航太 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 39.35 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1710 | 東聯 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 39.35 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 4707 | 磐亞 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 37.04 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1313 | 聯成 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 37.04 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 1310 | 台苯 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 37.04 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 6182 | 合晶 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 37.04 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | attention | C_attention | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 2630 | 亞航 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 36.99 | 51.09 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |
| B_strict_research_confirm | 3346 | 麗清 | vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; day_vol_ge_2 + macd_hist_pos + return_10d_20_50 | 36.89 | 50.5 | vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50 | normal | A_normal |  | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct; disposition_history_not_backfilled |

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
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+5 | 7452 | 7289 | 40.02 | -0.15 | -2.23 | 32.9 | 12.16 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+5 | 5257 | 5149 | 39.21 | -0.19 | -2.29 | 31.6 | 11.52 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+5 | 3787 | 3719 | 38.34 | -0.29 | -2.54 | 30.84 | 11.05 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+5 | 1285 | 1268 | 37.15 | -0.5 | -2.75 | 30.6 | 10.73 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+5 | 2797 | 2756 | 37.19 | -0.65 | -2.84 | 30.22 | 10.52 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+5 | 840 | 831 | 36.1 | -0.94 | -2.77 | 29.72 | 9.39 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+5 | 10849 | 10626 | 40.0 | -0.15 | -2.03 | 29.59 | 10.58 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+5 | 2131 | 2099 | 36.68 | -0.73 | -2.86 | 29.49 | 10.0 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+5 | 1623 | 1599 | 36.9 | -0.62 | -2.66 | 29.21 | 9.88 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+5 | 3690 | 3635 | 37.8 | -0.53 | -2.51 | 28.72 | 9.79 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+5 | 7368 | 7224 | 38.91 | -0.28 | -2.19 | 28.65 | 10.12 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+5 | 1050 | 1037 | 36.26 | -0.91 | -2.72 | 28.54 | 9.16 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+5 | 2790 | 2745 | 37.38 | -0.58 | -2.52 | 28.42 | 9.44 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+5 | 5143 | 5052 | 38.52 | -0.29 | -2.28 | 28.42 | 9.88 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_3pct | D+5 | 2037 | 2011 | 36.1 | -0.79 | -2.66 | 26.6 | 8.9 | ok |

### D+10 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 7452 | 7055 | 43.37 | 1.64 | -1.84 | 44.21 | 22.31 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 5257 | 4991 | 41.96 | 1.33 | -2.2 | 42.34 | 21.2 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 10849 | 10317 | 43.15 | 1.38 | -1.72 | 41.28 | 20.05 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 3787 | 3604 | 40.82 | 0.95 | -2.44 | 40.9 | 20.06 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 1285 | 1226 | 39.07 | 0.22 | -2.69 | 40.21 | 19.0 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 2797 | 2672 | 39.11 | 0.27 | -2.77 | 39.9 | 18.56 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 7368 | 7014 | 41.69 | 1.08 | -2.06 | 39.73 | 19.16 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 2131 | 2035 | 38.33 | 0.04 | -2.83 | 39.02 | 17.69 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 5143 | 4903 | 40.89 | 0.81 | -2.24 | 38.94 | 18.48 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 3690 | 3526 | 39.9 | 0.4 | -2.48 | 38.85 | 17.9 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 1623 | 1546 | 38.81 | 0.03 | -2.64 | 38.62 | 17.53 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 2790 | 2666 | 39.38 | 0.3 | -2.51 | 38.26 | 17.29 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+10 | 840 | 799 | 35.67 | -0.65 | -2.95 | 37.92 | 16.4 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 16432 | 15724 | 42.86 | 1.14 | -1.54 | 37.23 | 17.51 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_5pct | D+10 | 1050 | 998 | 36.37 | -0.63 | -2.93 | 37.17 | 15.73 | ok |

### D+20 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 7452 | 6646 | 44.58 | 4.4 | -1.98 | 55.37 | 34.19 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 5257 | 4709 | 42.9 | 3.62 | -2.45 | 53.17 | 32.15 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 10849 | 9746 | 44.82 | 3.95 | -1.72 | 52.87 | 31.88 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 3787 | 3404 | 41.6 | 2.98 | -2.9 | 51.5 | 30.23 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 7368 | 6645 | 43.21 | 3.17 | -2.25 | 51.18 | 29.93 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 1285 | 1153 | 40.07 | 1.81 | -2.99 | 50.82 | 28.19 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 2797 | 2522 | 40.01 | 2.2 | -3.28 | 50.12 | 28.67 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 5143 | 4638 | 42.0 | 2.68 | -2.67 | 49.96 | 28.46 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 2131 | 1918 | 39.62 | 2.0 | -3.28 | 49.53 | 28.26 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 16432 | 14866 | 44.84 | 3.49 | -1.47 | 49.43 | 28.7 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 3690 | 3328 | 40.5 | 2.14 | -2.99 | 49.25 | 27.88 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 2790 | 2509 | 40.26 | 1.98 | -2.99 | 48.94 | 27.46 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 1623 | 1458 | 39.37 | 1.27 | -3.23 | 48.9 | 26.41 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 10253 | 9276 | 43.4 | 2.92 | -2.0 | 48.57 | 27.67 | ok |
| volume_ratio_prev20_ge_10x_signal_return_ge_7pct | D+20 | 840 | 743 | 36.74 | 0.45 | -3.84 | 48.45 | 25.44 | ok |

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
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 5 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | long_base_low_zone_volume_reversal | pcb_ccl_theme | structural_theme_bucket | core_mainstream_theme | pcb_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | consumer_electronics_theme | structural_theme_bucket | core_mainstream_theme | consumer_electronics_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 3 | 100.0 |
| red_candle_but_not_strong_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 4 | 100.0 |
| relaxed_red_small_upper_shadow | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 5 | 2 | 100.0 |

### Latest Explosive Volume Events
| date | stock_id | stock_name | industry | market | close | volume_ratio_vs_prev20 | signal_return_1d_pct | signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | next_open_to_d10_max_high_return_pct | next_open_to_d20_max_high_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 3605 | 宏致 |  | TWSE | 90.1 | 9.685100183421424 | 5.257009345794383 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 5460 | 同協 |  | TPEx | 18.95 | 9.257052046086612 | 9.85507246376811 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 1466 | 聚隆 |  | TWSE | 17.85 | 8.404984052046625 | 9.846153846153861 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 8033 | 雷虎 |  | TWSE | 186.0 | 8.046636957126218 | 0.0 | red_candle_but_not_strong_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 5488 | 松普 |  | TPEx | 14.05 | 7.868416048678456 | 9.765625 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 6156 | 松上 |  | TPEx | 32.0 | 7.613659501439832 | 1.1058451816745807 | not_red_or_failed_close | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 3628 | 盈正 |  | TPEx | 80.0 | 7.6081886499093025 | 9.8901098901099 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 1417 | 嘉裕 |  | TWSE | 9.25 | 6.681228216658964 | 7.934655775962662 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 6215 | 和椿 |  | TWSE | 118.0 | 6.484823423005746 | 9.259259259259256 | strict_red_close_near_high | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 9935 | 慶豐富 |  | TWSE | 20.05 | 6.457901690185896 | 1.7766497461928932 | not_red_or_failed_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 3594 | 磐儀 |  | TPEx | 56.7 | 6.069170695425809 | 1.6129032258064724 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 1463 | 強盛新 |  | TWSE | 17.8 | 6.068955827368454 | 2.298850574712663 | red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 3563 | 牧德 |  | TWSE | 809.0 | 6.035512050340346 | 3.984575835475579 | red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 1294 | 漢田生技 |  | TPEx | 79.5 | 5.568720379146919 | 0.8883248730964466 | red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 2231 | 為升 |  | TWSE | 110.0 | 5.510654884081663 | 1.382488479262678 | red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 4590 | 富田-創 |  | TWSE | 88.0 | 5.4880554357948075 | 10.000000000000009 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 4533 | 協易機 |  | TPEx | 31.2 | 5.259488768396592 | 9.859154929577475 | strict_red_close_near_high | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 6133 | 金橋 |  | TWSE | 26.25 | 5.021766888026259 | 9.832635983263604 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 1460 | 宏遠 |  | TWSE | 7.92 | 5.017652488307548 | 9.999999999999986 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260702 | 5438 | 東友 |  | TPEx | 19.1 | 5.0139944022391045 | 4.087193460490468 | red_candle_but_not_strong_close | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |

## PDF Placement
- Place after the three-line candidate split and before or near category interpretation.
- Do not use this packet to replace the active core model ranking table.
- If current candidates overlap with core candidate rows, show the overlap as supporting evidence, not as a second buy/sell gate.

## Data Quality Notes
- Short-term samples are not full-cycle regime proof yet.
- Current use is suitable for tracking priority and discussion, not formal weight tuning.
- More bear-market and range-market samples are still required.

