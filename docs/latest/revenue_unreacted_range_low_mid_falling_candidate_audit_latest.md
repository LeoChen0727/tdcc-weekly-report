# 營收改善但股價尚未反應：低／中位下降型態候選稽核

- generated_at: `2026-07-31 16:57:20 Asia/Taipei`
- artifact_version: `low_mid_falling_candidate_v1_20260720`
- 狀態：`research_only`；不是正式 gate、ranking、operation adapter、PDF 或 promotion evidence。
- 月營收與季／年財報分離；EPS、毛利率、營益率、營業利益、業外與淨利全部排除。
- 來源錨點使用 trigger 當下最後一筆已知 qualifying revenue，觀察期限固定 0～60 交易日。
- D+1 與 continuation-confirmed D+2 採不同 information cutoff；paired rows 不是獨立樣本。
- Primary 保留 anomaly candidates；候選排除僅是 sensitivity。

## Primary 候選矩陣

| lifecycle_policy_id | confirmation_variant_id | candidate_variant_id | operation_count | unique_stock_count | unique_episode_count | win_rate_pct | avg_return_pct | median_return_pct | p10_return_pct | p90_return_pct | return_ge20_rate_pct | return_le_minus20_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rearm_after_realized_exit_next_trade_day | base_close_confirmed | source_mid_falling | 87 | 76 | 76 | 64.3678 | 13.5707 | 9.2362 | -15.7924 | 47.0429 | 28.7356 | 4.5977 |
| rearm_after_realized_exit_next_trade_day | base_close_confirmed | source_low_falling | 43 | 36 | 37 | 51.1628 | 14.6628 | 1.5873 | -19.2786 | 57.904 | 34.8837 | 9.3023 |
| rearm_after_realized_exit_next_trade_day | base_close_confirmed | source_low_or_mid_falling_union | 130 | 110 | 111 | 60.0 | 13.932 | 7.5306 | -16.3794 | 49.7115 | 30.7692 | 6.1538 |
| rearm_after_realized_exit_next_trade_day | delayed_next_close_continuation_bonus | source_mid_falling | 52 | 47 | 47 | 78.8462 | 15.8235 | 10.9837 | -10.8794 | 42.41 | 36.5385 | 0.0 |
| rearm_after_realized_exit_next_trade_day | delayed_next_close_continuation_bonus | source_low_falling | 21 | 19 | 19 | 66.6667 | 15.6751 | 7.8431 | -14.6497 | 58.9286 | 38.0952 | 9.5238 |
| rearm_after_realized_exit_next_trade_day | delayed_next_close_continuation_bonus | source_low_or_mid_falling_union | 73 | 65 | 65 | 75.3425 | 15.7808 | 9.4444 | -11.04 | 49.6902 | 36.9863 | 2.7397 |
| episode_first_match_once | base_close_confirmed | source_mid_falling | 40 | 40 | 40 | 65.0 | 10.5203 | 7.7377 | -16.018 | 46.1424 | 25.0 | 7.5 |
| episode_first_match_once | base_close_confirmed | source_low_falling | 25 | 24 | 25 | 52.0 | 12.4074 | 1.5873 | -20.1049 | 57.7549 | 36.0 | 12.0 |
| episode_first_match_once | base_close_confirmed | source_low_or_mid_falling_union | 65 | 64 | 65 | 60.0 | 11.2461 | 6.7308 | -18.3957 | 52.4751 | 29.2308 | 9.2308 |
| episode_first_match_once | delayed_next_close_continuation_bonus | source_mid_falling | 26 | 26 | 26 | 80.7692 | 17.1859 | 9.9767 | -10.4957 | 51.5284 | 34.6154 | 0.0 |
| episode_first_match_once | delayed_next_close_continuation_bonus | source_low_falling | 12 | 12 | 12 | 58.3333 | 20.7349 | 8.3041 | -19.8935 | 84.1617 | 41.6667 | 16.6667 |
| episode_first_match_once | delayed_next_close_continuation_bonus | source_low_or_mid_falling_union | 38 | 38 | 38 | 73.6842 | 18.3066 | 9.9767 | -12.4797 | 64.0819 | 36.8421 | 5.2632 |

- paired_confirmation_rows: `71`
