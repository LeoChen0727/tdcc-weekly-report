# W-Bottom Candidate Quality Audit

- generated_at: `2026-06-24 22:37:19 Asia/Taipei`
- model_id: `w_bottom_right_side`
- source_research_id: `w_bottom_tdcc_abc_backtest`
- rows: `470` dedup candidates
- advisory_status: `warning_research_variant_only`
- production impact: `none`; this artifact does not update production model conditions, scoring, ranking, or baseline.
- TDCC handling: TDCC is intentionally not used as a W observation-stage quality gate in this audit.

## Headline Counts

| metric | strict_symmetry_1_5 | loose_symmetry_2_0 |
| --- | ---: | ---: |
| W shape completed or already near neckline | 216 (45.96%) | 231 (49.15%) |
| Neckline volume breakout confirmed | 56 (11.91%) | 73 (15.53%) |
| Already near neckline at signal, without later volume breakout | 77 (16.38%) | - |

## Strict Symmetry 1.5 Quality Buckets

| bucket | count |
| --- | --- |
| right_low_broken_before_completion | 88 |
| completed_without_volume_breakout | 83 |
| already_near_neckline_at_signal | 77 |
| neckline_volume_breakout | 56 |
| right_low_broken_after_deadline | 40 |
| no_completion_within_symmetry | 38 |
| late_volume_breakout_not_w | 30 |
| future_window_incomplete | 30 |
| late_neckline_completion_not_w | 28 |

## Loose Symmetry 2.0 Quality Buckets

| bucket | count |
| --- | --- |
| right_low_broken_before_completion | 102 |
| completed_without_volume_breakout | 87 |
| neckline_volume_breakout | 73 |
| already_near_neckline_at_signal | 71 |
| future_window_incomplete | 37 |
| no_completion_within_symmetry | 31 |
| right_low_broken_after_deadline | 26 |
| late_neckline_completion_not_w | 23 |
| late_volume_breakout_not_w | 20 |

## Primary Review Flags

| bucket | count |
| --- | --- |
| right_low_failed | 128 |
| shape_completed_but_volume_missing | 83 |
| candidate_selected_too_near_neckline | 77 |
| did_not_complete_w | 68 |
| completion_too_late_for_w | 58 |
| passed_volume_breakout_confirmation | 56 |

## Candidate Examples Needing Review

| stock_id | signal_date | signal_distance_to_neckline_pct | signal_rebound_from_right_low_pct | sym1_5_quality_bucket | primary_review_flag |
| --- | --- | --- | --- | --- | --- |
| 1102 | 20260105 | -4.0609 | 4.1322 | right_low_broken_before_completion | right_low_failed |
| 2033 | 20260105 | -29.6214 | 3.268 | no_completion_within_symmetry | did_not_complete_w |
| 2305 | 20260105 | -4.8673 | 5.9113 | late_volume_breakout_not_w | completion_too_late_for_w |
| 2504 | 20260105 | -0.1342 | 7.0504 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |
| 2615 | 20260105 | -10.2975 | 3.4301 | right_low_broken_after_deadline | right_low_failed |
| 6409 | 20260105 | -19.2157 | 11.1111 | right_low_broken_before_completion | right_low_failed |
| 2347 | 20260106 | -14.1854 | 4.8027 | late_volume_breakout_not_w | completion_too_late_for_w |
| 3617 | 20260106 | -19.2678 | 3.202 | right_low_broken_before_completion | right_low_failed |
| 4562 | 20260106 | -10.4215 | 9.1298 | late_neckline_completion_not_w | completion_too_late_for_w |
| 2027 | 20260107 | -4.2146 | 8.0692 | late_volume_breakout_not_w | completion_too_late_for_w |
| 2359 | 20260107 | -9.1837 | 7.2289 | late_neckline_completion_not_w | completion_too_late_for_w |
| 3062 | 20260107 | -19.0476 | 3.0303 | late_volume_breakout_not_w | completion_too_late_for_w |
| 4938 | 20260107 | -12.782 | 3.1111 | late_neckline_completion_not_w | completion_too_late_for_w |
| 6994 | 20260107 | -10.566 | 3.9474 | right_low_broken_after_deadline | right_low_failed |
| 1906 | 20260108 | -7.0039 | 3.0172 | right_low_broken_after_deadline | right_low_failed |
| 2017 | 20260108 | -0.6623 | 8.0432 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |
| 4961 | 20260108 | -1.9868 | 10.0372 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |
| 5871 | 20260108 | -5.7778 | 3.4146 | right_low_broken_before_completion | right_low_failed |
| 6176 | 20260108 | -7.8947 | 3.3755 | late_volume_breakout_not_w | completion_too_late_for_w |
| 6414 | 20260108 | -3.3223 | 4.3011 | late_neckline_completion_not_w | completion_too_late_for_w |
| 6592 | 20260108 | -5.7187 | 4.2735 | right_low_broken_after_deadline | right_low_failed |
| 8374 | 20260108 | -7.0961 | 12.4174 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |
| 3022 | 20260109 | -6.867 | 3.3333 | right_low_broken_before_completion | right_low_failed |
| 3714 | 20260109 | 0.2869 | 10.2524 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |
| 1310 | 20260112 | -12.3246 | 4.7904 | late_volume_breakout_not_w | completion_too_late_for_w |
| 8222 | 20260112 | -0.3401 | 10.1504 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |
| 8454 | 20260112 | -5.8824 | 3.2258 | right_low_broken_after_deadline | right_low_failed |
| 1454 | 20260113 | -5.1471 | 3.2 | late_volume_breakout_not_w | completion_too_late_for_w |
| 4737 | 20260113 | -10.8197 | 3.4221 | right_low_broken_after_deadline | right_low_failed |
| 8215 | 20260113 | -0.2469 | 10.6849 | already_near_neckline_at_signal | candidate_selected_too_near_neckline |

## Reading Notes

- `already_near_neckline_at_signal` means the candidate was already in the neckline completion zone on the signal date, so it may be too late for a right-side early-entry model.
- `completed_without_volume_breakout` means price reached the neckline zone within the symmetry window, but did not satisfy the volume-breakout confirmation rule.
- `late_*_not_w` means the move happened after the symmetry window, so it is treated as a later breakout rather than a clean W-bottom completion.
