# INDIVIDUAL STOCK CHATGPT PACKET - 4541 晟田

## Metadata
- generated_at: 2026-07-10 22:27:34 Asia/Taipei
- stock_id: 4541
- stock_name: 晟田
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 166
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4541_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4541_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4541.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4541.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4541.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4541.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4541_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4541_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4541_latest.md?ref=main

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
- date: 20260709
- open: 62
- high: 66.4
- low: 60.8
- close: 61
- volume: 11666000
- ma5: 61.98
- ema23_primary: 53.8
- distance_to_ema23_pct: 13.39
- ma20: 52.98
- ma60: 48.6
- ma120: 46.32
- return_5d: 10.51
- return_20d: 30.62
- volume_ratio: 2.48
- distance_to_ma20_pct_auxiliary: 15.13
- distance_to_high_60_pct: -9.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,46.4,47,45.6,46.95,868000,46.02,2.01,45.34,45.17,2.28
20260612,47.1,48.1,47.05,47.55,1180000,46.15,3.03,45.51,45.27,3.37
20260615,48.1,49.25,47.75,49,1738000,46.39,5.63,45.76,45.39,4.26
20260616,49.65,49.95,47.7,48,1836000,46.52,3.17,45.98,45.5,3.85
20260617,47.85,51.3,47.8,51,3584000,46.9,8.75,46.38,45.66,5.73
20260618,50.2,52.4,49.9,50.9,2811000,47.23,7.77,46.72,45.81,3.79
20260622,51.8,52.7,50.3,51,2159000,47.54,7.27,47.05,45.97,2.55
20260623,51,51,48.5,48.5,1346000,47.62,1.84,47.27,46.06,1.47
20260624,48.15,49.05,47.65,48.85,767000,47.73,2.35,47.53,46.18,0.81
20260625,49.45,49.45,48.05,48.05,633000,47.75,0.62,47.72,46.27,0.65
20260626,48,48.6,46.75,47.5,862000,47.73,-0.49,47.85,46.37,0.85
20260629,48.25,50.5,48.25,48.65,2320000,47.81,1.76,48.02,46.5,2.05
20260630,48.2,51.9,47.6,51.9,2779000,48.15,7.79,48.28,46.67,2.19
20260701,55.6,57,52.8,56.7,9404000,48.86,16.04,48.83,46.94,5.4
20260702,55.3,58.5,54,55.2,7281000,49.39,11.76,49.22,47.18,3.46
20260703,55.5,60.7,55.3,60.7,6332000,50.33,20.6,49.9,47.5,2.62
20260706,63.8,66.7,61.4,66.7,13391000,51.7,29.02,50.87,47.86,4.34
20260707,66.7,67.4,60.6,61.1,10531000,52.48,16.42,51.6,48.13,2.95
20260708,63.9,65.5,57.3,60.4,12623000,53.14,13.66,52.27,48.36,3.03
20260709,62,66.4,60.8,61,11666000,53.8,13.39,52.98,48.6,2.48
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 40.36
- over_600_ratio: 36.68
- over_800_ratio: 34.48
- over_1000_ratio: 30.35
- over_400_change_1w: 1.17
- over_800_change_1w: 1.89
- over_1000_change_1w: -0.84
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,38.14,,28.33,,27.08,,0,False,False
20260508,38.29,0.15,29.34,1.01,26.77,-0.31,1,False,True
20260515,35.82,-2.47,27.88,-1.46,25.32,-1.45,0,False,False
20260522,33.8,-2.02,27.8,-0.08,25.31,-0.01,0,False,False
20260529,33.67,-0.13,27.84,0.04,25.3,-0.01,1,False,True
20260605,33.21,-0.46,29.15,1.31,25.28,-0.02,2,False,True
20260612,35.83,2.62,29.11,-0.04,25.27,-0.01,3,False,False
20260618,38.48,2.65,30.12,1.01,28.65,3.38,4,True,True
20260626,39.19,0.71,32.59,2.47,31.19,2.54,5,True,True
20260703,40.36,1.17,34.48,1.89,30.35,-0.84,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 4541 | 晟田 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | continued_overheated | 1.事實發生日:115/07/08 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                最近一月單月      去年同月       與去年同期增減%                    (115/05)      (114/05) ----------------------------------------------------------------- 營業收入(百萬元)     183            166                 10% 稅前淨利(百萬元)      31            -45            由虧轉盈 本期淨利(百萬元)      32            -36            由虧轉盈 每股盈餘(元)        0.47          -0.54            由虧轉盈  說明:115年及114年5月之稅前淨利分別包含淨兌換損失6百萬元      及73百萬元。 ================================================================= (2)單季                最近一季單季       去年同期     與去年同期增減%                (115年第1季)     (114年第1季) ----------------------------------------------------------------- 營業收入(百萬元)    451             344                31% 稅前淨利(百萬元)     57              52                10% 本期淨利(百萬元)     46              42                10% 每股盈餘(元)       0.68            0.62                10% ================================================================= (3)最近四季累計                      114年第2季至115年第1季 ----------------------------------------------------------------- 營業收入(百萬元)              1,752 稅前淨利(百萬元)                174 本期淨利(百萬元)                141 每股盈餘(元)                   2.09 ================================================================= (4)公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)115年5月和去年同期比較數之財務資料係本公司採IFRS會計  　準則編製之自結數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，且係本公司採IFRS下編製之    數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之    數，業經會計師查核(閱)。 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 4541 | 晟田 | 9 | 3 | 5 | 9 | 12 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
