# INDIVIDUAL STOCK CHATGPT PACKET - 6525 捷敏-KY

## Metadata
- generated_at: 2026-08-22 22:28:36 Asia/Taipei
- stock_id: 6525
- stock_name: 捷敏-KY
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
- date: 20260821
- open: 141.5
- high: 142
- low: 137
- close: 138
- volume: 1204242
- ma5: 143.5
- ema23_primary: 143.82
- distance_to_ema23_pct: -4.05
- ma20: 136.85
- ma60: 146.57
- ma120: 119.74
- return_5d: -4.83
- return_20d: -2.47
- volume_ratio: 0.51
- distance_to_ma20_pct_auxiliary: 0.84
- distance_to_high_60_pct: -37.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,142,144,137.5,142,1970954,160.98,-11.79,171.8,138.38,0.4
20260728,136.5,136.5,128,128,2244662,158.24,-19.11,171.05,138.97,0.45
20260729,128,129,116.5,120.5,2708219,155.09,-22.3,169.53,139.38,0.54
20260730,119.5,122.5,110,112,2628170,151.5,-26.07,167.55,139.54,0.53
20260731,123,123,120.5,123,615337,149.13,-17.52,165.38,139.88,0.13
20260803,124,133.5,121,127.5,3104099,147.32,-13.46,162.6,140.18,0.7
20260804,127,138.5,126.5,136,2597190,146.38,-7.09,159.35,140.67,0.59
20260805,140,142.5,134.5,135,2771420,145.43,-7.17,155.05,141.09,0.66
20260806,134.5,140.5,131,139,1678675,144.9,-4.07,152.05,141.62,0.46
20260807,143.5,144,135,135.5,2909008,144.11,-5.98,148.85,142.11,0.87
20260810,139.5,143.5,138,142,1797015,143.94,-1.35,146.32,142.53,0.58
20260811,142,145,139.5,140.5,1839385,143.65,-2.19,144.28,143.12,0.63
20260812,142,145,141,143,1321514,143.6,-0.41,142,143.67,0.49
20260813,145,152,144,150.5,3753437,144.17,4.39,139.95,144.34,1.41
20260814,152.5,152.5,144,145,2211748,144.24,0.53,138.57,144.87,0.87
20260817,144.5,149,140.5,147.5,1328105,144.51,2.07,138.18,145.43,0.54
20260818,148,158,147,148,4913226,144.8,2.21,138.03,145.96,2.04
20260819,144,158,142,142.5,3654213,144.61,-1.46,137.4,146.3,1.51
20260820,145,149.5,141,141.5,2368182,144.35,-1.98,137.03,146.43,0.97
20260821,141.5,142,137,138,1204242,143.82,-4.05,136.85,146.57,0.51
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 67.86
- over_600_ratio: 64.56
- over_800_ratio: 60.33
- over_1000_ratio: 58.88
- over_400_change_1w: -0.56
- over_800_change_1w: -1.39
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,65.63,-1.37,59.23,-0.79,57.09,0,0,False,False
20260612,64.42,-1.21,58.54,-0.69,57.09,0,0,False,False
20260618,63.78,-0.64,58.54,0,57.09,0,0,False,False
20260626,65.29,1.51,58.54,0,57.09,0,1,False,False
20260703,66.84,1.55,59.34,0.8,57.89,0.8,2,True,True
20260709,69.57,2.73,59.25,-0.09,57.09,-0.8,3,False,False
20260717,69.1,-0.47,59.86,0.61,57.09,0,4,False,True
20260724,69.19,0.09,62.64,2.78,60.5,3.41,5,True,True
20260731,69.54,0.35,61.38,-1.26,59.93,-0.57,6,False,False
20260807,69.66,0.12,61.08,-0.3,59,-0.93,7,False,False
20260814,68.42,-1.24,61.72,0.64,58.83,-0.17,8,False,True
20260821,67.86,-0.56,60.33,-1.39,58.88,0.05,9,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6525 | 捷敏-KY | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:捷敏股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:MoneyDJ理財網 6.報導內容:法人表示，受惠資料中心伺服器等相關功率元件訂單需求強勁 及傳統季節性備貨旺季來臨，目前公司稼動率達近9成水準，加上封測產能 吃緊、IDM大廠擴大委外釋單，在報價上也更具優勢。看好公司今年下半年 營收優於上半年，全年挑戰雙位數年增、創新高，EPS上看8元水準、創新高。 7.發生緣由:上述報導內容係屬該法人與媒體所做之推估，本公司營收及獲利狀況， 悉以公開資訊觀測站公佈之資料為準。 8.因應措施: (1)有關本公司之營運資訊，皆以公開資訊觀測站公告為主，特此說明。 (2)對於相關媒體之報導，請投資人審慎判斷，以保障自身權益。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 6525 | 捷敏-KY | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/08/10 2.公司名稱:捷敏股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:MoneyDJ理財網 6.報導內容:法人表示，受惠資料中心伺服器等相關功率元件訂單需求強勁 及傳統季節性備貨旺季來臨，目前公司稼動率達近9成水準，加上封測產能 吃緊、IDM大廠擴大委外釋單，在報價上也更具優勢。看好公司今年下半年 營收優於上半年，全年挑戰雙位數年增、創新高，EPS上看8元水準、創新高。 7.發生緣由:上述報導內容係屬該法人與媒體所做之推估，本公司營收及獲利狀況， 悉以公開資訊觀測站公佈之資料為準。 8.因應措施: (1)有關本公司之營運資訊，皆以公開資訊觀測站公告為主，特此說明。 (2)對於相關媒體之報導，請投資人審慎判斷，以保障自身權益。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6525 | 捷敏-KY | 4 | 4 | 4 | 4 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6525 | 捷敏-KY | 26 | 0 | 1813740.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
