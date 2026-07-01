# INDIVIDUAL STOCK CHATGPT PACKET - 3230 錦明

## Metadata
- generated_at: 2026-07-01 22:27:35 Asia/Taipei
- stock_id: 3230
- stock_name: 錦明
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 160
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3230_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3230_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3230.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3230.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3230.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3230.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3230_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3230_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3230_latest.md?ref=main

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
- action_summary_zh: 型態觀察 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_distribution_risk
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
- tdcc_distribution_warning
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260701
- open: 45.85
- high: 48
- low: 45.85
- close: 47.6
- volume: 1917000
- ma5: 42.79
- ema23_primary: 35.69
- distance_to_ema23_pct: 33.37
- ma20: 33.64
- ma60: 34.73
- ma120: 36.13
- return_5d: 27.61
- return_20d: 55.05
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: 41.51
- distance_to_high_60_pct: -0.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,31.25,31.55,30.2,30.85,31000,32.59,-5.35,31.89,36.81,0.1
20260604,30.85,31.05,30.4,30.75,31000,32.44,-5.21,31.73,36.64,0.11
20260605,31.3,31.5,30.35,30.55,31000,32.28,-5.37,31.55,36.48,0.12
20260608,28.5,30.25,27.9,29.9,421000,32.08,-6.81,31.41,36.33,1.8
20260609,30,30.5,29.5,29.8,199000,31.89,-6.56,31.26,36.17,0.9
20260610,29.95,30.65,29,29,285000,31.65,-8.38,31.09,36.02,1.29
20260611,29.15,29.65,28.4,28.9,250000,31.42,-8.03,30.97,35.82,1.24
20260612,29.3,29.4,28.45,28.8,219000,31.2,-7.7,30.9,35.62,1.23
20260615,28.85,29.3,28.85,29.1,208000,31.03,-6.22,30.72,35.4,1.31
20260616,29.4,29.55,28.75,28.75,445000,30.84,-6.77,30.49,35.18,3.05
20260617,28.7,29.85,28.2,29.4,331000,30.72,-4.29,30.35,35.01,2.27
20260618,29.85,30.15,29.1,29.9,338000,30.65,-2.45,30.22,34.84,2.25
20260622,31.55,32.85,30.95,31.35,3031000,30.71,2.09,30.17,34.68,10.09
20260623,34.45,34.45,31.5,34.45,6068000,31.02,11.05,30.27,34.58,10.08
20260624,33.9,37.3,33.2,37.3,5182000,31.54,18.25,30.56,34.52,6.03
20260625,37.5,38.5,35.45,36.25,2493000,31.94,13.51,30.85,34.42,2.54
20260626,36.6,39.85,36.5,39.85,4478000,32.6,22.26,31.32,34.4,3.72
20260629,43.4,43.8,41.5,43.8,4177000,33.53,30.63,32.01,34.47,2.96
20260630,46,46.45,42.35,46.45,10862000,34.61,34.22,32.79,34.58,5.56
20260701,45.85,48,45.85,47.6,1917000,35.69,33.37,33.64,34.73,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 53.04
- over_600_ratio: 50.94
- over_800_ratio: 50.22
- over_1000_ratio: 48.19
- over_400_change_1w: -3.6
- over_800_change_1w: -2.91
- over_1000_change_1w: -2.89
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.59,,54.65,,52.57,,0,False,False
20260508,57.46,-0.13,54.52,-0.13,52.44,-0.13,0,False,False
20260515,57.4,-0.06,54.46,-0.06,52.41,-0.03,0,False,False
20260522,57.18,-0.22,54.24,-0.22,52.19,-0.22,0,False,False
20260529,57.01,-0.17,53.67,-0.57,51.62,-0.57,0,False,False
20260605,57.01,0,53.36,-0.31,51.3,-0.32,1,False,False
20260612,56.91,-0.1,53.36,0,51.3,0,0,False,False
20260618,56.64,-0.27,53.13,-0.23,51.08,-0.22,0,False,False
20260626,53.04,-3.6,50.22,-2.91,48.19,-2.89,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3230 | 錦明 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  |  | continued_overheated | 1.董事會決議日期或發生變動日期:115/06/26 2.人員別（請輸入董事長或總經理）:董事長及副董事長 3.舊任者姓名: 蔡翔峰 簡豪廷 4.舊任者簡歷: 蔡翔峰 錦明實業股份有限公司董事長 簡豪廷 錦明實業股份有限公司副董事長 5.新任者姓名: 蔡翔峰 簡豪廷 6.新任者簡歷: 蔡翔峰 錦明實業股份有限公司董事長 簡豪廷 錦明實業股份有限公司副董事長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「職務調整」、「資遣」、 「退休」、「逝世」或「新任」）:任期屆滿 8.異動原因: 任期屆滿改選，股東常會全面改選董事，董事會推舉新任董事長及副董事長 9.新任生效日期:115/06/26 10.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第6款所定 對股東權益或證券價格有重大影響之事項):無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 3230 | 錦明 | 6 | 1 | 5 | 6 | 6 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
