# Monthly Revenue History Data Layer

- generated_at: `2026-07-17 23:29:51 Asia/Taipei`
- history_id: `monthly_revenue_history`
- history_version: `official_mops_monthly_revenue_v1`
- source_kind: `official_mops_current_monthly_revenue_openapi;official_mops_static_monthly_revenue_html_conservative_available_date_v1`
- source_fetch_mode: `official_current_sources`
- latest_build_rows: `1973`
- total_history_rows: `50999`
- unique_stocks: `1974`
- revenue_period_min: `202405`
- revenue_period_max: `202606`
- allowed_use: save full-market official monthly revenue rows and join research rows where `source_table_date <= signal_date`.
- forbidden_use: do not label older historical signals with the latest saved revenue period; formal model gates require sufficient coverage audit and promotion.
- current_limitation: the current official OpenAPI returns the latest available revenue period only; older periods require validated historical backfill or accumulation over future runs.
- historical_backfill_policy: static MOPS monthly revenue HTML backfill uses a conservative next-month-17 source date so historical research joins do not look ahead.
- official_source_fallback_policy: if any official OpenAPI source is empty or unavailable, reuse validated cached history for at most `25` days from its latest `source_table_date`; stale cache fails closed.

## Source Fetch Status

| market | source_market_name | raw_rows | standardized_rows | status |
| --- | --- | --- | --- | --- |
| listed | TWSE | 1082 | 1082 | ok |
| otc | TPEX | 891 | 891 | ok |

## Period Coverage

| revenue_period | rows | unique_stocks | source_table_date |
| --- | --- | --- | --- |
| 202405 | 1929 | 1929 | 20240617 |
| 202406 | 1931 | 1931 | 20240717 |
| 202407 | 1933 | 1933 | 20240817 |
| 202408 | 1940 | 1940 | 20240917 |
| 202409 | 1943 | 1943 | 20241017 |
| 202410 | 1951 | 1951 | 20241117 |
| 202411 | 1957 | 1957 | 20241217 |
| 202412 | 1960 | 1960 | 20250117 |
| 202501 | 1962 | 1962 | 20250217 |
| 202502 | 1962 | 1962 | 20250317 |
| 202503 | 1964 | 1964 | 20250417 |
| 202504 | 1966 | 1966 | 20250517 |
| 202505 | 1969 | 1969 | 20250617 |
| 202506 | 1970 | 1970 | 20250717 |
| 202507 | 1970 | 1970 | 20250817 |
| 202508 | 1971 | 1971 | 20250917 |
| 202509 | 1971 | 1971 | 20251017 |
| 202510 | 1971 | 1971 | 20251117 |
| 202511 | 1972 | 1972 | 20251217 |
| 202512 | 1972 | 1972 | 20260117 |
| 202601 | 1972 | 1972 | 20260217 |
| 202602 | 1972 | 1972 | 20260317 |
| 202603 | 1972 | 1972 | 20260417 |
| 202604 | 1972 | 1972 | 20260517 |
| 202605 | 1973 | 1973 | 20260617 |
| 202606 | 1974 | 1973 | 20260717 |

## Market Coverage

| revenue_period | market | rows | unique_stocks |
| --- | --- | --- | --- |
| 202405 | listed | 1053 | 1053 |
| 202405 | otc | 876 | 876 |
| 202406 | listed | 1054 | 1054 |
| 202406 | otc | 877 | 877 |
| 202407 | listed | 1056 | 1056 |
| 202407 | otc | 877 | 877 |
| 202408 | listed | 1060 | 1060 |
| 202408 | otc | 880 | 880 |
| 202409 | listed | 1062 | 1062 |
| 202409 | otc | 881 | 881 |
| 202410 | listed | 1067 | 1067 |
| 202410 | otc | 884 | 884 |
| 202411 | listed | 1073 | 1073 |
| 202411 | otc | 884 | 884 |
| 202412 | listed | 1073 | 1073 |
| 202412 | otc | 887 | 887 |
| 202501 | listed | 1074 | 1074 |
| 202501 | otc | 888 | 888 |
| 202502 | listed | 1074 | 1074 |
| 202502 | otc | 888 | 888 |
| 202503 | listed | 1075 | 1075 |
| 202503 | otc | 889 | 889 |
| 202504 | listed | 1077 | 1077 |
| 202504 | otc | 889 | 889 |
| 202505 | listed | 1078 | 1078 |
| 202505 | otc | 891 | 891 |
| 202506 | listed | 1079 | 1079 |
| 202506 | otc | 891 | 891 |
| 202507 | listed | 1079 | 1079 |
| 202507 | otc | 891 | 891 |
| 202508 | listed | 1080 | 1080 |
| 202508 | otc | 891 | 891 |
| 202509 | listed | 1080 | 1080 |
| 202509 | otc | 891 | 891 |
| 202510 | listed | 1080 | 1080 |
| 202510 | otc | 891 | 891 |
| 202511 | listed | 1081 | 1081 |
| 202511 | otc | 891 | 891 |
| 202512 | listed | 1081 | 1081 |
| 202512 | otc | 891 | 891 |
| 202601 | listed | 1081 | 1081 |
| 202601 | otc | 891 | 891 |
| 202602 | listed | 1081 | 1081 |
| 202602 | otc | 891 | 891 |
| 202603 | listed | 1081 | 1081 |
| 202603 | otc | 891 | 891 |
| 202604 | listed | 1081 | 1081 |
| 202604 | otc | 891 | 891 |
| 202605 | listed | 1082 | 1082 |
| 202605 | otc | 891 | 891 |
| 202606 | listed | 1082 | 1082 |
| 202606 | otc | 892 | 892 |

## Numerical Anomaly Labels

| revenue_numerical_anomaly_reason | rows |
| --- | --- |
| latest_revenue_yoy_abs_ge_300pct | 721 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct | 370 |
| cumulative_revenue_yoy_abs_ge_500pct | 135 |
| monthly_revenue_negative | 59 |
| latest_revenue_yoy_abs_ge_300pct;monthly_revenue_negative | 6 |
| cumulative_revenue_yoy_abs_ge_500pct;monthly_revenue_negative | 4 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct;monthly_revenue_negative | 3 |

## Current Sample

| market | stock_id | stock_name | revenue_period | source_table_date | latest_revenue_yoy_pct | cumulative_revenue_yoy_pct | revenue_strong_flag | allowed_for_formal_historical_model_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| listed | 1101 | 台泥 | 202606 | 20260717 | 32.398782 | 1.543623 | True | False |
| listed | 1102 | 亞泥 | 202606 | 20260717 | -2.214992 | -7.243233 | False | False |
| listed | 1103 | 嘉泥 | 202606 | 20260717 | -7.487762 | -10.868285 | False | False |
| listed | 1104 | 環泥 | 202606 | 20260717 | -18.912238 | -8.67728 | False | False |
| listed | 1108 | 幸福 | 202606 | 20260717 | -26.577034 | -19.775325 | False | False |
| listed | 1109 | 信大 | 202606 | 20260717 | -19.632053 | -16.391429 | False | False |
| listed | 1110 | 東泥 | 202606 | 20260717 | -4.010288 | -14.886927 | False | False |
| listed | 1201 | 味全 | 202606 | 20260717 | 5.130475 | -2.668287 | False | False |
| listed | 1203 | 味王 | 202606 | 20260717 | -1.127329 | -11.331677 | False | False |
| listed | 1210 | 大成 | 202606 | 20260717 | 12.173234 | 6.358784 | False | False |
| listed | 1213 | 大飲 | 202606 | 20260717 | 5.661482 | 11.387508 | True | False |
| listed | 1215 | 卜蜂 | 202606 | 20260717 | 8.691479 | 4.678387 | False | False |
| listed | 1216 | 統一 | 202606 | 20260717 | 4.598464 | 3.287616 | False | False |
| listed | 1217 | 愛之味 | 202606 | 20260717 | -2.410799 | -3.05597 | False | False |
| listed | 1218 | 泰山 | 202606 | 20260717 | -11.863344 | 1.953052 | False | False |
| listed | 1219 | 福壽 | 202606 | 20260717 | 0.404703 | -0.885568 | False | False |
| listed | 1220 | 台榮 | 202606 | 20260717 | 6.909244 | -3.010892 | False | False |
| listed | 1225 | 福懋油 | 202606 | 20260717 | 2.28427 | 3.167509 | False | False |
| listed | 1227 | 佳格 | 202606 | 20260717 | -1.565959 | 6.729979 | False | False |
| listed | 1229 | 聯華 | 202606 | 20260717 | -52.010749 | -22.928885 | False | False |
| listed | 1231 | 聯華食 | 202606 | 20260717 | 6.954929 | 4.382676 | False | False |
| listed | 1232 | 大統益 | 202606 | 20260717 | 16.299889 | 9.338003 | False | False |
| listed | 1233 | 天仁 | 202606 | 20260717 | 19.862153 | 4.816271 | False | False |
| listed | 1234 | 黑松 | 202606 | 20260717 | -5.28873 | -5.537952 | False | False |
| listed | 1235 | 興泰 | 202606 | 20260717 | -6.83966 | 37.048555 | True | False |
| listed | 1236 | 宏亞 | 202606 | 20260717 | 14.115905 | 4.151382 | False | False |
| listed | 1256 | 鮮活果汁-KY | 202606 | 20260717 | 52.27924 | 47.491044 | True | False |
| listed | 1301 | 台塑 | 202606 | 20260717 | -2.686567 | -3.618362 | False | False |
| listed | 1303 | 南亞 | 202606 | 20260717 | 31.786107 | 15.979324 | True | False |
| listed | 1304 | 台聚 | 202606 | 20260717 | -26.33844 | -8.266764 | False | False |
