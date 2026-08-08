# INDIVIDUAL STOCK CHATGPT PACKET - 6446 藥華藥

## Metadata
- generated_at: 2026-08-08 22:28:23 Asia/Taipei
- stock_id: 6446
- stock_name: 藥華藥
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6446_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6446_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6446_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6446_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6446_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6446_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6446_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6446_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6446_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6446_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6446_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6446_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6446.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6446.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6446.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6446.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6446_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6446_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6446_latest.md?ref=main

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
- date: 20260805
- open: 1245
- high: 1335
- low: 1240
- close: 1335
- volume: 4891358
- ma5: 1160
- ema23_primary: 1180.98
- distance_to_ema23_pct: 13.04
- ma20: 1202.25
- ma60: 1072.8
- ma120: 870.7
- return_5d: 23.61
- return_20d: -10.7
- volume_ratio: 1.51
- distance_to_ma20_pct_auxiliary: 11.04
- distance_to_high_60_pct: -14.97

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,1560,1570,1490,1530,4301198,1208.19,26.64,1190.6,903.92,1.4
20260709,1400,1400,1245,1285,6711957,1214.59,5.8,1205.55,914.63,2.12
20260713,1275,1310,1230,1250,3373173,1217.54,2.67,1221.35,924.63,1.09
20260714,1260,1260,1165,1200,4037292,1216.08,-1.32,1233.9,933.63,1.26
20260715,1235,1320,1210,1320,2157754,1224.74,7.78,1252.3,944.75,0.67
20260716,1335,1365,1250,1260,4420281,1227.68,2.63,1265.75,954.78,1.33
20260717,1225,1260,1190,1195,3377763,1224.96,-2.45,1275,963.87,1
20260720,1230,1235,1175,1175,2926691,1220.79,-3.75,1280.75,972.67,0.87
20260721,1185,1225,1175,1175,2044851,1216.98,-3.45,1284.75,981.77,0.61
20260722,1195,1215,1170,1180,2030357,1213.9,-2.79,1289,991.1,0.61
20260723,1185,1190,1125,1150,2928191,1208.57,-4.85,1288.5,1000.17,0.88
20260724,1150,1165,1120,1135,1580118,1202.44,-5.61,1285.5,1008.7,0.48
20260727,1155,1205,1130,1195,2059810,1201.82,-0.57,1287.5,1017.83,0.64
20260728,1160,1165,1110,1115,2794829,1194.58,-6.66,1279.75,1025.4,0.87
20260729,1120,1130,1050,1080,3830927,1185.04,-8.86,1266.75,1032.65,1.21
20260730,1065,1075,1015,1025,2848411,1171.7,-12.52,1250,1038.95,0.9
20260731,1075,1105,1045,1060,3531212,1162.39,-8.81,1233.25,1045.7,1.1
20260803,1100,1165,1090,1165,975946,1162.61,0.21,1221.75,1054.13,0.31
20260804,1205,1275,1200,1215,4174034,1166.97,4.12,1210.25,1062.32,1.31
20260805,1245,1335,1240,1335,4891358,1180.98,13.04,1202.25,1072.8,1.51
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 57.32
- over_600_ratio: 52.35
- over_800_ratio: 46.8
- over_1000_ratio: 44.11
- over_400_change_1w: 0.29
- over_800_change_1w: 0.84
- over_1000_change_1w: 0.55
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,56.13,0.21,46.98,0.14,43.73,0.9,3,True,True
20260529,56.42,0.29,47.28,0.3,43.55,-0.18,4,False,True
20260605,56.28,-0.14,46.94,-0.34,43.68,0.13,5,False,True
20260612,56.23,-0.05,47.25,0.31,44.02,0.34,6,False,True
20260618,56.49,0.26,47.14,-0.11,43.88,-0.14,7,False,False
20260626,57.31,0.82,47.26,0.12,44.72,0.84,8,True,True
20260703,57.87,0.56,46.91,-0.35,44.14,-0.58,9,False,False
20260709,57.64,-0.23,46.97,0.06,43.64,-0.5,10,False,True
20260717,57.13,-0.51,46.77,-0.2,44.16,0.52,11,False,True
20260724,56.95,-0.18,46.53,-0.24,43.96,-0.2,0,False,False
20260731,57.03,0.08,45.96,-0.57,43.56,-0.4,1,False,False
20260807,57.32,0.29,46.8,0.84,44.11,0.55,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6446 | 藥華藥 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | continued_2_3d | 1.事實發生日:115/07/08 2.發生緣由:依據臺灣證券交易所股份有限公司通知辦理 3.財務業務資訊:   期間              (月)                   (季)           (最近四季累計)               (IFRS-合併自結數)      (IFRS-合併核閱數)    (IFRS-合併查核                                                              /核閱數) -------------------------------------------------------------------------             最近一月   與去年同期   最近一季  與去年同期    (114年第2季   科目     (115年5月)     增減﹪     (115年      增減﹪     至115年第1季)                                      第一季) -------------------------------------------------------------------------  營業收入     2,458      108.48       5,121       57.23        17,499 （百萬）  稅前淨利     1,291     -389.46(註)   2,336       60.00         5,859 （百萬）  歸屬母公       993     -337.56(註)   2,150       70.23         5,932  司業主淨  利 （百萬）  每股盈餘      2.66     -335.40(註)    5.79       69.30         16.02 （元） 註：去年同期為負數。 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 6446 | 藥華藥 | revenue_pullback | 營收成長股價回檔 | 83.0 |  |  |  |  |  | continued_2_3d | 1.事實發生日:115/07/08 2.發生緣由:依據臺灣證券交易所股份有限公司通知辦理 3.財務業務資訊:   期間              (月)                   (季)           (最近四季累計)               (IFRS-合併自結數)      (IFRS-合併核閱數)    (IFRS-合併查核                                                              /核閱數) -------------------------------------------------------------------------             最近一月   與去年同期   最近一季  與去年同期    (114年第2季   科目     (115年5月)     增減﹪     (115年      增減﹪     至115年第1季)                                      第一季) -------------------------------------------------------------------------  營業收入     2,458      108.48       5,121       57.23        17,499 （百萬）  稅前淨利     1,291     -389.46(註)   2,336       60.00         5,859 （百萬）  歸屬母公       993     -337.56(註)   2,150       70.23         5,932  司業主淨  利 （百萬）  每股盈餘      2.66     -335.40(註)    5.79       69.30         16.02 （元） 註：去年同期為負數。 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告: 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6446 | 藥華藥 | 2 | 2 | 4 | 7 | 13 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
