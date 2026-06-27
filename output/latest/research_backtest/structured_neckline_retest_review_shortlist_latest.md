# Structured Neckline Retest Review Shortlist

- generated_at: `2026-06-27 20:06:00 Asia/Taipei`
- research_id: `structured_neckline_retest_review_shortlist`
- source_research_id: `structured_neckline_retest_review_packet`
- source_parameter_set_id: `structured_neckline_retest_review_packet_20260627`
- focus_exit_rule_ids: `tp10_intraday_or_fixed_20d_close;tp10_close_or_neutral_after_5pct_close_20d`
- segment_id: `low_position_le60_market_bull`
- stop_rule_id: `signal_low_stop`
- chart_root: `output\latest\research_backtest\structured_neckline_retest_shortlist`
- shortlist_chart_count: `55`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this shortlist does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Selection Purpose

This shortlist reduces the 380-chart structured-neckline retest packet to a manual review set for the two 10% exit rules. It selects return extremes, median cases, missed-upside cases, drawdown-risk cases, lowest-position cases, and wide-base cases. The selection is evidence triage only; it is not a production model rule.

## Outcome Summary

| exit_rule_id | outcome_result | shortlist_rows | unique_stocks | avg_return_pct | median_return_pct | avg_mfe_pct | avg_mae_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 11 | 11 | -8.3690 | -8.0702 | 4.2260 | -11.8705 |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 11 | 11 | 2.4403 | 2.8605 | 11.4748 | -3.2242 |
| tp10_close_or_neutral_after_5pct_close_20d | win | 11 | 11 | 13.2893 | 11.4613 | 13.9667 | -6.8159 |
| tp10_intraday_or_fixed_20d_close | loss | 13 | 13 | -6.9066 | -6.9277 | 5.2130 | -10.8060 |
| tp10_intraday_or_fixed_20d_close | win | 9 | 8 | 10.0000 | 10.0000 | 11.9613 | -6.2187 |

## Selection Reason Counts

| selection_reason | row_count |
| --- | --- |
| top_return_review | 15 |
| bottom_return_review | 15 |
| median_return_review | 10 |
| missed_upside_review | 8 |
| drawdown_risk_review | 8 |
| lowest_position_review | 6 |
| wide_base_review | 6 |

## Review Index

| exit_rule_id | outcome_result | stock_id | stock_name | signal_date | retest_entry_date | return_pct | mfe_pct | mae_pct | selection_reasons | shortlist_chart_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 6290 | 良維 | 20260224 | 20260306 | -16.9528 | 5.5794 | -18.2403 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260224_6290_20260306_loss_-16.9528.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3013 | 晟銘電 | 20260417 | 20260423 | -15.2610 | 1.2048 | -16.4659 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260417_3013_20260423_loss_-15.2610.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 2363 | 矽統 | 20260121 | 20260128 | -17.7419 | 2.4194 | -19.3548 | bottom_return_review;drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260121_2363_20260128_loss_-17.7419.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3051 | 力特 | 20260116 | 20260121 | -14.5756 | 8.4871 | -18.4502 | drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260116_3051_20260121_loss_-14.5756.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3230 | 錦明 | 20260211 | 20260303 | -11.2676 | 1.4085 | -18.3099 | drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260211_3230_20260303_loss_-11.2676.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 6147 | 頎邦 | 20260107 | 20260114 | -4.9123 | 5.2632 | -6.8421 | lowest_position_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260107_6147_20260114_loss_-4.9123.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3545 | 敦泰 | 20260119 | 20260127 | -8.0702 | 0.5263 | -8.2456 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260119_3545_20260127_loss_-8.0702.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 6488 | 環球晶 | 20260421 | 20260428 | -7.9602 | 0.1658 | -11.4428 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260421_6488_20260428_loss_-7.9602.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 1305 | 華夏 | 20250213 | 20250220 | 1.8657 | 4.4776 | -4.4776 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20250213_1305_20250220_loss_1.8657.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 1528 | 恩德 | 20250221 | 20250227 | 0.0000 | 7.0946 | -1.3514 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20250221_1528_20250227_loss_0.0000.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3481 | 群創 | 20250821 | 20250829 | 2.8169 | 9.8592 | -7.3944 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/03_loss/20250821_3481_20250829_loss_2.8169.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3163 | 波若威 | 20250106 | 20250109 | -2.2436 | 11.5385 | -2.2436 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250106_3163_20250109_neutral_-2.2436.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 8358 | 金居 | 20260415 | 20260420 | -0.8043 | 11.5282 | -4.9598 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20260415_8358_20260420_neutral_-0.8043.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 6197 | 佳必琪 | 20260311 | 20260316 | 0.8403 | 12.6050 | -5.6022 | bottom_return_review;missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20260311_6197_20260316_neutral_0.8403.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 2455 | 全新 | 20250611 | 20250625 | 2.7559 | 11.4173 | -3.5433 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250611_2455_20250625_neutral_2.7559.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 6706 | 惠特 | 20250918 | 20250930 | 2.8605 | 15.4946 | -0.4768 | median_return_review;missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250918_6706_20250930_neutral_2.8605.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3037 | 欣興 | 20250703 | 20250710 | 3.6290 | 14.1129 | -3.6290 | missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250703_3037_20250710_neutral_3.6290.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 1727 | 中華化 | 20250723 | 20250728 | 3.2258 | 15.8065 | -0.6452 | missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250723_1727_20250728_neutral_3.2258.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 2368 | 金像電 | 20250630 | 20250707 | 4.8414 | 8.3472 | -1.8364 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250630_2368_20250707_neutral_4.8414.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3714 | 富采 | 20251231 | 20260106 | 4.6025 | 8.7866 | -4.4630 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20251231_3714_20260106_neutral_4.6025.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3596 | 智易 | 20260226 | 20260306 | 4.5113 | 7.2682 | -4.2607 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20260226_3596_20260306_neutral_4.5113.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 2316 | 楠梓電 | 20250723 | 20250730 | 2.6247 | 9.3176 | -3.8058 | wide_base_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250723_2316_20250730_neutral_2.6247.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 2368 | 金像電 | 20250522 | 20250602 | 10.1365 | 13.0604 | -1.1696 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20250522_2368_20250602_win_10.1365.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 3704 | 合勤控 | 20250826 | 20250829 | 10.1493 | 11.6418 | -13.4328 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20250826_3704_20250829_win_10.1493.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 8422 | 可寧衛* | 20260107 | 20260112 | 10.1517 | 10.1517 | -0.1167 | bottom_return_review;lowest_position_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260107_8422_20260112_win_10.1517.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6147 | 頎邦 | 20260312 | 20260318 | 11.4613 | 11.4613 | -13.6103 | lowest_position_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260312_6147_20260318_win_11.4613.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 4908 | 前鼎 | 20260302 | 20260312 | 12.0507 | 12.0507 | -0.6342 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260302_4908_20260312_win_12.0507.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6175 | 立敦 | 20260415 | 20260420 | 12.1396 | 15.1745 | -8.9530 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260415_6175_20260420_win_12.1396.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 4157 | 太景*-KY | 20251203 | 20251208 | 20.3463 | 20.3463 | -6.4935 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20251203_4157_20251208_win_20.3463.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6016 | 康和證 | 20260424 | 20260505 | 19.6517 | 19.6517 | -1.2438 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260424_6016_20260505_win_19.6517.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6173 | 信昌電 | 20260415 | 20260420 | 18.7166 | 18.7166 | -21.1765 | top_return_review;drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260415_6173_20260420_win_18.7166.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 3163 | 波若威 | 20260128 | 20260205 | 10.7216 | 10.7216 | -8.1443 | wide_base_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260128_3163_20260205_win_10.7216.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 4973 | 廣穎 | 20260312 | 20260317 | 10.6568 | 10.6568 | 0.0000 | wide_base_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e04_tp10_close_5pct_neutral/01_win/20260312_4973_20260317_win_10.6568.png |
| tp10_intraday_or_fixed_20d_close | loss | 6290 | 良維 | 20260224 | 20260306 | -16.9528 | 5.5794 | -18.2403 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260224_6290_20260306_loss_-16.9528.png |
| tp10_intraday_or_fixed_20d_close | loss | 3013 | 晟銘電 | 20260417 | 20260423 | -15.2610 | 1.2048 | -16.4659 | bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260417_3013_20260423_loss_-15.2610.png |
| tp10_intraday_or_fixed_20d_close | loss | 2363 | 矽統 | 20260121 | 20260128 | -17.7419 | 2.4194 | -19.3548 | bottom_return_review;drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260121_2363_20260128_loss_-17.7419.png |
| tp10_intraday_or_fixed_20d_close | loss | 3230 | 錦明 | 20260211 | 20260303 | -11.2676 | 1.4085 | -18.3099 | drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260211_3230_20260303_loss_-11.2676.png |
| tp10_intraday_or_fixed_20d_close | loss | 6147 | 頎邦 | 20260107 | 20260114 | -4.9123 | 5.2632 | -6.8421 | lowest_position_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260107_6147_20260114_loss_-4.9123.png |
| tp10_intraday_or_fixed_20d_close | loss | 9921 | 巨大 | 20250224 | 20250306 | -6.9277 | 2.7108 | -9.3373 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250224_9921_20250306_loss_-6.9277.png |
| tp10_intraday_or_fixed_20d_close | loss | 2357 | 華碩 | 20260311 | 20260318 | -7.0234 | 1.0033 | -8.3612 | median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260311_2357_20260318_loss_-7.0234.png |
| tp10_intraday_or_fixed_20d_close | loss | 2867 | 三商壽 | 20250821 | 20250826 | -4.3046 | 9.6026 | -8.4437 | missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250821_2867_20250826_loss_-4.3046.png |
| tp10_intraday_or_fixed_20d_close | loss | 3714 | 富采 | 20251231 | 20260106 | -0.5579 | 8.7866 | -4.4630 | missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20251231_3714_20260106_loss_-0.5579.png |
| tp10_intraday_or_fixed_20d_close | loss | 3051 | 力特 | 20260116 | 20260121 | -14.5756 | 8.4871 | -18.4502 | missed_upside_review;drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260116_3051_20260121_loss_-14.5756.png |
| tp10_intraday_or_fixed_20d_close | loss | 1305 | 華夏 | 20250213 | 20250220 | 1.8657 | 4.4776 | -4.4776 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250213_1305_20250220_loss_1.8657.png |
| tp10_intraday_or_fixed_20d_close | loss | 4904 | 遠傳 | 20250930 | 20251003 | 5.0562 | 6.9663 | -0.3371 | top_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250930_4904_20251003_loss_5.0562.png |
| tp10_intraday_or_fixed_20d_close | loss | 3481 | 群創 | 20250821 | 20250829 | 2.8169 | 9.8592 | -7.3944 | top_return_review;missed_upside_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250821_3481_20250829_loss_2.8169.png |
| tp10_intraday_or_fixed_20d_close | win | 6173 | 信昌電 | 20260415 | 20260420 | 10.0000 | 18.7166 | -21.1765 | drawdown_risk_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260415_6173_20260420_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 8422 | 可寧衛* | 20260107 | 20260112 | 10.0000 | 10.1517 | -0.1167 | lowest_position_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260107_8422_20260112_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 6147 | 頎邦 | 20260312 | 20260318 | 10.0000 | 11.4613 | -13.6103 | lowest_position_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260312_6147_20260318_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 2368 | 金像電 | 20250522 | 20250602 | 10.0000 | 11.3060 | -1.1696 | top_return_review;bottom_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250522_2368_20250602_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 3163 | 波若威 | 20250106 | 20250109 | 10.0000 | 11.5385 | -2.2436 | top_return_review;bottom_return_review;median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250106_3163_20250109_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 3260 | 威剛 | 20250217 | 20250226 | 10.0000 | 11.2885 | -5.7013 | top_return_review;bottom_return_review;median_return_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250217_3260_20250226_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 2316 | 楠梓電 | 20250723 | 20250730 | 10.0000 | 11.8110 | -3.8058 | wide_base_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250723_2316_20250730_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 3163 | 波若威 | 20260128 | 20260205 | 10.0000 | 10.7216 | -8.1443 | wide_base_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260128_3163_20260205_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 4973 | 廣穎 | 20260312 | 20260317 | 10.0000 | 10.6568 | 0.0000 | wide_base_review | output/latest/research_backtest/structured_neckline_retest_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260312_4973_20260317_win_10.0000.png |

## Boundary Notes

- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.
- The shortlist is a subset of `structured_neckline_retest_review_latest.csv`; it does not regenerate signal logic.
- Manual review should compare whether the 10% take-profit rules win because the pattern is repeatable or because of a few non-repeatable spikes.
