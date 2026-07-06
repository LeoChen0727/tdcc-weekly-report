# INDIVIDUAL STOCK CHATGPT PACKET - 6174 安碁

## Metadata
- generated_at: 2026-07-06 22:27:46 Asia/Taipei
- stock_id: 6174
- stock_name: 安碁
- packet_status: standard_180d_window_packet
- latest_price_date: 20260706
- price_rows: 163
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6174_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6174_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6174.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6174.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6174.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6174.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6174_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6174_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6174_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
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
- date: 20260706
- open: 64.1
- high: 67
- low: 62
- close: 63
- volume: 12206000
- ma5: 57.04
- ema23_primary: 51.73
- distance_to_ema23_pct: 21.78
- ma20: 52.27
- ma60: 42.3
- ma120: 32.17
- return_5d: 29.1
- return_20d: 44.16
- volume_ratio: 2.11
- distance_to_ma20_pct_auxiliary: 20.52
- distance_to_high_60_pct: -5.97

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260608,39.35,45.95,39.35,44.5,2548000,42.37,5.02,43.66,32.55,1.41
20260609,45.1,48.95,43.8,48.95,5496000,42.92,14.04,44.14,33.01,2.76
20260610,48.8,51.6,47,47,12436000,43.26,8.64,44.49,33.44,5.03
20260611,47,51.7,46.6,51.7,8215000,43.96,17.59,45.12,33.94,2.94
20260612,54.7,55.6,50.3,50.3,12087000,44.49,13.05,45.77,34.43,3.67
20260615,51.4,55.3,51.4,55.3,3811000,45.39,21.82,46.49,35,1.15
20260616,57.8,59,53.7,54.9,9298000,46.19,18.87,47.26,35.55,2.6
20260617,54.9,56.8,51.7,52.9,3882000,46.75,13.17,47.73,36.08,1.12
20260618,52.2,54.2,51.4,52.3,2962000,47.21,10.79,48.22,36.59,0.97
20260622,53.1,53.5,49.55,51,2234000,47.52,7.31,48.43,37.08,0.7
20260623,50.5,50.5,48.6,48.95,1437000,47.64,2.74,48.51,37.54,0.44
20260624,48.65,51.1,48.15,50.2,2021000,47.86,4.9,48.66,38,0.61
20260625,51,51,48.65,49.3,1148000,47.98,2.76,48.79,38.44,0.34
20260626,49.05,54.2,49.05,54.2,3576000,48.49,11.76,49.17,38.97,1
20260629,57.5,58.4,48.8,48.8,7597000,48.52,0.58,49.28,39.41,1.93
20260630,48.85,51,48.85,49.8,1770000,48.63,2.41,49.5,39.87,0.44
20260701,51.3,54.4,51.3,54.4,4111000,49.11,10.78,49.92,40.41,0.97
20260702,54.4,59,52.2,56.2,9980000,49.7,13.08,50.41,40.97,2.11
20260703,56.8,61.8,56.8,61.8,8858000,50.71,21.88,51.31,41.63,1.71
20260706,64.1,67,62,63,12206000,51.73,21.78,52.27,42.3,2.11
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 62.05
- over_600_ratio: 58.2
- over_800_ratio: 56.8
- over_1000_ratio: 56.8
- over_400_change_1w: 0.24
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.55,,58.63,,57.01,,0,False,False
20260508,64.55,-2,58.63,0,57.01,0,0,False,False
20260515,64.53,-0.02,58.63,0,57.01,0,0,False,False
20260522,62.53,-2,57.01,-1.62,57.01,0,0,False,False
20260529,61.2,-1.33,56.97,-0.04,56.97,-0.04,0,False,False
20260605,61.2,0,56.97,0,56.97,0,0,False,False
20260612,64.38,3.18,56.87,-0.1,56.87,-0.1,1,False,False
20260618,63.42,-0.96,56.81,-0.06,56.81,-0.06,0,False,False
20260626,61.81,-1.61,56.8,-0.01,56.8,-0.01,0,False,False
20260703,62.05,0.24,56.8,0,56.8,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 6174 | 安碁 | true_breakout | 嚴格突破 | 74.0 |  |  | platform_breakout |  |  | continued_overheated | 1.事實發生日:115/07/03 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: 基本資料： (一)最近一月單月             115年05月     114年05月     與去年同期增減(%) 營業收入(百萬元)                 64.19         51.42              24.83 稅前淨利(百萬元)                  6.76         -8.40             180.47 歸屬母公司業主淨利(百萬元)        5.72         -6.79             184.24 每股盈餘(元)                      0.11         -0.14             178.57 (二)最近一季單季            115年第1季    114年第1季     與去年同期增減(%) 營業收入(百萬元)                166.49        143.87              15.72 稅前淨利(百萬元)                 19.21         15.71              22.28 歸屬母公司業主淨利(百萬元)       16.48         13.55              21.62 每股盈餘(元)                      0.33          0.27              22.22 (三)最近四季累計            114年第2季至115年第1季 營業收入(百萬元)                633.63 稅前淨利(百萬元)                 42.42 歸屬母公司業主淨利(百萬元)       36.01 每股盈餘(元)                      0.72 (四)公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1) 以上115年5月、114年5月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併數，未經會計師查核(閱)，僅供投資人參考。 (2) 最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係本公 司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3) 最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經會計 師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260706 | 6174 | 安碁 | 6 | 2 | 5 | 8 | 8 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
