# TDCC CHATGPT TRACKING PACKET

## Metadata
- generated_at: 2026-07-04 19:41:17 Asia/Taipei
- main_price_date: 20260703
- latest_tdcc_signal_date: 20260703
- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md
- overall_mature_d5_count: 307
- phase_mature_d5_count: 307
- overall_mature_d10_count: 264
- phase_mature_d10_count: 264
- overall_mature_d20_count: 119
- phase_mature_d20_count: 119
- pending_count: 47
- insufficient_sample_count: 798
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 512
- theme_other_pct: 15.83
- sample_status: phase_samples_available
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
- theme_lookup_rows: 512
- theme_lookup_sources: {'config': 28, 'company_theme_mapping': 28, 'all_candidates': 650}
- theme_other_before: 1101
- theme_other_after: 177
- theme_other_pct: 15.83
- sample_status: phase_samples_available
- relaxed_filter: False
- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution

## Mature Sample Status

- overall_mature_d5_count: 307
- phase_mature_d5_count: 307
- overall_mature_d10_count: 264
- phase_mature_d10_count: 264
- overall_mature_d20_count: 119
- phase_mature_d20_count: 119
- pending_count: 47
- insufficient_sample_count: 798
- phase_mature_join_quality: ok
- sample_status: phase_samples_available

- phase-level mature sample 已可使用。

## TDCC Strength Ranking Top 30

| rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | abm_score | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | risk_label | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1217 | 愛之味 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | watch_only | 83.00 | 4.00 | 1.50 | 2.05 | 2.81 | 2.07 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 1233 | 天仁 | other | single_name_signal | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 95.00 | 0.00 | 1.44 | 0.04 | 0.71 | 1.66 | 10.00 | 218.87 | 10.00 | 24.00 | 0.00 | -0.13 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3 | 1304 | 台聚 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | price_leading_tdcc | overheated | 42.00 | 17.42 | 13.14 | 13.71 | 16.80 | 4.10 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 95.00 | 5.41 | 0.00 | 2.60 | 3.32 | 1.58 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 5 | 1325 | 恆大 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 77.00 | 3.89 | -7.31 | -3.55 | -0.84 | 1.24 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6 | 1410 | 南染 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | watch_only | 90.00 | 3.22 | -3.93 | 2.54 | 2.24 | 3.49 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 7 | 1423 | 利華 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 62.00 | -0.81 | -15.54 | -7.49 | -9.20 | 0.04 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8 | 1437 | 勤益控 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 3.32 | 6.32 | 4.57 | 4.64 | 1.93 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 9 | 1464 | 得力 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | watch_only | 80.00 | 8.91 | 2.80 | 6.12 | 5.95 | 2.97 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 10 | 1474 | 弘裕 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | price_leading_tdcc | watch_only | 91.00 | 12.38 | 9.13 | 10.05 | 10.70 | 6.88 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 11 | 1709 | 和益 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | price_leading_tdcc | watch_only | 56.00 | 12.59 | 14.49 | 10.85 | 10.77 | 2.26 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 12 | 1733 | 五鼎 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 92.00 | 3.29 | -3.08 | 1.20 | 1.57 | 0.68 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 1734 | 杏輝 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 92.00 | 5.00 | 7.18 | 4.65 | 4.99 | 1.51 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 14 | 1737 | 臺鹽 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 0.94 | 1.10 | 0.11 | 0.83 | 1.11 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 1784 | 訊聯 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 7.06 | 3.56 | 4.55 | 3.78 | 1.59 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 16 | 2008 | 高興昌 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 2.50 | 2.67 | -0.68 | 1.26 | 0.52 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 2017 | 官田鋼 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 6.00 | -3.25 | 1.57 | 2.60 | 1.29 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 2107 | 厚生 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 1.57 | -0.96 | 0.90 | 0.56 | 1.27 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 2114 | 鑫永銓 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 2.26 | -0.98 | 1.01 | 0.98 | 1.51 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 2204 | 中華 | EV/auto electronics | non_mainstream_watch | medium | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 95.00 | 3.82 | 1.78 | 2.58 | 2.47 | 1.20 | 10.00 | 12.95 | 10.00 | 1.00 | 0.00 | 2.95 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 21 | 2390 | 云辰 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | watch_only | 72.00 | 13.73 | 1.15 | 6.61 | 9.17 | 2.82 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 22 | 2516 | 新建 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | watch_only | 83.00 | 2.92 | 14.63 | 4.94 | 4.29 | 0.72 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 23 | 2528 | 皇普 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 85.00 | 9.09 | 7.29 | 1.11 | 3.65 | 0.78 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 2540 | 愛山林 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | watch_only | 80.00 | 1.51 | 0.37 | -3.22 | 0.48 | 0.57 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 25 | 2618 | 長榮航 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | strong_momentum | 70.00 | 0.11 | 15.70 | 2.38 | 6.06 | 0.62 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 26 | 2645 | 長榮航太 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | overheated_after_tdcc | overheated | 0.00 | 26.98 | 31.21 | 26.67 | 22.80 | 2.54 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | overheated | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 27 | 2718 | 全心投控 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | watch_only | 83.00 | 5.75 | 11.13 | 3.12 | 5.71 | 0.41 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 28 | 2867 | 三商壽 | finance | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 91.00 | 1.90 | 5.42 | -2.74 | 1.83 | 0.59 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 29 | 2886 | 兆豐金 | finance | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 91.00 | -1.41 | 8.08 | -0.68 | 1.88 | 0.47 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 30 | 2949 | 欣新網 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | early_breakout | 87.00 | 3.81 | 10.78 | 4.03 | 5.29 | 0.70 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |

## Pre-Move Accumulation / ABM Top 30

| abm_rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | abm_score | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | accumulation_label | tracking_priority | trigger_to_watch | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5523 | 豐謙 | traditional industries | mainstream_leader | high | 99.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | -0.16 | 0.21 | -0.05 | 0.80 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 5278 | 尚凡* | other electronics | mainstream_leader | high | 99.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | 4.00 | 2.65 | 1.79 | 0.83 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 3 | 1102 | 亞泥 | traditional industries | mainstream_leader | high | 98.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 1.96 | 6.11 | 1.14 | 3.13 | 0.85 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 4 | 3252 | 海灣 | semiconductor | mainstream_leader | high | 95.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 3.16 | -0.83 | 1.79 | 1.26 | 1.29 | 10.00 | 103.91 | 10.00 | 13.00 | 0.00 | 1.91 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 5 | 1402 | 遠東新 | traditional industries | mainstream_leader | high | 95.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 2.11 | 5.63 | 0.19 | 3.16 | 0.75 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 6 | 2211 | 長榮鋼 | traditional industries | mainstream_leader | high | 95.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 3.10 | 2.01 | 0.37 | 2.33 | 1.43 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 7 | 1442 | 名軒 | traditional industries | mainstream_leader | high | 95.00 | 185.00 | 5 | False | True | tdcc_leading_price | quiet_accumulation | 5.56 | 2.70 | 1.11 | 3.91 | 1.50 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 5234 | 達興材料 | semiconductor equipment/materials | mainstream_leader | high | 93.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 6.49 | 2.81 | 0.84 | 2.94 | 0.85 | 10.00 | 43.75 | 10.00 | 5.00 | 0.00 | 0.75 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 9 | 2377 | 微星 | other electronics | mainstream_leader | high | 92.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 8.75 | 2.14 | 2.57 | 3.91 | 0.50 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 1339 | 昭輝 | traditional industries | mainstream_leader | high | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 3.11 | 2.17 | 1.14 | 1.83 | 0.70 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 2812 | 台中銀 | finance | mainstream_leader | high | 90.00 | 155.00 | 2 | False | True | tdcc_leading_price | quiet_accumulation | 3.03 | 5.15 | 2.35 | 3.30 | 1.14 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 12 | 1737 | 臺鹽 | biotechnology | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 0.94 | 1.10 | 0.11 | 0.83 | 1.11 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 2107 | 厚生 | biotechnology | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 1.57 | -0.96 | 0.90 | 0.56 | 1.27 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 5533 | 皇鼎 | traditional industries | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 2.16 | 1.07 | 0.75 | 1.45 | 0.75 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 6527 | 明達醫 | biotechnology | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 1.11 | 3.11 | 2.05 | 1.24 | 0.95 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 16 | 2845 | 遠東銀 | finance | mainstream_leader | high | 100.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 1.15 | 4.78 | 0.87 | 1.78 | 0.54 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 1457 | 宜進 | traditional industries | mainstream_leader | high | 97.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 4.63 | -5.47 | 2.12 | 1.87 | 1.39 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 95.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 5.41 | 0.00 | 2.60 | 3.32 | 1.58 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 1615 | 大山 | other electronics | mainstream_leader | high | 95.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 2.26 | -2.90 | -0.68 | 0.76 | 0.94 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 8404 | 百和興業-KY | biotechnology | mainstream_leader | high | 95.00 | 185.00 | 5 | False | True | tdcc_leading_price | quiet_accumulation | 5.26 | -4.49 | 1.42 | 0.95 | 1.47 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 21 | 6417 | 韋僑 | other electronics | mainstream_leader | high | 93.00 | 155.00 | 2 | False | True | tdcc_leading_price | quiet_accumulation | 3.47 | -3.25 | 1.89 | 1.27 | 0.87 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 22 | 1733 | 五鼎 | biotechnology | mainstream_leader | high | 92.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 3.29 | -3.08 | 1.20 | 1.57 | 0.68 | 10.00 | 179.13 | 10.00 | 22.00 | 0.00 | 1.13 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 23 | 1906 | 寶隆 | traditional industries | mainstream_leader | high | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 3.15 | 0.00 | -0.68 | 1.19 | 0.59 | 10.00 | 358.45 | 10.00 | 44.00 | 0.00 | 2.45 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 2886 | 兆豐金 | finance | mainstream_leader | high | 91.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | -1.41 | 8.08 | -0.68 | 1.88 | 0.47 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 25 | 2801 | 彰銀 | finance | mainstream_leader | high | 91.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | -0.43 | 8.88 | 1.29 | 1.92 | 0.32 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 26 | 6115 | 鎰勝 | other electronics | mainstream_leader | high | 90.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 1.88 | -2.00 | -0.16 | 0.67 | 0.76 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 27 | 4534 | 慶騰 | other electronics | mainstream_leader | high | 88.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 15.49 | 8.37 | 2.31 | 5.93 | 0.93 | 10.00 | 367.53 | 10.00 | 45.00 | 0.00 | 1.53 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 28 | 2852 | 第一保 | finance | mainstream_leader | high | 88.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 2.09 | -3.59 | 1.22 | -0.48 | 0.64 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 29 | 5871 | 中租-KY | finance | mainstream_leader | high | 88.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 2.64 | -2.10 | 1.51 | -0.24 | 0.48 | 10.00 | 69.83 | 10.00 | 7.00 | 0.00 | -0.17 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 30 | 3033 | 威健 | semiconductor | mainstream_leader | high | 88.00 | 175.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 2.86 | 0.80 | 1.14 | 1.26 | 0.35 | 8.00 | 103.91 | 8.00 | 13.00 | 0.00 | 1.91 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |

## Theme Mainstream Summary

| theme | theme_mainstream_status | signal_count | leading_count | confirmed_count | late_or_overheated_count | divergence_count | avg_tdcc_strength_score | avg_abm_score | representative_codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other electronics | mainstream_leader | 405 | 31 | 2 | 25 | 45 | 151.78 | 55.73 | 8084/8047/6409/6199/6609 |
| traditional industries | mainstream_leader | 219 | 31 | 1 | 23 | 17 | 164.82 | 57.43 | 1217/1304/1323/1325/1474 |
| other | single_name_signal | 177 | 19 | 2 | 3 | 29 | 162.63 | 62.92 | 1233/4161/4406/4198/4155 |
| biotechnology | mainstream_leader | 108 | 15 | 1 | 6 | 8 | 155.97 | 59.04 | 1733/1734/1784/1737/2107 |
| semiconductor | mainstream_leader | 92 | 7 | 2 | 7 | 9 | 148.86 | 53.83 | 6104/3252/3011/3045/3266 |
| semiconductor equipment/materials | mainstream_leader | 29 | 4 | 0 | 1 | 2 | 150.69 | 61.93 | 5234/2417/8163/2365/2352 |
| consumer electronics | non_mainstream_watch | 28 | 0 | 0 | 6 | 0 | 140.36 | 46.57 | 6164/7402/4934/5392/2406 |
| finance | mainstream_leader | 27 | 7 | 0 | 0 | 6 | 177.96 | 73.11 | 2867/2886/2845/2880/2890 |
| networking | non_mainstream_watch | 12 | 1 | 0 | 3 | 1 | 152.92 | 53.25 | 3081/2345/3596/6142/3221 |
| EV/auto electronics | non_mainstream_watch | 10 | 1 | 0 | 1 | 0 | 132.00 | 45.60 | 2204/2231/2241/1563/2233 |
| passive components | mainstream_overheated | 5 | 0 | 0 | 0 | 1 | 150.00 | 29.20 | 3624/2375/6173/8042/2492 |
| PCB/CCL | non_mainstream_watch | 3 | 0 | 0 | 0 | 0 | 70.00 | 46.33 | 5439/2355/5464 |
| power discrete/diodes | mainstream_overheated | 3 | 0 | 0 | 3 | 0 | 185.00 | 2.33 | 8261/2481/5425 |

## TDCC Strength Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1217 | 愛之味 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1233 | 天仁 | other | single_name_signal | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1304 | 台聚 | traditional industries | mainstream_leader | 235.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1325 | 恆大 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1410 | 南染 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1423 | 利華 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1437 | 勤益控 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1464 | 得力 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1474 | 弘裕 | traditional industries | mainstream_leader | 235.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1709 | 和益 | traditional industries | mainstream_leader | 235.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1733 | 五鼎 | biotechnology | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1734 | 杏輝 | biotechnology | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1737 | 臺鹽 | biotechnology | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1784 | 訊聯 | biotechnology | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2017 | 官田鋼 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2107 | 厚生 | biotechnology | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2114 | 鑫永銓 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2204 | 中華 | EV/auto electronics | non_mainstream_watch | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2390 | 云辰 | other electronics | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2516 | 新建 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2528 | 皇普 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2540 | 愛山林 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2618 | 長榮航 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2645 | 長榮航太 | traditional industries | mainstream_leader | 235.00 | overheated_after_tdcc | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2718 | 全心投控 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2867 | 三商壽 | finance | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2886 | 兆豐金 | finance | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2949 | 欣新網 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |

## Pre-Move / ABM Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5523 | 豐謙 | traditional industries | mainstream_leader | 99.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5278 | 尚凡* | other electronics | mainstream_leader | 99.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1102 | 亞泥 | traditional industries | mainstream_leader | 98.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 3252 | 海灣 | semiconductor | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1402 | 遠東新 | traditional industries | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2211 | 長榮鋼 | traditional industries | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1442 | 名軒 | traditional industries | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5234 | 達興材料 | semiconductor equipment/materials | mainstream_leader | 93.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2377 | 微星 | other electronics | mainstream_leader | 92.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1339 | 昭輝 | traditional industries | mainstream_leader | 92.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2812 | 台中銀 | finance | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1737 | 臺鹽 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2107 | 厚生 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5533 | 皇鼎 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 6527 | 明達醫 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2845 | 遠東銀 | finance | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1457 | 宜進 | traditional industries | mainstream_leader | 97.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；避免爆量長上影 |
| 1615 | 大山 | other electronics | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 8404 | 百和興業-KY | biotechnology | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 6417 | 韋僑 | other electronics | mainstream_leader | 93.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1733 | 五鼎 | biotechnology | mainstream_leader | 92.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1906 | 寶隆 | traditional industries | mainstream_leader | 92.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2886 | 兆豐金 | finance | mainstream_leader | 91.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2801 | 彰銀 | finance | mainstream_leader | 91.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 6115 | 鎰勝 | other electronics | mainstream_leader | 90.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 4534 | 慶騰 | other electronics | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2852 | 第一保 | finance | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 5871 | 中租-KY | finance | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 3033 | 威健 | semiconductor | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |

## 主流潛伏吸籌名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5523 | 豐謙 | traditional industries | mainstream_leader | 99.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5278 | 尚凡* | other electronics | mainstream_leader | 99.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1102 | 亞泥 | traditional industries | mainstream_leader | 98.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 3252 | 海灣 | semiconductor | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1402 | 遠東新 | traditional industries | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2211 | 長榮鋼 | traditional industries | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1442 | 名軒 | traditional industries | mainstream_leader | 95.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5234 | 達興材料 | semiconductor equipment/materials | mainstream_leader | 93.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2377 | 微星 | other electronics | mainstream_leader | 92.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1339 | 昭輝 | traditional industries | mainstream_leader | 92.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2812 | 台中銀 | finance | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1737 | 臺鹽 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2107 | 厚生 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5533 | 皇鼎 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 6527 | 明達醫 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2845 | 遠東銀 | finance | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1457 | 宜進 | traditional industries | mainstream_leader | 97.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；避免爆量長上影 |
| 1615 | 大山 | other electronics | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 相對 benchmark 轉正；量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 8404 | 百和興業-KY | biotechnology | mainstream_leader | 95.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |

## 非主流但值得觀察名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2204 | 中華 | EV/auto electronics | non_mainstream_watch | 95.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 3596 | 智易 | networking | non_mainstream_watch | 85.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |

## 孤單訊號 / 非主流降權名單

目前沒有可用資料。

## 主流過熱風險名單

目前沒有可用資料。

## TDCC 背離 + 弱族群名單

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1103 | 嘉泥 | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1219 | 福壽 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4510 | 高鋒 | other | single_name_signal | 155.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4535 | 至興 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4538 | 大詠城 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4552 | 力達-KY | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4571 | 鈞興-KY | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4722 | 國精化 | other | single_name_signal | 165.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4737 | 華廣 | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5902 | 德記 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6805 | 富世達 | other | single_name_signal | 155.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6835 | 圓裕 | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6906 | 現觀科 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6918 | 愛派司 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6923 | 中台 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6952 | 大武山 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6965 | 中傑-KY | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6982 | 大井泵浦 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6988 | 威力暘-創 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7718 | 友鋮 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7792 | 安葆 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7827 | 漢康-KY創 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8341 | 日友 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8342 | 益張 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8908 | 欣雄 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9110 | 越南控-DR | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9136 | 巨騰-DR | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9906 | 欣巴巴 | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9940 | 信義 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Top Risk List

- price_leading_tdcc: 股價已先漲，TDCC 訊號可能偏晚。
- overheated_after_tdcc: 籌碼強但股價已過熱。
- tdcc_price_divergence: TDCC 增加但股價轉弱，需列為失效觀察。

## Top Risk List - price_leading_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1474 | 弘裕 | traditional industries | mainstream_leader | 235.00 | price_leading_tdcc | 9.13 | 10.05 | 10.70 | 6.88 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1709 | 和益 | traditional industries | mainstream_leader | 235.00 | price_leading_tdcc | 14.49 | 10.85 | 10.77 | 2.26 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1304 | 台聚 | traditional industries | mainstream_leader | 235.00 | price_leading_tdcc | 13.14 | 13.71 | 16.80 | 4.10 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8476 | 台境* | biotechnology | mainstream_leader | 225.00 | price_leading_tdcc | 56.23 | 11.73 | 13.58 | 0.51 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4414 | 如興 | other | single_name_signal | 215.00 | price_leading_tdcc | 9.35 | 10.22 | 9.67 | 1.98 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4924 | 欣厚-KY | other electronics | mainstream_leader | 215.00 | price_leading_tdcc | 10.71 | 22.74 | 8.81 | 1.41 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6831 | 邁科 | other | single_name_signal | 205.00 | price_leading_tdcc | 28.02 | 18.73 | 15.39 | 0.84 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5011 | 久陽 | other | single_name_signal | 205.00 | price_leading_tdcc | 25.00 | 12.64 | 11.76 | 0.37 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3015 | 全漢 | semiconductor | mainstream_leader | 195.00 | price_leading_tdcc | 8.45 | 10.98 | 9.23 | 1.11 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3402 | 漢科 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 6.16 | 10.70 | 8.75 | 1.36 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8444 | 綠河-KY | biotechnology | mainstream_leader | 195.00 | price_leading_tdcc | 5.66 | 17.98 | 2.13 | 0.09 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6133 | 金橋 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 4.03 | 11.25 | 10.34 | 7.39 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5302 | 太欣 | semiconductor | mainstream_leader | 195.00 | price_leading_tdcc | 26.01 | 12.33 | 14.51 | 1.50 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3349 | 寶德 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 23.94 | 20.92 | 18.77 | 2.80 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3004 | 豐達科 | traditional industries | mainstream_leader | 195.00 | price_leading_tdcc | 18.11 | 10.85 | 12.32 | 4.02 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3711 | 日月光投控 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | 15.01 | 10.58 | 9.73 | 1.48 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4743 | 合一 | biotechnology | mainstream_leader | 195.00 | price_leading_tdcc | 14.14 | 19.75 | 15.09 | 4.41 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1309 | 台達化 | traditional industries | mainstream_leader | 195.00 | price_leading_tdcc | -1.47 | 12.54 | 11.58 | 4.77 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6538 | 倉和 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | -0.37 | 18.72 | 14.63 | 2.42 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2345 | 智邦 | networking | non_mainstream_watch | 185.00 | price_leading_tdcc | 8.96 | 11.64 | 10.76 | 0.86 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |

## Top Risk List - overheated_after_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4707 | 磐亞 | traditional industries | mainstream_leader | 235.00 | overheated_after_tdcc | 60.19 | 47.33 | 41.39 | 2.40 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6409 | 旭隼 | other electronics | mainstream_leader | 235.00 | overheated_after_tdcc | 48.70 | 34.85 | 28.78 | 1.26 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2645 | 長榮航太 | traditional industries | mainstream_leader | 235.00 | overheated_after_tdcc | 31.21 | 26.67 | 22.80 | 2.54 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2634 | 漢翔 | traditional industries | mainstream_leader | 225.00 | overheated_after_tdcc | 28.89 | 26.44 | 20.87 | 3.06 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2305 | 全友 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 72.06 | 14.63 | 22.04 | 0.19 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8261 | 富鼎 | power discrete/diodes | mainstream_overheated | 195.00 | overheated_after_tdcc | 81.30 | 48.16 | 43.58 | 2.48 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1515 | 力山 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 66.01 | 61.48 | 49.02 | 3.53 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8033 | 雷虎 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 53.76 | 57.24 | 41.30 | 1.16 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 7402 | 邑錡 | consumer electronics | non_mainstream_watch | 195.00 | overheated_after_tdcc | 38.50 | 50.76 | 35.22 | 4.36 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8046 | 南電 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 34.97 | 34.90 | 23.10 | 0.70 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6164 | 華興 | consumer electronics | non_mainstream_watch | 195.00 | overheated_after_tdcc | 33.85 | 29.66 | 29.39 | 2.75 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6753 | 龍德造船 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 24.19 | 26.07 | 21.72 | 2.86 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1310 | 台苯 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 24.18 | 22.43 | 20.52 | 2.86 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1301 | 台塑 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 22.24 | 19.44 | 22.02 | 3.11 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6525 | 捷敏-KY | semiconductor | mainstream_leader | 185.00 | overheated_after_tdcc | 53.14 | 27.29 | 29.19 | 2.37 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3055 | 蔚華科 | other electronics | mainstream_leader | 185.00 | overheated_after_tdcc | 47.34 | 66.72 | 53.41 | 5.52 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2481 | 強茂 | power discrete/diodes | mainstream_overheated | 185.00 | overheated_after_tdcc | 29.78 | 28.70 | 23.21 | 0.28 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1710 | 東聯 | traditional industries | mainstream_leader | 185.00 | overheated_after_tdcc | 22.40 | 37.42 | 26.53 | 3.11 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1314 | 中石化 | traditional industries | mainstream_leader | 185.00 | overheated_after_tdcc | 19.76 | 26.31 | 22.24 | 5.94 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4989 | 榮科 | other electronics | mainstream_leader | 185.00 | overheated_after_tdcc | 19.59 | 28.56 | 26.12 | 4.78 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Top Risk List - tdcc_price_divergence Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2867 | 三商壽 | finance | mainstream_leader | 235.00 | tdcc_price_divergence | 5.42 | -2.74 | 1.83 | 0.59 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9946 | 三發地產 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | 17.40 | -4.08 | 4.41 | 0.39 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4538 | 大詠城 | other | single_name_signal | 235.00 | tdcc_price_divergence | 1.63 | -0.42 | 0.12 | 0.39 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5283 | 禾聯碩 | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | 1.32 | -1.78 | 0.69 | 0.50 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2540 | 愛山林 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | 0.37 | -3.22 | 0.48 | 0.57 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8437 | 大地-KY | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | -8.22 | -4.81 | -2.72 | 0.86 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1325 | 恆大 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | -7.31 | -3.55 | -0.84 | 1.24 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6570 | 維田 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | -6.92 | -1.09 | -0.56 | 0.85 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6965 | 中傑-KY | other | single_name_signal | 235.00 | tdcc_price_divergence | -4.65 | -5.56 | -2.45 | 0.69 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3705 | 永信 | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | -4.39 | -5.07 | -2.55 | 0.43 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7718 | 友鋮 | other | single_name_signal | 235.00 | tdcc_price_divergence | -4.09 | -1.71 | -1.29 | 0.81 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9110 | 越南控-DR | other | single_name_signal | 235.00 | tdcc_price_divergence | -3.03 | -9.25 | -8.11 | 0.18 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4552 | 力達-KY | other | single_name_signal | 235.00 | tdcc_price_divergence | -2.19 | -7.41 | -3.28 | 0.93 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1423 | 利華 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | -15.54 | -7.49 | -9.20 | 0.04 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3713 | 新晶投控 | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | -12.79 | -3.78 | -2.26 | 1.12 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8047 | 星雲 | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | -1.88 | -4.48 | -5.18 | 0.74 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6170 | 統振 | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | -1.69 | -0.57 | -0.19 | 0.96 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4535 | 至興 | other | single_name_signal | 235.00 | tdcc_price_divergence | -1.47 | -1.99 | -1.34 | 0.69 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8342 | 益張 | other | single_name_signal | 235.00 | tdcc_price_divergence | -0.56 | -1.61 | -0.49 | 0.05 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2520 | 冠德 | traditional industries | mainstream_leader | 225.00 | tdcc_price_divergence | 9.59 | -4.94 | 1.80 | 0.32 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Phase Distribution

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 798.0 | 71.38 |
| tdcc_leading_price | 116.0 | 10.38 |
| tdcc_price_divergence | 116.0 | 10.38 |
| price_leading_tdcc | 45.0 | 4.03 |
| overheated_after_tdcc | 33.0 | 2.95 |
| tdcc_price_confirmed | 8.0 | 0.72 |
| failed_after_tdcc | 2.0 | 0.18 |

## Consecutive Weeks x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 418.0 |
| 1 | overheated_after_tdcc | 12.0 |
| 1 | price_leading_tdcc | 14.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 156.0 |
| 2 | overheated_after_tdcc | 7.0 |
| 2 | price_leading_tdcc | 9.0 |
| 2 | tdcc_leading_price | 35.0 |
| 2 | tdcc_price_confirmed | 4.0 |
| 2 | tdcc_price_divergence | 31.0 |
| 3 | insufficient_price_context | 96.0 |
| 3 | overheated_after_tdcc | 9.0 |
| 3 | price_leading_tdcc | 13.0 |
| 3 | tdcc_leading_price | 22.0 |
| 3 | tdcc_price_confirmed | 1.0 |
| 3 | tdcc_price_divergence | 20.0 |
| 4 | insufficient_price_context | 43.0 |
| 4 | overheated_after_tdcc | 1.0 |
| 4 | price_leading_tdcc | 2.0 |
| 4 | tdcc_leading_price | 12.0 |
| 4 | tdcc_price_confirmed | 1.0 |
| 4 | tdcc_price_divergence | 19.0 |
| 5 | insufficient_price_context | 26.0 |
| 5 | price_leading_tdcc | 3.0 |
| 5 | tdcc_leading_price | 11.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 17.0 |
| 6 | insufficient_price_context | 14.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_leading_price | 5.0 |
| 6 | tdcc_price_divergence | 9.0 |
| 7 | insufficient_price_context | 45.0 |
| 7 | overheated_after_tdcc | 3.0 |
| 7 | price_leading_tdcc | 3.0 |
| 7 | tdcc_leading_price | 31.0 |
| 7 | tdcc_price_confirmed | 1.0 |
| 7 | tdcc_price_divergence | 20.0 |

## Mature Performance Summary

只使用 mature_dN=True 的資料。pending 不可視為正面或負面。

- phase-level mature sample 已可使用。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 93.0 | 2.52 | 0.24 | 81.0 | 2.66 | 0.62 | 27.0 | 6.21 | 1.98 | 15.57 | -8.75 |
| overheated_after_tdcc | 104.0 | 4.36 | 2.42 | 96.0 | 6.95 | 4.21 | 59.0 | 13.84 | 8.84 | 19.68 | -9.90 |
| price_leading_tdcc | 76.0 | 7.14 | 4.35 | 59.0 | 4.49 | 2.60 | 26.0 | 2.32 | -0.97 | 17.92 | -8.36 |
| tdcc_leading_price | 19.0 | -0.10 | 0.30 | 17.0 | 2.43 | -2.67 | 6.0 | -0.39 | -3.95 | 10.73 | -9.31 |
| tdcc_price_confirmed | 6.0 | -3.57 | -3.78 | 4.0 | -0.94 | -6.69 | 0.0 |  |  | 6.37 | -14.03 |
| tdcc_price_divergence | 9.0 | -3.54 | -4.26 | 7.0 | -1.49 | -4.62 | 1.0 | 5.57 | 3.50 | 10.05 | -12.95 |

## TDCC Weekly Increase and Consecutive Candidate Reports

- 精華版與完整版由 report-ready CSV/MD/PDF 產出。
- 精華版包含當週增幅、連續累積、當週增幅 x TDCC 短線延續 D+5/D+10、連續累積 x TDCC 短線延續 D+5/D+10，各最多前十名。
- 完整版使用相同四個清單，各最多列前五十名；不足五十就全列。

- tdcc_weekly_report_section_manifest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_report_section_manifest_latest.csv
- tdcc_weekly_report_section_manifest_csv_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_report_section_manifest_latest.csv
- tdcc_weekly_candidate_highlight_for_report_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv
- tdcc_weekly_candidate_highlight_for_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md
- tdcc_weekly_candidate_full_for_report_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_for_report_latest.csv
- tdcc_weekly_candidate_full_for_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_for_report_latest.md
- tdcc_weekly_candidate_highlight_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_latest.pdf
- tdcc_weekly_candidate_full_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_latest.pdf
- tdcc_weekly_candidate_highlight_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_candidate_highlight_latest.pdf
- tdcc_weekly_candidate_full_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_candidate_full_latest.pdf
- tdcc_weekly_candidate_highlight_delivery_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260703.pdf
- tdcc_weekly_candidate_full_delivery_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260703.pdf
- tdcc_weekly_candidate_highlight_delivery_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260703.pdf
- tdcc_weekly_candidate_full_delivery_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260703.pdf

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
