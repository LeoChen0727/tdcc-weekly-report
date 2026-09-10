# Volume Attack Theme Layer

- generated_at: `2026-09-10 19:41:38 Asia/Taipei`
- signal_date: `20260910`
- source_watch: `output/latest/volume_breakout_watch_latest.csv`
- source_watch_sha256: `18d888d6bc364e77a0c5e8e8c2c4d939dec7bfcca67d844ead865d17734903d1`
- source_theme: `output/latest/daily_theme_leadership_latest.csv`
- warrant_projection_source: `output/latest/all_candidates_latest.csv`
- warrant_projection_source_sha256: `4d8f44097de2fb2efe987443028eeb7046860965581c833f72594ab69908bad9`
- warrant_official_parity_source: `output/latest/warrant_flow_latest.csv`
- warrant_official_parity_source_sha256: `b28bf3858c0a2a5862d8e1164c4d7a8f1d01eb7b13191877b00c4e516975bd51`
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
| 其他電子業_待細分    | single_name_signal    | market_theme              | core_mainstream            | single_stock_volume_attack   |                     2 |                             2 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              3628 | 盈正                  | bottom_volume_attack        | single-stock volume attack only; keep in individual line unless theme broadens   |
| 半導體業         | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     2 |                             2 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 2 |                       0 |              8227 | 巨有科技                | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |
| 電子零組件業       | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     2 |                             2 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 2 |                       0 |              3624 | 光頡                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |
| 電腦及週邊設備業     | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     2 |                             2 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 1 |                       0 |              2305 | 全友                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |
| 通信網路業        | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      |                     1 |                             1 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              4908 | 前鼎                  | bottom_volume_attack        | volume is active but overheat/distribution risk is high; downgrade chase entries |

## Stock-Level Volume Attack With Theme Status

|   volume_breakout_rank |   stock_id | stock_name   | theme_name   | theme_final_status    | theme_structural_status   | theme_mainstream_label     | theme_volume_attack_status   | volume_breakout_type   | volume_breakout_priority   | selection_status   |   volume_breakout_score | candidate_source_type        |   volume_ratio | tdcc_status   | warrant_flow_signal   | next_volume_breakout_confirmation                   |
|-----------------------:|-----------:|:-------------|:-------------|:----------------------|:--------------------------|:---------------------------|:-----------------------------|:-----------------------|:---------------------------|:-------------------|------------------------:|:-----------------------------|---------------:|:--------------|:----------------------|:----------------------------------------------------|
|                      1 |       8227 | 巨有科技         | 半導體業         | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   71.24 | individual_quality_candidate |         5.6747 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      2 |       3628 | 盈正           | 其他電子業_待細分    | single_name_signal    | market_theme              | core_mainstream            | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   68.41 | individual_quality_candidate |         7.5659 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      3 |       2338 | 光罩           | 半導體業         | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   67.98 | individual_quality_candidate |         6.9657 |               | no_signal             | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      4 |       6739 | 竹陞科技         | 其他電子業_待細分    | single_name_signal    | market_theme              | core_mainstream            | single_stock_volume_attack   | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   56.77 | individual_quality_candidate |         1.9447 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      5 |       3624 | 光頡           | 電子零組件業       | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   53.36 | individual_quality_candidate |         2.2231 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      6 |       2305 | 全友           | 電腦及週邊設備業     | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   52.66 | individual_quality_candidate |         2.315  |               | no_signal             | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      7 |       5386 | 青雲           | 電腦及週邊設備業     | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   47.98 | individual_quality_candidate |         2.2025 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      8 |       3354 | 律勝           | 電子零組件業       | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   46.91 | individual_quality_candidate |         3.4101 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
|                      9 |       4908 | 前鼎           | 通信網路業        | mainstream_overheated | core_mainstream_theme     | core_mainstream_overheated | overheated_volume_theme      | bottom_volume_attack   | A_bottom_volume_attack     | selected           |                   35.75 | individual_quality_candidate |         3.0157 |               |                       | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

## Read Order For ChatGPT

1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.
2. Read this file for the volume-attack theme layer.
3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.
4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.

