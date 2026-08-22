# INDIVIDUAL STOCK CHATGPT PACKET - 2723 美食-KY

## Metadata
- generated_at: 2026-08-22 22:27:08 Asia/Taipei
- stock_id: 2723
- stock_name: 美食-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2723_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2723_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2723_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2723_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2723_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2723_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2723_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2723_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2723_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2723_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2723_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2723_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2723.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2723.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2723.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2723.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2723_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2723_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2723_latest.md?ref=main

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
- action_rating_display_zh: 可小量試單
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 嚴格突破，價格結構尚未破壞，操作評級為「可小量試單」。
- entry_strategy_zh: 突破後順勢追蹤；可依「試單 1/3 部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 試單 1/3 部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 嚴格突破，價格結構尚未破壞，操作評級為「可小量試單」。 進場策略：突破後順勢追蹤；可依「試單 1/3 部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: starter_position
- action_rating_label_zh: 可小量試單
- confidence_level: medium
- thesis_state: breakout_confirmed
- entry_style: breakout_follow
- position_sizing: starter_1_3

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
- date: 20260821
- open: 73
- high: 73.2
- low: 72.5
- close: 73.2
- volume: 1644639
- ma5: 66.24
- ema23_primary: 64.02
- distance_to_ema23_pct: 14.34
- ma20: 62.92
- ma60: 64.53
- ma120: 65.92
- return_5d: 19.8
- return_20d: 18.06
- volume_ratio: 4.14
- distance_to_ma20_pct_auxiliary: 16.34
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,62.3,62.6,61.9,62.5,190859,64.67,-3.36,65.35,64.97,0.82
20260728,62,62.3,61.5,61.9,188926,64.44,-3.94,65.04,64.94,0.83
20260729,62.5,62.5,60.6,61.5,410122,64.19,-4.2,64.78,64.9,1.85
20260730,62,62,60.9,61.3,328561,63.95,-4.15,64.49,64.81,1.41
20260731,62.2,63.6,62,63.2,443892,63.89,-1.08,64.28,64.75,1.78
20260803,63.7,63.7,62,62.2,215554,63.75,-2.43,64.02,64.69,0.85
20260804,61.6,61.6,61,61.2,203144,63.54,-3.68,63.7,64.59,0.8
20260805,61.6,61.6,60.9,61.2,129066,63.34,-3.38,63.37,64.48,0.51
20260806,61.1,61.6,60.7,61.4,204959,63.18,-2.82,63.11,64.39,0.8
20260807,61.1,62.3,61.1,62.1,183314,63.09,-1.57,62.87,64.31,0.71
20260810,62.5,62.9,61.9,62.9,107925,63.07,-0.28,62.76,64.28,0.44
20260811,62.8,62.8,61.4,62,255454,62.99,-1.56,62.6,64.24,1.06
20260812,62.1,62.1,61,61.6,385670,62.87,-2.02,62.41,64.22,1.53
20260813,61.9,61.9,61,61.1,367839,62.72,-2.59,62.2,64.19,1.39
20260814,61.1,61.2,60.7,61.1,341012,62.59,-2.38,62.11,64.16,1.3
20260817,61.4,64.1,61.4,63.7,914200,62.68,1.63,62.1,64.17,3.08
20260818,63.5,63.6,62.4,62.5,229823,62.66,-0.26,62.02,64.17,0.77
20260819,63.3,65.3,61.8,65.2,578149,62.88,3.7,62.13,64.22,1.83
20260820,65.7,67.1,65.2,66.6,621113,63.19,5.4,62.36,64.32,1.89
20260821,73,73.2,72.5,73.2,1644639,64.02,14.34,62.92,64.53,4.14
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 68.8
- over_600_ratio: 65.59
- over_800_ratio: 63.93
- over_1000_ratio: 60.84
- over_400_change_1w: 0.6
- over_800_change_1w: -0.32
- over_1000_change_1w: -1.33
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,68.52,0.26,64.54,-0.15,61.4,-0.69,1,False,False
20260612,68.9,0.38,64.01,-0.53,61.41,0.01,2,False,True
20260618,68.63,-0.27,64.46,0.45,60.84,-0.57,3,False,True
20260626,68.41,-0.22,64.44,-0.02,60.84,0,0,False,False
20260703,68.67,0.26,64.43,-0.01,60.84,0,1,False,False
20260709,68.61,-0.06,63.94,-0.49,60.84,0,0,False,False
20260717,68.69,0.08,64.15,0.21,61.59,0.75,1,False,True
20260724,68.06,-0.63,64.17,0.02,61.62,0.03,2,False,True
20260731,68.47,0.41,64.17,0,61.62,0,3,False,False
20260807,68.83,0.36,64.72,0.55,61.64,0.02,4,True,True
20260814,68.2,-0.63,64.25,-0.47,62.17,0.53,5,False,True
20260821,68.8,0.6,63.93,-0.32,60.84,-1.33,6,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2723 | 美食-KY | true_breakout | 嚴格突破 | 144.0 |  |  | breakout_confirmed |  |  | first_seen | 1.提報董事會或經董事會決議日期:115/08/20 2.審計委員會通過日期:115/08/19 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元): 8,259,172 5.1月1日累計至本期止營業毛利(毛損) (仟元): 5,069,817 6.1月1日累計至本期止營業利益(損失) (仟元): 746,107 7.1月1日累計至本期止稅前淨利(淨損) (仟元): 809,807 8.1月1日累計至本期止本期淨利(淨損) (仟元): 584,645 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元): 574,918 10.1月1日累計至本期止基本每股盈餘(損失) (元): 3.19 11.期末總資產(仟元): 17,622,690 12.期末總負債(仟元): 6,876,235 13.期末歸屬於母公司業主之權益(仟元): 10,743,208 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2723 | 美食-KY | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
