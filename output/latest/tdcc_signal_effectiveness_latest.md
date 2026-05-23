# TDCC Signal Effectiveness Report

- generated_at: `2026-05-23 21:16:15 Asia/Taipei`
- factor_rows: `26`

## Factor Stats

| factor_group | sample_size | sample_status | win_rate_d5 | avg_return_d5 | median_return_d5 | avg_drawdown_d5 | win_rate_d10 | avg_return_d10 | win_rate_d20 | avg_return_d20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_thresholds | 543 | ok |  |  |  |  |  |  |  |  |
| consecutive_2w_all_thresholds | 237 | ok |  |  |  |  |  |  |  |  |
| consecutive_3w_all_thresholds | 104 | ok |  |  |  |  |  |  |  |  |
| over_1000_only | 93 | ok |  |  |  |  |  |  |  |  |
| over_800_or_above | 950 | ok |  |  |  |  |  |  |  |  |
| over_400_only | 160 | ok |  |  |  |  |  |  |  |  |
| all_thresholds_not_overheated | 445 | ok |  |  |  |  |  |  |  |  |
| all_thresholds_overheated | 98 | ok |  |  |  |  |  |  |  |  |
| theme_breadth_A | 1253 | ok |  |  |  |  |  |  |  |  |
| theme_breadth_B | 0 | insufficient_sample |  |  |  |  |  |  |  |  |
| theme_single_name_concentration | 0 | insufficient_sample |  |  |  |  |  |  |  |  |
| price_confirmed | 529 | ok |  |  |  |  |  |  |  |  |
| price_not_confirmed | 725 | ok |  |  |  |  |  |  |  |  |
| pre_5d_return_lt_5 | 804 | ok |  |  |  |  |  |  |  |  |
| pre_5d_return_5_15 | 292 | ok |  |  |  |  |  |  |  |  |
| pre_5d_return_15_25 | 93 | ok |  |  |  |  |  |  |  |  |
| pre_5d_return_gt_25 | 61 | ok |  |  |  |  |  |  |  |  |
| abm_score_ge_80 | 170 | ok |  |  |  |  |  |  |  |  |
| abm_score_70_80 | 172 | ok |  |  |  |  |  |  |  |  |
| abm_score_60_70 | 213 | ok |  |  |  |  |  |  |  |  |
| setup_quiet_accumulation | 228 | ok |  |  |  |  |  |  |  |  |
| setup_early_breakout | 5 | ok |  |  |  |  |  |  |  |  |
| setup_strong_momentum | 85 | ok |  |  |  |  |  |  |  |  |
| setup_overheated | 180 | ok |  |  |  |  |  |  |  |  |
| tdcc_strong_but_price_not_reacted | 0 | insufficient_sample |  |  |  |  |  |  |  |  |
| tdcc_strong_and_overheated | 103 | ok |  |  |  |  |  |  |  |  |

## Notes

- sample_size 太小時標示 insufficient_sample，不硬下結論。
- 最新未成熟批次不視為正面或負面訊號。
- ABM factor groups 已納入，未來可比較 quiet_accumulation 與 overheated 的 D+10 / D+20 差異。