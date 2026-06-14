# Volume Breakout Confirmed Operation Rank

- generated_at: `2026-06-14 22:58:07 Asia/Taipei`
- latest_price_date: `20260612`
- rank_rule: only confirmation rows with `confirmation_date == latest_price_date` appear here.
- entry_rule: confirmation after close, next trading day open.
- scope: research only; all rows keep `approved_for_daily=False`.

## Confirmed Rank

| operation_rank | stock_id | stock_name | trigger_id | tdcc_list_type | tdcc_rank | classification_id | attack_method | price_position_type | evidence_sample_size | evidence_win_rate | evidence_avg_return | evidence_median_return | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2243 | 宏旭-KY | next_day_continuation_confirmed | weekly_increase | 6 | limit_up_like_breakout | general_breakout | high_position | 12 | 66.67 | 21.6738 | 21.0916 | 31.8468 |
| 2 | 2484 | 希華 | next_day_continuation_confirmed | weekly_increase | 10 | high_position_breakout | volume_attack | high_position | 12 | 66.67 | 21.6738 | 21.0916 | 31.8468 |
| 3 | 2491 | 吉祥全 | pullback_5ma_confirmed | weekly_increase | 16 | locked_limit_up_breakout | locked_limit_up | high_position | 44 | 63.64 | 12.7533 | 5.6278 | 22.8198 |
| 4 | 2547 | 日勝生 | next_day_continuation_confirmed | no_tdcc |  | standard_breakout | general_breakout | middle_position | 555 | 43.6 | 2.6557 | -1.8838 | -1.3339 |
| 5 | 4306 | 炎洲 | next_day_continuation_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 555 | 43.6 | 2.6557 | -1.8838 | -1.3339 |
| 6 | 5701 | 劍湖山 | pullback_10ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 17 | 41.18 | 4.0384 | -2.4528 | -1.8365 |
| 7 | 2362 | 藍天 | pullback_10ma_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 461 | 40.78 | 2.3244 | -2.1148 | -1.9289 |
| 8 | 3011 | 今皓 | pullback_10ma_confirmed | no_tdcc |  | limit_up_like_breakout | volume_attack | middle_position | 690 | 38.7 | 1.8223 | -2.2259 | -2.4721 |
| 9 | 8101 | 華冠 | pullback_10ma_confirmed | no_tdcc |  | limit_up_like_breakout | volume_attack | middle_position | 690 | 38.7 | 1.8223 | -2.2259 | -2.4721 |
| 10 | 3285 | 微端 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 128 | 35.16 | 5.4684 | -4.3994 | -2.9978 |
| 11 | 5468 | 凱鈺 | next_day_continuation_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 128 | 35.16 | 5.4684 | -4.3994 | -2.9978 |
| 12 | 1714 | 和桐 | next_day_continuation_confirmed | no_tdcc |  | limit_up_like_breakout | volume_attack | high_position | 1704 | 39.26 | 1.753 | -3.2649 | -4.0826 |
| 13 | 2483 | 百容 | next_day_continuation_confirmed | no_tdcc |  | limit_up_like_breakout | volume_attack | high_position | 1704 | 39.26 | 1.753 | -3.2649 | -4.0826 |

## Pending Queue

| queue_date | signal_date | signal_age_trading_days | stock_id | stock_name | pending_trigger_ids | classification_id | attack_method | price_position_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260612 | 20260602 | 5 | 1229 | 聯華 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260612 | 20260528 | 8 | 1319 | 東陽 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260612 | 20260527 | 9 | 1409 | 新纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260528 | 8 | 1409 | 新纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260529 | 7 | 1409 | 新纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260612 | 20260611 | 1 | 1438 | 三地開發 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | low_position |
| 20260612 | 20260601 | 6 | 1444 | 力麗 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260527 | 9 | 1503 | 士電 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | standard_breakout | volume_attack | middle_position |
| 20260612 | 20260528 | 8 | 1521 | 大億 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260601 | 6 | 1718 | 中纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | low_position |
| 20260612 | 20260602 | 5 | 1718 | 中纖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260605 | 2 | 1904 | 正隆 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260602 | 5 | 2105 | 正新 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260602 | 5 | 2106 | 建大 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260612 | 20260528 | 8 | 2239 | 英利-KY | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | low_position |
| 20260612 | 20260602 | 5 | 2323 | 中環 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | low_position |
| 20260612 | 20260529 | 7 | 2324 | 仁寶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260602 | 5 | 2347 | 聯強 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260601 | 6 | 2352 | 佳世達 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260529 | 7 | 2357 | 華碩 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | high_position |
| 20260612 | 20260602 | 5 | 2379 | 瑞昱 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260605 | 2 | 2442 | 新美齊 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | general_breakout | low_position |
| 20260612 | 20260605 | 2 | 2461 | 光群雷 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260605 | 2 | 2483 | 百容 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260601 | 6 | 2497 | 怡利電 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260605 | 2 | 2501 | 國建 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | general_breakout | low_position |
| 20260612 | 20260611 | 1 | 2537 | 聯上發 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260601 | 6 | 2601 | 益航 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | low_position |
| 20260612 | 20260526 | 10 | 2881 | 富邦金 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260527 | 9 | 2881 | 富邦金 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260605 | 2 | 2883 | 凱基金 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260605 | 2 | 2903 | 遠百 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260605 | 2 | 3018 | 隆銘綠能 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | middle_position |
| 20260612 | 20260602 | 5 | 3049 | 精金 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | low_position |
| 20260612 | 20260601 | 6 | 3059 | 華晶科 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | high_position |
| 20260612 | 20260529 | 7 | 3226 | 龍鋒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | long_base_low_position | general_breakout | low_position |
| 20260612 | 20260605 | 2 | 3226 | 龍鋒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | wide_range_breakout | general_breakout | middle_position |
| 20260612 | 20260529 | 7 | 3288 | 點晶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260612 | 20260601 | 6 | 3288 | 點晶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260612 | 20260602 | 5 | 3288 | 點晶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260612 | 20260605 | 2 | 3406 | 玉晶光 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260528 | 8 | 3523 | 迎輝 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260612 | 20260527 | 9 | 3528 | 安馳 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260529 | 7 | 4938 | 和碩 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260602 | 5 | 4938 | 和碩 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260527 | 9 | 4973 | 廣穎 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260612 | 20260526 | 10 | 5285 | 界霖 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260602 | 5 | 6155 | 鈞寶 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | high_position |
| 20260612 | 20260601 | 6 | 6214 | 精誠 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | high_position |
| 20260612 | 20260529 | 7 | 6654 | 天正國際 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | high_position |
| 20260612 | 20260605 | 2 | 6890 | 來億-KY | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260605 | 2 | 6916 | 華凌 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260611 | 1 | 7788 | 松川精密 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260611 | 1 | 8021 | 尖點 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260612 | 20260602 | 5 | 8070 | 長華* | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260528 | 8 | 8077 | 洛碁 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260529 | 7 | 8077 | 洛碁 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260603 | 4 | 8077 | 洛碁 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260601 | 6 | 8105 | 凌巨 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | high_position |
| 20260612 | 20260602 | 5 | 8105 | 凌巨 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260529 | 7 | 8454 | 富邦媒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260602 | 5 | 8454 | 富邦媒 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
| 20260612 | 20260529 | 7 | 8472 | 夠麻吉 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | general_breakout | middle_position |
| 20260612 | 20260528 | 8 | 8473 | 山林水 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260612 | 20260529 | 7 | 8473 | 山林水 | next_day_continuation_confirmed/pullback_5ma_confirmed/pullback_10ma_confirmed | limit_up_like_breakout | volume_attack | high_position |
