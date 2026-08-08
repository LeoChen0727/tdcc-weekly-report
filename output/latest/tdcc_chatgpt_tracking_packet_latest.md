# TDCC CHATGPT TRACKING PACKET

## Metadata
- generated_at: 2026-08-08 15:53:29 Asia/Taipei
- main_price_date: 20260805
- latest_tdcc_signal_date: 20260807
- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md
- overall_mature_d5_count: 492
- phase_mature_d5_count: 491
- overall_mature_d10_count: 434
- phase_mature_d10_count: 433
- overall_mature_d20_count: 351
- phase_mature_d20_count: 350
- pending_count: 119
- insufficient_sample_count: 886
- ranking_quality: complete
- phase_mature_join_quality: D+5: overall=492, phase=491; D+10: overall=434, phase=433; D+20: overall=351, phase=350
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 300
- theme_other_pct: 15.37
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
- phase_mature_join_quality: D+5: overall=492, phase=491; D+10: overall=434, phase=433; D+20: overall=351, phase=350
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 300
- theme_lookup_sources: {'config': 28, 'company_theme_mapping': 28, 'all_candidates': 327}
- theme_other_before: 1159
- theme_other_after: 181
- theme_other_pct: 15.37
- sample_status: phase_samples_available
- relaxed_filter: False
- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution

## Mature Sample Status

- overall_mature_d5_count: 492
- phase_mature_d5_count: 491
- overall_mature_d10_count: 434
- phase_mature_d10_count: 433
- overall_mature_d20_count: 351
- phase_mature_d20_count: 350
- pending_count: 119
- insufficient_sample_count: 886
- phase_mature_join_quality: D+5: overall=492, phase=491; D+10: overall=434, phase=433; D+20: overall=351, phase=350
- sample_status: phase_samples_available

- phase-level mature sample 已可使用。

## TDCC Strength Ranking Top 30

| rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | abm_score | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | risk_label | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 525.00 | 36 | True | True | tdcc_price_divergence | quiet_accumulation | 96.00 | 1.02 | -2.70 | -0.02 | -0.56 | 0.50 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2 | 7718 | 友鋮 | other | single_name_signal | high | 395.00 | 26 | False | True | insufficient_price_context | quiet_accumulation | 70.00 |  |  |  |  |  | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 3 | 1233 | 天仁 | other | single_name_signal | high | 315.00 | 15 | True | True | tdcc_price_divergence | quiet_accumulation | 100.00 | -0.69 | 3.42 | -0.89 | 0.02 | 1.20 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4 | 2321 | 東訊 | other electronics | mainstream_leader | high | 305.00 | 14 | True | True | tdcc_price_divergence | watch_only | 65.00 | 1.35 | 7.91 | -0.84 | 1.04 | 0.45 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5 | 2516 | 新建 | traditional industries | mainstream_leader | high | 305.00 | 14 | True | True | tdcc_price_divergence | quiet_accumulation | 96.00 | -0.36 | 0.73 | -0.59 | -0.72 | 0.45 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6 | 2618 | 長榮航 | traditional industries | mainstream_leader | high | 305.00 | 14 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 3.59 | 8.53 | 6.35 | 3.06 | 0.40 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 7 | 2867 | 三商壽 | finance | mainstream_leader | high | 305.00 | 14 | True | True | insufficient_price_context | watch_only | 86.00 | 1.98 | 10.27 | 6.90 | 4.85 | 0.83 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 8 | 4406 | 新昕纖 | other | single_name_signal | high | 305.00 | 14 | True | True | insufficient_price_context | watch_only | 80.00 | -0.50 | 0.40 | 3.40 | 0.33 | 0.11 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 9 | 5523 | 豐謙 | traditional industries | mainstream_leader | high | 305.00 | 14 | True | True | tdcc_leading_price | quiet_accumulation | 96.00 | 0.33 | -0.16 | 2.73 | -0.05 | 0.30 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 6527 | 明達醫 | biotechnology | mainstream_leader | high | 305.00 | 14 | True | True | price_leading_tdcc | quiet_accumulation | 100.00 | 13.68 | 3.56 | 12.62 | 7.42 | 2.40 | 10.00 | 46.78 | 10.00 | 6.00 | 0.00 | 0.78 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 11 | 6965 | 中傑-KY | other | single_name_signal | high | 305.00 | 14 | True | True | tdcc_price_divergence | quiet_accumulation | 89.00 | -0.26 | -3.28 | -2.31 | -2.09 | 0.83 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 12 | 7760 | 享溫馨 | other | single_name_signal | high | 305.00 | 14 | True | True | tdcc_price_divergence | quiet_accumulation | 91.00 | -1.03 | -5.48 | -3.24 | -1.87 | 1.25 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 13 | 8401 | 白紗科 | biotechnology | mainstream_leader | high | 305.00 | 14 | True | True | tdcc_leading_price | quiet_accumulation | 86.00 | 0.89 | -1.09 | 1.16 | -0.53 | 0.28 | 10.00 | 46.78 | 10.00 | 6.00 | 0.00 | 0.78 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 6418 | 詠昇 | other electronics | mainstream_leader | high | 295.00 | 13 | True | True | insufficient_price_context | quiet_accumulation | 80.00 | 13.75 | -3.19 | 8.53 | 3.13 | 0.70 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 15 | 4119 | 旭富 | other | single_name_signal | high | 285.00 | 12 | True | True | tdcc_price_divergence | quiet_accumulation | 77.00 | 1.35 | 8.72 | -0.54 | 1.19 | 0.53 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 16 | 6170 | 統振 | other electronics | mainstream_leader | high | 285.00 | 12 | True | True | tdcc_leading_price | quiet_accumulation | 86.00 | -0.22 | -3.55 | 0.78 | -1.09 | 0.22 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 8930 | 青鋼 | other | single_name_signal | high | 285.00 | 12 | True | True | tdcc_leading_price | watch_only | 76.00 | 3.36 | 1.48 | 1.29 | -0.31 | 0.37 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 2511 | 太子 | traditional industries | mainstream_leader | high | 275.00 | 11 | True | True | tdcc_price_divergence | quiet_accumulation | 88.00 | 0.97 | -2.47 | -1.99 | -2.12 | 0.78 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 19 | 4737 | 華廣 | other | single_name_signal | high | 275.00 | 11 | True | True | tdcc_price_divergence | watch_only | 50.00 | -3.91 | -5.26 | -2.05 | -4.94 | 0.50 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 20 | 9906 | 欣巴巴 | other | single_name_signal | high | 275.00 | 11 | True | True | tdcc_price_divergence | quiet_accumulation | 96.00 | 2.63 | -4.88 | -2.39 | -2.45 | 0.51 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 21 | 1709 | 和益 | biotechnology | mainstream_leader | high | 265.00 | 13 | False | True | insufficient_price_context | quiet_accumulation | 70.00 |  |  |  |  |  | 10.00 | 46.78 | 10.00 | 6.00 | 0.00 | 0.78 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 22 | 2892 | 第一金 | finance | mainstream_leader | high | 265.00 | 10 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 0.00 | 4.11 | 4.43 | 2.53 | 1.21 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 23 | 5880 | 合庫金 | finance | mainstream_leader | high | 265.00 | 10 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | -3.33 | 3.98 | 2.43 | 0.68 | 1.03 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 6194 | 育富 | other electronics | mainstream_leader | high | 265.00 | 10 | True | True | tdcc_leading_price | quiet_accumulation | 89.00 | 1.54 | -7.05 | 1.07 | -1.67 | 0.98 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 25 | 3356 | 奇偶 | other electronics | mainstream_leader | high | 255.00 | 9 | True | True | tdcc_price_divergence | watch_only | 75.00 | 3.89 | -6.34 | -2.80 | -2.70 | 0.96 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 26 | 3499 | 環天科 | other electronics | mainstream_leader | high | 255.00 | 9 | True | True | tdcc_price_divergence | quiet_accumulation | 70.00 | 4.84 | -12.16 | -2.56 | -4.62 | 0.45 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 27 | 3666 | 光耀 | other electronics | mainstream_leader | high | 255.00 | 9 | True | True | insufficient_price_context | quiet_accumulation | 90.00 | 0.40 | -0.20 | 3.09 | 0.23 | 0.34 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 28 | 3712 | 永崴投控 | other electronics | mainstream_leader | high | 255.00 | 9 | True | True | price_leading_tdcc | strong_momentum | 65.00 | 23.78 | 15.67 | 11.10 | 14.84 | 1.02 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 29 | 6128 | 上福 | other electronics | mainstream_leader | high | 255.00 | 9 | True | True | tdcc_price_divergence | quiet_accumulation | 89.00 | 1.51 | -0.49 | -0.75 | -0.51 | 0.82 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 30 | 6461 | 益得 | other electronics | mainstream_leader | high | 255.00 | 9 | True | True | insufficient_price_context | quiet_accumulation | 82.00 | 1.96 | -5.17 | 1.01 | -0.51 | 0.40 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |

## Pre-Move Accumulation / ABM Top 30

| abm_rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | abm_score | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | accumulation_label | tracking_priority | trigger_to_watch | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1525 | 江申 | other electronics | mainstream_leader | high | 97.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 1.18 | 2.84 | 2.86 | 2.01 | 1.40 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 2008 | 高興昌 | traditional industries | mainstream_leader | high | 97.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -0.48 | 4.40 | 0.32 | 0.55 | 1.07 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 3 | 5523 | 豐謙 | traditional industries | mainstream_leader | high | 96.00 | 305.00 | 14 | True | True | tdcc_leading_price | quiet_accumulation | 0.33 | -0.16 | 2.73 | -0.05 | 0.30 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 4 | 1558 | 伸興 | other electronics | mainstream_leader | high | 96.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -0.44 | -0.87 | 2.48 | -0.52 | 0.52 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 5 | 2646 | 星宇航空 | traditional industries | mainstream_leader | high | 96.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | -1.86 | -0.24 | 0.01 | -1.10 | 0.64 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 6 | 6504 | 南六 | biotechnology | mainstream_leader | high | 91.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | -2.53 | 6.48 | 1.00 | 1.64 | 0.74 | 10.00 | 46.78 | 10.00 | 6.00 | 0.00 | 0.78 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 7 | 4972 | 湯石照明 | other electronics | mainstream_leader | high | 91.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | -2.65 | 1.11 | -1.00 | 0.86 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 2603 | 長榮 | traditional industries | mainstream_leader | high | 90.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 1.49 | 4.08 | 0.72 | 1.28 | 0.42 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 9 | 5880 | 合庫金 | finance | mainstream_leader | high | 100.00 | 265.00 | 10 | True | True | tdcc_leading_price | quiet_accumulation | -3.33 | 3.98 | 2.43 | 0.68 | 1.03 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 1463 | 強盛新 | traditional industries | mainstream_leader | high | 100.00 | 245.00 | 8 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | 0.56 | 0.76 | 0.52 | 0.34 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 6194 | 育富 | other electronics | mainstream_leader | high | 89.00 | 265.00 | 10 | True | True | tdcc_leading_price | quiet_accumulation | 1.54 | -7.05 | 1.07 | -1.67 | 0.98 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 12 | 2704 | 國賓 | traditional industries | mainstream_leader | high | 88.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -5.00 | 1.79 | 0.04 | -1.10 | 0.65 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 2890 | 永豐金 | finance | mainstream_leader | high | 88.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -0.39 | -7.64 | 1.79 | -2.19 | 0.40 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 2891 | 中信金 | finance | mainstream_leader | high | 88.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 2.38 | -9.40 | 2.21 | 0.87 | 0.70 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 6757 | 台灣虎航 | traditional industries | mainstream_leader | high | 88.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 2.91 | -5.52 | 2.28 | -0.20 | 0.44 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 16 | 2887 | 台新新光金 | finance | mainstream_leader | high | 87.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 4.07 | -3.77 | 0.48 | -1.52 | 0.80 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 8401 | 白紗科 | biotechnology | mainstream_leader | high | 86.00 | 305.00 | 14 | True | True | tdcc_leading_price | quiet_accumulation | 0.89 | -1.09 | 1.16 | -0.53 | 0.28 | 10.00 | 46.78 | 10.00 | 6.00 | 0.00 | 0.78 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 6170 | 統振 | other electronics | mainstream_leader | high | 86.00 | 285.00 | 12 | True | True | tdcc_leading_price | quiet_accumulation | -0.22 | -3.55 | 0.78 | -1.09 | 0.22 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 1438 | 三地開發 | traditional industries | mainstream_leader | high | 86.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -3.23 | 2.28 | 2.52 | 1.76 | 0.58 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 2206 | 三陽工業 | traditional industries | mainstream_leader | high | 86.00 | 195.00 | 6 | False | True | tdcc_leading_price | quiet_accumulation | -5.10 | -4.06 | 1.63 | -2.45 | 0.48 | 10.00 | 153.62 | 10.00 | 16.00 | 0.00 | 0.62 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 21 | 1535 | 中宇 | other electronics | mainstream_leader | high | 80.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 0.33 | -8.14 | 1.25 | -3.49 | 0.30 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 22 | 1618 | 合機 | other electronics | mainstream_leader | high | 80.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 5.75 | -4.69 | 0.74 | 1.08 | 0.42 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 23 | 3191 | 雲嘉南 | semiconductor | mainstream_leader | high | 100.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 9.41 | -0.27 | 2.62 | 2.07 | 1.61 | 10.00 | 57.18 | 10.00 | 7.00 | 0.00 | 1.18 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 3285 | 微端 | semiconductor | mainstream_leader | high | 100.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 7.61 | -3.23 | 2.64 | 1.64 | 1.06 | 10.00 | 57.18 | 10.00 | 7.00 | 0.00 | 1.18 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 25 | 3005 | 神基 | semiconductor equipment/materials | non_mainstream_watch | medium | 91.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 5.00 | 7.44 | 2.24 | 2.21 | 0.54 | 10.00 | 21.90 | 10.00 | 4.00 | 0.00 | 2.90 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 26 | 2832 | 台產 | finance | mainstream_leader | high | 85.00 | 205.00 | 4 | True | True | tdcc_leading_price | watch_only | 0.70 | 2.48 | 2.42 | 0.99 | 1.50 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 27 | 5283 | 禾聯碩 | other electronics | mainstream_leader | high | 85.00 | 205.00 | 4 | True | True | tdcc_leading_price | watch_only | 1.32 | 1.51 | 2.95 | 0.61 | 1.12 | 10.00 | 225.04 | 10.00 | 28.00 | 0.00 | 1.04 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 28 | 2882 | 國泰金 | finance | mainstream_leader | high | 80.00 | 195.00 | 3 | True | True | tdcc_leading_price | watch_only | 2.42 | -0.51 | 0.68 | 0.48 | 0.75 | 10.00 | 61.30 | 10.00 | 6.00 | 0.00 | 1.30 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 29 | 1101 | 台泥 | other | single_name_signal | high | 98.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 1.25 | 5.41 | 1.94 | 2.23 | 0.95 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 30 | 9935 | 慶豐富 | other | single_name_signal | high | 90.00 | 165.00 | 3 | False | True | tdcc_leading_price | quiet_accumulation | 1.29 | 5.95 | 1.25 | 2.18 | 1.69 | 10.00 | 179.27 | 10.00 | 20.00 | 0.00 | 0.27 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |

## Theme Mainstream Summary

| theme | theme_mainstream_status | signal_count | leading_count | confirmed_count | late_or_overheated_count | divergence_count | avg_tdcc_strength_score | avg_abm_score | representative_codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other electronics | mainstream_leader | 485 | 20 | 0 | 47 | 51 | 153.99 | 53.09 | 2321/6418/6170/6194/3666 |
| traditional industries | mainstream_leader | 204 | 14 | 1 | 5 | 27 | 162.60 | 59.52 | 1323/5523/2618/2516/2511 |
| other | single_name_signal | 181 | 17 | 0 | 6 | 24 | 164.81 | 59.56 | 7718/1233/4406/6965/7760 |
| biotechnology | mainstream_leader | 106 | 4 | 0 | 4 | 10 | 154.34 | 57.40 | 8401/6527/1709/2107/8437 |
| semiconductor | mainstream_leader | 103 | 5 | 0 | 18 | 8 | 154.22 | 50.77 | 2101/3191/3032/3268/3152 |
| semiconductor equipment/materials | non_mainstream_watch | 35 | 1 | 0 | 7 | 1 | 159.00 | 50.17 | 3005/2357/2362/6206/3017 |
| finance | mainstream_leader | 28 | 6 | 0 | 0 | 4 | 174.29 | 69.54 | 2867/2892/5880/2883/2884 |
| consumer electronics | non_mainstream_watch | 12 | 0 | 0 | 3 | 1 | 150.83 | 47.50 | 3024/2323/2486/6209/6244 |
| networking | non_mainstream_watch | 8 | 1 | 0 | 1 | 0 | 148.75 | 49.75 | 3491/5388/3704/2332/3081 |
| green energy | non_mainstream_watch | 4 | 0 | 0 | 0 | 1 | 155.00 | 53.50 | 1529/8422/8476/3551 |
| passive components | non_mainstream_watch | 4 | 0 | 0 | 0 | 0 | 107.50 | 44.50 | 3357/2375/3624/6173 |
| memory | mainstream_overheated | 3 | 0 | 0 | 3 | 0 | 175.00 | 16.67 | 2344/3006/5351 |
| optical communication/CPO | non_mainstream_watch | 2 | 0 | 0 | 1 | 0 | 90.00 | 40.00 | 4903/3450 |
| AI server supply chain | single_name_signal | 1 | 0 | 0 | 0 | 0 | 65.00 | 60.00 | 4916 |
| PCB/CCL | single_name_signal | 1 | 0 | 0 | 0 | 1 | 135.00 | 46.00 | 2355 |
| power discrete/diodes | single_name_signal | 1 | 0 | 0 | 0 | 0 | 40.00 | 37.00 | 8261 |

## TDCC Strength Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1323 | 永裕 | traditional industries | mainstream_leader | 525.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7718 | 友鋮 | other | single_name_signal | 395.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1233 | 天仁 | other | single_name_signal | 315.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2321 | 東訊 | other electronics | mainstream_leader | 305.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2516 | 新建 | traditional industries | mainstream_leader | 305.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2618 | 長榮航 | traditional industries | mainstream_leader | 305.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2867 | 三商壽 | finance | mainstream_leader | 305.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 4406 | 新昕纖 | other | single_name_signal | 305.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 5523 | 豐謙 | traditional industries | mainstream_leader | 305.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 6527 | 明達醫 | biotechnology | mainstream_leader | 305.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6965 | 中傑-KY | other | single_name_signal | 305.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7760 | 享溫馨 | other | single_name_signal | 305.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8401 | 白紗科 | biotechnology | mainstream_leader | 305.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 6418 | 詠昇 | other electronics | mainstream_leader | 295.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 4119 | 旭富 | other | single_name_signal | 285.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6170 | 統振 | other electronics | mainstream_leader | 285.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 8930 | 青鋼 | other | single_name_signal | 285.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2511 | 太子 | traditional industries | mainstream_leader | 275.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4737 | 華廣 | other | single_name_signal | 275.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9906 | 欣巴巴 | other | single_name_signal | 275.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1709 | 和益 | biotechnology | mainstream_leader | 265.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2892 | 第一金 | finance | mainstream_leader | 265.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 5880 | 合庫金 | finance | mainstream_leader | 265.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 6194 | 育富 | other electronics | mainstream_leader | 265.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3356 | 奇偶 | other electronics | mainstream_leader | 255.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3499 | 環天科 | other electronics | mainstream_leader | 255.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3666 | 光耀 | other electronics | mainstream_leader | 255.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 3712 | 永崴投控 | other electronics | mainstream_leader | 255.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6128 | 上福 | other electronics | mainstream_leader | 255.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6461 | 益得 | other electronics | mainstream_leader | 255.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |

## Pre-Move / ABM Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1525 | 江申 | other electronics | mainstream_leader | 97.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 97.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5523 | 豐謙 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1558 | 伸興 | other electronics | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2646 | 星宇航空 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 6504 | 南六 | biotechnology | mainstream_leader | 91.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 4972 | 湯石照明 | other electronics | mainstream_leader | 91.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2603 | 長榮 | traditional industries | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5880 | 合庫金 | finance | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1463 | 強盛新 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 6194 | 育富 | other electronics | mainstream_leader | 89.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2704 | 國賓 | traditional industries | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 2890 | 永豐金 | finance | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2891 | 中信金 | finance | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 6757 | 台灣虎航 | traditional industries | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2887 | 台新新光金 | finance | mainstream_leader | 87.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 8401 | 白紗科 | biotechnology | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 6170 | 統振 | other electronics | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1438 | 三地開發 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2206 | 三陽工業 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1535 | 中宇 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1618 | 合機 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3191 | 雲嘉南 | semiconductor | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；避免爆量長上影 |
| 3285 | 微端 | semiconductor | mainstream_leader | 100.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3005 | 神基 | semiconductor equipment/materials | non_mainstream_watch | 91.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 2832 | 台產 | finance | mainstream_leader | 85.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 5283 | 禾聯碩 | other electronics | mainstream_leader | 85.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2882 | 國泰金 | finance | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1101 | 台泥 | other | single_name_signal | 98.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 9935 | 慶豐富 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流潛伏吸籌名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1525 | 江申 | other electronics | mainstream_leader | 97.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 97.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5523 | 豐謙 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1558 | 伸興 | other electronics | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2646 | 星宇航空 | traditional industries | mainstream_leader | 96.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 6504 | 南六 | biotechnology | mainstream_leader | 91.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 4972 | 湯石照明 | other electronics | mainstream_leader | 91.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2603 | 長榮 | traditional industries | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5880 | 合庫金 | finance | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1463 | 強盛新 | traditional industries | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 6194 | 育富 | other electronics | mainstream_leader | 89.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2704 | 國賓 | traditional industries | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 2890 | 永豐金 | finance | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2891 | 中信金 | finance | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 6757 | 台灣虎航 | traditional industries | mainstream_leader | 88.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2887 | 台新新光金 | finance | mainstream_leader | 87.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 8401 | 白紗科 | biotechnology | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 6170 | 統振 | other electronics | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 1438 | 三地開發 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2206 | 三陽工業 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |

## 非主流但值得觀察名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3005 | 神基 | semiconductor equipment/materials | non_mainstream_watch | 91.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 3704 | 合勤控 | networking | non_mainstream_watch | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |

## 孤單訊號 / 非主流降權名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1101 | 台泥 | other | single_name_signal | 98.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 9935 | 慶豐富 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；避免爆量長上影；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8941 | 關中 | other | single_name_signal | 82.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4207 | 環泰 | other | single_name_signal | 100.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流過熱風險名單

目前沒有可用資料。

## TDCC 背離 + 弱族群名單

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1109 | 信大 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1217 | 愛之味 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1233 | 天仁 | other | single_name_signal | 315.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2355 | 敬鵬 | PCB/CCL | single_name_signal | 135.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4119 | 旭富 | other | single_name_signal | 285.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4162 | 智擎 | other | single_name_signal | 165.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4169 | 泰宗 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4190 | 佐登-KY | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4306 | 炎洲 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4426 | 利勤 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4533 | 協易機 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4714 | 永捷 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4737 | 華廣 | other | single_name_signal | 275.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6923 | 中台 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6925 | 意藍 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6937 | 天虹 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6965 | 中傑-KY | other | single_name_signal | 305.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7760 | 享溫馨 | other | single_name_signal | 305.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7786 | 東方風能 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9105 | 泰金寶-DR | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9906 | 欣巴巴 | other | single_name_signal | 275.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9918 | 欣天然 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9924 | 福興 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9929 | 秋雨 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9960 | 邁達康 | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Top Risk List

- price_leading_tdcc: 股價已先漲，TDCC 訊號可能偏晚。
- overheated_after_tdcc: 籌碼強但股價已過熱。
- tdcc_price_divergence: TDCC 增加但股價轉弱，需列為失效觀察。

## Top Risk List - price_leading_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6527 | 明達醫 | biotechnology | mainstream_leader | 305.00 | price_leading_tdcc | 3.56 | 12.62 | 7.42 | 2.40 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3712 | 永崴投控 | other electronics | mainstream_leader | 255.00 | price_leading_tdcc | 15.67 | 11.10 | 14.84 | 1.02 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6804 | 明係 | other | single_name_signal | 245.00 | price_leading_tdcc | 19.18 | 13.71 | 9.55 | 1.29 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6578 | 達邦蛋白 | biotechnology | mainstream_leader | 225.00 | price_leading_tdcc | 13.94 | 19.30 | 12.83 | 0.91 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4127 | 天良 | other | single_name_signal | 215.00 | price_leading_tdcc | 8.18 | 20.54 | 11.80 | 1.76 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2362 | 藍天 | semiconductor equipment/materials | non_mainstream_watch | 215.00 | price_leading_tdcc | 18.42 | 17.01 | 17.68 | 7.76 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 9939 | 宏全 | other | single_name_signal | 215.00 | price_leading_tdcc | 14.92 | 10.09 | 10.47 | 2.76 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6206 | 飛捷 | semiconductor equipment/materials | non_mainstream_watch | 205.00 | price_leading_tdcc | 7.43 | 11.63 | 12.76 | 1.58 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2006 | 東和鋼鐵 | traditional industries | mainstream_leader | 205.00 | price_leading_tdcc | 25.29 | 21.55 | 16.96 | 2.66 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6603 | 富強鑫 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | 0.19 | 10.41 | 2.10 | 1.38 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6423 | 億而得 | other electronics | mainstream_leader | 205.00 | price_leading_tdcc | -13.23 | 10.99 | 6.08 | 1.16 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3231 | 緯創 | semiconductor equipment/materials | non_mainstream_watch | 195.00 | price_leading_tdcc | 29.35 | 9.70 | 15.30 | 0.86 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3321 | 同泰 | other electronics | mainstream_leader | 195.00 | price_leading_tdcc | -8.02 | 10.03 | 8.37 | 1.48 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3226 | 龍鋒 | semiconductor | mainstream_leader | 185.00 | price_leading_tdcc | 4.67 | 13.53 | 8.13 | 1.98 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3260 | 威剛 | semiconductor | mainstream_leader | 185.00 | price_leading_tdcc | 4.21 | 14.12 | 7.95 | 1.81 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3543 | 州巧 | other electronics | mainstream_leader | 185.00 | price_leading_tdcc | 20.39 | 30.27 | 19.96 | 3.05 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3362 | 先進光 | other electronics | mainstream_leader | 175.00 | price_leading_tdcc | 4.76 | 10.87 | 5.31 | 0.09 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6491 | 晶碩 | other electronics | mainstream_leader | 175.00 | price_leading_tdcc | 1.07 | 13.28 | 9.19 | 1.41 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6226 | 光鼎 | other electronics | mainstream_leader | 175.00 | price_leading_tdcc | -9.50 | 27.42 | 4.62 | 0.97 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |

## Top Risk List - overheated_after_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3653 | 健策 | other electronics | mainstream_leader | 225.00 | overheated_after_tdcc | 39.06 | 20.42 | 26.77 | 1.33 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3491 | 昇達科 | networking | non_mainstream_watch | 215.00 | overheated_after_tdcc | 12.97 | 6.74 | 13.03 | 1.63 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3714 | 富采 | other electronics | mainstream_leader | 215.00 | overheated_after_tdcc | -6.79 | 7.93 | 6.94 | 1.22 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3339 | 泰谷 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 3.57 | 17.42 | 13.96 | 4.73 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3324 | 雙鴻 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 14.59 | 17.74 | 16.18 | 2.85 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3135 | 凌航 | semiconductor | mainstream_leader | 195.00 | overheated_after_tdcc | 8.75 | 24.81 | 19.11 | 2.53 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3489 | 森寶 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 7.47 | 38.49 | 22.94 | 1.65 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2049 | 上銀 | traditional industries | mainstream_leader | 195.00 | overheated_after_tdcc | 6.47 | 13.78 | 13.30 | 3.75 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3017 | 奇鋐 | semiconductor equipment/materials | non_mainstream_watch | 195.00 | overheated_after_tdcc | 26.45 | 20.97 | 25.61 | 2.09 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6669 | 緯穎 | semiconductor equipment/materials | non_mainstream_watch | 195.00 | overheated_after_tdcc | 24.06 | 15.01 | 16.91 | 0.68 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4967 | 十銓 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 20.17 | 29.51 | 22.58 | 2.66 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 5274 | 信驊 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 19.86 | 10.68 | 16.92 | 1.04 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2455 | 全新 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 11.04 | 8.30 | 17.13 | 3.98 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3036 | 文曄 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 10.93 | 13.01 | 15.65 | 2.48 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1597 | 直得 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 1.78 | 6.80 | 11.59 | 2.49 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3042 | 晶技 | semiconductor | mainstream_leader | 195.00 | overheated_after_tdcc | -15.53 | 6.25 | 3.80 | 0.64 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2421 | 建準 | traditional industries | mainstream_leader | 185.00 | overheated_after_tdcc | 7.67 | 16.21 | 15.93 | 4.99 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2464 | 盟立 | other electronics | mainstream_leader | 185.00 | overheated_after_tdcc | 11.60 | 20.34 | 19.54 | 3.19 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8299 | 群聯 | semiconductor | mainstream_leader | 185.00 | overheated_after_tdcc | -5.37 | 8.36 | 9.08 | 1.17 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 5392 | 能率 | other electronics | mainstream_leader | 185.00 | overheated_after_tdcc | -3.95 | 14.08 | 9.76 | 3.00 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Top Risk List - tdcc_price_divergence Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1323 | 永裕 | traditional industries | mainstream_leader | 525.00 | tdcc_price_divergence | -2.70 | -0.02 | -0.56 | 0.50 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1233 | 天仁 | other | single_name_signal | 315.00 | tdcc_price_divergence | 3.42 | -0.89 | 0.02 | 1.20 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2321 | 東訊 | other electronics | mainstream_leader | 305.00 | tdcc_price_divergence | 7.91 | -0.84 | 1.04 | 0.45 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2516 | 新建 | traditional industries | mainstream_leader | 305.00 | tdcc_price_divergence | 0.73 | -0.59 | -0.72 | 0.45 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7760 | 享溫馨 | other | single_name_signal | 305.00 | tdcc_price_divergence | -5.48 | -3.24 | -1.87 | 1.25 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6965 | 中傑-KY | other | single_name_signal | 305.00 | tdcc_price_divergence | -3.28 | -2.31 | -2.09 | 0.83 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4119 | 旭富 | other | single_name_signal | 285.00 | tdcc_price_divergence | 8.72 | -0.54 | 1.19 | 0.53 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4737 | 華廣 | other | single_name_signal | 275.00 | tdcc_price_divergence | -5.26 | -2.05 | -4.94 | 0.50 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 9906 | 欣巴巴 | other | single_name_signal | 275.00 | tdcc_price_divergence | -4.88 | -2.39 | -2.45 | 0.51 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2511 | 太子 | traditional industries | mainstream_leader | 275.00 | tdcc_price_divergence | -2.47 | -1.99 | -2.12 | 0.78 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3356 | 奇偶 | other electronics | mainstream_leader | 255.00 | tdcc_price_divergence | -6.34 | -2.80 | -2.70 | 0.96 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3499 | 環天科 | other electronics | mainstream_leader | 255.00 | tdcc_price_divergence | -12.16 | -2.56 | -4.62 | 0.45 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6128 | 上福 | other electronics | mainstream_leader | 255.00 | tdcc_price_divergence | -0.49 | -0.75 | -0.51 | 0.82 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1452 | 宏益 | traditional industries | mainstream_leader | 245.00 | tdcc_price_divergence | -5.93 | -3.42 | -3.39 | 1.74 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5481 | 新華 | other electronics | mainstream_leader | 245.00 | tdcc_price_divergence | -4.81 | -5.01 | -4.17 | 0.11 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6219 | 富旺 | other electronics | mainstream_leader | 245.00 | tdcc_price_divergence | -2.36 | -8.54 | -3.03 | 0.15 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1413 | 宏洲 | traditional industries | mainstream_leader | 245.00 | tdcc_price_divergence | -0.64 | -0.80 | -3.01 | 0.29 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6576 | 逸達 | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | -5.23 | -1.08 | -1.37 | 0.45 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6609 | 瀧澤科 | other electronics | mainstream_leader | 235.00 | tdcc_price_divergence | -4.14 | -0.27 | -2.24 | 0.19 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8466 | 美吉吉-KY | biotechnology | mainstream_leader | 235.00 | tdcc_price_divergence | -3.71 | -2.68 | -1.42 | 0.23 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Phase Distribution

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 886.0 | 75.21 |
| tdcc_price_divergence | 123.0 | 10.44 |
| overheated_after_tdcc | 76.0 | 6.45 |
| tdcc_leading_price | 68.0 | 5.77 |
| price_leading_tdcc | 19.0 | 1.61 |
| failed_after_tdcc | 5.0 | 0.42 |
| tdcc_price_confirmed | 1.0 | 0.08 |

## Consecutive Weeks x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 456.0 |
| 1 | overheated_after_tdcc | 39.0 |
| 1 | price_leading_tdcc | 3.0 |
| 10 | insufficient_price_context | 4.0 |
| 10 | tdcc_leading_price | 2.0 |
| 11 | insufficient_price_context | 2.0 |
| 11 | tdcc_price_divergence | 3.0 |
| 12 | insufficient_price_context | 7.0 |
| 12 | tdcc_leading_price | 2.0 |
| 12 | tdcc_price_divergence | 1.0 |
| 13 | insufficient_price_context | 3.0 |
| 14 | insufficient_price_context | 6.0 |
| 14 | price_leading_tdcc | 1.0 |
| 14 | tdcc_leading_price | 2.0 |
| 14 | tdcc_price_divergence | 4.0 |
| 15 | tdcc_price_divergence | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 161.0 |
| 2 | overheated_after_tdcc | 15.0 |
| 2 | price_leading_tdcc | 3.0 |
| 2 | tdcc_leading_price | 21.0 |
| 2 | tdcc_price_confirmed | 1.0 |
| 2 | tdcc_price_divergence | 40.0 |
| 26 | insufficient_price_context | 1.0 |
| 3 | failed_after_tdcc | 2.0 |
| 3 | insufficient_price_context | 106.0 |
| 3 | overheated_after_tdcc | 14.0 |
| 3 | price_leading_tdcc | 2.0 |
| 3 | tdcc_leading_price | 12.0 |
| 3 | tdcc_price_divergence | 30.0 |
| 36 | tdcc_price_divergence | 1.0 |
| 4 | failed_after_tdcc | 1.0 |
| 4 | insufficient_price_context | 56.0 |
| 4 | overheated_after_tdcc | 5.0 |
| 4 | price_leading_tdcc | 4.0 |
| 4 | tdcc_leading_price | 9.0 |
| 4 | tdcc_price_divergence | 16.0 |
| 5 | insufficient_price_context | 43.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 3.0 |
| 5 | tdcc_leading_price | 7.0 |
| 5 | tdcc_price_divergence | 8.0 |
| 6 | insufficient_price_context | 18.0 |
| 6 | overheated_after_tdcc | 1.0 |
| 6 | price_leading_tdcc | 1.0 |
| 6 | tdcc_leading_price | 7.0 |
| 6 | tdcc_price_divergence | 8.0 |
| 7 | insufficient_price_context | 12.0 |
| 7 | tdcc_leading_price | 3.0 |
| 7 | tdcc_price_divergence | 3.0 |
| 8 | insufficient_price_context | 8.0 |
| 8 | price_leading_tdcc | 1.0 |
| 8 | tdcc_leading_price | 2.0 |
| 8 | tdcc_price_divergence | 4.0 |
| 9 | insufficient_price_context | 3.0 |
| 9 | price_leading_tdcc | 1.0 |
| 9 | tdcc_leading_price | 1.0 |
| 9 | tdcc_price_divergence | 4.0 |

## Mature Performance Summary

只使用 mature_dN=True 的資料。pending 不可視為正面或負面。

- phase-level mature sample 已可使用。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 2.0 | -8.28 | -7.06 | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 185.0 | -0.60 | -0.88 | 153.0 | -1.78 | -1.49 | 107.0 | -7.39 | -4.21 | 12.17 | -10.54 |
| overheated_after_tdcc | 124.0 | 2.69 | 1.60 | 119.0 | 2.76 | 1.87 | 116.0 | -2.19 | -1.83 | 19.25 | -11.63 |
| price_leading_tdcc | 116.0 | 1.06 | -0.39 | 107.0 | -0.88 | -0.46 | 82.0 | -3.76 | -1.90 | 13.44 | -10.31 |
| tdcc_leading_price | 33.0 | -0.30 | 0.34 | 30.0 | -0.82 | -2.12 | 25.0 | -4.28 | -3.14 | 9.78 | -9.68 |
| tdcc_price_confirmed | 11.0 | -1.99 | -1.91 | 11.0 | 0.23 | 0.73 | 11.0 | -3.80 | -2.80 | 12.27 | -11.85 |
| tdcc_price_divergence | 20.0 | -6.38 | -5.86 | 13.0 | -8.25 | -6.20 | 9.0 | -6.80 | 1.58 | 8.65 | -16.86 |

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
- tdcc_weekly_candidate_highlight_delivery_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260807.pdf
- tdcc_weekly_candidate_full_delivery_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260807.pdf
- tdcc_weekly_candidate_highlight_delivery_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260807.pdf
- tdcc_weekly_candidate_full_delivery_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260807.pdf

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
