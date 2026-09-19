# INDIVIDUAL STOCK CHATGPT PACKET - 2542 興富發

## Metadata
- generated_at: 2026-09-19 15:52:48 Asia/Taipei
- stock_id: 2542
- stock_name: 興富發
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2542_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2542_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2542.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2542.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2542.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2542.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2542_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2542_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2542_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
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
- open: 48.8
- high: 48.9
- low: 47.15
- close: 47.8
- volume: 25349766
- ma5: 46.3
- ema23_primary: 46.84
- distance_to_ema23_pct: 2.05
- ma20: 47.33
- ma60: 45.39
- ma120: 42.95
- return_5d: 2.8
- return_20d: -2.05
- volume_ratio: 2.95
- distance_to_ma20_pct_auxiliary: 0.99
- distance_to_high_60_pct: -2.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,48.8,48.85,48.05,48.3,7277704,45.89,5.26,45.47,44.24,0.86
20260825,48,48.2,47.1,47.5,7128783,46.02,3.21,45.7,44.34,0.84
20260826,47.5,48,47.25,48,5420281,46.19,3.92,45.94,44.43,0.64
20260827,48,48.1,47.4,47.75,3370771,46.32,3.09,46.1,44.52,0.42
20260828,47.7,47.7,46.95,47,5444582,46.37,1.35,46.26,44.58,0.69
20260831,46.9,47.15,46.5,46.65,5554761,46.4,0.54,46.4,44.64,0.69
20260901,46.55,48,46.55,47.9,8094788,46.52,2.96,46.58,44.72,1.01
20260902,47.55,48,47.55,47.95,4263041,46.64,2.81,46.78,44.82,0.53
20260903,48,48.75,47.85,48.65,10377793,46.81,3.93,47.01,44.91,1.24
20260904,48.65,48.75,48.1,48.55,6938993,46.95,3.4,47.22,44.97,0.82
20260907,48.55,48.55,47.6,48,7664867,47.04,2.04,47.4,45.01,0.89
20260908,48,48,47.55,47.7,4033278,47.1,1.28,47.56,45.06,0.47
20260909,47.55,48.35,47.45,48.2,8134795,47.19,2.14,47.73,45.1,0.94
20260910,47.7,47.9,46.4,46.5,13798859,47.13,-1.34,47.73,45.13,1.62
20260911,46,46.85,46,46.5,6255442,47.08,-1.23,47.75,45.14,0.75
20260914,46.3,46.35,45.25,45.7,8970322,46.96,-2.69,47.69,45.16,1.09
20260915,45.6,45.6,44.85,45.25,9711683,46.82,-3.35,47.57,45.2,1.23
20260916,45.45,46.15,45.1,45.9,11786811,46.74,-1.81,47.45,45.26,1.51
20260917,46.2,47,45.8,46.85,12055585,46.75,0.21,47.38,45.32,1.53
20260918,48.8,48.9,47.15,47.8,25349766,46.84,2.05,47.33,45.39,2.95
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 65.96
- over_600_ratio: 64.66
- over_800_ratio: 63.37
- over_1000_ratio: 62.69
- over_400_change_1w: -0.19
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.14
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,62.27,-0.42,59.4,-0.62,58.56,-0.5,0,False,False
20260709,62.81,0.54,59.89,0.49,59.13,0.57,1,True,True
20260717,63.06,0.25,60.19,0.3,59.43,0.3,2,True,True
20260724,64.01,0.95,61.16,0.97,60.4,0.97,3,True,True
20260731,64.38,0.37,61.59,0.43,60.62,0.22,4,True,True
20260807,64.47,0.09,61.72,0.13,60.88,0.26,5,True,True
20260814,65.14,0.67,62.32,0.6,61.56,0.68,6,True,True
20260821,65.96,0.82,63.23,0.91,62.55,0.99,7,True,True
20260828,66.27,0.31,63.56,0.33,62.83,0.28,8,True,True
20260904,66.39,0.12,63.67,0.11,63.06,0.23,9,True,True
20260911,66.15,-0.24,63.39,-0.28,62.83,-0.23,0,False,False
20260918,65.96,-0.19,63.37,-0.02,62.69,-0.14,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2542 | 興富發 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | continued_2_3d | 1.契約種類:工程發包契約 2.事實發生日:115/9/17~115/9/17 3.董事會通過日期: 民國115年9月17日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 日商華大成營造工程股份有限公司，非關係人 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 「台中市西屯區惠國段88地號」工程發包金額為新台幣537,800,367元(含稅) 契約起迄日期：自簽約日起至全案工程完工日止 限制條款及其他重要約定事項：無 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 增加公司營業收入 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 不適用，非關係人交易 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2542 | 興富發 | 2 | 2 | 3 | 8 | 18 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2542 | 興富發 | 10 | 0 | 1225740.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
