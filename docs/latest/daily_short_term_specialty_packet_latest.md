# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-05-28 23:24:39 台北標準時間`
- main_price_date: `20260528`
- purpose: Force daily reports to include short-term specialty sections that are not part of the fixed six candidate categories.

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
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 53 | 56.60377358490566 | 3.53318562459065 | 60.37735849056604 | 3.1265187751252426 | ok_initial_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 54 | 61.111111111111114 | 4.904365045626126 | 59.25925925925925 | 3.356173095981236 | ok_initial_sample |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 37 | 45.94594594594595 | 2.2528002146140937 | 45.94594594594595 | 1.5480194802139131 | ok_initial_sample |

### D+10 Stats
| rule_name | mature_count | win_rate_close_to_close_pct | avg_relative_return_vs_benchmark_pct | win_rate_next_open_to_close_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- |
| phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w | 31 | 83.87096774193549 | 13.474838873664252 | 80.64516129032258 | 12.731785776147033 | ok_initial_sample |
| phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50 | 30 | 83.33333333333334 | 11.692903520551944 | 73.33333333333333 | 10.709988169589385 | ok_initial_sample |
| all_thresholds_overheated + 1w return 10~30 + MACD hist > 0 | 30 | 86.66666666666667 | 12.14298339680338 | 73.33333333333333 | 9.64020243682089 | ok_initial_sample |

### Current TDCC Edge Candidates
| stock_id | stock_name | theme | tdcc_price_phase |
| --- | --- | --- | --- |
| 3624 | 光頡 | passive components | overheated_after_tdcc |
| 3481 | 群創 | consumer electronics | overheated_after_tdcc |
| 3357 | 臺慶科 | passive components | overheated_after_tdcc |
| 8043 | 蜜望實 | other | overheated_after_tdcc |
| 2302 | 麗正 | other | overheated_after_tdcc |
| 6207 | 雷科 | other | overheated_after_tdcc |
| 1727 | 中華化 | other | overheated_after_tdcc |
| 8091 | 翔名 | other | overheated_after_tdcc |
| 2316 | 楠梓電 | other | overheated_after_tdcc |
| 5328 | 華容 | other | overheated_after_tdcc |
| 6209 | 今國光 | other | overheated_after_tdcc |
| 6116 | 彩晶 | other | overheated_after_tdcc |
| 8121 | 越峰 | other | overheated_after_tdcc |
| 6239 | 力成 | other | overheated_after_tdcc |
| 2428 | 興勤 | other | overheated_after_tdcc |
| 8261 | 富鼎 | power discrete/diodes | overheated_after_tdcc |
| 6284 | 佳邦 | other | overheated_after_tdcc |
| 6237 | 驊訊 | other | overheated_after_tdcc |
| 6271 | 同欣電 | other | overheated_after_tdcc |
| 3704 | 合勤控 | other | overheated_after_tdcc |

## Next-Open +10pct Touch Strict Parameter Research

- legacy_file_prefix: `weekly_surge` is kept only for backward compatibility.
- display_name_zh: `隔日開盤買進後 D+5 / D+10 / D+20 盤中觸及 +10% 研究`
- forbidden_label_zh: `周線急漲`
- not_weekly_candle: `True`
- section_required_in_daily_pdf: `True`
- section_type: `short_term_specialty_not_six_category`
- entry_basis: `D+1 open`; the signal is only knowable after the signal-day close.
- hit_definition: `D+1 open to D+N high reaches +10%`
- win_rate_definition: touch-rate of +10% intraperiod high after next-open entry; not D+N close-to-close return.
- model_effect_allowed: `False`
- allowed_use: `research_watchlist_and_reporting_priority_only`
- rule: show `D+5` and `D+10` tables separately.

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 85 | 47.06 | 9.29 | 13.02 | 1.3 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 85 | 47.06 | 9.29 | 13.02 | 1.3 | insufficient_sample |
| vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 66 | 46.97 | 8.99 | 12.64 | 0.99 | insufficient_sample |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 45 | 46.67 | 9.0 | 11.75 | 0.64 | insufficient_sample |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 45 | 46.67 | 9.0 | 11.75 | 0.64 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 106 | 46.23 | 9.01 | 12.67 | 1.14 | ok_initial_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 106 | 46.23 | 9.01 | 12.67 | 1.14 | ok_initial_sample |
| vol5_avg_ge_3 + market_strong_bull + bb_width_not_extreme + return_10d_20_50 | D+5 | 35 | 45.71 | 7.52 | 10.71 | 1.31 | insufficient_sample |
| vol5_avg_ge_3 + bb_width_not_extreme + return_10d_20_50 | D+5 | 35 | 45.71 | 7.52 | 10.71 | 1.31 | insufficient_sample |
| vol5_avg_ge_3 + market_bull + bb_width_not_extreme + return_10d_20_50 | D+5 | 35 | 45.71 | 7.52 | 10.71 | 1.31 | insufficient_sample |
| day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+5 | 88 | 45.45 | 8.77 | 11.17 | 1.15 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 124 | 45.16 | 9.44 | 12.49 | 1.21 | ok_initial_sample |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 45 | 73.33 | 20.0 | 24.89 | 0.64 | insufficient_sample |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 45 | 73.33 | 20.0 | 24.89 | 0.64 | insufficient_sample |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 40 | 72.5 | 17.46 | 22.44 | 0.54 | insufficient_sample |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 40 | 72.5 | 17.46 | 22.44 | 0.54 | insufficient_sample |
| day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 43 | 69.77 | 16.03 | 21.42 | 0.54 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 49 | 67.35 | 17.49 | 23.35 | 0.83 | insufficient_sample |
| vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+10 | 66 | 65.15 | 17.5 | 21.82 | 0.99 | insufficient_sample |
| vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 65 | 64.62 | 17.44 | 22.23 | 0.62 | insufficient_sample |
| vol5_avg_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 79 | 64.56 | 17.49 | 21.48 | 0.82 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 154 | 64.29 | 17.01 | 22.23 | 1.09 | ok_initial_sample |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 129 | 63.57 | 17.44 | 23.32 | 0.85 | ok_initial_sample |
| vol5_avg_ge_2 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+10 | 57 | 63.16 | 16.88 | 21.82 | 0.7 | insufficient_sample |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_strict_research_watch | 3257 | 虹冠電 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50 | 46.23 | 64.29 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 3131 | 弘塑 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 46.23 | 64.29 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2401 | 凌陽 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50 | 46.23 | 64.29 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2495 | 普安 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 45.16 | 64.29 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2312 | 金寶 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 45.16 | 64.29 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 3673 | TPK-KY | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 45.16 | 64.29 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 9105 | 泰金寶-DR | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 43.2 | 62.72 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2305 | 全友 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 43.2 | 62.72 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2356 | 英業達 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 43.2 | 62.72 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 6116 | 彩晶 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 43.2 | 62.72 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 1563 | 巧新 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 43.2 | 62.72 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 1409 | 新纖 | vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_high_up + return_10d_20_50 | 41.34 | 62.35 | vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6770 | 力積電 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50 | 42.68 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 2302 | 麗正 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 42.5 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8473 | 山林水 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | 42.5 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6271 | 同欣電 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.5 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 3704 | 合勤控 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.5 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8261 | 富鼎 | vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 42.5 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6870 | 騰雲 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 41.34 | 59.43 | vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8110 | 華東 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 42.68 | 57.96 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 3321 | 同泰 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 42.68 | 57.96 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6862 | 三集瑞-KY | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 42.68 | 57.96 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8150 | 南茂 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 42.68 | 57.96 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6155 | 鈞寶 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50 | 42.68 | 57.96 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 2426 | 鼎元 | day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + market_bull + rsi_50_75 + return_10d_20_50 | 40.58 | 57.07 | day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |

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
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+5 | 4631 | 4505 | 41.4 | 0.05 | -2.0 | 34.38 | 12.7 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+5 | 3195 | 3125 | 40.35 | -0.11 | -2.19 | 32.9 | 12.03 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+5 | 2283 | 2241 | 39.8 | -0.26 | -2.31 | 32.22 | 11.33 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+5 | 6573 | 6377 | 41.6 | 0.07 | -1.76 | 31.66 | 11.42 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+5 | 1680 | 1658 | 38.42 | -0.64 | -2.71 | 31.54 | 10.74 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+5 | 4396 | 4293 | 40.6 | -0.07 | -1.93 | 30.54 | 10.88 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+5 | 1261 | 1248 | 37.34 | -0.81 | -2.74 | 30.21 | 10.1 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+5 | 2169 | 2136 | 39.09 | -0.48 | -2.28 | 30.15 | 10.02 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+5 | 3042 | 2980 | 40.27 | -0.16 | -2.07 | 30.13 | 10.23 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+5 | 737 | 732 | 35.11 | -1.09 | -2.9 | 29.78 | 9.84 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+5 | 1624 | 1607 | 37.9 | -0.67 | -2.4 | 29.06 | 9.52 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+5 | 9777 | 9483 | 41.16 | 0.12 | -1.51 | 27.97 | 9.85 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+5 | 4007 | 3923 | 39.59 | -0.23 | -1.96 | 27.96 | 9.25 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+5 | 928 | 922 | 35.03 | -1.17 | -2.86 | 27.87 | 9.0 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_3pct | D+5 | 2806 | 2757 | 38.19 | -0.55 | -2.16 | 27.86 | 9.18 | ok |

### D+10 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+10 | 4631 | 4322 | 45.16 | 2.29 | -1.34 | 46.07 | 23.92 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+10 | 3195 | 3007 | 43.33 | 1.97 | -1.85 | 44.23 | 22.98 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+10 | 6573 | 6122 | 44.71 | 2.03 | -1.33 | 43.65 | 22.02 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+10 | 2283 | 2165 | 42.73 | 1.64 | -2.01 | 43.33 | 21.89 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+10 | 4396 | 4134 | 43.23 | 1.82 | -1.75 | 42.33 | 21.19 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+10 | 1680 | 1614 | 40.77 | 0.75 | -2.42 | 42.19 | 20.2 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+10 | 3042 | 2877 | 42.61 | 1.5 | -1.89 | 41.64 | 20.23 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+10 | 2169 | 2071 | 41.14 | 0.89 | -2.31 | 41.28 | 19.31 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+10 | 1261 | 1226 | 39.97 | 0.53 | -2.49 | 41.27 | 19.41 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+10 | 737 | 720 | 38.89 | 0.21 | -2.83 | 41.25 | 20.14 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+10 | 1624 | 1569 | 40.41 | 0.71 | -2.33 | 40.47 | 18.67 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+10 | 9777 | 9123 | 44.12 | 1.76 | -1.27 | 39.73 | 19.48 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+10 | 928 | 904 | 38.61 | 0.04 | -2.85 | 39.6 | 18.25 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+10 | 4007 | 3796 | 42.33 | 1.33 | -1.84 | 39.41 | 18.68 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+10 | 6051 | 5698 | 42.77 | 1.58 | -1.7 | 39.36 | 19.15 | ok |

### D+20 Explosive Volume Table
| rule_name | horizon | selected_stock_days | mature_count | close_win_rate_pct | avg_close_return_pct | median_close_return_pct | hit_rate_high_ge_10pct | hit_rate_high_ge_20pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_ratio_prev20_ge_2x_signal_return_ge_7pct | D+20 | 4631 | 3861 | 46.0 | 5.19 | -1.61 | 57.21 | 36.44 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_5pct | D+20 | 6573 | 5452 | 45.95 | 4.75 | -1.46 | 55.32 | 34.56 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_7pct | D+20 | 3195 | 2726 | 43.62 | 4.0 | -2.46 | 54.73 | 34.01 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_5pct | D+20 | 4396 | 3728 | 44.02 | 3.72 | -2.21 | 53.46 | 32.27 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_7pct | D+20 | 2283 | 1980 | 42.17 | 3.07 | -3.07 | 53.08 | 31.92 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_5pct | D+20 | 3042 | 2625 | 42.55 | 2.91 | -2.74 | 52.0 | 30.32 | ok |
| volume_ratio_prev20_ge_2x_signal_return_ge_3pct | D+20 | 9777 | 8171 | 45.91 | 4.15 | -1.26 | 51.94 | 31.15 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_7pct | D+20 | 1680 | 1490 | 40.74 | 2.1 | -3.3 | 51.88 | 30.6 | ok |
| volume_ratio_prev20_ge_3x_signal_return_ge_3pct | D+20 | 6051 | 5168 | 44.49 | 3.41 | -1.73 | 51.28 | 29.72 | ok |
| volume_ratio_prev20_ge_5x_signal_return_ge_5pct | D+20 | 2169 | 1915 | 40.94 | 2.12 | -3.12 | 51.07 | 29.5 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_7pct | D+20 | 737 | 674 | 39.17 | 1.43 | -3.69 | 50.89 | 29.38 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_7pct | D+20 | 1261 | 1134 | 39.51 | 1.71 | -3.55 | 50.62 | 29.81 | ok |
| volume_ratio_prev20_ge_6x_signal_return_ge_5pct | D+20 | 1624 | 1454 | 40.1 | 1.71 | -3.34 | 50.28 | 28.75 | ok |
| volume_ratio_prev20_ge_4x_signal_return_ge_3pct | D+20 | 4007 | 3476 | 42.61 | 2.71 | -2.42 | 50.17 | 28.45 | ok |
| volume_ratio_prev20_ge_8x_signal_return_ge_5pct | D+20 | 928 | 843 | 38.2 | 0.8 | -3.76 | 48.99 | 26.81 | ok |

### D+5 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| red_candle_but_not_strong_close | high_zone_extension_or_chase | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+5 | 6 | 7 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | bottom_or_low_zone_volume_reversal | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | bottom_or_low_zone_volume_reversal | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | insufficient_position_history | ai_server_theme | structural_theme_bucket | core_mainstream_theme | ai_server_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 4 | 0 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 3 | 5 | 2 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 0 | 1 | 100.0 |
| not_red_or_failed_close | high_zone_extension_or_chase | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 2 | 3 | 3 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 3 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+5 | 6 | 5 | 1 | 100.0 |

### D+10 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| invalid_intraday_range | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 4 | 3 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 0 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | network_communication_theme | structural_theme_bucket | core_mainstream_theme | network_communication_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 7 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 6 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 5 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 4 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 3 | 5 | 1 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 0 | 2 | 100.0 |
| red_candle_but_not_strong_close | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 4 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 0 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | high_zone_extension_or_chase | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 4 | 5 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+10 | 2 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 10 | 3 | 2 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 10 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 10 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 8 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 6 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable | D+10 | 5 | 7 | 1 | 100.0 |

### D+20 Explosive Volume By Price Position
| signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | theme_status_group | horizon | volume_ratio_threshold | min_signal_return_pct | mature_count | close_win_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| not_red_or_failed_close | near_high_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 7 | 1 | 100.0 |
| not_red_or_failed_close | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| not_red_or_failed_close | mid_range_volume_attack | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| not_red_or_failed_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| not_red_or_failed_close | mid_range_volume_attack | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| not_red_or_failed_close | mid_range_volume_attack | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 2 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 4 | 7 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | low_earth_orbit_satellite_theme | structural_theme_bucket | core_mainstream_theme | low_earth_orbit_satellite_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 7 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | semiconductor_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 7 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 2 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | mid_range_volume_attack | semiconductor_equipment_theme | structural_theme_bucket | core_mainstream_theme | semiconductor_equipment_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 5 | 1 | 100.0 |
| relaxed_red_small_upper_shadow | mid_range_volume_attack | passive_component_theme | structural_theme_bucket | core_mainstream_theme | passive_component_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 3 | 1 | 100.0 |
| strict_red_close_near_high | insufficient_position_history | glass_fiber_ccl_theme | structural_theme_bucket | core_mainstream_theme | glass_fiber_ccl_theme | mainstream_growth_theme | theme_context_unavailable | D+20 | 3 | 0 | 4 | 100.0 |

### Latest Explosive Volume Events
| date | stock_id | stock_name | industry | market | close | volume_ratio_vs_prev20 | signal_return_1d_pct | signal_quality_bucket | price_position_bucket | market_theme_group | theme_group_source | theme_structural_status | structural_theme_bucket | theme_mainstream_label | next_open_to_d10_max_high_return_pct | next_open_to_d20_max_high_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260527 | 2438 | 翔耀 |  | TWSE | 25.3 | 8.75722595822178 | 10.000000000000009 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 3257 | 虹冠電 |  | TWSE | 61.1 | 7.001378217160242 | 2.1739130434782705 | not_red_or_failed_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 1503 | 士電 |  | TWSE | 221.0 | 6.868487902795599 | 8.866995073891616 | strict_red_close_near_high | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 1409 | 新纖 |  | TWSE | 18.9 | 6.849635149489252 | 7.082152974504252 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 1340 | 勝悅-KY |  | TWSE | 5.52 | 6.545780749096642 | 4.150943396226414 | strict_red_close_near_high | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 5520 | 力泰 |  | TPEx | 82.2 | 6.456692913385827 | 0.0 | not_red_or_failed_close | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 5274 | 信驊 |  | TPEx | 18230.0 | 6.252972600379114 | 5.742459396751731 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 2516 | 新建 |  | TWSE | 13.6 | 5.878352200842433 | 5.836575875486383 | red_candle_but_not_strong_close | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 1810 | 和成 |  | TWSE | 19.9 | 5.875820173954962 | 6.133333333333324 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 8466 | 美吉吉-KY |  | TWSE | 16.5 | 5.736801413939451 | 3.4482758620689724 | not_red_or_failed_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 2434 | 統懋 |  | TWSE | 33.2 | 5.484083899646082 | 9.933774834437092 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 2369 | 菱生 |  | TWSE | 40.15 | 5.462941649142042 | 6.49867374005304 | relaxed_red_small_upper_shadow | high_zone_extension_or_chase | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 4952 | 凌通 |  | TWSE | 55.8 | 5.303264298143161 | 1.4545454545454417 | not_red_or_failed_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 6698 | 旭暉應材 |  | TWSE | 36.55 | 5.10578429266005 | 6.095791001451367 | relaxed_red_small_upper_shadow | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 1315 | 達新 |  | TWSE | 62.0 | 5.046365574723784 | 2.1416803953871355 | strict_red_close_near_high | bottom_or_low_zone_volume_reversal | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 3321 | 同泰 |  | TWSE | 19.05 | 4.986091460100324 | 4.670329670329676 | strict_red_close_near_high | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 7734 | 印能科技 |  | TPEx | 3840.0 | 4.8166539343009935 | 6.371191135734078 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 2321 | 東訊 |  | TWSE | 15.0 | 4.795674336186437 | 4.895104895104896 | red_candle_but_not_strong_close | mid_range_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 6855 | 數泓科 |  | TPEx | 111.0 | 4.720496894409938 | 0.0 | red_candle_but_not_strong_close | low_to_mid_reclaim_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |
| 20260527 | 8110 | 華東 |  | TWSE | 60.6 | 4.621045813402994 | 9.981851179673317 | red_candle_but_not_strong_close | near_high_volume_attack | theme_context_unavailable | unavailable | theme_context_unavailable | theme_context_unavailable | theme_context_unavailable |  |  |

## PDF Placement
- Place after the three-line candidate split and before or near category interpretation.
- Do not merge this packet into the six-category ranking table.
- If current candidates overlap with core candidate rows, show the overlap as a note, not as a model upgrade.

## Data Quality Notes
- Short-term samples are not full-cycle regime proof yet.
- Current use is suitable for tracking priority and discussion, not formal weight tuning.
- More bear-market and range-market samples are still required.

