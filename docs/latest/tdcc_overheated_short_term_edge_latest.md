# TDCC Overheated Short-Term Edge

- generated_at: `2026-07-05 04:09:25 Asia/Taipei`
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
| 20260703 | 2483 | 百容 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.46678635547574 | 69.23076923076923 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 4707 | 磐亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.686025408348453 | 46.95652173913043 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6409 | 旭隼 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.454452405322407 | 35.5291576673866 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.52083333333335 | 35.3932584269663 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5371 | 中光電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.48539638386647 | 32.999999999999986 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2481 | 強茂 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.285714285714285 | 29.374999999999996 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6525 | 捷敏-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.342465753424648 | 27.97202797202798 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2645 | 長榮航太 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.97947214076246 | 27.35294117647058 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2634 | 漢翔 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.95121951219512 | 27.118644067796605 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1314 | 中石化 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.96486825595987 | 26.9922879177378 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6753 | 龍德造船 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.74897119341564 | 26.74897119341564 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1313 | 聯成 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.789473684210531 | 23.275862068965523 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1310 | 台苯 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.035317860746723 | 23.110151187904982 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1301 | 台塑 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.965517241379317 | 20.116054158607355 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2059 | 川湖 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.449213161659525 | 16.533139111434814 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5483 | 中美晶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.353658536585357 | 16.298342541436472 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2305 | 全友 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.541310541310533 | 15.304606240713214 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1714 | 和桐 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.64150943396226 | 11.793611793611781 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2302 | 麗正 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.403397027600846 | 10.63829787234043 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2342 | 茂矽 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.313725490196072 | 5.615942028985499 | 197 | 51.27 | 2.84 | 188 | 63.83 | 4.21 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6213 | 聯茂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.708513708513713 | 40.71428571428572 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2061 | 風青 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.53035143769968 | 40.53030303030305 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6409 | 旭隼 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.454452405322407 | 35.5291576673866 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.52083333333335 | 35.3932584269663 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5371 | 中光電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.48539638386647 | 32.999999999999986 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2481 | 強茂 | power discrete/diodes | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.285714285714285 | 29.374999999999996 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6525 | 捷敏-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.342465753424648 | 27.97202797202798 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2645 | 長榮航太 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.97947214076246 | 27.35294117647058 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2634 | 漢翔 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.95121951219512 | 27.118644067796605 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1314 | 中石化 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.96486825595987 | 26.9922879177378 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6753 | 龍德造船 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.74897119341564 | 26.74897119341564 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1326 | 台化 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.461254612546114 | 25.461254612546114 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1313 | 聯成 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.789473684210531 | 23.275862068965523 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1310 | 台苯 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.035317860746723 | 23.110151187904982 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 5460 | 同協 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.55737704918033 | 22.53968253968255 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 3594 | 磐儀 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.026172300981457 | 22.4191866527633 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 6435 | 大中 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.060240963855431 | 20.314960629921263 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 1301 | 台塑 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.965517241379317 | 20.116054158607355 | 191 | 51.31 | 1.82 | 179 | 60.89 | 2.92 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260703 | 2231 | 為升 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 34.353741496598644 | 27.556512378902042 | 49 | 42.86 | 0.56 | 49 | 59.18 | 4.54 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 49 | 42.86 | 0.92 | -2.03 | 0.56 | 49 | 36.73 | -0.66 | -0.81 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 191 | 51.31 | 3.10 | 0.42 | 1.82 | 191 | 49.74 | 1.72 | 0.62 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 197 | 51.27 | 3.86 | 0.26 | 2.84 | 197 | 48.73 | 2.32 | 1.44 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 49 | 59.18 | 6.89 | 5.53 | 4.54 | 49 | 59.18 | 5.45 | 3.29 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 179 | 60.89 | 4.95 | 3.57 | 2.92 | 179 | 54.75 | 3.69 | 1.83 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 188 | 63.83 | 6.37 | 3.96 | 4.21 | 188 | 56.38 | 5.01 | 2.98 | ok_initial_sample |
