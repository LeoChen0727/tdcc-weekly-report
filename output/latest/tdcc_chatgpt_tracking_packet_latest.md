# TDCC CHATGPT TRACKING PACKET

## Metadata
- generated_at: 2026-05-30 15:48:49 Asia/Taipei
- main_price_date: 20260529
- latest_tdcc_signal_date: 20260529
- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md
- overall_mature_d5_count: 81
- phase_mature_d5_count: 81
- overall_mature_d10_count: 41
- phase_mature_d10_count: 41
- overall_mature_d20_count: 0
- phase_mature_d20_count: 0
- pending_count: 38
- insufficient_sample_count: 866
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 28
- theme_other_pct: 18.41
- sample_status: phase_d5_available_longer_horizons_pending
- relaxed_filter: False
- missing_columns: none

## Data Availability
- tdcc_signal_snapshot.csv: yes
- tdcc_normalized_signal_log.csv: yes
- tdcc_signal_performance.csv: yes
- tdcc_pre_move_accumulation_history.csv: yes
- tdcc_pre_move_accumulation_latest.csv: yes
- tdcc_signal_effectiveness_latest.csv: yes
- tdcc_signal_effectiveness_latest.md: yes

## Data Quality Notes
- missing_columns: none
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 28
- theme_lookup_sources: {'config': 28, 'company_theme_mapping': 28, 'all_candidates': 0}
- theme_other_before: 1197
- theme_other_after: 224
- theme_other_pct: 18.41
- sample_status: phase_d5_available_longer_horizons_pending
- relaxed_filter: False
- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution

## Mature Sample Status

- overall_mature_d5_count: 81
- phase_mature_d5_count: 81
- overall_mature_d10_count: 41
- phase_mature_d10_count: 41
- overall_mature_d20_count: 0
- phase_mature_d20_count: 0
- pending_count: 38
- insufficient_sample_count: 866
- phase_mature_join_quality: ok
- sample_status: phase_d5_available_longer_horizons_pending

- phase-level D+20 尚未成熟，不可做 phase 勝率結論。

## TDCC Strength Ranking Top 30

| rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | abm_score | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | risk_label | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 0.00 | -0.99 | -4.50 | 1.76 | 0.37 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 1438 | 三地開發 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 82.00 | -2.90 | -9.26 | -10.60 | -2.64 | 0.19 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3 | 1443 | 立益物流 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | strong_momentum | 66.00 | -3.64 | 18.63 | -12.66 | -2.04 | 0.58 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4 | 1452 | 宏益 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 80.00 | -1.42 | -8.33 | -12.78 | -3.44 | 0.51 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5 | 1460 | 宏遠 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 91.00 | -0.57 | -0.57 | -10.07 | -1.31 | 0.91 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6 | 1471 | 首利 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 86.00 | 2.76 | -1.33 | 0.13 | 3.96 | 2.68 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 7 | 1584 | 精剛 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 78.00 | 0.76 | 1.02 | -1.13 | -0.45 | 0.04 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 1614 | 三洋電 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 85.00 | 2.27 | -1.10 | -7.04 | 0.73 | 0.95 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 9 | 1617 | 榮星 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | watch_only | 87.00 | 7.05 | 6.33 | 2.89 | 7.70 | 3.18 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 10 | 1626 | 艾美特-KY | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 79.00 | 0.30 | -11.98 | -8.75 | -3.53 | 0.91 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 11 | 1723 | 中碳 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 98.00 | 0.73 | 5.11 | -4.86 | 2.54 | 0.85 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 12 | 1734 | 杏輝 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 83.00 | -0.16 | -2.54 | -8.32 | -0.19 | 1.44 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 2535 | 達欣工 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | early_breakout | 77.00 | 3.61 | 11.37 | -1.72 | 6.52 | 0.48 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 3038 | 全台 | semiconductor | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 0.22 | 1.31 | -5.54 | 1.35 | 1.18 | 10.00 | 115.14 | 10.00 | 14.00 | 0.00 | 3.14 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 3313 | 斐成 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 80.00 | -5.93 | -7.88 | -0.93 | -3.56 | 0.09 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 16 | 3434 | 哲固 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 1.55 | 1.55 | 2.49 | 2.27 | 0.49 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 6534 | 正瀚-創 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 100.00 | -1.03 | 3.78 | -9.58 | 0.27 | 2.18 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 18 | 6576 | 逸達 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 72.00 | -4.35 | -3.75 | -3.92 | -3.23 | 0.60 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 19 | 7718 | 友鋮 | other | single_name_signal | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | -1.80 | 4.26 | 0.06 | 0.32 | 1.50 | 10.00 | 242.25 | 10.00 | 25.00 | 0.00 | -0.75 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 8409 | 商之器 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 89.00 | -4.51 | -5.46 | -1.91 | -1.77 | 0.96 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 21 | 1308 | 亞聚 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | failed_after_tdcc | quiet_accumulation | 89.00 | -1.50 | -12.96 | -7.88 | -2.06 | 0.97 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | divergence_failed_watch | strong_but_divergent | 訊號後價格轉弱，列為失效觀察。 |
| 22 | 1527 | 鑽全 | other electronics | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 0.15 | 1.54 | -5.68 | 1.27 | 1.06 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 23 | 1535 | 中宇 | other electronics | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 89.00 | -0.10 | -2.95 | -8.34 | -0.50 | 0.81 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 2024 | 志聯 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 95.00 | -0.35 | 0.00 | -3.42 | 1.79 | 1.90 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 25 | 3705 | 永信 | other electronics | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_price_divergence | quiet_accumulation | 100.00 | 0.18 | 0.36 | -9.18 | 0.31 | 1.19 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 26 | 4527 | 方土霖 | other | single_name_signal | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 4.67 | 7.49 | 4.86 | 5.15 | 1.32 | 10.00 | 242.25 | 10.00 | 25.00 | 0.00 | -0.75 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 27 | 4744 | 皇將 | other | single_name_signal | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 3.28 | 4.69 | 3.15 | 3.47 | 0.16 | 10.00 | 242.25 | 10.00 | 25.00 | 0.00 | -0.75 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 28 | 1233 | 天仁 | other | single_name_signal | high | 215.00 | 5 | True | True | tdcc_price_divergence | watch_only | 86.00 | -2.78 | -2.61 | -11.43 | -2.11 | 14.19 | 10.00 | 242.25 | 10.00 | 25.00 | 0.00 | -0.75 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 29 | 1325 | 恆大 | traditional industries | mainstream_leader | high | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 1.50 | 3.05 | -6.57 | 0.14 | 0.61 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 30 | 1410 | 南染 | traditional industries | mainstream_leader | high | 215.00 | 5 | True | True | tdcc_price_divergence | quiet_accumulation | 86.00 | -0.19 | -3.99 | -10.69 | -2.04 | 0.28 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Pre-Move Accumulation / ABM Top 30

| abm_rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | abm_score | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | accumulation_label | tracking_priority | trigger_to_watch | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3310 | 佳穎 | other electronics | mainstream_leader | high | 93.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | -5.98 | 3.43 | 2.64 | 2.35 | 1.30 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 3434 | 哲固 | other electronics | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 1.55 | 1.55 | 2.49 | 2.27 | 0.49 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 3 | 5609 | 中菲行 | traditional industries | mainstream_leader | high | 100.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 0.62 | 3.85 | 0.89 | 1.61 | 0.49 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 4 | 1723 | 中碳 | biotechnology | mainstream_leader | high | 98.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 0.73 | 5.11 | -4.86 | 2.54 | 0.85 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 5 | 2347 | 聯強 | other electronics | mainstream_leader | high | 95.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 2.14 | 4.12 | -4.40 | 2.43 | 0.90 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 6 | 3050 | 鈺德 | semiconductor | mainstream_leader | high | 95.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.40 | 2.45 | -2.74 | 2.39 | 1.12 | 10.00 | 115.14 | 10.00 | 14.00 | 0.00 | 3.14 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 7 | 2718 | 全心投控 | traditional industries | mainstream_leader | high | 95.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 0.76 | 6.29 | -1.28 | 4.00 | 0.59 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 2546 | 根基 | traditional industries | mainstream_leader | high | 92.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 3.55 | 3.67 | -4.61 | 2.80 | 0.51 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 9 | 6189 | 豐藝 | other electronics | mainstream_leader | high | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -2.71 | 4.90 | -4.07 | 1.73 | 0.56 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 3376 | 新日興 | other electronics | mainstream_leader | high | 89.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -3.57 | -0.74 | -3.45 | -1.88 | 1.20 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 2365 | 昆盈 | other electronics | mainstream_leader | high | 88.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | -1.15 | 7.80 | -3.05 | 5.16 | 1.14 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 12 | 3303 | 岱稜 | other electronics | mainstream_leader | high | 86.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | 0.71 | -0.98 | -1.17 | 0.10 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 2476 | 鉅祥 | other electronics | mainstream_leader | high | 85.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 0.83 | 4.27 | -2.56 | 2.61 | 0.86 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 6752 | 叡揚 | other electronics | mainstream_leader | high | 83.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 0.50 | -3.81 | 1.57 | -0.32 | 1.36 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 6620 | 漢達 | other electronics | mainstream_leader | high | 82.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | -4.51 | -4.13 | 1.47 | -0.51 | 0.20 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 16 | 1314 | 中石化 | traditional industries | mainstream_leader | high | 81.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -0.56 | -5.12 | -3.89 | -0.28 | 0.96 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 3313 | 斐成 | other electronics | mainstream_leader | high | 80.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | -5.93 | -7.88 | -0.93 | -3.56 | 0.09 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 5403 | 中菲 | other electronics | mainstream_leader | high | 80.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | -0.47 | -8.85 | -1.39 | -3.69 | 0.56 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | -0.99 | -4.50 | 1.76 | 0.37 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 1709 | 和益 | biotechnology | mainstream_leader | high | 100.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 5.43 | 4.02 | -2.05 | 4.20 | 0.94 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 21 | 1733 | 五鼎 | biotechnology | mainstream_leader | high | 100.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.84 | 4.73 | -4.65 | 2.87 | 1.69 | 10.00 | 122.61 | 10.00 | 13.00 | 0.00 | -0.39 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 22 | 2008 | 高興昌 | traditional industries | mainstream_leader | high | 100.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 4.72 | 4.91 | -3.74 | 3.73 | 1.75 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 23 | 2603 | 長榮 | traditional industries | mainstream_leader | high | 100.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | -2.74 | 5.45 | -2.41 | 1.43 | 1.50 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 5324 | 士開 | other electronics | mainstream_leader | high | 87.00 | 205.00 | 4 | True | True | tdcc_leading_price | early_breakout | -0.42 | 11.74 | 2.09 | 4.57 | 0.08 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 25 | 2027 | 大成鋼 | traditional industries | mainstream_leader | high | 83.00 | 205.00 | 4 | True | True | tdcc_leading_price | watch_only | -0.72 | 10.48 | -4.13 | 3.37 | 0.56 | 10.00 | 360.59 | 10.00 | 37.00 | 0.00 | -2.41 | watch_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 26 | 6214 | 精誠 | other electronics | mainstream_leader | high | 80.00 | 205.00 | 4 | True | True | tdcc_leading_price | watch_only | 0.77 | 9.17 | -1.27 | 4.15 | 1.24 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | watch_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 27 | 6176 | 瑞儀 | other electronics | mainstream_leader | high | 80.00 | 195.00 | 3 | True | True | tdcc_leading_price | watch_only | -0.93 | 6.82 | -1.72 | 3.20 | 1.56 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | watch_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 28 | 6170 | 統振 | other electronics | mainstream_leader | high | 80.00 | 185.00 | 2 | True | True | tdcc_leading_price | watch_only | 1.98 | -1.34 | 0.80 | 0.98 | 0.23 | 10.00 | 679.65 | 10.00 | 88.00 | 0.00 | 2.65 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 29 | 4306 | 炎洲 | other | single_name_signal | high | 92.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | 6.44 | -3.01 | 4.02 | 1.52 | 10.00 | 242.25 | 10.00 | 25.00 | 0.00 | -0.75 | prime_pre_move | C_weak_or_discounted | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 30 | 8908 | 欣雄 | other | single_name_signal | high | 90.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.62 | 3.55 | 0.11 | 2.09 | 0.29 | 10.00 | 242.25 | 10.00 | 25.00 | 0.00 | -0.75 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |

## Theme Mainstream Summary

| theme | theme_mainstream_status | signal_count | leading_count | confirmed_count | late_or_overheated_count | divergence_count | avg_tdcc_strength_score | avg_abm_score | representative_codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other electronics | mainstream_leader | 529 | 53 | 6 | 61 | 31 | 155.29 | 50.69 | 1584/1626/1614/1617/3313 |
| other | single_name_signal | 224 | 24 | 0 | 3 | 32 | 155.69 | 59.10 | 7718/4527/4744/1233/4119 |
| traditional industries | mainstream_leader | 220 | 35 | 1 | 2 | 32 | 164.75 | 62.35 | 1323/1460/1443/1438/1452 |
| biotechnology | mainstream_leader | 117 | 11 | 1 | 5 | 18 | 156.50 | 56.39 | 1723/1734/8409/6576/6534 |
| semiconductor | mainstream_leader | 86 | 10 | 0 | 10 | 1 | 153.37 | 51.17 | 3038/3019/3047/3041/3060 |
| finance | non_mainstream_watch | 21 | 0 | 1 | 4 | 0 | 161.19 | 50.14 | 2816/2891/2881/2882/6005 |
| passive components | mainstream_overheated | 5 | 0 | 0 | 2 | 0 | 160.00 | 26.40 | 2375/2492/3624/3357/6173 |
| semiconductor equipment/materials | non_mainstream_watch | 4 | 1 | 0 | 2 | 0 | 173.75 | 38.25 | 3131/5234/8028/3498 |
| memory | mainstream_overheated | 3 | 0 | 0 | 1 | 0 | 175.00 | 14.00 | 2344/3006/5351 |
| power discrete/diodes | mainstream_overheated | 3 | 0 | 0 | 2 | 0 | 163.33 | 15.00 | 8261/5425/2481 |
| consumer electronics | non_mainstream_watch | 2 | 0 | 0 | 0 | 0 | 175.00 | 66.50 | 5371/6861 |
| networking | mainstream_overheated | 2 | 0 | 0 | 2 | 0 | 205.00 | 0.00 | 4906/6285 |
| PCB/CCL | single_name_signal | 1 | 0 | 0 | 0 | 0 | 50.00 | 40.00 | 5464 |

## TDCC Strength Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1323 | 永裕 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1438 | 三地開發 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1443 | 立益物流 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1452 | 宏益 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1460 | 宏遠 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1471 | 首利 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1584 | 精剛 | other electronics | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1614 | 三洋電 | other electronics | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1617 | 榮星 | other electronics | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1626 | 艾美特-KY | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1723 | 中碳 | biotechnology | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1734 | 杏輝 | biotechnology | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2535 | 達欣工 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3038 | 全台 | semiconductor | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3313 | 斐成 | other electronics | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3434 | 哲固 | other electronics | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 6534 | 正瀚-創 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6576 | 逸達 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7718 | 友鋮 | other | single_name_signal | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 8409 | 商之器 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1308 | 亞聚 | traditional industries | mainstream_leader | 225.00 | failed_after_tdcc | strong_but_divergent | 訊號後價格轉弱，列為失效觀察。 |
| 1527 | 鑽全 | other electronics | mainstream_leader | 225.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1535 | 中宇 | other electronics | mainstream_leader | 225.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2024 | 志聯 | traditional industries | mainstream_leader | 225.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3705 | 永信 | other electronics | mainstream_leader | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4527 | 方土霖 | other | single_name_signal | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 4744 | 皇將 | other | single_name_signal | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1233 | 天仁 | other | single_name_signal | 215.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1325 | 恆大 | traditional industries | mainstream_leader | 215.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1410 | 南染 | traditional industries | mainstream_leader | 215.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Pre-Move / ABM Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3310 | 佳穎 | other electronics | mainstream_leader | 93.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 3434 | 哲固 | other electronics | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5609 | 中菲行 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1723 | 中碳 | biotechnology | mainstream_leader | 98.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2347 | 聯強 | other electronics | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3050 | 鈺德 | semiconductor | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2718 | 全心投控 | traditional industries | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2546 | 根基 | traditional industries | mainstream_leader | 92.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6189 | 豐藝 | other electronics | mainstream_leader | 92.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3376 | 新日興 | other electronics | mainstream_leader | 89.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線 |
| 2365 | 昆盈 | other electronics | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3303 | 岱稜 | other electronics | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線 |
| 2476 | 鉅祥 | other electronics | mainstream_leader | 85.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6752 | 叡揚 | other electronics | mainstream_leader | 83.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 6620 | 漢達 | other electronics | mainstream_leader | 82.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1314 | 中石化 | traditional industries | mainstream_leader | 81.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3313 | 斐成 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 5403 | 中菲 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1709 | 和益 | biotechnology | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1733 | 五鼎 | biotechnology | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 |
| 2603 | 長榮 | traditional industries | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 |
| 5324 | 士開 | other electronics | mainstream_leader | 87.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2027 | 大成鋼 | traditional industries | mainstream_leader | 83.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6214 | 精誠 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6176 | 瑞儀 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影 |
| 6170 | 統振 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 4306 | 炎洲 | other | single_name_signal | 92.00 | C_weak_or_discounted | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8908 | 欣雄 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流潛伏吸籌名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3310 | 佳穎 | other electronics | mainstream_leader | 93.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 3434 | 哲固 | other electronics | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5609 | 中菲行 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1723 | 中碳 | biotechnology | mainstream_leader | 98.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2347 | 聯強 | other electronics | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3050 | 鈺德 | semiconductor | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2718 | 全心投控 | traditional industries | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2546 | 根基 | traditional industries | mainstream_leader | 92.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6189 | 豐藝 | other electronics | mainstream_leader | 92.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3376 | 新日興 | other electronics | mainstream_leader | 89.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線 |
| 2365 | 昆盈 | other electronics | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3303 | 岱稜 | other electronics | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線 |
| 2476 | 鉅祥 | other electronics | mainstream_leader | 85.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6752 | 叡揚 | other electronics | mainstream_leader | 83.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 6620 | 漢達 | other electronics | mainstream_leader | 82.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1314 | 中石化 | traditional industries | mainstream_leader | 81.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3313 | 斐成 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 5403 | 中菲 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1709 | 和益 | biotechnology | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |

## 非主流但值得觀察名單

目前沒有可用資料。

## 孤單訊號 / 非主流降權名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4306 | 炎洲 | other | single_name_signal | 92.00 | C_weak_or_discounted | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8908 | 欣雄 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 9933 | 中鼎 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4171 | 瑞基 | other | single_name_signal | 86.00 | C_weak_or_discounted | tdcc_leading_price | 相對 benchmark 轉正；站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 4108 | 懷特 | other | single_name_signal | 86.00 | C_weak_or_discounted | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4513 | 福裕 | other | single_name_signal | 82.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 7718 | 友鋮 | other | single_name_signal | 100.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4706 | 大恭 | other | single_name_signal | 100.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流過熱風險名單

目前沒有可用資料。

## TDCC 背離 + 弱族群名單

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1109 | 信大 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1220 | 台榮 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1233 | 天仁 | other | single_name_signal | 215.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4107 | 邦特 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4119 | 旭富 | other | single_name_signal | 205.00 | failed_after_tdcc | strong_but_divergent | 訊號後價格轉弱，列為失效觀察。 |
| 4120 | 友華 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4129 | 聯合 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4161 | 聿新科 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4178 | 永笙-KY | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4401 | 東隆興 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4406 | 新昕纖 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4426 | 利勤 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4439 | 冠星-KY | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4441 | 振大環球 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4535 | 至興 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4538 | 大詠城 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5009 | 榮剛 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6865 | 偉康科技 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6918 | 愛派司 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6923 | 中台 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6965 | 中傑-KY | other | single_name_signal | 205.00 | failed_after_tdcc | strong_but_divergent | 訊號後價格轉弱，列為失效觀察。 |
| 7760 | 享溫馨 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7811 | 民盛 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8342 | 益張 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8916 | 光隆 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8930 | 青鋼 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8933 | 愛地雅 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8941 | 關中 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8942 | 森鉅 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9902 | 台火 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9906 | 欣巴巴 | other | single_name_signal | 205.00 | failed_after_tdcc | strong_but_divergent | 訊號後價格轉弱，列為失效觀察。 |
| 9949 | 琉園 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Top Risk List

- price_leading_tdcc: 股價已先漲，TDCC 訊號可能偏晚。
- overheated_after_tdcc: 籌碼強但股價已過熱。
- tdcc_price_divergence: TDCC 增加但股價轉弱，需列為失效觀察。

## Top Risk List - price_leading_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6285 | 啟碁 | networking | mainstream_overheated | 205.00 | price_leading_tdcc | 47.69 | 14.04 | 16.00 | 0.79 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8121 | 越峰 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | 41.93 | 17.59 | 13.29 | 0.02 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3704 | 合勤控 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | 32.62 | 12.69 | 18.01 | 1.09 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5011 | 久陽 | other | single_name_signal | 205.00 | price_leading_tdcc | 26.78 | 22.46 | 16.51 | 0.06 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6282 | 康舒 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | 26.50 | 12.12 | 11.03 | 0.96 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5488 | 松普 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | 23.36 | 18.22 | 12.36 | 0.02 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6125 | 廣運 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | 19.53 | 12.24 | 10.43 | 0.04 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6617 | 共信-KY | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | -3.60 | 14.51 | 9.26 | 0.43 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8096 | 擎亞 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 37.33 | 26.35 | 15.91 | 0.01 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8454 | 富邦媒 | biotechnology | mainstream_leader | 195.00 | price_leading_tdcc | 35.48 | 14.55 | 19.88 | 3.39 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5284 | jpp-KY | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 31.63 | 11.27 | 16.08 | 0.72 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8088 | 品安 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 20.48 | 10.84 | 8.85 | 0.02 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3131 | 弘塑 | semiconductor equipment/materials | non_mainstream_watch | 195.00 | price_leading_tdcc | 16.95 | 18.82 | 14.44 | 2.55 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2243 | 宏旭-KY | traditional industries | mainstream_leader | 195.00 | price_leading_tdcc | 0.18 | 20.13 | 16.92 | 1.89 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6155 | 鈞寶 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 36.37 | 18.74 | 15.54 | 1.97 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6706 | 惠特 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 35.64 | 21.01 | 15.77 | 1.24 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6716 | 應廣 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 30.17 | 14.92 | 9.92 | 0.19 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4919 | 新唐 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 29.83 | 15.30 | 8.22 | 0.16 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8104 | 錸寶 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 23.76 | 12.74 | 16.69 | 7.71 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2338 | 光罩 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 23.19 | 12.23 | 11.73 | 1.10 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |

## Top Risk List - overheated_after_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1563 | 巧新 | other electronics | mainstream_leader | 215.00 | overheated_after_tdcc | 60.92 | 40.40 | 41.70 | 8.05 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2375 | 凱美 | passive components | mainstream_overheated | 205.00 | overheated_after_tdcc | 95.88 | 58.86 | 47.95 | 2.81 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2428 | 興勤 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 67.82 | 33.10 | 32.20 | 2.85 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8289 | 泰藝 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 63.62 | 36.02 | 27.88 | 0.02 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2356 | 英業達 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 52.94 | 25.83 | 28.58 | 2.91 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6870 | 騰雲 | other | single_name_signal | 205.00 | overheated_after_tdcc | 49.02 | 40.10 | 28.36 | 1.67 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4906 | 正文 | networking | mainstream_overheated | 205.00 | overheated_after_tdcc | 44.90 | 18.30 | 23.90 | 1.99 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2426 | 鼎元 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 41.71 | 22.53 | 13.08 | 1.51 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2353 | 宏碁 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 27.54 | 18.43 | 20.46 | 1.77 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3026 | 禾伸堂 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 201.65 | 87.38 | 59.80 | 0.21 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2492 | 華新科 | passive components | mainstream_overheated | 205.00 | overheated_after_tdcc | 199.62 | 82.61 | 65.23 | 0.24 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6284 | 佳邦 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 58.49 | 40.03 | 28.78 | 0.06 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8261 | 富鼎 | power discrete/diodes | mainstream_overheated | 195.00 | overheated_after_tdcc | 52.74 | 25.92 | 22.42 | 1.68 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6127 | 九豪 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 52.61 | 43.50 | 31.75 | 0.01 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8163 | 達方 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 47.47 | 7.45 | 20.77 | 1.90 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3491 | 昇達科 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 41.94 | 28.79 | 20.50 | 0.93 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2312 | 金寶 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 40.87 | 31.21 | 25.02 | 1.45 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8473 | 山林水 | biotechnology | mainstream_leader | 195.00 | overheated_after_tdcc | 40.39 | 36.18 | 32.27 | 3.98 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3189 | 景碩 | semiconductor | mainstream_leader | 195.00 | overheated_after_tdcc | 38.07 | 41.35 | 30.70 | 0.28 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1409 | 新纖 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 35.71 | 26.66 | 29.86 | 1.23 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Top Risk List - tdcc_price_divergence Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6534 | 正瀚-創 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | 3.78 | -9.58 | 0.27 | 2.18 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1443 | 立益物流 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | 18.63 | -12.66 | -2.04 | 0.58 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1438 | 三地開發 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | -9.26 | -10.60 | -2.64 | 0.19 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1452 | 宏益 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | -8.33 | -12.78 | -3.44 | 0.51 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8409 | 商之器 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | -5.46 | -1.91 | -1.77 | 0.96 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6576 | 逸達 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | -3.75 | -3.92 | -3.23 | 0.60 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1626 | 艾美特-KY | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | -11.98 | -8.75 | -3.53 | 0.91 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1460 | 宏遠 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | -0.57 | -10.07 | -1.31 | 0.91 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3705 | 永信 | other electronics | mainstream_leader | 225.00 | tdcc_price_divergence | 0.36 | -9.18 | 0.31 | 1.19 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9946 | 三發地產 | traditional industries | mainstream_leader | 215.00 | tdcc_price_divergence | 3.46 | -10.73 | 0.18 | 0.50 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1410 | 南染 | traditional industries | mainstream_leader | 215.00 | tdcc_price_divergence | -3.99 | -10.69 | -2.04 | 0.28 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1233 | 天仁 | other | single_name_signal | 215.00 | tdcc_price_divergence | -2.61 | -11.43 | -2.11 | 14.19 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2230 | 泰茂 | traditional industries | mainstream_leader | 205.00 | tdcc_price_divergence | 4.63 | -4.14 | -5.35 | 0.06 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6527 | 明達醫 | biotechnology | mainstream_leader | 205.00 | tdcc_price_divergence | 4.48 | -2.79 | 0.08 | 1.38 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6215 | 和椿 | other electronics | mainstream_leader | 205.00 | tdcc_price_divergence | 14.86 | -10.95 | 3.41 | 0.61 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3526 | 凡甲 | other electronics | mainstream_leader | 205.00 | tdcc_price_divergence | 11.82 | -2.72 | -0.78 | 0.33 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6283 | 淳安 | other electronics | mainstream_leader | 205.00 | tdcc_price_divergence | 11.11 | -13.79 | -2.10 | 0.28 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4111 | 濟生 | biotechnology | mainstream_leader | 205.00 | tdcc_price_divergence | 1.87 | -1.88 | -0.04 | 0.25 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5511 | 德昌 | traditional industries | mainstream_leader | 205.00 | tdcc_price_divergence | 1.42 | -2.49 | 0.29 | 0.54 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5460 | 同協 | other electronics | mainstream_leader | 205.00 | tdcc_price_divergence | 0.00 | -1.72 | -0.70 | 0.32 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Phase Distribution

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 866.0 | 71.16 |
| tdcc_leading_price | 134.0 | 11.01 |
| tdcc_price_divergence | 106.0 | 8.71 |
| overheated_after_tdcc | 55.0 | 4.52 |
| price_leading_tdcc | 39.0 | 3.20 |
| tdcc_price_confirmed | 9.0 | 0.74 |
| failed_after_tdcc | 8.0 | 0.66 |

## Consecutive Weeks x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 420.0 |
| 1 | overheated_after_tdcc | 15.0 |
| 1 | price_leading_tdcc | 14.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 183.0 |
| 2 | overheated_after_tdcc | 19.0 |
| 2 | price_leading_tdcc | 10.0 |
| 2 | tdcc_leading_price | 31.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 20.0 |
| 3 | insufficient_price_context | 104.0 |
| 3 | overheated_after_tdcc | 10.0 |
| 3 | price_leading_tdcc | 5.0 |
| 3 | tdcc_leading_price | 27.0 |
| 3 | tdcc_price_confirmed | 2.0 |
| 3 | tdcc_price_divergence | 20.0 |
| 4 | failed_after_tdcc | 5.0 |
| 4 | insufficient_price_context | 145.0 |
| 4 | overheated_after_tdcc | 10.0 |
| 4 | price_leading_tdcc | 10.0 |
| 4 | tdcc_leading_price | 61.0 |
| 4 | tdcc_price_confirmed | 5.0 |
| 4 | tdcc_price_divergence | 54.0 |
| 5 | insufficient_price_context | 4.0 |
| 5 | overheated_after_tdcc | 1.0 |
| 5 | tdcc_leading_price | 2.0 |
| 5 | tdcc_price_divergence | 3.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | insufficient_price_context | 3.0 |
| 6 | tdcc_leading_price | 3.0 |
| 6 | tdcc_price_divergence | 1.0 |
| 7 | insufficient_price_context | 7.0 |
| 7 | tdcc_leading_price | 10.0 |
| 7 | tdcc_price_divergence | 8.0 |

## Mature Performance Summary

只使用 mature_dN=True 的資料。pending 不可視為正面或負面。

- phase-level D+20 尚未成熟，不可做 phase 勝率結論。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 17.0 | 8.52 | 6.22 | 11.0 | 18.69 | 8.67 | 0.0 |  |  | 27.23 | -5.27 |
| overheated_after_tdcc | 39.0 | 9.05 | 7.27 | 16.0 | 24.13 | 15.66 | 0.0 |  |  | 31.28 | -6.01 |
| price_leading_tdcc | 16.0 | 7.13 | 4.93 | 8.0 | 13.39 | 10.33 | 0.0 |  |  | 21.08 | -7.07 |
| tdcc_leading_price | 6.0 | 4.11 | 0.78 | 5.0 | 3.11 | 4.43 | 0.0 |  |  | 11.62 | -5.94 |
| tdcc_price_confirmed | 2.0 | 5.29 |  | 0.0 |  |  | 0.0 |  |  |  |  |
| tdcc_price_divergence | 1.0 | -1.74 | -4.68 | 1.0 | 19.34 |  | 0.0 |  |  | 19.34 | -11.15 |

## Model Tuning Recommendation

- tuning_status: not_ready
- reason: insufficient mature D+10 / D+20 samples
- allowed_changes: reporting_priority_only
- forbidden_changes: core_weight_change
- threshold_for_review: each major phase mature_d10 >= 30, or overall mature_d20 >= 100 with at least 3-4 weeks of data
- note: 目前可以調整追蹤優先級與報告分層，但不可調整核心 TDCC / ABM 權重。

## Interpretation Rules
- pending 不可視為正面或負面。
- same stock_id + signal_date 只能算一筆 normalized signal。
- TDCC Strength Ranking 找籌碼最強，不等於潛伏吸籌。
- Pre-Move / ABM Ranking 才是找潛伏吸籌。
- price_leading_tdcc / overheated_after_tdcc 不可寫成潛伏吸籌。
- tdcc_price_divergence 要列為失效觀察。
- 必須同時看絕對報酬與相對 TWSE / TPEx benchmark。
- 在 tuning_status=not_ready 前，不可調整核心模型權重。
