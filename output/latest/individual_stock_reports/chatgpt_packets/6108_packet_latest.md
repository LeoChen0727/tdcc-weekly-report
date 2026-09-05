# INDIVIDUAL STOCK CHATGPT PACKET - 6108 競國

## Metadata
- generated_at: 2026-09-05 22:17:21 Asia/Taipei
- stock_id: 6108
- stock_name: 競國
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6108_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6108_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6108_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6108_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6108.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6108.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6108.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6108.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6108_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6108_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6108_latest.md?ref=main

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
- date: 20260904
- open: 23.25
- high: 23.5
- low: 22.7
- close: 22.95
- volume: 1378795
- ma5: 23.53
- ema23_primary: 22.41
- distance_to_ema23_pct: 2.42
- ma20: 23.07
- ma60: 19.62
- ma120: 19.03
- return_5d: -10.7
- return_20d: 21.43
- volume_ratio: 0.32
- distance_to_ma20_pct_auxiliary: -0.51
- distance_to_high_60_pct: -13.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,19,19,18.3,18.7,599029,17.54,6.59,17.09,18.36,0.76
20260811,19.35,20.3,19.05,19.55,2236936,17.71,10.38,17.2,18.37,2.64
20260812,19.85,20.2,19.65,19.95,2046188,17.9,11.47,17.31,18.4,2.25
20260813,19.95,21.8,19.85,21.7,4151310,18.21,19.14,17.52,18.45,3.83
20260814,21.7,22.6,20.95,22.1,3290187,18.54,19.21,17.8,18.5,2.74
20260817,22.4,23.35,22.2,22.9,3090934,18.9,21.15,18.12,18.56,2.35
20260818,23.1,24,23,23.6,3495620,19.29,22.32,18.47,18.63,2.41
20260819,23.75,25.8,23.35,24.75,5933400,19.75,25.33,18.88,18.71,3.47
20260820,25.25,26.6,24.15,26,9855505,20.27,28.27,19.34,18.82,4.55
20260821,26.55,26.55,24.8,25.95,6326680,20.74,25.11,19.8,18.93,2.57
20260824,24.7,24.7,23.4,23.4,3904718,20.96,11.62,20.12,18.98,1.49
20260825,22.45,23.6,21.9,22.85,5723486,21.12,8.19,20.44,19.03,2
20260826,22.85,23.3,22.45,22.75,3947429,21.26,7.02,20.76,19.07,1.31
20260827,23.85,24.6,23.1,23.8,4277452,21.47,10.86,21.14,19.15,1.35
20260828,24.3,26.15,24.1,25.7,11060642,21.82,17.77,21.59,19.25,3.01
20260831,26,26.15,23.7,23.85,6633776,21.99,8.46,21.94,19.32,1.67
20260901,24,24.45,23.6,23.9,2663045,22.15,7.9,22.29,19.39,0.65
20260902,23.55,24.6,23.5,23.9,2557023,22.3,7.2,22.61,19.47,0.61
20260903,24.25,24.25,23.05,23.05,2740157,22.36,3.09,22.86,19.54,0.64
20260904,23.25,23.5,22.7,22.95,1378795,22.41,2.42,23.07,19.62,0.32
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 56.09
- over_600_ratio: 54.26
- over_800_ratio: 51.17
- over_1000_ratio: 50.08
- over_400_change_1w: -0.19
- over_800_change_1w: 0.27
- over_1000_change_1w: 0.27
- tdcc_consecutive_up_weeks: 14
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,52.62,0.8,44.88,-0.19,43.02,0.37,3,False,True
20260626,52.56,-0.06,44.27,-0.61,42.43,-0.59,4,False,False
20260703,52.14,-0.42,44.19,-0.08,42.46,0.03,5,False,True
20260709,52.52,0.38,44.67,0.48,41.71,-0.75,6,False,True
20260717,52.64,0.12,44.07,-0.6,42.2,0.49,7,False,True
20260724,52.46,-0.18,46.38,2.31,44.46,2.26,8,False,True
20260731,53.01,0.55,46,-0.38,44.12,-0.34,9,False,False
20260807,52.89,-0.12,45.9,-0.1,43.42,-0.7,10,False,False
20260814,54.38,1.49,48.01,2.11,45.54,2.12,11,True,True
20260821,55.89,1.51,50.26,2.25,48.57,3.03,12,True,True
20260828,56.28,0.39,50.9,0.64,49.81,1.24,13,True,True
20260904,56.09,-0.19,51.17,0.27,50.08,0.27,14,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6108 | 競國 | pattern | 型態觀察 | 43.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.主管機關核准減資日期:115/07/31 2.辦理資本變更登記完成日期:115/08/31 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）:            實收資本額(元)     流通在外股數(股)         每股淨值(元)(註)           --------------     ---------------------    -----------------   減資前:  1,544,943,110          154,494,311                20.99   減資後:  1,081,460,180          108,146,018                29.99   註:每股淨值係以115年第2季經會計師核閱之財務報表為設算依據。 4.預計換股作業計畫: 請參考115年8月7日發布之重大訊息，如有調整或日程變動，將另行公告。 5.預計減資新股上市後之上市普通股股數:108,146,018股 6.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 7.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，請說明股權流通性偏低   之因應措施:不適用 8.其他應敘明事項:本公司減資變更登記業經經濟部商業發展署115年08月31日經授商字  第11530138570號函核准在案。；calendar event: ex_dividend on 20261007; status=confirmed; proximity=within_60d |
| 20260904 | 6108 | 競國 | revenue_pullback | 營收成長股價回檔 | 83.0 |  |  |  |  |  | stale_signal | 1.主管機關核准減資日期:115/07/31 2.辦理資本變更登記完成日期:115/08/31 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）:            實收資本額(元)     流通在外股數(股)         每股淨值(元)(註)           --------------     ---------------------    -----------------   減資前:  1,544,943,110          154,494,311                20.99   減資後:  1,081,460,180          108,146,018                29.99   註:每股淨值係以115年第2季經會計師核閱之財務報表為設算依據。 4.預計換股作業計畫: 請參考115年8月7日發布之重大訊息，如有調整或日程變動，將另行公告。 5.預計減資新股上市後之上市普通股股數:108,146,018股 6.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 7.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，請說明股權流通性偏低   之因應措施:不適用 8.其他應敘明事項:本公司減資變更登記業經經濟部商業發展署115年08月31日經授商字  第11530138570號函核准在案。；calendar event: ex_dividend on 20261007; status=confirmed; proximity=within_60d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 6108 | 競國 | revenue_breakout_low_response | 營收爆發低反應股 | 19 | 13 | A_優先追蹤 |  |  |  | stale_signal | 1.主管機關核准減資日期:115/07/31 2.辦理資本變更登記完成日期:115/08/31 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）:            實收資本額(元)     流通在外股數(股)         每股淨值(元)(註)           --------------     ---------------------    -----------------   減資前:  1,544,943,110          154,494,311                20.99   減資後:  1,081,460,180          108,146,018                29.99   註:每股淨值係以115年第2季經會計師核閱之財務報表為設算依據。 4.預計換股作業計畫: 請參考115年8月7日發布之重大訊息，如有調整或日程變動，將另行公告。 5.預計減資新股上市後之上市普通股股數:108,146,018股 6.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:100% 7.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，請說明股權流通性偏低   之因應措施:不適用 8.其他應敘明事項:本公司減資變更登記業經經濟部商業發展署115年08月31日經授商字  第11530138570號函核准在案。；calendar event: ex_dividend on 20261007; status=confirmed; proximity=within_60d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6108 | 競國 | 2 | 2 | 3 | 6 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
