# VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-08-11 20:00:17 Asia/Taipei`
- main_price_date: `20260811`
- watch_rows: `13`
- bottom_volume_attack_count: `13`
- selected_rows: `13`
- rows_with_risk_tags: `6`
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
| 1 | 2065 | 世豐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 5.5279 | 18.1102 | 16.4596 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 5468 | 凱鈺 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 2.9671 | 22.2 | 19.5695 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 8112 | 至上 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 3.8666 | 17.3709 | 17.096 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 9921 | 巨大 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.4886 | 32.7381 | 37.1464 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 5 | 4931 | 新盛力 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | continued_overheated | 4.3433 | 30.102 | 15.3846 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 6 | 6121 | 新普 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | stale_signal | 2.5038 | 17.4324 | 13.0039 | stale_signal | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 7 | 9914 | 美利達 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_many_days | 2.3054 | 23.7533 | 23.9159 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 8 | 2103 | 台橡 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 4.3785 | 31.422 | 14.6 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 9 | 6225 | 天瀚 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 2.0428 | 34.7345 | 23.5294 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 10 | 2536 | 宏普 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_2_3d | 2.2093 | 16.7131 | 8.2687 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 11 | 4148 | 全宇生技-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.8304 | 5.178 | 8.5142 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 12 | 9962 | 有益 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.4833 | 5.8282 | 5.2899 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 13 | 2392 | 正崴 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | stale_signal | 2.2374 | 13.6298 | 10.9244 | stale_signal | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

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

