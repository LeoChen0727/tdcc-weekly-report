# TDCC Overheated Short-Term Edge

- generated_at: `2026-10-03 15:36:08 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20261002-d841316b0644c08f`
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
| 20261002 | 6456 | GIS-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.193384223918585 | 43.364197530864224 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 4919 | 新唐 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.641791044776127 | 40.51724137931034 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6485 | 點序 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.303834808259595 | 39.799331103678924 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 2466 | 冠西電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.229074889867853 | 35.57692307692308 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6207 | 雷科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.824561403508774 | 35.159817351598164 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 8289 | 泰藝 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.209223847019114 | 32.62411347517731 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3114 | 好德 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.28731942215088 | 32.16666666666666 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3615 | 安可 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.493472584856406 | 31.964809384164216 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 5309 | 系統電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.572815533980588 | 30.099009900990104 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3189 | 景碩 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.89403973509933 | 28.04878048780488 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6488 | 環球晶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.263157894736832 | 27.001067235859132 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3042 | 晶技 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.414141414141415 | 24.258760107816713 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3236 | 千如 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.196796338672755 | 22.477064220183472 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3624 | 光頡 | passive components | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.820895522388053 | 20.731707317073166 | 61 | 57.38 | 0.66 | 59 | 54.24 | -1.40 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3016 | 嘉晶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.05498281786942 | 56.27705627705628 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 8150 | 南茂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.691588785046733 | 45.809414466130896 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6456 | GIS-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.193384223918585 | 43.364197530864224 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6168 | 宏齊 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.650485436893199 | 43.07931570762054 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 4919 | 新唐 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.641791044776127 | 40.51724137931034 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6485 | 點序 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.303834808259595 | 39.799331103678924 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3037 | 欣興 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.5 | 35.796045785639954 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3707 | 漢磊 | semiconductor | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.36752136752136 | 35.23809523809525 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6207 | 雷科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.824561403508774 | 35.159817351598164 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 8046 | 南電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.661157024793386 | 32.126696832579185 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 5309 | 系統電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.572815533980588 | 30.099009900990104 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3189 | 景碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.89403973509933 | 28.04878048780488 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6488 | 環球晶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.263157894736832 | 27.001067235859132 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3105 | 穩懋 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.913480885311863 | 25.07936507936508 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 6122 | 擎邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.760869565217384 | 25.048923679060664 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3042 | 晶技 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.414141414141415 | 24.258760107816713 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3236 | 千如 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.196796338672755 | 22.477064220183472 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3624 | 光頡 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.820895522388053 | 20.731707317073166 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 3591 | 艾笛森 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.040650406504064 | 19.915254237288128 | 107 | 55.14 | 0.98 | 103 | 53.40 | 0.18 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20261002 | 4919 | 新唐 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 21.641791044776127 | 40.51724137931034 | 11 | 54.55 | 4.87 | 10 | 50.00 | 6.73 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 11 | 54.55 | 7.19 | 0.30 | 4.87 | 11 | 45.45 | 3.67 | 1.58 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 61 | 57.38 | 1.91 | 1.15 | 0.66 | 61 | 49.18 | 0.35 | -0.75 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 107 | 55.14 | 2.23 | 0.42 | 0.98 | 107 | 51.40 | 1.07 | -0.08 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 10 | 50.00 | 9.70 | -0.80 | 6.73 | 10 | 50.00 | 6.67 | 3.94 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 59 | 54.24 | -0.55 | 1.55 | -1.40 | 59 | 50.85 | -0.69 | -1.33 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 103 | 53.40 | 1.51 | 1.29 | 0.18 | 103 | 54.37 | 1.66 | 0.46 | ok_initial_sample |
