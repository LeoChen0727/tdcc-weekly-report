# INDIVIDUAL STOCK CHATGPT PACKET - 6683 雍智科技

## Metadata
- generated_at: 2026-09-05 15:54:21 Asia/Taipei
- stock_id: 6683
- stock_name: 雍智科技
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6683_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6683_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6683_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6683_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6683_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6683_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6683_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6683_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6683_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6683_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6683_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6683_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6683.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6683.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6683.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6683.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6683_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6683_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6683_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260904
- open: 1420
- high: 1460
- low: 1335
- close: 1360
- volume: 1253000
- ma5: 1349
- ema23_primary: 1260.84
- distance_to_ema23_pct: 7.86
- ma20: 1252
- ma60: 1377.35
- ma120: 1545.8
- return_5d: 13.33
- return_20d: 21.43
- volume_ratio: 1.78
- distance_to_ma20_pct_auxiliary: 8.63
- distance_to_high_60_pct: -32.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,1150,1230,1150,1230,285000,1231.95,-0.16,1160.05,1512.35,0.49
20260811,1240,1280,1195,1245,878000,1233.04,0.97,1146.8,1504.18,1.49
20260812,1255,1290,1240,1270,356000,1236.12,2.74,1136.8,1495.35,0.65
20260813,1315,1395,1315,1395,614000,1249.36,11.66,1139.05,1491.6,1.16
20260814,1445,1460,1345,1370,1199000,1259.41,8.78,1146.8,1484.77,2.31
20260817,1350,1370,1280,1325,534000,1264.88,4.75,1157.8,1478.77,1.16
20260818,1325,1345,1255,1260,579000,1264.47,-0.35,1162.3,1472.27,1.34
20260819,1200,1275,1185,1190,433000,1258.27,-5.43,1160.8,1461.85,1
20260820,1230,1235,1115,1140,858000,1248.41,-8.68,1156.05,1450.85,1.84
20260821,1135,1160,1050,1070,831000,1233.54,-13.26,1150.05,1439.02,1.67
20260824,1090,1140,1080,1090,411000,1221.58,-10.77,1146.8,1428.85,0.8
20260825,1085,1130,1050,1130,322000,1213.95,-6.92,1151.3,1419.93,0.61
20260826,1130,1145,1110,1135,452000,1207.37,-5.99,1161.25,1410.27,0.83
20260827,1165,1245,1130,1245,588000,1210.51,2.85,1181.35,1401.93,1.06
20260828,1250,1250,1165,1200,1133000,1209.63,-0.8,1195,1393.35,1.89
20260831,1180,1225,1140,1210,537000,1209.66,0.03,1204.75,1385.52,0.88
20260901,1330,1330,1330,1330,169000,1219.69,9.04,1216.75,1380.85,0.28
20260902,1405,1460,1400,1460,716000,1239.72,17.77,1230,1380.27,1.14
20260903,1470,1475,1360,1385,1905000,1251.82,10.64,1240,1378.18,2.85
20260904,1420,1460,1335,1360,1253000,1260.84,7.86,1252,1377.35,1.78
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 21.85
- over_600_ratio: 14.63
- over_800_ratio: 14.63
- over_1000_ratio: 11.24
- over_400_change_1w: -0.09
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,20.19,-1.94,14.63,0,11.24,0,0,False,False
20260626,25.22,5.03,14.63,0,11.24,0,1,False,False
20260703,23.74,-1.48,14.63,0,11.24,0,0,False,False
20260709,23.78,0.04,14.63,0,11.24,0,1,False,False
20260717,22.58,-1.2,14.63,0,11.24,0,0,False,False
20260724,26.14,3.56,14.63,0,11.24,0,1,False,False
20260731,26.2,0.06,14.63,0,11.24,0,2,False,False
20260807,26.21,0.01,14.63,0,11.24,0,3,False,False
20260814,22.4,-3.81,14.63,0,11.24,0,0,False,False
20260821,21.88,-0.52,14.63,0,11.24,0,0,False,False
20260828,21.94,0.06,14.63,0,11.24,0,1,False,False
20260904,21.85,-0.09,14.63,0,11.24,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6683 | 雍智科技 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | stale_signal | 1.主管機關核准減資日期:115/08/27 2.辦理資本變更登記完成日期:115/08/27 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）: (1)本公司減資前實收資本額為新台幣275,571,610元，流通在外股數 為27,557,161股，每股淨值為新台幣102.61元。 (2)本公司減資後實收資本額為新台幣275,526,610元，流通在外股數 為27,552,661股，每股淨值為新台幣102.62元。 4.預計換股作業計畫:不適用 5.預計減資新股上櫃後之上櫃普通股股數:不適用 6.預計減資新股上櫃後之上櫃普通股股數占已發行普通股比率 （減資後上櫃普通股股數/減資後已發行普通股股數）:不適用 7.前二項預計減資後上櫃普通股股數未達500萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用 8.其他應敘明事項: (1)以上每股淨值係依最近一期(115年第2季)會計師核閱財務報告計算之。 (2)本公司本次辦理註銷限制員工權利新股計4,500股。 (3)本公司於115/09/02接獲主管機關變更登記核准信函。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 6683 | 雍智科技 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  |  | stale_signal | 1.主管機關核准減資日期:115/08/27 2.辦理資本變更登記完成日期:115/08/27 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）: (1)本公司減資前實收資本額為新台幣275,571,610元，流通在外股數 為27,557,161股，每股淨值為新台幣102.61元。 (2)本公司減資後實收資本額為新台幣275,526,610元，流通在外股數 為27,552,661股，每股淨值為新台幣102.62元。 4.預計換股作業計畫:不適用 5.預計減資新股上櫃後之上櫃普通股股數:不適用 6.預計減資新股上櫃後之上櫃普通股股數占已發行普通股比率 （減資後上櫃普通股股數/減資後已發行普通股股數）:不適用 7.前二項預計減資後上櫃普通股股數未達500萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用 8.其他應敘明事項: (1)以上每股淨值係依最近一期(115年第2季)會計師核閱財務報告計算之。 (2)本公司本次辦理註銷限制員工權利新股計4,500股。 (3)本公司於115/09/02接獲主管機關變更登記核准信函。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6683 | 雍智科技 | 2 | 2 | 2 | 3 | 3 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
