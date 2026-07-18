# INDIVIDUAL STOCK CHATGPT PACKET - 3704 合勤控

## Metadata
- generated_at: 2026-07-18 23:38:30 Asia/Taipei
- stock_id: 3704
- stock_name: 合勤控
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
- open: 44.9
- high: 46.9
- low: 44.8
- close: 45.7
- volume: 4787968
- ma5: 48.13
- ema23_primary: 46.44
- distance_to_ema23_pct: -1.6
- ma20: 46.73
- ma60: 43.02
- ma120: 38.76
- return_5d: 0.77
- return_20d: -7.4
- volume_ratio: 0.87
- distance_to_ma20_pct_auxiliary: -2.21
- distance_to_high_60_pct: -11.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,49.35,49.6,48.15,48.25,5001868,45.24,6.65,46.65,39.2,0.73
20260622,48.6,48.95,47.15,48.5,3368218,45.51,6.56,46.87,39.47,0.53
20260623,49,51.4,48.8,49.7,7683558,45.86,8.37,47.18,39.75,1.22
20260624,49.15,49.7,47.6,48.6,3701713,46.09,5.44,47.35,40.01,0.62
20260625,49,49,47.4,47.7,2388889,46.23,3.19,47.47,40.26,0.42
20260626,47.7,47.7,42.95,43,6807465,45.96,-6.43,47.35,40.42,1.21
20260629,43.7,45.85,43.5,45.25,4248331,45.9,-1.41,47.3,40.63,0.77
20260630,45.8,48.1,45.4,46.55,9139860,45.95,1.3,47.28,40.86,1.6
20260701,46.55,46.55,43.6,44.25,4968105,45.81,-3.41,47.1,41.05,0.89
20260702,44.25,45,43.75,44.85,1607289,45.73,-1.92,46.89,41.26,0.3
20260703,44.95,47.7,44.8,46.95,4775445,45.83,2.44,46.85,41.47,0.9
20260706,47.4,47.8,44.85,44.85,4073225,45.75,-1.97,46.71,41.64,0.78
20260707,46.55,46.55,44.35,44.85,3319181,45.67,-1.81,46.62,41.83,0.66
20260708,45.25,45.8,44,45.35,2012156,45.65,-0.65,46.44,41.98,0.41
20260709,46,46.35,45.1,45.35,1401803,45.62,-0.6,46.45,42.13,0.31
20260713,48,49.85,47.95,49.85,16834669,45.98,8.43,46.65,42.35,3.24
20260714,50.3,50.9,46.9,48.65,13166775,46.2,5.31,46.81,42.55,2.33
20260715,49.45,50.3,47.85,49.8,5998799,46.5,7.1,46.92,42.75,1.04
20260716,49.4,49.4,46.35,46.65,4262399,46.51,0.3,46.91,42.9,0.74
20260717,44.9,46.9,44.8,45.7,4787968,46.44,-1.6,46.73,43.02,0.87
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 66.3
- over_600_ratio: 63.24
- over_800_ratio: 61.44
- over_1000_ratio: 60.35
- over_400_change_1w: 0.47
- over_800_change_1w: 0.21
- over_1000_change_1w: 0.87
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,56.67,,51.76,,50.67,,0,False,False
20260508,56.74,0.07,51.83,0.07,50.27,-0.4,1,False,True
20260515,57.54,0.8,52.33,0.5,51.04,0.77,2,True,True
20260522,60.11,2.57,55.49,3.16,53.96,2.92,3,True,True
20260529,62.39,2.28,57.92,2.43,56.84,2.88,4,True,True
20260605,64.41,2.02,60.24,2.32,58.92,2.08,5,True,True
20260612,65.5,1.09,60.89,0.65,59.55,0.63,6,True,True
20260618,65.93,0.43,61.64,0.75,59.87,0.32,7,True,True
20260626,66.14,0.21,62.06,0.42,60.1,0.23,8,True,True
20260703,65.83,-0.31,61.23,-0.83,59.48,-0.62,0,False,False
20260717,66.3,0.47,61.44,0.21,60.35,0.87,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3704 | 合勤控 | pattern | 型態觀察 | 40.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會決議或公司決定日期:115/06/30 2.發行股數:27,500,000股。 3.每股面額:新台幣10元。 4.發行總金額:新台幣275,000,000元。 5.發行價格:新台幣10元。 6.員工認股股數:發行股數之10%,即2,750,000股。 7.原股東認購比率:發行股數之90%,即24,750,000股。 8.公開銷售方式及股數:不適用。 9.畸零股及逾期未認購股份之處理方式:不適用。 10.本次發行新股之權利義務:其權利義務與原已發行股份相同。 11.本次增資資金用途:充實營運資金。 12.現金增資認股基準日:115/07/05 13.最後過戶日:115/06/30 14.停止過戶起始日期:115/07/01 15.停止過戶截止日期:115/07/05 16.股款繳納期間:原股東及員工之股款繳納日為民國115年07月06日   ；特定人認股繳款日訂為民國115年07月07日。 17.與代收及專戶存儲價款行庫訂約日期:不適用。 18.委託代收存款機構:不適用。 19.委託存儲款項機構:不適用。 20.其他應敘明事項:因應現增作業實際發行情形，本現金增資   案內容及其他相關事宜，如經主管機關修正、或有未盡事宜   、或因客觀環境而變更時，擬授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 3704 | 合勤控 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.董事會決議或公司決定日期:115/06/30 2.發行股數:27,500,000股。 3.每股面額:新台幣10元。 4.發行總金額:新台幣275,000,000元。 5.發行價格:新台幣10元。 6.員工認股股數:發行股數之10%,即2,750,000股。 7.原股東認購比率:發行股數之90%,即24,750,000股。 8.公開銷售方式及股數:不適用。 9.畸零股及逾期未認購股份之處理方式:不適用。 10.本次發行新股之權利義務:其權利義務與原已發行股份相同。 11.本次增資資金用途:充實營運資金。 12.現金增資認股基準日:115/07/05 13.最後過戶日:115/06/30 14.停止過戶起始日期:115/07/01 15.停止過戶截止日期:115/07/05 16.股款繳納期間:原股東及員工之股款繳納日為民國115年07月06日   ；特定人認股繳款日訂為民國115年07月07日。 17.與代收及專戶存儲價款行庫訂約日期:不適用。 18.委託代收存款機構:不適用。 19.委託存儲款項機構:不適用。 20.其他應敘明事項:因應現增作業實際發行情形，本現金增資   案內容及其他相關事宜，如經主管機關修正、或有未盡事宜   、或因客觀環境而變更時，擬授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3704 | 合勤控 | 7 | 2 | 5 | 8 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
