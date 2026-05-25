# Raw Data Fetch Status

- generated_at: 2026-05-26 00:33:29 Asia/Taipei
- sources_checked: raw, pages, api
- checked_rows: 141
- success_rows: 105
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
| daily_market_full | success |
| daily_market_summary | success |
| daily_report_packet | success |
| daily_signal_performance_summary | success |
| individual_stock_available_raw_data_index | success |
| individual_stock_available_raw_data_index_slim | success |
| individual_stock_report_md | success |
| individual_stock_reports_index | success |
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
| all_candidates |  | api | success | 200 | 519 | 205 | 520 | 520 | ok | True |
| all_candidates |  | pages | missing_file | 404 | 0 | 0 | 0 | 520 | ok | False |
| all_candidates |  | raw | success | 200 | 519 | 205 | 520 | 520 | ok | True |
| candidate_repeat_appearance |  | api | success | 200 | 400 | 13 | 401 | 401 | ok | True |
| candidate_repeat_appearance |  | pages | missing_file | 404 | 0 | 0 | 0 | 401 | ok | False |
| candidate_repeat_appearance |  | raw | success | 200 | 400 | 13 | 401 | 401 | ok | True |
| daily_market_full |  | api | success | 200 | 567 | 1 | 567 | 567 | ok | True |
| daily_market_full |  | pages | missing_file | 404 | 0 | 0 | 0 | 567 | ok | False |
| daily_market_full |  | raw | success | 200 | 567 | 1 | 567 | 567 | ok | True |
| daily_market_summary |  | api | success | 200 | 447 | 1 | 447 | 447 | ok | True |
| daily_market_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 447 | ok | False |
| daily_market_summary |  | raw | success | 200 | 447 | 1 | 447 | 447 | ok | True |
| daily_report_packet |  | api | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_report_packet |  | pages | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_report_packet |  | raw | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_signal_performance_summary |  | api | success | 200 | 120 | 1 | 120 | 120 | ok | True |
| daily_signal_performance_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 120 | ok | False |
| daily_signal_performance_summary |  | raw | success | 200 | 120 | 1 | 120 | 120 | ok | True |
| individual_stock_available_raw_data_index |  | api | api_decode_failed | 200 | 0 | 0 | 0 | 2150 | ok | False |
| individual_stock_available_raw_data_index |  | pages | success | 200 | 2149 | 32 | 2150 | 2150 | ok | True |
| individual_stock_available_raw_data_index |  | raw | success | 200 | 2149 | 32 | 2150 | 2150 | ok | True |
| individual_stock_available_raw_data_index_slim |  | api | success | 200 | 2149 | 17 | 2150 | 2150 | ok | True |
| individual_stock_available_raw_data_index_slim |  | pages | success | 200 | 2149 | 17 | 2150 | 2150 | ok | True |
| individual_stock_available_raw_data_index_slim |  | raw | success | 200 | 2149 | 17 | 2150 | 2150 | ok | True |
| individual_stock_report_md | 1815 | api | success | 200 | 77 | 1 | 77 | 77 | ok | True |
| individual_stock_report_md | 1815 | pages | success | 200 | 77 | 1 | 77 | 77 | ok | True |
| individual_stock_report_md | 1815 | raw | success | 200 | 77 | 1 | 77 | 77 | ok | True |
| individual_stock_report_md | 2330 | api | success | 200 | 75 | 1 | 75 | 75 | ok | True |
| individual_stock_report_md | 2330 | pages | success | 200 | 75 | 1 | 75 | 75 | ok | True |
| individual_stock_report_md | 2330 | raw | success | 200 | 75 | 1 | 75 | 75 | ok | True |
| individual_stock_report_md | 2353 | api | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2353 | pages | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2353 | raw | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2484 | api | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2484 | pages | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 2484 | raw | success | 200 | 156 | 1 | 156 | 156 | ok | True |
| individual_stock_report_md | 8299 | api | success | 200 | 152 | 1 | 152 | 152 | ok | True |
| individual_stock_report_md | 8299 | pages | success | 200 | 152 | 1 | 152 | 152 | ok | True |
| individual_stock_report_md | 8299 | raw | success | 200 | 152 | 1 | 152 | 152 | ok | True |
| individual_stock_reports_index |  | api | success | 200 | 4 | 15 | 5 | 6 | ok | True |
| individual_stock_reports_index |  | pages | success | 200 | 4 | 15 | 5 | 6 | ok | True |
| individual_stock_reports_index |  | raw | success | 200 | 4 | 15 | 5 | 6 | ok | True |
| readme_first |  | api | success | 200 | 169 | 1 | 169 | 169 | ok | True |
| readme_first |  | pages | success | 200 | 169 | 1 | 169 | 169 | ok | True |
| readme_first |  | raw | success | 200 | 169 | 1 | 169 | 169 | ok | True |
| sell_strategy_backtest | 1815 | api | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 1815 | pages | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 1815 | raw | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2330 | api | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2330 | pages | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2330 | raw | missing_file | 404 | 0 | 0 | 0 | 0 | empty_table | False |
| sell_strategy_backtest | 2353 | api | success | 200 | 40 | 16 | 41 | 41 | ok | True |
| sell_strategy_backtest | 2353 | pages | missing_file | 404 | 0 | 0 | 0 | 41 | ok | False |
| sell_strategy_backtest | 2353 | raw | success | 200 | 40 | 16 | 41 | 41 | ok | True |
| sell_strategy_backtest | 2484 | api | success | 200 | 60 | 16 | 61 | 61 | ok | True |
| sell_strategy_backtest | 2484 | pages | missing_file | 404 | 0 | 0 | 0 | 61 | ok | False |
| sell_strategy_backtest | 2484 | raw | success | 200 | 60 | 16 | 61 | 61 | ok | True |
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
| stock_monitor |  | api | success | 200 | 161 | 1 | 161 | 161 | ok | True |
| stock_monitor |  | pages | missing_file | 404 | 0 | 0 | 0 | 161 | ok | False |
| stock_monitor |  | raw | success | 200 | 161 | 1 | 161 | 161 | ok | True |
| stock_price_history | 1815 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 1815 | pages | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 1815 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2330 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2330 | pages | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2330 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2353 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2353 | pages | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2353 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2484 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2484 | pages | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 2484 | raw | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 8299 | api | success | 200 | 135 | 39 | 136 | 136 | ok | True |
| stock_price_history | 8299 | pages | success | 200 | 135 | 39 | 136 | 136 | ok | True |
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
| tdcc_stock_history | 8299 | raw | success | 200 | 4 | 29 | 5 | 5 | insufficient_tdcc_history | True |
| tdcc_strength_ranking_top |  | api | success | 200 | 50 | 27 | 51 | 51 | ok | True |
| tdcc_strength_ranking_top |  | pages | missing_file | 404 | 0 | 0 | 0 | 51 | ok | False |
| tdcc_strength_ranking_top |  | raw | success | 200 | 50 | 27 | 51 | 51 | ok | True |
| tdcc_top_risk_list |  | api | success | 200 | 60 | 13 | 61 | 61 | ok | True |
| tdcc_top_risk_list |  | pages | missing_file | 404 | 0 | 0 | 0 | 61 | ok | False |
| tdcc_top_risk_list |  | raw | success | 200 | 60 | 13 | 61 | 61 | ok | True |
| tdcc_tracking_packet |  | api | success | 200 | 661 | 1 | 661 | 661 | ok | True |
| tdcc_tracking_packet |  | pages | missing_file | 404 | 0 | 0 | 0 | 661 | ok | False |
| tdcc_tracking_packet |  | raw | success | 200 | 661 | 1 | 661 | 661 | ok | True |
| warrant_flow_by_stock |  | api | success | 200 | 455 | 38 | 456 | 456 | ok | True |
| warrant_flow_by_stock |  | pages | missing_file | 404 | 0 | 0 | 0 | 456 | ok | False |
| warrant_flow_by_stock |  | raw | success | 200 | 455 | 38 | 456 | 456 | ok | True |
| warrant_market_report |  | api | success | 200 | 197 | 1 | 197 | 197 | ok | True |
| warrant_market_report |  | pages | missing_file | 404 | 0 | 0 | 0 | 197 | ok | False |
| warrant_market_report |  | raw | success | 200 | 197 | 1 | 197 | 197 | ok | True |
