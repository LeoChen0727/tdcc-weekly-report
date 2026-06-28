# Structured Neckline Close-Only Failure Control Audit

- research_id: `structured_neckline_close_only_failure_control_audit`
- parameter_set_id: `structured_neckline_close_only_failure_control_audit_20260629`
- selected_exit_rule_comparison_id: `tp10_close_with_5pct_pullback_neutral`
- selected rule source: `tp10_close_with_5pct_pullback_neutral`
- execution basis: buy next open; sell by close-based rules only
- intraday +10% touch is not used
- production impact: `none`
- production_readiness: `not_production_ready_research_only`

## Summary

| research_id                                          | research_variant_id           | parameter_set_id                                              | advisory_status               | failure_control_scope_id                             | selected_exit_rule_comparison_id      | failure_control_rule_id         |   close_negative_stop_threshold_pct |   sample_size |   unique_stock_count |   win_count |   neutral_count |   loss_count |   pure_win_rate_pct |   neutral_inclusive_success_rate_pct |   positive_return_rate_pct |   avg_return_pct |   median_return_pct |   avg_max_close_return_pct |   median_max_close_return_pct |   avg_min_close_return_pct |   median_min_close_return_pct |   changed_from_source_count |   source_loss_to_non_loss_count |   source_non_loss_to_loss_count | approved_for_daily   | production_readiness               | generated_at                    |
|:-----------------------------------------------------|:------------------------------|:--------------------------------------------------------------|:------------------------------|:-----------------------------------------------------|:--------------------------------------|:--------------------------------|------------------------------------:|--------------:|---------------------:|------------:|----------------:|-------------:|--------------------:|-------------------------------------:|---------------------------:|-----------------:|--------------------:|---------------------------:|------------------------------:|---------------------------:|------------------------------:|----------------------------:|--------------------------------:|--------------------------------:|:---------------------|:-----------------------------------|:--------------------------------|
| structured_neckline_close_only_failure_control_audit | warning_research_variant_only | structured_neckline_close_only_failure_control_audit_20260629 | warning_research_variant_only | selected_close_based_exit_close_only_failure_control | tp10_close_with_5pct_pullback_neutral | close_only_no_negative_stop     |                                     |            23 |                   21 |          10 |              10 |            3 |             76.9231 |                              86.9565 |                    78.2609 |           4.7406 |              4.6025 |                     9.191  |                        9.2742 |                    -5.192  |                       -2.2436 |                           2 |                               2 |                               0 | false                | not_production_ready_research_only | 2026-06-29 01:01:08 Asia/Taipei |
| structured_neckline_close_only_failure_control_audit | warning_research_variant_only | structured_neckline_close_only_failure_control_audit_20260629 | warning_research_variant_only | selected_close_based_exit_close_only_failure_control | tp10_close_with_5pct_pullback_neutral | close_only_loss_stop_minus5pct  |                                  -5 |            23 |                   21 |           6 |              10 |            7 |             46.1538 |                              69.5652 |                    60.8696 |           2.4116 |              2.8605 |                     6.7081 |                        7.6115 |                    -2.8161 |                       -2.2436 |                           4 |                               1 |                               3 | false                | not_production_ready_research_only | 2026-06-29 01:01:08 Asia/Taipei |
| structured_neckline_close_only_failure_control_audit | warning_research_variant_only | structured_neckline_close_only_failure_control_audit_20260629 | warning_research_variant_only | selected_close_based_exit_close_only_failure_control | tp10_close_with_5pct_pullback_neutral | close_only_loss_stop_minus8pct  |                                  -8 |            23 |                   21 |           7 |              10 |            6 |             53.8462 |                              73.913  |                    65.2174 |           2.2675 |              3.3067 |                     7.2161 |                        7.8464 |                    -3.8311 |                       -2.2436 |                           3 |                               1 |                               2 | false                | not_production_ready_research_only | 2026-06-29 01:01:08 Asia/Taipei |
| structured_neckline_close_only_failure_control_audit | warning_research_variant_only | structured_neckline_close_only_failure_control_audit_20260629 | warning_research_variant_only | selected_close_based_exit_close_only_failure_control | tp10_close_with_5pct_pullback_neutral | close_only_loss_stop_minus10pct |                                 -10 |            23 |                   21 |           7 |              10 |            6 |             53.8462 |                              73.913  |                    65.2174 |           2.2675 |              3.3067 |                     7.2161 |                        7.8464 |                    -3.8311 |                       -2.2436 |                           3 |                               1 |                               2 | false                | not_production_ready_research_only | 2026-06-29 01:01:08 Asia/Taipei |

## Loss Rows By Rule

### close_only_loss_stop_minus5pct

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason         | outcome_transition_from_source   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:--------------------|:---------------------------------|
|       3704 | 合勤控       |      20250826 |            20250829 |      -7.9104 |                 1.3433 |                -7.9104 | close_negative_stop | win_to_loss                      |
|       3051 | 力特         |      20260116 |            20260121 |      -6.8266 |                 2.583  |                -6.8266 | close_negative_stop | loss_to_loss                     |
|       2363 | 矽統         |      20260121 |            20260128 |      -6.129  |                -6.129  |                -6.129  | close_negative_stop | loss_to_loss                     |
|       6290 | 良維         |      20260224 |            20260306 |      -7.2961 |                 2.7897 |                -7.2961 | close_negative_stop | loss_to_loss                     |
|       6173 | 信昌電       |      20260415 |            20260420 |      -5.3476 |                -2.9947 |                -5.3476 | close_negative_stop | win_to_loss                      |
|       6175 | 立敦         |      20260415 |            20260420 |      -7.8907 |                 0.4552 |                -7.8907 | close_negative_stop | win_to_loss                      |
|       6488 | 環球晶       |      20260421 |            20260428 |     -11.1111 |                -3.8143 |               -11.1111 | close_negative_stop | loss_to_loss                     |

### close_only_loss_stop_minus8pct

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason         | outcome_transition_from_source   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:--------------------|:---------------------------------|
|       3704 | 合勤控       |      20250826 |            20250829 |     -11.6418 |                 1.3433 |               -11.6418 | close_negative_stop | win_to_loss                      |
|       3051 | 力特         |      20260116 |            20260121 |     -10.5166 |                 2.583  |               -10.5166 | close_negative_stop | loss_to_loss                     |
|       2363 | 矽統         |      20260121 |            20260128 |     -10.8065 |                -6.129  |               -10.8065 | close_negative_stop | loss_to_loss                     |
|       6290 | 良維         |      20260224 |            20260306 |     -12.4464 |                 2.7897 |               -12.4464 | close_negative_stop | loss_to_loss                     |
|       6173 | 信昌電       |      20260415 |            20260420 |     -11.4439 |                -2.9947 |               -11.4439 | close_negative_stop | win_to_loss                      |
|       6488 | 環球晶       |      20260421 |            20260428 |     -11.1111 |                -3.8143 |               -11.1111 | close_negative_stop | loss_to_loss                     |

### close_only_loss_stop_minus10pct

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason         | outcome_transition_from_source   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:--------------------|:---------------------------------|
|       3704 | 合勤控       |      20250826 |            20250829 |     -11.6418 |                 1.3433 |               -11.6418 | close_negative_stop | win_to_loss                      |
|       3051 | 力特         |      20260116 |            20260121 |     -10.5166 |                 2.583  |               -10.5166 | close_negative_stop | loss_to_loss                     |
|       2363 | 矽統         |      20260121 |            20260128 |     -10.8065 |                -6.129  |               -10.8065 | close_negative_stop | loss_to_loss                     |
|       6290 | 良維         |      20260224 |            20260306 |     -12.4464 |                 2.7897 |               -12.4464 | close_negative_stop | loss_to_loss                     |
|       6173 | 信昌電       |      20260415 |            20260420 |     -11.4439 |                -2.9947 |               -11.4439 | close_negative_stop | win_to_loss                      |
|       6488 | 環球晶       |      20260421 |            20260428 |     -11.1111 |                -3.8143 |               -11.1111 | close_negative_stop | loss_to_loss                     |

### close_only_no_negative_stop

|   stock_id | stock_name   |   signal_date |   retest_entry_date |   return_pct |   max_close_return_pct |   min_close_return_pct | exit_reason                        | outcome_transition_from_source   |
|-----------:|:-------------|--------------:|--------------------:|-------------:|-----------------------:|-----------------------:|:-----------------------------------|:---------------------------------|
|       3051 | 力特         |      20260116 |            20260121 |     -14.5756 |                 2.583  |               -18.2657 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                     |
|       2363 | 矽統         |      20260121 |            20260128 |     -18.2258 |                -6.129  |               -21.9355 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                     |
|       6290 | 良維         |      20260224 |            20260306 |     -17.5966 |                 3.4335 |               -17.8112 | fixed_20d_close_no_tp10_no_neutral | loss_to_loss                     |

## Boundary

- This is research/backtest advisory-only evidence.
- No production model condition, scoring, ranking, PDF logic, or baseline was changed.
- Failure-control rows are candidate exit definitions only, not production filters.
