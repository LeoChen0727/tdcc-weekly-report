# Repair Daily Price Range Report

- start_date: `20250201`
- end_date: `20250228`
- check_code: `2330`
- repaired_count: `19`
- skipped_count: `8`
- failed_count: `1`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20250201 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250202 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250203 | repaired | 1179 | 832 | 2011 | full_market_ok | data/daily_price/20250203.csv;data/daily_price/daily_price_20250203.csv |
| 20250204 | repaired | 1176 | 833 | 2009 | full_market_ok | data/daily_price/20250204.csv;data/daily_price/daily_price_20250204.csv |
| 20250205 | repaired | 1178 | 839 | 2017 | full_market_ok | data/daily_price/20250205.csv;data/daily_price/daily_price_20250205.csv |
| 20250206 | repaired | 1172 | 838 | 2010 | full_market_ok | data/daily_price/20250206.csv;data/daily_price/daily_price_20250206.csv |
| 20250207 | repaired | 1170 | 846 | 2016 | full_market_ok | data/daily_price/20250207.csv;data/daily_price/daily_price_20250207.csv |
| 20250208 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250209 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250210 | repaired | 1174 | 843 | 2017 | full_market_ok | data/daily_price/20250210.csv;data/daily_price/daily_price_20250210.csv |
| 20250211 | repaired | 1176 | 838 | 2014 | full_market_ok | data/daily_price/20250211.csv;data/daily_price/daily_price_20250211.csv |
| 20250212 | repaired | 1178 | 834 | 2012 | full_market_ok | data/daily_price/20250212.csv;data/daily_price/daily_price_20250212.csv |
| 20250213 | repaired | 1180 | 843 | 2023 | full_market_ok | data/daily_price/20250213.csv;data/daily_price/daily_price_20250213.csv |
| 20250214 | repaired | 1177 | 844 | 2021 | full_market_ok | data/daily_price/20250214.csv;data/daily_price/daily_price_20250214.csv |
| 20250215 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250216 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250217 | repaired | 1177 | 845 | 2022 | full_market_ok | data/daily_price/20250217.csv;data/daily_price/daily_price_20250217.csv |
| 20250218 | repaired | 1173 | 843 | 2016 | full_market_ok | data/daily_price/20250218.csv;data/daily_price/daily_price_20250218.csv |
| 20250219 | repaired | 1179 | 844 | 2023 | full_market_ok | data/daily_price/20250219.csv;data/daily_price/daily_price_20250219.csv |
| 20250220 | repaired | 1179 | 843 | 2022 | full_market_ok | data/daily_price/20250220.csv;data/daily_price/daily_price_20250220.csv |
| 20250221 | repaired | 1041 | 847 | 1888 | full_market_ok | data/daily_price/20250221.csv;data/daily_price/daily_price_20250221.csv |
| 20250222 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250223 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250224 | repaired | 1178 | 841 | 2019 | full_market_ok | data/daily_price/20250224.csv;data/daily_price/daily_price_20250224.csv |
| 20250225 | repaired | 1176 | 837 | 2013 | full_market_ok | data/daily_price/20250225.csv;data/daily_price/daily_price_20250225.csv |
| 20250226 | repaired | 1176 | 843 | 2019 | full_market_ok | data/daily_price/20250226.csv;data/daily_price/daily_price_20250226.csv |
| 20250227 | repaired | 1173 | 846 | 2019 | full_market_ok | data/daily_price/20250227.csv;data/daily_price/daily_price_20250227.csv |
| 20250228 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/02/28&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250228; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250228; TPEx batch best rows=0; date=20250228 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20250203 | True | 2330 | 台積電 | TWSE | 1065.0 | 1075.0 | 1060.0 | 1070.0 | 113031525 | 120769676393 |
| 20250204 | True | 2330 | 台積電 | TWSE | 1085.0 | 1100.0 | 1080.0 | 1095.0 | 57904652 | 63132252012 |
| 20250205 | True | 2330 | 台積電 | TWSE | 1110.0 | 1120.0 | 1105.0 | 1110.0 | 43082532 | 47931709801 |
| 20250206 | True | 2330 | 台積電 | TWSE | 1120.0 | 1120.0 | 1105.0 | 1115.0 | 33768196 | 37638807097 |
| 20250207 | True | 2330 | 台積電 | TWSE | 1110.0 | 1125.0 | 1105.0 | 1125.0 | 31107545 | 34745052940 |
| 20250210 | True | 2330 | 台積電 | TWSE | 1125.0 | 1125.0 | 1095.0 | 1105.0 | 31037109 | 34425517969 |
| 20250211 | True | 2330 | 台積電 | TWSE | 1110.0 | 1115.0 | 1100.0 | 1110.0 | 21023057 | 23294288731 |
| 20250212 | True | 2330 | 台積電 | TWSE | 1110.0 | 1115.0 | 1100.0 | 1100.0 | 26190392 | 28966591975 |
| 20250213 | True | 2330 | 台積電 | TWSE | 1090.0 | 1095.0 | 1080.0 | 1090.0 | 35681521 | 38806197999 |
| 20250214 | True | 2330 | 台積電 | TWSE | 1065.0 | 1070.0 | 1060.0 | 1060.0 | 73417323 | 78100130074 |
| 20250217 | True | 2330 | 台積電 | TWSE | 1065.0 | 1085.0 | 1065.0 | 1085.0 | 37215861 | 40057489554 |
| 20250218 | True | 2330 | 台積電 | TWSE | 1085.0 | 1100.0 | 1080.0 | 1100.0 | 24018940 | 26204727000 |
| 20250219 | True | 2330 | 台積電 | TWSE | 1090.0 | 1095.0 | 1085.0 | 1090.0 | 28756849 | 31328641002 |
| 20250220 | True | 2330 | 台積電 | TWSE | 1080.0 | 1085.0 | 1070.0 | 1080.0 | 31108197 | 33537160793 |
| 20250221 | True | 2330 | 台積電 | TWSE | 1085.0 | 1095.0 | 1080.0 | 1095.0 | 31480715 | 34322859039 |
| 20250224 | True | 2330 | 台積電 | TWSE | 1080.0 | 1085.0 | 1075.0 | 1075.0 | 33837606 | 36461265148 |
| 20250225 | True | 2330 | 台積電 | TWSE | 1055.0 | 1060.0 | 1050.0 | 1055.0 | 53174277 | 56084293935 |
| 20250226 | True | 2330 | 台積電 | TWSE | 1045.0 | 1060.0 | 1045.0 | 1060.0 | 42921499 | 45208281264 |
| 20250227 | True | 2330 | 台積電 | TWSE | 1085.0 | 1100.0 | 1080.0 | 1100.0 | 24018940 | 26204727000 |
