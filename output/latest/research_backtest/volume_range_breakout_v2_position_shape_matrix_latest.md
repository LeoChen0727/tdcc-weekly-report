# volume_range_breakout_v2_position_shape_matrix

research-only artifact; no production registry change.

Scope: d15_close_only_next_day_continuation_ma20_ema23_stop
Source sample size: 576
Valid returns: 556

Bucket assignment is exhaustive and non-overlapping per position axis.
Sample count is reported as context only and is not a disqualifier.
A bucket meets the win/return metric when win_rate >= 60% and both average and median return are positive.

## 120d Position x Shape Matrix

| position_bucket | shape_bucket | sample_size | valid_return_count | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | meets_win_return_metric |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| low_pos_le40 | consolidation | 8 | 8 | 87.5 | 12.5 | 17.5399 | 17.0606 | True |
| low_pos_le40 | non_consolidation | 13 | 13 | 76.9231 | 23.0769 | 38.6568 | 26.3815 | True |
| low_pos_le40 | wide_range | 5 | 5 | 80.0 | 20.0 | 21.0344 | 18.6131 | True |
| mid_pos_40_75 | consolidation | 30 | 30 | 43.3333 | 56.6667 | 2.7044 | -2.1755 | False |
| mid_pos_40_75 | non_consolidation | 16 | 16 | 75.0 | 25.0 | 10.3903 | 11.3967 | True |
| mid_pos_40_75 | wide_range | 9 | 9 | 88.8889 | 11.1111 | 16.9724 | 17.6471 | True |
| high_pos_gt75 | consolidation | 196 | 196 | 50.0 | 50.0 | 4.1759 | 0.0581 | False |
| high_pos_gt75 | non_consolidation | 208 | 208 | 59.6154 | 39.9038 | 8.4007 | 3.3063 | False |
| high_pos_gt75 | wide_range | 71 | 71 | 59.1549 | 40.8451 | 7.2979 | 7.2398 | False |
| unknown_position | consolidation | 2 | 0 |  |  |  |  | False |
| unknown_position | non_consolidation | 10 | 0 |  |  |  |  | False |
| unknown_position | wide_range | 8 | 0 |  |  |  |  | False |

## 240d Position x Shape Matrix

| position_bucket | shape_bucket | sample_size | valid_return_count | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | meets_win_return_metric |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| low_pos_le40 | consolidation | 12 | 12 | 58.3333 | 41.6667 | 5.7106 | 3.9245 | False |
| low_pos_le40 | non_consolidation | 19 | 19 | 73.6842 | 26.3158 | 36.4727 | 26.3815 | True |
| low_pos_le40 | wide_range | 5 | 5 | 80.0 | 20.0 | 21.0344 | 18.6131 | True |
| mid_pos_40_75 | consolidation | 51 | 51 | 37.2549 | 62.7451 | -0.3766 | -3.0812 | False |
| mid_pos_40_75 | non_consolidation | 34 | 34 | 73.5294 | 26.4706 | 10.9548 | 11.0085 | True |
| mid_pos_40_75 | wide_range | 13 | 13 | 92.3077 | 7.6923 | 17.1214 | 17.6471 | True |
| high_pos_gt75 | consolidation | 171 | 171 | 53.8012 | 46.1988 | 5.793 | 1.7347 | False |
| high_pos_gt75 | non_consolidation | 184 | 184 | 58.1522 | 41.3043 | 7.3407 | 2.694 | False |
| high_pos_gt75 | wide_range | 67 | 67 | 56.7164 | 43.2836 | 6.6914 | 6.1966 | False |
| unknown_position | consolidation | 2 | 0 |  |  |  |  | False |
| unknown_position | non_consolidation | 10 | 0 |  |  |  |  | False |
| unknown_position | wide_range | 8 | 0 |  |  |  |  | False |
