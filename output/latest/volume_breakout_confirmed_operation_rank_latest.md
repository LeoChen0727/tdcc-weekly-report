# Volume Breakout Confirmed Operation Rank

- generated_at: `2026-06-17 21:50:31 Asia/Taipei`
- latest_price_date: `20260617`
- rank_rule: only confirmation rows with `confirmation_date == latest_price_date` appear here.
- entry_rule: confirmation after close, next trading day open.
- scope: research only; all rows keep `approved_for_daily=False`.

## Confirmed Rank

| operation_rank | stock_id | stock_name | trigger_id | tdcc_list_type | tdcc_rank | classification_id | attack_method | price_position_type | evidence_sample_size | evidence_win_rate | evidence_avg_return | evidence_median_return | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2501 | 國建 | pullback_5ma_confirmed | weekly_increase | 45 | long_base_low_position | general_breakout | low_position | 16 | 56.25 | 11.1592 | 5.4914 | 11.4901 |
| 2 | 1905 | 華紙 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | low_position | 146 | 42.47 | 11.2298 | -2.311 | 4.4558 |
| 3 | 2903 | 遠百 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 367 | 38.15 | 2.1121 | -1.6807 | -1.437 |
| 4 | 7828 | 創新服務 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 367 | 38.15 | 2.1121 | -1.6807 | -1.437 |
| 5 | 6904 | 伯鑫 | next_day_continuation_confirmed | no_tdcc |  | standard_breakout | general_breakout | middle_position | 73 | 45.21 | 0.6675 | -0.7937 | -1.5755 |
| 6 | 2851 | 中再保 | next_day_continuation_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 224 | 43.75 | 1.4605 | -1.8185 | -2.1324 |
| 7 | 2324 | 仁寶 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 582 | 38.49 | 1.66 | -2.0858 | -2.3837 |
| 8 | 2357 | 華碩 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 582 | 38.49 | 1.66 | -2.0858 | -2.3837 |
| 9 | 6153 | 嘉聯益 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 582 | 38.49 | 1.66 | -2.0858 | -2.3837 |
| 10 | 2442 | 新美齊 | pullback_5ma_confirmed | no_tdcc |  | long_base_low_position | general_breakout | low_position | 186 | 32.8 | 0.6958 | -1.7457 | -2.5967 |
| 11 | 2547 | 日勝生 | pullback_5ma_confirmed | no_tdcc |  | standard_breakout | general_breakout | middle_position | 186 | 32.8 | 0.6958 | -1.7457 | -2.5967 |
| 12 | 2601 | 益航 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | low_position | 873 | 36.54 | 1.047 | -2.1097 | -2.8793 |
| 13 | 4551 | 智伸科 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1913 | 38.73 | 1.3955 | -3.3333 | -4.4533 |
| 14 | 4976 | 佳凌 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1913 | 38.73 | 1.3955 | -3.3333 | -4.4533 |
| 15 | 5227 | 立凱-KY | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1913 | 38.73 | 1.3955 | -3.3333 | -4.4533 |
| 16 | 6209 | 今國光 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1913 | 38.73 | 1.3955 | -3.3333 | -4.4533 |
| 17 | 6668 | 中揚光 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1913 | 38.73 | 1.3955 | -3.3333 | -4.4533 |
| 18 | 7610 | 聯友金屬-創 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1913 | 38.73 | 1.3955 | -3.3333 | -4.4533 |

## Pending Queue

| queue_date | signal_date | signal_age_trading_days | stock_id | stock_name | pending_trigger_ids | classification_id | attack_method | price_position_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 20260602 | 8 | 1229 | 聯華 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260617 | 20260612 | 3 | 1307 | 三芳 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260529 | 10 | 1409 | 新纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 1444 | 力麗 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260611 | 4 | 1714 | 和桐 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 1714 | 和桐 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260615 | 2 | 1714 | 和桐 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 1718 | 中纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260617 | 20260602 | 8 | 1718 | 中纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 1904 | 正隆 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260602 | 8 | 2106 | 建大 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260617 | 20260611 | 4 | 2243 | 宏旭-KY | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 2243 | 宏旭-KY | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 2305 | 全友 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 2323 | 中環 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260617 | 20260602 | 8 | 2347 | 聯強 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260601 | 9 | 2352 | 佳世達 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260529 | 10 | 2362 | 藍天 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260601 | 9 | 2362 | 藍天 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260602 | 8 | 2362 | 藍天 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 2379 | 瑞昱 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260605 | 5 | 2461 | 光群雷 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 2483 | 百容 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260611 | 4 | 2483 | 百容 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260611 | 4 | 2484 | 希華 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260615 | 2 | 2484 | 希華 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 2491 | 吉祥全 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 2493 | 揚博 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 2493 | 揚博 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 2497 | 怡利電 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 2537 | 聯上發 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260605 | 5 | 2883 | 凱基金 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260616 | 1 | 2910 | 統領 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260601 | 9 | 3011 | 今皓 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260605 | 5 | 3018 | 隆銘綠能 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260616 | 1 | 3019 | 亞光 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260612 | 3 | 3026 | 禾伸堂 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 3049 | 精金 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260617 | 20260601 | 9 | 3059 | 華晶科 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260603 | 7 | 3147 | 大綜 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 3226 | 龍鋒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | general_breakout | low_position |
| 20260617 | 20260605 | 5 | 3226 | 龍鋒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | wide_range_breakout | general_breakout | middle_position |
| 20260617 | 20260611 | 4 | 3285 | 微端 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 3285 | 微端 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 3288 | 點晶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 3288 | 點晶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 3288 | 點晶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 3346 | 麗清 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 3406 | 玉晶光 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260611 | 4 | 4306 | 炎洲 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260612 | 3 | 5227 | 立凱-KY | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 5227 | 立凱-KY | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 5426 | 振發 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 5426 | 振發 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260603 | 7 | 5426 | 振發 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260611 | 4 | 5468 | 凱鈺 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260612 | 3 | 5468 | 凱鈺 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 5468 | 凱鈺 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 5701 | 劍湖山 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 6155 | 鈞寶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260601 | 9 | 6214 | 精誠 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 6613 | 朋億* | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 6645 | 金萬林-創 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260617 | 20260529 | 10 | 6654 | 天正國際 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260605 | 5 | 6916 | 華凌 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260615 | 2 | 7631 | 聚賢研發-創 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | wide_range_breakout | volume_attack | middle_position |
| 20260617 | 20260602 | 8 | 8070 | 長華* | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 8077 | 洛碁 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260617 | 20260601 | 9 | 8101 | 華冠 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260601 | 9 | 8105 | 凌巨 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 8105 | 凌巨 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 8454 | 富邦媒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260602 | 8 | 8454 | 富邦媒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260617 | 20260529 | 10 | 8472 | 夠麻吉 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260617 | 20260529 | 10 | 8473 | 山林水 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
