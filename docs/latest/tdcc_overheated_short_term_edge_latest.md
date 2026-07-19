# TDCC Overheated Short-Term Edge

- generated_at: `2026-07-19 10:49:20 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260717-98c564c5bc4ab725`
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
| 20260717 | 8383 | 千附 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.690100430416067 | 41.49443561208268 | 226 | 50.44 | 2.53 | 197 | 62.94 | 3.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 3685 | 元創精密 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.739837398373975 | 31.88908145580587 | 226 | 50.44 | 2.53 | 197 | 62.94 | 3.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 4707 | 磐亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.724137931034484 | 31.06796116504855 | 226 | 50.44 | 2.53 | 197 | 62.94 | 3.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8039 | 台虹 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.0 | 30.067567567567565 | 226 | 50.44 | 2.53 | 197 | 62.94 | 3.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 4534 | 慶騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.10714285714286 | 22.287390029325515 | 226 | 50.44 | 2.53 | 197 | 62.94 | 3.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 1301 | 台塑 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.598540145985407 | 5.192629815745375 | 226 | 50.44 | 2.53 | 197 | 62.94 | 3.97 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8383 | 千附 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.690100430416067 | 41.49443561208268 | 216 | 48.15 | 1.28 | 191 | 60.21 | 2.98 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 3685 | 元創精密 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.739837398373975 | 31.88908145580587 | 216 | 48.15 | 1.28 | 191 | 60.21 | 2.98 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 6957 | 裕慶-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.66109785202863 | 31.117021276595747 | 216 | 48.15 | 1.28 | 191 | 60.21 | 2.98 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 8039 | 台虹 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.0 | 30.067567567567565 | 216 | 48.15 | 1.28 | 191 | 60.21 | 2.98 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260717 | 4534 | 慶騰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.10714285714286 | 22.287390029325515 | 216 | 48.15 | 1.28 | 191 | 60.21 | 2.98 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 51 | 43.14 | 1.22 | -2.03 | 0.54 | 51 | 37.25 | -0.23 | -0.85 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 216 | 48.15 | 1.90 | -0.26 | 1.28 | 216 | 45.37 | 0.25 | -0.19 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 226 | 50.44 | 2.89 | 0.23 | 2.53 | 226 | 46.02 | 1.09 | 0.85 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 49 | 59.18 | 6.89 | 5.53 | 4.54 | 49 | 59.18 | 5.45 | 3.29 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 191 | 60.21 | 4.98 | 3.57 | 2.98 | 191 | 53.93 | 3.74 | 1.90 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 197 | 62.94 | 6.11 | 3.75 | 3.97 | 197 | 55.33 | 4.71 | 2.70 | ok_initial_sample |
