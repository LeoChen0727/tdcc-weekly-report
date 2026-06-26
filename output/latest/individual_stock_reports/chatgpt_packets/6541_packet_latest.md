# INDIVIDUAL STOCK CHATGPT PACKET - 6541 泰福-KY

## Metadata
- generated_at: 2026-06-26 22:24:20 Asia/Taipei
- stock_id: 6541
- stock_name: 泰福-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260626
- price_rows: 291
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6541_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6541_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6541_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6541_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6541_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6541_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6541_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6541_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6541_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6541_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6541_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6541_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6541.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6541.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6541.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6541.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6541_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6541_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6541_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260626
- open: 39.35
- high: 39.95
- low: 38.3
- close: 38.55
- volume: 1098517
- ma5: 42.13
- ema23_primary: 40.76
- distance_to_ema23_pct: -5.43
- ma20: 40.81
- ma60: 40.27
- ma120: 44.85
- return_5d: -4.7
- return_20d: 1.72
- volume_ratio: 2.08
- distance_to_ma20_pct_auxiliary: -5.53
- distance_to_high_60_pct: -15.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260528,37.9,38.35,37.3,37.4,391896,39.06,-4.24,38.95,40.87,0.96
20260529,37.9,39.4,37.9,39,512543,39.05,-0.13,38.92,40.72,1.21
20260601,39.55,41.4,39,41.4,919912,39.25,5.48,39.03,40.67,2.04
20260602,41.35,42.4,40.3,41.85,715798,39.46,6.04,39.13,40.62,1.51
20260603,41.9,42.7,41.15,41.3,544242,39.62,4.25,39.19,40.56,1.12
20260604,41.3,41.95,41.15,41.15,279624,39.75,3.53,39.25,40.54,0.58
20260605,41.1,42.3,40.5,41.9,361280,39.92,4.95,39.38,40.53,0.75
20260608,41.8,43,40.7,41.75,561937,40.08,4.17,39.47,40.49,1.17
20260609,41.5,42.95,41.05,41.25,437469,40.17,2.68,39.57,40.46,0.9
20260610,40.8,41,39.5,39.55,581437,40.12,-1.43,39.51,40.42,1.19
20260611,40,40,38.3,38.4,254273,39.98,-3.95,39.5,40.37,0.57
20260612,39,39.7,38.9,39.45,233195,39.94,-1.21,39.55,40.33,0.54
20260615,40.15,40.5,39.45,40.15,331660,39.95,0.49,39.62,40.27,0.78
20260616,40.15,40.75,39.6,40.5,263044,40,1.25,39.73,40.26,0.62
20260617,40.45,41.2,40.05,40.45,280033,40.04,1.03,39.86,40.23,0.66
20260618,40.85,41.35,40.4,40.45,337648,40.07,0.95,39.94,40.21,0.79
20260622,40.45,42.75,40.05,42.55,655088,40.28,5.64,40.13,40.22,1.47
20260623,42.55,44.55,42.35,43.85,885562,40.58,8.07,40.42,40.26,1.91
20260624,44,45.6,43.5,45.25,901816,40.96,10.46,40.77,40.32,1.82
20260626,39.35,39.95,38.3,38.55,1098517,40.76,-5.43,40.81,40.27,2.08
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 72.15
- over_600_ratio: 68.87
- over_800_ratio: 67.04
- over_1000_ratio: 65.72
- over_400_change_1w: -0.01
- over_800_change_1w: -0.01
- over_1000_change_1w: 0.35
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.55,,67.16,,65.88,,0,False,False
20260508,71.54,-0.01,67.13,-0.03,65.85,-0.03,0,False,False
20260515,71.69,0.15,67.08,-0.05,65.44,-0.41,1,False,False
20260522,71.9,0.21,67.06,-0.02,65.44,0,2,False,False
20260529,71.92,0.02,67.05,-0.01,65.38,-0.06,3,False,False
20260605,72.08,0.16,67.03,-0.02,65.38,0,4,False,False
20260612,72.16,0.08,67.05,0.02,65.37,-0.01,5,False,True
20260618,72.15,-0.01,67.04,-0.01,65.72,0.35,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260626 | 6541 | 泰福-KY | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | first_seen | 1.事實發生日:115/06/24 2.公司名稱:Tanvex BioPharma USA, Inc. 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:本公司持股100%子公司。 5.發生緣由:Tanvex BioPharma USA, Inc.(本公司之子公司，以下簡稱「Tanvex US」) 於美國時間2026年6月23日接獲美國食品藥物管理局(FDA)針對其生物製劑查驗登記申請 (BLA) TX05 (Herceptin之生物相似藥)所發出之完整回覆信函(Complete Response Letter, CRL)。 6.因應措施:無。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): (1) 研發新藥名稱或代號：重組蛋白生物相似藥TX05 (Herceptin Biosimilar)。 (2) 用途：與參考藥Herceptin相同，目前除了主要適應症為乳癌外，還包括胃癌。 (3) 預計進行之所有研發階段：不適用。 (4) 目前進行中之研發階段：     A. 提出申請/通過核准/不通過核准/各期人體試驗(含期中分析)結果/發生其他影        響新藥研發之重大事件：        除需由下游製造商改善之事項外，FDA於本次CRL中未就Tanvex US所製造之原料        藥(drug substance)提出任何問題。     B. 未通過目的事業主管機關許可、各期人體臨床試驗(含期中分析)結果未達統計        上顯著意義或發生其他影響新藥研發之重大事件者，公司所面臨之風險及因應        措施：Tanvex US目前正與下游製造廠商積極討論相關改善措施、預計將於7月              底前向FDA提交回覆。     C. 通過目的事業主管機關許可、各期人體臨床試驗(含期中分析)結果達統計上顯        著意義或發生其他影響新藥研發之重大事件者，未來經營方向：不適用。     D. 已投入之累積研發費用：基於TX05產品未來國際合作可能性或因涉及營業機密                              考量，為保障公司及投資人權益，故不予公開揭露。 (5) 將再進行之下一研發階段：Tanvex US將持續與下游製造商合作，以完成BLA審查                             程序。     A. 預計完成時間：視主管機關審查時間而定。     B. 預計應負擔之義務：不適用。 (6) 巿場現況：根據國際醫藥專業統計機構IQVIA之資料，截至2026年3月，Herceptin及               其他生物相似藥產品，過去一年之美國市場銷售額約為10億美元，目前               有多種乳癌治療方式，其中以生物藥品治療者，有Perjeta、Enhertu及               Kadcyla等品牌。 (7) 藥物開發具有開發時程長、投入經費高、需經目的事業主管機關審核、且並未保證     一定能成功，此等可能使投資面臨風險，投資人應審慎判斷謹慎投資。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260626 | 6541 | 泰福-KY | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
