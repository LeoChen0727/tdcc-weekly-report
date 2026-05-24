# 全市場權證資料分析與追蹤

- generated_at: `2026-05-24 11:38:58 Asia/Taipei`
- data_date: `20260524`
- raw_rows: `29584`
- stock_level_rows: `458`
- turnover_ready: `False`
- 權證只作輔助訊號，不可單獨作為買進理由。

## 一、資料狀態

今日權證資料日期已跟主流程同步。
注意：今日 stock-level 權證成交金額為 0 或缺值，代表官方權證清單已更新，但成交金額/報價資料尚未成功解析；本報告只做清單與可得欄位追蹤，不假裝有資金熱度。

## 二、全市場認購/認售成交金額總覽

- call_turnover_total: `0.0`
- put_turnover_total: `0.0`
- call_warrant_count_total: `26914.0`
- put_warrant_count_total: `2670.0`

## 三、認購成交金額前20名標的

| stock_id | stock_name | call_turnover | call_warrant_count | candidate_category | tdcc_status | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 2330 | 台積電 | 0.0 | 939 |  |  |  |
| 0063 | 元大滬深300正2 | 0.0 | 650 |  |  |  |
| 2317 | 鴻海 | 0.0 | 537 | pattern,revenue_pullback |  |  |
| 2454 | 聯發科 | 0.0 | 511 | range_rebound |  |  |
| 3661 | 世芯-KY | 0.0 | 472 |  |  |  |
| 0001 | 臺股指數 | 0.0 | 463 |  |  |  |
| 6669 | 緯穎 | 0.0 | 424 | revenue_pullback |  |  |
| 3017 | 奇鋐 | 0.0 | 414 | revenue_pullback |  |  |
| 2313 | 華通 | 0.0 | 320 |  |  |  |
| 2327 | 國巨* | 0.0 | 309 |  |  |  |
| 2308 | 台達電 | 0.0 | 299 | revenue_pullback |  |  |
| 2345 | 智邦 | 0.0 | 291 | revenue_pullback |  |  |
| 2303 | 聯電 | 0.0 | 268 |  |  |  |
| 2368 | 金像電 | 0.0 | 256 | revenue_pullback |  |  |
| 3665 | 貿聯-KY | 0.0 | 256 |  |  |  |
| 1303 | 南亞 | 0.0 | 252 |  |  |  |
| 4958 | 臻鼎-KY | 0.0 | 246 |  |  |  |
| 0073 | 期元大道瓊白銀(原名：元大道瓊白銀) | 0.0 | 244 |  |  |  |
| 3008 | 大立光 | 0.0 | 241 |  |  |  |
| 3715 | 定穎投控 | 0.0 | 240 | revenue_pullback |  |  |

## 四、認售成交金額前20名標的

| stock_id | stock_name | put_turnover | put_warrant_count | candidate_category | tdcc_status | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | 臺股指數 | 0.0 | 449 |  |  |  |
| 2330 | 台積電 | 0.0 | 214 |  |  |  |
| 0050 | 元大台灣50 | 0.0 | 197 |  |  |  |
| 0063 | 元大滬深300正2 | 0.0 | 188 |  |  |  |
| 2308 | 台達電 | 0.0 | 60 | revenue_pullback |  |  |
| 6770 | 力積電 | 0.0 | 52 | pattern,revenue_pullback |  |  |
| 2317 | 鴻海 | 0.0 | 48 | pattern,revenue_pullback |  |  |
| 2454 | 聯發科 | 0.0 | 48 | range_rebound |  |  |
| 2313 | 華通 | 0.0 | 46 |  |  |  |
| 0073 | 期元大道瓊白銀(原名：元大道瓊白銀) | 0.0 | 45 |  |  |  |
| 2327 | 國巨* | 0.0 | 45 |  |  |  |
| 6669 | 緯穎 | 0.0 | 42 | revenue_pullback |  |  |
| 2345 | 智邦 | 0.0 | 41 | revenue_pullback |  |  |
| 3017 | 奇鋐 | 0.0 | 40 | revenue_pullback |  |  |
| 3037 | 欣興 | 0.0 | 40 |  |  |  |
| 0064 | 期元大S&P石油(原名：元大S&P石油) | 0.0 | 36 |  |  |  |
| 0070 | 期元大S&P黃金正2(原名：元大S&P黃金正2) | 0.0 | 28 |  |  |  |
| 2059 | 川湖 | 0.0 | 28 |  |  |  |
| 1303 | 南亞 | 0.0 | 27 |  |  |  |
| 2368 | 金像電 | 0.0 | 26 | revenue_pullback |  |  |

## 五、Call/Put 比異常標的

目前沒有可用資料。

## 六、族群權證熱度

| sector_or_theme | stock_count | call_turnover | put_turnover | call_put_turnover_ratio | representative_codes |
| --- | --- | --- | --- | --- | --- |
| unknown | 458 | 0.0 | 0.0 |  | 0001,0027,0039,0050,0052,0056,0061,0062,0063,0064 |

## 七、與每日候選分類、股價型態、TDCC、法人/主力資料交叉比對

| stock_id | stock_name | candidate_category | tdcc_status | call_turnover | put_turnover | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 0056 | 元大高股息 | pattern |  | 0.0 | 0.0 |  |
| 1215 | 卜蜂 | pattern |  | 0.0 | 0.0 |  |
| 1304 | 台聚 | pattern |  | 0.0 | 0.0 |  |
| 1305 | 華夏 | pattern |  | 0.0 | 0.0 |  |
| 1313 | 聯成 | pattern |  | 0.0 | 0.0 |  |
| 1402 | 遠東新 | pattern |  | 0.0 | 0.0 |  |
| 1409 | 新纖 | pattern |  | 0.0 | 0.0 |  |
| 1503 | 士電 | revenue_pullback |  | 0.0 | 0.0 |  |
| 1504 | 東元 | pattern |  | 0.0 | 0.0 |  |
| 1513 | 中興電 | pattern |  | 0.0 | 0.0 |  |
| 1514 | 亞力 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 1536 | 和大 | pattern |  | 0.0 | 0.0 |  |
| 1582 | 信錦 | range_rebound |  | 0.0 | 0.0 |  |
| 1590 | 亞德客-KY | revenue_pullback |  | 0.0 | 0.0 |  |
| 1597 | 直得 | revenue_pullback |  | 0.0 | 0.0 |  |
| 1605 | 華新 | pattern |  | 0.0 | 0.0 |  |
| 1609 | 大亞 | pattern |  | 0.0 | 0.0 |  |
| 1708 | 東鹼 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 1710 | 東聯 | pattern |  | 0.0 | 0.0 |  |
| 1714 | 和桐 | pattern,revenue_breakout_low_response,revenue_pullback |  | 0.0 | 0.0 |  |
| 1773 | 勝一 | range_rebound |  | 0.0 | 0.0 |  |
| 1802 | 台玻 | pattern |  | 0.0 | 0.0 |  |
| 1905 | 華紙 | pattern |  | 0.0 | 0.0 |  |
| 2009 | 第一銅 | pattern |  | 0.0 | 0.0 |  |
| 2027 | 大成鋼 | pattern |  | 0.0 | 0.0 |  |
| 2101 | 南港 | revenue_breakout_low_response,revenue_pullback |  | 0.0 | 0.0 |  |
| 2103 | 台橡 | pattern |  | 0.0 | 0.0 |  |
| 2105 | 正新 | pattern |  | 0.0 | 0.0 |  |
| 2233 | 宇隆 | range_rebound |  | 0.0 | 0.0 |  |
| 2301 | 光寶科 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 2308 | 台達電 | revenue_pullback |  | 0.0 | 0.0 |  |
| 2312 | 金寶 | pattern |  | 0.0 | 0.0 |  |
| 2317 | 鴻海 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 2324 | 仁寶 | pattern,range_rebound |  | 0.0 | 0.0 |  |
| 2328 | 廣宇 | pattern |  | 0.0 | 0.0 |  |
| 2329 | 華泰 | pattern |  | 0.0 | 0.0 |  |
| 2332 | 友訊 | range_rebound |  | 0.0 | 0.0 |  |
| 2337 | 旺宏 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 2338 | 光罩 | pattern |  | 0.0 | 0.0 |  |
| 2344 | 華邦電 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 2345 | 智邦 | revenue_pullback |  | 0.0 | 0.0 |  |
| 2347 | 聯強 | revenue_breakout_low_response,revenue_pullback |  | 0.0 | 0.0 |  |
| 2352 | 佳世達 | pattern,range_rebound |  | 0.0 | 0.0 |  |
| 2353 | 宏碁 | pattern,range_rebound,revenue_breakout_low_response,revenue_pullback |  | 0.0 | 0.0 |  |
| 2354 | 鴻準 | pattern |  | 0.0 | 0.0 |  |
| 2355 | 敬鵬 | range_rebound |  | 0.0 | 0.0 |  |
| 2356 | 英業達 | pattern |  | 0.0 | 0.0 |  |
| 2357 | 華碩 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 2359 | 所羅門 | pattern |  | 0.0 | 0.0 |  |
| 2360 | 致茂 | revenue_pullback |  | 0.0 | 0.0 |  |
| 2362 | 藍天 | range_rebound |  | 0.0 | 0.0 |  |
| 2363 | 矽統 | pattern,range_rebound,revenue_pullback |  | 0.0 | 0.0 |  |
| 2365 | 昆盈 | pattern |  | 0.0 | 0.0 |  |
| 2368 | 金像電 | revenue_pullback |  | 0.0 | 0.0 |  |
| 2369 | 菱生 | pattern,revenue_pullback |  | 0.0 | 0.0 |  |
| 2374 | 佳能 | pattern,revenue_breakout_low_response,revenue_pullback |  | 0.0 | 0.0 |  |
| 2376 | 技嘉 | revenue_pullback |  | 0.0 | 0.0 |  |
| 2377 | 微星 | pattern |  | 0.0 | 0.0 |  |
| 2379 | 瑞昱 | pattern |  | 0.0 | 0.0 |  |
| 2383 | 台光電 | revenue_pullback |  | 0.0 | 0.0 |  |

## 八、過熱與反指標風險

- 認購熱度高只是短線資金參考，不可單獨作為買進理由。
- 若股價已過熱、TDCC 轉弱或權證熱度過度集中，應視為追價風險。
- 若成交金額資料缺失，本日不做權證熱度強弱結論。

## 九、後續追蹤名單

| stock_id | stock_name | call_turnover | call_warrant_count | candidate_category | sub_theme |
| --- | --- | --- | --- | --- | --- |
| 2330 | 台積電 | 0.0 | 939 |  |  |
| 0063 | 元大滬深300正2 | 0.0 | 650 |  |  |
| 2317 | 鴻海 | 0.0 | 537 | pattern,revenue_pullback |  |
| 2454 | 聯發科 | 0.0 | 511 | range_rebound |  |
| 3661 | 世芯-KY | 0.0 | 472 |  |  |
| 0001 | 臺股指數 | 0.0 | 463 |  |  |
| 6669 | 緯穎 | 0.0 | 424 | revenue_pullback |  |
| 3017 | 奇鋐 | 0.0 | 414 | revenue_pullback |  |
| 2313 | 華通 | 0.0 | 320 |  |  |
| 2327 | 國巨* | 0.0 | 309 |  |  |
| 2308 | 台達電 | 0.0 | 299 | revenue_pullback |  |
| 2345 | 智邦 | 0.0 | 291 | revenue_pullback |  |
| 2303 | 聯電 | 0.0 | 268 |  |  |
| 2368 | 金像電 | 0.0 | 256 | revenue_pullback |  |
| 3665 | 貿聯-KY | 0.0 | 256 |  |  |
| 1303 | 南亞 | 0.0 | 252 |  |  |
| 4958 | 臻鼎-KY | 0.0 | 246 |  |  |
| 0073 | 期元大道瓊白銀(原名：元大道瓊白銀) | 0.0 | 244 |  |  |
| 3008 | 大立光 | 0.0 | 241 |  |  |
| 3715 | 定穎投控 | 0.0 | 240 | revenue_pullback |  |
