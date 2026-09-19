# INDIVIDUAL STOCK CHATGPT PACKET - 6525 捷敏-KY

## Metadata
- generated_at: 2026-09-19 22:17:21 Asia/Taipei
- stock_id: 6525
- stock_name: 捷敏-KY
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6525_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6525_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6525_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6525_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6525_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6525_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6525_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6525_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6525_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6525_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6525_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6525_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6525.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6525.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6525.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6525.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6525_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6525_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6525_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260918
- open: 131
- high: 136
- low: 130.5
- close: 135.5
- volume: 1517543
- ma5: 129.3
- ema23_primary: 134.4
- distance_to_ema23_pct: 0.82
- ma20: 134.43
- ma60: 147.76
- ma120: 128.44
- return_5d: 8.84
- return_20d: -1.81
- volume_ratio: 1.42
- distance_to_ma20_pct_auxiliary: 0.8
- distance_to_high_60_pct: -38.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,137,144,137,137,915029,143.25,-4.37,136.6,146.81,0.39
20260825,135.5,136.5,130.5,136,1108103,142.65,-4.66,137,147.03,0.49
20260826,136.5,143,135.5,141.5,1417728,142.55,-0.74,138.05,147.38,0.64
20260827,145,145,139,141.5,1112062,142.47,-0.68,139.53,147.74,0.52
20260828,143,150,143,144.5,2348123,142.64,1.31,140.6,148.15,1.06
20260831,143.5,143.5,138,139.5,1154281,142.37,-2.02,141.2,148.48,0.54
20260901,142,145.5,141.5,143,1087296,142.43,0.4,141.55,148.85,0.53
20260902,141,143,137,137,1084722,141.97,-3.5,141.65,149.15,0.55
20260903,138.5,142,135.5,135.5,1236719,141.43,-4.2,141.47,149.43,0.64
20260904,139.5,140.5,136,138,774279,141.15,-2.23,141.6,149.82,0.42
20260907,140,140.5,133,133.5,1269531,140.51,-4.99,141.18,150.11,0.7
20260908,135,136,129.5,130.5,989725,139.68,-6.57,140.68,150.19,0.56
20260909,132.5,132.5,129.5,130.5,815493,138.91,-6.06,140.05,150.18,0.47
20260910,130.5,131,129,129.5,667173,138.13,-6.25,139,150.22,0.42
20260911,126.5,127,124.5,124.5,891252,136.99,-9.12,137.97,150.12,0.59
20260914,123,130.5,119,128,915342,136.24,-6.05,137,149.88,0.61
20260915,126,130,125.5,125.5,531566,135.35,-7.28,135.88,149.38,0.42
20260916,126.5,130,125,128.5,840308,134.78,-4.66,135.18,148.68,0.74
20260917,129.5,130.5,128.5,129,672942,134.3,-3.94,134.55,148.07,0.64
20260918,131,136,130.5,135.5,1517543,134.4,0.82,134.43,147.76,1.42
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 67.84
- over_600_ratio: 64.27
- over_800_ratio: 60.51
- over_1000_ratio: 59.06
- over_400_change_1w: 0.31
- over_800_change_1w: -0.56
- over_1000_change_1w: 0.13
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,66.84,1.55,59.34,0.8,57.89,0.8,2,True,True
20260709,69.57,2.73,59.25,-0.09,57.09,-0.8,3,False,False
20260717,69.1,-0.47,59.86,0.61,57.09,0,4,False,True
20260724,69.19,0.09,62.64,2.78,60.5,3.41,5,True,True
20260731,69.54,0.35,61.38,-1.26,59.93,-0.57,6,False,False
20260807,69.66,0.12,61.08,-0.3,59,-0.93,7,False,False
20260814,68.42,-1.24,61.72,0.64,58.83,-0.17,8,False,True
20260821,67.86,-0.56,60.33,-1.39,58.88,0.05,9,False,True
20260828,67.55,-0.31,60.42,0.09,58.97,0.09,10,False,True
20260904,67.47,-0.08,60.37,-0.05,58.92,-0.05,0,False,False
20260911,67.53,0.06,61.07,0.7,58.93,0.01,1,True,True
20260918,67.84,0.31,60.51,-0.56,59.06,0.13,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6525 | 捷敏-KY | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.公司名稱:捷敏股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:MoneyDJ理財網 6.報導內容:法人表示，受惠資料中心伺服器等相關功率元件訂單需求強勁 及傳統季節性備貨旺季來臨，目前公司稼動率達近9成水準，加上封測產能 吃緊、IDM大廠擴大委外釋單，在報價上也更具優勢。看好公司今年下半年 營收優於上半年，全年挑戰雙位數年增、創新高，EPS上看8元水準、創新高。 7.發生緣由:上述報導內容係屬該法人與媒體所做之推估，本公司營收及獲利狀況， 悉以公開資訊觀測站公佈之資料為準。 8.因應措施: (1)有關本公司之營運資訊，皆以公開資訊觀測站公告為主，特此說明。 (2)對於相關媒體之報導，請投資人審慎判斷，以保障自身權益。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6525 | 捷敏-KY | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.公司名稱:捷敏股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:MoneyDJ理財網 6.報導內容:法人表示，受惠資料中心伺服器等相關功率元件訂單需求強勁 及傳統季節性備貨旺季來臨，目前公司稼動率達近9成水準，加上封測產能 吃緊、IDM大廠擴大委外釋單，在報價上也更具優勢。看好公司今年下半年 營收優於上半年，全年挑戰雙位數年增、創新高，EPS上看8元水準、創新高。 7.發生緣由:上述報導內容係屬該法人與媒體所做之推估，本公司營收及獲利狀況， 悉以公開資訊觀測站公佈之資料為準。 8.因應措施: (1)有關本公司之營運資訊，皆以公開資訊觀測站公告為主，特此說明。 (2)對於相關媒體之報導，請投資人審慎判斷，以保障自身權益。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 6525 | 捷敏-KY | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.公司名稱:捷敏股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:MoneyDJ理財網 6.報導內容:法人表示，受惠資料中心伺服器等相關功率元件訂單需求強勁 及傳統季節性備貨旺季來臨，目前公司稼動率達近9成水準，加上封測產能 吃緊、IDM大廠擴大委外釋單，在報價上也更具優勢。看好公司今年下半年 營收優於上半年，全年挑戰雙位數年增、創新高，EPS上看8元水準、創新高。 7.發生緣由:上述報導內容係屬該法人與媒體所做之推估，本公司營收及獲利狀況， 悉以公開資訊觀測站公佈之資料為準。 8.因應措施: (1)有關本公司之營運資訊，皆以公開資訊觀測站公告為主，特此說明。 (2)對於相關媒體之報導，請投資人審慎判斷，以保障自身權益。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6525 | 捷敏-KY | 1 | 1 | 1 | 2 | 11 | repeated_but_no_breakout | 近 10 日上榜 2 次、近 20 日上榜 11 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6525 | 捷敏-KY | 29 | 0 | 2537100.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
