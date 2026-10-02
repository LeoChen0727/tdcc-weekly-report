# VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-10-02 19:48:15 Asia/Taipei`
- main_price_date: `20261002`
- watch_rows: `34`
- bottom_volume_attack_count: `34`
- selected_rows: `34`
- rows_with_risk_tags: `23`
- watch_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.csv
- watch_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.md
- backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.csv
- backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.md

## Model Definition

- Model display name: 放量攻擊模型.
- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.
- The model intentionally does not require a 60D high breakout or moving-average reclaim.
- The model emits selected rows only. Risk flags and score components are ranking/operation context, not a separate watch/risk status.
- Same-day fake breakout is not confirmed on the signal date. Do not label a selected row as failed breakout until later price action confirms failure.
- Research observation basis is signal date next trading day open.

## Top Volume Attack

| advisory_volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5205 | 中茂 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 7.9675 | 31.7919 | 10.9489 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 5015 | 華祺 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 9.0619 | 11.655 | 8.6168 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 9933 | 中鼎 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_2_3d | 6.2819 | 11.4355 | 12.3926 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 3701 | 大眾控 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 5.2398 | 34.303 | 28.0925 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 5 | 4722 | 國精化 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 4.2904 | 21.6931 | 14.1439 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 6 | 6144 | 得利影 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 7.8689 | 11.5079 | 6.0377 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 7 | 3236 | 千如 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 3.4803 | 22.1968 | 21.9178 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 8 | 1735 | 日勝化 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 5.5889 | 9.3827 | 4.9763 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 9 | 6877 | 鏵友益 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 4.343 | 20.1581 | 33.9207 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 10 | 2033 | 佳大 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout |  | continued_overheated | 0.447 | 37.2654 | 107.7079 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 11 | 5013 | 強新 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 2.706 | 44.1538 | 63.5253 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 12 | 3673 | TPK-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 3.6766 | 24.3827 | 20.2985 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 13 | 4927 | 泰鼎-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_2_3d | 4.0636 | 10.0571 | 13.8298 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 14 | 3707 | 漢磊 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 2.6378 | 21.3675 | 36.9775 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 15 | 8150 | 南茂 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.1364 | 18.6916 | 40.7982 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 16 | 4919 | 新唐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 4.6738 | 21.6418 | 35.2697 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 17 | 6127 | 九豪 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | continued_overheated | 6.2619 | 21.7935 | 20.1646 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 18 | 6672 | 騰輝電子-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.1614 | 42.9967 | 61.3971 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 19 | 4958 | 臻鼎-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | stale_signal | 2.2436 | 18.6047 | 10.6509 | stale_signal | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 20 | 8182 | 加高 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | stale_signal | 6.3837 | 14.7095 | 16.7296 | stale_signal/long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 21 | 6155 | 鈞寶 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | continued_overheated | 5.8842 | 29.0036 | 29.4643 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 22 | 2061 | 風青 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 2.3271 | 21.5054 | 21.0714 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 23 | 6202 | 盛群 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_2_3d | 3.3922 | 7.1186 | 8.0342 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 24 | 1708 | 東鹼 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | repeated_but_no_breakout | 3.4512 | 12.1756 | 11.0672 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 25 | 3042 | 晶技 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 2.4722 | 16.4141 | 28.0556 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 26 | 3031 | 佰鴻 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | repeated_but_no_breakout | 3.2764 | 15.9011 | 33.0629 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 27 | 1310 | 台苯 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | stale_signal | 2.3593 | 8.7104 | 7.1349 | stale_signal | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 28 | 6122 | 擎邦 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.0868 | 15.7609 | 31.2115 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 29 | 2340 | 台亞 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 4.5848 | 33.1878 | 33.9678 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 30 | 4903 | 聯光通 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 2.6664 | 7.4733 | 19.0539 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 31 | 4556 | 旭然 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | continued_overheated | 3.8409 | 22.3291 | 63.5714 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 32 | 5285 | 界霖 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | continued_2_3d | 2.8433 | 7.3753 | 10.4911 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 33 | 2327 | 國巨* | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | repeated_but_no_breakout | 2.5921 | 9.2496 | 15.9259 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 34 | 3094 | 聯傑 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 2.3149 | 29.4659 | 70.6311 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | bottom_volume_attack | 4306 | 4072 | 2.0312 | 47.18 | 3934 | 4.101 | 49.87 | 3688 | 7.3461 | 50.49 | ok |
| volume_watch_scope | bottom_volume_attack | 4306 | 4072 | 2.0312 | 47.18 | 3934 | 4.101 | 49.87 | 3688 | 7.3461 | 50.49 | ok |

## Rules

- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.
- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.
- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.
- The watch artifact does not own warrant semantics. Formal warrant values are resolved later from the canonical all-candidates projection.
- If the stock falls back below the prior-20D-high breakout threshold after the signal, later reports may tag failure or higher risk.

