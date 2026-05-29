# Volume Attack Theme Layer

- generated_at: `2026-05-29 19:28:39 Asia/Taipei`
- signal_date: `20260528`
- source_watch: `output/latest/volume_breakout_watch_latest.csv`
- source_theme: `output/latest/daily_theme_leadership_latest.csv`
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

| theme_name   | theme_final_status   | theme_structural_status   | theme_mainstream_label   | theme_volume_attack_status   |   volume_attack_count |   range_breakout_volume_count |   range_breakout_watch_count |   ma_reclaim_volume_attack_count |   near_high_volume_watch_count |   strict_high_breakout_count |   tdcc_accumulation_count |   tdcc_distribution_warning_count |   warrant_bullish_count |   leader_stock_id | leader_stock_name   | leader_volume_attack_type   | interpretation                                                                                      |
|:-------------|:---------------------|:--------------------------|:-------------------------|:-----------------------------|----------------------:|------------------------------:|-----------------------------:|---------------------------------:|-------------------------------:|-----------------------------:|--------------------------:|----------------------------------:|------------------------:|------------------:|:--------------------|:----------------------------|:----------------------------------------------------------------------------------------------------|
| other        | single_name_signal   | single_name_signal        | single_name_signal       | theme_status_missing         |                     1 |                             0 |                            0 |                                0 |                              0 |                            0 |                         0 |                                 0 |                       0 |              7716 | 昱臺國際                | volume_expansion_watch      | theme mapping missing; do not classify as mainstream or non-mainstream until theme mapping is fixed |

## Stock-Level Volume Attack With Theme Status

|   stock_id | stock_name   | theme_name   | theme_final_status   | theme_structural_status   | theme_mainstream_label   | theme_volume_attack_status   | volume_breakout_type   | volume_breakout_priority   | selection_status                | candidate_source_type        |   volume_ratio | tdcc_status   | warrant_flow_signal   | next_volume_breakout_confirmation                              |
|-----------:|:-------------|:-------------|:---------------------|:--------------------------|:-------------------------|:-----------------------------|:-----------------------|:---------------------------|:--------------------------------|:-----------------------------|---------------:|:--------------|:----------------------|:---------------------------------------------------------------|
|       7716 | 昱臺國際         | other        | single_name_signal   | single_name_signal        | single_name_signal       | theme_status_missing         | volume_expansion_watch | D_risk_downgrade           | not_selected_by_candidate_model | individual_quality_candidate |         1.8657 |               |                       | risk first: avoid chasing until heat/TDCC/repeat risk improves |

## Read Order For ChatGPT

1. Read `daily_candidate_two_line_view_latest.md/csv` for mainstream vs individual lines.
2. Read this file for the volume-attack theme layer.
3. Read `volume_breakout_watch_latest.md/csv` only for detailed price/volume fields.
4. If a row lacks `theme_final_status` or `theme_volume_attack_status`, mark `theme_status_missing` instead of guessing.

