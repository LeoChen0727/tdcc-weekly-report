# 營收爆發但股價尚未反應模型：收盤確認時點稽核

- generated_at: `2026-07-13 18:41:51 Asia/Taipei`
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
| 訊號日直接進場對照組 | 0 | 維持原訊號日 D+20 收盤 | 5424.0 | 100.0 | 4750.0 | 29.9368 | 18.7579 | 51.3053 | 2.943 | -0.3466 | 23.8737 | 29.4105 | 0.0 | 0.0 | 0.0 | 0.0 |
| 隔日續強確認型 | 1 | 維持原訊號日 D+20 收盤 | 10312.0 | 47.126 | 4264.0 | 29.6435 | 17.894 | 52.4625 | 2.7854 | -0.609 | 23.7101 | 29.151 | 2755.0 | 1214.0 | -1.6975 | 0.0 |
| 隔日續強確認型 | 1 | 確認日 D+20 收盤 | 10373.0 | 44.9618 | 4079.0 | 29.5416 | 17.1856 | 53.2729 | 3.0252 | -0.8097 | 23.6578 | 29.6886 | 2821.0 | 1315.0 | -1.4172 | 0.0 |
| 區間突破確認型 | 3 | 維持原訊號日 D+20 收盤 | 17369.0 | 11.3199 | 1750.0 | 33.0857 | 13.3714 | 53.5429 | 3.4993 | -0.9695 | 27.3143 | 32.1714 | 7353.0 | 3558.0 | -6.3862 | 0.0 |
| 區間突破確認型 | 3 | 確認日 D+20 收盤 | 17065.0 | 11.3073 | 1702.0 | 34.4888 | 13.9248 | 51.5864 | 4.0604 | -0.6229 | 28.2021 | 33.1962 | 7231.0 | 3487.0 | -5.7768 | 0.0 |
| 區間突破確認型 | 5 | 維持原訊號日 D+20 收盤 | 12370.0 | 17.1173 | 1875.0 | 33.8133 | 14.08 | 52.1067 | 3.6122 | -0.5435 | 28.1067 | 31.2533 | 5044.0 | 2176.0 | -7.8504 | 0.0 |
| 區間突破確認型 | 5 | 確認日 D+20 收盤 | 11952.0 | 17.2322 | 1809.0 | 34.4942 | 14.1515 | 51.3543 | 4.0032 | -0.5195 | 29.1874 | 33.2781 | 4857.0 | 2120.0 | -6.75 | 0.0 |
| 區間突破確認型 | 10 | 維持原訊號日 D+20 收盤 | 7959.0 | 28.7575 | 1997.0 | 31.8478 | 14.8723 | 53.2799 | 2.9479 | -0.8484 | 26.1893 | 31.7476 | 3079.0 | 952.0 | -8.9604 | 0.0 |
| 區間突破確認型 | 10 | 確認日 D+20 收盤 | 7525.0 | 28.9562 | 1863.0 | 34.3532 | 13.3655 | 52.2813 | 4.0315 | -0.8021 | 28.6634 | 34.4069 | 2894.0 | 902.0 | -7.3 | 0.0 |
| 均線站回確認型 | 3 | 維持原訊號日 D+20 收盤 | 10568.0 | 39.2875 | 3546.0 | 30.6825 | 15.6796 | 53.6379 | 3.1016 | -0.8848 | 24.8731 | 30.0338 | 3218.0 | 1190.0 | -2.6723 | 0.0 |
| 均線站回確認型 | 3 | 確認日 D+20 收盤 | 10107.0 | 39.6281 | 3400.0 | 30.3824 | 16.3529 | 53.2647 | 3.1875 | -0.8533 | 24.7353 | 31.4118 | 3073.0 | 1134.0 | -2.3925 | 0.0 |
| 均線站回確認型 | 5 | 維持原訊號日 D+20 收盤 | 8209.0 | 52.2965 | 3648.0 | 29.6875 | 16.7763 | 53.5362 | 2.8208 | -0.9569 | 24.1228 | 29.7423 | 2091.0 | 618.0 | -3.0245 | 0.0 |
| 均線站回確認型 | 5 | 確認日 D+20 收盤 | 7799.0 | 52.3733 | 3446.0 | 30.1219 | 16.3668 | 53.5113 | 3.0622 | -0.8654 | 24.6373 | 31.5438 | 1996.0 | 579.0 | -2.6603 | 0.0 |
| 均線站回確認型 | 10 | 維持原訊號日 D+20 收盤 | 6287.0 | 72.079 | 3833.0 | 29.1938 | 16.9319 | 53.8742 | 2.605 | -0.9479 | 23.6368 | 30.42 | 1147.0 | 153.0 | -3.0942 | 0.0 |
| 均線站回確認型 | 10 | 確認日 D+20 收盤 | 5789.0 | 72.2606 | 3511.0 | 29.906 | 16.491 | 53.603 | 3.0782 | -0.9467 | 24.6084 | 31.7573 | 1044.0 | 156.0 | -2.4382 | 0.0 |

## 候選來源交集

| partition_key | partition_count | partition_rate_pct | source_partition_status |
| --- | --- | --- | --- |
| insufficient_future_10d_window | 5398.0 | 6.6628 | pass |
| next_day=0/range23=0/ma20_ema23=0 | 15529.0 | 19.1676 | pass |
| next_day=0/range23=0/ma20_ema23=1 | 17447.0 | 21.535 | pass |
| next_day=0/range23=1/ma20_ema23=1 | 8687.0 | 10.7224 | pass |
| next_day=1/range23=0/ma20_ema23=0 | 7094.0 | 8.7562 | pass |
| next_day=1/range23=0/ma20_ema23=1 | 14181.0 | 17.5037 | pass |
| next_day=1/range23=1/ma20_ema23=0 | 2.0 | 0.0025 | pass |
| next_day=1/range23=1/ma20_ema23=1 | 12679.0 | 15.6498 | pass |

## 數字異常檢查

| confirmation_variant_name_zh | pending_window_days | exit_clock_id | accepted_trade_count_before_candidate_sensitivity_exclusion | price_path_anomaly_candidate_count | metric_sample_count | max_realized_return_pct | max_return_stock_id | max_return_signal_date | min_realized_return_pct | min_return_stock_id | min_return_signal_date | top1_abs_return_share_pct | top5_abs_return_share_pct | trimmed_1pct_avg_return_pct | interpretation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 訊號日直接進場對照組 | 0 | signal_d20_close | 4750 | 7 | 4750 | 220.1893 | 4414 | 20250609 | -91.0164 | 4763 | 20250609 | 0.4327 | 1.537 | 2.4218 | blocked_pending_root_cause_anomaly_candidate_review |
| 隔日續強確認型 | 1 | signal_d20_close | 4264 | 7 | 4264 | 210.3976 | 4414 | 20250609 | -90.8508 | 4763 | 20250613 | 0.4739 | 1.7952 | 2.2745 | blocked_pending_root_cause_anomaly_candidate_review |
| 隔日續強確認型 | 1 | confirmation_d20_close | 4079 | 7 | 4079 | 224.159 | 4414 | 20250609 | -90.9613 | 4763 | 20250613 | 0.5082 | 1.8167 | 2.4805 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 3 | signal_d20_close | 1750 | 1 | 1750 | 139.1048 | 6658 | 20260417 | -40.6061 | 6727 | 20260519 | 0.6617 | 2.757 | 2.9373 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 3 | confirmation_d20_close | 1702 | 1 | 1702 | 117.3077 | 6949 | 20250710 | -40.676 | 2540 | 20250902 | 0.542 | 2.4732 | 3.4964 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 5 | signal_d20_close | 1875 | 1 | 1875 | 139.1048 | 6658 | 20260417 | -40.6061 | 6727 | 20260519 | 0.6159 | 2.5825 | 3.0591 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 5 | confirmation_d20_close | 1809 | 1 | 1809 | 220.603 | 5386 | 20260123 | -40.676 | 2540 | 20250901 | 0.9468 | 2.8165 | 3.3997 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 10 | signal_d20_close | 1997 | 2 | 1997 | 139.1048 | 6658 | 20260417 | -49.3438 | 8932 | 20260121 | 0.6171 | 2.3683 | 2.4661 | blocked_pending_root_cause_anomaly_candidate_review |
| 區間突破確認型 | 10 | confirmation_d20_close | 1863 | 2 | 1863 | 220.603 | 5386 | 20260122 | -51.706 | 8932 | 20260121 | 0.9027 | 2.6198 | 3.4273 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 3 | signal_d20_close | 3546 | 6 | 3546 | 239.3939 | 4414 | 20250613 | -90.967 | 4763 | 20250609 | 0.6102 | 2.1154 | 2.5476 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 3 | confirmation_d20_close | 3400 | 6 | 3400 | 251.5152 | 4414 | 20250613 | -90.9451 | 4763 | 20250609 | 0.6414 | 2.0043 | 2.6341 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 5 | signal_d20_close | 3648 | 5 | 3648 | 207.5758 | 4414 | 20250609 | -90.967 | 4763 | 20250609 | 0.5267 | 1.9177 | 2.3157 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 5 | confirmation_d20_close | 3446 | 6 | 3446 | 251.5152 | 4414 | 20250609 | -90.9451 | 4763 | 20250609 | 0.6327 | 2.0158 | 2.5204 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 10 | signal_d20_close | 3833 | 6 | 3833 | 207.5758 | 4414 | 20250609 | -90.967 | 4763 | 20250609 | 0.5131 | 1.739 | 2.0991 | blocked_pending_root_cause_anomaly_candidate_review |
| 均線站回確認型 | 10 | confirmation_d20_close | 3511 | 7 | 3511 | 251.5152 | 4414 | 20250609 | -90.9451 | 4763 | 20250609 | 0.6229 | 1.9844 | 2.5203 | blocked_pending_root_cause_anomaly_candidate_review |

## Large Detail Policy

逐筆 detail 僅保留確認後已成熟交易與價格路徑異常 evidence，位於 `output/latest/research_backtest/revenue_unreacted_range_close_confirmation_timing_audit_detail_latest.csv`；未確認／資料未成熟列由 summary 全量計數，不複製到 `docs/latest` 或 `output/history`。
