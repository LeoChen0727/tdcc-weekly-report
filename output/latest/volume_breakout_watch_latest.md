# Volume Attack Watch

- generated_at: `2026-08-11 20:00:17 Asia/Taipei`
- main_price_date: `20260811`
- total_watch_rows: `13`
- priority_distribution: `{'A_bottom_volume_attack': 13}`
- type_distribution: `{'bottom_volume_attack': 13}`
- scope_distribution: `{'bottom_volume_attack': 13}`
- selection_status_distribution: `{'selected': 13}`

## Interpretation

- Official model type is `bottom_volume_attack` only.
- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.
- No 60D-high gate, no moving-average gate, no same-day fake-breakout classification, and no selected/watch/risk sub-status.
- Long upper shadow or TDCC deterioration can reduce score or add risk tags, but they do not change the model hit into another model.
- Research observation basis is next trading day open after the signal date.
- This list is a model-selected universe and backtest layer. It is not standalone buy advice.

## Top Watch List

| advisory_volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2065 | 世豐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 5.5279 | 18.1102 | 16.4596 | 16.036203295428166 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 5468 | 凱鈺 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 2.9671 | 22.2 | 19.5695 | 21.94391777267739 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 8112 | 至上 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 3.8666 | 17.3709 | 17.096 | 17.14402858314299 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 9921 | 巨大 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.4886 | 32.7381 | 37.1464 | 26.769370700926622 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 5 | 4931 | 新盛力 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | continued_overheated | 4.3433 | 30.102 | 15.3846 | 24.51171875 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 6 | 6121 | 新普 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | stale_signal | 2.5038 | 17.4324 | 13.0039 | 16.060100166944903 | stale_signal | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 7 | 9914 | 美利達 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_many_days | 2.3054 | 23.7533 | 23.9159 | 17.69845232151772 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 8 | 2103 | 台橡 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 4.3785 | 31.422 | 14.6 | 22.76379217996787 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 9 | 6225 | 天瀚 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 2.0428 | 34.7345 | 23.5294 | 21.314741035856557 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 10 | 2536 | 宏普 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_2_3d | 2.2093 | 16.7131 | 8.2687 | 11.332536203002519 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 11 | 4148 | 全宇生技-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.8304 | 5.178 | 8.5142 | 5.613778536030534 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 12 | 9962 | 有益 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.4833 | 5.8282 | 5.2899 | 4.895104895104874 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 13 | 2392 | 正崴 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | stale_signal | 2.2374 | 13.6298 | 10.9244 | 10.792473945583003 | stale_signal | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

