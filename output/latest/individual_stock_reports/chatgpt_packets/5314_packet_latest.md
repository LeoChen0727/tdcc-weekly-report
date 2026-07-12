# INDIVIDUAL STOCK CHATGPT PACKET - 5314 世紀*

## Metadata
- generated_at: 2026-07-12 22:27:31 Asia/Taipei
- stock_id: 5314
- stock_name: 世紀*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 164
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5314_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5314_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5314_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5314_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5314_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5314_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5314_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5314_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5314_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5314_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5314_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5314_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5314.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5314.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5314.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5314.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5314_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5314_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5314_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
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
- date: 20260709
- open: 67.6
- high: 69.3
- low: 66
- close: 66
- volume: 6065000
- ma5: 68.06
- ema23_primary: 64.09
- distance_to_ema23_pct: 2.99
- ma20: 62.07
- ma60: 67.11
- ma120: 76.78
- return_5d: 1.54
- return_20d: 12.24
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: 6.33
- distance_to_high_60_pct: -20.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,59.8,60.3,58.2,58.4,1933000,64.23,-9.08,63.22,71.74,0.94
20260612,60.2,60.7,58.4,58.4,2203000,63.75,-8.39,62.77,71.37,1.12
20260615,59.3,59.8,58.1,58.1,1802000,63.28,-8.18,62.41,71.01,0.96
20260616,58.6,59.1,56.5,56.5,2349000,62.71,-9.9,62.16,70.66,1.39
20260617,56.7,57.5,55.8,56.8,2043000,62.22,-8.71,61.62,70.38,1.38
20260618,57.1,59.1,57,59,2625000,61.95,-4.76,61.09,70.16,2.42
20260622,60.6,62,60.2,61.1,4827000,61.88,-1.26,60.79,69.97,3.65
20260623,62.5,62.5,59.9,60.5,4159000,61.76,-2.05,60.58,69.8,2.72
20260624,60.7,61,59.3,59.4,2451000,61.57,-3.52,60.4,69.53,1.49
20260625,60.5,60.5,58,58,1818000,61.27,-5.34,60.19,69.22,1.05
20260626,57.6,57.7,55.3,55.3,2895000,60.77,-9.01,59.89,68.86,1.54
20260629,56,60.8,56,60.8,6167000,60.77,0.04,59.78,68.51,2.83
20260630,63.5,66.8,62.2,66.8,16637000,61.28,9.01,59.85,68.35,5.52
20260701,67.6,70.5,65.8,67,20018000,61.75,8.5,60.05,68.17,4.99
20260702,66.2,67.8,65,65,6677000,62.02,4.8,60.12,68,1.54
20260703,66,71.5,65.6,71.5,28765000,62.81,13.83,60.59,67.88,4.98
20260706,73,75,67.5,67.6,34557000,63.21,6.94,60.91,67.69,4.61
20260707,68.8,71.5,64.4,67.8,12446000,63.6,6.61,61.34,67.49,1.56
20260708,69.8,70.5,65.9,67.4,8889000,63.91,5.46,61.71,67.31,1.07
20260709,67.6,69.3,66,66,6065000,64.09,2.99,62.07,67.11,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 44.55
- over_600_ratio: 42.5
- over_800_ratio: 41.55
- over_1000_ratio: 40.66
- over_400_change_1w: -0.61
- over_800_change_1w: -0.32
- over_1000_change_1w: -0.6
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.17,,45.65,,44.76,,0,False,False
20260508,48.06,-0.11,44.3,-1.35,43.98,-0.78,0,False,False
20260515,46.95,-1.11,43.74,-0.56,43.41,-0.57,0,False,False
20260522,47.17,0.22,43.79,0.05,43.48,0.07,1,False,True
20260529,46.37,-0.8,43.04,-0.75,43.04,-0.44,0,False,False
20260605,46.27,-0.1,42.62,-0.42,42.62,-0.42,0,False,False
20260612,45.8,-0.47,42.97,0.35,42.14,-0.48,1,False,True
20260618,45.81,0.01,42.12,-0.85,41.52,-0.62,2,False,False
20260626,45.16,-0.65,41.87,-0.25,41.26,-0.26,0,False,False
20260703,44.55,-0.61,41.55,-0.32,40.66,-0.6,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 5314 | 世紀* | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  通過承認114年度盈餘分配案。 3.重要決議事項二、章程修訂:                  通過「公司章程」修訂案。 4.重要決議事項三、營業報告書及財務報表:                  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)114年度盈餘轉增資發行新股案。  (2)本公司擬發行限制員工權利新股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 5314 | 世紀* | revenue_breakout_low_response | 營收爆發低反應股 | 13.0 | 25.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  通過承認114年度盈餘分配案。 3.重要決議事項二、章程修訂:                  通過「公司章程」修訂案。 4.重要決議事項三、營業報告書及財務報表:                  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)114年度盈餘轉增資發行新股案。  (2)本公司擬發行限制員工權利新股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 5314 | 世紀* | 13 | 13 | 5 | 10 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
