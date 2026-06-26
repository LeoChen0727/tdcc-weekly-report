# Repair Daily Price Range Report

- start_date: `20240601`
- end_date: `20240630`
- check_code: `2330`
- repaired_count: `19`
- skipped_count: `10`
- failed_count: `1`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240601 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240602 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240603 | repaired | 1142 | 828 | 1970 | full_market_ok | data/daily_price/20240603.csv;data/daily_price/daily_price_20240603.csv |
| 20240604 | repaired | 1138 | 823 | 1961 | full_market_ok | data/daily_price/20240604.csv;data/daily_price/daily_price_20240604.csv |
| 20240605 | repaired | 1141 | 827 | 1968 | full_market_ok | data/daily_price/20240605.csv;data/daily_price/daily_price_20240605.csv |
| 20240606 | repaired | 1138 | 828 | 1966 | full_market_ok | data/daily_price/20240606.csv;data/daily_price/daily_price_20240606.csv |
| 20240607 | repaired | 1136 | 824 | 1960 | full_market_ok | data/daily_price/20240607.csv;data/daily_price/daily_price_20240607.csv |
| 20240608 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240609 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240610 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/06/10&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240610; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240610; TPEx batch best rows=0; date=20240610 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240611 | repaired | 1141 | 829 | 1970 | full_market_ok | data/daily_price/20240611.csv;data/daily_price/daily_price_20240611.csv |
| 20240612 | repaired | 1145 | 828 | 1973 | full_market_ok | data/daily_price/20240612.csv;data/daily_price/daily_price_20240612.csv |
| 20240613 | repaired | 1146 | 830 | 1976 | full_market_ok | data/daily_price/20240613.csv;data/daily_price/daily_price_20240613.csv |
| 20240614 | repaired | 1144 | 828 | 1972 | full_market_ok | data/daily_price/20240614.csv;data/daily_price/daily_price_20240614.csv |
| 20240615 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240616 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240617 | repaired | 1144 | 829 | 1973 | full_market_ok | data/daily_price/20240617.csv;data/daily_price/daily_price_20240617.csv |
| 20240618 | repaired | 1147 | 829 | 1976 | full_market_ok | data/daily_price/20240618.csv;data/daily_price/daily_price_20240618.csv |
| 20240619 | repaired | 1146 | 829 | 1975 | full_market_ok | data/daily_price/20240619.csv;data/daily_price/daily_price_20240619.csv |
| 20240620 | repaired | 1142 | 830 | 1972 | full_market_ok | data/daily_price/20240620.csv;data/daily_price/daily_price_20240620.csv |
| 20240621 | repaired | 1144 | 828 | 1972 | full_market_ok | data/daily_price/20240621.csv;data/daily_price/daily_price_20240621.csv |
| 20240622 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240623 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240624 | repaired | 1146 | 827 | 1973 | full_market_ok | data/daily_price/20240624.csv;data/daily_price/daily_price_20240624.csv |
| 20240625 | repaired | 1143 | 824 | 1967 | full_market_ok | data/daily_price/20240625.csv;data/daily_price/daily_price_20240625.csv |
| 20240626 | repaired | 1147 | 831 | 1978 | full_market_ok | data/daily_price/20240626.csv;data/daily_price/daily_price_20240626.csv |
| 20240627 | repaired | 1146 | 824 | 1970 | full_market_ok | data/daily_price/20240627.csv;data/daily_price/daily_price_20240627.csv |
| 20240628 | repaired | 1149 | 831 | 1980 | full_market_ok | data/daily_price/20240628.csv;data/daily_price/daily_price_20240628.csv |
| 20240629 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240630 | skipped_weekend | 0 | 0 | 0 | weekend |  |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240603 | True | 2330 | 台積電 | TWSE | 839.0 | 853.0 | 837.0 | 846.0 | 29629706 | 25053781742 |
| 20240604 | True | 2330 | 台積電 | TWSE | 844.0 | 851.0 | 837.0 | 839.0 | 31031104 | 26107162214 |
| 20240605 | True | 2330 | 台積電 | TWSE | 841.0 | 857.0 | 835.0 | 854.0 | 37531781 | 31774150536 |
| 20240606 | True | 2330 | 台積電 | TWSE | 893.0 | 899.0 | 885.0 | 894.0 | 67300344 | 60138015941 |
| 20240607 | True | 2330 | 台積電 | TWSE | 885.0 | 888.0 | 879.0 | 879.0 | 44489018 | 39240336617 |
| 20240611 | True | 2330 | 台積電 | TWSE | 892.0 | 895.0 | 883.0 | 883.0 | 57435637 | 51091497348 |
| 20240612 | True | 2330 | 台積電 | TWSE | 888.0 | 914.0 | 888.0 | 909.0 | 51874967 | 46791431521 |
| 20240613 | True | 2330 | 台積電 | TWSE | 923.0 | 935.0 | 911.0 | 919.0 | 59656092 | 54980784829 |
| 20240614 | True | 2330 | 台積電 | TWSE | 916.0 | 922.0 | 905.0 | 922.0 | 43289572 | 39603293460 |
| 20240617 | True | 2330 | 台積電 | TWSE | 913.0 | 925.0 | 913.0 | 921.0 | 28796529 | 26475733502 |
| 20240618 | True | 2330 | 台積電 | TWSE | 944.0 | 950.0 | 940.0 | 943.0 | 40870419 | 38583515635 |
| 20240619 | True | 2330 | 台積電 | TWSE | 953.0 | 984.0 | 953.0 | 981.0 | 76684138 | 74395758883 |
| 20240620 | True | 2330 | 台積電 | TWSE | 971.0 | 981.0 | 971.0 | 981.0 | 52144900 | 50859632569 |
| 20240621 | True | 2330 | 台積電 | TWSE | 961.0 | 978.0 | 960.0 | 970.0 | 97995843 | 94882220706 |
| 20240624 | True | 2330 | 台積電 | TWSE | 958.0 | 960.0 | 940.0 | 940.0 | 74081708 | 70162177693 |
| 20240625 | True | 2330 | 台積電 | TWSE | 925.0 | 945.0 | 923.0 | 945.0 | 62079701 | 57978440842 |
| 20240626 | True | 2330 | 台積電 | TWSE | 951.0 | 960.0 | 951.0 | 960.0 | 48821135 | 46668874056 |
| 20240627 | True | 2330 | 台積電 | TWSE | 951.0 | 961.0 | 949.0 | 960.0 | 41276086 | 39447006518 |
| 20240628 | True | 2330 | 台積電 | TWSE | 956.0 | 971.0 | 955.0 | 966.0 | 42998776 | 41476565443 |
