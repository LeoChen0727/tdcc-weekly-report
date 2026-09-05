# INDIVIDUAL STOCK CHATGPT PACKET - 6770 力積電

## Metadata
- generated_at: 2026-09-05 22:17:52 Asia/Taipei
- stock_id: 6770
- stock_name: 力積電
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6770_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6770_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6770_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6770_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6770_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6770_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6770_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6770_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6770_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6770_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6770_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6770_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6770.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6770.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6770.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6770.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6770_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6770_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6770_latest.md?ref=main

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
- date: 20260904
- open: 69.3
- high: 70
- low: 67
- close: 68.5
- volume: 85248242
- ma5: 70.1
- ema23_primary: 69.02
- distance_to_ema23_pct: -0.76
- ma20: 70.42
- ma60: 69.51
- ma120: 66.2
- return_5d: -2.14
- return_20d: 4.58
- volume_ratio: 0.42
- distance_to_ma20_pct_auxiliary: -2.72
- distance_to_high_60_pct: -23.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,66.6,69.4,66.6,67.6,231526872,64.3,5.13,63.35,69.88,1.17
20260811,66.4,67.5,65.3,67,110831134,64.53,3.83,63.24,69.95,0.57
20260812,68,73.7,67.9,73.7,428615022,65.29,12.88,63.12,70.15,2.08
20260813,75,77.4,72.7,74.9,471309109,66.09,13.32,63.04,70.42,2.27
20260814,76.6,81.8,76.3,78.4,527933484,67.12,16.81,63.52,70.76,2.4
20260817,79.9,79.9,74.2,74.6,259955163,67.74,10.12,64.1,71.02,1.16
20260818,75,75.7,69.5,69.7,226495303,67.91,2.64,64.33,71.12,0.99
20260819,67.3,69.6,66.5,66.6,176388814,67.8,-1.76,64.26,71.1,0.77
20260820,68.1,69.5,66.2,67.3,165662077,67.76,-0.67,64.33,71.04,0.71
20260821,67,68.5,66.5,68.4,116273055,67.81,0.87,64.67,70.94,0.5
20260824,68.4,72.9,67.6,70.8,162099266,68.06,4.03,65.11,70.77,0.7
20260825,70.5,71,66.6,69,158026446,68.14,1.27,65.77,70.44,0.67
20260826,69.8,71.4,69.2,70.2,109500620,68.31,2.77,66.76,70.16,0.47
20260827,71.3,72.1,69.6,69.6,118625661,68.42,1.73,67.77,69.89,0.52
20260828,70.8,73.3,69.9,70,127516696,68.55,2.12,68.54,69.65,0.54
20260831,69,73.2,68,73,207576800,68.92,5.92,69.45,69.52,0.89
20260901,73.6,73.7,70.4,70.8,151879084,69.08,2.5,69.99,69.45,0.65
20260902,70.1,71.4,69.2,70.4,68830476,69.19,1.75,70.2,69.5,0.31
20260903,71.2,72,67.5,67.8,115197089,69.07,-1.84,70.27,69.44,0.55
20260904,69.3,70,67,68.5,85248242,69.02,-0.76,70.42,69.51,0.42
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 45.09
- over_600_ratio: 42.98
- over_800_ratio: 41.68
- over_1000_ratio: 40.7
- over_400_change_1w: -0.86
- over_800_change_1w: -0.88
- over_1000_change_1w: -0.87
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,49.64,1.18,46.58,1.29,46.01,1.44,1,True,True
20260626,50.53,0.89,47.41,0.83,46.7,0.69,2,True,True
20260703,48.64,-1.89,45.56,-1.85,44.77,-1.93,0,False,False
20260709,47.86,-0.78,44.76,-0.8,43.94,-0.83,0,False,False
20260717,49.26,1.4,46.19,1.43,45.42,1.48,1,True,True
20260724,45.58,-3.68,42.35,-3.84,41.47,-3.95,0,False,False
20260731,43.51,-2.07,40.04,-2.31,39.14,-2.33,0,False,False
20260807,43.71,0.2,40.25,0.21,39.45,0.31,1,True,True
20260814,46.68,2.97,43.38,3.13,42.42,2.97,2,True,True
20260821,45.83,-0.85,42.46,-0.92,41.51,-0.91,0,False,False
20260828,45.95,0.12,42.56,0.1,41.57,0.06,1,True,True
20260904,45.09,-0.86,41.68,-0.88,40.7,-0.87,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6770 | 力積電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/07/15 2.公司名稱:力晶積成電子製造股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報 6.報導內容: 7月15日工商時報報導：「…，今年以來成熟製程代工價格持續調升，在供不應求下， 明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成。」 7.發生緣由: 針對媒體報導「明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成」， 力積電澄清說明如下：公司法說會僅就自身營業前景提出趨勢觀察，並未預測明年度 具體毛利率數字。至於媒體對我國整體成熟製程晶圓代工業明年毛利情況的概括性預 估，本公司不予置評。 8.因應措施:針對媒體報導內容發佈重大訊息澄清。 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 6770 | 力積電 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 16 | A_優先追蹤 |  |  | no_signal | stale_signal | 1.事實發生日:115/07/15 2.公司名稱:力晶積成電子製造股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報 6.報導內容: 7月15日工商時報報導：「…，今年以來成熟製程代工價格持續調升，在供不應求下， 明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成。」 7.發生緣由: 針對媒體報導「明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成」， 力積電澄清說明如下：公司法說會僅就自身營業前景提出趨勢觀察，並未預測明年度 具體毛利率數字。至於媒體對我國整體成熟製程晶圓代工業明年毛利情況的概括性預 估，本公司不予置評。 8.因應措施:針對媒體報導內容發佈重大訊息澄清。 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6770 | 力積電 | 24 | 4 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6770 | 力積電 | 273 | 33 | 15545940.0 | 1456560.0 | 10.67 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
