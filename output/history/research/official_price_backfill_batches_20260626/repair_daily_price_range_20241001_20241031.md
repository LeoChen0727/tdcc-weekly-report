# Repair Daily Price Range Report

- start_date: `20241001`
- end_date: `20241031`
- check_code: `2330`
- repaired_count: `19`
- skipped_count: `8`
- failed_count: `4`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20241001 | repaired | 1153 | 829 | 1982 | full_market_ok | data/daily_price/20241001.csv;data/daily_price/daily_price_20241001.csv |
| 20241002 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/10/02&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20241002; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20241002; TPEx batch best rows=0; date=20241002 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20241003 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/10/03&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20241003; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20241003; TPEx batch best rows=0; date=20241003 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20241004 | repaired | 1155 | 829 | 1984 | full_market_ok | data/daily_price/20241004.csv;data/daily_price/daily_price_20241004.csv |
| 20241005 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241006 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241007 | repaired | 1159 | 831 | 1990 | full_market_ok | data/daily_price/20241007.csv;data/daily_price/daily_price_20241007.csv |
| 20241008 | repaired | 1154 | 834 | 1988 | full_market_ok | data/daily_price/20241008.csv;data/daily_price/daily_price_20241008.csv |
| 20241009 | repaired | 1150 | 834 | 1984 | full_market_ok | data/daily_price/20241009.csv;data/daily_price/daily_price_20241009.csv |
| 20241010 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/10/10&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20241010; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20241010; TPEx batch best rows=0; date=20241010 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20241011 | repaired | 1154 | 830 | 1984 | full_market_ok | data/daily_price/20241011.csv;data/daily_price/daily_price_20241011.csv |
| 20241012 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241013 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241014 | repaired | 1153 | 825 | 1978 | full_market_ok | data/daily_price/20241014.csv;data/daily_price/daily_price_20241014.csv |
| 20241015 | repaired | 1153 | 836 | 1989 | full_market_ok | data/daily_price/20241015.csv;data/daily_price/daily_price_20241015.csv |
| 20241016 | repaired | 1156 | 826 | 1982 | full_market_ok | data/daily_price/20241016.csv;data/daily_price/daily_price_20241016.csv |
| 20241017 | repaired | 1151 | 825 | 1976 | full_market_ok | data/daily_price/20241017.csv;data/daily_price/daily_price_20241017.csv |
| 20241018 | repaired | 1155 | 836 | 1991 | full_market_ok | data/daily_price/20241018.csv;data/daily_price/daily_price_20241018.csv |
| 20241019 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241020 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241021 | repaired | 1159 | 832 | 1991 | full_market_ok | data/daily_price/20241021.csv;data/daily_price/daily_price_20241021.csv |
| 20241022 | repaired | 1156 | 831 | 1987 | full_market_ok | data/daily_price/20241022.csv;data/daily_price/daily_price_20241022.csv |
| 20241023 | repaired | 1155 | 833 | 1988 | full_market_ok | data/daily_price/20241023.csv;data/daily_price/daily_price_20241023.csv |
| 20241024 | repaired | 1158 | 834 | 1992 | full_market_ok | data/daily_price/20241024.csv;data/daily_price/daily_price_20241024.csv |
| 20241025 | repaired | 1157 | 834 | 1991 | full_market_ok | data/daily_price/20241025.csv;data/daily_price/daily_price_20241025.csv |
| 20241026 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241027 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20241028 | repaired | 1158 | 832 | 1990 | full_market_ok | data/daily_price/20241028.csv;data/daily_price/daily_price_20241028.csv |
| 20241029 | repaired | 1159 | 824 | 1983 | full_market_ok | data/daily_price/20241029.csv;data/daily_price/daily_price_20241029.csv |
| 20241030 | repaired | 1157 | 828 | 1985 | full_market_ok | data/daily_price/20241030.csv;data/daily_price/daily_price_20241030.csv |
| 20241031 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/10/31&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20241031; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20241031; TPEx batch best rows=0; date=20241031 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20241001 | True | 2330 | 台積電 | TWSE | 967.0 | 977.0 | 967.0 | 972.0 | 27877267 | 27093881327 |
| 20241004 | True | 2330 | 台積電 | TWSE | 986.0 | 986.0 | 967.0 | 977.0 | 43765757 | 42845984122 |
| 20241007 | True | 2330 | 台積電 | TWSE | 993.0 | 1010.0 | 989.0 | 1005.0 | 43850831 | 43905376215 |
| 20241008 | True | 2330 | 台積電 | TWSE | 1000.0 | 1010.0 | 997.0 | 1010.0 | 35344059 | 35503172585 |
| 20241009 | True | 2330 | 台積電 | TWSE | 1030.0 | 1035.0 | 1020.0 | 1020.0 | 53208610 | 54663169800 |
| 20241011 | True | 2330 | 台積電 | TWSE | 1025.0 | 1050.0 | 1020.0 | 1045.0 | 47776351 | 49706577415 |
| 20241014 | True | 2330 | 台積電 | TWSE | 1045.0 | 1055.0 | 1035.0 | 1045.0 | 39906157 | 41745442865 |
| 20241015 | True | 2330 | 台積電 | TWSE | 1050.0 | 1075.0 | 1050.0 | 1070.0 | 52066470 | 55504081569 |
| 20241016 | True | 2330 | 台積電 | TWSE | 1040.0 | 1070.0 | 1035.0 | 1045.0 | 60312846 | 63228552464 |
| 20241017 | True | 2330 | 台積電 | TWSE | 1050.0 | 1055.0 | 1030.0 | 1035.0 | 56618332 | 58862054838 |
| 20241018 | True | 2330 | 台積電 | TWSE | 1095.0 | 1100.0 | 1075.0 | 1085.0 | 91036335 | 99230303460 |
| 20241021 | True | 2330 | 台積電 | TWSE | 1090.0 | 1095.0 | 1080.0 | 1085.0 | 42094031 | 45813114865 |
| 20241022 | True | 2330 | 台積電 | TWSE | 1065.0 | 1075.0 | 1060.0 | 1075.0 | 43740591 | 46707090730 |
| 20241023 | True | 2330 | 台積電 | TWSE | 1060.0 | 1070.0 | 1055.0 | 1060.0 | 32895421 | 34912308143 |
| 20241024 | True | 2330 | 台積電 | TWSE | 1070.0 | 1075.0 | 1055.0 | 1060.0 | 40791484 | 43477824029 |
| 20241025 | True | 2330 | 台積電 | TWSE | 1065.0 | 1070.0 | 1060.0 | 1065.0 | 23347890 | 24867260319 |
| 20241028 | True | 2330 | 台積電 | TWSE | 1075.0 | 1080.0 | 1050.0 | 1050.0 | 41665065 | 44216316045 |
| 20241029 | True | 2330 | 台積電 | TWSE | 1035.0 | 1040.0 | 1020.0 | 1040.0 | 48097705 | 49680152085 |
| 20241030 | True | 2330 | 台積電 | TWSE | 1040.0 | 1055.0 | 1030.0 | 1030.0 | 40765247 | 42368799669 |
