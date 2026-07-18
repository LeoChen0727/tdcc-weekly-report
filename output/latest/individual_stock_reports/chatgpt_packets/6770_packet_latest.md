# INDIVIDUAL STOCK CHATGPT PACKET - 6770 力積電

## Metadata
- generated_at: 2026-07-19 06:19:27 Asia/Taipei
- stock_id: 6770
- stock_name: 力積電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-494211df6cae54ae
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
- date: 20260717
- open: 72.4
- high: 73.4
- low: 68.9
- close: 68.9
- volume: 273270140
- ma5: 71.94
- ema23_primary: 73.2
- distance_to_ema23_pct: -5.88
- ma20: 75.36
- ma60: 68.89
- ma120: 65.56
- return_5d: -3.09
- return_20d: -1.85
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: -8.58
- distance_to_high_60_pct: -27.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,71.5,75.3,70.7,74.2,245700060,70.53,5.2,74.16,62.75,0.94
20260622,79.5,81.6,78.5,81.6,133236652,71.45,14.2,75.05,63.06,0.52
20260623,82.8,86.1,78.3,78.6,504938034,72.05,9.09,75.6,63.29,1.89
20260624,78,85.7,77.2,85.7,476043030,73.19,17.1,76.34,63.67,1.74
20260625,89.3,89.3,82.8,83.2,479667659,74.02,12.4,76.77,64.07,1.73
20260626,83.2,85.2,78.1,78.3,332913359,74.38,5.27,76.64,64.41,1.3
20260629,79.9,82.3,77.6,78.9,220163758,74.75,5.55,76.16,64.84,0.97
20260630,79.9,80.4,77.8,79.7,197058093,75.17,6.03,75.79,65.25,1
20260701,80.2,80.5,72.7,74.3,264774867,75.09,-1.06,75.21,65.6,1.29
20260702,70.4,75.8,70.3,74.7,155504558,75.06,-0.48,74.72,65.94,0.74
20260703,73.3,75.1,72.1,73.4,101737426,74.92,-2.03,74.33,66.21,0.48
20260706,74.2,77.4,72.5,72.6,153798168,74.73,-2.85,74.23,66.52,0.72
20260707,73,74.3,69.7,70.1,161281480,74.34,-5.71,74.36,66.76,0.75
20260708,70.8,71.5,67.1,71.2,139718171,74.08,-3.89,74.35,67.04,0.63
20260709,71.5,74.3,70.9,71.1,156986667,73.83,-3.7,74.69,67.31,0.71
20260713,72.4,73,68.1,69,117782988,73.43,-6.03,74.92,67.58,0.53
20260714,69,70.4,63.4,69.2,175281346,73.08,-5.31,75.02,67.83,0.76
20260715,74,76.1,73.8,76.1,197628288,73.33,3.78,75.16,68.22,0.84
20260716,74.9,79.5,74.8,76.5,446262954,73.59,3.95,75.43,68.64,1.84
20260717,72.4,73.4,68.9,68.9,273270140,73.2,-5.88,75.36,68.89,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 49.26
- over_600_ratio: 47.41
- over_800_ratio: 46.19
- over_1000_ratio: 45.42
- over_400_change_1w: 1.4
- over_800_change_1w: 1.43
- over_1000_change_1w: 1.48
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.83,,40.6,,39.73,,0,False,False
20260508,47.1,3.27,43.89,3.29,43.09,3.36,1,True,True
20260515,43.68,-3.42,40.35,-3.54,39.48,-3.61,0,False,False
20260522,43.87,0.19,40.66,0.31,39.92,0.44,1,True,True
20260529,55.44,11.57,52.28,11.62,51.64,11.72,2,True,True
20260605,51.73,-3.71,48.5,-3.78,47.74,-3.9,0,False,False
20260612,48.46,-3.27,45.29,-3.21,44.57,-3.17,0,False,False
20260618,49.64,1.18,46.58,1.29,46.01,1.44,1,True,True
20260626,50.53,0.89,47.41,0.83,46.7,0.69,2,True,True
20260703,48.64,-1.89,45.56,-1.85,44.77,-1.93,0,False,False
20260709,47.86,-0.78,44.76,-0.8,43.94,-0.83,0,False,False
20260717,49.26,1.4,46.19,1.43,45.42,1.48,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6770 | 力積電 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | put_inflow | stale_signal | 1.事實發生日:115/07/15 2.公司名稱:力晶積成電子製造股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報 6.報導內容: 7月15日工商時報報導：「…，今年以來成熟製程代工價格持續調升，在供不應求下， 明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成。」 7.發生緣由: 針對媒體報導「明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成」， 力積電澄清說明如下：公司法說會僅就自身營業前景提出趨勢觀察，並未預測明年度 具體毛利率數字。至於媒體對我國整體成熟製程晶圓代工業明年毛利情況的概括性預 估，本公司不予置評。 8.因應措施:針對媒體報導內容發佈重大訊息澄清。 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 6770 | 力積電 | revenue_breakout_low_response | 營收爆發低反應股 | 12.0 | 33.0 | D_降級_TDCC轉弱 |  |  | put_inflow | stale_signal | 1.事實發生日:115/07/15 2.公司名稱:力晶積成電子製造股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報 6.報導內容: 7月15日工商時報報導：「…，今年以來成熟製程代工價格持續調升，在供不應求下， 明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成。」 7.發生緣由: 針對媒體報導「明年不僅力積電，台灣成熟製程晶圓代工廠毛利率都可望突破4成」， 力積電澄清說明如下：公司法說會僅就自身營業前景提出趨勢觀察，並未預測明年度 具體毛利率數字。至於媒體對我國整體成熟製程晶圓代工業明年毛利情況的概括性預 估，本公司不予置評。 8.因應措施:針對媒體報導內容發佈重大訊息澄清。 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6770 | 力積電 | 11 | 2 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6770 | 力積電 | 155 | 21 | 35715160.0 | 2579540.0 | 13.85 | put_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
