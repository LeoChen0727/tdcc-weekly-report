# 營收改善但股價尚未反應：低／中位下降型態候選稽核

- generated_at: `2026-08-23 07:24:41 Asia/Taipei`
- artifact_version: `low_mid_falling_candidate_v2_20260822`
- 狀態：`research_only`；不是正式 gate、ranking、operation adapter、PDF 或 promotion evidence。
- 月營收與季／年財報分離；EPS、毛利率、營益率、營業利益、業外與淨利全部排除。
- 來源錨點使用 trigger 當下最後一筆已知 qualifying revenue，觀察期限固定 0～60 交易日。
- D+1 與 continuation-confirmed D+2 採不同 information cutoff；paired rows 不是獨立樣本。
- Primary 保留 anomaly candidates；候選排除僅是 sensitivity。

## Primary 候選矩陣

| lifecycle_policy_id | confirmation_variant_id | candidate_variant_id | operation_count | unique_stock_count | unique_episode_count | win_rate_pct | avg_return_pct | median_return_pct | p10_return_pct | p90_return_pct | return_ge20_rate_pct | return_le_minus20_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rearm_after_realized_exit_next_trade_day | base_close_confirmed | source_mid_falling | 86 | 76 | 77 | 66.2791 | 13.5206 | 8.4886 | -13.2052 | 47.343 | 27.907 | 4.6512 |
| rearm_after_realized_exit_next_trade_day | base_close_confirmed | source_low_falling | 42 | 35 | 36 | 54.7619 | 15.3957 | 3.7151 | -19.4862 | 57.9786 | 33.3333 | 9.5238 |
| rearm_after_realized_exit_next_trade_day | base_close_confirmed | source_low_or_mid_falling_union | 128 | 109 | 111 | 62.5 | 14.1359 | 6.7553 | -15.7628 | 50.1149 | 29.6875 | 6.25 |
| rearm_after_realized_exit_next_trade_day | delayed_next_close_continuation_bonus | source_mid_falling | 53 | 48 | 48 | 77.3585 | 14.895 | 9.4077 | -11.04 | 42.2669 | 35.8491 | 0.0 |
| rearm_after_realized_exit_next_trade_day | delayed_next_close_continuation_bonus | source_low_falling | 21 | 19 | 19 | 71.4286 | 16.445 | 7.9585 | -14.6497 | 58.9286 | 38.0952 | 9.5238 |
| rearm_after_realized_exit_next_trade_day | delayed_next_close_continuation_bonus | source_low_or_mid_falling_union | 74 | 66 | 66 | 75.6757 | 15.3349 | 9.3692 | -11.4045 | 48.7981 | 36.4865 | 2.7027 |
| episode_first_match_once | base_close_confirmed | source_mid_falling | 41 | 40 | 41 | 63.4146 | 10.5414 | 6.7797 | -15.9701 | 45.8422 | 26.8293 | 7.3171 |
| episode_first_match_once | base_close_confirmed | source_low_falling | 26 | 25 | 26 | 50.0 | 11.5366 | -0.9774 | -20.0364 | 57.6804 | 34.6154 | 11.5385 |
| episode_first_match_once | base_close_confirmed | source_low_or_mid_falling_union | 67 | 65 | 67 | 58.209 | 10.9276 | 6.1824 | -18.4485 | 52.1589 | 29.8507 | 8.9552 |
| episode_first_match_once | delayed_next_close_continuation_bonus | source_mid_falling | 26 | 26 | 26 | 76.9231 | 14.9471 | 9.035 | -11.2436 | 46.2881 | 34.6154 | 0.0 |
| episode_first_match_once | delayed_next_close_continuation_bonus | source_low_falling | 13 | 13 | 13 | 61.5385 | 19.8664 | 9.4444 | -19.3109 | 81.358 | 38.4615 | 15.3846 |
| episode_first_match_once | delayed_next_close_continuation_bonus | source_low_or_mid_falling_union | 39 | 39 | 39 | 71.7949 | 16.5868 | 9.4444 | -15.4708 | 62.3641 | 35.8974 | 5.1282 |

- paired_confirmation_rows: `76`
