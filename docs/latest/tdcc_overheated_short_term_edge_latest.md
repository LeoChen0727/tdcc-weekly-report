# TDCC Overheated Short-Term Edge

- generated_at: `2026-09-12 15:32:48 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260911-3ac576b2856cc687`
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
| 20260911 | 6173 | 信昌電 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.324376199616125 | 21.338912133891206 | 101 | 55.45 | 0.87 | 96 | 51.04 | -0.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260911 | 2338 | 光罩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.70466321243523 | 19.375000000000007 | 101 | 55.45 | 0.87 | 96 | 51.04 | -0.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260911 | 6179 | 亞通 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.777027027027017 | 17.59868421052633 | 101 | 55.45 | 0.87 | 96 | 51.04 | -0.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260911 | 6426 | 統新 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.059369202226344 | 14.61100569259961 | 101 | 55.45 | 0.87 | 96 | 51.04 | -0.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260911 | 2305 | 全友 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 33.06320907617501 | 41.551724137931025 | 8 | 37.50 | 0.06 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260911 | 3624 | 光頡 | passive components | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 33.583690987124456 | 35.62091503267975 | 8 | 37.50 | 0.06 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260911 | 7610 | 聯友金屬-創 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 8.516483516483508 | 32.10702341137124 | 8 | 37.50 | 0.06 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 8 | 37.50 | 2.32 | -2.54 | 0.06 | 8 | 25.00 | -2.13 | -3.96 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 59 | 57.63 | 1.72 | 1.15 | 0.44 | 59 | 49.15 | 0.09 | -1.04 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 101 | 55.45 | 2.12 | 0.42 | 0.87 | 101 | 51.49 | 0.85 | -0.27 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 8 | 37.50 | 2.03 | -5.91 | -0.77 | 8 | 37.50 | -2.36 | -4.74 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 57 | 52.63 | -0.72 | 1.16 | -1.53 | 57 | 50.88 | -0.80 | -1.41 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 96 | 51.04 | 1.23 | 1.04 | -0.02 | 96 | 53.12 | 1.43 | 0.31 | ok_initial_sample |
