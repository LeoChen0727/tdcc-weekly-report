# INDIVIDUAL STOCK CHATGPT PACKET - 6129 普誠

## Metadata
- generated_at: 2026-08-01 22:28:13 Asia/Taipei
- stock_id: 6129
- stock_name: 普誠
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6129_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6129_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6129_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6129_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6129_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6129_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6129_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6129_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6129_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6129_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6129_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6129_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6129.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6129.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6129.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6129.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6129_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6129_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6129_latest.md?ref=main

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
- date: 20260730
- open: 13.6
- high: 13.7
- low: 13.05
- close: 13.2
- volume: 586000
- ma5: 14.13
- ema23_primary: 15.89
- distance_to_ema23_pct: -16.95
- ma20: 16.64
- ma60: 16.45
- ma120: 16.12
- return_5d: -12.87
- return_20d: -27.87
- volume_ratio: 0.35
- distance_to_ma20_pct_auxiliary: -20.65
- distance_to_high_60_pct: -37.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,18.05,20.1,18.05,20,4681000,17.35,15.27,16.97,16.51,2.65
20260703,19.45,19.65,18.85,19.15,3092000,17.5,9.42,17.09,16.57,1.61
20260706,19.15,21.05,19.05,20.85,5867000,17.78,17.27,17.32,16.66,2.65
20260707,20.15,20.15,18.8,18.9,4826000,17.87,5.74,17.49,16.71,2.01
20260708,19.15,19.2,18.1,18.65,1482000,17.94,3.97,17.64,16.75,0.6
20260709,18.65,19.05,18.5,19,1298000,18.03,5.4,17.83,16.8,0.52
20260713,18.6,19.25,17.7,18,1605000,18.02,-0.14,17.98,16.83,0.63
20260714,18,18.15,16.45,17.3,1330000,17.96,-3.7,18.08,16.85,0.52
20260715,17.4,17.5,17.2,17.3,725000,17.91,-3.4,18.16,16.87,0.28
20260716,17.3,17.3,16.6,16.65,844000,17.8,-6.48,18.2,16.87,0.33
20260717,16.35,16.35,15.25,15.35,1543000,17.6,-12.78,18.16,16.83,0.59
20260720,15.55,15.65,14.7,15.15,686000,17.4,-12.91,18.13,16.79,0.26
20260721,15.3,15.6,15.2,15.25,574000,17.22,-11.42,18.04,16.76,0.23
20260722,15.25,15.55,15.25,15.35,529000,17.06,-10.03,17.95,16.73,0.21
20260723,15.4,15.45,15,15.15,530000,16.9,-10.36,17.76,16.7,0.23
20260724,15.15,15.35,14.95,15,624000,16.74,-10.41,17.53,16.67,0.33
20260727,14.95,14.95,14.6,14.8,497000,16.58,-10.74,17.34,16.64,0.28
20260728,14.8,14.8,14.05,14.05,706000,16.37,-14.17,17.12,16.59,0.41
20260729,14.05,14.1,13,13.6,1103000,16.14,-15.73,16.89,16.53,0.65
20260730,13.6,13.7,13.05,13.2,586000,15.89,-16.95,16.64,16.45,0.35
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 17.06
- over_600_ratio: 15.21
- over_800_ratio: 14.04
- over_1000_ratio: 14.04
- over_400_change_1w: -0.4
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.15
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,17.31,0.53,14.4,0.48,13.43,0,2,False,True
20260522,16.71,-0.6,13.92,-0.48,13.43,0,0,False,False
20260529,16.95,0.24,13.92,0,13.43,0,1,False,False
20260605,16.44,-0.51,13.92,0,13.43,0,0,False,False
20260612,16.1,-0.34,13.92,0,13.43,0,0,False,False
20260618,16.38,0.28,13.92,0,13.43,0,1,False,False
20260626,17.16,0.78,15.06,1.14,14.03,0.6,2,True,True
20260703,17.99,0.83,14.96,-0.1,14.96,0.93,3,False,True
20260709,17.18,-0.81,14.99,0.03,14.44,-0.52,4,False,True
20260717,17.32,0.14,14.44,-0.55,14.44,0,5,False,False
20260724,17.46,0.14,14.19,-0.25,14.19,-0.25,6,False,False
20260731,17.06,-0.4,14.04,-0.15,14.04,-0.15,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6129 | 普誠 | revenue_pullback | 營收成長股價回檔 | 67.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期:NA 2.減資基準日:115/07/17 3.減資換發股票作業計畫:本公司於民國115年6月16日股東會決議通過辦理減資彌補虧 損案，業經證券櫃檯買賣中心民國115年7月16日證櫃監字第1150004330號函申報生效 在案；惟本次減資換發股票作業計畫，待辦理變更登記完成後，另行公告之。 4.換發股票基準日:NA 5.停止過戶起始日期:NA 6.停止過戶截止日期:NA 7.減資後新股權利義務:NA 8.新股預計上櫃日:NA 9.預計減資新股上櫃後之上櫃普通股股數:160,574,120股 10.預計減資新股上櫃後之上櫃普通股股數占已發行普通股比 率（減資後上櫃普通股股數/減資後已發行普通股股數）:100% 11.前二項預計減資後上櫃普通股股數未達500萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用 12.其他應敘明事項: (1)本公司於民國115年6月16日經股東常會決議通過減資彌補虧損案，並授權董事長 訂定減資基準日。俟呈奉經濟部核准減資變更登記後，授權董事長全權處理減資換 發股票作業計畫申請，並訂定減資換發股票基準日及新股預計上市買賣日等相關事 宜及另行公告。 (2)證券櫃檯買賣中心民國115年7月16日證櫃監字第1150004330號函申報生效。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6129 | 普誠 | 1 | 1 | 3 | 8 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
