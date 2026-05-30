# TDCC Overheated Short-Term Edge

- generated_at: `2026-05-30 17:32:32 Asia/Taipei`
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
| 20260529 | 2375 | 凱美 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.7918215613383 | 67.50503018108651 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8358 | 金居 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.47509578544062 | 56.09756097560976 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3189 | 景碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.704433497536943 | 50.0 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3042 | 晶技 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.443181818181813 | 49.65277777777777 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2495 | 普安 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.515837104072382 | 46.514935988620195 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.141987829614596 | 45.576407506702424 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2305 | 全友 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.595744680851062 | 45.12195121951221 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6127 | 九豪 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.19047619047619 | 44.886975242195895 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8473 | 山林水 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.633165829145746 | 44.827586206896555 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3532 | 台勝科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.370221327967805 | 44.01805869074491 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5864 | 致和證 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.668674698795172 | 42.54966887417218 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2428 | 興勤 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.412371134020614 | 41.747572815533985 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6870 | 騰雲 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.191489361702136 | 41.48936170212767 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6284 | 佳邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.58536585365853 | 41.420118343195256 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2312 | 金寶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.673716012084604 | 39.85637342908439 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6175 | 立敦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.647791619479047 | 39.377537212449255 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8289 | 泰藝 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.07784431137726 | 37.40740740740742 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2369 | 菱生 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.741029641185655 | 35.69023569023568 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8261 | 富鼎 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.125000000000009 | 34.57249070631969 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2356 | 英業達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.983193277310928 | 34.48275862068966 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3673 | TPK-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.077922077922064 | 33.38485316846984 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4939 | 亞電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.686472819216192 | 33.24538258575198 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 1530 | 亞崴 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.785714285714278 | 31.725417439703165 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6015 | 宏遠證 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.32268370607029 | 30.405405405405396 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3491 | 昇達科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.989637305699487 | 30.17751479289941 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6706 | 惠特 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.081081081081079 | 29.65299684542586 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6290 | 良維 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.820143884892087 | 28.044280442804425 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2353 | 宏碁 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.120135363790205 | 27.07581227436824 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4906 | 正文 | networking | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.325062034739474 | 26.947637292464897 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6196 | 帆宣 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.610859728506776 | 26.64188351920693 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3149 | 正達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.47377326565143 | 24.041811846689896 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6005 | 群益證 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.68965517241379 | 23.2 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8454 | 富邦媒 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.626631853785902 | 23.2 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6265 | 方土昶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.760914760914767 | 22.66666666666668 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2344 | 華邦電 | memory | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.400000000000002 | 22.00772200772201 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3135 | 凌航 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.16784869976358 | 20.601851851851862 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8477 | 創業家 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.517571884984026 | 19.999999999999996 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5284 | jpp-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.121951219512205 | 19.920318725099605 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2357 | 華碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.58357771260996 | 18.720748829953205 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2493 | 揚博 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.36363636363636 | 17.216117216117222 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2317 | 鴻海 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.59999999999999 | 16.297786720321938 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8163 | 達方 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.238429172510521 | 16.100443131462328 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2351 | 順德 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.260053619302957 | 15.277777777777768 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8028 | 昇陽半導體 | semiconductor equipment/materials | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.22448979591837 | 13.73913043478261 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2376 | 技嘉 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.72868217054264 | 13.32312404287903 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2408 | 南亞科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.755233494363937 | 11.39646869983948 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3317 | 尼克森 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.118265440210262 | 11.288180610889764 | 25 | 76.00 | 5.12 | 11 | 81.82 | 6.83 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3189 | 景碩 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.704433497536943 | 50.0 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3042 | 晶技 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.443181818181813 | 49.65277777777777 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2495 | 普安 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.515837104072382 | 46.514935988620195 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.141987829614596 | 45.576407506702424 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2305 | 全友 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.595744680851062 | 45.12195121951221 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6127 | 九豪 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.19047619047619 | 44.886975242195895 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3532 | 台勝科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.370221327967805 | 44.01805869074491 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5864 | 致和證 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.668674698795172 | 42.54966887417218 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2312 | 金寶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.673716012084604 | 39.85637342908439 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8289 | 泰藝 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.07784431137726 | 37.40740740740742 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2369 | 菱生 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.741029641185655 | 35.69023569023568 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2356 | 英業達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.983193277310928 | 34.48275862068966 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4939 | 亞電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.686472819216192 | 33.24538258575198 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6224 | 聚鼎 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.33681765389083 | 32.49651324965133 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 1530 | 亞崴 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.785714285714278 | 31.725417439703165 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6015 | 宏遠證 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.32268370607029 | 30.405405405405396 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3491 | 昇達科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.989637305699487 | 30.17751479289941 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6290 | 良維 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.820143884892087 | 28.044280442804425 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2353 | 宏碁 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.120135363790205 | 27.07581227436824 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4906 | 正文 | networking | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.325062034739474 | 26.947637292464897 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3149 | 正達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.47377326565143 | 24.041811846689896 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6005 | 群益證 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.68965517241379 | 23.2 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2344 | 華邦電 | memory | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.400000000000002 | 22.00772200772201 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3135 | 凌航 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.16784869976358 | 20.601851851851862 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8477 | 創業家 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.517571884984026 | 19.999999999999996 | 15 | 66.67 | -0.02 | 4 | 75.00 | -12.63 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5864 | 致和證 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 29.668674698795172 | 42.54966887417218 | 2 | 0.00 | -9.21 | 0 |  |  | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8150 | 南茂 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 42.85714285714286 | 39.67861557478367 | 2 | 0.00 | -9.21 | 0 |  |  | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6224 | 聚鼎 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 10.33681765389083 | 32.49651324965133 | 2 | 0.00 | -9.21 | 0 |  |  | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6290 | 良維 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 24.820143884892087 | 28.044280442804425 | 2 | 0.00 | -9.21 | 0 |  |  | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -3.38 | -3.38 | -9.21 | 2 | 0.00 | -13.08 | -17.92 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15 | 66.67 | 4.15 | 1.15 | -0.02 | 15 | 66.67 | 3.57 | -0.51 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25 | 76.00 | 8.11 | 2.33 | 5.12 | 25 | 76.00 | 7.44 | 3.61 | insufficient_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 0 |  |  |  |  | 0 |  |  |  | pending_only |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 4 | 75.00 | 9.05 | 5.21 | -12.63 | 4 | 100.00 | 10.24 | 1.82 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11 | 81.82 | 19.92 | 19.69 | 6.83 | 11 | 100.00 | 23.73 | 15.25 | insufficient_sample |
