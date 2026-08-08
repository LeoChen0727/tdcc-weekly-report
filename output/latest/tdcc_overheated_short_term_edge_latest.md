# TDCC Overheated Short-Term Edge

- generated_at: `2026-08-08 15:46:44 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260807-01698d0b1c2355ac`
- tuning_status: `not_ready`
- allowed_changes: `reporting_priority_only`
- forbidden_changes: `core_weight_change`

## Calculation Method

- close-to-close win rate: `dN_return_pct > 0`, from signal close to D+N close, only mature_dN=True rows.
- close-to-close relative return: stock D+N return minus TWSE/TPEx benchmark D+N return.
- next-open return: next trading day's open to D+N close.
- next-open relative return: stock next-open return minus benchmark next-open return when benchmark OHLC is available.
- pending rows are not counted as success or failure.
- These rules are a short-term reporting specialty, not a core TDCC/ABM weight change.

## Current Matching Stocks

| signal_date | stock_id | stock_name | theme | rule_name_zh | price_ret_1w | price_ret_2w | d5_mature_count | d5_win_rate_pct | d5_avg_relative_return_pct | d10_mature_count | d10_win_rate_pct | d10_avg_relative_return_pct | sample_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260807 | 3489 | 森寶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.855721393034806 | 35.60209424083769 | 70 | 57.14 | 1.02 | 68 | 54.41 | 0.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260807 | 8271 | 宇瞻 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.078431372549012 | 17.619047619047624 | 70 | 57.14 | 1.02 | 68 | 54.41 | 0.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260807 | 3489 | 森寶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.855721393034806 | 35.60209424083769 | 43 | 58.14 | -0.37 | 40 | 50.00 | -2.49 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260807 | 3006 | 晶豪科 | memory | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 57.31707317073172 | 21.41176470588235 | 4 | 25.00 | -6.64 | 3 | 33.33 | -7.74 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 4 | 25.00 | -3.67 | -3.38 | -6.64 | 4 | 0.00 | -9.21 | -11.49 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 43 | 58.14 | 1.45 | 0.42 | -0.37 | 43 | 46.51 | -0.11 | -1.71 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 70 | 57.14 | 2.61 | 0.78 | 1.02 | 70 | 50.00 | 1.23 | -0.22 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 3 | 33.33 | -2.69 | -5.35 | -7.74 | 3 | 33.33 | -9.13 | -13.30 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 40 | 50.00 | -1.74 | 0.15 | -2.49 | 40 | 50.00 | -1.13 | -1.58 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 68 | 54.41 | 1.46 | 1.61 | 0.14 | 68 | 55.88 | 2.11 | 0.98 | ok_initial_sample |
