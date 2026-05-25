# Raw Data Fetch Status

- generated_at: 2026-05-25 22:30:36 Asia/Taipei
- checked_rows: 84
- success_rows: 52
- suspicious_single_line_rows: 0
- content_not_expanded_rows: 12
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
| individual_stock_reports_index | success |
| readme_first | success |
| stock_monitor | success |
| surge_model_backtest | success |
| surge_model_feature_importance | success |
| surge_model_packet | success |
| surge_precondition_candidates | success |
| tdcc_phase_distribution | success |
| tdcc_pre_move_abm_top | success |
| tdcc_strength_ranking_top | success |
| tdcc_top_risk_list | success |
| tdcc_tracking_packet | success |
| warrant_flow_by_stock | success |
| warrant_market_report | success |

## Detail Preview

| logical_source | stock_id | source_type | status_category | http_status | rows | columns | line_count | local_line_count | sample_status | chatgpt_friendly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| readme_first |  | raw | success | 200 | 112 | 1 | 112 | 112 | ok | True |
| readme_first |  | pages | success | 200 | 5 | 1 | 5 | 112 | ok | True |
| readme_first |  | api | success | 200 | 112 | 1 | 112 | 112 | ok | True |
| readme_first |  | blob | success | 200 |  |  |  | 112 | ok | True |
| daily_report_packet |  | raw | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_report_packet |  | pages | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_report_packet |  | api | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_report_packet |  | blob | success | 200 |  |  |  | 1175 | ok | True |
| daily_market_summary |  | raw | success | 200 | 447 | 1 | 447 | 447 | ok | True |
| daily_market_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 447 | ok | False |
| daily_market_summary |  | api | success | 200 | 447 | 1 | 447 | 447 | ok | True |
| daily_market_summary |  | blob | success | 200 |  |  |  | 447 | ok | True |
| daily_market_full |  | raw | success | 200 | 567 | 1 | 567 | 567 | ok | True |
| daily_market_full |  | pages | missing_file | 404 | 0 | 0 | 0 | 567 | ok | False |
| daily_market_full |  | api | success | 200 | 567 | 1 | 567 | 567 | ok | True |
| daily_market_full |  | blob | success | 200 |  |  |  | 567 | ok | True |
| stock_monitor |  | raw | success | 200 | 161 | 1 | 161 | 161 | ok | True |
| stock_monitor |  | pages | missing_file | 404 | 0 | 0 | 0 | 161 | ok | False |
| stock_monitor |  | api | success | 200 | 161 | 1 | 161 | 161 | ok | True |
| stock_monitor |  | blob | success | 200 |  |  |  | 161 | ok | True |
| all_candidates |  | raw | success | 200 | 519 | 205 | 520 | 520 | ok | True |
| all_candidates |  | pages | missing_file | 404 | 0 | 0 | 0 | 520 | ok | False |
| all_candidates |  | api | success | 200 | 519 | 205 | 520 | 520 | ok | True |
| all_candidates |  | blob | content_not_expanded | 200 |  |  |  | 520 | ok | False |
| candidate_repeat_appearance |  | raw | success | 200 | 400 | 13 | 401 | 401 | ok | True |
| candidate_repeat_appearance |  | pages | missing_file | 404 | 0 | 0 | 0 | 401 | ok | False |
| candidate_repeat_appearance |  | api | success | 200 | 400 | 13 | 401 | 401 | ok | True |
| candidate_repeat_appearance |  | blob | content_not_expanded | 200 |  |  |  | 401 | ok | False |
| warrant_market_report |  | raw | success | 200 | 197 | 1 | 197 | 197 | ok | True |
| warrant_market_report |  | pages | missing_file | 404 | 0 | 0 | 0 | 197 | ok | False |
| warrant_market_report |  | api | success | 200 | 197 | 1 | 197 | 197 | ok | True |
| warrant_market_report |  | blob | success | 200 |  |  |  | 197 | ok | True |
| warrant_flow_by_stock |  | raw | success | 200 | 455 | 38 | 456 | 456 | ok | True |
| warrant_flow_by_stock |  | pages | missing_file | 404 | 0 | 0 | 0 | 456 | ok | False |
| warrant_flow_by_stock |  | api | success | 200 | 455 | 38 | 456 | 456 | ok | True |
| warrant_flow_by_stock |  | blob | content_not_expanded | 200 |  |  |  | 456 | ok | False |
| tdcc_tracking_packet |  | raw | success | 200 | 661 | 1 | 661 | 661 | ok | True |
| tdcc_tracking_packet |  | pages | missing_file | 404 | 0 | 0 | 0 | 661 | ok | False |
| tdcc_tracking_packet |  | api | success | 200 | 661 | 1 | 661 | 661 | ok | True |
| tdcc_tracking_packet |  | blob | success | 200 |  |  |  | 661 | ok | True |
| tdcc_strength_ranking_top |  | raw | success | 200 | 50 | 27 | 51 | 51 | ok | True |
| tdcc_strength_ranking_top |  | pages | missing_file | 404 | 0 | 0 | 0 | 51 | ok | False |
| tdcc_strength_ranking_top |  | api | success | 200 | 50 | 27 | 51 | 51 | ok | True |
| tdcc_strength_ranking_top |  | blob | content_not_expanded | 200 |  |  |  | 51 | ok | False |
| tdcc_pre_move_abm_top |  | raw | success | 200 | 50 | 28 | 51 | 51 | ok | True |
| tdcc_pre_move_abm_top |  | pages | missing_file | 404 | 0 | 0 | 0 | 51 | ok | False |
| tdcc_pre_move_abm_top |  | api | success | 200 | 50 | 28 | 51 | 51 | ok | True |
| tdcc_pre_move_abm_top |  | blob | content_not_expanded | 200 |  |  |  | 51 | ok | False |
| tdcc_phase_distribution |  | raw | success | 200 | 112 | 18 | 113 | 113 | ok | True |
| tdcc_phase_distribution |  | pages | missing_file | 404 | 0 | 0 | 0 | 113 | ok | False |
| tdcc_phase_distribution |  | api | success | 200 | 112 | 18 | 113 | 113 | ok | True |
| tdcc_phase_distribution |  | blob | content_not_expanded | 200 |  |  |  | 113 | ok | False |
| tdcc_top_risk_list |  | raw | success | 200 | 60 | 13 | 61 | 61 | ok | True |
| tdcc_top_risk_list |  | pages | missing_file | 404 | 0 | 0 | 0 | 61 | ok | False |
| tdcc_top_risk_list |  | api | success | 200 | 60 | 13 | 61 | 61 | ok | True |
| tdcc_top_risk_list |  | blob | content_not_expanded | 200 |  |  |  | 61 | ok | False |
| surge_model_packet |  | raw | success | 200 | 109 | 1 | 109 | 109 | ok | True |
| surge_model_packet |  | pages | missing_file | 404 | 0 | 0 | 0 | 109 | ok | False |
| surge_model_packet |  | api | success | 200 | 109 | 1 | 109 | 109 | ok | True |
| surge_model_packet |  | blob | success | 200 |  |  |  | 109 | ok | True |
| surge_precondition_candidates |  | raw | success | 200 | 100 | 19 | 101 | 101 | ok | True |
| surge_precondition_candidates |  | pages | missing_file | 404 | 0 | 0 | 0 | 101 | ok | False |
| surge_precondition_candidates |  | api | success | 200 | 100 | 19 | 101 | 101 | ok | True |
| surge_precondition_candidates |  | blob | content_not_expanded | 200 |  |  |  | 101 | ok | False |
| surge_model_backtest |  | raw | success | 200 | 15 | 17 | 16 | 16 | ok | True |
| surge_model_backtest |  | pages | missing_file | 404 | 0 | 0 | 0 | 16 | ok | False |
| surge_model_backtest |  | api | success | 200 | 15 | 17 | 16 | 16 | ok | True |
| surge_model_backtest |  | blob | content_not_expanded | 200 |  |  |  | 16 | ok | False |
| surge_model_feature_importance |  | raw | success | 200 | 10 | 14 | 11 | 11 | ok | True |
| surge_model_feature_importance |  | pages | missing_file | 404 | 0 | 0 | 0 | 11 | ok | False |
| surge_model_feature_importance |  | api | success | 200 | 10 | 14 | 11 | 11 | ok | True |
| surge_model_feature_importance |  | blob | content_not_expanded | 200 |  |  |  | 11 | ok | False |
| daily_signal_performance_summary |  | raw | success | 200 | 120 | 1 | 120 | 120 | ok | True |
| daily_signal_performance_summary |  | pages | missing_file | 404 | 0 | 0 | 0 | 120 | ok | False |
| daily_signal_performance_summary |  | api | success | 200 | 120 | 1 | 120 | 120 | ok | True |
| daily_signal_performance_summary |  | blob | success | 200 |  |  |  | 120 | ok | True |
| individual_stock_available_raw_data_index |  | raw | success | 200 | 2149 | 28 | 2150 | 2150 | ok | True |
| individual_stock_available_raw_data_index |  | pages | missing_file | 404 | 0 | 0 | 0 | 2150 | ok | False |
| individual_stock_available_raw_data_index |  | api | api_decode_failed | 200 | 0 | 0 | 0 | 2150 | ok | False |
| individual_stock_available_raw_data_index |  | blob | content_not_expanded | 200 |  |  |  | 2150 | ok | False |
| individual_stock_reports_index |  | raw | success | 200 | 4 | 13 | 5 | 5 | ok | True |
| individual_stock_reports_index |  | pages | missing_file | 404 | 0 | 0 | 0 | 5 | ok | False |
| individual_stock_reports_index |  | api | success | 200 | 4 | 13 | 5 | 5 | ok | True |
| individual_stock_reports_index |  | blob | content_not_expanded | 200 |  |  |  | 5 | ok | False |
