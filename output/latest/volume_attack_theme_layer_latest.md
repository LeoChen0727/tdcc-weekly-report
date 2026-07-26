# Volume Attack Theme Layer

- generated_at: `2026-07-26 15:09:54 Asia/Taipei`
- signal_date: `20260717`
- source_watch: `output/latest/volume_breakout_watch_latest.csv`
- source_watch_sha256: `8510ded0b1502a187277b12e6ca0a7ff548706d1773da1284b8db9ad040997de`
- source_theme: `output/latest/daily_theme_leadership_latest.csv`
- warrant_projection_source: `output/latest/all_candidates_latest.csv`
- warrant_projection_source_sha256: `b95fb177acbd82642758d09215b55712b71a7b0b722e17608c82e15667324fcd`
- warrant_official_parity_source: `output/latest/warrant_flow_latest.csv`
- warrant_official_parity_source_sha256: `01d9b53f670f9caf0d52add43c491f711d752ef7af4a1272244cdbc894aef6dd`
- rule: Volume-attack sections must show `theme_final_status`, `theme_structural_status`, `theme_mainstream_label`, and `theme_volume_attack_status`; do not show only the theme name.

## Status Rules

- confirmed_volume_theme: multiple volume breakouts with mainstream/emerging theme support.
- early_mainstream_candidate: at least three volume attack/watch rows in a mainstream/emerging theme, but not fully confirmed.
- watch_volume_theme: theme has volume attack evidence but breadth is still thin.
- single_stock_volume_attack: stock-level signal only; do not place in mainstream-funding front section.
- non_mainstream_volume_watch / weak_or_non_mainstream_volume_watch: observation only unless the stock confirms strongly.
- overheated_volume_theme / failed_volume_theme: downgrade chase entries and list as risk.
- theme_status_missing: source rows have no reliable stock theme; do not infer mainstream/non-mainstream from memory.

## Theme Volume Attack Matrix

| theme_name   | theme_final_status    | theme_structural_status   | theme_mainstream_label     | theme_volume_attack_status   |   volume_attack_count |   range_breakout_volume_count |   range_breakout_watch_count |   ma_reclaim_volume_attack_count |   near_high_volume_watch_count |   strict_high_breakout_count |   tdcc_accumulation_count |   tdcc_distribution_warning_count |   warrant_bullish_count |   leader_stock_id | leader_stock_name   | leader_volume_attack_type   | interpretation                                                                   |
|:-------------|:----------------------|:--------------------------|:---------------------------|:-----------------------------|----------------------:|------------------------------:|-----------------------------:|---------------------------------:|-------------------------------:|-----------------------------:|--------------------------:|----------------------------------:|------------------------:|------------------:|:--------------------|:----------------------------|:---------------------------------------------------------------------------------|
| 電子零組件業_待細分   | single_name_signal    | market_theme              | core_mainstream            | single_stock_volume_attack   |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              3288 | 點晶                  | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens   |
| 生技醫療業        | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated  | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              4139 | 馬光-KY               | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |
| 半導體業         | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 1 |                       0 |              6243 | 迅杰                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |
| 光電業          | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              3024 | 憶聲                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |

## Stock-Level Volume Attack With Theme Status

|   volume_breakout_rank |   stock_id | stock_name   | theme_name   | theme_final_status    | theme_structural_status   | theme_mainstream_label     | theme_volume_attack_status   | volume_breakout_type   | volume_breakout_priority   | selection_status   |   volume_breakout_score | candidate_source_type        |   volume_ratio | tdcc_status   | warrant_flow_signal   | next_volume_breakout_confirmation                   |
|-----------------------:|-----------:|:-------------|:-------------|:----------------------|:--------------------------|:---------------------------|:-----------------------------|:-----------------------|:---------------------------|:-------------------|------------------------:|:-----------------------------|---------------:|:--------------|:----------------------|:----------------------------------------------------|
|                      1 |       4139 | 馬光-KY        | 生技醫療業        | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated  | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   71.74 | risk_downgraded_candidate    |         9.2199 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      2 |       6243 | 迅杰           | 半導體業         | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   66.05 | individual_quality_candidate |         6.2003 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      3 |       3288 | 點晶           | 電子零組件業_待細分   | single_name_signal    | market_theme              | core_mainstream            | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   55.16 | individual_quality_candidate |         4.2197 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      4 |       3024 | 憶聲           | 光電業          | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   43.51 | individual_quality_candidate |         4.5208 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Read Order For ChatGPT

1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.
2. Read this file for the volume-attack theme layer.
3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.
4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.

