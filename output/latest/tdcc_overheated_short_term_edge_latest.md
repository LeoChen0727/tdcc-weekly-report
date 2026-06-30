# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-30 22:19:29 Asia/Taipei`
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
| 20260626 | 5328 | 華容 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.247787610619476 | 62.5 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 8261 | 富鼎 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.488372093023248 | 54.43037974683544 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 2316 | 楠梓電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.922141119221408 | 49.8371335504886 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 5011 | 久陽 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.981481481481467 | 42.77777777777778 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6213 | 聯茂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.750000000000004 | 39.71774193548387 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 8046 | 南電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.718535469107543 | 39.40520446096654 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6672 | 騰輝電子-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.94093686354379 | 36.76814988290398 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 1718 | 中纖 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.083164300202842 | 23.20441988950275 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6270 | 倍微 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.62162162162162 | 21.448863636363626 | 188 | 50.53 | 2.80 | 166 | 66.87 | 4.80 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 2316 | 楠梓電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.922141119221408 | 49.8371335504886 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 4716 | 大立 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.315068493150687 | 43.03030303030304 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 5011 | 久陽 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.981481481481467 | 42.77777777777778 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6243 | 迅杰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.209169054441258 | 42.62023217247099 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6213 | 聯茂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.750000000000004 | 39.71774193548387 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 8046 | 南電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.718535469107543 | 39.40520446096654 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 4707 | 磐亞 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.782608695652183 | 38.790931989924424 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6672 | 騰輝電子-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.94093686354379 | 36.76814988290398 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 1515 | 力山 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.76061776061777 | 33.1877729257642 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 7795 | 長廣 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.317073170731717 | 31.571428571428562 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 1718 | 中纖 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.083164300202842 | 23.20441988950275 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260626 | 6270 | 倍微 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.62162162162162 | 21.448863636363626 | 179 | 50.84 | 1.64 | 160 | 63.75 | 3.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 49 | 42.86 | 0.92 | -2.03 | 0.56 | 49 | 36.73 | -0.66 | -0.81 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 179 | 50.84 | 2.62 | 0.37 | 1.64 | 179 | 49.16 | 1.22 | 0.43 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 188 | 50.53 | 3.59 | 0.23 | 2.80 | 188 | 47.87 | 2.08 | 1.44 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 44 | 59.09 | 7.64 | 4.64 | 4.99 | 44 | 61.36 | 6.43 | 3.94 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 160 | 63.75 | 5.67 | 4.34 | 3.42 | 160 | 57.50 | 4.46 | 2.33 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 166 | 66.87 | 7.21 | 4.76 | 4.80 | 166 | 60.24 | 5.94 | 3.61 | ok_initial_sample |
