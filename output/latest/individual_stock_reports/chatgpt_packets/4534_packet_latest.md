# INDIVIDUAL STOCK CHATGPT PACKET - 4534 慶騰

## Metadata
- generated_at: 2026-07-16 22:27:35 Asia/Taipei
- stock_id: 4534
- stock_name: 慶騰
- packet_status: standard_180d_window_packet
- latest_price_date: 20260716
- price_rows: 170
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4534_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4534_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4534_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4534_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4534_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4534_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4534_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4534_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4534_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4534_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4534_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4534_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4534.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4534.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4534.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4534.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4534_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4534_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4534_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
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
- model_recommended
- decision_score_high
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
- date: 20260716
- open: 38.6
- high: 42.35
- low: 37.75
- close: 42.35
- volume: 4380000
- ma5: 36.87
- ema23_primary: 33.69
- distance_to_ema23_pct: 25.7
- ma20: 33.57
- ma60: 28.81
- ma120: 26.77
- return_5d: 28.72
- return_20d: 31.11
- volume_ratio: 2.31
- distance_to_ma20_pct_auxiliary: 26.14
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260617,32,33.8,32,33.65,1401000,29.75,13.1,29.5,26.29,0.78
20260618,33.1,34.1,32.95,33.65,1113000,30.08,11.88,30.09,26.38,0.61
20260622,34.3,35.9,33.6,33.8,3047000,30.39,11.23,30.56,26.51,1.53
20260623,34,34,31.4,32.4,1578000,30.55,6.04,30.85,26.61,0.76
20260624,31.65,32.65,31.3,31.85,900000,30.66,3.87,31.11,26.72,0.43
20260625,32.1,32.1,31,31.1,774000,30.7,1.31,31.38,26.82,0.36
20260626,31,31,28.1,29.7,1480000,30.62,-2.99,31.58,26.9,0.67
20260629,29.65,30.35,29.1,29.35,603000,30.51,-3.8,31.64,27,0.27
20260630,29.45,30.9,29.45,30.3,636000,30.49,-0.63,31.78,27.12,0.28
20260701,30.8,31.6,30,31,679000,30.54,1.52,31.98,27.25,0.29
20260702,30.15,34.1,30,34.1,3332000,30.83,10.6,32.25,27.44,1.35
20260703,33.45,35,32,34.3,2419000,31.12,10.21,32.38,27.62,0.93
20260706,34.3,37.7,34.3,36.1,3825000,31.54,14.47,32.53,27.82,1.37
20260707,36.1,36.3,32.8,32.9,2155000,31.65,3.95,32.58,27.92,0.79
20260708,32.9,33.55,32.15,32.9,884000,31.75,3.61,32.48,27.98,0.35
20260709,32.9,33.9,32.55,33.6,465000,31.91,5.3,32.58,28.07,0.21
20260713,35.2,35.35,33.7,34.9,1464000,32.16,8.53,32.83,28.21,0.72
20260714,36,36,32.95,35,1501000,32.39,8.04,32.92,28.35,0.78
20260715,35.5,38.5,35,38.5,5302000,32.9,17.01,33.07,28.55,2.81
20260716,38.6,42.35,37.75,42.35,4380000,33.69,25.7,33.57,28.81,2.31
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 40.32
- over_600_ratio: 34.98
- over_800_ratio: 32.61
- over_1000_ratio: 29.64
- over_400_change_1w: 0.73
- over_800_change_1w: 1.28
- over_1000_change_1w: 0.28
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,32.99,,27.3,,26.35,,0,False,False
20260508,32.42,-0.57,27.3,0,26.35,0,0,False,False
20260515,32.42,0,27.3,0,26.35,0,0,False,False
20260522,32.42,0,27.3,0,26.35,0,0,False,False
20260529,33.18,0.76,27.3,0,26.35,0,1,False,False
20260605,37.71,4.53,28.65,1.35,27.7,1.35,2,True,True
20260612,38.55,0.84,29.73,1.08,27.76,0.06,3,True,True
20260618,39.43,0.88,31.16,1.43,29.19,1.43,4,True,True
20260626,39.59,0.16,31.33,0.17,29.36,0.17,5,True,True
20260703,40.32,0.73,32.61,1.28,29.64,0.28,6,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260716 | 4534 | 慶騰 | true_breakout | 嚴格突破 | 94.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.發生變動日期:115/06/23 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:楊政學先生、連俊華先生、林舜天先生 4.舊任者簡歷: 楊政學先生/本公司獨立董事、明新科技大學企業管理系副教授。 連俊華先生/本公司獨立董事、尼得科超眾科技(股)公司獨立董事。 林舜天先生/本公司獨立董事、越峰電子材料股份有限公司獨立董事。 5.新任者姓名:連俊華先生、林舜天先生、蔡瑞哲先生 6.新任者簡歷: 連俊華先生/本公司獨立董事、尼得科超眾科技(股)公司獨立董事。 林舜天先生/本公司獨立董事、越峰電子材料股份有限公司獨立董事。 蔡瑞哲先生/本公司獨立董事、潤霈生技股份有限公司總經理兼研發長。 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，全面改選。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/15 ~ 115/06/14。 10.新任生效日期:115/06/23 ~ 118/06/22。 11.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260716 | 4534 | 慶騰 | 4 | 2 | 4 | 8 | 11 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
