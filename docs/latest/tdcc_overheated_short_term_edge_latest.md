# TDCC Overheated Short-Term Edge

- generated_at: `2026-09-19 15:38:36 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260918-b805c742e5cccca5`
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
| 20260918 | 6620 | 漢達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.161290322580648 | 38.6046511627907 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 3605 | 宏致 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.71428571428571 | 30.508474576271194 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 4924 | 欣厚-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.0 | 29.707112970711314 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 1560 | 中砂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.417721518987346 | 28.920863309352505 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 6147 | 頎邦 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.519337016574585 | 25.479452054794514 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 3066 | 李洲 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.87931034482758 | 21.052631578947366 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 6620 | 漢達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.161290322580648 | 38.6046511627907 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 3605 | 宏致 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.71428571428571 | 30.508474576271194 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 4924 | 欣厚-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.0 | 29.707112970711314 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 1560 | 中砂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.417721518987346 | 28.920863309352505 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 6147 | 頎邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.519337016574585 | 25.479452054794514 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 2303 | 聯電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.032028469750887 | 19.999999999999996 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 3264 | 欣銓 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.485900216919735 | 18.281938325991188 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 6668 | 中揚光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.31806615776082 | 15.61032863849765 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 3105 | 穩懋 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.28571428571428 | 11.234705228031139 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 8103 | 瀚荃 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.601769911504414 | 5.714285714285716 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 6168 | 宏齊 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 31.918505942275054 | 33.734939759036145 | 10 | 50.00 | 3.82 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 6147 | 頎邦 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 26.519337016574585 | 25.479452054794514 | 10 | 50.00 | 3.82 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260918 | 3066 | 李洲 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 28.87931034482758 | 21.052631578947366 | 10 | 50.00 | 3.82 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 10 | 50.00 | 6.28 | -0.53 | 3.82 | 10 | 40.00 | 3.14 | 0.93 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 59 | 57.63 | 1.72 | 1.15 | 0.44 | 59 | 49.15 | 0.09 | -1.04 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 103 | 56.31 | 2.36 | 0.47 | 1.08 | 103 | 52.43 | 1.16 | -0.02 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 8 | 37.50 | 2.03 | -5.91 | -0.77 | 8 | 37.50 | -2.36 | -4.74 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 59 | 54.24 | -0.55 | 1.55 | -1.40 | 59 | 50.85 | -0.69 | -1.33 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 101 | 52.48 | 1.32 | 1.16 | 0.04 | 101 | 53.47 | 1.44 | 0.30 | ok_initial_sample |
