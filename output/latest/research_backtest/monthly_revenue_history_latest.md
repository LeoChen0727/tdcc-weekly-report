# Monthly Revenue History Data Layer

- generated_at: `2026-10-20 19:32:17 Asia/Taipei`
- history_id: `monthly_revenue_history`
- history_version: `official_mops_monthly_revenue_v1`
- source_kind: `official_mops_current_monthly_revenue_openapi;official_mops_static_monthly_revenue_html_conservative_available_date_v1`
- source_fetch_mode: `official_current_sources`
- latest_build_rows: `1981`
- total_history_rows: `56933`
- unique_stocks: `1986`
- revenue_period_min: `202405`
- revenue_period_max: `202609`
- allowed_use: save full-market official monthly revenue rows and join research rows where `source_table_date <= signal_date`.
- forbidden_use: do not label older historical signals with the latest saved revenue period; formal model gates require sufficient coverage audit and promotion.
- current_limitation: the current official OpenAPI returns the latest available revenue period only; older periods require validated historical backfill or accumulation over future runs.
- historical_backfill_policy: static MOPS monthly revenue HTML backfill uses a conservative next-month-17 source date so historical research joins do not look ahead.
- official_source_fallback_policy: if any official OpenAPI source is empty or unavailable, reuse validated cached history for at most `25` days from its latest `source_table_date`; stale cache fails closed.

## Source Fetch Status

| market | source_market_name | raw_rows | standardized_rows | status |
| --- | --- | --- | --- | --- |
| listed | TWSE | 1088 | 1088 | ok |
| otc | TPEX | 893 | 893 | ok |

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
| 202607 | 1975 | 1975 | 20260817 |
| 202608 | 1978 | 1978 | 20260917 |
| 202609 | 1981 | 1981 | 20261017 |

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
| 202607 | listed | 1085 | 1085 |
| 202607 | otc | 890 | 890 |
| 202608 | listed | 1086 | 1086 |
| 202608 | otc | 892 | 892 |
| 202609 | listed | 1088 | 1088 |
| 202609 | otc | 893 | 893 |

## Numerical Anomaly Labels

| revenue_numerical_anomaly_reason | rows |
| --- | --- |
| latest_revenue_yoy_abs_ge_300pct | 814 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct | 415 |
| cumulative_revenue_yoy_abs_ge_500pct | 158 |
| monthly_revenue_negative | 64 |
| latest_revenue_yoy_abs_ge_300pct;monthly_revenue_negative | 8 |
| cumulative_revenue_yoy_abs_ge_500pct;monthly_revenue_negative | 5 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct;monthly_revenue_negative | 5 |

## Current Sample

| market | stock_id | stock_name | revenue_period | source_table_date | latest_revenue_yoy_pct | cumulative_revenue_yoy_pct | revenue_strong_flag | allowed_for_formal_historical_model_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| listed | 1101 | 台泥 | 202609 | 20261017 | 7.626848 | 3.298871 | False | False |
| listed | 1102 | 亞泥 | 202609 | 20261017 | 5.180647 | -5.145623 | False | False |
| listed | 1103 | 嘉泥 | 202609 | 20261017 | 6.0338 | -7.426 | False | False |
| listed | 1104 | 環泥 | 202609 | 20261017 | -12.900636 | -7.380784 | False | False |
| listed | 1108 | 幸福 | 202609 | 20261017 | -13.852373 | -18.086386 | False | False |
| listed | 1109 | 信大 | 202609 | 20261017 | -25.756107 | -19.03068 | False | False |
| listed | 1110 | 東泥 | 202609 | 20261017 | -13.219309 | -11.564033 | False | False |
| listed | 1201 | 味全 | 202609 | 20261017 | -12.34113 | -2.30957 | False | False |
| listed | 1203 | 味王 | 202609 | 20261017 | 0.555465 | -8.113007 | False | False |
| listed | 1210 | 大成 | 202609 | 20261017 | 13.154914 | 9.524322 | False | False |
| listed | 1213 | 大飲 | 202609 | 20261017 | -8.728647 | 12.14195 | True | False |
| listed | 1215 | 卜蜂 | 202609 | 20261017 | 6.245093 | 4.864147 | False | False |
| listed | 1216 | 統一 | 202609 | 20261017 | 5.803451 | 4.248855 | False | False |
| listed | 1217 | 愛之味 | 202609 | 20261017 | 2.269817 | 1.11022 | False | False |
| listed | 1218 | 泰山 | 202609 | 20261017 | -43.850392 | -14.379089 | False | False |
| listed | 1219 | 福壽 | 202609 | 20261017 | -28.488153 | -7.502533 | False | False |
| listed | 1220 | 台榮 | 202609 | 20261017 | 17.693814 | 3.561629 | False | False |
| listed | 1225 | 福懋油 | 202609 | 20261017 | -9.763937 | -2.418346 | False | False |
| listed | 1227 | 佳格 | 202609 | 20261017 | 8.665462 | 7.573325 | False | False |
| listed | 1229 | 聯華 | 202609 | 20261017 | 2.130978 | -4.908445 | False | False |
| listed | 1231 | 聯華食 | 202609 | 20261017 | -7.68312 | 2.733662 | False | False |
| listed | 1232 | 大統益 | 202609 | 20261017 | 32.882645 | 18.417291 | True | False |
| listed | 1233 | 天仁 | 202609 | 20261017 | 5.124572 | 5.183393 | False | False |
| listed | 1234 | 黑松 | 202609 | 20261017 | 6.316727 | -2.441295 | False | False |
| listed | 1235 | 興泰 | 202609 | 20261017 | -52.656783 | -3.901921 | False | False |
| listed | 1236 | 宏亞 | 202609 | 20261017 | -1.628445 | 4.787249 | False | False |
| listed | 1256 | 鮮活果汁-KY | 202609 | 20261017 | 33.804864 | 38.128156 | True | False |
| listed | 1301 | 台塑 | 202609 | 20261017 | 7.138175 | -0.568499 | False | False |
| listed | 1303 | 南亞 | 202609 | 20261017 | 55.258572 | 26.808141 | True | False |
| listed | 1304 | 台聚 | 202609 | 20261017 | 3.890561 | -4.965893 | False | False |
