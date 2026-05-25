# Daily Candidate Regression: 2484

- stock_id: `2484`
- stock_name: `希華`
- status: `pass`
- raw_universe: `True`
- raw_history_rows: `136`
- first_trigger_date: `20260520`
- latest_breakout_detected: `True`

## Expected Regression Behavior

- 20260520-20260521 should trigger right-side base / platform watch before the limit-up breakout.
- 20260522 should trigger range-strength / neckline breakout context.
- 20260525 should trigger strict breakout with volume confirmation.

## Case Replay

|   case_date | breakout_type   |   score |   close |   volume_ratio | pattern_stage       |   neckline_price |   neckline_distance_pct | platform_right_side_flag   | neckline_breakout_flag   | platform_breakout_flag   | volume_confirmed_breakout   | false_breakout_risk   |
|------------:|:----------------|--------:|--------:|---------------:|:--------------------|-----------------:|------------------------:|:---------------------------|:-------------------------|:-------------------------|:----------------------------|:----------------------|
|    20260520 | pattern_watch   |      54 |   44.3  |           2.46 | platform_right_side |             47.6 |                   -6.93 | True                       | False                    | False                    | True                        | False                 |
|    20260521 | pattern_watch   |      54 |   44.85 |           3.49 | platform_right_side |             47.6 |                   -5.78 | True                       | False                    | False                    | True                        | False                 |
|    20260522 | range_rebound   |      69 |   49.3  |           2.76 | neckline_breakout   |             47.6 |                    3.57 | False                      | True                     | True                     | True                        | False                 |
|    20260525 | true_breakout   |      94 |   54.2  |           2.4  | breakout_confirmed  |             51.2 |                    5.86 | True                       | True                     | True                     | True                        | False                 |
