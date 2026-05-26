# Raw Data Fetch Status

- generated_at: 2026-05-26 13:42:02 Asia/Taipei
- sources_checked: raw, pages, api, blob
- checked_rows: 36
- success_rows: 31
- suspicious_single_line_rows: 0
- content_not_expanded_rows: 3
- cache_miss_rows: 0
- internal_fetch_error_rows: 0
- csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/raw_data_fetch_status_latest.csv

## Meaning

- `missing_file` means a 404 was observed.
- `raw_fetch_failed`, `cache_miss`, `internal_fetch_error`, and `content_not_expanded` do not prove the repo lacks data.
- `file_exists_but_content_unreadable` means a fallback existence check found the file, but content retrieval failed.
- `standard_rawdata_report` requires stock price history rows >= 60; TDCC fewer than 8 rows is `insufficient_tdcc_history`.

## Logical Source Summary

| logical_source | best_status |
| --- | --- |
| individual_stock_chatgpt_packet | success |
| individual_stock_price_window_180_html | success |
| individual_stock_price_window_180_txt | success |
| individual_stock_report_md | success |
| individual_stock_tdcc_window_txt | success |
| sell_strategy_backtest | success |
| sell_strategy_summary | success |
| stock_price_history | success |
| tdcc_stock_history | success |

## Detail Preview

| logical_source | stock_id | source_type | status_category | http_status | rows | columns | line_count | local_line_count | sample_status | chatgpt_friendly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| individual_stock_chatgpt_packet | 8299 | api | success | 200 | 142 | 1 | 142 | 145 | ok | True |
| individual_stock_chatgpt_packet | 8299 | blob | success | 200 |  |  |  | 145 | ok | True |
| individual_stock_chatgpt_packet | 8299 | pages | success | 200 | 142 | 1 | 142 | 145 | ok | True |
| individual_stock_chatgpt_packet | 8299 | raw | success | 200 | 142 | 1 | 142 | 145 | ok | True |
| individual_stock_price_window_180_html | 8299 | api | success | 200 | 0 | 0 | 154 | 151 | ok | True |
| individual_stock_price_window_180_html | 8299 | blob | success | 200 |  |  |  | 151 | ok | True |
| individual_stock_price_window_180_html | 8299 | pages | success | 200 | 0 | 0 | 154 | 151 | ok | True |
| individual_stock_price_window_180_html | 8299 | raw | success | 200 | 0 | 0 | 154 | 151 | ok | True |
| individual_stock_price_window_180_txt | 8299 | api | success | 200 | 275 | 1 | 275 | 269 | ok | True |
| individual_stock_price_window_180_txt | 8299 | blob | success | 200 |  |  |  | 269 | ok | True |
| individual_stock_price_window_180_txt | 8299 | pages | success | 200 | 275 | 1 | 275 | 269 | ok | True |
| individual_stock_price_window_180_txt | 8299 | raw | success | 200 | 275 | 1 | 275 | 269 | ok | True |
| individual_stock_report_md | 8299 | api | success | 200 | 152 | 1 | 152 | 172 | ok | True |
| individual_stock_report_md | 8299 | blob | success | 200 |  |  |  | 172 | ok | True |
| individual_stock_report_md | 8299 | pages | success | 200 | 152 | 1 | 152 | 172 | ok | True |
| individual_stock_report_md | 8299 | raw | success | 200 | 152 | 1 | 152 | 172 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | api | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | blob | success | 200 |  |  |  | 11 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | pages | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | raw | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| sell_strategy_backtest | 8299 | api | success | 200 | 20 | 16 | 21 | 21 | ok | True |
| sell_strategy_backtest | 8299 | blob | content_not_expanded | 200 |  |  |  | 21 | ok | False |
| sell_strategy_backtest | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 21 | ok | False |
| sell_strategy_backtest | 8299 | raw | success | 200 | 20 | 16 | 21 | 21 | ok | True |
| sell_strategy_summary | 8299 | api | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| sell_strategy_summary | 8299 | blob | success | 200 |  |  |  | 28 | ok | True |
| sell_strategy_summary | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 28 | ok | False |
| sell_strategy_summary | 8299 | raw | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| stock_price_history | 8299 | api | success | 200 | 136 | 39 | 137 | 134 | ok | True |
| stock_price_history | 8299 | blob | content_not_expanded | 200 |  |  |  | 134 | ok | False |
| stock_price_history | 8299 | pages | success | 200 | 136 | 39 | 137 | 134 | ok | True |
| stock_price_history | 8299 | raw | success | 200 | 136 | 39 | 137 | 134 | ok | True |
| tdcc_stock_history | 8299 | api | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 8299 | blob | content_not_expanded | 200 |  |  |  | 5 | insufficient_tdcc_history | False |
| tdcc_stock_history | 8299 | pages | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 8299 | raw | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
