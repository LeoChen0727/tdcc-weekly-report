# Monthly Revenue History Data Layer

- generated_at: `2026-07-04 17:24:33 Asia/Taipei`
- history_id: `monthly_revenue_history`
- history_version: `official_mops_monthly_revenue_v1`
- source_kind: `official_mops_current_monthly_revenue_openapi;official_mops_static_monthly_revenue_html_conservative_available_date_v1`
- latest_build_rows: `49024`
- total_history_rows: `49025`
- unique_stocks: `1973`
- revenue_period_min: `202405`
- revenue_period_max: `202605`
- allowed_use: save full-market official monthly revenue rows and join research rows where `source_table_date <= signal_date`.
- forbidden_use: do not label older historical signals with the latest saved revenue period; formal model gates require sufficient coverage audit and promotion.
- current_limitation: the current official OpenAPI returns the latest available revenue period only; older periods require validated historical backfill or accumulation over future runs.
- historical_backfill_policy: static MOPS monthly revenue HTML backfill uses a conservative next-month-17 source date so historical research joins do not look ahead.

## Source Fetch Status

| market | source_market_name | raw_rows | standardized_rows | status |
| --- | --- | --- | --- | --- |
| listed | TWSE | 968 | 968 | ok |
| listed | TWSE | 85 | 85 | ok |
| otc | TPEX | 846 | 846 | ok |
| otc | TPEX | 30 | 30 | ok |
| listed | TWSE | 969 | 969 | ok |
| listed | TWSE | 85 | 85 | ok |
| otc | TPEX | 847 | 847 | ok |
| otc | TPEX | 30 | 30 | ok |
| listed | TWSE | 971 | 971 | ok |
| listed | TWSE | 85 | 85 | ok |

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

## Numerical Anomaly Labels

| revenue_numerical_anomaly_reason | rows |
| --- | --- |
| latest_revenue_yoy_abs_ge_300pct | 693 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct | 353 |
| cumulative_revenue_yoy_abs_ge_500pct | 122 |
| monthly_revenue_negative | 59 |
| latest_revenue_yoy_abs_ge_300pct;monthly_revenue_negative | 6 |
| cumulative_revenue_yoy_abs_ge_500pct;monthly_revenue_negative | 4 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct;monthly_revenue_negative | 3 |

## Current Sample

| market | stock_id | stock_name | revenue_period | source_table_date | latest_revenue_yoy_pct | cumulative_revenue_yoy_pct | revenue_strong_flag | allowed_for_formal_historical_model_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| listed | 1101 | 台泥 | 202405 | 20240617 | 44.43 | 13.57 | True | False |
| listed | 1102 | 亞泥 | 202405 | 20240617 | -10.75 | -14.78 | False | False |
| listed | 1103 | 嘉泥 | 202405 | 20240617 | 7.03 | 7.42 | False | False |
| listed | 1104 | 環泥 | 202405 | 20240617 | 10.74 | 5.96 | False | False |
| listed | 1108 | 幸福 | 202405 | 20240617 | -9.78 | 4.24 | False | False |
| listed | 1109 | 信大 | 202405 | 20240617 | -17.63 | -18.22 | False | False |
| listed | 1110 | 東泥 | 202405 | 20240617 | -4.37 | 2.81 | False | False |
| listed | 1201 | 味全 | 202405 | 20240617 | 17.41 | 12.83 | True | False |
| listed | 1203 | 味王 | 202405 | 20240617 | -7.26 | -2.71 | False | False |
| listed | 1210 | 大成 | 202405 | 20240617 | -12.25 | -7.23 | False | False |
| listed | 1213 | 大飲 | 202405 | 20240617 | 24.78 | -48.15 | True | False |
| listed | 1215 | 卜蜂 | 202405 | 20240617 | -6.08 | -6.09 | False | False |
| listed | 1216 | 統一 | 202405 | 20240617 | 18.21 | 19.86 | True | False |
| listed | 1217 | 愛之味 | 202405 | 20240617 | 12.13 | 2.43 | False | False |
| listed | 1218 | 泰山 | 202405 | 20240617 | -5.03 | 2.98 | False | False |
| listed | 1219 | 福壽 | 202405 | 20240617 | -15.8 | -14.15 | False | False |
| listed | 1220 | 台榮 | 202405 | 20240617 | 4.43 | 9.16 | False | False |
| listed | 1225 | 福懋油 | 202405 | 20240617 | -17.55 | -11.44 | False | False |
| listed | 1227 | 佳格 | 202405 | 20240617 | 8.29 | 10.98 | True | False |
| listed | 1229 | 聯華 | 202405 | 20240617 | 7.35 | 11.42 | True | False |
| listed | 1231 | 聯華食 | 202405 | 20240617 | 16.42 | 7.16 | False | False |
| listed | 1232 | 大統益 | 202405 | 20240617 | -7.52 | -7.27 | False | False |
| listed | 1233 | 天仁 | 202405 | 20240617 | 5.07 | 8.22 | False | False |
| listed | 1234 | 黑松 | 202405 | 20240617 | 4.44 | 2.56 | False | False |
| listed | 1235 | 興泰 | 202405 | 20240617 | 18.1 | 170.19 | True | False |
| listed | 1236 | 宏亞 | 202405 | 20240617 | -0.95 | 8.1 | False | False |
| listed | 1256 | 鮮活果汁-KY | 202405 | 20240617 | -24.2 | -5.85 | False | False |
| listed | 1301 | 台塑 | 202405 | 20240617 | 6.35 | -3.06 | False | False |
| listed | 1303 | 南亞 | 202405 | 20240617 | 0.53 | -5.92 | False | False |
| listed | 1304 | 台聚 | 202405 | 20240617 | 1.05 | -4.54 | False | False |
