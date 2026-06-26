# INDIVIDUAL STOCK CHATGPT PACKET - 8104 錸寶

## Metadata
- generated_at: 2026-06-25 22:24:55 Asia/Taipei
- stock_id: 8104
- stock_name: 錸寶
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 290
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8104_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8104_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8104_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8104_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8104_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8104_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8104_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8104_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8104_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8104_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8104_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8104_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8104.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8104.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8104.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8104.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8104_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8104_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8104_latest.md?ref=main

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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260624
- open: 39.3
- high: 40.55
- low: 39.3
- close: 40.1
- volume: 1333972
- ma5: 41.44
- ema23_primary: 39.61
- distance_to_ema23_pct: 1.24
- ma20: 40.73
- ma60: 36.55
- ma120: 35.81
- return_5d: 3.75
- return_20d: 14.74
- volume_ratio: 0.24
- distance_to_ma20_pct_auxiliary: -1.53
- distance_to_high_60_pct: -16.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,35.3,38.25,34.35,37.25,3914622,34.83,6.93,34.51,34.56,3.69
20260528,40.95,40.95,40.6,40.95,5254180,35.34,15.86,34.87,34.61,4.09
20260529,43.3,43.5,40.95,41.15,15570788,35.83,14.85,35.27,34.68,7.71
20260601,41.25,43,40.05,41.5,7200896,36.3,14.32,35.63,34.81,3.08
20260602,40.65,41.15,39,40.55,2984609,36.65,10.63,35.91,34.91,1.23
20260603,40.45,44.6,39.6,44.6,11336115,37.32,19.52,36.41,35.06,3.83
20260604,46.1,47.8,42.75,42.75,17657002,37.77,13.19,36.82,35.21,4.64
20260605,43.8,45.3,41.8,43.1,7896415,38.21,12.79,37.28,35.36,1.9
20260608,38.8,40.6,38.8,40.25,2666923,38.38,4.86,37.56,35.45,0.63
20260609,40.25,41.6,38.8,41.25,3452331,38.62,6.8,37.9,35.56,0.79
20260610,40.3,42.6,38.85,39.25,2707439,38.67,1.49,38.17,35.63,0.61
20260611,39.25,39.85,38,38.6,1229885,38.67,-0.18,38.36,35.71,0.28
20260612,39.5,40,38.55,38.55,1353900,38.66,-0.28,38.59,35.78,0.3
20260615,39.5,39.7,38.7,38.9,940236,38.68,0.57,38.83,35.85,0.21
20260616,39.5,40.15,37.5,38.65,2249181,38.68,-0.07,39.08,35.93,0.49
20260617,38.7,42.35,38.7,42.35,4458690,38.98,8.64,39.52,36.05,0.94
20260618,42.5,43.15,41.4,42.35,7310968,39.26,7.86,39.91,36.2,1.44
20260622,42.7,44.2,42.2,42.3,9007312,39.52,7.04,40.26,36.36,1.64
20260623,42.3,42.5,40.05,40.1,2603091,39.56,1.35,40.47,36.45,0.47
20260624,39.3,40.55,39.3,40.1,1333972,39.61,1.24,40.73,36.55,0.24
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 38.44
- over_600_ratio: 34.96
- over_800_ratio: 33.03
- over_1000_ratio: 32.14
- over_400_change_1w: 0.56
- over_800_change_1w: -0.29
- over_1000_change_1w: -0.29
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.04,,36.57,,34.8,,0,False,False
20260508,38.95,-0.09,36.51,-0.06,34.8,0,1,False,False
20260515,38.51,-0.44,35.69,-0.82,34.8,0,0,False,False
20260522,38.52,0.01,35.69,0,34.8,0,1,False,False
20260529,41.54,3.02,37.98,2.29,36.13,1.33,2,True,True
20260605,37.58,-3.96,34.18,-3.8,32.43,-3.7,0,False,False
20260612,37.88,0.3,33.32,-0.86,32.43,0,1,False,False
20260618,38.44,0.56,33.03,-0.29,32.14,-0.29,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 8104 | 錸寶 | pattern | 型態觀察 | 48.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.發生變動日期:115/06/17 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:法人董事 3.舊任者職稱及姓名:董事 錸寶科技股份有限公司代表人：楊慰芬 4.舊任者簡歷:錸寶科技股份有限公司代表人：楊慰芬，鈺德科技股份有限公司董事長 5.新任者職稱及姓名:董事 錸寶科技股份有限公司代表人：楊慰芬 6.新任者簡歷:錸寶科技股份有限公司代表人：楊慰芬，鈺德科技股份有限公司董事長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:全面改選 9.新任者選任時持股數:75,000,000股 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/03/02~115/03/01 11.新任生效日期:115/06/17 12.同任期董事變動比率:任期屆滿全面改選，不適用 13.同任期獨立董事變動比率:不適用 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 8104 | 錸寶 | 4 | 4 | 4 | 6 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
