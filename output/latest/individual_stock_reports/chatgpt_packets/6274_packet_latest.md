# INDIVIDUAL STOCK CHATGPT PACKET - 6274 台燿

## Metadata
- generated_at: 2026-07-19 22:27:59 Asia/Taipei
- stock_id: 6274
- stock_name: 台燿
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 171
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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260717
- open: 1195
- high: 1235
- low: 1170
- close: 1170
- volume: 5560000
- ma5: 1369
- ema23_primary: 1528.98
- distance_to_ema23_pct: -23.48
- ma20: 1609.25
- ma60: 1464.57
- ma120: 1025.63
- return_5d: -25.48
- return_20d: -29.94
- volume_ratio: 0.97
- distance_to_ma20_pct_auxiliary: -27.3
- distance_to_high_60_pct: -39.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,1790,1835,1770,1835,3462000,1535.67,19.49,1601.5,1195.52,0.92
20260622,1900,1920,1835,1900,7359000,1566.03,21.33,1623.75,1218.17,1.81
20260623,1905,1905,1715,1735,6126000,1580.11,9.8,1630.5,1237.42,1.42
20260624,1700,1765,1670,1765,4384000,1595.52,10.62,1639.75,1256.73,0.99
20260625,1795,1795,1650,1700,6721000,1604.23,5.97,1643.25,1274.63,1.43
20260626,1680,1750,1575,1580,5774000,1602.21,-1.39,1645.25,1290.93,1.18
20260629,1575,1585,1505,1555,4749000,1598.27,-2.71,1638.5,1307.37,0.94
20260630,1675,1710,1620,1680,5194000,1605.08,4.67,1637.25,1324.98,0.99
20260701,1710,1715,1595,1690,5263000,1612.16,4.83,1642.25,1342.8,0.96
20260702,1620,1710,1610,1690,4507000,1618.65,4.41,1642,1359.58,0.8
20260703,1655,1840,1615,1790,7637000,1632.93,9.62,1646.75,1377.33,1.29
20260706,1820,1825,1615,1630,7729000,1632.68,-0.16,1647.75,1391.22,1.24
20260707,1630,1715,1560,1575,6384000,1627.88,-3.25,1649.75,1404,1.02
20260708,1630,1665,1550,1645,5814000,1629.3,0.96,1651.25,1418.07,0.95
20260709,1635,1680,1565,1570,4825000,1624.36,-3.35,1654.75,1429.9,0.81
20260713,1600,1620,1525,1550,3719000,1618.16,-4.21,1658.5,1439.97,0.65
20260714,1515,1530,1395,1395,4744000,1599.57,-12.79,1656.75,1447.22,0.86
20260715,1420,1490,1410,1435,5829000,1585.85,-9.51,1650,1455.37,1.04
20260716,1410,1415,1295,1295,9065000,1561.62,-17.07,1634.25,1461.12,1.57
20260717,1195,1235,1170,1170,5560000,1528.98,-23.48,1609.25,1464.57,0.97
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 66.54
- over_600_ratio: 63.44
- over_800_ratio: 57.92
- over_1000_ratio: 54.97
- over_400_change_1w: 0.26
- over_800_change_1w: 0.22
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.11,,60.03,,57.18,,0,False,False
20260508,68.53,0.42,60.3,0.27,56.93,-0.25,1,False,True
20260515,68.72,0.19,60.99,0.69,57.97,1.04,2,True,True
20260522,69.21,0.49,61.01,0.02,57.96,-0.01,3,False,True
20260529,67.9,-1.31,60.38,-0.63,57.01,-0.95,0,False,False
20260605,67.41,-0.49,59.91,-0.47,56.93,-0.08,0,False,False
20260612,67.08,-0.33,58.75,-1.16,55.7,-1.23,0,False,False
20260618,67.35,0.27,59.99,1.24,56.96,1.26,1,True,True
20260626,67.03,-0.32,59.29,-0.7,56.23,-0.73,0,False,False
20260703,66.65,-0.38,58.78,-0.51,55.78,-0.45,0,False,False
20260709,66.28,-0.37,57.7,-1.08,55,-0.78,0,False,False
20260717,66.54,0.26,57.92,0.22,54.97,-0.03,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6274 | 台燿 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/09 2.公司名稱:台燿科技 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:更正本公司115年6月衍生性商品交易資訊 6.更正資訊項目/報表名稱:6.交換 7.更正前金額/內容/頁次: 1001224/未沖銷契約契約總金額 -6768未沖銷契約公允價值 -6768未沖銷契約本年度認列未實現損益金額 1628138已沖銷契約契約總金額 -8695已沖銷契約本年度認列已實現損益金額 8.更正後金額/內容/頁次: 1000776/未沖銷契約契約總金額 -7312/未沖銷契約公允價值 -7312/未沖銷契約本年度認列未實現損益金額 1596748/已沖銷契約契約總金額 -8156已沖銷契約本年度認列已實現損益金額 9.因應措施:更正後重新上傳公開資訊觀測站 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6274 | 台燿 | 2 | 2 | 4 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
