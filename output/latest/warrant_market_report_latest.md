# 全市場權證資料分析與追蹤

- generated_at: `2026-05-29 19:30:13 Asia/Taipei`
- data_date: `20260529`
- raw_rows: `29730`
- stock_level_rows: `455`
- turnover_ready: `True`
- 權證只作輔助訊號，不可單獨作為買進理由。

## 一、資料狀態

今日權證資料日期已跟主流程同步。


## 二、全市場認購/認售成交金額總覽

- call_turnover_total: `10700316870.0`
- put_turnover_total: `100130560.0`
- call_warrant_count_total: `27115.0`
- put_warrant_count_total: `2615.0`

## 三、認購成交金額前20名標的

| stock_id | stock_name | call_turnover | call_warrant_count | candidate_category | tdcc_status | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | 臺股指數 | 6085678790.0 | 434 |  |  |  |
| 2317 | 鴻海 | 298877460.0 | 527 | pattern,true_breakout |  |  |
| 2330 | 台積電 | 254646130.0 | 933 | range_rebound |  |  |
| 2408 | 南亞科 | 171752660.0 | 180 | pattern |  |  |
| 6770 | 力積電 | 143311340.0 | 195 | pattern,true_breakout |  |  |
| 3481 | 群創 | 120448880.0 | 144 | range_rebound |  |  |
| 0050 | 元大台灣50 | 102926860.0 | 232 | pattern |  |  |
| 3017 | 奇鋐 | 82650200.0 | 414 | pattern,revenue_pullback |  |  |
| 0063 | 元大滬深300正2 | 72849110.0 | 647 |  |  |  |
| 2327 | 國巨* | 69692970.0 | 295 |  |  |  |
| 2454 | 聯發科 | 68591580.0 | 487 | pattern |  |  |
| 2313 | 華通 | 66468630.0 | 331 | pattern |  |  |
| 2344 | 華邦電 | 65189790.0 | 165 | pattern,true_breakout |  |  |
| 6669 | 緯穎 | 64900600.0 | 418 | pullback_rebound,range_rebound,revenue_pullback |  |  |
| 2449 | 京元電子 | 59165030.0 | 234 | pattern,revenue_pullback |  |  |
| 1303 | 南亞 | 58766840.0 | 252 | range_rebound |  |  |
| 2303 | 聯電 | 58680740.0 | 275 |  |  |  |
| 6285 | 啟碁 | 55330280.0 | 215 | pattern |  |  |
| 2409 | 友達 | 53018940.0 | 187 | range_rebound |  |  |
| 8112 | 至上 | 51393400.0 | 159 | pattern,range_rebound,revenue_breakout_low_response,revenue_pullback |  |  |

## 四、認售成交金額前20名標的

| stock_id | stock_name | put_turnover | put_warrant_count | candidate_category | tdcc_status | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | 臺股指數 | 27180190.0 | 443 |  |  |  |
| 0063 | 元大滬深300正2 | 9864750.0 | 186 |  |  |  |
| 0050 | 元大台灣50 | 9137670.0 | 195 | pattern |  |  |
| 0098 | 主動統一台股增長 | 7299760.0 | 5 |  |  |  |
| 2330 | 台積電 | 4943140.0 | 204 | range_rebound |  |  |
| 3481 | 群創 | 3082050.0 | 18 | range_rebound |  |  |
| 2454 | 聯發科 | 3079750.0 | 45 | pattern |  |  |
| 6770 | 力積電 | 2989280.0 | 48 | pattern,true_breakout |  |  |
| 3661 | 世芯-KY | 2874490.0 | 20 | pattern |  |  |
| 2313 | 華通 | 2320680.0 | 48 | pattern |  |  |
| 2303 | 聯電 | 1604860.0 | 23 |  |  |  |
| 1802 | 台玻 | 1542800.0 | 21 | pattern |  |  |
| 2408 | 南亞科 | 1351110.0 | 15 | pattern |  |  |
| 2368 | 金像電 | 1132520.0 | 26 | pattern,revenue_pullback |  |  |
| 0066 | 國泰臺灣加權反1 | 1111240.0 | 23 |  |  |  |
| 6669 | 緯穎 | 1103920.0 | 39 | pullback_rebound,range_rebound,revenue_pullback |  |  |
| 3653 | 健策 | 940200.0 | 7 |  |  |  |
| 6285 | 啟碁 | 938270.0 | 18 | pattern |  |  |
| 2344 | 華邦電 | 922570.0 | 20 | pattern,true_breakout |  |  |
| 2317 | 鴻海 | 920810.0 | 47 | pattern,true_breakout |  |  |

## 五、Call/Put 比異常標的

| stock_id | stock_name | call_put_turnover_ratio | call_turnover | put_turnover | candidate_category | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 4967 | 十銓 | 495401.0 | 14862030.0 | 30.0 | pattern,revenue_pullback |  |
| 2486 | 一詮 | 112500.0 | 2250000.0 | 20.0 | pattern,revenue_pullback |  |
| 3305 | 昇貿 | 72763.1 | 21828930.0 | 300.0 |  |  |
| 2451 | 創見 | 43635.67 | 35344890.0 | 810.0 | pattern,revenue_pullback |  |
| 6805 | 富世達 | 15511.59 | 44983610.0 | 2900.0 | pullback_rebound,range_rebound,revenue_breakout_low_response,revenue_pullback |  |
| 6139 | 亞翔 | 12398.54 | 24797080.0 | 2000.0 | pattern,revenue_pullback |  |
| 8112 | 至上 | 10596.58 | 51393400.0 | 4850.0 | pattern,range_rebound,revenue_breakout_low_response,revenue_pullback |  |
| 2472 | 立隆電 | 7771.05 | 39166070.0 | 5040.0 |  |  |
| 1514 | 亞力 | 7325.94 | 7985270.0 | 1090.0 | pattern,revenue_pullback |  |
| 2474 | 可成 | 6987.61 | 20124320.0 | 2880.0 | range_rebound |  |
| 5243 | 乙盛-KY | 5714.46 | 9886010.0 | 1730.0 | pattern |  |
| 1301 | 台塑 | 2755.63 | 16258240.0 | 5900.0 | range_rebound |  |
| 0039 | 金融類 | 2346.7 | 704010.0 | 300.0 |  |  |
| 2605 | 新興 | 2303.58 | 2718230.0 | 1180.0 |  |  |
| 2371 | 大同 | 1937.82 | 4340720.0 | 2240.0 | pattern |  |
| 3034 | 聯詠 | 1762.55 | 19634760.0 | 11140.0 | pattern |  |
| 1503 | 士電 | 1649.12 | 11280010.0 | 6840.0 |  |  |
| 2337 | 旺宏 | 1404.46 | 6235800.0 | 4440.0 | pattern,revenue_pullback |  |
| 5284 | jpp-KY | 1287.49 | 4956820.0 | 3850.0 |  |  |
| 2357 | 華碩 | 1253.84 | 13014830.0 | 10380.0 | pattern,true_breakout |  |

## 六、族群權證熱度

| sector_or_theme | stock_count | call_turnover | put_turnover | call_put_turnover_ratio | representative_codes |
| --- | --- | --- | --- | --- | --- |
| unknown | 455 | 10700316870.0 | 100130560.0 | 106.86364752179554 | 0001,2317,8112,6805,2451,2059,2329,3406,8110,2324 |

## 七、與每日候選分類、股價型態、TDCC、法人/主力資料交叉比對

| stock_id | stock_name | candidate_category | tdcc_status | call_turnover | put_turnover | sub_theme |
| --- | --- | --- | --- | --- | --- | --- |
| 2317 | 鴻海 | pattern,true_breakout |  | 298877460.0 | 920810.0 |  |
| 8112 | 至上 | pattern,range_rebound,revenue_breakout_low_response,revenue_pullback |  | 51393400.0 | 4850.0 |  |
| 6805 | 富世達 | pullback_rebound,range_rebound,revenue_breakout_low_response,revenue_pullback |  | 44983610.0 | 2900.0 |  |
| 2451 | 創見 | pattern,revenue_pullback |  | 35344890.0 | 810.0 |  |
| 2329 | 華泰 | pattern,range_rebound |  | 28010250.0 | 29770.0 |  |
| 3406 | 玉晶光 | pattern,range_rebound |  | 27391370.0 | 69290.0 |  |
| 8110 | 華東 | range_rebound |  | 24047230.0 | 197520.0 |  |
| 2324 | 仁寶 | pattern,true_breakout |  | 22682700.0 | 204380.0 |  |
| 2474 | 可成 | range_rebound |  | 20124320.0 | 2880.0 |  |
| 3443 | 創意 | pullback_rebound,revenue_pullback |  | 18632960.0 | 20060.0 |  |
| 1301 | 台塑 | range_rebound |  | 16258240.0 | 5900.0 |  |
| 8271 | 宇瞻 | pullback_rebound,range_rebound,revenue_pullback |  | 11324320.0 | 18400.0 |  |
| 2354 | 鴻準 | pattern,range_rebound |  | 9810520.0 | 119690.0 |  |
| 5243 | 乙盛-KY | pattern |  | 9886010.0 | 1730.0 |  |
| 6176 | 瑞儀 | range_rebound |  | 5931140.0 | 29200.0 |  |
| 1304 | 台聚 | pattern |  | 4014470.0 | 187170.0 |  |
| 2352 | 佳世達 | pattern,range_rebound |  | 3415920.0 | 9800.0 |  |
| 3030 | 德律 | pattern,revenue_pullback |  | 47359570.0 | 0.0 |  |
| 4906 | 正文 | pattern,true_breakout |  | 31963170.0 | 0.0 |  |
| 1605 | 華新 | pattern,true_breakout |  | 26065200.0 | 0.0 |  |
| 3706 | 神達 | pattern,pullback_rebound,range_rebound,revenue_pullback |  | 24168350.0 | 0.0 |  |
| 1504 | 東元 | pattern,range_rebound |  | 20698960.0 | 0.0 |  |
| 2374 | 佳能 | pattern,pullback_rebound,range_rebound,revenue_breakout_low_response,revenue_pullback |  | 20199940.0 | 0.0 |  |
| 4938 | 和碩 | pattern,true_breakout |  | 15729980.0 | 0.0 |  |
| 3013 | 晟銘電 | pattern,range_rebound |  | 12467800.0 | 0.0 |  |
| 0052 | 富邦科技 | pattern |  | 10781250.0 | 0.0 |  |
| 2618 | 長榮航 | range_rebound |  | 6913820.0 | 0.0 |  |
| 1476 | 儒鴻 | pattern |  | 6773230.0 | 0.0 |  |
| 2419 | 仲琦 | pattern,range_rebound |  | 6643510.0 | 0.0 |  |
| 3380 | 明泰 | pattern,range_rebound |  | 5044190.0 | 0.0 |  |
| 3005 | 神基 | range_rebound |  | 4605440.0 | 0.0 |  |
| 1710 | 東聯 | pattern,range_rebound |  | 3612010.0 | 0.0 |  |
| 1609 | 大亞 | pattern,true_breakout |  | 3371960.0 | 0.0 |  |
| 3023 | 信邦 | pattern,range_rebound |  | 3147860.0 | 0.0 |  |
| 0050 | 元大台灣50 | pattern |  | 102926860.0 | 9137670.0 |  |
| 6669 | 緯穎 | pullback_rebound,range_rebound,revenue_pullback |  | 64900600.0 | 1103920.0 |  |
| 1303 | 南亞 | range_rebound |  | 58766840.0 | 220180.0 |  |
| 2409 | 友達 | range_rebound |  | 53018940.0 | 215340.0 |  |
| 2356 | 英業達 | pattern,true_breakout |  | 34391300.0 | 91170.0 |  |
| 2376 | 技嘉 | true_breakout |  | 34410450.0 | 0.0 |  |
| 2377 | 微星 | pattern |  | 27771630.0 | 86000.0 |  |
| 2367 | 燿華 | pattern |  | 21309630.0 | 845160.0 |  |
| 3034 | 聯詠 | pattern |  | 19634760.0 | 11140.0 |  |
| 2328 | 廣宇 | pattern,range_rebound |  | 18255760.0 | 0.0 |  |
| 7769 | 鴻勁 | range_rebound |  | 16393920.0 | 0.0 |  |
| 4967 | 十銓 | pattern,revenue_pullback |  | 14862030.0 | 30.0 |  |
| 2402 | 毅嘉 | pattern,range_rebound |  | 13341710.0 | 11200.0 |  |
| 2428 | 興勤 | range_rebound |  | 9100200.0 | 0.0 |  |
| 8131 | 福懋科 | pattern,range_rebound |  | 7379790.0 | 0.0 |  |
| 4916 | 事欣科 | true_breakout |  | 4988020.0 | 0.0 |  |
| 6505 | 台塑化 | pattern |  | 2938070.0 | 0.0 |  |
| 2610 | 華航 | range_rebound |  | 2738290.0 | 0.0 |  |
| 8103 | 瀚荃 | pullback_rebound,range_rebound,revenue_pullback |  | 2703670.0 | 0.0 |  |
| 6214 | 精誠 | pattern,range_rebound,revenue_pullback |  | 2111350.0 | 0.0 |  |
| 1402 | 遠東新 | pattern |  | 2055950.0 | 0.0 |  |
| 4571 | 鈞興-KY | pattern |  | 1869620.0 | 0.0 |  |
| 1536 | 和大 | pattern,range_rebound |  | 1863740.0 | 0.0 |  |
| 6753 | 龍德造船 | pullback_rebound,revenue_pullback |  | 1840110.0 | 0.0 |  |
| 3010 | 華立 | pattern |  | 1838610.0 | 0.0 |  |
| 3515 | 華擎 | pattern,range_rebound |  | 1716300.0 | 4720.0 |  |

## 八、過熱與反指標風險

- 認購熱度高只是短線資金參考，不可單獨作為買進理由。
- 若股價已過熱、TDCC 轉弱或權證熱度過度集中，應視為追價風險。
- 若成交金額資料缺失，本日不做權證熱度強弱結論。

## 九、後續追蹤名單

| stock_id | stock_name | call_turnover | call_warrant_count | candidate_category | sub_theme |
| --- | --- | --- | --- | --- | --- |
| 0001 | 臺股指數 | 6085678790.0 | 434 |  |  |
| 2317 | 鴻海 | 298877460.0 | 527 | pattern,true_breakout |  |
| 2330 | 台積電 | 254646130.0 | 933 | range_rebound |  |
| 2408 | 南亞科 | 171752660.0 | 180 | pattern |  |
| 6770 | 力積電 | 143311340.0 | 195 | pattern,true_breakout |  |
| 3481 | 群創 | 120448880.0 | 144 | range_rebound |  |
| 0050 | 元大台灣50 | 102926860.0 | 232 | pattern |  |
| 3017 | 奇鋐 | 82650200.0 | 414 | pattern,revenue_pullback |  |
| 0063 | 元大滬深300正2 | 72849110.0 | 647 |  |  |
| 2327 | 國巨* | 69692970.0 | 295 |  |  |
| 2454 | 聯發科 | 68591580.0 | 487 | pattern |  |
| 2313 | 華通 | 66468630.0 | 331 | pattern |  |
| 2344 | 華邦電 | 65189790.0 | 165 | pattern,true_breakout |  |
| 6669 | 緯穎 | 64900600.0 | 418 | pullback_rebound,range_rebound,revenue_pullback |  |
| 2449 | 京元電子 | 59165030.0 | 234 | pattern,revenue_pullback |  |
| 1303 | 南亞 | 58766840.0 | 252 | range_rebound |  |
| 2303 | 聯電 | 58680740.0 | 275 |  |  |
| 6285 | 啟碁 | 55330280.0 | 215 | pattern |  |
| 2409 | 友達 | 53018940.0 | 187 | range_rebound |  |
| 8112 | 至上 | 51393400.0 | 159 | pattern,range_rebound,revenue_breakout_low_response,revenue_pullback |  |
