# TDCC Overheated Short-Term Edge

- generated_at: `2026-09-26 15:35:31 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260924-db6f7ba61c9bf627`
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
| 20260924 | 6168 | 宏齊 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.46958981612446 | 47.65100671140938 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 6715 | 嘉基 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.90862944162437 | 39.227340267459134 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 2033 | 佳大 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.286871961102104 | 33.33333333333333 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 1569 | 濱川 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.423076923076927 | 32.446264073695 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 4956 | 光鋐 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 14.83870967741936 | 31.656804733727828 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 2030 | 彰源 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.361702127659562 | 28.541226215644834 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 3691 | 碩禾 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.502634351949418 | 24.357656731757448 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 4174 | 浩鼎 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.93693693693694 | 24.09177820267687 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 3624 | 光頡 | passive components | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.644067796610166 | 23.348017621145377 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 8150 | 南茂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.181084198385232 | 23.2123212321232 | 59 | 57.63 | 0.44 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 6168 | 宏齊 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.46958981612446 | 47.65100671140938 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 6945 | 圓祥生技 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.290322580645151 | 40.10152284263959 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 6715 | 嘉基 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.90862944162437 | 39.227340267459134 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 2033 | 佳大 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.286871961102104 | 33.33333333333333 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 1569 | 濱川 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.423076923076927 | 32.446264073695 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 3094 | 聯傑 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.531914893617005 | 29.594272076372306 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 2030 | 彰源 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.361702127659562 | 28.541226215644834 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 4924 | 欣厚-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.982456140350894 | 24.8062015503876 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 4174 | 浩鼎 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.93693693693694 | 24.09177820267687 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 3624 | 光頡 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.644067796610166 | 23.348017621145377 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 8150 | 南茂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.181084198385232 | 23.2123212321232 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 2454 | 聯發科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.44444444444444 | 11.970338983050844 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 2409 | 友達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.000000000000012 | 9.615384615384626 | 103 | 56.31 | 1.08 | 101 | 52.48 | 0.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 3016 | 嘉晶 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 38.52813852813852 | 45.45454545454546 | 10 | 50.00 | 3.82 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 3624 | 光頡 | passive components | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 18.644067796610166 | 23.348017621145377 | 10 | 50.00 | 3.82 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260924 | 8150 | 南茂 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 29.181084198385232 | 23.2123212321232 | 10 | 50.00 | 3.82 | 8 | 37.50 | -0.77 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

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
