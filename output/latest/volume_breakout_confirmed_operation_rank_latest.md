# Volume Breakout Confirmed Operation Rank

- generated_at: `2026-07-08 16:30:28 Asia/Taipei`
- latest_price_date: `20260707`
- rank_rule: only confirmation rows with `confirmation_date == latest_price_date` appear here.
- entry_rule: confirmation after close, next trading day open.
- scope: research only; all rows keep `approved_for_daily=False`.

## Confirmed Rank

| operation_rank | stock_id | stock_name | trigger_id | tdcc_list_type | tdcc_rank | classification_id | attack_method | price_position_type | evidence_sample_size | evidence_win_rate | evidence_avg_return | evidence_median_return | ranking_research_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1434 | 福懋 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 188 | 42.02 | 3.6117 | -1.2556 | 0.3254 |
| 2 | 2630 | 亞航 | pullback_5ma_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 188 | 42.02 | 3.6117 | -1.2556 | 0.3254 |
| 3 | 6603 | 富強鑫 | pullback_5ma_confirmed | no_tdcc |  | standard_breakout | general_breakout | middle_position | 13 | 46.15 | 5.5209 | -1.1268 | -0.0284 |
| 4 | 9960 | 邁達康 | pullback_10ma_confirmed | no_tdcc |  | high_position_breakout | volume_attack | high_position | 43 | 37.21 | 2.9108 | -1.996 | -1.5858 |
| 5 | 8033 | 雷虎 | pullback_5ma_confirmed | weekly_increase | 2 | locked_limit_up_breakout | locked_limit_up | middle_position | 23 | 39.13 | 6.7518 | -3.7915 | -1.7613 |
| 6 | 1617 | 榮星 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 522 | 39.46 | 2.0235 | -1.9083 | -1.8448 |
| 7 | 2427 | 三商電 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 522 | 39.46 | 2.0235 | -1.9083 | -1.8448 |
| 8 | 8928 | 鉅明 | pullback_5ma_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 522 | 39.46 | 2.0235 | -1.9083 | -1.8448 |
| 9 | 1909 | 榮成 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 295 | 42.37 | 1.0141 | -2.2792 | -3.1582 |
| 10 | 4114 | 健喬 | next_day_break_signal_high_confirmed | no_tdcc |  | high_position_breakout | general_breakout | high_position | 295 | 42.37 | 1.0141 | -2.2792 | -3.1582 |
| 11 | 2601 | 益航 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1630 | 37.67 | 0.7891 | -3.8115 | -5.6254 |
| 12 | 3066 | 李洲 | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1630 | 37.67 | 0.7891 | -3.8115 | -5.6254 |
| 13 | 6617 | 共信-KY | next_day_break_signal_high_confirmed | no_tdcc |  | locked_limit_up_breakout | locked_limit_up | high_position | 1630 | 37.67 | 0.7891 | -3.8115 | -5.6254 |

## Pending Queue

| queue_date | signal_date | signal_age_trading_days | stock_id | stock_name | pending_trigger_ids | classification_id | attack_method | price_position_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260707 | 20260703 | 2 | 1310 | 台苯 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260625 | 8 | 1313 | 聯成 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | standard_breakout | volume_attack | middle_position |
| 20260707 | 20260703 | 2 | 1313 | 聯成 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 1314 | 中石化 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 1326 | 台化 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 1409 | 新纖 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260625 | 8 | 1435 | 中福 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260707 | 20260629 | 6 | 1435 | 中福 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 1435 | 中福 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260629 | 6 | 1444 | 力麗 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 1444 | 力麗 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 1447 | 力鵬 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260701 | 4 | 1447 | 力鵬 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260702 | 3 | 1447 | 力鵬 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 1455 | 集盛 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260707 | 20260625 | 8 | 1515 | 力山 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260626 | 7 | 1515 | 力山 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260701 | 4 | 1515 | 力山 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260702 | 3 | 1515 | 力山 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 1515 | 力山 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260703 | 2 | 1708 | 東鹼 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260707 | 20260701 | 4 | 1709 | 和益 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260703 | 2 | 1717 | 長興 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260707 | 20260626 | 7 | 1718 | 中纖 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 1718 | 中纖 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 2103 | 台橡 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 2208 | 台船 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | low_position |
| 20260707 | 20260701 | 4 | 2466 | 冠西電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260702 | 3 | 2466 | 冠西電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 2466 | 冠西電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260626 | 7 | 2483 | 百容 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260706 | 1 | 2511 | 太子 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260707 | 20260630 | 5 | 2634 | 漢翔 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260630 | 5 | 2645 | 長榮航太 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260701 | 4 | 2645 | 長榮航太 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 2645 | 長榮航太 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 3026 | 禾伸堂 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 3055 | 蔚華科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260701 | 4 | 3055 | 蔚華科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260702 | 3 | 3055 | 蔚華科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 3055 | 蔚華科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260626 | 7 | 3230 | 錦明 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260707 | 20260629 | 6 | 3230 | 錦明 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 3230 | 錦明 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260702 | 3 | 3346 | 麗清 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260623 | 10 | 3360 | 尚立 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260624 | 9 | 3360 | 尚立 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 3518 | 柏騰 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260701 | 4 | 3605 | 宏致 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260702 | 3 | 3605 | 宏致 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260630 | 5 | 3611 | 鼎翰 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260707 | 20260629 | 6 | 3717 | 聯嘉投控 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 3717 | 聯嘉投控 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260623 | 10 | 4147 | 中裕 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 4147 | 中裕 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 4532 | 瑞智 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260701 | 4 | 4541 | 晟田 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 4541 | 晟田 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 4564 | 元翎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260707 | 20260625 | 8 | 4707 | 磐亞 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260626 | 7 | 4707 | 磐亞 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260629 | 6 | 4707 | 磐亞 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 4707 | 磐亞 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 4743 | 合一 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 4763 | 材料*-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260707 | 20260703 | 2 | 4911 | 德英 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | long_base_low_position | volume_attack | low_position |
| 20260707 | 20260624 | 9 | 4924 | 欣厚-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | volume_attack | high_position |
| 20260707 | 20260703 | 2 | 4989 | 榮科 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | middle_position |
| 20260707 | 20260624 | 9 | 5011 | 久陽 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 5371 | 中光電 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260629 | 6 | 5434 | 崇越 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260701 | 4 | 5483 | 中美晶 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260623 | 10 | 5489 | 彩富 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260624 | 9 | 6226 | 光鼎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260626 | 7 | 6226 | 光鼎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260629 | 6 | 6226 | 光鼎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260630 | 5 | 6226 | 光鼎 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 6477 | 安集 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
| 20260707 | 20260703 | 2 | 6509 | 聚和 | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | high_position_breakout | general_breakout | high_position |
| 20260707 | 20260703 | 2 | 6525 | 捷敏-KY | pullback_5ma_confirmed/next_day_break_signal_high_confirmed/next_day_continuation_confirmed/pullback_10ma_confirmed | locked_limit_up_breakout | locked_limit_up | high_position |
