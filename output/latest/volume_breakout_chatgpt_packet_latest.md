# VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-07-16 19:40:58 Asia/Taipei`
- main_price_date: `20260716`
- watch_rows: `11`
- bottom_volume_attack_count: `11`
- selected_rows: `11`
- rows_with_risk_tags: `4`
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

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6505 | 台塑化 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 4.3394 | 34.6801 | 51.8027 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 6680 | 鑫創電子 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 5.4952 | 14.2857 | 6.8646 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 4139 | 馬光-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 1.1831 | 40.1623 | 42.1811 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 4534 | 慶騰 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.309 | 28.7234 | 31.1146 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 5 | 9914 | 美利達 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_many_days | 5.1438 | 13.4771 | 13.6302 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 6 | 2527 | 宏璟 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 3.3633 | 19.9758 | 24.03 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 7 | 3413 | 京鼎 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_many_days | 2.6497 | 12.6844 | 16.9985 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 8 | 1439 | 雋揚 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.8923 | 11.6034 | 4.9603 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 9 | 6243 | 迅杰 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | first_seen | 2.3978 | 19.875 | 53.6859 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 10 | 8932 | 智通* | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_2_3d | 2.0221 | 8.3682 | 28.8557 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 11 | 6907 | 雅特力-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 2.5444 | 26.455 | 77.6952 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Backtest Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | bottom_volume_attack | 4180 | 4072 | 2.0312 | 47.18 | 3934 | 4.101 | 49.87 | 3688 | 7.3461 | 50.49 | ok |
| volume_watch_scope | bottom_volume_attack | 4180 | 4072 | 2.0312 | 47.18 | 3934 | 4.101 | 49.87 | 3688 | 7.3461 | 50.49 | ok |

## Rules

- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.
- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.
- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.
- TDCC, warrant, revenue, consolidation length, breakout magnitude, and position context are ranking components.
- If the stock falls back below the prior-20D-high breakout threshold after the signal, later reports may tag failure or higher risk.

