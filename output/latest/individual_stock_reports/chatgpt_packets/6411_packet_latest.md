# INDIVIDUAL STOCK CHATGPT PACKET - 6411 晶焱

## Metadata
- generated_at: 2026-07-01 22:28:25 Asia/Taipei
- stock_id: 6411
- stock_name: 晶焱
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6411_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6411_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6411_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6411_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6411_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6411_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6411_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6411_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6411_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6411_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6411_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6411_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6411.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6411.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6411.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6411.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6411_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6411_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6411_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- no_major_tdcc_warning
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
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260701
- open: 102
- high: 103.5
- low: 96
- close: 97.5
- volume: 1634000
- ma5: 98.4
- ema23_primary: 98.38
- distance_to_ema23_pct: -0.89
- ma20: 98.81
- ma60: 89.39
- ma120: 84.51
- return_5d: -8.45
- return_20d: -2.5
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: -1.32
- distance_to_high_60_pct: -17.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,100,104,100,100.5,102000,93.41,7.59,92.23,82.53,0.15
20260604,99.7,101.5,98,99.1,100000,93.89,5.55,93.1,82.9,0.15
20260605,97.8,101.5,96.1,99,98000,94.31,4.97,94.06,83.25,0.16
20260608,89.1,90.7,89.1,89.1,1721000,93.88,-5.09,94.39,83.38,2.61
20260609,89.9,92.8,87.6,91.7,1832000,93.7,-2.13,94.75,83.57,2.61
20260610,89.8,96.7,89.8,91.6,1737000,93.52,-2.06,95.23,83.77,2.29
20260611,92.4,95.6,90.3,93.9,1053000,93.55,0.37,95.67,84.03,1.5
20260612,96.9,102,96.8,97.7,1788000,93.9,4.05,96.43,84.31,2.42
20260615,100,100.5,96.4,96.4,1264000,94.11,2.44,97.1,84.58,1.63
20260616,97,99.6,96,96.4,951000,94.3,2.23,97.8,84.89,1.19
20260617,96.4,98.4,95.3,97.2,621000,94.54,2.81,98.36,85.2,0.82
20260618,100,106.5,100,106.5,3555000,95.54,11.47,98.95,85.73,4.57
20260622,113.5,117,110,114,5878000,97.08,17.43,99.91,86.38,5.51
20260623,113.5,115.5,103,104.5,4866000,97.69,6.97,100.33,86.83,3.73
20260624,102.5,108.5,102.5,106.5,2393000,98.43,8.2,100.63,87.33,1.69
20260625,108,108,102,102,1255000,98.73,3.32,100.68,87.75,0.85
20260626,102,102,96.9,96.9,1509000,98.57,-1.7,99.97,88.12,0.98
20260629,96.8,99.8,96.2,96.4,703000,98.39,-2.03,99.3,88.52,0.45
20260630,97.5,99.7,97,99.2,772000,98.46,0.75,98.93,88.96,0.48
20260701,102,103.5,96,97.5,1634000,98.38,-0.89,98.81,89.39,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 37
- over_600_ratio: 29.73
- over_800_ratio: 25.65
- over_1000_ratio: 21.94
- over_400_change_1w: 1.45
- over_800_change_1w: 0.33
- over_1000_change_1w: 1.15
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,37.57,,25.81,,22.37,,0,False,False
20260508,37.78,0.21,25.85,0.04,22.35,-0.02,1,False,True
20260515,38.54,0.76,26.01,0.16,22.41,0.06,2,True,True
20260522,40.15,1.61,27.33,1.32,22.81,0.4,3,False,True
20260529,41.48,1.33,26.5,-0.83,23.74,0.93,4,False,True
20260605,37.26,-4.22,26.1,-0.4,23.34,-0.4,0,False,False
20260612,36.1,-1.16,25.43,-0.67,20.79,-2.55,0,False,False
20260618,35.55,-0.55,25.32,-0.11,20.79,0,0,False,False
20260626,37,1.45,25.65,0.33,21.94,1.15,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6411 | 晶焱 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | repeated_but_no_breakout | 1.主管機關核准減資日期:NA 2.辦理資本變更登記完成日期:115/06/23 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）: (1)本次註銷限制員工權利新股3,300股，    每股面額新台幣10元，共計減少資本33,000元。 (2)註銷減資前：本公司實收資本額為新台幣995,006,310元，    流通在外股數為99,500,631股，每股淨值新台幣48.91元。 (3)註銷減資後：實收資本額為新台幣994,973,310元，    流通在外股數為99,497,331股，每股淨值新台幣48.91元。 (註：每股淨值以115年第1季之財務報表歸屬於母公司業主之權益為計算依據) 4.預計換股作業計畫:不適用。 5.預計減資新股上櫃後之上櫃普通股股數:不適用。 6.預計減資新股上櫃後之上櫃普通股股數占已發行普通股比率 （減資後上櫃普通股股數/減資後已發行普通股股數）:不適用。 7.前二項預計減資後上櫃普通股股數未達500萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用。 8.其他應敘明事項: (1)本公司於115/06/24接獲經濟部變更登記核准函。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6411 | 晶焱 | 1 | 1 | 3 | 6 | 11 | repeated_but_no_breakout | 近 10 日上榜 6 次、近 20 日上榜 11 次，但尚未有效突破，需等待攻擊確認。 |

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
