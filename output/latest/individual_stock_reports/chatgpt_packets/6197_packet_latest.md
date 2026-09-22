# INDIVIDUAL STOCK CHATGPT PACKET - 6197 佳必琪

## Metadata
- generated_at: 2026-09-20 22:17:45 Asia/Taipei
- stock_id: 6197
- stock_name: 佳必琪
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6197_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6197_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6197_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6197_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6197_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6197_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6197_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6197_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6197_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6197_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6197_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6197_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6197.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6197.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6197.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6197.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6197_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6197_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6197_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure
- acceptable_risk_reward

### post_entry_watch_items
- next_monthly_revenue
- next_tdcc_update
- 23ema_hold_or_reclaim
- volume_price_confirmation
- prior_high_breakout_quality
- sector_benchmark_strength
- event_follow_through
- warrant_overheat_check

### downgrade_reason
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260918
- open: 310
- high: 323.5
- low: 309
- close: 320.5
- volume: 3872484
- ma5: 301.8
- ema23_primary: 304.11
- distance_to_ema23_pct: 5.39
- ma20: 304.07
- ma60: 313.96
- ma120: 280.49
- return_5d: 6.83
- return_20d: 10.33
- volume_ratio: 2.29
- distance_to_ma20_pct_auxiliary: 5.4
- distance_to_high_60_pct: -20.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,288.5,295.5,288.5,290,371451,303.7,-4.51,298.38,322.38,0.23
20260825,292,299.5,284,299,876564,303.31,-1.42,298.82,322.41,0.55
20260826,303,309,301.5,307,1733571,303.62,1.11,300.3,322.38,1.14
20260827,309,312,305,308,1274479,303.98,1.32,302.43,322.32,0.86
20260828,311,314,309.5,309.5,1256784,304.44,1.66,303.45,322,0.86
20260831,305,308.5,300,302.5,1032324,304.28,-0.59,303.45,321.77,0.72
20260901,304,321.5,304,317,1926759,305.34,3.82,303.9,321.63,1.37
20260902,322,333.5,313.5,313.5,6629877,306.02,2.44,303.95,321.41,4.03
20260903,314,315.5,299,299,2845571,305.44,-2.11,303.07,320.68,1.68
20260904,301,317.5,294.5,315,3153237,306.23,2.86,304.15,320.5,1.89
20260907,316,317,308,308,1708357,306.38,0.53,304.1,320.34,1.04
20260908,310,310,300,300.5,1048510,305.89,-1.76,304.05,319.89,0.64
20260909,305,308,301.5,302.5,728834,305.61,-1.02,303.9,319.41,0.45
20260910,300.5,304.5,298.5,301,709344,305.22,-1.38,303.35,319.08,0.46
20260911,298,304.5,298,300,1083400,304.79,-1.57,303,318.53,0.71
20260914,298,301,294.5,297,815302,304.14,-2.35,302.77,317.69,0.53
20260915,297,300,292,292,762733,303.13,-3.67,302.68,316.68,0.5
20260916,293.5,299.5,292.5,295,507371,302.45,-2.46,302.38,315.76,0.34
20260917,302,309.5,300,304.5,1462984,302.62,0.62,302.57,314.84,0.96
20260918,310,323.5,309,320.5,3872484,304.11,5.39,304.07,313.96,2.29
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 44.47
- over_600_ratio: 40.35
- over_800_ratio: 38.72
- over_1000_ratio: 35.79
- over_400_change_1w: 0.27
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.84
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,47.15,-0.98,42.51,0.42,39.56,-0.4,5,False,True
20260709,46.31,-0.84,41.63,-0.88,39.44,-0.12,0,False,False
20260717,45.39,-0.92,40.78,-0.85,39.32,-0.12,0,False,False
20260724,45.8,0.41,40.27,-0.51,38.82,-0.5,1,False,False
20260731,46.16,0.36,40.21,-0.06,37.98,-0.84,2,False,False
20260807,46.21,0.05,40.02,-0.19,37.8,-0.18,3,False,False
20260814,44.84,-1.37,39.74,-0.28,37.54,-0.26,0,False,False
20260821,45.14,0.3,39.68,-0.06,37.57,0.03,1,False,True
20260828,44.52,-0.62,39.06,-0.62,37.62,0.05,2,False,True
20260904,44.21,-0.31,38.79,-0.27,36.64,-0.98,0,False,False
20260911,44.2,-0.01,38.74,-0.05,36.63,-0.01,1,False,False
20260918,44.47,0.27,38.72,-0.02,35.79,-0.84,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6197 | 佳必琪 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | call_strong_inflow | continued_2_3d | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 普通股現金股利新台幣854,601,174元，合計每股配發新台幣7.0元。 3.變更後發放股利種類及金額: 普通股現金股利新台幣854,601,174元，合計每股配發新台幣6.92325997元。 4.變更原因: 因本公司國內無擔保轉換公司債轉換成普通股，致使本公司流通在外股數 發生變動而影響股東配息比率異動，依民國115年03月06日董事會決議由 董事會授權董事長調整配息率。 5.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6197 | 佳必琪 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_strong_inflow | continued_2_3d | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 普通股現金股利新台幣854,601,174元，合計每股配發新台幣7.0元。 3.變更後發放股利種類及金額: 普通股現金股利新台幣854,601,174元，合計每股配發新台幣6.92325997元。 4.變更原因: 因本公司國內無擔保轉換公司債轉換成普通股，致使本公司流通在外股數 發生變動而影響股東配息比率異動，依民國115年03月06日董事會決議由 董事會授權董事長調整配息率。 5.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 6197 | 佳必琪 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  | call_strong_inflow | continued_2_3d | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 普通股現金股利新台幣854,601,174元，合計每股配發新台幣7.0元。 3.變更後發放股利種類及金額: 普通股現金股利新台幣854,601,174元，合計每股配發新台幣6.92325997元。 4.變更原因: 因本公司國內無擔保轉換公司債轉換成普通股，致使本公司流通在外股數 發生變動而影響股東配息比率異動，依民國115年03月06日董事會決議由 董事會授權董事長調整配息率。 5.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6197 | 佳必琪 | 2 | 2 | 3 | 5 | 9 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6197 | 佳必琪 | 125 | 0 | 25423610.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
