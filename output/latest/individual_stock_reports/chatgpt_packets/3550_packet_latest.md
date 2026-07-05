# INDIVIDUAL STOCK CHATGPT PACKET - 3550 聯穎

## Metadata
- generated_at: 2026-07-05 22:27:07 Asia/Taipei
- stock_id: 3550
- stock_name: 聯穎
- packet_status: standard_180d_window_packet
- latest_price_date: 20260703
- price_rows: 297
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3550_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3550_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3550.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3550.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3550.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3550.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3550_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3550_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3550_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 營收成長股價回檔 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- date: 20260703
- open: 36.4
- high: 37.65
- low: 33.2
- close: 33.4
- volume: 13944271
- ma5: 33.15
- ema23_primary: 30.51
- distance_to_ema23_pct: 9.49
- ma20: 31.33
- ma60: 24.25
- ma120: 20.73
- return_5d: 6.37
- return_20d: 39.46
- volume_ratio: 1.28
- distance_to_ma20_pct_auxiliary: 6.6
- distance_to_high_60_pct: -15.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260605,24.1,24.9,22.65,24.05,10952260,21.29,12.99,21.11,20.01,3.14
20260608,21.7,24.05,21.7,23.55,4841810,21.47,9.67,21.22,20.14,1.35
20260609,23.9,25.9,23.05,25.9,11675585,21.84,18.57,21.5,20.29,2.92
20260610,28.2,28.45,26.7,28.45,19668746,22.39,27.05,21.92,20.46,4
20260611,30,30.1,27,28.6,22256002,22.91,24.83,22.3,20.6,3.81
20260612,30.2,30.5,28.35,29.05,11919158,23.42,24.03,22.7,20.75,1.92
20260615,30.1,30.4,27.9,28.05,9298925,23.81,17.82,23.07,20.89,1.41
20260616,28,30.85,27.6,30.85,10939707,24.39,26.46,23.6,21.08,1.56
20260617,32.95,33.9,32.05,33.9,4661591,25.19,34.59,24.3,21.33,0.65
20260618,37.2,37.25,36.2,37.25,3088839,26.19,42.22,25.12,21.64,0.43
20260622,38.4,39.7,35.8,35.9,20071272,27,32.96,25.82,21.94,2.49
20260623,36.25,36.5,34.4,35,6297942,27.67,26.5,26.5,22.23,0.76
20260624,35.3,38.5,34.8,36,17339769,28.36,26.93,27.28,22.54,1.93
20260625,35.1,35.2,32.4,32.95,8769143,28.74,14.63,27.92,22.77,0.94
20260626,32.5,34.3,31.35,31.4,6328052,28.97,8.4,28.49,22.98,0.66
20260629,31.4,31.45,29.65,30.45,5600505,29.09,4.68,28.98,23.19,0.57
20260630,31.4,31.95,29.85,31.8,4587000,29.32,8.48,29.5,23.41,0.47
20260701,33.7,34.95,32,33.4,12561000,29.66,12.63,30.11,23.68,1.23
20260702,34.3,36.7,34.15,36.7,13042000,30.24,21.35,30.86,23.99,1.21
20260703,36.4,37.65,33.2,33.4,13944271,30.51,9.49,31.33,24.25,1.28
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 51.29
- over_600_ratio: 45.96
- over_800_ratio: 41.94
- over_1000_ratio: 38.56
- over_400_change_1w: 1.07
- over_800_change_1w: -1.87
- over_1000_change_1w: -1.75
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,44.1,,37.43,,35.01,,0,False,False
20260508,42.31,-1.79,37.3,-0.13,36.5,1.49,1,False,True
20260515,42.59,0.28,38.11,0.81,36.5,0,2,False,True
20260522,44.32,1.73,38.43,0.32,36.88,0.38,3,True,True
20260529,43.23,-1.09,37.44,-0.99,36.64,-0.24,0,False,False
20260605,48.27,5.04,41.11,3.67,38.45,1.81,1,True,True
20260612,50.55,2.28,46.47,5.36,43.06,4.61,2,True,True
20260618,53.97,3.42,48.84,2.37,44.56,1.5,3,True,True
20260626,50.22,-3.75,43.81,-5.03,40.31,-4.25,0,False,False
20260703,51.29,1.07,41.94,-1.87,38.56,-1.75,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 3550 | 聯穎 | revenue_pullback | 營收成長股價回檔 | 68.0 |  |  |  |  |  | repeated_but_no_breakout | 1.發生變動日期:115/06/16 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名: (1)獨立董事徐永珍先生 (2)獨立董事巫麗卿女士 (3)獨立董事黃詩易先生 4.舊任者簡歷: (1)獨立董事徐永珍先生：國立清華大學電機工程學系暨電子工程研究所教授 (2)獨立董事巫麗卿女士：本公司獨立董事 (3)獨立董事黃詩易先生：本公司獨立董事 5.新任者姓名:待董事會委任。 6.新任者簡歷:待董事會委任。 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿。 8.異動原因:配合115年股東常會全面改選董事及獨立董事。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/08/09-115/06/29 10.新任生效日期:尚未委任。 11.其他應敘明事項:新任薪資報酬委員將於董事會委任後另行公告。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 3550 | 聯穎 | 1 | 1 | 1 | 4 | 14 | repeated_but_no_breakout | 近 10 日上榜 4 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

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
