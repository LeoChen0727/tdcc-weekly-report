# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-03 17:02:58 Asia/Taipei`
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
| 20260529 | 2375 | 凱美 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.7918215613383 | 67.50503018108651 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2495 | 普安 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.515837104072382 | 46.514935988620195 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.141987829614596 | 45.576407506702424 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6127 | 九豪 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.19047619047619 | 44.886975242195895 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6284 | 佳邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.58536585365853 | 41.420118343195256 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2312 | 金寶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.673716012084604 | 39.85637342908439 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6175 | 立敦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.647791619479047 | 39.377537212449255 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2369 | 菱生 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.741029641185655 | 35.69023569023568 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6706 | 惠特 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.081081081081079 | 29.65299684542586 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4906 | 正文 | networking | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.325062034739474 | 26.947637292464897 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6265 | 方土昶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.760914760914767 | 22.66666666666668 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2344 | 華邦電 | memory | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.400000000000002 | 22.00772200772201 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8028 | 昇陽半導體 | semiconductor equipment/materials | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.22448979591837 | 13.73913043478261 | 25 | 76.00 | 3.88 | 25 | 84.00 | 11.75 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2495 | 普安 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.515837104072382 | 46.514935988620195 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.141987829614596 | 45.576407506702424 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6127 | 九豪 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.19047619047619 | 44.886975242195895 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2312 | 金寶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.673716012084604 | 39.85637342908439 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2369 | 菱生 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.741029641185655 | 35.69023569023568 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4906 | 正文 | networking | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.325062034739474 | 26.947637292464897 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2344 | 華邦電 | memory | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.400000000000002 | 22.00772200772201 | 15 | 66.67 | -0.55 | 15 | 73.33 | 0.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -3.38 | -3.38 | -9.21 | 2 | 0.00 | -13.08 | -17.92 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15 | 66.67 | 4.15 | 1.15 | -0.55 | 15 | 66.67 | 3.57 | -0.51 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25 | 76.00 | 8.11 | 2.33 | 3.88 | 25 | 76.00 | 7.44 | 3.61 | insufficient_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -5.91 | -5.91 |  | 0 |  |  |  | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15 | 73.33 | 6.84 | 8.75 | 0.97 | 4 | 100.00 | 10.24 | 1.82 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25 | 84.00 | 14.99 | 13.17 | 11.75 | 11 | 100.00 | 23.73 | 15.25 | insufficient_sample |
