# Volume Attack Watch

- generated_at: `2026-07-16 19:40:58 Asia/Taipei`
- main_price_date: `20260716`
- total_watch_rows: `11`
- priority_distribution: `{'A_bottom_volume_attack': 11}`
- type_distribution: `{'bottom_volume_attack': 11}`
- scope_distribution: `{'bottom_volume_attack': 11}`
- selection_status_distribution: `{'selected': 11}`

## Interpretation

- Official model type is `bottom_volume_attack` only.
- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.
- No 60D-high gate, no moving-average gate, no same-day fake-breakout classification, and no selected/watch/risk sub-status.
- Long upper shadow or TDCC deterioration can reduce score or add risk tags, but they do not change the model hit into another model.
- Research observation basis is next trading day open after the signal date.
- This list is a model-selected universe and backtest layer. It is not standalone buy advice.

## Top Watch List

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6505 | 台塑化 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 4.3394 | 34.6801 | 51.8027 | 36.15862479788954 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 6680 | 鑫創電子 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 5.4952 | 14.2857 | 6.8646 | 13.190862196020635 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 4139 | 馬光-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 1.1831 | 40.1623 | 42.1811 | 34.84242365108792 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 4534 | 慶騰 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.309 | 28.7234 | 31.1146 | 26.14491026882122 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 5 | 9914 | 美利達 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_many_days | 5.1438 | 13.4771 | 13.6302 | 11.960640914832798 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 6 | 2527 | 宏璟 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 3.3633 | 19.9758 | 24.03 | 19.110576923076916 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 7 | 3413 | 京鼎 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_many_days | 2.6497 | 12.6844 | 16.9985 | 16.22423366547501 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 8 | 1439 | 雋揚 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.8923 | 11.6034 | 4.9603 | 8.501692134140072 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 9 | 6243 | 迅杰 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | first_seen | 2.3978 | 19.875 | 53.6859 | 18.857284501456295 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 10 | 8932 | 智通* | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_2_3d | 2.0221 | 8.3682 | 28.8557 | 16.666666666666675 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 11 | 6907 | 雅特力-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 2.5444 | 26.455 | 77.6952 | 40.77455455750256 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

