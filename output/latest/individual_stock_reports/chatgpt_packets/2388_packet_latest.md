# INDIVIDUAL STOCK CHATGPT PACKET - 2388 威盛

## Metadata
- generated_at: 2026-09-19 22:16:02 Asia/Taipei
- stock_id: 2388
- stock_name: 威盛
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2388_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2388_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2388_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2388_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2388_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2388_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2388_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2388_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2388_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2388_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2388_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2388_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2388.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2388.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2388.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2388.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2388_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2388_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2388_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- decision_score_high
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
- date: 20260918
- open: 70.9
- high: 71.1
- low: 69.8
- close: 69.9
- volume: 2818265
- ma5: 70.52
- ema23_primary: 73.77
- distance_to_ema23_pct: -5.24
- ma20: 73.99
- ma60: 73.75
- ma120: 72.4
- return_5d: -7.05
- return_20d: -5.41
- volume_ratio: 0.68
- distance_to_ma20_pct_auxiliary: -5.53
- distance_to_high_60_pct: -17.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,73.8,74.9,72.1,72.1,2214243,74.74,-3.53,75.11,73.35,0.41
20260825,72.1,72.2,70.2,71.9,2226821,74.5,-3.49,75.22,73.27,0.42
20260826,72.6,74.7,72,74,3026628,74.46,-0.62,75.55,73.25,0.6
20260827,74.8,75.2,72.5,72.5,2004474,74.3,-2.42,75.91,73.21,0.41
20260828,73.1,74.2,72.7,73.3,1551472,74.21,-1.23,76.05,73.2,0.33
20260831,72.9,73.5,71.5,72.7,1997572,74.09,-1.87,75.89,73.19,0.44
20260901,72.9,74.9,72.9,73.3,2051162,74.02,-0.97,75.53,73.27,0.49
20260902,72.7,77.2,72.7,76.4,5310277,74.22,2.94,75.2,73.46,1.4
20260903,76.1,78,73.7,75,6337270,74.28,0.96,74.98,73.61,1.72
20260904,75.4,82.4,75.4,81.4,14272565,74.88,8.71,75.16,73.89,3.43
20260907,82,83,77.1,77.7,8928166,75.11,3.44,75.01,74.09,2.05
20260908,78.1,81.2,75.8,76.1,8501828,75.2,1.2,74.86,74.26,1.86
20260909,76.8,78.5,76,77.9,3223793,75.42,3.29,74.88,74.38,0.72
20260910,78.1,78.1,76.4,77.7,1974089,75.61,2.76,74.95,74.54,0.46
20260911,75.7,76.5,75.1,75.2,2593225,75.58,-0.5,74.91,74.54,0.61
20260914,74.7,74.8,72.2,72.3,2929348,75.3,-3.99,74.56,74.39,0.7
20260915,72.1,72.8,69.4,69.4,3721940,74.81,-7.23,74.41,74.14,0.91
20260916,70.2,71.4,69.4,71.3,2250709,74.52,-4.32,74.38,74,0.57
20260917,71.9,72.4,69.5,69.7,4760943,74.12,-5.96,74.19,73.85,1.17
20260918,70.9,71.1,69.8,69.9,2818265,73.77,-5.24,73.99,73.75,0.68
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 71.38
- over_600_ratio: 69.88
- over_800_ratio: 69.4
- over_1000_ratio: 67.96
- over_400_change_1w: -0.95
- over_800_change_1w: -0.64
- over_1000_change_1w: -0.34
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,68.41,-0.48,66.02,-0.32,64.89,-0.02,0,False,False
20260709,68.41,0,66.21,0.19,64.56,-0.33,1,False,True
20260717,68.5,0.09,66.38,0.17,64.39,-0.17,2,False,True
20260724,69.09,0.59,66.5,0.12,65.04,0.65,3,True,True
20260731,69.29,0.2,66.6,0.1,65.5,0.46,4,True,True
20260807,71.58,2.29,69.49,2.89,68.4,2.9,5,True,True
20260814,71.58,0,69.2,-0.29,67.46,-0.94,0,False,False
20260821,71.5,-0.08,68.91,-0.29,67.19,-0.27,0,False,False
20260828,71.23,-0.27,68.9,-0.01,67.35,0.16,1,False,True
20260904,71.74,0.51,69.05,0.15,67.79,0.44,2,True,True
20260911,72.33,0.59,70.04,0.99,68.3,0.51,3,True,True
20260918,71.38,-0.95,69.4,-0.64,67.96,-0.34,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2388 | 威盛 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | no_signal | stale_signal | 1.原預定買回股份總金額上限(元):13,905,286,277 2.原預定買回之期間:115/07/09~115/09/07 3.原預定買回之數量(股):20,000,000 4.原預定買回區間價格(元):48.65~90.00 5.本次實際買回期間:115/07/09~115/09/07 6.本次已買回股份數量(股):20,000,000 7.本次已買回股份總金額(元):1,494,758,388 8.本次平均每股買回價格(元):74.74 9.累積已持有自己公司股份數量(股):20,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):3.60 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 2388 | 威盛 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 14 | A_優先追蹤 |  |  | no_signal | stale_signal | 1.原預定買回股份總金額上限(元):13,905,286,277 2.原預定買回之期間:115/07/09~115/09/07 3.原預定買回之數量(股):20,000,000 4.原預定買回區間價格(元):48.65~90.00 5.本次實際買回期間:115/07/09~115/09/07 6.本次已買回股份數量(股):20,000,000 7.本次已買回股份總金額(元):1,494,758,388 8.本次平均每股買回價格(元):74.74 9.累積已持有自己公司股份數量(股):20,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):3.60 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2388 | 威盛 | 20 | 8 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2388 | 威盛 | 82 | 3 | 733910.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
