# TDCC Overheated Short-Term Edge

- generated_at: `2026-09-05 15:36:48 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260904-ef2f08472cf64a89`
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
| 20260904 | 6620 | 漢達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.21893491124261 | 43.333333333333336 | 57 | 57.89 | 0.32 | 52 | 51.92 | -1.26 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 3374 | 精材 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.398963730569944 | 40.293637846655784 | 57 | 57.89 | 0.32 | 52 | 51.92 | -1.26 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 7711 | 永擎 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.774127310061594 | 36.94474539544963 | 57 | 57.89 | 0.32 | 52 | 51.92 | -1.26 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 3094 | 聯傑 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.970588235294134 | 30.069930069930063 | 57 | 57.89 | 0.32 | 52 | 51.92 | -1.26 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 2455 | 全新 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.658986175115214 | 30.04926108374384 | 57 | 57.89 | 0.32 | 52 | 51.92 | -1.26 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 3406 | 玉晶光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.049073064340245 | 61.80981595092025 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 4908 | 前鼎 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.157894736842106 | 46.73202614379084 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 6620 | 漢達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.21893491124261 | 43.333333333333336 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 3374 | 精材 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.398963730569944 | 40.293637846655784 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 7711 | 永擎 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.774127310061594 | 36.94474539544963 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 8103 | 瀚荃 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.903225806451623 | 30.319148936170205 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 3094 | 聯傑 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.970588235294134 | 30.069930069930063 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260904 | 2455 | 全新 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.658986175115214 | 30.04926108374384 | 96 | 55.21 | 0.82 | 87 | 51.72 | 0.37 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 8 | 37.50 | 2.32 | -2.54 | 0.06 | 8 | 25.00 | -2.13 | -3.96 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 57 | 57.89 | 1.68 | 1.15 | 0.32 | 57 | 49.12 | 0.06 | -1.16 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 96 | 55.21 | 2.19 | 0.39 | 0.82 | 96 | 51.04 | 0.93 | -0.34 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 7 | 42.86 | 3.85 | -5.35 | 0.39 | 7 | 42.86 | -1.29 | -4.23 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 52 | 51.92 | -0.28 | 1.35 | -1.26 | 52 | 51.92 | -0.32 | -1.06 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 87 | 51.72 | 1.86 | 1.16 | 0.37 | 87 | 54.02 | 2.06 | 0.74 | ok_initial_sample |
