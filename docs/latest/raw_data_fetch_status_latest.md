# Raw Data Fetch Status

- generated_at: 2026-06-20 22:58:45 Asia/Taipei
- sources_checked: raw, pages, api, blob
- checked_rows: 384
- success_rows: 99
- suspicious_single_line_rows: 0
- content_not_expanded_rows: 29
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
| all_candidates | success |
| candidate_repeat_appearance | success |
| daily_market_full | success |
| daily_market_summary | success |
| daily_report_packet | success |
| daily_signal_performance_summary | success |
| individual_stock_available_raw_data_index | api_fetch_failed |
| individual_stock_available_raw_data_index_slim | api_fetch_failed |
| individual_stock_chatgpt_packet | api_fetch_failed |
| individual_stock_chatgpt_packet_index | api_fetch_failed |
| individual_stock_chatgpt_packet_index_md | api_fetch_failed |
| individual_stock_price_window_180_html | api_fetch_failed |
| individual_stock_price_window_180_txt | api_fetch_failed |
| individual_stock_report_md | success |
| individual_stock_reports_index | api_fetch_failed |
| individual_stock_tdcc_window_txt | api_fetch_failed |
| readme_first | success |
| sell_strategy_backtest | success |
| sell_strategy_summary | success |
| stock_monitor | success |
| stock_price_history | success |
| surge_model_backtest | success |
| surge_model_feature_importance | success |
| surge_model_packet | success |
| surge_precondition_candidates | success |
| tdcc_phase_distribution | success |
| tdcc_pre_move_abm_top | success |
| tdcc_stock_history | success |
| tdcc_strength_ranking_top | success |
| tdcc_top_risk_list | success |
| tdcc_tracking_packet | success |
| warrant_flow_by_stock | success |
| warrant_market_report | success |

## Detail Preview

| logical_source | stock_id | source_type | status_category | http_status | rows | columns | line_count | local_line_count | sample_status | chatgpt_friendly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_candidates |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 4211 | ok | False |
| all_candidates |  | blob | content_not_expanded | 200 |  |  |  | 4211 | ok | False |
| all_candidates |  | pages | missing_file | 404 | 0 | 0 | 0 | 4211 | ok | False |
| all_candidates |  | raw | success | 200 | 470 | 242 | 4211 | 4211 | ok | True |
| candidate_repeat_appearance |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 471 | ok | False |
| candidate_repeat_appearance |  | blob | content_not_expanded | 200 |  |  |  | 471 | ok | False |
| candidate_repeat_appearance |  | pages | missing_file | 404 | 0 | 0 | 0 | 471 | ok | False |
| candidate_repeat_appearance |  | raw | success | 200 | 470 | 13 | 471 | 471 | ok | True |
| daily_market_full |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 529 | ok | False |
| daily_market_full |  | blob | success | 200 |  |  |  | 529 | ok | True |
| daily_market_full |  | pages | missing_file | 404 | 0 | 0 | 0 | 529 | ok | False |
| daily_market_full |  | raw | success | 200 | 529 | 1 | 529 | 529 | ok | True |
| daily_market_summary |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 230 | ok | False |
| daily_market_summary |  | blob | success | 200 |  |  |  | 230 | ok | True |
| daily_market_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 230 | ok | False |
| daily_market_summary |  | raw | success | 200 | 230 | 1 | 230 | 230 | ok | True |
| daily_report_packet |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 1386 | ok | False |
| daily_report_packet |  | blob | success | 200 |  |  |  | 1386 | ok | True |
| daily_report_packet |  | pages | success | 200 | 1386 | 1 | 1386 | 1386 | ok | True |
| daily_report_packet |  | raw | success | 200 | 1386 | 1 | 1386 | 1386 | ok | True |
| daily_signal_performance_summary |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 132 | ok | False |
| daily_signal_performance_summary |  | blob | success | 200 |  |  |  | 132 | ok | True |
| daily_signal_performance_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 132 | ok | False |
| daily_signal_performance_summary |  | raw | success | 200 | 132 | 1 | 132 | 132 | ok | True |
| individual_stock_available_raw_data_index |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index |  | blob | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index |  | pages | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index |  | raw | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index_slim |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index_slim |  | blob | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index_slim |  | pages | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_available_raw_data_index_slim |  | raw | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_chatgpt_packet | 1815 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 1815 | blob | missing_file | 404 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 2324 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2324 | blob | missing_file | 404 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2324 | pages | missing_file | 404 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2324 | raw | missing_file | 404 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2330 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2330 | blob | missing_file | 404 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 208 | ok | False |
| individual_stock_chatgpt_packet | 2353 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 2353 | blob | missing_file | 404 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 2353 | raw | missing_file | 404 | 0 | 0 | 0 | 209 | ok | False |
| individual_stock_chatgpt_packet | 2484 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 207 | ok | False |
| individual_stock_chatgpt_packet | 2484 | blob | missing_file | 404 | 0 | 0 | 0 | 207 | ok | False |
| individual_stock_chatgpt_packet | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 207 | ok | False |
| individual_stock_chatgpt_packet | 2484 | raw | missing_file | 404 | 0 | 0 | 0 | 207 | ok | False |
| individual_stock_chatgpt_packet | 3207 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 213 | ok | False |
| individual_stock_chatgpt_packet | 3207 | blob | missing_file | 404 | 0 | 0 | 0 | 213 | ok | False |
| individual_stock_chatgpt_packet | 3207 | pages | missing_file | 404 | 0 | 0 | 0 | 213 | ok | False |
| individual_stock_chatgpt_packet | 3207 | raw | missing_file | 404 | 0 | 0 | 0 | 213 | ok | False |
| individual_stock_chatgpt_packet | 8299 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 214 | ok | False |
| individual_stock_chatgpt_packet | 8299 | blob | missing_file | 404 | 0 | 0 | 0 | 214 | ok | False |
| individual_stock_chatgpt_packet | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 214 | ok | False |
| individual_stock_chatgpt_packet | 8299 | raw | missing_file | 404 | 0 | 0 | 0 | 214 | ok | False |
| individual_stock_chatgpt_packet | INDIVIDUALSTOCKREADPROTOCOL | api | api_fetch_failed | 403 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_chatgpt_packet | INDIVIDUALSTOCKREADPROTOCOL | blob | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_chatgpt_packet | INDIVIDUALSTOCKREADPROTOCOL | pages | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_chatgpt_packet | INDIVIDUALSTOCKREADPROTOCOL | raw | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_chatgpt_packet_index |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_chatgpt_packet_index |  | blob | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_chatgpt_packet_index |  | pages | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_chatgpt_packet_index |  | raw | missing_file | 404 | 0 | 0 | 0 | 2398 | ok | False |
| individual_stock_chatgpt_packet_index_md |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 247 | ok | False |
| individual_stock_chatgpt_packet_index_md |  | blob | missing_file | 404 | 0 | 0 | 0 | 247 | ok | False |
| individual_stock_chatgpt_packet_index_md |  | pages | missing_file | 404 | 0 | 0 | 0 | 247 | ok | False |
| individual_stock_chatgpt_packet_index_md |  | raw | missing_file | 404 | 0 | 0 | 0 | 247 | ok | False |
| individual_stock_price_window_180_html | 1815 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 1815 | blob | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 2324 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2324 | blob | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2324 | pages | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2324 | raw | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2330 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2330 | blob | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2353 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2353 | blob | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2353 | raw | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2484 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2484 | blob | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 2484 | raw | missing_file | 404 | 0 | 0 | 0 | 198 | ok | False |
| individual_stock_price_window_180_html | 3207 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 3207 | blob | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 3207 | pages | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 3207 | raw | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 8299 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 8299 | blob | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | 8299 | raw | missing_file | 404 | 0 | 0 | 0 | 170 | ok | False |
| individual_stock_price_window_180_html | INDIVIDUALSTOCKREADPROTOCOL | api | api_fetch_failed | 403 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_html | INDIVIDUALSTOCKREADPROTOCOL | blob | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_html | INDIVIDUALSTOCKREADPROTOCOL | pages | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_html | INDIVIDUALSTOCKREADPROTOCOL | raw | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_txt | 1815 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 1815 | blob | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 2324 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2324 | blob | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2324 | pages | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2324 | raw | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2330 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2330 | blob | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2353 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2353 | blob | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2353 | raw | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2484 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2484 | blob | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 2484 | raw | missing_file | 404 | 0 | 0 | 0 | 363 | ok | False |
| individual_stock_price_window_180_txt | 3207 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 3207 | blob | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 3207 | pages | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 3207 | raw | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 8299 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 8299 | blob | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | 8299 | raw | missing_file | 404 | 0 | 0 | 0 | 307 | ok | False |
| individual_stock_price_window_180_txt | INDIVIDUALSTOCKREADPROTOCOL | api | api_fetch_failed | 403 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_txt | INDIVIDUALSTOCKREADPROTOCOL | blob | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_txt | INDIVIDUALSTOCKREADPROTOCOL | pages | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_price_window_180_txt | INDIVIDUALSTOCKREADPROTOCOL | raw | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_report_md | 1815 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 52 | ok | False |
| individual_stock_report_md | 1815 | blob | success | 200 |  |  |  | 52 | ok | True |
| individual_stock_report_md | 1815 | pages | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 1815 | raw | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 2324 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 52 | ok | False |
| individual_stock_report_md | 2324 | blob | success | 200 |  |  |  | 52 | ok | True |
| individual_stock_report_md | 2324 | pages | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 2324 | raw | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 2330 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 54 | ok | False |
| individual_stock_report_md | 2330 | blob | success | 200 |  |  |  | 54 | ok | True |
| individual_stock_report_md | 2330 | pages | success | 200 | 54 | 1 | 54 | 54 | ok | True |
| individual_stock_report_md | 2330 | raw | success | 200 | 54 | 1 | 54 | 54 | ok | True |
| individual_stock_report_md | 2353 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 52 | ok | False |
| individual_stock_report_md | 2353 | blob | success | 200 |  |  |  | 52 | ok | True |
| individual_stock_report_md | 2353 | pages | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 2353 | raw | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 2484 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 54 | ok | False |
| individual_stock_report_md | 2484 | blob | success | 200 |  |  |  | 54 | ok | True |
| individual_stock_report_md | 2484 | pages | success | 200 | 54 | 1 | 54 | 54 | ok | True |
| individual_stock_report_md | 2484 | raw | success | 200 | 54 | 1 | 54 | 54 | ok | True |
| individual_stock_report_md | 3207 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 52 | ok | False |
| individual_stock_report_md | 3207 | blob | success | 200 |  |  |  | 52 | ok | True |
| individual_stock_report_md | 3207 | pages | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 3207 | raw | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 8299 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 52 | ok | False |
| individual_stock_report_md | 8299 | blob | success | 200 |  |  |  | 52 | ok | True |
| individual_stock_report_md | 8299 | pages | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | 8299 | raw | success | 200 | 52 | 1 | 52 | 52 | ok | True |
| individual_stock_report_md | INDIVIDUALSTOCKREADPROTOCOL | api | api_fetch_failed | 403 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_report_md | INDIVIDUALSTOCKREADPROTOCOL | blob | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_report_md | INDIVIDUALSTOCKREADPROTOCOL | pages | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_report_md | INDIVIDUALSTOCKREADPROTOCOL | raw | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| individual_stock_reports_index |  | api | api_fetch_failed | 403 | 0 | 0 | 0 | 8 | ok | False |
| individual_stock_reports_index |  | blob | missing_file | 404 | 0 | 0 | 0 | 8 | ok | False |
| individual_stock_reports_index |  | pages | missing_file | 404 | 0 | 0 | 0 | 8 | ok | False |
| individual_stock_reports_index |  | raw | missing_file | 404 | 0 | 0 | 0 | 8 | ok | False |
| individual_stock_tdcc_window_txt | 1815 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 1815 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2324 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2324 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2324 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2324 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2330 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2330 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2353 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2353 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2353 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2484 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2484 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 2484 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 3207 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 3207 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 3207 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 3207 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 8299 | api | api_fetch_failed | 403 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 8299 | blob | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |
| individual_stock_tdcc_window_txt | 8299 | raw | missing_file | 404 | 0 | 0 | 0 | 19 | ok | False |

_Only first 200 rows shown. Use CSV for all rows._
