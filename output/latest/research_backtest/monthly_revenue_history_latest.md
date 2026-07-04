# Monthly Revenue History Data Layer

- generated_at: `2026-07-04 16:20:04 Asia/Taipei`
- history_id: `monthly_revenue_history`
- history_version: `official_mops_monthly_revenue_v1`
- source_kind: `official_mops_current_monthly_revenue_openapi`
- current_fetch_rows: `1972`
- total_history_rows: `1972`
- unique_stocks: `1972`
- revenue_period_min: `202605`
- revenue_period_max: `202605`
- allowed_use: save full-market official monthly revenue rows and join research rows where `source_table_date <= signal_date`.
- forbidden_use: do not label older historical signals with the latest saved revenue period; formal model gates require sufficient coverage audit and promotion.
- current_limitation: the current official OpenAPI returns the latest available revenue period only; older periods require separate validated backfill or accumulation over future runs.

## Source Fetch Status

| market | source_market_name | raw_rows | standardized_rows | status |
| --- | --- | --- | --- | --- |
| listed | TWSE | 1082 | 1082 | ok |
| otc | TPEX | 890 | 890 | ok |

## Period Coverage

| revenue_period | rows | unique_stocks | source_table_date |
| --- | --- | --- | --- |
| 202605 | 1972 | 1972 | 20260617 |

## Market Coverage

| revenue_period | market | rows | unique_stocks |
| --- | --- | --- | --- |
| 202605 | listed | 1082 | 1082 |
| 202605 | otc | 890 | 890 |

## Numerical Anomaly Labels

| revenue_numerical_anomaly_reason | rows |
| --- | --- |
| latest_revenue_yoy_abs_ge_300pct | 29 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct | 26 |
| cumulative_revenue_yoy_abs_ge_500pct | 11 |
| monthly_revenue_negative | 1 |

## Current Sample

| market | stock_id | stock_name | revenue_period | source_table_date | latest_revenue_yoy_pct | cumulative_revenue_yoy_pct | revenue_strong_flag | allowed_for_formal_historical_model_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| listed | 1101 | 台泥 | 202605 | 20260617 | -0.059289 | -3.630832 | False | False |
| listed | 1102 | 亞泥 | 202605 | 20260617 | -1.155982 | -8.278298 | False | False |
| listed | 1103 | 嘉泥 | 202605 | 20260617 | -7.503351 | -11.526188 | False | False |
| listed | 1104 | 環泥 | 202605 | 20260617 | 1.976346 | -6.714901 | False | False |
| listed | 1108 | 幸福 | 202605 | 20260617 | -13.762221 | -18.553815 | False | False |
| listed | 1109 | 信大 | 202605 | 20260617 | -14.512022 | -15.699717 | False | False |
| listed | 1110 | 東泥 | 202605 | 20260617 | -10.648509 | -16.79678 | False | False |
| listed | 1201 | 味全 | 202605 | 20260617 | -5.081564 | -4.173858 | False | False |
| listed | 1203 | 味王 | 202605 | 20260617 | -10.047941 | -13.088339 | False | False |
| listed | 1210 | 大成 | 202605 | 20260617 | 10.160866 | 5.260299 | False | False |
| listed | 1213 | 大飲 | 202605 | 20260617 | 14.295725 | 12.618175 | True | False |
| listed | 1215 | 卜蜂 | 202605 | 20260617 | 1.654683 | 3.903628 | False | False |
| listed | 1216 | 統一 | 202605 | 20260617 | 2.698138 | 3.029531 | False | False |
| listed | 1217 | 愛之味 | 202605 | 20260617 | -14.606255 | -3.192754 | False | False |
| listed | 1218 | 泰山 | 202605 | 20260617 | -1.424326 | 4.664707 | False | False |
| listed | 1219 | 福壽 | 202605 | 20260617 | -6.859445 | -1.120462 | False | False |
| listed | 1220 | 台榮 | 202605 | 20260617 | -12.603967 | -4.965069 | False | False |
| listed | 1225 | 福懋油 | 202605 | 20260617 | 2.269763 | 3.333176 | False | False |
| listed | 1227 | 佳格 | 202605 | 20260617 | 5.440384 | 8.213576 | False | False |
| listed | 1229 | 聯華 | 202605 | 20260617 | -8.840017 | -8.75663 | False | False |
| listed | 1231 | 聯華食 | 202605 | 20260617 | -3.14559 | 3.90088 | False | False |
| listed | 1232 | 大統益 | 202605 | 20260617 | 9.902577 | 8.082455 | False | False |
| listed | 1233 | 天仁 | 202605 | 20260617 | -3.792582 | 2.138665 | False | False |
| listed | 1234 | 黑松 | 202605 | 20260617 | -22.71679 | -5.586742 | False | False |
| listed | 1235 | 興泰 | 202605 | 20260617 | -37.976163 | 46.889591 | True | False |
| listed | 1236 | 宏亞 | 202605 | 20260617 | -4.286211 | 2.874026 | False | False |
| listed | 1256 | 鮮活果汁-KY | 202605 | 20260617 | 23.65197 | 46.773658 | True | False |
| listed | 1301 | 台塑 | 202605 | 20260617 | 0.669262 | -3.789435 | False | False |
| listed | 1303 | 南亞 | 202605 | 20260617 | 31.352602 | 13.038717 | True | False |
| listed | 1304 | 台聚 | 202605 | 20260617 | -1.425242 | -4.701645 | False | False |
