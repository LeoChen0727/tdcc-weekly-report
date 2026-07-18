# INDIVIDUAL STOCK CHATGPT PACKET - 2637 慧洋-KY

## Metadata
- generated_at: 2026-07-18 21:44:09 Asia/Taipei
- stock_id: 2637
- stock_name: 慧洋-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 11
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2637_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2637_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2637.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2637.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2637.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2637.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2637_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2637_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2637_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when tdcc_rows >= 8 and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260717
- open: 81.6
- high: 81.9
- low: 79.2
- close: 79.4
- volume: 2795263
- ma5: 82.86
- ema23_primary: 78.7
- distance_to_ema23_pct: 0.89
- ma20: 77.61
- ma60: 75.97
- ma120: 73.34
- return_5d: -4.34
- return_20d: 2.58
- volume_ratio: 0.83
- distance_to_ma20_pct_auxiliary: 2.31
- distance_to_high_60_pct: -9.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,76.8,77.4,75.4,77.4,5408866,76.9,0.65,77.25,73.72,0.82
20260622,77.9,77.9,76.3,77.1,2003159,76.92,0.24,77.55,73.85,0.3
20260623,77.3,77.4,76.2,76.8,2241864,76.91,-0.14,77.64,73.95,0.35
20260624,76.7,76.8,75.1,75.7,2701575,76.81,-1.44,77.68,74.07,0.42
20260625,76,76.3,75.4,76.1,2628435,76.75,-0.84,77.69,74.19,0.42
20260626,75.6,75.9,71.6,71.7,4074745,76.33,-6.06,77.44,74.24,0.66
20260629,72.4,73.1,70.9,72.6,2266513,76.02,-4.49,77.31,74.33,0.37
20260630,72.9,73.3,72.2,72.6,1918775,75.73,-4.13,77,74.39,0.32
20260701,73.6,73.6,71,71.4,2559954,75.37,-5.27,76.72,74.45,0.44
20260702,71.2,72.2,70.8,71.7,1553717,75.06,-4.48,76.45,74.51,0.28
20260703,71.7,74.4,71.7,74.3,2188340,75,-0.93,76.26,74.59,0.41
20260706,76.9,78.9,76.1,78.4,3836505,75.28,4.14,76.15,74.72,0.81
20260707,77.8,79.7,77.8,79,4476071,75.59,4.51,76.17,74.87,1.01
20260708,79.1,81.4,79.1,80,4023583,75.96,5.32,76.13,75.03,0.98
20260709,80,83,79.4,83,7993726,76.55,8.43,76.48,75.24,2.02
20260713,83.4,88,82.5,84.7,6524259,77.23,9.68,76.8,75.44,1.67
20260714,86.6,86.6,81.5,83.8,4025402,77.77,7.75,77.06,75.6,1.06
20260715,84.8,84.8,82.9,83.9,2000477,78.28,7.17,77.3,75.73,0.55
20260716,84.2,84.2,82.1,82.5,1727406,78.64,4.91,77.5,75.9,0.5
20260717,81.6,81.9,79.2,79.4,2795263,78.7,0.89,77.61,75.97,0.83
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 82.48
- over_600_ratio: 80.77
- over_800_ratio: 79.12
- over_1000_ratio: 77.95
- over_400_change_1w: 1.52
- over_800_change_1w: 1.68
- over_1000_change_1w: 1.95
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.24,,76.52,,75.35,,0,False,False
20260508,81.02,0.78,77.13,0.61,75.94,0.59,1,True,True
20260515,80.87,-0.15,76.95,-0.18,75.76,-0.18,0,False,False
20260522,80.69,-0.18,76.72,-0.23,75.18,-0.58,0,False,False
20260529,81.11,0.42,77.47,0.75,75.81,0.63,1,True,True
20260605,81.35,0.24,77.48,0.01,76.4,0.59,2,True,True
20260612,81.61,0.26,78.03,0.55,76.96,0.56,3,True,True
20260618,81.48,-0.13,78.07,0.04,76.76,-0.2,4,False,True
20260626,81.29,-0.19,77.76,-0.31,76.45,-0.31,0,False,False
20260703,80.96,-0.33,77.44,-0.32,76,-0.45,0,False,False
20260717,82.48,1.52,79.12,1.68,77.95,1.95,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2637 | 慧洋-KY | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | stale_signal | 1. 原公告日期： 114/03/17 2. 簡述原公告申報內容： 董事會核准購置內海造船株式會社建造之二艘高規格散裝貨輪案 交易數量：39,000噸散裝貨輪二艘 單位價格：不高於USD 35,375,000 交易總金額：不高於USD 70,750,000 3. 變動緣由及主要內容： 原公告取得資產案因雙方未達共識故終止。 4. 變動後對公司財務業務之影響： 因尚未簽訂契約及支付款項，故對本公司財務業務無重大影響。 5. 其他應敘明事項： 無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2637 | 慧洋-KY | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | stale_signal | 1. 原公告日期： 114/03/17 2. 簡述原公告申報內容： 董事會核准購置內海造船株式會社建造之二艘高規格散裝貨輪案 交易數量：39,000噸散裝貨輪二艘 單位價格：不高於USD 35,375,000 交易總金額：不高於USD 70,750,000 3. 變動緣由及主要內容： 原公告取得資產案因雙方未達共識故終止。 4. 變動後對公司財務業務之影響： 因尚未簽訂契約及支付款項，故對本公司財務業務無重大影響。 5. 其他應敘明事項： 無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 2637 | 慧洋-KY | revenue_breakout_low_response | 營收爆發低反應股 | 14.0 | 32.0 | D_降級_TDCC轉弱 |  |  | call_inflow | stale_signal | 1. 原公告日期： 114/03/17 2. 簡述原公告申報內容： 董事會核准購置內海造船株式會社建造之二艘高規格散裝貨輪案 交易數量：39,000噸散裝貨輪二艘 單位價格：不高於USD 35,375,000 交易總金額：不高於USD 70,750,000 3. 變動緣由及主要內容： 原公告取得資產案因雙方未達共識故終止。 4. 變動後對公司財務業務之影響： 因尚未簽訂契約及支付款項，故對本公司財務業務無重大影響。 5. 其他應敘明事項： 無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2637 | 慧洋-KY | 11 | 3 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2637 | 慧洋-KY | 22 | 0 | 1136400.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
