# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-06 16:56:46 Asia/Taipei`
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
| 20260605 | 6207 | 雷科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.596412556053806 | 60.734149054505004 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 4939 | 亞電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.217821782178234 | 50.948166877370426 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 4534 | 慶騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.553191489361698 | 36.701030927835056 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 3615 | 安可 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.482197355035606 | 26.603575184016837 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 8043 | 蜜望實 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.120567375886516 | 22.222222222222232 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 6126 | 信音 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.718309859154925 | 18.055555555555557 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 4534 | 慶騰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.553191489361698 | 36.701030927835056 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260605 | 3615 | 安可 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.482197355035606 | 26.603575184016837 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -3.38 | -3.38 | -9.21 | 2 | 0.00 | -13.08 | -17.92 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22 | 72.73 | 4.18 | 1.99 | 0.90 | 22 | 50.00 | 1.16 | -1.62 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 38 | 73.68 | 5.68 | 2.43 | 3.01 | 38 | 57.89 | 3.58 | 1.26 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -5.91 | -5.91 | -12.54 | 2 | 0.00 | -14.51 | -20.14 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15 | 73.33 | 6.84 | 8.75 | 1.42 | 15 | 73.33 | 6.21 | 1.65 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25 | 84.00 | 14.99 | 13.17 | 9.02 | 25 | 88.00 | 14.45 | 9.01 | insufficient_sample |
