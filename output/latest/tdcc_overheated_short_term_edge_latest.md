# TDCC Overheated Short-Term Edge

- generated_at: `2026-08-15 15:47:06 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260814-4a7d44bd65038f59`
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
| 20260814 | 5351 | 鈺創 | memory | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.884615384615373 | 82.94360385144428 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6213 | 聯茂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.393316195372748 | 82.50950570342206 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3605 | 宏致 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.325581395348838 | 66.45569620253164 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 7711 | 永擎 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.86666666666666 | 61.36752136752137 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 8039 | 台虹 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.73684210526316 | 57.06051873198847 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3081 | 聯亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.195227765726678 | 55.82822085889572 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 8996 | 高力 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.488038277511958 | 49.70760233918128 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 4931 | 新盛力 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.478060046189373 | 48.16901408450705 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6265 | 方土昶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.8158844765343 | 47.405660377358494 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6770 | 力積電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.694656488549622 | 43.853211009174316 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3443 | 創意 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.24202420242025 | 43.62680683311433 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2464 | 盟立 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.662824207492804 | 42.75092936802973 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3234 | 光環 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.97674418604652 | 42.63322884012539 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6446 | 藥華藥 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.967741935483875 | 41.50943396226414 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3017 | 奇鋐 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.157989228007175 | 39.439655172413794 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6187 | 萬潤 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.831858407079654 | 37.2443487621098 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6538 | 倉和 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.89655172413794 | 33.33333333333333 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6108 | 競國 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.93121693121695 | 32.732732732732764 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3044 | 健鼎 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.85786802030456 | 32.24932249322494 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2357 | 華碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.9094247246022 | 22.962962962962962 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3543 | 州巧 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.388888888888893 | 21.331316187594563 | 72 | 56.94 | 1.02 | 70 | 52.86 | 0.01 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 8996 | 高力 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.488038277511958 | 49.70760233918128 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 4931 | 新盛力 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.478060046189373 | 48.16901408450705 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6770 | 力積電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.694656488549622 | 43.853211009174316 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3443 | 創意 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.24202420242025 | 43.62680683311433 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2464 | 盟立 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.662824207492804 | 42.75092936802973 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3234 | 光環 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.97674418604652 | 42.63322884012539 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2408 | 南亞科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.035010940919033 | 42.0249653259362 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6446 | 藥華藥 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.967741935483875 | 41.50943396226414 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3017 | 奇鋐 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.157989228007175 | 39.439655172413794 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6187 | 萬潤 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.831858407079654 | 37.2443487621098 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3211 | 順達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.509601181683896 | 33.904109589041084 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6538 | 倉和 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.89655172413794 | 33.33333333333333 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 6108 | 競國 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.93121693121695 | 32.732732732732764 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3044 | 健鼎 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.85786802030456 | 32.24932249322494 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 4510 | 高鋒 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.835411471321702 | 31.96022727272727 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2359 | 所羅門 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.149825783972123 | 31.818181818181813 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3532 | 台勝科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.919999999999998 | 31.123388581952117 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2465 | 麗臺 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.69095182138662 | 30.653950953678468 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 2357 | 華碩 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.9094247246022 | 22.962962962962962 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 3543 | 州巧 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.388888888888893 | 21.331316187594563 | 43 | 58.14 | -0.37 | 43 | 48.84 | -2.85 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 8996 | 高力 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 22.488038277511958 | 49.70760233918128 | 5 | 40.00 | -6.64 | 4 | 25.00 | -10.23 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260814 | 7610 | 聯友金屬-創 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | -5.405405405405405 | 45.83333333333333 | 5 | 40.00 | -6.64 | 4 | 25.00 | -10.23 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 5 | 40.00 | 1.74 | -1.36 | -6.64 | 5 | 20.00 | -4.72 | -11.49 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 43 | 58.14 | 1.45 | 0.42 | -0.37 | 43 | 46.51 | -0.11 | -1.71 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 72 | 56.94 | 2.52 | 0.39 | 1.02 | 72 | 50.00 | 1.16 | -0.22 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 4 | 25.00 | -6.01 | -5.91 | -10.23 | 4 | 25.00 | -11.00 | -14.54 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 43 | 48.84 | -2.05 | -0.87 | -2.85 | 43 | 48.84 | -1.55 | -2.07 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 70 | 52.86 | 1.33 | 1.42 | 0.01 | 70 | 55.71 | 1.97 | 0.83 | ok_initial_sample |
