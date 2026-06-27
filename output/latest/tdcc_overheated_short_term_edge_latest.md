# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-28 02:40:39 Asia/Taipei`
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
| 20260626 | 5328 | 華容 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.247787610619476 | 62.5 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 8261 | 富鼎 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.488372093023248 | 54.43037974683544 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 2316 | 楠梓電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.922141119221408 | 49.8371335504886 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 5011 | 久陽 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.981481481481467 | 42.77777777777778 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6213 | 聯茂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.750000000000004 | 39.71774193548387 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 8046 | 南電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.718535469107543 | 39.40520446096654 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6672 | 騰輝電子-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.94093686354379 | 36.76814988290398 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 1718 | 中纖 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.083164300202842 | 23.20441988950275 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6270 | 倍微 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.62162162162162 | 21.448863636363626 | 55 | 61.82 | 2.01 | 44 | 65.91 | 4.04 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 2316 | 楠梓電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.922141119221408 | 49.8371335504886 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 5011 | 久陽 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.981481481481467 | 42.77777777777778 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6213 | 聯茂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.750000000000004 | 39.71774193548387 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 8046 | 南電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.718535469107543 | 39.40520446096654 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6672 | 騰輝電子-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.94093686354379 | 36.76814988290398 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 1515 | 力山 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.76061776061777 | 33.1877729257642 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 7795 | 長廣 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.317073170731717 | 31.571428571428562 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 1718 | 中纖 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.083164300202842 | 23.20441988950275 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6270 | 倍微 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.62162162162162 | 21.448863636363626 | 29 | 68.97 | 0.62 | 25 | 64.00 | 0.59 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 3 | 33.33 | -2.15 | -1.36 | -8.74 | 3 | 0.00 | -9.30 | -15.00 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29 | 68.97 | 3.53 | 1.88 | 0.62 | 29 | 51.72 | 2.06 | -0.58 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 55 | 61.82 | 3.97 | 1.88 | 2.01 | 55 | 52.73 | 2.79 | 0.98 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -5.91 | -5.91 | -12.54 | 2 | 0.00 | -14.51 | -20.14 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25 | 64.00 | 3.95 | 1.96 | 0.59 | 25 | 68.00 | 5.95 | 2.92 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 44 | 65.91 | 7.40 | 4.33 | 4.04 | 44 | 75.00 | 9.70 | 6.42 | ok_initial_sample |
