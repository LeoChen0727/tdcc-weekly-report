# Repair Daily Price Range Report

- start_date: `20240901`
- end_date: `20240930`
- check_code: `2330`
- repaired_count: `20`
- skipped_count: `9`
- failed_count: `1`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20240901 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240902 | repaired | 1149 | 822 | 1971 | full_market_ok | data/daily_price/20240902.csv;data/daily_price/daily_price_20240902.csv |
| 20240903 | repaired | 1148 | 821 | 1969 | full_market_ok | data/daily_price/20240903.csv;data/daily_price/daily_price_20240903.csv |
| 20240904 | repaired | 1152 | 828 | 1980 | full_market_ok | data/daily_price/20240904.csv;data/daily_price/daily_price_20240904.csv |
| 20240905 | repaired | 1153 | 827 | 1980 | full_market_ok | data/daily_price/20240905.csv;data/daily_price/daily_price_20240905.csv |
| 20240906 | repaired | 1149 | 822 | 1971 | full_market_ok | data/daily_price/20240906.csv;data/daily_price/daily_price_20240906.csv |
| 20240907 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240908 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240909 | repaired | 1150 | 821 | 1971 | full_market_ok | data/daily_price/20240909.csv;data/daily_price/daily_price_20240909.csv |
| 20240910 | repaired | 1150 | 831 | 1981 | full_market_ok | data/daily_price/20240910.csv;data/daily_price/daily_price_20240910.csv |
| 20240911 | repaired | 1151 | 823 | 1974 | full_market_ok | data/daily_price/20240911.csv;data/daily_price/daily_price_20240911.csv |
| 20240912 | repaired | 1153 | 830 | 1983 | full_market_ok | data/daily_price/20240912.csv;data/daily_price/daily_price_20240912.csv |
| 20240913 | repaired | 1151 | 828 | 1979 | full_market_ok | data/daily_price/20240913.csv;data/daily_price/daily_price_20240913.csv |
| 20240914 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240915 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240916 | repaired | 1151 | 830 | 1981 | full_market_ok | data/daily_price/20240916.csv;data/daily_price/daily_price_20240916.csv |
| 20240917 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=113/09/17&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20240917; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20240917; TPEx batch best rows=0; date=20240917 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
| 20240918 | repaired | 1152 | 833 | 1985 | full_market_ok | data/daily_price/20240918.csv;data/daily_price/daily_price_20240918.csv |
| 20240919 | repaired | 1151 | 828 | 1979 | full_market_ok | data/daily_price/20240919.csv;data/daily_price/daily_price_20240919.csv |
| 20240920 | repaired | 1153 | 834 | 1987 | full_market_ok | data/daily_price/20240920.csv;data/daily_price/daily_price_20240920.csv |
| 20240921 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240922 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240923 | repaired | 1151 | 833 | 1984 | full_market_ok | data/daily_price/20240923.csv;data/daily_price/daily_price_20240923.csv |
| 20240924 | repaired | 1150 | 825 | 1975 | full_market_ok | data/daily_price/20240924.csv;data/daily_price/daily_price_20240924.csv |
| 20240925 | repaired | 1154 | 832 | 1986 | full_market_ok | data/daily_price/20240925.csv;data/daily_price/daily_price_20240925.csv |
| 20240926 | repaired | 1154 | 830 | 1984 | full_market_ok | data/daily_price/20240926.csv;data/daily_price/daily_price_20240926.csv |
| 20240927 | repaired | 1155 | 833 | 1988 | full_market_ok | data/daily_price/20240927.csv;data/daily_price/daily_price_20240927.csv |
| 20240928 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240929 | skipped_weekend | 0 | 0 | 0 | weekend |  |
| 20240930 | repaired | 1154 | 835 | 1989 | full_market_ok | data/daily_price/20240930.csv;data/daily_price/daily_price_20240930.csv |

## Check Code 2330

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20240902 | True | 2330 | 台積電 | TWSE | 950.0 | 955.0 | 943.0 | 948.0 | 19272593 | 18270058260 |
| 20240903 | True | 2330 | 台積電 | TWSE | 948.0 | 952.0 | 939.0 | 940.0 | 23205623 | 21908471541 |
| 20240904 | True | 2330 | 台積電 | TWSE | 894.0 | 905.0 | 888.0 | 889.0 | 93169835 | 83424133824 |
| 20240905 | True | 2330 | 台積電 | TWSE | 907.0 | 915.0 | 900.0 | 902.0 | 34147890 | 30998595394 |
| 20240906 | True | 2330 | 台積電 | TWSE | 909.0 | 918.0 | 903.0 | 918.0 | 28248063 | 25786016936 |
| 20240909 | True | 2330 | 台積電 | TWSE | 892.0 | 900.0 | 891.0 | 899.0 | 38448946 | 34456838126 |
| 20240910 | True | 2330 | 台積電 | TWSE | 907.0 | 911.0 | 901.0 | 904.0 | 34312646 | 31067424234 |
| 20240911 | True | 2330 | 台積電 | TWSE | 906.0 | 906.0 | 900.0 | 901.0 | 19513256 | 17621000956 |
| 20240912 | True | 2330 | 台積電 | TWSE | 936.0 | 944.0 | 928.0 | 940.0 | 43749260 | 40999951508 |
| 20240913 | True | 2330 | 台積電 | TWSE | 955.0 | 955.0 | 939.0 | 947.0 | 28307441 | 26795862243 |
| 20240916 | True | 2330 | 台積電 | TWSE | 952.0 | 952.0 | 943.0 | 947.0 | 14456888 | 13692259575 |
| 20240918 | True | 2330 | 台積電 | TWSE | 945.0 | 948.0 | 933.0 | 941.0 | 30094662 | 28303054525 |
| 20240919 | True | 2330 | 台積電 | TWSE | 940.0 | 960.0 | 936.0 | 960.0 | 35254383 | 33482773635 |
| 20240920 | True | 2330 | 台積電 | TWSE | 981.0 | 982.0 | 971.0 | 973.0 | 66762167 | 65105344444 |
| 20240923 | True | 2330 | 台積電 | TWSE | 971.0 | 977.0 | 971.0 | 977.0 | 15399658 | 15013916758 |
| 20240924 | True | 2330 | 台積電 | TWSE | 976.0 | 987.0 | 971.0 | 987.0 | 29324170 | 28726805585 |
| 20240925 | True | 2330 | 台積電 | TWSE | 1000.0 | 1005.0 | 998.0 | 1005.0 | 43039991 | 43053012337 |
| 20240926 | True | 2330 | 台積電 | TWSE | 1010.0 | 1015.0 | 1005.0 | 1015.0 | 43341810 | 43835515361 |
| 20240927 | True | 2330 | 台積電 | TWSE | 1020.0 | 1025.0 | 1000.0 | 1000.0 | 37665070 | 38074974690 |
| 20240930 | True | 2330 | 台積電 | TWSE | 978.0 | 990.0 | 957.0 | 957.0 | 66874949 | 65017701862 |
