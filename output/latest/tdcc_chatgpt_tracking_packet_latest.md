# TDCC CHATGPT TRACKING PACKET

## Metadata
- generated_at: 2026-05-25 12:50:57 Asia/Taipei
- main_price_date: 20260524
- latest_tdcc_signal_date: 20260522
- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md
- overall_mature_d5_count: 3592
- phase_mature_d5_count: 3592
- overall_mature_d10_count: 2457
- phase_mature_d10_count: 2457
- overall_mature_d20_count: 1229
- phase_mature_d20_count: 1229
- pending_count: 1201
- insufficient_sample_count: 472
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- sample_status: phase_samples_available
- relaxed_filter: False
- missing_columns: none

## Data Availability
- tdcc_signal_snapshot.csv: yes
- tdcc_normalized_signal_log.csv: yes
- tdcc_signal_performance.csv: yes
- tdcc_pre_move_accumulation_history.csv: yes
- tdcc_pre_move_accumulation_latest.csv: yes
- tdcc_signal_effectiveness_latest.md: yes

## Data Quality Notes
- missing_columns: none
- ranking_quality: complete
- phase_mature_join_quality: ok
- benchmark_available: yes
- sample_status: phase_samples_available
- relaxed_filter: False
- packet_generated_from: snapshot + ABM latest + normalized performance + phase distribution

## TDCC Strength Ranking Top 30

| rank | stock_id | stock_name | theme | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | abm_score | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | risk_label | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1323 | 永裕 | other | 415.00 | 25 | True | True | tdcc_leading_price | quiet_accumulation | 96.00 | 4.15 | -9.66 | 2.82 | 0.78 | 0.54 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 2 | 1460 | 宏遠 | other | 415.00 | 25 | True | True | tdcc_price_divergence | watch_only | 76.00 | -0.85 | 3.71 | -5.32 | -0.81 | 0.70 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 3 | 3434 | 哲固 | other | 415.00 | 25 | True | True | tdcc_leading_price | quiet_accumulation | 82.00 | 2.29 | -4.29 | -2.15 | 0.72 | 0.00 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 4 | 6576 | 逸達 | other | 415.00 | 25 | True | True | tdcc_leading_price | quiet_accumulation | 90.00 | 1.90 | -0.62 | -1.47 | 0.26 | 0.00 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 5 | 2816 | 旺旺保 | other | 325.00 | 16 | True | True | tdcc_leading_price | quiet_accumulation | 92.00 | 2.31 | 1.64 | 0.38 | 1.22 | 0.40 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 6 | 7718 | 友鋮 | other | 315.00 | 15 | True | True | tdcc_leading_price | quiet_accumulation | 95.00 | 3.31 | 5.61 | -1.85 | 3.21 | 0.00 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 7 | 1734 | 杏輝 | other | 305.00 | 14 | True | True | tdcc_leading_price | quiet_accumulation | 89.00 | 0.49 | -3.45 | -1.27 | -0.93 | 0.90 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 8 | 8409 | 商之器 | other | 295.00 | 13 | True | True | tdcc_leading_price | quiet_accumulation | 82.00 | 4.18 | -0.25 | -1.59 | 1.94 | 0.00 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 9 | 1452 | 宏益 | other | 285.00 | 12 | True | True | tdcc_price_divergence | quiet_accumulation | 76.00 | -2.75 | -8.23 | -6.95 | -4.35 | 0.58 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 10 | 1474 | 弘裕 | other | 285.00 | 12 | True | True | tdcc_price_divergence | quiet_accumulation | 78.00 | -1.41 | -2.87 | -3.98 | -1.56 | 2.95 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 11 | 3313 | 斐成 | other | 265.00 | 10 | True | True | tdcc_leading_price | quiet_accumulation | 90.00 | 6.79 | -4.07 | -2.52 | 0.83 | 0.00 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 12 | 1584 | 精剛 | other | 255.00 | 9 | True | True | tdcc_price_divergence | watch_only | 66.00 | -0.51 | -3.68 | -5.61 | -1.12 | 0.00 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 13 | 1471 | 首利 | other | 245.00 | 8 | True | True | tdcc_price_divergence | quiet_accumulation | 77.00 | 5.85 | -8.82 | -3.85 | -1.30 | 0.95 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 14 | 1805 | 寶徠 | other | 245.00 | 8 | True | True | tdcc_price_divergence | quiet_accumulation | 85.00 | -0.49 | -4.27 | -7.64 | -3.42 | 1.71 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 15 | 1414 | 東和 | other | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 75.00 | -0.96 | -4.63 | -6.23 | -4.42 | 0.88 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 16 | 1438 | 三地開發 | other | 235.00 | 7 | True | True | failed_after_tdcc | quiet_accumulation | 62.00 | 0.98 | -23.33 | -0.37 | -4.26 | 0.25 | 10.00 | divergence_failed_watch | strong_but_divergent | 訊號後價格走弱，列為失效觀察。 |
| 17 | 1626 | 艾美特-KY | other | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 76.00 | -0.40 | -9.45 | -10.64 | -6.33 | 0.35 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 18 | 1799 | 易威 | other | 235.00 | 7 | True | True | tdcc_price_divergence | quiet_accumulation | 80.00 | -5.53 | -15.57 | -8.51 | -6.94 | 0.00 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 19 | 3038 | 全台 | other | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 97.00 | 2.89 | 0.43 | -0.28 | 1.68 | 1.68 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 20 | 1443 | 立益物流 | other | 225.00 | 6 | True | True | tdcc_price_divergence | strong_momentum | 62.00 | -0.38 | 16.26 | -4.21 | 5.59 | 0.26 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 21 | 1614 | 三洋電 | other | 225.00 | 6 | True | True | tdcc_price_divergence | quiet_accumulation | 79.00 | -0.65 | -3.75 | -5.35 | -2.25 | 0.90 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 22 | 1617 | 榮星 | other | 225.00 | 6 | True | True | tdcc_price_divergence | watch_only | 75.00 | 4.20 | -2.93 | -2.59 | 0.15 | 1.93 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 23 | 1723 | 中碳 | other | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 97.00 | 3.03 | 1.11 | 0.66 | 2.88 | 1.01 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 24 | 1760 | 寶齡富錦 | other | 225.00 | 6 | True | True | tdcc_price_divergence | quiet_accumulation | 70.00 | 0.98 | -4.19 | -5.63 | -3.36 | 0.34 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 25 | 6534 | 正瀚-創 | other | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 97.00 | 0.10 | -1.82 | -0.34 | 1.55 | 1.26 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 26 | 1308 | 亞聚 | other | 215.00 | 5 | True | True | tdcc_price_divergence | quiet_accumulation | 62.00 | 2.31 | -15.02 | -2.34 | -3.83 | 0.69 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 27 | 1527 | 鑽全 | other | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 100.00 | 2.81 | 2.17 | 0.10 | 1.35 | 1.65 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |
| 28 | 1535 | 中宇 | other | 215.00 | 5 | True | True | tdcc_price_divergence | quiet_accumulation | 96.00 | 0.41 | -3.42 | -3.29 | -1.29 | 0.55 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 29 | 1906 | 寶隆 | other | 215.00 | 5 | True | True | tdcc_price_divergence | quiet_accumulation | 69.00 | -0.94 | -9.09 | -6.14 | -4.04 | 2.03 | 10.00 | divergence_failed_watch | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 30 | 2024 | 志聯 | other | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 95.00 | 5.60 | -1.74 | -0.16 | 1.96 | 1.69 | 10.00 | potential_accumulation | strong_but_pre_move | 籌碼強，但股價尚未明顯反應。 |

## Pre-Move Accumulation / ABM Top 30

| abm_rank | stock_id | stock_name | theme | abm_score | tdcc_strength_score | tdcc_consecutive_up_weeks | all_thresholds_up | high_thresholds_up | tdcc_price_phase | setup_type | price_return_5d | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | theme_breadth_score | accumulation_label | tracking_priority | trigger_to_watch | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1723 | 中碳 | other | 97.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 3.03 | 1.11 | 0.66 | 2.88 | 1.01 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 2 | 5876 | 上海商銀 | other | 97.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -0.12 | 0.12 | 1.36 | 1.33 | 1.06 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 3 | 3617 | 碩天 | other | 95.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 5.53 | 4.16 | 0.18 | 3.82 | 1.33 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 4 | 1733 | 五鼎 | other | 95.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | 3.13 | 2.95 | 2.99 | 3.08 | 0.82 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 5 | 2535 | 達欣工 | other | 95.00 | 195.00 | 6 | False | True | tdcc_leading_price | quiet_accumulation | 3.20 | 2.65 | 2.85 | 3.83 | 1.05 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 6 | 1409 | 新纖 | other | 95.00 | 155.00 | 2 | False | True | tdcc_leading_price | quiet_accumulation | 2.08 | 2.38 | 0.78 | 2.02 | 1.18 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 7 | 3045 | 台灣大 | other | 93.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -2.18 | 0.00 | 0.22 | -0.13 | 1.38 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 8 | 9946 | 三發地產 | other | 93.00 | 175.00 | 4 | False | True | tdcc_leading_price | quiet_accumulation | 0.00 | 2.75 | 2.43 | 2.77 | 0.81 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 9 | 2816 | 旺旺保 | other | 92.00 | 325.00 | 16 | True | True | tdcc_leading_price | quiet_accumulation | 2.31 | 1.64 | 0.38 | 1.22 | 0.40 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 10 | 3413 | 京鼎 | other | 92.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -0.15 | 3.01 | 1.42 | 2.69 | 0.44 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 11 | 8342 | 益張 | other | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 3.60 | -1.92 | 1.05 | 1.26 | 0.01 | 10.00 | prime_pre_move | A_prime_watch | 量縮守住 MA20；相對 benchmark 維持轉強；避免爆量長上影 | 籌碼強，但股價尚未明顯反應。 |
| 12 | 3038 | 全台 | other | 97.00 | 235.00 | 7 | True | True | tdcc_leading_price | quiet_accumulation | 2.89 | 0.43 | -0.28 | 1.68 | 1.68 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；量能降溫後再確認 | 籌碼強，但股價尚未明顯反應。 |
| 13 | 6534 | 正瀚-創 | other | 97.00 | 225.00 | 6 | True | True | tdcc_leading_price | quiet_accumulation | 0.10 | -1.82 | -0.34 | 1.55 | 1.26 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 14 | 3705 | 永信 | other | 97.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | -0.71 | 1.46 | -0.87 | 0.32 | 1.04 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 15 | 1323 | 永裕 | other | 96.00 | 415.00 | 25 | True | True | tdcc_leading_price | quiet_accumulation | 4.15 | -9.66 | 2.82 | 0.78 | 0.54 | 10.00 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；溫和放量站上 5 日 / 10 日均線；股價止跌並族群同步轉強 | 籌碼強，但股價尚未明顯反應。 |
| 16 | 4905 | 台聯電 | other | 96.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 2.05 | -8.59 | -3.25 | 0.13 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線；股價止跌並族群同步轉強 | 籌碼強，但股價尚未明顯反應。 |
| 17 | 7718 | 友鋮 | other | 95.00 | 315.00 | 15 | True | True | tdcc_leading_price | quiet_accumulation | 3.31 | 5.61 | -1.85 | 3.21 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 18 | 2024 | 志聯 | other | 95.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 5.60 | -1.74 | -0.16 | 1.96 | 1.69 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；量能降溫後再確認 | 籌碼強，但股價尚未明顯反應。 |
| 19 | 5511 | 德昌 | other | 92.00 | 195.00 | 3 | True | True | tdcc_leading_price | quiet_accumulation | -0.69 | 2.42 | -1.82 | 1.10 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 20 | 2035 | 唐榮 | other | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 2.72 | 0.18 | -1.58 | 1.02 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 21 | 2412 | 中華電 | other | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | -0.72 | 0.74 | -1.23 | 0.05 | 0.60 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 22 | 5209 | 新鼎 | other | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 0.91 | 0.60 | -1.85 | 1.08 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 23 | 5609 | 中菲行 | other | 92.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 1.64 | 1.64 | -2.24 | 1.71 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 24 | 6576 | 逸達 | other | 90.00 | 415.00 | 25 | True | True | tdcc_leading_price | quiet_accumulation | 1.90 | -0.62 | -1.47 | 0.26 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 25 | 3313 | 斐成 | other | 90.00 | 265.00 | 10 | True | True | tdcc_leading_price | quiet_accumulation | 6.79 | -4.07 | -2.52 | 0.83 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線；股價止跌並族群同步轉強 | 籌碼強，但股價尚未明顯反應。 |
| 26 | 1233 | 天仁 | other | 90.00 | 205.00 | 4 | True | True | tdcc_leading_price | quiet_accumulation | 0.00 | 1.41 | -1.60 | 0.11 | 0.22 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 27 | 1734 | 杏輝 | other | 89.00 | 305.00 | 14 | True | True | tdcc_leading_price | quiet_accumulation | 0.49 | -3.45 | -1.27 | -0.93 | 0.90 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；站回 MA20；溫和放量站上 5 日 / 10 日均線；股價止跌並族群同步轉強 | 籌碼強，但股價尚未明顯反應。 |
| 28 | 2414 | 精技 | other | 88.00 | 185.00 | 2 | True | True | tdcc_leading_price | quiet_accumulation | 3.93 | 9.13 | 1.06 | 5.30 | 0.91 | 10.00 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 29 | 2606 | 裕民 | other | 88.00 | 165.00 | 3 | False | True | tdcc_leading_price | quiet_accumulation | 4.14 | 6.51 | -0.98 | 3.40 | 0.88 | 10.00 | prime_pre_move | B_confirm_needed | 相對 benchmark 轉正；量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |
| 30 | 4744 | 皇將 | other | 87.00 | 215.00 | 5 | True | True | tdcc_leading_price | quiet_accumulation | 1.21 | 6.01 | 0.02 | 1.91 | 0.00 | 10.00 | prime_pre_move | B_confirm_needed | 量縮守住 MA20；溫和放量站上 5 日 / 10 日均線 | 籌碼強，但股價尚未明顯反應。 |

## Top Risk List - price_leading_tdcc Top 20

| stock_id | stock_name | theme | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4908 | 前鼎 | other | 195.00 | price_leading_tdcc | 51.70 | 12.97 | 17.79 | 0.00 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2233 | 宇隆 | other | 195.00 | price_leading_tdcc | 44.89 | 17.24 | 15.64 | 2.04 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3707 | 漢磊 | semiconductor | 195.00 | price_leading_tdcc | 44.21 | 10.70 | 16.22 | 0.00 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8390 | 金益鼎 | other | 195.00 | price_leading_tdcc | 41.68 | 24.15 | 18.22 | 0.00 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8926 | 台汽電 | other | 195.00 | price_leading_tdcc | 34.14 | 22.44 | 17.42 | 0.89 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2355 | 敬鵬 | PCB/CCL | 195.00 | price_leading_tdcc | 29.37 | 24.27 | 19.21 | 2.53 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6446 | 藥華藥 | other | 195.00 | price_leading_tdcc | 28.78 | 10.28 | 13.34 | 0.42 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2356 | 英業達 | other | 195.00 | price_leading_tdcc | 28.51 | 18.48 | 18.86 | 2.75 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 8105 | 凌巨 | other | 195.00 | price_leading_tdcc | 25.63 | 26.82 | 19.63 | 2.30 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3035 | 智原 | other | 195.00 | price_leading_tdcc | 25.22 | 16.94 | 12.61 | 1.42 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2363 | 矽統 | other | 195.00 | price_leading_tdcc | 23.29 | 10.69 | 14.19 | 2.18 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3356 | 奇偶 | other | 195.00 | price_leading_tdcc | 21.73 | 13.29 | 9.94 | 1.49 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6113 | 亞矽 | other | 195.00 | price_leading_tdcc | 20.52 | 9.05 | 15.25 | 0.00 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6282 | 康舒 | other | 195.00 | price_leading_tdcc | 19.58 | 12.29 | 13.33 | 2.22 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 3191 | 雲嘉南 | other | 195.00 | price_leading_tdcc | 19.57 | 17.95 | 16.09 | 0.00 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 1447 | 力鵬 | other | 195.00 | price_leading_tdcc | 17.88 | 19.62 | 14.65 | 1.05 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 6988 | 威力暘-創 | other | 195.00 | price_leading_tdcc | 17.61 | 13.58 | 10.60 | 1.11 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 4155 | 訊映 | other | 195.00 | price_leading_tdcc | 16.92 | 14.88 | 11.15 | 1.07 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 2425 | 承啟 | other | 195.00 | price_leading_tdcc | 16.84 | 10.88 | 7.71 | 0.73 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |
| 5488 | 松普 | other | 195.00 | price_leading_tdcc | 15.96 | 10.98 | 11.66 | 0.00 | strong_but_late | 股價已先漲，TDCC 訊號可能偏晚。 |

## Top Risk List - overheated_after_tdcc Top 20

| stock_id | stock_name | theme | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6834 | 天二科技 | other | 195.00 | overheated_after_tdcc | 99.15 | 44.97 | 51.39 | 3.09 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 3048 | 益登 | semiconductor | 195.00 | overheated_after_tdcc | 94.52 | 74.11 | 55.25 | 1.58 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 8040 | 九暘 | other | 195.00 | overheated_after_tdcc | 83.36 | 49.58 | 42.65 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 3624 | 光頡 | passive components | 195.00 | overheated_after_tdcc | 75.96 | 51.71 | 37.72 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 3236 | 千如 | other | 195.00 | overheated_after_tdcc | 75.50 | 52.51 | 46.26 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2911 | 麗嬰房 | other | 195.00 | overheated_after_tdcc | 73.80 | 68.46 | 52.76 | 1.90 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2375 | 凱美 | passive components | 195.00 | overheated_after_tdcc | 66.87 | 47.19 | 39.81 | 2.95 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 6207 | 雷科 | other | 195.00 | overheated_after_tdcc | 59.12 | 37.98 | 27.54 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 8069 | 元太 | other | 195.00 | overheated_after_tdcc | 52.38 | 34.90 | 24.72 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 8121 | 越峰 | other | 195.00 | overheated_after_tdcc | 48.68 | 25.04 | 22.82 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 6116 | 彩晶 | other | 195.00 | overheated_after_tdcc | 40.40 | 27.21 | 24.47 | 1.26 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 6237 | 驊訊 | other | 195.00 | overheated_after_tdcc | 39.62 | 22.17 | 25.44 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2428 | 興勤 | other | 195.00 | overheated_after_tdcc | 39.37 | 25.70 | 22.97 | 1.14 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2316 | 楠梓電 | other | 195.00 | overheated_after_tdcc | 34.06 | 34.85 | 21.44 | 1.66 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 4991 | 環宇-KY | other | 195.00 | overheated_after_tdcc | 28.19 | 23.02 | 19.19 | 0.00 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2401 | 凌陽 | other | 195.00 | overheated_after_tdcc | 24.24 | 19.95 | 20.92 | 4.26 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 1582 | 信錦 | other | 195.00 | overheated_after_tdcc | 23.66 | 29.38 | 18.90 | 1.99 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 3704 | 合勤控 | other | 195.00 | overheated_after_tdcc | 23.08 | 23.05 | 20.20 | 3.20 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2492 | 華新科 | passive components | 195.00 | overheated_after_tdcc | 125.00 | 85.90 | 60.65 | 0.57 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |
| 2327 | 國巨* | other | 195.00 | overheated_after_tdcc | 113.22 | 60.10 | 52.96 | 1.30 | strong_but_overheated | 籌碼強但股價已過熱，防追高。 |

## Top Risk List - tdcc_price_divergence Top 20

| stock_id | stock_name | theme | tdcc_strength_score | tdcc_price_phase | price_return_20d | relative_return_vs_benchmark | distance_ma20_pct | volume_ratio_20d | risk_bucket | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1460 | 宏遠 | other | 415.00 | tdcc_price_divergence | 3.71 | -5.32 | -0.81 | 0.70 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1452 | 宏益 | other | 285.00 | tdcc_price_divergence | -8.23 | -6.95 | -4.35 | 0.58 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1474 | 弘裕 | other | 285.00 | tdcc_price_divergence | -2.87 | -3.98 | -1.56 | 2.95 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1584 | 精剛 | other | 255.00 | tdcc_price_divergence | -3.68 | -5.61 | -1.12 | 0.00 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1471 | 首利 | other | 245.00 | tdcc_price_divergence | -8.82 | -3.85 | -1.30 | 0.95 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1805 | 寶徠 | other | 245.00 | tdcc_price_divergence | -4.27 | -7.64 | -3.42 | 1.71 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1626 | 艾美特-KY | other | 235.00 | tdcc_price_divergence | -9.45 | -10.64 | -6.33 | 0.35 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1414 | 東和 | other | 235.00 | tdcc_price_divergence | -4.63 | -6.23 | -4.42 | 0.88 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1799 | 易威 | other | 235.00 | tdcc_price_divergence | -15.57 | -8.51 | -6.94 | 0.00 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1443 | 立益物流 | other | 225.00 | tdcc_price_divergence | 16.26 | -4.21 | 5.59 | 0.26 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1760 | 寶齡富錦 | other | 225.00 | tdcc_price_divergence | -4.19 | -5.63 | -3.36 | 0.34 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1614 | 三洋電 | other | 225.00 | tdcc_price_divergence | -3.75 | -5.35 | -2.25 | 0.90 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1617 | 榮星 | other | 225.00 | tdcc_price_divergence | -2.93 | -2.59 | 0.15 | 1.93 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1906 | 寶隆 | other | 215.00 | tdcc_price_divergence | -9.09 | -6.14 | -4.04 | 2.03 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1535 | 中宇 | other | 215.00 | tdcc_price_divergence | -3.42 | -3.29 | -1.29 | 0.55 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1308 | 亞聚 | other | 215.00 | tdcc_price_divergence | -15.02 | -2.34 | -3.83 | 0.69 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1325 | 恆大 | other | 205.00 | tdcc_price_divergence | 0.76 | -4.16 | -0.42 | 0.89 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1305 | 華夏 | other | 205.00 | tdcc_price_divergence | -17.61 | -4.34 | -6.85 | 0.76 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1410 | 南染 | other | 205.00 | tdcc_price_divergence | -16.40 | -5.58 | -4.07 | 0.15 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |
| 1304 | 台聚 | other | 205.00 | tdcc_price_divergence | -16.04 | -4.75 | -5.98 | 0.71 | strong_but_divergent | TDCC 增加但股價轉弱，需防失效。 |

## Phase Distribution

| tdcc_price_phase | sample_count | pct_of_total |
| --- | --- | --- |
| insufficient_price_context | 472.0 | 39.50 |
| tdcc_price_divergence | 337.0 | 28.20 |
| tdcc_leading_price | 159.0 | 13.31 |
| price_leading_tdcc | 119.0 | 9.96 |
| overheated_after_tdcc | 85.0 | 7.11 |
| tdcc_price_confirmed | 18.0 | 1.51 |
| failed_after_tdcc | 5.0 | 0.42 |

## Consecutive Weeks x Phase

| tdcc_consecutive_up_weeks | tdcc_price_phase | signal_count |
| --- | --- | --- |
| 1 | insufficient_price_context | 391.0 |
| 1 | overheated_after_tdcc | 28.0 |
| 1 | price_leading_tdcc | 38.0 |
| 10 | tdcc_leading_price | 1.0 |
| 12 | tdcc_price_divergence | 2.0 |
| 13 | tdcc_leading_price | 1.0 |
| 14 | tdcc_leading_price | 1.0 |
| 15 | tdcc_leading_price | 1.0 |
| 16 | tdcc_leading_price | 1.0 |
| 2 | failed_after_tdcc | 2.0 |
| 2 | insufficient_price_context | 37.0 |
| 2 | overheated_after_tdcc | 18.0 |
| 2 | price_leading_tdcc | 33.0 |
| 2 | tdcc_leading_price | 54.0 |
| 2 | tdcc_price_confirmed | 7.0 |
| 2 | tdcc_price_divergence | 101.0 |
| 25 | tdcc_leading_price | 3.0 |
| 25 | tdcc_price_divergence | 1.0 |
| 3 | failed_after_tdcc | 2.0 |
| 3 | insufficient_price_context | 42.0 |
| 3 | overheated_after_tdcc | 39.0 |
| 3 | price_leading_tdcc | 48.0 |
| 3 | tdcc_leading_price | 81.0 |
| 3 | tdcc_price_confirmed | 11.0 |
| 3 | tdcc_price_divergence | 216.0 |
| 4 | insufficient_price_context | 2.0 |
| 4 | tdcc_leading_price | 6.0 |
| 4 | tdcc_price_divergence | 4.0 |
| 5 | tdcc_leading_price | 6.0 |
| 5 | tdcc_price_divergence | 3.0 |
| 6 | tdcc_leading_price | 3.0 |
| 6 | tdcc_price_divergence | 4.0 |
| 7 | failed_after_tdcc | 1.0 |
| 7 | tdcc_leading_price | 1.0 |
| 7 | tdcc_price_divergence | 3.0 |
| 8 | tdcc_price_divergence | 2.0 |
| 9 | tdcc_price_divergence | 1.0 |

## Mature Performance Summary

只使用 mature_dN=True 的資料。pending 不可視為正面或負面。

- phase-level mature sample 已可用。

| tdcc_price_phase | mature_sample_d5 | avg_ret_d5 | avg_relative_ret_d5 | mature_sample_d10 | avg_ret_d10 | avg_relative_ret_d10 | mature_sample_d20 | avg_ret_d20 | avg_relative_ret_d20 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed_after_tdcc | 12.0 | -0.55 | -4.77 | 8.0 | 2.48 | -7.86 | 8.0 | -2.46 | -18.51 | 6.32 | -5.13 |
| insufficient_price_context | 1907.0 | 0.31 | -0.67 | 1482.0 | 1.57 | -1.28 | 467.0 | 0.71 | -8.60 | 6.93 | -5.23 |
| overheated_after_tdcc | 133.0 | 4.42 | 3.40 | 73.0 | 9.38 | 7.10 | 5.0 | 1.16 | -8.88 | 17.53 | -9.59 |
| price_leading_tdcc | 149.0 | 4.43 | 2.58 | 83.0 | 4.14 | 0.98 | 33.0 | -2.52 | -14.22 | 12.97 | -6.74 |
| tdcc_leading_price | 569.0 | 0.87 | -1.54 | 380.0 | -0.22 | -4.47 | 358.0 | -0.34 | -9.03 | 3.90 | -3.54 |
| tdcc_price_confirmed | 44.0 | 3.51 | 1.33 | 23.0 | -0.44 | -2.91 | 22.0 | -3.90 | -12.75 | 8.76 | -5.99 |
| tdcc_price_divergence | 778.0 | 0.79 | -1.86 | 408.0 | -0.32 | -4.58 | 336.0 | 0.49 | -8.25 | 4.67 | -3.90 |

## Interpretation Rules
- pending 不可視為正面或負面。
- same stock_id + signal_date 只能算一筆 normalized signal。
- TDCC Strength Ranking 找籌碼最強，不等於潛伏吸籌。
- Pre-Move / ABM Ranking 才是找潛伏吸籌。
- price_leading_tdcc / overheated_after_tdcc 不可寫成潛伏吸籌。
- tdcc_price_divergence 要列為失效觀察。
- 必須同時看絕對報酬與相對 TWSE / TPEx benchmark。
