# TDCC Overheated Short-Term Edge

- generated_at: `2026-07-31 00:48:37 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260724-88f3a903b384007d`
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
| 20260724 | 8039 | 台虹 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.675324675324674 | 55.84415584415585 | 68 | 58.82 | 1.70 | 65 | 56.92 | 0.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260724 | 6414 | 樺漢 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.582278481012665 | 26.903553299492387 | 68 | 58.82 | 1.70 | 65 | 56.92 | 0.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260724 | 5227 | 立凱-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.525641025641036 | 33.00165837479272 | 40 | 62.50 | 0.06 | 37 | 54.05 | -1.46 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260724 | 6414 | 樺漢 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.582278481012665 | 26.903553299492387 | 40 | 62.50 | 0.06 | 37 | 54.05 | -1.46 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260724 | 3231 | 緯創 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.776978417266186 | 23.875432525951567 | 40 | 62.50 | 0.06 | 37 | 54.05 | -1.46 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260724 | 5227 | 立凱-KY | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 28.525641025641036 | 33.00165837479272 | 3 | 33.33 | -8.74 | 3 | 33.33 | -7.74 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 3 | 33.33 | -2.15 | -1.36 | -8.74 | 3 | 0.00 | -9.30 | -15.00 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 40 | 62.50 | 2.28 | 1.36 | 0.06 | 40 | 50.00 | 0.67 | -1.31 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 68 | 58.82 | 3.37 | 1.36 | 1.70 | 68 | 51.47 | 1.95 | 0.42 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 3 | 33.33 | -2.69 | -5.35 | -7.74 | 3 | 33.33 | -9.13 | -13.30 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 37 | 54.05 | -0.23 | 1.55 | -1.46 | 37 | 54.05 | 0.36 | -0.54 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 65 | 56.92 | 2.47 | 1.93 | 0.85 | 65 | 58.46 | 3.11 | 1.69 | ok_initial_sample |
