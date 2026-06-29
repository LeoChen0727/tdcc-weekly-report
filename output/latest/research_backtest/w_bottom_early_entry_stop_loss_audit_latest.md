# W-bottom Early Entry Stop-loss Audit

- production impact: `none`
- model_id: `w_bottom_right_side`
- selected segment: `smooth_core_mainstream_right_rebound_5_20_bull`
- entry rule: `right_low_signal_next_open`
- source outcome rule: `tp10_or_neutral_after_5pct_close_40d`
- stop-loss candidates: no stop, right-low close stop, W-structure-low close stop, W-structure-low stop with D+20 gain exit, W-structure-low close stop with 1% buffer.
- price convention: entry uses next trading day's open; stop/target/neutral/expiry exits use close.

## Selected Segment Comparison

| stop_rule_id                               | evaluated_sample_size | win_count | neutral_count | loss_count | stop_hit_count | pure_win_rate_pct | neutral_inclusive_success_rate_pct | avg_return_pct | median_return_pct | min_return_pct | delta_pure_win_rate_pct | delta_avg_return_pct | min_return_improvement_pct | recommendation_status                  |
| ------------------------------------------ | --------------------- | --------- | ------------- | ---------- | -------------- | ----------------- | ---------------------------------- | -------------- | ----------------- | -------------- | ----------------------- | -------------------- | -------------------------- | -------------------------------------- |
| no_fixed_stop_d40_v1                       | 31                    | 13        | 11            | 7          | 0              | 65.0000           | 77.4194                            | 2.9504         | 4.7478            | -56.6854       | 0.0000                  | 0.0000               | 0.0000                     | current_v1_baseline                    |
| right_low_close_stop_d40                   | 31                    | 12        | 10            | 9          | 7              | 57.1429           | 70.9677                            | 3.9918         | 4.6377            | -10.2890       | -7.8571                 | 1.0414               | 46.3964                    | risk_repair_candidate_research_only    |
| w_structure_low_close_stop_d40             | 31                    | 12        | 10            | 9          | 7              | 57.1429           | 70.9677                            | 3.7225         | 4.6377            | -10.9907       | -7.8571                 | 0.7721               | 45.6947                    | risk_repair_candidate_tradeoff_review  |
| w_structure_low_stop_d20_gain10_else_d40   | 31                    | 18        | 0             | 13         | 10             | 58.0645           | 58.0645                            | 11.2532        | 6.2374            | -12.7202       | -6.9355                 | 8.3028               | 43.9652                    | preferred_v2_candidate_tradeoff_review |
| w_structure_low_close_stop_1pct_buffer_d40 | 31                    | 12        | 10            | 9          | 6              | 57.1429           | 70.9677                            | 3.4502         | 4.6377            | -14.3258       | -7.8571                 | 0.4998               | 42.3596                    | risk_repair_candidate_research_only    |

## Interpretation

- Baseline `no_fixed_stop_d40_v1`: pure win `65.0000%`, inclusive success `77.4194%`, avg return `2.9504%`, min return `-56.6854%`.
- Candidate `w_structure_low_stop_d20_gain10_else_d40`: positive-return rate `58.0645%`, inclusive success `58.0645%`, avg return `11.2532%`, min return `-12.7202%`.
- The hybrid D+20/D+40 rule repairs left-tail risk, avoids early +10% profit truncation, and improves average return. It must not be promoted silently as production v2 without an explicit model-change PR.
- Structure-stop with old +10%/+5% rule: pure win `57.1429%`, avg return `3.7225%`, min return `-10.9907%`.

## All Segment Summary

| segment_id                                              | stop_rule_id                               | evaluated_sample_size | pure_win_rate_pct | neutral_inclusive_success_rate_pct | avg_return_pct | min_return_pct | recommendation_status                  |
| ------------------------------------------------------- | ------------------------------------------ | --------------------- | ----------------- | ---------------------------------- | -------------- | -------------- | -------------------------------------- |
| smooth_right_rebound_5_20_strong_bull                   | no_fixed_stop_d40_v1                       | 45                    | 57.5758           | 68.8889                            | 1.4741         | -56.6854       | current_v1_baseline                    |
| smooth_right_rebound_5_20_strong_bull                   | right_low_close_stop_d40                   | 45                    | 47.2222           | 57.7778                            | 2.5295         | -10.2890       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_strong_bull                   | w_structure_low_close_stop_d40             | 45                    | 48.5714           | 60.0000                            | 2.3393         | -12.6263       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_strong_bull                   | w_structure_low_stop_d20_gain10_else_d40   | 45                    | 46.6667           | 46.6667                            | 5.6655         | -12.7202       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_strong_bull                   | w_structure_low_close_stop_1pct_buffer_d40 | 45                    | 51.4286           | 62.2222                            | 2.4401         | -14.3258       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_bull                          | no_fixed_stop_d40_v1                       | 63                    | 53.3333           | 66.6667                            | 2.0376         | -56.6854       | current_v1_baseline                    |
| smooth_right_rebound_5_20_bull                          | right_low_close_stop_d40                   | 62                    | 42.5532           | 56.4516                            | 2.2334         | -10.2890       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_bull                          | w_structure_low_close_stop_d40             | 62                    | 45.6522           | 59.6774                            | 2.4383         | -12.6263       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_bull                          | w_structure_low_stop_d20_gain10_else_d40   | 62                    | 46.7742           | 46.7742                            | 6.3806         | -12.7202       | risk_repair_candidate_research_only    |
| smooth_right_rebound_5_20_bull                          | w_structure_low_close_stop_1pct_buffer_d40 | 62                    | 47.8261           | 61.2903                            | 2.4704         | -14.3258       | risk_repair_candidate_research_only    |
| smooth_core_mainstream_right_rebound_5_20_strong_bull   | no_fixed_stop_d40_v1                       | 26                    | 66.6667           | 76.9231                            | 2.5990         | -56.6854       | current_v1_baseline                    |
| smooth_core_mainstream_right_rebound_5_20_strong_bull   | right_low_close_stop_d40                   | 26                    | 57.8947           | 69.2308                            | 3.8407         | -10.2890       | risk_repair_candidate_research_only    |
| smooth_core_mainstream_right_rebound_5_20_strong_bull   | w_structure_low_close_stop_d40             | 26                    | 57.8947           | 69.2308                            | 3.5196         | -10.9907       | risk_repair_candidate_research_only    |
| smooth_core_mainstream_right_rebound_5_20_strong_bull   | w_structure_low_stop_d20_gain10_else_d40   | 26                    | 53.8462           | 53.8462                            | 8.1599         | -12.7202       | risk_repair_candidate_research_only    |
| smooth_core_mainstream_right_rebound_5_20_strong_bull   | w_structure_low_close_stop_1pct_buffer_d40 | 26                    | 57.8947           | 69.2308                            | 3.1948         | -14.3258       | risk_repair_candidate_research_only    |
| smooth_core_mainstream_right_rebound_5_20_bull          | no_fixed_stop_d40_v1                       | 31                    | 65.0000           | 77.4194                            | 2.9504         | -56.6854       | current_v1_baseline                    |
| smooth_core_mainstream_right_rebound_5_20_bull          | right_low_close_stop_d40                   | 31                    | 57.1429           | 70.9677                            | 3.9918         | -10.2890       | risk_repair_candidate_research_only    |
| smooth_core_mainstream_right_rebound_5_20_bull          | w_structure_low_close_stop_d40             | 31                    | 57.1429           | 70.9677                            | 3.7225         | -10.9907       | risk_repair_candidate_tradeoff_review  |
| smooth_core_mainstream_right_rebound_5_20_bull          | w_structure_low_stop_d20_gain10_else_d40   | 31                    | 58.0645           | 58.0645                            | 11.2532        | -12.7202       | preferred_v2_candidate_tradeoff_review |
| smooth_core_mainstream_right_rebound_5_20_bull          | w_structure_low_close_stop_1pct_buffer_d40 | 31                    | 57.1429           | 70.9677                            | 3.4502         | -14.3258       | risk_repair_candidate_research_only    |
| core_mainstream_price_le30_rebound_3_20_volume_red_bull | no_fixed_stop_d40_v1                       | 106                   | 47.4359           | 61.3208                            | 2.8211         | -21.3666       | current_v1_baseline                    |
| core_mainstream_price_le30_rebound_3_20_volume_red_bull | right_low_close_stop_d40                   | 106                   | 32.9268           | 48.1132                            | 0.6121         | -21.1905       | not_preferred_in_current_grid          |
| core_mainstream_price_le30_rebound_3_20_volume_red_bull | w_structure_low_close_stop_d40             | 100                   | 35.1351           | 52.0000                            | 0.4505         | -21.1905       | not_preferred_in_current_grid          |
| core_mainstream_price_le30_rebound_3_20_volume_red_bull | w_structure_low_stop_d20_gain10_else_d40   | 100                   | 41.0000           | 41.0000                            | 4.7384         | -21.1905       | risk_repair_candidate_research_only    |
| core_mainstream_price_le30_rebound_3_20_volume_red_bull | w_structure_low_close_stop_1pct_buffer_d40 | 100                   | 37.8378           | 54.0000                            | 0.8416         | -21.1905       | not_preferred_in_current_grid          |
