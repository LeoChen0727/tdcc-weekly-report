# 營收爆發低反應股 Debug Report

- 產生時間：`2026-05-21 00:36:05 Asia/Taipei`

## 診斷統計

| item | value |
|---|---:|
| raw_revenue_rows | 1958 |
| standardized_revenue_rows | 0 |
| price_rows | 251211 |
| tdcc_rows | 1968 |
| revenue_condition_pass | 0 |
| price_metrics_pass | 0 |
| low_response_pass | 0 |
| overheat_pass | 0 |
| score_pass | 0 |
| final_rows | 0 |

## 營收欄位狀態

- revenue_schema_status：`missing_code_or_latest_yoy`

### selected_revenue_columns

| field | selected column |
|---|---|
| code_col | `ticker` |
| name_col | `name` |
| industry_col | `industry` |
| date_col | `None` |
| latest_revenue_col | `monthly_revenue` |
| latest_yoy_col | `None` |
| cumulative_yoy_col | `None` |

### raw_revenue_columns

- `ticker`
- `name`
- `industry`
- `revenue_period`
- `monthly_revenue`
- `revenue_yoy_pct`
- `cumulative_yoy_pct`
- `market`

## 主要刷掉原因

| reason | count |
|---|---:|
| price_or_revenue_empty | 1 |

## 樣本資料

沒有樣本資料。