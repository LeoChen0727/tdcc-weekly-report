# INDIVIDUAL STOCK CHATGPT PACKET - 3260 威剛

## Metadata
- generated_at: 2026-07-12 22:27:02 Asia/Taipei
- stock_id: 3260
- stock_name: 威剛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 166
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
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
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260709
- open: 408
- high: 418
- low: 405.5
- close: 410
- volume: 7745000
- ma5: 408
- ema23_primary: 411.09
- distance_to_ema23_pct: -0.26
- ma20: 410
- ma60: 418.29
- ma120: 377.74
- return_5d: 0.49
- return_20d: 5.13
- volume_ratio: 0.75
- distance_to_ma20_pct_auxiliary: 0
- distance_to_high_60_pct: -17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,388,399.5,378,394.5,13824000,419.84,-6.04,418.25,413.63,2.23
20260612,416,422,405.5,405.5,11982000,418.65,-3.14,417.27,413.15,2
20260615,414.5,435,413,423,16112000,419.01,0.95,417.52,412.24,2.59
20260616,430,434,417,417,13924000,418.84,-0.44,418.88,410.44,2.24
20260617,412,417,405.5,416,8232000,418.61,-0.62,419.4,409.75,1.4
20260618,420,425,412,423,12103000,418.97,0.96,419.9,409.93,2.07
20260622,434,443,427.5,434,15594000,420.22,3.28,420.73,410.73,2.36
20260623,436,436,410,412,13449000,419.54,-1.8,420.95,410.84,1.86
20260624,402,410,399,408.5,8268000,418.62,-2.42,420.88,411.47,1.08
20260625,421,423,407.5,409.5,9000000,417.86,-2,420.73,411.78,1.11
20260626,409.5,421,396,397.5,10709000,416.16,-4.48,420.38,412.24,1.25
20260629,399,406.5,394.5,404,5433000,415.15,-2.69,419.82,413.39,0.61
20260630,407.5,415,396,409,11091000,414.64,-1.36,418.93,414.07,1.18
20260701,411.5,412,392,398.5,14202000,413.29,-3.58,415.38,414.68,1.41
20260702,384,408,382.5,408,7750000,412.85,-1.17,412.68,415.43,0.74
20260703,404,411.5,403,411.5,5835000,412.74,-0.3,410.35,415.81,0.54
20260706,416,420,408,410.5,7015000,412.55,-0.5,409.8,416.55,0.64
20260707,417,418,404,404,8455000,411.84,-1.9,409.85,417.08,0.79
20260708,408,413,397,404,5808000,411.19,-1.75,409,417.73,0.55
20260709,408,418,405.5,410,7745000,411.09,-0.26,410,418.29,0.75
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 29.03
- over_600_ratio: 26.7
- over_800_ratio: 25.82
- over_1000_ratio: 23.97
- over_400_change_1w: -1.8
- over_800_change_1w: -0.78
- over_1000_change_1w: -1.27
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,41.44,,35.94,,33.78,,0,False,False
20260508,38.64,-2.8,34.19,-1.75,31.68,-2.1,0,False,False
20260515,36.47,-2.17,32.61,-1.58,31.51,-0.17,0,False,False
20260522,34.99,-1.48,31.22,-1.39,28.74,-2.77,0,False,False
20260529,32.95,-2.04,28.62,-2.6,26.41,-2.33,0,False,False
20260605,35.16,2.21,31.23,2.61,29.87,3.46,1,True,True
20260612,32.51,-2.65,28.13,-3.1,26.49,-3.38,0,False,False
20260618,32.63,0.12,28.49,0.36,26.31,-0.18,1,False,True
20260626,30.83,-1.8,26.6,-1.89,25.24,-1.07,0,False,False
20260703,29.03,-1.8,25.82,-0.78,23.97,-1.27,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3260 | 威剛 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.事實發生日: 115年7月8日  2.發生緣由:  威剛科技股份有限公司公開收購琉園股份有限公司（以下簡稱琉園） 普通股，截至民國115年7月8日止下午3點30分止累積應賣股數總計 為10,133,986股，已達最低收購數量10,000,000股，本次公開收 購條件已成就，爰依公開收購公開發行公司有價證券管理辦法第19條 第2項第2款規定公告。  3.因應措施:如有任何問題，請洽本次公開收購委任機構福邦證券 股份有限公司，應賣諮詢專線：02-2383-6888 4.其他金融監督管理委員會證券期貨局規定事項:  (1)依公開收購公開發行公司有價證券管理辦法第19條第6項  規定，應賣人於公開收購人為本公告後，除法律另有規定外，  不得撤銷其應賣。  (2)本次公開收購之條件已成就，應賣股數如無因假扣押、假處分  等保全程序或強制執行程序，或出現其他轉讓之限制，使已應賣  股份視為自始未提出應賣，且無其他經主管機關核准後得停止公  開收購之情事，本次公開收購將於公開收購期間屆滿日(如經延長  則為延長期間屆滿日)次日起算五個營業日(含第五個營業日)以內  辦理應賣有價證券交割及收購對價支付事宜。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 3260 | 威剛 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 18.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.事實發生日: 115年7月8日  2.發生緣由:  威剛科技股份有限公司公開收購琉園股份有限公司（以下簡稱琉園） 普通股，截至民國115年7月8日止下午3點30分止累積應賣股數總計 為10,133,986股，已達最低收購數量10,000,000股，本次公開收 購條件已成就，爰依公開收購公開發行公司有價證券管理辦法第19條 第2項第2款規定公告。  3.因應措施:如有任何問題，請洽本次公開收購委任機構福邦證券 股份有限公司，應賣諮詢專線：02-2383-6888 4.其他金融監督管理委員會證券期貨局規定事項:  (1)依公開收購公開發行公司有價證券管理辦法第19條第6項  規定，應賣人於公開收購人為本公告後，除法律另有規定外，  不得撤銷其應賣。  (2)本次公開收購之條件已成就，應賣股數如無因假扣押、假處分  等保全程序或強制執行程序，或出現其他轉讓之限制，使已應賣  股份視為自始未提出應賣，且無其他經主管機關核准後得停止公  開收購之情事，本次公開收購將於公開收購期間屆滿日(如經延長  則為延長期間屆滿日)次日起算五個營業日(含第五個營業日)以內  辦理應賣有價證券交割及收購對價支付事宜。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3260 | 威剛 | 14 | 13 | 5 | 10 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
