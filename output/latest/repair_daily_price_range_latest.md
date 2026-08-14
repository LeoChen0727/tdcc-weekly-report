# Repair Daily Price Range Report

- mode: `selected_dates`
- selected_dates: `20250411,20250521,20250908,20250912,20250916,20251015,20251017`
- start_date: ``
- end_date: ``
- source_base_sha: `8176fee986d1659896a681e89f99f0171c481b0a`
- check_code: `5291`
- repaired_count: `7`
- skipped_count: `0`
- failed_count: `0`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | price_sha256 | reason | saved_files |
|---|---|---:|---:|---:|---|---|---|
| 20250411 | repaired | 1186 | 845 | 2031 | 89f2177b6f31537294434dbafa7bde0a51954771e0c750e7bff84a2bd0ad0abc | full_market_ok_exact_historical_date | data/daily_price/20250411.csv;data/daily_price/daily_price_20250411.csv |
| 20250521 | repaired | 1187 | 848 | 2035 | 77bb957bdcd1392fa0340cbb552bdb8205ba3b96d979fd72783dfe0368170e04 | full_market_ok_exact_historical_date | data/daily_price/20250521.csv;data/daily_price/daily_price_20250521.csv |
| 20250908 | repaired | 1195 | 855 | 2050 | 66a92ce32f3bbba70f8d83ce557e81190d168e814c0c17dad0da697f4f73db45 | full_market_ok_exact_historical_date | data/daily_price/20250908.csv;data/daily_price/daily_price_20250908.csv |
| 20250912 | repaired | 1199 | 860 | 2059 | 7a32b61ed136a15efc519fcae09c85943e4d21c75ea4cbfcfc358eb11e5afb32 | full_market_ok_exact_historical_date | data/daily_price/20250912.csv;data/daily_price/daily_price_20250912.csv |
| 20250916 | repaired | 1203 | 849 | 2052 | 115c35a00dba8dc2d2047d6645d8c20332d80639469d40238564eeb11258067d | full_market_ok_exact_historical_date | data/daily_price/20250916.csv;data/daily_price/daily_price_20250916.csv |
| 20251015 | repaired | 1205 | 850 | 2055 | 671a17fe97895eaf62274f5798a2c4b1b575fa7b68510ffdad1f5bd3ba307a4d | full_market_ok_exact_historical_date | data/daily_price/20251015.csv;data/daily_price/daily_price_20251015.csv |
| 20251017 | repaired | 1204 | 848 | 2052 | 2ea87b045021603d89c28ad73645fe7b88b33d0030c7e7f4179b9fe053db7ac2 | full_market_ok_exact_historical_date | data/daily_price/20251017.csv;data/daily_price/daily_price_20251017.csv |

## Check Code 5291

| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 20250411 | True | 5291 | 邑昇 | TPEx | 20.9 | 22.0 | 20.3 | 22.0 | 174000 | 3691700 |
| 20250521 | True | 5291 | 邑昇 | TPEx | 26.0 | 26.2 | 25.7 | 26.05 | 67000 | 1744900 |
| 20250908 | True | 5291 | 邑昇 | TPEx | 24.05 | 24.1 | 23.8 | 24.1 | 48000 | 1150850 |
| 20250912 | True | 5291 | 邑昇 | TPEx | 24.3 | 24.3 | 23.7 | 23.9 | 79000 | 1884750 |
| 20250916 | True | 5291 | 邑昇 | TPEx | 23.8 | 25.8 | 23.75 | 24.8 | 95000 | 2388850 |
| 20251015 | True | 5291 | 邑昇 | TPEx | 24.6 | 25.1 | 24.55 | 25.0 | 10000 | 248850 |
| 20251017 | True | 5291 | 邑昇 | TPEx | 25.0 | 25.4 | 25.0 | 25.0 | 28000 | 702050 |

## Selected-Date Stock History Repair

- repair_dates: `20250411,20250521,20250908,20250912,20250916,20251015,20251017`
- eligible_stock_union_count: `2064`
- eligible_stock_date_row_count: `14178`
- existing_history_count: `2061`
- created_history_stock_ids: `00925,4945,6287`
- changed_history_count: `2064`
- untouched_history_count: `323`
- non_selected_base_sha256: `1a40c194317b55b762481f7595f2c1e1b7e062a0b726f2aa5b05b5593dc0c4ec`
- pre_repair_indicator_sha256: `4f32eb42dbfd5c92463ae803a966d8652b7ee162d802f2e93e86d1df269d11b8`
- untouched_history_sha256: `e5063ab3930f575c2cfc507cda5340034955b05cb7d1f1ea73149b10b02781fe`
- new_history_source_coverage: `target_dates_only`
