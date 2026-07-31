# INDIVIDUAL STOCK CHATGPT PACKET - 3324 雙鴻

## Metadata
- generated_at: 2026-07-31 22:27:10 Asia/Taipei
- stock_id: 3324
- stock_name: 雙鴻
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260724-88f3a903b384007d
- official_tdcc_signal_date: 20260724
- latest_tdcc_date: 20260724
- tdcc_rows: 13
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3324_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3324_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3324_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3324_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3324_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3324_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3324_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3324_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3324_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3324_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3324_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3324_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3324.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3324.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3324.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3324.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3324_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3324_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3324_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 834
- high: 872
- low: 810
- close: 820
- volume: 2046000
- ma5: 883.6
- ema23_primary: 926.59
- distance_to_ema23_pct: -11.5
- ma20: 919.9
- ma60: 1007.05
- ma120: 1018.37
- return_5d: -11.16
- return_20d: -18.81
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: -10.86
- distance_to_high_60_pct: -36.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,994,1040,977,1040,2247000,1041.39,-0.13,1048.9,1059.27,1.06
20260703,1020,1030,1010,1020,1320000,1039.61,-1.89,1040.65,1059.52,0.62
20260706,1035,1035,1005,1010,1070000,1037.14,-2.62,1035.65,1059.87,0.5
20260707,1005,1020,960,970,2087000,1031.54,-5.97,1029.4,1059.53,1.01
20260708,960,960,904,925,3301000,1022.67,-9.55,1020.15,1059.28,1.61
20260709,932,942,920,920,1385000,1014.11,-9.28,1015.65,1058.53,0.72
20260713,921,924,896,905,1088000,1005.02,-9.95,1011,1057.42,0.59
20260714,899,904,819,864,2239000,993.27,-13.01,1001.45,1054.4,1.22
20260715,872,905,872,896,1014000,985.16,-9.05,993.5,1052.08,0.56
20260716,905,922,885,902,1487000,978.23,-7.79,986.1,1049.78,0.82
20260717,879,930,869,913,3759000,972.79,-6.15,979.25,1047.5,1.94
20260720,913,918,831,858,2272000,963.23,-10.92,968.65,1042.55,1.15
20260721,873,930,870,926,1941000,960.13,-3.55,961.2,1039.57,0.98
20260722,937,948,907,908,1805000,955.78,-5,955.35,1034.45,0.92
20260723,928,959,922,923,3108000,953.05,-3.15,948.75,1030.17,1.55
20260724,916,990,906,943,4167000,952.21,-0.97,945.4,1026.8,1.97
20260727,943,943,890,930,1776000,950.36,-2.14,943.4,1022.97,0.85
20260728,878,893,867,870,1941000,943.67,-7.81,937.15,1018.47,0.92
20260729,864,894,816,855,3138000,936.28,-8.68,929.4,1012.88,1.46
20260730,834,872,810,820,2046000,926.59,-11.5,919.9,1007.05,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260724
- over_400_ratio: 44.08
- over_600_ratio: 38.36
- over_800_ratio: 34.71
- over_1000_ratio: 29.21
- over_400_change_1w: 0.95
- over_800_change_1w: 0.11
- over_1000_change_1w: 2.08
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260508,49.63,-2.03,39.21,-0.32,33.17,-2.36,0,False,False
20260515,48.85,-0.78,37.35,-1.86,31.27,-1.9,1,False,False
20260522,46.7,-2.15,36.36,-0.99,29.4,-1.87,0,False,False
20260529,46.26,-0.44,34.84,-1.52,27.82,-1.58,0,False,False
20260605,50.67,4.41,39.14,4.3,32.34,4.52,1,True,True
20260612,47.41,-3.26,37.9,-1.24,31,-1.34,0,False,False
20260618,46.82,-0.59,37.65,-0.25,31.83,0.83,1,False,True
20260626,45.51,-1.31,35.34,-2.31,28.65,-3.18,0,False,False
20260703,44.93,-0.58,35.13,-0.21,27.55,-1.1,0,False,False
20260709,43.7,-1.23,34.49,-0.64,27.02,-0.53,0,False,False
20260717,43.13,-0.57,34.6,0.11,27.13,0.11,1,False,True
20260724,44.08,0.95,34.71,0.11,29.21,2.08,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3324 | 雙鴻 | pullback_rebound | 回檔後短線轉強 | 63.0 |  |  |  |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/06/22 1.召開法人說明會之日期：115/06/22 ~ 115/06/23 2.召開法人說明會之時間：16 時 00 分  3.召開法人說明會之地點：英國倫敦維多利亞堤道 60 號 4.法人說明會擇要訊息：公告本公司受邀參加 JP Morgan Asia Pacific All Star Forum 5.其他應敘明事項：會議簡報等資料將依規定於期限前揭露於公開資訊觀測站。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 3324 | 雙鴻 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/06/22 1.召開法人說明會之日期：115/06/22 ~ 115/06/23 2.召開法人說明會之時間：16 時 00 分  3.召開法人說明會之地點：英國倫敦維多利亞堤道 60 號 4.法人說明會擇要訊息：公告本公司受邀參加 JP Morgan Asia Pacific All Star Forum 5.其他應敘明事項：會議簡報等資料將依規定於期限前揭露於公開資訊觀測站。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 3324 | 雙鴻 | revenue_breakout_low_response | 營收爆發低反應股 | 10.0 | 41.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/06/22 1.召開法人說明會之日期：115/06/22 ~ 115/06/23 2.召開法人說明會之時間：16 時 00 分  3.召開法人說明會之地點：英國倫敦維多利亞堤道 60 號 4.法人說明會擇要訊息：公告本公司受邀參加 JP Morgan Asia Pacific All Star Forum 5.其他應敘明事項：會議簡報等資料將依規定於期限前揭露於公開資訊觀測站。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3324 | 雙鴻 | 4 | 2 | 4 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
