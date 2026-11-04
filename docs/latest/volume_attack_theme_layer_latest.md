# Volume Attack Theme Layer

- generated_at: `2026-11-04 19:40:56 Asia/Taipei`
- signal_date: `20261104`
- source_watch: `output/latest/volume_breakout_watch_latest.csv`
- source_watch_sha256: `fee1f42e2ee2f3e72358aa5729579d0502582fc1a30d6cb871194d5665a3690c`
- source_theme: `output/latest/daily_theme_leadership_latest.csv`
- warrant_projection_source: `output/latest/all_candidates_latest.csv`
- warrant_projection_source_sha256: `f3c49deb0a10cc95f23f135465bcad5b59592db5974c85376eab5d5f2aa48e85`
- warrant_official_parity_source: `output/latest/warrant_flow_latest.csv`
- warrant_official_parity_source_sha256: `5315d85af2849b628af176e76bc9758b4cbbeeeacb2777fabfa9c35d4195e134`
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
| 資訊服務業_待細分    | single_name_signal        | market_theme              | core_mainstream            | single_stock_volume_attack   |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              7819 | 精誠金融                | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens         |
| 紡織纖維         | single_name_signal        | non_mainstream_theme      | non_mainstream_single_name | single_stock_volume_attack   |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              1410 | 南染                  | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens         |
| 航運業          | mainstream_follow_through | non_mainstream_theme      | non_mainstream_flow_active | non_mainstream_volume_watch  |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              2643 | 捷迅                  | bottom_volume_attack        | volume activity without mainstream support; keep separate from mainstream-funding line |
| 其他           | mainstream_overheated     | non_mainstream_theme      | non_mainstream_overheated  | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              1416 | 廣豐                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries       |

## Stock-Level Volume Attack With Theme Status

|   volume_breakout_rank |   stock_id | stock_name   | theme_name   | theme_final_status        | theme_structural_status   | theme_mainstream_label     | theme_volume_attack_status   | volume_breakout_type   | volume_breakout_priority   | selection_status   |   volume_breakout_score | candidate_source_type        |   volume_ratio | tdcc_status   | warrant_flow_signal   | next_volume_breakout_confirmation                   |
|-----------------------:|-----------:|:-------------|:-------------|:--------------------------|:--------------------------|:---------------------------|:-----------------------------|:-----------------------|:---------------------------|:-------------------|------------------------:|:-----------------------------|---------------:|:--------------|:----------------------|:----------------------------------------------------|
|                      1 |       7819 | 精誠金融         | 資訊服務業_待細分    | single_name_signal        | market_theme              | core_mainstream            | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   76.63 | individual_quality_candidate |         8.1558 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      2 |       1410 | 南染           | 紡織纖維         | single_name_signal        | non_mainstream_theme      | non_mainstream_single_name | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   64.71 | individual_quality_candidate |         4.7115 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      3 |       2643 | 捷迅           | 航運業          | mainstream_follow_through | non_mainstream_theme      | non_mainstream_flow_active | non_mainstream_volume_watch  | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   60.4  | individual_quality_candidate |        11.4667 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      4 |       1416 | 廣豐           | 其他           | mainstream_overheated     | non_mainstream_theme      | non_mainstream_overheated  | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   40.69 | individual_quality_candidate |         2.3384 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Read Order For ChatGPT

1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.
2. Read this file for the volume-attack theme layer.
3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.
4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.

