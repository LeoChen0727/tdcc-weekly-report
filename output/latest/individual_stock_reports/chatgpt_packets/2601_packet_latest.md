# INDIVIDUAL STOCK CHATGPT PACKET - 2601 益航

## Metadata
- generated_at: 2026-07-12 22:26:46 Asia/Taipei
- stock_id: 2601
- stock_name: 益航
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 300
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2601_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2601_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2601.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2601.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2601.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2601.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2601_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2601_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2601_latest.md?ref=main

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
- thesis_state: breakout_initial
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
- date: 20260709
- open: 7.8
- high: 8.28
- low: 7.8
- close: 7.98
- volume: 37809537
- ma5: 7
- ema23_primary: 6.09
- distance_to_ema23_pct: 30.93
- ma20: 5.96
- ma60: 5.53
- ma120: 5.68
- return_5d: 46.15
- return_20d: 36.88
- volume_ratio: 5.83
- distance_to_ma20_pct_auxiliary: 34.01
- distance_to_high_60_pct: -3.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,5.89,5.89,5.55,5.71,1529516,5.57,2.47,5.45,5.53,0.39
20260612,5.68,5.84,5.68,5.75,1794253,5.59,2.91,5.5,5.52,0.46
20260615,5.84,5.98,5.81,5.85,1370196,5.61,4.3,5.55,5.51,0.35
20260616,5.85,5.85,5.7,5.72,1466782,5.62,1.81,5.59,5.51,0.38
20260617,5.81,6.05,5.55,5.9,2768978,5.64,4.58,5.64,5.5,0.72
20260618,5.97,5.98,5.8,5.81,1743215,5.66,2.73,5.68,5.5,0.46
20260622,6,6,5.6,5.68,2764903,5.66,0.39,5.71,5.49,0.72
20260623,5.68,5.68,5.5,5.57,2281554,5.65,-1.42,5.73,5.49,0.6
20260624,5.55,5.61,5.46,5.54,1255085,5.64,-1.8,5.76,5.48,0.33
20260625,5.54,5.6,5.49,5.49,1722052,5.63,-2.46,5.78,5.47,0.46
20260626,5.38,5.56,5.35,5.35,2115168,5.61,-4.56,5.8,5.45,0.57
20260629,5.35,5.45,5.35,5.39,1120456,5.59,-3.53,5.8,5.45,0.31
20260630,5.45,5.45,5.36,5.45,1571000,5.58,-2.26,5.79,5.44,0.47
20260701,5.45,5.49,5.37,5.43,1073000,5.56,-2.41,5.74,5.43,0.35
20260702,5.51,5.51,5.42,5.46,1253000,5.56,-1.71,5.7,5.42,0.55
20260703,5.46,6,5.46,6,5252076,5.59,7.29,5.69,5.43,2.39
20260706,6.6,6.6,6.6,6.6,5780000,5.68,16.27,5.71,5.44,2.61
20260707,6.95,7.2,6.7,6.87,28261967,5.78,18.95,5.76,5.46,8.19
20260708,7,7.55,6.95,7.55,26882744,5.92,27.46,5.85,5.49,5.73
20260709,7.8,8.28,7.8,7.98,37809537,6.09,30.93,5.96,5.53,5.83
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 32.46
- over_600_ratio: 29.68
- over_800_ratio: 28.81
- over_1000_ratio: 26.76
- over_400_change_1w: 0.11
- over_800_change_1w: 0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,31.86,,28.55,,26.32,,0,False,False
20260508,32.3,0.44,28.62,0.07,26.48,0.16,1,True,True
20260515,32.04,-0.26,28.46,-0.16,26.42,-0.06,0,False,False
20260522,32.09,0.05,28.42,-0.04,26.51,0.09,1,False,True
20260529,32.26,0.17,28.82,0.4,26.91,0.4,2,True,True
20260605,32.45,0.19,28.8,-0.02,26.77,-0.14,3,False,False
20260612,32.34,-0.11,28.71,-0.09,26.45,-0.32,0,False,False
20260618,32.4,0.06,28.67,-0.04,26.74,0.29,1,False,True
20260626,32.35,-0.05,28.75,0.08,26.7,-0.04,2,False,True
20260703,32.46,0.11,28.81,0.06,26.76,0.06,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2601 | 益航 | true_breakout | 嚴格突破 | 89.0 |  |  | platform_breakout |  |  | continued_overheated | 1.事實發生日:115/07/08 2.發生緣由:115/07/08 3.財務業務資訊: (1)單月                 最近一個月單月   與去年同期                    115年5月        增減%                         (IFRS自結數) 營業收入(百萬元)        137           5.81% 稅前淨利(百萬元)         6          -67.77% 歸屬於母公司淨利         8          167.26% (百萬元) 每股盈餘(元)            0.01        167.26% ----------------- ------------------- --------------- (2)單季                  最近一季單季    與去年同期                  115年第1季        增減%                         合併核閱數                     (IFRS會計師查核數) 營業收入(百萬元)        568         56.56% 稅前淨利(百萬元)         18        153.37% 歸屬於母公司淨利        -14         89.43% (百萬元) 每股盈餘(元)           -0.02        50.00% ----------------- ------------------- --------------- (3)最近四季累計                       最近四季累計                   (114年第2季至115年第1季)                         合併核閱數                      (IFRS會計師查核數) 營業收入(百萬元)         1,695 稅前淨利(百萬元)           -33 歸屬於母公司淨利        -1,227 (百萬元) 每股盈餘(元)             -0.06 ----------------- ------------------- --------------- 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2601 | 益航 | 5 | 2 | 5 | 7 | 13 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
