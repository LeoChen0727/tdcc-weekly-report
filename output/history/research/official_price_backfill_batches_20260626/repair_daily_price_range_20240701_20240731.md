# Repair Daily Price Range Report

- start_date: `20240701`
- end_date: `20240731`
- check_code: `2330`
- repaired_count: `21`
- skipped_count: `8`
- failed_count: `2`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240701 | repaired | 1147 | 831 | 1978 | full_market_ok | data/daily_price/20240701.csv;data/daily_price/daily_price_20240701.csv |
| 20240702 | repaired | 1148 | 834 | 1982 | full_market_ok | data/daily_price/20240702.csv;data/daily_price/daily_price_20240702.csv |
| 20240703 | repaired | 1147 | 829 | 1976 | full_market_ok | data/daily_price/20240703.csv;data/daily_price/daily_price_20240703.csv |
| 20240704 | repaired | 1149 | 832 | 1981 | full_market_ok | data/daily_price/20240704.csv;data/daily_price/daily_price_20240704.csv |
| 20240705 | repaired | 1147 | 831 | 1978 | full_market_ok | data/daily_price/20240705.csv;data/daily_price/daily_price_20240705.csv |
| 20240706 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240707 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240708 | repaired | 1149 | 833 | 1982 | full_market_ok | data/daily_price/20240708.csv;data/daily_price/daily_price_20240708.csv |
| 20240709 | repaired | 1151 | 831 | 1982 | full_market_ok | data/daily_price/20240709.csv;data/daily_price/daily_price_20240709.csv |
| 20240710 | repaired | 1148 | 829 | 1977 | full_market_ok | data/daily_price/20240710.csv;data/daily_price/daily_price_20240710.csv |
| 20240711 | repaired | 1148 | 829 | 1977 | full_market_ok | data/daily_price/20240711.csv;data/daily_price/daily_price_20240711.csv |
| 20240712 | repaired | 1152 | 831 | 1983 | full_market_ok | data/daily_price/20240712.csv;data/daily_price/daily_price_20240712.csv |
| 20240713 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240714 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240715 | repaired | 1144 | 829 | 1973 | full_market_ok | data/daily_price/20240715.csv;data/daily_price/daily_price_20240715.csv |
| 20240716 | repaired | 1146 | 831 | 1977 | full_market_ok | data/daily_price/20240716.csv;data/daily_price/daily_price_20240716.csv |
| 20240717 | repaired | 1148 | 830 | 1978 | full_market_ok | data/daily_price/20240717.csv;data/daily_price/daily_price_20240717.csv |
| 20240718 | repaired | 1149 | 832 | 1981 | full_market_ok | data/daily_price/20240718.csv;data/daily_price/daily_price_20240718.csv |
| 20240719 | repaired | 1147 | 830 | 1977 | full_market_ok | data/daily_price/20240719.csv;data/daily_price/daily_price_20240719.csv |
| 20240720 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240721 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240722 | repaired | 1148 | 827 | 1975 | full_market_ok | data/daily_price/20240722.csv;data/daily_price/daily_price_20240722.csv |
| 20240723 | repaired | 1148 | 832 | 1980 | full_market_ok | data/daily_price/20240723.csv;data/daily_price/daily_price_20240723.csv |
| 20240724 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/07/24&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240724; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240724; TPEx batch best rows=0; date=20240724 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240725 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/07/25&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240725; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240725; TPEx batch best rows=0; date=20240725 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240726 | repaired | 1145 | 829 | 1974 | full_market_ok | data/daily_price/20240726.csv;data/daily_price/daily_price_20240726.csv |
| 20240727 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240728 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240729 | repaired | 1151 | 832 | 1983 | full_market_ok | data/daily_price/20240729.csv;data/daily_price/daily_price_20240729.csv |
| 20240730 | repaired | 1151 | 828 | 1979 | full_market_ok | data/daily_price/20240730.csv;data/daily_price/daily_price_20240730.csv |
| 20240731 | repaired | 1149 | 830 | 1979 | full_market_ok | data/daily_price/20240731.csv;data/daily_price/daily_price_20240731.csv |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240701 | True | 2330 | 台積電 | TWSE | 968.0 | 977.0 | 965.0 | 968.0 | 20936005 | 20320957284 |
| 20240702 | True | 2330 | 台積電 | TWSE | 967.0 | 971.0 | 959.0 | 960.0 | 27992930 | 26971516491 |
| 20240703 | True | 2330 | 台積電 | TWSE | 976.0 | 979.0 | 967.0 | 979.0 | 25022531 | 24386705873 |
| 20240704 | True | 2330 | 台積電 | TWSE | 1000.0 | 1010.0 | 997.0 | 1005.0 | 47251502 | 47347126144 |
| 20240705 | True | 2330 | 台積電 | TWSE | 1005.0 | 1010.0 | 1000.0 | 1005.0 | 21735614 | 21827958195 |
| 20240708 | True | 2330 | 台積電 | TWSE | 1005.0 | 1050.0 | 1000.0 | 1035.0 | 45678332 | 47210175550 |
| 20240709 | True | 2330 | 台積電 | TWSE | 1030.0 | 1055.0 | 1025.0 | 1040.0 | 54339957 | 56382512235 |
| 20240710 | True | 2330 | 台積電 | TWSE | 1020.0 | 1050.0 | 1015.0 | 1045.0 | 51810372 | 53308027550 |
| 20240711 | True | 2330 | 台積電 | TWSE | 1065.0 | 1080.0 | 1055.0 | 1080.0 | 49304453 | 52782475514 |
| 20240712 | True | 2330 | 台積電 | TWSE | 1030.0 | 1045.0 | 1025.0 | 1040.0 | 79472761 | 82222185037 |
| 20240715 | True | 2330 | 台積電 | TWSE | 1040.0 | 1045.0 | 1025.0 | 1040.0 | 44123104 | 45805242410 |
| 20240716 | True | 2330 | 台積電 | TWSE | 1040.0 | 1070.0 | 1035.0 | 1055.0 | 36244442 | 38188299315 |
| 20240717 | True | 2330 | 台積電 | TWSE | 1035.0 | 1045.0 | 1020.0 | 1030.0 | 62390596 | 64372740657 |
| 20240718 | True | 2330 | 台積電 | TWSE | 988.0 | 1005.0 | 986.0 | 1005.0 | 94327431 | 93948039256 |
| 20240719 | True | 2330 | 台積電 | TWSE | 988.0 | 995.0 | 970.0 | 970.0 | 110541544 | 108678133437 |
| 20240722 | True | 2330 | 台積電 | TWSE | 964.0 | 965.0 | 938.0 | 939.0 | 90266550 | 85567920175 |
| 20240723 | True | 2330 | 台積電 | TWSE | 963.0 | 979.0 | 956.0 | 979.0 | 53439290 | 51686291065 |
| 20240726 | True | 2330 | 台積電 | TWSE | 915.0 | 930.0 | 915.0 | 924.0 | 95625050 | 88299582909 |
| 20240729 | True | 2330 | 台積電 | TWSE | 942.0 | 948.0 | 936.0 | 944.0 | 44000914 | 41481319942 |
| 20240730 | True | 2330 | 台積電 | TWSE | 930.0 | 949.0 | 926.0 | 940.0 | 45996400 | 42988422577 |
| 20240731 | True | 2330 | 台積電 | TWSE | 929.0 | 940.0 | 928.0 | 934.0 | 47407263 | 44270020990 |
