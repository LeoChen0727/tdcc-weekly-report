# INDIVIDUAL STOCK CHATGPT PACKET - 6126 信音

## Metadata
- generated_at: 2026-06-27 22:24:08 Asia/Taipei
- stock_id: 6126
- stock_name: 信音
- packet_status: standard_180d_window_packet
- latest_price_date: 20260626
- price_rows: 157
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6126_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6126_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6126.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6126.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6126.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6126.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6126_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6126_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6126_latest.md?ref=main

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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
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
- date: 20260626
- open: 39.6
- high: 39.6
- low: 35.65
- close: 35.75
- volume: 4233000
- ma5: 38.94
- ema23_primary: 38.64
- distance_to_ema23_pct: -7.47
- ma20: 39.79
- ma60: 35.06
- ma120: 34.79
- return_5d: -11.29
- return_20d: 1.13
- volume_ratio: 1.31
- distance_to_ma20_pct_auxiliary: -10.15
- distance_to_high_60_pct: -19.66

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260529,36,36.15,35.35,35.5,36000,34.12,4.05,34.08,32.52,0.03
20260601,36.95,37.85,36.35,37.25,37000,34.38,8.35,34.26,32.62,0.03
20260602,38.2,39.15,36.85,38.8,38,34.75,11.66,34.51,32.73,0
20260603,38.8,42.65,37.8,42.65,42000,35.41,20.46,34.97,32.9,0.04
20260604,42.2,44.5,41,43,43000,36.04,19.31,35.47,33.12,0.05
20260605,42.8,43.65,38.7,42.5,41000,36.58,16.19,35.99,33.27,0.05
20260608,38.3,39.15,38.25,38.3,5533000,36.72,4.3,36.26,33.35,5.15
20260609,39.55,41.15,38.55,40.95,4781000,37.07,10.45,36.65,33.49,3.76
20260610,39.95,41.8,38.55,38.6,4059000,37.2,3.76,36.96,33.59,2.83
20260611,39.6,42.45,39.1,41.55,11590000,37.56,10.61,37.41,33.74,5.94
20260612,42.05,42.95,40.1,40.25,10563000,37.79,6.52,37.78,33.88,4.49
20260615,40.9,43.3,40.1,41.65,6639000,38.11,9.29,38.17,34.01,2.55
20260616,41.95,42,39.4,39.4,3814000,38.22,3.1,38.46,34.1,1.4
20260617,39.5,40.7,38.9,40.4,2112000,38.4,5.21,38.78,34.23,0.79
20260618,40.6,41.25,40,40.3,1984000,38.56,4.52,39.01,34.38,0.77
20260622,40.9,40.9,39.7,40.15,2463000,38.69,3.77,39.22,34.53,0.91
20260623,40.7,40.75,39.25,39.4,2517000,38.75,1.68,39.38,34.66,0.89
20260624,39,39.8,38.55,39.8,1430000,38.84,2.48,39.55,34.81,0.5
20260625,40.05,41.1,39.5,39.6,2876000,38.9,1.8,39.77,34.96,0.95
20260626,39.6,39.6,35.65,35.75,4233000,38.64,-7.47,39.79,35.06,1.31
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 37.82
- over_600_ratio: 36.25
- over_800_ratio: 33.09
- over_1000_ratio: 31.78
- over_400_change_1w: -1.96
- over_800_change_1w: -2.33
- over_1000_change_1w: -0.88
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.86,,29.43,,28.17,,0,False,False
20260508,35.09,0.23,29.5,0.07,28.17,0,1,False,True
20260515,35.24,0.15,29.68,0.18,29.06,0.89,2,True,True
20260522,36.6,1.36,30.58,0.9,28.57,-0.49,3,False,True
20260529,37.63,1.03,32.34,1.76,30.3,1.73,4,True,True
20260605,39.56,1.93,35.35,3.01,34.73,4.43,5,True,True
20260612,39.78,0.22,35.42,0.07,32.66,-2.07,6,False,True
20260618,37.82,-1.96,33.09,-2.33,31.78,-0.88,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260626 | 6126 | 信音 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  |  | repeated_but_no_breakout | 1.董事會決議日期:115/06/23 2.發放股利種類及金額:現金股利美金2,213,292.41元 3.其他應敘明事項: (1)、信音(香港)國際控股有限公司分配予SINGATRON (BVI) ENTERPRISE CO.,LTD.，再由SINGATRON (BVI)ENTERPRISE CO.,LTD.分配予本公司。 (2)、信音(香港)國際控股有限公司及SINGATRON (BVI)ENTERPRISE CO.,LTD.為本公司100%持股之重要子公司。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260626 | 6126 | 信音 | revenue_breakout_low_response | 營收爆發低反應股 | 15.0 | 13.0 | A_優先追蹤 |  |  |  | repeated_but_no_breakout | 1.董事會決議日期:115/06/23 2.發放股利種類及金額:現金股利美金2,213,292.41元 3.其他應敘明事項: (1)、信音(香港)國際控股有限公司分配予SINGATRON (BVI) ENTERPRISE CO.,LTD.，再由SINGATRON (BVI)ENTERPRISE CO.,LTD.分配予本公司。 (2)、信音(香港)國際控股有限公司及SINGATRON (BVI)ENTERPRISE CO.,LTD.為本公司100%持股之重要子公司。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260626 | 6126 | 信音 | 4 | 4 | 4 | 4 | 12 | repeated_but_no_breakout | 近 10 日上榜 4 次、近 20 日上榜 12 次，但尚未有效突破，需等待攻擊確認。 |

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
