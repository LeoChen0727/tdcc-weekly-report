# INDIVIDUAL STOCK CHATGPT PACKET - 2539 櫻花建

## Metadata
- generated_at: 2026-07-20 22:26:57 Asia/Taipei
- stock_id: 2539
- stock_name: 櫻花建
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2539_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2539_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2539_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2539_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2539_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2539_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2539_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2539_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2539_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2539_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2539_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2539_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2539.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2539.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2539.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2539.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2539_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2539_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2539_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260717
- open: 40.8
- high: 41.6
- low: 40.8
- close: 40.8
- volume: 1771263
- ma5: 40.72
- ema23_primary: 39.59
- distance_to_ema23_pct: 3.06
- ma20: 39.54
- ma60: 39.01
- ma120: 43.56
- return_5d: 3.82
- return_20d: 3.55
- volume_ratio: 1.61
- distance_to_ma20_pct_auxiliary: 3.19
- distance_to_high_60_pct: -11.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,39.8,40.25,39.15,39.95,1771484,38.46,3.89,37.31,41.55,0.74
20260622,39.95,39.95,38.55,38.65,1776165,38.47,0.46,37.34,41.4,0.73
20260623,38.5,38.85,38.3,38.65,1068071,38.49,0.43,37.44,41.23,0.47
20260624,38.65,39.45,38.2,39.1,950165,38.54,1.46,37.66,41.07,0.45
20260625,39.15,39.4,38.8,38.95,696124,38.57,0.98,37.95,40.91,0.37
20260626,38.5,38.75,37.75,38.1,1140843,38.53,-1.12,38.13,40.75,0.63
20260629,38.95,39.3,38.4,39.3,732696,38.6,1.82,38.26,40.61,0.43
20260630,39.5,39.5,38.55,38.9,878365,38.62,0.72,38.37,40.46,0.55
20260701,39.15,39.4,38.55,39.25,1265544,38.67,1.49,38.53,40.32,0.81
20260702,39.3,39.3,38.65,39.1,664587,38.71,1.01,38.66,40.17,0.43
20260703,38.5,39.4,38.5,39.3,690232,38.76,1.4,38.72,40.03,0.49
20260706,39.3,39.8,39.1,39.7,961631,38.84,2.22,38.84,39.89,0.69
20260707,39.7,40.35,39.45,39.8,915059,38.92,2.27,39,39.76,0.67
20260708,39.8,39.8,38.95,39.15,705772,38.94,0.55,39.11,39.62,0.52
20260709,39.15,39.5,39.05,39.3,406586,38.97,0.85,39.11,39.48,0.34
20260713,39.3,41,39.3,40.95,1363423,39.13,4.64,39.21,39.38,1.27
20260714,41.2,41.2,40.15,40.55,1276476,39.25,3.31,39.3,39.27,1.24
20260715,40.6,40.95,39.75,40.1,1453977,39.32,1.98,39.35,39.16,1.39
20260716,40.1,41.4,40.1,41.2,1493740,39.48,4.36,39.47,39.08,1.42
20260717,40.8,41.6,40.8,40.8,1771263,39.59,3.06,39.54,39.01,1.61
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 86.94
- over_600_ratio: 85.52
- over_800_ratio: 85.13
- over_1000_ratio: 84.3
- over_400_change_1w: 0.02
- over_800_change_1w: 0.01
- over_1000_change_1w: -0.06
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,87.66,,85.81,,85.29,,0,False,False
20260508,87.67,0.01,85.9,0.09,85.22,-0.07,1,False,True
20260515,87.45,-0.22,85.68,-0.22,85,-0.22,0,False,False
20260522,87.3,-0.15,85.63,-0.05,84.96,-0.04,0,False,False
20260529,87.13,-0.17,85.21,-0.42,84.53,-0.43,0,False,False
20260605,87.03,-0.1,85.13,-0.08,84.22,-0.31,0,False,False
20260612,86.88,-0.15,84.96,-0.17,84.21,-0.01,0,False,False
20260618,86.81,-0.07,84.96,0,84.21,0,1,False,False
20260626,86.88,0.07,85.04,0.08,84.29,0.08,2,False,True
20260703,86.83,-0.05,85.1,0.06,84.27,-0.02,3,False,True
20260709,86.92,0.09,85.12,0.02,84.36,0.09,4,False,True
20260717,86.94,0.02,85.13,0.01,84.3,-0.06,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2539 | 櫻花建 | revenue_pullback | 營收成長股價回檔 | 63.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.發生變動日期:115/06/30 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:許振華、王癸元、黃子翎 4.舊任者簡歷: 許振華 / 協侑營造有限公司行政服務處總經理 王癸元 / 亞洲大學副教授 黃子翎 / 誠佳建設(股)公司行政服務處經理 5.新任者姓名:王癸元、徐文宗、黃瓊瑤 6.新任者簡歷: 王癸元 / 亞洲大學副教授 徐文宗 / 維翰聯合法律事務所主持律師 黃瓊瑤 / 雲林科技大學教授 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，重新委任 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/13~115/06/12 10.新任生效日期:115/6/30 11.其他應敘明事項: 本屆薪資報酬委員會任期115/06/30~118/06/15，同本屆董事會任期。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 2539 | 櫻花建 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 18.0 | B_可觀察 |  |  |  | stale_signal | 1.發生變動日期:115/06/30 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:許振華、王癸元、黃子翎 4.舊任者簡歷: 許振華 / 協侑營造有限公司行政服務處總經理 王癸元 / 亞洲大學副教授 黃子翎 / 誠佳建設(股)公司行政服務處經理 5.新任者姓名:王癸元、徐文宗、黃瓊瑤 6.新任者簡歷: 王癸元 / 亞洲大學副教授 徐文宗 / 維翰聯合法律事務所主持律師 黃瓊瑤 / 雲林科技大學教授 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，重新委任 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/13~115/06/12 10.新任生效日期:115/6/30 11.其他應敘明事項: 本屆薪資報酬委員會任期115/06/30~118/06/15，同本屆董事會任期。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 2539 | 櫻花建 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.發生變動日期:115/06/30 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:許振華、王癸元、黃子翎 4.舊任者簡歷: 許振華 / 協侑營造有限公司行政服務處總經理 王癸元 / 亞洲大學副教授 黃子翎 / 誠佳建設(股)公司行政服務處經理 5.新任者姓名:王癸元、徐文宗、黃瓊瑤 6.新任者簡歷: 王癸元 / 亞洲大學副教授 徐文宗 / 維翰聯合法律事務所主持律師 黃瓊瑤 / 雲林科技大學教授 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，重新委任 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/13~115/06/12 10.新任生效日期:115/6/30 11.其他應敘明事項: 本屆薪資報酬委員會任期115/06/30~118/06/15，同本屆董事會任期。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2539 | 櫻花建 | 2 | 2 | 4 | 4 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
