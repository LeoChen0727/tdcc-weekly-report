# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-13 18:27:29 Asia/Taipei`
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
| 20260612 | 4973 | 廣穎 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.0447284345048 | 50.98814229249011 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2478 | 大毅 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.930069930069937 | 44.11764705882353 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2491 | 吉祥全 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.190053285968027 | 40.04474272930649 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 9910 | 豐泰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.32911392405063 | 36.14814814814815 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 3026 | 禾伸堂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.538461538461547 | 34.03508771929824 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6409 | 旭隼 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.336927223719673 | 33.62068965517242 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6270 | 倍微 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.41652323580034 | 28.11918063314711 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2887 | 台新新光金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.708812260536398 | 27.966101694915245 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 4534 | 慶騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.222222222222232 | 24.06015037593985 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6173 | 信昌電 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.43844492440605 | 23.4375 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 1904 | 正隆 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.214463840398995 | 21.164021164021165 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2882 | 國泰金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.668161434977577 | 20.938628158844775 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6449 | 鈺邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.172043010752699 | 19.60227272727273 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.51637764932564 | 19.107142857142854 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2413 | 環科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.821763602251426 | 18.83495145631069 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 3236 | 千如 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.909090909090917 | 8.59106529209621 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 8121 | 越峰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.580645161290317 | 6.987951807228909 | 38 | 73.68 | 3.01 | 25 | 84.00 | 9.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 9910 | 豐泰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.32911392405063 | 36.14814814814815 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 3026 | 禾伸堂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.538461538461547 | 34.03508771929824 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6409 | 旭隼 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.336927223719673 | 33.62068965517242 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6270 | 倍微 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.41652323580034 | 28.11918063314711 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 2887 | 台新新光金 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.708812260536398 | 27.966101694915245 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 3296 | 勝德 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.3972286374134 | 26.633165829145746 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 4534 | 慶騰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.222222222222232 | 24.06015037593985 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260612 | 6173 | 信昌電 | passive components | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.43844492440605 | 23.4375 | 22 | 72.73 | 0.90 | 15 | 73.33 | 1.42 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

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
