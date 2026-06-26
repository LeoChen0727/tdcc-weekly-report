# Repair Daily Price Range Report

- start_date: `20250101`
- end_date: `20250131`
- check_code: `2330`
- repaired_count: `15`
- skipped_count: `8`
- failed_count: `8`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20250101 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/01&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250101; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250101; TPEx batch best rows=0; date=20250101 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250102 | repaired | 1174 | 839 | 2013 | full_market_ok | data/daily_price/20250102.csv;data/daily_price/daily_price_20250102.csv |
| 20250103 | repaired | 1173 | 833 | 2006 | full_market_ok | data/daily_price/20250103.csv;data/daily_price/daily_price_20250103.csv |
| 20250104 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250105 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250106 | repaired | 1041 | 834 | 1875 | full_market_ok | data/daily_price/20250106.csv;data/daily_price/daily_price_20250106.csv |
| 20250107 | repaired | 1175 | 835 | 2010 | full_market_ok | data/daily_price/20250107.csv;data/daily_price/daily_price_20250107.csv |
| 20250108 | repaired | 1169 | 838 | 2007 | full_market_ok | data/daily_price/20250108.csv;data/daily_price/daily_price_20250108.csv |
| 20250109 | repaired | 1173 | 840 | 2013 | full_market_ok | data/daily_price/20250109.csv;data/daily_price/daily_price_20250109.csv |
| 20250110 | repaired | 1174 | 834 | 2008 | full_market_ok | data/daily_price/20250110.csv;data/daily_price/daily_price_20250110.csv |
| 20250111 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250112 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250113 | repaired | 1175 | 841 | 2016 | full_market_ok | data/daily_price/20250113.csv;data/daily_price/daily_price_20250113.csv |
| 20250114 | repaired | 1172 | 836 | 2008 | full_market_ok | data/daily_price/20250114.csv;data/daily_price/daily_price_20250114.csv |
| 20250115 | repaired | 1177 | 832 | 2009 | full_market_ok | data/daily_price/20250115.csv;data/daily_price/daily_price_20250115.csv |
| 20250116 | repaired | 1177 | 838 | 2015 | full_market_ok | data/daily_price/20250116.csv;data/daily_price/daily_price_20250116.csv |
| 20250117 | repaired | 1208 | 832 | 2040 | full_market_ok | data/daily_price/20250117.csv;data/daily_price/daily_price_20250117.csv |
| 20250118 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250119 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250120 | repaired | 1176 | 833 | 2009 | full_market_ok | data/daily_price/20250120.csv;data/daily_price/daily_price_20250120.csv |
| 20250121 | repaired | 1173 | 834 | 2007 | full_market_ok | data/daily_price/20250121.csv;data/daily_price/daily_price_20250121.csv |
| 20250122 | repaired | 1175 | 841 | 2016 | full_market_ok | data/daily_price/20250122.csv;data/daily_price/daily_price_20250122.csv |
| 20250123 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/23&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250123; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250123; TPEx batch best rows=0; date=20250123 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250124 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/24&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250124; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250124; TPEx batch best rows=0; date=20250124 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250125 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250126 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20250127 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/27&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250127; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250127; TPEx batch best rows=0; date=20250127 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250128 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/28&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250128; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250128; TPEx batch best rows=0; date=20250128 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250129 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/29&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250129; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250129; TPEx batch best rows=0; date=20250129 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250130 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/30&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250130; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250130; TPEx batch best rows=0; date=20250130 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20250131 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/31&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250131; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250131; TPEx batch best rows=0; date=20250131 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20250102 | True | 2330 | 台積電 | TWSE | 1070.0 | 1075.0 | 1055.0 | 1065.0 | 45045125 | 47883206644 |
| 20250103 | True | 2330 | 台積電 | TWSE | 1080.0 | 1085.0 | 1075.0 | 1075.0 | 31244211 | 33728652860 |
| 20250106 | True | 2330 | 台積電 | TWSE | 1100.0 | 1125.0 | 1095.0 | 1125.0 | 77874801 | 86585128825 |
| 20250107 | True | 2330 | 台積電 | TWSE | 1150.0 | 1160.0 | 1130.0 | 1130.0 | 54691485 | 62664127156 |
| 20250108 | True | 2330 | 台積電 | TWSE | 1110.0 | 1130.0 | 1105.0 | 1105.0 | 49181518 | 54760296689 |
| 20250109 | True | 2330 | 台積電 | TWSE | 1100.0 | 1115.0 | 1100.0 | 1100.0 | 29916198 | 33052210793 |
| 20250110 | True | 2330 | 台積電 | TWSE | 1100.0 | 1110.0 | 1100.0 | 1100.0 | 24475751 | 26996697889 |
| 20250113 | True | 2330 | 台積電 | TWSE | 1110.0 | 1115.0 | 1070.0 | 1075.0 | 62629547 | 68093421797 |
| 20250114 | True | 2330 | 台積電 | TWSE | 1085.0 | 1090.0 | 1075.0 | 1090.0 | 31280235 | 33915048410 |
| 20250115 | True | 2330 | 台積電 | TWSE | 1085.0 | 1085.0 | 1065.0 | 1065.0 | 37966582 | 40677529813 |
| 20250116 | True | 2330 | 台積電 | TWSE | 1095.0 | 1115.0 | 1090.0 | 1105.0 | 49872673 | 54934128041 |
| 20250117 | True | 2330 | 台積電 | TWSE | 1420.0 | 1435.0 | 1415.0 | 1430.0 | 33103697 | 47179906765 |
| 20250120 | True | 2330 | 台積電 | TWSE | 1125.0 | 1135.0 | 1120.0 | 1120.0 | 32062171 | 36076248367 |
| 20250121 | True | 2330 | 台積電 | TWSE | 1115.0 | 1125.0 | 1110.0 | 1120.0 | 24368832 | 27256307475 |
| 20250122 | True | 2330 | 台積電 | TWSE | 1140.0 | 1150.0 | 1135.0 | 1135.0 | 45996696 | 52510666410 |
