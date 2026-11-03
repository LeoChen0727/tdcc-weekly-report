# Volume Attack Theme Layer

- generated_at: `2026-11-03 19:37:59 Asia/Taipei`
- signal_date: `20261103`
- source_watch: `output/latest/volume_breakout_watch_latest.csv`
- source_watch_sha256: `2a86734a24fa0f9e5db1b21e8e55db34816511e41297c3b23a57acd7a336a317`
- source_theme: `output/latest/daily_theme_leadership_latest.csv`
- warrant_projection_source: `output/latest/all_candidates_latest.csv`
- warrant_projection_source_sha256: `6bfc11b16718e359a21f319f54953b9e0301a601e16cbf7cbdf7a15ffba1948b`
- warrant_official_parity_source: `output/latest/warrant_flow_latest.csv`
- warrant_official_parity_source_sha256: `ef764011c7bc77a81fd3608b448ec2dec695ac37dfd5f849683602bb4b41062a`
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

| theme_name   | theme_final_status    | theme_structural_status   | theme_mainstream_label    | theme_volume_attack_status   |   volume_attack_count |   range_breakout_volume_count |   range_breakout_watch_count |   ma_reclaim_volume_attack_count |   near_high_volume_watch_count |   strict_high_breakout_count |   tdcc_accumulation_count |   tdcc_distribution_warning_count |   warrant_bullish_count |   leader_stock_id | leader_stock_name   | leader_volume_attack_type   | interpretation                                                                   |
|:-------------|:----------------------|:--------------------------|:--------------------------|:-----------------------------|----------------------:|------------------------------:|-----------------------------:|---------------------------------:|-------------------------------:|-----------------------------:|--------------------------:|----------------------------------:|------------------------:|------------------:|:--------------------|:----------------------------|:---------------------------------------------------------------------------------|
| 數位雲端_待細分     | single_name_signal    | market_theme              | core_mainstream           | single_stock_volume_attack   |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              6865 | 偉康科技                | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens   |
| 資訊服務業        | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated | overheated_volume_theme      |                     3 |                             3 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              8272 | 全景軟體                | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |
| 鋼鐵工業         | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 1 |                       0 |              5013 | 強新                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |

## Stock-Level Volume Attack With Theme Status

|   volume_breakout_rank |   stock_id | stock_name   | theme_name   | theme_final_status    | theme_structural_status   | theme_mainstream_label    | theme_volume_attack_status   | volume_breakout_type   | volume_breakout_priority   | selection_status   |   volume_breakout_score | candidate_source_type        |   volume_ratio | tdcc_status   | warrant_flow_signal   | next_volume_breakout_confirmation                   |
|-----------------------:|-----------:|:-------------|:-------------|:----------------------|:--------------------------|:--------------------------|:-----------------------------|:-----------------------|:---------------------------|:-------------------|------------------------:|:-----------------------------|---------------:|:--------------|:----------------------|:----------------------------------------------------|
|                      1 |       8272 | 全景軟體         | 資訊服務業        | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   76.61 | individual_quality_candidate |        10.6921 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      2 |       7767 | 仁大資訊         | 資訊服務業        | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   75.68 | individual_quality_candidate |        15.044  |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      3 |       6865 | 偉康科技         | 數位雲端_待細分     | single_name_signal    | market_theme              | core_mainstream           | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   71.72 | individual_quality_candidate |        13.2597 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      4 |       5013 | 強新           | 鋼鐵工業         | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   62.15 | individual_quality_candidate |         3.3833 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      5 |       5202 | 力新           | 資訊服務業        | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   54.31 | individual_quality_candidate |         3.9003 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Read Order For ChatGPT

1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.
2. Read this file for the volume-attack theme layer.
3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.
4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.

