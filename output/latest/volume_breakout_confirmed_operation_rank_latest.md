# Volume Breakout Confirmed Operation Rank

- generated_at: `2026-06-19 03:07:29 Asia/Taipei`
- latest_price_date: `20260618`
- rank_rule: only confirmation rows with `confirmation_date == latest_price_date` appear here.
- entry_rule: confirmation after close, next trading day open.
- scope: research only; all rows keep `approved_for_daily=False`.

## Confirmed Rank

| operation_rank | stock_id | stock_name | trigger_id | tdcc_list_type | tdcc_rank | classification_id | attack_method | price_position_type | evidence_sample_size | evidence_win_rate | evidence_avg_return | evidence_median_return | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3624 | 光頡 | next_day_break_signal_high_confirmed | weekly_increase | 7 | high_position_breakout | volume_attack | high_position | 15 | 60.0 | 15.7847 | 11.9403 | 19.9536 |
| 2 | 2484 | 希華 | pullback_5ma_confirmed | weekly_increase | 10 | locked_limit_up_breakout | locked_limit_up | high_position | 17 | 52.94 | 12.6883 | 6.1047 | 12.2207 |
| 3 | 3236 | 千如 | pullback_5ma_confirmed | weekly_increase | 35 | locked_limit_up_breakout | locked_limit_up | high_position | 17 | 52.94 | 12.6883 | 6.1047 | 12.2207 |
| 4 | 8121 | 越峰 | pullback_5ma_confirmed | weekly_increase | 41 | locked_limit_up_breakout | locked_limit_up | high_position | 17 | 52.94 | 12.6883 | 6.1047 | 12.2207 |
| 5 | 6182 | 合晶 | next_day_break_signal_high_confirmed | weekly_increase | 43 | high_position_breakout | volume_attack | high_position | 43 | 46.51 | 9.0158 | -2.2222 | 2.6537 |
| 6 | 2851 | 中再保 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 275 | 41.09 | 2.923 | -1.278 | -0.2248 |
| 7 | 3285 | 微端 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 481 | 40.54 | 2.3246 | -1.7595 | -1.3958 |
| 8 | 5345 | 馥鴻 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 481 | 40.54 | 2.3246 | -1.7595 | -1.3958 |
| 9 | 2596 | 綠意 | pullback_10ma_confirmed | no_tdcc |  | wide_range_breakout | volume_attack | middle_position | 73 | 30.14 | 1.2622 | -1.996 | -2.6499 |
| 10 | 2302 | 麗正 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 282 | 42.91 | 1.2764 | -2.0934 | -2.6828 |
| 11 | 2618 | 長榮航 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 282 | 42.91 | 1.2764 | -2.0934 | -2.6828 |
| 12 | 2718 | 全心投控 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 282 | 42.91 | 1.2764 | -2.0934 | -2.6828 |
| 13 | 2342 | 茂矽 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 471 | 39.07 | 1.0476 | -3.0 | -4.2143 |
| 14 | 3362 | 先進光 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 471 | 39.07 | 1.0476 | -3.0 | -4.2143 |
| 15 | 6488 | 環球晶 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 471 | 39.07 | 1.0476 | -3.0 | -4.2143 |
| 16 | 8906 | 花王 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 471 | 39.07 | 1.0476 | -3.0 | -4.2143 |
| 17 | 2061 | 風青 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1521 | 37.74 | 0.6778 | -3.8591 | -5.7803 |
| 18 | 2332 | 友訊 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1521 | 37.74 | 0.6778 | -3.8591 | -5.7803 |
| 19 | 3060 | 銘異 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1521 | 37.74 | 0.6778 | -3.8591 | -5.7803 |
| 20 | 4976 | 佳凌 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1521 | 37.74 | 0.6778 | -3.8591 | -5.7803 |
| 21 | 6742 | 澤米 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1521 | 37.74 | 0.6778 | -3.8591 | -5.7803 |

## Pending Queue

| queue_date | signal_date | signal_age_trading_days | stock_id | stock_name | pending_trigger_ids | classification_id | attack_method | price_position_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 20260612 | 4 | 1307 | 三芳 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260610 | 6 | 1438 | 三地開發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260618 | 20260608 | 8 | 1455 | 集盛 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 1714 | 和桐 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260612 | 4 | 1714 | 和桐 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260611 | 5 | 2243 | 宏旭-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260612 | 4 | 2243 | 宏旭-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 2305 | 全友 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 2413 | 環科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 2461 | 光群雷 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260609 | 7 | 2478 | 大毅 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260605 | 9 | 2483 | 百容 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 2483 | 百容 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260609 | 7 | 2484 | 希華 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260612 | 4 | 2493 | 揚博 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 2493 | 揚博 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 2501 | 國建 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 2520 | 冠德 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 2537 | 聯上發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 2537 | 聯上發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260609 | 7 | 2801 | 彰銀 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260616 | 2 | 2910 | 統領 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260617 | 1 | 3008 | 大立光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260605 | 9 | 3018 | 隆銘綠能 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260618 | 20260609 | 7 | 3022 | 威強電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260612 | 4 | 3026 | 禾伸堂 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 3093 | 港建* | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | wide_range_breakout | volume_attack | middle_position |
| 20260618 | 20260617 | 1 | 3094 | 聯傑 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260611 | 5 | 3290 | 東浦 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 3290 | 東浦 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260610 | 6 | 3362 | 先進光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 3362 | 先進光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260611 | 5 | 3441 | 聯一光電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 3441 | 聯一光電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260604 | 10 | 3550 | 聯穎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260609 | 7 | 3550 | 聯穎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 3550 | 聯穎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 3624 | 光頡 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 3624 | 光頡 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260617 | 1 | 3630 | 新鉅科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260611 | 5 | 4102 | 永日 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | standard_breakout | volume_attack | middle_position |
| 20260618 | 20260608 | 8 | 4402 | 郡都開發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260618 | 20260610 | 6 | 4402 | 郡都開發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260616 | 2 | 4551 | 智伸科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260609 | 7 | 4556 | 旭然 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 4556 | 旭然 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 4939 | 亞電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260610 | 6 | 4946 | 辣椒 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260618 | 20260612 | 4 | 5227 | 立凱-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 5227 | 立凱-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 5227 | 立凱-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 5228 | 鈺鎧 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260616 | 2 | 5328 | 華容 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260604 | 10 | 5426 | 振發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 5426 | 振發 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 5450 | 南良 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260618 | 20260611 | 5 | 5455 | 昇益 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | standard_breakout | volume_attack | middle_position |
| 20260618 | 20260612 | 4 | 5457 | 宣德 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260618 | 20260617 | 1 | 5460 | 同協 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260611 | 5 | 5468 | 凱鈺 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260612 | 4 | 5468 | 凱鈺 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 5468 | 凱鈺 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260617 | 1 | 5471 | 松翰 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260610 | 6 | 5534 | 長虹 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260609 | 7 | 5876 | 上海商銀 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260618 | 20260612 | 4 | 6173 | 信昌電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 6182 | 合晶 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 6517 | 保勝光學 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260617 | 1 | 6517 | 保勝光學 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260615 | 3 | 6613 | 朋億* | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 6645 | 金萬林-創 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 6668 | 中揚光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260617 | 1 | 6668 | 中揚光 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260618 | 20260615 | 3 | 6693 | 廣閎科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260604 | 10 | 6890 | 來億-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260615 | 3 | 7631 | 聚賢研發-創 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | wide_range_breakout | general_breakout | middle_position |
| 20260618 | 20260617 | 1 | 7782 | 光速火箭 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | wide_range_breakout | volume_attack | middle_position |
| 20260618 | 20260608 | 8 | 7788 | 松川精密 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260608 | 8 | 8043 | 蜜望實 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260618 | 20260616 | 2 | 8071 | 能率網通 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
