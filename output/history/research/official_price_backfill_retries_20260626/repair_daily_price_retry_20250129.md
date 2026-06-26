# Repair Daily Price Range Report

- start_date: `20250129`
- end_date: `20250129`
- check_code: `2330`
- repaired_count: `0`
- skipped_count: `0`
- failed_count: `1`

## Repair Results

| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |
|---|---|---:|---:|---:|---|---|
| 20250129 | failed | 1236 | 0 | 1236 | GET https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d=114/01/29&s=0,asc,0 -> status=200, chars=1391211; TPEX_OLD_DAILY_CSV: rejected response date 20260626; target date is 20250129; Skip TPEx latest-only source=TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES for historical target date 20250129; TPEx batch best rows=0; date=20250129 twse_rows=1236 tpex_rows=0 total_rows=1236 full_market_ok=False |  |
