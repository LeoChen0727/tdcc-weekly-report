# INDIVIDUAL STOCK CHATGPT PACKET - 2543 皇昌

## Metadata
- generated_at: 2026-07-30 22:27:07 Asia/Taipei
- stock_id: 2543
- stock_name: 皇昌
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2543_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2543_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2543.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2543.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2543.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2543.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2543_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2543_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2543_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260730
- open: 37
- high: 37
- low: 35.45
- close: 35.55
- volume: 1719660
- ma5: 37.68
- ema23_primary: 39.17
- distance_to_ema23_pct: -9.24
- ma20: 38.7
- ma60: 41.77
- ma120: 51.58
- return_5d: -8.96
- return_20d: -7.18
- volume_ratio: 1.39
- distance_to_ma20_pct_auxiliary: -8.13
- distance_to_high_60_pct: -30.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,38.8,38.95,38.1,38.3,966553,42.37,-9.61,43.72,46.07,0.38
20260703,38.1,39.4,38.1,39.2,850665,42.11,-6.91,43.37,45.74,0.34
20260706,40.2,40.35,39.15,39.45,801300,41.89,-5.82,42.88,45.44,0.36
20260707,39.35,39.8,38.3,38.5,837983,41.61,-7.46,42.43,45.12,0.42
20260708,38.5,38.8,38.15,38.7,440176,41.36,-6.44,41.92,44.81,0.24
20260709,38.85,39.15,38.45,38.8,860735,41.15,-5.71,41.41,44.49,0.53
20260713,39.65,40.75,39.45,39.75,1873125,41.03,-3.13,41.06,44.19,1.19
20260714,40.7,40.7,38.4,38.7,1494093,40.84,-5.24,40.65,43.88,0.96
20260715,38.55,39.65,38.55,39.55,788252,40.73,-2.9,40.29,43.58,0.52
20260716,39.85,40.25,39.1,39.75,866331,40.65,-2.21,39.93,43.32,0.58
20260717,39.5,40.6,38.2,38.25,2345321,40.45,-5.44,39.52,43.08,1.51
20260720,38.7,39.3,37.75,38.5,1321648,40.29,-4.44,39.24,42.87,0.89
20260721,38.65,41,38.65,40,1590952,40.26,-0.65,39.09,42.7,1.09
20260722,39.9,40.35,39,39,1053872,40.16,-2.88,38.95,42.55,0.74
20260723,39,39.25,38.75,39.05,613734,40.07,-2.53,38.95,42.43,0.53
20260724,39.05,39.8,38.55,38.6,675812,39.94,-3.36,38.9,42.3,0.61
20260727,40.1,40.8,38.35,39,1383554,39.86,-2.17,38.93,42.19,1.26
20260728,38.7,39.4,38.4,38.75,1324364,39.77,-2.57,38.94,42.06,1.18
20260729,38.85,39.5,35.9,36.5,2975037,39.5,-7.59,38.83,41.91,2.48
20260730,37,37,35.45,35.55,1719660,39.17,-9.24,38.7,41.77,1.39
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 71.28
- over_600_ratio: 70.03
- over_800_ratio: 67.68
- over_1000_ratio: 66.82
- over_400_change_1w: 0.15
- over_800_change_1w: 0.01
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,72.55,,69.08,,68.56,,0,False,False
20260508,72,-0.55,68.68,-0.4,68.19,-0.37,0,False,False
20260515,71.4,-0.6,67.65,-1.03,67.32,-0.87,0,False,False
20260522,70.96,-0.44,67.76,0.11,67.11,-0.21,1,False,True
20260529,70.59,-0.37,67.22,-0.54,66.38,-0.73,0,False,False
20260605,71.26,0.67,67.8,0.58,66.99,0.61,1,True,True
20260612,71.72,0.46,68.1,0.3,67.62,0.63,2,True,True
20260618,71.84,0.12,68.19,0.09,67.7,0.08,3,True,True
20260626,71.38,-0.46,67.87,-0.32,67.03,-0.67,0,False,False
20260703,71.16,-0.22,67.7,-0.17,66.86,-0.17,0,False,False
20260709,71.13,-0.03,67.67,-0.03,66.86,0,0,False,False
20260717,71.28,0.15,67.68,0.01,66.82,-0.04,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2543 | 皇昌 | revenue_pullback | 營收成長股價回檔 | 62.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  | no_signal | stale_signal | 1.原預定買回股份總金額上限(元):4,192,993,463 2.原預定買回之期間:115/05/19~115/07/18 3.原預定買回之數量(股):20,000,000 4.原預定買回區間價格(元):35.00~70.00 5.本次實際買回期間:115/05/21~115/06/16 6.本次已買回股份數量(股):14,235,000 7.本次已買回股份總金額(元):661,434,108 8.本次平均每股買回價格(元):46.47 9.累積已持有自己公司股份數量(股):14,235,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.69 11.本次未執行完畢之原因: 維護股東權益並兼顧市場機制，視股價變化及成交量狀況分批買回， 故未能執行完畢 12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 2543 | 皇昌 | revenue_breakout_low_response | 營收爆發低反應股 | 11.0 | 37.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.原預定買回股份總金額上限(元):4,192,993,463 2.原預定買回之期間:115/05/19~115/07/18 3.原預定買回之數量(股):20,000,000 4.原預定買回區間價格(元):35.00~70.00 5.本次實際買回期間:115/05/21~115/06/16 6.本次已買回股份數量(股):14,235,000 7.本次已買回股份總金額(元):661,434,108 8.本次平均每股買回價格(元):46.47 9.累積已持有自己公司股份數量(股):14,235,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.69 11.本次未執行完畢之原因: 維護股東權益並兼顧市場機制，視股價變化及成交量狀況分批買回， 故未能執行完畢 12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2543 | 皇昌 | 1 | 1 | 3 | 3 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2543 | 皇昌 | 20 | 0 | 52830.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
