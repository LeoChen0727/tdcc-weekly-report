# INDIVIDUAL STOCK CHATGPT PACKET - 6214 精誠

## Metadata
- generated_at: 2026-07-19 22:27:56 Asia/Taipei
- stock_id: 6214
- stock_name: 精誠
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6214_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6214_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6214_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6214_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6214_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6214_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6214_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6214_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6214_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6214_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6214_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6214_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6214.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6214.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6214.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6214.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6214_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6214_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6214_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260717
- open: 138
- high: 139.5
- low: 136
- close: 137
- volume: 1463916
- ma5: 139.9
- ema23_primary: 136.93
- distance_to_ema23_pct: 0.05
- ma20: 135.43
- ma60: 132.77
- ma120: 123.3
- return_5d: -4.53
- return_20d: -2.84
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: 1.16
- distance_to_high_60_pct: -15.43

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,142.5,143.5,140.5,142,2660556,138.54,2.5,140.43,126.17,0.96
20260622,143,143,139,141,4810505,138.74,1.63,140.97,126.71,1.68
20260623,135,136.5,129.5,130,4237140,138.01,-5.81,141.03,127.04,1.41
20260624,129.5,131,127.5,131,1401287,137.43,-4.68,141.1,127.41,0.46
20260625,131.5,131.5,129,129.5,889887,136.77,-5.31,141.12,127.76,0.3
20260626,129.5,131.5,127.5,128,1812744,136.04,-5.91,141.07,128.12,0.61
20260629,129,132,129,129,1218275,135.45,-4.76,140.97,128.52,0.41
20260630,130,136,130,134,2490700,135.33,-0.98,140.47,128.96,0.87
20260701,135,135,130,131,1741190,134.97,-2.94,139.12,129.35,0.63
20260702,132,134.5,132,132,1332446,134.72,-2.02,138.07,129.72,0.57
20260703,131,135.5,131,133.5,1455116,134.62,-0.83,137.25,130.09,0.67
20260706,134.5,137,134.5,136.5,1649328,134.78,1.28,136.85,130.45,0.78
20260707,136.5,136.5,133,133,1674593,134.63,-1.21,136.47,130.76,0.81
20260708,135,136.5,133.5,135,1058851,134.66,0.25,136.07,131.07,0.53
20260709,142,147,142,143.5,5156264,135.4,5.98,136.07,131.49,2.43
20260713,145.5,146,140,141,1857281,135.86,3.78,136.03,131.85,0.87
20260714,141,143,137.5,140.5,1793029,136.25,3.12,135.78,132.13,0.85
20260715,143,143,140,141,880516,136.65,3.19,135.68,132.38,0.43
20260716,141.5,142,139.5,140,1093501,136.93,2.25,135.62,132.61,0.54
20260717,138,139.5,136,137,1463916,136.93,0.05,135.43,132.77,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 56.55
- over_600_ratio: 52.76
- over_800_ratio: 49.22
- over_1000_ratio: 45.29
- over_400_change_1w: 1.43
- over_800_change_1w: 0.4
- over_1000_change_1w: -0.22
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.15,,48.65,,45.3,,0,False,False
20260508,54.98,-0.17,48.91,0.26,46.27,0.97,1,False,True
20260515,55.39,0.41,48.88,-0.03,46.25,-0.02,2,False,False
20260522,55.57,0.18,49,0.12,46.01,-0.24,3,False,True
20260529,56.39,0.82,49.58,0.58,46.6,0.59,4,True,True
20260605,57.74,1.35,50.56,0.98,47.96,1.36,5,True,True
20260612,58.19,0.45,50.57,0.01,47.94,-0.02,6,False,True
20260618,57.08,-1.11,50.07,-0.5,47.46,-0.48,0,False,False
20260626,56.05,-1.03,49.12,-0.95,46.14,-1.32,0,False,False
20260703,55.63,-0.42,48.9,-0.22,45.61,-0.53,0,False,False
20260709,55.12,-0.51,48.82,-0.08,45.51,-0.1,0,False,False
20260717,56.55,1.43,49.22,0.4,45.29,-0.22,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6214 | 精誠 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.董事會決議或公司決定日期:115/07/09 2.原現金股利發放日:115/07/10 3.變更後現金股利發放日:115/07/13 4.變更原因: 本公司現金股利訂於115年7月10日發放，如因受颱風停班影響，致部分停止上班地區 金融機構作業日程需順延，現金股利發放日將順延至下一營業日115年7月13日發放。 5.其他應敘明事項: 未受颱風停班影響，將依原訂日期115年7月10日發放現金股利。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 6214 | 精誠 | revenue_breakout_low_response | 營收爆發低反應股 | 14.0 | 31.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.董事會決議或公司決定日期:115/07/09 2.原現金股利發放日:115/07/10 3.變更後現金股利發放日:115/07/13 4.變更原因: 本公司現金股利訂於115年7月10日發放，如因受颱風停班影響，致部分停止上班地區 金融機構作業日程需順延，現金股利發放日將順延至下一營業日115年7月13日發放。 5.其他應敘明事項: 未受颱風停班影響，將依原訂日期115年7月10日發放現金股利。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6214 | 精誠 | 2 | 2 | 4 | 9 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6214 | 精誠 | 8 | 0 | 1073380.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
