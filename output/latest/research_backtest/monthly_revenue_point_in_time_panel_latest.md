# Monthly Revenue Point-In-Time Panel

- generated_at: `2026-07-12 16:58:53 Asia/Taipei`
- panel_id: `monthly_revenue_point_in_time_panel`
- panel_version: `daily_snapshot_observed_revenue_v1`
- source_kind: `daily_all_candidates_snapshot_observed_asof`
- status: `coverage_limited_research_only`
- allowed_use: research-only as-of join when `research_join_allowed=True`.
- forbidden_use: do not make revenue a formal historical model gate from this panel; `allowed_for_formal_historical_model_use` must remain `False` until a full release-date source is validated.
- release_date_boundary: when the source column contains a revenue year-month such as `11505`, it is treated as period metadata, not as an actual release date.

## Status Counts

| point_in_time_status | rows |
| --- | --- |
| ready_snapshot_observed_missing_release_date | 6512 |

## Snapshot Coverage

| observed_as_of_date | rows | unique_stocks |
| --- | --- | --- |
| 20260615 | 351 | 351 |
| 20260616 | 327 | 327 |
| 20260617 | 353 | 353 |
| 20260622 | 566 | 566 |
| 20260623 | 480 | 480 |
| 20260624 | 454 | 454 |
| 20260626 | 374 | 374 |
| 20260629 | 374 | 374 |
| 20260630 | 412 | 412 |
| 20260701 | 125 | 125 |
| 20260702 | 468 | 468 |
| 20260703 | 547 | 547 |
| 20260706 | 515 | 515 |
| 20260707 | 430 | 430 |
| 20260708 | 410 | 410 |
| 20260709 | 326 | 326 |

## Numerical Anomaly Labels

| revenue_numerical_anomaly_reason | rows |
| --- | --- |
| cumulative_revenue_yoy_abs_ge_500pct | 43 |
| latest_revenue_yoy_abs_ge_300pct | 194 |
| latest_revenue_yoy_abs_ge_300pct;cumulative_revenue_yoy_abs_ge_500pct | 118 |

## Sample

| observed_as_of_date | stock_id | stock_name | revenue_period | latest_revenue_yoy_pct | cumulative_revenue_yoy_pct | revenue_positive_flag | revenue_strong_flag | point_in_time_status | allowed_for_formal_historical_model_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260615 | 1102 | 亞泥 | 202605 | -1.155981889962417 | -8.278297583764248 | False | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1210 | 大成 | 202605 | 10.160866102072845 | 5.260299152079415 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1216 | 統一 | 202605 | 2.698137955165315 | 3.029530865721399 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1227 | 佳格 | 202605 | 5.440383507442792 | 8.213575593837419 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1229 | 聯華 | 202605 | -8.840017248814144 | -8.756630075866308 | False | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1303 | 南亞 | 202605 | 31.35260234219728 | 13.038717238575767 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1307 | 三芳 | 202605 | 9.148413885522777 | 3.7186151759706254 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1316 | 上曜 | 202605 | 152.96 | 138.95 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1319 | 東陽 | 202605 | 2.539306387253242 | -17.00779185697848 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1326 | 台化 | 202605 | 15.45293772932748 | 10.63219857925148 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1342 | 八貫 | 202605 | 37.20016912494105 | 26.64678034191004 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1402 | 遠東新 | 202605 | 19.43789600671313 | 4.018480051327095 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1434 | 福懋 | 202605 | 5.625479396216586 | -5.595008577657048 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1440 | 南紡 | 202605 | -13.433878339303774 | -17.77879777772479 | False | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1447 | 力鵬 | 202605 | -45.56331500781842 | 3.9370406197863046 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1449 | 佳和 | 202605 | 98.72 | 44.35 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1504 | 東元 | 202605 | 10.55212011300114 | 7.192093297117473 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1513 | 中興電 | 202605 | 3.61626985725604 | 2.325232220096636 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1514 | 亞力 | 202605 | -30.827827257260537 | 10.770090213425329 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1532 | 勤美 | 202605 | 26.03639140629689 | 12.235327355322426 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1560 | 中砂 | 202605 | 17.780558404040463 | 24.517713602426284 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1597 | 直得 | 202605 | 51.38 | 44.13 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1605 | 華新 | 202605 | 11.130693995600756 | -5.3630528138921845 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1608 | 華榮 | 202605 | 7.832588367750069 | 16.303642395423676 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1609 | 大亞 | 202605 | 21.98 | 18.2 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1612 | 宏泰 | 202605 | -13.62685024739556 | 1.124191097261592 | True | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1618 | 合機 | 202605 | 153.16268341919277 | -7.777041541987246 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1708 | 東鹼 | 202605 | 18.3827165106022 | 13.182001902430631 | True | True | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1710 | 東聯 | 202605 | -28.89570420595356 | -10.258738178818136 | False | False | ready_snapshot_observed_missing_release_date | False |
| 20260615 | 1711 | 永光 | 202605 | 9.417415608106976 | 4.695985179076647 | True | False | ready_snapshot_observed_missing_release_date | False |
