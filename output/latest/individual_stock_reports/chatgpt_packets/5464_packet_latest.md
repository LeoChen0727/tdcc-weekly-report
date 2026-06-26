# INDIVIDUAL STOCK CHATGPT PACKET - 5464 霖宏

## Metadata
- generated_at: 2026-06-25 22:24:05 Asia/Taipei
- stock_id: 5464
- stock_name: 霖宏
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 155
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5464_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5464.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5464.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5464_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_confirmed
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
- model_recommended
- decision_score_high
- price_structure_not_broken
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260624
- open: 98
- high: 98
- low: 94.9
- close: 98
- volume: 2766000
- ma5: 83.04
- ema23_primary: 72.81
- distance_to_ema23_pct: 34.6
- ma20: 74.47
- ma60: 52.89
- ma120: 39.6
- return_5d: 40
- return_20d: 35.73
- volume_ratio: 2.86
- distance_to_ma20_pct_auxiliary: 31.59
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,73.1,73.1,71.1,71.1,72000,56.57,25.68,56.46,37.98,0.04
20260528,70,78.2,69,75.5,77000,58.15,29.84,58.64,38.78,0.05
20260529,77,83,75.6,83,82000,60.22,37.83,61.14,39.7,0.05
20260601,88,91,74.9,80.5,82000,61.91,30.03,63.37,40.58,0.06
20260602,78.9,80,72.5,76.3,74,63.11,20.9,65.22,41.41,0
20260603,76.3,78.7,69.1,69.9,72000,63.67,9.78,66.54,42.12,0.06
20260604,69,69,63,65.8,65000,63.85,3.05,67.45,42.77,0.06
20260605,66.8,69.1,63.3,67.6,66000,64.16,5.36,68.21,43.45,0.1
20260608,61.5,65.5,61.3,63.8,890000,64.13,-0.52,68.52,44.06,1.57
20260609,65.4,70.1,64.1,70.1,897000,64.63,8.46,68.86,44.77,1.6
20260610,70.1,75,67.2,67.5,1506000,64.87,4.05,69.14,45.44,2.95
20260611,64.2,73.8,64.2,69.9,1301000,65.29,7.06,69.66,46.15,2.56
20260612,73,74.9,66.8,71.8,1939000,65.83,9.07,70.39,46.87,3.63
20260615,71.8,73.8,69.1,71.5,1810000,66.3,7.84,71.1,47.6,3.14
20260616,70.2,72.7,69.6,70,817000,66.61,5.09,71.47,48.29,1.42
20260617,69,75.4,68,73.4,1489000,67.18,9.26,71.77,49.05,2.46
20260618,74.4,75.1,73,73.7,871000,67.72,8.83,71.88,49.81,1.42
20260622,73,81,73,81,2723000,68.83,17.69,72.38,50.7,3.65
20260623,84.5,89.1,81.6,89.1,1803000,70.52,26.35,73.19,51.72,2.17
20260624,98,98,94.9,98,2766000,72.81,34.6,74.47,52.89,2.86
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 73.09
- over_600_ratio: 71.24
- over_800_ratio: 65.46
- over_1000_ratio: 57.66
- over_400_change_1w: 1.04
- over_800_change_1w: 0.5
- over_1000_change_1w: 0.5
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,62.27,,58.64,,52.07,,0,False,False
20260508,66.57,4.3,63.43,4.79,54.28,2.21,1,True,True
20260515,69.73,3.16,64.61,1.18,58.05,3.77,2,True,True
20260522,71.59,1.86,64.11,-0.5,56.24,-1.81,3,False,False
20260529,71.79,0.2,63.42,-0.69,55.61,-0.63,4,False,False
20260605,70.86,-0.93,64.32,0.9,56.52,0.91,5,False,True
20260612,72.05,1.19,64.96,0.64,57.16,0.64,6,True,True
20260618,73.09,1.04,65.46,0.5,57.66,0.5,7,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 5464 | 霖宏 | true_breakout | 嚴格突破 | 99.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.發生變動日期:115/06/16 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、 自然人董事或自然人監察人）:自然人董事、獨立董事 3.舊任者職稱及姓名: 董事-張枋霖 董事-張鵬展 董事-張哲明 獨立董事-林惠芬 獨立董事-申元洪 獨立董事-侯翰 獨立董事-陳麗玲 4.舊任者簡歷: 董事-張枋霖 霖宏科技股份有限公司董事長 董事-張鵬展 霖宏科技股份有限公司副董事長 董事-張哲明 霖宏科技股份有限公司副總經理 獨立董事-林惠芬 維揚聯合會計師事務所執業會計師 獨立董事-申元洪 世新大學專任助理教授 獨立董事-侯  翰 實踐大學金融學系專任教授兼系主任 獨立董事-陳麗玲 大同技術學院餐飲管理系專任助理教授 5.新任者職稱及姓名: 董事-張枋霖 董事-張鵬展 董事-張哲明 獨立董事-侯翰 獨立董事-陳麗玲 獨立董事-林怡君 獨立董事-陳怡旭 6.新任者簡歷: 董事-張枋霖 霖宏科技股份有限公司董事長 董事-張鵬展 霖宏科技股份有限公司副董事長 董事-張哲明 霖宏科技股份有限公司副總經理 獨立董事-侯  翰 實踐大學金融學系專任教授兼系主任 獨立董事-陳麗玲 全達會計師事務所執業會計師 獨立董事-林怡君 立隆電子工業(股)公司財務部經理 獨立董事-陳怡旭 帝頡顧問管理股份有限公司 法務 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿改選 9.新任者選任時持股數: 董事-張枋霖：9,178,112 董事-張鵬展：4,745,065 董事-張哲明：  951,237 獨立董事-侯翰：0 獨立董事-陳麗玲：0 獨立董事-林怡君：0 獨立董事-陳怡旭：0 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/21~115/06/20 11.新任生效日期:115/06/16 12.同任期董事變動比率:不適用(全面改選) 13.同任期獨立董事變動比率:不適用(全面改選) 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第6款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 5464 | 霖宏 | 3 | 1 | 3 | 3 | 4 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
