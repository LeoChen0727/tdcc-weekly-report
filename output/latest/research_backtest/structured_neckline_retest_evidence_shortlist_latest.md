# Structured Neckline Retest Evidence Shortlist

- generated_at: `2026-06-28 23:05:14 Asia/Taipei`
- research_id: `structured_neckline_retest_evidence_shortlist`
- source_research_id: `structured_neckline_retest_review_shortlist`
- source_parameter_set_id: `structured_neckline_retest_review_shortlist_20260627`
- chart_root: `output\latest\research_backtest\structured_neckline_retest_evidence_shortlist`
- chart_count: `55`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this evidence packet does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Why This Exists

The previous shortlist charts only drew a horizontal neckline. This packet redraws the same rows with the 90-session reference window, left/right support lows, support average line, support touches, and the high anchor that produced the reconstructed horizontal neckline.

## Evidence Rule

- The structured-neckline proxy first finds two recent local support lows within 9% of each other.
- It then sets the horizontal neckline to the maximum high after the left support low and before the signal date.
- The signal date must close above that neckline after the volume-confirmed event has been detected upstream.
- `visual_pre_signal_context` uses the same chart span that the manual reviewer saw: from the evidence chart's left edge to the trading day before the signal date.

## Summary

| exit_rule_id | outcome_result | rows | unique_stocks | avg_support_gap_pct | avg_base_width_pct | avg_visual_pre_signal_return_pct | avg_base_age_sessions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 11 | 11 | 1.2682 | 17.7273 | 6.0774 | 38.7273 |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 11 | 11 | 3.0061 | 29.2617 | 2.7312 | 55.5455 |
| tp10_close_or_neutral_after_5pct_close_20d | win | 11 | 11 | 2.1615 | 35.3865 | 16.8296 | 48.0000 |
| tp10_intraday_or_fixed_20d_close | loss | 13 | 13 | 2.1385 | 13.4122 | -3.6847 | 42.4615 |
| tp10_intraday_or_fixed_20d_close | win | 9 | 8 | 2.1602 | 42.9896 | 18.2389 | 48.7778 |

## Visual Pre-Signal Context Summary

| outcome_result | visual_pre_signal_context | rows | unique_stocks |
| --- | --- | --- | --- |
| loss | bearish | 14 | 9 |
| loss | bullish | 3 | 2 |
| loss | mixed | 6 | 4 |
| loss | sideways_or_consolidation | 1 | 1 |
| neutral | bearish | 3 | 3 |
| neutral | bullish | 3 | 3 |
| neutral | mixed | 4 | 4 |
| neutral | sideways_or_consolidation | 1 | 1 |
| win | bearish | 5 | 3 |
| win | bullish | 9 | 6 |
| win | mixed | 6 | 5 |

## Review Index

| exit_rule_id | outcome_result | stock_id | stock_name | signal_date | reference_price | neckline_anchor_date | left_support_date | right_support_date | support_gap_pct | visible_context_start | visible_context_end | visual_pre_signal_context | base_age_sessions | evidence_chart_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 1305 | 華夏 | 20250213 | 12.7500 | 20250203 | 20250106 | 20250117 | 3.4934 | 20240916 | 20250212 | bearish | 21 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20250213_1305_20250220_loss_1.8657.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 1528 | 恩德 | 20250221 | 15.8500 | 20250218 | 20250113 | 20250203 | 0.3802 | 20240925 | 20250220 | mixed | 22 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20250221_1528_20250227_loss_0.0000.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3481 | 群創 | 20250821 | 12.8500 | 20250819 | 20250603 | 20250701 | 1.7021 | 20250402 | 20250820 | bearish | 57 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20250821_3481_20250829_loss_2.8169.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 6147 | 頎邦 | 20260107 | 54.9000 | 20260102 | 20251118 | 20251229 | 0.3883 | 20250114 | 20260106 | bearish | 34 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260107_6147_20260114_loss_-4.9123.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3051 | 力特 | 20260116 | 22.2000 | 20260108 | 20251124 | 20251210 | 0.0000 | 20250820 | 20260115 | mixed | 37 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260116_3051_20260121_loss_-14.5756.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3545 | 敦泰 | 20260119 | 55.3000 | 20260106 | 20251121 | 20251216 | 1.6410 | 20250821 | 20260116 | bearish | 39 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260119_3545_20260127_loss_-8.0702.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 2363 | 矽統 | 20260121 | 53.0000 | 20260120 | 20251121 | 20260105 | 0.0000 | 20250825 | 20260120 | mixed | 41 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260121_2363_20260128_loss_-17.7419.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3230 | 錦明 | 20260211 | 40.5000 | 20260210 | 20260106 | 20260121 | 0.1464 | 20250227 | 20260210 | bearish | 26 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260211_3230_20260303_loss_-11.2676.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 6290 | 良維 | 20260224 | 202.0000 | 20260223 | 20251118 | 20251205 | 2.9412 | 20250304 | 20260223 | bullish | 61 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260224_6290_20260306_loss_-16.9528.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 3013 | 晟銘電 | 20260417 | 111.0000 | 20260330 | 20260310 | 20260327 | 2.9050 | 20251119 | 20260416 | bearish | 26 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260417_3013_20260423_loss_-15.2610.png |
| tp10_close_or_neutral_after_5pct_close_20d | loss | 6488 | 環球晶 | 20260421 | 555.0000 | 20260420 | 20260109 | 20260309 | 0.3529 | 20251121 | 20260420 | bullish | 62 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/03_loss/20260421_6488_20260428_loss_-7.9602.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3163 | 波若威 | 20250106 | 153.0000 | 20250103 | 20241118 | 20241218 | 3.6145 | 20240816 | 20250103 | mixed | 34 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250106_3163_20250109_neutral_-2.2436.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 2455 | 全新 | 20250611 | 112.5000 | 20250513 | 20250409 | 20250422 | 3.3215 | 20250109 | 20250610 | bearish | 41 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250611_2455_20250625_neutral_2.7559.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 2368 | 金像電 | 20250630 | 290.0000 | 20250611 | 20250311 | 20250520 | 7.0732 | 20250206 | 20250627 | bullish | 73 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250630_2368_20250707_neutral_4.8414.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3037 | 欣興 | 20250703 | 116.5000 | 20250624 | 20250331 | 20250609 | 6.6304 | 20250211 | 20250702 | mixed | 62 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250703_3037_20250710_neutral_3.6290.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 1727 | 中華化 | 20250723 | 27.9500 | 20250528 | 20250422 | 20250623 | 0.9524 | 20250304 | 20250722 | bearish | 63 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250723_1727_20250728_neutral_3.2258.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 2316 | 楠梓電 | 20250723 | 69.5000 | 20250722 | 20250520 | 20250603 | 0.0000 | 20250304 | 20250722 | bullish | 44 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250723_2316_20250730_neutral_2.6247.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 6706 | 惠特 | 20250918 | 76.9000 | 20250917 | 20250623 | 20250813 | 2.0270 | 20250429 | 20250917 | sideways_or_consolidation | 59 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20250918_6706_20250930_neutral_2.8605.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3714 | 富采 | 20251231 | 34.8500 | 20251212 | 20251105 | 20251208 | 2.5915 | 20250805 | 20251230 | mixed | 39 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20251231_3714_20260106_neutral_4.6025.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 3596 | 智易 | 20260226 | 195.0000 | 20251203 | 20251118 | 20251219 | 0.2809 | 20250925 | 20260225 | bearish | 63 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20260226_3596_20260306_neutral_4.5113.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 6197 | 佳必琪 | 20260311 | 162.5000 | 20260105 | 20251224 | 20260304 | 4.0590 | 20251009 | 20260310 | mixed | 45 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20260311_6197_20260316_neutral_0.8403.png |
| tp10_close_or_neutral_after_5pct_close_20d | neutral | 8358 | 金居 | 20260415 | 318.5000 | 20260225 | 20251126 | 20260330 | 2.5172 | 20251117 | 20260414 | bullish | 88 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/02_neutral/20260415_8358_20260420_neutral_-0.8043.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 2368 | 金像電 | 20250522 | 244.0000 | 20250219 | 20250212 | 20250319 | 1.1442 | 20241220 | 20250520 | mixed | 65 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20250522_2368_20250602_win_10.1365.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 3704 | 合勤控 | 20250826 | 28.9000 | 20250804 | 20250623 | 20250716 | 0.9615 | 20250409 | 20250825 | mixed | 46 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20250826_3704_20250829_win_10.1493.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 4157 | 太景*-KY | 20251203 | 10.8500 | 20251202 | 20250407 | 20251119 | 0.0000 | 20241211 | 20251202 | bearish | 23 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20251203_4157_20251208_win_20.3463.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 8422 | 可寧衛* | 20260107 | 34.5000 | 20260102 | 20251119 | 20251209 | 6.3107 | 20250731 | 20260106 | bearish | 33 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260107_8422_20260112_win_10.1517.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 3163 | 波若威 | 20260128 | 428.5000 | 20260105 | 20251105 | 20251121 | 1.4019 | 20250213 | 20260127 | bullish | 58 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260128_3163_20260205_win_10.7216.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 4908 | 前鼎 | 20260302 | 89.7000 | 20260226 | 20251218 | 20260113 | 5.1316 | 20250307 | 20260226 | mixed | 42 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260302_4908_20260312_win_12.0507.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 4973 | 廣穎 | 20260312 | 58.8000 | 20260121 | 20251105 | 20251215 | 1.6153 | 20250319 | 20260311 | bullish | 81 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260312_4973_20260317_win_10.6568.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6147 | 頎邦 | 20260312 | 60.0000 | 20260120 | 20251219 | 20260206 | 0.3831 | 20250319 | 20260311 | bearish | 49 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260312_6147_20260318_win_11.4613.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6173 | 信昌電 | 20260415 | 74.9000 | 20260225 | 20260206 | 20260324 | 1.3356 | 20251117 | 20260414 | bullish | 38 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260415_6173_20260420_win_18.7166.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6175 | 立敦 | 20260415 | 59.6000 | 20260414 | 20260203 | 20260327 | 2.0000 | 20251117 | 20260414 | bullish | 41 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260415_6175_20260420_win_12.1396.png |
| tp10_close_or_neutral_after_5pct_close_20d | win | 6016 | 康和證 | 20260424 | 18.2500 | 20260423 | 20260128 | 20260331 | 3.4921 | 20251126 | 20260423 | bullish | 52 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e04_tp10_close_5pct_neutral/01_win/20260424_6016_20260505_win_19.6517.png |
| tp10_intraday_or_fixed_20d_close | loss | 1305 | 華夏 | 20250213 | 12.7500 | 20250203 | 20250106 | 20250117 | 3.4934 | 20240916 | 20250212 | bearish | 21 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250213_1305_20250220_loss_1.8657.png |
| tp10_intraday_or_fixed_20d_close | loss | 9921 | 巨大 | 20250224 | 157.0000 | 20241126 | 20241120 | 20250204 | 5.4054 | 20240926 | 20250221 | bearish | 60 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250224_9921_20250306_loss_-6.9277.png |
| tp10_intraday_or_fixed_20d_close | loss | 2867 | 三商壽 | 20250821 | 5.5000 | 20250730 | 20250611 | 20250715 | 0.2004 | 20250402 | 20250820 | bearish | 51 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250821_2867_20250826_loss_-4.3046.png |
| tp10_intraday_or_fixed_20d_close | loss | 3481 | 群創 | 20250821 | 12.8500 | 20250819 | 20250603 | 20250701 | 1.7021 | 20250402 | 20250820 | bearish | 57 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250821_3481_20250829_loss_2.8169.png |
| tp10_intraday_or_fixed_20d_close | loss | 4904 | 遠傳 | 20250930 | 87.2000 | 20250926 | 20250709 | 20250801 | 0.6196 | 20250509 | 20250926 | sideways_or_consolidation | 54 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20250930_4904_20251003_loss_5.0562.png |
| tp10_intraday_or_fixed_20d_close | loss | 3714 | 富采 | 20251231 | 34.8500 | 20251212 | 20251105 | 20251208 | 2.5915 | 20250805 | 20251230 | mixed | 39 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20251231_3714_20260106_loss_-0.5579.png |
| tp10_intraday_or_fixed_20d_close | loss | 6147 | 頎邦 | 20260107 | 54.9000 | 20260102 | 20251118 | 20251229 | 0.3883 | 20250114 | 20260106 | bearish | 34 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260107_6147_20260114_loss_-4.9123.png |
| tp10_intraday_or_fixed_20d_close | loss | 3051 | 力特 | 20260116 | 22.2000 | 20260108 | 20251124 | 20251210 | 0.0000 | 20250820 | 20260115 | mixed | 37 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260116_3051_20260121_loss_-14.5756.png |
| tp10_intraday_or_fixed_20d_close | loss | 2363 | 矽統 | 20260121 | 53.0000 | 20260120 | 20251121 | 20260105 | 0.0000 | 20250825 | 20260120 | mixed | 41 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260121_2363_20260128_loss_-17.7419.png |
| tp10_intraday_or_fixed_20d_close | loss | 3230 | 錦明 | 20260211 | 40.5000 | 20260210 | 20260106 | 20260121 | 0.1464 | 20250227 | 20260210 | bearish | 26 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260211_3230_20260303_loss_-11.2676.png |
| tp10_intraday_or_fixed_20d_close | loss | 6290 | 良維 | 20260224 | 202.0000 | 20260223 | 20251118 | 20251205 | 2.9412 | 20250304 | 20260223 | bullish | 61 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260224_6290_20260306_loss_-16.9528.png |
| tp10_intraday_or_fixed_20d_close | loss | 2357 | 華碩 | 20260311 | 563.0000 | 20260102 | 20251224 | 20260121 | 7.4074 | 20251009 | 20260310 | bearish | 45 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260311_2357_20260318_loss_-7.0234.png |
| tp10_intraday_or_fixed_20d_close | loss | 3013 | 晟銘電 | 20260417 | 111.0000 | 20260330 | 20260310 | 20260327 | 2.9050 | 20251119 | 20260416 | bearish | 26 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/03_loss/20260417_3013_20260423_loss_-15.2610.png |
| tp10_intraday_or_fixed_20d_close | win | 3163 | 波若威 | 20250106 | 153.0000 | 20250103 | 20241118 | 20241218 | 3.6145 | 20240816 | 20250103 | mixed | 34 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250106_3163_20250109_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 3260 | 威剛 | 20250217 | 82.0000 | 20250214 | 20241216 | 20250203 | 3.6364 | 20240919 | 20250214 | mixed | 37 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250217_3260_20250226_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 2368 | 金像電 | 20250522 | 244.0000 | 20250219 | 20250212 | 20250319 | 1.1442 | 20241220 | 20250520 | mixed | 65 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250522_2368_20250602_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 2316 | 楠梓電 | 20250723 | 69.5000 | 20250722 | 20250520 | 20250603 | 0.0000 | 20250304 | 20250722 | bullish | 44 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20250723_2316_20250730_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 8422 | 可寧衛* | 20260107 | 34.5000 | 20260102 | 20251119 | 20251209 | 6.3107 | 20250731 | 20260106 | bearish | 33 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260107_8422_20260112_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 3163 | 波若威 | 20260128 | 428.5000 | 20260105 | 20251105 | 20251121 | 1.4019 | 20250213 | 20260127 | bullish | 58 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260128_3163_20260205_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 4973 | 廣穎 | 20260312 | 58.8000 | 20260121 | 20251105 | 20251215 | 1.6153 | 20250319 | 20260311 | bullish | 81 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260312_4973_20260317_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 6147 | 頎邦 | 20260312 | 60.0000 | 20260120 | 20251219 | 20260206 | 0.3831 | 20250319 | 20260311 | bearish | 49 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260312_6147_20260318_win_10.0000.png |
| tp10_intraday_or_fixed_20d_close | win | 6173 | 信昌電 | 20260415 | 74.9000 | 20260225 | 20260206 | 20260324 | 1.3356 | 20251117 | 20260414 | bullish | 38 | output/latest/research_backtest/structured_neckline_retest_evidence_shortlist/e03_tp10_intraday_or_fixed_20d/01_win/20260415_6173_20260420_win_10.0000.png |

## Boundary Notes

- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.
- This is chart-evidence clarification only. It does not change the model event selection, exit rules, scoring, ranking, or production contract.
