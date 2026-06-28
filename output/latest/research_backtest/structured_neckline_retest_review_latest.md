# Structured Neckline Retest Review Packet

- generated_at: `2026-06-27 18:52:24 Asia/Taipei`
- research_id: `structured_neckline_retest_review_packet`
- source_research_id: `structured_neckline_retest_entry_exit_grid`
- source_parameter_set_id: `structured_neckline_retest_entry_exit_grid_20260627`
- segment_id: `low_position_le60_market_bull`
- stop_rule_id: `signal_low_stop`
- chart_root: `output\latest\research_backtest\structured_neckline_retest_review`
- chart_count: `380`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this packet does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Why This Packet Exists

This packet isolates the low-position plus bull-market structured-neckline retest entries using `signal_low_stop`. The goal is manual chart review of wins, neutrals, and losses, and a concentration check to see whether the apparent return improvement is driven by only a few outsized winners.

## Exit Rule Summary

| exit_rule_id | sample_size | unique_stock_count | max_rows_single_stock | max_single_stock_row_share_pct | win_count | neutral_count | loss_count | incomplete_count | pure_win_rate_pct | neutral_inclusive_success_rate_pct | positive_return_rate_pct | avg_return_pct | median_return_pct | max_return_pct | top5_positive_return_sum_share_pct | avg_return_ex_top5_positive_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fixed_10d_close | 95 | 89 | 2 | 2.1053 | 46 | 0 | 49 | 0 | 48.4211 | 48.4211 | 48.4211 | 3.2290 | 0.0000 | 66.5979 | 37.3528 | 0.7989 |
| fixed_20d_close | 95 | 89 | 2 | 2.1053 | 51 | 0 | 44 | 0 | 53.6842 | 53.6842 | 53.6842 | 9.9964 | 2.1858 | 115.5309 | 34.1812 | 5.5728 |
| tp10_close_or_neutral_after_5pct_close_20d | 95 | 89 | 2 | 2.1053 | 40 | 22 | 33 | 0 | 54.7945 | 65.2632 | 65.2632 | 3.3070 | 3.3067 | 20.3463 | 16.3995 | 2.4333 |
| tp10_intraday_or_fixed_20d_close | 95 | 89 | 2 | 2.1053 | 58 | 0 | 37 | 0 | 61.0526 | 61.0526 | 64.2105 | 3.2765 | 10.0000 | 10.0000 | 8.4783 | 2.9029 |

## Review Index

| exit_rule_id | outcome_result | stock_id | stock_name | signal_date | retest_entry_date | exit_date | return_pct | mfe_pct | mae_pct | chart_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fixed_10d_close | loss | 1528 | 恩德 | 20250221 | 20250227 | 20250227 | 0.0000 | 7.0946 | -1.3514 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250221_1528_20250227_loss_0.0000.png |
| fixed_10d_close | loss | 6213 | 聯茂 | 20250522 | 20250527 | 20250610 | 0.0000 | 2.5471 | -7.8627 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250522_6213_20250527_loss_0.0000.png |
| fixed_10d_close | loss | 6451 | 訊芯-KY | 20250807 | 20250812 | 20250825 | 0.0000 | 5.0595 | -8.0357 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250807_6451_20250812_loss_0.0000.png |
| fixed_10d_close | loss | 2637 | 慧洋-KY | 20250214 | 20250225 | 20250311 | -0.2401 | 5.5222 | -10.5642 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250214_2637_20250225_loss_-0.2401.png |
| fixed_10d_close | loss | 1305 | 華夏 | 20250213 | 20250220 | 20250306 | -0.3731 | 2.6119 | -4.4776 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250213_1305_20250220_loss_-0.3731.png |
| fixed_10d_close | loss | 6147 | 頎邦 | 20260312 | 20260318 | 20260331 | -0.4298 | 12.7507 | -13.6103 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260312_6147_20260318_loss_-0.4298.png |
| fixed_10d_close | loss | 1326 | 台化 | 20250723 | 20250729 | 20250811 | -1.0601 | 4.5936 | -9.1873 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250723_1326_20250729_loss_-1.0601.png |
| fixed_10d_close | loss | 3596 | 智易 | 20260226 | 20260306 | 20260319 | -1.2531 | 7.2682 | -4.2607 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260226_3596_20260306_loss_-1.2531.png |
| fixed_10d_close | loss | 3714 | 富采 | 20251231 | 20260106 | 20260119 | -1.5342 | 6.2762 | -4.4630 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20251231_3714_20260106_loss_-1.5342.png |
| fixed_10d_close | loss | 8289 | 泰藝 | 20260224 | 20260302 | 20260313 | -1.5670 | 21.3675 | -10.2564 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260224_8289_20260302_loss_-1.5670.png |
| fixed_10d_close | loss | 4534 | 慶騰 | 20260123 | 20260224 | 20260310 | -1.7143 | 23.0476 | -2.8571 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260123_4534_20260224_loss_-1.7143.png |
| fixed_10d_close | loss | 2634 | 漢翔 | 20250806 | 20250811 | 20250822 | -1.7276 | 2.4390 | -7.2154 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250806_2634_20250811_loss_-1.7276.png |
| fixed_10d_close | loss | 2376 | 技嘉 | 20260410 | 20260416 | 20260429 | -2.6786 | 4.2857 | -3.2143 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260410_2376_20260416_loss_-2.6786.png |
| fixed_10d_close | loss | 3481 | 群創 | 20250821 | 20250829 | 20250917 | -2.8169 | 1.4085 | -7.3944 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250821_3481_20250829_loss_-2.8169.png |
| fixed_10d_close | loss | 3013 | 晟銘電 | 20250616 | 20250619 | 20250702 | -2.9304 | 4.0293 | -10.2564 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250616_3013_20250619_loss_-2.9304.png |
| fixed_10d_close | loss | 2327 | 國巨* | 20251021 | 20251027 | 20251107 | -3.6961 | 7.5975 | -8.0082 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20251021_2327_20251027_loss_-3.6961.png |
| fixed_10d_close | loss | 6173 | 信昌電 | 20260415 | 20260420 | 20260504 | -3.7433 | 1.6043 | -21.1765 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260415_6173_20260420_loss_-3.7433.png |
| fixed_10d_close | loss | 6197 | 佳必琪 | 20260311 | 20260316 | 20260327 | -3.9216 | 12.6050 | -8.4034 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260311_6197_20260316_loss_-3.9216.png |
| fixed_10d_close | loss | 3645 | 達邁 | 20260115 | 20260120 | 20260202 | -3.9936 | 20.2875 | -5.2716 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260115_3645_20260120_loss_-3.9936.png |
| fixed_10d_close | loss | 6175 | 立敦 | 20260415 | 20260420 | 20260504 | -4.2489 | 1.6692 | -8.9530 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260415_6175_20260420_loss_-4.2489.png |
| fixed_10d_close | loss | 4526 | 東台 | 20260116 | 20260121 | 20260129 | -4.3302 | 3.3829 | -4.7361 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260116_4526_20260121_loss_-4.3302.png |
| fixed_10d_close | loss | 5522 | 遠雄 | 20250604 | 20250609 | 20250620 | -4.4540 | 8.3333 | -5.4598 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250604_5522_20250609_loss_-4.4540.png |
| fixed_10d_close | loss | 1313 | 聯成 | 20250716 | 20250724 | 20250806 | -4.8780 | 5.3659 | -8.2927 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250716_1313_20250724_loss_-4.8780.png |
| fixed_10d_close | loss | 2520 | 冠德 | 20251219 | 20251229 | 20251231 | -5.0633 | 0.0000 | -5.0633 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20251219_2520_20251229_loss_-5.0633.png |
| fixed_10d_close | loss | 8422 | 可寧衛* | 20260107 | 20260112 | 20260123 | -5.7176 | 21.1202 | -10.6184 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260107_8422_20260112_loss_-5.7176.png |
| fixed_10d_close | loss | 2409 | 友達 | 20250917 | 20250926 | 20251014 | -6.0498 | 2.4911 | -6.0498 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250917_2409_20250926_loss_-6.0498.png |
| fixed_10d_close | loss | 2374 | 佳能 | 20250610 | 20250613 | 20250620 | -6.4748 | 0.7194 | -7.1942 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250610_2374_20250613_loss_-6.4748.png |
| fixed_10d_close | loss | 9921 | 巨大 | 20250224 | 20250306 | 20250314 | -6.9277 | 2.7108 | -9.3373 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250224_9921_20250306_loss_-6.9277.png |
| fixed_10d_close | loss | 9105 | 泰金寶-DR | 20260114 | 20260120 | 20260123 | -6.9277 | 0.0000 | -7.8313 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260114_9105_20260120_loss_-6.9277.png |
| fixed_10d_close | loss | 2357 | 華碩 | 20260311 | 20260318 | 20260331 | -7.0234 | 1.0033 | -8.3612 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260311_2357_20260318_loss_-7.0234.png |
| fixed_10d_close | loss | 3051 | 力特 | 20260116 | 20260121 | 20260203 | -7.9336 | 8.4871 | -11.2546 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260116_3051_20260121_loss_-7.9336.png |
| fixed_10d_close | loss | 6488 | 環球晶 | 20260421 | 20260428 | 20260429 | -7.9602 | 0.1658 | -11.4428 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260421_6488_20260428_loss_-7.9602.png |
| fixed_10d_close | loss | 3545 | 敦泰 | 20260119 | 20260127 | 20260202 | -8.0702 | 0.5263 | -8.2456 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260119_3545_20260127_loss_-8.0702.png |
| fixed_10d_close | loss | 2014 | 中鴻 | 20250723 | 20250728 | 20250804 | -8.0745 | 0.6211 | -9.0062 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250723_2014_20250728_loss_-8.0745.png |
| fixed_10d_close | loss | 3019 | 亞光 | 20260126 | 20260129 | 20260130 | -8.7879 | 4.2424 | -10.9091 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260126_3019_20260129_loss_-8.7879.png |
| fixed_10d_close | loss | 1304 | 台聚 | 20250723 | 20250731 | 20250804 | -9.2920 | 0.0000 | -11.7699 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250723_1304_20250731_loss_-9.2920.png |
| fixed_10d_close | loss | 6706 | 惠特 | 20250918 | 20250930 | 20251009 | -9.8927 | 15.4946 | -12.8725 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250918_6706_20250930_loss_-9.8927.png |
| fixed_10d_close | loss | 2324 | 仁寶 | 20250917 | 20250925 | 20251013 | -10.6383 | 7.2340 | -13.1915 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250917_2324_20250925_loss_-10.6383.png |
| fixed_10d_close | loss | 2327 | 國巨* | 20260113 | 20260120 | 20260202 | -10.7266 | 5.3633 | -11.5917 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260113_2327_20260120_loss_-10.7266.png |
| fixed_10d_close | loss | 2344 | 華邦電 | 20250618 | 20250627 | 20250707 | -11.0849 | 2.3585 | -11.0849 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250618_2344_20250627_loss_-11.0849.png |
| fixed_10d_close | loss | 1810 | 和成 | 20260109 | 20260120 | 20260130 | -11.6945 | 2.3866 | -12.4105 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260109_1810_20260120_loss_-11.6945.png |
| fixed_10d_close | loss | 4533 | 協易機 | 20260121 | 20260127 | 20260209 | -11.9891 | 14.0327 | -12.2616 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260121_4533_20260127_loss_-11.9891.png |
| fixed_10d_close | loss | 3230 | 錦明 | 20260211 | 20260303 | 20260316 | -12.2427 | 1.4085 | -18.3099 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260211_3230_20260303_loss_-12.2427.png |
| fixed_10d_close | loss | 6139 | 亞翔 | 20250620 | 20250625 | 20250708 | -12.2807 | 2.6316 | -14.3275 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250620_6139_20250625_loss_-12.2807.png |
| fixed_10d_close | loss | 3047 | 訊舟 | 20250827 | 20250904 | 20250923 | -15.0327 | 2.1786 | -15.4684 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20250827_3047_20250904_loss_-15.0327.png |
| fixed_10d_close | loss | 3013 | 晟銘電 | 20260417 | 20260423 | 20260430 | -15.2610 | 1.2048 | -16.4659 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260417_3013_20260423_loss_-15.2610.png |
| fixed_10d_close | loss | 4973 | 廣穎 | 20260312 | 20260317 | 20260330 | -16.6047 | 21.6853 | -28.5006 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260312_4973_20260317_loss_-16.6047.png |
| fixed_10d_close | loss | 2363 | 矽統 | 20260121 | 20260128 | 20260202 | -17.7419 | 2.4194 | -19.3548 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260121_2363_20260128_loss_-17.7419.png |
| fixed_10d_close | loss | 8096 | 擎亞 | 20260128 | 20260224 | 20260309 | -20.9104 | 10.2418 | -20.9104 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/03_loss/20260128_8096_20260224_loss_-20.9104.png |
| fixed_10d_close | win | 3163 | 波若威 | 20260128 | 20260205 | 20260302 | 66.5979 | 77.1134 | -8.1443 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260128_3163_20260205_win_66.5979.png |
| fixed_10d_close | win | 6234 | 高僑 | 20260414 | 20260422 | 20260506 | 62.9213 | 77.8090 | -1.6854 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260414_6234_20260422_win_62.9213.png |
| fixed_10d_close | win | 6217 | 中探針 | 20260119 | 20260204 | 20260226 | 48.4945 | 48.4945 | -12.9952 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260119_6217_20260204_win_48.4945.png |
| fixed_10d_close | win | 8033 | 雷虎 | 20250723 | 20250728 | 20250808 | 29.4872 | 43.5897 | -5.1282 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250723_8033_20250728_win_29.4872.png |
| fixed_10d_close | win | 1528 | 恩德 | 20250731 | 20250805 | 20250818 | 27.3529 | 27.3529 | -3.5294 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250731_1528_20250805_win_27.3529.png |
| fixed_10d_close | win | 3535 | 晶彩科 | 20250609 | 20250618 | 20250701 | 26.4671 | 36.2874 | -6.3473 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250609_3535_20250618_win_26.4671.png |
| fixed_10d_close | win | 1802 | 台玻 | 20250715 | 20250724 | 20250806 | 23.2190 | 34.5646 | -0.2639 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250715_1802_20250724_win_23.2190.png |
| fixed_10d_close | win | 6207 | 雷科 | 20260430 | 20260506 | 20260519 | 22.8404 | 36.6032 | -8.1991 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260430_6207_20260506_win_22.8404.png |
| fixed_10d_close | win | 4908 | 前鼎 | 20260302 | 20260312 | 20260325 | 20.5074 | 30.0211 | -0.6342 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260302_4908_20260312_win_20.5074.png |
| fixed_10d_close | win | 8046 | 南電 | 20250703 | 20250710 | 20250723 | 20.3509 | 25.6140 | -2.8070 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250703_8046_20250710_win_20.3509.png |
| fixed_10d_close | win | 1447 | 力鵬 | 20260518 | 20260521 | 20260603 | 18.3362 | 18.3362 | -8.9983 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260518_1447_20260521_win_18.3362.png |
| fixed_10d_close | win | 6209 | 今國光 | 20250805 | 20250811 | 20250822 | 16.6102 | 21.8644 | -1.0169 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250805_6209_20250811_win_16.6102.png |
| fixed_10d_close | win | 2328 | 廣宇 | 20250815 | 20250820 | 20250902 | 14.9688 | 32.4324 | -1.2474 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250815_2328_20250820_win_14.9688.png |
| fixed_10d_close | win | 3317 | 尼克森 | 20260505 | 20260508 | 20260521 | 14.3505 | 21.4502 | -6.3444 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260505_3317_20260508_win_14.3505.png |
| fixed_10d_close | win | 2317 | 鴻海 | 20250724 | 20250801 | 20250814 | 14.0000 | 14.2857 | 0.0000 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250724_2317_20250801_win_14.0000.png |
| fixed_10d_close | win | 8163 | 達方 | 20260508 | 20260515 | 20260528 | 13.6012 | 19.0108 | -1.7002 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260508_8163_20260515_win_13.6012.png |
| fixed_10d_close | win | 8383 | 千附 | 20260413 | 20260416 | 20260429 | 13.3455 | 40.7678 | 0.0000 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260413_8383_20260416_win_13.3455.png |
| fixed_10d_close | win | 9933 | 中鼎 | 20250721 | 20250725 | 20250807 | 12.6984 | 15.3439 | -1.9400 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250721_9933_20250725_win_12.6984.png |
| fixed_10d_close | win | 6291 | 沛亨 | 20260128 | 20260210 | 20260305 | 12.6556 | 29.4606 | -1.6598 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260128_6291_20260210_win_12.6556.png |
| fixed_10d_close | win | 2368 | 金像電 | 20250630 | 20250707 | 20250718 | 10.1836 | 10.1836 | -1.8364 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250630_2368_20250707_win_10.1836.png |
| fixed_10d_close | win | 3704 | 合勤控 | 20250826 | 20250829 | 20250917 | 10.1493 | 21.1940 | -13.4328 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250826_3704_20250829_win_10.1493.png |
| fixed_10d_close | win | 2308 | 台達電 | 20250703 | 20250711 | 20250724 | 9.9788 | 13.1635 | 0.0000 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250703_2308_20250711_win_9.9788.png |
| fixed_10d_close | win | 2316 | 楠梓電 | 20250723 | 20250730 | 20250812 | 9.7113 | 11.8110 | -3.8058 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250723_2316_20250730_win_9.7113.png |
| fixed_10d_close | win | 3163 | 波若威 | 20250106 | 20250109 | 20250122 | 8.6538 | 11.5385 | -2.2436 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250106_3163_20250109_win_8.6538.png |
| fixed_10d_close | win | 6016 | 康和證 | 20260424 | 20260505 | 20260518 | 8.4577 | 27.8607 | -1.2438 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260424_6016_20260505_win_8.4577.png |
| fixed_10d_close | win | 2368 | 金像電 | 20250522 | 20250602 | 20250613 | 8.3821 | 13.0604 | -1.1696 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250522_2368_20250602_win_8.3821.png |
| fixed_10d_close | win | 8358 | 金居 | 20260415 | 20260420 | 20260504 | 7.9088 | 11.5282 | -13.0027 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260415_8358_20260420_win_7.9088.png |
| fixed_10d_close | win | 4157 | 太景*-KY | 20251203 | 20251208 | 20251219 | 7.3593 | 31.6017 | -6.4935 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20251203_4157_20251208_win_7.3593.png |
| fixed_10d_close | win | 3661 | 世芯-KY | 20250627 | 20250702 | 20250715 | 7.3248 | 10.6688 | -0.9554 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250627_3661_20250702_win_7.3248.png |
| fixed_10d_close | win | 4540 | 全球傳動 | 20260115 | 20260120 | 20260202 | 6.7757 | 25.7009 | -1.8692 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260115_4540_20260120_win_6.7757.png |
| fixed_10d_close | win | 3037 | 欣興 | 20250703 | 20250710 | 20250723 | 6.0484 | 14.1129 | -3.6290 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250703_3037_20250710_win_6.0484.png |
| fixed_10d_close | win | 4904 | 遠傳 | 20250930 | 20251003 | 20251022 | 5.8427 | 5.9551 | -0.3371 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250930_4904_20251003_win_5.8427.png |
| fixed_10d_close | win | 3260 | 威剛 | 20250217 | 20250226 | 20250312 | 5.4732 | 7.7537 | -5.7013 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250217_3260_20250226_win_5.4732.png |
| fixed_10d_close | win | 2404 | 漢唐 | 20250620 | 20250625 | 20250708 | 4.7473 | 5.9724 | -6.5850 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250620_2404_20250625_win_4.7473.png |
| fixed_10d_close | win | 3017 | 奇鋐 | 20250604 | 20250611 | 20250624 | 4.6875 | 10.0852 | -0.2841 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250604_3017_20250611_win_4.6875.png |
| fixed_10d_close | win | 6153 | 嘉聯益 | 20250626 | 20250710 | 20250723 | 4.4776 | 10.8209 | -3.7313 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250626_6153_20250710_win_4.4776.png |
| fixed_10d_close | win | 2355 | 敬鵬 | 20260112 | 20260116 | 20260129 | 4.3296 | 15.9218 | -4.1899 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260112_2355_20260116_win_4.3296.png |
| fixed_10d_close | win | 2405 | 輔信 | 20250805 | 20250811 | 20250822 | 4.0984 | 9.2896 | -2.4590 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250805_2405_20250811_win_4.0984.png |
| fixed_10d_close | win | 6290 | 良維 | 20260224 | 20260306 | 20260319 | 3.4335 | 4.2918 | -13.9485 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260224_6290_20260306_win_3.4335.png |
| fixed_10d_close | win | 4707 | 磐亞 | 20260410 | 20260416 | 20260429 | 3.4247 | 16.4384 | -4.1096 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260410_4707_20260416_win_3.4247.png |
| fixed_10d_close | win | 1727 | 中華化 | 20250723 | 20250728 | 20250808 | 2.7419 | 15.8065 | -0.6452 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250723_1727_20250728_win_2.7419.png |
| fixed_10d_close | win | 2867 | 三商壽 | 20250821 | 20250826 | 20250909 | 2.1523 | 9.6026 | -8.4437 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250821_2867_20250826_win_2.1523.png |
| fixed_10d_close | win | 6147 | 頎邦 | 20260107 | 20260114 | 20260127 | 1.9298 | 5.2632 | -1.9298 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20260107_6147_20260114_win_1.9298.png |
| fixed_10d_close | win | 2301 | 光寶科 | 20250703 | 20250710 | 20250723 | 0.8621 | 2.1552 | -1.7241 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250703_2301_20250710_win_0.8621.png |
| fixed_10d_close | win | 3044 | 健鼎 | 20250618 | 20250624 | 20250707 | 0.4115 | 3.9095 | -1.8519 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250618_3044_20250624_win_0.4115.png |
| fixed_10d_close | win | 2455 | 全新 | 20250611 | 20250625 | 20250708 | 0.3937 | 5.1181 | -3.5433 | output/latest/research_backtest/structured_neckline_retest_review/e01_fixed_10d_close/01_win/20250611_2455_20250625_win_0.3937.png |
| fixed_20d_close | loss | 1528 | 恩德 | 20250221 | 20250227 | 20250227 | 0.0000 | 7.0946 | -1.3514 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250221_1528_20250227_loss_0.0000.png |
| fixed_20d_close | loss | 4534 | 慶騰 | 20260123 | 20260224 | 20260324 | 0.0000 | 23.0476 | -5.7143 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260123_4534_20260224_loss_0.0000.png |
| fixed_20d_close | loss | 8383 | 千附 | 20260413 | 20260416 | 20260514 | -0.1828 | 40.7678 | -1.0969 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260413_8383_20260416_loss_-0.1828.png |
| fixed_20d_close | loss | 3714 | 富采 | 20251231 | 20260106 | 20260202 | -0.5579 | 8.7866 | -4.4630 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20251231_3714_20260106_loss_-0.5579.png |
| fixed_20d_close | loss | 6139 | 亞翔 | 20250620 | 20250625 | 20250722 | -0.8772 | 2.6316 | -14.3275 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250620_6139_20250625_loss_-0.8772.png |
| fixed_20d_close | loss | 4533 | 協易機 | 20260121 | 20260127 | 20260305 | -2.8610 | 14.0327 | -16.8937 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260121_4533_20260127_loss_-2.8610.png |
| fixed_20d_close | loss | 6213 | 聯茂 | 20250522 | 20250527 | 20250624 | -2.8793 | 4.8726 | -8.6379 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250522_6213_20250527_loss_-2.8793.png |
| fixed_20d_close | loss | 4973 | 廣穎 | 20260312 | 20260317 | 20260415 | -3.2218 | 21.6853 | -28.5006 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260312_4973_20260317_loss_-3.2218.png |
| fixed_20d_close | loss | 2324 | 仁寶 | 20250917 | 20250925 | 20251030 | -3.9716 | 7.2340 | -13.1915 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250917_2324_20250925_loss_-3.9716.png |
| fixed_20d_close | loss | 3163 | 波若威 | 20250106 | 20250109 | 20250204 | -4.1667 | 11.5385 | -11.5385 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250106_3163_20250109_loss_-4.1667.png |
| fixed_20d_close | loss | 6451 | 訊芯-KY | 20250807 | 20250812 | 20250909 | -4.1667 | 5.0595 | -8.0357 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250807_6451_20250812_loss_-4.1667.png |
| fixed_20d_close | loss | 2867 | 三商壽 | 20250821 | 20250826 | 20250926 | -4.3046 | 9.6026 | -8.4437 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250821_2867_20250826_loss_-4.3046.png |
| fixed_20d_close | loss | 4526 | 東台 | 20260116 | 20260121 | 20260129 | -4.3302 | 3.3829 | -4.7361 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260116_4526_20260121_loss_-4.3302.png |
| fixed_20d_close | loss | 6147 | 頎邦 | 20260107 | 20260114 | 20260202 | -4.9123 | 5.2632 | -6.8421 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260107_6147_20260114_loss_-4.9123.png |
| fixed_20d_close | loss | 2520 | 冠德 | 20251219 | 20251229 | 20251231 | -5.0633 | 0.0000 | -5.0633 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20251219_2520_20251229_loss_-5.0633.png |
| fixed_20d_close | loss | 3596 | 智易 | 20260226 | 20260306 | 20260323 | -5.7644 | 7.2682 | -7.0175 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260226_3596_20260306_loss_-5.7644.png |
| fixed_20d_close | loss | 2327 | 國巨* | 20251021 | 20251027 | 20251121 | -5.9548 | 7.5975 | -8.4189 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20251021_2327_20251027_loss_-5.9548.png |
| fixed_20d_close | loss | 2374 | 佳能 | 20250610 | 20250613 | 20250620 | -6.4748 | 0.7194 | -7.1942 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250610_2374_20250613_loss_-6.4748.png |
| fixed_20d_close | loss | 9921 | 巨大 | 20250224 | 20250306 | 20250314 | -6.9277 | 2.7108 | -9.3373 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250224_9921_20250306_loss_-6.9277.png |
| fixed_20d_close | loss | 9105 | 泰金寶-DR | 20260114 | 20260120 | 20260123 | -6.9277 | 0.0000 | -7.8313 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260114_9105_20260120_loss_-6.9277.png |
| fixed_20d_close | loss | 2357 | 華碩 | 20260311 | 20260318 | 20260331 | -7.0234 | 1.0033 | -8.3612 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260311_2357_20260318_loss_-7.0234.png |
| fixed_20d_close | loss | 6488 | 環球晶 | 20260421 | 20260428 | 20260429 | -7.9602 | 0.1658 | -11.4428 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260421_6488_20260428_loss_-7.9602.png |
| fixed_20d_close | loss | 3545 | 敦泰 | 20260119 | 20260127 | 20260202 | -8.0702 | 0.5263 | -8.2456 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20260119_3545_20260127_loss_-8.0702.png |
| fixed_20d_close | loss | 2014 | 中鴻 | 20250723 | 20250728 | 20250804 | -8.0745 | 0.6211 | -9.0062 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250723_2014_20250728_loss_-8.0745.png |
| fixed_20d_close | loss | 3013 | 晟銘電 | 20250616 | 20250619 | 20250716 | -8.4249 | 4.0293 | -13.1868 | output/latest/research_backtest/structured_neckline_retest_review/e02_fixed_20d_close/03_loss/20250616_3013_20250619_loss_-8.4249.png |

## Reading Notes

- Review folders by `exit_rule_id` first, then compare win/neutral/loss charts side by side.
- `top5_positive_return_sum_share_pct` is an outlier concentration check, not a trading rule.
- `avg_return_ex_top5_positive_pct` removes the top five positive-return rows for that exit rule to show whether average return is still supported after excluding the biggest winners.
- This is research-only evidence and does not promote structured-neckline logic to production.
