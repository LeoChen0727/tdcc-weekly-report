# BOTTOM VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-06-12 14:27:10 Asia/Taipei`
- main_price_date: `20260611`
- watch_rows: `13`
- bottom_volume_attack_count: `13`
- selected_rows: `13`
- rows_with_risk_tags: `9`
- watch_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.csv
- watch_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.md
- backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.csv
- backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.md

## Model Definition

- Model display name: 底部放量攻擊模型.
- Hard gates: close >= prior 20 trading day high excluding signal day * 1.02; volume_ratio >= 2.0; 20D average volume >= 1000 lots; bullish candle.
- The model intentionally does not require a 60D high breakout or moving-average reclaim.
- The model emits selected rows only. Risk flags and score components are ranking/operation context, not a separate watch/risk status.
- Same-day fake breakout is not confirmed on the signal date. Do not label a selected row as failed breakout until later price action confirms failure.
- Research entry basis is signal date next trading day open.

## Top Bottom Volume Attack

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1438 | 三地開發 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 6.3279 | 20.25 | 10.8295 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 1714 | 和桐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 6.4424 | 46.789 | 46.789 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 2537 | 聯上發 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | strong_accumulation | continued_overheated | 7.1809 | 12.4378 | 10.2439 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 8021 | 尖點 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | B_confirm_needed | mild_accumulation | first_seen | 3.5006 | 22.8448 | 32.8671 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 5345 | 馥鴻 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.0603 | 43.4077 | 62.5287 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 2597 | 潤弘 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 2.5679 | 22.5225 | 27.5 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 7 | 4306 | 炎洲 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 2.9076 | 11.2281 | 18.7266 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 8 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 3.9146 | 35.8824 | 46.2025 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 9 | 2243 | 宏旭-KY | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | first_seen | 2.9276 | 13.0217 | 56.351 | tdcc_distribution_warning | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 10 | 9910 | 豐泰 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 3.0611 | 34.9096 | 30.3763 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 11 | 7788 | 松川精密 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 3.7142 | 43.0079 | 48.4932 | tdcc_distribution_warning/continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 12 | 2547 | 日勝生 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | platform_breakout | C_watch_only | distribution_warning | stale_signal | 2.8575 | 10.8871 | 7.3171 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 13 | 2484 | 希華 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 3.2054 | 14.0977 | 53.2828 | tdcc_distribution_warning/continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

## Backtest Summary

_No rows._

## Rules

- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.
- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.
- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.
- TDCC, warrant, revenue, consolidation length, breakout magnitude, and position context are ranking components.
- If the stock falls back below the prior-20D-high breakout threshold after entry, later reports may tag failure or reduce risk.

