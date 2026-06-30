# INDIVIDUAL STOCK CHATGPT PACKET - 3211 順達

## Metadata
- generated_at: 2026-06-30 22:27:04 Asia/Taipei
- stock_id: 3211
- stock_name: 順達
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 159
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3211_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3211_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3211.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3211.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3211.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3211.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3211_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3211_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3211_latest.md?ref=main

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
- date: 20260630
- open: 403
- high: 420
- low: 398.5
- close: 413
- volume: 2886000
- ma5: 404.5
- ema23_primary: 414.79
- distance_to_ema23_pct: -0.43
- ma20: 421.6
- ma60: 395.15
- ma120: 353.52
- return_5d: -3.39
- return_20d: -5.28
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: -2.04
- distance_to_high_60_pct: -16.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,436,441.5,416,422,423,402.03,4.97,399.02,363.96,0
20260603,426,464,421,464,446000,407.2,13.95,403.5,366.32,0.08
20260604,454,470,452.5,454,461000,411.1,10.44,407,369.01,0.1
20260605,450.5,451.5,415,423,427000,412.09,2.65,409.07,370.82,0.1
20260608,381,397.5,381,393,8540000,410.5,-4.26,408.57,372.16,2.24
20260609,400,431.5,398.5,422,9439000,411.46,2.56,409.57,374.18,2.72
20260610,414,427,405,405,7601000,410.92,-1.44,410.32,375.8,2.29
20260611,396,403,382.5,398.5,6782000,409.88,-2.78,411.48,377.37,2.12
20260612,417.5,422,408,418,4940000,410.56,1.81,414.4,379.22,1.67
20260615,429,440,422,428.5,6290000,412.05,3.99,417.45,381.27,2.06
20260616,434,453,432.5,437.5,8239000,414.18,5.63,421.38,383.51,2.52
20260617,435.5,442.5,425,428,4594000,415.33,3.05,425.43,385.23,1.41
20260618,430.5,446.5,428,436,5269000,417.05,4.54,429.57,387.48,1.59
20260622,440,458.5,422.5,452.5,9198000,420,7.74,432.8,389.76,2.46
20260623,455.5,460,425.5,427.5,7257000,420.63,1.63,432.85,391.09,1.78
20260624,419,425,412.5,419,3632000,420.49,-0.36,430.35,392.04,0.86
20260625,425,426,405.5,408,4806000,419.45,-2.73,427.55,392.76,1.08
20260626,403,407.5,386.5,390,4235000,417,-6.47,424.93,393.35,0.91
20260629,390,408.5,389,392.5,2515000,414.96,-5.41,422.75,394.14,0.53
20260630,403,420,398.5,413,2886000,414.79,-0.43,421.6,395.15,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 53.66
- over_600_ratio: 49.75
- over_800_ratio: 45.05
- over_1000_ratio: 43.91
- over_400_change_1w: -1.05
- over_800_change_1w: -2.85
- over_1000_change_1w: -1.48
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.62,,47.47,,41.48,,0,False,False
20260508,52.81,-1.81,45.8,-1.67,39.83,-1.65,0,False,False
20260515,51.09,-1.72,45.49,-0.31,39.56,-0.27,0,False,False
20260522,48.79,-2.3,41.75,-3.74,37.67,-1.89,0,False,False
20260529,58.76,9.97,50.64,8.89,47.6,9.93,1,True,True
20260605,56.1,-2.66,48.7,-1.94,42.87,-4.73,0,False,False
20260612,54.18,-1.92,47.37,-1.33,44.29,1.42,1,False,True
20260618,54.71,0.53,47.9,0.53,45.39,1.1,2,True,True
20260626,53.66,-1.05,45.05,-2.85,43.91,-1.48,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 3211 | 順達 | pattern | 型態觀察 | 45.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.發生變動日期:115/06/22 2.功能性委員會名稱:提名委員會 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名:  董　　事：鹿寮坑(股)公司代表人：鍾聰明  獨立董事：謝漢萍  獨立董事：林政憲  獨立董事：許婉美 6.新任者簡歷:  董　　事 鹿寮坑(股)公司代表人：鍾聰明；順達科技(股)公司董事長  獨立董事 謝漢萍；凱崴電子(股)公司獨立董事  獨立董事 林政憲；律宇國際商務法律事務所主持律師  獨立董事 許婉美；之初創業投資管理顧問(股)公司監察人 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）:  「新任」。 8.異動原因:設置提名委員會。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:不適用。 10.新任生效日期:115/06/22 11.其他應敘明事項:  提名委員會成員推舉謝漢萍獨立董事為召集人。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 3211 | 順達 | 1 | 1 | 3 | 5 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
