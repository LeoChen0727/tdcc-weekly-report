# DAILY SHORT-TERM SPECIALTY PACKET

## Metadata
- generated_at: `2026-05-28 14:56:22 台北標準時間`
- main_price_date: `20260527`
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

## Weekly Surge Strict Parameter Research

- section_required_in_daily_pdf: `True`
- section_type: `short_term_specialty_not_six_category`
- entry_basis: `D+1 open`
- hit_definition: `D+1 open to D+N high reaches +10%`
- model_effect_allowed: `False`
- allowed_use: `research_watchlist_and_reporting_priority_only`
- rule: show `D+5` and `D+10` tables separately.

### D+5 Parameter Table
| rule_name | target_window | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 42 | 50.0 | 9.62 | 12.19 | 0.57 | insufficient_sample |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 42 | 50.0 | 9.62 | 12.19 | 0.57 | insufficient_sample |
| vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 64 | 48.44 | 9.44 | 12.81 | 1.05 | insufficient_sample |
| day_vol_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+5 | 83 | 48.19 | 9.56 | 11.55 | 1.16 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 117 | 47.86 | 9.61 | 12.75 | 1.26 | ok_initial_sample |
| day_vol_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+5 | 67 | 47.76 | 9.56 | 11.98 | 1.36 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 82 | 47.56 | 9.59 | 13.03 | 1.4 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_all_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 82 | 47.56 | 9.59 | 13.03 | 1.4 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 103 | 46.6 | 9.29 | 12.66 | 1.21 | ok_initial_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50 | D+5 | 103 | 46.6 | 9.29 | 12.66 | 1.21 | ok_initial_sample |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 37 | 45.95 | 8.82 | 10.78 | 0.33 | insufficient_sample |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+5 | 37 | 45.95 | 8.82 | 10.78 | 0.33 | insufficient_sample |

### D+10 Parameter Table
| rule_name | target_window | selected_stock_days | hit_rate_pct | median_next_open_to_high_return_pct | avg_next_open_to_high_return_pct | avg_signal_close_to_next_open_gap_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vol5_avg_ge_1_5 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 42 | 78.57 | 21.4 | 25.99 | 0.57 | insufficient_sample |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 42 | 78.57 | 21.4 | 25.99 | 0.57 | insufficient_sample |
| day_vol_ge_2 + market_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 37 | 78.38 | 19.68 | 23.28 | 0.33 | insufficient_sample |
| day_vol_ge_2 + market_strong_bull + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 37 | 78.38 | 19.68 | 23.28 | 0.33 | insufficient_sample |
| day_vol_ge_2 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 40 | 75.0 | 17.46 | 22.13 | 0.34 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + bb_width_not_extreme + return_10d_20_50 | D+10 | 46 | 71.74 | 19.84 | 24.25 | 0.78 | insufficient_sample |
| vol5_avg_ge_2 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+10 | 64 | 67.19 | 17.5 | 21.67 | 1.05 | insufficient_sample |
| vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 63 | 66.67 | 17.44 | 22.09 | 0.66 | insufficient_sample |
| vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 146 | 66.44 | 17.46 | 22.67 | 1.14 | ok_initial_sample |
| vol5_avg_ge_2 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 77 | 66.23 | 17.49 | 21.35 | 0.86 | insufficient_sample |
| vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50 | D+10 | 121 | 66.12 | 17.57 | 23.93 | 0.9 | ok_initial_sample |
| vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50 | D+10 | 117 | 65.81 | 16.31 | 22.78 | 1.26 | ok_initial_sample |

### Current Strict Research Candidates
| research_priority | stock_id | stock_name | matched_rules | best_d5_hit_rate_pct | best_d10_hit_rate_pct | best_d10_rule | research_caveat |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_strict_research_watch | 2495 | 普安 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2312 | 金寶 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 6209 | 今國光 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 4919 | 新唐 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 6141 | 柏承 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2355 | 敬鵬 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2233 | 宇隆 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_all_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + kd_bullish_not_overheated + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 47.86 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 6525 | 捷敏-KY | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + tdcc_high_up + rsi_50_75 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50 | 45.89 | 66.44 | vol5_avg_ge_1_5 + tdcc_high_up + rsi_50_75 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2401 | 凌陽 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 46.6 | 62.96 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 6271 | 同欣電 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 42.59 | 62.96 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 2305 | 全友 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 42.59 | 62.96 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 3704 | 合勤控 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50 | 42.59 | 62.96 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| A_strict_research_watch | 8473 | 山林水 | vol5_avg_ge_2 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_2 + market_bull + tdcc_all_up + close_above_ema23 + return_10d_20_50 | 42.59 | 62.96 | vol5_avg_ge_2 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 2484 | 希華 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_2 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + rsi_50_75 + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + rsi_50_75 + return_10d_20_50 | 42.89 | 58.41 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8110 | 華東 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 42.89 | 58.41 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 2493 | 揚博 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_bull + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50; vol5_avg_ge_1_5 + kd_bullish_not_overheated + bb_width_not_extreme + return_10d_20_50 | 42.89 | 58.41 | vol5_avg_ge_1_5 + bb_width_not_extreme + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 2302 | 麗正 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50 | 41.06 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6116 | 彩晶 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50 | 41.06 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 3673 | TPK-KY | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50 | 41.06 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8261 | 富鼎 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50 | 41.06 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 8926 | 台汽電 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50 | 41.06 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6770 | 力積電 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + bb_width_not_extreme + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_bull + bb_width_not_extreme + return_10d_20_50 | 40.69 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 6239 | 力成 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 38.97 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 3481 | 群創 | day_vol_ge_2 + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_high_up + return_10d_20_50; day_vol_ge_2 + market_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 38.97 | 58.12 | day_vol_ge_2 + tdcc_high_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |
| B_strict_research_confirm | 2472 | 立隆電 | vol5_avg_ge_1_5 + tdcc_all_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + macd_hist_pos + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_all_up + return_10d_20_50; vol5_avg_ge_1_5 + tdcc_high_up + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + close_above_ema23 + return_10d_20_50; vol5_avg_ge_1_5 + market_strong_bull + tdcc_high_up + macd_hist_pos + return_10d_20_50 | 41.06 | 57.95 | vol5_avg_ge_1_5 + tdcc_all_up + close_above_ema23 + return_10d_20_50 | strict_no_latest_theme_label; research_only; entry_basis_D+1_open; target_next_open_to_high_10pct |

## PDF Placement
- Place after the three-line candidate split and before or near category interpretation.
- Do not merge this packet into the six-category ranking table.
- If current candidates overlap with core candidate rows, show the overlap as a note, not as a model upgrade.

## Data Quality Notes
- Short-term samples are not full-cycle regime proof yet.
- Current use is suitable for tracking priority and discussion, not formal weight tuning.
- More bear-market and range-market samples are still required.

