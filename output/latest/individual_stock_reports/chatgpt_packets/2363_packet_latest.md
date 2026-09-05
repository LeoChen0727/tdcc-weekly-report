# INDIVIDUAL STOCK CHATGPT PACKET - 2363 矽統

## Metadata
- generated_at: 2026-09-05 22:15:53 Asia/Taipei
- stock_id: 2363
- stock_name: 矽統
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2363_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2363_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2363_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2363_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2363_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2363_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2363_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2363_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2363_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2363_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2363_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2363_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2363.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2363.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2363.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2363.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2363_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2363_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2363_latest.md?ref=main

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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260904
- open: 50.7
- high: 51.2
- low: 50.4
- close: 51.1
- volume: 1964400
- ma5: 50.96
- ema23_primary: 52.18
- distance_to_ema23_pct: -2.07
- ma20: 52.03
- ma60: 57.8
- ma120: 56.88
- return_5d: -1.35
- return_20d: -4.84
- volume_ratio: 0.53
- distance_to_ma20_pct_auxiliary: -1.8
- distance_to_high_60_pct: -32.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,54.6,54.8,53.6,54,5470781,55.4,-2.53,54.51,61.4,0.75
20260811,54.2,57.3,53.3,57,9332065,55.53,2.64,54.26,61.34,1.31
20260812,56.9,58.5,55.3,55.4,7614052,55.52,-0.22,53.78,61.24,1.1
20260813,55.6,56.5,54.4,54.4,5577288,55.43,-1.85,53.35,61.14,0.81
20260814,54.7,55.2,53.4,53.4,2955221,55.26,-3.36,53.18,61.03,0.46
20260817,53.3,54.1,53,53.1,2216280,55.08,-3.59,53,60.86,0.36
20260818,53.1,53.6,51.3,51.3,3297620,54.76,-6.33,52.7,60.61,0.55
20260819,50,51.4,49.85,50.8,2060933,54.43,-6.68,52.29,60.3,0.36
20260820,51.9,52.2,50.5,51,1511296,54.15,-5.81,51.98,60.02,0.27
20260821,51.1,51.5,50.4,50.7,1788029,53.86,-5.87,51.75,59.76,0.33
20260824,50.4,52.6,50.4,50.6,4165416,53.59,-5.58,51.55,59.52,0.76
20260825,50.6,50.6,49.2,50.4,2903922,53.32,-5.48,51.61,59.25,0.55
20260826,50.5,51.6,50.4,51.3,1927373,53.15,-3.49,51.9,58.98,0.39
20260827,51.6,51.8,50.5,50.7,2743280,52.95,-4.25,52.2,58.71,0.6
20260828,51,53.3,51,51.8,5590442,52.85,-1.99,52.33,58.49,1.26
20260831,50.6,51.3,50.4,51.1,3164672,52.71,-3.05,52.39,58.29,0.74
20260901,51.8,53.1,51.2,51.5,4380842,52.61,-2.1,52.4,58.1,1.03
20260902,51,51.9,50.9,51,1919873,52.47,-2.81,52.31,58,0.48
20260903,51.3,51.9,50.1,50.1,3454519,52.28,-4.16,52.16,57.87,0.87
20260904,50.7,51.2,50.4,51.1,1964400,52.18,-2.07,52.03,57.8,0.53
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 34.71
- over_600_ratio: 33.31
- over_800_ratio: 32.13
- over_1000_ratio: 30.74
- over_400_change_1w: -0.07
- over_800_change_1w: -0.27
- over_1000_change_1w: -0.11
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,36.63,0,33.25,0.08,32.04,0.42,1,False,True
20260626,41.37,4.74,38.4,5.15,36.98,4.94,2,True,True
20260703,38.8,-2.57,36.16,-2.24,34.61,-2.37,0,False,False
20260709,37.49,-1.31,34.98,-1.18,32.7,-1.91,0,False,False
20260717,36.73,-0.76,34.2,-0.78,31.27,-1.43,0,False,False
20260724,35.95,-0.78,32.97,-1.23,30.53,-0.74,0,False,False
20260731,35.21,-0.74,31.95,-1.02,30.4,-0.13,0,False,False
20260807,35.85,0.64,33.06,1.11,31.18,0.78,1,True,True
20260814,35.71,-0.14,33,-0.06,31.47,0.29,2,False,True
20260821,35.39,-0.32,32.19,-0.81,30.96,-0.51,0,False,False
20260828,34.78,-0.61,32.4,0.21,30.85,-0.11,1,False,True
20260904,34.71,-0.07,32.13,-0.27,30.74,-0.11,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2363 | 矽統 | revenue_pullback | 營收成長股價回檔 | 50.0 |  |  |  |  | no_signal | stale_signal | 1.提報董事會或經董事會決議日期:115/07/27 2.審計委員會通過日期:115/07/27 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):2026/01/01~2026/06/30 4.1月1日累計至本期止營業收入(仟元):2,211,081 5.1月1日累計至本期止營業毛利(毛損) (仟元):628,335 6.1月1日累計至本期止營業利益(損失) (仟元):121,979 7.1月1日累計至本期止稅前淨利(淨損) (仟元):175,408 8.1月1日累計至本期止本期淨利(淨損) (仟元):106,329 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):103,177 10.1月1日累計至本期止基本每股盈餘(損失) (元):0.20 11.期末總資產(仟元):52,079,509 12.期末總負債(仟元):3,088,848 13.期末歸屬於母公司業主之權益(仟元):48,864,470 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2363 | 矽統 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 49 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.提報董事會或經董事會決議日期:115/07/27 2.審計委員會通過日期:115/07/27 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):2026/01/01~2026/06/30 4.1月1日累計至本期止營業收入(仟元):2,211,081 5.1月1日累計至本期止營業毛利(毛損) (仟元):628,335 6.1月1日累計至本期止營業利益(損失) (仟元):121,979 7.1月1日累計至本期止稅前淨利(淨損) (仟元):175,408 8.1月1日累計至本期止本期淨利(淨損) (仟元):106,329 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):103,177 10.1月1日累計至本期止基本每股盈餘(損失) (元):0.20 11.期末總資產(仟元):52,079,509 12.期末總負債(仟元):3,088,848 13.期末歸屬於母公司業主之權益(仟元):48,864,470 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2363 | 矽統 | 48 | 11 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2363 | 矽統 | 102 | 5 | 2322700.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
