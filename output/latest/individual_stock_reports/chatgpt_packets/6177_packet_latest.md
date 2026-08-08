# INDIVIDUAL STOCK CHATGPT PACKET - 6177 達麗

## Metadata
- generated_at: 2026-08-08 16:02:24 Asia/Taipei
- stock_id: 6177
- stock_name: 達麗
- packet_status: standard_180d_window_packet
- latest_price_date: 20260805
- price_rows: 319
- current_main_price_date: 20260805
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260807-01698d0b1c2355ac
- official_tdcc_signal_date: 20260807
- latest_tdcc_date: 20260807
- tdcc_rows: 15
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6177_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6177_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6177_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6177_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6177_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6177_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6177_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6177_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6177_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6177_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6177_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6177_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6177.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6177.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6177.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6177.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6177_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6177_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6177_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260805
- open: 47.6
- high: 47.8
- low: 47.1
- close: 47.75
- volume: 835004
- ma5: 47.43
- ema23_primary: 47.14
- distance_to_ema23_pct: 1.28
- ma20: 47.24
- ma60: 45.97
- ma120: 46.36
- return_5d: 1.38
- return_20d: 5.29
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 1.08
- distance_to_high_60_pct: -7.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,45.35,45.5,45.15,45.2,771525,45.74,-1.19,46.38,45.45,0.32
20260709,45.2,45.5,45.1,45.3,469946,45.71,-0.89,46.31,45.44,0.22
20260713,45.9,46.45,45.8,46.1,1401766,45.74,0.79,46.25,45.43,0.7
20260714,46.4,46.4,45.55,46,1605975,45.76,0.52,46.19,45.43,0.83
20260715,46.5,47,46.2,46.9,1368867,45.86,2.28,46.17,45.45,0.72
20260716,47.1,48.2,46.85,48,1732910,46.03,4.27,46.23,45.5,0.89
20260717,47.5,48.95,47.3,47.5,2462112,46.16,2.91,46.19,45.55,1.27
20260720,48.1,48.1,46.9,47.35,1173535,46.26,2.36,46.04,45.58,0.74
20260721,47.6,48.2,47.2,47.55,757151,46.36,2.56,46.12,45.6,0.6
20260722,47.95,48.95,47.55,48.3,1520696,46.53,3.81,46.24,45.64,1.2
20260723,48.6,48.7,47.7,48.5,786324,46.69,3.88,46.36,45.71,0.62
20260724,48.05,48.7,48.05,48.55,745205,46.84,3.64,46.49,45.77,0.59
20260727,48.6,48.85,47.85,47.9,861473,46.93,2.06,46.6,45.8,0.69
20260728,47.8,47.85,47.1,47.4,1010566,46.97,0.91,46.71,45.83,0.82
20260729,47.65,47.85,46.4,47.1,1770406,46.98,0.25,46.81,45.86,1.4
20260730,47.55,48.15,46.8,47.45,1501072,47.02,0.91,46.88,45.9,1.25
20260731,48.2,48.6,47.05,47.3,2368257,47.04,0.54,46.98,45.92,1.87
20260803,47.3,47.9,47,47.35,1696437,47.07,0.59,47.06,45.95,1.29
20260804,47.1,47.4,46.75,47.3,1457603,47.09,0.45,47.12,45.96,1.09
20260805,47.6,47.8,47.1,47.75,835004,47.14,1.28,47.24,45.97,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 75.54
- over_600_ratio: 73.04
- over_800_ratio: 69.95
- over_1000_ratio: 66.78
- over_400_change_1w: -0.63
- over_800_change_1w: -0.17
- over_1000_change_1w: -0.19
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,75.71,-0.05,70.24,0.06,68.33,-0.17,1,False,True
20260529,75.07,-0.64,69.13,-1.11,67.45,-0.88,0,False,False
20260605,75.1,0.03,68.73,-0.4,67.23,-0.22,1,False,False
20260612,75.25,0.15,68.99,0.26,67.3,0.07,2,True,True
20260618,75.29,0.04,69.46,0.47,67.39,0.09,3,False,True
20260626,75.21,-0.08,68.83,-0.63,66.56,-0.83,4,False,False
20260703,74.99,-0.22,68.66,-0.17,66.41,-0.15,0,False,False
20260709,75.1,0.11,68.76,0.1,66.51,0.1,1,True,True
20260717,75.48,0.38,69.88,1.12,66.9,0.39,2,True,True
20260724,75.77,0.29,70.06,0.18,67.25,0.35,3,True,True
20260731,76.17,0.4,70.12,0.06,66.97,-0.28,4,False,True
20260807,75.54,-0.63,69.95,-0.17,66.78,-0.19,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6177 | 達麗 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  | no_signal | stale_signal | 1.契約種類: 混合契約股票連結債券 2.事實發生日:115/7/15 3.契約金額: 單筆契約金額共1筆，合約金額計US$ 1,000仟元(折合NT$ 31,640仟元) 4.支付保證金或權利金金額: 無 5.處理程序所訂之全部或個別契約損失上限金額: 衍生性商品單筆損失上限達個別契約20% 6.從事衍生性商品交易原因: 以交易為目的 7.被避險項目: 無 8.被避險項目部位之金額: 無 9.被避險項目之損益狀況: 無 10.依公平價值評估(含已實現及未實現)之損失金額: 個別契約：共1筆契約累積未實現損失US$ 213仟元(折合NT$ 6,310仟元) 11.損失發生原因及對公司之影響: 持有該混合商品產生之未實現評價損失；該損失對公司營運無重大影響 12.契約期間: 2026/6/09至2026/11/16 13.限制條款: 無 14.其他重要約定事項: 無 15.其他敘明事項: 代子公司寶信營造(股)公司公告從事衍生性商品交易達所訂個別契約損失金額上限；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 6177 | 達麗 | revenue_breakout_low_response | 營收爆發低反應股 | 18.0 | 22.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.契約種類: 混合契約股票連結債券 2.事實發生日:115/7/15 3.契約金額: 單筆契約金額共1筆，合約金額計US$ 1,000仟元(折合NT$ 31,640仟元) 4.支付保證金或權利金金額: 無 5.處理程序所訂之全部或個別契約損失上限金額: 衍生性商品單筆損失上限達個別契約20% 6.從事衍生性商品交易原因: 以交易為目的 7.被避險項目: 無 8.被避險項目部位之金額: 無 9.被避險項目之損益狀況: 無 10.依公平價值評估(含已實現及未實現)之損失金額: 個別契約：共1筆契約累積未實現損失US$ 213仟元(折合NT$ 6,310仟元) 11.損失發生原因及對公司之影響: 持有該混合商品產生之未實現評價損失；該損失對公司營運無重大影響 12.契約期間: 2026/6/09至2026/11/16 13.限制條款: 無 14.其他重要約定事項: 無 15.其他敘明事項: 代子公司寶信營造(股)公司公告從事衍生性商品交易達所訂個別契約損失金額上限；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 6177 | 達麗 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 65.0 |  |  | neckline_challenge |  | no_signal | stale_signal | 1.契約種類: 混合契約股票連結債券 2.事實發生日:115/7/15 3.契約金額: 單筆契約金額共1筆，合約金額計US$ 1,000仟元(折合NT$ 31,640仟元) 4.支付保證金或權利金金額: 無 5.處理程序所訂之全部或個別契約損失上限金額: 衍生性商品單筆損失上限達個別契約20% 6.從事衍生性商品交易原因: 以交易為目的 7.被避險項目: 無 8.被避險項目部位之金額: 無 9.被避險項目之損益狀況: 無 10.依公平價值評估(含已實現及未實現)之損失金額: 個別契約：共1筆契約累積未實現損失US$ 213仟元(折合NT$ 6,310仟元) 11.損失發生原因及對公司之影響: 持有該混合商品產生之未實現評價損失；該損失對公司營運無重大影響 12.契約期間: 2026/6/09至2026/11/16 13.限制條款: 無 14.其他重要約定事項: 無 15.其他敘明事項: 代子公司寶信營造(股)公司公告從事衍生性商品交易達所訂個別契約損失金額上限；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6177 | 達麗 | 5 | 2 | 5 | 6 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6177 | 達麗 | 6 | 0 | 50390.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
