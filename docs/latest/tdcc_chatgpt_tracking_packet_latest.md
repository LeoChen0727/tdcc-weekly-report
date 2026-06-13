# TDCC CHATGPT TRACKING PACKET

## Metadata
- generated_at: 2026-06-13 18:54:40 Asia/Taipei
- main_price_date: 20260612
- latest_tdcc_signal_date: 20260612
- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md
- overall_mature_d5_count: 119
- phase_mature_d5_count: 119
- overall_mature_d10_count: 82
- phase_mature_d10_count: 82
- overall_mature_d20_count: 41
- phase_mature_d20_count: 41
- pending_count: 99
- insufficient_sample_count: 840
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- theme_data_available: yes
- theme_lookup_rows: 28
- theme_other_pct: 21.3
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
- theme_lookup_rows: 28
- theme_lookup_sources: {'config': 28, 'company_theme_mapping': 28, 'all_candidates': 0}
- theme_other_before: 1083
- theme_other_after: 233
- theme_other_pct: 21.3
- sample_status: phase_samples_available
- relaxed_filter: False
- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution

## Mature Sample Status

- overall_mature_d5_count: 119
- phase_mature_d5_count: 119
- overall_mature_d10_count: 82
- phase_mature_d10_count: 82
- overall_mature_d20_count: 41
- phase_mature_d20_count: 41
- pending_count: 99
- insufficient_sample_count: 840
- phase_mature_join_quality: ok
- sample_status: phase_samples_available

- phase-level mature sample 已可使用。

## TDCC Strength Ranking Top 30

| rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | abm_score | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | risk_label | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1233 | 天仁 | other | single_name_signal | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 86.00 | 0.72 | -2.97 | -0.68 | -1.53 | 0.30 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2 | 1304 | 台聚 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 82.00 | -4.51 | -0.39 | 6.22 | 0.59 | 0.52 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 3 | 1323 | 永裕 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | watch_only | 81.00 | -3.18 | 1.80 | -0.96 | -0.94 | 1.32 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4 | 1410 | 南染 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_price_divergence | watch_only | 65.00 | -2.75 | -7.46 | -4.08 | -5.36 | 1.66 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5 | 1443 | 立益物流 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | watch_only | 83.00 | 5.95 | -1.48 | 6.17 | 2.93 | 0.94 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 6 | 1460 | 宏遠 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | -0.70 | 1.00 | 3.27 | 0.46 | 0.64 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 7 | 1626 | 艾美特-KY | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | watch_only | 70.00 | -0.50 | -5.19 | 1.96 | 0.23 | 0.46 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 1734 | 杏輝 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 0.64 | 1.78 | 4.54 | 2.12 | 1.03 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 9 | 1737 | 臺鹽 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 0.47 | 0.95 | 1.89 | 0.61 | 0.64 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 2024 | 志聯 | traditional industries | mainstream_leader | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 90.00 | -1.05 | 2.16 | 2.69 | 1.92 | 0.67 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 3705 | 永信 | other electronics | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 100.00 | 1.60 | 3.25 | 3.95 | 1.96 | 0.83 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 12 | 4527 | 方土霖 | other | single_name_signal | high | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 95.00 | -1.78 | -5.16 | -1.06 | -4.44 | 1.21 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 13 | 7718 | 友鋮 | other | single_name_signal | high | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 91.00 | -4.33 | -3.16 | 2.43 | -2.87 | 1.37 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 8409 | 商之器 | biotechnology | mainstream_leader | high | 235.00 | 7 | True | True | insufficient_price_context | quiet_accumulation | 91.00 | 0.00 | 0.00 | 4.87 | -0.49 | 1.26 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 15 | 1236 | 宏亞 | other | single_name_signal | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 4.05 | 2.19 | 7.46 | 5.02 | 1.04 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 16 | 1313 | 聯成 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | watch_only | 69.00 | 0.90 | 0.45 | 8.92 | 4.02 | 0.88 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 17 | 1423 | 利華 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | price_leading_tdcc | watch_only | 79.00 | 4.76 | 12.19 | 11.66 | 7.66 | 11.27 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 18 | 1455 | 集盛 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | price_leading_tdcc | strong_momentum | 65.00 | 8.59 | 23.33 | 25.82 | 16.10 | 1.48 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 19 | 1459 | 聯發 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_leading_price | watch_only | 80.00 | 1.72 | -0.84 | 2.55 | 0.60 | 0.42 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | potential_accumulation | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 1733 | 五鼎 | biotechnology | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_price_divergence | quiet_accumulation | 96.00 | -3.62 | 2.99 | -1.40 | -1.39 | 0.42 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 21 | 2008 | 高興昌 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | tdcc_price_confirmed | quiet_accumulation | 85.00 | 2.74 | 9.09 | 9.37 | 5.36 | 0.31 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | confirmed_move | strong_confirmed | 籌碼改善且股價已開始確認。 |
| 22 | 2027 | 大成鋼 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 91.00 | -0.23 | 9.70 | 6.58 | 3.96 | 0.47 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 23 | 2064 | 晉椿 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | price_leading_tdcc | quiet_accumulation | 88.00 | -4.39 | 9.27 | 10.99 | 3.13 | 0.84 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 24 | 2107 | 厚生 | biotechnology | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | watch_only | 92.00 | 3.32 | 1.93 | 7.91 | 4.30 | 3.67 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 25 | 2380 | 虹光 | other electronics | mainstream_leader | high | 225.00 | 6 | True | True | price_leading_tdcc | watch_only | 65.00 | 11.44 | 10.67 | 13.28 | 10.41 | 3.66 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | late_or_chasing_risk | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 26 | 2385 | 群光 | other electronics | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | -1.74 | 4.44 | 7.28 | 5.07 | 1.43 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 27 | 2477 | 美隆電 | other electronics | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | watch_only | 66.00 | -1.35 | 4.51 | 6.52 | 2.64 | 0.51 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 28 | 2492 | 華新科 | passive components | mainstream_overheated | overheated | 225.00 | 6 | True | True | overheated_after_tdcc | overheated | 0.00 | -10.31 | 116.98 | 25.77 | 22.96 | 0.38 | 10.00 | 29.05 | 10.00 | 0.00 | 0.00 | 29.05 | overheated | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 29 | 2505 | 國揚 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 95.00 | 7.43 | 4.44 | 7.18 | 5.48 | 1.39 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 30 | 2542 | 興富發 | traditional industries | mainstream_leader | high | 225.00 | 6 | True | True | insufficient_price_context | quiet_accumulation | 92.00 | 5.89 | 9.37 | 7.27 | 4.04 | 1.79 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | insufficient_data | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |

## Pre-Move Accumulation / ABM Top 30

| abm_rank | stock_id | stock_name | theme | theme_mainstream_status | theme_heat_level | abm_score | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | theme_momentum_score | theme_tdcc_breadth_score | theme_price_breadth_score | theme_warrant_heat_score | theme_relative_strength | accumulation_label | tracking_priority | trigger_to_watch | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2034 | 允強 | traditional industries | mainstream_leader | high | 97.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 0.75 | -0.25 | 1.51 | 0.85 | 1.45 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 2 | 2024 | 志聯 | traditional industries | mainstream_leader | high | 90.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | -1.05 | 2.16 | 2.69 | 1.92 | 0.67 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 3 | 5283 | 禾聯碩 | other electronics | mainstream_leader | high | 90.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -0.19 | 2.92 | 2.41 | 0.92 | 0.77 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 4 | 1737 | 臺鹽 | biotechnology | mainstream_leader | high | 100.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 0.47 | 0.95 | 1.89 | 0.61 | 0.64 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼持續改善，但股價尚未明顯反應。 |
| 5 | 2926 | 誠品生活 | biotechnology | mainstream_leader | high | 91.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 0.87 | -4.13 | 2.33 | -2.49 | 1.51 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | prime_pre_move | B_confirm_needed | 站回 MA20；避免爆量長上影；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 6 | 6198 | 瑞築 | other electronics | mainstream_leader | high | 91.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 1.96 | -4.15 | 2.14 | -2.43 | 1.19 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 7 | 8367 | 建新國際 | traditional industries | mainstream_leader | high | 86.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -1.59 | -3.81 | 0.64 | -1.82 | 0.37 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 8 | 3023 | 信邦 | other electronics | mainstream_leader | high | 86.00 | 155.00 | 2 | False | True | tdcc_leading_price | quiet_accumulation | 0.32 | 4.15 | 0.63 | 1.63 | 0.34 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 9 | 3252 | 海灣 | semiconductor | non_mainstream_watch | medium | 91.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | -5.82 | 2.93 | -1.32 | 1.22 | 10.00 | 50.93 | 10.00 | 13.00 | 0.00 | 4.93 | prime_pre_move | B_confirm_needed | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 10 | 1459 | 聯發 | traditional industries | mainstream_leader | high | 80.00 | 225.00 | 6 | True | True | tdcc_leading_price | watch_only | 1.72 | -0.84 | 2.55 | 0.60 | 0.42 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 11 | 2373 | 震旦行 | other electronics | mainstream_leader | high | 80.00 | 195.00 | 3 | True | True | tdcc_leading_price | watch_only | -1.71 | 1.41 | 1.61 | 0.26 | 0.39 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 12 | 1720 | 生達 | biotechnology | mainstream_leader | high | 80.00 | 185.00 | 2 | True | True | tdcc_leading_price | watch_only | 0.81 | 2.80 | 2.72 | 1.03 | 0.49 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | watch_pre_move | B_confirm_needed | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 13 | 9908 | 大台北 | other | single_name_signal | high | 93.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 0.51 | 0.34 | 2.29 | 0.58 | 0.88 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 14 | 7718 | 友鋮 | other | single_name_signal | high | 91.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | -4.33 | -3.16 | 2.43 | -2.87 | 1.37 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 15 | 8941 | 關中 | other | single_name_signal | high | 91.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -1.95 | -4.57 | 2.55 | -2.52 | 1.69 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 站回 MA20；避免爆量長上影；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 16 | 4119 | 旭富 | other | single_name_signal | high | 90.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 1.46 | -1.19 | 1.99 | 0.24 | 0.66 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 17 | 8930 | 青鋼 | other | single_name_signal | high | 89.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -1.42 | -3.98 | 2.76 | -2.35 | 0.94 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 18 | 4106 | 雃博 | other | single_name_signal | high | 88.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -3.12 | 4.95 | 0.62 | -0.96 | 0.63 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 19 | 4171 | 瑞基 | other | single_name_signal | high | 86.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | -3.59 | -4.64 | 1.54 | -2.92 | 0.33 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 20 | 4108 | 懷特 | other | single_name_signal | high | 86.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 1.23 | 4.24 | 1.67 | 1.11 | 0.54 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 21 | 9912 | 偉聯 | other | single_name_signal | high | 100.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 0.40 | 2.46 | 1.66 | 0.20 | 0.17 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | prime_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 22 | 4747 | 強生 | biotechnology | mainstream_leader | high | 75.00 | 195.00 | 6 | False | True | tdcc_leading_price | quiet_accumulation | -2.87 | -0.55 | 0.64 | -3.97 | 1.04 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 23 | 1776 | 展宇 | biotechnology | mainstream_leader | high | 73.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -1.62 | 8.01 | 0.71 | -0.27 | 0.37 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 24 | 1626 | 艾美特-KY | other electronics | mainstream_leader | high | 70.00 | 235.00 | 7 | True | True | tdcc_leading_price | watch_only | -0.50 | -5.19 | 1.96 | 0.23 | 0.46 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | watch_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 25 | 2613 | 中櫃 | traditional industries | mainstream_leader | high | 70.00 | 205.00 | 4 | True | True | tdcc_leading_price | watch_only | -1.56 | 0.68 | 2.63 | 1.03 | 0.65 | 10.00 | 184.90 | 10.00 | 39.00 | 0.00 | 4.90 | watch_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 26 | 1604 | 聲寶 | other electronics | mainstream_leader | high | 70.00 | 175.00 | 4 | False | True | tdcc_leading_price | watch_only | 1.30 | 2.63 | 1.47 | 0.86 | 0.80 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | watch_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 27 | 1712 | 興農 | biotechnology | mainstream_leader | high | 66.00 | 165.00 | 3 | False | True | tdcc_leading_price | watch_only | 1.66 | -3.75 | 2.66 | -0.22 | 0.41 | 10.00 | 81.16 | 10.00 | 12.00 | 0.00 | 3.16 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 28 | 3704 | 合勤控 | other electronics | mainstream_leader | high | 62.00 | 225.00 | 6 | True | True | tdcc_leading_price | strong_momentum | -5.42 | 22.54 | 1.59 | 4.51 | 0.56 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | watch_pre_move | C_weak_or_discounted | 量縮守住 MA20；放量站上 5 日 / 10 日均線 | 籌碼持續改善，但股價尚未明顯反應。 |
| 29 | 1512 | 瑞利 | other electronics | mainstream_leader | high | 62.00 | 185.00 | 2 | True | True | tdcc_leading_price | watch_only | -1.44 | -3.79 | 0.11 | -1.27 | 0.75 | 10.00 | 224.31 | 10.00 | 53.00 | 0.00 | 2.31 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 | 籌碼持續改善，但股價尚未明顯反應。 |
| 30 | 9918 | 欣天然 | other | single_name_signal | high | 78.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -1.14 | 0.35 | 1.38 | -0.61 | 0.61 | 10.00 | 166.07 | 10.00 | 24.00 | 0.00 | 3.07 | watch_pre_move | C_weak_or_discounted | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 | 籌碼持續改善，但股價尚未明顯反應。 |

## Theme Mainstream Summary

| theme | theme_mainstream_status | signal_count | leading_count | confirmed_count | late_or_overheated_count | divergence_count | avg_tdcc_strength_score | avg_abm_score | representative_codes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other electronics | mainstream_leader | 435 | 9 | 0 | 54 | 25 | 149.17 | 52.14 | 1626/3705/6662/2477/2380 |
| other | single_name_signal | 233 | 13 | 0 | 21 | 18 | 159.83 | 57.49 | 1233/4527/7718/4119/4107 |
| traditional industries | mainstream_leader | 197 | 6 | 3 | 33 | 7 | 165.38 | 61.82 | 1304/1443/1460/1410/1323 |
| biotechnology | mainstream_leader | 112 | 6 | 0 | 8 | 10 | 160.22 | 58.46 | 1734/1737/8409/6508/4111 |
| semiconductor | non_mainstream_watch | 70 | 1 | 0 | 17 | 4 | 153.43 | 47.69 | 3266/3285/3092/3056/3252 |
| finance | mainstream_follow_through | 31 | 0 | 2 | 11 | 0 | 170.81 | 64.23 | 2836/2867/2881/2886/2882 |
| passive components | mainstream_overheated | 4 | 0 | 0 | 4 | 0 | 190.00 | 0.00 | 2492/6173/2375/3624 |
| PCB/CCL | non_mainstream_watch | 3 | 0 | 0 | 0 | 0 | 146.67 | 50.33 | 5464/2355/5439 |
| consumer electronics | non_mainstream_watch | 3 | 0 | 0 | 0 | 0 | 128.33 | 52.67 | 2383/5371/8045 |
| semiconductor equipment/materials | non_mainstream_watch | 3 | 0 | 0 | 0 | 1 | 123.33 | 56.33 | 5234/4763/8028 |
| green energy | single_name_signal | 1 | 0 | 0 | 0 | 0 | 125.00 | 52.00 | 1529 |
| networking | single_name_signal | 1 | 0 | 0 | 0 | 0 | 110.00 | 45.00 | 8071 |
| optical communication/CPO | single_name_signal | 1 | 0 | 0 | 0 | 1 | 155.00 | 52.00 | 4903 |

## TDCC Strength Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1233 | 天仁 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1304 | 台聚 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1323 | 永裕 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1410 | 南染 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1443 | 立益物流 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1460 | 宏遠 | traditional industries | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1626 | 艾美特-KY | other electronics | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1734 | 杏輝 | biotechnology | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1737 | 臺鹽 | biotechnology | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 2024 | 志聯 | traditional industries | mainstream_leader | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 3705 | 永信 | other electronics | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 4527 | 方土霖 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7718 | 友鋮 | other | single_name_signal | 235.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 8409 | 商之器 | biotechnology | mainstream_leader | 235.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1236 | 宏亞 | other | single_name_signal | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1313 | 聯成 | traditional industries | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 1423 | 利華 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1455 | 集盛 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1459 | 聯發 | traditional industries | mainstream_leader | 225.00 | tdcc_leading_price | strong_but_pre_move | 籌碼持續改善，但股價尚未明顯反應。 |
| 1733 | 五鼎 | biotechnology | mainstream_leader | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2008 | 高興昌 | traditional industries | mainstream_leader | 225.00 | tdcc_price_confirmed | strong_confirmed | 籌碼改善且股價已開始確認。 |
| 2027 | 大成鋼 | traditional industries | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2064 | 晉椿 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2107 | 厚生 | biotechnology | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2380 | 虹光 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2385 | 群光 | other electronics | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2477 | 美隆電 | other electronics | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2492 | 華新科 | passive components | mainstream_overheated | 225.00 | overheated_after_tdcc | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2505 | 國揚 | traditional industries | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |
| 2542 | 興富發 | traditional industries | mainstream_leader | 225.00 | insufficient_price_context | insufficient_data | 價格或 benchmark 資料不足，不列入強弱判斷。 |

## Pre-Move / ABM Ranking by Theme Mainstream Status

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2034 | 允強 | traditional industries | mainstream_leader | 97.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2024 | 志聯 | traditional industries | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5283 | 禾聯碩 | other electronics | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1737 | 臺鹽 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2926 | 誠品生活 | biotechnology | mainstream_leader | 91.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；避免爆量長上影；價格止跌並重新轉強 |
| 6198 | 瑞築 | other electronics | mainstream_leader | 91.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 8367 | 建新國際 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3023 | 信邦 | other electronics | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 3252 | 海灣 | semiconductor | non_mainstream_watch | 91.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 1459 | 聯發 | traditional industries | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2373 | 震旦行 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1720 | 生達 | biotechnology | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 9908 | 大台北 | other | single_name_signal | 93.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 7718 | 友鋮 | other | single_name_signal | 91.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8941 | 關中 | other | single_name_signal | 91.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；避免爆量長上影；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4119 | 旭富 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8930 | 青鋼 | other | single_name_signal | 89.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4106 | 雃博 | other | single_name_signal | 88.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4171 | 瑞基 | other | single_name_signal | 86.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4108 | 懷特 | other | single_name_signal | 86.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 9912 | 偉聯 | other | single_name_signal | 100.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4747 | 強生 | biotechnology | mainstream_leader | 75.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 1776 | 展宇 | biotechnology | mainstream_leader | 73.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 1626 | 艾美特-KY | other electronics | mainstream_leader | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2613 | 中櫃 | traditional industries | mainstream_leader | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1604 | 聲寶 | other electronics | mainstream_leader | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1712 | 興農 | biotechnology | mainstream_leader | 66.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3704 | 合勤控 | other electronics | mainstream_leader | 62.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1512 | 瑞利 | other electronics | mainstream_leader | 62.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 9918 | 欣天然 | other | single_name_signal | 78.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流潛伏吸籌名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2034 | 允強 | traditional industries | mainstream_leader | 97.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2024 | 志聯 | traditional industries | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 5283 | 禾聯碩 | other electronics | mainstream_leader | 90.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 1737 | 臺鹽 | biotechnology | mainstream_leader | 100.00 | A_prime_watch | tdcc_leading_price | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 |
| 2926 | 誠品生活 | biotechnology | mainstream_leader | 91.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；避免爆量長上影；價格止跌並重新轉強 |
| 6198 | 瑞築 | other electronics | mainstream_leader | 91.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 8367 | 建新國際 | traditional industries | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3023 | 信邦 | other electronics | mainstream_leader | 86.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1459 | 聯發 | traditional industries | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 2373 | 震旦行 | other electronics | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1720 | 生達 | biotechnology | mainstream_leader | 80.00 | B_confirm_needed | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 4747 | 強生 | biotechnology | mainstream_leader | 75.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 1776 | 展宇 | biotechnology | mainstream_leader | 73.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線 |
| 1626 | 艾美特-KY | other electronics | mainstream_leader | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 2613 | 中櫃 | traditional industries | mainstream_leader | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1604 | 聲寶 | other electronics | mainstream_leader | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1712 | 興農 | biotechnology | mainstream_leader | 66.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |
| 3704 | 合勤控 | other electronics | mainstream_leader | 62.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線 |
| 1512 | 瑞利 | other electronics | mainstream_leader | 62.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強 |

## 非主流但值得觀察名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3252 | 海灣 | semiconductor | non_mainstream_watch | 91.00 | B_confirm_needed | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |

## 孤單訊號 / 非主流降權名單

| stock_id | stock_name | theme | theme_mainstream_status | abm_score | tracking_priority | tdcc_price_phase | trigger_to_watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9908 | 大台北 | other | single_name_signal | 93.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 7718 | 友鋮 | other | single_name_signal | 91.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8941 | 關中 | other | single_name_signal | 91.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；避免爆量長上影；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4119 | 旭富 | other | single_name_signal | 90.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 8930 | 青鋼 | other | single_name_signal | 89.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4106 | 雃博 | other | single_name_signal | 88.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4171 | 瑞基 | other | single_name_signal | 86.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |
| 4108 | 懷特 | other | single_name_signal | 86.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 9912 | 偉聯 | other | single_name_signal | 100.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 9918 | 欣天然 | other | single_name_signal | 78.00 | C_weak_or_discounted | tdcc_leading_price | 站回 MA20；放量站上 5 日 / 10 日均線；等待第二檔 / 第三檔同族群股票同步轉強 |
| 6923 | 中台 | other | single_name_signal | 70.00 | C_weak_or_discounted | tdcc_leading_price | 量縮守住 MA20；放量站上 5 日 / 10 日均線；價格止跌並重新轉強；等待第二檔 / 第三檔同族群股票同步轉強 |

## 主流過熱風險名單

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2492 | 華新科 | passive components | mainstream_overheated | 225.00 | overheated_after_tdcc | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## TDCC 背離 + 弱族群名單

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1220 | 台榮 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1233 | 天仁 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4195 | 基米-創 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4198 | 欣大健康 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4303 | 信立 | other | single_name_signal | 205.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4439 | 冠星-KY | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4527 | 方土霖 | other | single_name_signal | 235.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4571 | 鈞興-KY | other | single_name_signal | 155.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4737 | 華廣 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4766 | 南寶 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4903 | 聯光通 | optical communication/CPO | single_name_signal | 155.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6806 | 森崴能源 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6835 | 圓裕 | other | single_name_signal | 165.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6919 | 康霈* | other | single_name_signal | 175.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6988 | 威力暘-創 | other | single_name_signal | 225.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7631 | 聚賢研發-創 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7768 | 頌勝科技 | other | single_name_signal | 215.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7818 | 溢泰實業 | other | single_name_signal | 195.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8996 | 高力 | other | single_name_signal | 185.00 | tdcc_price_divergence | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Top Risk List

- price_leading_tdcc: 股價已先漲，TDCC 訊號可能偏晚。
- overheated_after_tdcc: 籌碼強但股價已過熱。
- tdcc_price_divergence: TDCC 增加但股價轉弱，需列為失效觀察。

## Top Risk List - price_leading_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2064 | 晉椿 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 9.27 | 10.99 | 3.13 | 0.84 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5511 | 德昌 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 5.83 | 12.41 | 5.28 | 0.83 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2596 | 綠意 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 5.30 | 17.80 | 7.44 | 0.68 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8121 | 越峰 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | 30.59 | 12.38 | 14.94 | 0.04 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2881 | 富邦金 | finance | mainstream_follow_through | 225.00 | price_leading_tdcc | 30.20 | 19.13 | 15.53 | 0.66 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1455 | 集盛 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 23.33 | 25.82 | 16.10 | 1.48 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4306 | 炎洲 | other | single_name_signal | 225.00 | price_leading_tdcc | 22.43 | 19.21 | 13.82 | 2.40 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2597 | 潤弘 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 17.23 | 22.21 | 13.38 | 1.18 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3713 | 新晶投控 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | 14.08 | 19.48 | 8.96 | 0.30 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6180 | 橘子 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | 12.63 | 15.11 | 9.03 | 0.30 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1423 | 利華 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 12.19 | 11.66 | 7.66 | 11.27 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2380 | 虹光 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | 10.67 | 13.28 | 10.41 | 3.66 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2618 | 長榮航 | traditional industries | mainstream_leader | 225.00 | price_leading_tdcc | 10.26 | 11.20 | 7.72 | 1.32 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6662 | 樂斯科 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | 0.67 | 10.25 | 2.94 | 1.68 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8047 | 星雲 | other electronics | mainstream_leader | 225.00 | price_leading_tdcc | -3.92 | 26.00 | 9.32 | 0.75 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1904 | 正隆 | traditional industries | mainstream_leader | 215.00 | price_leading_tdcc | 30.48 | 22.42 | 15.64 | 1.01 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3625 | 西勝 | other electronics | mainstream_leader | 215.00 | price_leading_tdcc | 3.75 | 10.22 | 2.62 | 0.07 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2414 | 精技 | other electronics | mainstream_leader | 215.00 | price_leading_tdcc | 28.44 | 22.45 | 18.94 | 3.74 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6153 | 嘉聯益 | other electronics | mainstream_leader | 215.00 | price_leading_tdcc | 20.60 | 21.21 | 19.91 | 4.03 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1709 | 和益 | biotechnology | mainstream_leader | 215.00 | price_leading_tdcc | 17.31 | 12.17 | 11.08 | 1.45 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |

## Top Risk List - overheated_after_tdcc Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3285 | 微端 | semiconductor | non_mainstream_watch | 225.00 | overheated_after_tdcc | 45.26 | 46.45 | 34.57 | 1.57 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4402 | 郡都開發 | traditional industries | mainstream_leader | 225.00 | overheated_after_tdcc | 31.20 | 45.56 | 31.38 | 0.45 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4707 | 磐亞 | other | single_name_signal | 225.00 | overheated_after_tdcc | 23.46 | 41.91 | 21.27 | 0.03 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2492 | 華新科 | passive components | mainstream_overheated | 225.00 | overheated_after_tdcc | 116.98 | 25.77 | 22.96 | 0.38 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 8454 | 富邦媒 | biotechnology | mainstream_leader | 215.00 | overheated_after_tdcc | 88.62 | 90.89 | 51.04 | 0.44 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2243 | 宏旭-KY | traditional industries | mainstream_leader | 215.00 | overheated_after_tdcc | 67.57 | 59.56 | 46.50 | 2.33 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3147 | 大綜 | semiconductor | non_mainstream_watch | 205.00 | overheated_after_tdcc | 90.42 | 89.09 | 61.51 | 1.31 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3236 | 千如 | semiconductor | non_mainstream_watch | 205.00 | overheated_after_tdcc | 78.78 | 13.98 | 23.77 | 0.01 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6409 | 旭隼 | other electronics | mainstream_leader | 205.00 | overheated_after_tdcc | 21.73 | 34.88 | 25.85 | 1.32 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4741 | 泓瀚 | other | single_name_signal | 205.00 | overheated_after_tdcc | 19.63 | 28.23 | 25.44 | 0.16 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6890 | 來億-KY | other | single_name_signal | 195.00 | overheated_after_tdcc | 51.93 | 52.74 | 37.69 | 0.24 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 4534 | 慶騰 | other | single_name_signal | 195.00 | overheated_after_tdcc | 41.03 | 29.45 | 26.27 | 0.18 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6270 | 倍微 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 27.17 | 33.51 | 21.72 | 0.23 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3026 | 禾伸堂 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 131.52 | 35.30 | 43.04 | 1.08 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2478 | 大毅 | other electronics | mainstream_leader | 195.00 | overheated_after_tdcc | 114.37 | 45.38 | 38.61 | 2.50 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 7610 | 聯友金屬-創 | other | single_name_signal | 195.00 | overheated_after_tdcc | 100.00 | 27.45 | 20.34 | 0.60 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 6173 | 信昌電 | passive components | mainstream_overheated | 185.00 | overheated_after_tdcc | 88.10 | 28.83 | 33.62 | 0.28 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 1714 | 和桐 | biotechnology | mainstream_leader | 185.00 | overheated_after_tdcc | 48.29 | 61.09 | 46.52 | 6.36 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 2491 | 吉祥全 | other electronics | mainstream_leader | 185.00 | overheated_after_tdcc | 45.92 | 41.31 | 28.21 | 0.23 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |
| 3550 | 聯穎 | other electronics | mainstream_leader | 185.00 | overheated_after_tdcc | 43.10 | 43.66 | 33.50 | 2.67 | strong_but_overheated | 籌碼強但股價已過熱，需防追高。 |

## Top Risk List - tdcc_price_divergence Top 20

| stock_id | stock_name | theme | theme_mainstream_status | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1323 | 永裕 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | 1.80 | -0.96 | -0.94 | 1.32 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1410 | 南染 | traditional industries | mainstream_leader | 235.00 | tdcc_price_divergence | -7.46 | -4.08 | -5.36 | 1.66 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4527 | 方土霖 | other | single_name_signal | 235.00 | tdcc_price_divergence | -5.16 | -1.06 | -4.44 | 1.21 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1233 | 天仁 | other | single_name_signal | 235.00 | tdcc_price_divergence | -2.97 | -0.68 | -1.53 | 0.30 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 1733 | 五鼎 | biotechnology | mainstream_leader | 225.00 | tdcc_price_divergence | 2.99 | -1.40 | -1.39 | 0.42 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 8437 | 大地-KY | biotechnology | mainstream_leader | 225.00 | tdcc_price_divergence | -8.77 | -6.10 | -7.92 | 0.34 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6988 | 威力暘-創 | other | single_name_signal | 225.00 | tdcc_price_divergence | -7.95 | -14.75 | -12.22 | 0.46 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3588 | 通嘉 | other electronics | mainstream_leader | 225.00 | tdcc_price_divergence | -7.87 | -10.57 | -6.85 | 0.49 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4439 | 冠星-KY | other | single_name_signal | 225.00 | tdcc_price_divergence | -6.63 | -1.44 | -2.20 | 1.26 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6509 | 聚和 | biotechnology | mainstream_leader | 225.00 | tdcc_price_divergence | -0.86 | -5.32 | -5.56 | 0.03 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2911 | 麗嬰房 | traditional industries | mainstream_leader | 215.00 | tdcc_price_divergence | 71.34 | -10.47 | 9.11 | 1.20 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 7768 | 頌勝科技 | other | single_name_signal | 215.00 | tdcc_price_divergence | 12.50 | -0.56 | -1.50 | 0.27 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3092 | 鴻碩 | semiconductor | non_mainstream_watch | 215.00 | tdcc_price_divergence | -6.49 | -3.69 | -2.94 | 0.42 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 4961 | 天鈺 | other electronics | mainstream_leader | 215.00 | tdcc_price_divergence | -6.48 | -3.61 | -3.33 | 0.41 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6655 | 科定 | other electronics | mainstream_leader | 215.00 | tdcc_price_divergence | -12.68 | -6.75 | -7.80 | 0.10 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 3605 | 宏致 | other electronics | mainstream_leader | 215.00 | tdcc_price_divergence | -10.39 | -9.02 | -6.23 | 0.55 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 6570 | 維田 | biotechnology | mainstream_leader | 205.00 | tdcc_price_divergence | 30.23 | -7.13 | 6.17 | 0.55 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2476 | 鉅祥 | other electronics | mainstream_leader | 205.00 | tdcc_price_divergence | 3.80 | -4.85 | 1.88 | 0.48 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 2114 | 鑫永銓 | traditional industries | mainstream_leader | 205.00 | tdcc_price_divergence | 2.39 | -0.06 | -0.83 | 0.89 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |
| 5234 | 達興材料 | semiconductor equipment/materials | non_mainstream_watch | 205.00 | tdcc_price_divergence | -9.82 | -9.79 | -5.01 | 0.32 | strong_but_divergent | TDCC 增加但股價轉弱，需防訊號失效。 |

## Phase Distribution

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 840.0 | 76.78 |
| price_leading_tdcc | 113.0 | 10.33 |
| tdcc_price_divergence | 65.0 | 5.94 |
| tdcc_leading_price | 35.0 | 3.20 |
| overheated_after_tdcc | 35.0 | 3.20 |
| tdcc_price_confirmed | 5.0 | 0.46 |
| failed_after_tdcc | 1.0 | 0.09 |

## Consecutive Weeks x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 403.0 |
| 1 | overheated_after_tdcc | 9.0 |
| 1 | price_leading_tdcc | 21.0 |
| 2 | insufficient_price_context | 153.0 |
| 2 | overheated_after_tdcc | 8.0 |
| 2 | price_leading_tdcc | 32.0 |
| 2 | tdcc_leading_price | 7.0 |
| 2 | tdcc_price_confirmed | 2.0 |
| 2 | tdcc_price_divergence | 17.0 |
| 3 | insufficient_price_context | 90.0 |
| 3 | overheated_after_tdcc | 7.0 |
| 3 | price_leading_tdcc | 13.0 |
| 3 | tdcc_leading_price | 6.0 |
| 3 | tdcc_price_divergence | 15.0 |
| 4 | insufficient_price_context | 59.0 |
| 4 | overheated_after_tdcc | 5.0 |
| 4 | price_leading_tdcc | 17.0 |
| 4 | tdcc_leading_price | 3.0 |
| 4 | tdcc_price_divergence | 12.0 |
| 5 | insufficient_price_context | 36.0 |
| 5 | overheated_after_tdcc | 2.0 |
| 5 | price_leading_tdcc | 12.0 |
| 5 | tdcc_leading_price | 1.0 |
| 5 | tdcc_price_confirmed | 1.0 |
| 5 | tdcc_price_divergence | 8.0 |
| 6 | failed_after_tdcc | 1.0 |
| 6 | insufficient_price_context | 86.0 |
| 6 | overheated_after_tdcc | 4.0 |
| 6 | price_leading_tdcc | 16.0 |
| 6 | tdcc_leading_price | 14.0 |
| 6 | tdcc_price_confirmed | 2.0 |
| 6 | tdcc_price_divergence | 8.0 |
| 7 | insufficient_price_context | 13.0 |
| 7 | price_leading_tdcc | 2.0 |
| 7 | tdcc_leading_price | 4.0 |
| 7 | tdcc_price_divergence | 5.0 |

## Mature Performance Summary

只使用 mature_dN=True 的資料。pending 不可視為正面或負面。

- phase-level mature sample 已可使用。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 0.0 |  |  | 0.0 |  |  | 0.0 |  |  |  |  |
| insufficient_price_context | 26.0 | 5.21 | 3.03 | 18.0 | 14.38 | 7.79 | 11.0 | 10.70 | 5.78 | 24.57 | -6.95 |
| overheated_after_tdcc | 57.0 | 5.54 | 2.72 | 39.0 | 16.22 | 10.14 | 16.0 | 22.64 | 17.96 | 24.48 | -6.54 |
| price_leading_tdcc | 26.0 | 6.24 | 4.19 | 16.0 | 9.09 | 3.09 | 8.0 | -1.66 | -6.99 | 19.56 | -5.94 |
| tdcc_leading_price | 7.0 | 4.36 | 1.40 | 6.0 | 2.15 | -5.78 | 5.0 | -2.69 | -6.85 | 11.42 | -5.64 |
| tdcc_price_confirmed | 2.0 | 5.29 | 0.47 | 2.0 | 21.87 | 20.03 | 0.0 |  |  | 23.17 | -3.99 |
| tdcc_price_divergence | 1.0 | -1.74 | -4.68 | 1.0 | 19.34 | 11.44 | 1.0 | 5.75 | 3.67 | 19.34 | -11.15 |

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

## TDCC Weekly Increase and Consecutive Candidate Reports

- 精華版與完整版由 report-ready CSV/MD/PDF 產出。
- 精華版包含當週增幅、連續累積、當週增幅 x TDCC 短線延續 D+5/D+10、連續累積 x TDCC 短線延續 D+5/D+10，各最多前十名。
- 完整版使用相同四個清單，各最多列前五十名；不足五十就全列。

- tdcc_weekly_candidate_highlight_for_report_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv
- tdcc_weekly_candidate_highlight_for_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_for_report_latest.md
- tdcc_weekly_candidate_full_for_report_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_for_report_latest.csv
- tdcc_weekly_candidate_full_for_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_for_report_latest.md
- tdcc_weekly_candidate_highlight_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_highlight_latest.pdf
- tdcc_weekly_candidate_full_pdf_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/tdcc_weekly_candidate_full_latest.pdf
- tdcc_weekly_candidate_highlight_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_candidate_highlight_latest.pdf
- tdcc_weekly_candidate_full_pdf_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/tdcc_weekly_candidate_full_latest.pdf
