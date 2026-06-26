# Repair Daily Price Range Report

- start_date: `20240401`
- end_date: `20240430`
- check_code: `2330`
- repaired_count: `20`
- skipped_count: `8`
- failed_count: `2`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240401 | repaired | 1132 | 828 | 1960 | full_market_ok | data/daily_price/20240401.csv;data/daily_price/daily_price_20240401.csv |
| 20240402 | repaired | 1136 | 823 | 1959 | full_market_ok | data/daily_price/20240402.csv;data/daily_price/daily_price_20240402.csv |
| 20240403 | repaired | 1131 | 822 | 1953 | full_market_ok | data/daily_price/20240403.csv;data/daily_price/daily_price_20240403.csv |
| 20240404 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/04/04&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240404; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240404; TPEx batch best rows=0; date=20240404 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240405 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/04/05&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240405; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240405; TPEx batch best rows=0; date=20240405 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240406 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240407 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240408 | repaired | 1132 | 829 | 1961 | full_market_ok | data/daily_price/20240408.csv;data/daily_price/daily_price_20240408.csv |
| 20240409 | repaired | 1013 | 829 | 1842 | full_market_ok | data/daily_price/20240409.csv;data/daily_price/daily_price_20240409.csv |
| 20240410 | repaired | 1130 | 824 | 1954 | full_market_ok | data/daily_price/20240410.csv;data/daily_price/daily_price_20240410.csv |
| 20240411 | repaired | 1128 | 828 | 1956 | full_market_ok | data/daily_price/20240411.csv;data/daily_price/daily_price_20240411.csv |
| 20240412 | repaired | 1131 | 826 | 1957 | full_market_ok | data/daily_price/20240412.csv;data/daily_price/daily_price_20240412.csv |
| 20240413 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240414 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240415 | repaired | 1130 | 823 | 1953 | full_market_ok | data/daily_price/20240415.csv;data/daily_price/daily_price_20240415.csv |
| 20240416 | repaired | 1132 | 825 | 1957 | full_market_ok | data/daily_price/20240416.csv;data/daily_price/daily_price_20240416.csv |
| 20240417 | repaired | 1130 | 829 | 1959 | full_market_ok | data/daily_price/20240417.csv;data/daily_price/daily_price_20240417.csv |
| 20240418 | repaired | 1132 | 827 | 1959 | full_market_ok | data/daily_price/20240418.csv;data/daily_price/daily_price_20240418.csv |
| 20240419 | repaired | 1131 | 827 | 1958 | full_market_ok | data/daily_price/20240419.csv;data/daily_price/daily_price_20240419.csv |
| 20240420 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240421 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240422 | repaired | 1133 | 830 | 1963 | full_market_ok | data/daily_price/20240422.csv;data/daily_price/daily_price_20240422.csv |
| 20240423 | repaired | 1132 | 825 | 1957 | full_market_ok | data/daily_price/20240423.csv;data/daily_price/daily_price_20240423.csv |
| 20240424 | repaired | 1133 | 822 | 1955 | full_market_ok | data/daily_price/20240424.csv;data/daily_price/daily_price_20240424.csv |
| 20240425 | repaired | 1128 | 820 | 1948 | full_market_ok | data/daily_price/20240425.csv;data/daily_price/daily_price_20240425.csv |
| 20240426 | repaired | 1128 | 829 | 1957 | full_market_ok | data/daily_price/20240426.csv;data/daily_price/daily_price_20240426.csv |
| 20240427 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240428 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240429 | repaired | 1131 | 827 | 1958 | full_market_ok | data/daily_price/20240429.csv;data/daily_price/daily_price_20240429.csv |
| 20240430 | repaired | 1131 | 825 | 1956 | full_market_ok | data/daily_price/20240430.csv;data/daily_price/daily_price_20240430.csv |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240401 | True | 2330 | 台積電 | TWSE | 783.0 | 783.0 | 769.0 | 770.0 | 22348250 | 17301753062 |
| 20240402 | True | 2330 | 台積電 | TWSE | 784.0 | 790.0 | 783.0 | 790.0 | 42219075 | 33230356267 |
| 20240403 | True | 2330 | 台積電 | TWSE | 783.0 | 785.0 | 778.0 | 780.0 | 32909892 | 25719094412 |
| 20240408 | True | 2330 | 台積電 | TWSE | 789.0 | 792.0 | 783.0 | 783.0 | 40567580 | 31925988285 |
| 20240409 | True | 2330 | 台積電 | TWSE | 795.0 | 820.0 | 792.0 | 819.0 | 61642573 | 49946542596 |
| 20240410 | True | 2330 | 台積電 | TWSE | 815.0 | 819.0 | 810.0 | 815.0 | 31109466 | 25358780514 |
| 20240411 | True | 2330 | 台積電 | TWSE | 811.0 | 820.0 | 811.0 | 820.0 | 27772972 | 22655121636 |
| 20240412 | True | 2330 | 台積電 | TWSE | 823.0 | 826.0 | 817.0 | 818.0 | 32473155 | 26663806808 |
| 20240415 | True | 2330 | 台積電 | TWSE | 804.0 | 812.0 | 803.0 | 806.0 | 41251141 | 33300372097 |
| 20240416 | True | 2330 | 台積電 | TWSE | 802.0 | 803.0 | 785.0 | 788.0 | 54120813 | 42833069476 |
| 20240417 | True | 2330 | 台積電 | TWSE | 798.0 | 808.0 | 793.0 | 804.0 | 36616351 | 29324186091 |
| 20240418 | True | 2330 | 台積電 | TWSE | 796.0 | 810.0 | 792.0 | 804.0 | 45765617 | 36684269610 |
| 20240419 | True | 2330 | 台積電 | TWSE | 769.0 | 770.0 | 746.0 | 750.0 | 143868560 | 109032970933 |
| 20240422 | True | 2330 | 台積電 | TWSE | 740.0 | 757.0 | 740.0 | 742.0 | 52354944 | 39093628250 |
| 20240423 | True | 2330 | 台積電 | TWSE | 761.0 | 761.0 | 752.0 | 754.0 | 32067682 | 24247217869 |
| 20240424 | True | 2330 | 台積電 | TWSE | 770.0 | 785.0 | 769.0 | 783.0 | 41652749 | 32458429294 |
| 20240425 | True | 2330 | 台積電 | TWSE | 770.0 | 774.0 | 765.0 | 766.0 | 30492037 | 23412746667 |
| 20240426 | True | 2330 | 台積電 | TWSE | 788.0 | 789.0 | 782.0 | 782.0 | 34721905 | 27272338208 |
| 20240429 | True | 2330 | 台積電 | TWSE | 790.0 | 795.0 | 787.0 | 795.0 | 30704200 | 24322394064 |
| 20240430 | True | 2330 | 台積電 | TWSE | 797.0 | 802.0 | 790.0 | 790.0 | 41627249 | 33118845170 |
