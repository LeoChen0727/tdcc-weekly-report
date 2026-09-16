# Volume Attack Theme Layer

- generated_at: `2026-09-16 19:45:41 Asia/Taipei`
- signal_date: `20260916`
- source_watch: `output/latest/volume_breakout_watch_latest.csv`
- source_watch_sha256: `7651731e77f27041f21bcac95fbab96d14cd2bfcba1041ca2f0e49c83930e5cc`
- source_theme: `output/latest/daily_theme_leadership_latest.csv`
- warrant_projection_source: `output/latest/all_candidates_latest.csv`
- warrant_projection_source_sha256: `5f873e08da495048f7961ea1033f537f7472a4a99c57f6fa8cfd0893c936828c`
- warrant_official_parity_source: `output/latest/warrant_flow_latest.csv`
- warrant_official_parity_source_sha256: `c3da683f268475a96ef806244df9d80a2d119d4bc67f078bd3bc0fad00c34fa4`
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

| theme_name   | theme_final_status        | theme_structural_status   | theme_mainstream_label     | theme_volume_attack_status   |   volume_attack_count |   range_breakout_volume_count |   range_breakout_watch_count |   ma_reclaim_volume_attack_count |   near_high_volume_watch_count |   strict_high_breakout_count |   tdcc_accumulation_count |   tdcc_distribution_warning_count |   warrant_bullish_count |   leader_stock_id | leader_stock_name   | leader_volume_attack_type   | interpretation                                                                         |
|:-------------|:--------------------------|:--------------------------|:---------------------------|:-----------------------------|----------------------:|------------------------------:|-----------------------------:|---------------------------------:|-------------------------------:|-----------------------------:|--------------------------:|----------------------------------:|------------------------:|------------------:|:--------------------|:----------------------------|:---------------------------------------------------------------------------------------|
| 資訊服務業_待細分    | single_name_signal        | market_theme              | core_mainstream            | single_stock_volume_attack   |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              6590 | 普鴻                  | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens         |
| 光電業_待細分      | single_name_signal        | market_theme              | core_mainstream            | single_stock_volume_attack   |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              6560 | 欣普羅                 | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens         |
| 生技醫療業        | mainstream_leader         | non_mainstream_theme      | non_mainstream_flow_active | non_mainstream_volume_watch  |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              4744 | 皇將                  | bottom_volume_attack        | volume activity without mainstream support; keep separate from mainstream-funding line |
| 化學工業         | mainstream_follow_through | non_mainstream_theme      | non_mainstream_flow_active | non_mainstream_volume_watch  |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              1776 | 展宇                  | bottom_volume_attack        | volume activity without mainstream support; keep separate from mainstream-funding line |
| 光電業          | mainstream_overheated     | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     2 |                             2 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              6226 | 光鼎                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries       |
| 通信網路業        | mainstream_overheated     | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              6218 | 豪勉                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries       |

## Stock-Level Volume Attack With Theme Status

|   volume_breakout_rank |   stock_id | stock_name   | theme_name   | theme_final_status        | theme_structural_status   | theme_mainstream_label     | theme_volume_attack_status   | volume_breakout_type   | volume_breakout_priority   | selection_status   |   volume_breakout_score | candidate_source_type        |   volume_ratio | tdcc_status   | warrant_flow_signal   | next_volume_breakout_confirmation                   |
|-----------------------:|-----------:|:-------------|:-------------|:--------------------------|:--------------------------|:---------------------------|:-----------------------------|:-----------------------|:---------------------------|:-------------------|------------------------:|:-----------------------------|---------------:|:--------------|:----------------------|:----------------------------------------------------|
|                      1 |       6218 | 豪勉           | 通信網路業        | mainstream_overheated     | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   69.2  | individual_quality_candidate |         5.165  |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      2 |       6560 | 欣普羅          | 光電業_待細分      | single_name_signal        | market_theme              | core_mainstream            | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   64.01 | individual_quality_candidate |         4.9612 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      3 |       4744 | 皇將           | 生技醫療業        | mainstream_leader         | non_mainstream_theme      | non_mainstream_flow_active | non_mainstream_volume_watch  | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   60.15 | individual_quality_candidate |         4.9328 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      4 |       6226 | 光鼎           | 光電業          | mainstream_overheated     | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   58.32 | individual_quality_candidate |         0.2764 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      5 |       6590 | 普鴻           | 資訊服務業_待細分    | single_name_signal        | market_theme              | core_mainstream            | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   53.83 | individual_quality_candidate |         6.891  |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      6 |       6168 | 宏齊           | 光電業          | mainstream_overheated     | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   51.5  | individual_quality_candidate |         2.6871 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      7 |       1776 | 展宇           | 化學工業         | mainstream_follow_through | non_mainstream_theme      | non_mainstream_flow_active | non_mainstream_volume_watch  | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   47.85 | individual_quality_candidate |         3.4172 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Read Order For ChatGPT

1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.
2. Read this file for the volume-attack theme layer.
3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.
4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.

