# INDIVIDUAL STOCK CHATGPT PACKET - 3704 合勤控

## Metadata
- generated_at: 2026-09-26 15:52:08 Asia/Taipei
- stock_id: 3704
- stock_name: 合勤控
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3704_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3704_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3704_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3704_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3704_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3704_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3704_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3704_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3704_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3704_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3704_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3704_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3704.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3704.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3704.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3704.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3704_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3704_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3704_latest.md?ref=main

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
- date: 20260924
- open: 40.3
- high: 40.75
- low: 40
- close: 40.5
- volume: 1010185
- ma5: 41.08
- ema23_primary: 41.11
- distance_to_ema23_pct: -1.48
- ma20: 40.62
- ma60: 43.42
- ma120: 42.24
- return_5d: 0.5
- return_20d: -4.59
- volume_ratio: 0.38
- distance_to_ma20_pct_auxiliary: -0.28
- distance_to_high_60_pct: -20.43

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,42.75,43.15,42,42,1259249,43.33,-3.07,43.85,45.46,0.36
20260831,42,43.6,41.65,41.65,2132609,43.19,-3.57,43.67,45.36,0.61
20260901,41.7,42.3,41.4,41.7,1325634,43.07,-3.17,43.46,45.26,0.4
20260902,41.65,42.4,41.55,42.1,804864,42.99,-2.06,43.12,45.18,0.26
20260903,42.1,42.75,40,40,3368025,42.74,-6.4,42.76,45.03,1.06
20260904,41.15,41.15,39.5,40.1,2882332,42.52,-5.68,42.48,44.95,0.9
20260907,40.4,40.65,39.4,39.7,1402668,42.28,-6.11,41.94,44.85,0.52
20260908,39.8,40.15,38.9,38.9,1557833,42,-7.38,41.62,44.74,0.67
20260909,39,39.6,39,39.4,569510,41.78,-5.7,41.45,44.6,0.28
20260910,39.45,39.6,39.05,39.4,667187,41.58,-5.25,41.33,44.48,0.35
20260911,39,40.75,38.85,40.5,3177682,41.49,-2.4,41.16,44.33,1.71
20260914,40.4,41.6,40.1,41.2,3075562,41.47,-0.65,41.06,44.22,1.68
20260915,41.9,42.4,39.7,39.8,10631775,41.33,-3.7,40.98,44.07,4.88
20260916,39.95,40.95,39.9,40.15,2536945,41.23,-2.62,40.91,43.91,1.15
20260917,40.5,40.9,39.75,40.3,3611889,41.15,-2.08,40.81,43.77,1.56
20260918,40.6,41.2,40.35,41.15,2036622,41.15,-0.01,40.79,43.66,0.88
20260921,41.3,42.35,40.55,42.15,3288841,41.24,2.21,40.8,43.65,1.36
20260922,42.5,42.6,40.85,41.3,5363474,41.24,0.14,40.8,43.58,2.05
20260923,41.15,41.3,40.25,40.3,1884275,41.16,-2.1,40.71,43.48,0.71
20260924,40.3,40.75,40,40.5,1010185,41.11,-1.48,40.62,43.42,0.38
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 64.85
- over_600_ratio: 61.27
- over_800_ratio: 59.49
- over_1000_ratio: 57.96
- over_400_change_1w: 0.08
- over_800_change_1w: -0.48
- over_1000_change_1w: -0.72
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,65.86,0.03,60.82,-0.41,59.51,0.03,1,False,True
20260717,66.3,0.44,61.44,0.62,60.35,0.84,2,True,True
20260724,66.89,0.59,61.59,0.15,60.3,-0.05,3,False,True
20260731,66.85,-0.04,61.51,-0.08,60.02,-0.28,4,False,False
20260807,67.6,0.75,62.38,0.87,60.89,0.87,5,True,True
20260814,67.13,-0.47,62.22,-0.16,60.73,-0.16,0,False,False
20260821,66.69,-0.44,61.23,-0.99,59.72,-1.01,0,False,False
20260828,66.27,-0.42,61.31,0.08,59.15,-0.57,1,False,True
20260904,66.04,-0.23,61.25,-0.06,59.52,0.37,2,False,True
20260911,65.68,-0.36,61.36,0.11,59.41,-0.11,3,False,True
20260918,64.77,-0.91,59.97,-1.39,58.68,-0.73,0,False,False
20260924,64.85,0.08,59.49,-0.48,57.96,-0.72,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3704 | 合勤控 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.董事會決議或公司決定日期:115/06/30 2.發行股數:27,500,000股。 3.每股面額:新台幣10元。 4.發行總金額:新台幣275,000,000元。 5.發行價格:新台幣10元。 6.員工認股股數:發行股數之10%,即2,750,000股。 7.原股東認購比率:發行股數之90%,即24,750,000股。 8.公開銷售方式及股數:不適用。 9.畸零股及逾期未認購股份之處理方式:不適用。 10.本次發行新股之權利義務:其權利義務與原已發行股份相同。 11.本次增資資金用途:充實營運資金。 12.現金增資認股基準日:115/07/05 13.最後過戶日:115/06/30 14.停止過戶起始日期:115/07/01 15.停止過戶截止日期:115/07/05 16.股款繳納期間:原股東及員工之股款繳納日為民國115年07月06日   ；特定人認股繳款日訂為民國115年07月07日。 17.與代收及專戶存儲價款行庫訂約日期:不適用。 18.委託代收存款機構:不適用。 19.委託存儲款項機構:不適用。 20.其他應敘明事項:因應現增作業實際發行情形，本現金增資   案內容及其他相關事宜，如經主管機關修正、或有未盡事宜   、或因客觀環境而變更時，擬授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3704 | 合勤控 | 8 | 8 | 5 | 8 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3704 | 合勤控 | 7 | 0 | 45910.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
