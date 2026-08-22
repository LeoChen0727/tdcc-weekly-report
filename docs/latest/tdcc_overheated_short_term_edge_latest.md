# TDCC Overheated Short-Term Edge

- generated_at: `2026-08-22 15:47:28 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260821-d1df4c843f691346`
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
| 20260821 | 3498 | 陽程 | semiconductor equipment/materials | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.518987341772156 | 64.8068669527897 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 3234 | 光環 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.62271062271063 | 40.46511627906977 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 6108 | 競國 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.42081447963799 | 37.301587301587304 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 3508 | 位速 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.519480519480517 | 35.67251461988303 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 6141 | 柏承 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.714285714285715 | 33.137829912023456 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 2851 | 中再保 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.548387096774203 | 32.86318758815232 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 1815 | 富喬 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.404371584699454 | 30.38416763678695 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 3441 | 聯一光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.684964200477324 | 26.777251184834117 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 2609 | 陽明 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.031007751937985 | 26.732673267326735 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 2611 | 志信 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.050167224080258 | 23.297491039426532 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 3653 | 健策 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.122554067971159 | 23.17351598173516 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 2426 | 鼎元 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.42342342342343 | 21.238938053097357 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 6426 | 統新 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.045662100456632 | 17.27493917274938 | 79 | 55.70 | 0.79 | 72 | 51.39 | -0.25 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 6141 | 柏承 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.714285714285715 | 33.137829912023456 | 49 | 57.14 | -0.22 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 1815 | 富喬 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.404371584699454 | 30.38416763678695 | 49 | 57.14 | -0.22 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 3441 | 聯一光 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.684964200477324 | 26.777251184834117 | 49 | 57.14 | -0.22 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 2611 | 志信 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.050167224080258 | 23.297491039426532 | 49 | 57.14 | -0.22 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 2426 | 鼎元 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.42342342342343 | 21.238938053097357 | 49 | 57.14 | -0.22 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260821 | 3441 | 聯一光 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 27.684964200477324 | 26.777251184834117 | 6 | 33.33 | -1.53 | 5 | 40.00 | -2.26 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 6 | 33.33 | 0.83 | -2.54 | -1.53 | 6 | 16.67 | -4.08 | -5.86 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 49 | 57.14 | 1.13 | 0.42 | -0.22 | 49 | 46.94 | -0.46 | -1.62 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 79 | 55.70 | 2.09 | 0.37 | 0.79 | 79 | 49.37 | 0.72 | -0.43 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 5 | 40.00 | 1.57 | -5.35 | -2.26 | 5 | 40.00 | -4.60 | -7.74 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 43 | 48.84 | -2.05 | -0.87 | -2.85 | 43 | 48.84 | -1.55 | -2.07 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 72 | 51.39 | 1.07 | 1.22 | -0.25 | 72 | 54.17 | 1.68 | 0.54 | ok_initial_sample |
