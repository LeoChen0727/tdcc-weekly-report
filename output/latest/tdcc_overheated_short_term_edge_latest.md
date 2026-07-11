# TDCC Overheated Short-Term Edge

- generated_at: `2026-07-11 18:23:36 Asia/Taipei`
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
| 20260703 | 2231 | 為升 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 34.353741496598644 | 27.556512378902042 | 6 | 66.67 | -4.21 | 6 | 66.67 | 2.28 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6409 | 旭隼 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.454452405322407 | 35.5291576673866 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.52083333333335 | 35.3932584269663 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5371 | 中光電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.48539638386647 | 32.999999999999986 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2481 | 強茂 | power discrete/diodes | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.285714285714285 | 29.374999999999996 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6525 | 捷敏-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.342465753424648 | 27.97202797202798 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2645 | 長榮航太 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.97947214076246 | 27.35294117647058 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2634 | 漢翔 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.95121951219512 | 27.118644067796605 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1314 | 中石化 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.96486825595987 | 26.9922879177378 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6753 | 龍德造船 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.74897119341564 | 26.74897119341564 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1313 | 聯成 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.789473684210531 | 23.275862068965523 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1310 | 台苯 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.035317860746723 | 23.110151187904982 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1301 | 台塑 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.965517241379317 | 20.116054158607355 | 32 | 68.75 | 0.25 | 29 | 65.52 | 0.95 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2483 | 百容 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.46678635547574 | 69.23076923076923 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 4707 | 磐亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.686025408348453 | 46.95652173913043 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6409 | 旭隼 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.454452405322407 | 35.5291576673866 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.52083333333335 | 35.3932584269663 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5371 | 中光電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.48539638386647 | 32.999999999999986 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2481 | 強茂 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.285714285714285 | 29.374999999999996 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6525 | 捷敏-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.342465753424648 | 27.97202797202798 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2645 | 長榮航太 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.97947214076246 | 27.35294117647058 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2634 | 漢翔 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.95121951219512 | 27.118644067796605 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1314 | 中石化 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.96486825595987 | 26.9922879177378 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6753 | 龍德造船 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.74897119341564 | 26.74897119341564 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1313 | 聯成 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.789473684210531 | 23.275862068965523 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1310 | 台苯 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.035317860746723 | 23.110151187904982 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1301 | 台塑 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.965517241379317 | 20.116054158607355 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2059 | 川湖 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.449213161659525 | 16.533139111434814 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5483 | 中美晶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.353658536585357 | 16.298342541436472 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2305 | 全友 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.541310541310533 | 15.304606240713214 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1714 | 和桐 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.64150943396226 | 11.793611793611781 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2302 | 麗正 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.403397027600846 | 10.63829787234043 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2342 | 茂矽 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.313725490196072 | 5.615942028985499 | 59 | 62.71 | 2.15 | 55 | 63.64 | 2.67 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 6 | 66.67 | 1.66 | 1.11 | -4.21 | 6 | 50.00 | -1.36 | -6.37 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 32 | 68.75 | 3.42 | 1.99 | 0.25 | 32 | 53.12 | 1.99 | -0.94 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 59 | 62.71 | 4.35 | 2.11 | 2.15 | 59 | 54.24 | 3.14 | 1.08 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 6 | 66.67 | 6.53 | 6.51 | 2.28 | 6 | 66.67 | 0.18 | -3.21 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29 | 65.52 | 3.94 | 1.97 | 0.95 | 29 | 68.97 | 5.41 | 2.80 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 55 | 63.64 | 5.47 | 1.99 | 2.67 | 55 | 67.27 | 6.75 | 4.16 | ok_initial_sample |
