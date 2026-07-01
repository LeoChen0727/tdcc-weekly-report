# INDIVIDUAL STOCK CHATGPT PACKET - 2022 聚亨

## Metadata
- generated_at: 2026-07-01 22:27:02 Asia/Taipei
- stock_id: 2022
- stock_name: 聚亨
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 295
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2022_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2022_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2022_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2022_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2022_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2022_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2022_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2022_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2022_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2022_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2022_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2022_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2022.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2022.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2022.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2022.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2022_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2022_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2022_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 7.79
- high: 8.16
- low: 7.68
- close: 8
- volume: 1593000
- ma5: 7.73
- ema23_primary: 7.81
- distance_to_ema23_pct: 2.49
- ma20: 7.82
- ma60: 8.08
- ma120: 8.46
- return_5d: 3.49
- return_20d: 3.36
- volume_ratio: 1.81
- distance_to_ma20_pct_auxiliary: 2.37
- distance_to_high_60_pct: -16.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,7.78,8.19,7.76,8.08,2836846,7.92,1.96,7.84,8.49,2.15
20260604,8.1,8.17,8,8.08,1610437,7.94,1.79,7.84,8.48,1.19
20260605,8.05,8.05,7.88,8.02,949708,7.94,0.95,7.84,8.46,0.69
20260608,7.78,7.89,7.6,7.85,782690,7.94,-1.09,7.82,8.44,0.58
20260609,7.91,7.99,7.82,7.89,524375,7.93,-0.54,7.81,8.42,0.39
20260610,7.8,7.94,7.79,7.79,897313,7.92,-1.65,7.78,8.4,0.67
20260611,7.8,7.84,7.6,7.7,667927,7.9,-2.56,7.77,8.38,0.53
20260612,7.8,7.87,7.76,7.8,723470,7.89,-1.19,7.78,8.36,0.6
20260615,7.9,7.92,7.82,7.85,652784,7.89,-0.51,7.79,8.34,0.54
20260616,7.86,7.93,7.75,7.79,518128,7.88,-1.17,7.8,8.32,0.43
20260617,7.81,7.83,7.73,7.77,371439,7.87,-1.3,7.82,8.29,0.31
20260618,7.79,7.82,7.7,7.72,709537,7.86,-1.78,7.82,8.26,0.59
20260622,7.78,7.88,7.76,7.85,1275328,7.86,-0.11,7.84,8.24,1.04
20260623,7.85,7.85,7.71,7.72,603225,7.85,-1.62,7.81,8.21,0.57
20260624,7.72,7.76,7.63,7.73,544117,7.84,-1.37,7.81,8.19,0.55
20260625,7.73,7.8,7.66,7.68,615121,7.82,-1.85,7.81,8.16,0.64
20260626,7.65,7.72,7.57,7.59,493379,7.8,-2.75,7.81,8.14,0.53
20260629,7.59,7.67,7.59,7.64,287969,7.79,-1.94,7.81,8.11,0.32
20260630,7.64,7.75,7.64,7.75,906000,7.79,-0.49,7.8,8.09,1.05
20260701,7.79,8.16,7.68,8,1593000,7.81,2.49,7.82,8.08,1.81
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 39.82
- over_600_ratio: 38.5
- over_800_ratio: 37.25
- over_1000_ratio: 36.44
- over_400_change_1w: -0.11
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 8
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,38.78,,36.38,,35.87,,0,False,False
20260508,38.97,0.19,36.6,0.22,36.07,0.2,1,True,True
20260515,39.16,0.19,36.67,0.07,36.4,0.33,2,False,True
20260522,38.95,-0.21,36.72,0.05,36.45,0.05,3,False,True
20260529,39.21,0.26,36.74,0.02,36.47,0.02,4,True,True
20260605,39.69,0.48,36.78,0.04,36.51,0.04,5,True,True
20260612,39.75,0.06,36.96,0.18,36.43,-0.08,6,False,True
20260618,39.93,0.18,37.23,0.27,36.43,0,7,False,True
20260626,39.82,-0.11,37.25,0.02,36.44,0.01,8,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2022 | 聚亨 | pullback_rebound | 回檔後短線轉強 | 62.0 |  |  |  |  |  | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/06/23 1.召開法人說明會之日期：115/06/23 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：高雄市岡山區新樂街79-1號 聚亨公司一樓會議室 4.法人說明會擇要訊息：公司營運概況說明 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |
| 20260701 | 2022 | 聚亨 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  |  | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/06/23 1.召開法人說明會之日期：115/06/23 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：高雄市岡山區新樂街79-1號 聚亨公司一樓會議室 4.法人說明會擇要訊息：公司營運概況說明 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260701 | 2022 | 聚亨 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/06/23 1.召開法人說明會之日期：115/06/23 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：高雄市岡山區新樂街79-1號 聚亨公司一樓會議室 4.法人說明會擇要訊息：公司營運概況說明 5.其他應敘明事項：無 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2022 | 聚亨 | 1 | 1 | 1 | 2 | 7 | repeated_but_no_breakout | 近 10 日上榜 2 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

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
