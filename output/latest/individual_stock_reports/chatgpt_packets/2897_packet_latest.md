# INDIVIDUAL STOCK CHATGPT PACKET - 2897 王道銀行

## Metadata
- generated_at: 2026-08-22 22:27:12 Asia/Taipei
- stock_id: 2897
- stock_name: 王道銀行
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2897_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2897_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2897_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2897_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2897_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2897_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2897_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2897_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2897_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2897_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2897_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2897_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2897.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2897.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2897.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2897.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2897_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2897_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2897_latest.md?ref=main

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
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260821
- open: 10.2
- high: 10.25
- low: 10.15
- close: 10.25
- volume: 2544347
- ma5: 10.2
- ema23_primary: 10.22
- distance_to_ema23_pct: 0.3
- ma20: 10.19
- ma60: 10.33
- ma120: 10.18
- return_5d: 1.99
- return_20d: 0.99
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 0.61
- distance_to_high_60_pct: -4.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,10.15,10.35,10.1,10.3,6996219,10.4,-0.93,10.44,10.3,1.31
20260728,10.25,10.3,10.1,10.2,5142901,10.38,-1.73,10.43,10.3,0.94
20260729,10.3,10.3,10.05,10.25,10572240,10.37,-1.15,10.42,10.3,1.8
20260730,10.25,10.25,10.15,10.25,4219274,10.36,-1.05,10.41,10.3,0.72
20260731,10.2,10.4,10.2,10.25,6525868,10.35,-0.97,10.4,10.31,1.08
20260803,10.2,10.25,10.15,10.2,5939025,10.34,-1.33,10.38,10.31,0.98
20260804,10.1,10.25,10.1,10.2,4000394,10.33,-1.22,10.36,10.31,0.66
20260805,10.2,10.25,10.15,10.25,3078410,10.32,-0.68,10.35,10.31,0.51
20260806,10.15,10.2,10.1,10.1,3471362,10.3,-1.96,10.32,10.31,0.57
20260807,10.15,10.2,10.1,10.15,1977642,10.29,-1.35,10.3,10.31,0.33
20260810,10.2,10.2,10.05,10.15,2571777,10.28,-1.24,10.29,10.31,0.44
20260811,10.15,10.2,10.1,10.15,4007127,10.27,-1.14,10.27,10.31,0.7
20260812,10.1,10.15,10.05,10.1,2639935,10.25,-1.49,10.25,10.31,0.47
20260813,10.15,10.15,10.05,10.15,2558432,10.24,-0.92,10.23,10.31,0.46
20260814,10.15,10.15,10.05,10.05,2922186,10.23,-1.74,10.21,10.31,0.54
20260817,10.05,10.2,10.05,10.2,3721890,10.23,-0.25,10.21,10.32,0.72
20260818,10.15,10.15,10.05,10.15,1421906,10.22,-0.68,10.19,10.32,0.29
20260819,10.1,10.2,10.05,10.15,1637632,10.21,-0.62,10.17,10.32,0.38
20260820,10.2,10.25,10.15,10.25,3538996,10.22,0.33,10.18,10.33,0.87
20260821,10.2,10.25,10.15,10.25,2544347,10.22,0.3,10.19,10.33,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 85.92
- over_600_ratio: 83.95
- over_800_ratio: 82.73
- over_1000_ratio: 81.74
- over_400_change_1w: 0.06
- over_800_change_1w: 0.16
- over_1000_change_1w: 0.2
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,85.16,0.2,82.02,0.35,81,0.38,1,True,True
20260612,85.47,0.31,82.39,0.37,81.33,0.33,2,True,True
20260618,85.56,0.09,82.32,-0.07,81.18,-0.15,3,False,False
20260626,85.58,0.02,82.45,0.13,81.21,0.03,4,True,True
20260703,85.53,-0.05,82.39,-0.06,81.3,0.09,5,False,True
20260709,85.62,0.09,82.49,0.1,81.41,0.11,6,True,True
20260717,85.57,-0.05,82.27,-0.22,81.24,-0.17,0,False,False
20260724,85.56,-0.01,82.19,-0.08,81.23,-0.01,0,False,False
20260731,85.83,0.27,82.49,0.3,81.6,0.37,1,True,True
20260807,85.88,0.05,82.49,0,81.53,-0.07,2,False,False
20260814,85.86,-0.02,82.57,0.08,81.54,0.01,3,False,True
20260821,85.92,0.06,82.73,0.16,81.74,0.2,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2897 | 王道銀行 | pattern | 型態觀察 | 54.0 |  |  | base_building |  |  | stale_signal | 1.提報董事會或經董事會決議日期:115/08/19 2.審計委員會通過日期:115/08/18 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止利息淨收益(仟元):1,695,791 5.1月1日累計至本期止淨收益(仟元):6,454,412 6.1月1日累計至本期止稅前淨利(損) (仟元):3,237,113 7.1月1日累計至本期止本期淨利(淨損) (仟元):2,669,326 8.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):1,625,874 9.1月1日累計至本期止基本每股盈餘(損失) (元):0.54 10.期末總資產(仟元):738,762,815 11.期末總負債(仟元):672,870,014 12.期末歸屬於母公司業主之權益(仟元):45,240,014 13.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2897 | 王道銀行 | 2 | 2 | 2 | 5 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
