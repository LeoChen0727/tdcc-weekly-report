# Repair Daily Price Range Report

- start_date: `20240201`
- end_date: `20240229`
- check_code: `2330`
- repaired_count: `13`
- skipped_count: `8`
- failed_count: `8`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240201 | repaired | 1128 | 817 | 1945 | full_market_ok | data/daily_price/20240201.csv;data/daily_price/daily_price_20240201.csv |
| 20240202 | repaired | 1125 | 820 | 1945 | full_market_ok | data/daily_price/20240202.csv;data/daily_price/daily_price_20240202.csv |
| 20240203 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240204 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240205 | repaired | 1126 | 818 | 1944 | full_market_ok | data/daily_price/20240205.csv;data/daily_price/daily_price_20240205.csv |
| 20240206 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/06&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240206; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240206; TPEx batch best rows=0; date=20240206 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240207 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/07&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240207; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240207; TPEx batch best rows=0; date=20240207 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240208 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/08&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240208; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240208; TPEx batch best rows=0; date=20240208 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240209 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/09&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240209; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240209; TPEx batch best rows=0; date=20240209 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240210 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240211 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240212 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/12&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240212; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240212; TPEx batch best rows=0; date=20240212 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240213 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/13&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240213; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240213; TPEx batch best rows=0; date=20240213 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240214 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/14&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240214; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240214; TPEx batch best rows=0; date=20240214 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240215 | repaired | 1128 | 820 | 1948 | full_market_ok | data/daily_price/20240215.csv;data/daily_price/daily_price_20240215.csv |
| 20240216 | repaired | 1130 | 821 | 1951 | full_market_ok | data/daily_price/20240216.csv;data/daily_price/daily_price_20240216.csv |
| 20240217 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240218 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240219 | repaired | 1129 | 824 | 1953 | full_market_ok | data/daily_price/20240219.csv;data/daily_price/daily_price_20240219.csv |
| 20240220 | repaired | 1126 | 817 | 1943 | full_market_ok | data/daily_price/20240220.csv;data/daily_price/daily_price_20240220.csv |
| 20240221 | repaired | 1128 | 817 | 1945 | full_market_ok | data/daily_price/20240221.csv;data/daily_price/daily_price_20240221.csv |
| 20240222 | repaired | 1011 | 818 | 1829 | full_market_ok | data/daily_price/20240222.csv;data/daily_price/daily_price_20240222.csv |
| 20240223 | repaired | 1128 | 821 | 1949 | full_market_ok | data/daily_price/20240223.csv;data/daily_price/daily_price_20240223.csv |
| 20240224 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240225 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240226 | repaired | 1128 | 819 | 1947 | full_market_ok | data/daily_price/20240226.csv;data/daily_price/daily_price_20240226.csv |
| 20240227 | repaired | 1128 | 818 | 1946 | full_market_ok | data/daily_price/20240227.csv;data/daily_price/daily_price_20240227.csv |
| 20240228 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/02/28&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240228; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240228; TPEx batch best rows=0; date=20240228 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240229 | repaired | 1127 | 823 | 1950 | full_market_ok | data/daily_price/20240229.csv;data/daily_price/daily_price_20240229.csv |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240201 | True | 2330 | 台積電 | TWSE | 625.0 | 628.0 | 619.0 | 628.0 | 46924943 | 29237425981 |
| 20240202 | True | 2330 | 台積電 | TWSE | 633.0 | 635.0 | 628.0 | 635.0 | 27797894 | 17563853315 |
| 20240205 | True | 2330 | 台積電 | TWSE | 645.0 | 647.0 | 638.0 | 646.0 | 48037344 | 30931242935 |
| 20240215 | True | 2330 | 台積電 | TWSE | 709.0 | 709.0 | 693.0 | 697.0 | 132263803 | 92592826951 |
| 20240216 | True | 2330 | 台積電 | TWSE | 697.0 | 699.0 | 683.0 | 683.0 | 48963167 | 33742716965 |
| 20240219 | True | 2330 | 台積電 | TWSE | 674.0 | 682.0 | 674.0 | 678.0 | 36366837 | 24665534552 |
| 20240220 | True | 2330 | 台積電 | TWSE | 675.0 | 688.0 | 675.0 | 687.0 | 31403730 | 21494427969 |
| 20240221 | True | 2330 | 台積電 | TWSE | 678.0 | 683.0 | 678.0 | 681.0 | 31980543 | 21748906940 |
| 20240222 | True | 2330 | 台積電 | TWSE | 695.0 | 695.0 | 685.0 | 692.0 | 34269392 | 23664176835 |
| 20240223 | True | 2330 | 台積電 | TWSE | 701.0 | 703.0 | 696.0 | 697.0 | 48404478 | 33847447281 |
| 20240226 | True | 2330 | 台積電 | TWSE | 700.0 | 700.0 | 695.0 | 698.0 | 29976379 | 20917136411 |
| 20240227 | True | 2330 | 台積電 | TWSE | 700.0 | 701.0 | 691.0 | 698.0 | 35389548 | 24647159479 |
| 20240229 | True | 2330 | 台積電 | TWSE | 691.0 | 698.0 | 688.0 | 690.0 | 59337072 | 40973093720 |
