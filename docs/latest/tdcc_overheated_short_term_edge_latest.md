# TDCC Overheated Short-Term Edge

- generated_at: `2026-07-19 01:56:50 Asia/Taipei`
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
| 20260717 | 6907 | 雅特力-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.02564102564102 | 52.258064516129025 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8383 | 千附 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.690100430416067 | 41.49443561208268 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 3685 | 元創精密 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.739837398373975 | 31.88908145580587 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 4707 | 磐亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.724137931034484 | 31.06796116504855 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8039 | 台虹 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.0 | 30.067567567567565 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 4534 | 慶騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.10714285714286 | 22.287390029325515 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 1301 | 台塑 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.598540145985407 | 5.192629815745375 | 65 | 58.46 | 1.43 | 59 | 62.71 | 2.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8383 | 千附 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.690100430416067 | 41.49443561208268 | 37 | 62.16 | -0.53 | 32 | 62.50 | 0.12 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 3685 | 元創精密 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.739837398373975 | 31.88908145580587 | 37 | 62.16 | -0.53 | 32 | 62.50 | 0.12 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8039 | 台虹 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.0 | 30.067567567567565 | 37 | 62.16 | -0.53 | 32 | 62.50 | 0.12 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 4534 | 慶騰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.10714285714286 | 22.287390029325515 | 37 | 62.16 | -0.53 | 32 | 62.50 | 0.12 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 6 | 66.67 | 1.66 | 1.11 | -4.21 | 6 | 50.00 | -1.36 | -6.37 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 37 | 62.16 | 1.81 | 1.15 | -0.53 | 37 | 45.95 | -0.00 | -2.10 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 65 | 58.46 | 3.16 | 1.15 | 1.43 | 65 | 49.23 | 1.62 | 0.05 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 6 | 66.67 | 6.53 | 6.51 | 2.28 | 6 | 66.67 | 0.18 | -3.21 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 32 | 62.50 | 2.98 | 1.97 | 0.12 | 32 | 62.50 | 4.22 | 1.70 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 59 | 62.71 | 5.12 | 1.99 | 2.40 | 59 | 64.41 | 6.21 | 3.68 | ok_initial_sample |
