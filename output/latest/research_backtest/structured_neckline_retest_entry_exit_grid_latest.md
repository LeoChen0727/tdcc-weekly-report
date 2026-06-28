# Structured Neckline Retest Entry Exit Grid

- generated_at: `2026-06-27 18:37:19 Asia/Taipei`
- research_id: `structured_neckline_retest_entry_exit_grid`
- source_research_id: `breakout_family_retest_grid`
- source_parameter_set_id: `breakout_family_retest_grid_20260627`
- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.
- advisory status: `warning_research_variant_only`; approved_for_daily=false; production readiness is `not_production_ready_research_only`.

## Scope

This grid only evaluates structured neckline events that already passed the research retest-not-broken then renewed attack entry path. It asks which stop and exit/outcome definition works better after that entry exists.

Stop rules tested: `signal_low_stop`, `retest_low_stop`, `neckline_minus_2pct_stop`, and `source_retest_or_neckline_2pct_stop`.

Exit/outcome rules tested: `fixed_10d_close`, `fixed_20d_close`, `tp10_intraday_or_fixed_20d_close`, and `tp10_close_or_neutral_after_5pct_close_20d`.

Metric definitions: `pure_win_rate_pct` excludes neutral rows and is win / (win + loss). `neutral_inclusive_success_rate_pct` counts win plus neutral over evaluated rows. These are intentionally separate, so neutral is not silently renamed as win rate. `positive_return_rate_pct`, `avg_return_pct`, and `median_return_pct` are included because win rate alone is not enough when rule results are close.

Intraday ordering is conservative: if a stop and a 10% target are both touched on the same day, the stop is counted first because the intraday sequence is unknown.

TDCC segmentation is evaluated at the retest-entry date, not the original signal date, because this grid is about the actual retest-entry buy point.

## Top All-Retest Rule Combinations

| stop_rule_id | exit_rule_id | sample_size | evaluated_sample_size | pure_win_rate_pct | neutral_inclusive_success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct | stop_hit_count | tp10_hit_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 374 | 43.0464 | 54.0107 | 54.2781 | 1.3684 | 1.8246 | 126 | 130 |
| neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 374 | 41.4474 | 52.4064 | 51.8717 | 0.8057 | 0.9479 | 138 | 126 |
| source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 374 | 41.4474 | 52.4064 | 52.1390 | 0.8057 | 1.0895 | 136 | 126 |
| signal_low_stop | tp10_intraday_or_fixed_20d_close | 374 | 374 | 50.0000 | 50.0000 | 55.0802 | 0.8569 | 9.6624 | 134 | 187 |
| source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | 374 | 374 | 48.9305 | 48.9305 | 53.4759 | 0.5189 | 5.0973 | 143 | 183 |
| neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | 374 | 374 | 48.6631 | 48.6631 | 53.2086 | 0.5187 | 4.4041 | 145 | 182 |
| retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 374 | 37.1336 | 48.3957 | 47.0588 | 0.7130 | -0.8332 | 171 | 114 |
| retest_low_stop | tp10_intraday_or_fixed_20d_close | 374 | 374 | 44.6524 | 44.6524 | 47.5936 | 0.4893 | -0.7100 | 181 | 167 |
| signal_low_stop | fixed_10d_close | 374 | 374 | 43.5829 | 43.5829 | 43.5829 | 0.9862 | -1.1566 | 108 | 0 |
| neckline_minus_2pct_stop | fixed_10d_close | 374 | 374 | 43.3155 | 43.3155 | 43.3155 | 0.8653 | -1.7509 | 122 | 0 |
| source_retest_or_neckline_2pct_stop | fixed_10d_close | 374 | 374 | 43.3155 | 43.3155 | 43.3155 | 0.8222 | -1.7509 | 120 | 0 |
| signal_low_stop | fixed_20d_close | 374 | 374 | 42.7807 | 42.7807 | 42.7807 | 4.0226 | -1.8397 | 156 | 0 |
| source_retest_or_neckline_2pct_stop | fixed_20d_close | 374 | 374 | 41.1765 | 41.1765 | 41.1765 | 3.2574 | -3.9632 | 169 | 0 |
| neckline_minus_2pct_stop | fixed_20d_close | 374 | 374 | 40.9091 | 40.9091 | 40.9091 | 3.2869 | -3.9632 | 171 | 0 |
| retest_low_stop | fixed_10d_close | 374 | 374 | 38.2353 | 38.2353 | 38.2353 | 0.4562 | -2.9152 | 172 | 0 |
| retest_low_stop | fixed_20d_close | 374 | 374 | 35.2941 | 35.2941 | 35.2941 | 2.7204 | -3.9180 | 212 | 0 |

## Segment Summary

| segment_id | stop_rule_id | exit_rule_id | sample_size | pure_win_rate_pct | neutral_inclusive_success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_retest_entries | neckline_minus_2pct_stop | fixed_10d_close | 374 | 43.3155 | 43.3155 | 43.3155 | 0.8653 | -1.7509 |
| all_retest_entries | neckline_minus_2pct_stop | fixed_20d_close | 374 | 40.9091 | 40.9091 | 40.9091 | 3.2869 | -3.9632 |
| all_retest_entries | neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 41.4474 | 52.4064 | 51.8717 | 0.8057 | 0.9479 |
| all_retest_entries | neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | 374 | 48.6631 | 48.6631 | 53.2086 | 0.5187 | 4.4041 |
| all_retest_entries | retest_low_stop | fixed_10d_close | 374 | 38.2353 | 38.2353 | 38.2353 | 0.4562 | -2.9152 |
| all_retest_entries | retest_low_stop | fixed_20d_close | 374 | 35.2941 | 35.2941 | 35.2941 | 2.7204 | -3.9180 |
| all_retest_entries | retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 37.1336 | 48.3957 | 47.0588 | 0.7130 | -0.8332 |
| all_retest_entries | retest_low_stop | tp10_intraday_or_fixed_20d_close | 374 | 44.6524 | 44.6524 | 47.5936 | 0.4893 | -0.7100 |
| all_retest_entries | signal_low_stop | fixed_10d_close | 374 | 43.5829 | 43.5829 | 43.5829 | 0.9862 | -1.1566 |
| all_retest_entries | signal_low_stop | fixed_20d_close | 374 | 42.7807 | 42.7807 | 42.7807 | 4.0226 | -1.8397 |
| all_retest_entries | signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 43.0464 | 54.0107 | 54.2781 | 1.3684 | 1.8246 |
| all_retest_entries | signal_low_stop | tp10_intraday_or_fixed_20d_close | 374 | 50.0000 | 50.0000 | 55.0802 | 0.8569 | 9.6624 |
| all_retest_entries | source_retest_or_neckline_2pct_stop | fixed_10d_close | 374 | 43.3155 | 43.3155 | 43.3155 | 0.8222 | -1.7509 |
| all_retest_entries | source_retest_or_neckline_2pct_stop | fixed_20d_close | 374 | 41.1765 | 41.1765 | 41.1765 | 3.2574 | -3.9632 |
| all_retest_entries | source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 374 | 41.4474 | 52.4064 | 52.1390 | 0.8057 | 1.0895 |
| all_retest_entries | source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | 374 | 48.9305 | 48.9305 | 53.4759 | 0.5189 | 5.0973 |
| low_position_le60 | neckline_minus_2pct_stop | fixed_10d_close | 105 | 47.6190 | 47.6190 | 47.6190 | 2.3467 | 0.0000 |
| low_position_le60 | neckline_minus_2pct_stop | fixed_20d_close | 105 | 52.3810 | 52.3810 | 52.3810 | 8.7012 | 1.8657 |
| low_position_le60 | neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 105 | 50.0000 | 60.9524 | 60.0000 | 2.6342 | 2.8605 |
| low_position_le60 | neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | 105 | 56.1905 | 56.1905 | 61.9048 | 2.9568 | 10.0000 |
| low_position_le60 | retest_low_stop | fixed_10d_close | 105 | 41.9048 | 41.9048 | 41.9048 | 1.2432 | -1.7143 |
| low_position_le60 | retest_low_stop | fixed_20d_close | 105 | 43.8095 | 43.8095 | 43.8095 | 6.0342 | -2.8777 |
| low_position_le60 | retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 105 | 44.0476 | 55.2381 | 53.3333 | 1.6632 | 2.5862 |
| low_position_le60 | retest_low_stop | tp10_intraday_or_fixed_20d_close | 105 | 50.4762 | 50.4762 | 53.3333 | 1.8567 | 10.0000 |
| low_position_le60 | signal_low_stop | fixed_10d_close | 105 | 49.5238 | 49.5238 | 49.5238 | 3.1223 | 0.0000 |
| low_position_le60 | signal_low_stop | fixed_20d_close | 105 | 56.1905 | 56.1905 | 56.1905 | 10.2856 | 2.8169 |
| low_position_le60 | signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 105 | 55.0000 | 65.7143 | 64.7619 | 3.9165 | 3.6290 |
| low_position_le60 | signal_low_stop | tp10_intraday_or_fixed_20d_close | 105 | 60.0000 | 60.0000 | 65.7143 | 3.5581 | 10.0000 |
| low_position_le60 | source_retest_or_neckline_2pct_stop | fixed_10d_close | 105 | 47.6190 | 47.6190 | 47.6190 | 2.2714 | 0.0000 |
| low_position_le60 | source_retest_or_neckline_2pct_stop | fixed_20d_close | 105 | 52.3810 | 52.3810 | 52.3810 | 8.6259 | 1.8657 |
| low_position_le60 | source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 105 | 50.0000 | 60.9524 | 60.0000 | 2.5596 | 2.8605 |
| low_position_le60 | source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | 105 | 56.1905 | 56.1905 | 61.9048 | 2.8815 | 10.0000 |
| low_position_le60_market_bull | neckline_minus_2pct_stop | fixed_10d_close | 95 | 46.3158 | 46.3158 | 46.3158 | 2.3941 | -0.2401 |
| low_position_le60_market_bull | neckline_minus_2pct_stop | fixed_20d_close | 95 | 50.5263 | 50.5263 | 50.5263 | 8.4918 | 0.1493 |
| low_position_le60_market_bull | neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 95 | 50.6667 | 61.0526 | 61.0526 | 2.7027 | 2.8605 |
| low_position_le60_market_bull | neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | 95 | 57.8947 | 57.8947 | 61.0526 | 2.8487 | 10.0000 |
| low_position_le60_market_bull | retest_low_stop | fixed_10d_close | 95 | 40.0000 | 40.0000 | 40.0000 | 1.1704 | -2.8777 |
| low_position_le60_market_bull | retest_low_stop | fixed_20d_close | 95 | 42.1053 | 42.1053 | 42.1053 | 5.7734 | -2.8793 |
| low_position_le60_market_bull | retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 95 | 44.1558 | 54.7368 | 53.6842 | 1.6756 | 2.5862 |
| low_position_le60_market_bull | retest_low_stop | tp10_intraday_or_fixed_20d_close | 95 | 51.5789 | 51.5789 | 52.6316 | 1.8620 | 10.0000 |
| low_position_le60_market_bull | signal_low_stop | fixed_10d_close | 95 | 48.4211 | 48.4211 | 48.4211 | 3.2290 | 0.0000 |
| low_position_le60_market_bull | signal_low_stop | fixed_20d_close | 95 | 53.6842 | 53.6842 | 53.6842 | 9.9964 | 2.1858 |
| low_position_le60_market_bull | signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 95 | 54.7945 | 65.2632 | 65.2632 | 3.3070 | 3.3067 |
| low_position_le60_market_bull | signal_low_stop | tp10_intraday_or_fixed_20d_close | 95 | 61.0526 | 61.0526 | 64.2105 | 3.2765 | 10.0000 |
| low_position_le60_market_bull | source_retest_or_neckline_2pct_stop | fixed_10d_close | 95 | 46.3158 | 46.3158 | 46.3158 | 2.3243 | -0.2401 |
| low_position_le60_market_bull | source_retest_or_neckline_2pct_stop | fixed_20d_close | 95 | 50.5263 | 50.5263 | 50.5263 | 8.4220 | 0.1493 |
| low_position_le60_market_bull | source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 95 | 50.6667 | 61.0526 | 61.0526 | 2.6336 | 2.8605 |
| low_position_le60_market_bull | source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | 95 | 57.8947 | 57.8947 | 61.0526 | 2.7788 | 10.0000 |
| market_regime_bull | neckline_minus_2pct_stop | fixed_10d_close | 323 | 44.8916 | 44.8916 | 44.8916 | 1.3456 | -1.5670 |
| market_regime_bull | neckline_minus_2pct_stop | fixed_20d_close | 323 | 41.4861 | 41.4861 | 41.4861 | 3.5281 | -3.8153 |
| market_regime_bull | neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 323 | 43.3460 | 53.8700 | 53.8700 | 0.8840 | 1.8657 |
| market_regime_bull | neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | 323 | 51.0836 | 51.0836 | 54.4892 | 0.7746 | 10.0000 |
| market_regime_bull | retest_low_stop | fixed_10d_close | 323 | 39.0093 | 39.0093 | 39.0093 | 0.7329 | -2.8846 |
| market_regime_bull | retest_low_stop | fixed_20d_close | 323 | 35.6037 | 35.6037 | 35.6037 | 2.6902 | -3.8813 |
| market_regime_bull | retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 323 | 38.7218 | 49.5356 | 48.9164 | 0.7596 | 0.0000 |
| market_regime_bull | retest_low_stop | tp10_intraday_or_fixed_20d_close | 323 | 46.7492 | 46.7492 | 48.9164 | 0.6968 | 0.0000 |
| market_regime_bull | signal_low_stop | fixed_10d_close | 323 | 45.2012 | 45.2012 | 45.2012 | 1.4900 | -1.0057 |
| market_regime_bull | signal_low_stop | fixed_20d_close | 323 | 43.3437 | 43.3437 | 43.3437 | 4.3023 | -1.7261 |
| market_regime_bull | signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 323 | 44.8276 | 55.4180 | 56.3467 | 1.2804 | 2.4735 |
| market_regime_bull | signal_low_stop | tp10_intraday_or_fixed_20d_close | 323 | 52.3220 | 52.3220 | 56.3467 | 1.0863 | 10.0000 |
| market_regime_bull | source_retest_or_neckline_2pct_stop | fixed_10d_close | 323 | 44.8916 | 44.8916 | 44.8916 | 1.2894 | -1.5670 |
| market_regime_bull | source_retest_or_neckline_2pct_stop | fixed_20d_close | 323 | 41.7957 | 41.7957 | 41.7957 | 3.4877 | -3.8153 |
| market_regime_bull | source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 323 | 43.3460 | 53.8700 | 54.1796 | 0.8739 | 1.9729 |
| market_regime_bull | source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | 323 | 51.3932 | 51.3932 | 54.7988 | 0.7647 | 10.0000 |
| market_regime_correction | neckline_minus_2pct_stop | fixed_10d_close | 24 | 33.3333 | 33.3333 | 33.3333 | -1.8732 | -5.0436 |
| market_regime_correction | neckline_minus_2pct_stop | fixed_20d_close | 24 | 29.1667 | 29.1667 | 29.1667 | 2.4929 | -6.3668 |
| market_regime_correction | neckline_minus_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 24 | 33.3333 | 50.0000 | 37.5000 | 2.6319 | -4.5287 |
| market_regime_correction | neckline_minus_2pct_stop | tp10_intraday_or_fixed_20d_close | 24 | 37.5000 | 37.5000 | 41.6667 | -0.8559 | -5.0436 |
| market_regime_correction | retest_low_stop | fixed_10d_close | 24 | 33.3333 | 33.3333 | 33.3333 | -0.5914 | -4.0489 |
| market_regime_correction | retest_low_stop | fixed_20d_close | 24 | 29.1667 | 29.1667 | 29.1667 | 4.5909 | -4.0489 |
| market_regime_correction | retest_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 24 | 27.7778 | 45.8333 | 33.3333 | 1.9310 | -3.6397 |
| market_regime_correction | retest_low_stop | tp10_intraday_or_fixed_20d_close | 24 | 33.3333 | 33.3333 | 37.5000 | -0.4704 | -3.6397 |
| market_regime_correction | signal_low_stop | fixed_10d_close | 24 | 33.3333 | 33.3333 | 33.3333 | -1.1850 | -2.7363 |
| market_regime_correction | signal_low_stop | fixed_20d_close | 24 | 29.1667 | 29.1667 | 29.1667 | 3.5689 | -3.5273 |
| market_regime_correction | signal_low_stop | tp10_close_or_neutral_after_5pct_close_20d | 24 | 33.3333 | 50.0000 | 37.5000 | 3.7665 | -1.1816 |
| market_regime_correction | signal_low_stop | tp10_intraday_or_fixed_20d_close | 24 | 37.5000 | 37.5000 | 41.6667 | 0.2023 | -1.2090 |
| market_regime_correction | source_retest_or_neckline_2pct_stop | fixed_10d_close | 24 | 33.3333 | 33.3333 | 33.3333 | -1.7808 | -5.6693 |
| market_regime_correction | source_retest_or_neckline_2pct_stop | fixed_20d_close | 24 | 29.1667 | 29.1667 | 29.1667 | 2.5851 | -6.0603 |
| market_regime_correction | source_retest_or_neckline_2pct_stop | tp10_close_or_neutral_after_5pct_close_20d | 24 | 33.3333 | 50.0000 | 37.5000 | 2.7759 | -4.8724 |
| market_regime_correction | source_retest_or_neckline_2pct_stop | tp10_intraday_or_fixed_20d_close | 24 | 37.5000 | 37.5000 | 41.6667 | -0.7119 | -5.5646 |

## Research Boundary

- This grid does not promote structured neckline or W-bottom breakout logic to production.
- It does not write research variants into the production baseline.
- It does not modify `daily_full_pipeline`, production PDF renderers, stock model contracts, ranking, or scoring.
- A formal promotion/sync PR is still required before any production model change.

Detail rows: `20544`
Summary rows: `144`
