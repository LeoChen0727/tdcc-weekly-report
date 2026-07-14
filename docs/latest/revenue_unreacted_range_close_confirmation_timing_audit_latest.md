# 營收爆發但股價尚未反應模型：收盤確認時點稽核

- generated_at: `2026-07-14 13:57:09 Asia/Taipei`
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
| 訊號日直接進場對照組 | 0 | 維持原訊號日 D+20 收盤 | 5440.0 | 100.0 | 4762.0 | 29.9664 | 18.7526 | 51.281 | 2.9429 | -0.3454 | 23.8765 | 29.4204 | 0.0 | 0.0 | 0.0 | 0.0 |
| 隔日續強確認型 | 1 | 維持原訊號日 D+20 收盤 | 10340.0 | 47.1005 | 4272.0 | 29.6348 | 17.8839 | 52.4813 | 2.7785 | -0.609 | 23.7125 | 29.1667 | 2762.0 | 1223.0 | -1.6999 | 0.0 |
| 隔日續強確認型 | 1 | 確認日 D+20 收盤 | 10417.0 | 44.9243 | 4087.0 | 29.5571 | 17.1764 | 53.2665 | 3.0242 | -0.8097 | 23.6604 | 29.6795 | 2830.0 | 1323.0 | -1.4186 | 0.0 |
| 區間突破確認型 | 3 | 維持原訊號日 D+20 收盤 | 17489.0 | 11.2846 | 1761.0 | 33.0494 | 13.2879 | 53.6627 | 3.4859 | -0.9756 | 27.314 | 32.2544 | 7385.0 | 3581.0 | -6.3977 | 0.0 |
| 區間突破確認型 | 3 | 確認日 D+20 收盤 | 17161.0 | 11.2688 | 1710.0 | 34.5029 | 13.8596 | 51.6374 | 4.0763 | -0.651 | 28.1871 | 33.1579 | 7267.0 | 3499.0 | -5.8409 | 0.0 |
| 區間突破確認型 | 5 | 維持原訊號日 D+20 收盤 | 12441.0 | 17.0926 | 1882.0 | 33.7407 | 14.0276 | 52.2317 | 3.5811 | -0.5724 | 28.0553 | 31.4028 | 5064.0 | 2187.0 | -7.8684 | 0.0 |
| 區間突破確認型 | 5 | 確認日 D+20 收盤 | 12038.0 | 17.1805 | 1819.0 | 34.4695 | 14.0737 | 51.4568 | 4.0056 | -0.5256 | 29.1369 | 33.37 | 4879.0 | 2132.0 | -6.8121 | 0.0 |
| 區間突破確認型 | 10 | 維持原訊號日 D+20 收盤 | 8004.0 | 28.7813 | 2004.0 | 31.7365 | 14.9202 | 53.3433 | 2.9156 | -0.8775 | 26.0978 | 31.8363 | 3090.0 | 954.0 | -8.9842 | 0.0 |
| 區間突破確認型 | 10 | 確認日 D+20 收盤 | 7583.0 | 28.9279 | 1876.0 | 34.1151 | 13.3262 | 52.5586 | 3.9599 | -0.8906 | 28.4648 | 34.5949 | 2910.0 | 904.0 | -7.307 | 0.0 |
| 均線站回確認型 | 3 | 維持原訊號日 D+20 收盤 | 10615.0 | 39.1737 | 3561.0 | 30.6655 | 15.6698 | 53.6647 | 3.1003 | -0.8872 | 24.8526 | 30.1039 | 3227.0 | 1201.0 | -2.6733 | 0.0 |
| 均線站回確認型 | 3 | 確認日 D+20 收盤 | 10151.0 | 39.4997 | 3412.0 | 30.3341 | 16.354 | 53.3118 | 3.1729 | -0.8547 | 24.7069 | 31.3892 | 3086.0 | 1140.0 | -2.4108 | 0.0 |
| 均線站回確認型 | 5 | 維持原訊號日 D+20 收盤 | 8239.0 | 52.2915 | 3660.0 | 29.7268 | 16.7486 | 53.5246 | 2.8303 | -0.9569 | 24.153 | 29.7814 | 2098.0 | 622.0 | -3.034 | 0.0 |
| 均線站回確認型 | 5 | 確認日 D+20 收盤 | 7835.0 | 52.2721 | 3458.0 | 30.1041 | 16.3968 | 53.4991 | 3.0499 | -0.8654 | 24.6096 | 31.5211 | 2008.0 | 581.0 | -2.6775 | 0.0 |
| 均線站回確認型 | 10 | 維持原訊號日 D+20 收盤 | 6305.0 | 72.0667 | 3844.0 | 29.1623 | 16.9355 | 53.9022 | 2.6009 | -0.9545 | 23.6212 | 30.4631 | 1148.0 | 153.0 | -3.1081 | 0.0 |
| 均線站回確認型 | 10 | 確認日 D+20 收盤 | 5824.0 | 72.2111 | 3524.0 | 29.8808 | 16.5153 | 53.6039 | 3.0707 | -0.9466 | 24.6027 | 31.7253 | 1048.0 | 157.0 | -2.442 | 0.0 |

## 候選來源交集

| partition_key | partition_count | partition_rate_pct | source_partition_status |
| --- | --- | --- | --- |
| insufficient_future_10d_window | 5453.0 | 6.6838 | pass |
| next_day=0/range23=0/ma20_ema23=0 | 15683.0 | 19.2229 | pass |
| next_day=0/range23=0/ma20_ema23=1 | 17672.0 | 21.6608 | pass |
| next_day=0/range23=1/ma20_ema23=1 | 8779.0 | 10.7606 | pass |
| next_day=1/range23=0/ma20_ema23=0 | 7101.0 | 8.7038 | pass |
| next_day=1/range23=0/ma20_ema23=1 | 14197.0 | 17.4015 | pass |
| next_day=1/range23=1/ma20_ema23=0 | 2.0 | 0.0025 | pass |
| next_day=1/range23=1/ma20_ema23=1 | 12698.0 | 15.5641 | pass |

## 數字異常檢查

| confirmation_variant_name_zh | pending_window_days | exit_clock_id | accepted_trade_count_before_candidate_sensitivity_exclusion | price_path_anomaly_candidate_count | metric_sample_count | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | top1_abs_return_share_pct | top5_abs_return_share_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 訊號日直接進場對照組 | 0 | signal_d20_close | 4762 | 7 | 4762 | 220.1893 | 4414 | 20250609 | -91.0164 | 4763 | 20250609 | 0.4314 | 1.5326 | 2.4249 | blocked_pending_root_cause_anomaly_candidate_review |
| 隔日續強確認型 | 1 | signal_d20_close | 4272 | 7 | 4272 | 210.3976 | 4414 | 20250609 | -90.8508 | 4763 | 20250613 | 0.4734 | 1.7932 | 2.2684 | blocked_pending_root_cause_anomaly_candidate_review |
| 隔日續強確認型 | 1 | confirmation_d20_close | 4087 | 7 | 4087 | 224.159 | 4414 | 20250609 | -90.9613 | 4763 | 20250613 | 0.5074 | 1.8138 | 2.4806 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 3 | signal_d20_close | 1761 | 1 | 1761 | 139.1048 | 6658 | 20260417 | -40.6061 | 6727 | 20260519 | 0.6586 | 2.7442 | 2.9271 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 3 | confirmation_d20_close | 1710 | 1 | 1710 | 117.3077 | 6949 | 20250710 | -40.676 | 2540 | 20250902 | 0.5394 | 2.4613 | 3.5153 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 5 | signal_d20_close | 1882 | 1 | 1882 | 139.1048 | 6658 | 20260417 | -40.6061 | 6727 | 20260519 | 0.6137 | 2.5732 | 3.0295 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 5 | confirmation_d20_close | 1819 | 1 | 1819 | 220.603 | 5386 | 20260123 | -40.676 | 2540 | 20250901 | 0.9406 | 2.7978 | 3.4055 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 10 | signal_d20_close | 2004 | 2 | 2004 | 139.1048 | 6658 | 20260417 | -49.3438 | 8932 | 20260121 | 0.6157 | 2.3633 | 2.4151 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 10 | confirmation_d20_close | 1876 | 2 | 1876 | 220.603 | 5386 | 20260122 | -51.706 | 8932 | 20260121 | 0.8995 | 2.6105 | 3.3586 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 3 | signal_d20_close | 3561 | 6 | 3561 | 239.3939 | 4414 | 20250613 | -90.967 | 4763 | 20250609 | 0.608 | 2.1077 | 2.5487 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 3 | confirmation_d20_close | 3412 | 6 | 3412 | 251.5152 | 4414 | 20250613 | -90.9451 | 4763 | 20250609 | 0.6398 | 1.9993 | 2.6213 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 5 | signal_d20_close | 3660 | 5 | 3660 | 207.5758 | 4414 | 20250609 | -90.967 | 4763 | 20250609 | 0.5246 | 1.9103 | 2.3271 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 5 | confirmation_d20_close | 3458 | 6 | 3458 | 251.5152 | 4414 | 20250609 | -90.9451 | 4763 | 20250609 | 0.6314 | 2.0117 | 2.5098 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 10 | signal_d20_close | 3844 | 6 | 3844 | 207.5758 | 4414 | 20250609 | -90.967 | 4763 | 20250609 | 0.5117 | 1.7345 | 2.0965 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 10 | confirmation_d20_close | 3524 | 7 | 3524 | 251.5152 | 4414 | 20250609 | -90.9451 | 4763 | 20250609 | 0.6213 | 1.9795 | 2.5148 | blocked_pending_root_cause_anomaly_candidate_review |

## Large Detail Policy

逐筆 detail 僅保留確認後已成熟交易與價格路徑異常 evidence，位於 `output/latest/research_backtest/revenue_unreacted_range_close_confirmation_timing_audit_detail_latest.csv`；未確認／資料未成熟列由 summary 全量計數，不複製到 `docs/latest` 或 `output/history`。
