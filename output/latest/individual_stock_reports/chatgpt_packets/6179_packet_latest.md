# INDIVIDUAL STOCK CHATGPT PACKET - 6179 亞通

## Metadata
- generated_at: 2026-07-30 22:28:23 Asia/Taipei
- stock_id: 6179
- stock_name: 亞通
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6179_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6179_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6179.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6179.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6179.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6179.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6179_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6179_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6179_latest.md?ref=main

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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- confidence_level: high
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
- decision_score_high
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
- open: 23.1
- high: 23.45
- low: 22.75
- close: 22.85
- volume: 595000
- ma5: 23.8
- ema23_primary: 25.2
- distance_to_ema23_pct: -9.32
- ma20: 25.85
- ma60: 25.09
- ma120: 25.44
- return_5d: -11.43
- return_20d: -13.12
- volume_ratio: 0.34
- distance_to_ma20_pct_auxiliary: -11.61
- distance_to_high_60_pct: -21.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,26.35,26.55,25.75,26.25,1733000,25.44,3.2,25.22,24.64,0.94
20260703,26.45,26.75,25.95,26.55,812000,25.53,4,25.33,24.68,0.43
20260706,27,28.6,26.95,28.15,5039000,25.75,9.33,25.55,24.74,2.36
20260707,28.25,28.25,26.6,26.95,2511000,25.85,4.27,25.76,24.77,1.16
20260708,26.95,27.25,26.5,26.8,1120000,25.93,3.37,25.93,24.8,0.51
20260709,27.2,29.1,27.15,27.95,3407000,26.09,7.11,26.13,24.85,1.51
20260713,28.55,28.7,27.3,27.85,4923000,26.24,6.13,26.36,24.9,2.01
20260714,27.8,27.8,26.5,27.8,1934000,26.37,5.42,26.55,24.95,0.78
20260715,28.1,28.1,27.25,27.75,1040000,26.49,4.77,26.73,25.01,0.42
20260716,28.1,28.45,27,27,1508000,26.53,1.78,26.82,25.05,0.64
20260717,26.6,27.2,24.35,24.8,3301000,26.38,-6.01,26.77,25.04,1.37
20260720,25,25.15,23.5,24.2,1663000,26.2,-7.64,26.64,25.03,0.72
20260721,24.25,25.1,24.25,24.8,527000,26.09,-4.93,26.55,25.05,0.24
20260722,24.8,25.6,24.8,25.4,667000,26.03,-2.42,26.46,25.07,0.33
20260723,25.5,25.8,25.25,25.8,472000,26.01,-0.81,26.37,25.1,0.25
20260724,25.6,25.6,24.7,24.7,627000,25.9,-4.64,26.3,25.11,0.34
20260727,24.7,25,24.15,24.35,484000,25.77,-5.51,26.23,25.12,0.27
20260728,23.9,24.15,23.5,24,922000,25.62,-6.34,26.14,25.12,0.52
20260729,24,24.2,22.4,23.1,1927000,25.41,-9.1,26.02,25.11,1.06
20260730,23.1,23.45,22.75,22.85,595000,25.2,-9.32,25.85,25.09,0.34
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 41.8
- over_600_ratio: 37.45
- over_800_ratio: 33.6
- over_1000_ratio: 31.56
- over_400_change_1w: -0.36
- over_800_change_1w: -0.8
- over_1000_change_1w: -1.24
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,38.42,,32.56,,29.41,,0,False,False
20260508,38.75,0.33,32.39,-0.17,29.29,-0.12,1,False,False
20260515,38.81,0.06,31.62,-0.77,29.55,0.26,2,False,True
20260522,40.53,1.72,33.2,1.58,30.59,1.04,3,True,True
20260529,39.28,-1.25,32.22,-0.98,29.54,-1.05,0,False,False
20260605,38.67,-0.61,31.63,-0.59,28.55,-0.99,0,False,False
20260612,38.24,-0.43,30.64,-0.99,28.54,-0.01,1,False,False
20260618,40.11,1.87,32.07,1.43,29.54,1,2,True,True
20260626,41.79,1.68,33.76,1.69,30.65,1.11,3,True,True
20260703,41.9,0.11,33.86,0.1,31.28,0.63,4,True,True
20260709,42.16,0.26,34.4,0.54,32.8,1.52,5,True,True
20260717,41.8,-0.36,33.6,-0.8,31.56,-1.24,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6179 | 亞通 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/26 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:   發放股東現金每股0.5元(總額新台幣88,662,325元)；發放方式為   (1)資本公積發放現金新台幣88,662,325元 4.除權（息）交易日:115/08/14 5.最後過戶日:115/08/17 6.停止過戶起始日期:115/08/18 7.停止過戶截止日期:115/08/22 8.除權（息）基準日:115/08/22 9.債券最後申請轉換日期:115/07/24 10.債券停止轉換起始日期:115/07/28 11.債券停止轉換截止日期:115/08/22 12.普通股現金股利發放日期:115/09/10 13.其他應敘明事項:配合本公司第三次無擔保轉換公司債到期相關作業，   爰依董事會授權，調整除息基準日及相關作業時程，以維護投資人權益。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 6179 | 亞通 | revenue_breakout_low_response | 營收爆發低反應股 | 19.0 | 11.0 | B_可觀察 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/26 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:   發放股東現金每股0.5元(總額新台幣88,662,325元)；發放方式為   (1)資本公積發放現金新台幣88,662,325元 4.除權（息）交易日:115/08/14 5.最後過戶日:115/08/17 6.停止過戶起始日期:115/08/18 7.停止過戶截止日期:115/08/22 8.除權（息）基準日:115/08/22 9.債券最後申請轉換日期:115/07/24 10.債券停止轉換起始日期:115/07/28 11.債券停止轉換截止日期:115/08/22 12.普通股現金股利發放日期:115/09/10 13.其他應敘明事項:配合本公司第三次無擔保轉換公司債到期相關作業，   爰依董事會授權，調整除息基準日及相關作業時程，以維護投資人權益。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6179 | 亞通 | 2 | 2 | 4 | 8 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
