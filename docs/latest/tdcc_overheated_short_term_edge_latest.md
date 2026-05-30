# TDCC Overheated Short-Term Edge

- generated_at: `2026-05-30 19:14:14 Asia/Taipei`
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
| 20260529 | 2375 | 凱美 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.7918215613383 | 67.50503018108651 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8358 | 金居 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.47509578544062 | 56.09756097560976 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3189 | 景碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.704433497536943 | 50.0 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3042 | 晶技 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 22.443181818181813 | 49.65277777777777 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2495 | 普安 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.515837104072382 | 46.514935988620195 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.141987829614596 | 45.576407506702424 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2305 | 全友 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.595744680851062 | 45.12195121951221 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6127 | 九豪 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.19047619047619 | 44.886975242195895 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8473 | 山林水 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.633165829145746 | 44.827586206896555 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3532 | 台勝科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.370221327967805 | 44.01805869074491 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5864 | 致和證 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.668674698795172 | 42.54966887417218 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2428 | 興勤 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.412371134020614 | 41.747572815533985 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6870 | 騰雲 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.191489361702136 | 41.48936170212767 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6284 | 佳邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.58536585365853 | 41.420118343195256 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2312 | 金寶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.673716012084604 | 39.85637342908439 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6175 | 立敦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.647791619479047 | 39.377537212449255 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8289 | 泰藝 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.07784431137726 | 37.40740740740742 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2369 | 菱生 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.741029641185655 | 35.69023569023568 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8261 | 富鼎 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.125000000000009 | 34.57249070631969 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2356 | 英業達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.983193277310928 | 34.48275862068966 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3673 | TPK-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.077922077922064 | 33.38485316846984 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4939 | 亞電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.686472819216192 | 33.24538258575198 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 1530 | 亞崴 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.785714285714278 | 31.725417439703165 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6015 | 宏遠證 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.32268370607029 | 30.405405405405396 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3491 | 昇達科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.989637305699487 | 30.17751479289941 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6706 | 惠特 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.081081081081079 | 29.65299684542586 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6290 | 良維 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.820143884892087 | 28.044280442804425 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2353 | 宏碁 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.120135363790205 | 27.07581227436824 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4906 | 正文 | networking | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.325062034739474 | 26.947637292464897 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6196 | 帆宣 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.610859728506776 | 26.64188351920693 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3149 | 正達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.47377326565143 | 24.041811846689896 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6005 | 群益證 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.68965517241379 | 23.2 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8454 | 富邦媒 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.626631853785902 | 23.2 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6265 | 方土昶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.760914760914767 | 22.66666666666668 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2344 | 華邦電 | memory | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.400000000000002 | 22.00772200772201 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3135 | 凌航 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.16784869976358 | 20.601851851851862 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8477 | 創業家 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.517571884984026 | 19.999999999999996 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5284 | jpp-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.121951219512205 | 19.920318725099605 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2357 | 華碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.58357771260996 | 18.720748829953205 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2493 | 揚博 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.36363636363636 | 17.216117216117222 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2317 | 鴻海 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.59999999999999 | 16.297786720321938 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8163 | 達方 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.238429172510521 | 16.100443131462328 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2351 | 順德 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.260053619302957 | 15.277777777777768 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8028 | 昇陽半導體 | semiconductor equipment/materials | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.22448979591837 | 13.73913043478261 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2376 | 技嘉 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.72868217054264 | 13.32312404287903 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2408 | 南亞科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 11.755233494363937 | 11.39646869983948 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3317 | 尼克森 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.118265440210262 | 11.288180610889764 | 85 | 67.06 | 5.96 | 54 | 85.19 | 11.82 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3189 | 景碩 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.704433497536943 | 50.0 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3042 | 晶技 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.443181818181813 | 49.65277777777777 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2495 | 普安 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.515837104072382 | 46.514935988620195 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.141987829614596 | 45.576407506702424 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3537 | 堡達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.315186246418339 | 45.28301886792452 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2305 | 全友 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.595744680851062 | 45.12195121951221 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 7709 | 榮田 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.96467991169979 | 45.01312335958006 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6127 | 九豪 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.19047619047619 | 44.886975242195895 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3624 | 光頡 | passive components | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.21857923497268 | 44.356955380577425 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3532 | 台勝科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.370221327967805 | 44.01805869074491 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 5864 | 致和證 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.668674698795172 | 42.54966887417218 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8255 | 朋程 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.07006369426752 | 41.48936170212767 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2312 | 金寶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.673716012084604 | 39.85637342908439 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6862 | 三集瑞-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.783068783068792 | 39.44099378881987 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8182 | 加高 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 14.752116082224909 | 39.35389133627021 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4555 | 氣立 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.901408450704224 | 38.995215311004806 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2481 | 強茂 | power discrete/diodes | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.722846441947574 | 38.29787234042554 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8289 | 泰藝 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.07784431137726 | 37.40740740740742 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 8162 | 微矽電子-創 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.888157894736857 | 36.87150837988826 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6405 | 悅城 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.07006369426752 | 36.410256410256416 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3229 | 晟鈦 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.0 | 36.176066024759294 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2369 | 菱生 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.741029641185655 | 35.69023569023568 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 3528 | 安馳 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.266524520255864 | 35.68129330254042 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2356 | 英業達 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.983193277310928 | 34.48275862068966 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 4939 | 亞電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.686472819216192 | 33.24538258575198 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6411 | 晶焱 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.911485774499457 | 33.17191283292979 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2441 | 超豐 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.940170940170933 | 32.86384976525822 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6224 | 聚鼎 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.33681765389083 | 32.49651324965133 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 1570 | 力肯 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.752969121140133 | 32.233502538071065 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2454 | 聯發科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 11.658031088082899 | 32.208588957055206 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 1530 | 亞崴 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.785714285714278 | 31.725417439703165 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 2303 | 聯電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.754385964912288 | 31.36363636363637 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260529 | 6015 | 宏遠證 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.32268370607029 | 30.405405405405396 | 90 | 65.56 | 4.01 | 53 | 81.13 | 8.43 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 30 | 50.00 | 4.33 | 0.23 | 2.77 | 30 | 50.00 | 2.84 | 1.55 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 90 | 65.56 | 6.76 | 4.21 | 4.01 | 90 | 63.33 | 4.68 | 2.24 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 85 | 67.06 | 8.47 | 5.66 | 5.96 | 85 | 63.53 | 5.59 | 3.39 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 24 | 75.00 | 15.41 | 11.62 | 11.51 | 24 | 79.17 | 14.99 | 11.20 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 53 | 81.13 | 13.02 | 9.00 | 8.43 | 53 | 77.36 | 12.78 | 8.09 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 54 | 85.19 | 16.52 | 12.25 | 11.82 | 54 | 79.63 | 14.94 | 10.22 | ok_initial_sample |
