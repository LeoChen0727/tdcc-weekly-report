# Daily Theme Leadership Layer

- generated_at: `2026-07-10 01:34:23 Asia/Taipei`
- signal_date: `20260709`
- source: `output/latest/all_candidates_latest.csv`
- purpose: keep mainstream-theme selection separate from individual-quality / latent-watch selection.

## Theme Matrix

| theme_name   | theme_final_status    | theme_structural_status   | theme_mainstream_label    |   theme_candidate_count |   theme_priority_high_count |   theme_priority_confirm_count |   theme_true_breakout_count |   theme_volume_breakout_count |   theme_near_high_count |   theme_tdcc_strong_count |   theme_tdcc_mild_count |   theme_warrant_bullish_count |   theme_overheated_count |   theme_avg_relative_strength_vs_benchmark |   theme_leader_stock_id | theme_leader_stock_name   |   theme_breadth_score |   theme_strength_score |   theme_risk_score |
|:-------------|:----------------------|:--------------------------|:--------------------------|------------------------:|----------------------------:|-------------------------------:|----------------------------:|------------------------------:|------------------------:|--------------------------:|------------------------:|------------------------------:|-------------------------:|-------------------------------------------:|------------------------:|:--------------------------|----------------------:|-----------------------:|-------------------:|
| TPEx         | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated |                      75 |                           0 |                              0 |                           3 |                            27 |                      20 |                        10 |                      36 |                             0 |                       57 |                                          0 |                    5488 | 松普                        |                   100 |                    100 |                100 |
| TWSE         | mainstream_overheated | non_mainstream_theme      | non_mainstream_overheated |                     195 |                           0 |                              0 |                           8 |                            40 |                      75 |                        32 |                      86 |                            42 |                      114 |                                          0 |                    6416 | 瑞祺電通                      |                   100 |                    100 |                100 |

## Status Rules

- theme_final_status is the daily flow/breadth state, not the structural mainstream definition.
- theme_structural_status=core_mainstream_theme only for core growth themes such as consumer electronics, semiconductors, passive components, PC/NB, AI server, PCB/CCL, networking/optical, power, thermal and connectors.
- Textile, financial, steel, shipping, construction, chemical, plastic and similar cyclical/traditional groups are non_mainstream_theme even when daily flow is strong.
- mainstream_leader/mainstream_follow_through/emerging_theme require core_mainstream_theme before entering the mainstream capital line.
- report_line_memberships can contain both mainstream and non_mainstream; dual identity stocks must be eligible for both report views without changing score.
- single_name_signal: stock-level signal only; keep it in individual/latent line.
- weak_theme: theme breadth or relative strength is weak.
- mainstream_overheated: theme is hot but risk/overheat/distribution is high.

