# Raw Data Fetch Status

- generated_at: 2026-05-27 21:29:26 Asia/Taipei
- sources_checked: raw, pages, api
- checked_rows: 216
- success_rows: 175
- suspicious_single_line_rows: 0
- content_not_expanded_rows: 0
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
| daily_candidate_decision | success |
| daily_candidate_decision_md | success |
| daily_candidate_decision_packet | success |
| daily_market_full | success |
| daily_market_summary | success |
| daily_report_packet | success |
| daily_signal_performance_summary | success |
| individual_stock_available_raw_data_index | success |
| individual_stock_available_raw_data_index_slim | success |
| individual_stock_chatgpt_packet | success |
| individual_stock_chatgpt_packet_index | success |
| individual_stock_chatgpt_packet_index_md | success |
| individual_stock_price_window_180_html | success |
| individual_stock_price_window_180_txt | success |
| individual_stock_report_md | success |
| individual_stock_reports_index | success |
| individual_stock_tdcc_window_txt | success |
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
| all_candidates |  | api | api_decode_failed | 200 | 0 | 0 | 0 | 651 | ok | False |
| all_candidates |  | pages | missing_file | 404 | 0 | 0 | 0 | 651 | ok | False |
| all_candidates |  | raw | success | 200 | 650 | 278 | 651 | 651 | ok | True |
| candidate_repeat_appearance |  | api | success | 200 | 455 | 13 | 456 | 456 | ok | True |
| candidate_repeat_appearance |  | pages | missing_file | 404 | 0 | 0 | 0 | 456 | ok | False |
| candidate_repeat_appearance |  | raw | success | 200 | 455 | 13 | 456 | 456 | ok | True |
| daily_candidate_decision |  | api | success | 200 | 650 | 36 | 651 | 651 | ok | True |
| daily_candidate_decision |  | pages | missing_file | 404 | 0 | 0 | 0 | 651 | ok | False |
| daily_candidate_decision |  | raw | success | 200 | 650 | 36 | 651 | 651 | ok | True |
| daily_candidate_decision_md |  | api | success | 200 | 277 | 1 | 277 | 277 | ok | True |
| daily_candidate_decision_md |  | pages | missing_file | 404 | 0 | 0 | 0 | 277 | ok | False |
| daily_candidate_decision_md |  | raw | success | 200 | 277 | 1 | 277 | 277 | ok | True |
| daily_candidate_decision_packet |  | api | success | 200 | 215 | 1 | 215 | 215 | ok | True |
| daily_candidate_decision_packet |  | pages | missing_file | 404 | 0 | 0 | 0 | 215 | ok | False |
| daily_candidate_decision_packet |  | raw | success | 200 | 215 | 1 | 215 | 215 | ok | True |
| daily_market_full |  | api | success | 200 | 788 | 1 | 788 | 788 | ok | True |
| daily_market_full |  | pages | missing_file | 404 | 0 | 0 | 0 | 788 | ok | False |
| daily_market_full |  | raw | success | 200 | 788 | 1 | 788 | 788 | ok | True |
| daily_market_summary |  | api | success | 200 | 443 | 1 | 443 | 443 | ok | True |
| daily_market_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 443 | ok | False |
| daily_market_summary |  | raw | success | 200 | 443 | 1 | 443 | 443 | ok | True |
| daily_report_packet |  | api | success | 200 | 1426 | 1 | 1426 | 1426 | ok | True |
| daily_report_packet |  | pages | success | 200 | 1426 | 1 | 1426 | 1426 | ok | True |
| daily_report_packet |  | raw | success | 200 | 1426 | 1 | 1426 | 1426 | ok | True |
| daily_signal_performance_summary |  | api | success | 200 | 122 | 1 | 122 | 122 | ok | True |
| daily_signal_performance_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 122 | ok | False |
| daily_signal_performance_summary |  | raw | success | 200 | 122 | 1 | 122 | 122 | ok | True |
| individual_stock_available_raw_data_index |  | api | api_decode_failed | 200 | 0 | 0 | 0 | 2151 | ok | False |
| individual_stock_available_raw_data_index |  | pages | success | 200 | 2149 | 32 | 2150 | 2151 | ok | True |
| individual_stock_available_raw_data_index |  | raw | success | 200 | 2149 | 32 | 2150 | 2151 | ok | True |
| individual_stock_available_raw_data_index_slim |  | api | success | 200 | 2149 | 17 | 2150 | 2151 | ok | True |
| individual_stock_available_raw_data_index_slim |  | pages | success | 200 | 2149 | 17 | 2150 | 2151 | ok | True |
| individual_stock_available_raw_data_index_slim |  | raw | success | 200 | 2149 | 17 | 2150 | 2151 | ok | True |
| individual_stock_chatgpt_packet | 1815 | api | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 1815 | pages | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 1815 | raw | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 2330 | api | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 2330 | pages | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 2330 | raw | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 2353 | api | success | 200 | 146 | 1 | 146 | 146 | ok | True |
| individual_stock_chatgpt_packet | 2353 | pages | success | 200 | 146 | 1 | 146 | 146 | ok | True |
| individual_stock_chatgpt_packet | 2353 | raw | success | 200 | 146 | 1 | 146 | 146 | ok | True |
| individual_stock_chatgpt_packet | 2484 | api | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 2484 | pages | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 2484 | raw | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 8299 | api | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 8299 | pages | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet | 8299 | raw | success | 200 | 145 | 1 | 145 | 145 | ok | True |
| individual_stock_chatgpt_packet_index |  | api | api_decode_failed | 200 | 0 | 0 | 0 | 2151 | ok | False |
| individual_stock_chatgpt_packet_index |  | pages | success | 200 | 2149 | 36 | 2150 | 2151 | ok | True |
| individual_stock_chatgpt_packet_index |  | raw | success | 200 | 2149 | 36 | 2150 | 2151 | ok | True |
| individual_stock_chatgpt_packet_index_md |  | api | success | 200 | 245 | 1 | 245 | 245 | ok | True |
| individual_stock_chatgpt_packet_index_md |  | pages | success | 200 | 245 | 1 | 245 | 245 | ok | True |
| individual_stock_chatgpt_packet_index_md |  | raw | success | 200 | 245 | 1 | 245 | 245 | ok | True |
| individual_stock_price_window_180_html | 1815 | api | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 1815 | pages | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 1815 | raw | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2330 | api | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2330 | pages | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2330 | raw | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2353 | api | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2353 | pages | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2353 | raw | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2484 | api | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2484 | pages | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 2484 | raw | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 8299 | api | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 8299 | pages | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_html | 8299 | raw | success | 200 | 0 | 0 | 152 | 153 | ok | True |
| individual_stock_price_window_180_txt | 1815 | api | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 1815 | pages | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 1815 | raw | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2330 | api | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2330 | pages | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2330 | raw | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2353 | api | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2353 | pages | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2353 | raw | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2484 | api | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2484 | pages | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 2484 | raw | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 8299 | api | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 8299 | pages | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_price_window_180_txt | 8299 | raw | success | 200 | 271 | 1 | 271 | 273 | ok | True |
| individual_stock_report_md | 1815 | api | success | 200 | 77 | 1 | 77 | 77 | ok | True |
| individual_stock_report_md | 1815 | pages | success | 200 | 77 | 1 | 77 | 77 | ok | True |
| individual_stock_report_md | 1815 | raw | success | 200 | 77 | 1 | 77 | 77 | ok | True |
| individual_stock_report_md | 2330 | api | success | 200 | 75 | 1 | 75 | 75 | ok | True |
| individual_stock_report_md | 2330 | pages | success | 200 | 75 | 1 | 75 | 75 | ok | True |
| individual_stock_report_md | 2330 | raw | success | 200 | 75 | 1 | 75 | 75 | ok | True |
| individual_stock_report_md | 2353 | api | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2353 | pages | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2353 | raw | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2484 | api | success | 200 | 174 | 1 | 174 | 174 | ok | True |
| individual_stock_report_md | 2484 | pages | success | 200 | 174 | 1 | 174 | 174 | ok | True |
| individual_stock_report_md | 2484 | raw | success | 200 | 174 | 1 | 174 | 174 | ok | True |
| individual_stock_report_md | 8299 | api | success | 200 | 172 | 1 | 172 | 172 | ok | True |
| individual_stock_report_md | 8299 | pages | success | 200 | 172 | 1 | 172 | 172 | ok | True |
| individual_stock_report_md | 8299 | raw | success | 200 | 172 | 1 | 172 | 172 | ok | True |
| individual_stock_reports_index |  | api | success | 200 | 5 | 15 | 6 | 6 | ok | True |
| individual_stock_reports_index |  | pages | success | 200 | 5 | 15 | 6 | 6 | ok | True |
| individual_stock_reports_index |  | raw | success | 200 | 5 | 15 | 6 | 6 | ok | True |
| individual_stock_tdcc_window_txt | 1815 | api | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 1815 | pages | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 1815 | raw | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2330 | api | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2330 | pages | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2330 | raw | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2353 | api | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2353 | pages | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2353 | raw | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2484 | api | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2484 | pages | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 2484 | raw | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | api | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | pages | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| individual_stock_tdcc_window_txt | 8299 | raw | success | 200 | 11 | 1 | 11 | 11 | ok | True |
| readme_first |  | api | success | 200 | 211 | 1 | 211 | 211 | ok | True |
| readme_first |  | pages | success | 200 | 5 | 1 | 5 | 211 | ok | True |
| readme_first |  | raw | success | 200 | 211 | 1 | 211 | 211 | ok | True |
| sell_strategy_backtest | 1815 | api | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2330 | api | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2353 | api | success | 200 | 40 | 16 | 41 | 41 | ok | True |
| sell_strategy_backtest | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 41 | ok | False |
| sell_strategy_backtest | 2353 | raw | success | 200 | 40 | 16 | 41 | 41 | ok | True |
| sell_strategy_backtest | 2484 | api | success | 200 | 80 | 16 | 81 | 81 | ok | True |
| sell_strategy_backtest | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 81 | ok | False |
| sell_strategy_backtest | 2484 | raw | success | 200 | 80 | 16 | 81 | 81 | ok | True |
| sell_strategy_backtest | 8299 | api | success | 200 | 20 | 16 | 21 | 21 | ok | True |
| sell_strategy_backtest | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 21 | ok | False |
| sell_strategy_backtest | 8299 | raw | success | 200 | 20 | 16 | 21 | 21 | ok | True |
| sell_strategy_summary | 1815 | api | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| sell_strategy_summary | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| sell_strategy_summary | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| sell_strategy_summary | 2330 | api | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| sell_strategy_summary | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| sell_strategy_summary | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 0 | content_not_expanded | False |
| sell_strategy_summary | 2353 | api | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| sell_strategy_summary | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 28 | ok | False |
| sell_strategy_summary | 2353 | raw | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| sell_strategy_summary | 2484 | api | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| sell_strategy_summary | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 28 | ok | False |
| sell_strategy_summary | 2484 | raw | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| sell_strategy_summary | 8299 | api | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| sell_strategy_summary | 8299 | pages | missing_file | 404 | 0 | 0 | 0 | 28 | ok | False |
| sell_strategy_summary | 8299 | raw | success | 200 | 28 | 1 | 28 | 28 | ok | True |
| stock_monitor |  | api | success | 200 | 155 | 1 | 155 | 155 | ok | True |
| stock_monitor |  | pages | missing_file | 404 | 0 | 0 | 0 | 155 | ok | False |
| stock_monitor |  | raw | success | 200 | 155 | 1 | 155 | 155 | ok | True |
| stock_price_history | 1815 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 1815 | pages | success | 200 | 134 | 39 | 135 | 136 | ok | True |
| stock_price_history | 1815 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2330 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2330 | pages | success | 200 | 134 | 39 | 135 | 136 | ok | True |
| stock_price_history | 2330 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2353 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2353 | pages | success | 200 | 134 | 39 | 135 | 136 | ok | True |
| stock_price_history | 2353 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2484 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2484 | pages | success | 200 | 134 | 39 | 135 | 136 | ok | True |
| stock_price_history | 2484 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 8299 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 8299 | pages | success | 200 | 134 | 39 | 135 | 136 | ok | True |
| stock_price_history | 8299 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| surge_model_backtest |  | api | success | 200 | 15 | 17 | 16 | 16 | ok | True |
| surge_model_backtest |  | pages | missing_file | 404 | 0 | 0 | 0 | 16 | ok | False |
| surge_model_backtest |  | raw | success | 200 | 15 | 17 | 16 | 16 | ok | True |
| surge_model_feature_importance |  | api | success | 200 | 10 | 14 | 11 | 11 | ok | True |
| surge_model_feature_importance |  | pages | missing_file | 404 | 0 | 0 | 0 | 11 | ok | False |
| surge_model_feature_importance |  | raw | success | 200 | 10 | 14 | 11 | 11 | ok | True |
| surge_model_packet |  | api | success | 200 | 109 | 1 | 109 | 109 | ok | True |
| surge_model_packet |  | pages | missing_file | 404 | 0 | 0 | 0 | 109 | ok | False |
| surge_model_packet |  | raw | success | 200 | 109 | 1 | 109 | 109 | ok | True |
| surge_precondition_candidates |  | api | success | 200 | 100 | 19 | 101 | 101 | ok | True |
| surge_precondition_candidates |  | pages | missing_file | 404 | 0 | 0 | 0 | 101 | ok | False |
| surge_precondition_candidates |  | raw | success | 200 | 100 | 19 | 101 | 101 | ok | True |
| tdcc_phase_distribution |  | api | success | 200 | 112 | 18 | 113 | 113 | ok | True |
| tdcc_phase_distribution |  | pages | missing_file | 404 | 0 | 0 | 0 | 113 | ok | False |
| tdcc_phase_distribution |  | raw | success | 200 | 112 | 18 | 113 | 113 | ok | True |
| tdcc_pre_move_abm_top |  | api | success | 200 | 50 | 28 | 51 | 51 | ok | True |
| tdcc_pre_move_abm_top |  | pages | missing_file | 404 | 0 | 0 | 0 | 51 | ok | False |
| tdcc_pre_move_abm_top |  | raw | success | 200 | 50 | 28 | 51 | 51 | ok | True |
| tdcc_stock_history | 1815 | api | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 1815 | pages | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 1815 | raw | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2330 | api | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2330 | pages | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2330 | raw | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2353 | api | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2353 | pages | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2353 | raw | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2484 | api | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2484 | pages | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 2484 | raw | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 8299 | api | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_stock_history | 8299 | pages | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |

_Only first 200 rows shown. Use CSV for all rows._
