# INDIVIDUAL STOCK CHATGPT PACKET - 2467 志聖

## Metadata
- generated_at: 2026-09-06 22:16:26 Asia/Taipei
- stock_id: 2467
- stock_name: 志聖
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2467_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2467_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2467_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2467_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2467_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2467_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2467_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2467_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2467_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2467_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2467_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2467_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2467.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2467.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2467.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2467.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2467_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2467_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2467_latest.md?ref=main

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
- date: 20260904
- open: 620
- high: 622
- low: 570
- close: 603
- volume: 1244842
- ma5: 608.8
- ema23_primary: 572.31
- distance_to_ema23_pct: 5.36
- ma20: 570.65
- ma60: 562.77
- ma120: 546.03
- return_5d: -1.15
- return_20d: 20.6
- volume_ratio: 0.88
- distance_to_ma20_pct_auxiliary: 5.67
- distance_to_high_60_pct: -10.27

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,521,550,521,550,1532465,529.22,3.93,523.15,572.57,0.89
20260811,549,549,529,532,1100899,529.45,0.48,522.95,571.65,0.66
20260812,535,568,535,552,1692423,531.33,3.89,521.1,570.95,1.04
20260813,565,572,546,548,1524156,532.72,2.87,517.5,570.48,1.03
20260814,552,558,532,535,981740,532.91,0.39,516.35,570.17,0.69
20260817,552,588,539,588,2156722,537.5,9.39,519.65,570.22,1.51
20260818,599,616,557,564,2558610,539.71,4.5,521.35,569.57,1.73
20260819,552,566,538,547,1357774,540.32,1.24,521.4,567.63,0.91
20260820,552,572,552,560,1357324,541.96,3.33,522.5,565.83,0.9
20260821,559,568,552,560,837313,543.46,3.04,524.75,564.22,0.55
20260824,554,579,533,533,931944,542.59,-1.77,524.8,562.82,0.63
20260825,526,535,505,535,667454,541.96,-1.28,526.15,561.42,0.48
20260826,540,575,534,570,1132206,544.29,4.72,531.6,560.3,0.83
20260827,575,592,561,585,1562230,547.69,6.81,538.7,560.25,1.17
20260828,600,624,588,610,2420640,552.88,10.33,545.27,560.17,1.76
20260831,595,616,570,613,1360430,557.89,9.88,551.05,559.95,1.02
20260901,620,643,617,624,1718207,563.4,10.76,557.1,560.68,1.25
20260902,617,630,608,609,953685,567.2,7.37,561.7,561.37,0.69
20260903,622,622,594,595,1093999,569.52,4.47,565.5,561.72,0.79
20260904,620,622,570,603,1244842,572.31,5.36,570.65,562.77,0.88
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 69.94
- over_600_ratio: 67.66
- over_800_ratio: 63.42
- over_1000_ratio: 59.48
- over_400_change_1w: 0.24
- over_800_change_1w: 0.81
- over_1000_change_1w: -0.25
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,68.36,0.1,61.06,0.86,58.43,2.49,2,True,True
20260626,67.92,-0.44,60.91,-0.15,58.06,-0.37,0,False,False
20260703,69.39,1.47,61.92,1.01,60.27,2.21,1,True,True
20260709,68.44,-0.95,61.57,-0.35,59.93,-0.34,0,False,False
20260717,68.76,0.32,61.84,0.27,60.18,0.25,1,True,True
20260724,68.48,-0.28,62.55,0.71,59.17,-1.01,2,False,True
20260731,68.06,-0.42,62.34,-0.21,57.93,-1.24,0,False,False
20260807,68.28,0.22,62.29,-0.05,60,2.07,1,False,True
20260814,68.9,0.62,62.67,0.38,60.4,0.4,2,True,True
20260821,69.57,0.67,62.98,0.31,59.67,-0.73,3,False,True
20260828,69.7,0.13,62.61,-0.37,59.73,0.06,4,False,True
20260904,69.94,0.24,63.42,0.81,59.48,-0.25,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2467 | 志聖 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_put_bullish | continued_2_3d | 符合條款第四條第XX款：12 事實發生日：115/08/12 1.召開法人說明會之日期：115/08/12 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：櫃買中心11樓多功能資訊媒體區 地址：台北市羅斯福路二段100號11樓 4.法人說明會擇要訊息：本公司受邀參加櫃檯買賣中心主辦之「櫃買市場業績發表會」，會中就本公司115年第2季之財務報告相關資訊暨營運概況進行說明。 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2467 | 志聖 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | call_put_bullish | continued_2_3d | 符合條款第四條第XX款：12 事實發生日：115/08/12 1.召開法人說明會之日期：115/08/12 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：櫃買中心11樓多功能資訊媒體區 地址：台北市羅斯福路二段100號11樓 4.法人說明會擇要訊息：本公司受邀參加櫃檯買賣中心主辦之「櫃買市場業績發表會」，會中就本公司115年第2季之財務報告相關資訊暨營運概況進行說明。 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2467 | 志聖 | revenue_breakout_low_response | 營收爆發低反應股 | 22 | 4 | A_優先追蹤 |  |  | call_put_bullish | continued_2_3d | 符合條款第四條第XX款：12 事實發生日：115/08/12 1.召開法人說明會之日期：115/08/12 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：櫃買中心11樓多功能資訊媒體區 地址：台北市羅斯福路二段100號11樓 4.法人說明會擇要訊息：本公司受邀參加櫃檯買賣中心主辦之「櫃買市場業績發表會」，會中就本公司115年第2季之財務報告相關資訊暨營運概況進行說明。 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2467 | 志聖 | 2 | 2 | 4 | 7 | 16 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2467 | 志聖 | 74 | 2 | 8293090.0 | 90350.0 | 91.79 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
