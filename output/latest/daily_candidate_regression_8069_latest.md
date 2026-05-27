# Daily Candidate Regression: 8069

- stock_id: `8069`
- stock_name: `元太`
- status: `pass`
- raw_universe: `True`
- raw_history_rows: `137`
- first_early_entry_date: `20260507`
- first_neckline_challenge_date: `20260508`
- first_strict_breakout_date: `20260512`

## Expected Regression Behavior

- 20260507 should detect W-bottom / right-side style early watch before the strongest breakout.
- 20260508 should detect neckline challenge / range rebound with volume confirmation.
- 20260512 should detect strict 60-day volume-confirmed breakout.
- Later high-zone rows should be interpreted as post-surge context, not pre-move accumulation.

## Case Replay

|   case_date | breakout_type   |   score |   close |   volume_ratio | pattern_stage      |   neckline_price |   neckline_distance_pct | w_bottom_flag   | w_bottom_right_side_flag   | early_entry_watch_flag   | right_side_follow_through_flag   | neckline_challenge_flag   | neckline_breakout_flag   | platform_breakout_flag   | volume_confirmed_breakout   | false_breakout_risk   |
|------------:|:----------------|--------:|--------:|---------------:|:-------------------|-----------------:|------------------------:|:----------------|:---------------------------|:-------------------------|:---------------------------------|:--------------------------|:-------------------------|:-------------------------|:----------------------------|:----------------------|
|    20260505 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260506 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260507 | pattern_watch   |      54 |   153   |           1.96 | early_entry_watch  |            163.5 |                   -6.42 | False           | False                      | True                     | False                            | False                     | False                    | False                    | True                        | False                 |
|    20260508 | range_rebound   |      69 |   162   |           2.72 | neckline_challenge |            162.5 |                   -0.31 | False           | False                      | False                    | True                             | True                      | False                    | False                    | True                        | False                 |
|    20260511 | pattern_watch   |      54 |   178   |           0.61 | base_building      |            165   |                    7.88 | True            | False                      | False                    | False                            | False                     | False                    | False                    | False                       | False                 |
|    20260512 | true_breakout   |      89 |   195.5 |           5.5  | breakout_confirmed |            193.5 |                    1.03 | True            | False                      | False                    | False                            | False                     | True                     | True                     | True                        | False                 |
|    20260513 | true_breakout   |      94 |   215   |           2.96 | breakout_confirmed |            195.5 |                    9.97 | True            | True                       | False                    | False                            | False                     | True                     | True                     | True                        | False                 |
|    20260514 | true_breakout   |      89 |   226   |           3.4  | platform_breakout  |            215   |                    5.12 | True            | True                       | False                    | False                            | False                     | True                     | True                     | True                        | False                 |
|    20260515 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260518 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260519 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260520 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260521 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260522 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260525 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
|    20260526 |                 |         |         |                |                    |                  |                         |                 |                            |                          |                                  |                           |                          |                          |                             |                       |
