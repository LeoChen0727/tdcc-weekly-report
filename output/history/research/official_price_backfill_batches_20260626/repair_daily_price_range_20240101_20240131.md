# Repair Daily Price Range Report

- start_date: `20240101`
- end_date: `20240131`
- check_code: `2330`
- repaired_count: `22`
- skipped_count: `8`
- failed_count: `1`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240101 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/01/01&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240101; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240101; TPEx batch best rows=0; date=20240101 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240102 | repaired | 1123 | 814 | 1937 | full_market_ok | data/daily_price/20240102.csv;data/daily_price/daily_price_20240102.csv |
| 20240103 | repaired | 1124 | 809 | 1933 | full_market_ok | data/daily_price/20240103.csv;data/daily_price/daily_price_20240103.csv |
| 20240104 | repaired | 1119 | 807 | 1926 | full_market_ok | data/daily_price/20240104.csv;data/daily_price/daily_price_20240104.csv |
| 20240105 | repaired | 1120 | 815 | 1935 | full_market_ok | data/daily_price/20240105.csv;data/daily_price/daily_price_20240105.csv |
| 20240106 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240107 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240108 | repaired | 1120 | 815 | 1935 | full_market_ok | data/daily_price/20240108.csv;data/daily_price/daily_price_20240108.csv |
| 20240109 | repaired | 1117 | 819 | 1936 | full_market_ok | data/daily_price/20240109.csv;data/daily_price/daily_price_20240109.csv |
| 20240110 | repaired | 1122 | 812 | 1934 | full_market_ok | data/daily_price/20240110.csv;data/daily_price/daily_price_20240110.csv |
| 20240111 | repaired | 1124 | 815 | 1939 | full_market_ok | data/daily_price/20240111.csv;data/daily_price/daily_price_20240111.csv |
| 20240112 | repaired | 1114 | 818 | 1932 | full_market_ok | data/daily_price/20240112.csv;data/daily_price/daily_price_20240112.csv |
| 20240113 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240114 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240115 | repaired | 1120 | 821 | 1941 | full_market_ok | data/daily_price/20240115.csv;data/daily_price/daily_price_20240115.csv |
| 20240116 | repaired | 1121 | 810 | 1931 | full_market_ok | data/daily_price/20240116.csv;data/daily_price/daily_price_20240116.csv |
| 20240117 | repaired | 1123 | 821 | 1944 | full_market_ok | data/daily_price/20240117.csv;data/daily_price/daily_price_20240117.csv |
| 20240118 | repaired | 1119 | 816 | 1935 | full_market_ok | data/daily_price/20240118.csv;data/daily_price/daily_price_20240118.csv |
| 20240119 | repaired | 1123 | 818 | 1941 | full_market_ok | data/daily_price/20240119.csv;data/daily_price/daily_price_20240119.csv |
| 20240120 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240121 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240122 | repaired | 1118 | 818 | 1936 | full_market_ok | data/daily_price/20240122.csv;data/daily_price/daily_price_20240122.csv |
| 20240123 | repaired | 1122 | 813 | 1935 | full_market_ok | data/daily_price/20240123.csv;data/daily_price/daily_price_20240123.csv |
| 20240124 | repaired | 1123 | 814 | 1937 | full_market_ok | data/daily_price/20240124.csv;data/daily_price/daily_price_20240124.csv |
| 20240125 | repaired | 1124 | 816 | 1940 | full_market_ok | data/daily_price/20240125.csv;data/daily_price/daily_price_20240125.csv |
| 20240126 | repaired | 1119 | 816 | 1935 | full_market_ok | data/daily_price/20240126.csv;data/daily_price/daily_price_20240126.csv |
| 20240127 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240128 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240129 | repaired | 1123 | 816 | 1939 | full_market_ok | data/daily_price/20240129.csv;data/daily_price/daily_price_20240129.csv |
| 20240130 | repaired | 1126 | 812 | 1938 | full_market_ok | data/daily_price/20240130.csv;data/daily_price/daily_price_20240130.csv |
| 20240131 | repaired | 1124 | 812 | 1936 | full_market_ok | data/daily_price/20240131.csv;data/daily_price/daily_price_20240131.csv |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240102 | True | 2330 | 台積電 | TWSE | 590.0 | 593.0 | 589.0 | 593.0 | 27997826 | 16549619798 |
| 20240103 | True | 2330 | 台積電 | TWSE | 584.0 | 585.0 | 576.0 | 578.0 | 40134497 | 23267025945 |
| 20240104 | True | 2330 | 台積電 | TWSE | 580.0 | 581.0 | 577.0 | 580.0 | 18063758 | 10466284102 |
| 20240105 | True | 2330 | 台積電 | TWSE | 578.0 | 580.0 | 574.0 | 576.0 | 22008878 | 12685460114 |
| 20240108 | True | 2330 | 台積電 | TWSE | 582.0 | 585.0 | 579.0 | 583.0 | 19270119 | 11232942053 |
| 20240109 | True | 2330 | 台積電 | TWSE | 588.0 | 589.0 | 583.0 | 586.0 | 23718766 | 13909252422 |
| 20240110 | True | 2330 | 台積電 | TWSE | 581.0 | 586.0 | 580.0 | 584.0 | 13708117 | 8006229126 |
| 20240111 | True | 2330 | 台積電 | TWSE | 586.0 | 589.0 | 583.0 | 586.0 | 27842729 | 16323168586 |
| 20240112 | True | 2330 | 台積電 | TWSE | 581.0 | 588.0 | 581.0 | 584.0 | 17636558 | 10304253419 |
| 20240115 | True | 2330 | 台積電 | TWSE | 590.0 | 590.0 | 585.0 | 586.0 | 21900687 | 12873769022 |
| 20240116 | True | 2330 | 台積電 | TWSE | 581.0 | 588.0 | 579.0 | 580.0 | 28889681 | 16817280777 |
| 20240117 | True | 2330 | 台積電 | TWSE | 583.0 | 584.0 | 578.0 | 581.0 | 46857735 | 27229863028 |
| 20240118 | True | 2330 | 台積電 | TWSE | 586.0 | 589.0 | 585.0 | 588.0 | 36746623 | 21575062923 |
| 20240119 | True | 2330 | 台積電 | TWSE | 625.0 | 627.0 | 614.0 | 626.0 | 176166037 | 109423769320 |
| 20240122 | True | 2330 | 台積電 | TWSE | 633.0 | 633.0 | 623.0 | 626.0 | 70829523 | 44436449501 |
| 20240123 | True | 2330 | 台積電 | TWSE | 629.0 | 629.0 | 622.0 | 628.0 | 45761889 | 28681559251 |
| 20240124 | True | 2330 | 台積電 | TWSE | 628.0 | 630.0 | 624.0 | 627.0 | 29905121 | 18779693566 |
| 20240125 | True | 2330 | 台積電 | TWSE | 635.0 | 642.0 | 633.0 | 642.0 | 59214638 | 37803501446 |
| 20240126 | True | 2330 | 台積電 | TWSE | 644.0 | 646.0 | 639.0 | 644.0 | 44103850 | 28392638215 |
| 20240129 | True | 2330 | 台積電 | TWSE | 646.0 | 648.0 | 644.0 | 648.0 | 29828008 | 19268444564 |
| 20240130 | True | 2330 | 台積電 | TWSE | 642.0 | 647.0 | 642.0 | 642.0 | 40398877 | 26028211247 |
| 20240131 | True | 2330 | 台積電 | TWSE | 634.0 | 637.0 | 626.0 | 628.0 | 47554701 | 29978630024 |
