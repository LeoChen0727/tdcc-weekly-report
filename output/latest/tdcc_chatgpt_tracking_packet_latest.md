# TDCC CHATGPT TRACKING PACKET

## Metadata
- generated_at: 2026-07-14 09:49:22 Asia/Taipei
- main_price_date: 20260713
- latest_tdcc_signal_date: 20260709
- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md
- overall_mature_d5_count: 11553
- phase_mature_d5_count: 11553
- overall_mature_d10_count: 10420
- phase_mature_d10_count: 10420
- overall_mature_d20_count: 7121
- phase_mature_d20_count: 7121
- pending_count: 89
- insufficient_sample_count: 30
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 356
- theme_other_pct: 12.5
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
- theme_lookup_rows: 356
- theme_lookup_sources: {'config': 28, 'company_theme_mapping': 28, 'all_candidates': 451}
- theme_other_before: 63
- theme_other_after: 8
- theme_other_pct: 12.5
- sample_status: phase_samples_available
- relaxed_filter: False
- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution

## Mature Sample Status

- overall_mature_d5_count: 11553
- phase_mature_d5_count: 11553
- overall_mature_d10_count: 10420
- phase_mature_d10_count: 10420
- overall_mature_d20_count: 7121
- phase_mature_d20_count: 7121
- pending_count: 89
- insufficient_sample_count: 30
- phase_mature_join_quality: ok
- sample_status: phase_samples_available

- phase-level mature sample 已可使用。

## TDCC Strength Ranking Top 30

| rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | abm_score | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | risk_label | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1102 | 亞泥 | other | single_name_signal | medium | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 96.00 | -1.92 | 3.78 | 0.84 | -0.10 | 0.62 | 10.00 | 27.86 | 10.00 | 3.00 | 0.00 | 4.86 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 1217 | 愛之味 | other | single_name_signal | medium | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 92.00 | 0.00 | 1.22 | 3.16 | 0.83 | 0.67 | 10.00 | 27.86 | 10.00 | 3.00 | 0.00 | 4.86 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 3 | 1233 | 天仁 | other | single_name_signal | medium | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 89.00 | -1.59 | 1.27 | 1.59 | -0.67 | 0.80 | 10.00 | 27.86 | 10.00 | 3.00 | 0.00 | 4.86 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 4 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 92.00 | 3.29 | 4.35 | 4.98 | 2.50 | 0.46 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 5 | 1325 | 恆大 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_price_divergence | quiet_accumulation | 72.00 | -0.20 | -6.14 | -1.22 | -3.13 | 0.38 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6 | 1339 | 昭輝 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 1.13 | 2.99 | 3.30 | 1.11 | 0.35 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 7 | 1402 | 遠東新 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_price_divergence | quiet_accumulation | 95.00 | -3.35 | -0.72 | -2.07 | -3.22 | 1.06 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8 | 1410 | 南染 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 90.00 | -0.19 | 5.00 | 8.22 | 3.77 | 1.53 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 9 | 1442 | 名軒 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 90.00 | 1.07 | 1.61 | 5.40 | 2.66 | 0.40 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 10 | 1457 | 宜進 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 86.00 | -1.74 | -3.41 | 1.60 | -1.24 | 0.58 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 1464 | 得力 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 92.00 | -2.76 | 1.93 | 5.38 | 0.86 | 0.46 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 12 | 1709 | 和益 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | price_leading_tdcc | strong_momentum | 63.00 | 4.27 | 15.37 | 15.97 | 9.91 | 1.53 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 13 | 1734 | 杏輝 | biotechnology | mainstream_follow_through | medium | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 0.61 | 5.75 | 4.27 | 2.07 | 0.51 | 10.00 | 23.26 | 10.00 | 2.00 | 0.00 | 3.26 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 14 | 1784 | 訊聯 | biotechnology | mainstream_follow_through | medium | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 2.98 | 4.22 | 4.99 | 1.80 | 1.06 | 10.00 | 23.26 | 10.00 | 2.00 | 0.00 | 3.26 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 15 | 1906 | 寶隆 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 0.89 | 1.35 | 3.29 | 0.29 | 0.22 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 16 | 2008 | 高興昌 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_price_divergence | quiet_accumulation | 96.00 | -3.08 | 1.36 | -3.14 | -2.04 | 0.41 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 17 | 2107 | 厚生 | biotechnology | mainstream_follow_through | medium | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 96.00 | -0.58 | -0.97 | 0.79 | -0.17 | 0.56 | 10.00 | 23.26 | 10.00 | 2.00 | 0.00 | 3.26 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 2114 | 鑫永銓 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 0.34 | 1.24 | 2.06 | 0.35 | 0.49 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 2204 | 中華 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 92.00 | 1.06 | 1.97 | 4.84 | 1.69 | 0.61 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 20 | 2377 | 微星 | semiconductor equipment/materials | emerging_theme | medium | 195.00 | 3 | True | True | price_leading_tdcc | quiet_accumulation | 100.00 | 1.40 | 9.85 | 10.56 | 4.54 | 1.19 | 10.00 | 18.80 | 10.00 | 2.00 | 0.00 | 5.80 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 21 | 2516 | 新建 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 96.00 | -2.15 | 4.20 | 0.86 | -0.35 | 0.66 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 22 | 2618 | 長榮航 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_price_divergence | quiet_accumulation | 80.00 | -9.79 | 6.31 | -9.06 | -6.16 | 1.05 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 23 | 2645 | 長榮航太 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | overheated_after_tdcc | overheated | 0.00 | 21.83 | 42.43 | 40.28 | 27.10 | 3.29 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | overheated | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 24 | 2701 | 萬企 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 1.41 | 3.85 | 3.83 | 1.69 | 0.87 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 25 | 2718 | 全心投控 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 96.00 | -5.93 | 2.82 | 1.58 | -1.98 | 0.28 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 26 | 2801 | 彰銀 | finance | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 3.00 | 7.61 | 4.29 | 3.43 | 0.64 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 27 | 2812 | 台中銀 | finance | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 85.00 | 2.23 | 6.19 | 4.69 | 3.03 | 0.49 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 28 | 2845 | 遠東銀 | finance | mainstream_leader | high | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 1.54 | 3.12 | 2.71 | 1.11 | 0.25 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 29 | 2867 | 三商壽 | finance | mainstream_leader | high | 195.00 | 3 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 4.24 | 8.58 | 5.09 | 3.72 | 0.77 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 30 | 2949 | 欣新網 | traditional industries | mainstream_leader | high | 195.00 | 3 | True | True | overheated_after_tdcc | overheated | 0.00 | 19.71 | 29.32 | 26.43 | 20.03 | 5.54 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | overheated | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Pre-Move Accumulation / ABM Top 30

| abm_rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | abm_score | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | accumulation_label | tracking_priority | trigger_to_watch | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2107 | 厚生 | biotechnology | mainstream_follow_through | medium | 96.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -0.58 | -0.97 | 0.79 | -0.17 | 0.56 | 10.00 | 23.26 | 10.00 | 2.00 | 0.00 | 3.26 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 2516 | 新建 | traditional industries | mainstream_leader | high | 96.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -2.15 | 4.20 | 0.86 | -0.35 | 0.66 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 3 | 2718 | 全心投控 | traditional industries | mainstream_leader | high | 96.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -5.93 | 2.82 | 1.58 | -1.98 | 0.28 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 4 | 2114 | 鑫永銓 | traditional industries | mainstream_leader | high | 100.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 0.34 | 1.24 | 2.06 | 0.35 | 0.49 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 5 | 2845 | 遠東銀 | finance | mainstream_leader | high | 100.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 1.54 | 3.12 | 2.71 | 1.11 | 0.25 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 6 | 3033 | 威健 | semiconductor | mainstream_follow_through | medium | 81.00 | 85.00 | 3 | False | True | tdcc_leading_price | quiet_accumulation | -1.59 | -1.20 | 2.66 | -0.16 | 0.50 | 2.00 | 22.10 | 2.00 | 2.00 | 0.00 | 2.10 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 7 | 6609 | 瀧澤科 | other electronics | mainstream_leader | high | 96.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -5.01 | -7.44 | 1.29 | -2.45 | 0.45 | 10.00 | 52.95 | 10.00 | 5.00 | 0.00 | 2.95 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 5324 | 士開 | other electronics | mainstream_leader | high | 88.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -1.63 | 0.00 | 2.96 | -0.66 | 0.46 | 10.00 | 52.95 | 10.00 | 5.00 | 0.00 | 2.95 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 9 | 3596 | 智易 | other electronics | mainstream_leader | high | 87.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 1.31 | 5.15 | 1.43 | 2.00 | 0.45 | 10.00 | 52.95 | 10.00 | 5.00 | 0.00 | 2.95 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 1457 | 宜進 | traditional industries | mainstream_leader | high | 86.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -1.74 | -3.41 | 1.60 | -1.24 | 0.58 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 3023 | 信邦 | other electronics | mainstream_leader | high | 84.00 | 165.00 | 3 | False | True | tdcc_leading_price | quiet_accumulation | -1.21 | 6.36 | 2.10 | 1.18 | 0.83 | 10.00 | 52.95 | 10.00 | 5.00 | 0.00 | 2.95 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 12 | 1102 | 亞泥 | other | single_name_signal | medium | 96.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -1.92 | 3.78 | 0.84 | -0.10 | 0.62 | 10.00 | 27.86 | 10.00 | 3.00 | 0.00 | 4.86 | prime_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 1233 | 天仁 | other | single_name_signal | medium | 89.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -1.59 | 1.27 | 1.59 | -0.67 | 0.80 | 10.00 | 27.86 | 10.00 | 3.00 | 0.00 | 4.86 | prime_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 5234 | 達興材料 | semiconductor equipment/materials | emerging_theme | medium | 74.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -4.28 | -0.91 | 1.04 | -2.35 | 0.62 | 10.00 | 18.80 | 10.00 | 2.00 | 0.00 | 5.80 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 1722 | 台肥 | biotechnology | mainstream_follow_through | medium | 68.00 | 135.00 | 3 | False | False | tdcc_leading_price | watch_only | -1.14 | 0.53 | 1.32 | -1.05 | 0.67 | 10.00 | 23.26 | 10.00 | 2.00 | 0.00 | 3.26 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 16 | 3293 | 鈊象 | semiconductor | mainstream_follow_through | medium | 62.00 | 135.00 | 3 | False | False | tdcc_leading_price | watch_only | -7.00 | -6.88 | 1.27 | -3.61 | 0.51 | 10.00 | 22.10 | 10.00 | 2.00 | 0.00 | 2.10 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 2852 | 第一保 | finance | mainstream_leader | high | 68.00 | 140.00 | 3 | False | False | tdcc_leading_price | watch_only | 0.56 | -3.25 | 2.70 | -0.04 | 0.31 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 2211 | 長榮鋼 | traditional industries | mainstream_leader | high | 62.00 | 140.00 | 3 | False | False | tdcc_leading_price | watch_only | -0.52 | 2.81 | 2.48 | 0.17 | 0.57 | 10.00 | 58.33 | 10.00 | 6.00 | 0.00 | 5.33 | watch_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 5871 | 中租-KY | finance | mainstream_leader | high | 61.00 | 130.00 | 3 | False | False | tdcc_leading_price | watch_only | -0.87 | -4.18 | 1.08 | -1.40 | 0.61 | 10.00 | 33.43 | 10.00 | 3.00 | 0.00 | 3.43 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |

## Theme Mainstream Summary

| theme | theme_mainstream_status | signal_count | leading_count | confirmed_count | late_or_overheated_count | divergence_count | avg_tdcc_strength_score | avg_abm_score | representative_codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| traditional industries | mainstream_leader | 24 | 5 | 0 | 3 | 5 | 183.33 | 78.58 | 1323/1325/1339/1402/1410 |
| other electronics | mainstream_leader | 13 | 5 | 0 | 0 | 3 | 173.85 | 81.08 | 3541/5278/4968/3713/3596 |
| other | single_name_signal | 8 | 2 | 0 | 1 | 0 | 178.75 | 75.75 | 1102/1217/1233/4119/4155 |
| biotechnology | mainstream_follow_through | 7 | 2 | 0 | 0 | 0 | 177.86 | 89.14 | 1734/2107/1784/6527/1733 |
| finance | mainstream_leader | 6 | 3 | 0 | 0 | 0 | 175.00 | 84.00 | 2801/2812/2845/2867/2852 |
| semiconductor | mainstream_follow_through | 4 | 2 | 0 | 0 | 1 | 120.00 | 64.75 | 3293/3078/3092/3033 |
| semiconductor equipment/materials | emerging_theme | 2 | 1 | 0 | 1 | 0 | 195.00 | 87.00 | 2377/5234 |

## TDCC Strength Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1102 | 亞泥 | other | single_name_signal | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1217 | 愛之味 | other | single_name_signal | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1233 | 天仁 | other | single_name_signal | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1325 | 恆大 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1339 | 昭輝 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1402 | 遠東新 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1410 | 南染 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1442 | 名軒 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1457 | 宜進 | traditional industries | mainstream_leader | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1464 | 得力 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1709 | 和益 | traditional industries | mainstream_leader | 195.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1734 | 杏輝 | biotechnology | mainstream_follow_through | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1784 | 訊聯 | biotechnology | mainstream_follow_through | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1906 | 寶隆 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2107 | 厚生 | biotechnology | mainstream_follow_through | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2114 | 鑫永銓 | traditional industries | mainstream_leader | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2204 | 中華 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2377 | 微星 | semiconductor equipment/materials | emerging_theme | 195.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2516 | 新建 | traditional industries | mainstream_leader | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2618 | 長榮航 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2645 | 長榮航太 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2701 | 萬企 | traditional industries | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2718 | 全心投控 | traditional industries | mainstream_leader | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2801 | 彰銀 | finance | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2812 | 台中銀 | finance | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2845 | 遠東銀 | finance | mainstream_leader | 195.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2867 | 三商壽 | finance | mainstream_leader | 195.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2949 | 欣新網 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Pre-Move / ABM Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2107 | 厚生 | biotechnology | mainstream_follow_through | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2516 | 新建 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2718 | 全心投控 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2114 | 鑫永銓 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2845 | 遠東銀 | finance | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 3033 | 威健 | semiconductor | mainstream_follow_through | 81.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 6609 | 瀧澤科 | other electronics | mainstream_leader | 96.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 5324 | 士開 | other electronics | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 3596 | 智易 | other electronics | mainstream_leader | 87.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1457 | 宜進 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3023 | 信邦 | other electronics | mainstream_leader | 84.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1102 | 亞泥 | other | single_name_signal | 96.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 1233 | 天仁 | other | single_name_signal | 89.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 5234 | 達興材料 | semiconductor equipment/materials | emerging_theme | 74.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 1722 | 台肥 | biotechnology | mainstream_follow_through | 68.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 3293 | 鈊象 | semiconductor | mainstream_follow_through | 62.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2852 | 第一保 | finance | mainstream_leader | 68.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2211 | 長榮鋼 | traditional industries | mainstream_leader | 62.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 5871 | 中租-KY | finance | mainstream_leader | 61.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |

## 主流潛伏吸籌名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2107 | 厚生 | biotechnology | mainstream_follow_through | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2516 | 新建 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2718 | 全心投控 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2114 | 鑫永銓 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2845 | 遠東銀 | finance | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 3033 | 威健 | semiconductor | mainstream_follow_through | 81.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 6609 | 瀧澤科 | other electronics | mainstream_leader | 96.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 5324 | 士開 | other electronics | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 3596 | 智易 | other electronics | mainstream_leader | 87.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1457 | 宜進 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3023 | 信邦 | other electronics | mainstream_leader | 84.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 5234 | 達興材料 | semiconductor equipment/materials | emerging_theme | 74.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 1722 | 台肥 | biotechnology | mainstream_follow_through | 68.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 3293 | 鈊象 | semiconductor | mainstream_follow_through | 62.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2852 | 第一保 | finance | mainstream_leader | 68.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2211 | 長榮鋼 | traditional industries | mainstream_leader | 62.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 5871 | 中租-KY | finance | mainstream_leader | 61.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |

## 非主流但值得觀察名單

目前沒有可用資料。

## 孤單訊號 / 非主流降權名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1102 | 亞泥 | other | single_name_signal | 96.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 1233 | 天仁 | other | single_name_signal | 89.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流過熱風險名單

目前沒有可用資料。

## TDCC 背離 + 弱族群名單

目前沒有可用資料。

## Top Risk List

- price_leading_tdcc: 股價已先漲，TDCC 訊號可能偏晚。
- overheated_after_tdcc: 籌碼強但股價已過熱。
- tdcc_price_divergence: TDCC 增加但股價轉弱，需列為失效觀察。

## Top Risk List - price_leading_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2377 | 微星 | semiconductor equipment/materials | emerging_theme | 195.00 | price_leading_tdcc | 9.85 | 10.56 | 4.54 | 1.19 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4198 | 欣大健康 | other | single_name_signal | 195.00 | price_leading_tdcc | 25.59 | 16.31 | 15.62 | 2.74 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1709 | 和益 | traditional industries | mainstream_leader | 195.00 | price_leading_tdcc | 15.37 | 15.97 | 9.91 | 1.53 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |

## Top Risk List - overheated_after_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2645 | 長榮航太 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 42.43 | 40.28 | 27.10 | 3.29 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2949 | 欣新網 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 29.32 | 26.43 | 20.03 | 5.54 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Top Risk List - tdcc_price_divergence Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2618 | 長榮航 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | 6.31 | -9.06 | -6.16 | 1.05 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4968 | 立積 | other electronics | mainstream_leader | 195.00 | tdcc_price_divergence | 5.19 | -2.75 | -1.48 | 0.64 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | 1.36 | -3.14 | -2.04 | 0.41 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1325 | 恆大 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | -6.14 | -1.22 | -3.13 | 0.38 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1402 | 遠東新 | traditional industries | mainstream_leader | 195.00 | tdcc_price_divergence | -0.72 | -2.07 | -3.22 | 1.06 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6283 | 淳安 | other electronics | mainstream_leader | 165.00 | tdcc_price_divergence | -4.92 | -2.78 | -2.09 | 0.28 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2540 | 愛山林 | traditional industries | mainstream_leader | 140.00 | tdcc_price_divergence | -4.52 | -0.64 | -1.42 | 0.39 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3092 | 鴻碩 | semiconductor | mainstream_follow_through | 130.00 | tdcc_price_divergence | 1.05 | -3.94 | -6.02 | 0.46 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Phase Distribution

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 30.0 | 46.88 |
| tdcc_leading_price | 20.0 | 31.25 |
| tdcc_price_divergence | 8.0 | 12.50 |
| price_leading_tdcc | 3.0 | 4.69 |
| overheated_after_tdcc | 2.0 | 3.12 |
| failed_after_tdcc | 1.0 | 1.56 |

## Consecutive Weeks x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 2 | insufficient_price_context | 2.0 |
| 3 | failed_after_tdcc | 1.0 |
| 3 | insufficient_price_context | 28.0 |
| 3 | overheated_after_tdcc | 2.0 |
| 3 | price_leading_tdcc | 3.0 |
| 3 | tdcc_leading_price | 20.0 |
| 3 | tdcc_price_divergence | 8.0 |

## Mature Performance Summary

只使用 mature_dN=True 的資料。pending 不可視為正面或負面。

- phase-level mature sample 已可使用。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 31.0 | -0.15 | -1.05 | 24.0 | 2.09 | -2.34 | 21.0 | 0.04 | -6.14 | 8.50 | -5.23 |
| insufficient_price_context | 7805.0 | 0.67 | -0.84 | 7280.0 | 1.79 | -0.50 | 4647.0 | 4.02 | -1.42 | 9.11 | -5.52 |
| overheated_after_tdcc | 436.0 | 2.27 | 1.90 | 369.0 | 7.39 | 4.68 | 268.0 | 13.96 | 8.96 | 19.96 | -9.53 |
| price_leading_tdcc | 596.0 | 2.99 | 0.83 | 508.0 | 4.73 | 1.79 | 276.0 | 7.36 | 1.01 | 16.83 | -6.63 |
| tdcc_leading_price | 1191.0 | 0.16 | 0.01 | 988.0 | 1.33 | -2.44 | 867.0 | 1.63 | -3.56 | 6.30 | -4.48 |
| tdcc_price_confirmed | 98.0 | 0.35 | 0.24 | 87.0 | 0.57 | -3.39 | 72.0 | 1.54 | -3.88 | 9.61 | -6.98 |
| tdcc_price_divergence | 1396.0 | 0.00 | -0.34 | 1164.0 | 1.37 | -2.96 | 970.0 | 1.94 | -3.99 | 6.87 | -4.41 |

## TDCC Weekly Increase and Consecutive Candidate Reports

- Highlight and full TDCC weekly candidate reports are generated from report-ready CSV/MD/PDF artifacts.
- The highlight report includes weekly increase leaders, consecutive accumulation leaders, and TDCC candidates that intersect with daily model signals.
- The full report keeps the broad weekly increase and consecutive accumulation tables, while model-cross rows are limited to the TDCC short-term continuation model.

- tdcc_weekly_increase_ranking_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_increase_ranking_latest.csv
- tdcc_weekly_increase_ranking_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_increase_ranking_latest.md
- tdcc_consecutive_accumulation_ranking_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_consecutive_accumulation_ranking_latest.csv
- tdcc_consecutive_accumulation_ranking_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_consecutive_accumulation_ranking_latest.md
- tdcc_weekly_model_cross_summary_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_model_cross_summary_latest.csv
- tdcc_weekly_model_cross_summary_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_model_cross_summary_latest.md
- tdcc_weekly_candidate_highlight_for_report_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv
- tdcc_weekly_candidate_highlight_for_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md
- tdcc_weekly_candidate_full_for_report_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_for_report_latest.csv
- tdcc_weekly_candidate_full_for_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_for_report_latest.md
- tdcc_weekly_candidate_highlight_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_latest.pdf
- tdcc_weekly_candidate_full_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_latest.pdf
- tdcc_weekly_candidate_highlight_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_candidate_highlight_latest.pdf
- tdcc_weekly_candidate_full_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_candidate_full_latest.pdf

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
