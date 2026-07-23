# INDIVIDUAL STOCK CHATGPT PACKET - 1316 上曜

## Metadata
- generated_at: 2026-07-23 22:26:26 Asia/Taipei
- stock_id: 1316
- stock_name: 上曜
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 305
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1316_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1316_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1316.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1316.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1316.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1316.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1316_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1316_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1316_latest.md?ref=main

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
- date: 20260717
- open: 10.35
- high: 10.4
- low: 10.05
- close: 10.05
- volume: 2930416
- ma5: 10.27
- ema23_primary: 10.45
- distance_to_ema23_pct: -3.86
- ma20: 10.42
- ma60: 10.71
- ma120: 11.92
- return_5d: -2.9
- return_20d: -9.46
- volume_ratio: 1.54
- distance_to_ma20_pct_auxiliary: -3.53
- distance_to_high_60_pct: -16.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,11.15,11.3,10.9,10.95,2549845,10.81,1.28,10.59,11.26,0.69
20260622,10.75,10.75,10.45,10.5,3899422,10.79,-2.65,10.59,11.23,1.03
20260623,10.6,10.6,10.3,10.3,2205418,10.74,-4.14,10.59,11.19,0.6
20260624,10.2,10.45,10.2,10.35,1195542,10.71,-3.38,10.6,11.16,0.33
20260625,10.45,10.45,10.3,10.3,1087088,10.68,-3.54,10.61,11.13,0.3
20260626,10.25,10.3,10.1,10.1,1614654,10.63,-4.98,10.6,11.09,0.45
20260629,10.15,10.45,10.15,10.35,1420445,10.61,-2.42,10.62,11.06,0.4
20260630,10.5,10.5,10.3,10.45,1353238,10.59,-1.35,10.62,11.03,0.39
20260701,10.5,10.5,10.35,10.4,944028,10.58,-1.68,10.62,11.01,0.28
20260702,10.35,10.55,10.25,10.55,1246488,10.57,-0.24,10.62,10.98,0.38
20260703,10.55,11.15,10.55,10.95,4459235,10.61,3.24,10.63,10.96,1.32
20260706,11.25,11.25,10.75,10.75,2539821,10.62,1.24,10.64,10.94,0.75
20260707,10.75,10.75,10.35,10.35,2013253,10.6,-2.32,10.64,10.91,0.6
20260708,10.35,10.45,10.25,10.35,1355405,10.58,-2.13,10.63,10.88,0.4
20260709,10.35,10.4,10.25,10.35,828807,10.56,-1.96,10.6,10.85,0.31
20260713,10.4,10.45,10.2,10.3,1237872,10.54,-2.23,10.57,10.82,0.55
20260714,10.35,10.35,10,10.2,2486878,10.51,-2.92,10.52,10.79,1.21
20260715,10.3,10.45,10.2,10.45,1386787,10.5,-0.5,10.49,10.76,0.73
20260716,10.5,10.55,10.3,10.35,1329505,10.49,-1.33,10.47,10.74,0.72
20260717,10.35,10.4,10.05,10.05,2930416,10.45,-3.86,10.42,10.71,1.54
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 42.89
- over_600_ratio: 38.58
- over_800_ratio: 35.12
- over_1000_ratio: 32.68
- over_400_change_1w: 3.95
- over_800_change_1w: 4.39
- over_1000_change_1w: 4.56
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,39.16,,31.44,,28.56,,0,False,False
20260508,39.19,0.03,30.67,-0.77,28.32,-0.24,1,False,False
20260515,39.44,0.25,30.22,-0.45,28.11,-0.21,2,False,False
20260522,39.08,-0.36,30.55,0.33,28.02,-0.09,3,False,True
20260529,39.25,0.17,30.79,0.24,28.64,0.62,4,True,True
20260605,39.55,0.3,31.58,0.79,29.46,0.82,5,True,True
20260612,38.52,-1.03,30.38,-1.2,28.53,-0.93,0,False,False
20260618,38.46,-0.06,30.59,0.21,28.5,-0.03,1,False,True
20260626,38.69,0.23,30.45,-0.14,28.36,-0.14,2,False,False
20260703,39.01,0.32,30.7,0.25,28.12,-0.24,3,False,True
20260709,38.94,-0.07,30.73,0.03,28.12,0,4,False,True
20260717,42.89,3.95,35.12,4.39,32.68,4.56,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1316 | 上曜 | revenue_pullback | 營收成長股價回檔 | 82.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  承認114年度虧損撥補案。                  經票決結果:贊成205,280,383權，反對1,458,697權                  廢票0權，贊成占表決總權數95.30%，本案照                  原議案通過。 3.重要決議事項二、章程修訂:                  修訂本公司章程案。                  經票決結果:贊成206,124,489權，反對680,662權                  廢票0權，贊成占表決總權數95.70%，本案照                  原議案通過。 4.重要決議事項三、營業報告書及財務報表:                  承認114年度營業報告書及財務報表案。                  經票決結果:贊成206,092,573權，反對655,634權，                  廢票0權，贊成占表決總權數95.68%，本案照                  原議案通過。 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:                   (1) 本公司114年度營業狀況報告。                   (2) 審計委員會查核本公司114年度決算表冊報告書。                   (3) 募集與發行可轉換公司債有關事項報告。                   (4) 114年私募普通股案執行情形。                   (5) 擬辦理私募普通股案。                       經票決結果:贊成204,537,662權，反對2,257,514權                       廢票0權，贊成占表決總權數94.96%，本案照                       原議案通過。 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 1316 | 上曜 | revenue_breakout_low_response | 營收爆發低反應股 | 18.0 | 14.0 | B_可觀察 |  |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  承認114年度虧損撥補案。                  經票決結果:贊成205,280,383權，反對1,458,697權                  廢票0權，贊成占表決總權數95.30%，本案照                  原議案通過。 3.重要決議事項二、章程修訂:                  修訂本公司章程案。                  經票決結果:贊成206,124,489權，反對680,662權                  廢票0權，贊成占表決總權數95.70%，本案照                  原議案通過。 4.重要決議事項三、營業報告書及財務報表:                  承認114年度營業報告書及財務報表案。                  經票決結果:贊成206,092,573權，反對655,634權，                  廢票0權，贊成占表決總權數95.68%，本案照                  原議案通過。 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:                   (1) 本公司114年度營業狀況報告。                   (2) 審計委員會查核本公司114年度決算表冊報告書。                   (3) 募集與發行可轉換公司債有關事項報告。                   (4) 114年私募普通股案執行情形。                   (5) 擬辦理私募普通股案。                       經票決結果:贊成204,537,662權，反對2,257,514權                       廢票0權，贊成占表決總權數94.96%，本案照                       原議案通過。 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1316 | 上曜 | 2 | 2 | 4 | 8 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
