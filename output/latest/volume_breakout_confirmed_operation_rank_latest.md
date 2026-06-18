# Volume Breakout Confirmed Operation Rank

- generated_at: `2026-06-18 11:38:53 Asia/Taipei`
- latest_price_date: `20260617`
- rank_rule: only confirmation rows with `confirmation_date == latest_price_date` appear here.
- entry_rule: confirmation after close, next trading day open.
- scope: research only; all rows keep `approved_for_daily=False`.

## Confirmed Rank

| operation_rank | stock_id | stock_name | trigger_id | tdcc_list_type | tdcc_rank | classification_id | attack_method | price_position_type | evidence_sample_size | evidence_win_rate | evidence_avg_return | evidence_median_return | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2501 | 國建 | pullback_5ma_confirmed | weekly_increase | 45 | long_base_low_position | general_breakout | low_position | 15 | 53.33 | 10.2779 | 4.878 | 10.069 |
| 2 | 1905 | 華紙 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | low_position | 148 | 42.57 | 11.022 | -2.311 | 4.3 |
| 3 | 2903 | 遠百 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 305 | 39.34 | 2.3486 | -1.6687 | -1.2416 |
| 4 | 7828 | 創新服務 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 305 | 39.34 | 2.3486 | -1.6687 | -1.2416 |
| 5 | 2547 | 日勝生 | pullback_5ma_confirmed | no_tdcc |  | standard_breakout | general_breakout | middle_position | 11 | 36.36 | 4.1928 | -2.3585 | -1.7673 |
| 6 | 2324 | 仁寶 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 519 | 39.69 | 1.8581 | -2.0067 | -2.1165 |
| 7 | 2357 | 華碩 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 519 | 39.69 | 1.8581 | -2.0067 | -2.1165 |
| 8 | 6153 | 嘉聯益 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 519 | 39.69 | 1.8581 | -2.0067 | -2.1165 |
| 9 | 2851 | 中再保 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 270 | 43.7 | 1.479 | -1.96 | -2.3308 |
| 10 | 6904 | 伯鑫 | next_day_break_signal_high_confirmed | no_tdcc |  | standard_breakout | general_breakout | middle_position | 270 | 43.7 | 1.479 | -1.96 | -2.3308 |
| 11 | 2442 | 新美齊 | pullback_5ma_confirmed | no_tdcc |  | long_base_low_position | general_breakout | low_position | 158 | 32.28 | 0.6173 | -1.8086 | -2.7499 |
| 12 | 2601 | 益航 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | low_position | 770 | 37.14 | 1.1634 | -2.0907 | -2.7635 |
| 13 | 4551 | 智伸科 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 2098 | 38.13 | 1.2612 | -3.2828 | -4.4783 |
| 14 | 4976 | 佳凌 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 2098 | 38.13 | 1.2612 | -3.2828 | -4.4783 |
| 15 | 5227 | 立凱-KY | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 2098 | 38.13 | 1.2612 | -3.2828 | -4.4783 |
| 16 | 6209 | 今國光 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 2098 | 38.13 | 1.2612 | -3.2828 | -4.4783 |
| 17 | 6668 | 中揚光 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 2098 | 38.13 | 1.2612 | -3.2828 | -4.4783 |
| 18 | 7610 | 聯友金屬-創 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 2098 | 38.13 | 1.2612 | -3.2828 | -4.4783 |

## Pending Queue

| queue_date | signal_date | signal_age_trading_days | stock_id | stock_name | pending_trigger_ids | classification_id | attack_method | price_position_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 20260602 | 8 | 1229 | 聯華 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260617 | 20260612 | 3 | 1307 | 三芳 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260529 | 10 | 1409 | 新纖 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 1444 | 力麗 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260611 | 4 | 1714 | 和桐 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 1714 | 和桐 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260615 | 2 | 1714 | 和桐 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 1718 | 中纖 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260617 | 20260602 | 8 | 1718 | 中纖 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 1904 | 正隆 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260602 | 8 | 2106 | 建大 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260617 | 20260611 | 4 | 2243 | 宏旭-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 2243 | 宏旭-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 2305 | 全友 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 2323 | 中環 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260617 | 20260602 | 8 | 2347 | 聯強 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260601 | 9 | 2352 | 佳世達 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260529 | 10 | 2362 | 藍天 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260601 | 9 | 2362 | 藍天 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260602 | 8 | 2362 | 藍天 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 2379 | 瑞昱 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260605 | 5 | 2461 | 光群雷 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 2483 | 百容 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260611 | 4 | 2483 | 百容 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260611 | 4 | 2484 | 希華 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260615 | 2 | 2484 | 希華 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 2491 | 吉祥全 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 2493 | 揚博 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 2493 | 揚博 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 2497 | 怡利電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 2537 | 聯上發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260605 | 5 | 2883 | 凱基金 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260616 | 1 | 2910 | 統領 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260601 | 9 | 3011 | 今皓 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260605 | 5 | 3018 | 隆銘綠能 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260616 | 1 | 3019 | 亞光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260612 | 3 | 3026 | 禾伸堂 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 3049 | 精金 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260617 | 20260601 | 9 | 3059 | 華晶科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260603 | 7 | 3147 | 大綜 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 3226 | 龍鋒 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | long_base_low_position | general_breakout | low_position |
| 20260617 | 20260605 | 5 | 3226 | 龍鋒 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | wide_range_breakout | general_breakout | middle_position |
| 20260617 | 20260611 | 4 | 3285 | 微端 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 3285 | 微端 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 3288 | 點晶 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 3288 | 點晶 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 3288 | 點晶 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 3346 | 麗清 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 3406 | 玉晶光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260611 | 4 | 4306 | 炎洲 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260612 | 3 | 5227 | 立凱-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 5227 | 立凱-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 5426 | 振發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 5426 | 振發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260603 | 7 | 5426 | 振發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260611 | 4 | 5468 | 凱鈺 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 5468 | 凱鈺 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 5468 | 凱鈺 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 5701 | 劍湖山 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 6155 | 鈞寶 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 6214 | 精誠 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 6613 | 朋億* | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 6645 | 金萬林-創 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260529 | 10 | 6654 | 天正國際 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 6916 | 華凌 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 7631 | 聚賢研發-創 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | wide_range_breakout | volume_attack | middle_position |
| 20260617 | 20260602 | 8 | 8070 | 長華* | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 8077 | 洛碁 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260601 | 9 | 8101 | 華冠 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260601 | 9 | 8105 | 凌巨 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 8105 | 凌巨 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 8454 | 富邦媒 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 8454 | 富邦媒 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 8472 | 夠麻吉 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260529 | 10 | 8473 | 山林水 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
