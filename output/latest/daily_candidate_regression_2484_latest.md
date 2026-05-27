# Daily Candidate Regression: 2484

- stock_id: `2484`
- stock_name: `希華`
- status: `pass`
- raw_universe: `True`
- raw_history_rows: `137`
- first_entry_zone_date: `20260511`
- first_early_entry_date: `20260518`
- first_attack_date: `20260520`
- latest_breakout_detected: `True`

## Expected Regression Behavior

- 20260511-20260514 should mark the pullback entry-zone context after the prior impulse.
- 20260518-20260519 should trigger early-entry / right-side watch before the platform breakout.
- 20260520-20260521 should trigger high-emphasis range-strength / right-side attack before the limit-up breakout.
- 20260522 should trigger range-strength / neckline breakout context.
- 20260525 should trigger strict breakout with volume confirmation.

## Case Replay

|   case_date | breakout_type   |   score |   close |   volume_ratio | pattern_stage       |   neckline_price |   neckline_distance_pct | pullback_entry_zone_flag   | early_entry_watch_flag   | right_side_follow_through_flag   | platform_right_side_flag   | neckline_breakout_flag   | platform_breakout_flag   | volume_confirmed_breakout   | false_breakout_risk   |
|------------:|:----------------|--------:|--------:|---------------:|:--------------------|-----------------:|------------------------:|:---------------------------|:-------------------------|:---------------------------------|:---------------------------|:-------------------------|:-------------------------|:----------------------------|:----------------------|
|    20260511 | pattern_watch   |      43 |   39.6  |           0.65 | pullback_entry_zone |             47.6 |                  -16.81 | True                       | False                    | False                            | False                      | False                    | False                    | False                       | False                 |
|    20260512 | pattern_watch   |      35 |   38.9  |           0.59 | pullback_entry_zone |             47.6 |                  -18.28 | True                       | False                    | False                            | False                      | False                    | False                    | False                       | False                 |
|    20260513 | pattern_watch   |      35 |   37.9  |           0.52 | pullback_entry_zone |             47.6 |                  -20.38 | True                       | False                    | False                            | False                      | False                    | False                    | False                       | False                 |
|    20260514 | pattern_watch   |      40 |   38.3  |           0.61 | pullback_entry_zone |             47.6 |                  -19.54 | True                       | False                    | False                            | False                      | False                    | False                    | False                       | False                 |
|    20260515 |                 |         |         |                |                     |                  |                         |                            |                          |                                  |                            |                          |                          |                             |                       |
|    20260518 | pattern_watch   |      54 |   41    |           1.44 | early_entry_watch   |             47.6 |                  -13.87 | False                      | True                     | False                            | False                      | False                    | False                    | False                       | False                 |
|    20260519 | pattern_watch   |      54 |   40.3  |           1.76 | early_entry_watch   |             47.6 |                  -15.34 | False                      | True                     | False                            | False                      | False                    | False                    | True                        | False                 |
|    20260520 | range_rebound   |      69 |   44.3  |           2.46 | platform_right_side |             47.6 |                   -6.93 | False                      | False                    | True                             | True                       | False                    | False                    | True                        | False                 |
|    20260521 | range_rebound   |      69 |   44.85 |           3.49 | platform_right_side |             47.6 |                   -5.78 | False                      | False                    | True                             | True                       | False                    | False                    | True                        | False                 |
|    20260522 | range_rebound   |      69 |   49.3  |           2.76 | neckline_breakout   |             47.6 |                    3.57 | False                      | False                    | True                             | False                      | True                     | True                     | True                        | False                 |
|    20260525 | true_breakout   |      94 |   54.2  |           2.4  | breakout_confirmed  |             51.2 |                    5.86 | False                      | False                    | False                            | True                       | True                     | True                     | True                        | False                 |
