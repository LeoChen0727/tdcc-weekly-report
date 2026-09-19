# INDIVIDUAL STOCK CHATGPT PACKET - 6274 台燿

## Metadata
- generated_at: 2026-09-19 22:17:16 Asia/Taipei
- stock_id: 6274
- stock_name: 台燿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6274_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6274_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6274_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6274_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6274_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6274_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6274_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6274_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6274_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6274_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6274_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6274_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6274.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6274.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6274.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6274.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6274_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6274_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6274_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260918
- open: 1365
- high: 1395
- low: 1335
- close: 1370
- volume: 9241000
- ma5: 1377
- ema23_primary: 1403.16
- distance_to_ema23_pct: -2.36
- ma20: 1405.75
- ma60: 1430.75
- ma120: 1352.69
- return_5d: 0.37
- return_20d: -8.36
- volume_ratio: 1.41
- distance_to_ma20_pct_auxiliary: -2.54
- distance_to_high_60_pct: -25.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,1505,1540,1455,1455,3557000,1471.49,-1.12,1419,1508.5,0.64
20260825,1430,1485,1395,1485,5255000,1472.61,0.84,1436.75,1505.08,0.95
20260826,1475,1560,1465,1530,5584000,1477.39,3.56,1462.25,1502.17,1.03
20260827,1560,1565,1420,1445,8281000,1474.7,-2.01,1484,1499.75,1.61
20260828,1460,1515,1440,1490,4976000,1475.97,0.95,1503,1496.33,0.93
20260831,1435,1485,1385,1435,7008000,1472.56,-2.55,1513.75,1492,1.24
20260901,1435,1480,1430,1450,4590000,1470.68,-1.41,1519.25,1489.33,0.84
20260902,1435,1460,1400,1410,3289000,1465.62,-3.79,1516.25,1487.25,0.6
20260903,1420,1430,1340,1345,4441000,1455.57,-7.6,1507,1482.75,0.91
20260904,1390,1425,1295,1365,5598000,1448.02,-5.73,1503.25,1480.5,1.19
20260907,1395,1405,1345,1370,5580000,1441.52,-4.96,1498.75,1478.75,1.14
20260908,1405,1430,1335,1345,4724000,1433.48,-6.17,1485.75,1477.33,0.95
20260909,1360,1405,1315,1345,8129000,1426.1,-5.69,1473,1473.58,1.55
20260910,1345,1400,1330,1395,4654000,1423.51,-2,1462.75,1470,0.87
20260911,1355,1395,1335,1365,4431000,1418.64,-3.78,1447.25,1464.92,0.82
20260914,1340,1440,1320,1410,7142000,1417.92,-0.56,1437.75,1457.83,1.31
20260915,1430,1450,1370,1370,6447000,1413.92,-3.11,1429,1449,1.18
20260916,1360,1460,1345,1415,6899000,1414.01,0.07,1424.75,1443.67,1.25
20260917,1445,1460,1275,1320,21653000,1406.18,-6.13,1412,1436.25,3.4
20260918,1365,1395,1335,1370,9241000,1403.16,-2.36,1405.75,1430.75,1.41
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 63.31
- over_600_ratio: 61.1
- over_800_ratio: 57.21
- over_1000_ratio: 53.87
- over_400_change_1w: -0.21
- over_800_change_1w: 0.91
- over_1000_change_1w: 1.84
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,66.65,-0.38,58.78,-0.51,55.78,-0.45,0,False,False
20260709,66.28,-0.37,57.7,-1.08,55,-0.78,0,False,False
20260717,66.54,0.26,57.92,0.22,54.97,-0.03,1,False,True
20260724,66.84,0.3,57.97,0.05,54.68,-0.29,2,False,True
20260731,66.7,-0.14,57.99,0.02,54.71,0.03,3,False,True
20260807,66.75,0.05,59.16,1.17,55.23,0.52,4,False,True
20260814,66.9,0.15,59,-0.16,55.06,-0.17,5,False,False
20260821,66.33,-0.57,58.81,-0.19,54.26,-0.8,0,False,False
20260828,64.52,-1.81,57.54,-1.27,53.58,-0.68,0,False,False
20260904,64.14,-0.38,57.54,0,53.31,-0.27,0,False,False
20260911,63.52,-0.62,56.3,-1.24,52.03,-1.28,0,False,False
20260918,63.31,-0.21,57.21,0.91,53.87,1.84,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6274 | 台燿 | pullback_rebound | 回檔後短線轉強 | 82.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/08/10 2.發生緣由:依據證券櫃檯買賣中心通知辦理 3.財務業務資訊: (一)單月(最近一月單月自結數)                             115年7月 / 114年7月 / 與去年同期之增減%                           ----------- ---------   ------------------- 營業收入(百萬元)              5,909      2,667         121.6% 稅前淨利(百萬元)              1,865        428         355.7% 歸屬母公司業主淨利(百萬元)    1,306        329         297.0% 每股盈餘(元)                   4.36       1.17         272.6% (二)單季(最近一季單季，會計師查核數)                          115年第2季 / 114年第2季 / 與去年同期之增減%                         ------------- ---------   ------------------- 營業收入(百萬元)      	     14,301        6,780       110.9% 稅前淨利(百萬元)             3,427          840       308.0% 歸屬母公司業主淨利(百萬元)   2,342          652       259.2% 每股盈餘(元)                  8.02         2.36       239.8% (三)最近四季累計(會計師查核數)                          114年第3季至115年第2季                       --------------------------- 營業收入(百萬元)      	      41,543 稅前淨利(百萬元)              8,046 歸屬母公司業主淨利(百萬元)    5,689 每股盈餘(元)                  19.72 (四)公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)以上115年7月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之合併數 ，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第2季係指單季數字，非為最近財務報告中之累計數字，且係本公司 採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併數，業經會計師 查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6274 | 台燿 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/08/10 2.發生緣由:依據證券櫃檯買賣中心通知辦理 3.財務業務資訊: (一)單月(最近一月單月自結數)                             115年7月 / 114年7月 / 與去年同期之增減%                           ----------- ---------   ------------------- 營業收入(百萬元)              5,909      2,667         121.6% 稅前淨利(百萬元)              1,865        428         355.7% 歸屬母公司業主淨利(百萬元)    1,306        329         297.0% 每股盈餘(元)                   4.36       1.17         272.6% (二)單季(最近一季單季，會計師查核數)                          115年第2季 / 114年第2季 / 與去年同期之增減%                         ------------- ---------   ------------------- 營業收入(百萬元)      	     14,301        6,780       110.9% 稅前淨利(百萬元)             3,427          840       308.0% 歸屬母公司業主淨利(百萬元)   2,342          652       259.2% 每股盈餘(元)                  8.02         2.36       239.8% (三)最近四季累計(會計師查核數)                          114年第3季至115年第2季                       --------------------------- 營業收入(百萬元)      	      41,543 稅前淨利(百萬元)              8,046 歸屬母公司業主淨利(百萬元)    5,689 每股盈餘(元)                  19.72 (四)公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)以上115年7月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之合併數 ，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第2季係指單季數字，非為最近財務報告中之累計數字，且係本公司 採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併數，業經會計師 查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6274 | 台燿 | 23 | 23 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
