# INDIVIDUAL STOCK CHATGPT PACKET - 4743 合一

## Metadata
- generated_at: 2026-08-22 22:27:56 Asia/Taipei
- stock_id: 4743
- stock_name: 合一
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4743_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4743_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4743_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4743_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4743_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4743_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4743_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4743_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4743_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4743_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4743_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4743_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4743.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4743.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4743.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4743.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4743_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4743_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4743_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
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
- open: 48.55
- high: 51.1
- low: 48.2
- close: 50
- volume: 3336000
- ma5: 47.99
- ema23_primary: 47.34
- distance_to_ema23_pct: 5.62
- ma20: 45.94
- ma60: 48.85
- ma120: 50.88
- return_5d: 7.53
- return_20d: 7.87
- volume_ratio: 1.8
- distance_to_ma20_pct_auxiliary: 8.83
- distance_to_high_60_pct: -20.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,46.55,46.8,45.9,46.25,1182000,49.75,-7.03,51.19,50.77,0.3
20260728,46,46.25,43.65,43.65,2754000,49.24,-11.35,50.84,50.61,0.69
20260729,44.25,44.9,41.1,42.25,3278000,48.66,-13.16,50.34,50.41,0.83
20260730,42,42.5,40.8,41.15,1939000,48.03,-14.32,49.81,50.15,0.5
20260731,42.85,42.85,41.6,41.75,1944000,47.51,-12.12,49.29,49.94,0.51
20260803,44.5,45.9,44,45.45,3428000,47.34,-3.98,48.7,49.82,0.99
20260804,44.2,47.65,44.2,47.45,2180000,47.34,0.22,48.09,49.75,0.8
20260805,45.9,46.95,45.7,45.75,2605000,47.21,-3.1,47.54,49.66,1.01
20260806,45.7,45.95,44.45,45.55,1433000,47.07,-3.24,47.03,49.56,0.6
20260807,45.05,46.5,45.05,45.6,1122000,46.95,-2.88,46.6,49.48,0.49
20260810,45.6,45.85,45.1,45.45,849000,46.83,-2.94,46.32,49.37,0.4
20260811,46.5,47.45,46.15,47.3,2097000,46.87,0.93,46.24,49.32,1.04
20260812,47.5,48.7,46.8,46.85,1401000,46.86,-0.03,46.05,49.26,0.7
20260813,47.3,47.95,46.65,47.95,1374000,46.95,2.12,45.93,49.23,0.68
20260814,47.95,48.1,46.25,46.5,1105000,46.92,-0.89,45.82,49.19,0.58
20260817,46.9,48.3,46.6,46.9,1049000,46.92,-0.03,45.78,49.07,0.56
20260818,46.8,47.7,46.7,47.4,755000,46.96,0.95,45.76,48.98,0.41
20260819,47,47.65,46.55,47.35,1014000,46.99,0.77,45.74,48.9,0.56
20260820,48.1,49.35,48.1,48.3,2265000,47.1,2.55,45.76,48.86,1.23
20260821,48.55,51.1,48.2,50,3336000,47.34,5.62,45.94,48.85,1.8
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 45.91
- over_600_ratio: 43.12
- over_800_ratio: 41.67
- over_1000_ratio: 41.3
- over_400_change_1w: -0.07
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.13
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,45.75,0.22,41.66,0.09,41.3,0.27,1,True,True
20260612,45.67,-0.08,41.65,-0.01,41.29,-0.01,0,False,False
20260618,45.79,0.12,41.43,-0.22,41.25,-0.04,1,False,False
20260626,45.97,0.18,41.68,0.25,41.3,0.05,2,True,True
20260703,46.16,0.19,42.12,0.44,41.74,0.44,3,True,True
20260709,46.91,0.75,42.96,0.84,42.58,0.84,4,True,True
20260717,46.26,-0.65,42.42,-0.54,42.04,-0.54,0,False,False
20260724,46.39,0.13,42.26,-0.16,42.08,0.04,1,False,True
20260731,45.68,-0.71,41.27,-0.99,40.89,-1.19,0,False,False
20260807,45.72,0.04,41.37,0.1,40.82,-0.07,1,False,True
20260814,45.98,0.26,41.82,0.45,41.43,0.61,2,True,True
20260821,45.91,-0.07,41.67,-0.15,41.3,-0.13,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4743 | 合一 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | continued_2_3d | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):76,528 5.1月1日累計至本期止營業毛利(毛損) (仟元):32,152 6.1月1日累計至本期止營業利益(損失) (仟元):(397,539) 7.1月1日累計至本期止稅前淨利(淨損) (仟元):109,138 8.1月1日累計至本期止本期淨利(淨損) (仟元):98,652 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):99,064 10.1月1日累計至本期止基本每股盈餘(損失) (元):0.21 11.期末總資產(仟元):11,266,282 12.期末總負債(仟元):872,671 13.期末歸屬於母公司業主之權益(仟元):10,248,576 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4743 | 合一 | 3 | 3 | 4 | 9 | 15 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
