# 營收爆發但股價尚未反應模型：收盤確認時點稽核

- generated_at: `2026-08-23 06:52:52 Asia/Taipei`
- status: `research_only_not_promotion_ready`
- 候選池：強月營收條件使用 `source_table_date <= signal_date` 的歷史 as-of join，股價仍在近期 23 日區間且攻擊尚未開始。
- 三個研究分支分開回放與計算，績效不得混算：隔日續強確認型、區間突破確認型、均線站回確認型。
- 進場：確認日收盤後才成立，次一交易日開盤進場。
- 出場時鐘：同時比較原訊號日 D+20 收盤與確認日 D+20 收盤；本稽核不加停損，先隔離確認時點效果。
- 勝／和／敗：報酬 >= +5% 為勝；0% 至未滿 +5% 為和；報酬 < 0% 為敗。
- 去重：逐股 chronological lifecycle replay；待確認與持有期間的後續同股訊號全部壓掉。
- 樣本數只揭露，不會單獨作為否定研究分支的理由。
- scope：僅使用月營收；EPS、毛利率、營益率、營業利益、業外、淨利與季／年財報不在本輪範圍。
- production_change: `none`

## 三分支績效

| confirmation_variant_name_zh | pending_window_days | exit_clock_name_zh | pending_episode_count | confirmation_rate_pct | accepted_trade_count | win_rate_pct | neutral_rate_pct | failure_rate_pct | avg_realized_return_pct | median_realized_return_pct | high_return_8_rate_pct | loss_5_rate_pct | avoided_failure_count | missed_win_count | avg_timing_cost_vs_direct_signal_d20_pct | same_stock_overlap_pair_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 訊號日直接進場對照組 | 0 | 維持原訊號日 D+20 收盤 | 6823.0 | 100.0 | 6045.0 | 28.1886 | 18.6931 | 53.1183 | 2.0231 | -0.7692 | 22.2002 | 31.1828 | 0.0 | 0.0 | 0.0 | 0.0 |
| 隔日續強確認型 | 1 | 維持原訊號日 D+20 收盤 | 12838.0 | 46.885 | 5354.0 | 27.0078 | 17.7064 | 55.2858 | 1.5093 | -1.1628 | 21.5913 | 31.9014 | 3624.0 | 1381.0 | -1.7453 | 0.0 |
| 隔日續強確認型 | 1 | 確認日 D+20 收盤 | 12577.0 | 46.3371 | 5153.0 | 27.518 | 15.9907 | 56.4914 | 1.5725 | -1.476 | 21.6767 | 32.3307 | 3536.0 | 1384.0 | -1.6361 | 0.0 |
| 區間突破確認型 | 3 | 維持原訊號日 D+20 收盤 | 22277.0 | 10.1529 | 2058.0 | 31.2439 | 13.5083 | 55.2478 | 2.478 | -1.2869 | 25.8989 | 34.208 | 9812.0 | 4184.0 | -6.3787 | 0.0 |
| 區間突破確認型 | 3 | 確認日 D+20 收盤 | 21752.0 | 10.2819 | 2021.0 | 32.2118 | 13.7556 | 54.0327 | 2.8271 | -1.4205 | 26.1257 | 35.329 | 9571.0 | 4072.0 | -6.0115 | 0.0 |
| 區間突破確認型 | 5 | 維持原訊號日 D+20 收盤 | 15901.0 | 15.4902 | 2201.0 | 31.6674 | 13.7665 | 54.5661 | 2.4994 | -1.1679 | 25.761 | 33.0759 | 6693.0 | 2657.0 | -7.6745 | 0.0 |
| 區間突破確認型 | 5 | 確認日 D+20 收盤 | 15429.0 | 15.5095 | 2126.0 | 32.7375 | 13.4525 | 53.81 | 2.7864 | -1.3226 | 27.1872 | 35.4657 | 6445.0 | 2575.0 | -6.9712 | 0.0 |
| 區間突破確認型 | 10 | 維持原訊號日 D+20 收盤 | 10024.0 | 26.6183 | 2333.0 | 30.1757 | 14.7878 | 55.0364 | 2.0625 | -1.4134 | 24.3892 | 33.0476 | 4041.0 | 1195.0 | -8.6997 | 0.0 |
| 區間突破確認型 | 10 | 確認日 D+20 收盤 | 9586.0 | 26.4094 | 2176.0 | 32.261 | 13.0974 | 54.6415 | 2.7017 | -1.4878 | 26.6085 | 36.8107 | 3829.0 | 1107.0 | -7.7805 | 0.0 |
| 均線站回確認型 | 3 | 維持原訊號日 D+20 收盤 | 13575.0 | 36.9067 | 4290.0 | 28.2284 | 15.9207 | 55.8508 | 1.7304 | -1.2615 | 22.2611 | 33.007 | 4298.0 | 1468.0 | -2.7496 | 0.0 |
| 均線站回確認型 | 3 | 確認日 D+20 收盤 | 12966.0 | 37.4702 | 4118.0 | 27.8048 | 15.2501 | 56.9451 | 1.5607 | -1.6667 | 22.2924 | 35.3084 | 4082.0 | 1366.0 | -2.6747 | 0.0 |
| 均線站回確認型 | 5 | 維持原訊號日 D+20 收盤 | 10505.0 | 49.8316 | 4416.0 | 27.9438 | 16.3043 | 55.7518 | 1.77 | -1.3953 | 22.1241 | 32.3822 | 2786.0 | 816.0 | -3.0931 | 0.0 |
| 均線站回確認型 | 5 | 確認日 D+20 收盤 | 10031.0 | 49.6934 | 4167.0 | 27.9338 | 15.3108 | 56.7555 | 1.6333 | -1.6162 | 22.4382 | 34.9652 | 2689.0 | 751.0 | -2.9012 | 0.0 |
| 均線站回確認型 | 10 | 維持原訊號日 D+20 收盤 | 7888.0 | 70.3081 | 4691.0 | 26.6255 | 17.0113 | 56.3632 | 1.5806 | -1.4377 | 21.3601 | 32.3812 | 1543.0 | 239.0 | -3.1377 | 0.0 |
| 均線站回確認型 | 10 | 確認日 D+20 收盤 | 7322.0 | 70.0144 | 4238.0 | 27.7253 | 15.5026 | 56.7721 | 1.5837 | -1.6563 | 22.4398 | 35.2525 | 1425.0 | 224.0 | -2.775 | 0.0 |

## 候選來源交集

| partition_key | partition_count | partition_rate_pct | source_partition_status |
| --- | --- | --- | --- |
| insufficient_future_10d_window | 6108.0 | 5.978 | pass |
| next_day=0/range23=0/ma20_ema23=0 | 20661.0 | 20.2212 | pass |
| next_day=0/range23=0/ma20_ema23=1 | 21918.0 | 21.4514 | pass |
| next_day=0/range23=1/ma20_ema23=1 | 10234.0 | 10.0161 | pass |
| next_day=1/range23=0/ma20_ema23=0 | 9893.0 | 9.6824 | pass |
| next_day=1/range23=0/ma20_ema23=1 | 18395.0 | 18.0034 | pass |
| next_day=1/range23=1/ma20_ema23=0 | 1.0 | 0.001 | pass |
| next_day=1/range23=1/ma20_ema23=1 | 14965.0 | 14.6464 | pass |

## 數字異常檢查

| confirmation_variant_name_zh | pending_window_days | exit_clock_id | accepted_trade_count_before_candidate_sensitivity_exclusion | price_path_anomaly_candidate_count | metric_sample_count | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | top1_abs_return_share_pct | top5_abs_return_share_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 訊號日直接進場對照組 | 0 | signal_d20_close | 6045 | 7 | 6045 | 252.6646 | 4414 | 20250605 | -91.0164 | 4763 | 20250609 | 0.3905 | 1.3336 | 1.5144 | blocked_pending_root_cause_anomaly_candidate_review |
| 隔日續強確認型 | 1 | signal_d20_close | 5354 | 8 | 5354 | 210.3976 | 4414 | 20250609 | -90.8508 | 4763 | 20250613 | 0.369 | 1.4037 | 1.0374 | blocked_pending_root_cause_anomaly_candidate_review |
| 隔日續強確認型 | 1 | confirmation_d20_close | 5153 | 7 | 5153 | 224.159 | 4414 | 20250609 | -90.9613 | 4763 | 20250613 | 0.3941 | 1.441 | 1.0748 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 3 | signal_d20_close | 2058 | 1 | 2058 | 139.1048 | 6658 | 20260417 | -47.0936 | 8438 | 20260701 | 0.5676 | 2.4658 | 1.9924 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 3 | confirmation_d20_close | 2021 | 1 | 2021 | 220.603 | 5386 | 20260127 | -54.3003 | 8042 | 20260626 | 0.8715 | 2.5516 | 2.2581 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 5 | signal_d20_close | 2201 | 2 | 2201 | 187.4372 | 5386 | 20260128 | -49.3438 | 8932 | 20260121 | 0.7132 | 2.5911 | 1.9902 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 5 | confirmation_d20_close | 2126 | 2 | 2126 | 220.603 | 5386 | 20260127 | -54.3003 | 8042 | 20260626 | 0.8123 | 2.3796 | 2.261 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 10 | signal_d20_close | 2333 | 1 | 2333 | 139.1048 | 6658 | 20260417 | -52.1552 | 4989 | 20260630 | 0.53 | 2.3635 | 1.5977 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 10 | confirmation_d20_close | 2176 | 1 | 2176 | 220.603 | 5386 | 20260127 | -54.3003 | 8042 | 20260626 | 0.7828 | 2.2363 | 2.1852 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 3 | signal_d20_close | 4290 | 6 | 4290 | 222.7273 | 4414 | 20250611 | -90.967 | 4763 | 20250609 | 0.4648 | 1.7498 | 1.2624 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 3 | confirmation_d20_close | 4118 | 7 | 4118 | 269.5652 | 5386 | 20260128 | -90.9451 | 4763 | 20250609 | 0.5604 | 1.9479 | 1.0429 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 5 | signal_d20_close | 4416 | 7 | 4416 | 239.3939 | 4414 | 20250613 | -90.967 | 4763 | 20250609 | 0.4938 | 1.6956 | 1.2813 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 5 | confirmation_d20_close | 4167 | 7 | 4167 | 251.5152 | 4414 | 20250613 | -90.9451 | 4763 | 20250609 | 0.5203 | 1.8796 | 1.1241 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 10 | signal_d20_close | 4691 | 5 | 4691 | 240.9091 | 4414 | 20250605 | -90.967 | 4763 | 20250609 | 0.4839 | 1.5873 | 1.1127 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 10 | confirmation_d20_close | 4238 | 7 | 4238 | 251.5152 | 4414 | 20250605 | -90.9451 | 4763 | 20250609 | 0.5104 | 1.8437 | 1.067 | blocked_pending_root_cause_anomaly_candidate_review |

## Large Detail Policy

逐筆 detail 僅保留確認後已成熟交易與價格路徑異常 evidence，位於 `output/latest/research_backtest/revenue_unreacted_range_close_confirmation_timing_audit_detail_latest.csv`；未確認／資料未成熟列由 summary 全量計數，不複製到 `docs/latest` 或 `output/history`。
