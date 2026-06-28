# Structured Neckline Logical Failure Exit Audit

- research_id: `structured_neckline_logical_failure_exit_audit`
- parameter_set_id: `structured_neckline_logical_failure_exit_audit_20260629`
- baseline_rule_id: `close_only_no_logical_failure_exit`
- execution basis: buy next open; sell by close-based rules only
- intraday high/low trigger is not used
- production impact: `none`
- production_readiness: `not_production_ready_research_only`

## Summary

| research_id                                    | research_variant_id           | parameter_set_id                                        | advisory_status               | failure_exit_scope_id                     | failure_exit_rule_id               |   sample_size |   unique_stock_count |   win_count |   neutral_count |   loss_count |   pure_win_rate_pct |   neutral_inclusive_success_rate_pct |   positive_return_rate_pct |   avg_return_pct |   median_return_pct |   avg_max_close_return_pct |   median_max_close_return_pct |   avg_min_close_return_pct |   median_min_close_return_pct |   changed_from_baseline_count |   baseline_loss_to_non_loss_count |   baseline_non_loss_to_loss_count | approved_for_daily   | production_readiness               | generated_at                    |
|:-----------------------------------------------|:------------------------------|:--------------------------------------------------------|:------------------------------|:------------------------------------------|:-----------------------------------|--------------:|---------------------:|------------:|----------------:|-------------:|--------------------:|-------------------------------------:|---------------------------:|-----------------:|--------------------:|---------------------------:|------------------------------:|---------------------------:|------------------------------:|------------------------------:|----------------------------------:|----------------------------------:|:---------------------|:-----------------------------------|:--------------------------------|
| structured_neckline_logical_failure_exit_audit | warning_research_variant_only | structured_neckline_logical_failure_exit_audit_20260629 | warning_research_variant_only | selected_close_based_logical_failure_exit | close_only_no_logical_failure_exit |            23 |                   21 |          10 |              10 |            3 |             76.9231 |                              86.9565 |                    78.2609 |           4.7406 |              4.6025 |                     9.191  |                        9.2742 |                    -5.192  |                       -2.2436 |                             0 |                                 0 |                                 0 | false                | not_production_ready_research_only | 2026-06-29 01:28:20 Asia/Taipei |
| structured_neckline_logical_failure_exit_audit | warning_research_variant_only | structured_neckline_logical_failure_exit_audit_20260629 | warning_research_variant_only | selected_close_based_logical_failure_exit | neckline_close_lost_two_sessions   |            23 |                   21 |          10 |              10 |            3 |             76.9231 |                              86.9565 |                    78.2609 |           4.8712 |              4.6025 |                     9.191  |                        9.2742 |                    -5.0307 |                       -2.2436 |                             0 |                                 0 |                                 0 | false                | not_production_ready_research_only | 2026-06-29 01:28:20 Asia/Taipei |
| structured_neckline_logical_failure_exit_audit | warning_research_variant_only | structured_neckline_logical_failure_exit_audit_20260629 | warning_research_variant_only | selected_close_based_logical_failure_exit | retest_low_close_break             |            23 |                   21 |           8 |              10 |            5 |             61.5385 |                              78.2609 |                    73.913  |           2.9652 |              3.629  |                     7.7483 |                        8.311  |                    -4.8765 |                       -2.2436 |                             2 |                                 0 |                                 2 | false                | not_production_ready_research_only | 2026-06-29 01:28:20 Asia/Taipei |
| structured_neckline_logical_failure_exit_audit | warning_research_variant_only | structured_neckline_logical_failure_exit_audit_20260629 | warning_research_variant_only | selected_close_based_logical_failure_exit | signal_low_close_break             |            23 |                   21 |           9 |              10 |            4 |             69.2308 |                              82.6087 |                    73.913  |           3.7939 |              3.8202 |                     8.5709 |                        8.3333 |                    -5.0307 |                       -2.2436 |                             1 |                                 0 |                                 1 | false                | not_production_ready_research_only | 2026-06-29 01:28:20 Asia/Taipei |
| structured_neckline_logical_failure_exit_audit | warning_research_variant_only | structured_neckline_logical_failure_exit_audit_20260629 | warning_research_variant_only | selected_close_based_logical_failure_exit | close_below_5ma_two_sessions       |            23 |                   21 |           7 |               8 |            8 |             46.6667 |                              65.2174 |                    56.5217 |           2.0345 |              2.6247 |                     6.6149 |                        7.8464 |                    -3.5184 |                       -2.2436 |                             5 |                                 0 |                                 5 | false                | not_production_ready_research_only | 2026-06-29 01:28:20 Asia/Taipei |
| structured_neckline_logical_failure_exit_audit | warning_research_variant_only | structured_neckline_logical_failure_exit_audit_20260629 | warning_research_variant_only | selected_close_based_logical_failure_exit | close_below_10ma_two_sessions      |            23 |                   21 |           8 |               8 |            7 |             53.3333 |                              69.5652 |                    60.8696 |           2.3739 |              2.8605 |                     7.235  |                        8.311  |                    -4.2837 |                       -2.2436 |                             4 |                                 0 |                                 4 | false                | not_production_ready_research_only | 2026-06-29 01:28:20 Asia/Taipei |

## Loss Rows By Rule

### close_below_5ma_two_sessions

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason                  | outcome_transition_from_baseline   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:-----------------------------|:-----------------------------------|
|       3260 | 威剛         |      20250217 |            20250226 |      -3.5348 |                -1.1403 |                -3.5348 | close_below_5ma_two_sessions | neutral_to_loss                    |
|       3714 | 富采         |      20251231 |            20260106 |      -2.5105 |                 1.9526 |                -2.5105 | close_below_5ma_two_sessions | neutral_to_loss                    |
|       3051 | 力特         |      20260116 |            20260121 |      -4.059  |                 2.583  |                -4.059  | close_below_5ma_two_sessions | loss_to_loss                       |
|       2363 | 矽統         |      20260121 |            20260128 |     -14.6774 |                -6.129  |               -14.6774 | close_below_5ma_two_sessions | loss_to_loss                       |
|       6290 | 良維         |      20260224 |            20260306 |     -12.4464 |                 2.7897 |               -12.4464 | close_below_5ma_two_sessions | loss_to_loss                       |
|       6173 | 信昌電       |      20260415 |            20260420 |     -11.4439 |                -2.9947 |               -11.4439 | close_below_5ma_two_sessions | win_to_loss                        |
|       6175 | 立敦         |      20260415 |            20260420 |      -3.6419 |                 0.4552 |                -4.4006 | close_below_5ma_two_sessions | win_to_loss                        |
|       6488 | 環球晶       |      20260421 |            20260428 |     -11.1111 |                -3.8143 |               -11.1111 | close_below_5ma_two_sessions | win_to_loss                        |

### close_below_10ma_two_sessions

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason                   | outcome_transition_from_baseline   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:------------------------------|:-----------------------------------|
|       3260 | 威剛         |      20250217 |            20250226 |      -3.5348 |                -1.1403 |                -3.5348 | close_below_10ma_two_sessions | neutral_to_loss                    |
|       3714 | 富采         |      20251231 |            20260106 |      -2.371  |                 1.9526 |                -2.5105 | close_below_10ma_two_sessions | neutral_to_loss                    |
|       3051 | 力特         |      20260116 |            20260121 |      -7.5646 |                 2.583  |                -7.5646 | close_below_10ma_two_sessions | loss_to_loss                       |
|       2363 | 矽統         |      20260121 |            20260128 |     -18.2258 |                -6.129  |               -18.2258 | close_below_10ma_two_sessions | loss_to_loss                       |
|       6290 | 良維         |      20260224 |            20260306 |     -12.4464 |                 2.7897 |               -12.4464 | close_below_10ma_two_sessions | loss_to_loss                       |
|       6173 | 信昌電       |      20260415 |            20260420 |     -17.2193 |                -2.9947 |               -18.5027 | close_below_10ma_two_sessions | win_to_loss                        |
|       6175 | 立敦         |      20260415 |            20260420 |      -4.7041 |                 0.4552 |                -7.8907 | close_below_10ma_two_sessions | win_to_loss                        |

### retest_low_close_break

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason            | outcome_transition_from_baseline   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:-----------------------|:-----------------------------------|
|       1528 | 恩德         |      20250221 |            20250227 |       2.3649 |                 2.3649 |                 2.3649 | retest_low_close_break | win_to_loss                        |
|       3051 | 力特         |      20260116 |            20260121 |     -18.2657 |                 2.583  |               -18.2657 | retest_low_close_break | loss_to_loss                       |
|       2363 | 矽統         |      20260121 |            20260128 |     -14.6774 |                -6.129  |               -14.6774 | retest_low_close_break | loss_to_loss                       |
|       6290 | 良維         |      20260224 |            20260306 |     -17.8112 |                 3.4335 |               -17.8112 | retest_low_close_break | loss_to_loss                       |
|       6488 | 環球晶       |      20260421 |            20260428 |     -11.1111 |                -3.8143 |               -11.1111 | retest_low_close_break | win_to_loss                        |

### close_only_no_logical_failure_exit

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason                        | outcome_transition_from_baseline   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:-----------------------------------|:-----------------------------------|
|       3051 | 力特         |      20260116 |            20260121 |     -14.5756 |                 2.583  |               -18.2657 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                       |
|       2363 | 矽統         |      20260121 |            20260128 |     -18.2258 |                -6.129  |               -21.9355 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                       |
|       6290 | 良維         |      20260224 |            20260306 |     -17.5966 |                 3.4335 |               -17.8112 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                       |

### neckline_close_lost_two_sessions

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason                        | outcome_transition_from_baseline   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:-----------------------------------|:-----------------------------------|
|       3051 | 力特         |      20260116 |            20260121 |     -14.5756 |                 2.583  |               -18.2657 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                       |
|       2363 | 矽統         |      20260121 |            20260128 |     -18.2258 |                -6.129  |               -18.2258 | neckline_close_lost_two_sessions   | loss_to_loss                       |
|       6290 | 良維         |      20260224 |            20260306 |     -14.5923 |                 3.4335 |               -17.8112 | neckline_close_lost_two_sessions   | loss_to_loss                       |

### signal_low_close_break

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason                        | outcome_transition_from_baseline   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:-----------------------------------|:-----------------------------------|
|       3051 | 力特         |      20260116 |            20260121 |     -14.5756 |                 2.583  |               -18.2657 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                       |
|       2363 | 矽統         |      20260121 |            20260128 |     -18.2258 |                -6.129  |               -18.2258 | signal_low_close_break             | loss_to_loss                       |
|       6290 | 良維         |      20260224 |            20260306 |     -17.8112 |                 3.4335 |               -17.8112 | signal_low_close_break             | loss_to_loss                       |
|       6488 | 環球晶       |      20260421 |            20260428 |     -11.1111 |                -3.8143 |               -11.1111 | signal_low_close_break             | win_to_loss                        |

## Boundary

- This is research/backtest advisory-only evidence.
- No production model condition, scoring, ranking, PDF logic, or baseline was changed.
- Logical failure rows are candidate exit definitions only, not production filters.
