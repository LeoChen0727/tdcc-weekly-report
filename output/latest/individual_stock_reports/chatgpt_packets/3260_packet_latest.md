# INDIVIDUAL STOCK CHATGPT PACKET - 3260 威剛

## Metadata
- generated_at: 2026-09-05 22:16:28 Asia/Taipei
- stock_id: 3260
- stock_name: 威剛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3260_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3260_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3260_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3260_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3260.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3260.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3260.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3260.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3260_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3260_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3260_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
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
- decision_score_high
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
- date: 20260904
- open: 401
- high: 404.5
- low: 390.5
- close: 400.5
- volume: 4708000
- ma5: 406.7
- ema23_primary: 406.94
- distance_to_ema23_pct: -1.58
- ma20: 408.82
- ma60: 403.04
- ma120: 408.34
- return_5d: -2.79
- return_20d: -3.73
- volume_ratio: 0.49
- distance_to_ma20_pct_auxiliary: -2.04
- distance_to_high_60_pct: -12.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,421,424,411,411,11365000,398.09,3.24,390.6,406.46,0.91
20260811,409.5,409.5,400.5,405.5,7404000,398.71,1.7,390.73,406.13,0.59
20260812,408.5,422,408.5,409.5,11906000,399.61,2.48,390.8,405.99,0.95
20260813,416,419,409,409,7790000,400.39,2.15,391.23,406.31,0.61
20260814,415.5,419,400,402,10163000,400.52,0.37,393,406.25,0.8
20260817,404,404,397,400,4773000,400.48,-0.12,395.57,406.03,0.38
20260818,404,406,386,387,9164000,399.36,-3.09,396.5,405.52,0.72
20260819,377.5,395,375,395,6156000,398.99,-1,397.27,405.32,0.48
20260820,396,404,391,401,6363000,399.16,0.46,398.4,405.17,0.5
20260821,400.5,422.5,399,422.5,20651000,401.11,5.33,400.38,405.33,1.55
20260824,425.5,459.5,421.5,438.5,31204000,404.22,8.48,402.2,405.9,2.14
20260825,437.5,437.5,407,418.5,16790000,405.41,3.23,404.68,405.96,1.13
20260826,421,422,411,416,7952000,406.29,2.39,405.77,405.77,0.58
20260827,416,422,414,415.5,5637000,407.06,2.07,407.62,404.88,0.43
20260828,418,418.5,407,412,6697000,407.47,1.11,408.3,404.04,0.55
20260831,408.5,416.5,407,413.5,4594000,407.98,1.35,409.4,403.3,0.39
20260901,416.5,417.5,410.5,412,3920000,408.31,0.9,410.07,403.14,0.35
20260902,411,415.5,409,412.5,3520000,408.66,0.94,410.9,403.3,0.32
20260903,417,419.5,394,395,9994000,407.52,-3.07,409.6,402.87,0.97
20260904,401,404.5,390.5,400.5,4708000,406.94,-1.58,408.82,403.04,0.49
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 35.18
- over_600_ratio: 32.28
- over_800_ratio: 30.44
- over_1000_ratio: 28.56
- over_400_change_1w: -1.68
- over_800_change_1w: -2
- over_1000_change_1w: -1.69
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,32.63,0.12,28.49,0.36,26.31,-0.18,1,False,True
20260626,30.83,-1.8,26.6,-1.89,25.24,-1.07,0,False,False
20260703,29.03,-1.8,25.82,-0.78,23.97,-1.27,0,False,False
20260709,29.84,0.81,26.63,0.81,25.01,1.04,1,True,True
20260717,30.09,0.25,26.29,-0.34,25.19,0.18,2,False,True
20260724,30.52,0.43,26.14,-0.15,25.08,-0.11,3,False,False
20260731,30.41,-0.11,26.23,0.09,24.06,-1.02,4,False,True
20260807,32.66,2.25,28.96,2.73,27.61,3.55,5,True,True
20260814,33.4,0.74,30.37,1.41,27.96,0.35,6,True,True
20260821,32.84,-0.56,29.14,-1.23,28.08,0.12,7,False,True
20260828,36.86,4.02,32.44,3.3,30.25,2.17,8,True,True
20260904,35.18,-1.68,30.44,-2,28.56,-1.69,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3260 | 威剛 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  |  | stale_signal | 1.事實發生日: 115年7月8日 2.發生緣由: 威剛科技股份有限公司公開收購琉園股份有限公司（以下簡稱琉園） 普通股，截至民國115年7月8日止下午3點30分止累積應賣股數總計 為10,133,986股，已達最低收購數量10,000,000股，本次公開收 購條件已成就，爰依公開收購公開發行公司有價證券管理辦法第19條 第2項第2款規定公告。 3.因應措施:如有任何問題，請洽本次公開收購委任機構福邦證券 股份有限公司，應賣諮詢專線：02-2383-6888 4.其他金融監督管理委員會證券期貨局規定事項: (1)依公開收購公開發行公司有價證券管理辦法第19條第6項 規定，應賣人於公開收購人為本公告後，除法律另有規定外， 不得撤銷其應賣。 (2)本次公開收購之條件已成就，應賣股數如無因假扣押、假處分 等保全程序或強制執行程序，或出現其他轉讓之限制，使已應賣 股份視為自始未提出應賣，且無其他經主管機關核准後得停止公 開收購之情事，本次公開收購將於公開收購期間屆滿日(如經延長 則為延長期間屆滿日)次日起算五個營業日(含第五個營業日)以內 辦理應賣有價證券交割及收購對價支付事宜。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 3260 | 威剛 | revenue_breakout_low_response | 營收爆發低反應股 | 23 | 1 | A_優先追蹤 |  |  |  | stale_signal | 1.事實發生日: 115年7月8日 2.發生緣由: 威剛科技股份有限公司公開收購琉園股份有限公司（以下簡稱琉園） 普通股，截至民國115年7月8日止下午3點30分止累積應賣股數總計 為10,133,986股，已達最低收購數量10,000,000股，本次公開收 購條件已成就，爰依公開收購公開發行公司有價證券管理辦法第19條 第2項第2款規定公告。 3.因應措施:如有任何問題，請洽本次公開收購委任機構福邦證券 股份有限公司，應賣諮詢專線：02-2383-6888 4.其他金融監督管理委員會證券期貨局規定事項: (1)依公開收購公開發行公司有價證券管理辦法第19條第6項 規定，應賣人於公開收購人為本公告後，除法律另有規定外， 不得撤銷其應賣。 (2)本次公開收購之條件已成就，應賣股數如無因假扣押、假處分 等保全程序或強制執行程序，或出現其他轉讓之限制，使已應賣 股份視為自始未提出應賣，且無其他經主管機關核准後得停止公 開收購之情事，本次公開收購將於公開收購期間屆滿日(如經延長 則為延長期間屆滿日)次日起算五個營業日(含第五個營業日)以內 辦理應賣有價證券交割及收購對價支付事宜。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3260 | 威剛 | 15 | 15 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
