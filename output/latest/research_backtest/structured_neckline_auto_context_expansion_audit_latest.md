# Structured Neckline Auto Context Expansion Audit

- research_id: `structured_neckline_auto_context_expansion_audit`
- parameter_set_id: `structured_neckline_auto_context_expansion_audit_20260629`
- source_pool: `all_retest_entries` from structured neckline retest entry/exit grid
- auto context window: 90 sessions before signal date through the trading day before signal date
- failure rules compared: `close_only_no_logical_failure_exit` and `neckline_close_lost_two_sessions`
- execution basis: buy next open; sell by close-based rules only
- intraday high/low trigger is not used
- production impact: `none`
- production_readiness: `not_production_ready_research_only`

## Key Summary

| analysis_scope_id                              | failure_exit_rule_id               |   sample_size |   win_count |   neutral_count |   loss_count |   neutral_inclusive_success_rate_pct |   avg_return_pct |   median_return_pct |
|:-----------------------------------------------|:-----------------------------------|--------------:|------------:|----------------:|-------------:|-------------------------------------:|-----------------:|--------------------:|
| all_retest_entries                             | close_only_no_logical_failure_exit |           374 |         147 |              75 |          152 |                              59.3583 |           1.7914 |              2.8634 |
| all_retest_entries                             | neckline_close_lost_two_sessions   |           374 |         133 |              72 |          169 |                              54.8128 |           1.0851 |              1.9922 |
| all_auto_non_bearish                           | close_only_no_logical_failure_exit |           318 |         129 |              61 |          128 |                              59.7484 |           1.9244 |              2.934  |
| all_auto_non_bearish                           | neckline_close_lost_two_sessions   |           318 |         115 |              60 |          143 |                              55.0314 |           1.1204 |              1.8782 |
| low_position_le60_market_bull                  | close_only_no_logical_failure_exit |            95 |          42 |              23 |           30 |                              68.4211 |           3.5294 |              3.8062 |
| low_position_le60_market_bull                  | neckline_close_lost_two_sessions   |            95 |          41 |              21 |           33 |                              65.2632 |           3.3251 |              3.629  |
| low_position_le60_market_bull_auto_non_bearish | close_only_no_logical_failure_exit |            48 |          27 |              11 |           10 |                              79.1667 |           5.5353 |             10.378  |
| low_position_le60_market_bull_auto_non_bearish | neckline_close_lost_two_sessions   |            48 |          26 |              11 |           11 |                              77.0833 |           5.7927 |             10.279  |

## Auto Context Distribution

| analysis_scope_id                              | auto_pre_signal_context   |   event_count |   win_count |   neutral_count |   loss_count |   neutral_inclusive_success_rate_pct |   avg_return_pct |
|:-----------------------------------------------|:--------------------------|--------------:|------------:|----------------:|-------------:|-------------------------------------:|-----------------:|
| all_retest_entries                             | bearish                   |            56 |          18 |              14 |           24 |                              57.1429 |           1.036  |
| all_retest_entries                             | sideways_or_consolidation |            58 |          14 |               7 |           37 |                              36.2069 |          -0.2716 |
| all_retest_entries                             | slow_uptrend              |           172 |          77 |              32 |           63 |                              63.3721 |           2.7447 |
| all_retest_entries                             | volatile_mixed            |            88 |          38 |              22 |           28 |                              68.1818 |           1.7683 |
| all_auto_non_bearish                           | sideways_or_consolidation |            58 |          14 |               7 |           37 |                              36.2069 |          -0.2716 |
| all_auto_non_bearish                           | slow_uptrend              |           172 |          77 |              32 |           63 |                              63.3721 |           2.7447 |
| all_auto_non_bearish                           | volatile_mixed            |            88 |          38 |              22 |           28 |                              68.1818 |           1.7683 |
| all_auto_bearish                               | bearish                   |            56 |          18 |              14 |           24 |                              57.1429 |           1.036  |
| low_position_le60_market_bull                  | bearish                   |            47 |          15 |              12 |           20 |                              57.4468 |           1.4809 |
| low_position_le60_market_bull                  | sideways_or_consolidation |             7 |           3 |               1 |            3 |                              57.1429 |           2.5884 |
| low_position_le60_market_bull                  | slow_uptrend              |            16 |          13 |               2 |            1 |                              93.75   |          10.0183 |
| low_position_le60_market_bull                  | volatile_mixed            |            25 |          11 |               8 |            6 |                              76      |           3.4914 |
| low_position_le60_market_bull_auto_non_bearish | sideways_or_consolidation |             7 |           3 |               1 |            3 |                              57.1429 |           2.5884 |
| low_position_le60_market_bull_auto_non_bearish | slow_uptrend              |            16 |          13 |               2 |            1 |                              93.75   |          10.0183 |
| low_position_le60_market_bull_auto_non_bearish | volatile_mixed            |            25 |          11 |               8 |            6 |                              76      |           3.4914 |
| low_position_le60_market_bull_auto_bearish     | bearish                   |            47 |          15 |              12 |           20 |                              57.4468 |           1.4809 |

## Boundary

- This is research/backtest advisory-only evidence.
- No production model condition, scoring, ranking, PDF logic, or baseline was changed.
- Auto context labels are candidate research labels only, not production filters.
