# INDIVIDUAL STOCK CHATGPT PACKET - 2027 大成鋼

## Metadata
- generated_at: 2026-09-05 22:15:44 Asia/Taipei
- stock_id: 2027
- stock_name: 大成鋼
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2027_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2027_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2027_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2027_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2027_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2027_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2027_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2027_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2027_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2027_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2027_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2027_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2027.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2027.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2027.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2027.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2027_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2027_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2027_latest.md?ref=main

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
- date: 20260904
- open: 50.7
- high: 50.8
- low: 49
- close: 50.2
- volume: 17349221
- ma5: 49.71
- ema23_primary: 48.45
- distance_to_ema23_pct: 3.61
- ma20: 49.31
- ma60: 44.44
- ma120: 41.78
- return_5d: 3.72
- return_20d: 7.73
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: 1.79
- distance_to_high_60_pct: -4.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,47.45,47.8,46.75,47.3,18613189,43.59,8.5,43.27,42.15,0.92
20260811,47.5,47.75,46,46.45,14988975,43.83,5.98,43.63,42.26,0.74
20260812,46.45,47.6,46.2,46.85,10107686,44.08,6.28,43.91,42.38,0.52
20260813,48.5,51.5,48,50.4,58730639,44.61,12.98,44.38,42.56,2.67
20260814,50,50,46.85,47.6,36686198,44.86,6.11,44.73,42.66,1.59
20260817,47.9,51.3,47.55,50,43019012,45.29,10.41,45.2,42.79,1.75
20260818,49.3,50.2,48.8,49.7,15806951,45.65,8.86,45.63,42.92,0.63
20260819,48.75,50.5,48.2,50,18075115,46.02,8.66,45.95,43.02,0.78
20260820,50,51.6,49.95,50.5,15981417,46.39,8.86,46.25,43.18,0.7
20260821,50.5,50.5,49.4,50.3,9436777,46.72,7.67,46.59,43.31,0.41
20260824,51,52.3,50.5,51,15833188,47.07,8.34,46.91,43.46,0.71
20260825,51.1,51.4,50.3,50.6,7980484,47.37,6.83,47.33,43.61,0.36
20260826,50.6,50.8,49.6,50,10774807,47.59,5.07,47.67,43.73,0.51
20260827,50,50.3,48.5,48.65,17970345,47.67,2.05,47.91,43.81,0.86
20260828,48.55,48.9,48.15,48.4,10383787,47.74,1.39,48.17,43.88,0.51
20260831,48.4,49.45,47.85,48.8,16409254,47.82,2.04,48.39,43.96,0.81
20260901,48.6,50.3,48.6,49.8,12934911,47.99,3.77,48.67,44.06,0.64
20260902,49.35,49.85,49.05,49.55,7500145,48.12,2.97,48.93,44.19,0.38
20260903,49.45,50.5,49.4,50.2,11064729,48.29,3.95,49.13,44.31,0.6
20260904,50.7,50.8,49,50.2,17349221,48.45,3.61,49.31,44.44,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 78.32
- over_600_ratio: 76.41
- over_800_ratio: 75.35
- over_1000_ratio: 74.38
- over_400_change_1w: 0.16
- over_800_change_1w: 0.21
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,73.93,-0.08,70.84,-0.12,69.9,-0.08,0,False,False
20260626,73.77,-0.16,70.65,-0.19,69.75,-0.15,0,False,False
20260703,73.91,0.14,70.69,0.04,69.79,0.04,1,True,True
20260709,73.95,0.04,70.74,0.05,69.84,0.05,2,True,True
20260717,74.27,0.32,71.02,0.28,70.17,0.33,3,True,True
20260724,75.45,1.18,72.24,1.22,71.38,1.21,4,True,True
20260731,75.73,0.28,72.68,0.44,71.86,0.48,5,True,True
20260807,76.61,0.88,73.57,0.89,72.78,0.92,6,True,True
20260814,77.72,1.11,74.77,1.2,73.97,1.19,7,True,True
20260821,78.2,0.48,75.26,0.49,74.61,0.64,8,True,True
20260828,78.16,-0.04,75.14,-0.12,74.38,-0.23,9,False,False
20260904,78.32,0.16,75.35,0.21,74.38,0,10,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2027 | 大成鋼 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/08/19 2.公司名稱:美國大成國際公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由:更正子公司美國大成國際公司115年6月衍生性商品交易資訊 6.更正資訊項目/報表名稱: 非持有供交易-不符避險會計/遠期契約 & 交換 7.更正前金額/內容/頁次: 遠期契約(單位：仟元)  未沖銷契約-契約總金額：0  未沖銷契約-公允價值：0  未沖銷契約-本年度認列未實現損益金額：0 交換(單位：仟元)  未沖銷契約-契約總金額：6,572,525  未沖銷契約-公允價值：164,397  未沖銷契約-本年度認列未實現損益金額：164,397 8.更正後金額/內容/頁次: 遠期契約(單位：仟元)  未沖銷契約-契約總金額：4,991,962  未沖銷契約-公允價值：88,211  未沖銷契約-本年度認列未實現損益金額：88,211 交換(單位：仟元)  未沖銷契約-契約總金額：1,580,563  未沖銷契約-公允價值：76,187  未沖銷契約-本年度認列未實現損益金額：76,187 9.因應措施:重新上傳至公開資訊觀測站。 10.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2027 | 大成鋼 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/08/19 2.公司名稱:美國大成國際公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由:更正子公司美國大成國際公司115年6月衍生性商品交易資訊 6.更正資訊項目/報表名稱: 非持有供交易-不符避險會計/遠期契約 & 交換 7.更正前金額/內容/頁次: 遠期契約(單位：仟元)  未沖銷契約-契約總金額：0  未沖銷契約-公允價值：0  未沖銷契約-本年度認列未實現損益金額：0 交換(單位：仟元)  未沖銷契約-契約總金額：6,572,525  未沖銷契約-公允價值：164,397  未沖銷契約-本年度認列未實現損益金額：164,397 8.更正後金額/內容/頁次: 遠期契約(單位：仟元)  未沖銷契約-契約總金額：4,991,962  未沖銷契約-公允價值：88,211  未沖銷契約-本年度認列未實現損益金額：88,211 交換(單位：仟元)  未沖銷契約-契約總金額：1,580,563  未沖銷契約-公允價值：76,187  未沖銷契約-本年度認列未實現損益金額：76,187 9.因應措施:重新上傳至公開資訊觀測站。 10.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2027 | 大成鋼 | 31 | 7 | 5 | 10 | 20 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 20 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2027 | 大成鋼 | 63 | 3 | 8788460.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
