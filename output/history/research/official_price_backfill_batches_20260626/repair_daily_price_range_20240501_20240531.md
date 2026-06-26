# Repair Daily Price Range Report

- start_date: `20240501`
- end_date: `20240531`
- check_code: `2330`
- repaired_count: `22`
- skipped_count: `8`
- failed_count: `1`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240501 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/05/01&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240501; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240501; TPEx batch best rows=0; date=20240501 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240502 | repaired | 1131 | 827 | 1958 | full_market_ok | data/daily_price/20240502.csv;data/daily_price/daily_price_20240502.csv |
| 20240503 | repaired | 1130 | 826 | 1956 | full_market_ok | data/daily_price/20240503.csv;data/daily_price/daily_price_20240503.csv |
| 20240504 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240505 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240506 | repaired | 1135 | 826 | 1961 | full_market_ok | data/daily_price/20240506.csv;data/daily_price/daily_price_20240506.csv |
| 20240507 | repaired | 1130 | 822 | 1952 | full_market_ok | data/daily_price/20240507.csv;data/daily_price/daily_price_20240507.csv |
| 20240508 | repaired | 1128 | 827 | 1955 | full_market_ok | data/daily_price/20240508.csv;data/daily_price/daily_price_20240508.csv |
| 20240509 | repaired | 1135 | 826 | 1961 | full_market_ok | data/daily_price/20240509.csv;data/daily_price/daily_price_20240509.csv |
| 20240510 | repaired | 1136 | 831 | 1967 | full_market_ok | data/daily_price/20240510.csv;data/daily_price/daily_price_20240510.csv |
| 20240511 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240512 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240513 | repaired | 1135 | 828 | 1963 | full_market_ok | data/daily_price/20240513.csv;data/daily_price/daily_price_20240513.csv |
| 20240514 | repaired | 1136 | 826 | 1962 | full_market_ok | data/daily_price/20240514.csv;data/daily_price/daily_price_20240514.csv |
| 20240515 | repaired | 1138 | 829 | 1967 | full_market_ok | data/daily_price/20240515.csv;data/daily_price/daily_price_20240515.csv |
| 20240516 | repaired | 1142 | 828 | 1970 | full_market_ok | data/daily_price/20240516.csv;data/daily_price/daily_price_20240516.csv |
| 20240517 | repaired | 1139 | 828 | 1967 | full_market_ok | data/daily_price/20240517.csv;data/daily_price/daily_price_20240517.csv |
| 20240518 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240519 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240520 | repaired | 1144 | 821 | 1965 | full_market_ok | data/daily_price/20240520.csv;data/daily_price/daily_price_20240520.csv |
| 20240521 | repaired | 1139 | 823 | 1962 | full_market_ok | data/daily_price/20240521.csv;data/daily_price/daily_price_20240521.csv |
| 20240522 | repaired | 1144 | 829 | 1973 | full_market_ok | data/daily_price/20240522.csv;data/daily_price/daily_price_20240522.csv |
| 20240523 | repaired | 1144 | 829 | 1973 | full_market_ok | data/daily_price/20240523.csv;data/daily_price/daily_price_20240523.csv |
| 20240524 | repaired | 1137 | 826 | 1963 | full_market_ok | data/daily_price/20240524.csv;data/daily_price/daily_price_20240524.csv |
| 20240525 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240526 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240527 | repaired | 1141 | 828 | 1969 | full_market_ok | data/daily_price/20240527.csv;data/daily_price/daily_price_20240527.csv |
| 20240528 | repaired | 1142 | 828 | 1970 | full_market_ok | data/daily_price/20240528.csv;data/daily_price/daily_price_20240528.csv |
| 20240529 | repaired | 1138 | 829 | 1967 | full_market_ok | data/daily_price/20240529.csv;data/daily_price/daily_price_20240529.csv |
| 20240530 | repaired | 1142 | 824 | 1966 | full_market_ok | data/daily_price/20240530.csv;data/daily_price/daily_price_20240530.csv |
| 20240531 | repaired | 1144 | 828 | 1972 | full_market_ok | data/daily_price/20240531.csv;data/daily_price/daily_price_20240531.csv |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240502 | True | 2330 | 台積電 | TWSE | 789.0 | 789.0 | 772.0 | 772.0 | 47536363 | 36983047647 |
| 20240503 | True | 2330 | 台積電 | TWSE | 788.0 | 788.0 | 773.0 | 780.0 | 31026748 | 24240817990 |
| 20240506 | True | 2330 | 台積電 | TWSE | 791.0 | 793.0 | 786.0 | 786.0 | 33733509 | 26644713164 |
| 20240507 | True | 2330 | 台積電 | TWSE | 797.0 | 800.0 | 792.0 | 800.0 | 35917824 | 28623349239 |
| 20240508 | True | 2330 | 台積電 | TWSE | 794.0 | 802.0 | 792.0 | 802.0 | 22585765 | 18032263877 |
| 20240509 | True | 2330 | 台積電 | TWSE | 798.0 | 802.0 | 796.0 | 796.0 | 22863681 | 18267303103 |
| 20240510 | True | 2330 | 台積電 | TWSE | 803.0 | 807.0 | 798.0 | 802.0 | 27560431 | 22107595449 |
| 20240513 | True | 2330 | 台積電 | TWSE | 823.0 | 825.0 | 818.0 | 819.0 | 38146948 | 31315059679 |
| 20240514 | True | 2330 | 台積電 | TWSE | 816.0 | 825.0 | 811.0 | 825.0 | 29663617 | 24309306615 |
| 20240515 | True | 2330 | 台積電 | TWSE | 838.0 | 844.0 | 837.0 | 839.0 | 41805778 | 35112739055 |
| 20240516 | True | 2330 | 台積電 | TWSE | 852.0 | 856.0 | 837.0 | 841.0 | 46276890 | 39179826883 |
| 20240517 | True | 2330 | 台積電 | TWSE | 848.0 | 848.0 | 834.0 | 835.0 | 27855719 | 23373478247 |
| 20240520 | True | 2330 | 台積電 | TWSE | 834.0 | 838.0 | 822.0 | 835.0 | 30148330 | 25069342221 |
| 20240521 | True | 2330 | 台積電 | TWSE | 830.0 | 841.0 | 830.0 | 841.0 | 20548110 | 17214095315 |
| 20240522 | True | 2330 | 台積電 | TWSE | 845.0 | 865.0 | 843.0 | 864.0 | 40904357 | 35027824713 |
| 20240523 | True | 2330 | 台積電 | TWSE | 875.0 | 877.0 | 867.0 | 875.0 | 40771207 | 35638205695 |
| 20240524 | True | 2330 | 台積電 | TWSE | 858.0 | 872.0 | 858.0 | 867.0 | 37353467 | 32358555678 |
| 20240527 | True | 2330 | 台積電 | TWSE | 872.0 | 878.0 | 866.0 | 869.0 | 32691921 | 28496096179 |
| 20240528 | True | 2330 | 台積電 | TWSE | 867.0 | 873.0 | 865.0 | 865.0 | 32712504 | 28375286215 |
| 20240529 | True | 2330 | 台積電 | TWSE | 861.0 | 868.0 | 856.0 | 857.0 | 51073346 | 43924367680 |
| 20240530 | True | 2330 | 台積電 | TWSE | 841.0 | 848.0 | 838.0 | 838.0 | 42535118 | 35840589611 |
| 20240531 | True | 2330 | 台積電 | TWSE | 838.0 | 846.0 | 821.0 | 821.0 | 90177283 | 74602358441 |
