# Raw Data Fetch Status

- generated_at: 2026-05-25 22:43:01 Asia/Taipei
- sources_checked: raw
- checked_rows: 21
- success_rows: 21
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
| all_candidates |  | raw | success | 200 | 519 | 205 | 520 | 520 | ok | True |
| candidate_repeat_appearance |  | raw | success | 200 | 400 | 13 | 401 | 401 | ok | True |
| daily_market_full |  | raw | success | 200 | 567 | 1 | 567 | 567 | ok | True |
| daily_market_summary |  | raw | success | 200 | 447 | 1 | 447 | 447 | ok | True |
| daily_report_packet |  | raw | success | 200 | 1175 | 1 | 1175 | 1175 | ok | True |
| daily_signal_performance_summary |  | raw | success | 200 | 120 | 1 | 120 | 120 | ok | True |
| individual_stock_available_raw_data_index |  | raw | success | 200 | 2149 | 28 | 2150 | 2150 | ok | True |
| individual_stock_reports_index |  | raw | success | 200 | 4 | 13 | 5 | 5 | ok | True |
| readme_first |  | raw | success | 200 | 122 | 1 | 122 | 122 | ok | True |
| stock_monitor |  | raw | success | 200 | 161 | 1 | 161 | 161 | ok | True |
| surge_model_backtest |  | raw | success | 200 | 15 | 17 | 16 | 16 | ok | True |
| surge_model_feature_importance |  | raw | success | 200 | 10 | 14 | 11 | 11 | ok | True |
| surge_model_packet |  | raw | success | 200 | 109 | 1 | 109 | 109 | ok | True |
| surge_precondition_candidates |  | raw | success | 200 | 100 | 19 | 101 | 101 | ok | True |
| tdcc_phase_distribution |  | raw | success | 200 | 112 | 18 | 113 | 113 | ok | True |
| tdcc_pre_move_abm_top |  | raw | success | 200 | 50 | 28 | 51 | 51 | ok | True |
| tdcc_strength_ranking_top |  | raw | success | 200 | 50 | 27 | 51 | 51 | ok | True |
| tdcc_top_risk_list |  | raw | success | 200 | 60 | 13 | 61 | 61 | ok | True |
| tdcc_tracking_packet |  | raw | success | 200 | 661 | 1 | 661 | 661 | ok | True |
| warrant_flow_by_stock |  | raw | success | 200 | 455 | 38 | 456 | 456 | ok | True |
| warrant_market_report |  | raw | success | 200 | 197 | 1 | 197 | 197 | ok | True |
